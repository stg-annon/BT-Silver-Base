
###PUBLIC EVENTS (more about shaming than whoring herself off to other people) There will be points for these events at the early stages

###Here's the current list of planned public shaming events, more may be added.
#Panty Thief - Done
#Wear a shorter skirt
#Wear a more revealing shirt 
#Walk of shame 
#Blowjob under desk in front of someone - Unsure about this one
#Cum walk




################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your panties" ###############################
label hg_ps_PantyThief: #(Whoring = 3 - 5)
    hide screen hermione_main
    with d3
    m "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    m "[hermione_name]?"
    call her_main("I am listening, [genie_name].")
    m "I will need your panties..."
    
    if whoring <=2:
        jump too_much
    
    $ menu_x = 0.5 #Menu is moved to the left side.
    show screen blktone 
    show screen ctc
    with d3
    
    call her_main(xpos=120,ypos=0)
    
    if hg_ps_points[hg_ps_PantyThief_ID] == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_heart = 1 #Event hearts level (0-3)
        $ hg_ps_hearts[hg_ps_PantyThief_ID] = 1 #Event hearts level (0-3)
        
        call her_main("W-what?","body_11")
        her "My... panties...?"
        her "[genie_name], this is..."
        m "This is the favour I will be buying from you today, [hermione_name]..."
        m "If you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You need my...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("...panties, [genie_name]?","body_47")
        m "Yes I do..."
        call her_main("May I ask what you are planning to do with them...?","body_66")
        m "Ehm...I'm conducting research..."
        her "But this is kind of inappropriate, don't you think?"
        m "But don't you hate it that some of the girls from \"Slytherin\"..."
        m "Are selling favours for house points, [hermione_name]?"
        call her_main("Yes I do!","body_47")
        call her_main("(Those \"Slythering\" tramps have no dignity.)","body_12")
        m "Well, there you go then!"
        call her_main("Huh?","body_66")
        m "Beat them at their own game!"
        call her_main("What?","body_14")
        m "Yes! Don't just put the \"Gryffindor\" house back on top..."
        m "But do it by beating them at their own game!"
        call her_main("[genie_name]...","body_11")
        m "A headmaster cannot play favourites, but you know how I feel about \"Gryffindor\"..."
        m "I wish I could give you the points but that would ruin the system..."
        show screen blktone8
        hide screen hermione_main
        with d3
        ">Suddenly Hermione extends her arm to you..."
        ">You see that she is clutching a little piece of fabric in her fist..."
        #">Her panties? You can't help but wonder when she managed to take them off..."
        m "??!"
        ">You acquired Hermione's panties..."
        hide screen blktone8
        with d3
        call her_main("Just take them [genie_name]...","body_67")
        m "What? When did you?"
        her "Your speech was so moving..."
        her "You are so right, [genie_name]! I shall beat them at their own game!"
        her "My classes are about to start, so I should probably go now..."
        call her_main("...........","body_23",xpos=370)
        call her_main("...I hope nobody will notice that I have no underwear on today...","body_29")
        call her_main("Oh, and I will be back tonight to pick them up, [genie_name].","body_31")
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        call her_main(".............","body_34")
        jump hg_ps_PantyThief_ends

    else: #<========================================================================================== FIRST EVENT!
        if hg_ps_points[hg_ps_PantyThief_ID] >= 1:
            her "Again, [genie_name]?"
            m "Yes again..."
        her "Here..."
        if whoring >= 12: #LEVEL 05
            hide screen hermione_main
            with d3
            ">Hermione pulls her panties out of her pocket..."
            m "What?"
            call her_main("Yes, I had a feeling that you might ask for these today, [genie_name].","body_45")
            m "A feeling?"
            call her_main("Well, to be completely honest I just do not bother to wear them much anymore...","body_68")
        else:
            hide screen hermione_main
            with d3
            ">Hermione takes off her panties and hands them over to you..."
        ">Hermione's panties acquired."
        call her_main("Well, the classes are about to start, so I'd better go now...","body_15")
    
    label hg_ps_PantyThief_ends:
        
    $ hg_ps_InProgress[hg_ps_PantyThief_ID] = True #True when Hermione has no panties on.
    
    hide screen blkfade
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen chair_02
    hide screen hermione_blink
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen ctc
    show screen genie
    with d3
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door.
    with Dissolve(.3)
    
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
        $ hermione_sleeping = True
        jump night_main_menu
