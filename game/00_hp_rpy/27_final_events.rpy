label want_to_rule:
    
    $ event_chairman_happened = True #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
   
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    #her "Professor Dumbledore?"
    her "[genie_name]?"
    m "Miss Granger, how can I help you?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Sir, have you made your decision yet on who will be in charge of the \"ABOC\" this year?"
    m "\"ABOC\"?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "The \"Autumn Ball Organization Committee\", sir..."
    m "Ehm... Sure..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Please excuse me if I am being too direct with this, sir..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "But I think you should put me in charge."
    her "I did it last year and it was the best organized \"autumn ball\" Hogwarts has had in years."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "You said so yourself, sir. Do you remember?"
    m "Right, of course..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "So, is this a yes?"
    her "Does this mean I will be in charge again this year?"
    menu:
        m "..."
        "\"You shall be in charge, miss Granger.\"":
            jump one_thing
        "\"No. Professor Snape shall be in charge!\"":
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Professor Snape, sir?"
            her "But, traditionally organizing and hosting the ball is the responsibility of the students..."
            her "Teachers are only present as the guests of honour..."
            m "Well of course... I was just kidding."
            m "You shall be in charge, miss Granger..."
            label one_thing:
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
            her "Thank you, sir."
            m "There is one condition, though..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "A conditions, sir?"
            
            $ d_flag_04 = False
            label no_sleeping_with_professor:
                pass
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            menu:  
                m "..."
                "\"Show me your tits first.\"":
                    $ mad += 9
                    $ d_flag_01 = True
                    pass
                "\"Show me your pussy first.\"":
                    $ mad += 9
                    $ d_flag_02 = True
                    pass
                "\"Strip naked for me first.\"":
                    $ mad += 17
                    $ d_flag_03 = True
                    pass
                "\"You will have to sleep with me.\"" if not d_flag_04:
                    $ mad += 17
                    $ d_flag_04 = True
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I will have to... sleep...?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "..................."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "I am not stupid, sir... Quite the opposite in fact."
                    her "And I understand that the nature of the favours I have been selling you lately..."
                    her "...Might have led you to believe that I would be willing to..."
                    her "...To let you have your way with me eventually, sir..."
                    m "Wha-a-a...? I would never--"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Please, let me finish, sir."
                    m "Right..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I know that you are a rather wise man yourself, sir."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "So, please... understand this..."
                    her "I may be willing to sacrifice my pride and even my dignity for the sake of my house..."
                    her "But sleeping with my headmaster?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "That is where I draw the line, sir."
                    m "Got it. Let's just forget I said anything."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_141.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "{size=-5}(I wish I could...){/size}"
                    jump no_sleeping_with_professor
    
                    
                    
                    
       
                "\"Never mind. the Position is yours.\"":
                    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3         
                    show screen blkfade 
                    with d5
                    pause.7
                    pass
    

            if d_flag_01 or d_flag_02 or d_flag_03:
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "What?!"
                m "What?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                #her "Professor!"
                her "[genie_name]!"
                m "What?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "You are abusing your power, sir. Again!"
                m "Seriously? After all those favours you sold me?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Those were for the sake of my house, sir."
                m "Well this one is for the sake of the \"Autumn prom\"."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "It's the \"Autumn Ball\", sir..."
                m "Oh, come on..."
                m "Entrusting the thing to somebody else would be a crime, you know that."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her ".........."
                m "Don't you care about your classmates at all?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "What?"
                m "Put your selfishness aside for once, would you?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "My... selfishness?"
                m "Your classmates deserve the best organized ball possible!"
                m "And only {size=+5}YOU{/size} can give them that!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "...that is true actually."
                m "People depend on you, girl!"
                if d_flag_01:
                    m "So I suggest that you stop being selfish and show me your tits!"
                elif d_flag_02:
                    m "So I suggest that you stop being selfish and show me your pussy!"
                elif d_flag_03:
                    m "So I suggest that you stop being selfish and get naked for me!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                #her "You are completely right, professor!"
                her "You are completely right, [genie_name]!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "I must do this. Everyone depends on me."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Just give me a second please..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d5   
                m "............"
                if d_flag_01: # SHOW ME TITS
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    hide screen blkfade
                    with d3
                    hide screen bld1
                    with d3
                    hide screen hermione_main
                    with d5
                    $ menu_x = 0.5 #Default menu position restored.
                    show screen ctc
                    pause.3
                    show screen hermione_04
                    with fade
                    pause
                    show screen bld1
                    with d3
                    
                    $ badges = False
                    
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    show screen ctc
                    pause
                    hide screen ctc
                    m "Very good miss Granger..."
                    m "Your ample tits are always a welcome sight..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "...................."
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d5   
                    show screen blkfade 
                    with d5
                    pause.7
                elif d_flag_02: # SHOW ME PUSSY
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    $ only_upper = True
                    
                    hide screen blkfade
                    with d3
                    hide screen bld1
                    with d3
                    hide screen hermione_main
                    with d5
                    $ menu_x = 0.5 #Default menu position restored.
                    show screen ctc
                    pause
                    show screen hermione_03
                    with fade
                    pause
                    show screen bld1
                    with d3
            
                    $ uni_sperm = True
                    $ u_sperm = "01_hp/13_hermione_main/panties.png" #Panties
            
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_60.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    
                    show screen ctc
                    pause
                    hide screen ctc
                    
                    her ".............................."
                    with hpunch
                    g4 "What are you doing, girl?!"
                    g4 "I am your headmaster! Do you have no shame?!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/191.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "What?! But--"
                    g9 "He-he... Relax, girl. I'm just kidding."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_62.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    #her "Professor, that was just mean."
                    her "[genie_name], that was just mean."
                    g9 "He-he..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_61.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "....................................."
                    m "I do like your shaved little pussy though..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_61.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her ".....thank you, sir."
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3         
                    show screen blkfade 
                    with d5
                    pause.7
                    $ uni_sperm = False
                
                elif d_flag_03: # STRIP NAKED
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    # (Hermione locks the door).
                    hide screen bld1
                    with d3
                    pause.3
                    #Walks to the door
                    
                    $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01_f 
                    pause 2
                    hide screen hermione_walk_01_f 
                    $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    show screen hermione_01_f
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = im.Flip("01_hp/animation/h_walk_03.png", horizontal=True)
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = im.Flip("01_hp/animation/h_walk_01.png", horizontal=True)
                    show screen ctc
                    pause
                    m "??!"
                    hide screen h_c_u
                    hide screen ctc
                    $ walk_xpos=650 #Animation of walking chibi. (From)
                    $ walk_xpos2=400 #Coordinates of it's movement. (To)
                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01 
                    pause 3
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    show screen hermione_02 #Hermione stands still.
                    show screen bld1
                    with Dissolve(.3)
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ h_ypos=0
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    her "Just in case..."
                    show screen ctc
                    pause
                    hide screen ctc
                    show screen blkfade
                    with d5
                    m ".........................."
                    ">Hermione is taking her clothes off, one piece after another..."
                    ">Vest, shirt, her skirt and finally... the panties."
                    
                    #$ only_upper = True
                    
                    
                    hide screen hermione_main
                    $ badges = False # Turns off badges layer.
                    $ wear_shirts = False
                    $ wear_skirts = False
                    
                    $ hermione_chibi_xpos = 310 # Default 360
                    #$ hermione_chibi_ypos = 210
                    $  h_c_u_pic = "01_hp/08_animation_02/01.png" #Hermione naked. 
                    show screen h_c_u 
                    
                    hide screen blkfade
                    with d7
                    show screen ctc
                    pause
                    hide screen ctc
                    
                    
                    #add h_c_u_pic at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
                    g9 "Ni-i-i-ce!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_105.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    show screen ctc
                    pause
                    hide screen ctc
                    her "*Sob!*"
                    m "Huh?"
                    
                    $ h_tears = True
                    $  u_tears_pic = "01_hp/13_hermione_main/tears_01.png"
                    
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_107.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Oh, please, don't mind me, sir."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_105.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Just enjoy the... {w}the... {w}the view..."
                    m "Are you... crying?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_97.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Sob!* No, not really, sir... *sob!*..."
                    her "It is just that I am standing here before my headmaster completely naked... *SOB!*"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_114.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "These are the tears of shame, sir."
                    her "I can't help it! *Sob!*"
                    m "Are you sure that you are ok with this?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $  u_tears_pic = "01_hp/13_hermione_main/tears_04.png"
                    $ h_body = "01_hp/13_hermione_main/body_101.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Yes, yes, sir, please.... *Sob!*"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_104.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Please keep on looking at my naked body... *Sob!*"
                    g4 "(What the...?)"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_191.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Sir, I am begging you!"
                    m "Kind of sounds like an order--"       
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_192.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I need it!"
                    her "...I need to shamelessly present my naked body before you like this!"
                    m ".............?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_193.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I need to feel this embarrassment and humiliation! *SOB!*"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_194.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "The fate of the \"Autumn ball\" depends on this..."
                    her "So, sir, please..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_195.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Keep looking at my naked breasts, and my pussy..."
                    show screen ctc
                    pause
                    hide screen ctc
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_196.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Yes! Make my skin burn with shame, sir... *Sob!*"
                    m "Ehm... right... Ok..."
                    m "Listen, I think this will do..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_191.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Are you sure, sir?"
                    her "Are you sure that you humiliated me enough, sir?"
                    m "...................."
                    m "(Is she getting off on this? Is she being sarcastic? I don't get it...)"
                    her ".........................."
                    show screen ctc
                    pause
                    hide screen ctc
                    m "Just put your clothes back on, Miss Granger. You're making me feel uncomfortable."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_103.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "As you wish, sir..."
                    
                    show screen ctc
                    pause 
                    hide screen ctc
                    
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    
                    show screen ctc
                    pause 
                    hide screen ctc
                    
                    $  u_tears_pic = "01_hp/13_hermione_main/tears_03.png"
                    show screen blkfade 
                    with d5
                    pause.7
                
                    
                    
                    
                    
                    
                             
                        
                    
                    
                    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.             
                    
    $ hermione_chibi_xpos = 360 # Default 360
    show screen hermione_02 #Hermione stands still.
    hide screen blkfade
    with d5
    
    $ badges = True
    $ wear_shirts = True
    $ wear_skirts = True
    
    show screen ctc
    pause 
    hide screen ctc
    show screen bld1
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "So I am officially in charge of this year's \"Autumn Ball Organization Committee\" now?"
    m "That you are."
    her "Thank you sir! You will not regret this, I promise!"
    m "{size=-4}(Why would I?){/size}"
    m "{size=-4}(I couldn't care less about the whole thing...){/size}"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Well, I'd better go now. I have so many arrangements to make!"
    m "By all means, Miss Granger. Have a nice day."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3 
    
    hide screen bld1


    hide screen hermione_02


    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    pause.2
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    pause.5
    show screen bld1
    with d3
    m "........................................"
    m "A ball, huh?"
    m "I wonder if I will have to show up for that..."
    hide screen bld1
    with d3
    $ hermione_takes_classes = True
    $ days_without_an_event = 0

    $ h_tears = False
    
    call music_block
    
    return
    
