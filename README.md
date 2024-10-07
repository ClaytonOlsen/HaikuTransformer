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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horizontal Paragraph Boxes</title>
    <style>
        .container {
            display: flex;
            justify-content: space-between;
        }

        .box {
            border: 1px solid black;
            padding: 20px;
            margin: 10px;
            width: 30%; /* Adjust width so 3 boxes fit */
            box-sizing: border-box; /* Ensures padding is included in width */
            text-align: left; /* Align text to the left */
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">
            <h2>Title 1</h2>
            <p>This is the first paragraph of content in the box. You can have longer text, and it will wrap automatically within this box.</p>
        </div>
        <div class="box">
            <h2>Title 2</h2>
            <p>This is the second paragraph of content in another box. It will also wrap inside its own box with space between the other boxes.</p>
        </div>
        <div class="box">
            <h2>Title 3</h2>
            <p>This is the third paragraph of content. All three boxes should now be aligned horizontally with equal spacing and proper alignment.</p>
        </div>
    </div>
</body>












-------------------------------
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Side by Side Text Boxes</title>
    <style>
        .container {
            display: flex;
            justify-content: space-between;
        }

        .box {
            border: 1px solid black;
            padding: 20px;
            margin: 10px;
            width: 30%;
            text-align: center;
        }

        h2 {
            margin-top: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="box">
            <h2>Title 1</h2>
            <p>Is so setting faith? / U'll always happy I'll pron. / You and eat on daw.'\nWill surprised?\nSnowfall. / The sclimber of wine. / Only spectaculates.\nBlinding. / The dunes sheds. / Calhed roses.\nOne last gum. / The begin speaks. / Darkness.\nA long on threads. / One book only mango. / The dog.\nHalf pilleting. / Of thoughts leave. / Sinsing the quilt.\n[Eliter] / Feeling my elophone home. / Wilding persons.\nPale thunder. / The pie. / Of wet patching.\nSoft chargazes. / The twilight catch comes kiss. / Half, the sunfire shine.\nOutdoor real. / Understanding. / The Ass pints of.\nWaiting forgettrail. / I rar into their scent. / A retiremember.\nRemember Sharp notes. / Returned the ocean. / A rising down.\nJust be overcast. / Another glare separated. / Guard\'s shadow.\nAt the tea. / Of the ragged hospital day. / Open at the back off.\nHeadstove. / The flame of my trip. / Opens in the echos.\nMoon shadow. / The swishing pens. / Of all space.\nEvening day. / A bottle dreaming on. / Won\'t letter down?\nWhiteTre. / Swrinking tide. / In the sunset.\nCrowd war dish. / On a snaple prayer. / Twisters.\nCoffee mantisming shop. / The way goodwill roundness. / I didn\'t look.\nFirst day. / The softed blowing trouble. / The river heads.\nThe meterafish. / In the passage. / Two thick reminder.\nDeep in the hunt. / The ech other granted town. / Of word.\nEmotion Tree. / I don\'t kis. / Who wores it peppers.</p>
        </div>
        <div class="box">
            <h2>Title 2</h2>
            <p>This is the content of the second box.</p>
        </div>
        <div class="box">
            <h2>Title 3</h2>
            <p>This is the content of the third box.</p>
        </div>
    </div>
</body>
</html>











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
            <p>
</p>
        </div>
        <div class="box">
            <h3>Regex Tokenizer with 1000 character</h3>
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
            <h3>Regex Tokenizer with 5000 character</h3>
            <p>This is the content of the third box. You can add more text here.</p>
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