label hg_ps_PantyThief_soaked:### PANTIES SOAKED IN CUM ###
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        call her_main("Hm....?","body_71",xpos=120)
        call her_main("[genie_name]? What is this?","body_05")
        her "What have you done to them?"
        call her_main("They are covered in something slimy...","body_07")
        menu:
            "\"An experiment went wrong\"":
                call her_main("An experiment went wrong, [genie_name]?","body_02")
                m "Yes... Or maybe I should rather say..."
                g9 "\"An experiment went very right\"? He-he..."
                call her_main(".....................?","body_07")
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Some top secret research I'm conducting."
                m "I can't discuss it with a student."
                call her_main("................................","body_05")
            "\"You gave them to me like this!\"":
                her "I most certainly did not, [genie_name]!"
                her ".........................."
        call her_main("Well, these will require some serious cleaning before I can put them on again...","body_71")
        m "Or you could put them on now."
        call her_main("What?","body_14")
        call her_main("I really would rather not, [genie_name]...","body_13")
        menu:
            "\"Put them on or lose the points!\"":
                $ mad +=7
                call her_main("What?","body_72")
                her "[genie_name], you are joking, right?"
                m "I am not..."
                call her_main("B-but...","body_31")
                call her_main("........................................","body_33")
                call her_main("(Must you always have your way, [genie_name]?)","body_47")
                m "What was that, [hermione_name]?"
                call her_main("It's nothing, [genie_name].","body_30")
                her "Putting my panties back on!"
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">Hermione hesitantly puts on her panties..."
                ">A tiny stream of cum trickles down one of her legs..."
                ">Hermione looks very uncomfortable..."
                hide screen blktone8
                with d3
                call her_main("......................","body_34")
            "\"Well, suit yourself...\"":
                pass
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        call her_main("My panties...","body_71")
        call her_main("What happened to them [genie_name]?","body_73")
        menu: 
            "\"An experiment went wrong.\"":
                her "Hm..."
                her "I see..."
            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."
        hide screen hermione_main
        with d3
        ">Hermione gives her cum-soaked underwear a quizzical look..."
        call her_main("Seems like these will require some serious cleaning before I can put them on again...","body_71")
        m "Why not put them on now?"
        call her_main("Hm....?","body_17")
        call her_main("Well, I suppose I could wear them one more time before putting them into laundry...","body_71")
        hide screen hermione_main
        with d3
        show screen blktone8
        with d3
        ">Hermione puts the panties on..."
        hide screen blktone8
        with d3
        call her_main("(This feels funny...)","body_34")
        call her_main("Will this be all, [genie_name]?","body_44")
    if whoring >= 9 and whoring <= 15: #LEVEL 04+ (THIRD EVENT)
        call her_main("My panties...","body_71")
        if hg_ps_PantyThief_SoakedPantiesFlag:
            her "They are covered in something slimy again..."
        else:
            her "They are covered in something slimy..."
        her "And they smell funny..."
        call her_main("Hm... That smell...","body_29")
        her "It's familiar somehow..."
        call her_main("What exactly did you do to them, [genie_name]?","body_45")
        menu:
            "\"An experiment went wrong\"":
                her "An experiment, huh?"
                her "Of what nature?"
                call her_main("No, don't answer that... I think I know...","body_46")
            "\"You gave them to me like this!\"":
                her "I don't think so, [genie_name]."
                her "But it's alright if you don't want to tell me, [genie_name]..."
                her "I think I know exactly what happened to them..."
            "\"I came all over them!\"":
                call her_main("I knew it...","body_64")
                her "They reek of semen!"
        call her_main("Hm...","body_68")
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?","body_64")
        menu: 
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Well, if I must..."
            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"
        
        call her_main("I am only doing this to give my house a fair chance at winning the cup this year...","body_74")
        m "Right..."
        hide screen hermione_main
        with d3
        show screen blktone8
        with d3
        ">Hermione swiftly slides her drenched panties on..."
        hide screen blktone8
        with d3
    elif whoring > 15: ###New variant of the event
        call her_main("My panties...","body_78")
        if hg_ps_points[hg_ps_PantyThief_ID] >= 1:
            her "You came all over them again..."
        else:
            her "You came all over them..."
        call her_main("Hm...","body_68")
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?","body_64")
        menu: 
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Yes [genie_name]..."
                call her_main("I am only doing this to give my house a fair chance at winning the cup this year.","body_75")
                call her_main("I don't like how it feels at all...","body_78")
                m "Right..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">Hermione swiftly slides her drenched panties on..."
                call her_main("...","body_121")
                hide screen blktone8
                with d3
            "\"Why don't you clean them now?\"":
                $ cleaned_panties = True
                call her_main("Clean them How? You don't have a wash basin in here.","body_31")
                m "You're right, you'll have to use your mouth then."
                call her_main("My mouth?!","body_72")
                m "What's the big deal? It wouldn't be the first time you've tasted my cum."
                call her_main("It's a bit different! I wore these panties before I gave them to you.","body_30")
                call her_main("Not to mention that your cum is all cold and slimey...","body_32")
                m "Well in that case hand them back."
                call her_main("What? Can't I just put them on?","body_122") 
                m "I'm afraid not, you clean them now or you hand them back."
                call her_main("{size=-4}Fine...{/size}","body_118")
                m "What was that?"
                call her_main("I said I'll clean them ok!","body_132")
                m "Well..."
                call her_main("...","body_118")
                ">Hermione reluctantly puts her cum-soaked panties in her mouth."
                call her_main("Mmmmhhhhh!","body_42")
                m "That's it, not as bas as you thought now is it?"
                call her_main("...","body_222")
                m "Make sure you get them nice and clean now..."
                call her_main("*gulp*","body_224")
                m "That's it. Do you think they're clean yet."
                call her_main("*Mmmhhhmmm*","body_125")
                m "Well then you can probably take them out of your mouth."
                call her_main("*Ahhhhh*","body_135")
                m "There, nice and clean."
                call her_main("*Yes [genie_name]*","body_121")
    
    jump back_from_soaked