#==========================
    
label against_the_rule:
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    $ snape_against_chairman_hap = True # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    $ days_without_an_event = 0
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To)
    show screen snape_walk_01 
    with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "01_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.3)
    
    
                
    sna "Are you bloody insane?!"
    m "You know, sometimes I think I may be..."
    
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ tt_xpos=120 #Defines position of the Snape's full length sprite. Right - 300                      #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                               #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "You appointed the girl as the head of the \"Autumn Ball Organization Committee\"?!!"
    m "I'm guessing that's bad?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_10.png"                                                               #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Bad?{w} {size=+5}BAD?!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_15.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "{size=+5}That's a catastrophe!{/size}"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_16.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "last year's ball was completely horrible!"
    m "Was it? I heard differently..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_10.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Oh really? And who told you that?"
    m "not a very reliable source apparently..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_08.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Dammit... Dammit all to hell..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_07.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "I had big plans for the thing..."
    m "Really? Like what?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Oh, that doesn't matter now..."
    #sna "The girl is a complete control freak..."
    sna "Now the girl will use prefects or the ghosts to keep an eye on me throughout entire thing..."
    m "Right, that reminds me..."
#    hide screen snape_main                                                                                                                   #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                              #SNAPE
#    show screen snape_main                                                                                                                 #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    sna "Huh?"
    m "Am I supposed to show up as well?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Show up?"
    sna "You are expected to host the bloody thing!"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "But don't you worry! I'll figure something out!"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Hm... I'll Probably have to host the ball instead..."
    m "............"
