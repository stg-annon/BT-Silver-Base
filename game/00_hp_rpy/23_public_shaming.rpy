
###PUBLIC EVENTS (more about shaming than whoring herself off to other people) There will be points for these events at the early stages

###Here's the current list of planned public shaming events, more may be added.
#Panty Thief - Done
#Wear a shorter skirt
#Wear a more revealing shirt 
#Walk of shame 
#Blowjob under desk in front of someone
#Cum walk


#At the moment the favours are based off of the whoring stat, so they line up with the personal favours. This is going to be changed at some point to instead focus on a new shaming stat. At the moment the favours aren't really there 
# to support this though.



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
            jump silver_requests
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
    
    if hg_ps_PantyThief_OBJ.points == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_heart = 1 #Event hearts level (0-3)
        $ hg_ps_PantyThief_OBJ.hearts_level = 1 #Event hearts level (0-3)
        
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
        if hg_ps_PantyThief_OBJ.points >= 1:
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
        
    $ hg_ps_PantyThief_OBJ.inProgress = True #True when Hermione has no panties on.
    
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
    
    call her_walk(500,710,2)
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
        if hg_ps_PantyThief_OBJ.points >= 1:
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
    $ hg_ps_PantyThief_OBJ.complete = True
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(710,500,3)
    
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
                $ hg_ps_PantyThief_OBJ.hearts_level = 1 #Event hearts level (0-3)
                $ sc34CG(1, 10)
                call her_main("Oh...","body_15",xpos=120)
                her "Quite ordinary actually..."
                call her_main("Although I could not help but worry that somebody would notice somehow...","body_13")
                call her_main(".....","body_29")
                call her_main("Can I have my panties back now?","body_31")
                m "Of course..."
                hide screen sccg 
                with d3
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
                $ hg_ps_PantyThief_OBJ.hearts_level = 2 #Event hearts level (0-3)
                $ sc34CG(1, 5)
                call her_main("Oh...","body_15",xpos=120)
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                call her_main("I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"...","body_16")
                call her_main("I felt bad that I had to give the speech without any underwear on...","body_12")
                hide screen sccg
                with d3
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
                $ hg_ps_PantyThief_OBJ.hearts_level = 3 #Event hearts level (0-3)
                $ sc34CG(1, 11)
                call her_main("Another ordinary day at hogwarts...","body_16",xpos=120)
                her "Nothing worth mentioning happened today..."
                call her_main("Although I have to admit...","body_29")
                her "It was oddly empowering to have no underwear on..."
                her "Hm..."
                call her_main("Can I have my panties back now please?","body_45")
                hide screen sccg
                with d3
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
        $ hg_ps_PantyThief_OBJ.hearts_level = 4 #Event hearts level (0-4)
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
    
    $ hg_ps_PantyThief_OBJ.points += 1
    $ hg_ps_PantyThief_OBJ.inProgress = False #False when favor is not in progress
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
    
    call her_walk(500,710,2)
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
label hg_ps_WalkOfShame: #This will become more intense as the wear a shorter skirt and wear a sluttier shirt favours are completed

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
    $ hg_ps_WalkOfShame_OBJ.inProgress = True

label hg_ps_WalkOfShame_complete:#Returns to your office after being made walk around the school with no shirt
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
        jump hg_ps_WearMyCum_Scene_2 #This is 1 until I write 2
    else:
        jump hg_ps_WearMyCum_Scene_2 #This is 1 until I write 3







label hg_ps_WearMyCum_Scene_1:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("What?!?","body_48")
    call her_main("You can't be serious!","body_49")
    call her_main("It's bad enough that I let you cum on me in private!","body_50")
    call her_main("But in public?","body_51")
    call her_main("I think I better leave...","body_61")
    m "Wait, wait, wait."
    m "What about if nobody could see it?"
    call her_main("Well I suppose that would be alright...","body_50")
    call her_main("But what's the point if they can't see it?","body_29")
    m "You'll know it's there."
    call her_main("Hmmmm...","body_12") #Haggle here
    call her_main("How much will I be paid?","body_17") 
    m "30 points."
    call her_main("30! I expect at least 70 for such a filthy act!","body_32") 
    m "40."
    call her_main("60!","body_30") 
    m "50 points, final offer."
    call her_main("Ok, I'll do it.","body_29")
    m "Really?"
    call her_main("As long as nobody can see it then I don't see the big issue.","body_69")
    m "Splendid. Care to give me a hand?"
    call her_main("...","body_124")
    #Start jerk off chibis
    hide screen hermione_main            
    hide screen bld1
    with d3
    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause.1
    show screen blkfade
    with Dissolve(1)
    pause.3

    hide screen genie
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "handjob_ani"
    show screen chair_02
    show screen g_c_u
    show screen desk_02
    hide screen blktone
    hide screen hermione_walk_01 
    hide screen blkfade
    call her_head("Why are you making me do this [genie_name]?","body_117")
    m "What do you mean?"
    call her_head("Why are you making me jerk you off...","body_118")
    call her_head("So that you can cum on me...","body_121")
    call her_head("And make me wear it around the school?","body_131")
    m "I'm not making you do anything."
    m "You're doing this because I asked you to."
    call her_head("But if I don't, Gryffindor will lose the house cup.","body_132")
    m "And?"
    call her_head("Harry and Ron will be so dissapointed...","body_28")
    m "So that's why you are doing this? For those two boys?"
    call her_head("Sort of... I'm not sure that they'd be too upset though.","body_29")
    m "Are you sure it's not because you love it."
    call her_head("What?","body_44")
    m "Coming in here whenever I summon you."
    m "Doing whatever I tell you, whenever I tell you."
    m "Doing slutty things in front of your peers because I tell you."
    call her_head("...","body_85")
    m "I'll tell you what, I'll make things interesting."
    m "So long as I cum on you and you wear it around classes today, Gryffindor will get 50 points."
    call her_head("How does that make it interesting?","body_66")
    m "Because I'll let you choose where I cum."
    ">You fell her hands tense around your cock."
    call her_head("You're letting me choose?","body_46")
    m "Anywhere, as long as it's on you. It can be your shoes for all I care."
    call her_head("Ok...","body_53")
    m "Well hurry up [hermione_name], classes will start soon."
    ">She starts jerking your cock with renewed vigour."
    m "So where are you going to hide it?"
    call her_head("I'm not sure.","body_44")
    call her_head("I'm trying to think of somewhere no one will be able to see it.","body_44")
    m "Well you better think of some place soon!"
    call her_head("Why's that?","body_122")
    g9 "Because I'm about to cum!"
    call her_head("Already? Where should I-","body_119")
    menu:
        "-Stay Silent-": # Cum under shirt
            $ cum_location = 1
            ">Hermione swiftly pulls her shirt up..."
            ">She then pushes your already dribbling cock against her belly and covers it up again..."
            ">The sensation of her skin under your engorged cock almost makes you lightheaded..."
            ">Hermione placed your cock a bit higher than you would expect..."
            ">You can feel her incredibly soft tits rubbing against the tip of your cock..."
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "{size=+5}ARGH! YES!!!{/size}"

            call her_head("!!!!!!!!!!!","body_48") 

            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "undershirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            pause 
                    
            $ aftersperm = True

            call her_main("Well, this shouldn't be too bad...","body_44") 
            m "I'm sure no one will notice."
            call her_main("They better not.","body_49") 

        "\"Just keep on jerking [hermione_name]!\"": # Cum on skirt 
            $ cum_location = 2
            ">Hermionely keeps jerking your cock, her eyes darting between it and herself."
            g4 "Get ready whore, here it comes!"
            call her_head("Wait, where am I supposed to-","body_28")
            g9 "{size=+5}ARGH! YES!!!{/size}"
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_11.png"
            $ uni_sperm = True
            call her_main("!!!!!!!!!!!","body_48") 
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            m "That's it, all over you slut."
            call her_main("...","body_71") 
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("Will that be all [genie_name].","body_70") 
            m "I don't suppose you could kiss it for good luck?"
            call her_main("I don't think so.","body_69") 
            m "Well then that should be all then [hermione_name]."

        "\"Take it on your face slut!\"":
            $ cum_location = 3
            ">Hermione bends down and place your cock in front of her face."
            m "Get ready slut, here it comes!"
            call her_head("...","body_72")
            g9 "{size=+5}ARGH! YES!!!{/size}"
            call her_head("I can't...","body_88")
            ">Hermione moves your cock away from her face at the last second."
            ">You erupt over the top of her head, covering her hair in your spunk."
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_12.png"
            $ uni_sperm = True
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            call her_main("!!!!!!!!!!!","body_48") 
            m "Yes... I Feel so much better now..."
            call her_main("..............","body_33") 
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("How could you!","body_32") 
            m "How could I?"
            call her_main("You told me to let you cum on my face!","body_30") 
            m "I did."
            call her_main("Why would you say something like that!","body_20") 
            call her_main("If I hadn't moved at the last second my face would be covered!","body_21") 
            m "You didn't have to listen to me."
            call her_main("What?","body_28") 
            m "I only said that you had to have my cum on you."
            m "I never said where."
            call her_main("You mean I didn't have to...","body_29") 
            m "Not at all."

    show screen hermione_stand 
    hide screen chair_02
    hide screen desk_02
    show screen genie
    hide screen g_c_u
    $ her_head_ypos = her_head_tits
    hide screen blkfade
    with d5
    ">You tuck your cock back into your robe."
    m "Oh and one last thing before you head to class."
    call her_main("Yes...","body_50")
    m "If you return to this office after classes without any cum on you, Slytherin gets 200 points." 
    call her_main("{size=+10}200! That is not fair!{/size}","body_48") 
    m "It's Only unfair if you clean it off."
    call her_main("...","body_49") 

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    $ hermione_SC.chibi.ypos = 250 #Default: 250
    show screen hermione_blink #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3


    jump end_hg_pf




label hg_ps_WearMyCum_Scene_2:
    $ hg_ps_WearMyCum_OBJ.inProgress = True
    call her_main("Again?","body_48")
    call her_main("You can not be serious!","body_49")
    call her_main("I already let you do this to me once, isn't that enough?","body_50")
    m "It's enough when I say it's enough."
    m "Besides, was it really such an issue last time?"
    call her_main("Well I guess not...","body_82")
    call her_main("But will it still be hidden this time?","body_29")
    m "That's up to you."
    call her_main("Hmmmm...","body_12") #Haggle here
    call her_main("How much will I be paid this time then?","body_17") 
    m "20 points."
    call her_main("20! we agreed on 50 last time!","body_32") 
    m "40."
    call her_main("70!","body_30") 
    m "50 points, final offer."
    call her_main("80 and I'll let people see it.","body_58")
    m "Really?"
    call her_main("As long as it isn't too obvious.","body_59")
    m "Deal."
    call her_main("...","body_124")
    #Start jerk off chibis
    hide screen hermione_main            
    hide screen bld1
    with d3
    $ walk_xpos=500 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause.1
    show screen blkfade
    with Dissolve(1)
    pause.3

    hide screen genie
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "handjob_ani"
    show screen chair_02
    show screen g_c_u
    show screen desk_02
    hide screen blktone
    hide screen hermione_walk_01 
    hide screen blkfade
    call her_head("Why are you asking me to do this [genie_name]?","body_117")
    m "This question again?"
    m "Let me answer your question with one of my own."
    call her_head("Ok...","body_118")
    m "Why are you jerking me off [hermione_name]?"
    call her_head("Because you asked me to...","body_121")
    m "And is that the only reason?"
    call her_head("No...","body_131")
    m "Are you sure?"
    m "What is your other reason then?"
    call her_head("if I don't, Gryffindor will lose the house cup.","body_132")
    m "That lie again?"
    call her_head("It's not a lie...","body_28")
    m "So you'd rather win the house cup than make me happy?"
    call her_head("Maybe... Can't I do both?","body_29")
    m "You can..."
    call her_head("Good","body_53")
    m "But I want you to be honest."
    m "So I'm going to give you a choice."
    m "You can stop jerking me off right now, leave the room and I'll give you the 80 points. However, I'll be very upset."
    call her_head("or?","body_31")
    m "Or, you can keep jerking me off, wear my cum around the school and get no points."
    call her_head("NO POINTS?","body_32")
    m "None. You will make an old man very happy though."
    call her_head("Can't you just pay me for wearing your cum?","body_34")
    m "No."
    ">You fell her hands tense around your cock."
    call her_head("You're making me choose? Between getting 80 points for doing nothing.","body_50")
    call her_head("Or getting paid nothing for wearing your cum around the school.","body_51")
    m "Indeed I am [hermione_name]."
    call her_head("{size=-5}Ok...{/size}","body_85")
    m "Well hurry up [hermione_name], classes will start soon, best make your decision."
    ">She starts jerking your cock with renewed vigour."
    call her_head("...","body_17")
    call her_head("You better appreciate this.","body_12")
    m "Oh I'm appreciating it!"
    call her_head("Really?","body_14")
    g9 "You're about to see how much I'm appreciating it!"
    call her_head("What, Already? Where should I-","body_119")
    menu:
        "-Stay Silent-": # Legs
            $ cum_location = 4
            ">Hermionely keeps jerking your cock, her eyes darting between it and herself."
            g4 "Get ready slut, here it comes!"
            call her_head("Wait, where am I supposed to-","body_28")
            g9 "{size=+5}ARGH! YES!!!{/size}"
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_13.png"
            $ uni_sperm = True
            call her_main("!!!!!!!!!!!","body_48") 
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            m "That's it, all over your milky thighs."
            call her_main("...","body_71") 
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("Will that be all [genie_name].","body_70") 
            m "I don't suppose you could kiss it for good luck?"
            call her_main("...{p}...","body_78") 
            $ g_c_u_pic = "kiss_ani"
            $ renpy.play('sounds/kiss.mp3') 
            with kissiris
            pause
            show screen blkfade
            with d3
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            hide screen blkfade
            with d3
            m "Good girl."

        "\"Just keep on jerking [hermione_name]!\"": # Cum on shirt front 
            $ cum_location = 5
            ">Hermionely keeps jerking your cock, her eyes focused intently on it."
            g4 "Get ready whore, here i come!"
            call her_head("...","body_28")
            g9 "{size=+5}ARGH! YES!!! RIGHT ON THOSE TITS!{/size}"
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
            $ uni_sperm = True
            call her_main("!!!!!!!!!!!","body_48") 
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            m "That's it, all over you slut."
            call her_main("...","body_71") 
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("It's all over me.","body_70") 
            m "That it is."
            call her_main("I think I should go now...","body_71") 

        "\"Take it on your face slut!\"":
            $ cum_location = 6
            ">Hermione bends down and place your cock in front of her face."
            m "Get ready slut, here it comes!"
            call her_head("...","body_72")
            g9 "{size=+5}ARGH! YES!!!{/size}"
            call her_head("...","body_88")
            ">You erupt onto her face, dousing her in your spunk."
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
            $ uni_sperm = True
            $ genie_chibi_xpos = 60 #-185 behind the desk.
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "on_shirt_cum_ani"
            hide screen blkfade
            with d3
            show screen ctc
            hide screen bld1
            with d3
            pause
            show screen bld1
            with d3
            call her_main("!!!!!!!!!!!","body_48") 
            m "Yes... I Feel so much better now..."
            call her_main("..............","body_33") 
            pause
            $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
            call her_main("How could you!","body_32") 
            m "How could I?"
            call her_main("You came all over my face!","body_30") 
            m "I did."
            call her_main("Why would you ask me to do that!","body_20") 
            call her_main("I'm completely covered in your cum!","body_21") 
            m "You didn't have to listen to me."
            call her_main("...","body_28") 
            m "I only said that you had to have my cum on you."
            m "I never said where."
            call her_main("You told me to do it though...","body_29") 

    show screen hermione_stand 
    hide screen chair_02
    hide screen desk_02
    show screen genie
    hide screen g_c_u
    $ her_head_ypos = her_head_tits
    hide screen blkfade
    with d5
    ">You tuck your cock back into your robe."
    m "Oh and one last thing before you head to class."
    call her_main("Yes...","body_121")
    m "If you return to this office after classes without any cum on you, I'll be very upset." 
    call her_main("Yes [genie_name].","body_78") 
    m "Have fun. Say hi to your friends for me."
    call her_main("...","body_84") 

    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 500 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_blink #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3


    jump end_hg_pf


label hg_ps_WearMyCum_Scene_3:



label hg_ps_WearMyCum_complete: #Hermione returns from her day of wearing your cum
    $ hg_ps_WearMyCum_OBJ.inProgress = False
    $ hg_ps_WearMyCum_OBJ.complete = True
    if cum_location <= 3:
        jump hg_ps_WearMyCum_complete_1
    else:
        jump hg_ps_WearMyCum_complete_2


label hg_ps_WearMyCum_complete_1:
    if cum_location == 1: #Cum under shirt
        $ aftersperm = True
        ">Hermione returns to your office, your cum stains still visible on her shirt."
        call her_main("...I did it [genie_name].","body_53")
        call her_main("I kept your cum on me all day.","body_54")
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor += 50
                call her_main("Thank you [genie_name], will that be all?","body_55")
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, I had potions class and then transfiguration.","body_16")
                m "And do you think that anyone noticed?"
                call her_main("I don't think so [genie_name]. Ginny Weasley asked me about it during transfiguration class though.","body_15")
                m "And what did you tell her?"
                call her_main("I just said that I spilled some Wiggenweld potion on myself in potions class.","body_14")
                m "Very cunning of you. 50 points to Gryffindor."
                $ gryffindor += 50
                call her_main("Thank you [genie_name], if that's all I might head to bed.","body_55")
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","body_06")
    elif cum_location == 2: #Cum on skirt 
        $ u_sperm = "01_hp/13_hermione_main/auto_11.png"
        $ uni_sperm = True
        ">Hermione returns to your office."
        call her_main("...I did it [genie_name].","body_33")
        call her_main("I kept your cum on me all day.","body_34")
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor += 50
                call her_main("Thank you [genie_name], will that be all?","body_29")
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, I had potions class and then transfiguration.","body_29")
                m "And do you think that anyone noticed?"
                call her_main("I think a few people did [genie_name]. I could hear The first years all whispering as I walked past.","body_57b")
                m "And how did you feel?"
                call her_main("Excited. I just wish that they knew why I was doing this.","body_59")
                m "Speaking of that, 50 points to Gryffindor."
                $ gryffindor += 50
                call her_main("Oh, right the points, Thank you [genie_name]. if that's all I might head to bed.","body_87")
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","body_83")
    else: #Cum on hair
        $ u_sperm = "01_hp/13_hermione_main/auto_12.png"
        $ uni_sperm = True
        ">Hermione returns to your office."
        call her_main("...I did it [genie_name].","body_26","tears_03")
        call her_main("I kept your cum on me {p}all day.","body_27","tears_03")
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor += 50
                $ mad += 5
                call her_main("...","body_50","tears_03a")
                m "Well [hermione_name], you may leave now."
                call her_main("Hmmmphh...","body_51","tears_03a")
            "\"Tell me about your day.\"":
                $ mad += 10
                call her_main("My day...","body_33","tears_03a")
                call her_main("This was the worst day of my life!","body_32","tears_03a")
                call her_main("I've never been so ashamed!","body_34","tears_03a")
                m "Did your friends treat you poorly?"
                call her_main("No! That's the worst part!","body_30","tears_03a")
                call her_main("I expected to be an outcast, to sit by myself and not have Ginny or Luna talk to me.","body_29","tears_03a")
                call her_main("But they didn't even acknowledge the fact that I was covered in cum!","body_12","tears_03a")
                call her_main("They acted as if nothing was wrong.","body_20","tears_03a")
                call her_main("I even tried to provoke a response from Ginny by asking her what she thought of my hair!","body_21","tears_03a")
                m "And what was her reaction?"
                call her_main("She said that it suited me!","body_27","tears_03a")
                m "Maybe they're just used to you acting like this."
                call her_main("That's the problem! They think that this slutty persona is who I am now!","body_28","tears_03a")
                m "Isn't it?"
                call her_main("...","body_27","tears_03a")
                call her_main("Good night [genie_name].","body_33","tears_03a")

    jump end_hg_pf


label hg_ps_WearMyCum_complete_2:
    if cum_location == 4: #Cum on legs
        $ u_sperm = "01_hp/13_hermione_main/auto_13.png"
        $ uni_sperm = True
        ">Hermione returns to your office, your cum still visible on her legs."
        call her_main("...I did it [genie_name].","body_53")
        call her_main("I kept your cum on me all day.","body_54")
        menu:
            "\"Good Work!\"":
                call her_main("Thank you [genie_name], will that be all?","body_55")
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, well, except for Luna...","body_16")
                m "Luna?"
                call her_main("Luna Lovegood, sir.","body_15")
                m "What happened with miss Lovegood?"
                call her_main("She kept trying to tell me that a Cornish pixie had given me a present.","body_69")
                m "A cornish pixie had given you a present?"
                call her_main("I didn't know what she was talking about either. Cornish pixies are nasty little things that would never do anything nice.","body_66")
                m "Well what happened after that?"
                call her_main("Well I asked her what she was talking about and then she ran her finger up my leg, scooping up some of your cum!","body_64")
                m "Really?"
                call her_main("That's not the worst part. She then proceded to taste it!","body_65")
                m "I don't believe you."
                call her_main("I was as shocked as you were.","body_16")
                m "Well you have certainly made this old man very happy."
                call her_main("Thank you [genie_name]. if that's all I might head to bed.","body_87")
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","body_83")
    elif cum_location == 5: #Cum on shirt 
        $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
        $ uni_sperm = True
        ">Hermione returns to your office, her shirt still covered in cum."
        call her_main("...I did it [genie_name].","body_33")
        call her_main("I kept your cum on me all day.","body_34")
        menu:
            "\"Good Work!\"":
                call her_main("Thank you [genie_name], will that be all?","body_29")
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, I had Defense against the dark arts class and then herbology.","body_29")
                m "And do you think that anyone noticed?"
                call her_main("I think most people did [genie_name]. I'm not sure if they all knew it was cum though.","body_57b")
                m "And how did you feel?"
                call her_main("Excited. Getting to see everyone's faces as they realised what it was...","body_59")
                m "So you don't mind them knowing?"
                call her_main("I suppose not... As long as it makes you happy.","body_87")
                m "Very well, goodnight [hermione_name]."
                call her_main("Good night [genie_name].","body_83")
    else: #Cum on face
        $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
        $ uni_sperm = True
        ">Hermione returns to your office."
        call her_main("...I did it [genie_name].","body_91b","tears_03")
        call her_main("I kept your cum on me {p}all day.","body_91b","tears_03")
        menu:
            "\"Good Work!\"":
                call her_main("...","body_91b","tears_03a")
                m "Well [hermione_name], you may leave now."
                call her_main("Did I at least make you happy?","body_92","tears_03a")
                m "You did."
                call her_main("Good.","body_90","tears_03a")
            "\"Tell me about your day.\"":
                call her_main("My day...","body_33","tears_03a")
                call her_main("It was completely normal.","body_32","tears_03a")
                m "Really? Nothing strange happened at all?"
                call her_main("No. Everyone treated me how I deserved to be treated.","body_30","tears_03a")
                m "And how's that?"
                call her_main("Like a slut.","body_29","tears_03a")
                call her_main("Boys cat called me.","body_12","tears_03a")
                call her_main("Put me down.","body_20","tears_03a")
                call her_main("Snape made me stand out the front of the class During defense against the dark arts.","body_21","tears_03a")
                m "What did he make you do in front of the class?"
                call her_main("Nothing, I just had to stand there for the whole lesson.","body_27","tears_03a")
                m "Did your friends say anything?"
                call her_main("Nothing.","body_28","tears_03a")
                call her_main("...","body_27","tears_03a")
                call her_main("Did I{p}make you happy?","body_92","tears_03a")
                m "You did."
                call her_main("Good night [genie_name].","body_33","tears_03a")

    jump end_hg_pf

label hg_ps_WearMyCum_complete_3:

#Blowjob in front of Luna
#Genie tells Hermione to go fetch a student and that she will be sucking him off while he talks to them

#Three variants, each with a differing level of exhibitionism
#1 Hermione is as silent as possible, Luna almost completely unaware
#2 Hermione quite loud, Luna actively aware that something is wrong
#3 Hermione crawls out from under the desk covered in Genie's cum trying to pass it off
label hg_ps_HiddenBlowjob:
    jump hg_ps_HiddenBlowjob_1


label hg_ps_HiddenBlowjob_1:
    m "[hermione_name], I have an interesting proposition for you today."
    her "Is it sex?"
    m "Not quite."
    her "Then what is it?"
    m "Well it involves you bringing in a friend."
    her "A friend?!"
    her "I can't let one of my friends find out what we do here!"
    m "Don't worry, this isn't about them finding out."
    her "Then what is it about?"
    m "It's about you learning to be more comfortable with yourself around your peers."
    her "Comfortable with myself?"
    m "Yes. To do this I'll need you to bring a friend of yours to my office."
    her "What for?"
    m "So I can talk to them."
    her "That doesn't sound too bad..."
    m "While you suck me off."
    her "What?! There's no way I'm doing that!"
    m "Why not?"
    her "Why not? Because my reputation would be ruined! I'm not blowing you in front of other students, let alone one of my friends!"
    m "What if they didn't know you were there?"
    her "How so? I can't just be hidden behind you while you look at a cupboard."
    m "Well, the area under my desk is quite spacious."
    her "Hmmmmm, I'm not sure, what if they overheard us?"
    m "Just do it quietly"
    her "I can't I'm going to do it properly."
    #Needs more dialogue where Genie convinces her to accept, and Hermione agrees.
    m "Well surely you can think of someone that'll be suitable for the position?"
    her "Hmmmmm"
    her "Bingo!"
    m "Have you suddenly remembered that one of your friends is a deaf mute?"
    her "Better [genie_name], Luna Lovegood."
    m "Lovegood? That can't be a real name."
    her "It is."
    m "Well then why her?"
    her "Let's just say that people are less likely to believe her if she tries to spread rumours."
    m "Hmmm, I'm not sure if I agree with-"
    her "She's also a blonde with big tits."
    m "Perfect! Tell her to drop by my office."
    her "As soon as you tell me, what to tell her, what you want to see her for."
    m "Tell her I'd like to discuss the behaviour of certain students at the school"
    her "Ok, I'll tell her to come to your office in about 10 minutes."
    her "That should give me time to get back here first."
    #Hermione walks out fade to black
    her "It's tiny under here!"
    m "What are you talking about, there's tons of space!"
    her "Not with your legs either side of me."
    "*Knock* *Knock* *Knock*"
    m "{size=-5}Shhhh, she's here!{/size}"
    her "What should I do?"
    m "Come in!"
    #Luna walks in
    "As Luna walks in you grab the back of Hermione's head and force it down the length of your cock."
    her "!!!!"
    lun "Hello Professor, Hermione Granger said that you wanted to see me?"
    m "Ah yes, Miss Lovegood (pffft), right on time."
    "You ease off on Hermione, allowing her to move at her own pace."
    her "mmmmm"
    lun "What did you want to talk to me about sir?"

    m "I'd like to talk to you about a series of uniform changes that are taking place in the school."
    lun "Are you referring to Miss Granger, Professor?"
    "You feel Hermione tense up under the desk."
    m "Indeed I am."
    "You slide your hips forward, pinning Hermione's head between your cock and the back of the desk."
    m "Have you noticed any difference in the uniform of Miss Granger?"
    lun "I have sir."
    m "Please, describe these changes to me in detail, I have a feeling that she may change what she wears when she visits me."
    lun "Well for one her skirt is ridiculously short!"
    m "How short?"
    lun "You can see her panties sir!"
    "You start thrusting into hermiones mouth"
    m "Is that so?"
    lun "It is, though only some of the time."
    her "*glck*"
    m "Some of the time?"
    lun "Well other times she doesn't even wear them."
    "You feel Hermione start to speed up."
    m "Really?" 
    lun "really. Don't even get me started on her tops."
    "You reach under the desk and grab the back of Hermione's head."
    lun "Is everything ok sir?"
    m "Yes, yes, just scratching my leg, Please, go on."
    lun "Well sometimes she only wears her school vest."
    m "And can you see anything innapropriate?"
    lun "She's showing off a lot of cleavage sir."
    m "That would be problematic."
    "You pull her forward, until you can feel her nose press into your crotch."
    her "!!!"
    m "And how do you think Ms Granger should be punished?"
    "You let hermione slide back."
    her "*slurp*"
    lun "Well she ties it in a knot so it's barely even there!"
    m ""

    #Hermione says goodbye bla bla bla
    "Hermione leaves your office."

    jump hg_ps_HiddenBlowjob_complete




label hg_ps_HiddenBlowjob_complete:
    jump hg_ps_HiddenBlowjob_complete_1


label hg_ps_HiddenBlowjob_complete_1:

    jump end_hg_pf

label hg_ps_Buttplug: 
    
    $ current_payout = 55 #Used when haggling about price of the favour.
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to wear a buttplug around the school?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            m "What Type?"
            menu:
                "-Small, regular-":
                    $ buttplug_size = 1
                "-Medium, magical-" if hg_ps_Buttplug_OBJ.points >= 1:
                    $ buttplug_size = 2
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_ps_Buttplug_OBJ.points == 0 and buttplug_size == 1: # <================================================================================ FIRST TIME
        if whoring <=10:
            m "[hermione_name], I want you to do something different today..."
            call her_main("...?","body_07",xpos=140)
            m "I want you to wear a buttplug around the school."
            jump too_much
        m "[hermione_name], I want you to do something different today..."
        call her_main("...........","body_15",xpos=370)
        ">You pull a large size buttplug out from under your desk and place it in front of her."
        call her_main("and what is that supposed to be? Some sort of animals tail?","body_08")
        m "Not exactly, it's a buttplug. I want you to put it in while you attend class today."
        stop music
        with hpunch
        call her_main("{size=+5}What?!!{/size}","body_48")
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("You expect me to put that massive thing in my...","body_47")
        her "and then parade myself around the school!"
        m "It just looks like a fake tail, No one will be able to tell what it really is."
        call her_main("{size=+5}That's not the point!{/size}","body_30")
        her "I'm not going to put that ridiculous thing anywhere near my butt!"
        call her_main("We are done here, [genie_name]!","body_76")
        m "Alright, alright, calm down..."
        call her_main("I most certainly will not, [genie_name]! That thing is beyond absurd!","body_30")
        m "Alright, fine, maybe I underestimated how large it is..."
        call her_main("You think [genie_name]?! I'd like to see you try and fit it up your-","body_47")
        m "alright, alright..."
        call her_main(".........","body_79")
        m "How about we try one a little less... ambitious."
        call her_main("............","body_120")
        m "I'm willing to give \"Gryffindor\" fifty five points."
        m "and All I ask for..."
        call her_main("..........?","body_17")
        ">You pull out the small buttplug from your desk."
        m "...is that you wear this to class..."
        call her_main("!!!......","body_47")
        m "Oh, come on... Just a harmless little baby one."
        call her_main("...","body_66")
        m "Fifty five house points..."
        call her_main("..............","body_69")
        call her_main("Fine.","body_79")
        m "Fantastic."
        m "Will you be putting it in now then?"
        call her_main("........","body_69")
        call her_main("I'll put it in in the girls bathroom [genie_name]","body_69")
        m "Hmmm... we'll i'll See you tonight then."
    elif buttplug_2_worn == False and buttplug_size == 2: # <================================================================================ FIRST TIME
        if whoring <=15:
            m "[hermione_name], I want you to try something different today..."
            call her_main("...?","body_07",xpos=140)
            ">You place the medium sized buttplug on the table."
            m "I want you to wear this buttplug around the school."
            jump too_much
        $ buttplug_2_worn = True
        m "[hermione_name], I want you to try something different today..."
        call her_main("...........","body_15",xpos=370)
        ">You pull the medium size buttplug out from under your desk and place it in front of her."
        call her_main("and what is this supposed to be?","body_08")
        m "Can't you tell it's a buttplug? They shouldn't be new to you at this point."
        call her_main("...","body_50")
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("Why does it have a such a large tail attached to it...","body_61")
        her "you can't expect me to wear that around the school!"
        m "I can and do, unless you want our little trading game to come to a halt..."
        call her_main("but it's so long! everyone will be able to see it!","body_33")
        m "That's the point, [hermione_name]..."
        call her_main("...........","body_34")
        call her_main("I want 100 points.","body_61")
        menu:
            "\"Fine, but I expect you to put it in now.\"":
                $ current_payout = 100
                call her_main("What? Right now!?.","body_97")
                call her_main("In front of you?","body_122")
                m "100 points [hermione_name]..."
                call her_main("ugh... Fine...","body_118")
                call her_main("But I'm not turning around!","body_81")
                m "Whatever suits you best..."
                ">You hand her the buttplug"
                call her_main("{size=-7}It's so big...{/size}","body_88")
                ">Hermione lifts her skirt and presses it against her asshole."
                call her_main("ughh... it's too big...","body_132")
                call her_main("It won't fit!","body_131")
                m "well then Try spitting on it."
                call her_main(".........","body_118")
                ">She spits on the end of it and then retries."
                call her_main("it didn't work, It's just too bi-","body_117")
                stop music
                $ hermione_buttplugs = True
                $ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_b_on.png"
                with hpunch
                call her_main("{size=+5}!!!!{/size}","body_104")
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                call her_main(".............","body_117")
                call her_main("...","body_118")
                call her_main("well.... ah, I... better get to.... class... then...","body_122")
                m "See you tonight [hermione_name]."

            "\"You'll get 70.\"":
                $ current_payout = 70
                call her_main("Hmmmph...","body_103")
                call her_main("Alright then, just don't expect me to show it to you!","body_77")
                m "So long as you wear it to class then you'll get your 70 points."
                ">You hand her the buttplug."
                call her_main("Will that be all [genie_name]?.","body_81")
                m "Yes [hermione_name], see you tonight."
                call her_main("{size=-5}(cheap bastard...){/size}","body_69")

    
    else: # <================================================================================ NOT FIRST TIME
        if whoring <= 15 and buttplug_size == 1: # LEVEL 06 FIRST EVENT.
            m "Today's favour shall be..."
            call her_main(".........","body_117",xpos=370)
            m "Wearing your favorite little buttplug to class!"
            call her_main("...again?","body_118")
            m "Sure, why not?"
            m "And another fifty five house points for the \"Gryffindor\" house of course."
            call her_main("..........","body_29")
            m "So... Are you ok with that, [hermione_name]?"
            call her_main("I suppose so...","body_69")
            ">You hand her the buttplug."
            m "Fantastic! See you after class."
        
        elif whoring <= 20 and buttplug_size == 1: # LEVEL 07
            ">You pull out the large buttplug."
            m "Ready to try out the dragon yet?"
            stop music fadeout 1.0
            call her_main("What?","body_72",xpos=370)
            call her_main("Of course not! That thing would tear me--","body_30")
            ">you pull out the small buttplug"
            m "How about this one then?"
            call her_main("Oh, ok then!","body_80")
            m "You'll do it that easily?"
            call her_main("Well for fifty five house points I'd be crazy not to.","body_84")
            call her_main("Plus I don't hate the way it feels","body_107")
            ">You hand her the buttplug."
            m "why don't you put it in now."
            call her_main("you want me to put it in now? in front of you!","body_72")
            m "I don't see the harm in it."
            call her_main("well... it does save me having to visit the girls bathroom before class...","body_73")
            call her_main("alright then, I'll do it... but I want an extra five points!","body_46")
            m "Done."
            $ current_payout += 5
            call her_main("well... here goes.","body_46")
            ">Hermione lifts her skirt and sticks it in rather slowly."
            #$ hermione_buttplugs = True
            #$ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_a_on.png"
            call her_main("{image=textheart}ah{image=textheart}...","body_106")
            call her_main("i better head to class...","body_105")
            m "See you tonight [hermione_name]."
            call her_main("{size=-5}({image=textheart}it feels so good{image=textheart}){/size}","body_106")
        
        elif whoring >= 21 and buttplug_size == 1: # LEVEL 08+
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","body_68",xpos=370)
            m "You're eager."
            call her_main("well... I mean it is a lot of points and... i've sort of grown fond of how it feels...","body_87")
            m "Great. Go have fun then!"
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."
            #$ hermione_buttplugs = True
            #$ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_a_on.png"
            call her_main("{image=textheart}ah{image=textheart}...","body_106")
            call her_main("I will, [genie_name]. Thank you.","body_74")

        elif whoring <= 19 and buttplug_size == 2: # LEVEL 06 FIRST EVENT.
            m "Today my gracious request will be..."
            call her_main(".........","body_117",xpos=370)
            m "That you wear everyone's favorite magical buttplug to class!"
            call her_main("...again?","body_118")
            m "why not? This will be the easiest fifty five points you'll ever earn!"
            call her_main("..........","body_29")
            m "Do you have a problem with it, [hermione_name]?"
            call her_main("I suppose not...","body_69")
            ">You hand her the buttplug."
            m "Fantastic! See you after class."
        
        elif whoring <= 23 and buttplug_size == 2: # LEVEL 07
            if buttplug_2_question == False:
                $ buttplug_2_question = True
                ">You pull out the buttplug."
                m "Ready to try out the phoenix again?"
                call her_main("Oh, I suppose so...","body_105",xpos=370)
                call her_main("But is it alright if I ask you something first?","body_87")
                m "What's that [hermione_name]"
                call her_main("Don't you worry about us getting caught?","body_82")
                m "Why would I?"
                call her_main("Well it's just that making me wear something like this is drawing a lot of attention...","body_10")
                call her_main("and what if someone realises that it's you who's making me do all this...","body_11")
                m "and who is going to suspect the great albis dumbledorf?"
                call her_main("...I suppose no one...","body_29")
                m "Then don't worry about it. If anyone asks just tell them you're going through an exhibitionist stage."
                m "Speaking of which..."
                ">You hand her the buttplug."
                call her_main("Oh... right...","body_59")
                ">Hermione lifts her skirt and pushes it in gently, taking her time."
                $ hermione_buttplugs = True
                $ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_b_on.png"
                call her_main("{image=textheart}{image=textheart}{image=textheart}ah{image=textheart}{image=textheart}{image=textheart}...","body_106")
                call her_main("i better... head to class... now...","body_107")
                m "See you tonight [hermione_name]."
                call her_main("{size=-5}({image=textheart}it's... so... big...{image=textheart}){/size}","body_106")
            else:
                ">You pull out the buttplug."
                m "Ready for the phoenix again?"
                call her_main("Oh, alright then...","body_87",xpos=370)
                call her_main("but if you pay me and additional 5 points I'll turn around as I put it in...","body_105")
                menu:
                    "\"Done\"":
                        $ current_payout += 5
                        call her_main("thank you [genie_name], you won't regret it...","body_107")
                    "\"Fifty five is all I can do.\"":
                        m "Any more and people might get suspicious."
                        call her_main("hmmmm I suppose you're right...","body_103")
                        call her_main("but as a present i'll show you anyway...","body_124")
                        call her_main("although you better appreciate it...","body_129")
                        m "I'm sure I will."
                ">You hand her the buttplug."
                call her_main("well... here goes...","body_59")
                ">Hermione turns around, lifts her skirt and pushes it in gently, taking her time."
                $ hermione_buttplugs = True
                $ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_b_on.png"
                call her_main("{image=textheart}{image=textheart}{image=textheart}ah{image=textheart}{image=textheart}{image=textheart}...","body_106")
                call her_main("i better... head to class... now...","body_105")
                m "See you tonight [hermione_name]."
                call her_main("{size=-5}({image=textheart}it's... so... good...{image=textheart}){/size}","body_106")
            
        elif whoring >= 24 and buttplug_size == 2: # LEVEL 08+
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about wearing a buttpl-?"
            call her_main("I'll do it.","body_68",xpos=370)
            m "You're eager. I haven't even said what one yet..."
            call her_main("oh... can it be the big one... with the long tail...","body_87")
            call her_main("please...","body_105")
            m "well seeing as how you asked so nicely..."
            ">You hand her the buttplug."
            ">Hermione turns around and lifts her skirt giving you a full view as she inserts it."
            $ hermione_buttplugs = True
            $ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_b_on.png"
            call her_main("{image=textheart}ah{image=textheart}...","body_106")
            call her_main("Thank you [genie_name]!","body_107")
            call her_main("{size=-5}({image=textheart}it feels so good... I might have to buy my own...{image=textheart}){/size}","body_106")
    
    $ hg_ps_Buttplug_OBJ.inProgress = True
    
    call hg_pr_transition_block
    if buttplug_size == 2:
        $ hermione_buttplugs = True
        $ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_b_on.png"
    jump day_main_menu
    
label hg_ps_Buttplug_complete:
    call hg_pr_EnterRoom_block
    
    if whoring <= 15 and buttplug_size == 1: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            $ sc34CG(1, 8)
            call her_main("It was awful... of course...","body_09",xpos=370)
            m "Just tell me what happened, [hermione_name]..."
            call her_main("I've never been so uncomfortable in my life [genie_name]!","body_66")
            call her_main("I wasn't able to focus on anything all day!","body_81")
            m "Why's that?"
            call her_main("Whenever I was sitting down in class it just kept prodding me...","body_69")
            her "So naturally I had to adjust the way I was sitting, [genie_name]..."
            $ sc34CG(1, 9)
            call her_main("but that just made it worse...","body_69")
            m "Do you think anyone else noticed you?"
            call her_main("I've got no idea...","body_79")
            $ sc34CG(1, 10)
            call her_main("I could hardly think straight... Let alone notice other people.","body_79")
            m "So it felt good then?"
            call her_main("Good?","body_31")
            $ sc34CG(1, 12)
            call her_main("If you call getting your... butt teased all day good...","body_73")
            call her_main("Then yes, I suppose it did...","body_70")
            $ sc34CG(1, 13)
            call her_main("Still... being this distracted during class could really damage my grades...","body_117")
            m "I wouldn't worry about that. Just think of Gryffindor!"
            call her_main("Speaking of that...","body_81")
            hide screen sccg
            with d3
            m "Oh yes, quite right."
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            call her_main("It went well, [genie_name]...","body_31",xpos=370)
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Barely anybody noticed that I was wearing it..."
            call her_main("...Except for a few girls from Ravenclaw...","body_183")
            m "What happened?"
            call her_main("I was walking down the hall, on my way to potions class...","body_127")
            call her_main("And suddenly a gust of wind came and blew my skirt up...","body_44")
            m "A gust of wind? inside?"
            call her_main("It must have been from a window...","body_13")
            call her_main("Anyway the three girls walking behind me may have... seen it.","body_87")
            m "Did they say anything to you?"
            call her_main("No... But I did hear them giggling afterwards...","body_88")
            m "Well, it sounds like a job well done..."
        
        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            m "[hermione_name], how did it go?"
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            show screen blktone
            with d3
            call her_main("Awful, [genie_name]. Simply awful...","body_32",xpos=370)
            m "What happened?"
            call her_main("Moaning Myrtle happend!","body_33")
            m "Moaning Mittle?"
            call her_main("That pesky little ghost!","body_12")
            call her_main("This thing left me so frustrated that in my free period I went to the girls toilets to...","body_69")
            call her_main("Relieve myself...","body_29")
            call her_main("When all of a sudden that annoying ghost poked her head through the door!","body_30")
            call her_main("As it if wasn't bad enough that she saw me...","body_87")
            call her_main("She then started yelling \'Hermione has a buttplug\' to everyone in the toilets!","body_86")
            call her_main("Luckily the stalls where empty! Imagine if they weren't!","body_50")
            m "Well, it certainly sounds like you've earned your points."
    
    elif whoring <= 20 and buttplug_size == 1: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Of course.","body_31",xpos=370)
            m "Did anyone notice?"
            call her_main("Yes... well I might have...","body_59")
            call her_main("shown someone...","body_58")
            her "I was in the library fetching some books when I saw Luna..."
            her "She was reading at a desk..."
            call her_main("So I decided to walk over to her and have a chat...","body_56")
            call her_main("She was talking about something nonsensical...","body_54")
            her "And I figured that if she saw it..."
            her "no one would believe her..."
            m "alright..."
            call her_main("So I feigned dropping my quill...","body_56")
            m "Go on..."
            call her_main("then I turned around in front of her...","body_59")
            her "and bent over..."
            her "...keeping my knees straight..."
            call her_main("...giving her a full view...","body_78")
            m "I see..."
            m "Did she say anything?"
            call her_main("No, [genie_name]...","body_105")
            her "But when I turned back around she didn't make eye contact..."
            m "Hm..."
            call her_main("I don't think I've seen anyone blush so hard...","body_128")
            m "Well it sounds like you've earned your points and then some."
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            $ sc34CG(1, 9, 1)
            call her_main("I did, [genie_name]...","body_16",xpos=370)
            call her_main("Although I am still not sure how I feel about all of this...","body_29")
            $ sc34CG(1, 11, 1)
            call her_main("It's starting to really affect my grades...","body_29")
            call her_main("I couldn't even tell you what potions we were taught today...","body_31")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("Me, Hermione Granger...","body_87")
            $ sc34CG(1, 12, 1)
            call her_main("Not learning in class...","body_118")
            m "Well you could try relieving yourself in between lessons."
            $ sc34CG(1, 13, 1)
            call her_main("Oh, i've tried that... but it doesn't work...","body_117")
            her "It just makes the next class harder..."
            $ sc34CG(1, 12, 1)
            call her_main("today, After potions I went to my room to... calm myself...","body_107")
            call her_main("But it just made herbology worse...","body_87")
            $ sc34CG(1, 11, 1)
            call her_main("I was forced into touching myself in the middle of class...","body_88")
            call her_main("Do you think anyone noticed, [genie_name]?","body_190")
            $ sc34CG(1, 9, 1)
            menu:
                "\"What? Of course not, [hermione_name]!\"":
                    $ sc34CG(1, 8, 2)
                    call her_main("..............","body_188")
                    call her_main("You are right, [genie_name]...","body_124")
                    her "I was very discreet..."
                    $ sc34CG(1, 12, 3)
                    call her_main("very quiet...","body_121")
                    call her_main("barely making a sound...","body_68")
                    call her_main("[genie_name], can I get paid now, please?","body_58")
                    her "......"
                "\"Of course they did!\"":
                    $ sc34CG(1, 13, 2)
                    m "Do you honestly believe that no one noticed you touching yourself?"
                    call her_main("I was afraid that you would say that, [genie_name]...","body_20")
                    m "You were surrounded by people!"
                    call her_main("........","body_20")
                    call her_main("[genie_name], can I get paid now, please?","body_21")
            hide screen sccg
            with d3
            m "Certainly."
        
        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            $ sc34CG(1, 11)
            call her_main("Yes, [genie_name]. I did.","body_16",xpos=370)
            m "Great. Tell me more."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("Well, there's not much to tell...","body_14")
            $ sc34CG(1, 12)
            her "I attended classes..."
            her "tried to take notes."
            her "all in all it was a fairly regular day..."
            $ sc34CG(1, 13)
            call her_main("Well as regular as it could have been with a plug up my butt.","body_69")
            m "and Nobody noticed?"
            call her_main("I don't think so, [genie_name].","body_79")
            $ sc34CG(1, 11)
            m "Well I suppose something interesting can't happen everyday."
            hide screen sccg
            with d3
            
    
    elif whoring >= 21 and buttplug_size == 1: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name].","body_06",xpos=370)
            m "Well? How was your day?"
            call her_main("great, [genie_name]...","body_78")
            m "go on..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            $ sc34CG(1, 14, 1)
            call her_main("Well I've worked out how to deal with this thing being in me all day...","body_105")
            m "Really? And how is that?"
            call her_main("before now I've been going around it the wrong way...","body_107")
            call her_main("I just tried to ignore it...","body_127")
            her "and pay attention in class..."
            call her_main("But that didn't work at all...","body_44")
            call her_main("I was just too... distracted...","body_59")
            $ sc34CG(1, 15, 2)
            call her_main("So I thought to myself that I've just got to focus on it...","body_78")
            $ sc34CG(1, 16, 3)
            call her_main("block out everything else...","body_124")
            $ sc34CG(1, 17, 2)
            call her_main("...embrace it...","body_123")
            m "and how did you do that?"
            call her_main("well if I rock my hips while I'm sitting in class it's almost enough...","body_128")
            $ sc34CG(1, 16, 3)
            call her_main("but if I sit of the edge of my chair while I rock my hips...","body_129")
            $ sc34CG(1, 17, 2)
            call her_main("{image=textheart}{image=textheart}{image=textheart}","body_121")
            m "So you worked out how to pleasure yourself in class."
            call her_main("I did [genie_name].","body_124")
            her "Although I worry that it will really start to affect my grades..."
            m "Well I'm sure that missing one class a day is something you can catch up on."
            $ sc34CG(1, 15, 2)
            call her_main("only One?","body_122")
            m "You mean to say that you spent all your class time pleasuring yourself?"
            $ sc34CG(1, 17, 2)
            call her_main("..........","body_121")
            m "Nice work, [hermione_name]."
            hide screen sccg
            with d3
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name].","body_06",xpos=370)
            call her_main("But, umm...","body_11")
            m "...?"
            call her_main("Well, I may have gotten a bit more attention than I had hoped for...","body_85")
            call her_main("...............","body_88")
            m "Tell me what happened, [hermione_name]."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("I might have had a few photos taken...","body_87")
            m "Photos..."
            call her_main("Well I was in the library minding my own business...","body_83")
            her "When I went to get a copy of Zygmunt Budge's book of potions."
            call her_main("as it was on the bottom shelf I had to kneel down to reach it...","body_82")
            call her_main("When all of a sudden I heard the flash of a camera!","body_103")
            her "I turned around and there was Colin Creevey..."
            her "with the biggest grin on his face!"
            m "You let your photo be taken?!"
            call her_main("I didn't let anything of the sort happen! It was without my consent!","body_86")
            call her_main("I even made him promise not to show anyone the photo...","body_87")
            her "...in exchange I did have to let him take a few more..."
            her "but he insisted that he wouldn't show anyone else..."
            m "And you believe him?"
            call her_main("Of course [genie_name], he's a Gryffindor.","body_83")
            call her_main("Although the thought did cross my mind.","body_87")
            call her_main("What if he were to distribute the photos around the school.","body_88")
            call her_main("Imagine everyone looking at photos of me...","body_107")
            her "Everyone would know what I was wearing..."
            call her_main("Any time someone saw me they'd think about whether or not it was in...","body_124")
            m "That's quite the thought process."
            call her_main("Yes, well I certainly don't want that happening...","body_129")
            m "I'm sure..."
            call her_main("","body_128")
            m "It sounds like a job well done [hermione_name]."
        
        elif one_out_of_three == 3: 
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes, I did [genie_name]...","body_129",xpos=370)
            m "Did anyone notice?"
            her "maybe a few third years..."
            m "well go on."
            call her_main("It was the stairs...","body_128")
            her "I may have gotten a little carried away with myself..."
            m "What happened, [hermione_name]?"
            call her_main("Well as I was walking to divination class I ended up in front of a group of third year students...","body_129")
            call her_main("And seeing as how they were behind me on the stairs they may have been able to... see it.","body_128")
            m "So you intentionally showed it to a group of boys? You don't expect me to grant you extra points for showing them, do you?"
            call her_main("Of course not, [genie_name].","body_188")
            m "Then why do it?"
            call her_main("Well, it just sort of just happened...","body_190")
            call her_main("plus the look on their faces when they noticed it...","body_123")
            call her_main("they could barely hide their...","body_121")
            m "So you like being seen then?"
            call her_main("well...","body_107")
            m "Well done, [hermione_name]."
            call her_main("","body_124")

    elif whoring <= 19 and buttplug_size == 2: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how was it?"
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("It was awful... simply awful...","body_09",xpos=370)
            m "what happened, [hermione_name]..."
            call her_main("It was that nasty professor snape, [genie_name]!","body_103")
            call her_main("I've never been so embarassed in my life!","body_81")
            m "What did he do?"
            call her_main("Well in potions class I may have corrected him about the proper way to crush a Sopophorous bean...","body_69")
            her "so he made me stand out the front and show him the \'correct\' way..."
            call her_main("and what's worse is that he made me do it facing away from the class...","body_79")
            m "Do you think anyone saw it?"
            call her_main("Everyone saw it!","body_85")
            call her_main("I could barely even crush the bean my legs were shaking that hard...","body_88")
            m "Well it sounds like you earned your points."
            call her_main(".......","body_71")
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            call her_main("It went well, [genie_name]...","body_31",xpos=370)
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "A group of second years from \"hufflepuff\" even complemented me on it..."
            call her_main("...they said that it looked cute...","body_68")
            m "did anything else happen?"
            call her_main("well seeing as how they were so nice...","body_59")
            call her_main("I might have flicked my skirt up for them...","body_105")
            m "you showed it to them?"
            call her_main("well they were so kind...","body_107")
            call her_main("and they could already see most of it...","body_124")
            m "Did they say anything to you?"
            call her_main("No... But the looks on their faces...","body_128")
            m "Well, it sounds like a job well done..."
        
        elif one_out_of_three == 3: ### EVENT (C) cat swatting it
            label buttplug_magic_show:
                pass
            $ buttplug_magic_known = True
            m "[hermione_name], how did it go?"
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            show screen blktone
            with d3
            call her_main("what on earth did you do to this thing?!","body_32",xpos=370)
            m "What happened?"
            call her_main("Why did you not tell me this \'thing\' was cursed!","body_33")
            m "Cursed?"
            call her_main("It vibrates!","body_12")
            m "Really? When?"
            call her_main("when something else touches it...","body_69")
            m "Wouldn't your skirt set it off then?"
            call her_main("I think it has to be alive...","body_29")
            call her_main("All I know is that when my cat crookshanks swatted at it went off!","body_30")
            m "How bad was it?"
            call her_main("It was ridiculous! I was barely able to stand...","body_131")
            call her_main("but then crookshanks thought it was some sort of game... he wouldn't leave it alone...","body_132")
            call her_main("the vibrations were so intense that my knees gave out and I collapsed onto my bed!","body_118")
            call her_main("then he just played with it for hours...","body_122")
            m "are you still up for wearing it in the future?"
            call her_main("I suppose... So long as I know how it works now.","body_120")
            call her_main("I'll just have to keep it away from crookshanks...","body_118")
            call her_main("{size=-6}or not...{/size}","body_121")
            m "Well good work then [hermione_name]"
    
    elif whoring <= 23 and buttplug_size == 2: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A) luna plays with it in the library
            if not buttplug_magic_known:
                jump buttplug_magic_show
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you have fun?"
            show screen blktone
            with d3
            call her_main("I suppose you could say that.","body_59",xpos=370)
            m "Anything interesting happen?"
            call her_main("Yes... well I might have...","body_59")
            call her_main("had someone...","body_60")
            call her_main("touch it...","body_58")
            m "hmmmm..."
            call her_main("It was luna lovegood again.","body_56")
            call her_main("We ended up sitting next to each other in class.","body_13")
            her "we were talking about school, clothes..."
            m "Yes, yes, spit it out..."
            call her_main("well she said that she thought my tail was cute...","body_56")
            m "Go on..."
            call her_main("then she asked so politely if she could touch it...","body_59")
            call her_main("I could hardly say no...","body_107")
            call her_main("so I... let her spend the rest of the lesson... playing with it...","body_105")
            m "I see..."
            m "Did she realise what was happening?"
            call her_main("maybe... it felt so good that it was hard to keep it hidden.","body_121")
            her "But I think that just made her want to touch it more..."
            m "Hm..."
            call her_main("I don't think I've ever had a better lesson...","body_123")
            m "Well it sounds like you've earned your points and then some."
        
        elif one_out_of_three == 2: ### EVENT (B) 
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("I did, [genie_name].","body_16",xpos=370)
            call her_main("Only... ehm...","body_68")
            m "What is it this time [hermione_name]?"
            call her_main("Well... you know my friend...","body_45")
            her "Ginny Weasley..."
            call her_main("well I told her about the tail...","body_188")
            her "and how it worked and well..."
            m "Just say it, [hermione_name]."
            call her_main("Well, we decided to skip herbology class together...","body_107")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("And then she sort of grabbed it...","body_106")
            call her_main("And she just played with it so aggressively...","body_123")
            her "I was a mess afterwards..."
            g9 "And did you return the favour?"
            if touched_by_boy == True:
                call her_main("Err... maybe...","body_190")
                m "What did you do?"
                call her_main("well I don't want to say too much [genie_name].","body_188") # :)
                her "but after she saw what it was doing to me..."
                her "she insisted that I let her have a go..."
                call her_main("and that's all I'll say...","body_124") # :)
                m "Hmmmm, well you did earn your points [hermione_name], even if you are secretive about it..."
            else:
                call her_main("...No.","body_87")
                m "Why not?"
                call her_main("well I don't mind letting her touch the tail [genie_name].","body_82") # :)
                her "but anything else..."
                m "Very good [hermione_name]..."
        
        elif one_out_of_three == 3: ### EVENT (C) called a slut by slytherin
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes, [genie_name]. I did.","body_103",xpos=370)
            m "Great. Tell me more."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("Well, there's not much to tell...","body_87")
            her "I attended classes..."
            her "studied for the upcoming potions exam..."
            call her_main("it was a normal day except for a group of those nasty \"slytherin\" tramps...","body_103")
            call her_main("I was minding my business on the way to class when they called me a \"butt slut\".","body_118")
            m "did you say anything back to them?"
            call her_main("and sink to their level...","body_69")
            m "Well I suppose it's for the best."
            
    
    elif whoring >= 24 and buttplug_size == 2: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A) groped by first years
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], how was your day?"
            show screen blktone
            with d3
            call her_main("Awful, I was attacked by a group of rabid students, [genie_name].","body_62",xpos=370)
            m "Attacked? By How many?"
            call her_main("six first years, [genie_name]...","body_61")
            m "you were attacked by first years?"
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("I may have been exaggerating slightly...","body_10")
            m "what happened?"
            call her_main("well I was sitting in the library, minding my own business...","body_12")
            call her_main("when all of a sudden a group of first year students came from nowhere asking me all these questions...","body_97")
            call her_main("\"is it fluffy\"...","body_103")
            call her_main("\"why are you wearing it\"...","body_118")
            call her_main("\"does it feel nice\"...","body_124")
            call her_main("\"can we touch it\"...","body_124")
            call her_main("\"can you make it wag\"...","body_122")
            m "what did you do?"
            call her_main("well I made them promise to keep quiet about it...","body_120")
            call her_main("but in exchange I may have had to let them touch it...","body_87")
            call her_main("{image=textheart}{image=textheart}{image=textheart}","body_121")
            m "So you let a group of innocent first years touch your buttplug..."
            call her_main("It sounds sinister when you put it like that.","body_103")
            her "All I did was take them to a secluded part of the library and let them touch my tail..."
            m "Well that's alright then..."
            call her_main(".......","body_124")
            m "So did you enjoy it?"
            call her_main("..........","body_117")
            call her_main("Truthfully [genie_name].... It was the most one of the most pleasurable experiences of my life...","body_123")
            call her_main("all their hands touching it...","body_121")
            call her_main("taking turns...","body_106")
            call her_main("all the while it was vibrating away...","body_124")
            call her_main("I nearly passed out.","body_133")
            call her_main("I even tried to make them stop...","body_134")
            call her_main("but they just kept going...","body_136")
            m "Nice work, [hermione_name]."
        
        elif one_out_of_three == 2: ### EVENT (B) glory hole with astoria
            if not buttplug_magic_known:
                jump buttplug_magic_show
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name]...","body_06",xpos=370)
            call her_main("Did you know there are holes between the stalls in the girls bathroom?","body_55")
            m "i did not, but What does that have to do with your buttplug?"
            call her_main("Well, I noticed that the hole is the same height as the tail...","body_56")
            call her_main("...............","body_57b")
            m "go on, [hermione_name]."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("I might have put it through...","body_59")
            m "what?"
            call her_main("Well I was in the stall finishing up...","body_54")
            her "When a girl entered the other stall."
            call her_main("I wasn't sure but I thought that it may have been a \"slytherin\"...","body_44")
            call her_main("So I decided to stick my tail through!","body_46")
            m "did they touch it?"
            call her_main("not immediately...","body_54")
            call her_main("but after I gave it a little wiggle she eventually came around...","body_68")
            call her_main("she was curious at first but eventually she started to really play with it...","body_107")
            call her_main("stroking it... flicking it... I even think she may have licked it...","body_121")
            her "...imagine that... a slytherin, licking something that was in my..."
            her "It was incredible... I could barely stand while it happened..."
            m "did you find out who it was?"
            call her_main("I did [genie_name].","body_11")
            call her_main("It was at lunch, in the great hall.","body_127")
            call her_main("I was walking past the slytherin table on my way to sit down...","body_127")
            call her_main("when I saw that little... vixen, astoria greengrass.","body_129")
            her "she couldn't take her eyes off of it..."
            call her_main("imagine that... astoria greengrass... pureblood, licking my...","body_136")
            call her_main("{image=textheart}........{image=textheart}","body_121")
            m "It sounds like you've earned your points today then [hermione_name]."
            call her_main("...{size=-7}(I would have done this for free...){/size}","body_59")
        
        elif one_out_of_three == 3: 
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes, I did [genie_name]...","body_129",xpos=370)
            m "Anything interesting happen?"
            her "do you know that Patil twins [genie_name]?"
            m "no but do continue."
            call her_main("well they were walking down the hall behind me...","body_128")
            her "I swear I could hear them whispering to each other..."
            call her_main("and I thought I may as well give them something to talk about...","body_129")
            call her_main("So I stopped, kept my knees straight and bent over as far as I could...","body_128")
            m "You exposed yourself just like that?"
            call her_main(".......","body_188")
            m "Very good, [hermione_name]!"
    
    $ gryffindor += current_payout #55
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."
    
    $ hg_ps_Buttplug_OBJ.points += 1
    $ hg_ps_Buttplug_OBJ.complete = True
    $ hg_ps_Buttplug_OBJ.inProgress = False
    $ hermione_buttplugs = False
    
    call hg_pr_transition_block
    return
