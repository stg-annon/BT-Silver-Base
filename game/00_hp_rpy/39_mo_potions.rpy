###POTION SCENES
label potion_scene_1: #catears (keep in mind Genie is trying to transform her into another girl)
    m "[hermione_name]?"
    call her_main("Yes, [genie_name]?","body_01")
    m "Today I have a new type of favour for you to perform."
    call her_main("What do you mean new? What do I have to do?","body_07")
    m "It's quite simple, today you will be drinking a potion"
    call her_main("Is that it? How much will I get paid?","body_08")
    m "20 points."
    call her_main("Hmmm, what type of potion is it?","body_17")
    call her_main("Polyjuice? Amortentia? Babbling Beverage? Felix Felicis?","body_24")
    m "That's a secret [hermione_name]."
    call her_main("...","body_73")
    m "Well [hermione_name], what do you say? Will you drink a harmless little potion?"
    m "For Gyrffindor?"
    call her_main("Fine...","body_16")
    ">Hermione takes a whiff of the thick potion."
    call her_main("This smells disgusting. Like mud and wet dog fur.","body_43")
    call her_main("Do I really have to drink this?","body_11")
    m "You do. I suggest holding your nose if the smell is too much."
    call her_main("For Gryffindor.","body_20")
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione holds her nose and quickly downs the flask."
    call her_main("","body_42")
    pause
    call her_main("","body_22")
    hide screen ch_potion
    show screen hermione_blink
    her "Ughhh. That was horrible."
    m "Well done."
    call her_main("Now will you at least tell me what this potion does.","body_21")
    m "It should be noticeable any second now..."
    call her_main("Well? Is it supposed to make my breasts bigger? They don't feel any bigger.","body_73")
    m "No. Hmmmm, it mustn't have worked."
    call her_main("What was it supposed to do?","body_70")
    m "There's no point in telling you now. It was going to be a surprise."
    m "Damn Twins must've conned me."
    call her_main("Is that all [genie_name]?","body_15")
    m "Yes, [hermione_name], 20 points to Gryffindor."
    call her_main("Thank you [genie_name].","body_06")
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
    $ hermione_takes_classes = True
    jump day_main_menu

label potion_scene_1_2: #Scene where Hermione comes back after classes angry and confused at being given cat ears and a tail.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    call her_main("How could you do this to me [genie_name]?","body_05")
    her "Try and turn me into a cat!"
    call her_main("In the middle of class!","body_29")
    m "I didn't try and turn you into a cat [hermione_name]."
    call her_main("Then why do I have ears and a tail?","body_30")
    m "I have no idea. The potion I gave you was supposed to turn you into a different girl."
    call her_main("What!? You didn't use polyjuice potion did you [genie_name]?","body_48")
    m "What's that?"
    call her_main("There's no point playing dumb [genie_name].","body_79")
    call her_main("Well at least I know that it will wear off by morning.","body_69")
    menu:
        "-Let her go-":
            m "Goodnight [hermione_name]."
            call her_main("Goodnight [genie_name].","body_120")
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
    call her_main("75 points? How?","body_17")
    m "By sucking my cock."
    call her_main("Like this? I look like a cat! Why would you ask me at a time like this?","body_119")
    call her_main("You're not some sort of pervert who likes animals are you?","body_117")
    m "Of course not, I just think that you have a very unique look at the moment and that it would be a shame not to do anything with it."
    call her_main("Fine, just promise me you aren't going to do anything weird.","body_120")
    m "I promise. Now, kneel."
    ">Hermione walks over and kneels before you."
    m "Good girl."
    call her_main("...","body_115")
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
    $ hermione_SC.chibi.xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_SC.chibi.ypos = 10
    $ h_c_u_pic = "hand_ani"
    show screen h_c_u
    hide screen g_c_u
    with d3
    $ hermione_main_zorder = 8
    call her_main("It's because of your stupid potion, it's \nmade my tongue all rough.","body_116")
    call her_main("Do you want to stop?","body_68")
    hide screen hermione_main
    m "No, keep going, just try not to focus on the tongue work too much."
    call her_main("Yes [genie_name].","body_69")
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
    call her_main("Of course [genie_name].","body_128")     
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
    call her_main("I can't help it [genie_name], whenever \nanything touches my ears I just purr.","body_74")
    hide screen hermione_main
    m "It feels amazing, now cock back in the mouth girl."
    call her_main("Yes [genie_name].","body_80")
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
    call her_main("","body_125")
    pause .1
    call her_main("*gulp* *Purr* *Purr*","body_126")
    call her_main("","body_125")
    pause .1
    call her_main("*gulp* *Purr* *gulp*","body_126")
    call her_main("","body_125")
    pause .1
    call her_main("*Purr* *gulp* *gulp*","body_126")
    ">You pull your cock out of her purring mouth."
    show screen h_c_u
    hide screen g_c_u
    call her_main("Mmmmm, it might be this potion but that tasted \ngood...","body_128")
    hide screen hermione_main
    m "Well, you certainly earned your 75 points."
    $ gryffindor += 75
    $ h_c_u_pic = "hand_ani"
    call her_main("Thank you [genie_name]. Will that be all.","body_78")
    hide screen hermione_main
    m "One last thing."
    m "Who's a good girl?"
    call her_main("..........","body_29")
    call her_main("I am...","body_46")

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
    $ hermione_SC.chibi.ypos = 250
    jump night_main_menu
    
    
label potion_scene_2_1: #breast expansion - Until chibis are added for it tifucking won't be written (ayylmao)
    m "Guess what I have for you today."
    call her_main("Is it another foul tasting potion that will try transform me into a hideous animal?","body_04")
    m "Well I mean this one smells nice."
    call her_main("Will it taste nice though?","body_02")
    m "Only one way to find out."
    ">You hand her the potion and she brings it up to her nose."
    call her_main("Well you're right, it does smell good. Let's find out if it tastes good...","body_06")
    hide screen hermione_blink
    show screen ch_potion
    ">She drinks the potion at a leisurely pace."
    call her_main("Ahhh.","body_74")
    call her_main("","body_64")
    show screen hermione_blink
    hide screen ch_potion
    her "That wasn't actually that bad."
    call her_main("So, now that I've had the potion, will you tell me what it's supposed to do.","body_122")
    m "No need to ruin the fun, it should take effect relatively quickly."
    call her_main("Well what am I supposed to do until then?","body_128")
    m "You could show me your tits."
    call her_main("I don't think so [genie_name], you're only paying me for drinking the potion.","body_127")
    call her_main("If you expect to see me without my shirt on then you'll have to try a little harder.","body_129")
    m "Oh I wouldn't be so sure of that."
    call her_main("So is that what it does? Makes me show you my breasts? Is it some sort of mind control potion?","body_45")
    m "Mind control? Where's the fun in that? No, this is something much more entertaining."
    call her_main("Well it better happen soon otherwise I'm lea-","body_69")
    ">You notice her breasts start to expand ever so slightly." ###Start using facial expressions mixed with Captain Nemo art
    call her_main("...","body_79")
    call her_main("As I said, something better happen soon or I'm leaving.","body_29")
    m "I wouldn't worry about it, from the looks of it, it's already started."
    call her_main("Why, what's wrong with me?","body_31")
    m "There's nothing wrong with you. If anything, it's an improvement."
    call her_main("What is?","body_79")
    ">She starts patting down her body. Checking to see if she has grown any new ears or a tail."
    call her_main("I don't see what you could be...","body_87")
    ">She grabs her breasts to check them."
    call her_main("!!!","body_118")
    call her_main("Have my breasts gotten bigger?","body_119")
    m "About time you noticed."
    call her_main("Why would you make my breasts bigger? They're already big enough!","body_117")
    m "You know what they say, can't have too much of a good thing."
    call her_main("It's the other way around [genie_name].","body_79")
    m "Is it? Well I prefer my version."
    call her_main("Well how big are they supposed to-","body_118")
    ">Her breast swell up again."
    call her_main("You can't be serious. At this rate they're going to rip my shirt.","body_119")
    m "Well they should stop there."
    call her_main("Good, they're big enough as is.","body_47")
    menu:
        "-Send her to class-":
            m "You're right, I suppose they are big enough."
            m "Well that's all for today, 20 points to Gryffindor."
            call her_main("That's all? You're not going to make me do something else?","body_48")
            m "Why would I, I asked you to drink a potion and you drank it. You're free to leave."
            call her_main("Thank you [genie_name], I'll head back to my room.","body_46")
            m "Room? It's time for class [hermione_name]. What do you think Professor Snape will say once he hears that you skipped class?"
            call her_main("Well I can't be expected to go like this.","body_66")
            m "Why not? Everything is covered."
            call her_main("Barely. And what will people think of me.","body_118")
            m "Just tell them that you are still developing. I'm sure that they're used to enormous breasts anyway, what's a few extra sizes."
            call her_main("...Fine. Just promise me that they won't get any bigger.","body_120")
            m "I can't promise that, your still in school. A lot of girls don't stop growing until their 30."
            call her_main("You know what I mean [genie_name].","body_86")
            m "I'm afraid that I don't [hermione_name], now you'd best hurry if you don't want to be late."
            call her_main("...Yes [genie_name].","body_79")
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
    call her_main("I want an extra 40.","body_79")
    m "I haven't even told you what I want to-"
    call her_main("If you want to touch my breasts it will be an extra 40 points.","body_69")
    m "Deal."
    ">Hermione walks over to behind your desk, her breasts swaying rhythmically as she moves."
    show screen blkfade
    hide screen hermione_blink #Stands with tits out.
    hide screen genie
    show screen groping_naked_tits
    with d1
    with d5
    hide screen blkfade
    call her_main("Well...","body_44")
    ">You reach out and grab her breasts through her stretched shirt."
    call her_main("!!!","body_119")
    call her_main("Please be gentle [genie_name]. They seem to be much more sensitve than usual, it must be the potion.","body_117")
    m "Well I'll take that into account..."
    ">You take a breast in each hand and start kneading them with your fingers."
    call her_main("...","body_127")
    m "They're certainly much larger than usual."
    call her_main("...yes","body_121")
    ">You continue massaging them gently through her shirt. Pulling them apart and then pressing them into one another."
    call her_main("...It feels like they're getting-","body_118")
    call h_action("expand_breasts")
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png" 
    $ custom_outfit_old = 20
    "*RIIIP*"
    call her_main("!!!","body_119")
    call her_main("You said that they wouldn't get any bigger! Now look, my shirt has been ruined.","body_86")
    m "Don't worry about that [hermione_name], worry about earning your 40 points."
    call her_main("Just hurry up.","body_79")
    menu: #Will add titfuck here
        #"-Suck her nipples-":
            #"asd"
        "-Titfuck her-":
            m "Well come here then!"
            hide screen groping_naked_tits
            $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_xlarge.png"
            jump start_titfuck
        "-Play with her nipples-":
            pass
    ">You take her exposed breasts back into your hands and continue massaging"
    call her_main("sir... they seem to have become more sensitive...","body_78")
    call her_main("Please don't do anything sudden.","body_121")
    m "Like this?"
    ">You take both nipple between your thumb and index finger."
    call her_main("!!!","body_130")
    call her_main("Please stop... it's too much, it's like my nipples are on fire.","body_132")
    m "Shhhh, just be still, it'll all be over soon."
    ">You start rolling her nipples in between your fingers."
    call her_main("...","body_131")
    ">You feel her push her crotch against your thigh."
    m "Feeling a little aroused are we?"
    ">You start to pinch and pull her nipples."
    call her_main("Ohhh","body_121")
    ">She starts grinding herself against your thigh"
    m "Well, well, well, you are sensitive now aren't you? Trying to grind out an orgasm on your headmasters leg, how shameless."
    call her_main("...","body_123")
    m "Well let's see if we can do something about that."
    ">You start alternating pinching and pulling her nipples hard, pulling the nipples out as far as you can and then pushing them back into her breast."
    call her_main("!!!","body_130")
    her "I-I-I'm cumming!"
    ">She starts grinding hard against your leg as a wet spot starts to form on her skirt."
    m "What a naughty little girl."
    ">She breathes heavily as she rests against you"
    call her_main("Will... that be all [genie_name]?","body_121")
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
    $ h_action_show_top = False
    $ h_action_show_bra = False
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_takes_classes = True
    jump day_main_menu



label potion_scene_2_1_2: #Hermione comes back after having her breasts expand in class


label potion_scene_2_2: #ass expansion
    m "[hermione_name], I have another potion for you to try today."
    call her_main("Another one? Where are you getting these?","body_08")
    m "That's of no concern to you. What should concern you is the 20 points that you are able to earn should you drink it."
    call her_main("...Fine, give me the bottle.","body_07")
    ">She takes a quizzical smell of the bottle."
    call her_main("At least this one smells good.","body_06")
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">She drinks the whole potion over a series of gulps."
    hide screen ch_potion
    with d3
    show screen hermione_blink
    call her_main("Ahhh, that was good! So what was it?","body_24")
    m "The effects should be visible soon enough."
    call her_main("Well can you at least give me a hint?","body_14")
    m "Let's just say that it's a redistribution of ass{w}ets." ###Added {w} instead of your ...
    call her_main("What do you mean by--","body_12")
    ">Hermione goes white as she starts to feel her body churn."
    call her_main("What's going on. It feels like my insides are moving.","body_18")
    call her_main("And my ass, it feels so... good.","body_121")
    ">You start to notice her ass increase in size."    ###Use bigger butt from Captain Nemo
    call her_main("It feels too sensitive... I have to take my skirt off","body_119") ###changed so to too
    
    hide screen hermione_main
    show screen blktone 
    show screen ctc
    with d3
    call h_action("expand_ass")
    call her_main("","body_118",xpos=140,ypos=0)
    
    pause
    
    call her_main("ughhh, has it gotten bigger?","body_118")
    call her_main("Is that what this potion's supposed to do? Makes my ass bigger?","body_120")
    m "Evidently."
    call her_main("Why does my ass feel so good?","body_121") ###new
    ">Hermione keeps rubbing her ass, rolling her fingers across her expanded buttocks."
    m "Hmmm, it's not supposed to, but I guess every case is different."
    call her_main("It's just so sensitive... [genie_name] do you think that you could... massage me?","body_123")
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
    call her_main("Please [genie_name]... please take advantage of me...","body_131")
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
            call her_main("!!!","body_132")
            call her_main("[genie_name] please... I'm too sensitive. If you do that, \nI'm not sure I'll be able to control myself.","body_121")
            hide screen hermione_main
            m "Well in that case..."
            ">You slowly pull your finger away from her asshole."
            call her_main("Thank yo-","body_121")
            ">And then fully insert it."
            call her_main("...","body_119")
            her "..."
            her "..."
            call her_main("{size=-10}I'm cumming{/size}","body_130")
            hide screen hermione_main
            m "What was that?"
            ">You start turning your finger."
            call her_main("{size=+10}I'm cumming!{/size}","body_32")
            ">Her asshole starts quivering around your finger."
            hide screen hermione_main
            m "What a little anal slut. I wonder what you'll do once I try this."
            ">You start pumping your finger in and out of her shivering asshole."
            call her_main("!!!","body_132")
            call her_main("I'm cumming again!","body_131")
            m "So soon?"
            call her_main("I can't stop! Please [genie_name], please, no more!","body_119")
            menu:
                "-Stop-":
                    m "Well, I suppose that's enough for now..."
                    ">You pull your finger out of her asshole and she immediately slumps over your desk."
                    call her_main("That was... great...","body_123")
                    ">She lies on your desk, breathing heavily."
                "-Keep Going-":
                    m "What was that [hermione_name]? It almost sounded like you asked me to stop."     ###Or would it be better if she start to tear up and cry a bit?
                    ">You increase the pace."
                    call her_main("Please...","body_131")
                    m "Please what?"
                    ">You insert a second finger."
                    call her_main("Please... stop... you'll break me...","body_118")
                    ">You grab her hip with one hand and keep finger fucking her asshole."
                    call her_main("...","body_132")
                    call her_main("...","body_32")
                    ">You feel her body go limp as her asshole relentlessly quivers around your fingers."
                    m "There, wasn't that nice?"
                    ">You slow down and pull out of her asshole."
                    call her_main("...yeeess...[genie_name]...","body_123")
                    m "Good girl."
            m "Well you best be off to class."
            call her_main("...With my butt looking like this?","body_118")
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
            $ hermione_SC.chibi.xpos = 400 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            show screen bld1
            hide screen blkfade
            with Dissolve(1)
            call her_main("Yes [genie_name].","body_124")
            m "Oh I almost forgot, 20 points to Gryffindor!"
            $ gryffindor += 20
            call her_main("Oh... right, the points. Thank you.","body_123")
            ">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it."
            $ custom_skirt = 0
            $ h_action_show_skirt = True
            call her_main("...","body_87")
        "-Hot dog her-" if whoring >= 17:
            m "Bend over [hermione_name]."
            ">Before she even has a chance to react you push her forward over your desk."
            hide screen hermione_main
            hide screen groping_02
            with d3
            show screen ch_hotdog
            call her_main("!!!","body_119")
            call her_main("What are you going to do [genie_name]?","body_122")
            hide screen hermione_main
            m "Well seeing as how your ass has become so fucking huge I thought I may as well put it to good use."
            ">You pull you cock out from your robes and place it on top of her ass crack."
            call her_main("Your not going to fuck my asshole are you [genie_name]?","body_123")
            hide screen hermione_main
            m "Not your asshole, [hermione_name], I intend to fuck your entire ass!"
            ">You grab a firm hold of her cheeks and pull them apart, allowing your shaft to rest in between, on top of her asshole."
            m "A perfect fit wouldn't you say?"
            call her_main("What do you-","body_117")
            hide screen hermione_main
            ">You squeeze her ass-cheeks back together around your cock and start pumping in between them."
            call her_main("!!!","body_136")
            hide screen hermione_main
            m "Fuck, you're ass is so soft. It's like fucking a pillow."
            call her_main("Ahhh","body_138")
            call her_main("Please [genie_name]","body_134")
            hide screen hermione_main
            m "Ughh, this feels so good, we might have to make this permanent."
            call her_main("Permanent?","body_139")
            hide screen hermione_main
            m "You wouldn't mind would you?"
            m "Having me use your ass a sex-toy everyday."
            call her_main("...","body_141")
            hide screen hermione_main
            m "I asked you a question [hermione_name]."
            call her_main("... no [genie_name]...","body_133")
            hide screen hermione_main
            ">You feel her asshole start quiver as you glide over it."
            m "Of course you wouldn't, you're enjoying this more than I am, aren't you?"
            call her_main("...yes... I'm loving... you using my ass as your toy","body_134")
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
            $ hermione_SC.chibi.xpos = 400 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            show screen bld1
            hide screen blkfade
            with Dissolve(1)
            call her_main("...With my butt looking like this?","body_141")
            m "I'm sure no one will be able to tell with your skirt on. Now hurry up, I feel like a nap.'"
            #call her_main("Yes [genie_name].","body_141")
            m "Oh I almost forgot, 20 points to Gryffindor!"
            $ gryffindor += 20
            call her_main("Oh... right, the points. Thank you.","body_136")
            ">Hermione picks up her skirt and attempts to put it on. Her ass is so huge that it barely covers half of it."
            $ h_action_show_skirt = True
            ">Your cum is still visible on her ass."
            call her_main("...","body_127")
    
    
    show screen blktone 
    show screen ctc
    with d3

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
    hide screen blktone
    call update_her_uniform

    jump day_main_menu
        #will add this later
        #"-Fuck her ass-" if whoring >= 22:    