#    sna ".................."
#    hide screen snape_main                                                                                                                   #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                              #SNAPE
#    show screen snape_main                                                                                                                 #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    sna "Yes! I will do it!"
#    sna "And I shall be on my best behavior!"
#    hide screen snape_main                                                                                                                   #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                              #SNAPE
#    show screen snape_main                                                                                                                 #SNAPE
#    with d3                                                                                                                                                  #SNAPE
#    sna "Yes, that'll show her!"
#    m "................"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Well, the Autumn ball is about to happen and Hermione Granger is in charge..."
    sna "There is no changing it now..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Sorry for the outburst..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_16.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "That girl brings out the worst in me..."
    m "Don't sweat it..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "You know what...?"
    sna "I don't feel like working today..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Do we still have any of Dumbledore's wine left?"
    m "I believe so..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Great! Pour me some..."
    m "Seriously? You're just gonna bail on your class like that?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Yeah, big news - I hate my job."
    sna "And since you are my boss..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "I don't know why I even bother teaching those so-called students..."
    m "To maintain the charade?"
    m "for the Same reason why I never leave this room...?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Right..."
    sna "But you know what else could endanger out little enterprise?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_07.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Me losing it during class and strangling a couple of \"Gryffindor\" maggots with my bare hands..."
    m "Hm... I see your point..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                              #SNAPE
    show screen snape_main                                                                                                                 #SNAPE
    with d3                                                                                                                                                  #SNAPE
    sna "Seriously, man... I need a drink..."

    show screen blkfade
    with d3
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    show screen fireplace_fire
    hide screen genie
    hide screen chair
    hide screen desk
    show screen desk
    
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    hide screen snape_main
    with d3

    
    hide screen blkfade
    with d3
    $ fire_in_fireplace = True
    
    show screen bld1
    with d3
    "Professor Snape spends the day in your chamber, drinking the stress away."
    
    if not sfmax:# Turns TRUE when friendship with Snape been maxed out.
        ">Your relationship with him has improved."
        $ snape_friendship +=1
   
    show screen blkfade
    with d3
    hide screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    hide screen fireplace_fire
    show screen genie
    show screen chair
    show screen desk
    hide screen desk
    
    hide screen bld1

    stop bg_sounds #Stops playing the fire SFX.
   
    jump night_start
         
#    hide screen snape_main
#    hide screen bld1
#    with d3
    
#    $ walk_xpos=360 #Animation of walking chibi. (From desk) 360
#    $ walk_xpos2=610 #Coordinates of it's movement. (To the door) 610
    
#    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
#    show screen snape_walk_01_f 
#    pause 3
#    hide screen snape_walk_01_f 
#    show screen snape_01_f #Snape stands still. (Mirrored).
#    pause.2
#    who2 "................."
#    who2 "One more thing..."
#    show screen bld1
#    show screen snape_main
#    with Dissolve(.3)
#    who2 "You must dismiss any lies you hear about me and those slytherin girls..."
#    m "You got it!"
#    hide screen bld1
#    hide screen snape_main
#    hide screen snape_01_f #Snape stands still. (Mirrored).
#    with Dissolve(.3)
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

#    return
    
#============================

label crying_about_dress:
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    her "My parents sent me the wrong dress!"
    m "are You kidding me!?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "They sent me the dress I wore to the ball last year..."
    m "Those inconsiderate bastards!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_67.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Are you making fun of me sir?"
    m "Can you blame me?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I will become the laughingstock of Hogwarts! *Sob!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "My reputation is as good as ruined! *Sob!*"
    m "Seriously? After all the favours you sold me you care about a thing like this?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Wearing the same dress to the \"Autumn Ball\" for two years in a row would be more humiliating than any favour I sold you so far, sir."
    with hpunch
    g4 "You've gotta be kidding me..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Oh, you wouldn't understand..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_148.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "You're just like my father!"
    m "I beg your pardon?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_144.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I mean... ehm..."
    her "Forgive me sir..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I don't know why I am telling you all of this..."
    m "................"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "......................*sob!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I think I'd better go now...*sob*"
    m "Well, don't let me keep you a moment longer, miss Granger...."
    # Walks to the door.
    
 
    

    
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    

    $ hermione_chibi_xpos = 610 # Stands near the door.
    show screen hermione_01_f #Hermione stands still.
    pause.3
    $ h_body = "01_hp/13_hermione_main/body_145.png"                                                                                                                                                         # HERMIONE HEAD
    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390                                # HERMIONE HEAD
    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.       # HERMIONE HEAD
    show screen bld1
    with d3
    show screen h_head2                                                                                                                                                                                                                    # HERMIONE HEAD         
    her "(My life is ruined...)"
    hide screen h_head2       
    hide screen hermione_01_f #Hermione stands still.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
   
    
    pause.5
    m "Hm... I don't remember ever seeing the girl this desperate..."
    m "And that says a lot, all things considered..."
    m "I suppose whoring herself out for house points is a significantly smaller problem than not having a proper prom dress..."
    m ".............."
    m "Schoolgirls..."
       
    hide screen bld1
    with d3
    
    $ hermione_takes_classes = True
    
    call music_block
    
    return 
    
