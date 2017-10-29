##(Level 01) (5 pt.) (Flirt with classmates). (Available during daytime only).
label hg_pr_FlirtClassmate:
    hide screen hermione_main
    with d3
    m "{size=-4}(Ask her to go flirt with some boys from \"Slytherin\"?){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    m "[hermione_name]?"
    call her_main("Yes?","body_13",xpos=140)
    if hg_pr_FlirtClassmate_OBJ.points == 0 and whoring <= 5: ### LEVEL 01 and LEVEL 02
        ### LEVEL 01 ### <===============================================================FIRST EVENT!
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "What is your opinion on the boys of the \"Slytherin\" house?"
        call her_main("I detest them, [genie_name].","body_05")
        m "Well, too bad. Because I want you to get really friendly with a few of them today."
        call her_main("If I must...","body_13")
        her "Yes, I think I can manage to be civil with them for one day."
        m "Yes, and when I say \"get friendly with them...\""
        m "I actually mean that I need you to flirt with them..."
        call her_main("Flirt?!","body_48")
        call her_main("[genie_name]!","body_47")
        call her_main("I'm not even going to ask why you'd be interested in this, [genie_name]...","body_17")
        call her_main("But why \"Slytherin\"?","body_11")
        her "If you need me to be flirtatious today, I think I can manage that..."
        her "But, please, can't be another house?"
        call her_main("The \"Gryffindors\" maybe?","body_44")
        m "I am only trying to protect your reputation, [hermione_name]."
        call her_main("[genie_name]?","body_15")
        m "Do you value the opinion the \"Slytherin\" students have of you?"
        call her_main("I couldn't care less about the opinions of those Neanderthals.","body_30")
        m "What about the students of the \"Gryffindor\" house?"
        call her_main("Their opinion means the world to me--","body_29")
        call her_main("Oh, I see...","body_06")
        m "Exactly... Just looking out for you [hermione_name]."
        her "Em... Thank you [genie_name]..."
        call music_block
        
    else:
        if whoring <= 2: ### LEVEL 01
            m "I need you to go make some new friends at \"Slytherin\" house."
            her "You mean you need me to flirt with the \"Slytherin\" boys again [genie_name]?"
            m "That's exactly what I need you to do today, [hermione_name]."
            call her_main("Must I really do this [genie_name]?","body_02")
            m "We have been through this, [hermione_name]."
            m "Going to the \"Slytherin\" boys is in your best interests."
            call her_main("Yes, I know, [genie_name].","body_04")
            her "But why must I this at all?"
            m "Nobody is forcing you, [hermione_name]..."
            call her_main("You don't need to remind me of that, [genie_name]...","body_05")
            call her_main("Alright if I must... [genie_name]...","body_07")
            
        else: #if whoring >= 3 and whoring >= 6: ### LEVEL 02 and higher ## <=========================================================== SECOND EVENT!
            m "I need you to flirt with some boys of the \"Slytherin\" house today."
            her "I will see what I can do, [genie_name]."
            m "Great. I'll be expecting your report today after classes."
    her "Well, I'd better go now. Classes are about to start..."
    
    $ hg_pr_FlirtClassmate_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_FlirtClassmate_complete:
    call hg_pr_EnterRoom_block
    call her_main("Good evening, [genie_name].","body_01",xpos=370,ypos=0)
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."
    menu:
        "\"Great. You earned your points.\"":
            pass
        "\"Give me the details.\"":
            hide screen hermione_main
            with d3
            m "How many boys did you flirt with today, [hermione_name]?"
            m "Give me the details."
            show screen blktone
            with d3
            if whoring >= 0 and whoring <= 2: ### LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    call her_main("Well...","body_10",xpos=370)
                    her "There was this one freshman boy..."
                    her "........."
                    m "I'm listening..."
                    her "Well... I went to him and I said \"Hey, handsome!\"."
                    m "And?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("He showed me his tongue and ran off, [genie_name].","body_07")
                    m "Did you try to lure him in with a lolipop?"
                    call her_main("I did not, [genie_name]...","body_10")
                    her "The thought never crossed my mind, but--"
                    m "That was a joke, [hermione_name]."
                    call her_main("[genie_name]?","body_07")
                    m "I didn't send you out there to harass little kids!"
                    call her_main(".............","body_09")
                    m "I told you to flirt with boys {size=+5}your{/size} age!"
                    call her_main("I wanted to at first, but...","body_07")
                    call her_main("I guess I got scared...","body_12")
                    her "I mean I despise those \"Slytherins\" way too much to flirt with them, [genie_name]!"
                    call her_main("I would have to fight my gag-reflex the entire time!","body_05")
                    menu:
                        "\"Fine. Just try harder next time.\"":
                            call her_main("Thank you, [genie_name].","body_06")
                            her "I will, I promise!"
                        "\"Favour failed! No points for you!\"":
                            stop music fadeout 1.0
                            call her_main("I understand...","body_07")
                            m "Get out of my sight..."
                            call her_main("Yes, [genie_name]...Sorry, [genie_name]...","body_09")
                            jump could_not_flirt
                
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Well, I tried to complement an upperclassman...","body_10",xpos=370)
                    m "Did he appreciate it?"
                    call her_main("He called me a \"Gryffindor whore\", [genie_name]!","body_76")
                    m "I see..."
                    m "What did you do then?"
                    call her_main("Well that was not the proper way to address a fellow \"Hogwarts\" student...","body_04")
                    her "So I told him that I would report him."
                    m "A truly captivating story..."
                    m "Anything else?"
                    call her_main("Yes, there was also this one student at the library...","body_09")
                    her "He was obviously struggling with a problem..."
                    her "So I offered my help..."
                    m "And?"
                    call her_main("He called me a \"Patronizing Gryffindor Whore\", [genie_name]...","body_76")
                    m "Did you threaten to report him as well?"
                    call her_main("Of course, [genie_name].","body_04")
                    m "*sigh*"
                    m "Anything else?"
                    call her_main("Well, there was one more incident but the outcome was pretty much the same...","body_09")
                    m "\"The Gryffindor whore\"?"
                    call her_main(".........yes, [genie_name].","body_66")
                    m "You are doing it all wrong, [hermione_name]."
                    call her_main("I am sorry, [genie_name]. I thought this would be easy...","body_69")
                    menu:
                        "\"Well, at least you are trying.\"":
                            call her_main("Apparently flirting is not my forte...","body_34")
                        "\"Favour failed! No points of you!\"":
                            stop music fadeout 1.0
                            call her_main("You are not going to pay me, [genie_name]?","body_11")
                            $ mad +=15
                            call her_main("But, you promised!","body_21")
                            call her_main("................","body_20")
                            jump could_not_flirt
                
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    call her_main("Well, the \"Slytherin\" quidditch team was practicing in the stadium today...","body_10",xpos=370)
                    her "I thought I could sneak into the bleachers and cheer them on..."
                    call her_main("But...","body_12")
                    m "Yes?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("A whole flock of those \"Slytherin\" harlots was already there, [genie_name].","body_77")
                    her "They were cheering and yelling..."
                    call her_main("And one of them even exposed herself in an inappropriate manner to the players, [genie_name]...","body_47")
                    her "I cannot believe our school accepts such behavior..."
                    m "So... how did this captivating drama end?"
                    call her_main("I just left [genie_name]...","body_69")
                    menu:
                        m "Hm..."
                        "\"Well, here are your points.\"":
                            call her_main("Thank you, [genie_name]...","body_16")               
                            
                        "\"Favour failed! No points for you!\"":
                            stop music fadeout 1.0
                            call her_main("I don't feel like I deserved any this time anyway...","body_12")
                            jump could_not_flirt
            
            elif whoring >= 3 and whoring <= 5: ### LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    call her_main("Well, there was this one guy at the library...","body_10",xpos=140)
                    her "He was obviously struggling with some assignment, so I offered my help..."
                    m "And?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Well, to my surprise he accepted it...","body_75")
                    her "He let me finish the assignment for him..."
                    call her_main("While I was working he made a couple of inappropriate comments but I just smiled in response...","body_34")
                    m "So, basically, he was the one doing the flirting..."
                    call her_main("well... yes.","body_24")
                    call her_main("But, despite my better judgment I did encourage his improper behavior...","body_45")
                    m "By being quiet?"
                    her "Yes [genie_name]..."
                    her "I mean, this does amount to something, right?"
                    m "Meh..."
                    m "What else do you have for me?"
                    call her_main("Right...","body_69")
                    her "Later in a corridor these two other guys complemented my appearance in a very vulgar manner..."
                    call her_main("But I just smiled at them...","body_34")
                    m "You were on the receiving end again, then..."
                    m "This is not what I ordered you to do, [hermione_name]."
                    call her_main("I know, [genie_name]!","body_34")
                    call her_main("But I am so busy. Between the \"MRM\" meetings and the classes...","body_69")
                    her "I barely have any time--"
                    m "Is this all you got for me this time then?"
                    call her_main("No, [genie_name].","body_69")
                    her "Just an hour ago or so I ran into Draco Malfoy, [genie_name]."
                    m "No way!!! (No idea who that is...)"
                    her "I forced myself to be friendly with him and..."
                    call her_main("We ended up having a decent conversation for a change.","body_74") 
                    m "I see... That \"Dark-oh\" guy..."
                    m "Was he looking at your legs at all?"
                    call her_main("What?","body_02")
                    m "Did he stare at your legs or not, [hermione_name]?"
                    call her_main("Em... He might have...","body_44")
                    m "What about your tits?"
                    call her_main("[genie_name]!!!","body_47")
                    m "Fine. You get your points. Keep up the good work."
                    call her_main("","body_29")
                
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 1.0
                    call her_main("Well...","body_10",xpos=370)
                    her "This morning I did flirt with this one guy..."
                    call her_main("Then after the second period there was this other guy...","body_13")
                    call her_main("And then something bizarre happened...","body_28")
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "This angry-looking guy from the \"Slythetin\" came to me and asked me out on a date..."
                    call her_main("I told him \"no\" at first, but we ended up taking a walk together.","body_13")
                    m "Did you enjoy yourself, [hermione_name]?"
                    call her_main("I think I did [genie_name]... To my own astonishment...","body_31")
                    call her_main("There was something about his \"devil-may-care\" attitude...","body_45")
                    call her_main("He was so confident and calm and...","body_74")
                    call her_main("I still loathe the \"Slytherin\" house of course!","body_34")
                    call her_main("But...","body_73")
                    her "Maybe some of the students got there by mistake?"
                    call her_main("Could the \"sorting hat\" make... miscalculations ?","body_10")
                    menu:
                        "\"Just take your points and go!\"":
                            call her_main("................","body_07")
                        "\"The almighty hat is never wrong!\"":
                            call her_main("Yes, of course... Everybody knows that...","body_13")
                        "\"Could what make what?\"":
                            call her_main("Oh, nevermind me, [genie_name].","body_13")
                            her "Everyone knows that the \"Sorting Hat\" is never wrong."
                
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Five guys, [genie_name]!","body_75",xpos=370)
                    m "Really?"
                    call her_main("Yes!","body_74")
                    call her_main("This one guy this morning.","body_74")
                    her "Then another two right after the first period."
                    her "And then another one before the third period."
                    call her_main("And after that I had a surprisingly pleasant conversation with one more.","body_68")
                    call her_main("That last one was quite smart and well mannered too.","body_74")
                    her "............................"
                    her "................"
                    call her_main("But I still refuse to change my opinion about the \"Slytherin\" house, [genie_name].","body_34")
                    m "I'm not asking you to, [hermione_name]."
                    her "I am only doing this to help my own house!"
                    call her_main("The proud house of \"Gryffndor\"!","body_32")
                    m "Alright, alright, calm down, [hermione_name]."
                    call her_main("","body_74")

            elif whoring >= 6: # LEVEL 03 and higher.
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ sc34CG(2, 7, 1, 1)
                    call her_main("Eleven boys, [genie_name]!","body_75",xpos=370)
                    m "Eleven? Really? Your personal best, [hermione_name]."
                    call her_main("Yes.","body_74")
                    call her_main("Let's see...","body_68")
                    her "Those two handsome guys right before the first period started..."
                    call her_main("Then I exchanged a few rather inappropriate messages with this other guy, during the the first period.","body_64")
                    call her_main("After that there was this one other guy...","body_68")
                    call her_main("Then those three guys...","body_73")
                    call her_main("Then one more right before the last period...","body_74")
                    call her_main("And finally this last guy that walked me right to your tower, [genie_name]...","body_75")
                    m "So, eleven then?"
                    m "Those \"Slytherin\" boys are really starting to like you, huh?"
                    $ sc34CG(2, 7, 1, 2)
                    call her_main("I suppose so...","body_74")
                    call her_main("Well, not all of them were nice to me at first...","body_73")
                    call her_main("But I use this trick to \"tame\" them.","body_64")
                    m "A trick?"
                    $ sc34CG(2, 6, 1, 1)
                    call her_main("Yes... Whenever a boy from \"Slytherin\" is being mean to me or calls me a name...","body_74")
                    her "I just swallow my pride and smile in response."
                    m "Hm..."
                    m "So, if for example, somebody were to call you a \"whore\" you would just smile at them?"
                    call her_main("Well, yes, [genie_name]...","body_34")
                    m "Yeah, I'm sure that wins them over."
                    m "Great job, [hermione_name]."
                    call her_main("","body_68")
                    hide screen sccg
                    with d3
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Two dates, seven quite pleasant conversations...","body_75",xpos=370)
                    call her_main("And I even let this one guy kiss me...","body_68")
                    m "Quite impressive, [hermione_name]."
                    call her_main("I think so too, [genie_name]. Thank you.","body_74")
                    call her_main("Oh, and there was also this little freshman kid...","body_75")
                    her "I tried to flirt with him too, but we ended up just chatting..."
                    her "He kept calling me \"Miss Hermione\"..."
                    her "So adorable..."
                    m "Well I didn't send you to harass little kids, [hermione_name]."
                    call her_main("I didn't haras--","body_66")
                    call her_main("[genie_name]! Seven flirts and two dates amount to something, don't they?","body_34")
                    m "Oh, absolutely."
                    call her_main("Then I would like to receive my payment now...","body_30")
                    call her_main("","body_33")
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    call her_main("[genie_name], I am sorry, but...","body_33",xpos=370)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("I hate those \"Slytherin\" tramps, [genie_name]!","body_47")
                    m "Tell me what happened."
                    call her_main("I don't want to talk about it...","body_69")
                    m "Tell me what happened, [hermione_name]!"
                    call her_main("I don't want to talk about it, [genie_name].","body_76")
                    call her_main("Please don't make me...","body_69")
                    menu:
                        "\"Fine. I'll let it go for today.\"":
                            call her_main("Thank you, [genie_name].","body_33")
                            m "No luck with the flirting today then?"
                            call her_main("Oh, quite the opposite, [genie_name].","body_34")
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            her "One of the boys actually took me to the \"Slytherin\" common room today..."
                            call her_main("There were at least a dozen of them there...","body_03")
                            call her_main("All of the boys knew who I was...","body_04")
                            her "I was the center of attention at first..."
                            call her_main("And it felt sort of wonderful...","body_78")
                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                            call her_main("Then a bunch of those \"Slytherin\" harlots stumbled in and...","body_66")
                            m "And?"
                            call her_main("Well, they started saying stuff and doing things...","body_69")
                            her "Anyway, I had to leave..."
                            m "I see..."
                            m "Well, I say you deserve your points anyway, [hermione_name]."
                            call her_main("","body_74")

                        "\"Tell me now, or lose the points!\"":
                            $ mad +=10
                            call her_main("[genie_name], please, I don't want to discuss this with you, [genie_name].","body_66")
                            m "No one is forcing you, [hermione_name]."
                            m "You are free to leave."
                            call her_main("{size=-4}(Stubborn old man!){/size}","body_47")
                            jump could_not_flirt
            
    $ gryffindor +=5
    m "The \"Gryffindor\" house gets 5 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_FlirtClassmate_OBJ.points += 1
    $ hg_pr_FlirtClassmate_OBJ.complete = True
    $ hg_pr_FlirtClassmate_OBJ.inProgress = False
    
    if whoring <= 2:
        $ whoring +=1
    
    call hg_pr_transition_block
    return
    
    