label potion_scene_3: #cum addiction - work in progress, has some scenes adjusted for it
    m "[hermione_name], today I have a very special potion that I would like you to drink."
    call her_main("What does this one do?","body_07")
    m "As always, it's going to be a surprise."
    call her_main("You're not going to try to transform me into a cat again are you [genie_name]?","body_07")
    call her_main("","body_07")
    m "Of course not, now would you kindly drink the potion."
    call her_main("...","body_12")
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">Hermione cautiously starts drinking the potion."
    call her_main("","body_126")
    pause .5
    hide screen ch_potion
    with d3
    show screen hermione_blink
    call her_main("This isn't a potion! This is just a bottle full of your cum!","body_30")
    call her_main("Ughhh and it's cold as well.","body_43")
    m "So it just tastes like cum to you?"
    call her_main("Of course it does, what else would it taste like?","body_47")
    ">Hermione starts unconsciously licking her lips."
    call her_main("At least warn me next time you make me drink your cum [genie_name].","body_10")
    m "What do you mean next time?"
    call her_main("Well you're such a pervert you'll probably try and do this again. At least warn me so it's not such a shock.","body_79")
    m "Ok, [hermione_name], I'll make sure to warn you next time."
    call her_main("Is that all then [genie_name]?","body_69")
    m "Yes [hermione_name], 20 points to Gryffindor."
    call her_main("Thank you [genie_name].","body_08")
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
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    ">Hermione quickly enters your office."
    call her_main("What the hell did you do to me?","body_32")
    m "Whatever are you talking about [hermione_name]?"
    call her_main("Ughh, it doesn't matter, just let me suck it.","body_29")
    m "Why on earth would you want to do that? You're a top student, that doesn't sound appropriate."
    call her_main("You know exactly what you did to me. Now let me suck your filthy old cock.","body_47")
    menu:
        "-Let her suck your dick-":
            m "Well if you insist [hermione_name]."
        "-Make her beg-":
            m "I don't think that you deserve to after calling it filthy and old."
            m "Perhaps if you asked nicely..."
            call her_main("Fine. Please let me suck your dick [genie_name].","body_44")
            m "Hmmm, I don't think that was sincere enough."
            call her_main("Please [genie_name], let me suck your big, thick dick. Pretty please.","body_34")
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
    call her_main("","body_66")
    $ hermione_SC.chibi.xpos = -150 #-185 behind the desk. (Also 5 is something).
    $ hermione_SC.chibi.ypos = 10
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
    call her_main("","body_69")
    show screen h_c_u
    hide screen g_c_u
    with d3   
    her "Being this aroused."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gobble!* *Slurp!*"
    call her_main("","body_68")
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
    call her_main("","body_64")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "I even masturbated in the girls bathroom."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Gobble!!* *Gltch!!* *Gobble!!!*"
    call her_main("","body_79")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "But nothing worked."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3   
    her "*Slurp!* *Gulp!* *Slurp!*"
    call her_main("","body_78")
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
    call her_main("","body_65")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "You know why this is happening to me."
    hide screen h_c_u
    hide screen hermione_main
    show screen g_c_u
    with d3  
    her "*Slurp!* *Slurp!* *Gulp!*"
    call her_main("","body_64")
    show screen h_c_u
    hide screen g_c_u
    with d3 
    her "Whatever was in that delicious potion you made \nme drink this morning."
    hide screen hermione_main
    m "Delicious? I thought you said it was just a bottle full of my cum?"
    m "Are you sure that you're just not a little slut who's become addicted to her Headmaster's semen?"
    call her_main("I'm sure. There was something else in there.","body_122")
    hide screen hermione_main
    m "Whatever you say [hermione_name]. Now if you want your reward you better get back to work."
    call her_main("","body_129")
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
            call her_main("{size=+7}!!!{/size}","body_32")
            hide screen hermione_main
            ">The sensation of entering her throat sends you over the edge."
            m "Better start swallowing slut!"
            ">You start pumping your thick load directly into her stomach."
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            ">Hermione's eyes widen and tears form as she senses your semen enter her."
            call her_main("hhaanooo hhhheerrr","body_130")
            hide screen hermione_main
            ">Her hands shoot down into her pants as she starts violently orgasming."
            ">The sight of her pleasuring herself as you use her throat only prolongs your orgasm."
            m "You dirty little girl. Getting off from your headmaster sticking his cock down your throat."
            m "I bet your loving this, being used as a nothing more than a toy."
            ">She says nothing but quickens the pace of her masturbation."
            ">You finally pull out of keen mouth with a satisfactory pop."
            call her_main("It won't stop!","body_132")
            hide screen hermione_main
            m "What won't?"
            call her_main("I-I can't stop cumming [genie_name]...","body_117")
            hide screen hermione_main
            ">The stimulation proves too much and she passes out."
            
        "-Cum in her mouth-":
            m "This is it girl. Get ready."
            ">Hermione starts swirling her tongue and focusing on the tip of your shaft."
            g4 "That's done it slut! Start swallowing."
            ">You explode into her mouth."
            $ g_c_u_pic = "cum_in_mouth_ani"
            $ aftersperm = True
            call her_main("mmmmmmm *gulp* *gulp*","body_125")
            hide screen hermione_main
            ">Hermiones eyes go blank as she starts swallowing down your load."
            m "That's it, swallow it down like a good girl. You earned your prize."
            call her_main("*gulp* *gulp* *gulp* *gulp*","body_126")
            hide screen hermione_main
            ">As she swallows you notice her legs start to convulse as she starts to orgasm."
            call her_main("*gulp* *gulp* *gulp* ","body_125")
            hide screen hermione_main
            ">You finally remove your shaft from her hungry mouth."
            m "Very good girl. Almost entirely clean... except for a bit of cum on the tip."
            m "I can't dirty my robes now can I? Better wipe this off."
            ">You wipe yourself clean on the tip of her nose."
            call her_main("...","body_126")
            hide screen hermione_main
            m "There much better."
            ">Her legs have not stopped quivering since you first came."
            m "Well aren't you going to say anything [hermione_name]?"
            call her_main("Thank you maste-","body_133")
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
            call her_main("What are you doing [genie_name]?","body_48")
            hide screen hermione_main
            m "Giving you your well earned reward."
            $ g_c_u_pic = "cum_on_face_ani"
            hide screen h_c_u
            show screen g_c_u
            with d3 
            $ uni_sperm = True
            ">You start pumping your cock quickly and explode all over the young witch's face"
            m "Take it you filthy cum slut!"
            call her_main("{size=+5}!!!{/size}","body_121")
            hide screen hermione_main
            ">Hermione immediately starts masturbating shamelessly in front of you."
            call her_main("{size=+5}I'm cumming{/size}","body_117")
            hide screen hermione_main
            m "What was that [hermione_name]?"
            call her_main("I-I'm cumming","body_130")
            hide screen hermione_main
            m "Just from a facial? What sort of cumslut have you become Miss Granger?"
            m "What would your parents think? Looking at you covered in some old mans cum."
            call her_main("No. Please stop, I'll-","body_34")
            hide screen hermione_main
            m "They'd be ashamed at what you've become. A whore who gets off from being used as a toy."
            call her_main("I-I'm cumming again [genie_name]. It won't stop...","body_32")
            hide screen hermione_main
            ">Hermione's voice trails off as she pass out from the over stimulation."
        "-Cum on the floor-":
            m "I'm cumming whore."
            call her_main("mmmmmmmm","body_115")
            hide screen hermione_main
            ">She goes to bury her face into her crouch but you put your palm on her forehead and push her away."
            show screen h_c_u
            hide screen g_c_u
            with d3 
            call her_main("[genie_name], what are you doing?","body_119")
            hide screen hermione_main
            m "giving you your reward"
            ">After a few quick pumps you point your dick at the floor and explode."
            call her_main("PROFESSOR! Why would you waste that?","body_118")
            hide screen hermione_main
            m "It's not wasted [hermione_name], your reward is right there waiting for you."
            call her_main("I'm not going to eat that. The floor in here is\n disgusting.","body_117")
            hide screen hermione_main
            m "Well you can always wait until tomorrow morning then."
            call her_main("TOMORROW MORNING!? I can't wait that long. \nCan't you just cum again?","body_119")
            hide screen hermione_main
            m "No [hermione_name], I'm a tired old man and it's time for me to go to sleep."
            m "You can either eat off the floor or you can come back tomorrow."
            call her_main("...Fine","body_120")
            hide screen hermione_main
            ">She begrudgingly starts scooping your cum off the floor with her fingers."
            menu:
                "-Watch her-":
                    call her_main("","body_125")
                    ">She scoops up as much as she can into her palm \nand quickly moves it to her mouth."
                    pass
                "-Make her lick it up-":
                    m "Not with your fingers [hermione_name]."
                    call her_main("What do you mean not with my fingers? How \nelse am I supposed to eat it?","body_117")
                    hide screen hermione_main
                    m "You have a perfectly good tongue, I suggest that you put it to use."
                    call her_main("You expect me to LICK your old cum off the \nfloor?","body_118")
                    hide screen hermione_main
                    m "I do. Unless of course you would prefer to go back to your room hungry and unsatisfied."
                    call her_main("...","body_117")
                    hide screen hermione_main
                    ">She bends over with her head to the floor."
                    $ aftersperm = True
                    call her_main("(This is so degrading)","body_116")
                    hide screen hermione_main
                    ">She puts her tongue out licks your cum."
            ">The effect is instantaneous."
            $ aftersperm = True
            call her_main("I-I'm cumming.","body_126") #small text
            hide screen hermione_main
            m "What was that?"
            call her_main("I'm cumming!","body_133")
            hide screen hermione_main
            ">Hermione's hand shoots under her skirt as she starts violently orgasming."
            call her_main("What's wrong with me [genie_name]?","body_134")
            hide screen hermione_main
            m "A lot of things [hermione_name], considering you just ate my cum off the ground."
            call her_main("I can't stop cumming...","body_139")
            hide screen hermione_main
            ">Hermione loses conciousness."
    hide screen bld1
    hide screen hermione_main
    ">Hermione is in an unconscious heap on the floor."
    menu:
        "-Carry her back to her room as is-":   
            ">You pick her limp body up and carry her to her room."
            ">As you enter the dormitory you hear her talk in her sleep."
            call her_main("Of course I swallow... just form a line...","body_131")
            hide screen hermione_main
            ">You place her carefully back into her bed."
            m "Sleep tight slut."
        "-Clean her up and take her back to her room-":   
            $ uni_sperm = False
            ">You pick her limp body up and carry her to her room."
            ">As you enter the dormitory you hear her mumble in her sleep."
            call her_main("You want a kiss [genie_name]? Of course I don't mind...","body_127")
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
    hide screen blktone
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    $ hermione_SC.chibi.ypos = 250 #Default: 250
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
    call her_main("I'm not sure that I like these potions [genie_name].","body_07")
    call her_main("Especially after the time you tried to turn me into a cat.","body_09")
    m "To be fair I was trying to turn you into another girl..."
    call her_main("That's not much better [genie_name].","body_05")
    m "Isn't it?"
    call her_main("Well at least promise me that this one isn't going to embarrass me in the middle of class.","body_04")
    call her_main("My reputation is suffering enough as it is. I don't need these constant potions causing me to transform in front of my peers.","body_12")
    m "I promise that this potion won't affect your body in any way."
    call her_main("Well then what on earth is it going to do?","body_05")
    m "As always [hermione_name], you'll ha-"
    call her_main("Have to wait and see. I know.","body_07")
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione quickly drinks the potion."      #new
    call her_main("","body_04")
    hide screen ch_potion
    show screen hermione_blink
    her "Can I go now?"
    m "Yes you may. 20 points to Gryffindor"
    call her_main("Thank you [genie_name].","body_16")
    
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
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png"
    $ transparent_quest = True
    jump day_main_menu

label potion_scene_4_2: #Scene where Hermione comes back after classes angry and confused at having her uniform made transparent
    $ transparent_quest = False
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    if whoring <= 7: #Very angry and embarrassed
        ">Hermione bursts into your office."
        call her_main("How could you [genie_name]!","body_22")
        call her_main("I am the laughing stock of the entire school!","body_21")
        call her_main("Now everyone knows what I look like naked!","body_20")
        m "Tell me about what happened."
        call her_main("Tell you about what happened? I'm never speaking to you again.","body_21")
        $ mad += 20
        $ transparency = 1
        # $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/"+outfit.breast_layer+".png"
        # This is bugged and causes a crash. Things don't go catistrophically wrong without this line, so I've edited it out until you can fix it.
    elif whoring <= 13: #Mildly aggravated
        ">Hermione comes into your office quickly without knocking."
        call her_main("Again?","body_34")
        m "What's this about [hermione_name]?"
        call her_main("Why would you make my clothes invisible again?","body_31")
        m "Why not?"
        call her_main("Ugh, you're such a pig.","body_29")
        m "Tell me about what happened."
        call her_main("...","body_33")
        call her_main("Fine, but I expect an extra 10 points.","body_31")
        m "As you wish."
        call her_main("Well I started off with potions class as usual when I started to feel like all eyes were on me.","body_66")
        m "I wonder why."
        call her_main("As I was saying I was completing potions class and felt like everyone wouldn't take their eyes off of me.","body_69")
        call her_main("I didn't think anything of it until I was approached by Professor Snape at the end of the lesson.","body_79")
        call her_main("He normally criticises me during potions class. Stuff like getting dosages wrong, things that I know are correct.","body_29")
        m "Back to the story [hermione_name]."
        call her_main("Well when he commented that he liked my outfit I was suspicious. I thought that perhaps he was talking about my shirt until I looked down and saw that everything was see through.","body_66")
        call her_main("But I just ignored him, finished class and ran here.","body_69")
        m "You just finished class?"
        call her_main("Of course, I can't afford to miss potions class. I'm doing poorly enough without missing class.","body_79")
        m "Well fair enough. You may go now."
        call her_main("Hmmph. Goodbye [genie_name].","body_29")

    elif whoring <= 20: #Slightly aroused
        ">Hermione enters your office"
        call her_main("Can you at least warn me next time?","body_08")
        m "Well, that'd take away from the suspense wouldn't it?"
        call her_main("Hmmmm, well at least ask what I'm doing before you give me the potion.","body_10")
        m "Why, what did you have to do today that was so important?"
        call her_main("I had to give a speech for languages!","body_28")
        call her_main("Do you have any idea how inappropriate it was giving a speech on morality in front of the entire class-","body_16")
        call her_main("{size=+5}As my clothes became transparent!{/size}","body_28")
        m "Well I imagine it depends on what side of morality you were arguing."
        call her_main("It doesn't matter.","body_16")
        m "Are you sure that you didn't enjoy it?"
        call her_main("How could I. I had to stand there as my friends and peers all saw me naked.","body_17")
        m "You finished your speech?"
        call her_main("Certainly, I had to make sure that everyone knew my views on morality.","body_15")
        m "Well I'm sure they have a crystal clear view of it now."
        call her_main("Hmmph, are you done?","body_12")
        m "Yes, you may go now."
        call her_main("Good bye [genie_name].","body_02")
    else: #Highly aroused (doesn't even acknowledge that her clothes are see-through)
        ">Hermione enters the office casually."
        m "Hello [hermione_name], how was your day today?"
        call her_main("Fine [genie_name]. Why do you ask?","body_06")
        m "No reason. Anything unusual happen today?"
        call her_main("Hmmmm, now that you mention it I suppose that boys in class were a little more forward than usual.","body_10")
        m "How so?"
        call her_main("Well nothing serious, just small stuff like calling me names, groping me.","body_13")
        m "Groping you? What on earth could have provoked them to do that?"
        call her_main("I don't know [genie_name]. I can't imagine any reason that I would be attracting attention today...","body_45")
        m "You're getting off on this aren't you?"
        call her_main("...","body_46")
        call her_main("I've never been so turned on in my life. Having all eyes on me. Having every boy imagine doing unspeakable things to me.","body_121")
        call her_main("Snape made me stand out the front of class after I talked back to him.","body_124")
        call her_main("I think that I orgasmed just from the looks people gave me.","body_123")
        m "Well done [hermione_name]. You're becoming quite the slut."
        call her_main("Thank you [genie_name]. Is that all?","body_128")
        m "Yes, you can go now slut."
        call her_main("{image=textheart}","body_46")
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    $ transparency = 1
    call update_her_uniform
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_sleeping = True
    jump night_main_menu
        
label potion_scene_5: #Lamia potion
    call her_main("That's dumb.","body_32")
    m "I literally don't know."
    jump day_main_menu

label potion_scene_6: #Luna potion
    m "Might I offer you a drink?"
    call her_main("You're not trying to get me drunk on Butterbeer again are you?","body_03")
    m "Nothing of the sort, just a harmless little potion."
    ">You hand her the potion bottle."
    call her_main("Another of your mysterious potions?","body_08")
    her "Let me guess, you won't tell me what it does and I'll embarrass myself in front of the whole class?"
    m "Not at all."
    call her_main("That's new.","body_17")
    her "... and somehow worrying"
    her "So what exactly is it then?"
    m "It's your regular, run-off-the-mill Polyjuice Potion."
    call her_main("Ugh. Those taste like muck.","body_33")
    her "...and what will it turn me into?"
    m "That, Miss Granger, is a secret."
    call her_main("Typical.","body_23")
    m "It'll taste a lot sweeter if you imagine all the points you'll earn for Gryffindor."
    m "How much of a lead did Slytherin have on you again?"
    her "You're right [genie_name]. I can't let Gryffindor down!"
    ">She downs the thick potion."
    call her_main("Blehgh.","body_43")
    her "I was wrong, not muck. Snot. It's as thick as Trollsnot."
    m "As long as you keep it down, you'll earn Gryffindor a great deal of points."
    her "And I will."
    call her_main("So what now? I just go to class?","body_44")
    m "Not yet, tell me something about yourself."
    call her_main("Well, ever since I started my \"Extracurricular activities\" with you my attendance and grades have started slipping.","body_16")
    m "Troubling indeed."

    if whoring <= 13:
        call her_main("It is! [genie_name], I used to be at the top of the class. My scores were impeccable. ","body_30")
        m "And how are your scores now?"
        call her_main("Well I'm still at the top... Just not by as much.","body_12")
        m "Well, there are times when academic excellence shouldn't be your primary concern."
        call her_main("Hmmph, and what /should/ be my primary concern then?","body_17")
        m "Currently. I'd say your face is pretty high on the list"
        call her_main("Excuse me. That is hardly appropriate for a headmaster.","body_35")
        m "No, I'm serious. You should really see the look on your face."

    else:
        call her_main("Not really. I realize there are other things I can excel in.","body_06")
        m "Like sucking cocks for house-points"
        call her_main("Professor!","body_30")
        m "Oh don't be so modest. If sucking dick was a class, you'd be Magna Cum Laude."
        call her_main("Thank you professor. You know, there's time to earn some more points before class. If you're feeling generous I could...","body_30")
        m "I'd have to know on whose face I'll be cumming though "
        call her_main("What do you mean? ...My face of course... I mean ...*urp*","body_30")
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
    m "Absolutely. (Not a chance) But, what if you bump into her in the halls?"
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
    jump day_main_menu
    
label potion_scene_7: #Ahegao potion
    m "How long until your next class [hermione_name]?"
    call her_main("about fifteen minutes sir.","body_02")
    m "in that case I think you might have to be a little late."
    call her_main("what? why?","body_11")
    g4 "Well, it might be a bit hard for you to attend class with my cock buried in your tight little pussy."
    call her_main("Oh...","body_105")
    m "That's not going to be a problem is it [hermione_name]?"
    call her_main("of course not [genie_name]! Let me just take my clothes off...","body_106")

    show screen blkfade
    with d3
    hide screen bld1
    hide screen hermione_blink
    #SEX
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    call her_main("ahhhhhhhhh....{image=textheart}","body_130")
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    hide screen genie
    $ ccg_folder = "herm_sex"
    $ ccg1 = "blank"
    $ ccg3 = "blank"
    $ ccg2 = 1
    show screen ccg
    hide screen blkfade
    with d3
    her "Ah...{image=textheart}"
    g4 "mmmm, you like that don't you slut?"
    $ ccg2 = 2
    her "yes...{image=textheart}"
    $ ccg2 = 3
    her "even though I have to miss class..."
    $ ccg2 = 4
    her "I Honestly don't care...{image=textheart}"
    $ ccg2 = 5
    her "This just feels too goooood..."
    pause
    ">You quietly pull out the small vial from your pocket and pull the stopper out."
    $ ccg2 = 6
    her "Mmmm, don't slow down [genie_name]..."
    g4 "You asked for it!"
    ">You speed up the pace as you go to pour a drop onto her ass, your hand barely managing to stay stable..."
    $ ccg2 = 7
    her "Harder [genie_name]!!!"
    pause
    ">You feel hermione suddenly push her pussy back towards you, causing you to spill about a quarter of the vial onto her ass..."
    $ ccg3 = "p1"
    m "..."
    $ ccg2 = 8
    her "What was that?"
    m "Ugh... nothing... just a bit of spit. Keep going slut."
    $ ccg2 = 9
    her "Ah...{image=textheart} alright then..."
    ">You quickly put the stopper back into the vial and slip it back into your robes."
    $ ccg2 = 10
    her "Ah... ah... ah..."
    pause
    $ ccg2 = 11
    her "[genie_name], you think you could... ah..."
    g4 "What is it slut?"
    $ ccg2 = 12
    her "Could you please... spank me... ah...?"
    g4 "of course!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass a hard spank, accidentally causing the potion to explode out from underneath your hand, coating her even more."
    $ ccg3 = "p2"
    $ ccg2 = 13
    pause
    her "{size=+10}!!!{/size}"
    ">Hermione's sopping cunt starts contracting around your cock uncontrollably."
    g4 "Mmmm, cumming already slut?"
    $ ccg2 = 14
    her "Y-yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 15
    her "I{image=textheart} can't{image=textheart} stop..........{image=textheart}{image=textheart}{image=textheart}"
    ">True to her word, you don't feel an end to her relentless spasming."
    g4 "I love it when cum on my cock whore!"
    $ ccg2 = 16
    pause
    her "no...{image=textheart} sir...{image=textheart} you...{image=textheart} don't...{image=textheart} understand...{image=textheart}"
    $ ccg2 = 17
    her "It...{image=textheart} won't...{image=textheart} stop...{image=textheart}"
    g4 "I don't see how that's my problem!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, savoring the feeling of another orgasm flowing through the young witch."
    $ ccg2 = 18
    her "{size=+10}!!!{/size}"
    $ ccg2 = 19
    her "its......{image=textheart} {image=textheart} "
    $ ccg2 = 20
    pause
    her "my{image=textheart}  whole{image=textheart}  body...{image=textheart}{image=textheart}{image=textheart} "
    g4 "Speak up slut!"
    $ ccg2 = 21
    her "My body's...{image=textheart} {image=textheart} on fire..."
    $ ccg2 = 22
    her "I can't...{image=textheart}"
    $ ccg2 = 23
    her "why...{image=textheart}"
    $ ccg2 = 24
    her "Why {image=textheart}does {image=textheart}it {image=textheart}feel {image=textheart}this {image=textheart}goooooooooood...{image=textheart}{image=textheart}{image=textheart}"
    g4 "enjoying yourself are we?"
    $ ccg2 = 25
    her "No...{image=textheart} ah... yesssss....{image=textheart}"
    $ ccg2 = 26
    her "it's like...{image=textheart}"
    $ ccg2 = 27
    her "each time you thrust...{image=textheart}{image=textheart} that big fat {image=textheart}cock{image=textheart} in me...{image=textheart}"
    $ ccg2 = 28
    pause
    her "it's like I {image=textheart}{image=textheart}cum{image=textheart}{image=textheart}..."
    her "But it never resets..."
    $ ccg2 = 29
    her "Each time is just another stronger {image=textheart}orgasm{image=textheart}..."
    $ ccg2 = 30
    her "{size=+10}AND{image=textheart} THEY{image=textheart} NEVER{image=textheart} STOOO{image=textheart}OOOP!!!!!!"
    g4 "Sounds nice... and what about when I give your fat ass a nice... slap?"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass another hard slap, holding your hand against her warm flesh, swirling the potion around underneath it."
    $ ccg2 = 31
    her "{size=+20}{image=textheart}{image=textheart}!!!{image=textheart}{image=textheart}{/size}"
    $ ccg2 = 32
    her "{image=textheart}my{image=textheart} {image=textheart}brain...{image=textheart}"
    $ ccg2 = 33
    her "You're{image=textheart} going{image=textheart} to{image=textheart} kill{image=textheart} me...{image=textheart}"
    g4 "Stop being so overdramatic..."
    pause
    $ ccg2 = 34
    her "I'm not...{image=textheart}"
    her "Ah.....{image=textheart} some....{image=textheart} thing....{image=textheart} is....{image=textheart} wrong....{image=textheart}"
    ">Hermione's words start to slow, eventually only being able to mutter a squeak of a word every time you thrust into her."
    g4 "Maybe it was the potion I poured all over your ass earlier?"
    $ ccg2 = 35
    her "{size=+20}{image=textheart}{image=textheart}what?{image=textheart}{image=textheart}{/size}"
    g4 "Don't worry, the effects should wear off in about an hour..."
    $ ccg2 = 36
    her "{size=+20}!!!!!!!{/size}"
    g4 "In the mean time, why don't you just sit back and enjoy the ride."
    $ ccg2 = 37
    her "{image=textheart}e-e-enjoy....{image=textheart}"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    $ ccg2 = 38
    pause
    her "{size=+20}!!!!!!!{/size}"
    $ ccg2 = 39
    her "Pleeeease...{image=textheart}{image=textheart}{image=textheart}"
    $ ccg2 = 40
    her "my...{image=textheart}mind...{image=textheart}is...{image=textheart}breaking...{image=textheart}"
    ">You start to pick up the pace, treating her as nothing more than your mewling fuckmeat..."
    g4 "MMMM, you always no what to say to get me going!!"
    $ ccg2 = 41
    her "...{image=textheart}{image=textheart}{image=textheart}"
    ">Eventually the endless spasming of her drenched pussy around your cock prove too much."
    g4 "Ah!!! Here It comes whore!"
    $ ccg2 = 42
    pause
    her "{image=textheart}........{image=textheart}"
    ">You start firing cum directly into her womb."
    $ ccg3 = "s4"
    $ ccg2 = 43
    pause
    her "{image=textheart}!!!{image=textheart}"
    g4 "TAKE THIS!!!"
    $ renpy.play('sounds/slap.mp3')
    show screen white 
    pause.1
    hide screen white
    with hpunch
    ">You give her ass one last slap, stinging your hand as you shoot the last rope into her waiting cunt."
    $ ccg3 = "s5"
    $ ccg2 = 44
    pause
    her "{image=textheart}........{image=textheart}"
    her "{image=textheart}...............{image=textheart}"
    $ ccg2 = 45
    pause
    her "{image=textheart}.......................{image=textheart}"
    show screen blkfade
    with d3
    ">Eventually hermione's eyes roll back into her head as she collapses forward onto your desk."
    ">you carry her unconscious body back to her room to sleep the last of the potion off."
    hide screen ccg
    hide screen hermione_main
    hide screen hermione_blink
    show screen genie
    hide screen blkfade
    with d3
    $ hermione_takes_classes = True
    jump day_main_menu



    