#===========================
label sorry_about_hesterics:
    $ sorry_for_hesterics = True # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    $ days_without_an_event = 0
    
    $ have_no_dress_hap = True #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    $ days_without_an_event = 0
    
    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    
    m "Miss Granger?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Sorry to disturb you sir..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I came to apologize for my..."
    her "...my hysterical behaviour yesterday."
    m "Sure thing, don't worry about it."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, sir."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Still, I cannot help but feel awful for causing a scene..."
    m "So the issue has been resolved then?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Not really..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Not at all actually..."
    m "Hm..?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "But that is not a big deal..."
    her "I'm just overreacting..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    her "I woN't be able to attend the ball this year... so what?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I spent countless hours with organizing the event..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE

    $ h_tears = True
    $  u_tears_pic = "01_hp/13_hermione_main/tears_01.png"
    $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I worked so hard... and..."
    
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_tears = False
    $ h_body = "01_hp/13_hermione_main/body_139.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "And now I will not even be able to... to... *Sob!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "To... *SOB!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Excuse me sir!"
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    
    $ walk_xpos=370 #Animation of walking chibi. (From) 300
    $ walk_xpos2=750 #Coordinates of it's movement. (To) 610
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen. 0.02
    hide screen no_groping_02
    hide screen bld1
    show screen genie
    show screen hermione_run
    #with fade
    pause 1.3 # .9
    hide screen hermione_run
    with Dissolve(.1)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    pause.5
    
    show screen bld1
    with d3
    
    m "......................................."
    m "Hm..."
    $ hermione_takes_classes = True
    hide screen bld1
    with d3
    
    call music_block
    
    return
    
    
#=========================
label giving_thre_dress:
    $ gave_the_dress = True #Turns True when Hermione has the dress.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    stop music fadeout 1.0
    m "Here... This is for you..."
    $ the_gift = "01_hp/18_store/01.png" # DRESS.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">You give the ball gown to Hermione..."
    hide screen gift
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Hm...? What is this?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    with hpunch
    her "{size=+7}A DRESS?!{/size}"
    m "I thought that you--"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    #her "PROFESSOR!"
    her "[genie_name]!"
    g4 "What? What happened? Don't tell me it's the wrong color or something!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "It's perfect, sir...*sob!*"
    her "It's perfect... *sob!* ...I love it."
    m "You sure don't look like it..."
    her "I am sorry, sir... *Sob!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I... I am just..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I am so happy..."
    her "Thank you, sir. Thank you so much."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I cannot believe that you would do something like that for me..."
    m "Well, I did. Now stop crying."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_147.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I can't, sir. I am so happy and so grateful..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_144.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Do you want me to suck your cock, sir?"
    m "What?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_144.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Because I will do it!"
    her "And I will swallow and everything!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "And you wouldn't have to pay me a single house point!"
    m "uhm... Maybe some other time..."
    m "This is not the type of crying I find arousing..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I'm sorry, sir. I'm such a mess..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "But this is so unexpected..."
    her "You made me so happy, sir...*sob!*"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you sir! *SOB!* Thank you! *SOB!*"
    m "Well... err... there, there..."
    m "Better stop crying before you stain that new dress of yours with those tears..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_147.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "My new dress! *SOB!*"
    m "Alright, you know what? Just get out of my office."
    m "Just take your dress and leave."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Of course... I am sorry, sir!"
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3          
    
    
    
    
    
    
    
    
  
   
   
   
   
   

    
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3






    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.8
    show screen bld1
    with d3
    m "......................"
    m "Women..."
    hide screen bld1
    with d3

    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
    
    
    
###======================================================================
    
    
label good_bye_snape:

    $ days_without_an_event = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ walk_xpos=470 #Animation of walking chibi. (From)
    $ walk_xpos2=360 #Coordinates of it's movement. (To) 360
    show screen snape_walk_01 
    #with d3
    pause 1.5
    show screen snape_02 #Snape stands still.
    show screen bld1
    with Dissolve(.3)
    $ tt_xpos=300 #Defines position of the Snape's full length sprite.
    $ tt_ypos=0
    $ s_sprite = "01_hp/10_snape_main/snape_01.png"
    show screen snape_main
    with Dissolve(.1)
    

    sna "Genie..."
    m "Severus?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ tt_xpos=120 #Defines position of the Snape's full length sprite. Right - 300                      #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                               #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