##(Level 02) (15 pt.) (Flirt with teachers). (Available during daytime only).
label hg_pr_FlirtTeacher:
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests

    m "[hermione_name], I want you to be especially flirtatious with your teachers today."
    if whoring <=2 or hg_pr_FlirtClassmate_OBJ.points <= 1:
        jump too_much
   

    if hg_pr_FlirtTeacher_OBJ.points == 0 and whoring <= 8: ### up to LEVEL 03
    ### LEVEL 03 ### <===============================================================FIRST EVENT!
        call her_main("I will do my best, [genie_name]!","body_01",xpos=140)
        call her_main("I am glad you finally decided to act, [genie_name]!","body_02")
        m "Huh?"
        call her_main("You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?","body_07") 
        call her_main("I am honoured to pose as bait in this noble endeavor.","body_16")
        m "Ehm... Yeah, that's exactly what I'm doing."
        call her_main("Splendid! You can count on me, [genie_name]!","body_07")
    else:
        call her_main("I shall provide you with a detailed report later tonight, [genie_name].","body_07",xpos=140)
        m "I will be waiting..."
    

    
    her "Well, I'd better go now. Classes are about to start..."
    
    $ hg_pr_FlirtTeacher_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_FlirtTeacher_complete:
    call hg_pr_EnterRoom_block
    call her_main("Good evening, [genie_name].","body_01",xpos=370,ypos=0)
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."
    menu:
        "\"Great. Here are your points.\"":
            pass
        "\"Give me the details.\"":
            hide screen hermione_main
            with d3
            m "Tell me how many teachers did you flirt with, [hermione_name]?"
            m "Give me the details."
            show screen blktone
            with d3
    
            if  whoring >= 3 and whoring <= 5: ### LEVEL 02 <===================================================================== EVENT LEVEL 01
                if one_out_of_three == 1: ### EVENT (A) Flitwick
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Well, I tried flirting with Professor Flitwick...","body_10",xpos=370)
                    call her_main("But it didn't really work...","body_09")
                    call her_main("..............................","body_12")
                    m "How exciting..."
                    m "Is this all you have for me today, [hermione_name]?"
                    call her_main("Y-yes...","body_11")
                    her "But [genie_name], I know for a fact that professor Flitwick is \"dirty\"!"
                    her "Everyone knows that because of his height..."
                    call her_main("He sometimes... ehm...","body_13")
                    call her_main("He likes to look up girl's skirts, [genie_name]!","body_29")
                    m "Don't we all?"
                    call her_main("What?","body_31")
                    m "I said, don't we all hate it and must be outraged by the a man like Professor Flick-flick."
                    call her_main("Er... It's \"Professor Flitwick\", [genie_name].","body_07")
                    m "Right. Putting him on my \"Naughty boys list\" as we speak."
                    call her_main("......................","body_17")
                    m "Well, I hate to admit it but you did a lousy job of today's favour, [hermione_name]."
                    call her_main("................................","body_12")
                    menu:
                        "\"No points for you!\"":

                            call her_main("But [genie_name], I did my best!","body_28")
                            call her_main("You are going back on your promise [genie_name]!","body_67")
                            m "......................."
                            stop music fadeout 1.0
                            call her_main("How unbecoming of a school headmaster!","body_32")
                            m "You are dismissed, [hermione_name]."
                            call her_main("Tsk!","body_76")
                            $ mad += 18
                            call music_block
                            jump could_not_flirt_02
                        "\"Here are your point's though.\"":
                            call her_main("Really?","body_28")
                            call her_main("Thank you so much [genie_name]!","body_75")
                           
                elif one_out_of_three == 2: ### EVENT (B) Snape
                    call her_main("..................","body_13",xpos=140)
                    her "............................"
                    m "[hermione_name]?"
                    call her_main("Yes, [genie_name]... I'm sorry... I just...","body_11")
                    call her_main("............","body_13")
                    m "Did you do what I asked you to do?"
                    call her_main("I tried, [genie_name]. I really did...","body_14")
                    m "Who did you try to flirt with?"
                    call her_main(".........","body_13")
                    call her_main("Professor Snape, [genie_name].","body_12")
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    m "Severus? Interesting..."
                    m "How did it go?"
                    call her_main("It was awful [genie_name]...","body_07")
                    her "I am sorry, but I really hate professor Snape, [genie_name]!"
                    m "I'm sure the feeling is mutual..."
                    m "Tell me what happened."
                    call her_main("Nothing happened, [genie_name]. He just laughed at me...","body_09")
                    call her_main("I may not have much feminine charm, but I tried to be nice...","body_29")
                    call her_main("And he just started laughing in my face!","body_30")
                    call her_main("...it is really scary to see professor Snape laugh...","body_34")
                    her "........"
                    her "I am awful at flirting, I am sorry [genie_name]..."
                    call her_main("But I know that professor Snape is \"dirty\"!","body_47")
                    her "If you were to send someone else to him the outcome would be different, I know it!"
                    m "Someone else?"
                    call her_main("Yes! Someone with more experience at this...","body_44")
                    her "Someone..."
                    her "Someone, uhm..."
                    m "Sluttier?"
                    call her_main("Yes, I suppose...","body_66")
                    m "Don't you give up, [hermione_name]. We will make a slut err--"
                    m "I mean a woman out of you yet!"
                    call her_main("...................","body_79")
                    menu:
                        "\"...But you get no points this time\"":
                            call her_main("But I did my best...","body_12")
                            call her_main("And I feel so humiliated now...","body_34")
                            call her_main("But I understand and won't argue with your decision...","body_33")
                            call music_block
                            jump could_not_flirt_02
                        "\"Here are your points, [hermione_name].\"":
                            pass
                
                elif one_out_of_three == 3: ### EVENT (C) Filch
                    stop music fadeout 1.0
                    call her_main("I tried to flirt with mr.Filch, [genie_name]...","body_10",xpos=140)
                    m "I see. {size=-5}(No idea who that is.){/size}"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Yes, I know that technically mr.Filch is not a teacher...","body_11")
                    m "Huh?"
                    call her_main("But he is part of the school's staff...","body_01")
                    her "And we did hit it off quite well too!"
                    her "He was surprisingly sweet."
                    her "But I don't think he is \"dirty\", [genie_name]."
                    m "Gotcha... Mr.Fil{size=+7}TH{/size} is off the list then."
                    call her_main("It's \"Mr.Filch\", [genie_name]...","body_07")
                    m "What did I say?"
            
            elif whoring >= 6 and whoring <= 8: ### LEVEL 03 <======================================================================================= EVENT LEVEL 02
                if one_out_of_three == 1: ### EVENT (A) Slughorn
                    stop music fadeout 1.0
                    call her_main("Well, professor Slughorn invited me over to one of his...","body_10",xpos=140)
                    her "Rather disturbing tea-parties..."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("There were plenty of girls...","body_16")
                    her "But all of them were much younger then me..."
                    call her_main("Almost every guest was a freshman...","body_17")
                    call her_main("We had tea and some cake...","body_16")
                    her "Everything was pretty harmless..."
                    m "Did you flirt with the man or not?"
                    her "I did..."
                    call her_main("Or at least I tried...","body_17")
                    her "Professor Slughorn seems to be more interested in much younger girls..."
                    m "You almost sound jealous, [hermione_name]."
                    call her_main("What?!","body_18")
                    call her_main("That is preposterous!","body_69")
                    m "Here are your points..."
                    her "...................."
                
                elif one_out_of_three == 2: ### EVENT (B) Lockhart
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("I had an amazing day, [genie_name]!","body_80",xpos=140)
                    m "Do tell, [hermione_name]..."
                    call her_main("I had a class with professor Lockhart today...","body_68")
                    her "[genie_name] Lockhart is so charming and smart and..."
                    call her_main("And perfect...","body_78")
                    m "Please spare me your schoolgirl crush, [hermione_name]."
                    call her_main("[genie_name] Lockhart was even kind enough to give me his autograph...","body_80")
                    m "How kind of him indeed."
                    call her_main("Yes, I can't wait to show it to the girls!","body_68")
                    m "Hm... Can I see it?"
                    call her_main("[genie_name]?","body_45")
                    m "The Autograph, [hermione_name]. Can I see it?"
                    call her_main("Well... Em... It's in a rather private area, [genie_name].","body_44")
                    m "What? Well, then professor Goldenheart surely is \"dirty\"!"
                    call her_main("It's professor Lockhart, [genie_name]...","body_69")
                    her "And... Ehm..."
                    her "Well, it's not {size=+5}that{/size} private..."
                    m "Show it to me then!"
                    call her_main("No, [genie_name]! That would be inappropriate!","body_66")
                    menu: 
                        "{size=-3}\"Lockhart will be out of this school in no time!\"{/size}":
                            call her_main("Because of me?","body_72")
                            call her_main("[genie_name], please!","body_67")
                            m "Show me!"
                            call her_main("No, it's embarrassing!","body_32")
                            menu:
                                "\"Fine. Here are your points.\"":
                                    call her_main("Thank you for understanding, [genie_name].","body_74")
                                "\"Show me or I won't pay you!\"":
                                    call her_main("What?!","body_72")
                                    call her_main("...............","body_73")
                                    call her_main("..................","body_29")
                                    call her_main("Well, alright, but only to clear my idol's name...","body_47")
                                    hide screen hermione_main
                                    with d3
                                    show screen blktone8
                                    with d5
                                    call her_head("Here....","head_exp/12")
                                    m "Hm..."
                                    hide screen blktone8 
                                    with d5
                                    call set_hermione_action("lift_skirt")
                                    #$ only_upper = True #Skirt lifted.
                                    #$ autograph = True #Autograph shown.
                                    call her_main("","body_51",xpos=140)
                                    show screen ctc
                                    with d3
                                    pause
                                    call her_main("As you can see Professor Lockhart is nothing but an embodiment of everything pure and courageous!","body_50")
                                    pause
                                    m "Do I? From this?"
                                    her "You should not worry about professor Lockhart, [genie_name]."
                                    her "He is not \"dirty\"."
                                    m "Ah, what do I care..."
                                    call her_main("............?","body_51")
                                    hide screen hermione_main 
                                    with d3
                                    call reset_hermione_main
                                    #$ only_upper = False #Skirt lifted.#no legs bug
                                    #$ autograph = False #Autograph shown.
                                    call her_main("","body_47")
                                    pause
                                    hide screen ctc
                                    $ mad += 18
                        "\"FIne... Here are your points.\"":
                            call her_main("Thank you for understanding, [genie_name].","body_74")
                            
                elif one_out_of_three == 3: ### EVENT (C) Filch
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Well, I spent quite some time by flirting with mr.Filch today.","body_15",xpos=370)
                    call her_main("What a well read and exceptionally well mannered gentleman mr.Filch is.","body_16")
                    m "........"
                    call her_main("But I don't think anyone knows him like that...","body_13")
                    her "I don't think anyone knows mr.Filch like I do."
                    call her_main("I feel like he really opened up to me, [genie_name].","body_06")
                    m "Right..."
                    m "This, mr.Fli{size=+7}nt{/size}--"
                    call her_main("It's mr.Filch, [genie_name].","body_04")
                    m "Yeah, whatever... Is he a teacher here then?"
                    her "Mr.Filch? A teacher? No, [genie_name]..."
                    call her_main("He is the caretaker...","body_06")
                    m "A caretaker...?"
                    m "You mean he is a janitor?"
                    call her_main("Well...","body_10")
                    m "[hermione_name], I did not send you out there to charm school janitors!"
                    call her_main("But mr.Filch is part of the school staff, [genie_name]!","body_14")
                    menu:
                        "\"Just take your points and go!\"":
                            call her_main(".........................","body_03")
                        "\"Favour failed! No points for you!\"":
                            $ mad +=15
                            call her_main("But [genie_name]?","body_07")
                            m "You are dismissed, [hermione_name]."
                            call her_main(".........................................","body_05")
                            jump could_not_flirt_02
            
            elif whoring >= 9: ### LEVEL 04 <============================================================================ EVENT LEVEL04
                if one_out_of_three == 1: ### EVENT (A) Filch
                    stop music fadeout 1.0
                    call her_main(".............................","body_33",xpos=370)
                    her "....................................."
                    m "[hermione_name]?"
                    call her_main("[genie_name], I.....","body_34")
                    m "What is it? What happened?"
                    call her_main("Well...","body_29")
                    her "It's mr.Filch, [genie_name]..."
                    m "The janitor?"
                    call her_main("I flirted with him a little...","body_31")
                    her "And it went great at first..."
                    call her_main(".......................","body_29")
                    m "................?"
                    call her_main("And then...","body_31")
                    call her_main("Not sure if I should...","body_29")
                    m "[hermione_name], if you are not going to speak up, you may as well leave."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("He showed me his \"thing\", [genie_name]!","body_32")
                    m "His what?"
                    call her_main("His... manhood, [genie_name].","body_34")
                    g9 "Way to go, Janitor-guy!"
                    call her_main("What?!","body_72")
                    m "*Khem* I mean, this is unspeakable!"
                    call her_main("Yes... Vile crooked thing all covered in veins...","body_21")
                    m "Spare me the grisly details, [hermione_name]."
                    call her_main("Why would he do such a thing?","body_20")
                    her "One second we were just talking and then..."
                    m "Well, your noble  sacrifice shall not go unnoticed, [hermione_name]!"
                    m "Fifteen points to \"Gryf--"
                    call her_main("Professor, please wait.","body_19")
                    m "Huh?"
                    call her_main("Well, aren't you going to do something about this?","body_31")
                    m "Well..."
                    call her_main("What if I am not the first victim..?","body_47")
                    her "Some unfortunate freshman could be traumatized for life!"
                    m "And who wouldn't be really?"
                    call her_main("Does this mean you will take action, [genie_name]?","body_31")
                    m "uhm... Yeah, sure..."
                    m "There! Putting it on my \"to-do-list\"..."
                    m "\"Take care of the creepy janitor-guy and his crooked cock.\"..."
                    m "Yes, first thing tomorrow."
                    call her_main("Thank you [genie_name].","body_16")
                    call her_main("Can I have my points now?","body_75")
    
                elif one_out_of_three == 2: ### EVENT (B) Snape
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Professor Snape!","body_76",xpos=370)
                    m "Ehm... Yeah, I'm pretty sure it's Dumbledore or something..."
                    hide screen hermione_main
                    with d3
                    
                    g4 "{size=-5}(Wait, did {size=+7}he{/size} just put me under another disguise?){/size}"
                    g4 "{size=-5}(So do I look like that Professor Snape guy now?){/size}"
                    g4 "{size=-5}(By the great desert sands! Akabur, you need to learn restrain yourself!){/size}"
                    a5 "{size=-5}(Would you hear the girl out first! Geez...){/size}"
                    call her_main("[genie_name]? Who are you talking to?","body_02")
                    m "Em... I'm communicating with a spirit from another dimension..."
                    call her_main(".....??!","body_17")
                    hide screen hermione_main
                    with d3
                    a6 "{size=-5}(Stick to the script, you bastard!){/size}"
                    g4 "Yes, a particularly annoying spirit... Annoying and dumb!"
                    a6 "{size=-5}(You......!){/size}"
                    call her_main("[genie_name], please, you need to listen to me!","body_02")
                    m "Yes, yes, [hermione_name], I'm listening."
                    call her_main("I just confirmed that professor Snape is corrupted and \"dirty\", [genie_name]!","body_04")
                    m "Tell me what happened."
                    
                    hide screen blktone
                    with d3
                    show screen snape_groping
                    with d5
                    
                    call her_main("Well, during the classes today...","body_02")
                    her "I have been doing my best to attract professor Snape's attention..."
                    her "I have been giving him \"dreamy looks\"..."
                    her "And I've been eyeing his crotch..."
                    m "You..."
                    m "Eyed his crotch?"
                    call her_main("Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly...","body_04")
                    m "Where do you get this stuff?"
                    call her_main("Women's magazines...","body_10")
                    call her_main("Well, anyway, it worked, [genie_name].","body_07")
                    call her_main("As soon as the class was over, professor Snape grabbed my buttocks, [genie_name]!","body_47")
                    m "The fiend!"
                    m "Did you enjoy it, though?"
                    call her_main("[genie_name], I am only doing this--","body_30")
                    
                    hide screen snape_groping
                    with d5
                    show screen blktone
                    with d3
                    
                    m "Go \"Gryffindors\"! honour and all that. Yes, I remember."
                    m "Here are your points."
                    call her_main("","body_66")
  
                elif one_out_of_three == 3: ### EVENT (C) Lockhart
                    stop music fadeout 1.0
                    call her_main("Professor Lockhart!","body_09",xpos=370)
                    m "Got it! Adding him to the \"Naughty list\"!"
                    call her_main("No, [genie_name], it's not that...","body_11")
                    call her_main("Or...","body_12")
                    her "I'm not sure..."
                    call her_main("I used to adore him...","body_11")
                    call her_main("But he...","body_13")
                    her "He just..."
                    call her_main("How is this possible?","body_20")
                    her "I can't believe this..."
                    hide screen hermione_main
                    with d3
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "{size=-4}(Agh! The suspense is killing me!){/size}" 
                    m "{size=-4}(Did he force her to blow him?){/size}"
                    m "{size=-4}(Did he rape her?){/size}"
                    g4 "What was it, [hermione_name]? Speak up!"
                    call her_main("Huh?","body_14")
                    m "What did Professor Lockhart do to you?"
                    call her_main("Ehm... Nothing, [genie_name]...","body_13")
                    m "Nothing?!"
                    call her_main("Yes, I sort of cornered mr.Lockhart today...","body_11")
                    call her_main("And I also may have sort of made a pass at him...","body_31")
                    m "Seriously?"
                    call her_main("Yes... Not sure what had gotten into me, [genie_name]...","body_34")
                    m "Way to go, [hermione_name]!"
                    call her_main("Hear me out first [genie_name], please!","body_32")
                    m "My apologies. Please continue."
                    call her_main("Well, I always knew that mr.Lockhart was a true gentleman and...","body_14")
                    her "And... and I just wanted to clear his name from any suspicions once and for all..."
                    call her_main("...............","body_29")
                    her "Well mr.Lockhart did not reject me..."
                    m "You are killing me [hermione_name]!"
                    m "He didn't reject you, he didn't rape you..."
                    m "What the hell happened then?"
                    call her_main(".............","body_33")
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("I made him cry, [genie_name]...","body_34")
                    m "..............wait.......what?"
                    call her_main("He gave me a bewildered look and then started to sob...","body_28")
                    her "He looked like he was genuinely afraid of me, [genie_name]."
                    call her_main("I think...","body_29")
                    her "I think mr.Lockhart might be afraid of women..."
                    m "Afraid of women?"
                    m "What is that supposed to mean?"
                    call her_main("That he is into boys, [genie_name]?","body_34")
                    m "Oh..."
                    call her_main("............","body_44")
                    m "..........."
                    m "Well, I bet it was a traumatizing experience for you, [hermione_name]."
                    call her_main("It was, [genie_name]...","body_31")
                    m "Well, I hope these points will make you feel better."
    
    $ gryffindor +=15
    m "The \"Gryffindors\" gets 15 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_FlirtTeacher_OBJ.points += 1
    $ hg_pr_FlirtTeacher_OBJ.complete = True
    $ hg_pr_FlirtTeacher_OBJ.inProgress = False
    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1
    
    call hg_pr_transition_block
    return
    
    