label potion_scene_8: #Hypno potion
    m "[hermione_name], I have another special potion for you today."
    call her_main("Who are you even buying these off?","body_07")
    m "A good magician never tells."
    call her_main("Magician? You're a wizard, and this better not have any long term side effects.","body_07")
    call her_main("I'm still coughing up fur balls every now again from that polyjuice potion.","body_07")
    m "Of course it won't, now would you kindly drink the potion."
    call her_main("...","body_12")
    show screen ch_potion
    with d3
    hide screen hermione_blink
    ">Hermione cautiously starts drinking the potion."
    call her_main("","body_126")
    pause .5
    hide screen ch_potion
    with d3
    show screen hermione_blink
    call her_main("This isn't bad at all.","body_53")
    call her_main("I feel...","body_74")
    m "You feel what?"
    call her_main("I-I feel gre...","body_71")
    ">Hermione's eyes go blank and she stares forward blankly."
    call her_main("What am I?","body_123b")
    m "You're an air-headed bimbo who only wants to make people happy."
    $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/skirt_6.png"
    $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_5.png"
    $ hermione_wear_panties = False
    #call set_h_hair(hair_style="B",color=2)
    call her_main("I am an airheaded bimbo who only wants to make people happy...","body_225b")
    m "You love being covered in my cum."
    $ hermione_badge = "01_hp/13_characters/hermione/accessories/badges/cum_badge.png"
    $ hermione_badges = True
    call her_main("I love being covered in your cum...","body_225b")
    m "You're breasts are incredibly sensitive to pleasure."
    call her_main("My breasts are incredibly sensitive to pleasure......","body_225b")
    ">Hermione closes her eyes and appears to nod off."
    call her_main("......","body_84")
    call her_main("Where am I?","body_44b")
    m "You're in my office."
    call her_main("I am?","body_44b")
    call her_main("How did I get here?","body_44b")
    m "You walked in here about 2 minutes ago."
    call her_main("Huh, I must have forgotten, silly old me.","body_53b")
    call her_main("So professor, what am I doing here?","body_54b")
    m "I'm just going to ask you a few questions."
    call her_main("They're not going to be hard questions are they?","body_57")
    call her_main("I don't like hard questions.","body_57b")
    m "Don't worry they'll be nice and easy for you."
    call her_main("yay!","body_75")
    m "First question, Who are you?"
    call her_main("That's an easy one! I'm Hermione Granger, the prettiest girl in the whole school!","body_80")
    m "And what are your hobbies?"
    call her_main("Doing my makeup{image=textheart}, dancing{image=textheart} and dressing happy{image=textheart}!","body_74")
    m "Dressing happy?"
    call her_main("You know, wearing nice things to make other people happy!{image=textheart}","body_78")
    m "You like making people happy?"
    call her_main("Of course mistah professor, making people happy{image=textheart} makes me happy{image=textheart}!","body_75")
    call her_main("Once I finish school I want to get a job where all I do is make people happy{image=textheart}!","body_74")
    m "Ok, final question;"
    m "How would you like to make yourself happy?"
    call her_main("Make myself happy?","body_73b")
    call her_main("But I'm already happy, silly!","body_74")
    m "Even happier."
    call her_main("Even happier? {size=+10}YAY!{/size}","body_80")
    call her_main("So how am I going to be happier? Am I going to get naked?","body_68b")
    m "That'd be a good start."
    call her_main("{image=textheart}AAAAAAWWWEEESOOOOOOOOMMME!{image=textheart}","body_106")
    ">Hermione starts slowly stripping, removing her top first."
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    $ wear_shirts = False
    call update_her_uniform
    call update_chibi_uniform
    $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/skirt_6.png"
    call her_main("You know they don't let us walk around naked at school?","body_103b")
    m "Really? I can't imagine why not."
    call her_main("I know right? It's like so dumb! Everyone would just be happier{image=textheart} if they got to be naked.","body_121")
    ">Hermione removes her skirt"
    $ hermione_wear_skirt = False
    call update_chibi_uniform
    call her_main("I know everyone who sees me naked is happy!","body_128b")
    m "You've certainly made me happy."
    call her_main("Thanks mistah professor sir! That makes me so happy{image=textheart}!","body_57b")
    m "(I don't think I can stand her saying the word happy much more...)"
    m "Now Hermione, I want you to touch your breasts."
    ">Hermione moves her hands up to her breasts"
    call h_action("lift_breasts")
    $ h_action_show_skirt = False
    call her_main("Like this? This feels sooooo gooood!","body_59b")
    call her_main("It's like mah hands are moving on their own...","body_121")
    call her_main("It's soooo goodd but It's weeeiiird... I need something... anything...","body_131")
    m "Would you like to touch yourself down there?"
    call her_main("Yes mistah [genie_name]. please.","body_132")
    menu:
        "-make her beg-":
            m "I want you to beg."
            call her_main("Please mistah sir...","body_132", "blush")
            m "Please what?"
            call her_main("Ohmigawd Please let me touch myself down there... I'll do anything...","body_140b", "blush")
            m "Anything?"
            call her_main("Anything. I just need to feel happy...","body_138b", "blush")
            m "Tell me what you are and I'll let you."
            call her_main("I'm Hermione, the school slut.","body_136", "blush")
            m "More."
            call her_main("geez, I'm a dumb bimbo fuckbunny... that just wants to feel happy...","body_134", "blush")
            m "And what makes you happy?"
            call her_main("Making you happy{image=textheart} [genie_name].","body_133b", "blush")
            m "Good girl."
        "-let her touch herself-":
            m "Go on then."
            call her_main("Thank you soooo{image=textheart} much [genie_name]!","body_134", "blush")
    call h_action("covering")
    call her_main("This is soooo goood","body_136", "blush")
    call her_main("Mistah [genie_name] can you please do something for me?","body_209b", "blush")
    m "What's that?"
    call her_main("If it's not tooo much trouble could you...","body_134", "blush")
    ">Hermione starts pinching her nipple."
    call h_action("pinch")
    call her_main("could you please cum on me?","body_219", "blush")
    m "Well if it makes you happy."
    ">you stand up and head towards her."
    call her_main("thank you, thank you thank you! You're the best headmaster {size=+5}EVER!{/size}","body_80", "blush")
    hide screen genie
    $ genie_chibi_xpos = 5 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "jerking_off_02_ani"
    show screen chair_02
    show screen g_c_u
    show screen desk_02

    hide screen blkfade
    hide screen blktone
    hide screen bld1
    show screen ctc
    with fade
    call h_action("covering")
    call her_main("...","body_78", "blush")
    call h_action("pinch")
    call her_main("I don't know how other girls do it...","body_71b", "blush")
    m "Do what?"
    call her_main("Stop themselves from coming here and getting you to cover them in yummy cummy!","body_73b", "blush")
    call h_action("covering")
    call her_main("I mean I can barely stop mahself coming here everyday!","body_75", "blush")
    m "That's it..."
    call h_action("pinch")
    call her_main("Hmmm, I just luv playin' with mah boobies{image=textheart}{image=textheart}{image=textheart}","body_78", "blush")
    call her_main("They're just so soft...","body_196", "blush")
    call h_action("covering")
    call her_main("And they feel soo good. They're really sensi--","body_205", "blush")
    call her_main("Sensi---","body_213", "blush")
    call h_action("pinch")
    call her_main("What's the word?","body_214", "blush")
    m "Sensitive."
    call h_action("covering")
    call her_main("That's right they're really sensitive!","body_212", "blush")
    m "So am I..."
    call her_main("Are you going to cum?","body_219", "blush")
    call h_action("pinch")
    call her_main("Please do it on my face!","body_219", "blush")
    call her_main("No wait my tits...","body_216", "blush")
    call h_action("covering")
    call her_main("No wait my face!","body_212", "blush")
    menu:
        "-Cum on her face-":
            g4 "Here it comes slut!"
            call her_main("{image=textheart}!!!{image=textheart}","body_211b", "blush")
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
            $ uni_sperm = True
            g4 "that's it, all over your face."
            call h_action("pinch")
            call her_main("...{image=textheart}{image=textheart}{image=textheart}","body_212", "blush")
        "-Cum on her tits-":
            g4 "Here it comes fuckbunny!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","body_211b", "blush")
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            $ u_sperm = "01_hp/13_hermione_main/auto_02.png"
            $ uni_sperm = True
            g4 "All over your tits."
            call h_action("pinch")
            call her_main("It's so warm...{image=textheart}{image=textheart}{image=textheart}","body_212", "blush")
        "-cover her in cum-":
            g4 "Here it comes whore!"
            call her_main("{image=textheart}{image=textheart}{image=textheart}","body_211b", "blush")
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            $ u_sperm = "01_hp/13_hermione_main/auto_05.png"
            $ uni_sperm = True
            g4 "that's right slut, All over you."
            call h_action("pinch")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","body_212", "blush")
    $ genie_chibi_xpos = 5 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "jerking_off_02_ani"
    call her_main("...","body_136")
    $ hermione_dribble = True
    call her_main("That felt {size=+5}SOOOOO!{/size} good!","body_134", "blush")
    call h_action("lift_breasts")
    $ h_action_show_skirt = False
    call her_main("Can we do it again! Please! Pretty please! Pretty please with cum on top!","body_133b", "blush")
    m "Not today."
    hide screen chair_02
    hide screen desk_02
    show screen genie
    hide screen g_c_u
    hide screen blkfade
    with d5
    call her_main("Awwwwww.","body_132", "blush")
    call her_main("Well ok... I suppose I'll head to class then.","body_87b", "blush")
    m "About that. I think it'd be better if you went back to your dorm."
    call her_main("Why's that mistah [genie_name] sir?","body_82b", "blush")
    m "I think you need to have a little nap and let this wear off."
    call her_main("whatever you say sir!","body_83", "blush")
    call h_action("")
    call her_main("And thanks again!{image=textheart} You're the best!","body_80", "blush")



    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    m "(Maybe I should have told her to get dressed first...)"
    
    $ hermione_badges = False
    $ hermione_dribble = False
    $ hermione_takes_classes = True
    $ hermione_wear_skirt = True
    $ hermione_wear_top = True
    $ hermione_wear_bra = True
    $ wear_shirts = True
    call update_her_uniform
    call update_chibi_uniform
    jump day_main_menu

label potion_scene_9: #Clone potion
    m "Do you ever feel conflicted about what we do in here [hermione_name]?"
    her "Conflicted? I suppose I do... why do you ask?"
    m "because I have a new potion that can help you come to terms with this internal conflict."
    her "What? How?"
    m "It splits your mind into two parts, allowing you to confront yourself and address the problem."
    her "Splits my mind?! That doesn't sound very safe!"
    m "It only splits your mind metaphorically. I ensure you it's as safe as can be."
    her "Well if you made it yourself then I trust it. I mean it's not like the weasley twins made it."
    m "Of course not... Now if you'd kindly drink it we can get to the bottom of your conflicted nature."
    her "..."
    her "Well here goes..."
    ">Hermione drinks the potion."
    her "Mmmmmm it's so sweet..."
    herA "Ughhhh, it's so sour..."

    #Hermione split into two versions of herself, one slutty, one prudish
    #Slutty one wants to have sex with Genie 
    #Genie obliges
    #Slutty Hermione enjoying it immensely 
    #Genie trying to convince pruddy Hermione to join in
    #Prude Hermione wants no part in it, although she is slightly aroused
    #Slut Hermione 
    #Genie cums in Hermione
    #Slut Hermione wants to go again 
    #Slut Hermione offers to suck Genie to get him hard 
    #Genie says why don't we get prude Hermione to do it
    #Slut Hermione says that's a great idea
    #Prude Hermione refuses
    #Slut Hermione and Genie force her to her knees
    #Genie talks dirty to Prude Hermione while Slutty Hermione encourages her
    #Genie ends up covering her in cum
    #Prude Hermione partially speechless
    #Slutty Hermione wants to go again but Genie is spent
    #Hermione reforms into one person
    #Genie ridicules her, saying that even the most prudish and reseverved version of herself ended up sucking him off
    #Hermione feels both shame and pride
    #THE END












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

label potion_scene_10: #Time stop potion
    m "Do you ever feel conflicted about what we do in here [hermione_name]?"

    #Paralyze/time stop Hermione
    #Have genie molest her
    #Have options to molest breast/ass/pussy (required to do all 3)
    #Have her resume time and lose her mind from the cumulative amount of pleasure she felt
    #Have genie carry her back to her dorm in a semi-conscious state. 












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

label potion_scene_11: #Milking potion

    if potion_scene_11_progress == 0 or whoring < 13:
        $ potion_scene_11_progress = 1
        jump potion_scene_11_1
    elif potion_scene_11_progress == 1 or whoring < 18:
        $ potion_scene_11_progress = 2
        jump potion_scene_11_2
    else:
        jump potion_scene_11_3











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