label hg_ps_PantyThief_complete: # WHORING LEVEL 02 <=================
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    
    show screen hermione_blink #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    call her_main("Good evening, [genie_name]...","body_01",xpos=370,ypos=0)
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Here are your panties.\"":
            if hg_ps_PantyThief_SoakedPantiesFlag:
                jump hg_ps_PantyThief_soaked
            else:
                her "Thank you, [genie_name]."
                her "And my payment?"
                m "Of course."
        "\"How was your day, [hermione_name]?\"":
            if  whoring <= 5: #WHORING LVL 02. EVENT LEVEL: 01
                $ new_request_03_heart = 1 #Event hearts level (0-3)
                $ hg_ps_hearts[hg_ps_PantyThief_ID] = 1 #Event hearts level (0-3)
                
                call her_main("Oh...","body_15",xpos=120)
                her "Quite ordinary actually..."
                call her_main("Although I could not help but worry that somebody would notice somehow...","body_13")
                call her_main(".....","body_29")
                call her_main("Can I have my panties back now?","body_31")
                m "Of course..."
                hide screen hermione_main
                with d3
                ">You give Hermione her panties back..."
                if hg_ps_PantyThief_SoakedPantiesFlag:
                    jump hg_ps_PantyThief_soaked
                else:
                    call her_main("And my payment?","body_31")
                    m "Yes, yes..."
            elif whoring >= 6 and whoring <= 8: #WHORING LVL 03. EVENT LEVEL 02.
                $ new_request_03_heart = 2 #Event hearts level (0-3)
                $ hg_ps_hearts[hg_ps_PantyThief_ID] = 2 #Event hearts level (0-3)
                
                call her_main("Oh...","body_15",xpos=120)
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                call her_main("I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"...","body_16")
                call her_main("I felt bad that I had to give the speech without any underwear on...","body_12")
                menu:
                    "\"You little hypocrite!\"":
                        $ mad +=5
                        call her_main("[genie_name]?","body_14")
                        m "You sold your panties to me this morning..."
                        m "And a couple of hours later you already publicly condemned that exact behaviour..."
                        #m "What would you call this?"
                        #call her_main("I know you are right, [genie_name]...","body_69")
                        call her_main("(But we need the points...)","body_69")
                        call her_main("Can I have my payment now please?","body_66")
                        m "What about your panties?"
                        call her_main("Oh, them too of course...","body_34") 
                        if hg_ps_PantyThief_SoakedPantiesFlag:
                            jump hg_ps_PantyThief_soaked
                        else:
                            pass
                    "\"It's for the greater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so corrupted..."
                        call her_main("I shall remain a symbol of righteousness to my peers, no matter what!","body_16")
                        call her_main("Can I have my panties back now, please?","body_31")
                        if hg_ps_PantyThief_SoakedPantiesFlag:
                            jump hg_ps_PantyThief_soaked
                        else:
                            her "And my payment."
            elif whoring >= 9: #WHORING LVL 04. EVENT LEVEL 03.
                $ new_request_03_heart = 3 #Event hearts level (0-3)
                $ hg_ps_hearts[hg_ps_PantyThief_ID] = 3 #Event hearts level (0-3)
                
                call her_main("Another ordinary day at hogwarts...","body_16",xpos=120)
                her "Nothing worth mentioning happened today..."
                call her_main("Although I have to admit...","body_29")
                her "It was oddly empowering to have no underwear on..."
                her "Hm..."
                call her_main("Can I have my panties back now please?","body_45")
                m "Of course..."
                hide screen hermione_main
                with d3
                ">You give Hermione her panties back..."
                if hg_ps_PantyThief_SoakedPantiesFlag:
                    jump hg_ps_PantyThief_soaked
                else:
                    call her_main("And my payment?","body_45")
                    m "Yes, yes..."
    label back_from_soaked:
    if hg_ps_PantyThief_SoakedPantiesFlag and whoring >= 9 and whoring <= 15 :
        m "You can go now."
        call her_main("What about my points?","body_30")
        m "You still want points after I just gave you a gift?"
        her "What gift?"
        m "You're wearing it"
        her "What, semen soaked panties?"
        m "if you'd prefer the points then just take them off"
        call her_main("well... I am already wearing them","body_29")
        m "then say thank you for the gift"
        call her_main("Thank you, [genie_name]...","body_17")
        m "You can go now."
        her "Good night, [genie_name]."
    elif hg_ps_PantyThief_SoakedPantiesFlag and whoring > 15:
        $ hg_ps_hearts[hg_ps_PantyThief_ID] = 4 #Event hearts level (0-4)
        m "You can go now."
        call her_main("yes, [genie_name]","body_118")
        m "After you say thank you. "
        call her_main("Thank you for what?","body_122")
        m "For my cum"
        call her_main("...","body_124")
        call her_main("Thank you for your cum [genie_name]...","body_123")
        m "You may go now."
        her "Good night, [genie_name]."
    else:
        $ gryffindor +=15
        m "Fifteen points to \"Gryffindor\" [hermione_name]. Well deserved." 
        her "Thank you, [genie_name]..."
        m "You can go now."
        her "Good night, [genie_name]."
        #m "Yes, good night..."
        
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    
    if whoring <= 5:
        $ whoring +=1
    
    $ hg_ps_points[hg_ps_PantyThief_ID] += 1
    $ hg_ps_InProgress[hg_ps_PantyThief_ID] = False #False when favor is not in progress
    $ hg_ps_PantyThief_SoakedPantiesFlag = False #TRUE if you jerked off in panties
    
    hide screen blkfade
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen chair_02
    hide screen hermione_blink
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen ctc
    show screen genie
    with d3
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door.
    with Dissolve(.3)
    
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
        $ hermione_sleeping = True
        jump night_main_menu


#Wear a shorter skirt
label hg_ps_shorter_skirt:


#Wear a sluttier shirt
label hg_ps_sluttier_shirt:

    
#Walk Of Shame
label hg_ps_WalkOfAtonement: #This will become more intense as the wear a shorter skirt and wear a sluttier shirt favours are completed

    m "[hermione_name], what classes do you have today?"
    call her_main("What? Since when have you taken an interest in my education?","body_07")
    m "I'm your headmaster, of course I care about your studies."
    call her_main("Hmmmm...","body_07")
    call her_main("Well I have potions class with Professor Snape in the morning and then defence against the dark arts after lunch.","body_07")
    m "So you have Snape as your teacher today?"
    call her_main("Yes [genie_name].","body_07")
    m "That's good. Today I have a task for you to complete."
    call her_main("A task?","body_07")
    m "Yes, I'd like you to attend class."
    call her_main("Is that all?","body_07")
    m "Without your shirt."
    call her_main("WHAT?","body_07")
    call her_main("Why on earth would I do that?","body_07")
    m "Because I asked you to."
    call her_main("...but what about Snape? What about my classmates?","body_07")
    m "Don't worry about Snape, I'm sure that he's used to your behaviour by now."
    m "And as for your classmates, is there anyone that will be surprised?"
    call her_main("Well Ginny would be...","body_07")
    m "What? Shocked to find out that her friend is a massive slut who shows herself off to anyone and everyone any chance she can get?"
    m "Look at your neck [hermione_name], look at what you are wearing. I'd be surprised if there is anyone in the school who doesn't know what a whore you are."
    call her_main("...","body_07")
    ">She holds back tears as she hands you her shirt."
    call her_main("I suppose that you're right [genie_name].","body_07")
    call her_main("Well I best be off... Can't be late for class.","body_07")
    ">She leaves your office reluctantly."
    $ hg_ps_InProgress[hg_ps_WalkOfAtonement_ID] = True

label hg_ps_WalkOfAtonement_complete:#Returns to your office after being made walk around the school with no shirt
    return
    
#WearMyCum
label hg_ps_WearMyCum: #Walk around school covered in genies cum 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    m "Today I have another small favor to ask of you."
    call her_main("What is it?","body_45")
    m "I'd like you to attend class."
    call her_main("Of course...","body_45")
    m "After I cum on you...."
    if whoring < 10:
    	jump too_much
    elif whoring < 15: 
    	jump hg_ps_WearMyCum_Scene_1
    elif whoring < 20:
    	jump hg_ps_WearMyCum_Scene_2
    else:
    	jump hg_ps_WearMyCum_Scene_3







label hg_ps_WearMyCum_Scene_1:
	call her_main("What?!?","body_45")
	call her_main("You can't be serious!","body_45")
	call her_main("It's bad enough that I let you cum on me in private!","body_45")
	call her_main("But in public?","body_45")
	call her_main("I think I better leave...","body_45")
	m "Wait, wait, wait."
	m "What about if nobody could see it?"
	call her_main("Well I suppose that would be alright...","body_45")
	call her_main("But what's the point if they can't see it?","body_45")
	m "You'll know it's there."
	call her_main("Hmmmm...","body_45")
	call her_main("Ok, I'll do it.","body_45")
	m "Really?"
	her "As long as nobody can see it then I don't see the big issue."
	m "Splendid. Care to give me a hand?"
	her "..."
	#Start jerk off chibis


label hg_ps_WearMyCum_Scene_2:



label hg_ps_WearMyCum_Scene_3:
















    ###OLD INTRO
    m "Suck my dick, [hermione_name]."
    call her_main("Of course...","body_45",xpos=140)
    # Sucking.
    
    call set_u_ani("blowjob_ani","hand_ani",-150,10)
    call u_play_ani
    
    show screen chair_02
    hide screen hermione_main
    hide screen genie
    hide screen hermione_blink #Hermione stands still.
    hide screen blkfade
    hide screen blktone
    hide screen bld1
    show screen ctc
    with fade
    pause
    show screen bld1
    with d3
    
    her "*Slurp!* *Slurp!* *Gulp!*"
    m "Yes, good girl..."
    her "*Slurp!* *Gobble!* *Slurp!*"
    her "*Slurp!* *Slurp!* *Gulp!*"
    show screen blktone
    with d3
    ">Hermione keeps sucking on your cock with a rather fierce determination."
    ">Her technique is lacking but she makes up for it with the effort she puts it."
    hide screen blktone
    with d3
    m "Yes... I love your eager, little mouth girl..."
    her "*Gobble!* *Gobble!* *Gobble!*"
    call u_pause_ani
    call her_head("[genie_name]?"."body_121")          
    m "Hm?"
    call her_head("Are you going to cum on my face today?"."body_121")
    call her_head("Or do you plan to cum in my mouth?")
    m "I Plan to splatter your face with cum!"
    call her_head("I see..."."body_121")
    m "Why do you ask?"
    call her_head("Oh... I just read in a book that semen contains a lot of antioxidants...","body_123")
    call her_head("It's good for the skin...")
    m "Great. One facial coming up."
    m "Back to work now."
    call u_play_ani
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "Hm..."
    m "You are getting better at this [hermione_name]."
    her "*Slurp!* *Slurp!* *Gulp!*"
    m "Ok, say something nasty now..."
    her "*Slurp--?"
    call u_pause_ani
    call her_head("I'm a slut [genie_name]."."body_129")
    call her_head("A slut for your cum."."body_128")
    m "That's it [hermione_name]."
    call her_head("It's all I can think about [genie_name]."."body_124")
    call her_head("Sucking your dirty old cock...")
    m "Well you better get back to it then [hermione_name]"
    call her_head("Thank you [genie_name]."."body_123")
    m "You're welcome cumslut."
    call her_head("..."."body_78")
    call u_play_ani
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "Yes, like this... Good..."
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "You know what? I think we are almost there."
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "Yes, definitely."
    her "*Slurp!* *Gobble!* *Gobble!*"
    m "Alright, [hermione_name], this is the final stretch."
    g4 "Show me what you've got."
    her "!!! *Gobble-goble-slurp-goble!* !!!"
    g4 "Yes, like that!"
    her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
    g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
    g4 "Ghr!!!"
    show screen bld1
    hide screen blkfade
    with d3
    call u_pause_ani
    g4 "Ready for your facial, [hermione_name]?"
    call her_head("Yes [genie_name]!"."body_123")      
    g4 "Here it comes then!"
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+7}Whore!{/size}"
    call her_head("!!?"."body_48")
    
    call set_u_ani("cum_on_face_ani")
    
    show screen ctc
    hide screen bld1
    with d3
    pause
    hide screen ctc
    show screen bld1
    with d3
    
    #Cumming.
    $ uni_sperm = True
    $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
    call her_head("[genie_name]..."."body_48")  
    g4 "All over your fucking face!"
    call her_head("Aaah!"."body_123")
    call set_u_ani("cum_on_face_blink_ani")
    m "Well, I'm done."
    
    her "Thank you [genie_name]."
    ">She goes to reach for a towel to clean her face."
    m "Not so fast [hermione_name], today I have an extra little task that I would like you to perform."
    her "What is it this time?"
    m "Today, I want you to wear my cum on your face."
    her "What? In front of my friends?"
    m "Especially in front of your friends. They deserve to know what a slut you've become."
    her "Do I have to wear it the whole day? It will smell so bad, not to mention that it will dry off."
    m "[hermione_name] let me make this as clear as I possibly can."
    m "If you come back to my office tonight without my cum on your face."
    m "Your school life will come to an end. Is that perfectly clear?"
    her "..."
    her "Yes [genie_name]."
    m "Good, now hurry along. We don't want you being late for class now do we?"
    her "No sir..."
    $ hg_ps_InProgress[hg_ps_WearMyCum_ID] = True


