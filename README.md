# HaikuLLMTransformer

Built using just the decoder part of the model described in <a href="https://arxiv.org/abs/1706.03762">Attention is All You Need</a>. The model structure is shown below

![image](https://github.com/user-attachments/assets/24e63a8f-966e-40fe-b6ed-fd8bdfc4dbae)

Goal: Make a text generator that can maintain some of the structure in the dataset and formulate real words.

The dataset used was statworx/haiku from huggingface. The dataset consists of mostly haikus in the 5-7-5 syllable structure, but there are many unstructured 3 line poems in the mix, so the aim of the generator will be mostly to produce legable 3 line poems, separated by "/" between the lines and "\n" or a new line for new poems.

<hr style="border: none; border-top: 2px solid black; width: 100%;">

pytorch version 2.1.2

<hr style="border: none; border-top: 2px solid black; width: 100%;">

The first run through was using a very simple tokenization strategy, simply translating the different characters from the dataset into number. These files are specified with the suffix SimpleEncode. I have additionally tested using a Regex tokenizer for splitting words using apostrophes, hyphens, etc. and created combined tokens for common patters. Below I kept track of the differences.

<hr style="border: none; border-top: 2px solid black; width: 100%;">


## Text Output

</head>
<body>
    <div class="container">
        <div class="box">
            <h3>Simple Tokenizer</h2>
            <p>Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.'<br>
                Will surprised?\nSnowfall. / The sclimber of wine. / Only spectaculates.<br>
                Blinding. / The dunes sheds. / Calhed roses.<br>
                One last gum. / The begin speaks. / Darkness.<br>
                A long on threads. / One book only mango. / The dog.<br>
                Half pilleting. / Of thoughts leave. / Sinsing the quilt.<br>
                [Eliter] / Feeling my elophone home. / Wilding persons.<br>
                Pale thunder. / The pie. / Of wet patching.<br>
                Soft chargazes. / The twilight catch comes kiss. / Half, the sunfire shine.<br>
                Remember Sharp notes. / Returned the ocean. / A rising down.<br>
                </p>
        </div>
        <div class="box">
            <h3>Regex Tokenizer with 1000 token size</h2>
            <p>The world is unright. / Haiku therapy. / Taste of anama.<br>
                Mirror, envy dewgs. / Where ait spells lied?<br>
                My dog kayoffs to. / Those who am I still alive. / An accidental legs.<br>
                Near of refuseddit. / The water dust. / The lingering sun.<br>
                Rivering heat. / My air turns clapped. / On the cashiernewbe.<br>
                A dark chains collect. / On Christmas standard. / Hurry.<br>
                Bult of Aard. / Drimy hand on my face.<br>
                Sweet wintery. / Evide. / My heart boxes, catches a mxsport.<br>
                Another stood. / In Towiti if noticer. / Looks wrapped at work.<br>
                The words are shower. / Early flated the sky. / All that will lack of life.</p>
        </div>
        <div class="box">
            <h3>Regex Tokenizer with 3000 token size</h2>
            <p>Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.<br>
                Getting the one, Yuk. / Everything I'm short is. / Everything good to.<br>
                No wig awful, R. / So much I remember. / If you pout to ship.<br>
                Memes about my heart. / Bad is even no gas? / Do nothing somebody.<br>
                Sunday shiny drop. / Parting hards of the wisel? / Even the boys like.<br>
                Shit was the pierced. / Off, Luck ugly, I remind. / It is enjoy your door.<br>
                Beautiful rearing. / Stop never ending running. / Blockstors, from itself.<br>
                A child's time hours. / The snowfall ripping heavy up. / And fillend messions.<br>
                Oh, babe, I'm home. / Here foreading why you're Not? / The folded, let's busy.<br>
                Then I wope I looking. / Today and got to win this. / Til I'll really wish.<br>
            </p>
        </div>
    </div>
</body>

## Syllable Counts

Simple Encoding Tokenizer             | Regex Tokenizer with 1000 Length             |  Regex Tokenizer with 3000 Length
:-------------------------:|:-------------------------:|:-------------------------:
<img src="Images/SimpleEncodeSyllables.png" width="325" />  | <img src="Images/Regex1000TokenSyllables.png" width="325" />  |  <img src="Images/Regex3000TokenSyllables.png" width="325" />