##(Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label hg_pr_ClassmateTouchYou:
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to go get touched by one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_pr_ClassmateTouchYou_OBJ.points == 0: # <================================================================================ FIRST TIME
        m "[hermione_name]?"
        call her_main("[genie_name]?","body_01",xpos=140)
        m "You do like boys your age, don't you?"
        call her_main("...?","body_03")
        m "one of your classmates maybe?"
        call her_main("Well...","body_10")
        her "Must I really discuss things like this with you, [genie_name]?"
        call her_main("It's a bit embarrassing...","body_29")
        m "Sure, I understand. I don't need to know the details..."
        m "But here is what I need you to do today, [hermione_name]."
        m "Go confront that boy you fancy. The one you think is \"just so dreamy\"..."
        call her_main(".......?","body_31")
        m "And let him touch you..."
        if whoring <=5 or hg_pr_FlirtTeacher_OBJ.points <= 1: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much
        call her_main("Let him... touch me, [genie_name]?","body_31")
        m "Yes, touch you. The way boys touch girls?"
        m "How old are you, [hermione_name]? You look mature enough..."
        m "Haven't you had \"the talk\" with your parents already?"
        call her_main("\"The talk\", [genie_name]?","body_34")
        m "Yes, \"the talk\"! About how boys are different than the girls...?"
        m "Boys have a \"pee-pee\" and girls like to put that  \"pee-pee\" in their mouths?"
        call her_main("!!!","body_03")
        call her_main("What kind of demented parent would have such a talk with their child?","body_47")
        m "I bet Akabur would."
        call her_main("I beg your parodon, [genie_name]?","body_17")
        m "*Khem!* I said, a responsible and caring one!"
        m "Well, in any case. That is your task for today, [hermione_name]."
        m "Find a way to persuade one of your classmates to fondle you a little..."
        call her_main("..........","body_69")
        m "You are a pretty girl, it shouldn't be too hard."
        her "....................."
        call her_main("How many points would I receive after completing such a task, [genie_name]?","body_66")
        m "Hm... Twenty five should do..."
        call her_main("Twenty five house points...","body_69")
        her "...."
        call her_main("Well, so be it then...","body_66")
        m "Great..."
        call her_main("I'd better go now. The classes are about to start...","body_05")
        hide screen hermione_main
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 
            m "[hermione_name]?"
            call her_main("[genie_name]?","body_01",xpos=140)
            m "How about you go let one of your classmates molest you a little again?"
            call her_main("........","body_120")
            m "Twenty five house points, [hermione_name]."
            call her_main("[genie_name], it's just...","body_69")
            call her_main("I do not understand why I must do things like that...","body_79")
            m "To help out your house?"
            call her_main("That's not what I meant...","body_66")
            call her_main("Oh, never mind...","body_69")
            her "The classes are about to start, I'd better go..."
            m "Will you do it?"
            call her_main("I don't know... Maybe...","body_66")
            hide screen hermione_main
        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "[hermione_name], I need you to go out there, and make one of your classmates molest you a little."
            call her_main("I understand, [genie_name]...","body_01",xpos=140)
            m "Off you go then."
            her "..........."
            hide screen hermione_main
        elif whoring >= 12: # LEVEL 05+
            m "[hermione_name], I need you to go out there..."
            m "Find a handsome guy and force yourself on him!"
            call her_main("You mean like...","body_01",xpos=140)
            call her_main("In a sexual way, [genie_name]?","body_122")
            m "What? No, I mean just let him get under your uniform that's all..."
            call her_main("Oh, I see...","body_24")
            call her_main("I wonder who it should be this time...","body_68")
            call her_main("More than one boy, is not a problem, is it, [genie_name]?","body_117")
            m "A problem? Of course not!"
            m "If anything - it is encouraged." 
            call her_main("Great. I will see you after the classes then, [genie_name]. As usual.","body_122")
            m "Yes. Good luck."
            hide screen hermione_main
    
    $ hg_pr_ClassmateTouchYou_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_ClassmateTouchYou_complete:
    call hg_pr_EnterRoom_block
    call her_main("Good evening, [genie_name].","body_01",xpos=370,ypos=0)
    m "[hermione_name]..."
    m "Did you complete your task?"
    her "I did as you asked [genie_name]..."
    menu:
        "\"Great. Here are your points.\"":
            pass
        "\"Give me the details.\"":
            hide screen hermione_main
            with d3
            m "Give me the details."
            show screen blktone
            with d3
            
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # EVENT LEVEL 01.
                stop music fadeout 3.0
                call her_main("......","body_12")
                call her_main("Well... Em...","body_13")
                m "Speak up, [hermione_name]."
                m "Did you let some lucky guy feel you up or what?"
                    
                if one_out_of_three == 1: ### EVENT (A)
                    her "I did, [genie_name]..."
                    m "So? Tell me more."
                    her "Well, there is not much to tell..."
                    call her_main("I told that one guy I know that he could touch me a little if he wants...","body_31")
                    call her_main("He thought I was joking at first...","body_29")
                    call her_main("So embarrassing...","body_33")
                    m "So, did he cop a feel or not?"
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    call her_main("He did...","body_33")
                    m "Well, where did he touch you, [hermione_name]?"
                    call her_main("Ehm... My legs...","body_29")
                    her "And my breasts a little I suppose..."
                    m "That's all?"
                    call her_main("Yes, [genie_name]...","body_31")
                    call her_main("It's getting late... I think I'd better leave now...","body_33")
                    call her_main("I'm sorry, [genie_name]...","body_34")
                    m "Nothing to be sorry about, [hermione_name]."
                    m "You did good. This will do for now."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 3.0
                    call her_main("I did, [genie_name].","body_69")
                    her "But it was all very awkward and embarrassing..."
                    m "That's the whole point of it, [hermione_name]."
                    m "Tell me where you were touched today..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Ehm..."
                    call her_main("Well he touched me under my skirt a little...","body_117")
                    her "Then I let him rub my..."
                    call her_main("...my pussy through the panties, [genie_name].","body_118")
                    m "Very good. Then what happened?"
                    call her_main("Then he sort of started to touch himself [genie_name]...","body_131")
                    her "So, I decided to leave..."
                    m "I see..."
                    call her_main(".............","body_33")
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    her "I did, [genie_name]..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    call her_main("I led this one guy from \"Hufflepuff\" to an empty classroom and I told him that he can touch me if he wants.","body_31")
                    her "That I don't mind..."
                    call her_main("...........","body_29")
                    m "And?"
                    call her_main("Well, he did touch me a little at first...","body_31")
                    call her_main("......","body_33")
                    m "Don't make me pull every word out of you, [hermione_name]!"
                    m "Then what happened?"
                    call her_main("Well...","body_87")
                    stop music fadeout 1.0
                    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
                    call her_main("He asked me to call him a \"sissy boy\"...","body_44")
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    call her_main("And he kept on reassuring me that he has a very small penis...","body_31")
                    call her_main("He just kept repeating that *sob!*...","body_22")
                    call her_main("Why would anyone be like this?","body_21")
                    her "*Sob!* I Could not stay in his company a moment longer, so I just ran."
                    m "I'm sorry to hear this..."
                    call her_main("It was truly awful, [genie_name]...","body_21")
                    m "There, there..."
                    call her_main("*Sob!*","body_23")
                    m "Will ten extra points make you feel better?"
                    call her_main("Huh? That would be very sweet of you [genie_name].","body_19")
                    m "Of course... Ten extra points to \"Gryffindor\"."
                    call her_main("Thank you [genie_name]...","body_140")
                    m "And the rest of your payment..."
            
            elif whoring >= 9 and whoring <= 11: # LEVEL 04
                if one_out_of_three == 1: ### EVENT (A)
                    call her_main("Well... There is not much to tell...","body_16")
                    her "I found this one boy from \"Ravenclaw\"..."
                    her "Led him to one of the empty classrooms in the eastern wing..."
                    her "He thought I wanted to make out with him..."
                    her "But I told him that I just want him to touch me..."
                    call her_main("...so he did.","body_33")
                    m "I see..."
                    m "Well done, [hermione_name]."
                    call her_main("Will I be getting my points now?","body_44")
                    m "In a minute, [hermione_name]. I have a question I would like to ask you before that."
                    call her_main("???","body_31")
                    m "Did you enjoy it?"
                    m "Did it feel good to be touched by that boy?"
                    call her_main("Oh...","body_127")
                    her "Well, he was rather handsome I suppose..."
                    call her_main("I didn't hate it, if that's what you mean, [genie_name]...","body_120")
                    m "I see..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    call her_main("Well...","body_16")
                    her "I'm not sure whether or not this counts, but..."
                    her "During the herbology class today..."
                    call her_main("I let this one boy slide his hand under my skirt...","body_44")
                    her "So while Professor Sprout explained the differences between \"mandrake\" and \"mandragore\"..."
                    call her_main("Something I already knew of course...","body_08")
                    call her_main("I let my lab partner massage my buttocks...","body_44")
                    her "And that is all..."
                    m "Hm..."
                    menu:
                        "\"You can do better than that, [hermione_name].\"":
                            call her_main("Yes, I know, [genie_name]. I am sorry.","body_31")
                            m "Just make sure you try harder next time."
                            her "I will, [genie_name]."
                        "\"Kudos on doing this during class.\"":
                            call her_main("Thank you, [genie_name].","body_74")
                            m "I say you deserve to get paid."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    call her_main(".................","body_69")
                    m "???"
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    call her_main("I don't want to talk about it, [genie_name]...","body_69")
                    m "What happened, [hermione_name]. Spit it out."
                    call her_main(".................","body_79")
                    call her_main("But... it's so embarrassing...","body_31")
                    call her_main("Do I really have to, [genie_name]?","body_33")
                    m "Yes, I happen to love embarrassing things!"
                    call her_main(".................","body_69")
                    her "Well, alright..."
                    her "I approached this one guy that I always found attractive..."
                    her "Managed to muster up enough courage to ask him to follow me..."
                    call her_main("Normally I wouldn't dare...","body_31")
                    her "But the fact that I was doing this as a task entrusted to me by someone else..."
                    her "made it easier somehow..."
                    m "Happy to help, [hermione_name]."
                    call her_main("I led him to the library...","body_87")
                    her "We found a secluded spot behind one of the book shelves..."
                    her "And I told him that he can touch me wherever he wants..."                 
                    her "And...."
                    call her_main("..........","body_88")
                    m "What?"
                    call her_main(".....................","body_33")
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    call her_main("He started to touch my... feet, [genie_name].","body_32")
                    m "Huh?"
                    m "Your \"Feet\"? Is that what kids call tits these days?"
                    call her_main("I'd wish, [genie_name]...","body_66")
                    her "He asked me to take off my shoes..."
                    her "Then he..."
                    call her_main("He started to smell my toes, [genie_name]!","body_21")
                    call her_main("I felt so... violated!","body_22")
                    m "So he didn't touch your tits, or your butt?"
                    call her_main("No, [genie_name]... *sob!*","body_143")
                    m "Alright, then what happened?"
                    call her_main("Nothing! I couldn't bear the humiliation... I just ran...","body_142")
                    her "I even left my shoes behind and had to come back later to pick them up..."
                    call her_main("*Sob!*............","body_145")
                    m "Hm..."
                    m "Well, you did get molested..."
                    m "Although in a rather unconventional manner..."
                    call her_main("*Sob!* I wish he would have just touched my breasts like a descent boy would, [genie_name]... *Sob!*","body_145")
                    m "There, there..."
                    m "You earned you pay today..."
            
            elif whoring >= 12: # LEVEL 05+
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    call her_main("......","body_29")
                    call her_main("Well...","body_31")
                    her "During the potions class today..."
                    her "I wrote a note on a piece of paper..."
                    her "I was about to slide it to my lab partner when..."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Professor Snape snatched it right out of my hand...","body_69")
                    call her_main("He then read it out loud before the entire class...","body_79")
                    m "What did the note say?"
                    call her_main("Well...","body_87")
                    her "It said: \"You can touch my butt if you want. I bet professor Snape would never notice.\""
                    call her_main("Everyone was laughing...","body_118")
                    her "It was so embarrassing I wanted to die..."
                    call her_main("I really hate professor Snape, [genie_name]...","body_47")
                    m "What happened then?"
                    call her_main("Nothing...","body_87")
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    $ sc34CG(2, 19, 6, 5)
                    her "But when the class was over..."
                    her "These two nasty-looking boys from \"Slytherin\" cornered me..."
                    her "Actually they weren't mean to me or anything..."
                    her "So we just waited for everyone to leave the classroom..."
                    $ sc34CG(2, 16, 6, 9)
                    call her_main("And then I let them touch me...","body_117")
                    $ sc34CG(2, 17, 6, 9)
                    her "They touched me everywhere, [genie_name]..."
                    m "\"Everywhere\", huh?"
                    her "Yes... Everywhere, [genie_name]..."
                    call her_main("There were hands under my skirt, under my shirt...","body_128")
                    $ sc34CG(2, 16, 6, 9)
                    her "And then I started to breathe heavily..."
                    call her_main("So one of them just put his hand over my mouth...","body_121")
                    her "And their hands were so... thorough..." 
                    $ sc34CG(2, 17, 6, 9)
                    her "My head started to spin..."
                    $ sc34CG(2, 16, 6, 9)
                    call her_main("It was most exhilarating, [genie_name].","body_128")
                    m "Very good, [hermione_name]. Very good indeed."
                    hide screen sccg
                    with d3
                
                if one_out_of_three == 2: ### EVENT (B)
                    call her_main("Actually something quite unexpected happened to me today, [genie_name]...","body_01")
                    her "Right after the Defence Against the Dark Arts class..."
                    her "This stocky \"Hufflepuff \" boy came up to me..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    call her_main("He said someone told him that I let boys touch me...","body_122")
                    call her_main("Normally I would deny everything...","body_128")
                    her "But I decided not to waste the opportunity..."
                    call her_main("I took the boy to a quiet spot and let him touch me...","body_78")
                    her "I let him run his hands up and down my thighs..."
                    her "I let him fondle my breasts..."
                    call her_main("All the usual things...","body_128")
                    m "Well done, [hermione_name]."
                    
                if one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    call her_main("Well...","body_44")
                    her "I did what you told me to do, [genie_name]..."
                    her "But... it sort of... ehm..."
                    call her_main("Well, it sort of escalated into something else...","body_78")
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Hm?"
                    call her_main("uhm...","body_44")
                    her "I sort of... got caught while I was letting this one boy fondle my breasts..."
                    m "You got caught? By one of the teachers?"
                    call her_main("No, [genie_name]...","body_45")
                    call her_main("By the boy's girlfriend...","body_46")
                    m "Interesting..."
                    call her_main("She was furious with him at first...","body_117")
                    call her_main("But then...","body_122")
                    call her_main("Ehm... She started to touch my breasts as well...","body_124")
                    call her_main("Almost the same way her boyfriend did just a moment ago...","body_111")
                    her "Then she turned to him and she said..."
                    call her_main("\"I love you baby, and I want to share everything with you...\"","body_16")
                    her "\"...And that includes your whores.\""
                    call her_main("I did not appreciate being called a whore of course...","body_117")
                    call her_main("But that was such a sweet and romantic gesture...","body_06")
                    her "Wouldn't you agree, [genie_name]?"
                    m "Totally..."
                    m "Seems that true love {size=+5}does{/size} exist after all."
                    m "Then what happened?"
                    call her_main("Ehm... Well, they kissed of course...","body_24")
                    call her_main("And then they both started to touch me again...","body_44")
                    call her_main("And then he was kind of only touching her and she was only touching him...","body_29")
                    her "And they kissed..."
                    her "I suddenly felt like the third wheel in that situation, so I just slipped away quietly..."
                    m "I see..."
    
    $ gryffindor +=25
    m "The \"Gryffindor\" house gets 25 points!"
    her "Thank you, [genie_name]."
    
    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    $ hg_pr_ClassmateTouchYou_OBJ.points += 1
    $ hg_pr_ClassmateTouchYou_OBJ.complete = True
    $ hg_pr_ClassmateTouchYou_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return
    
    