label hg_ps_WearMyCum_complete: #Hermione returns from her day of wearing your cum
    ">Hermione returns to your office."
    call her_main("...I did it [genie_name].","body_07")
    call her_main("I managed to keep it on all day.","body_07")
    call her_main("Even though it smelled","body_07")
    call her_main("and Ginny told me to wipe it off.","body_07")
    call her_main("I kept it on.","body_07")
    m "Good girl."
    menu:
        "-Go back to your room-":
            m "That'll be all [hermione_name], you may go now."
            call her_main("Thank you [genie_name]","body_07")
        "-Tell me what happened-":
            pass
    call her_main("Well I managed to walk to class without anyone seeing me.","body_07")
    call her_main("When I got there the class was lined up out the front waiting for Professor Snape.","body_07")
    call her_main("When Ginny saw what was on my face she immediately ran over to me and told me to clean myself up.","body_07")
    call her_main("","body_07")
    m "What did you do?"
    call her_main("I told her that I didn't know what she was talking about.","body_07")
    call her_main("She told me to run to the bathroom and look in the mirror.","body_07")
    call her_main("so I said that she was just crazy and that good girls don't miss class.","body_07")
    m "Smooth. What happened once you got into class?"
    call her_main("Well no one sat next to me, I assume because of the smell.","body_07")
    call her_main("Apart from that though no one really acknowledged me. I think none of them really cared.","body_07")
    m "They've probably come to expect it from you."
    call her_main("I suppose so. Is that all [genie_name]?","body_07")
    m "That's all for now [hermione_name], you may leave."
    call her_main("Thank you [genie_name]","body_07")



