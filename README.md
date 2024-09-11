# HaikuTransformer

Built using just the decoder part of the model described in <a href="https://arxiv.org/abs/1706.03762">Attention is All You Need</a>. The model structure is shown below

![image](https://github.com/user-attachments/assets/d4200b1d-87e4-4bfb-95e3-40a37fdf13fc)

Goal: Make a text generator that can maintain some of the structure in the dataset and formulate real words.

The dataset used was statworx/haiku from huggingface. The dataset consists of mostly haikus in the 5-7-5 syllable structure, but there are some unstructured 3 line poems in the mix.

The results of the generator are found in testContexts.ipynb and the model is found in BigramLanguageModelTrain.py.