##(Level 04) (35 pt.) (Flash your tits to a boy). (Available during daytime only).
label hg_pr_FlashClassmate: #LV.4 (Whoring = 9 - 11)
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to flash her tits to one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_pr_FlashClassmate_OBJ.points == 0: # <================================================================================ FIRST TIME
        m "[hermione_name]..."
        m "I would like to award \"Gryffindor\" with 25 house points today."
        call her_main("Really?","body_01",xpos=140)
        her "Thank you, [genie_name]!"
        m "Yes, but first I will require your help with something..."
        her "Of course, [genie_name]! Anything!"
        m "I need you to go out there and show off your tits to people..."
        stop music fadeout 1.0
        call her_main("...?","body_02")
        m "You know, flash your breasts to some boys..."
        call her_main("?!!","body_48")
        if whoring <=8 or hg_pr_ClassmateTouchYou_OBJ.points <= 1:
            jump too_much
        her "[genie_name]!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("This is a completely new level of inappropriate, even for you, [genie_name]!","body_47")
        her "How can you ask one of your pupils to perform such a task?"
        m "So that's how you feel then? I see..."
        m "I suppose I will be awarding those points to some other house instead ..."
        m "\"Slytherin\" perhaps?"
        call her_main("................","body_66")
        m "But, you know, no pressure..."
        call her_main("[genie_name]...","body_69")
        her "The fate of my house is very important to me, but..."
        m "Is it really?"
        m "Why don't you show it to me then?"
        m "Yes. Show me how important it is to you exactly, [hermione_name]."
        call her_main("But this is inappropriate...","body_47")
        m "Are we really in any position to discuss what is appropriate and what is not at this point?"
        call her_main("..................","body_69")
        m "I would say that ship has sailed a long time ago..."
        call her_main("..............","body_66")
        m "All I ask you to do is to give some lucky boy a quick peek..."
        call her_main("But why? Why must I do things like this, [genie_name]?","body_69")
        m "A minute of your time for 25 house points..."
        m "A pretty nifty deal, wouldn't you agree?"
        her "I suppose..."
        her "Well alright, I'll see what I can do..."
    
    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 9 and whoring <= 11: # LEVEL 04 FIRST EVENT.
            m "I think you need to show off your tits some more, [hermione_name]."
            call her_main("You mean to you, [genie_name]?","body_44",xpos=140)
            m "No, to your classmates..."
            call her_main("Oh...","body_117")
            m "Yes, go do that and then report back to me..."
            call her_main("Will I get paid for this?","body_69")
            m "Of course you will get paid for this, [hermione_name]. Don't be silly."
            m "Thirty five house points. The usual rate..."
            call her_main(".................","body_69")
            call her_main("Well alright... I will see what I can do, [genie_name]...","body_66")
        
        elif whoring >= 12 and whoring <= 14: # LEVEL 05
            m "[hermione_name]. I have a question for you."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "Why do you think women have breasts?"
            call her_main("...what do you mean, [genie_name]?","body_44",xpos=140)
            m "Alright, let me rephrase this..."
            m "What would you say is the most common application for the female mammary glands?"
            call her_main("Oh...","body_15")
            call her_main("Production of milk?","body_17")
            m "Good. What else do women use their tits for?"
            call her_main("Hm..","body_13")
            call her_main("...to attract men?","body_17")
            m "Yes. Let's concentrate on that."
            m "I need you to go out there..."
            m "Find some lucky bastard..."
            m "And flash him your tits..."
            call her_main("{size=-3}(I just knew that this was exactly where this conversation was heading...){/size}","body_66")
            m "What was that, [hermione_name]?"
            call her_main("I said I'd better go then, [genie_name].","body_69")
            her "my classes are about to start..."
            m "Thirty five house points will be waiting for you here upon your return, [hermione_name]."
            call her_main("..............","body_79")
        
        elif whoring >= 15: # LEVEL 06+
            m "[hermione_name] I need you to go out there and flash your tits to one of your classmates."
            call her_main("I will do my best [genie_name].","body_127",xpos=140)
            m "Really? Just like that? No complaints or anything?"
            call her_main("I am getting paid for this, am I not?","body_128")
            m "Of course."
            call her_main("Why would I complain about a simple task like this then?","body_127")
            her "Thirty five house points is a fair prices for a few seconds of excitement... err..."
            call her_main("...I mean, embarrassment.","body_74")
            m "{size=-3}(She changed this much already?){/size}"
            g9 "{size=-3}(I'm so good at this training thing that it's starting to get creepy!){/size}"
            call her_main("Classes are about to start... I'd better leave now.","body_45")
            her "I will see you later tonight, [genie_name]."
    
    $ hg_pr_FlashClassmate_OBJ.inProgress = True

    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_FlashClassmate_complete:
    call hg_pr_EnterRoom_block
    
    if whoring >= 9 and whoring <= 11: # LEVEL 04 <=============================================================EVENT LEVEL 01                    
        if one_out_of_three == 1: ### EVENT (A)
                call her_main("Good evening, [genie_name]...","body_31",xpos=370)
                m "[hermione_name]..."
                m "So, how did it go?"
                call her_main("Ehm... Not too well, actually...","body_34")
                her "................................"
                m "Just tell me what happened, [hermione_name]."
                call her_main("That is the thing, [genie_name]...","body_31")
                her "Nothing happened..."
                call her_main("I just couldn't bring myself to do it...","body_87")
                m "I see..."
                m "Well, I can't just give you the points for nothing, [hermione_name]."
                call her_main("Of course, [genie_name]... I understand...","body_16")
                call her_main("I shall try harder next time... I promise...","body_29")
                m "Then I will just put these thirty five points aside for now..."
                call her_main("Thank you, [genie_name]...","body_29")
                her "..."
                her "I'd better go now."
                $ hg_pr_FlashClassmate_OBJ.inProgress = False
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("Ehm... Sort of...","body_29",xpos=370)
            m "Sort of?"
            call her_main("Yes... uhm...","body_31")
            her "Well, I decided to try and flash them to this \"hufflepuff\" boy..."
            call her_main("I've been waiting for the right moment...","body_87")
            her "I was worried that something would go wrong..."
            call her_main("And, of course, everything that could - did...","body_69")
            call her_main("When I tried to expose myself to the boy...","body_31")
            her "At first I only pulled up my vest..."
            her "Then I tried to pull my shirt up as well..."
            her "And one of my breasts got entangled in the fabric and was pulled up along with the shirt..."
            call her_main("So only one of my breasts was naked and I was desperately trying to free the other one.","body_32")
            her "Other students started to pay attention to me..."
            her "So I had to fix my clothes back into place quickly..."
            her "And then the moment was gone..."
            call her_main("............","body_33")
            m "Hm..."
            m "What about the boy? Did he see your tits or not?"
            call her_main("Well, I think he may have seen one of them...","body_31")
            her "But from the way he was looking at me..."
            her "I doubt that he understood that the whole commotion was for his benefit."
            call her_main("......................","body_29")
            call her_main("I'm sorry, [genie_name]...","body_31")
            m "That's alright..."
            m "I wouldn't expect you to perform perfectly this early in your training..."
            call her_main("(My training?)","body_117")
        
        elif one_out_of_three == 3: ### EVENT (C)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            $ sc34CG(3, 5)
            call her_main("Yes I did, [genie_name].","body_29",xpos=370)
            m "Good. Tell me more."
            $ sc34CG(3, 4)
            call her_main("Ehm... There is not much to tell, really...","body_31")
            her "I spent the first half of the day with studying in the library..."
            her "It is usually quite deserted during that time..."
            her "Apart from me there was only one student..."
            $ sc34CG(3, 6)
            call her_main("Some boy from \"Ravenclaw\"...","body_120")
            her "So I waved to him and when he looked up at me..."
            $ sc34CG(3, 7)
            call her_main("I quickly pulled my shirt up...","body_117")
            m "Good job."
            m "How did he react to the sight of your naked tits?"
            $ sc34CG(3, 8)
            call her_main("I'm not sure...","body_118")
            $ sc34CG(3, 9)
            call her_main("He looked rather shocked I suppose...","body_117")
            $ sc34CG(3, 10)
            call her_main("After I showed him my breasts it got too embarrassing for me to stay there any longer...","body_118")
            $ sc34CG(3, 11)
            call her_main("So I just gathered all my books and left...","body_117")
            $ sc34CG(3, 6)
            m "I see..."
            hide screen sccg
            with d3
    
    elif whoring >= 12 and whoring <= 14: # LEVEL 05 <=============================================================EVENT LEVEL 02
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            show screen blktone
            with d3
            m "[hermione_name]. Did you complete your task?"
            call her_main("Yes I did, [genie_name].","body_44",xpos=370)
            call her_main(".............","body_118")
            m "Well? How did it go?"
            call her_main("................","body_118")
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("Just for the record, [genie_name]...","body_69")
            m "Hm?"
            call her_main("I think that forcing your pupils to do things like this...","body_30")
            call her_main("Is beneath an esteemed wizard such as yourself...","body_120")
            m "\"Forcing\"? Nobody is forcing you to do anything, [hermione_name]."
            m "You came to me, remember?"
            call her_main("..........","body_31")
            m "You begged me to buy a sexual favour from you."
            call her_main("...I....","body_29")
            call her_main("I never said \"sexual\"...","body_31")
            m "Nevertheless, you can stop selling me these favours at any moment, [hermione_name]."
            call her_main("I suppose...","body_69")
            m "And yet you keep on coming back..."
            call her_main("............................","body_118")
            m "I think you may actually be taking some twisted form of pleasure from this."
            call her_main("What?","body_47")
            m "Shame on you, [hermione_name]. Shame on you."
            call her_main("[genie_name], I never...!","body_47")
            m "Enough of this. Did you complete your task or not?"
            call her_main("Yes I did...","body_120")
            m "And?"
            call her_main("And that is all I am going to say...","body_87")
            call her_main("........","body_120")
            m ".........."
            her "........"
            m "Oh, whatever. Just take your points and go."
            call her_main("Thank you, [genie_name].","body_120")
        
        elif one_out_of_three == 2: ### EVENT (B)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name]..."
            call her_main("Good evening, [genie_name]...","body_33",xpos=370)
            m "Did you complete your task?"
            call her_main("Yes, I did, [genie_name]...","body_31")
            call her_main("..........","body_33")
            m "................"
            her "..............."
            m "Well?"
            call her_main("Can I get paid now please?","body_31")
            m "Not before you tell me what exactly you did today."
            call her_main("....................","body_33")
            call her_main("Do I really have to, [genie_name]?","body_31")
            m "When you are being coy like this..."
            m "It only makes me more curious. You know that, right?"
            call her_main("Aww...","body_117")
            call her_main("Well... Ehm...","body_118")
            her "Well, alright, here it goes..."
            call her_main("I flashed my tits to that \"Slytherin\" underclassman in a corridor...","body_32")
            her "But I was standing too close to him..."
            call her_main("....","body_33")
            her "...."
            call her_main("Well, he sort of grabbed one of my breasts, [genie_name]...","body_31")
            her "he squeezed it hard and just wouldn't let go..."
            call her_main("He made me promise to meet him after my classes...","body_117")
            her "And let him..."
            call her_main("\"Play with my tits\" some more...","body_131")
            call her_main("You see, that is why I hate \"slytherin\" boys, [genie_name]...","body_118")
            her "They don't have a shred of honour.."
            her "..."
            m "Did you keep your promise?"
            call her_main("No, not yet...","body_117")
            her "I'm planning to meet that awful boy after we are done here, [genie_name]."
            m "I see..."
            m "Well, I shouldn't keep you waiting then, should I?"
        
        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], did you complete your task?"
            show screen blktone 
            with d3
            call her_main("I did [genie_name]...","body_14",xpos=370)
            m "I'm listening..."
            call her_main("Well...","body_31")
            her "I had to spend a big portion of the day at the school library..."
            her "So I didn't really have the time to perform your task properly, [genie_name]..."
            m "Hm...?"
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Instead I just went to the library window and..."
            call her_main("...I just pulled my shirt up and pressed my bare breasts against the glass...","body_118")
            her "I stood there like that for several seconds..."
            her "To make sure that at least someone sees me from the outside..."
            call her_main("I hope this still counts, [genie_name]...","body_117")
            m "Hm..."
            m "How many students would you say saw you standing behind that window?"
            call her_main("I am not sure, [genie_name]... A couple maybe...?","body_118")
            m "\"Maybe\"?"
            call her_main("I don't know, [genie_name]...","body_182")
            her "To be honest I kept my eyes closed..."
            m "How do you know that anyone saw you at all then, [hermione_name]?"
            call her_main("I heard someone shout: \"Look! At that window over there!\".","body_141")
            her "When I heard that I covered up and quickly left..."
            call her_main("....","body_117")
            m "Hm..."
            m "Well, alright... I think this counts..."
    
    elif whoring >= 15: # LEVEL 06+ <=============================================================EVENT LEVEL 03
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("I did [genie_name]...","body_45",xpos=370)
            m "I'm listening..."
            $ sc34CG(3, 5)
            call her_main("Well... I had to spend a big portion of the day in the school library...","body_44")
            her "So I didn't really have the time to perform your task properly, [genie_name]..."
            m "Hm...?"
            $ sc34CG(3, 6)
            call her_main("Instead I just made sure there were no teachers around...","body_117")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            $ sc34CG(3, 7)
            her "Pulled my shirt up..."
            call her_main("And then I just sat there like that for a while...","body_31")
            $ sc34CG(3, 12)
            call her_main("trying to get some studying done...","body_87")
            her "I don't think there were many people around..."
            call her_main("Or at least I hope so...","body_118")
            $ sc34CG(3, 13)
            call her_main("But they definitely saw my breasts, [genie_name]...","body_117")
            $ sc34CG(3, 7)
            call her_main("eventually A few first years seemed to notice...","body_118")
            $ sc34CG(3, 10)
            call her_main("I had to leave pretty quickly after that...","body_117")
            m "Hm..."
            m "How many people would you say saw your tits today, [hermione_name]?"
            $ sc34CG(3, 9)
            call her_main("Hard to say, [genie_name]...","body_31")
            her "Two dozen boys or so I suppose..."
            $ sc34CG(3, 12)
            call her_main("A few girls as well...","body_29")
            $ sc34CG(3, 11)
            her "I think the school librarian may have seen me too..."
            m "Hm... Well, I'd say that's a job well done."
            hide screen sccg 
            with d3
        
        elif one_out_of_three == 2: ### EVENT (B)
            stop music fadeout 1.0
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name].","body_45",xpos=370)
            m "Well, tell me all about it, then."
            call her_main("Ehm... Alright...","body_31")
            her "I was flashing my tits to this boy in the \"Gryffindor\" common room..."
            call her_main("When my friend, Ginny walked in on us...","body_14")
            m "Another boy?"
            call her_main("A boy? No, Ginny is a girl's name, [genie_name].","body_13")
            m "....."
            call her_main("Ginny Weasley, [genie_name].","body_14")
            m "Alright, fine, continue..."
            call her_main("uhm...","body_13")
            her "......."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("*Giggle*","body_24")
            m "Hm...?"
            call her_main("Then Ginny grabbed my breasts...","body_46")
            her "And started to squeeze them..."
            her "then she started to kiss my breasts passionately..."
            m "............"
            call her_main("to kiss and suck on my nipples...","body_111")
            call her_main("And I couldn't help myself - I started to moan...","body_128")
            m ".............."
            call her_main("And then the boy took out his throbbing cock...","body_129")
            her "And sprayed his hot spunk all over me and Ginny!"
            call her_main("And then me and Ginny, we licked his hot sperm off of our young bodies...","body_111")
            m ".............."
            m "Are you making this up, [hermione_name]?"
            call her_main("...maybe.","body_24")
            call her_main("I just thought that you would like to hear something like that, [genie_name]...","body_128")
            m "What I would like to hear, [hermione_name], is the truth."
            call her_main("Even if it's incredibly dull, [genie_name]?","body_127")
            m "Dull or not..."
            m "I only want to know what actually happened..."
            m "Keep your fantasies to yourself, [hermione_name]."
            call her_main("As you wish, [genie_name].","body_70")
            her "My friend Ginny walked in on my flashing my tits to that guy."
            her "But She promised me that she won't tell anyone."
            call her_main("And that's all that happened, [genie_name]...","body_15")
            m "I see..."
            m "I still prefer this to some made up stories..."
        
        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("Yes I did, [genie_name]...","body_45",xpos=370)
            m "Alright, tell me how did it go."
            call her_main("Well, let's see...","body_29")
            her "First I flashed them to that one boy from \"Ravenclaw\"..."
            call her_main("Then to that upperclassman from \"Hufflepuff\"...","body_31")
            call her_main("Then there was this other boy from \"Ravenclaw\".","body_45")
            m "???"
            call her_main("After that I flashed my tits to some \"Gryffindor\" underclassman by mistake...","body_34")
            call her_main("No, wait...  the boy from \"Gryffindor\" was after that other boy...","body_29")
            m "How many boys did you flash your tits to today, [hermione_name]?"
            call her_main("Half a dozen or so?","body_117")
            call her_main("I had an opening in my schedule...","body_122")
            her "So I decided to go for some extra credit with your assignment, [genie_name]."
            m "This is not an assignment, [hermione_name]..."
            m "And there are no extra credits..."
            call her_main("Oh...?","body_31")
            m "You are still getting your usual payment, [hermione_name], and that's it."
            call her_main("Oh... I see...","body_29")
            m "But, [hermione_name]..."
            call her_main("Yes, [genie_name]?","body_31")
            g9 "That was very well done."
            call her_main("Thank you, [genie_name].","body_128")
    
    $ gryffindor +=35
    m "The \"Gryffindor\" house gets 35 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_FlashClassmate_OBJ.points += 1
    $ hg_pr_FlashClassmate_OBJ.complete = True
    $ hg_pr_FlashClassmate_OBJ.inProgress = False
    
    $ hermione_sleeping = True
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    
    call her_walk(400,610,2)
    show screen hermione_stand_f #Hermione stands still.
    pause.3
    
    if one_out_of_three == 2 and whoring >= 12 and whoring <= 14: #Event level 02.
        $ her_head_ypos = her_head_only
        call her_head("\"Slytherin\"...","body_120")
    if one_out_of_three == 3 and whoring >= 12 and whoring <= 14: #Event level 02.
        $ her_head_ypos = her_head_only
        call her_head("(I can't believe I did that today...)","body_120")
        call her_head("(What if Harry or Ron saw me like that?)","body_119")
        call her_head("(Standing there...)")
        call her_head("(Pressing my breasts against that window glass...)")
        call her_head("(I would probably just die of embarrassment right there on the spot...)","body_118")
        call her_head("(No. Protecting the honor of the \"Gryffindor\" house is my number one priority.)","body_120")
        call her_head("(We must get the cup this year, no matter the cost...)")
        call her_head("(........)","body_118")
    if whoring >= 15 and one_out_of_three == 1: # LEVEL 06+ <=============================================================EVENT LEVEL 03
        $ her_head_ypos = her_head_only
        call her_head(".........................","body_123")
    
    hide screen hermione_stand_f #Hermione stands still.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with d3
    call music_block
    
    return
    
    
