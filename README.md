# HaikuTransformer

Built using just the decoder part of the model described in <a href="https://arxiv.org/abs/1706.03762">Attention is All You Need</a>. The model structure is shown below

![image](https://github.com/user-attachments/assets/dd3e592c-b6a8-4c65-8846-ca3cb835c461)


Goal: Make a text generator that can maintain some of the structure in the dataset and formulate real words.

The dataset used was statworx/haiku from huggingface. The dataset consists of mostly haikus in the 5-7-5 syllable structure, but there are some unstructured 3 line poems in the mix.

The results of the generator are found in testContexts.ipynb and the model is found in BigramLanguageModelTrain.py.

