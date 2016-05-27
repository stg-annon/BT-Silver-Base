###POTION SCENES
label potion_scene_1: #catears (keep in mind Genie is trying to transform her into another girl)
    m "[hermione_name]?"
    $ changeHermioneMainScreen(hg_pth+"body_01.png")
    her "Yes, [genie_name]?"
    m "Today I have a new type of favour for you to perform."
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    her "What do you mean new? What do I have to do?"
    m "It's quite simple, today you will be drinking a potion"
    $ changeHermioneMainScreen(hg_pth+"body_08.png")
    her "Is that it? How much will I get paid?"
    m "20 points."
    $ changeHermioneMainScreen(hg_pth+"body_17.png")
    her "Hmmm, what type of potion is it?"
    $ changeHermioneMainScreen(hg_pth+"body_24.png")
    her "Polyjuice? Amortentia? Babbling Beverage? Felix Felicis?"
    m "That's a secret [hermione_name]."
    $ changeHermioneMainScreen(hg_pth+"body_73.png")
    her "..."
    m "Well [hermione_name], what do you say? Will you drink a harmless little potion?"
    m "For Gyrffindor?"
    $ changeHermioneMainScreen(hg_pth+"body_16.png")
    her "Fine..."
    ">Hermione takes a whif of the thick potion."
    $ changeHermioneMainScreen(hg_pth+"body_43.png")
    her "This smells disgusting. Like mud and wet dog fur."
    $ changeHermioneMainScreen(hg_pth+"body_11.png")
    her "Do I really have to drink this?"
    m "You do. I suggest holding your nose if the smell is too much."
    $ changeHermioneMainScreen(hg_pth+"body_20.png")
    her "For Gryffindor."
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione holds her nose and quickly downs the flask."
    $ changeHermioneMainScreen(hg_pth+"body_42.png")
    pause
    $ changeHermioneMainScreen(hg_pth+"body_22.png")
    hide screen ch_potion
    show screen hermione_blink
    her "Ughhh. That was horrible."
    m "Well done."
    $ changeHermioneMainScreen(hg_pth+"body_21.png")
    her "Now will you at least tell me what this potion does."
    m "It should be noticeable any second now..."
    $ changeHermioneMainScreen(hg_pth+"body_73.png")
    her "Well? Is it supposed to make my breasts bigger? They don't feel any bigger."
    m "No. Hmmmm, it mustn't have worked."
    $ changeHermioneMainScreen(hg_pth+"body_70.png")###Left off
    her "What was it supposed to do?"
    m "There's no point in telling you now. It was going to be a surprise."
    m "Damn Snape must've conned me."
    $ changeHermioneMainScreen(hg_pth+"body_15.png")
    her "Is that all [genie_name]?"
    m "Yes, [hermione_name], 20 points to Gryffindor."
    $ changeHermioneMainScreen(hg_pth+"body_06.png")
    her "Thank you [genie_name]."
    ">Hermione heads off to class."
    $ gryffindor += 20

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ ears = True
    if hair_color == 5:
        $ hair_color = 0
    elif hair_color == 6:
        $ hair_color = 1
    elif hair_color == 7:
        $ hair_color = 3
    elif hair_color == 8:
        $ hair_color = 4
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_1_2: #Scene where Hermione comes back after classes angry and confused at being given cat ears and a tail.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    $ changeHermioneMainScreen(hg_pth+"body_05.png")
    her "How could you do this to me [genie_name]?"
    her "Try and turn me into a cat!"
    $ changeHermioneMainScreen(hg_pth+"body_29.png")
    her "In the middle of class!"
    m "I didn't try and turn you into a cat [hermione_name]."
    $ changeHermioneMainScreen(hg_pth+"body_30.png")
    her "Then why do I have ears and a tail?"
    m "I have no idea. The potion I gave you was supposed to turn you into a different girl."
    $ changeHermioneMainScreen(hg_pth+"body_48.png")
    her "What!? You didn't use polyjuice potion did you [genie_name]?"
    m "What's that?"
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "There's no point playing dumb [genie_name]."
    $ changeHermioneMainScreen(hg_pth+"body_69.png")
    her "Well at least I know that it will wear off by morning."
    menu:
        "-Let her go-":
            m "Goodnight [hermione_name]."
            $ changeHermioneMainScreen(hg_pth+"body_120.png")
            her "Goodnight [genie_name]."
            hide screen bld1
            hide screen hermione_main
            hide screen blktone 
            hide screen ctc
            with Dissolve(.3)
            $ ears = False
            
            call her_walk(400,610,2)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            with Dissolve(.3)
            
            $ hermione_sleeping = True
            jump night_main_menu
        "-Make her suck you off-" if whoring >= 17:
            pass
    m "Wait [hermione_name], how would you like to earn 75 additional points?"
    $ changeHermioneMainScreen(hg_pth+"body_17.png")
    her "75 points? How?"
    m "By sucking my cock."
    $ changeHermioneMainScreen(hg_pth+"body_119.png")
    her "Like this? I look like a cat! Why would you ask me at a time like this?"
    $ changeHermioneMainScreen(hg_pth+"body_117.png")
    her "You're not some sort of pervert who likes animals are you?"
    m "Of course not, I just think that you have a very unique look at the moment and that it would be a shame not to do anything with it."
    $ changeHermioneMainScreen(hg_pth+"body_120.png")
    her "Fine, just promise me you aren't going to do anything weird."
    m "I promise. Now, kneel."
    ">Hermione walks over and kneels before you."
    m "Good girl."
    $ changeHermioneMainScreen(hg_pth+"body_115.png")
    her "..."
    ">Hermione takes you into her mouth"                ###Have the chibi scene of her sucking
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    show screen g_c_u
    
    hide screen hermione_blink #Hermione stands still.
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    show screen ctc
    with fade
    pause
    show screen bld1
    with d3
    m "Good god what is with your tongue?! It feels like velcro."
    her "*Slurp?*"    
    $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_chibi_ypos = 10
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ hermione_main_zorder = 8
    $ changeHermioneMainScreen(hg_pth+"body_116.png", x_pos=390, y_pos= 235)    ###Stop the chibi scene
    her "It's because of your stupid potion, it's \nmade my tongue all rough."
    $ changeHermioneMainScreen(hg_pth+"body_68.png", x_pos=390, y_pos= 235)    
    her "Do you want to stop?"
    hide screen hermione_main
    m "No, keep going, just try not to focus on the tongue work too much."
    $ changeHermioneMainScreen(hg_pth+"body_69.png", x_pos=390, y_pos= 235)    
    her "Yes [genie_name]."
    hide screen hermione_main
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    hide screen h_c_u
    show screen g_c_u
    with d3
    ">Hermione swallows your cock again, taking care\nnot to apply too much pressure with her tongue."   ###start sucking scene. might insert more sucking noises for a little while or add pauses
    m "So you still went to all your classes?"
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ changeHermioneMainScreen(hg_pth+"body_128.png", x_pos=390, y_pos= 235)         ###stop sucking
    her "Of course [genie_name]."     
    hide screen hermione_main  
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    hide screen h_c_u
    show screen g_c_u
    m "Even looking like this?"                         ###start sucking
    m "What would everyone have thought? Would they just assume that you were under an evil slytherin spell?"
    m "Or would they just think that slutty little Miss Granger was just begging for attention again."
    m "Wearing skimpy outfits and trying to look like a cat."
    ">You go to place your hand on the back of her head but her new ears block the way."
    m "These are quite soft."
    ">You start feeling and patting the ears."
    ">Hermione starts involuntary purring"
    m "Oh good heavens!"
    m "It's like your whole mouth has become a vibrator."
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ changeHermioneMainScreen(hg_pth+"body_74.png", x_pos=390, y_pos= 235)         ###stop sucking
    her "I can't help it [genie_name], whenever \nanything touches my ears I just purr."
    hide screen hermione_main
    m "It feels amazing, now cock back in the mouth girl."
    $ changeHermioneMainScreen(hg_pth+"body_80.png", x_pos=390, y_pos= 235)    
    her "Yes [genie_name]."
    $ g_c_u_pic = "blowjob_ani"
    show screen chair_02
    hide screen h_c_u
    show screen g_c_u
    hide screen hermione_main
    with d3
    m "You immediately put your hands back on her ears and start stroking them as she sucks you."### start sucking
    her "*Slurp!* *Purr* *Slurp!*"
    m "Oh gods yes. This is Fantastic."
    her "*Purr* *Slurp!* *Purr*"
    m "Get ready girl... Here it comes."
    her "*Purr* *Purr* *Purr*"
    ">You grab her ears and pull her head into you causing the tip of your cock to rest on her purring throat."###show genie climax scene
    g4 "{size=+10}ARGH!!!!!!!!!!!!!!!!{/size}"
    her "*Purr* *Purr* *Purr*"
    ">You shoot you load directly down her throat."     ###have picture 125 and 126 play each time she swallows
    show screen ctc
    pause
    with d3
    $ g_c_u_pic = "cum_in_mouth_ani"
    hide screen h_c_u   # SUCKING
    show screen g_c_u # SUCKING
    with d3 
    $ changeHermioneMainScreen(hg_pth+"body_125.png", x_pos=390, y_pos= 235)
    pause .1
    $ changeHermioneMainScreen(hg_pth+"body_126.png", x_pos=390, y_pos= 235)
    her "*gulp* *Purr* *Purr*"
    $ changeHermioneMainScreen(hg_pth+"body_125.png", x_pos=390, y_pos= 235)
    pause .1
    $ changeHermioneMainScreen(hg_pth+"body_126.png", x_pos=390, y_pos= 235)
    her "*gulp* *Purr* *gulp*"
    $ changeHermioneMainScreen(hg_pth+"body_125.png", x_pos=390, y_pos= 235)
    pause .1
    $ changeHermioneMainScreen(hg_pth+"body_126.png", x_pos=390, y_pos= 235)
    her "*Purr* *gulp* *gulp*"
    ">You pull your cock out of her purring mouth."
    show screen h_c_u
    hide screen g_c_u
    $ changeHermioneMainScreen(hg_pth+"body_128.png", x_pos=390, y_pos= 235) 
    her "Mmmmm, it might be this potion but that tasted \ngood..."
    hide screen hermione_main
    m "Well, you certainly earned your 75 points."
    $ gryffindor += 75
    $ h_c_u_pic = "hand_ani"
    $ changeHermioneMainScreen(hg_pth+"body_78.png", x_pos=390, y_pos= 235) 
    her "Thank you [genie_name]. Will that be all."
    hide screen hermione_main
    m "One last thing."
    m "Who's a good girl?"
    $ changeHermioneMainScreen(hg_pth+"body_29.png", x_pos=390, y_pos= 235) 
    her ".........."
    $ changeHermioneMainScreen(hg_pth+"body_46.png", x_pos=390, y_pos= 235) 
    her "I am..."

    $ ears = False
    $ hermione_main_zorder = 5
    hide screen chair_02
    hide screen bld1
    hide screen h_c_u
    hide screen g_c_u
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ hermione_chibi_ypos = 250
    jump night_main_menu
    
    
