"""
From Attention is All you Need model structure. Decoder only model that aims to generate text:

"""



import torch
import torch.nn as nn
from torch.nn import functional as F
torch.manual_seed(1337)



class Head(nn.Module):
    """ one head of self-attention """

    def __init__(self, head_size, block_size, n_embd, dropout):
        super().__init__()
        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)
        self.register_buffer('tril', torch.tril(torch.ones(block_size, block_size)))
        self.dropout = nn.Dropout(dropout)

    def forward(self, x):
        B,T,C = x.shape
        #B = Batch, T = Time(block size/lookback window), C = channel(vocab size)
        k = self.key(x)   # (B,T,C)
        q = self.query(x) # (B,T,C)
        # compute attention scores ("affinities")
        wei = q @ k.transpose(-2,-1) * C**-0.5 # (B, T, C) @ (B, C, T) -> (B, T, T) Normalized with scaled attention
        wei = wei.masked_fill(self.tril[:T, :T] == 0, float('-inf')) # (B, T, T)
        wei = F.softmax(wei, dim=-1) # (B, T, T)
        wei = self.dropout(wei)
        # perform the weighted aggregation of the values
        v = self.value(x) # (B,T,C)
        out = wei @ v # (B, T, T) @ (B, T, C) -> (B, T, C)
        return out
    
class MultiHeadAttention(nn.Module):
    def __init__(self, num_heads, head_size, block_size, n_embd, dropout):
        super().__init__()
        self.heads = nn.ModuleList([Head(head_size, block_size, n_embd, dropout) for _ in range(num_heads)])
        self.proj = nn.Linear(n_embd, n_embd)# projecting out of residual path to be added at end
        self.dropout = nn.Dropout(dropout)
    
    def forward(self,x):
        out = torch.cat([h(x) for h in self.heads], dim=-1) # concatenate heads
        out = self.dropout(self.proj(out))
        return out # project back into original pathway
    

class FeedForward(nn.Module):
    """Linear layer -> Relu -> Linear -> Dropout from paper"""

    def __init__(self, n_embd, dropout):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4* n_embd), #in paper the middle layers are 4x the outer layers
            nn.ReLU(),
            nn.Linear(4* n_embd, n_embd),# added for projection layer back into length of n_embed
            nn.Dropout(dropout),
        )
    def forward(self, x):
        return self.net(x)
    
class Block(nn.Module):

    def __init__(self, n_embd, n_head, block_size, dropout):
        super().__init__()
        head_size = n_embd // n_head
        self.sa = MultiHeadAttention(n_head, head_size, block_size, n_embd, dropout)
        self.ffwd = FeedForward(n_embd, dropout)
        self.ln1 = nn.LayerNorm(n_embd)
        self.ln2 = nn.LayerNorm(n_embd)

    def forward(self,x):
        x = x + self.sa(self.ln1(x))
        x = x + self.ffwd(self.ln2(x))
        return x




class BigramLanguageModel(nn.Module):

    def __init__(self, block_size, vocab_size, n_embd, n_head, dropout, device):
        super().__init__()
        self.device = device
        self.block_size = block_size
        # each token directly reads off the logits for the next token from a lookup table
        self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
        self.position_embedding_table = nn.Embedding(block_size, n_embd)
        #Adding in blocks aka the layers of the NN
        self.blocks = nn.Sequential(
            Block(n_embd, n_head, block_size, dropout),
            Block(n_embd, n_head, block_size, dropout),
            Block(n_embd, n_head, block_size, dropout),
            nn.LayerNorm(n_embd),
        )
        self.lm_head = nn.Linear(n_embd, vocab_size) #Turn into words at the end (embedded words that will be decoded)
        

    def forward(self, idx, targets=None):
        B, T = idx.shape
        tok_emb = self.token_embedding_table(idx) # (B,T,C)
        pos_emb = self.position_embedding_table(torch.arange(T, device=self.device)) # T,C
        x  = tok_emb + pos_emb
        x = self.blocks(x)
        logits = self.lm_head(x) # (B,T,C) The Decoder to create the logits
        if targets is None:
            loss = None
        else:
            B, T, C = logits.shape
            logits = logits.view(B*T, C)
            targets = targets.view(B*T)
            loss = F.cross_entropy(logits, targets)

        return logits, loss

    def generate(self, idx, max_new_tokens):
        # idx is (B, T) array of indices in the current context
        for _ in range(max_new_tokens):
            # crop the idx to stay below the block size
            idx_cond = idx[:, -self.block_size:]
            # get the predictions
            logits, loss = self(idx_cond)
            # focus only on the last time step (Bigram model)
            logits = logits[:, -1, :]
            # apply softmax to get probabilities
            probs = F.softmax(logits, dim=-1) # (B, C)
            # sample from the distribution
            idx_next = torch.multinomial(probs, num_samples=1) # (B, 1)
            # append sampled index to the running sequence
            idx = torch.cat((idx, idx_next), dim=1) # (B, T+1)
        return idx
    

class utilTools:
    def __init__(self, train_data, val_data, block_size, batch_size, device):
        self.train_data = train_data
        self.val_data = val_data
        self.block_size = block_size
        self.batch_size = batch_size
        self.device = device
    # data loading
    def get_batch(self, split):
        # generate a small batch of data of inputs x and targets y
        data = self.train_data if split == 'train' else self.val_data
        ix = torch.randint(len(data) - self.block_size, (self.batch_size,))
        x = torch.stack([data[i:i+self.block_size] for i in ix])
        y = torch.stack([data[i+1:i+self.block_size+1] for i in ix])
        x, y = x.to(self.device), y.to(self.device)
        return x, y

    @torch.no_grad()
    def estimate_loss(self, model, eval_iters):
        out = {}
        model.eval()
        for split in ['train', 'val']:
            losses = torch.zeros(eval_iters)
            for k in range(eval_iters):
                X, Y = self.get_batch(split)
                logits, loss = model(X, Y)
                losses[k] = loss.to(self.device).item()
            out[split] = losses.mean()
        model.train()
        return out
    