##(Level 05) (45 pt.) (MAKE OUT WITH A GIRL). (Available during daytime only).
label hg_pr_KissAGirl: #LV.5 (Whoring = 12 - 14)
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to go make out with one of her female classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_pr_KissAGirl_OBJ.points == 0: # <================================================================================ FIRST TIME
        m "Have You ever kissed another girl, [hermione_name]?"
        call her_main("?!","body_07",xpos=140)
        if whoring <=11 or hg_pr_FlashClassmate_OBJ.points <= 1: # Counts how many times you sent Hermione to flash a classmate.
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("I am not a... lesbian, [genie_name].","body_02")
        m "Silly girl... You don't need to be a lesbian to kiss girls."
        m "I mean, I do it and I am not a lesbian either."
        call her_main("...............","body_05")
        her "[genie_name]--"
        m "No, \"[genie_name]s\"! This is your task for today!"
        m "Go find a cute little thing and plant a \"smooch\" on her!"
        call her_main("[genie_name], but I am--","body_11")
        m "Dismissed, [hermione_name]."
        call her_main("[genie_name]!......","body_07")
        m "I said you're dismissed."
        call her_main("*Humph!*...","body_09")
    
    else: # <================================================================================ NOT FIRST TIME
        m "A forty five house points worth of favour is up for grabs!"
        m "Are you interested, [hermione_name]?"
        if whoring >= 12 and whoring <= 14: # LEVEL 05 FIRST EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("It depends...","body_03",xpos=140)
            her "Will I have to do something depraved again?"
            m "\"Depraved\"??! When did I ever--?"
            call her_main("Really, [genie_name]?","body_04")
            m "Fine, fine... But all I want you to do today is to make out with another girl."
            call her_main("Oh, is that all?","body_05") # :(
            m "Yes... Pretty basic stuff for you, right?"
            m "And you will be getting forty five house points afterwards of course."
            call her_main(".............","body_07")
            m "So... Are you up for it?"
            call her_main("I will see what I can do, [genie_name]...","body_69")
            m "Great. See you after your classes then."
            call her_main("................","body_79")
        
        elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.
            call her_main("I suppose...","body_70",xpos=140)
            m "Great. All you need to do is make out with another girl."
            call her_main("I see...","body_71")
            m "Up for the task, [hermione_name]?"
            call her_main("I suppose...","body_29")
            m "Great. See you after your classes then."
        
        elif whoring >= 18: # LEVEL 07+ Event level 03.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("Sure, why not?","body_06",xpos=140)
            m "Great."
            m "I want you to make out with another girl today."
            call her_main("Alright.","body_45")
            call her_main("I know a couple of girls who are hungry for attention and wouldn't mind putting on a little show.","body_64")
            m "Great. See you after your classes then."
    
    $ hg_pr_KissAGirl_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_KissAGirl_complete:
    call hg_pr_EnterRoom_block
    
    if whoring >= 12 and whoring <= 14: # LEVEL 05                    
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            m "[hermione_name]..."
            m "Did you succeed in completing your task?"
            show screen blktone
            with d3
            call her_main("I...","body_11",xpos=370)
            m "I told you to make out with another girl..."
            m "Did you do it?"
            call her_main("I...","body_10")
            her "I tried, [genie_name]. I really did."
            m "And?"
            call her_main("Well...","body_29")
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            her "It was awkward and embarrassing..."
            m "did you do it or not?"
            call her_main("...no I did not, [genie_name]...","body_69")
            her "All I did was making a complete fool out of myself..."
            call her_main("In front of the entire class...","body_47")
            m "Tell me what happened, [hermione_name]."
            call her_main("No, I will not, [genie_name].","body_69")
            her "Not in a million years!"
            call her_main("Why do I have to perform such ridiculous tasks anyway?!","body_132")
            her "What is the point of all this?"
            call her_main("I hate this!","body_30")
            call her_main("...............","body_69")
            her "................."
            m ".............."
            m "You are not getting paid, you know that, right?"
            call her_main("I don't care...","body_30")
            $ mad +=25
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
        
        elif one_out_of_three == 2: ### EVENT (B)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("I did, [genie_name]...","body_16",xpos=370)
            m "Good. Give me the details."
            call her_main("Well, I kissed a girl. Just like you told me to, [genie_name].","body_17")
            m "I guess it was embarrassing for you, girl?"
            call her_main("Very much so, [genie_name].","body_69") # :( D: :D::D:D:D::D::D::D::DDD:DD
            m "Did you enjoy it though?"
            call her_main("*Humph!*...","body_79")
            m "So you kissed a girl and you liked it?"
            call her_main("Yes...","body_66")
            m "Did your tongues touch?"
            call her_main("Yes...","body_66")
            her "It was a proper deep kiss, if that's what you want to know."
            her "Can I just get my payment now?"
            call her_main("Please, [genie_name]...","body_69")
            m "Well, alright..."
        
        elif one_out_of_three == 3: ### EVENT (C)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes, I did, [genie_name].","body_16",xpos=370)
            m "Good. Tell me how it went."
            call her_main("It went well, [genie_name].","body_16")
            m "Great. Give me the details."
            call her_main("What would you like to know, [genie_name]?","body_04")
            m "Tell me everything! Was the girl pretty?"
            m "Did she return your kiss?"
            call her_main("She was relatively pretty, [genie_name].","body_08")
            her "And she did return my kiss..."
            call her_main("...........","body_184")
            call her_main("Anything else, [genie_name]?","body_08")
            m "...."
            m "Why are you being difficult, [hermione_name]?"
            call her_main("With all due respect, [genie_name]...","body_04")
            her "You told me to make out with another girl, and I did..."
            call her_main("Now, I would like to get paid if you would be so kind.","body_03")
            m "......................"
            menu:
                "\"I don't appreciate your attitude, [hermione_name].\"":
                    call her_main("Well, that is unfortunate, [genie_name].","body_04")
                    m "Sure is..."
                    m "Because you are not getting paid you insolent, little witch."
                    stop music fadeout 1.0
                    call her_main("What?","body_03")
                    call her_main("[genie_name], you can't do that!","body_11")
                    m "Dismissed."
                    call her_main("B-but--","body_10")
                    call her_main("[genie_name], please!","body_11")
                    her "The girl was from \"Hufflepuff\" and--"
                    m "Too late for that, [hermione_name]."
                    m "You are dismissed."
                    call her_main("......","body_21")
                    $ mad +=25
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                            
                "\"Fine. Here is your payment, girl.\"":
                    pass
    
    elif whoring >= 15 and whoring <= 17: # LEVEL 06. Event level 02.     
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("I did, [genie_name]...","body_16",xpos=370)
            m "Well, don't just stand there. Give me the details."
            call her_main("Ehm, alright...","body_14")
            her "The girl was from \"Ravenclaw\"..."
            call her_main("I think she may have been an underclassman, but I did not ask...","body_13")
            her "We got to talking about boys..."
            call her_main("And she told me that she never kissed one...","body_16")
            her "And that she is worried that she might be very bad at it..."
            call her_main("So I just offered my help...","body_06")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "And then we spent some time in one of the bathroom stalls..."
            call her_main("Making out...","body_45")
            call her_main("She caught on real quick... I think she could be really good at it with some practice...","body_31")
            call her_main("Also she was quite adorable...","body_45")
            call her_main("She kept calling me \"[hermione_name]\"...","body_46")
            m "Hm..."
            m "I Don't recall sending you out with a task to confuse little kids, [hermione_name]."
            call her_main("\"Little kids\"? [genie_name], please...","body_64")
            her "You should have seen that girl..."
            her "A little petite? Maybe... But definitely not a \"kid\"."
            call her_main("And I assure you that she was anything but confused.","body_111")
            her "In fact, at the end of our \"Study session\" she got rather obnoxious..."
            call her_main("And it sort of felt as if she was taking advantage of me...","body_31")
            m "Oh... Well, in that case..."
            call her_main("","body_45")
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name]. Did you complete your task?"
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("I did, [genie_name].","body_16",xpos=370)
            m "Tell me how it went."
            call her_main("Well... Ehm...","body_31")
            her "There is this one girl who is into girls..."
            her "I thought she would be the ideal candidate for my task..."
            her "so I told her that I am curious and that I would like to kiss her..."
            call her_main("She said that we should go to the girls' restroom for that...","body_87")
            her "But I just kissed her right there in the corridor..."
            call her_main("And she kissed me back but...","body_31")
            call her_main("It got weird really fast...","body_118")
            her "The way she kissed me..."
            call her_main("She did it like a boy would, [genie_name]...","body_117")
            call her_main("Aggressive but confident...","body_118")
            call her_main("Naturally a small group of spectators gathered up around us right away...","body_120")
            call her_main("Mostly boys of course...","body_183")
            call her_main("Some of them even cheered us on...","body_182")
            call her_main(".....","body_129")
            her "By the way, the girl I kissed, [genie_name]..."
            m "Hm...?"
            call her_main("She is one of those unpopular kids...","body_127")
            her "I know that other students make fun of her sometimes..."
            call her_main("But today changed everything...","body_129")
            her "I Single-handedly turned that girl from a social outcast..."
            call her_main("Into \"that lesbian girl who made out with Hermione Granger\"!","body_111")
            m "Wow... You are just like some kind of hero or something..."
            call her_main("I suppose I am, [genie_name]...","body_128")
            her "I changed that poor girl's life..."
            m "Now you are just pulling on my heartstrings..."
        
        elif one_out_of_three == 3: ### EVENT (C)
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("[genie_name]?","body_16",xpos=370)
            m "Yes, [hermione_name]?"
            call her_main("May I ask you a question, [genie_name]?","body_31")
            m "By all means."
            call her_main("Ehm...","body_69")
            call her_main("Why are boys so into watching girls make out with each other, [genie_name]?","body_66")
            menu:
                m "..."
                "\"Who knows? Boys are weird.\"":
                    call her_main("Yes, they are, aren't they...?","body_118")
                    m "Yes, yes..."
                    m "And that is why young girls such as yourself...."
                    m "Are often interested in a much older gentleman..."
                    call her_main("??!","body_117")
                    call her_main("That is not what I meant, [genie_name]...","body_79")
                "\"You wouldn't understand, girl.\"":
                    call her_main("Hm...","body_120")
                    call her_main("What about you, [genie_name]?","body_117")
                    her "Where you like that when you were a boy?"
                    m "You mean if I enjoyed watching two girls going at it?"
                    m "Well of course."
                    m "I still do..."
                    call her_main("Oh...","body_120")
                "\"Kissing girls? Where?!!\"":
                    call her_main("Tsk!......................","body_76") # :(
            call her_main("Well, I am only asking you this, [genie_name], because...","body_87")
            call her_main("...it is sort of becoming a new trend in our school...","body_117")
            her "Some girls are willing to do this simply to catch the attention of the boy they fancy..."
            m "Are you one of those girls, [hermione_name]?"
            call her_main("I suppose...","body_118")
            call her_main("I mean, only because of the favours you buy from me, [genie_name]...","body_120")
            m "Good... Tell me more."
            call her_main("Well, as you know, I am quite popular...","body_80")
            call her_main("So all I had to do is just mention that I would not mind doing it today...","body_74")
            her "And I had half a dozen girls lined up instantly..."
            call her_main("I chose a girl from \"Gryffindor\" of course...","body_45")
            call her_main("And we put on a little show right in the middle of the classroom...","body_31")
            m "Good... Tongue and everything?"
            call her_main("Tongue and everything, [genie_name].","body_29")
            m "Nicely done."
            call her_main("","body_45")
    
    elif whoring >= 18: # LEVEL 07+                  
        if one_out_of_three == 1: ### EVENT (A) # Snowballing
            label snowballing:
                pass
            m "[hermione_name]..."
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("Good evening, [genie_name].","body_16",xpos=370)
            m "Did you complete your task, girl?"
            call her_main("I did, [genie_name].","body_15")
            m "I'm all ears..."
            call her_main("Well, I kissed that annoying blond girl from \"Slytherin\"...","body_17")
            m "Hm... \"annoying\", huh?"
            m "Because she happens to be from \"Slytherin\"."
            call her_main("Precisely so, [genie_name].","body_16")
            m "Hm..."
            m "Don't you think that that's a little bit of prejudice on your part?"
            m "Or shall I say that you are being a \"housist\"?"
            call her_main("...a \"housist\", [genie_name]?","body_185")
            m "Well, you know... It's like \"sexist\" or \"ageist\"..."
            m "You just put an \"ist\" after something and it automatically becomes a bad thing..."
            call her_main("\"housist\" is not an actual word, [genie_name]...","body_13")
            m "It's not? Well, give it time..."
            call her_main(".............?","body_185")
            m "\"Housophobic\"...?"
            m "No, wait, I got it!"
            m "\"Housophobe\"!"
            call her_main("Stop it, [genie_name]. I am not any of those weird words...","body_07")
            her "\"Slytherins\" are evil and annoying. Nobody likes them, and that is a fact!"
            m "Fine, whatever. Back to the \"girl-kissing\" then."
            call her_main("...............","body_29")
            her "Like I was saying..."
            call her_main("I kissed that girl from \"Slytherin\"...","body_31")
            call her_main("Normally I would never do it, of course...","body_69")
            her "Not with someone from that wretched house anyways..."
            call her_main("But she approached me first and practically begged me to do it with her...","body_79")
            call her_main("And today of all days...","body_69")
            her "to be honest..."
            call her_main("She was quite attractive...","body_79")
            call her_main("For someone from \"slytherin\" that is...","body_120")
            call her_main("I did not ask her why she needed this so desperately...","body_127")
            her "She was probably just trying to boost her own popularity at my expense..."
            her "Or it could also be that someone from the school staff bought this favour from her..."
            call her_main("The same way you buy favours from me, [genie_name]...","body_186")
            m "(Snape?)"
            call her_main("If that is the case I am sure that it was professor Snape...","body_47")
            m "What? He would never..."
            call her_main("You should really investigate Professor Snape's activities, [genie_name]...","body_69")
            m "Of course..."
            m "Putting him on my \"naughty boys list\" as we speak..."
            call her_main("..........","body_66")
            m "What happened next, [hermione_name]?"
            call her_main("Oh, right...","body_87")
            her "Well, we made out for a while..."
            her "She was very... passionate."
            call her_main("So I imagine it was quite a spectacle...","body_122")
            her "The boys were cheering and whistling..."
            call her_main("So we decided to \"snowball\" a little...","body_124")
            m "I'm sorry, you decided to do what?"
            call her_main("To \"snowball\", [genie_name].","body_122")
            call her_main("It is when one girl spits into another girl's mouth...","body_128")
            her "We call it \"snowballing\"..."
            her "The boys really go crazy from that for some reason..."
            m "I imagine they do..."
            call her_main("So she spat into my mouth...","body_127")
            her "And then I spat into hers..."
            call her_main("Although I would much rather spit in her face!","body_187")
            call her_main("Then she returned my spit...","body_69")
            call her_main("And I had to fight the urge to slap her smug face for doing that...","body_187")
            call her_main("But I don't think the boys would appreciate that...","body_120")
            m "Well... You would be surprised..."
            call her_main("In any case, After that we kissed some more...","body_124")
            her "And then the break was over..."
            call her_main("And we had to run to class...","body_122")
            m "*Sigh...* Nonchalant and innocent schooldays..."
            m "Home assignments... Classes..."
            m "Schoolgirls \"snowballing\" in the courtyard..."
            m "Well done, [hermione_name]."
            call her_main("","body_68")
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("I did, [genie_name].","body_16",xpos=370)
            call her_main("Only... ehm...","body_68")
            m "What is it?"
            call her_main("Well... I have this friend...","body_45")
            her "Her name is Ginny Weasley..."
            call her_main("And... uhm...","body_188")
            her "I'm Not sure how to say this..."
            m "Just say it, [hermione_name]."
            call her_main("Well, we decided to skip the potions class together...","body_31")
            her "And study for the upcoming Herbology test instead..."
            her "So me and Ginny, we were studying..."
            her "And we got to talking about boys..."
            m "Naturally..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("And then I sort of kissed her...","body_189")
            call her_main("And Ginny returned my kiss with such passion...","body_128")
            her "that we sort of ended up doing more than just kissing..."
            g9 "And afterwards you had a pillow fight in lingerie?"
            call her_main("Err... No...","body_190")
            m "What did you do then?"
            call her_main("I am not telling you, [genie_name].","body_188") # :)
            her "You sent me out to kiss a girl..."
            her "And I did just that."
            call her_main("The rest shall remain private.","body_122")
            m "Now you are just being cruel, you little witch."
            call her_main("My points please.","body_64") # :)
            m "Fine..."
        
        elif one_out_of_three == 3: ### EVENT (C) Only takes place once
            if lazy_aka_not_yet:
                pass
            else:
                jump snowballing
            $ lazy_aka_not_yet = False #Makes sure this event only takes place once.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name].","body_45",xpos=370)
            m "Splendid. Tell me more."
            show screen blktone
            with d3
            call her_main("Of course.","body_64")
            her "I decided to go for a different approach today..."                                                                                                                                                                                                              
            stop music
            call her_main("I figured that iffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","body_63",xpos=500)
            m "Huh?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            her "If I coulddddddddddddddddddd"
            pause
            pause
            pause
            with hpunch
            g4 "{size=+5}Goddammit!!!{/size}"
            g4 "{size=+5}AKABUR?!!!{/size}"
            a4 "Huh...? WHAT?!! What do you want from me?"
            a4 "There is no release date set! Stop asking me!"
            g4 "What are you talking about?"
            a5 "I mean, I'm not sleeping..." 
            a7 "*Yawn*..."
            a5 "................"
            m "So Is Hermione going to stutter from now on? Is that what this is?"
            pause
            pause
            g4 "Are you still there?"
            a1 "I'm not sleeping..."
            a5 "Just resting my eyes..."
            g4 "Dammit, man."
            g4 "Just go catch up on some sleep before you ruin the whole thing."
            m "Get some shuteye and then finish this event properly."
            a1 "I can't..."
            a1 "I want this game to be released as soon as possible..."
            a1 "No, scratch that. I want it to be released sooner than possible..."
            a1 "People trust me... and..."
            a7 "*yawn*..."
            a1 "And...."
            pause
            pause
            m "Akabur?"
            m "Dude?"
            pause
            pause
            m "*Sigh*...well, we could let this one event slide I suppose."
            m "Just this once though..."
            m "And Hermione's \"perversion\" level did increase..."
            m "So there is no need for save-scumming..."
            aa "Zzzz....zzz....."
            aa "Zzz.... Lola? no... Put your tits away I said... Zzzz....."
            aa "Zzz.... And don't call me that.... Zzz...."
            m "*Sigh...* That's just sad..."
    
    $ gryffindor +=45
    m "The \"Gryffindor\" house gets 45 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_KissAGirl_OBJ.points += 1
    $ hg_pr_KissAGirl_OBJ.complete = True
    $ hg_pr_KissAGirl_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return
    
    
##(Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).
label hg_pr_HandjobClassmate: #LV.6 (Whoring = 15 - 17)
    
    $ current_payout = 55 #Used when haggling about price of the favour.
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to give a handjob to one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_pr_HandjobClassmate_OBJ.points == 0: # <================================================================================ FIRST TIME
        if whoring <=14 or hg_pr_KissAGirl_OBJ.points <= 1:
            m "[hermione_name], I want you to do something different today..."
            call her_main("...?","body_07",xpos=140)
            m "I want you to give a handjob to one of your classmates."
            jump too_much
        m "[hermione_name], I want you to do something different today..."
        call her_main("...........","body_15",xpos=140)
        m "I want you to go out there and have sex with one of your classmates."
        stop music
        with hpunch
        call her_main("{size=+5}What?!!{/size}","body_48")
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("Now you have done it, [genie_name]! You crossed the line!","body_47")
        her "I know I did sell you a couple of rather questionable favours in the past..."
        with vpunch
        call her_main("{size=+5}But THIS?!{/size}","body_86")
        her "I cannot believe that you would ask one of your pupils to... to..."
        call her_main("We are done here, [genie_name]!","body_76")
        m "Alright, alright, calm down, would you?"
        call her_main("I most certainly would not, [genie_name]! This is beyond inappropriate!","body_30")
        m "Alright, fine, maybe I really did cross some sort of line this time..."
        call her_main("You think [genie_name]?! You think!!?","body_47")
        m "Yes, I apologize..."
        call her_main(".........","body_79")
        m "How about we try something less... engaging instead?"
        call her_main("............","body_120")
        m "I'll be willing to grant \"Gryffindor\" fifty five points."
        m "All I ask in return is..."
        call her_main("..........?","body_187")
        m "...that you go out there and give some lucky boy a handjob..."
        call her_main("!!!......","body_47")
        m "Oh, come on... Just a harmless handjob."
        call her_main("...","body_66")
        m "Fifty five house points..."
        call her_main("..............","body_69")
        call her_main("I am glad that you came to your senses, [genie_name].","body_79")
        m "Oh, but of course. Thank you for keeping me in check."
        m "Are you up for it then?"
        call her_main("I am willing to give it a try...","body_69")
        m "Splendid... See you tonight then."
    
    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 15 and whoring <= 17: # LEVEL 06 FIRST EVENT.
            m "Today's favour shall be..."
            call her_main(".........","body_117",xpos=140)
            m "A Handjob to the boy of your choosing!"
            call her_main("...again?","body_118")
            m "Sure, why not?"
            m "And another fifty five house points for the \"Gryffindor\" house of course."
            call her_main("..........","body_29")
            m "So... Are you up for that, [hermione_name]?"
            call her_main("I will see what I can do...","body_69")
            m "Splendid!"
        
        elif whoring >= 18 and whoring <= 20: # LEVEL 07
            m "Ready to go have sex with one of your classmates yet?"
            stop music fadeout 1.0
            call her_main("What?","body_72",xpos=140)
            call her_main("Of course not! I would never--","body_30")
            m "How about a handjob then?"
            call her_main("...............","body_69")
            m "Oh come on. You did it before."
            call her_main("hm..........","body_79")
            her "Fifty five house points?"
            m "Naturally."
            call her_main("Well, alright... I'll see what I can do...","body_118")
        
        elif whoring >= 21: # LEVEL 08+
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "What do you think about giving one of your classmates another handjob?"
            call her_main("I don't mind, [genie_name].","body_71",xpos=140)
            m "Really?"
            call her_main("Yes... I mean, it's just a handjob...","body_68")
            m "Great. Go have fun then!"
            m "And report back to me after your classes, as usual."
            call her_main("Of course, [genie_name].","body_74")
    
    $ hg_pr_HandjobClassmate_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_HandjobClassmate_complete:
    call hg_pr_EnterRoom_block
    
    if whoring >= 15 and whoring <= 17: # LEVEL 06                    
        if one_out_of_three == 1: ### EVENT (A)
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("Quite awful... of course...","body_09",xpos=370)
            m "Just tell me what happened, [hermione_name]..."
            call her_main("I made a complete fool out of myself, that's what happened, [genie_name].","body_66")
            her "....."
            m "..."
            call her_main("..........","body_29")
            call her_main("I don't want to talk about it...","body_69")
            her "You told me to go and touch a boy's penis and I did just that, [genie_name]."
            call her_main("Please, just let me have my points now, [genie_name]...","body_31")
            m "I did not tell you to \"go and touch a boy's penis\", [hermione_name]."
            m "I told you to give one of your classmates a proper handjob."
            call her_main("Well, yes... that was what I meant of course...","body_79")
            m "Did you make him cum, then?"
            call her_main("[genie_name]?","body_31")
            m "Did his \"wee-wee\" shoot white stuff at you, [hermione_name]?"
            call her_main("Well...","body_29")
            call her_main("No, it did not...","body_33")
            menu: 
                "\"Well, this doesn't count then.\"":
                    stop music fadeout 4.0
                    call her_main("What?","body_119",xpos=140)
                    her "But, [genie_name], I..."
                    m "If you didn't make him cum then that wasn't a proper handjob. Period."
                    call her_main("But... But what was it then...?","body_117")
                    m "How should I know? A cock massage?"
                    call her_main("Aww...","body_118")
                    her "But I really tried my best..."
                    m "No handjob - no payment, [hermione_name]."
                    call her_main(".....","body_117")
                    m "You are free to go, [hermione_name]."
                    call her_main(".........","body_69")
                    $ mad +=9
                    $ hg_pr_HandjobClassmate_OBJ.inProgress = False
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                "\"You shall only get half the payment then.\"":
                    $ current_payout = 27 #Used when haggling about price of th favour.
                    call her_main("Oh...?","body_31",xpos=140)
                    m "Is that a Problem, [hermione_name]?"
                    call her_main("No [genie_name]... It's only fair I suppose...","body_118")
                    m "Of course it is!"
                "\"Well, you did try. Here are the points.\"":
                    call her_main("Really?","body_117",xpos=140)
                    call her_main("Thank you, [genie_name]!","body_87")
                    call her_main("I promise, I will try harder next time!","body_45")
                    call her_main("Ehm... Should you request a similar favour in the future, I mean...","body_44")
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            call her_main("It went well, [genie_name]...","body_31",xpos=370)
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "I asked one if the \"Gryffindor\" boys to let me do \"it\" to him..."
            call her_main("To my surprise he agreed eagerly.","body_183")
            m "Shocker..."
            call her_main("So we hid behind one of those huge tapestries in the east wing...","body_127")
            call her_main("And I... wanked him until he came...","body_69")
            her "........."
            call her_main("And I asked him to keep the whole thing a secret, but...","body_117")
            m "What's the matter, [hermione_name]?"
            m "Doubting the honesty of your fellow \"Gryffindors\"?"
            call her_main("Of course not, [genie_name].","body_120")
            call her_main("...........................","body_118")
            call her_main("Still... Performing this sort of task could really damage my reputation...","body_117")
            m "Is this your way of asking for a raise, [hermione_name]?"
            m "Fifty Five points is as high as I can go with this one."
            call her_main("Oh... Of course...","body_118")
            m "Unless, you've changed your mind about having sex with one of your classmates?"
            call her_main("What?","body_48")
            call her_main("[genie_name], I am not a prostitute!","body_118")
            m "Well, in that case..."
        
        elif one_out_of_three == 3: ### EVENT (C) Event level: 01.
            # HERMIONE HAVE A CUM-STAIN ON HER SHOULDER.
            m "[hermione_name], how did it go?"
            $ aftersperm = True #Shows stains on Hermione's uniform.
            $ uni_sperm = True  #Universal sperm.
            $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            show screen blktone
            with d3
            call her_main("Awful, [genie_name]. Simply awful...","body_32",xpos=370)
            m "You've got something... in your hair there..."
            call her_main("Huh?","body_31")
            call her_main("Oh, no! I thought I got it all off...","body_189")
            show screen ctc
            pause
            show screen blkfade 
            with d3
            pause.5
            $ uni_sperm = False  #Universal sperm.
            call her_main("","body_120")
            hide screen blkfade
            with d3
            pause
            hide screen ctc
            m "Hm... So I suppose you have completed your task?"
            call her_main("I did, [genie_name]...","body_69")
            m "What's the problem, then?"
            call her_main("..........","body_29")
            call her_main("All boys are jerks! That is the problem, [genie_name]!","body_30")
            call her_main("I gave this one boy a good wanking...","body_87")
            her "And do you know how he thanked me?"
            call her_main("He got his spunk allover me...","body_86")
            call her_main("And he did that on purpose, I know he did!","body_30")
            call her_main("Nasty, good for nothing \"ravenclaws\"...","body_29")
            m "Well, I'd say a job well done."
    
    elif whoring >= 18 and whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Ehm...","body_31",xpos=370)
            her "Not yet, [genie_name]..."
            m "Not yet?"
            call her_main("Yes... Let me explain, [genie_name]...","body_29")
            call her_main("uhm... Well...","body_31")
            her "I was wanking this one boy off in one of the empty classrooms..."
            her "And that nasty ghost Peeves walked in..."
            call her_main("Or rather flew in on us...","body_29")
            call her_main("And as soon as he realized what I was doing to the boy...","body_31")
            her "He started to yell obscenities at us..."
            her "So we had to leave in a hurry..."
            m "I see..."
            call her_main("That is not all, [genie_name]...","body_69")
            m "Go on..."
            call her_main("Well, I sort of made a promise to the boy...","body_87")
            her "I promised to meet him after my classes and..."
            call her_main("...and finish what I have started...","body_79")
            m "I see..."
            m "Did you?"
            call her_main("No, [genie_name]. Not yet...","body_117")
            her "I am going to meet him as soon as we are done here, [genie_name]."
            m "Hm..."
            call her_main("So if you could just give those points in advance...","body_118")
            her "I would go meet with the boy right away and..."
            call her_main("And give him a proper handjob...","body_189")
            menu:
                "\"No. You failed this favour, [hermione_name].\"":
                    stop music fadeout 3.0
                    call her_main("B-but...","body_183")
                    call her_main("But I gave him my word...","body_119")
                    her "I swore on Godric Gryffindor's name..."
                    call her_main("And now I will have to give him the wank off no matter what...","body_118")
                    m "Well, I didn't force you to give him that promise, did I?"
                    call her_main("......","body_117")
                    call her_main("This is just not fair!","body_32")
                    $ mad +=20
                    $ hg_pr_HandjobClassmate_OBJ.inProgress = False
                    jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                "\"Alright, I think I can trust you.\"":
                    call her_main("Thank you, [genie_name].","body_45")
                    her "I knew you would understand."
                    m "Just make sure you finish your job properly this time."
                    call her_main("Of course, [genie_name]. I will give him the wank of his life, I promise!","body_74")
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("I did, [genie_name]...","body_16",xpos=370)
            call her_main("Although I am still not sure how I feel about all of this...","body_29")
            m "You personal feelings are of no concern to me, [hermione_name]."
            m "Just tell me how it went."
            call her_main("Well, there is not much to tell. [genie_name]...","body_31")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "Today I gave another handjob to one of my classmates..."
            call her_main("Me, Hermione Granger...","body_87")
            call her_main("Giving free hanjobs in the school's restroom...","body_118")
            m "Wait. What do you mean with \"free\"?"
            call her_main("Oh, of course... I get paid with house points for this...","body_117")
            her "But nobody knows about that..."
            her "And to everyone else this just looks like some harlot who does this for fun..."
            call her_main("They must think I am a slut...","body_87")
            call her_main("..............","body_88")
            call her_main("Do you think I'm a slut, [genie_name]?","body_190")
            menu:
                "\"What? Of course not, [hermione_name]!\"":
                    call her_main("..............","body_188")
                    call her_main("You are right, [genie_name]...","body_124")
                    her "I am making this sacrifice for the glory of the \"Gryffindor\" house."
                    call her_main("I am not taking pleasure in this sort of activity...","body_121")
                    call her_main("Because if I would...","body_69")
                    her "That would mean I really am a slut..."
                    call her_main("And I am not...","body_118")
                    her "......"
                    her "I am not a slut..."
                "\"A slut? No... Not yet.\"":
                    call her_main("\"Not yet\"??!","body_117")
                    call her_main("..........","body_118")
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("Well, of course!","body_72")
                    call her_main("You are right, as usual, [genie_name]!","body_15")
                    m "Huh?"
                    call her_main("I have done a few... naughty things...","body_14")
                    her "But that does not mean anything!"
                    call her_main("...........","body_12")
                "\"Yes, that's exactly what you are.\"":
                    call her_main("I was afraid that you would say that, [genie_name]...","body_20")
                    her "But you are wrong, [genie_name]."
                    call her_main("You of all people should understand that I take no pleasure in this...","body_21")
                    call her_main("I just do what needs to be done...","body_23")
                    $ mad = 10
            call her_main("[genie_name], can I just get paid now, please?","body_13")
            m "Get paid? But you didn't tell me how it went yet?"
            her "I did not?"
            call her_main("[genie_name], I gave a handjob to one of my classmates today...","body_183")
            her "I wanked his cock until he came..."
            call her_main("Is that not what you told me to do?","body_66")
            m "That's exactly what I told you to do, [hermione_name]."
            call her_main("Then I would like to get paid now, please.","body_184")
            m "........"
            m "Fine..."
        
        elif one_out_of_three == 3: ### EVENT (C)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes, [genie_name]. I did.","body_16",xpos=370)
            m "Great. Tell me more."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("Well, today was a rather busy day...","body_14")
            her "And I had to catch up on some studying..."
            her "So I really had no time to plan this out properly, like I normally would..."
            her "I pretty much just approached the first boy I saw..."
            call her_main("And asked him if he wants me to wank him off.","body_69")
            her "a Few minutes later I was already stroking his hard cock in the restroom stall..."
            m "How very efficient of you..."
            call her_main("Thank you, [genie_name].","body_79")
            call her_main("So, as I was saying...","body_69")
            her "I wanked his cock until he came..."
            call her_main("But after that he said: \"Good job, slut\" and just left me there...","body_66")
            call her_main("Such a mean thing to do...","body_69")
            call her_main("It made me feel so cheap... and used.","body_120")
            her "But it get's worse..."
            her "......."
            call her_main("I think on some level it also made me feel good somehow...","body_118")
            her "All these favours I have been selling to you lately, [genie_name]..."
            call her_main("...it's starting to affect me.","body_117")
            her "[genie_name], what is happening to me?"
            menu:
                "\"This is nothing. Stop overthinking it!\"":
                    call her_main(".......","body_190")
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    call her_main("You are probably right, [genie_name]. As usual...","body_188")
                    her "This does not have to mean anything..."
                "\"That is a natural response...\"":
                    call her_main("It is?","body_190")
                    m "Of course."
                    m "You are a girl and he is a boy..."
                    m "You got excited and it made you feel good..."
                    call her_main("Hm...","body_188")
                    m "Now if you were to give a handjob and feel completely indifferent about it..."
                    m "...that would be... unnatural."
                    call her_main("I think you are right, [genie_name].","body_190")
                    call her_main("As usual.","body_188") # :)
                "\"Yes! All goes according to plan!\"":
                    call her_main("What?","body_119")
                    m "What?"
                    call her_main("[genie_name], did you just say \"All goes according to plan\"?","body_187")
                    m "Did I?"
                    m "Oh, yes, of course."
                    m "ensuring that \"Gryffindor\" gets the house cup this year."
                    m "That's the plan And thanks to your hard work, [hermione_name]..."
                    m "All goes according to keik-... I mean, the plan..."
                    call her_main("Hm...","body_120")
                    $ mad += 11
    
    elif whoring >= 21: # LEVEL 08+                    
        if one_out_of_three == 1: ### EVENT (A)
            if sucked_off_ron: #In public events. Give a handjob to classmate. Event level 03. Event # 1. "Jerked of and suked of Ron Weasley". Turns True after that.
                jump blowjob_ron
            else:
                $ sucked_off_ron = True #Makes sure this event is not repeated twice.
                stop music fadeout 1.0
                # HERMIONE HAS CUM ON HAIR.
                #$ aftersperm = True #Shows stains on Hermione's uniform.
                $ uni_sperm = True  #Universal sperm.
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                show screen blktone
                with d3
                call her_main("[genie_name]...","body_11",xpos=370)
                m "[hermione_name]..."
                call her_main("I did a bad thing today, [genie_name]...","body_10")
                m "Did you now? Do tell..."
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                her "Yes, I did a bad thing... a very bad thing..."
                call her_main("A very bad and foolish thing...","body_09")
                her "..."
                m "...................."
                her "......................"
                call her_main("I wanked off one of my best friend's brothers...","body_22")
                m "Interesting..."
                call her_main("Seemed like such a great idea at first...","body_21")
                her "And Ron was so up for it..."
                call her_main("But if Ginny were to find out... she...","body_139")
                call her_main("She would most certainly kill me, [genie_name]...","body_22")
                m "A handjob, huh? Are you sure that was all you did?"
                call her_main("[genie_name]?","body_21")
                m "There is something in your hair..."
                call her_main("What? But I swallowed it all... err...","body_19")
                call her_main("I mean...","body_140")
                call her_main("*Sigh*","body_139")
                her "...I sucked him off, [genie_name]."
                her "I did not plan to... but..."
                call her_main("Ron is always so nice to me...","body_140")
                call her_main("And I wanted to thank him...*Sob!*","body_143")
                call her_main("And now Ginny will kill me! *Sob!*","body_22")
                her "She will kill me, [genie_name]!"
                call her_main("And if she does not I will probably die of shame anyway.","body_143")
                her "No, no, no... How will I ever face her...?"
                m "Calm down, [hermione_name]."
                m "I assure you, this is not something a boy would be eager to brag about to his sister."
                call her_main("It is not?","body_140")
                m "Don't be silly, [hermione_name]."
                call her_main("Hm...","body_23")
                call her_main("You are probably right, [genie_name]...","body_19")
                her "And I made Ron give me his word that he will keep the whole incident a secret..."
                call her_main("So, I think I should just trust him to keep his word...","body_10")
                call her_main("..........","body_13")
                her "..."
                call her_main("Will I get paid for this, [genie_name]?","body_06")
                m "Of course."
        
        elif one_out_of_three == 2: ### EVENT (B) (WANK DURING CLASS). Event level: 03.
            label blowjob_ron: #Sent here if sucked off Ron already.
                pass
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes I did, [genie_name].","body_06",xpos=370)
            call her_main("But, ehm...","body_11")
            m "...?"
            call her_main("Well, I did not just wank off one of my classmates...","body_31")
            her "I.............."
            call her_main("...............","body_88")
            m "Spit it out, [hermione_name]. The suspense is killing me."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("I sort of did it during class...","body_87")
            m "Impressive..."
            call her_main("Sir, you don't understand.  Let me try and explain.","body_118")
            hide screen blktone
            with d3
            her "I don't even know what came over me."
            show screen dual_hand_job
            with d5
            call her_main("I was trying to act as nonchalant as I could...")
            her "But, I suddenly had this incredibly pleasant urge to do it during Professor Snape's class."
            her "I couldn't even take notes with my other hand..."
            her "It was wrapped around another thick hot cock too."
            m "You gave two boys handjobs at the same time?!"
            call her_main("Yes Sir.","body_122")
            call her_main("And I think I gave them the wank of their life too...","body_124")
            her "Because they did not just cum."
            her "Their cocks simply exploded with spunk."
            m "You enjoyed it, didn't you?"
            call her_main("To be completely honest with you, sir... I did.","body_123")
            call her_main("It was exciting.","body_111")
            call her_main("God, there was so much.  My hands looked like a candle had dripped hot wax all over them.","body_123")
            call her_main("I didn't know what to do I could't just go about the rest of class with huge globs of cum all over my hands.","body_118")
            her "So I decided to rub it all over the inside of my thighs to keep from having to stain my clothes."
            call her_main("Every time I walked I could smell their cum from between my legs.","body_134")
            m "That's quite an interesting story miss Granger."
            hide screen dual_hand_job
            with d5
            show screen blktone
            with d3
            call her_main("I definately want them both at the same time.","body_133")
            m "..."
            call her_main("Yeah, two huge cocks exploding massive loads of cum everywhere.","body_134")
            m "........"
            call her_main(".......","body_134")
            m "Ehm....."
            call her_main("Oh god, I'm sorry [genie_name], I was thinking of something else.","body_119")
            m "Yes... sure, OK."
            call her_main("","body_01")
        
        elif one_out_of_three == 3: ### EVENT (C) Event level: 03. (Wanked off 5 boys).
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            call her_main("Yes, I did [genie_name]...","body_129",xpos=370)
            her "More than once actually..."
            m "More than once?"
            call her_main("Five times, [genie_name]...","body_128")
            her "I got carried away a little I suppose..."
            m "What do you mean \"five times\", [hermione_name]?"
            call her_main("I mean I wanked off five boys today, [genie_name].","body_129")
            m "Very impressive, [hermione_name]."
            call her_main("Thank you, [genie_name].","body_128")
            m "You don't expect me to multiply your payment by seven or anything, do you?"
            call her_main("Of course not, [genie_name].","body_188")
            m "Than why do it?"
            call her_main("Well, it sort of just happened...","body_190")
            her "I was wanking off this one boy..."
            her "And another boy walked in on us..."
            her "He called his friends..."
            call her_main("One thing lead to another...","body_128")
            m "And you ended up jerking off five cocks..."
            call her_main("...yes.","body_121")
            m "Well done, miss Garnger."
            call her_main("","body_128")
    
    $ gryffindor += current_payout #55
    m "The \"Gryffindor\" house gets [current_payout] points!"
    her "Thank you, [genie_name]."
    
    $ uni_sperm = False  #Universal sperm.
    $ aftersperm = False #Shows stains on Hermione's uniform.
    
    $ hg_pr_HandjobClassmate_OBJ.points += 1
    $ hg_pr_HandjobClassmate_OBJ.complete = True
    $ hg_pr_HandjobClassmate_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return
    
    
##(Level 07) (65 pt.) (Blowjob to a boy). (Available during daytime only).
label hg_pr_BlowjobClassmate: #LV.7 (Whoring = 18 - 20)
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to go give a blowjob to one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_pr_BlowjobClassmate_OBJ.points == 0: # <================================================================================ FIRST TIME
        m "[hermione_name], I will be buying another favour from you today."
        call her_main("Thank you, [genie_name]. I really appreciate it.","body_16",xpos=140)
        m "Sure, Happy to help."
        m "I need you to go give a blowjob to one of your classmates."
        stop music fadeout 1.0
        call her_main("!!!","body_48")
        her "...with my mouth?"
        if whoring <=17 or hg_pr_HandjobClassmate_OBJ.points <= 1:
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "Yes, that's how it's usually done..."
        call her_main("[genie_name], I...","body_120")
        call her_main("I refuse to sell you a depraved favour like that, [genie_name].","body_186")
        call her_main("Can't I just kiss another girl instead?","body_131")
        her "I do not mind that..." 
        m "[hermione_name], please stop wasting my time..."
        m "If you are not in the mood to sell favours today..."
        m "Then there is the door."
        call her_main("But I need the points, [genie_name]. You know that.","body_120")
        m "It's as the saying goes, [hermione_name]..."
        m "\"If you won't suck a dick for it - you don't need it.\""
        call her_main("Tch...","body_187")
        her "............................"
        m ".........................................."
        call her_main("...alright.","body_69")
        her "I'll do it..."
        m "Go do it, then!"
        m "Report back to me after your classes."
        call her_main("......................................................................","body_187")
        her "......................................................................"
        her "......................................................................"
        m "You may leave, [hermione_name]."
        her "........."
    
    else: # <================================================================================ NOT FIRST TIME
        if whoring >= 18 and whoring <= 20: # LEVEL 07 FIRST EVENT.
            m "Go give some lucky boy another blowjob, [hermione_name]."
            call her_main("......Again?","body_66",xpos=140)
            m "Yes, again."
            call her_main("..........","body_79")
        elif whoring >= 21: # LEVEL 08+ SECOND EVENT.
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "[hermione_name]..."
            m "Do you believe in horoscopes?"
            call her_main("Not even a little bit, [genie_name]...","body_12",xpos=140)
            m "Well, maybe you should..."
            call her_main("...?","body_14")
            m "Because I got yours right here and it says..."
            m "\"Dedicate today to something you do well\"..."
            call her_main("Something I do well...?","body_13")
            m "Go suck on some cocks, [hermione_name]."
            call her_main(".....................","body_79") # :(
            m "Report back to me after your classes as usual..."
            call her_main("Of course...","body_69")
    
    $ hg_pr_BlowjobClassmate_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_BlowjobClassmate_complete:
    call hg_pr_EnterRoom_block
    
    if whoring >= 18 and whoring <= 20: # LEVEL 07                    
        if one_out_of_three == 1: ### EVENT (A)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            m "You know the drill, [hermione_name]. Start talking."
            show screen blktone
            with d3
            call her_main("I have completed your task, [genie_name].","body_66",xpos=370)
            m "Good. Tell me more."
            call her_main("What is there to tell, [genie_name]?","body_69")
            her "I sucked off one of my classmates today..."
            her "And that's it..."
            m "Hm... I see..."
            m "..............."
            call her_main("....................................","body_118")
            m "Did you swallow?"
            call her_main("...........................","body_79")
            m "[hermione_name], did you swallow the load properly?"
            call her_main("Yes I did, [genie_name].","body_47")
            m "Well, I suppose that will do for now..."
        
        elif one_out_of_three == 2: ### EVENT (B)
            m "[hermione_name], did you complete your task?"
            show screen blktone
            with d3
            play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            call her_main("[genie_name], I...","body_118",xpos=370)
            her "I tried, but..."
            call her_main("The boy turned me down, [genie_name]...","body_67")
            call her_main("I cannot believe that actually happened...","body_22")
            her "I am one of the top students in this school!"
            her "One of the most popular ones too..."
            call her_main("And he turns me down?","body_47","tears_01")
            her "Why would he insult me like that?!"
            m "So you're insulted because that boy refused to put his cock in your mouth?"
            call her_main("Wouldn't you be, [genie_name]?","body_47","tears_02")
            m "I think I would get over it rather quickly..."
            call her_main("He rejected me [genie_name]...","body_187")
            her "Who does he think he is?!"
            call her_main("With all due respect, [genie_name], you wouldn't understand...","body_186")
            m "Well, in any case. I can't pay you for this."
            call her_main("Of course... I would not expect you to, [genie_name].","body_79","tears_01")
            her "I failed to complete my task and deserve no praise of any kind..."
            her "And should you pay me out of pity..."
            call her_main("Then That would only worsen the insult...","body_69")
            m "Hm... In that case, maybe I should pay you anyway..."
            call her_main("No, [genie_name]. I would not accept it...","body_79")
            m "Hm... Well, this will be all then."
            her "Have a good night, [genie_name]."
            hide screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3   
            $ display_h_tears = False
            $ hg_pr_BlowjobClassmate_OBJ.inProgress = False
            jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
        
        elif one_out_of_three == 3: ### EVENT (C)
            #play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            call her_main("I still find the idea of selling a favour like this appalling, [genie_name].","body_69",xpos=370)
            call her_main("But other than that it well surprising well...","body_79")
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            her "I gave a proper blowjob to this handsome boy from \"Ravenclaw\"..."
            call her_main("And he was such a gentleman about it...","body_87")
            call her_main("He even warned me when he was about to cum.","body_118")
            m "A true gentleman indeed."
            m "Did you swallow?"
            call her_main("Of course I did, [genie_name].","body_120")
            her "I told you - I gave the boy a proper blowjob."
            call her_main("The least I could do for someone who treated me with respect for a change...","body_118")
            m "Well, in that case."
            
    if whoring >= 21: # LEVEL 08 =+               
        if one_out_of_three == 1: ### EVENT (A)
            stop music fadeout 1.0
            # HERMIONE ALL MESSED UP, WITH RUNNING MASCARA.
            $ u_tears_pic = "01_hp/13_hermione_main/tears_03.png"
            $ display_h_tears = True
            $ aftersperm = True
            $ uni_sperm = True
            $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
            show screen blktone
            with d3
            call her_main("","body_47",xpos=370)
            show screen ctc
            pause
            hide screen ctc
            m "[hermione_name]..."
            m "You look like hell..."
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
            call her_main("[genie_name], I have been raped.","body_30")
            m "Seriously?"
            call her_main("Yes, [genie_name].","body_79")
            her "That nasty boy from \"Slytherin\" raped me..."
            call her_main("Or raped my face rather I suppose...","body_87")
            her "And--"
            play sound "sounds/burp.mp3"
            call her_main("*Burp!*...","body_132")
            call her_main("Excuse me.","body_118")
            call her_main("He came so much I was barely able to swallow it all...","body_86")
            her "Bloody bastard!"
            call her_main("You think I could file a complaint, [genie_name]?","body_187")
            m "Hm... I suppose..."
            m "But keep in mind that the moment we bring the ministry into this..."
            m "All this \"favour selling business\" will have to stop immediately."
            call her_main("Oh...?","body_189")
            her ".................."
            call her_main("Please, never mind what I just said then...","body_74")
            m "Are you sure? You look pretty messed up."
            her "No, no. It's nothing really..."
            her "After all I was the one who offered him a free blowjob..."
            her "He just got a bit rough with me closer to the end, that's all..."
            her "I think I am just overreacting..."
            m "I see..."
            her "Can I just--"
            play sound "sounds/burp.mp3"
            call her_main("*Burp!*...","body_48")
            call her_main("Excuse me, [genie_name].","body_118")
            call her_main("{size=-3}(He just kept on cumming... My stomach feels so full...){/size}","body_34")
            call her_main("Can I get my payment now, please?","body_31")
        
        elif one_out_of_three == 2: ### EVENT (B)
            # HERMIONE COVERED IN CUM
            label suked_off_them_both:
                pass
            stop music fadeout 1.0
            $ uni_sperm = True
            $ u_sperm = "01_hp/13_hermione_main/auto_10.png"
            show screen blktone
            with d3
            call her_main("","body_78")
            show screen ctc
            pause
            hide screen ctc
            her "Good evening, [genie_name]..."
            g4 "[hermione_name]?!"
            g4 "What happened to you, [hermione_name]?"
            g4 "All I asked you to do was to give a blowjob to one of your classmates."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("That... that was exactly what I did, [genie_name].","body_118")
            m "[hermione_name], you are covered in cum head to toe."
            call her_main("I am?","body_121")
            her "Oh... Did I forget to clean myself up?"
            call her_main("How embarrassing...","body_128")
            her "That thing at the boy's restroom sort of escalated I suppose..."
            her "Before I knew what happened I was surrounded with hard throbbing cocks..."
            call her_main("Oh... Just talking about it makes me shiver with excitement... err..","body_133")
            call her_main("...I mean, with fear... no, not fear...","body_136")
            call her_main("Embarrassment?","body_188")
            m "Are you asking me?"
            call her_main("Oh, excuse me, [genie_name]... I feel a little lightheaded...","body_123")
            her "I think I need to go lie down for a while..."
            m "Don't forget to take a shower first."
            call her_main("A shower? Why?","body_128")
            m "Never mind..."
            show screen ctc
            pause
            hide screen ctc
        
        elif one_out_of_three == 3: ### EVENT (C)
            if  suked_off_ron_and_har:
                jump suked_off_them_both
            else:
                 $ suked_off_ron_and_har = True #In public events. Give blowjob to a classmate. Event level 03. Event # 3. "Sukerd off Harrt and Ron". Turns True after that.
            m "[hermione_name], how did it go?"
            show screen blktone
            with d3
            call her_main("Splendid, [genie_name]. Simply splendid.","body_74",xpos=370)
            m "Really? Do tell."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            call her_main("Today I did something I wanted to do for such a long time now...","body_78")
            her "But never could muster up enough courage for..."
            m "Hm..?"
            call her_main("Today I sucked off my two best friend in the entire world!","body_121")
            call her_main("And it was every bit as exciting as I thought it would be.","body_124")
            call her_main("I made their cocks all sloppy with saliva...","body_123")
            her "I sucked on their balls too..."
            call her_main("But the best part was to see their faces...","body_134")
            her "The boys could not believe it was actually happening..."
            call her_main("To be honest, neither could I...","body_133")
            her "I, Hermione granger - the girl they knew for years..."
            call her_main("Sucking on their cocks...","body_135")
            call her_main("Like some nasty little slut...","body_139")
            m "Are you in love with those boys, [hermione_name]?"
            call her_main("I don't know, [genie_name]... Maybe...","body_74")
            her "Could I get paid now please?"
            m "Sure..."
    
    $ gryffindor += 65 #65
    m "The \"Gryffindor\" house gets 65 points!"
    her "Thank you, [genie_name]."
    
    $ display_h_tears = False
    $ aftersperm = False
    $ uni_sperm = False
    
    $ public_whore_ending = True #Activates "Public Whore" ending.
    
    $ hg_pr_BlowjobClassmate_OBJ.points += 1
    $ hg_pr_BlowjobClassmate_OBJ.complete = True
    $ hg_pr_BlowjobClassmate_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return
    
    