label potion_scene_2_1: #breast expansion - Until chibis are added for it tifucking won't be written
    m "Guess what I have for you today."
    $ changeHermioneMainScreen(hg_pth+"body_04.png")
    her "Is it another foul tasting potion that will try transform me into a hideous animal?"
    m "Well I mean this one smells nice."
    $ changeHermioneMainScreen(hg_pth+"body_02.png")
    her "Will it taste nice though?"
    m "Only one way to find out."
    ">You hand her the potion and she brings it up to her nose."
    $ changeHermioneMainScreen(hg_pth+"body_06.png")
    her "Well you're right, it does smell good. Let's find out if it tastes good..."
    hide screen hermione_blink
    show screen ch_potion
    ">She drinks the potion at a leisurely pace."
    $ changeHermioneMainScreen(hg_pth+"body_74.png")
    her "Ahhh."
    $ changeHermioneMainScreen(hg_pth+"body_64.png")
    show screen hermione_blink
    hide screen ch_potion
    her "That wasn't actually that bad."
    $ changeHermioneMainScreen(hg_pth+"body_122.png")
    her "So, now that I've had the potion, will you tell me what it's supposed to do."
    m "No need to ruin the fun, it should take effect relatively quickly."
    $ changeHermioneMainScreen(hg_pth+"body_128.png")
    her "Well what am I supposed to do until then?"
    m "You could show me your tits."
    $ changeHermioneMainScreen(hg_pth+"body_127.png")
    her "I don't think so [genie_name], you're only paying me for drinking the potion."
    $ changeHermioneMainScreen(hg_pth+"body_129.png")
    her "If you expect to see me without my shirt on then you'll have to try a little harder."
    m "Oh I wouldn't be so sure of that."
    $ changeHermioneMainScreen(hg_pth+"body_45.png")
    her "So is that what it does? Makes me show you my breasts? Is it some sort of mind control potion?"
    m "Mind control? Where's the fun in that? No, this is something much more entertaining."
    $ changeHermioneMainScreen(hg_pth+"body_69.png")
    her "Well it better happen soon otherwise I'm lea-"
    ">You notice her breasts start to expand ever so slightly." ###Start using facial expressions mixed with Captain Nemo art
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "..."
    $ changeHermioneMainScreen(hg_pth+"body_29.png")
    her "As I said, something better happen soon or I'm leaving."
    m "I wouldn't worry about it, from the looks of it, it's already started."
    $ changeHermioneMainScreen(hg_pth+"body_31.png")
    her "Why, what's wrong with me?"
    m "There's nothing wrong with you. If anything, it's an improvement."
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "What is?"
    ">She starts patting down her body. Checking to see if she has grown any new ears or a tail."
    $ changeHermioneMainScreen(hg_pth+"body_87.png")
    her "I don't see what you could be..."
    ">She grabs her breasts to check them."
    $ changeHermioneMainScreen(hg_pth+"body_118.png")
    her "!!!"
    $ changeHermioneMainScreen(hg_pth+"body_119.png")
    her "Have my breasts gotten bigger?"
    m "About time you noticed."
    $ changeHermioneMainScreen(hg_pth+"body_117.png")
    her "Why would you make my breasts bigger? They're already big enough!"
    m "You know what they say, can't have too much of a good thing."
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "It's the other way around [genie_name]."
    m "Is it? Well I prefer my version."
    $ changeHermioneMainScreen(hg_pth+"body_118.png")
    her "Well how big are they supposed to-"
    ">Her breast swell up again."
    $ custom_breast = 4
    $ changeHermioneMainScreen(hg_pth+"body_119.png")
    her "You can't be serious. At this rate they're going to rip my shirt."
    m "Well they should stop there."
    $ changeHermioneMainScreen(hg_pth+"body_47.png")
    her "Good, they're big enough as is."
    menu:
        "-Send her to class-":
            m "You're right, I suppose they are big enough."
            m "Well that's all for today, 20 points to Gryffindor."
            $ changeHermioneMainScreen(hg_pth+"body_48.png")
            her "That's all? You're not going to make me do something else?"
            m "Why would I, I asked you to drink a potion and you drank it. You're free to leave."
            $ changeHermioneMainScreen(hg_pth+"body_46.png")
            her "Thank you [genie_name], I'll head back to my room."
            m "Room? It's time for class [hermione_name]. What do you think Professor Snape will say once he hears that you skipped class?"
            $ changeHermioneMainScreen(hg_pth+"body_66.png")
            her "Well I can't be expected to go like this."
            m "Why not? Everything is covered."
            $ changeHermioneMainScreen(hg_pth+"body_118.png")
            her "Barely. And what will people think of me."
            m "Just tell them that you are still developing. I'm sure that they're used to enormous breasts anyway, what's a few extra sizes."
            $ changeHermioneMainScreen(hg_pth+"body_120.png")
            her "...Fine. Just promise me that they won't get any bigger."
            m "I can't promise that, your still in highschool. A lot of girls don't stop growing until their 30."
            $ changeHermioneMainScreen(hg_pth+"body_86.png")
            her "You know what I mean [genie_name]."
            m "I'm afraid that I don't [hermione_name], now you'd best hurry if you don't want to be late."
            $ changeHermioneMainScreen(hg_pth+"body_79.png")
            her "...Yes [genie_name]."
            hide screen bld1
            hide screen hermione_main
            hide screen blktone 
            hide screen ctc
            with Dissolve(.3)
            
            call her_walk(400,610,2)
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            with Dissolve(.3)
            
            $ hermione_takes_classes = True
            jump day_main_menu
        "-Play with her breasts-":
            pass
    m "Well that's a matter of personal opinion."
    m "Now how would you like to earn some additional points?"
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "I want an extra 40."
    m "I haven't even told you what I want to-"
    $ changeHermioneMainScreen(hg_pth+"body_69.png")
    her "If you want to touch my breasts it will be an extra 40 points."
    m "Deal."
    ">Hermione walks over to behind your desk, her breasts swaying rhythmically as she moves."
    show screen blkfade
    hide screen hermione_blink #Stands with tits out.
    hide screen genie
    show screen groping_naked_tits
    with d1
    with d5
    hide screen blkfade
    $ changeHermioneMainScreen(hg_pth+"body_44.png")
    her "Well..."
    ">You reach out and grab her breasts through her stretched shirt."
    $ changeHermioneMainScreen(hg_pth+"body_119.png")
    her "!!!"
    $ changeHermioneMainScreen(hg_pth+"body_117.png")
    her "Please be gentle [genie_name]. They seem to be much more sensitve than usual, it must be the potion."
    m "Well I'll take that into account..."
    ">You take a breast in each hand and start kneading them with your fingers."
    $ changeHermioneMainScreen(hg_pth+"body_127.png")
    her "..."
    m "They're certainly much larger than usual."
    $ changeHermioneMainScreen(hg_pth+"body_121.png")
    her "...yes"
    ">You continue massaging them gently through her shirt. Pulling them apart and then pressing them into one another."
    $ changeHermioneMainScreen(hg_pth+"body_118.png")
    her "...It feels like they're getting-"
    $ custom_breast =2
    $ custom_outfit_old = 20
    "*RIIIP*"
    $ changeHermioneMainScreen(hg_pth+"body_119.png")
    her "!!!"
    $ changeHermioneMainScreen(hg_pth+"body_86.png")
    her "You said that they wouldn't get any bigger! Now look, my shirt has been ruined."
    m "Don't worry about that [hermione_name], worry about earning your 40 points."
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "Just hurry up."
    menu: #Will add titfuck here
        #"-Suck her nipples-":
            #"asd"
        #"-Titfuck her-":
            #"asd"
        "-Play with her nipples-":
            pass
    ">You take her exposed breasts back into your hands and continue massaging"
    $ changeHermioneMainScreen(hg_pth+"body_78.png")
    her "sir... they seem to have become more sensitive..."
    $ changeHermioneMainScreen(hg_pth+"body_121.png")
    her "Please don't do anything sudden."
    m "Like this?"
    ">You take both nipple between your thumb and index finger."
    $ changeHermioneMainScreen(hg_pth+"body_130.png")
    her "!!!"
    $ changeHermioneMainScreen(hg_pth+"body_132.png")
    her "Please stop... it's too much, it's like my nipples are on fire."
    m "Shhhh, just be still, it'll all be over soon."
    ">You start rolling her nipples in between your fingers."
    $ changeHermioneMainScreen(hg_pth+"body_131.png")
    her "..."
    ">You feel her push her crotch against your thigh."
    m "Feeling a little aroused are we?"
    ">You start to pinch and pull her nipples."
    $ changeHermioneMainScreen(hg_pth+"body_121.png")
    her "Ohhh"
    ">She starts grinding herself against your thigh"
    m "Well, well, well, you are sensitive now aren't you? Trying to grind out an orgasm on your headmasters leg, how shameless."
    $ changeHermioneMainScreen(hg_pth+"body_123.png")
    her "..."
    m "Well let's see if we can do something about that."
    ">You start alternating pinching and pulling her nipples hard, pulling the nipples out as far as you can and then pushing them back into her breast."
    $ changeHermioneMainScreen(hg_pth+"body_130.png")
    her "!!!"
    her "I-I-I'm cumming!"
    ">She starts grinding hard against your leg as a wet spot starts to form on her skirt."
    m "What a naughty little girl."
    ">She breathes heavily as she rests against you"
    $ changeHermioneMainScreen(hg_pth+"body_121.png")
    her "Will... that be all [genie_name]?"
    m "Yes [hermione_name]. You can go now."
    $ custom_breast = 0
    $ custom_outfit_old = 0
    hide screen bld1
    hide screen hermione_main
    hide screen groping_naked_tits
    hide screen blktone 
    hide screen ctc
    show screen genie
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_takes_classes = True
    jump day_main_menu



