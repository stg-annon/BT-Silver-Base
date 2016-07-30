
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
                $ hg_ps_PantyThief_OBJ.hearts_level = 2 #Event hearts level (0-3)
                
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
                $ hg_ps_PantyThief_OBJ.hearts_level = 3 #Event hearts level (0-3)
                
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
        jump hg_ps_WearMyCum_Scene_1 #This is 1 until I write 2
    else:
        jump hg_ps_WearMyCum_Scene_1 #This is 1 until I write 3







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
    call her_head("And make me where it around the school?","body_131")
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
    $ hermione_chibi_xpos = 500 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_blink #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3


    jump end_hg_pf




label hg_ps_WearMyCum_Scene_2:



label hg_ps_WearMyCum_Scene_3:



label hg_ps_WearMyCum_complete: #Hermione returns from her day of wearing your cum
    $ hg_ps_WearMyCum_OBJ.inProgress = False
    jump hg_ps_WearMyCum_complete_1


label hg_ps_WearMyCum_complete_1:
    if cum_location == 1: #Cum under shirt
        $ aftersperm = True
        ">Hermione returns to your office, your cum stains still visible on her shirt."
        call her_main("...I did it [genie_name].","body_53")
        call her_main("I kept your cum on me all day.","body_54")
        menu:
            "\"50 Points to gryffindor!\"":
                $ gryffindor =+ 50
                call her_main("Thank you [genie_name], will that be all?","body_55")
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, I had potions class and then transfiguration.","body_16")
                m "And do you think that anyone noticed?"
                call her_main("I don't think so [genie_name]. Ginny Weasley asked me about it during transfiguration class though.","body_15")
                m "And what did you tell her?"
                call her_main("I just said that I spilled some Wiggenweld potion on myself in potions class.","body_14")
                m "Very cunning of you. 50 points to Gryffindor."
                $ gryffindor =+ 50
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
                $ gryffindor =+ 50
                call her_main("Thank you [genie_name], will that be all?","body_29")
                m "Yes [hermione_name], you may leave now. "
            "\"Tell me about your day.\"":
                call her_main("It was a pretty normal day, I had potions class and then transfiguration.","body_29")
                m "And do you think that anyone noticed?"
                call her_main("I think a few people did [genie_name]. I could hear The first years all whispering as I walked past.","body_57b")
                m "And how did you feel?"
                call her_main("Excited. I just wish that they knew why I was doing this.","body_59")
                m "Speaking of that, 50 points to Gryffindor."
                $ gryffindor =+ 50
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
                $ gryffindor =+ 50
                $ mad =+ 5
                call her_main("...","body_50","tears_03a")
                m "Well [hermione_name], you may leave now."
                call her_main("Hmmmphh...","body_51","tears_03a")
            "\"Tell me about your day.\"":
                $ mad =+ 10
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
    

label hg_ps_WearMyCum_complete_3:

#Blowjob in front of Luna
#Genie tells Hermione to go fetch a student and that she will be sucking him off while he talks to them

#Three variants, each with a differing level of exhibitionism
#1 Hermione is as silent as possible, Luna almost completely unaware
#2 Hermione quite loud, Luna actively aware that something is wrong
#3 Hermione crawls out from under the desk covered in Genie's cum trying to pass it off
label hg_ps_HiddenBlowjob:




label hg_ps_HiddenBlowjob_complete:

