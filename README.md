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
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Three Boxes Next to Each Other</title>
    <style>
        /* Styling the container to display boxes side by side */
        .container {
            display: flex;
            justify-content: space-around; /* Spacing between boxes */
            padding: 20px;
        }

        /* Styling for each box */
        .box {
            background-color: #f0f0f0;
            padding: 20px;
            width: 30%;
            text-align: center;
            border: 1px solid #ccc;
            border-radius: 10px;
        }

        /* Styling for each title */
        .box h3 {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

    <div class="container">
        <div class="box">
            <h3>Simple Encoding for Tokenizer</h3>
            <p>Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.
'\nWill surprised?\nSnowfall. / The sclimber of wine. / Only spectaculates.\nBlinding. / The dunes sheds. / Calhed roses.\nOne last gum. / The begin speaks. / Darkness.\nA long on threads. / One book only mango. / The dog.\nHalf pilleting. / Of thoughts leave. / Sinsing the quilt.\n[Eliter] / Feeling my elophone home. / Wilding persons.\nPale thunder. / The pie. / Of wet patching.\nSoft chargazes. / The twilight catch comes kiss. / Half, the sunfire shine.\nOutdoor real. / Understanding. / The Ass pints of.\nWaiting forgettrail. / I rar into their scent. / A retiremember.\nRemember Sharp notes. / Returned the ocean. / A rising down.\nJust be overcast. / Another glare separated. / Guard\'s shadow.\nAt the tea. / Of the ragged hospital day. / Open at the back off.\nHeadstove. / The flame of my trip. / Opens in the echos.\nMoon shadow. / The swishing pens. / Of all space.\nEvening day. / A bottle dreaming on. / Won\'t letter down?\nWhiteTre. / Swrinking tide. / In the sunset.\nCrowd war dish. / On a snaple prayer. / Twisters.\nCoffee mantisming shop. / The way goodwill roundness. / I didn\'t look.\nFirst day. / The softed blowing trouble. / The river heads.\nThe meterafish. / In the passage. / Two thick reminder.\nDeep in the hunt. / The ech other granted town. / Of word.\nEmotion Tree. / I don\'t kis. / Who wores it peppers.
</p>
        </div>
        <div class="box">
            <h3>Regex Tokenizer with 1000 character  85% words</h3>
            <p>Macross America. / Has a party. / Sandits, Earrengthe.\nToo many seeing stuff. / They flopped for the second trip. / Others singlute.\nBare borne. / Caloup, pop and so flowers and. / His pains where will find it with all me.\nHer eyes are online. / Swing ash eye, fake, fire. / Bey, my sure does it. / Respect for you.\nWant to feel among? / Commit, just like made it.\nYou gotta cry. / Leave me like your fan fight enough from. / I trusted me like I miss able. / I'm saying received.\nGot a long showing me. / Signs of love life. / So much music is bying.\nOK, don't care, yeah, God? / If only I could tim.\nTurnal me while me. / Murdered the awesome, I. / Weard your time guys.\nI'm about to stay. / My I'm spending hate. / More than and I'm not.\nThe worst till Jin. / Me without a place, but you is. / Mitch on Tuesday, my. / Show me you bowel.\nI fucking krake try. / You thank you, someone, I'm. / So exhausted by tonight.\nJoe's making A. / Shopping all night faking. / I should be writing. / Like a heart Christget? / During sex, stress.\nI can for fools back, u. / Eat healed. / The lawn present.\nIt's crazy guidance. / In verse of class, lol.\nI swear my joke, kid's body. / Also, when it's. / Time to take a shit.\nHey, you think absolute he's. / Dang to see Obama.\nI don't er. / Thankful, oshat I miss A. / Burber, Tinube and my brain. / Brighter.\nSleeping next to tell me. / Is came out of heavy. / Bringming without Cedar fuck.\nI don't remember. / Arfired, e dropping.\nI'll always act. / Is beat the best. / Sleep is excarantu, rather shit me. / That would I knew this thing to. / Give t wish tonight and. / I'm so lonely.\nMy face is wonderful day. / And knows I'm pretty much. / This for Christmas.\nBeing bitches are wrong for the. / Best feelings, so damn."</p>
        </div>
        <div class="box">
            <h3>Regex Tokenizer with 3000 character 86% words</h3>
            <p>"I love her feet, yeat wave.\nMacross America. / Has a party. / Sandits, Earrengthe.\nToo many seeing stuff. / They flopped for the second trip. / Others singlute.\nBare borne. / Caloup, pop and so flowers and. / His pains where will find it with all me.\nHer eyes are online. / Swing ash eye, fake, fire. / Bey, my sure does it. / Respect for you.\nWant to feel among? / Commit, just like made it.\nYou gotta cry. / Leave me like your fan fight enough from. / I trusted me like I miss able. / I'm saying received.\nGot a long showing me. / Signs of love life. / So much music is bying.\nOK, don't care, yeah, God? / If only I could tim.\nTurnal me while me. / Murdered the awesome, I. / Weard your time guys.\nI'm about to stay. / My I'm spending hate. / More than and I'm not.\nThe worst till Jin. / Me without a place, but you is. / Mitch on Tuesday, my. / Show me you bowel.\nI fucking krake try. / You thank you, someone, I'm. / So exhausted by tonight.\nJoe's making A. / Shopping all night faking. / I should be writing. / Like a heart Christget? / During sex, stress.\nI can for fools back, u. / Eat healed. / The lawn present.\nIt's crazy guidance. / In verse of class, lol.\nI swear my joke, kid's body. / Also, when it's. / Time to take a shit.\nHey, you think absolute he's. / Dang to see Obama.\nI don't er. / Thankful, oshat I miss A. / Burber, Tinube and my brain. / Brighter.\nSleeping next to tell me. / Is came out of heavy. / Bringming without Cedar fuck.\nI don't remember. / Arfired, e dropping.\nI'll always act. / Is beat the best. / Sleep is excarantu, rather shit me. / That would I knew this thing to. / Give t wish tonight and. / I'm so lonely.\nMy face is wonderful day. / And knows I'm pretty much. / This for Christmas.\nBeing bitches are wrong for the. / Best feelings, so damn.\nLuice and all the bam. / About your revice. / From an open boil.\nI'm plore and Mark pants. / Now is therapy failried. / Makes me feel my dad bitch.\nSorry for food. / Playing again, since. / I can prote a little trump. / Can't take it it.\nSurprise swer on account. / To make you fixes.\nEven if you don't know. / How people acick? / Call okay, in my ham? / If someone can die."
</p>
        </div>
    </div>

</body>







Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.
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
From til town, record. / The reacher a dollrine hawk. / The Liflip of rain.