#    sna "The \"Autumn Ball\" is tonight..."
#    m "Is it...?"
#    sna "....................."
#    m ".....?"
    sna "I think I may have figured out why your magic does not work the way it should..."
    g4 "Seriously?!"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Yes..."
    sna "It's quite obvious actually... I'm surprised that it didn't cross my mind before."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "You see, the thing is that every building in \"Hogwarts\" is enchanted with all kinds of protection spells..."
    m "Protection spells, huh?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Yes..."
    sna "Very powerful, old and nasty magic..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Even the land itself is heavily enchanted for kilometers in every direction..."
    m "Hm..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Basically, any number of spells could be interfering with your powers around here..."
    m "Wait, then how come that you have no problems with casting your spells?"
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "My magic is \"Hogwarts\" magic, friend..."
    sna "But I bet your powers are alien enough to be perceived as a threat."
    m "Interesting..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "I think if you manage to get far enough from the school grounds..."
    m "I will be able to go home... finally..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "Yes, and the best time to do that would be tonight..."
    hide screen snape_main                                                                                                                   #SNAPE
    with d3                                                                                                                                                  #SNAPE
    $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
    show screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    sna "While everyone is preoccupied with that bloody \"Autumn ball\" you could sneak out unnoticed..."
    
    hide screen snape_main                                                                                                                  #SNAPE
    with d3                                                                                                                                                   #SNAPE
    
    show screen blkfade
    with d5
    hide screen genie
    hide screen bld1
    hide screen snape_02 #Snape stands still.
    show screen chair_02
    show screen g_c_u
    $ genie_chibi_xpos = 80
    $ genie_chibi_ypos = 205
    $ g_c_u_pic = "01_hp/05_props/hand_00.png"
    play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 # EPIC THEME.
    pause 1
    m "Right, tonight is the night of the \"Autumn ball\"..."
    m "So it ends tonight then..."
    $ s_head_xpos = 330 # x = 330,
    $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
    $ s_sprite = "01_hp/10_snape_main/snape_09.png"
    show screen s_head2
    sna_[17] "Seems like it..."
    hide screen s_head2
    hide screen blkfade 
    with d3
    pause.5

    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
    sna "In case I'm right and will never see you again..."
    hide screen s_head2
    m "Right..."
    show screen blkfade
    with d3
    $ g_c_u_pic = "01_hp/05_props/hand_01.png"
    hide screen blkfade
    with d3
    pause 2
    show screen bld1
    with d3
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_26.png"
    sna2 "The past several month were the best months of my life, Genie..."
    sna2 "Thank you for that, you incredible traveler from another world..."
    sna "Thank you, my friend..."
    hide screen s_head2
    m "I don't know what to say, Severus..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"
    sna "Then don't say anything..."
    sna2 "Just move on to your next adventure..."
    sna "Our world has stalled you long enough..."
    hide screen s_head2
    m "Thank you for keeping me company and being my only friend here, Severus."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_27.png"
    sna "Thank you for being mine..." #TEARS?
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"
    sna "I'd better go now..."
    #Goes to the door, stops and turns around.
    
    hide screen s_head2
    show screen blkfade
    with d5
    show screen genie
    hide screen bld1
    hide screen chair_02
    hide screen g_c_u

    pause.5
    # SNAPE LEAVES
    
    hide screen ctc
    
    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    hide screen blkfade 
    with d3
    pause 3
    
    hide screen snape_walk_01_f 


    show screen snape_01_f #Snape stands still near the door. (Mirrored).
    pause.5
    show screen snape_01#Snape stands still.
    
    
    
    
    
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d5
    
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_01.png"
    sna "One more thing though..."
    hide screen s_head2
    m "Yes?"
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/24.png"
    sna "If it all goes well..."
    sna2 "Will I find the real Albus Dumbledore in that chair tomorrow?"
    hide screen s_head2
    m "I believe so..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_04.png"
    sna "Hm..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
    sna2 "Albus can't know that I was aware of his absence..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_01.png"
    sna "Is there a way to tell you guys apart?"
    hide screen s_head2
    m ".............."
    m "How about a secret password?"
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
    sna "A password?"
    hide screen s_head2
    m "Yes... just ask me tomorrow: \"Who rules?\"."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_01.png"
    sna "\"Who rules?\""
    hide screen s_head2
    g9 "\"Akabur rules!\""
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
    sna "Akuba... ehm... What does it mean?"
    hide screen s_head2
    m "Just a phrase that you will only be able to hear from the real me..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_02.png"
    sna "I understand..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"
    sna "Alright then..."
    sna "Have a save trip home..."
    hide screen s_head2
    m "Thank you. Have fun with hosting the ball..."
    show screen s_head2
    $ s_sprite = "01_hp/10_snape_main/snape_06.png"
    sna "*Sigh*"
    hide screen s_head2
    pause.3
    hide screen bld1
    with d3
    pause.3
    
    stop music fadeout 1.0

    show screen snape_01_f#Snape stands still.

    pause.5
    hide screen snape_01#Snape stands still.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_01_f#Snape stands still.
    
    pause 1
    show screen ctc
    pause
    hide screen ctc
    
    
    
    m "............................"
    m "So this is it then...?"
    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
    m "Seems like my time in this world has come to an end..."
    m "......................."
    if not public_whore_ending: #YOUR PERSONAL WHORE ENDING. WRITING A LETTER.
        m "That Means I'll probably never see the girl again..."
        m "..........."
        m "When I first met her she was so annoying..."
        m "to be honest, all the training I put her through changed very little in that regard..."
        m "But we did have a few special moments together..."
        m ".............."
        m "......................"
        m "I doesn't feel right to leave her without saying goodbye properly..."
        m "And yet I don't want to miss my chance to sneak out unnoticed..."
        m "I don't like long goodbyes..."
        m "Hm..."
        m "I suppose I could leave her a note or something..."
        
        m "Let's see..."
        show screen bld1
        with d3
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "\"Dear...\""
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "Hm... How shoud I adress her?"
        menu:
            m "Dear..."
            "\"Miss Granger\"":
                 $ word_01 = "Hermione Granger" 
            "\"Nasty whore\"":
                $ word_01 = "nasty whore"
            "\"Slut\"":
                $ word_01 = "slut"
            "\"Cumbucket\"":
                $ word_01 = "cumbucket"
            "\"Human female\"":
                $ word_01 = "human female"
            "\"friend\"":
                $ word_01 = "friend"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Yes, \"Dear [word_01]\" fits perfectly..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        m "\"...it is time for me to go back...\""
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "What should I write now?"
        menu:
            m "...time to go back..."
            "\"home\"":
                $ word_02 = "home"
            "\"to the mothership\"":
                $ word_02 = "to the mothership"
            "\"to Dimension \"X\"":
                $ word_02 = "to Dimension \"X\""
            "\"to my world\"":
                $ word_02 = "to my world"
            "\"To my Home Planet - Krypton\"":
                $ word_02 = "to my Home Planet - Krypton"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Yes, \"Time to go back [word_02]\" that will do..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        m "\"...farewell my little...\""
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "What should I write now?"
        menu:
            m "...farewell my little... "
            "\"cock-hungry slut\"":
                $ word_03 = "cock-hungry slut"
            "\"cum receptacle\"":
                $ word_03 = "cum receptacle"
            "\"Girl\"":
                $ word_03 = "girl"
            "\"Witch\"":
                $ word_03 = "witch"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Yes, \"farewell my little [word_03]\" sounds about right..."
        ">scribble-scribble-scribble..."
        ">scribble-scribble-scribble..."
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "And now to sign it as..."
        label stupid_kent:
            pass
        menu:
            m "..."
            "\"Genie\"":
                $ word_04 = "Genie"
            "\"Clark Kent\"":
                $ word_04 = "Clark Kent"
                hide screen genie
                show screen paperwork
                with Dissolve(0.3)
                m "Yes, \"sincerely yours, [word_04]\"..."
                show screen genie
                hide screen paperwork
                with Dissolve(0.3)
                m "..........."
                m "No, that doesn't make any sense..."
                jump stupid_kent
            "\"Lord Voldemort\"":
                $ word_04 = "Lord Voldemort"
            "\"Traveler\"":
                $ word_04 = "Traveler"
        hide screen genie
        show screen paperwork
        with Dissolve(0.3)
        m "Yes, \"[word_04]\"..."
        show screen genie
        hide screen paperwork
        with Dissolve(0.3)
        m "........................"
        m "Yes, this should do..."
    hide screen bld1
    with d3
    m "Well, off I go then..."
    
    show screen blkfade
    with d5

    $ g_c_u_pic = "01_hp/05_props/walk_01.png"
    $ genie_chibi_xpos = 270
    $genie_chibi_ypos = 260
    hide screen genie
    show screen chair_02
    hide screen desk
    show screen desk
    show screen g_c_u
    pause.5
    hide screen blkfade
    with d5
    
    
    
    m "........."
        
    

    

    $ walk_xpos=270 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    hide screen g_c_u
    show screen genie_walk
    hide screen blkfade 
    pause 3
    
    hide screen genie_walk


    $ genie_chibi_xpos = 610
    show screen g_c_u
    pause 1
    m "...................."
    m "Agrabah... here I come..."
    
    show screen ctc
    pause
    hide screen ctc
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen g_c_u
    pause.3
    show screen ctc
    pause
    hide screen ctc
    ">.......................{w}............................{w}.....................{w}......................"
    pause.7
    show screen blkfade
    with d7
    pause 1
    
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    $ end_u_1_pic =  "01_hp/17_ending/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    hide screen blkfade 
    with d7
    
    show screen ctc
    pause
    hide screen ctc
    

    
    m "Severus was right..."
    pause.5
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRASS.
    $ end_u_3_pic =  "01_hp/17_ending/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    
    
    m "The farther away I get from the school grounds..."
    m "The more powerful I'm starting to feel..."
    
    $ end_u_4_pic =  "01_hp/17_ending/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    m "I think  this is far enough..."
    m "Time to undo the spell and go back home..."
    m ".........."
    m "...................."
    m "Agrabah, here I come..."
    if not persistent.game_complete: # FIRST PLAYTHOURGH. 
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        with d9
        pause .5
        
        play music "music/Plaint.mp3" fadein 1 fadeout 1 #SAD CREDITS MUSIC.
        
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}This is ending \"00\" out of \"02\".{/color}{/size}"
        
        centered "{size=+7}{color=#cbcbcb}Thank you for playing!{/color}{/size}\n\n
                  {size=+5}{color=#cbcbcb}AKABUR 2014{/color}{/size}"
        
        
        #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
        #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
        #scene image "08_ending/e05.png" with Dissolve(2)
        # show akaani with d5

        
        centered "{cps=20}{size=+5}{color=#ea91b0}-Hermione Trainer-{/color}{/size}\n\n
        {size=+5}{color=#e5e297}-Producer-{/color}{/size}\n{color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Head programmer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Writer-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Artwork-{/color}{/size}\n     {color=#cbcbcb}AKABUR{/color}\n\n
        {size=+5}{color=#e5e297}-Additional Artwork-{/color}{/size}\n     {color=#cbcbcb}DAHR{/color}\n\n
        {size=+5}{color=#e5e297}-Sound Effects-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n"
    #    {size=+5}{color=#e5e297}-MUSIC-{/color}{/size}\n\n

    #    {color=#e5e297}(From \"NEWGROUNDS\")\n
    #    {color=#e5e297}\"Eastern Journey\" {/color}{color=#cbcbcb}by Pike270.{/color}\n
    #    {color=#e5e297}\"Grape Soda Is Fucking Raw\"{/color} {color=#cbcbcb}by jrayteam6.{/color}\n
    #    {color=#e5e297}\"The Eastern Wind\"{/color} {color=#cbcbcb}by roensb.{/color}\n
    #    {color=#e5e297}\"Silly Cat\" {/color}{color=#cbcbcb}by Maverlyn.{/color}\n
    #    {color=#e5e297}\"Kabul Flight\" {/color}{color=#cbcbcb}by Jumpstart.{/color}\n
    #    {color=#e5e297}\"Sleep Walking\" {/color}{color=#cbcbcb}by hektikmusic.{/color}{/cps}"
        #nvl clear
    #    hide akaani
        
        $ renpy.play('sounds/scratch.wav')
        stop music
        with hpunch
        g4 "Wait, I'm still here!"
        centered "{size=+7}{color=#cbcbcb}WHAT?!{/color}{/size}"
        g4 "I said I am still here, dammit!"
        centered "{size=+7}{color=#cbcbcb}Oh... :({/color}{/size}"
        
        
        
        hide screen end_u_4                                           #<---- SCREEN
        with d1
        hide screen blkfade 
        with d9
        play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
        
    m "....................."
    if persistent.game_complete:
        m "No, I can't just leave like this!"
    else:
        m "I can't just leave like this!"
    
    m "I must see the girl one last time..."
    
    show screen ctc
    pause
    hide screen ctc
    
    show screen blkfade
    with d7
    
    stop music fadeout 1.0
    
    if not persistent.game_complete: # FIRST PLAY THROUGH.
        centered "{size=+7}{color=#cbcbcb}Fine whatever...{/color}{/size}"
    play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
    centered "{size=+7}{color=#cbcbcb}\"The Annual Hogwarts Autumn Ball\"{/color}{/size}"

    hide screen end_u_4                                           #<---- SCREEN
    jump your_whore
    
    return
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