label potion_scene_11_1: #Milking potion part 1
    m "[hermione_name], how would you like to try a nice little potion?"
    call her_main("...","body_04")
    call her_main("If I had the option I'd prefer not to...","body_02")
    m "well-"
    call her_main("but unfortunately, \"Slytherin\" winning the house cup this year isn't an option!","body_30")
    m "So you'll drink the potion then?"
    call her_main("Yes [genie_name], I'll drink your potion.","body_17")
    m "Fantastic!"
    ">You hand her the cloudy potion."
    ">Hermione cautiously smells the mixture."
    call her_main("Is this milk?","body_12")
    call her_main("...","body_09")
    call her_main("I guess it doesn't matter...","body_08")
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione quickly drinks the potion."
    hide screen ch_potion
    show screen hermione_blink
    call her_main("Ah...","body_126")
    call her_main("It was milk!","body_46")
    m "Yes. Apparently it's a special kind of milk."
    call her_main("Apparently?","body_08")
    call her_main("Do you even know where this came from?","body_09")
    m "O-Of course I do."
    m "I'm the great dingledoor after all!"
    call her_main("...","body_08")
    call her_main("If you don't want to say what it is that's fine sir...","body_04")
    call her_main("But there's no need to insult me.","body_07")
    m "(what did I say?)"
    m "Yes, well, you should notice the effects starting to manifest soon enough."
    call her_main("Hmmm...","body_128")
    call her_main("And what sort of \'effects\' would that be?","body_08")
    m "You may notice a some minor swelling in those nice tits of yours."
    call her_main("...","body_06")
    call her_main("Is this milk going to make by breasts bigger [genie_name]?","body_09")
    m "That's one half of it."
    call her_main("...","body_07")
    call her_main("And the other half?","body_12")
    m "Well you might start to notice a little milk coming from your-"
    call her_main("What???","body_48")
    call her_main("Professor, Do you mean to say that this potion is going to cause me to lactate?","body_09")
    m "That's one way to put it."
    call her_main("...","body_07")
    call her_main("Well how long is it supposed to last? I do have classes today.","body_12")
    call her_main("I'm falling behind enough as it is...","body_29")
    m "Really?"
    call her_main("Yes... I think it's all this fooling around sir.","body_33")
    call her_main("I nearly got a \"b\" in biology the other day...","body_28")
    m "Well speaking of biology..."
    ">You notice hermione's breasts slight to swell slightly."
    call her_main("!!!","body_18")
    call her_main("[genie_name], they're growing rather quickly!","body_28")
    m "This is all perfectly normal."
    call her_main("...","body_08")
    ">Hermione's breasts start to visibly swell again."
    call her_main("Ugh... it feels like my organs are sliding into my chest...","body_28")
    call her_main("This isn't going to cause any ongoing issues is it?","body_09")
    m "O-o-of course not..."
    call her_main("...","body_07")
    call her_main("That wasn't very inspiring...","body_09")
    m "Just focus on the matter at hand."
    $ hermione_perm_expand = True
    call update_her_uniform
    ">You hear a faint popping as Hermione's shirt fails to hold back her rapidly expanding breasts."
    call her_main("!!!","body_18")
    call her_main("[genie_name], this is ridiculous!","body_28")
    call her_main("I can't be expected to go to class looking like this!","body_29")
    m "Why not? I don't think they're that much bigger than normal."
    call her_main("Are you kidding me?","body_66")
    call her_main("They're {size=+5}humungous!{/size}","body_77")
    m "Well if you want them to go back to normal..."
    call her_main("What? Do you have an antidote?","body_68")
    m "Not an antidote, but I do have a method that would alleviate the swelling."
    call her_main("...","body_61")
    call her_main("I'm listening...","body_09")
    m "Well as far as I can tell, you're breasts are swelling due to an excess supply of milk."
    call her_main("...","body_61")
    m "If we somehow got it all out of there, I'm sure they'd revert to normal size in no time at all."
    call her_main("...","body_72")
    call her_main("You can't be serious!","body_79")
    call her_main("Are you suggesting that I be milked! Like some sort of animal!","body_81")
    m "I'm simply offering a way to fix your problem."
    m "If you don't want my help then I'm afraid you'll have to go to class in your current condition."
    call her_main("*hmph*","body_09")
    call her_main("It can't be any worse than being milked.","body_08")
    call her_main("Honestly, [genie_name], I'm shocked that you would even suggest something so completely ridiculous.","body_07")
    call her_main("I think I better get going...","body_12")
    m "Well, 20 points to \"gryffindor\""
    $ gryffindor += 20
    call her_main("Thanks...","body_17")
    $ milking = -1

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

label potion_scene_11_2: #Milking potion part 2
    #Genie offers hermione the potion again
    #She reluctantly accepts, but says that she expects to be paid double.
    #takes potion
    #comments on taste
    #wait
    #breasts expand
    #Genie offers milking
    #Hermione reluctantly accepts
    #Pulls out machine
    #Hermione shocked, expected to be by hand
    #Tries to refuse
    #Genie says she has already agreed
    #Upset, she puts on the milker
    #Slowly starts to work
    #Hermione is Cautious at first but gradually starts to enjoy it
    #starts to enjoy it a little too much
    #starts moaning, gets close to cumming
    #milking stops
    #she is somewhat upset but goes to class wearing expanded clothes
    m "[hermione_name], how would you like to try some nice milk?"
    call her_main("...","body_09")
    call her_main("is this the damn milk potion again sir?","body_30")
    m "maybe..."
    ">You hand her the cloudy potion."
    ">Hermione cautiously smells the mixture."
    call her_main("It is!","body_12")
    call her_main("...","body_09")
    call her_main("well...","body_08")
    call her_main("if you want me to drink this damn potion again...","body_08")
    call her_main("I have two conditons...","body_12")
    m "Name them."
    call her_main("One!","body_30")
    call her_main("I demand to be paid one hundred points!","body_30")
    call her_main("Two!","body_30")
    call her_main("I expect you to make the milking stop...","body_32")
    m "Deal!"
    call her_main("Well alright then...","body_34")
    ">Hermione takes one last look at the potion before closing her eyes..."
    hide screen hermione_blink
    show screen ch_potion
    call her_main("...","body_125")
    ">Hermione quickly gulps down the potion."
    hide screen ch_potion
    show screen hermione_blink
    call her_main("Ah...","body_126")
    call her_main("That doesn't actually taste too bad.","body_46")
    m "Is it just like cows milk?"
    call her_main("Sort of...","body_08")
    call her_main("It's a little sweeter...","body_44")
    call her_main("but not in a bad way...","body_54")
    call her_main("It also looks a little more yellow.","body_71")
    m "Yes, well, you should notice it start to affect you soon."
    call her_main("Hmmm...","body_73")
    call her_main("well how are you going to solve the milk problem [genie_name]?","body_87")
    call her_main("Am I going to have to stand here...","body_78")
    call her_main("With my shirt off...","body_105")
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call update_her_uniform
    ">Hermione quickly removes her top."
    call her_main("while you use your rough hands to milk me...","body_106")
    call her_main("like some sort of animal!","body_123")
    m "Not quite..."
    ">YOu hand her the milking harness."
    call her_main("What's this???","body_130")
    m "A milker."
    call her_main("Professor, Do you really expect me to put this on?","body_131")
    m "unless you want to go to class with those puppies full of milk."
    call her_main("but...","body_132")
    call her_main("Can't you just do it by hand...","body_121")
    call her_main("I though it would be just like when you play with them normally...","body_122")
    m "No can do. I don't think I'd be able to get it all out before your classes anyway"
    call her_main("I'm sure there's tim-","body_60")
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded.png" 
    ">You notice hermione's breasts slight to swell slightly."
    call her_main("!!!","body_208b")
    call her_main("[genie_name], they're growing rather quickly!","body_208")
    m "This is all perfectly normal."
    call her_main("please...","body_197")
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png" 
    ">Hermione's breasts start to visibly swell again."
    call her_main("ughhh...","body_106")
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
    ">You notice hermione's breasts swell for the final time."
    call her_main("!!!","body_182b")
    call her_main("[genie_name], this is ridiculous!","body_182")
    call her_main("do they have to be so big?","body_187")
    m "Yes."
    call her_main("...","body_185")
    call her_main("pervert.","body_186")
    m "Well seeing as how they've reached full size..."
    call her_main("*hmph* Fine!","body_79")
    call her_main("Let me just put on your weird milking device that you own for some reason!","body_103")
    m "Well technically I'm just borrowing it, so if you could make sure not to break it..."
    call her_main("...","body_09")
    call her_main("Ugh... the things I put up with for this house.","body_17")
    ">hermione slowly slips the harness on."
    $ milking = 1
    call h_action("milk_breasts")
    call her_main("There! Happy now!","body_43", "blush")
    m "I mean if you could moo that would really Complete the picture..."
    call her_main("...","body_49", "blush")
    call her_main("can we just get this over with...","body_103", "blush")
    m "Um... It's enchanted..."
    "(Does it have an on switch)"
    call her_main("Wait... This is an enchanted item? Please don't turn it on-","body_117", "blush")
    ">You hear a faint noise as the harness on hermione's chest springs to life."
    $ milking = 2
    call h_action("milk_breasts")
    call her_main("!!!","body_213", "blush")
    call her_main("{size=+5}OFF! TURN OFF!{/size}","body_132", "blush")
    m "I think you need to wait until it's done."
    call her_main("Ugh...","body_219", "blush")
    call her_main("I can't...","body_131", "blush")
    call her_main("It's too much...","body_131", "blush")
    m "What's wrong?"
    call her_main("Ugh... it's the sucking...","body_131", "blush")
    call her_main("It's too intense!","body_132", "blush")
    m "Can't you just ride it out?"
    call her_main("Ugh.... maybe... {p}I'll try.","body_134", "blush")
    ">You wait a few more mintues as hermione is milked in front of you."
    $ milking = 3
    call h_action("milk_breasts")
    call her_main("...","body_135", "blush")
    ">Her expression slowly fades from discomfort to pleasure."
    call her_main("...","body_133", "blush")
    $ milking = 4
    call h_action("milk_breasts")
    ">The machine makes a pleasant sounding click as it looks to turn off."
    m "Alright, well, look like you're good to head off to class."
    call her_main("What?","body_12", "blush")
    call her_main("Can't you leave it on...","body_131", "blush")
    m "I'm afraid not."
    m "(I don't even know how it turns on...)"
    call her_main("But I was so close...","body_132", "blush")
    call her_main("...","body_103", "blush")
    call her_main("Fine... I better get to potions class then...","body_73", "blush")
    ">Hermione takes off the harness. You see the passing look of regret on her face."
    call h_action("none")
    $ hermione_wear_top = True
    $ hermione_wear_bra = True
    $ hermione_perm_expand = True
    call update_her_uniform
    m "Feel better?"
    call her_main("Surprisingly yes...","body_82", "blush")
    call her_main("They even seem like they've shrunk a little bit.","body_87", "blush")
    call her_main("So you're sure they're not going to leak anymore?","body_08", "blush")
    m "oh um, no of course not..."
    call her_main("...","body_07", "blush")
    call her_main("well I'd like to be paid now [genie_name]...","body_12", "blush")





    m "Oh yes, quite right. 100 points to \"gryffindor\"!"
    $ gryffindor += 100
    call her_main("Thank you sir...","body_08", "blush")
    call her_main("(Although I still have to head to class with these huge things...)","body_12", "blush")
    call her_main("(not that I mind the extra attention...)","body_105", "blush")

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ milking = 0

    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    $ hermione_takes_classes = True
    $ hermione_sleeping = True #this is intentional 
    $ hermione_perm_expand = False
    jump day_main_menu

