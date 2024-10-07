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


### Text Output

</head>
<body>
    <div class="container">
        <div class="box">
            <h2>Title 1</h2>
            <p>Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.'\nWill surprised?\nSnowfall. / The sclimber of wine. / Only spectaculates.\nBlinding. / The dunes sheds. / Calhed roses.\nOne last gum. / The begin speaks. / Darkness.\nA long on threads. / One book only mango. / The dog.\nHalf pilleting. / Of thoughts leave. / Sinsing the quilt.\n[Eliter] / Feeling my elophone home. / Wilding persons.\nPale thunder. / The pie. / Of wet patching.\nSoft chargazes. / The twilight catch comes kiss. / Half, the sunfire shine.\nOutdoor real. / Understanding. / The Ass pints of.\nWaiting forgettrail. / I rar into their scent. / A retiremember.\nRemember Sharp notes. / Returned the ocean. / A rising down.\nJust be overcast. / Another glare separated. / Guard\'s shadow.\nAt the tea. / Of the ragged hospital day. / Open at the back off.\nHeadstove. / The flame of my trip. / Opens in the echos.\nMoon shadow. / The swishing pens. / Of all space.\nEvening day. / A bottle dreaming on. / Won\'t letter down?\nWhiteTre. / Swrinking tide. / In the sunset.\nCrowd war dish. / On a snaple prayer. / Twisters.\nCoffee mantisming shop. / The way goodwill roundness. / I didn\'t look.\nFirst day. / The softed blowing trouble. / The river heads.\nThe meterafish. / In the passage. / Two thick reminder.\nDeep in the hunt. / The ech other granted town. / Of word.\nEmotion Tree. / I don\'t kis. / Who wores it peppers.</p>
        </div>
        <div class="box">
            <h2>Title 2</h2>
            <p>The world is unright. / Haiku therapy. / Taste of anama.
Mirror, envy dewgs. / Where ait spells lied?
My dog kayoffs to. / Those who am I still alive. / An accidental legs.
Near of refuseddit. / The water dust. / The lingering sun.
Rivering heat. / My air turns clapped. / On the cashiernewbe.
A dark chains collect. / On Christmas standard. / Hurry.
Bult of Aard. / Drimy hand on my face.
Sweet wintery. / Evide. / My heart boxes, catches a mxsport.
Another stood. / In Towiti if noticer. / Looks wrapped at work.
The words are shower. / Early flated the sky. / All that will lack of life.</p>
        </div>
        <div class="box">
            <h2>Title 3</h2>
            <p>Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.
Getting the one, Yuk. / Everything I'm short is. / Everything good to.
No wig awful, R. / So much I remember. / If you pout to ship.
Memes about my heart. / Bad is even no gas? / Do nothing somebody.
Sunday shiny drop. / Parting hards of the wisel? / Even the boys like.
Shit was the pierced. / Off, Luck ugly, I remind. / It is enjoy your door.
Beautiful rearing. / Stop never ending running. / Blockstors, from itself.
A child's time hours. / The snowfall ripping heavy up. / And fillend messions.
Oh, babe, I'm home. / Here foreading why you're Not? / The folded, let's busy.
Then I wope I looking. / Today and got to win this. / Til I'll really wish.
When Wentten Tausts? / Violens when I just remember. / And selent girls out.
Even wow long you. / Has a handweore climi, right? / Through, eat employes.
Forhing him fup when. / You it in pints mround on. / Your friends are just down.
I dunno thank you. / Life or world, drive me, I'm t. / Get surprised and spei.
Just love my haircut. / Comes up by my death nine's a. / Friend jeans appears shore.
The shit stabbles short. / Wildrupts the come to hideague. / As caught, purpose.
Thus to postpain up. / Half by h mid motel right. / I was finally.
From til town, record. / The reacher a dollrine hawk. / The Liflip of rain.</p>
        </div>
    </div>
</body>