label potion_scene_2_1_2: #Hermione comes back after having her breasts expand in class


label potion_scene_2_2: #ass expansion
    m "[hermione_name], I have another potion for you to try today."
    $ changeHermioneMainScreen(hg_pth+"body_08.png")
    her "Another one? Where are you getting these?"
    m "That's of no concern to you. What should concern you is the 20 points that you are able to earn should you drink it."
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    her "...Fine, give me the bottle."
    ">She takes a quizzical smell of the bottle."
    $ changeHermioneMainScreen(hg_pth+"body_06.png")
    her "At least this one smells good."
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">She drinks the whole potion over a series of gulps."
    hide screen ch_potion
    with d3
    show screen hermione_blink
    $ changeHermioneMainScreen(hg_pth+"body_24.png")
    her "Ahhh, that was good! So what was it?"
    m "The effects should be visible soon enough."
    $ changeHermioneMainScreen(hg_pth+"body_14.png")
    her "Well can you at least give me a hint?"
    m "Let's just say that it's a redistribution of ass{w}ets." ###Added {w} instead of your ...
    $ changeHermioneMainScreen(hg_pth+"body_12.png")
    her "What do you mean by--"
    ">Hermione goes white as she starts to feel her body churn."
    $ changeHermioneMainScreen(hg_pth+"body_18.png")
    her "What's going on. It feels like my insides are moving."
    $ changeHermioneMainScreen(hg_pth+"body_121.png")
    her "And my ass, it feels so... good."
    ">You start to notice her ass increase in size."    ###Use bigger butt from Captain Nemo
    $ changeHermioneMainScreen(hg_pth+"body_119.png")
    her "It feels too sensitive... I have to take my skirt off" ###changed so to too
    pause 0.2
    $ custom_skirt = 2
    $ changeHermioneMainScreen(hg_pth+"body_118.png")
    her "ughhh, has it gotten bigger?"
    $ changeHermioneMainScreen(hg_pth+"body_120.png")
    her "Is that what this potion's supposed to do? Makes my ass bigger?"
    m "Evidently."
    $ changeHermioneMainScreen(hg_pth+"body_121.png")
    her "Why does my ass feel so good?" ###new
    ">Hermione keeps rubbing her ass, rolling her fingers across her expanded buttocks."
    m "Hmmm, it's not supposed to, but I guess every case is different."
    $ changeHermioneMainScreen(hg_pth+"body_123.png")
    her "It's just so sensitive... [genie_name] do you think that you could... massage me?"
    m "Well I mean I'm hardly going to say no am I."
    ">Hermione hops over to your desk, her ass bouncing as she moves, and presents herself to you."
    hide screen bld1
    with d3
    
    call her_walk(400,280,3,redux_pause=2)
    show screen blkfade
    with Dissolve(1)
    pause.5
    hide screen genie
    show screen ctc
    show screen no_groping_02
    with d1
    hide screen blkfade
    with d5
    pause
    $ changeHermioneMainScreen(hg_pth+"body_131.png")
    her "Please [genie_name]... please take advantage of me..."
    m "As you command."
    ">You take her engorged buttocks in your hands. Each one is now much larger than before."
    hide screen hermione_main
    hide screen no_groping_02
    with d3
    show screen groping_02
    m "Well this potion certainly is effective."
    ">You start firmly stroking her ass cheeks. Pulling them apart to reveal her asshole and then squishing them together."
    ">Seeing her tight asshole gives you an idea."
    $ hermione_main_zorder = 8
    menu: #Thought about adding a rimming option here but the chibis don't really support it
        "-Finger her asshole-":
            ">You pull her asscheeks open again to show her puckered hole."
            m "Let's see how sensitive you really are."
            ">You start teasing the entrance with your finger, circling the entrance slowly."
            $ changeHermioneMainScreen(hg_pth+"body_132.png", x_pos=390, y_pos= 235)
            her "!!!"
            $ changeHermioneMainScreen(hg_pth+"body_121.png", x_pos=390, y_pos= 235)
            her "[genie_name] please... I'm too sensitive. If you do that, \nI'm not sure I'll be able to control myself."
            hide screen hermione_main
            m "Well in that case..."
            ">You slowly pull your finger away from her asshole."
            $ changeHermioneMainScreen(hg_pth+"body_121.png", x_pos=390, y_pos= 235)
            her "Thank yo-"
            ">And then fully insert it."
            $ changeHermioneMainScreen(hg_pth+"body_119.png", x_pos=390, y_pos= 235)
            her "..."
            her "..."
            her "..."
            $ changeHermioneMainScreen(hg_pth+"body_130.png", x_pos=390, y_pos= 235)
            her "{size=-10}I'm cumming{/size}"
            hide screen hermione_main
            m "What was that?"
            ">You start turning your finger."
            $ changeHermioneMainScreen(hg_pth+"body_32.png", x_pos=390, y_pos= 235)
            her "{size=+10}I'm cumming!{/size}"
            ">Her asshole starts quivering around your finger."
            hide screen hermione_main
            m "What a little anal slut. I wonder what you'll do once I try this."
            ">You start pumping your finger in and out of her shivering asshole."
            $ changeHermioneMainScreen(hg_pth+"body_132.png", x_pos=390, y_pos= 235)
            her "!!!"
            $ changeHermioneMainScreen(hg_pth+"body_131.png", x_pos=390, y_pos= 235)
            her "I'm cumming again!"
            m "So soon?"
            $ changeHermioneMainScreen(hg_pth+"body_119.png", x_pos=390, y_pos= 235)
            her "I can't stop! Please [genie_name], please, no more!"
            menu:
                "-Stop-":
                    m "Well, I suppose that's enough for now..."
                    ">You pull your finger out of her asshole and she immediately slumps over your desk."
                    $ changeHermioneMainScreen(hg_pth+"body_123.png", x_pos=390, y_pos= 235)
                    her "That was... great..."
                    ">She lies on your desk, breathing heavily."
                "-Keep Going-":
                    m "What was that [hermione_name]? It almost sounded like you asked me to stop."     ###Or would it be better if she start to tear up and cry a bit?
                    ">You increase the pace."
                    $ changeHermioneMainScreen(hg_pth+"body_131.png", x_pos=390, y_pos= 235)
                    her "Please..."
                    m "Please what?"
                    ">You insert a second finger."
                    $ changeHermioneMainScreen(hg_pth+"body_118.png", x_pos=390, y_pos= 235)
                    her "Please... stop... you'll break me..."
                    ">You grab her hip with one hand and keep finger fucking her asshole."
                    $ changeHermioneMainScreen(hg_pth+"body_132.png", x_pos=390, y_pos= 235)
                    her "..."
                    $ changeHermioneMainScreen(hg_pth+"body_32.png", x_pos=390, y_pos= 235)
                    her "..."
                    ">You feel her body go limp as her asshole relentlessly quivers around your fingers."
                    m "There, wasn't that nice?"
                    ">You slow down and pull out of her asshole."
                    $ changeHermioneMainScreen(hg_pth+"body_123.png", x_pos=390, y_pos= 235)
                    her "...yeeess...[genie_name]..."
                    m "Good girl."
            m "Well you best be off to class."
            $ changeHermioneMainScreen(hg_pth+"body_118.png")
            her "...With my butt looking like this?"
            m "I'm sure no one will be able to tell \nwith your skirt on. Now hurry up \nI have things to attend to."
            $ hermione_main_zorder = 5
            hide screen blktone8
            hide screen ctc
            hide screen bld1
            hide screen groping_01
            hide screen groping_02
            show screen hermione_blink
            show screen genie
            with d1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            show screen bld1
            hide screen blkfade
            with Dissolve(1)
            $ changeHermioneMainScreen(hg_pth+"body_124.png")
            her "Yes [genie_name]."
            m "Oh I almost forgot, 20 points to Gryffindor!"
            $ gryffindor += 20
            $ changeHermioneMainScreen(hg_pth+"body_123.png")
            her "Oh... right, the points. Thank you."
            ">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it."
            $ custom_skirt = 0
            $ changeHermioneMainScreen(hg_pth+"body_87.png")
            her "..."
        "-Hot dog her-" if whoring >= 17:
            m "Bend over [hermione_name]."
            ">Before she even has a chance to react you push her forward over your desk."
            hide screen hermione_main
            hide screen groping_02
            with d3
            show screen ch_hotdog
            $ changeHermioneMainScreen(hg_pth+"body_119.png", x_pos=390, y_pos= 235)
            her "!!!"
            $ changeHermioneMainScreen(hg_pth+"body_122.png", x_pos=390, y_pos= 235)
            her "What are you going to do [genie_name]?"
            hide screen hermione_main
            m "Well seeing as how your ass has become so fucking huge I thought I may as well put it to good use."
            ">You pull you cock out from your robes and place it on top of her ass crack."
            $ changeHermioneMainScreen(hg_pth+"body_123.png", x_pos=390, y_pos= 235)
            her "Your not going to fuck my asshole are you [genie_name]?"
            hide screen hermione_main
            m "Not your asshole, [hermione_name], I intend to fuck your entire ass!"
            ">You grab a firm hold of her cheeks and pull them apart, allowing your shaft to rest in between, on top of her asshole."
            m "A perfect fit wouldn't you say?"
            $ changeHermioneMainScreen(hg_pth+"body_117.png", x_pos=390, y_pos= 235)
            her "What do you-"
            hide screen hermione_main
            ">You squeeze her asscheeks back together around your cock and start pumping in between them."
            $ changeHermioneMainScreen(hg_pth+"body_136.png", x_pos=390, y_pos= 235)
            her "!!!"
            hide screen hermione_main
            m "Fuck, you're ass is so soft. It's like fucking a pillow."
            $ changeHermioneMainScreen(hg_pth+"body_138.png", x_pos=390, y_pos= 235)
            her "Ahhh"
            $ changeHermioneMainScreen(hg_pth+"body_134.png", x_pos=390, y_pos= 235)
            her "Please [genie_name]"
            hide screen hermione_main
            m "Ughh, this feels so good, we might have to make this permanent."
            $ changeHermioneMainScreen(hg_pth+"body_139.png", x_pos=390, y_pos= 235)
            her "Permanent?"
            hide screen hermione_main
            m "You wouldn't mind would you?"
            m "Having me use your ass a sextoy everyday."
            $ changeHermioneMainScreen(hg_pth+"body_141.png", x_pos=390, y_pos= 235)
            her "..."
            hide screen hermione_main
            m "I asked you a question [hermione_name]."
            $ changeHermioneMainScreen(hg_pth+"body_133.png", x_pos=390, y_pos= 235)
            her "... no [genie_name]..."
            hide screen hermione_main
            ">You feel her asshole start quiver as you glide over it."
            m "Of course you wouldn't, you're enjoying this more than I am, aren't you?"
            $ changeHermioneMainScreen(hg_pth+"body_134.png", x_pos=390, y_pos= 235)
            her "...yes... I'm loving... you using my ass as your toy"
            hide screen hermione_main
            m "That's it girl, here I come!"
            ">With one final thrust you cum, covering her fat ass with your seed."
            hide screen ch_hotdog
            $ g_c_u_pic = "sex_cum_out_ani"
            show screen chair_02
            show screen g_c_u
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            show screen ctc
            pause
            hide screen ctc
            $ uni_sperm = True
            $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
            m "Ughhh"
            m "All over your fucking back."
            ">You fall back into your chair, spent."
            m "You may go now [hermione_name]."
            $ hermione_main_zorder = 5
            hide screen blktone8
            hide screen ctc
            hide screen bld1
            hide screen groping_01
            hide screen groping_02
            hide screen chair_02
            hide screen g_c_u
            show screen hermione_blink
            show screen genie
            with d1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            show screen bld1
            hide screen blkfade
            with Dissolve(1)
            $ changeHermioneMainScreen(hg_pth+"body_141.png")
            her "...With my butt looking like this?"
            m "I'm sure no one will be able to tell with your skirt on. Now hurry up, I feel like a nap.'"
            #$ changeHermioneMainScreen(hg_pth+"body_141.png")
            her "Yes [genie_name]."
            m "Oh I almost forgot, 20 points to Gryffindor!"
            $ gryffindor += 20
            $ changeHermioneMainScreen(hg_pth+"body_136.png")
            her "Oh... right, the points. Thank you."
            ">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it."
            $ custom_skirt = 0
            ">Your cum is still visible on her ass."
            $ changeHermioneMainScreen(hg_pth+"body_127.png")   ###Add sweat to picture
            her "..."


    hide screen bld1
    hide screen hermione_main
    $ uni_sperm = False
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ hermione_takes_classes = True
    hide screen groping_02
    hide screen hermione_main
    hide screen no_groping_02

    jump day_main_menu
        #will add this later
        #"-Fuck her ass-" if whoring >= 22:    

