# HaikuTransformer

Built using just the decoder part of the model described in <a href="[url](https://github.com/user-attachments/assets/9256297e-a7bb-4d17-b543-31b876a5a1e0)">Attention is All You Need</a>
. The model structure is shown below

![image]()

Goal: Make a text generator that can maintain some of the structure in the dataset and formulate real words.

The dataset used was statworx/haiku from huggingface. The dataset consists of mostly haikus in the 5-7-5 syllable structure, but there are some unstructured 3 line poems in the mix.

The results of the generator are found in testContexts.ipynb and the model is found in BigramLanguageModelTrain.py.

