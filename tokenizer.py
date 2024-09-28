import regex as re

def get_stats(tokensList):
    counts = {}
    for pair in zip(tokensList, tokensList[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

def merge(ids, pair, idx):
  # in the list of ints (ids), replace all consecutive occurences of pair with the new token idx
  newids = []
  i = 0
  while i < len(ids):
    # if we are not at the very last position AND the pair matches, replace it
    if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
      newids.append(idx)
      i += 2 # skip this pair now as we are mergining them
    else:
      newids.append(ids[i])
      i += 1
  return newids



###################################################################################################
###################################################################################################



class RegExpTokenizer():
    # Using Regular expression to split words in the same pattern as GPT 4
    # Ex: Haven't -> "Haven", "'t" 
    def __init__(self):
            super().__init__()

    def encode(self, text, vocab_size, verbose = False):
        assert vocab_size >= 256
        gpt4pat = re.compile(r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""
        ) #all seperators like suffixes on contractions or punctuations, empty spaces etc.
        text_chunks = re.findall(gpt4pat, text)
        # input text preprocessing
        ids = []
        for chunk in text_chunks:
            chunk_bytes = chunk.encode("utf-8") # raw bytes
            ids.extend(chunk_bytes)
        # iteratively merge the most common pairs to create new tokens
        merges = {} # (int, int) -> int
        vocab = {idx: bytes([idx]) for idx in range(256)} # idx -> bytes
        num_merges = vocab_size - 256
        tokens = ids
        for i in range(num_merges):
            stats = get_stats(tokens) #find common pairings
            pair = max(stats, key=stats.get)
            idx = 256 + i
            if verbose:
                print(f"merging {pair} into a new token {idx}")
            tokens = merge(tokens, pair, idx) # merge common pairs into new token >256
            # save the merge
            merges[pair] = idx
            vocab[idx] = vocab[pair[0]] + vocab[pair[1]]
        # save class variables
        self.merges = merges # used in encode()
        self.vocab = vocab   # used in decode()
        
        if verbose:
            #Compression Ratio
            print("tokens length:", len(tokens))
            print("ids length:", len(ids))
            print(f"compression ratio: {len(ids) / len(tokens):.2f}X")
        
        return tokens

    def decode(self, tokens):
        part_bytes = []
        for idx in tokens:
            if idx in self.vocab:
                part_bytes.append(self.vocab[idx])
            elif idx in self.inverse_special_tokens:
                part_bytes.append(self.inverse_special_tokens[idx].encode("utf-8"))
            else:
                raise ValueError(f"invalid token id: {idx}")
        text_bytes = b"".join(part_bytes)
        text = text_bytes.decode("utf-8", errors="replace")
        return text

        