label potion_scene_3: #cum addiction - work in progress, has some scenes adjusted for it
    m "[hermione_name], today I have a very special potion that I would like you to drink."
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    her "What does this one do?"
    m "As always, it's going to be a surprise."
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    her "You're not going to try to transform me into a cat again are you [genie_name]?"
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    m "Of course not, now would you kindly drink the potion."
    $ changeHermioneMainScreen(hg_pth+"body_12.png")
    her "..."
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">Hermione cautiously starts drinking the potion."
    $ changeHermioneMainScreen(hg_pth+"body_126.png")
    pause .5
    hide screen ch_potion
    with d3
    show screen hermione_blink
    $ changeHermioneMainScreen(hg_pth+"body_30.png")
    her "This isn't a potion! This is just a bottle full of your cum!"
    $ changeHermioneMainScreen(hg_pth+"body_43.png")
    her "Ughhh and it's cold as well."
    m "So it just tastes like cum to you?"
    $ changeHermioneMainScreen(hg_pth+"body_47.png")
    her "Of course it does, what else would it taste like?"
    ">Hermione starts unconsciously licking her lips."
    $ changeHermioneMainScreen(hg_pth+"body_10.png")
    her "At least warn me next time you make me drink your cum [genie_name]."
    m "What do you mean next time?"
    $ changeHermioneMainScreen(hg_pth+"body_79.png")
    her "Well you're such a pervert you'll probably try and do this again. At least warn me so it's not such a shock."
    m "Ok, [hermione_name], I'll make sure to warn you next time."
    $ changeHermioneMainScreen(hg_pth+"body_69.png")
    her "Is that all then [genie_name]?"
    m "Yes [hermione_name], 20 points to Gryffindor."
    $ changeHermioneMainScreen(hg_pth+"body_08.png")
    her "Thank you [genie_name]."
    ">Hermione leaves the room with the remaining potion firmly in her grasp."    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ addicted = True
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_3_2: #Scene where Hermione comes back addicted to your cum (replace sucking noises with actual text)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    ">Hermione quickly enters your office."
    $ changeHermioneMainScreen(hg_pth+"body_32.png")
    her "What the hell did you do to me?"
    m "Whatever are you talking about [hermione_name]?"
    $ changeHermioneMainScreen(hg_pth+"body_29.png")
    her "Ughh, it doesn't matter, just let me suck it."
    m "Why on earth would you want to do that? You're a top student, that doesn't sound appropriate."
    $ changeHermioneMainScreen(hg_pth+"body_47.png")
    her "You know exactly what you did to me. Now let me suck your filthy old cock."
    menu:
        "-Let her suck your dick-":
            m "Well if you insist [hermione_name]."
        "-Make her beg-":
            m "I don't think that you deserve to after calling it filthy and old."
            m "Perhaps if you asked nicely..."
            $ changeHermioneMainScreen(hg_pth+"body_44.png")
            her "Fine. Please let me suck your dick [genie_name]."
            m "Hmmm, I don't think that was sincere enough."
            $ changeHermioneMainScreen(hg_pth+"body_34.png")
            her "Please [genie_name], let me suck your big, thick dick. Pretty please."
            m "Much better."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "blowjob_ani"
    $ h_c_u_pic = "hand_ani"
    show screen chair_02
    show screen g_c_u
    
    hide screen hermione_blink #Hermione stands still.
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    show screen ctc
    with fade
    pause
    show screen bld1
    with d3
    $ hermione_main_zorder = 8
    ">As soon as you remove your cock from your robe Hermione is on top of you."
    $ changeHermioneMainScreen(hg_pth+"body_66.png", x_pos=390, y_pos= 235)    ###stop sucking
    $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_chibi_ypos = 10
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3      
    her "Do you have any idea how hard it was sitting \nthrough classes today?"
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3      
    her "*Slurp!* *Slurp!* *Slurp!*"    ###start sucking etc....
    $ changeHermioneMainScreen(hg_pth+"body_69.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3   
    her "Being this aroused."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gobble!* *Slurp!*"
    $ changeHermioneMainScreen(hg_pth+"body_68.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3   
    her "With no way to relieve myself."
    her "I tried everything."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Gobble!* *Slurp!* *Slurp!*"
    $ changeHermioneMainScreen(hg_pth+"body_64.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "I even masturbated in the girls bathroom."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    $ changeHermioneMainScreen(hg_pth+"body_79.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "But nothing worked."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gulp!* *Slurp!*"
    $ changeHermioneMainScreen(hg_pth+"body_78.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "All I could think about was the taste of your \nfilthy cum."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gulp!* *Gulp!*"
    m "My my, someone is becoming quite the slut wouldn't you say [hermione_name]"
    her "*Slurp!* *Gulp!* *Slurp!*"
    $ changeHermioneMainScreen(hg_pth+"body_65.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "You know why this is happening to me."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3  
    her "*Slurp!* *Slurp!* *Gulp!*"
    $ changeHermioneMainScreen(hg_pth+"body_64.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "Whatever was in that delicious potion you made \nme drink this morning."
    hide screen hermione_main
    m "Delicious? I thought you said it was just a bottle full of my cum?"
    m "Are you sure that you're just not a little slut who's become addicted to her Headmaster's semen?"
    $ changeHermioneMainScreen(hg_pth+"body_122.png", x_pos=390, y_pos= 235)
    her "I'm sure. There was something else in there."
    hide screen hermione_main
    m "Whatever you say [hermione_name]. Now if you want your reward you better get back to work."
    $ changeHermioneMainScreen(hg_pth+"body_129.png", x_pos=390, y_pos= 235)
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "..."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Slurp!* *Gulp!*"
    ">She is incredibly enthusiastic. You can feel your load building."
    menu:
        "-Cum down her throat-":
            m "Here it comes slut."
            ">Hermione quickly swallows the majority of your shaft. You can feel the tip of your head pressed against the entrance to her throat."
            m "You'll have to do better than that if you want your reward [hermione_name]."
            ">You place your hands on the back of her head pull her head into you."
            $ changeHermioneMainScreen(hg_pth+"body_32.png", x_pos=390, y_pos= 235)
            her "{size=+7}!!!{/size}"
            hide screen hermione_main
            ">The sensation of entering her throat sends you over the edge."
            m "Better start swallowing slut!"
            ">You start pumping your thick load directly into her stomach."
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            ">Hermione's eyes widen and tears form as she senses your semen enter her."
            $ changeHermioneMainScreen(hg_pth+"body_130.png", x_pos=390, y_pos= 235)
            her "hhaanooo hhhheerrr"
            hide screen hermione_main
            ">Her hands shoot down into her pants as she starts violently orgasming."
            ">The sight of her pleasuring herself as you use her throat only prolongs your orgasm."
            m "You dirty little girl. Getting off from your headmaster sticking his cock down your throat."
            m "I bet your loving this, being used as a nothing more than a toy."
            ">She says nothing but quickens the pace of her masturbation."
            ">You finally pull out of keen mouth with a satisfactory pop."
            $ changeHermioneMainScreen(hg_pth+"body_132.png", x_pos=390, y_pos= 235)
            her "It won't stop!"
            hide screen hermione_main
            m "What won't?"
            $ changeHermioneMainScreen(hg_pth+"body_117.png", x_pos=390, y_pos= 235)
            her "I-I can't stop cumming [genie_name]..."
            hide screen hermione_main
            ">The stimulation proves too much and she passes out."
            
        "-Cum in her mouth-":
            m "This is it girl. Get ready."
            ">Hermione starts swirling her tongue and focusing on the tip of your shaft."
            m "That's done it slut. Start swallowing."
            ">You explode into her mouth."
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            $ changeHermioneMainScreen(hg_pth+"body_125.png", x_pos=390, y_pos= 235)
            her "mmmmmmm *gulp* *gulp*"
            hide screen hermione_main
            ">Hermiones eyes go blank as she starts swallowing down your load."
            m "That's it, swallow it down like a good girl. You earned your prize."
            $ changeHermioneMainScreen(hg_pth+"body_126.png", x_pos=390, y_pos= 235)
            her "*gulp* *gulp* *gulp* *gulp*"
            hide screen hermione_main
            ">As she swallows you notice her legs start to convulse as she starts to orgasm."
            $ changeHermioneMainScreen(hg_pth+"body_125.png", x_pos=390, y_pos= 235)
            her "*gulp* *gulp* *gulp* "
            hide screen hermione_main
            ">You finally remove your shaft from her hungry mouth."
            m "Very good girl. Almost entirely clean... except for a bit of cum on the tip."
            m "I can't dirty my robes now can I? Better wipe this off."
            ">You wipe yourself clean on the tip of her nose."
            $ changeHermioneMainScreen(hg_pth+"body_126.png", x_pos=390, y_pos= 235)
            her "..."
            hide screen hermione_main
            m "There much better."
            ">Her legs have not stopped quivering since you first came."
            m "Well aren't you going to say anything [hermione_name]?"
            $ changeHermioneMainScreen(hg_pth+"body_133.png", x_pos=390, y_pos= 235)
            her "Thank you maste-"
            hide screen hermione_main
            ">She collapses into a heap on the ground with her legs still shaking."
        "-Cum on her face-":
            m "Get ready girl, here it comes."
            ">Hermione increases her efforts and starts focusing on the head of your penis."
            m "Not so quick [hermione_name]."
            show screen h_c_u
            hide screen g_c_u
            with d3 
            ">You quickly pull your penis out from her mouth."
            $ changeHermioneMainScreen(hg_pth+"body_48.png", x_pos=390, y_pos= 235)
            her "What are you doing [genie_name]?"
            hide screen hermione_main
            m "Giving you your well earned reward."
            $ g_c_u_pic = "cum_on_face_ani"
            hide screen h_c_u
            show screen g_c_u
            with d3 
            $ uni_sperm = True
            ">You start pumping your cock quickly and explode all over the young witch's face"
            m "Take it you filthy cum slut!"
            $ changeHermioneMainScreen(hg_pth+"body_121.png", x_pos=390, y_pos= 235)
            her "{size=+5}!!!{/size}"
            hide screen hermione_main
            ">Hermione immediately starts masturbating shamelessly in front of you."
            $ changeHermioneMainScreen(hg_pth+"body_117.png", x_pos=390, y_pos= 235)
            her "{size=+5}I'm cumming{/size}"
            hide screen hermione_main
            m "What was that [hermione_name]?"
            $ changeHermioneMainScreen(hg_pth+"body_130.png", x_pos=390, y_pos= 235)
            her "I-I'm cumming"
            hide screen hermione_main
            m "Just from a facial? What sort of cumslut have you become Miss Granger?"
            m "What would your parents think? Looking at you covered in some old mans cum."
            $ changeHermioneMainScreen(hg_pth+"body_34.png", x_pos=390, y_pos= 235)
            her "No. Please stop, I'll-"
            hide screen hermione_main
            m "They'd be ashamed at what you've become. A whore who gets off from being used as a toy."
            $ changeHermioneMainScreen(hg_pth+"body_32.png", x_pos=390, y_pos= 235)
            her "I-I'm cumming again [genie_name]. It won't stop..."
            hide screen hermione_main
            ">Hermione's voice trails off as she pass out from the over stimulation."
        "-Cum on the floor-":
            m "I'm cumming whore."
            $ changeHermioneMainScreen(hg_pth+"body_115.png", x_pos=390, y_pos= 235)
            her "mmmmmmmm"
            hide screen hermione_main
            ">She goes to bury her face into her crouch but you put your palm on her forehead and push her away."
            show screen h_c_u
            hide screen g_c_u
            with d3 
            $ changeHermioneMainScreen(hg_pth+"body_119.png", x_pos=390, y_pos= 235)
            her "[genie_name], what are you doing?"
            hide screen hermione_main
            m "giving you your reward"
            ">After a few quick pumps you point your dick at the floor and explode."
            $ changeHermioneMainScreen(hg_pth+"body_118.png", x_pos=390, y_pos= 235)
            her "PROFESSOR! Why would you waste that?"
            hide screen hermione_main
            m "It's not wasted [hermione_name], your reward is right there waiting for you."
            $ changeHermioneMainScreen(hg_pth+"body_117.png", x_pos=390, y_pos= 235)
            her "I'm not going to eat that. The floor in here is\n disgusting."
            hide screen hermione_main
            m "Well you can always wait until tomorrow morning then."
            $ changeHermioneMainScreen(hg_pth+"body_119.png", x_pos=390, y_pos= 235)
            her "TOMORROW MORNING!? I can't wait that long. \nCan't you just cum again?"
            hide screen hermione_main
            m "No [hermione_name], I'm a tired old man and it's time for me to go to sleep."
            m "You can either eat off the floor or you can come back tomorrow."
            $ changeHermioneMainScreen(hg_pth+"body_120.png", x_pos=390, y_pos= 235)
            her "...Fine"
            hide screen hermione_main
            ">She begrudgingly starts scooping your cum off the floor with her fingers."
            menu:
                "-Watch her-":
                    $ changeHermioneMainScreen(hg_pth+"body_125.png", x_pos=390, y_pos= 235)
                    ">She scoops up as much as she can into her palm \nand quickly moves it to her mouth."
                    pass
                "-Make her lick it up-":
                    m "Not with your fingers [hermione_name]."
                    $ changeHermioneMainScreen(hg_pth+"body_117.png", x_pos=390, y_pos= 235)
                    her "What do you mean not with my fingers? How \nelse am I supposed to eat it?"
                    hide screen hermione_main
                    m "You have a perfectly good tongue, I suggest that you put it to use."
                    $ changeHermioneMainScreen(hg_pth+"body_118.png", x_pos=390, y_pos= 235)
                    her "You expect me to LICK your old cum off the \nfloor?"
                    hide screen hermione_main
                    m "I do. Unless of course you would prefer to go back to your room hungry and unsatisfied."
                    $ changeHermioneMainScreen(hg_pth+"body_117.png", x_pos=390, y_pos= 235)
                    her "..."
                    hide screen hermione_main
                    ">She bends over with her head to the floor."
                    $ aftersperm = True
                    $ changeHermioneMainScreen(hg_pth+"body_116.png", x_pos=390, y_pos= 235)
                    her "(This is so degrading)"
                    hide screen hermione_main
                    ">She puts her tongue out licks your cum."
            ">The effect is instantaneous."
            $ aftersperm = True
            $ changeHermioneMainScreen(hg_pth+"body_126.png", x_pos=390, y_pos= 235)
            her "I-I'm cumming." #small text
            hide screen hermione_main
            m "What was that?"
            $ changeHermioneMainScreen(hg_pth+"body_133.png", x_pos=390, y_pos= 235)
            her "I'm cumming!"
            hide screen hermione_main
            ">Hermione's hand shoots under her skirt as she starts violently orgasming."
            $ changeHermioneMainScreen(hg_pth+"body_134.png", x_pos=390, y_pos= 235)
            her "What's wrong with me [genie_name]?"
            hide screen hermione_main
            m "A lot of things [hermione_name], considering you just ate my cum off the ground."
            $ changeHermioneMainScreen(hg_pth+"body_139.png", x_pos=390, y_pos= 235)
            her "I can't stop cumming..."
            hide screen hermione_main
            ">Hermione loses conciousness."
    hide screen bld1
    hide screen hermione_main
    ">Hermione is in an unconscious heap on the floor."
    menu:
        "-Carry her back to her room as is-":   
            ">You pick her limp body up and carry her to her room."
            ">As you enter the dormitory you hear her talk in her sleep."
            $ changeHermioneMainScreen(hg_pth+"body_131.png", x_pos=390, y_pos= 235)
            her "Of course I swallow... just form a line..."
            hide screen hermione_main
            ">You place her carefully back into her bed."
            m "Sleep tight slut."
        "-Clean her up and take her back to her room-":   
            $ uni_sperm = False
            ">You pick her limp body up and carry her to her room."
            ">As you enter the dormitory you hear her mumble in her sleep."
            $ changeHermioneMainScreen(hg_pth+"body_127.png", x_pos=390, y_pos= 235)
            her "You want a kiss [genie_name]? Of course I don't mind..."
            hide screen hermione_main
            ">You place her carefully back into her bed."
            m "Sleep tight Hermione."
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    hide screen blkfade
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    $ addicted = False
    $ uni_sperm = False
    $ aftersperm = False
    with Dissolve(.3)
    $ hermione_main_zorder = 5
    $ hermione_sleeping = True
    hide screen hermione_main

    jump night_main_menu
        
label potion_scene_4: #Transparent uniform
    m "[hermione_name], I have another potion for you."
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    her "I'm not sure that I like these potions [genie_name]."
    $ changeHermioneMainScreen(hg_pth+"body_09.png")
    her "Especially after the time you tried to turn me into a cat."
    m "To be fair I was trying to turn you into another girl..."
    $ changeHermioneMainScreen(hg_pth+"body_05.png")
    her "That's not much better [genie_name]."
    m "Isn't it?"
    $ changeHermioneMainScreen(hg_pth+"body_04.png")
    her "Well at least promise me that this one isn't going to embarrass me in the middle of class."
    $ changeHermioneMainScreen(hg_pth+"body_12.png")
    her "My reputation is suffering enough as it is. I don't need these constant potions causing me to transform in front of my peers."
    m "I promise that this potion won't affect your body in any way."
    $ changeHermioneMainScreen(hg_pth+"body_05.png")
    her "Well then what on earth is it going to do?"
    m "As always [hermione_name], you'll ha-"
    $ changeHermioneMainScreen(hg_pth+"body_07.png")
    her "Have to wait and see. I know."
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione quickly drinks the potion."      #new
    $ changeHermioneMainScreen(hg_pth+"body_04.png")
    hide screen ch_potion
    show screen hermione_blink
    her "Can I go now?"
    m "Yes you may. 20 points to Gryffindor"
    $ changeHermioneMainScreen(hg_pth+"body_16.png")
    her "Thank you [genie_name]."
    
    $ gryffindor += 20
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_takes_classes = True
    if whoring <= 7:
        $ transparency = 0.8
    elif whoring <= 13:
        $ transparency = 0.6
    elif whoring <= 20:
        $ transparency = 0.4
    else:
        $ transparency = 0.2
    jump day_main_menu

label potion_scene_4_2: #Scene where Hermione comes back after classes angry and confused at having her uniform made transparent
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    if whoring <= 7: #Very angry and embarrassed
        ">Hermione bursts into your office."
        $ changeHermioneMainScreen(hg_pth+"body_22.png")        ###Could add more tears if desired
        her "How could you [genie_name]!"
        $ changeHermioneMainScreen(hg_pth+"body_21.png")
        her "I am the laughing stock of the entire school!"
        $ changeHermioneMainScreen(hg_pth+"body_20.png")
        her "Now everyone knows what I look like naked!"
        m "Tell me about what happened."
        $ changeHermioneMainScreen(hg_pth+"body_21.png")
        her "Tell you about what happened? I'm never speaking to you again."
        $ mad += 20
        $ transparency = 1
    elif whoring <= 13: #Mildly aggravated
        ">Hermione comes into your office quickly without knocking."
        $ changeHermioneMainScreen(hg_pth+"body_34.png")
        her "Again?"
        m "What's this about [hermione_name]?"
        $ changeHermioneMainScreen(hg_pth+"body_31.png")
        her "Why would you make my clothes invisible again?"
        m "Why not?"
        $ changeHermioneMainScreen(hg_pth+"body_29.png")
        her "Ugh, you're such a pig."
        m "Tell me about what happened."
        $ changeHermioneMainScreen(hg_pth+"body_33.png")
        her "..."
        $ changeHermioneMainScreen(hg_pth+"body_31.png")
        her "Fine, but I expect an extra 10 points."
        m "As you wish."
        $ changeHermioneMainScreen(hg_pth+"body_66.png")
        her "Well I started off with potions class as usual when I started to feel like all eyes were on me."
        m "I wonder why."
        $ changeHermioneMainScreen(hg_pth+"body_69.png")
        her "As I was saying I was completing potions class and felt like everyone wouldn't take their eyes off of me."
        $ changeHermioneMainScreen(hg_pth+"body_79.png")
        her "I didn't think anything of it until I was approached by Professor Snape at the end of the lesson."
        $ changeHermioneMainScreen(hg_pth+"body_29.png")
        her "He normally criticises me during potions class. Stuff like getting dosages wrong, things that I know are correct."
        m "Back to the story [hermione_name]."
        $ changeHermioneMainScreen(hg_pth+"body_66.png")
        her "Well when he commented that he liked my outfit I was suspicious. I thought that perhaps he was talking about my shirt until I looked down and saw that everything was see through."
        $ changeHermioneMainScreen(hg_pth+"body_69.png")
        her "But I just ignored him, finished class and ran here."
        m "You just finished class?"
        $ changeHermioneMainScreen(hg_pth+"body_79.png")
        her "Of course, I can't afford to miss potions class. I'm doing poorly enough without missing class."
        m "Well fair enough. You may go now."
        $ changeHermioneMainScreen(hg_pth+"body_29.png")
        her "Hmmph. Goodbye [genie_name]."

    elif whoring <= 20: #Slightly aroused
        ">Hermione enters your office"
        $ changeHermioneMainScreen(hg_pth+"body_08.png")
        her "Can you at least warn me next time?"
        m "Well, that'd take away from the suspense wouldn't it?"
        $ changeHermioneMainScreen(hg_pth+"body_10.png")
        her "Hmmmm, well at least ask what I'm doing before you give me the potion."
        m "Why, what did you have to do today that was so important?"
        $ changeHermioneMainScreen(hg_pth+"body_28.png")
        her "I had to give a speech for languages!"
        $ changeHermioneMainScreen(hg_pth+"body_16.png")
        her "Do you have any idea how inappropriate it was giving a speech on morality in front of the entire class-"
        $ changeHermioneMainScreen(hg_pth+"body_28.png")
        her "{size=+5}As my clothes became transparent!{/size}"
        m "Well I imagine it depends on what side of morality you were arguing."
        $ changeHermioneMainScreen(hg_pth+"body_16.png")
        her "It doesn't matter."
        m "Are you sure that you didn't enjoy it?"
        $ changeHermioneMainScreen(hg_pth+"body_17.png")
        her "How could I. I had to stand there as my friends and peers all saw me naked."
        m "You finished your speech?"
        $ changeHermioneMainScreen(hg_pth+"body_15.png")
        her "Certainly, I had to make sure that everyone knew my views on morality."
        m "Well I'm sure they have a crystal clear view of it now."
        $ changeHermioneMainScreen(hg_pth+"body_12.png")
        her "Hmmph, are you done?"
        m "Yes, you may go now."
        $ changeHermioneMainScreen(hg_pth+"body_02.png")
        her "Good bye [genie_name]."
    else: #Highly aroused (doesn't even acknowledge that her clothes are see-through)
        ">Hermione enters the office casually."
        m "Hello [hermione_name], how was your day today?"
        $ changeHermioneMainScreen(hg_pth+"body_06.png")
        her "Fine [genie_name]. Why do you ask?"
        m "No reason. Anything unusual happen today?"
        $ changeHermioneMainScreen(hg_pth+"body_10.png")
        her "Hmmmm, now that you mention it I suppose that boys in class were a little more forward than usual."
        m "How so?"
        $ changeHermioneMainScreen(hg_pth+"body_13.png")
        her "Well nothing serious, just small stuff like calling me names, groping me."
        m "Groping you? What on earth could have provoked them to do that?"
        $ changeHermioneMainScreen(hg_pth+"body_45.png")
        her "I don't know [genie_name]. I can't imagine any reason that I would be attracting attention today..."
        m "You're getting off on this aren't you?"
        $ changeHermioneMainScreen(hg_pth+"body_46.png")
        her "..."
        $ changeHermioneMainScreen(hg_pth+"body_121.png")
        her "I've never been so turned on in my life. Having all eyes on me. Having every boy imagine doing unspeakable things to me."
        $ changeHermioneMainScreen(hg_pth+"body_124.png")
        her "Snape made me stand out the front of class after I talked back to him."
        $ changeHermioneMainScreen(hg_pth+"body_123.png")
        her "I think that I orgasmed just from the looks people gave me."
        m "Well done [hermione_name]. You're becoming quite the slut."
        $ changeHermioneMainScreen(hg_pth+"body_128.png")
        her "Thank you [genie_name]. Is that all?"
        m "Yes, you can go now slut."
        $ changeHermioneMainScreen(hg_pth+"body_46.png")
        her "{image=textheart}"#lovehearts ""
    $ transparency = 1
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_sleeping = True
    jump night_main_menu
        
label potion_scene_5: #Lamia potion
    $ changeHermioneMainScreen(hg_pth+"body_32.png")
    her "That's dumb."
    m "I literally don't know."
    jump day_main_menu

label potion_scene_6: #Luna potion
    m "Might I offer you a drink?"
    $ changeHermioneMainScreen(hg_pth+"body_03.png")
    her "You're not trying to get me drunk on Butterbeer again are you?"
    m "Nothing of the sort, just a harmless little potion."
    ">You hand her the potion bottle."
    $ changeHermioneMainScreen(hg_pth+"body_08.png")
    her "Another of your mysterious potions?"
    her "Let me guess, you won't tell me what it does and I'll embarrass myself in front of the whole class?"
    m "Not at all."
    $ changeHermioneMainScreen(hg_pth+"body_17.png")
    her "That's new."
    her "... and somehow worrying"
    her "So what exactly is it then?"
    m "It's your regular, run-off-the-mill Polyjuice Potion."
    $ changeHermioneMainScreen(hg_pth+"body_33.png")
    her "Ugh. Those taste like muck."
    her "... and what'll it turn me into?"
    m "That, Miss Granger, is a secret."
    $ changeHermioneMainScreen(hg_pth+"body_23.png")
    her "Typical."
    m "It'll taste a lot sweeter if you imagine all the points you'll earn for Gryffindor."
    m "How much of a lead did Slytherin have on you again?"
    her "You're right [genie_name]. I can't let Gryffindor down!"
    ">She downs the thick potion."
    $ changeHermioneMainScreen(hg_pth+"body_43.png")
    her "Blehgh."
    her "I was wrong, not muck. Snot. It's as thick as Trollsnot."
    m "As long as you keep it down, you'll earn Gryffindor a great deal of points."
    her "And I will."
    $ changeHermioneMainScreen(hg_pth+"body_44.png")
    her "So what now? I just go to class?"
    m "Not yet, tell me something about yourself."
    $ changeHermioneMainScreen(hg_pth+"body_16.png")
    her "Well, ever since I started my \"Extracurricular activities\" with you my attendance and grades have started slipping."
    m "Troubling indeed."

    if whoring <= 13:
        $ changeHermioneMainScreen(hg_pth+"body_30.png")
        her "It is! [genie_name], I used to be at the top of the class. My scores were impeccable. "
        m "And how are your scores now?"
        $ changeHermioneMainScreen(hg_pth+"body_12.png")
        her "Well I'm still at the top... Just not by as much."
        m "Well, there are times when academic excellence shouldn't be your primary concern."
        $ changeHermioneMainScreen(hg_pth+"body_17.png")
        her "Hmmph, and what /should/ be my primary concern then?"
        m "Currently. I'd say your face is pretty high on the list"
        $ changeHermioneMainScreen(hg_pth+"body_35.png")
        her "Excuse me. That is hardly appropriate for a headmaster."
        m "No, I'm serious. You should really see the look on your face."

    else:
        $ changeHermioneMainScreen(hg_pth+"body_06.png")
        her "Not really. I realize there are other things I can excel in."
        m "Like sucking cocks for house-points"
        $ changeHermioneMainScreen(hg_pth+"body_30.png")
        her "Professor!"
        m "Oh don't be so modest. If sucking dick was a class, you'd be Magna Cum Laude."
        $ changeHermioneMainScreen(hg_pth+"body_30.png")
        her "Thank you professor. You know, there's time to earn some more points before class. If you're feeling generous I could..."
        m "I'd have to know on whose face I'll be cumming though "
        $ changeHermioneMainScreen(hg_pth+"body_30.png")
        her "What do you mean? ...My face of course... I mean ...*urp*"
        m "Maybe you should check the mirror"
    "*POOF*"
    hide screen hermione_main
    hide screen hermione_blink
    $ luna_chibi("stand")
    $ changeLuna(1, 1, 4, 1)
    her "Ughhh... I feel like I'm going to throw up! Did the Polyjuice work??"
    m "Like a charm."
    ">Hermione starts examining herself, feeling out her outfit and pausing at her breasts." 
    $ changeLuna(5, 1, 5, 1)
    her "Apparently I'm still a girl. Someone from Ravenclaw?"
    m "Keen powers of observation, Miss Granger"
    ">Hermione grabs a lock of her hair"
    $ changeLuna(1, 7, 1, 4)
    her "Definitely a blonde, though she could absolutely use a comb"
    $ changeLuna(1, 5, 1, 1)
    ">Suddenly Hermione feels something stuck in the mess of blonde. On closer examination it appears to be a wand."
    $ changeLuna(4, 1, 3, 1)
    her "..."
    her "You turned me into Loony Lovegood... I mean Luna Lovegood!?!"
    m "Very astute [hermione_name]."
    m "(No idea who that is, but she looks good.)"
    $ changeLuna(4, 1, 3, 17)
    her "Why on earth would you want me to look like Luna? She's completely mental!"
    m "I'm not seeing anything really wrong with her."
    $ changeLuna(1, 1, 4, 4)
    her "She has... imaginary friends and believes in things that can't possibly exist [genie_name]. She is absolutely mad."
    m "Fortunately, I'm not really interested in her mental health. I am interested in her impressive, and quite real, chest."
    $ changeLuna(5, 1, 5, 3)
    her "You can't possibly be interested in that... that girl's paltry breasts."
    m "Currently they're yours. And they don't look so paltry from where I'm sitting [hermione_name]. Do I detect a hint of jealousy?"
    $ changeLuna(1, 1, 3, 3)
    her "Not at all, I suppose it is only natural that someone of your advanced age has trouble with their eyesight."
    m "(definitely struck a nerve there.) Is that any way to talk to your elders, [hermione_name]? Perhaps you need a good spanking to remind you of your manners. We old people are good at giving those."
    $ changeLuna(1, 1, 4, 9)
    her "I..I apologize [genie_name]. I don't know what came over me."
    m "Apology accepted. I'm sure they can't hold a candle to the brilliance of your boobs."
    $ changeLuna(1, 2, 1, 4)
    her "I'd like to think I'm more than just a pair of breasts... but thank you [genie_name]. That was flattering. In a way."
    m "If you want to dispel all doubt, we could compare. Why don't you lift your shirt and show me what you... err... She's got under that sweater."
    $ changeLuna(4, 2, 3, 4)
    her "I'm still not entirely comfortable with this..."
    ">Hermione quickly strips off her Ravenclaw top, followed by her bra."
    hide screen luna
    $ luna_chibi("stand_topless")
    $ luna_wear_top = False
    $ luna_wear_bra = False
    $ changeLuna(5, 2, 5, 3)
    her "There, see. Perfectly ordinary breasts. Absolutely no need to keep looking at them."
    m "I'm not quite convinced, the soft pale skin, the cute pink nipples and they look like quite a handful. I think you might have some serious competition here [hermione_name]."
    $ changeLuna(5, 1, 3, 17)
    her "You can't be serious! They're saggy and couldn't even fill a first-year's palm!"
    m "Hmmm, I'm not sure. I think a closer examination is required."
    ">In a huff, Hermione walks over and presents her new set of breasts"
    m "Yes yes, upon closer inspection it seems I was wrong. Luna's breasts are indeed second to your own."
    $ changeLuna(5, 1, 3, 4)
    her "I'm glad you came to your senses. Thank you, If you're completely satisfied, I'll cover these hideous things up now."
    m "Completely [hermione_name]. 20 points to Gryffindor."
    hide screen luna
    $ luna_chibi("stand")
    $ luna_wear_top = True
    $ luna_wear_bra = True
    $ changeLuna(3, 1, 1, 1)
    her "Well I best be off to classes."
    m "You're going to class looking like a fellow classmate?"
    $ changeLuna(1, 1, 5, 1)
    her "It's not going to be a problem. Luna's barely in class as it is, I can just pretend to be her. Maybe I'll even improve her test scores. You'll notify the teachers I can't attend class right?"
    m "Absolutely. (Not a chance.) But, what if you bump into her in the halls?"
    $ changeLuna(5, 1, 1, 4)
    her "Believe me [genie_name], Luna will probably think I'm some kind of Wrackspurt that's messing with her head."
    hide screen bld1
    hide screen blkfade
    hide screen luna
    $ menu_x = 0.5 
    $ hermione_takes_classes = True
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen luna_chibi
    with d3
    $ luna_known = True
    jump day_main_menu

    