label potion_scene_11_3: #Milking potion part 3
    $ milking = 0
    #Genie offers hermione the potion
    #Agrees on the condition that she milks him
    #Genie agrees
    #option to add extra ingredient
    #Hermione drinks potion
    #Comments that the milk tastes sweeter than regular milk
    #wait
    #Breasts expand
    #takes her top off

    #option 1 (futa)

    #option 2 (Permanent expansion)
    m "[hermione_name], feel like a milkshake?"
    call her_main("Really? Strawberry please!","body_80")
    m "I've only got vanilla sorry..."
    ">You hand her the cloudy potion."
    ">Hermione cautiously smells the mixture."
    call her_main("This is that damn milk again!","body_119")
    call her_main("...","body_09")
    call her_main("I wanted a milkshake...","body_71")
    m "I'm sure if you shake the bottle it'll go frothy."
    call her_main("It's not the same!","body_30")
    call her_main("There's no sugar or flavouring!","body_09")
    if potion_version > 1:
        m "well, this one does have an extra ingredient..."
        call her_main("Really?","body_122")
        call her_main("Is it Strawberry?","body_121")
        m "WHy don't you have a taste and find out?"
        call her_main("Alright then...","body_08")
        call her_main("(I hope it's Strawberry!)","body_80")
    else:
        m "Just drink it..."
        call her_main("*hmph* fine...","body_08")
        call her_main("(At the very least he should have added chocolate flavouring...)","body_08")
    ">Hermione takes one last look at the potion before closing her eyes..."
    hide screen hermione_blink
    show screen ch_potion
    ">Hermione quickly gulps down the potion."
    hide screen ch_potion
    show screen hermione_blink
    call her_main("Ah...","body_126")
    call her_main("That wasn't Strawberry!","body_79")
    m "Did you really think it would be?"
    call her_main("I mean... Sort of?","body_73")
    call her_main("you are a wizard after all...","body_71")
    call her_main("the house elfs make me a milkshake whenever i ask...","body_61")
    m "Speaking of milkshakes!"
    ">You notice hermione's breasts start to swell..."
    call her_main("Ugh... this always feels so weird...","body_118")
    call her_main("I better take my shirt off before \'they\' rip the buttons...","body_07")
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call update_her_uniform
    ">Hermione quickly removes her top."
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded.png" 
    if not potion_version == 2: #Orgasms while milking
        ">You notice hermione's breasts start to grow a little more."
        call her_main("!!!","body_119")
        call her_main("ugh...","body_106")
        m "mmmm, just like that."
        call her_main("(this is so weird...)","body_118")
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png" 
        ">Hermione's breasts start to visibly swell again."
        call her_main("!!!","body_119", "blush")
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        ">You notice hermione's breasts swell for the final time."
        call her_main("!!!","body_118", "blush")
        call her_main("[genie_name], this is ridiculous!","body_79", "blush")
        call her_main("did you make the potion stronger this time?","body_103", "blush")
        m "What are you talking about girl, they're the same size as always."
        call her_main("are you sure...","body_09", "blush")
        ">Hermione jiggles her boobs side to side."
        call her_main("They just feel so much ...heavier... than before.","body_73", "blush")
        m "Well seeing as how you emptied them of their milk last time, maybe they made more..."
        call her_main("they better not have...","body_132", "blush")
        call her_main("just hand me the milker so I can get to class...","body_79", "blush")
        m "Is that the only reason you want it?"
        call her_main("What? Why else would I want it?","body_107", "blush")
        m "I seem to remember you enjoying yourself with it last time."
        call her_main("You really are disgusting sometimes [genie_name]...","body_69", "blush")
        m "Whatever you say..."
        ">You hand hermione the harness."
        ">hermione takes it from your hands and slowly slips it on, taking care to make sure the cups fit."
        $ milking = 1
        call h_action("milk_breasts")
        call her_main("...","body_182b", "blush")
        m "are you sure you can't moo?..."
        call her_main("...","body_105", "blush")
        call her_main("{size=-5}moo...{/size}","body_107", "blush")
        m "what was that?"
        call her_main("I'm not saying it again [genie_name]... {size=-5}once is enough...{/size}","body_103", "blush")
        call her_main("...","body_73")
        call her_main("on!","body_131")
        ">You hear a faint noise as the harness on hermione's chest springs to life."
        $ milking = 2
        call h_action("milk_breasts")
        call her_main("!!!","body_105", "blush")
        call her_main("Ugh... it feels different this time...","body_131", "blush")
        call her_main("like there's so much more in my breasts...","body_132", "blush")
        call her_main("and it all wants to come out...","body_133", "blush")
        call her_main("It's too much...","body_134", "blush")
        m "What's wrong?"
        call her_main("ah... it's the sucking...","body_136", "blush")
        call her_main("It's not like before!","body_134", "blush")
        m "is it hurting you?"
        call her_main("ah.... no... {p}It's not bad...","body_133", "blush")
        $ milking = 3
        call h_action("milk_breasts")
        call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","body_123", "blush")
        ">You notice the canister in front of her fill with milk at an alarming rate..."
        call her_main("ah... it's so good...","body_136", "blush")
        $ milking = 4
        call h_action("milk_breasts")
        ">The machine makes a pleasant sounding click as it looks to turn off."
        m "Alright, well, look like you're good to head off to class."
        call her_main("What? but sir...","body_131", "blush")
        call her_main("they're still so full...","body_132", "blush")
        m "it looks like the machines full I'm afraid."
        call her_main("(But I was so close...)","body_131", "blush")
        call her_main("ah... and if I go to class like this I'll leak everywhere!","body_132", "blush")
        m "well if you empty the cannister It'll probably turn back on."
        call her_main("empty it...","body_122", "blush")
        ">Hermione takes a look at the full milk cannister."
        call her_main("Can I just pour it out on the floor then?","body_71")
        m "And waste all that nutritious milk?"
        menu:
            "-make her drink it-":
                call her_main("Do you want to drink it then [genie_name]?","body_122", "blush")
                m "Um, I'm afraid not... I just had a big bowl of cereal."
                call her_main("...","body_71", "blush")
                call her_main("Well then do you have a bottle for me to store it in...","body_122", "blush")
                m "fresh out..."
                call her_main("...","body_103", "blush")
                m "I'm afraid you'll have to drink it yourself."
                call her_main("...","body_105", "blush")
                call her_main("{size=-5}alright...{/size}","body_107")
                m "Really?"
                call her_main("Well it's not like I can go to class leaking milk again...","body_103", "blush")
                call her_main("and besides, it's not the worst feeling in the world...","body_118", "blush")
                call her_main("I wouldn't mind giving the machine another go...","body_121", "blush")
                m "Well, bottoms up!"
                call her_main("...","body_71", "blush")
                $ milking = 5
                call h_action("milk_breasts")
                ">Hermione gives the cannister one final look before unscrewing it and putting it to her lips."
                call her_main("(For gryffindor!)","body_30")
                ">She takes a mouthful of her own milk."
                call her_main("...","body_125", "blush")
                call her_main("*gulp*","body_126", "blush")
                ">She takes the last half into her mouth."
                call her_main("...","body_125")
                call her_main("*gulp*","body_126", "blush")
                call her_main("ah...","body_123", "blush")
                call her_main("I think I'll need to skip a meal after all this milk...","body_122", "blush")
                ">She slowly screws the cannister back into milker."
                $ milking = 1
                call h_action("milk_breasts")
                call her_main("...","body_124", "blush")
                call her_main("on!","body_127", "blush")
                ">The milker once again comes to life as it starts to milk Hermione for a second time."
            "-drink it yourself-":
                call her_main("Do you want to drink it then [genie_name]?","body_122", "blush")
                m "Waste not, want not!"
                call her_main("...","body_119", "blush")
                call her_main("well, here you are then...","body_117", "blush")
                $ milking = 5
                call h_action("milk_breasts")
                ">Hermione gives the cannister one final look before unscrewing it and handing it to you."
                call her_main("(weirdo...)","body_118", "blush")
                ">you take a mouthful of her milk."
                m "Mmmmmm... Delicious!"
                call her_main("...","body_122", "blush")
                call her_main("really? You liked my milk?","body_107", "blush")
                m "More than water from an oasis!"
                call her_main("...","body_12", "blush")
                call her_main("well...","body_105")
                call her_main("Are you going to finish it?","body_111", "blush")
                ">You finish the cannister in one final mouthful."
                call her_main("...","body_75", "blush")
                ">She slowly screws the cannister back into milker."
                $ milking = 1
                call h_action("milk_breasts")
                call her_main("(I can't believe he liked it...)","body_46", "blush")
                call her_main("(maybe it does taste good...)","body_56", "blush")
                call her_main("...","body_124", "blush")
                call her_main("on!","body_127", "blush")
                ">The milker once again comes to life as it starts to milk Hermione for a second time."


        call her_main("!!!","body_123", "blush")
        call her_main("ugh... it's so gooood...","body_106", "blush")
        $ hermione_dribble = True
        $ milking = 2
        call h_action("milk_breasts")
        call her_main("ah... it's like the straps are massaging me while it sucks...","body_133", "blush")
        call her_main("mmmm... it's amazing...","body_134", "blush")
        ">Hermione lets the machine continue it's work."
        $ milking = 3
        call h_action("milk_breasts")
        call her_main("ah... I think that's all of it [genie_name]...","body_73", "blush")
        ">You notice the amount of milk coming from hermione's breasts has almost stopped."
        m "How was it?"
        call her_main("it felt amazing...","body_106", "blush")
        call her_main("it even almost made me cum...","body_124", "blush")
        call her_main("but you can turn it off now...","body_122", "blush")
        m "Um..."
        ">The machine struggles to suck any more milk from hermione's heaving chest."
        m "I'm not sure how... I think it only shuts off when it's full?"
        call her_main("well I don't think it's going to be able to get much more-","body_120", "blush")
        ">You hear the harness start to whir, like a vacuum cleaner caught on carpet."
        call her_main("!!!","body_197", "blush")
        ">You hear a strange click come from the harness."
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("Ah!!!","body_194", "blush")
        ">You see a small squirt of milk come out of hermione's nipples."
        $ hermione_squirt = False
        ">The cannister is still barely more than half full."
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+5}Ah!!!{/size}","body_134", "blush")
        ">Another small squirt of milk comes out of hermione's nipples."
        $ hermione_squirt = False
        call her_main("{size=+5}It's making me cum!{/size}","body_132", "blush")
        call her_main("{size=+5}why is it-{/size}","body_131")
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_133", "blush")
        $ hermione_squirt = False
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_136", "blush")
        $ hermione_squirt = False
        show screen blkfade
        with d3
        ">The machine continues for another couple of minutes. Each crack is accompanied by a small squirt of milk into the cups..."
        $ milking = 4
        call h_action("milk_breasts")
        hide screen blkfade 
        with d3

        call her_main("...","body_135", "blush")
        ">Hermione stands before you, unable to speak."
        m "Oh um... 20 points to \"gryffindor\"!"
        $ gryffindor += 20
        call her_main("...","body_135", "blush")
        ">And I'll be needing this back."
        call her_main("...","body_135", "blush")
        show screen blkfade
        with d3
        ">You slowly remove the milk filled harness. There are red marks, surrounding her tender looking nipples, where the cups were."
        call h_action("none")
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        m "Hmmm, maybe we overdid it a little today."
        hide screen blkfade
        call her_main("...","body_138", "blush")
        m "Why don't you head back to your room... I think you've earned a day off."
        call her_main("yes...","body_133", "blush")
        call her_main("I'll go now...","body_134", "blush")
        m "Maybe you should get dressed first..."
        call her_main("...","body_136", "blush")
        ">Hermione slowly dresses herself, fumbling at every point."
        $ hermione_wear_panties = True
        $ hermione_wear_bra = True
        $ hermione_wear_skirt = True
        $ hermione_wear_top = True
        $ hermione_perm_expand = True
        $ hermione_dribble = False
        call update_her_uniform
        call her_main("good bye sir...","body_133", "blush")
        if potion_version == 2:
            ">Hermione's breasts will now be permanently large thanks to Snape's added ingredient."
            ">however, Making her take the potion again may reset the effect..."



    else: #futa variant
        ">You notice hermione's breasts start to grow a little more."
        call her_main("!!!","body_119")
        # change boobs
        call her_main("ugh...","body_106")
        m "mmmm, just like that."
        call her_main("(this is so weird...)","body_118")
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png" 
        ">Hermione's breasts start to visibly swell again."
        call her_main("!!!","body_119")
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_xlarge.png" 
        ">You notice hermione's breasts swell for the final time."
        call her_main("!!!","body_118")
        call her_main("[genie_name], this is ridiculous!","body_79")
        call her_main("did you make the potion stronger this time?","body_103")
        m "Well there was an extra ingredient in there..."
        call her_main("What? are my boobs going to get even bigger?","body_103")
        ">Hermione jiggles her boobs side to side."
        call her_main("I don't think I'd be able to stand!","body_73")
        m "Your breasts shouldn't grow any bigger..."
        call her_main("Oh...","body_59")
        m "You may notice something else start to grow however."
        call her_main("What? Not cat ears again please...","body_69")
        m "Don't worry, it's a human organ.?"
        call her_main("...","body_119")
        call her_main("wait...","body_118")
        call her_main("you don't mean...","body_85")
        call her_main("you wouldn't... would you?","body_103")
        m "We'll just have to wait and see..."
        call her_main("You really are a disgusting pervert [genie_name]...","body_186")
        m "Whatever you say..."
        call her_main("Please tell me I'm not going to grow a damn d-","body_118")
        call her_main("...","body_119")
        call her_main("You damn {size=+10}pervert!{/size}","body_132")
        $ hermione_futa = True
        $ hermione_wear_skirt = False
        $ hermione_wear_panties = False
        $ h_action_show_skirt = False
        ">Hermione removes her skirt, revealing a throbbing erection."
        g9 "Woah! Nice..."
        call her_main("Nice? How is this nice?","body_86")
        call her_main("I have a damn {size=+10}cock!{/size}","body_76")
        m "Come on [hermione_name]... where's your sense of adventure?"
        call her_main("Adventure?","body_79")
        call her_main("Going into the chamber of secrets was an adventure sir...","body_08")
        call her_main("Standing in my headmasters office while he makes me drink some random potion he probably found in the gutter-","body_30")
        call her_main("-That makes me have huge, {size=+3}lactating{/size}, {size=+5}tits{/size} and a giant {size=+10}{b}DICK{/b}{/size} is {size=+2}not {size=+2}an {size=+4}adventure!{/size}","body_86")
        m "Don't forget about the magical milking machine..."
        ">You hand hermione the milking harness."
        m "Surely this makes it an adventure..."
        call her_main("What do you expect me to do with this?","body_09")
        call her_main("It's hardly going to be able to get rid of this {size=+10}DICK{/size} now is it.","body_77")
        m "Actually, it should."
        m "(I hope it does anyway... Snape did say it was magic.)"
        call her_main("really?","body_79")
        m "Really, really."
        call her_main("Ugh, fine... (the stuff I put up with)","body_103")
        ">hermione takes it from your hands and goes to put it on."
        call her_main("Where's my stupid dick supposed to go...","body_117")
        call her_main("It's in the way of the cannister.","body_118")
        m "Try sticking it into the bottom of the cannister."
        call her_main("What... why would that-","body_79")
        $ milking = 1
        call h_action("milk_breasts")
        $ h_action_show_skirt = False
        call her_main("!!!","body_133", "blush")
        m "how's that?"
        call her_main("I'm sorry about being angry before [genie_name]...","body_138", "blush")
        call her_main("I didn't know it would feel like this...","body_136", "blush")
        m "like what?"
        call her_main("It's so fricking good...","body_134", "blush")
        call her_main("I never though sex could be like this...","body_133")
        call her_main("being inside something...","body_134")
        call her_main("It's the best!","body_136", "blush")
        call her_main("At this rate I'll cum before we even have to turn the thing on-","body_138", "blush")
        ">You hear a faint noise as the harness on hermione's chest springs to life."
        $ milking = 2
        call h_action("milk_breasts")
        $ h_action_show_skirt = False
        call her_main("!!!","body_123", "blush")
        call her_main("no!","body_140", "blush")
        call her_main("Stop it!","body_141", "blush")
        call her_main("{size=+5}I'm serious!!!{/size}","body_142", "blush")
        call her_main("{size=+10}It's too much... TURN it off!!!{/size}","body_130", "blush")
        m "What's wrong?"
        call her_main("ah... it's sucking {b}everything{/b}...","body_134", "blush")
        call her_main("ah... and the milk is splashing on my {image=textheart}dick{image=textheart}......","body_136", "blush")
        m "is it hurting you?"
        call her_main("ah.... no... {p}It's just too good...{image=textheart}","body_123")
        $ milking = 3
        call h_action("milk_breasts")
        $ h_action_show_skirt = False
        call her_main("ah...{image=textheart}{image=textheart}{image=textheart}","body_133")
        ">You notice the canister in front of her fill with milk at an alarming rate..."
        call her_main("ah... please [genie_name]...","body_141", "blush")
        call her_main("ah... you have to turn it off...","body_143", "blush")
        call her_main("{size=-2}i'll {size=-2}go {size=-2}insane {size=-2}if {size=-2}you {size=-2}don't...{/size}","body_138", "blush")
        $ milking = 4
        call h_action("milk_breasts")
        $ h_action_show_skirt = False
        ">You notice the cannister fill, yet the machine keeps working."
        call her_main("What? but it's full...","body_71", "blush")
        call her_main("it should turn off...","body_142", "blush")
        call her_main("please... let it turn off...","body_145", "blush")
        m "(What did snape say again? untellable extension ham?)"
        m "Well i should have mentioned something about that cannister being extended invisibly...."
        call her_main("Did you put an undetectable extension charm on this cannister?","body_144", "blush")
        call her_main("{size=+5}did you?!{/size}","body_146", "blush")
        m "Possibly."
        call her_main("no...","body_147", "blush")
        ">Hermione takes a look at the full milk cannister."
        call her_main("Will it ever stop?","body_143", "blush")
        m "ahhhh..."
        call her_main("!!!","body_142", "blush")
        call her_main("ugh... {image=textheart}it's so{image=textheart} gooood...","body_138", "blush")
        $ hermione_dribble = True
        call her_main("ah... the straps are massaging me while it sucks my dick...","body_134", "blush")
        call her_main("mmmm... it's amazing...{image=textheart}{image=textheart}","body_136", "blush")
        ">Hermione lets the machine continue it's work."
        call her_main("...","body_135", "blush")
        ">You notice the amount of milk coming from hermione's breasts has almost stopped."
        call her_main("it feels amazing...","body_136", "blush")
        call her_main("it's made me cum so much...","body_134", "blush")
        ">The machine struggles to suck any more milk from hermione's heaving chest."
        m "Well hopefully it has a safety mechanism for when you're out of milk..."
        call her_main("well that should be soon-","body_138", "blush")
        ">You hear the harness start to whir, like a vacuum cleaner caught on carpet."
        call her_main("!!!","body_119", "blush")
        ">You hear a strange click come from the harness."
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+15}!!!{image=textheart}{image=textheart}{image=textheart}!!!{/size}","body_123", "blush")
        ">You see a small squirt of milk come out of hermione's nipples."
        $ hermione_squirt = False
        ">The cannister still looks completely full."
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_123", "blush")
        ">Another small squirt of milk comes out of hermione's nipples."
        $ hermione_squirt = False
        call her_main("{size=+5}It's making me cum so {b}hard{/b}...{/size}","body_138", "blush")
        call her_main("{size=+5}why is it-{/size}","body_139")
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_136", "blush")
        $ hermione_squirt = False
        "*Zzzzkkk*"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ hermione_squirt = True
        call her_main("{size=+5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_134", "blush")
        $ hermione_squirt = False
        show screen blkfade
        with d3
        ">The machine continues for another couple of minutes. Each crack is accompanied by a small squirt of milk into the cups and a pulse of her cock into the cannister..."
        $ milking = 4
        call h_action("milk_breasts")
        $ h_action_show_skirt = False
        ">You let it continue for a little longer before it finally stops."
        hide screen blkfade 
        with d3

        call her_main("{size=-10}t-turn it...{/size}","body_141")
        ">Hermione stands before you, barely able to speak."
        call her_main("{size=-8}t-turn it...{/size}","body_141")
        call her_main("{size=-6}t-turn it...{/size}","body_141")
        call her_main("{size=-4}t-turn it... up...{/size}","body_142")
        m "I think you've had enough... 20 points to \"gryffindor\"!"
        $ gryffindor += 20
        call her_main("...","body_141")
        ">And I'll be needing this back."
        call her_main("...","body_143")
        show screen blkfade
        with d3
        ">You slowly remove the milk filled harness. There are red marks, surrounding her tender looking nipples, where the cups were."
        call h_action("none")
        $ hermione_wear_panties = False
        $ hermione_wear_bra = False
        $ hermione_wear_skirt = False
        $ hermione_wear_top = False
        $ hermione_futa = False
        $ hermione_dribble = False
        ">As you pull the heavy cannister off her cock it flops down before wilting away into nothingness."
        m "(eww...)"
        m "Hmmm, I think you probably overdid it a little today."
        hide screen blkfade
        call her_main("{size=-6}more...{/size}","body_142")
        m "Why don't you head back to your room... I think you've earned another day off."
        call her_main("yes...","body_141")
        call her_main("I'll go now...","body_143")
        m "Maybe you should get dressed first..."
        call her_main("...","body_142")
        ">Hermione slowly dresses herself, fumbling at every point."
        $ hermione_wear_panties = True
        $ hermione_wear_bra = True
        $ hermione_wear_skirt = True
        $ hermione_wear_top = True
        call her_main("good bye sir...","body_143")



    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    $ milking = 0
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    $ hermione_takes_classes = True
    $ hermione_sleeping = True
    if not potion_version == 3:
        $ hermione_perm_expand = False
    jump day_main_menu



label potion_scene_11_1_2: #Milking potion part 1 night time
    $ aftersperm = True
    $ milking = 0
    ">Hermione bursts through your door."
    call her_main("Professor! why didn't you warn me about this!","body_77")
    m "About what? I told you your breasts would expand."
    call her_main("Look at my shirt!","body_76")
    m "Hmmm, seems like you had a bit of an accident."
    call her_main("An accident?","body_08")
    call her_main("I've been leaking milk all day!","body_86")
    m "It doesn't seem that bad..."
    call her_main("This is the third shirt that I've had to wear today!","body_04")
    call her_main("All the others are soaked through!","body_77")
    call her_main("Even my vest is soaked...","body_09")
    m "Well I did offer to relieve your issue..."
    call her_main("by milking me like some sort of... animal!","body_05")
    call her_main("I'm upset you'd even think that would be a possibility.","body_51")
    m "Well it would have solved your \'problem\'."
    call her_main("...","body_08")
    call her_main("Well I expect to be paid extra after this humiliation.","body_50")
    m "how much?"
    call her_main("30 points.","body_61")
    m "Fine, 30 points to \"gryffindor\"."
    $ gryffindor += 30 
    call her_main("*hmph*","body_50")
    call her_main("So when are these \'things\' going to go away? Or do I have to go get one of the nurses to shrink them?","body_51")
    m "They should go back to normal Sometime tonight."
    call her_main("good...","body_08")
    call her_main("but don't think I've forgiven you!","body_04")
    ">Hermione storms out in a huff."
    $ mad =+ 10
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    $ hermione_sleeping = True
    $ hermione_perm_expand = False
    $ aftersperm = False
    m "(bitches... you'd think she'd be happy to get some {size=+5}big kahunas{/size} for free!)"
    jump day_main_menu
    #comes back after class
    #shirt covered in milk stains
    #furious at genie 
    #Genie responds saying he should have let him milk her
    #Hermione is angry again at him for suggesting it
    #demands more points 
    #asks when they're going to go away
    #genie says she has to get the milk out of them
    #offers to milk her again
    #refuses and says she can take care of it herself
    #leaves

label potion_scene_11_2_2: #Milking potion part 2 night time
    m "asd"
    #comes back after class
    #breasts still expanded
    #genie asks her how her day was
    #She had a good day
    #Appreciates the attention from everyone
    #Milking prevented her from leaking
    #Says she wouldn't mind taking the potion again some time












