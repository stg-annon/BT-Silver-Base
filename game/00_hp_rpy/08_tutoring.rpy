label tutoring:

    $ tut_happened = True # Turns TRUE after you click the tutoring button and see th message that tutoring is not a part of this game. Make sure the tutoring button will not be visible after that.
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    
    her "Of course, sir."
    her "I'll go get my books then."
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    

    $ only_upper = True
    $ badges = False
    $ ne = False # Desplays a fishnets in hermione_main screen.


    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_199.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    
    
    hide screen blkfade
    with d3
    
    show screen ctc
    pause
    hide screen ctc
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    
    her "Again, thank you for doing this for me, sir..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_199.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "..........."
#########################################################
###########JJ edits start  ##############################
#   hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_200.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "Sir?"
#    m "...................."
#    stop music fadeout 1.0
#    g4 "I can't do this."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "Huh?"
#    m "I can't tutor you, miss Granger..."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
#    her "B-but..."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_201.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "But, sir, you promised!"
#    m "No, you don't understand..."
#    m "I literally {size=+7}can not{/size} do that."
#    m "Akabur is a lazy faggot and cut this content..."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_202.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "???"
#    m "I know, I know."
#    m "Over $7,000 USD a month, and he can't finish a single fucking game?"
#    m "I sure hope you didn't donate to him, otherwise you'd have been ripped off."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_203.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "Is he really that much of a jew?"
#    m "Unfortunately, yes. And people just don't understand."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_204.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "Why not?"
#    m "Because they're retarded. He could shit on a plate, take a picture, and ask for $500 and he'd get it."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_205.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    stop music
#    her "{size=+7}SERIOUSLY?!{/size}"
#    show screen blktone8
#    with d3
#    ">Hermione can't believe anyone would be that stupid."
#    hide screen blktone8
#    with d3
#    m "*Sigh* It's an unfortunate truth..."
#    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_206.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
#    her "Sir, I think I'll be leaving now..."
#    show screen blkfade
#    hide screen hermione_main
#    with d3
#    m "Well, alright then. I can't blame you after hearing all of that."
#########################################################
###########JJ additions   12/28/2014 ####################  
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_203.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Sir?"
    m "Ah, yes, Miss Granger.  Well, let\’s start with what you need help with."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_201.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I don't really know.  I can read my books to find answers and write parchments."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_204.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I hoped you could teach me something that would give me an advantage with practical magic so I didn't have to practice that so much."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_202.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "(Practical magic?  I can't do what she does with wands and words!  What the hell am I going to teach her?  Think fast, Genie!)"
    m "Ah, well, um..."
    her "Professor?"
    m "Ummm...Well, you see, practical magic...isn't always that practical.  You must learn to use magic {i}differently{/i} if you want to progress."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Use magic differently?  I've been doing things the same way as long as I've been at Hogwarts!"
    her "I'm doing it exactly the way I was taught!  The way the teachers do it!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_206.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    her "And I'm the best at nearly every kind of magic among all of the students!  And better than some of the teachers as well!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_202.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    m "Yet as you say, you are now beginning to have difficulty with some of your classes.  The teachers are saying that your work isn't up to par?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_198.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3
    her "Y-yes.  In some of them.  Professor Snape particularly, but some are saying..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_202.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    m "I know.  The teachers have all come to me concerned about your...stagnation.  You should be progressing much faster in your ability than you are."
    m "Some have said they are concerned you may not be able to pass the next tier of tests satisfactorily."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_205.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    her "The N.E.W.T.s?  But...but I must pass them!  No one has said I might fail!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_202.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3 
    m "You said you were failing tests already.  If you cannot pass simple course work I don't know how you will pass a newt..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_204.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3 
    her "Professor, this is terrible!  I've done so well before!  I can't fail now!  What is the problem?  I have to fix whatever it is!"
    m "Hmm.  I have a suspicion as to why you are having difficulties.  I think a small demonstration is in order..."
    m "Let's put the books away for now and ready your wand."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_203.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3 
    her "Yes, sir."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_15_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    
    m "Good.  Now, let me see you cast a spell.  Why don’t you do something simple, like, say, produce a flower here on my desk."
    her "All right sir."
    her ">Hermione waves her wand"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Flos productum!"
    show screen H_Flowers_in
    her ">A small flower appears on the desk."
    $ hermione_body = "01_hp/13_hermione_main/body_15_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "That was fine wand work, Miss Granger.  Now, please make it vanish."
    her ">Hermione waves her wand again. "
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Evanesco!" 
    hide screen H_Flowers_in
    show screen H_Flowers_out
    hide screen H_Flowers_out
    with d3
    her "> The flower vanishes"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_15_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "Now, let me see you try it without the wand."                                                                                                                                                                                                              #HERMIONE
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_08_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Without the wand, sir?"
    m "Yes, yes.  Put your wand away and produce a flower again.  No gestures, either.  And no magic words."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_16_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "But...but it won’t work, Professor.  Magic doesn’t work that way, sir.  You know that!"
    m "Ah, but I do not know that, Miss Granger.  Watch!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_15_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "<Now for a bit of razzle-dazzle.  And maybe a little bonus just for me...>"
    m ">Genie arches an eyebrow and a bouquet of flowers appears on his desk."
    show screen G_Flowers_in
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/HermioneDancerTransform.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "That’s amazing, sir!  You did magic without a wand or anything!  And not a simple spell, either!"
    m ">Genie nods again and the flowers vanish."
    hide screen G_Flowers_in
    show screen G_Flowers_out
    hide screen G_Flowers_out
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_130_wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "<I can't believe she didn't notice that!>"
    m "Indeed, Miss Granger.  You are a talented witch and you should be able to do the same as I do by now."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_15_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "Something troubles me that I noticed about you when you were using magic.  I have an idea why you cannot do the same.  May I see your wand?"
    her "My wand?  Of course. (Hermione hands the wand over to Genie)"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "Hmm.  Hmmm.  Very interesting.  Quite remarkable, I would say.  You do rather a lot of magic with the wand, I believe."
    $ hermione_body = "01_hp/13_hermione_main/body_13_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Well, yes, sir.  And all the time.  Every chance I get, really.  What is it, Professor?"
    m "Well, Miss Granger, it seems you have done yourself in somewhat.  Frankly I haven't seen anything like this in years."
    m "You see, I checked your aura and then checked your wand’s aura.  You have practically no magical aura left in you at all."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_12_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Auras?  Isn’t that just a bunch of Divination nonsense?"
    m "Oh, no, that’s not true at all.  Every living thing has a life aura.  Witches and wizards also have a magical aura.  Wands, however do not."  
    m "Or they should not, I should say.  Perhaps you should be paying more attention in Divination class."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_07_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I haven't taken any Divination classes in years!  Trelawney is such a fraud!"
    m "Who?"
    her "Sorry, sir.  {b}Professor{/b} Trelawney."
    m "But I see your problem.  When you use your wand to cast a spell, you are focusing the magical energy you have inside you through the wand.  "
    m "It may leave a trace behind, usually small.  A portion of your magical aura."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_11_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I see.  That must be why Priori Incantatem can reveal the last spell a wand was used to cast!"
    m "Whatever.  Focusing through the wand is a simple way to teach the basics of magic to beginners, but for some it becomes a crutch."
    m "And if they are not careful they may leave more and more of their magical essence in the wand itself as they attempt greater magic."
    m "Eventually they must use their wand for any magic they do because they have managed to drain much of their magical essence into the wand over time."
    m "Soon they themselves are little more than any non-magical person unless the have their wand.  You have invested nearly all of your magical ability into your wand!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_13_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Is that why I have so much trouble casting spells with someone else's wand?"
    m  "Very good, Miss Granger!  You have the right of it."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_10_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "But that means I might become a muggle or a squib one day?  If I don’t have my wand, I mean?"
    m "(what the hell is a squib?)  Perhaps.  And that would be a disaster for you if you were to have your wand damaged or lost through some calamity!"  
    m "But I think I can help you halt and possibly reverse the process.  It may be that you can get your magic back inside you and return you to normal.  "
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_22_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Oh, Professor, I will do anything to get my magic back where it belongs!  I can almost feel it, that I’m not as magical as I once was!"
    her "How do I restore it?"
    m "It will take some time to repair, I’m afraid.  It will come back to some degree eventually on its own."
    m "You would have to refrain from doing magic of any sort while you built back up again."
    m "You might get back to half your original level in as little as three or four years."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_130_wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Three....or four years!?!  Oh, I can’t wait that long, sir!  I have tests coming up and need to practice for them right away! " 
    her "And from what you say, with as little magic as I have in me now I don’t think I could pass any examination!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_22_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    m "Your school examinations do pose a problem.  But I once read of another way to retrieve a magic aura from a your wand that might be much faster.  "
    m "You will have to work hard at it though."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_07_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I am not afraid of hard work, sir!  I would do anything to get my abilities back! Just tell me what to do!"
    m "Fine, fine.  You see, your magic ability resides inside you."
    m "Much like your consciousness resides in your brain, your magic resides in what you may have heard of as your chakra.  "
    m "Specifically it is the Muladhara Chakra, the source of your body’s energy.  It is there you must channel the energy back to from your wand."
    m "<I can't believe wasting time reading all of those idiotic books paid off with some useful mumbo-jumbo!>"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_08_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Where is the mula-...mudla-...Oh, where is it located?  How do I channel the energy back to it so I can be restored?"
    m "It is near the coccyx at the base of your spine.  I have read that lost magical energy must come back in through one of the body’s natural portals."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_10_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Portals?  What are those?"
    m "Ah, well that should be obvious.  Any part of your body which is open to the outside world.  "
    m "Your mouth, for example, or your nostril or ear canals."
    m "You need only hold the wand at a portal and focus on bringing the magical energy back inside you.  "
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ hermione_body = "01_hp/13_hermione_main/body_10_Wand.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Professor, I know it's important and I need to do it but...do you think...this...transfer...will it hurt?"
    m "Quite the opposite, Miss Granger.  I think you will find the experience quite invigorating!"
    her "Ah, good.  Though I don’t think that I should put my wand in my ear.  That might be dangerous."
    m "I agree.  Why don’t we try it holding it at your mouth."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "(Hermione puts the wand to her mouth and clenches it between her teeth)"
    her_wLeft "Aike hizs?"
    m "Splendid, splendid.  Now, focus your concentration on pulling the magical energy into your body through your mouth.  "
    m "Think of it as breathing in the magic!  "
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her_wShut "(Hermione grimaces and grits her teeth)"
    m "Do you feel it? Do you feel a stirring at the base of your spine where the energy is flowing?"
    her_wMad "(Hermione makes a mad face and shakes her head)"
    m "Perhaps you are not trying hard enough.  Focus your will on the wand and bring the power into you!"
    her_wOneopen "(Hermione grits her teeth more and furrows her brow.)"
    her_wOneopen "Ih gnoch huerking!"
    m "I beg your pardon?"
    call her_head("(She takes the wand from her mouth.)","head_exp/25")
    call her_head("Professor, it’s just not working.  I don’t feel anything at all!")
    m "Please hand me your wand, Miss Granger.  I want to examine it again."
    her "(Hermione hands the wand over)"
    m "Alas, I see no change whatsoever in the wand’s aura.  There are now some teeth marks, I'm afraid."
    m "I believe you are right that you did not retrieve even an iota of magical energy from the wand."
    m "I’m sorry.  Perhaps we should see about transferring you to a muggle school near your parents' home..."
    her "But Professor!  There must be another way!  Perhaps I was not doing it correctly?!"
    m "Let me think for a moment……"
    m "……"
    m "Ah, by Merlin’s beard, why didn’t I think of this first!  The mouth is much too far from the chakra to be any use as a portal!  "
    m "The Muladhara Chakra is at the base of the spine!  You should use a portal much closer to it for the energy to be able to find its way back!"
    her "The…the base of the spine?  But that would be…"
    m "Oh.  Dear me.  I see.  I do indeed.  But if it is the only way... "
    her "Professor, I don’t want to put my wand…back there.  It would get dirty and how would I sit down and…"
    m "I suppose I should start the school transfer paperwork right away..."
    her "Oh, Professor Dumbledore!  I can't leave Hogwarts!  I love it here!  There has to be some other way..."
    m "Wait, wait!  I have the solution.  I am such a foolish old man!  I forgot you are a young woman!  "
    m "I was thinking only if it were myself trying to retrieve the energy!"
    m "But you have another portal in the near vicinity that should work nearly as well!"
    her "What?  Do you mean…"
    m "Yes, yes.  Of course.  How stupid of me to not suggest it from the start.  "
    m "Here, Miss Granger.  Take your wand handle and put it between your legs..."
    her "Be--between my legs?"
    m "Yes, yes.  That should work as well as the other.  The proximity is quite close."
    her "But, sir, that's not possible!  I never touch myself down there.  It's a dirty place.  I'm not like one of the Slytherin girls, you know."
    m "Miss Granger, I'm not asking you to do this for my gratification.  This is solely for your benefit.  If you don't wish to take my advice..."
    m "I'm sure those transfer forms are in this drawer here..."
    her "I...I suppose it is okay if I do it under a teacher's instruction.  I just want you to know that I'm a very good girl."
    her "I don't touch anything down there except to wash.  True Gryffindors never touch themselves in a bad way!"
    m "I was sure all girls touched themselves from time to time.  Just out of curiosity at least."
    her "Oh, no, Professor.  I have always kept away from any of that.  It's too distracting from my studies!  "
    her "Though I suspect that some of my roommates may do it sometimes, late at night."
    her "I've told them over and over how it is not good for them to do but they usually just tell me it's none of my business."
    m "As I said, it is up to you do decide whether to do as I recommend.  There are some fine  schools for young muggle ladies I hear..."
    her "I...I think I will do it.  I will at least try to bring myself to do it, at least.  I must have my magic back!"
    m "Splendid!  Well, you may begin any time you are ready."
    her "But, Professor… I can’t do that in front of you!  You are a man and that’s….that’s a private area."
    m "Well, I think it best to have me nearby to ensure nothing untoward happens.  Would you like for me to close my eyes so you won’t be embarrassed?  "
    her "I...I guess that would be all right.  For safety, you know."
    m "Very well."
    m "<I wonder if this spell that makes me look like Dumbledore will let me...>"
    # black screen
#    hide screen hermione_main    
    m "They are closed now.  You may begin."
    her "Thank you sir.  I'd be too embarrassed to have you watch this."
    m "<Wow! It worked!>"
    her "(Hermione blushes and puts the wand under her skirt)"
    hide screen hermione_blink
    show screen hermione_02_w
    her "All right, Professor.  Now what do I do?"
    m "Do you feel the energy coursing into you?"
    her "No sir.  I don’t feel anything but foolish."
    m "Ah, well, do not worry about that.  Perhaps it’s not in the right position.  Move it around a bit."
    her "You aren’t looking, are you?"
    m "No, no, Miss Granger.  This is a magical experiment.  My mind is focused only on getting you some relief from your problem."
    m "And as headmaster I never \"peek\"!"
    hide screen hermione_02_w
    show screen hermione_02_wSlow
    her "Well, I am moving it around some."
    m "Good, good.  Keep moving it.  You must awaken the magical energies within to free them more readily.  It may require vigorous agitation."
    her "I am doing it.  I am moving it."
    m "Do you feel anything? "
    her "Ah…yes.  Yes sir.  I’m...I think I there's something going on..."
    m "How does it feel?  That may be the energy beginning to seep back into you."
    her "Oh…oh, my.  Yes, it does feel good."
    m "Wonderful.  The affinity the magic has for your body should make the transit quite pleasant.  Now keep at it for a bit more."
    her "I am, Professor.  I…I really do feel something wonderful.  Would it be okay to move it faster?  I don’t want to cause a problem…"
    m "No, no.  Move it at whatever speed you think is optimizing the energy transfer you feel."
    hide screen hermione_02_wSlow
    $hermione_SC.chibi.ypos = 247
    show screen hermione_02_wFast
    her "........."
    her "Oh..."
    her "Oh...oh dear..."
    m "Are you all right Miss Granger?"
    her "Oh...oh, yes... yes...yesssss..."
    m "Good, good.  Continue what you are doing and you will be rewarded I’m sure."
    her "...Ah.....ah....oh.....mmmmmf....."
    her "Ah!..Ah!...Ahhhhh!"
    m "May I open my eyes now?"
    her "....Ah....AH......AAHHH.....Oh......wait....."
    her " ....Just a little more, I think.........."
    her " .............."
    her " AH!  AH! OH!  AH!  AHHhhhhhh!"
    hide screen hermione_02_w
    show screen hermione_02_wf1
    her " ....hah....hooo....oh...Oh, my!"
    m "............."
    her "You (huh huh)....you can (hah huh hah)....you can open your..(swallow)..eyes now, I think.  (huh huhhh)"
    hide screen hermione_02_wf1
    $hermione_SC.chibi.ypos = 250
    show screen hermione_02_wf2
    m "Well, Miss Granger, do you think that was a success?"
    her "Oh, heavens yes!  I never thought my wand could do something like that...I mean, store all that energy!  "
    m "Wonderful!  Now, let me examine your wand again, please."
    her "(Hermione pulls it from under her skirt, looks at it, then pauses and wipes it off on the hem before handing to Genie)"
    hide screen hermione_02_wf
    show screen hermione_blink
    m "Hmmm.  Yes, yes, yes.  Excellent!  Miss Granger, I believe you may have reduced the amount of magic stored in the wand by a considerable amount."  
    m "Possibly 2 or maybe even 3 percent!"
    her "Two percent!? Is that all?"
    m "Oh, yes.  But that was an excellent first attempt.  You should be very proud of the way you have performed tonight.  "
    m "This is very advanced magic especially for one of your age.  Ten points to Gryffindor!"
    $ current_payout = 10  # Let's give her a little encouragement for her first masturbation session
    $ gryffindor +=current_payout  #10 points
    her "Ten points?!  Th-thank you sir!"
    m "Do not thank me.  You earned it, Miss Granger.  "
    her "Will I get ten points every time I successfuly transfer my magic back?"
    m "Miss Granger!  Please!  I awarded you points because you were able to master a new magical skill!"
    m "Please do not try to bait me into awarding more points for something that benefits you alone!"
    her "I'm sorry, sir.  I really need to find a way to help Gryffindor get more points.  The Slytherins are cheating and may win the House Cup!"
    m "Regardless of that, you must continue to work on retrieving your magic at all costs.  Any time you have a free moment you need to work on it.  "
    m "Perhaps late at night before you go to sleep, or in the mornings at your bath.  Or if you find you cannot sleep."  
    m "When you take a break in the library, or are reading in class."
    her "I think I can manage to do that..."
    m "But I warn you, every time you use your wand to do magic in class or elsewhere some of your essence will leach back into it."
    m "You will need to be diligent in retrieving it afterwards so you do not get behind again!"
    m "Once we have built your innate magic back to a usable level I can help you learn to move beyond the wand, so to speak!"
    her "Oh, Professor!  Thank you so much!  I will work very hard to get my magic back from my wand!  "
    her "And to think all this time I was actually making things worse by practising magic so much!  "
    m "You may want to cut back on that until you can retrieve more of your essence."
    her "That will affect my grades, I'm sure.  But I will do it!  I don't want to go back to living as a muggle!"
    her "Um, Professor, can I still come by for lessons, or just to talk to you?  I want to be ready for when I no longer need my wand to do magic."
    m "Of course, my dear.  Feel free to come as often as you like!  Now, I have some work to do and you need to be off to bed."
    her "Yes, sir.  And I promise you I will be retrieving more of my magic when I get back to my room!"
    m "Oh, and Miss Granger?"
    her "Yes, Professor?"
    m "I think you should re-enroll in the Divination class.  Professor Treelawn can help you learn to read auras so you will know how much magic you have restored."
    her "It's Professor Trelawney, sir.  And Divination is during the time I spend in the library each day catching up on my other classwork!"
    m "If you want to continue to recover your powers you will need the skills she can teach you."
    m "I can think of no other teacher here who would be more qualified.  But do not worry."
    m "I will write a note to her asking her to let you into her class and to give you a little extra time to catch up on the assignments you have missed."
    her "All right.  I will try to get her work done on top of everything else I have in my {i}real{/i} classes.  And without my study period, too."
    m "Very good, Miss Granger.  I'm sure you will be right as rain before you know it."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    $ badges = True
    with d3                                                                                                                                                                                                                        #HERMIONE
#    $ hermione_body = "01_hp/13_hermione_main/body_205.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
#    show screen hermione_main                                                                                                                                                                                 #HERMIONE
#    with d3                                                                                                                                                                                                                        #HERMIONE
    stop music
    
#    show screen blktone8
#    with d3

    $ only_upper = False
    $ ne = True # Desplays a fishnets in hermione_main screen.
    
    
    
    
    
    
    
    
    
    #"You spend the evening tutoring Hermione. Hermione become a bit smarter."
    
#    if knowledge >= 5 and tutoring_events == 0 and whoring >= 1:
#        $ tutoring_events += 1
#        "Event 01"
        
#    if knowledge >= 10 and tutoring_events == 1 and whoring >= 2: #LEVEL 02
#        $ tutoring_events += 1
#        "Event 02"
        
#    if knowledge >= 15 and tutoring_events == 2 and whoring >= 3: #LEVEL 03
#        $ tutoring_events += 1
#        "Event 03"
        
#    if knowledge >= 20 and tutoring_events == 3 and whoring >= 4: #LEVEL 04
#        $ tutoring_events += 1
#        "Event 04"
        
#    if knowledge >= 25 and tutoring_events == 4 and whoring >= 5: #LEVEL 05
#        $ tutoring_events += 1
#        "Event 05"
        
#    if knowledge >= 30 and tutoring_events == 5 and whoring >= 7: #LEVEL 06
#        $ tutoring_events += 1
#        "Event 06"
        
#    if knowledge >= 35 and tutoring_events == 6 and whoring >= 8: #LEVEL 07
#        $ tutoring_events += 1
#        "Event 07"
         
#    if knowledge >= 40 and tutoring_events == 7 and whoring >= 9: #LEVEL 08
#        $ tutoring_events += 1
#        "Event 08"
        
#    if knowledge >= 45 and tutoring_events == 8 and whoring >= 11: #LEVEL 09
#        $ tutoring_events += 1
#        "Event 09"
        
#    if knowledge >= 50 and tutoring_events == 9 and whoring >= 13: #EVENT 10
#        $ tutoring_events += 1
#        "Event 10"
        
#    if knowledge >= 55 and tutoring_events == 10 and whoring >= 14: #EVENT 10
#        $ tutoring_events += 1
#        "Event 11"
        
#    if knowledge >= 60 and tutoring_events == 11 and whoring >= 16: #EVENT 11
#        $ tutoring_events += 1
#        "Event 12"
         
#    if knowledge >= 65 and tutoring_events == 12 and whoring >= 18: #EVENT 12
#        $ tutoring_events += 1
#        "Event 13"
        
#    if knowledge >= 70 and tutoring_events == 13 and whoring >= 20: #EVENT 13
#        $ tutoring_events += 1
#        "Event 14"
        
#    if knowledge >= 75 and tutoring_events == 14 and whoring >= 21: #EVENT 14
#        $ tutoring_events += 1
#        "Event 15"
        
 
    
   
#    $ knowledge +=1
#    "You dismiss Hermione."
    jump day_start