##(Level ??) (?? pt.) (Blowjob to a teacher). (Available during daytime only).
label hg_pr_BlowjobTeacher:# "teacher blowjob" (Level ??)
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to give a blowjob to one of her teachers?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if whoring < 15:
        jump too_much
    else:
        m "Today's favour shall be..."
        call her_main(".........",117,140)
        m "A Blowjob with Professor Snape!"
        call her_main("Snape!",119)
        call her_main("Ehm...",127)
        her "I don't mind, sir."
        m "Really?"
        call her_main("Yes... I mean, it's just a blowjob, I've already grown quite accustomed to it...",68)
        m "Great. Go have fun then!"
        m "And report back to me after your classes, as usual."
        call her_main("Of course, sir.",74)
    
    $ hg_pr_BlowjobTeacher_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_BlowjobTeacher_complete:
    call hg_pr_EnterRoom_block
    
    call her_main("Good evening, sir...","body_01",xpos=370,ypos=0)
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    m "You know the drill, girl. Start talking."
    show screen blktone
    with d3
    call her_main("I have completed your task, sir.","body_66")
    m "Good. Tell me more."
    call her_main("There isn't that much to say, sir?","body_69")
    her "I wrapped my lips around Professor Snape's cock like the good student I am and sucked him off just like you requested."
    her "And that's it..."
    m "Hm. I'm not sure, You seem exceptionally evasive this evening."
    m "..............."
    call her_main("....................................","body_118")
    m "Did you swallow?"
    call her_main("...........................","body_79")
    m "Miss Granger, did you swallow his load properly?"
    call her_main("No sir, I did not...","body_47")
    m "No?  How do you consider that a proper blowjob Miss Granger?"
    call her_main("It's not my fault Sir!","body_118")
    her "You see it's like this...."
    hide screen blktone
    show screen snape_facial
    with d5
    call her_main("Professor Snape and I have a break just after lunch.","body_124")
    her "So I asked if I could have his thick hard cock in my little school girl mouth."
    m "Woah, child."
    call her_main("I know, flirting with all those boys has let me say the filthiest things without even a second thought.","body_75")
    call her_main("Cock, cum, fuck, blowjob, pussy, cunt.....mudblood...","body_123")
    call her_main("So we sneak off to this little spot and I set out one of my books and my wand just in case someone happens by.","body_45")
    her "Then I kneel down so I can start to suck him off."
    m "Where you enjoying yourself?"
    call her_main("Not so much at first.","body_43")
    call her_main("Did you know Professor Snape says the most interesting things with his cock in a student's mouth.","body_16")
    call her_main("Things like mudslut and cumdump, things a Professor should never say.","body_121")
    her "Foul things that turned me on finally."
    call her_main("I swear, if I wore panties these days I'd have had to change before I went to my next class.","body_134")
    call her_main("I'm sure he didn't know about this favour though.","body_127")
    call her_main("Because he was pounding the back of my throat and his fingers were clenched in my hair.","body_78")
    her "He'd just fuck and fuck and fuck my tight little throat."
    call her_main("I was hoping he'd pull out a little and at least let me savour it before dumping himself into me.","body_78")
    call her_main("But then he pulled all the way out and came all over my face and hair.","body_86")
    her "All i could do was barely catch some in my hands when it dribbled off my face."
    call her_main("So I did not manage to \"Properly\" swallow that bastard's load, Sir.","body_69")
    call her_main("However, I will admit to savouring what I could off my hands and collecting what i could smear from my face that I couldn't catch into my hot little mouth.","body_129")
    call her_main("You should have heard the smacking sound I was making to get as much cum as I could between my lips.","body_134")
    hide screen snape_facial
    with d5
    show screen blktone
    with d3
    call her_main("Are you satisfied with that [genie_name]?","body_68")
    m "That miss Granger, was better than I had initially expected."
    $ gryffindor +=70
    m "Seventy points to \"Gryffindor\" miss Granger." 
    her "Thank you, sir..."
    m "You can go now."
    her "Good night, sir."
    #m "Yes, good night..."
    
    $ hg_pr_BlowjobTeacher_OBJ.points += 1
    $ hg_pr_BlowjobTeacher_OBJ.complete = True
    $ hg_pr_BlowjobTeacher_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return    
    
    
##(Level 08) (75 pt.) (FUCK A CLASSMATE). (Available during daytime only).
label hg_pr_SexWithClassmate: #LV.8 (Whoring = 21 - 23)

    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to fuck one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    
    if hg_pr_SexWithClassmate_OBJ.points == 0: # <================================================================================ FIRST TIME
        m "[hermione_name]..."
        m "Today I need you to have sex with a classmate of your choice."
        if whoring <=20 or hg_pr_BlowjobClassmate_OBJ.points <= 1:
            jump too_much
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("..............","body_47",xpos=140)
        call her_main("I had the feeling that we would get to this sooner or later...","body_66")
        call her_main("But...","body_69")
        her "..................."
        m "If you do this, \"Gryffindor\" will be getting seventy five points tonight."
        call her_main("Well, then I will do it, [genie_name].","body_79")
        m "Great. See you after your classes then."
        call her_main(".............","body_120")
    else: # <================================================================================ NOT FIRST TIME
        m "[hermione_name]..."
        m "I need you to go have sex with another classmate of yours."
        call her_main("Again, [genie_name]?","body_117",xpos=140)
        m "Yes. And you will get 75 points again as well."
        call her_main("Well, alright...","body_79")
    
    $ hg_pr_SexWithClassmate_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_SexWithClassmate_complete:
    # LEVEL 08+                
    if one_out_of_three == 1: ### EVENT (A)
        if fucked_ron_and_har:
            jump returns_next_morning
        else:
            $ fucked_ron_and_har = True #In public events. Have sex with a classmate. Event # 1. "Returns next morning". Turns True after that.
        m "....."
        m ".........."
        m "She was supposed to be here, by now..."
        m "Hm..."
        $ hg_pr_SexWithClassmate_OBJ.points += 1
        $ hg_pr_SexWithClassmate_OBJ.inProgress = False
        $ hermione_sleeping = True
        $ hg_pr_SexWithClassmate_AltFlag = True #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.
        return
        # NEXT MORNING
    
    elif one_out_of_three == 2: ### EVENT (B)
        call hg_pr_EnterRoom_block
        m "[hermione_name], did you complete your task?"
        show screen blktone
        with d3
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("Yes I did, [genie_name].","body_120",xpos=370)
        call her_main("And in the school library of all places...","body_186")
        her "At first I was kind of worried that we would make too much noise..."
        her "But the boy literally lasted only one minute, [genie_name]."
        m "Don't hold it against him, [hermione_name]."
        m "You are quite attractive, he probably got too excited..."
        call her_main("Nevertheless...","body_120")
        her "A dozen or so of rather gingerly thrusts and he is cumming already?"
        her "As a girl I cannot help but feel disappointed..."
        m "I see..."
        m "What did you do afterwards?"
        m "Pulled up your panties and went about your business as if nothing happened?"
        call her_main("My panties?","body_87")
        call her_main("I rarely bother to wear them anymore, [genie_name].","body_69")
        m "Oh really?"
        call her_main("Yes... I find not wearing any underwear very empowering.","body_79")
        m "Good for you, [hermione_name]."
    
    elif one_out_of_three == 3: ### EVENT (C)
        label returns_next_morning:
            pass
        call hg_pr_EnterRoom_block
        m "[hermione_name], did you complete your task?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        call her_main("I did, [genie_name].","body_120",xpos=370)
        call her_main("I took one of the \"Ravenclaw\" boys to the girl's restroom...","body_124")
        her "...and let him have his way with me in one of the stalls."
        m "Well done, [hermione_name]."
        call her_main(".....................","body_69")
        m "I said you did great. What's the matter?"
        call her_main("Ehm... well...","body_189")
        her "I am getting paid well for performing such tasks..."
        her "So I have no right to complain, but..."
        m "Hm...?"
        call her_main("My reputation is starting to suffer and it troubles me, [genie_name]...","body_183")
        m "Your reputation?"
        call her_main("Well, yes... ehm...","body_189")
        m ".............."
        call her_main("No, sorry, please disregard what I just said, [genie_name].","body_120")
        m "Hm..."
    
    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return
    
label hg_pr_SexWithClassmate_Alt: #Hermione does not show up. This is label where she shows up next morning.
    $ hg_pr_SexWithClassmate_AltFlag = False #Turns True when hermione fails to show up after her "Fuck a classmate" favour. Runs an event next morning.
    call hg_pr_EnterRoom_block
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    m "[hermione_name], you missed your debriefing yesterday."
    call her_main("Yes, [genie_name], I apologize... *yawn*...","body_16",xpos=370)
    m "Care to explain yourself?"
    call her_main("Of course, [genie_name].","body_190")
    call her_main("It is sort of embarrassing, though...","body_188")
    call her_main("I spent the last night with two of my friends...","body_190")
    m "A slumber party with some girlfriends, huh?"
    call her_main("Girlfriends?","body_122")
    call her_main("No, [genie_name]. Harry and Ron are boys...","body_189")
    m "Hm..."
    call her_main("Yes, we were best friends for such a long time...","body_188")
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    call her_main("But last night the boys made me their little plaything...","body_128")
    call her_main("And I did not mind it one bit...","body_123")
    her "They did everything they wanted to do to me..."
    her "And everything I wanted to be done to me has been done..."
    call her_main(".................","body_121")
    call her_main("Will I get paid for this, [genie_name]?","body_122")
    
    $ gryffindor += 75 #75
    m "\"Gryffindor\" gets 75 points!"
    her "Thank you, [genie_name]."
    
    $ hg_pr_SexWithClassmate_OBJ.points += 1
    $ hg_pr_SexWithClassmate_OBJ.complete = True
    $ hg_pr_SexWithClassmate_OBJ.inProgress = False
    
    call hg_pr_transition_block
    return
    
    

##(Level ??) (?? pt.) (Sex with teacher). (Available during daytime only).
label hg_pr_SexWithTeacher:# "teacher sex" (Level 09)
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to have sex with one of her teachers?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
            
    if whoring < 20:
        jump too_much
    else:
        m "Today's favour shall be..."
        call her_main(".........","body_117",xpos=140)
        m "To have sex with Professor Snape!"
        call her_main("Can i really?","body_48")
        call her_main("Ehm...","body_127")
        her "I don't mind, sir."
        m "Really?"
        call her_main("Yes... I mean, it's just sex, you've already partaken in that favour of me several times, I might even be a little eager for this...","body_68")
        ">Perhaps this has gone too far?"
        ">Nah..."
        m "Excellent i expect a very detailed report this evening."
        call her_main("Of course, sir.","body_74")
    
    $ hg_pr_SexWithTeacher_OBJ.inProgress = True
    
    call hg_pr_transition_block
    jump day_main_menu
    
label hg_pr_SexWithTeacher_complete:
    call hg_pr_EnterRoom_block
    
    call her_main("Good evening, sir...","body_01",xpos=370,ypos=0)
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    m "You're a bit late this evening."
    show screen blktone
    with d3
    call her_main("I know Sir, I'm incredibly sorry.","body_118")
    call her_main("But you can rest assure I've come straight from completing your task Sir.","body_122")
    m "Just now?"
    m "It's just past supper.  Why did you not take care of it during the day?"
    call her_main("Sir, it's not like I can simply take time during the middle of the day to bend over for Professor Snape.","body_124")
    call her_main("I must continue to go to my classes and recieve my education.","body_127")
    her "There just isn't much time."
    her "Let me explain to you how it went."
    hide screen blktone
    show screen snape_sex
    with d5
    her "Just before lunch today I saw Professor Snape and offered to let him shag me senseless."
    call her_main("We'll just say Professor Snape was all too eager to \"shove his thick cock in my pussy\"","body_128")
    ">No surprise there."
    her "But neither of us could really get started right then and there.  He told me he'd catch up with me this evening."
    call her_main("I didn't know he meant to catch me out in the halls after supper.","body_124")
    call her_main("Needless to say I was not ready for him, so I quickly gave him one of the sloppiest blowjobs I've managed yet.","body_127")
    call her_main("He was so slick and hard between my lips, I could have kept going if not for needing to have him fuck me just like you wanted.","body_123")
    call her_main("And that's it...","body_118")
    m "Hmmm. I'm certain that's false, didn't you say something about the halls?"
    call her_main("Oh, No!","body_119")
    m "Spill slut."
    call her_main("Fine.","body_79")
    call her_main("Professor Snape did catch me in the corridors yes.","body_47")
    call her_main("That's where I sucked his cock.","body_118")
    her "That's where he vanished my skirt."
    call her_main("That's where he pulled up my shirt and displayed my tits.","body_140")
    call her_main("That's where he conjured panties on me to keep my knees together and \"his cunt\" nice and tight.","body_142")
    call her_main("That's where he came so much in \"his cunt\"....","body_145")
    call her_main("it spurted his thick cum out as it came blindingly hard all around that cock.","body_146")
    hide screen snape_sex
    with d5
    show screen blktone
    call her_main("I think I needed another two in my mouth and ass for the perfect moment.","body_152")
    her "Three thick cocks spreading my hot little holes...yeah...perfect."
    m "My god girl, are you quite alright?"
    call her_main("God yes, that was one of the hottest things I've ever experienced.","body_153")
    m "Then why are you crying?"
    her "Tears of joy Sir."
    m "Woah, child it's just sex."
    call her_main("I hope one day you can use me like that with everyone around.","body_155")
    her "The risk of being seen is such a huge turn on for me."
    m "I see.  I will most certainly consider that option in the future between us."
    m "Now please clean yourself up, you look like an unsightly whore."
    her "Yes Sir."
    call her_main("I hope I've completely satisfied you [genie_name].","body_01")
    m "That miss Granger, was an experience."
    ">Hermione rubs her legs together subtly."
    her "[genie_name] if I could get my points and be excused, I would love to get back to my dorm."
    
    $ gryffindor +=80
    m "Eighty points to \"Gryffindor\" miss Granger. Well deserved." 
    her "Thank you, sir..."
    m "You can go now."
    her "Good night, sir."
    m "Yes, good night..."
    
    $ hg_pr_SexWithTeacher_OBJ.points += 1
    $ hg_pr_SexWithTeacher_OBJ.complete = True
    $ hg_pr_SexWithTeacher_OBJ.inProgress = False
    
    
    call hg_pr_transition_block
    return
    
    
    
    
label hg_pr_transition_block:
    hide screen bld1
    hide screen hermione_main
    hide screen blktone
    hide screen hermione_blink
    hide screen ctc
    with d3
    
    call her_walk(400,610,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    return
    
label hg_pr_EnterRoom_block:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(520,400,2)
    show screen hermione_blink #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    show screen hermione_blink
    with d3
    return
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(520,400,2)
    show screen hermione_blink
    show screen bld1
    with d3
    pause.5
    
    
