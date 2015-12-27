
        
        
        
###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label new_request_22: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main 
    with d3
    if request_22_points == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
    if "slytherin_cheerleader" in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                m "A Slytherin Cheerleader."
                if whoring >= 10:
                    $ changeHermioneMainScreen(hg_pth+"body_30.png")
                    her "A Slytherin?"
                    m "Just for a minute."
                    $ changeHermioneMainScreen(hg_pth+"body_34.png")
                    her "..."
                    $ changeHermioneMainScreen(hg_pth+"body_33.png")
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 3
                    $ stockings = 4
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass

    if request_22_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, [genie_name]?"
        m "I plan to grant \"Gryffindor\" 55 house points today..."
        m "If you suck me off..."
        if whoring <=14: # LEVEL 05
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Oh..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Alright."
        m "Really? Just like that?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes. I know I'm supposed feel outraged..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But somehow I do not..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I suppose I am just glad that I can help out my house..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And if to do that I must put your penis in my mouth so be it..."
        m "Well, alright then."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Although, now when I say it out loud like this..."
        m "Too late! You already said \"yes\"!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I know..."
        label blowjob_jumping:
        
        # BLOWJOB
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
#        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
#        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE


        

        
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Yes..."
        m "Try to take it deeper now..."
        her "*Gulp!* *Gobble!* *Gobble!*"
        m "Yes, like that. Good."
        her "*Slurp!* *Gltch!* *Gulp!*"
        m "Yes, that's a good girl."
        menu:
            m "Hm..."
            "\"Whatever happened to your \"MRM\" thing?\"":
                her "*Slurp?*"
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Oh, well..."
                her "We are still active, but..."
                hide screen h_head2       
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gobble!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "But we are not getting as popular and as much support as I thought we would..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Slurp!* *Gulp!* *Gulp!*"
                m "Oh... This is good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Hm..."
                m "So you don't mind selling me sexual favours, letting me play with your tits and such..."
                her "*Gobble!* *Gltch!* *Slurp!*"
                m "And then condemn such behavior in front of the other students."
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "You perverted, little hypocrite."
                her "*Gulp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "That's not what we stand for, [genie_name]."
                hide screen h_head2
                m "What do you mean?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_16.png" # HERMIONE
                her2 "The \"MRM\" is about gender equality."
                her2 "We are not as much against selling sexual favours to the teachers..."
                her2 "As we are against the gender inequality that the selling of sexual favour creates..."
                hide screen h_head2
                m "Hm..."
                m "This conversation is starting to bore me..."
                m "Suck on my cock some more before we continue."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Of course, [genie_name]."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Gobble!* *Slurp!* *Slurp!*"
                m "Yes, much better..."
                m "But you still disapprove of selling the favours, right?"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Yes, it is frowned upon..."
                hide screen h_head2 
                m "And yet, you are the biggest offender by far."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her "But what choice do I have?"
                her2 "I've been put in a very difficult position..."
                hide screen h_head2
                m "The cock, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Right, sorry..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Slurp!* *Gulp!* *Gltch!*"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "This one time we had a meeting right after I sold you another favour, [genie_name]."
                her2 "I had to give a speech with my uniform all messy and stained."
                her2 "It felt awful that I had to do that..."
                hide screen h_head2     
                m "You did enjoy it a little bit though..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE  
                her "Well..."
                hide screen h_head2        
                m "Just admit it."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "..............."
                hide screen h_head2
                m "Yes, I knew it. You took pleasure in it, you little perv."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "I suppose it was embarrassing and exciting at the same time..."
                her2 "And it made me feel even worse about myself."
                hide screen h_head2
                m "You poor thing."
                m "Cock back in the mouth."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Yes, [genie_name]."
                hide screen h_head2
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                

            "\"Your parents must be proud of you...\"":
                her "*Slurp--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_75.png" # HERMIONE
                her "Yes, I believe they are..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "With me being an excellent student despite being muggle-born and all..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "Although at first they were against sending me to some \"Bogus boarding school\"."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Took some effort to convince them that \"Hogwarts\" is a respectable institution."
                hide screen h_head2     
                m "Yes, a respectable institution indeed."
                m "Cock back in your mouth [hermione_name]."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gulp!* *Gobble!*"
                hide screen h_head2     
                m "Yes, just keep at it for a while..."
                her "*Slurp!* *Gltch!* *Gulp!*"
                hide screen h_head2     
                m "Good, good..."
                m "So, what would your folks say if they were to see you now, [hermione_name]?"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "They would not understand of course..."
                her "But I do not care."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "I am not afraid to \"get my hands dirty\" and do what needs to be done."
                hide screen h_head2     
                m "A bit rebellious, aren't you?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Hm... I suppose I am."
                hide screen h_head2     
                m "Back to sucking then. Teach your folks a lesson."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Slurp!*"
                

            "\"Tell me about the \"Gryffindor\" house.\"":
                her "*Slurp--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_13.png" # HERMIONE
                her "What can I say that you don't already know, [genie_name]?"
                hide screen h_head2     
                m "Yes... Ehm... I know everything of course."
                m "But I want to see how much you know."
                m "To test your knowledge on the subject."
                show screen blktone
                with d3
                ">As soon as you mention \"test\" Hermone's eyes light up with excitement."
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_80.png" # HERMIONE
                her "OK. But I need a moment gather my thoughts..."
                hide screen h_head2  
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Oh, yes... Take as much time as you need, [hermione_name]."
                her "*Slurp!* *Gulp!* *Slurp!*"
                her "*Gulp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                hide screen ctc
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "The \"Gryffindor\" house was founded by Godric Gryffindor, thus the name."
                her2 "The heraldic animal of \"Gryffindor\" is the lion..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her "And it's colors are red and gold."
                hide screen h_head2   
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                her "*Gulp!* *Slurp!* *Slurp!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "Professor Minerva McGonagall is the headmaster of our house."
                her2 "The \"Gryffindor\" house emphasizes the traits of courage..."
                her2 "As well as \"daring, nerve and chivalry\"..."
                her2 "And thus its members are generally regarded as brave but reckless..."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Slurp!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "\"Gryffindor\" corresponds roughly to the element of fire..."
                her2 "And for that reason the colours of red and gold were chosen."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Hm..."
                m "Well, I thought I could turn this around somehow to make fun of you..."
                hide screen h_head2     
                her "*Slurp??*"
                m "Well, with your house representing courage and righteousness and such..."
                m "And you being a nasty slut..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_86.png" # HERMIONE
                her "[genie_name]!"
                hide screen h_head2     
                hide screen h_head2     
                m "But to be honest..."
                m "\"Daring, nerve, fire, recklessness\"..."
                m "That sort of describes your personality quite well..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                her "[genie_name]..."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Gobble!!* *Gltch!!* *Gobble!!!*"
                m "Good girl..."
        
        m "Good..."
        her "*Gobble!* *Slurp!* *Slurp!*"
        m "Good... Back and forth, back and forth... Good girl."
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
        her "[genie_name]... I am a... whore."
        hide screen h_head2  
        m "What?"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Slurp-Slurp-Slurp!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her2 "I truly am a slut and deeply enjoy sucking your cock."
        hide screen h_head2  
        m "Oh, yes, yes... Say more things like that."
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Slurp!* *Gulp!* *Slurp!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Please, [genie_name]. Cum for me."
        hide screen h_head2  
        with hpunch
        g4 "Argh! You little...!!!"
        g4 "{size=-4}(Here it comes. Should I give her a warning?){/size}"
        menu:
            m "..."
            "-Warn her-":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Yes, I love to suck and --"
                hide screen h_head2  
                g4 "Heads up, [hermione_name]! Here it comes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
                her "!!!"
                hide screen h_head2      
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                ">Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion."
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}ARGH!{/size}"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "And some more!"
                her "*Gulp!* *Gulp!* *Gulp!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Well, I think that's it."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_126.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Are you alright there, [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes, [genie_name]..."
                her "You came so much..."
                hide screen h_head2  
                m "You managed to swallow it all though."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes... I thought I would choke..."
                her2 "But I made a promise to myself that I won't let go of your penis no matter what!"
                hide screen h_head2  
                m "Good girl."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Thank you, [genie_name]."
                her "But, still... You came so much..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "I almost feel as if I just got fed..."
                her "My stomach is so full..."
                hide screen h_head2  
                g9 "Yes, I fed you with my cum!"
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "I think I may skip the meal and go straight to class today."
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "Yes. I think I may skip supper tonight..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Can I get paid now?"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
            "-Don't bother-":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Yes, I love to suck and --"
                hide screen h_head2  
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Whore!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                hide screen h_head2
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "[genie_name]..."
                hide screen h_head2  
                g4 "Don't you move now, [hermione_name]."
                g4 "Yes, just be still and take it."
                g4 "Argh! You little slut! You make me cum hard, [hermione_name]!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Whew..."
                $ g_c_u_pic = "cum_on_face_blink_ani"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Alright, I'm done..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "................."
                if daytime:
                    her "My classes are about to start..."
                else:
                    pass
                hide screen h_head2  
                m "Just wipe it off and you'll be alright."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............"
                hide screen h_head2  
                m "Unless, you don't want to."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Huh?"
                hide screen h_head2  
                m "And would rather go outside looking like this."
                m "Let everyone see what a nasty little slut you are."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Of course not, [genie_name]!"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                stop music fadeout 1.0
                if daytime:
                    m "You better go before you are late for your classes..."
                else:
                    m "It's getting late..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                    her "Yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Can I get paid before I leave, [genie_name]?"
                hide screen h_head2
                $ aftersperm = True

        
        
    elif request_22_points == 1: #  <============================================================== EVENT 02
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "[genie_name]?"
        m "How about another blowjob?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "[genie_name], how dare you propose such a thing to one of your pupils!"
        m "Wha...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "This is unbecoming of a man of your standing."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "You should be ashamed of yourself [genie_name]!"
        menu:
            m "???"
            "\"Fine. No points to you then! Leave!\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "[genie_name], calm down, please."
                m "You are dismissed, [hermione_name]."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "[genie_name], please, I didn't mean any of the things I said."
                m "What?"
            "\"Ehm... I am sorry?\"":
                stop music fadeout 1.0
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "*Giggle*"
                m "Huh?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "I got you... [genie_name]."
                m "What?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Well, so much has happened lately..."
        her2 "I had so many new experiences that kind of changed the way I look at things..."
        her2 "So I was just trying to imagine how the \"old me\" would've reacted to this."
        m "So..."
        g4 "You were messing with me then?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "uhm... I'm sorry [genie_name], I didn't mean to..."
        g4 "You nasty little girl! You must be punished!"
        g9 "I'll punish you with my cock!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "..............................."

        jump blowjob_jumping
  
    elif request_22_points >= 2: # <============================================================== EVENT 03
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Suck my dick, [hermione_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                         #HERMIONE                                                                                                                                                                                                                                          
        her "Of course..."
        # Sucking.
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
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
        
        $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
        "> *Knock-knock-knock!*"
        her "{size=+7}!!!{/size}"
        m "Hm?"
        if daytime:
            m "Who could that be?"
        else:
            m "Who could that be at this hour?"
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
        her "([genie_name], what should I do?)"
        hide screen h_head2
        m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
        sna "Albus? Are you there? I need to talk to you."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "(It's professor Snape!)"
        her "([genie_name], please, send him away, I beg you!)"
        hide screen h_head2
        menu:
            m "..."
            "\"Please, come on in, Severus.\"":
                $ mad = 30
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_76.png" # HERMIONE
                stop music fadeout 1.0
                her "([genie_name], no!)"
                hide screen h_head2
                show screen blktone
                with d3
                with hpunch
                ">Hermione gives your balls a firm twist full of frustration."
                hide screen blktone
                with d3
                g4 "Ouch!"
                hide screen bld1
                with d3
                # SNAPE COMES IN
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ walk_xpos=610 #Animation of walking chibi. (From)
                $ walk_xpos2=360 #Coordinates of it's movement. (To)
                $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                show screen snape_walk_01 
                pause 4
                show screen snape_02 #Snape stands still.
                show screen bld1
                with d3
                $ s_head_xpos = 330 # x = 330,
                $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
                $ s_sprite = "01_hp/10_snape_main/snape_01.png"
                show screen s_head2

                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                sna "Good, you are here."
                hide screen s_head2
                
                $ g_c_u_pic = "blowjob_ani" # sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Listen, there is something I want to discuss..."
                $ s_sprite = "01_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Hm...?"
                sna "Genie? Are you alright?"
                hide screen s_head2
                her "{size=-4}(Ginny!!? Is she here as well?!){/size}"
                her "{size=-4}(No, please! I will die of shame!){/size}"
                m "Yes, Severus, I am fine..."
                her "{size=-4}(What? *Slurp...?* *Slurp...?* *Gulp...?*){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "What are you... looking at?"
                hide screen s_head2
                m "Ehm... Just admiring...{w} the cupboard."
                m "Please continue..."
                $ s_sprite = "01_hp/10_snape_main/snape_05.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "..............."
                hide screen s_head2
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                m "Did you want to discuss something?"
                $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Yes. That Hermione girl."
                hide screen s_head2
                her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                m "Oh... What about her?"
                $ s_sprite = "01_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "You promised that you would take care of the little witch."
                hide screen s_head2
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "But she is still being a major pain in my arse!"
                sna "Her tactics have changed..."
                $ s_sprite = "01_hp/10_snape_main/snape_03.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna2 "But the amount of grief she manages to bring me is the same..."
                hide screen s_head2
                m "I see... ah..."
                $ s_sprite = "01_hp/10_snape_main/snape_10.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "I swear, that girl is driving me crazy!"
                hide screen s_head2
                g4 "Yeah, she is driving me crazy as well... ah..."
                her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_04.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Will you take care of this then?"
                hide screen s_head2
                m "Yes. She'll get what she deserves."
                $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                show screen s_head2                                                          # SNAPE
                sna "Good. That is all I wanted to hear."
                if daytime:
                    hide screen s_head2
                    m "Well, have a good day, Severus."
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Yes, thank you."
                else:
                    hide screen s_head2
                    m "Good night, Severus."
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Right..."
                # SNAPE LEAVES
                hide screen s_head2
                hide screen ctc
                
                hide screen bld1
                with d3
                $ walk_xpos=360 #Animation of walking chibi. (From desk)
                $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
                show screen snape_walk_01_f 
                pause 3
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                hide screen snape_walk_01_f 
                with d4
                pause.5
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen blkfade
                with d5
    
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
                ">Seeing her being so confused and vulnerable and yet continuing to perform her task diligently pushes you over the edge."
                g4 "(Here it comes!)"

                
            "\"I am busy right now, Severus.\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "(Thank you, [genie_name].)"
                hide screen h_head2                                                          
                sna "Busy? With what?"
                sna "All you do is sit on you arse all day."
                sna "I really need to talk to you about something."
                m "I said I am busy, Severus."
                m "Understood? I am \"busy\"!"
                sna "Oh... You mean \"Busy\" busy? Gotcha!"
                sna "Well, I'll talk to you later then."
                #">Hermione keeps sucking on your cock with a rather fierce determination."
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING                
                #">Hermione is working hard to please you..."
                her "*Slurp!* *Slurp!* *Gulp!*"
                show screen blktone
                with d3
                ">Hermione keeps sucking on your cock with a rather fierce determination."
                ">Her technique is lacking but she makes up for it with the effort she puts it."
                hide screen blktone
                with d3
                m "Yes... I love your eager, little mouth girl..."
                her "*Gobble!* *Gobble!* *Gobble!*"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "[genie_name]?"
                hide screen h_head2          
                m "Hm?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Are you going to cum on my face today?"
                her "Or do you plan to cum in my mouth?"
                hide screen h_head2
                menu:
                    "\"I Plan to splatter your face with cum!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "I see..."
                        hide screen h_head2
                        m "Why do you ask?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "Oh... I just read in a book that semen contains a lot of antioxidants..."
                        her "It's good for the skin..."
                        hide screen h_head2
                        m "Great. One facial coming up."
                        m "Back to work now."
                    "\"I Plan to fill your mouth with cum!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                        her "I see..."
                        hide screen h_head2
                        m "Why do you ask?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Well, I am trying to watch my calorie-intake..."
                        her2 "I just wonder how much calories your load contains, [genie_name]."
                        her2 "Maybe I should skip my next meal..."
                        hide screen h_head2
                        m "[hermione_name]."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Yes?"
                        hide screen h_head2
                        m "Dick back in the mouth."
                    "\"I don't plan so far ahead.\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "I see..."
                        hide screen h_head2
                        m "Don't you like surprises?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "Not really..."
                        her "I rather enjoy planning ahead actually..."
                        hide screen h_head2
                        m "Well some things in life are just unpredictable."
                        m "There is only one way to find out for sure."
                        
                    "\"What would you like?\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "If it is all the same to you, [genie_name]..."
                        if generating_points == 1:
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                            her2 "I would like you to cum on my face, [genie_name]."
                            her2 "I read that it's good for the skin."
                        else:
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                            her2 "I would like you to cum in my mouth."
                            her2 "You usually cum so much so I think I will be able to just skip my next meal..."
                            her2 "And do some homework instead."
                        hide screen h_head2
                        m "Well, we'll see about that."
                        m "Back to sucking now."
                    
                    
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING   
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Hm..."
                m "You are getting better at this [hermione_name]."
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Ok, say something nasty now..."
                her "*Slurp--?"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                if whoring <= 20:
                    $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                    her "uhm..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                    her "I eat cockroaches?"
                    hide screen h_head2
                    m "What the fuck?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                    her "T-they are pretty nasty, [genie_name]..."
                    hide screen h_head2
                    m "No, [hermione_name], I mean something dirty!"
                    m "And don't you dare to say \"mud\"!"
                    m "I mean dirty in a sexual way!"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                    her "Oh... Ehm..."
                    hide screen h_head2
                    m "Ah, never mind, the moment is gone..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                    her "Ehm... I'm sorry, [genie_name]."
                    hide screen h_head2
                    m "Yeah, whatever. Make it up to me by sucking my cock harder."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                    her "Of course, [genie_name]."
                    hide screen h_head2
                else:
                    $ h_body = "01_hp/13_hermione_main/body_129.png" # HERMIONE
                    her "I'm a slut [genie_name]."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE
                    her "A slut for your cum."
                    hide screen h_head2
                    m "That's it [hermione_name]."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                    her "It's all I can think about [genie_name]."
                    her "Sucking your dirty old cock..."
                    hide screen h_head2
                    m "Well you better get back to it then [hermione_name]"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                    her "Thank you [genie_name]."
                    hide screen h_head2
                    m "You're welcome cumslut."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_78.png" # HERMIONE
                    her "..."
                    hide screen h_head2
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                
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
                
        menu:
            g4 "!!!"
            "-Cum in her mouth-":
                hide screen blkfade
                with d3
                g4 "Here it comes, [hermione_name]! get ready to swallow fast!"
                her "!!!"
                
                hide screen h_head2      
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}ARGH!{/size}"
                g4 "Eat my cum, slut!"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Yes! Down your fucking throat!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Well, I think that's it."
                m "You can let go now..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_125.png" # HERMIONE
                her "..........................."
                her "................"
                her "........"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "*GULP!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her "Gua-ha..."
                hide screen h_head2  
                m "You alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Yes, [genie_name]..."
                hide screen h_head2  
                m "Going to skip your next meal?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "I think so..."
                her "You always cum so much, [genie_name]..."
                hide screen h_head2  
                m "Heh... And who's fault is that??"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "............." #Smile.
                her "Can I get paid now?"
                if whoring >= 20:
                    hide screen h_head2  
                    if daytime:
                        m "What, even after I just gave you lunch?"
                    else:
                        m "What, even after I fed you dinner"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_17.png" # HERMIONE
                    her "............." #Smile.
                    her "Fine, I suppose this was worth a meal"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3

                
            "-Cum on her face-":
                show screen bld1
                hide screen blkfade
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                g4 "Ready for your facial, [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes [genie_name]!"
                hide screen h_head2      
                g4 "Here it comes then!"
                
                hide screen h_head2  
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Whore!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                hide screen h_head2
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "[genie_name]..."
                hide screen h_head2  
                g4 "All over your fucking face!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Aaah!"
                $ g_c_u_pic = "cum_on_face_blink_ani"
                hide screen h_head2  
                m "Well, I'm done."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "...................................."
                hide screen h_head2  
                m "I said it's over, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes, I heard you [genie_name]..."
                hide screen h_head2  
                m "So... Aren't you going to clean up?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "In a moment..."
                her2 "I'm giving my skin time to soak in the anti-oxidants..." 
                hide screen h_head2  
                m "Hm... I find this quite hot..."
                m "Take your time, [hermione_name]..."
                show screen blkfade
                with d3
                stop music fadeout 1.0 
                ">A while later."
                $ uni_sperm = False
                $ aftersperm = True
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "I take it you enjoyed yourself [genie_name]?"
                hide screen h_head2  
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Yes I did, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Good, so Can I get paid now?"
                if whoring >= 20:
                    hide screen h_head2  
                    m "What, even after I just gave you a salon treatment?"
                    m "Women pay a lot of money for a good facial."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_17.png" # HERMIONE
                    her "............." #Smile.
                    her "Fine, but my skin better look better tomorrow."
                hide screen h_head2  
                
                    
                
            
        
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    $ badges = True # Turns the badges layer of hermione_main back on.
    if whoring <= 19:
        m "Yes, [hermione_name]. 55 points to \"Gryffindor\"." 
        $ gryffindor +=55
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 17:
        $ whoring +=1


    
    
    if request_22_points == 0:
        $ new_request_22_01 = True #  HEARTS
    if request_22_points == 1:
        $ new_request_22_02 = True #  HEARTS
    if request_22_points >= 2:
        $ new_request_22_03 = True #  HEARTS

    $ request_22_points += 1

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   
    
    
    

###################REQUEST_29 (Level 07) (65 pt.) (Sex). #################################################################
label new_request_29: #LV.7 (Whoring = 18 - 20)

    hide screen hermione_main 
    with d3
    m "{size=-4}(Should I ask her to have sex with me?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
  
    if request_29_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "[genie_name]?"
        m "The favour I will be buying from you today..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her ".......?"
        m "How should I put this delicately...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Is it sex, [genie_name]?"
        m "Well, yes. How did you...?"
        if whoring <=17:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Not a terribly difficult deduction all things considered..."
        m "You don't mind then?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "Of course, I mind, [genie_name]!"
        her "I am not a prostitute!"
        m "But you'll do it anyway??"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her2 "\"Gryffindor\" is falling behind again..."
        her2 "What choice do I have...?"
        m "Great!"
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
       
        label your_ass:
            
        show screen blkfade 
        with d7
            
        stop music fadeout 1.0
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
        her "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE
        her "!!!!!!!!!!!!!!!"
        hide screen h_head2                        
        m "Relax, [hermione_name]. I'm Just gonna take off your panties."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_49.png" # HERMIONE
        her ".............."
        hide screen h_head2                        
        m "Are you ready?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_50.png" # HERMIONE
        her "No..."
        hide screen h_head2                        
        m "Good girl."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ooooohhhhhhhhhhhh....{image=textheart.png}"
        hide screen h_head2




        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3    
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            
            
            
            
        
        
        #FUCKING
        
        g4 "Your pussy... It's so tight."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
        her "................"
        hide screen h_head2                       
        m "You alright?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
        her "A-ha... It's too big..."
        her "You will rip me apart, [genie_name]!"
        hide screen h_head2        
        m "Nonsense! My cock is of a regular size."
        m "It's not my fault that you are so tiny."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
        her "......................"
        hide screen h_head2         
        hide screen ctc
        menu:
            "\"You should be ashamed of yourself!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "I am not ashamed, [genie_name]!"
                her "I am doing this for the sake my house!"
                her "To help my--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "ah-ha-a..."
                her "My classmates depend on me... ah-a..."
                hide screen h_head2  
                m "Are you sure that's the only reason?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "I don't know--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her2 "ah-a..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "I don't know what you mean, [genie_name]."
                hide screen h_head2  
                m "It seems to me that you are enjoying this a little bit too much."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "I'm not, [genie_name]!"
                hide screen h_head2  
                m "Really?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "......................"
                hide screen h_head2  
                m "Then why is your pussy so wet?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "....................a-ha.{image=textheart.png}"
                hide screen h_head2  
                m "Admit it, you enjoy getting fucked by your [genie_name]!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "I do not!"
                hide screen h_head2  
                m "Stubborn girl..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Aha...{image=textheart.png}" 
                hide screen h_head2  
            "\"So... What's new in your life?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "...[genie_name]?"
                hide screen h_head2  
                m "Just trying to have a polite conversation."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Ah-ah... But... ah..."
                hide screen h_head2  
                m "Any news from your folks?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her "My parents?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "[genie_name], please, I cannot talk..."
                hide screen h_head2  
                m "Why not? Enjoying this too much?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "I am not... ah...{image=textheart.png}"
                hide screen h_head2  
                m "I think you are."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "I am only doing this for the points, [genie_name]..."
                hide screen h_head2  
                m "Oh, I see..."
                m "So you are like a prostitute then."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "What?"
                hide screen h_head2  
                m "Well I pay you to have sex with me. How would you call that?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "I am not a prostitute..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
                her "Why are you being so mean to me, [genie_name]?"
                hide screen h_head2  
                m "I think you like it when I'm mean."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_67.png" # HERMIONE
                her "I do not!"
                hide screen h_head2  
                m "Really? Then why is your pussy so wet?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Not because of that!"
                hide screen h_head2  
                m "If you say so..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "A-ah...{image=textheart.png}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "I am... ah...{image=textheart.png} not a prostitute..."            
                hide screen h_head2  
            "\"......................................................\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "A-ha... ah..."
                hide screen h_head2  
                m "*Panting!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah... ha-aha..."
                hide screen h_head2  
                m "Oh..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah-ah..."
                hide screen h_head2  
                m "......................"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah... ah..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Ah... [genie_name]?"
                hide screen h_head2  
                m "What is it?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah... Do you.... like it?"
                hide screen h_head2  
                m "Do I like drilling your super-tight pussy?"
                m "Very much so, [hermione_name]. Why?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "....................."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah... You just got so quiet..."
                hide screen h_head2  
                m "Just enjoying the moment, [hermione_name]."
                m "What about you? You alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah... yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "It hurts a little though, ah..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Your penis is too big... ah..."
                hide screen h_head2  
                m "Hm..."
                m "You need me to slow down or something?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "No, [genie_name]... You don't have to..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Please, don't mind me... Enjoy your moment."
                her "I will... ah... Get used to it eventually... ah..."
                hide screen h_head2  
                m "As you say, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah-a...{image=textheart.png}"
                hide screen h_head2  

        m "Yes, this is great!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Ah-ah...{image=textheart.png}"
        hide screen h_head2  
        if daytime:
            m "Going to classes after this?"
        else:
            m "Going to bed after this?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Yes, ah...{image=textheart.png}"
        her "If I'll be able to walk..."
        hide screen h_head2  
        g4 "Ght! {image=textheart.png} Yes, you always say the right things, [hermione_name]!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
        her "Ah...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}"
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her "{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        m "Huh? You alright?"
        show screen blktone8
        with d3
        ">Hermione's legs are shaking..."
        m "[hermione_name]?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her "{image=textheart.png}{image=textheart.png}{image=textheart.png}I think I'm cumming, [genie_name]!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        g9 "Tch... You nasty slut!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
        her "AAH! I can't hold it!"
        hide screen h_head2  
        g4 "You need to be punished for being such a slut!"
        ">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!"
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her "NO! STOP! PLEASE!"
        hide screen h_head2  
        g4 "Who told you you could cum, slut? This is your punishment!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
        her "[genie_name], no, ah-a!{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
        her "Ah-a...{image=textheart.png}I will go insane!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        g4 "{size=+7}Grragh!{/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
        her "No...{image=textheart.png} ah...{image=textheart.png}"
        her "I think I will...{image=textheart.png} pass out...{image=textheart.png}"
        hide screen h_head2  
        g4 "ARGH! YOU WHORE!"
        menu:
            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"

                m "Well, that was rather intense..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_135.png" # HERMIONE
                her "*heavy panting*"
                hide screen h_head2
                m "You alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ah... yes..."
                her "My legs are still shaking..."
                hide screen h_head2
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                if daytime:
                    her "But I think I will be able to make it to my classes..."
                else:
                    her2 "But I think I will be able to make it to the common room..."
                hide screen h_head2
                m "Good."
                m "Did you enjoy getting fucked by your [genie_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_136.png" # HERMIONE
                her "[genie_name], I am only doing this for my house."
                hide screen h_head2
                m "Seriously? Still?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Could I just get paid now... please?"
                hide screen h_head2
    
            "-Cum inside Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                
                
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "You came inside of me..."
                hide screen h_head2
                g9 "I sure did."
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "But..."
                hide screen h_head2
                m "What?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "What if I get pregnant?"
                hide screen h_head2
                m "Nah, you will be alright..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "How do you know, [genie_name]?"
                hide screen h_head2
                m "We witchers are infertile."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Witchers?"
                hide screen h_head2
                m "Sure... You are a witch, that make me a witcher, right?"
                m "And everyone knows that witchers are infertile..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "[genie_name], you make no sense..."
                her "Can I please just get paid now...?"
                hide screen h_head2

    elif request_29_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "[hermione_name], are you keeping your pussy wet and ready for me?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "[genie_name]!"
        m "Just say \"I do\" and come over here, [hermione_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "..........."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "I do...."
        hide screen hermione_main    
        jump your_ass

    elif request_29_points >= 2: # THIRD EVENT <============================================================== EVENT 03
        m "[hermione_name]..."
        m "Last night I had a dream..."
        g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        if whoring >= 24:
            $ h_body = "01_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        else:
            $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.   
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "In that dream, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        if whoring <= 23:
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                     
            her "Did I happen to receive 65 house points afterwards?"
            g9 "Why yes, you did, [hermione_name]."
        else:
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                     
            her "Did you cum inside me or not?"
            g9 "I'm not sure [hermione_name], care to find out?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                     
        her "..............................."
        her "Let me just take my panties off..."
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        show screen blkfade
        with d3
        # SEX
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ooooohhhhhhhhhhhh....{image=textheart.png}"
        hide screen h_head2
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        show screen bld1
        with d3    


        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
        her "Ah...{image=textheart.png}"
        hide screen h_head2      
        m "Your pussy feels a bit looser today..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE    
        her "Does it...{image=textheart.png} ah...?{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE    
        her "That's all because of you [genie_name]...{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE    
        her2 "You are ruining my little pussy with your monstrous penis...{image=textheart.png}"
        hide screen h_head2     
        g4 "Agh, you whore!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE    
        her "Ah...{image=textheart.png}{image=textheart.png}"
        hide screen h_head2     

        
        
#        if not ask_me_once: #Turns true after Hermione asks you about your true identity, during sex.
#            $ ask_me_once = True #Turns true after Hermione asks you about your true identity, during sex.
#            her "[genie_name], can I ask you something?"
#            m "What is it, [hermione_name]?"
#            her "Ah... Oh, not so deep please..."
#            her "Ah... I... Ah..."
#            her "?!!"
#            her "[genie_name]? Why did you stop?"
#            m "What did you want to ask me, [hermione_name]?"
#            her "But I think I was about to cum..."
#            m "So soon? Good think I did stop then."
#            her "[genie_name], please..."
#            her "I want to ask you this question while..."
#            her "While you are fucking me..."
#            her "Ah..."
#            her "[genie_name], I just want to know..."
#            her "Are you really [genie_name]?"
#            g4 "WHAT!?"
#            menu:
#                m "!!!"
#                "\"Yes! Albus Dumbledore! That's me!\"":
#                    her "Oh..."
#                    her "You just been acting so unlike yourself lately..."
#                    g4 "You whore! Your little pussy is the best!"
#                    her "I suppose that was just my imagination then..."
#                    her "Ah-ah-a..."
#                "\"You got me... The truth is...\"":
        m "Yes! Do you like it when I fuck you like this?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE    
        her "Yes, [genie_name]..."
        hide screen h_head2  
        menu:
            g4 "..."
            "\"Be sweet but passionate.\"":
                m "Yes, you're liking this?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE    
                her "I do, [genie_name]... ah...{image=textheart.png}"
                hide screen h_head2  
                m "Good girl!"
                m "Just relax and take my cock!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE    
                her "Yes... ah...{image=textheart.png}"
                hide screen h_head2  
                m "All the way in... all the way..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE    
                her "Ah...{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "Yes, my little princess..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE    
                her "What?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE    
                her "No, please don't call me that... ah...{image=textheart.png}"
                her2 "My daddy used to call me his little princess when I was little..."
                hide screen h_head2  
                m "Well, right now I am your daddy!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE    
                her "Ah...{image=textheart.png} ah-ah...{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "And you are my little princess-slut!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE    
                her "Ah...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
            "\"Be mean to her!\"":
                hide screen h_head2  
                m "Yes, you slut!"
                m "I bet you love every second of this!"
                show screen blktone
                hide screen ctc
                with d3
                ">You pick up the pace."
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE    
                her "Ah...{image=textheart.png} [genie_name]..."
                hide screen h_head2  
                m "You nasty slut!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ah...{image=textheart.png} ah-a...{image=textheart.png}"
                hide screen h_head2  
                m "You are a disgrace, [hermione_name]!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ah-ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "Your parents sent you here to study, not to screw your teachers, you disgusting cunt!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ah-a...{image=textheart.png} But I am only doing this--"
                hide screen h_head2  
                m "Nobody cares why you are doing this, cocksucker!"
                m "Look at what you've become!"
                m "Butt-naked, on your professor's old cock, like a cheap whore!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE    
                her "Ah...{image=textheart.png} No...{image=textheart.png} stop saying...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                show screen blktone
                with d3
                ">You pick up the pace some more."
                $ g_c_u_pic = "sex2_ani"
                ">The room fills up with rhythmical sound of a flesh hitting flesh..."
                hide screen blktone
                with d3
                m "You let me molest you... You suck my cock..."
                m "What are you after that I ask you!?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE    
                her "................"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE    
                her "Ah...{image=textheart.png} ah....{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE    
                her "......................."
                her "{size=-5}I am a whore...{/size}"
                #her "{size=-5}I am a whore... ah...{\size}"
                hide screen h_head2  
        
        m "Yes! That's exactly what you are!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE  
        her "Ah... ah... ah..."
        her "[genie_name], you think you could... ah..."
        hide screen h_head2  
        m "What?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Could you spank me a little... ah...?"
        hide screen h_head2  
        g4 "Gladly!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE  
        her "Aa-a-ah!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        m "You liked that one, huh?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Ah..!{image=textheart.png} Yes!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2  
        m "And some more!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Ahh! Yes!"
        hide screen h_head2     
        show screen blktone
        with d3
        ">You notice that every time you slap the girl's butt, her pussy clutches your cock tightly for a second..."
        ">You love the sensation..."
        ">You unleash another series of slaps on Hermione's ass-cheeks."
        ">Every single one met with a gasp of excitement from the girl."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE  
        her "Aah!!!{image=textheart.png}{image=textheart.png}{image=textheart.png} IT HURTS!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE  
        her2 "It hurts...{image=textheart.png}{image=textheart.png}{image=textheart.png} It hurts...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2 
        m "Hm?"
        m "Why your legs are shaking, [hermione_name]?"
        m "Are you cumming?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE  
        her "Yes...{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2 
        m "Well, I think I will follow your example then."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE  
        her ".............."
        hide screen h_head2 
        show screen blktone 
        with d3
        ">You start fucking Hermione with renewed determination!"
        hide screen blktone 
        with d3
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE  
        her "Ah! No! I can't...{image=textheart.png} I...{image=textheart.png} ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
        hide screen h_head2 
        m "Shut it whore!"
        g4 "Argh!"
        menu:
            "-Cum inside of Hermione-":
                with hpunch
                g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
                
                
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "!!!"
                her "AH! IT'S FILLING ME UP!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                g4 "I'm Not done yet, bitch!"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "AH! MY BELLY!"
                hide screen h_head2    
                g4 "{size=+5}SLUT!{/size}"






                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"

                show screen blktone
                with d7
               

                
                
                
                
    
 
                
                m "Well, this was pretty great..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ah...{image=textheart.png}"
                hide screen h_head2
                m "You alright there, slut? Ehm, I mean, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Yes... I..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_135.png" # HERMIONE
                her "I feel so full..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                her "You came inside of me, [genie_name]!"
                hide screen h_head2     
                m "I sure did."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "You shouldn't have..."
                hide screen h_head2     
                m "Didn't you enjoy it?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "....maybe."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "I think I came several times..."
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Maybe you are right, [genie_name], and I shouldn't worry so much."
                if whoring <= 23:
                    her "Can I get my payment now?"
                hide screen h_head2     

            "-Cum all over Hermione-":
                
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2
                g4 "{size=+5}You whore! Take this!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "{size=+5}!!!{/size}"
                hide screen h_head2
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                
                


                
                m "Well, that was pretty great..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Ah...{image=textheart.png}"
                hide screen h_head2                                                             
                m "You alright there, slut?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Yes... I..."
                hide screen h_head2         
                m "Didn't you enjoy this?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "....I think so..."
                hide screen h_head2       
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "I think I came several times, [genie_name]..."
                if whoring <= 23:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                    her "Can I get my payment now?"
                hide screen h_head2     
        
        
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    hide screen blktone
    with d3
    
    stop music fadeout 4.0
    if whoring <= 23:
        m "Yes, [hermione_name]. 65 points to the \"Gryffindor\" house." 
        $ gryffindor +=65
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 20: # Level 07 <
        $ whoring +=1




    if request_29_points == 0:
        $ new_request_29_01 = True # HEARTS
    if request_29_points == 1:
        $ new_request_29_02 = True # HEARTS
    if request_29_points >= 2:
        $ new_request_29_03 = True # HEARTS



    $ request_29_points += 1

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

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    #call music_block 
    
    if daytime:
        jump night_start
    else:
        jump day_start
                   
   

 
 
###############################################################################################################################
### LEVEL 09 ##################################################################################################################
###################REQUEST_31 (Level 08) (75 pt.) (Anal sex).  #####################################################
label new_request_31: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main 
    with d3
    m "{size=-4}(Should I ask her to have anal sex with me?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
 
    if request_31_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "[genie_name]..?"
        m "How familiar you are with the term \"Anal Sex\"?"
        if whoring <=20:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "90 house points..."
        m "What?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE          
        her "............................."
        m "Well alright then. 90 house points it is."
        hide screen hermione_main   
        
        
        label lucky_guess:
            
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
        her "..........."
        hide screen h_head2      
        m "Let's see..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
        her "................."
        hide screen h_head2      
        m "Hm..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
        her "!!!"
        hide screen h_head2      
        g4 "Oh, come on!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
        her "Ouch!"
        hide screen h_head2      
        m "Just try to loosen up a little, would you?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
        her "I'm trying!"
        hide screen h_head2      
        m "Ok, what if I do this..?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
        her "Ouch! What are you doing, [genie_name]?"
        hide screen h_head2      
        m "Yeah, this won't work either..."
        m "Hm..."
        m "Alright, I think I know what we should do."
        menu:
            m "..."
            "\"I think I'll spit on it and just force it in!\"":
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
                her "Force it in, [genie_name]?!"
                hide screen h_head2      
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g3 "*SPIT!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Eeeeeew!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "No, [genie_name], wait! Maybe if I just relax--"
                hide screen h_head2      
                m "No need, here I come!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_22.png" # HERMIONE
                her "ARGH!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Ouch! Ouch! Ouch!"
                hide screen h_head2      
                g4 "Almost in!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "No, you're hurting me! You are hurting me!"
                hide screen h_head2      
                g4 "Almost! Almost!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ah! It hurts!"
                hide screen h_head2      
                g4 "Shut it, [hermione_name]! I'm doing you a favour!"
                g4 "Your anus is so tight it's completely un-fuckable!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Then stop, please!"
                hide screen h_head2      
                m "No! We need to loosen up your asshole a little!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
                her "But I don't want you to!"
                hide screen h_head2      
                m "Really? How do you expect people to fuck you up your ass then?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "What people?"
                hide screen h_head2      
                g4 "You know... people."
                g4 "Argh, dammit... My dick is hurting too now."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Stop then! Stop, [genie_name]!"
                her "I've changed my mind! I don't need 90 points!"
                hide screen h_head2      
                g4 "I think I'm almost..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}AAAAAAAAhhhhh!!!{/size}"
                hide screen h_head2
                g4 "YES!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!"
                hide screen h_head2
                g4 "Let us pump this little asshole full of semen then, shall we?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_137.png" # HERMIONE
                her "Yes... Please, I just want this to end..."
                hide screen h_head2




                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3    
                        
                        
                        
                
                
                
                
                #SCHUSH!
                
               
                g4 "Agh... You want this to end sooner?"
                g4 "Help me out then!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*sob!* How?"
                hide screen h_head2       
                g4 "You know..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Oh..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "I am a whore??"
                hide screen h_head2    
                g9 "Yes you are!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "*Sob!* I am a whore..."
                her "I love to suck cock..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her2 "And now my tiny asshole is getting ripped to pieces... *Sob!*"
                hide screen h_head2    
                g4 "Yes! Yes!"
                g4 "Agrh! Yes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "No! Is it getting bigger?! I'm scared!"
                hide screen h_head2    
                g4 "ARGH!"

                
            "\"Suck me off first. Lubricate my cock!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Oh... Alright..."
                hide screen h_head2    
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #SUCKING
                
                hide screen blkfade
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3
                        
                
                
                
                
                
                
                
                her "*Slurp!* *Slurp!* *Slurp!*"
                hide screen h_head2    
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                hide screen h_head2    
                m "Alright, I think that's enough. Back on the desk now."
                show screen blkfade
                with d3

                
                #ON THE DESK
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............."
                hide screen h_head2    
                g4 "Yes! Almost!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ouch!"
                hide screen h_head2    
                m "Relax. Almost in."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}AAAAAAAAhhhhh!!!{/size}"
                hide screen h_head2
                g4 "YES!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "My... my..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "It hurts!"
                hide screen h_head2
                g4 "Let's pump this little asshole full of semen then, shall we?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "....................."
                hide screen h_head2               
                
                # SEX
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3    


                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "....................."
                hide screen h_head2    
                m "You alright there, slut?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her2 "Ah... You are... stretching me out from the inside... [genie_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "And it still hurts..."
                hide screen h_head2    
                m "Hm..."
                m "Maybe not enough lubrication...?"
                m "Come on down, [hermione_name]. Suck my dick some more."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "What? But..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "But it's dirty... It's been inside already."
                hide screen h_head2    
                m "Yes, it's been inside, but that doesn't mean it's dirty now."
                m "Come one, [hermione_name]. Suck my cock some more."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                hide screen h_head2   
                show screen blkfade
                with d3
                
                
                #SUCKING
                
                hide screen blkfade
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3
                
                
                
                
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Can you taste your ass on my dick?"
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Alright, Maybe that's enough."
                show screen blkfade
                with d3
               

                
                #ON DESK AGAIN.
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3    
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ah..."
                hide screen h_head2     
                m "Better now?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "It still hurts..."
                her "But I think I will be fine..."
                hide screen h_head2     
                m "I'll take it slow for now..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "Ah... thank you, [genie_name]."
                hide screen h_head2     
                m "Oh... yes... this feels great..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                hide screen h_head2     
                m "Oh... So tight..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_143.png" # HERMIONE
                her "................"
                hide screen h_head2     
                m "Why are you being so quiet [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Because this is painful..."
                her "And I just want you to cum sooner, [genie_name]..."
                hide screen h_head2     
                m "So you stifle your cries of pain?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "yes [genie_name]. *Sob!*"
                hide screen h_head2     
                m "Don't do that."
                m "Sob, scream and cry as much as you wish!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "B-but--"
                hide screen h_head2     
                m "That will make me cum sooner."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Really? *Sob!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*Sob!* It hurts! *Sob!* It hurts so much! *Sob!*"
                hide screen h_head2     
                m "Yes, yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*SOB!*"
                hide screen h_head2     
                m "You poor little kid..."
                m "A Big, evil man is raping your asshole!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_146.png" # HERMIONE
                her "*SOB!* Yeees! *SOB!*"
                hide screen h_head2     
                g4 "Argh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_147.png" # HERMIONE
                her "No, I'm scared! *SOB!*"
                hide screen h_head2   
        
        menu:
            "-Fill Hermione up with cum-":
                g4 "Argh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE  
                her "No! AH!"
                hide screen h_head2    
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "AH! IT'S FILLING ME UP!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                
                
                g4 "Yes, you whore! Yes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "It hurts, it hurts!"
                hide screen h_head2         
                g4 "Shut up!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_149.png" # HERMIONE
                her "No, I am already full! Stop cumming, you bastard!"
                hide screen h_head2      
                g4 "Shut the fuck up, slut! I am not done yet!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_146.png" # HERMIONE
                her "No! Please! My stomach! I will explode!"
                hide screen h_head2   
                g4 "ARGH!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "No, I think I will throw up..."
                hide screen h_head2    
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_150.png" # HERMIONE
                play sound "sounds/burp.mp3"
                her "{size=+7}*BURP!*!!!!!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_151.png" # HERMIONE
                her "......................."
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "{size=+7}*GULP!*{/size}"  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*SOB!* I HATE YOU..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_148.png" # HERMIONE
                her "{size=+5}I HATE YOU AND YOUR NASTY OLD COCK?{/size}"
                her "{size=+5}I HATE YOU! YOU HEAR ME?!{/size}"
                hide screen h_head2   
                g4 "Agh...Shut it, whore!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*sob!* *Sob!*..."
                hide screen h_head2
                
                
                
                
                
                
                
                # AFTER CUM INSIDE
                
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "*Sob!*..."
                hide screen h_head2
                m "Whew!... I think that was the last of it."
                m "You alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Yes... *Sob!*"
                hide screen h_head2 
                m "Are You crying?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "My butt hurts, but I am alright, [genie_name]..."
                hide screen h_head2 
                m "Well, you took my dick stoically, I must say..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Thank you [genie_name]..."
                hide screen h_head2 

                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_152.png" # HERMIONE
                her "I apologize for saying that I hate you, [genie_name]..."
                her "And your cock is not nasty..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_153.png" # HERMIONE
                her "I don't know what's gotten into me..."
                hide screen h_head2
                g9 "My dick!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_153.png" # HERMIONE
                her2 "I suppose it's as when you call me a \"whore\". I know you actually don't mean it..."
                hide screen h_head2    
                m "Yeah, sure..."
                m "Does it still hurt?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_154.png" # HERMIONE  
                her "A little..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_155.png" # HERMIONE
                her "I also feel full and warm inside..."
                hide screen h_head2      
                m "You plan to keep it in? My cum I mean."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_156.png" # HERMIONE     
                her "Yes..."
                if daytime:
                    her2 "I hope it won't start leaking during my classes..."
                else:
                    her2 "I hope it won't start leaking before I get to my room..."
                hide screen h_head2 
                m "Well, good luck on your journey."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_155.png" # HERMIONE  
                her "Can I get paid now please?"
                hide screen h_head2 
                
                    
                
                
                
                
            "-Pull out and cum on Hermione-":
                
                $ g_c_u_pic = "sex_cum_out_ani"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ah...{image=textheart.png}{image=textheart.png}{image=textheart.png}"

                hide screen h_head2     
                g4 "Yes!!! Allover your ass!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ah... It's so hot!"
                hide screen h_head2          

                
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
                
                m "Well, I'm done... You can get off my desk now."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Yes, [genie_name]..."
                hide screen h_head2     
                m "You feeling alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Yes, [genie_name]. It still hurts a little, but..."
                hide screen h_head2     
                m "But what?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "But in a good way... [genie_name]."
                hide screen h_head2     
                m "In a good way, huh?"
                g9 "Heh... You cute, little mynx."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Can I get paid now, [genie_name]?"
                hide screen h_head2 

        
    elif request_31_points == 1: # FIRST EVENT <============================================================== EVENT 02
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE                     
        her "[genie_name]?"
        m "I will be buying another favour from you today..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "............."
        m "Care to guess what the favour will be?"
        m "You have three attempts to find out."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "..........."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "Anal sex?"
        g4 "Wha..........?!"
        g4 "How did you...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "Just a lucky guess, [genie_name]..."
        m "Sometimes you scare me, [hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3 
        jump lucky_guess
        
        
        
        
        
    elif request_31_points >= 2: # FIRST EVENT <============================================================== EVENT 03
        m "How about another assfuck, [hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE     
        her "Of course, [genie_name]."
        g9 "Come here, you little mynx!"
        hide screen hermione_main     
        with d3
        # SEX
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
        her "........"
        hide screen h_head2               
        m "Hm..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
        her "..........."
        hide screen h_head2
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ooooohhhhhhhhhhhh....{image=textheart.png}"
        hide screen h_head2
        g4 "Oh, ye-es!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Ah..."
        hide screen h_head2
        m "It seems like your butthole became a bit more welcoming, [hermione_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE
        her "Ah... It still hurts a little."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_129.png" # HERMIONE
        her "And please, just call me \"whore\", [genie_name]."
        hide screen h_head2
        g4 "Agh! You slut! You always get me with your words!"



        
        
        
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3    
        
        
        
        
        
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        # INSERTION
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ah... Ah..."
        her "Ah..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE
        her "[genie_name]?"
        hide screen h_head2
        m "Yes, whore?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Em..."
        hide screen h_head2
        hide screen ctc
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Would you marry me, [genie_name]?"
        hide screen h_head2
        with hpunch
        g4 "{size=+9} WHAT?!{/size}"
        g4 "Don't tell me you're pregnant, [hermione_name]!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
        her "I Couldn't get pregnant the way we are doing it, [genie_name]..."
        hide screen h_head2
        m "What is this talk of marriage then?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "You misunderstood me [genie_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her "I meant to say, would you marry a girl {size=+5}like{/size} me?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
        her2 "I would never propose to a man with his cock in my ass, [genie_name]..."
        hide screen h_head2
        m "Good. Because I don't think any man would be able to say \"no\" to then."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ah{image=textheart.png}..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her2 "What I meant... ah{image=textheart.png} {w} ...to say was ah{image=textheart.png}... {w}...do you think someone would ever ah{image=textheart.png}... {w} ...want to marry a girl like me?"
        hide screen h_head2
        m "Huh?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her "I mean, with all that was happening lately... ah{image=textheart.png}..."
        her "I can't help but feel unclean... damaged even."
        her "And in a no way innocent..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Who would want a wife like that?"
        hide screen h_head2  
        menu:
            m "..."
            "\"I would marry you in a heartbeat!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "What?"
                hide screen h_head2  
                m "Well, hypothetically speaking of course..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_54.png" # HERMIONE
                her "...of course...{image=textheart.png}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_53.png" # HERMIONE
                her ".............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                her "But why do you say that, [genie_name]?"
                hide screen h_head2  
                m "Huh?"
                m "What do you mean \"why\", whore?"
                m "You are young and attractive..."
                m "Tight asshole, full tits and wet little pussy..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her "Ah...{image=textheart.png}"
                hide screen h_head2  
                m "You will make some lucky guy a very happy man one day, whore."
                m "Ehm, I mean, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "No, \"whore\" is good. Call me that, [genie_name]."
                hide screen h_head2  
                m "There, you see? You are a great catch, I'm telling you, whore."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Ah...{image=textheart.png} Thank you, [genie_name]."
                hide screen h_head2  
                m "Huh?"
                m "Are you crying?"
                label among_other_things:
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Among other things, [genie_name]...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                m "Among other things?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_135.png" # HERMIONE
                her "I'm cumming [genie_name]...{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                g4 "Agh! My cock!" 
                g4 "Relax your muscles a little, would you?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "BUT I'M CUMMING!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2  
                g4 "Fine! Have it your way whore!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}"
                hide screen h_head2  
                g4 "{size=+7}Argh!{/size}"
                
            "\"Marriage is out of the picture for you.\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_143.png" # HERMIONE
                her "That's what I thought..."
                hide screen h_head2  
                m "Oh... I just love that little asshole of yours!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "....................."
                her2 "Yes... After all the things I had to do for my house..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "...no one will ever want me..."
                hide screen h_head2  
                m "Oh, they will want you alright!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "What? But you said..."
                hide screen h_head2  
                m "Marriage, [hermione_name]. Marriage is impossible for you."
                m "But as a man-pleaser you are a great catch!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Really?"
                hide screen h_head2  
                m "Are you kidding me?!"
                m "Young, hot and slutty. You could have any man you want!"
                m "Or a wizard or whatever you are into..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_157.png" # HERMIONE
                her "I think you may be right, [genie_name]."
                hide screen h_head2  
                m "I know I am right, whore."
                m "Now wiggle that little ass of yours a little."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Like this?"
                hide screen h_head2  
                m  "Yes, that's a good whore."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "I am a whore, aren't I?"
                hide screen h_head2  
                m "You just sold me your asshole for 90 house points. How would you call that?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Yes, yes...{image=textheart.png} I am a whore...{image=textheart.png}"
                hide screen h_head2  
                m "Are you crying?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "-Fill Hermione up with cum-":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                hide screen h_head2 
                m "Yes! Argh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ah!{image=textheart.png} It's filling me up!{image=textheart.png} I can feel it!{image=textheart.png}"
                hide screen h_head2 
                m "Shut up, whore!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_137.png" # HERMIONE
                her "Ah! I AM A WHORE!!!!{image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2 
                m "Agh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Ah...{image=textheart.png} your cum, [genie_name]...{image=textheart.png}"
                hide screen h_head2 
                m "Yes, yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "Ah...{image=textheart.png}"
                hide screen h_head2          
                m "......"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
            "-Cum allover Hermione-":
                
                $ g_c_u_pic = "sex_cum_out_ani"
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
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ah-aha! You're cumming! {image=textheart.png}{image=textheart.png}{image=textheart.png}"
                hide screen h_head2    
                g4 "{size=+7}Yes I do, whore!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_147.png" # HERMIONE
                her "Ah, me too! Me too!"
                hide screen h_head2    
                g4 "{size=+7}FUCKING SLUT!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Ah...{image=textheart.png} your cum...{image=textheart.png}"
                her "I'm so full...{image=textheart.png}{image=textheart.png}{image=textheart.png}"


                hide screen h_head2     
                g4 "Yes!!! All over your ass!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ah... It's so hot!"
                hide screen h_head2          

                
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7

                
                
                
                
                
                
                
                
                
                
                
               
              
        #Ending
        m "Well, this was intense..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Ah-ha...{image=textheart.png} ah...{image=textheart.png}"
        hide screen h_head2   
        m "Are You alright, [hermione_name]?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "I think so... I'm not sure..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "I think I may still be cumming, [genie_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Or maybe not..."
        her "Everything is in a daze... and my legs feel so weak..."
        if whoring <= 23:
            her "Can I just get paid now, [genie_name]?"
        hide screen h_head2                                                             # HERMIONE

        
    
    stop music fadeout 1.0
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
 
 
    if whoring <= 23:
        m "Yes, [hermione_name]. 90 points to \"Gryffindor\"." 
        $ gryffindor +=90
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_141.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 23: # Level 08 <
        $ whoring +=1

    if request_31_points == 0:
        $ new_request_31_01 = True # HEARTS.
    if request_31_points == 1:
        $ new_request_31_02 = True # HEARTS.
    if request_31_points >= 2:
        $ new_request_31_03 = True # HEARTS.


    $ request_31_points += 1

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

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   

    





###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night) ############################################################################
label new_request_12: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3
    if request_12_points == 0:
        m "{size=-4}(I feel like playing with those titties.){/size}"
    else:
        m "{size=-4}(I feel like playing with those titties again.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    if whoring <=8:
        jump too_much
        
    if request_12_points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.
        m "[hermione_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, [genie_name]?"
        m "How about selling me another favour today?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Uhm... Alright..."
        her "What will it be, [genie_name]?"
        m "Well, how about you come closer and bare your tits for me...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "!!!"
        m "I want to give them a good squeeze."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name] Dumbledore! Don't you think this is too much?"
        m "You think?"
        her "I am not one of those harlots from \"Slytherin\", you know..."
        m "I know... You are from \"Gryfonmon\"... or something..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And if I don't feel like it I don't have to sell you a single favour, [genie_name]!"
        m "Of course..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "..................."
        m "I'll give you 35 house points for this."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "......................."
        her "All you are going to do is watch, [genie_name]?"
        m "Well, I feel more like touching, actually..."
        her "...................................."


    else: # Intro. Not first time.
        if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.
            m "[hermione_name]..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "[genie_name]?"
            m "I feel like playing with your tits a little..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "[genie_name]... I'd prefer it if you wouldn't make me such offers..."
            m "Why? Too hard to resist?"
            her "Nothing like that, [genie_name]."
            m "I'll give you 35 house points for this..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her ".................."
            her "Well, alright... You can touch them a little..."
        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.
            m "[hermione_name]..."
            
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE              
            her "[genie_name]?"
            m "I feel like playing with your tits a little..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Of course [genie_name]..."
    
    hide screen hermione_main
    with d3
    hide screen blktone
    with d3
    hide screen bld1
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 1
    show screen blkfade
    with Dissolve(1)
    pause.5


    hide screen hermione_walk_01
    hide screen genie
    show screen ctc
    #show screen chair_02 #Genie's chair.
    hide screen genie
    show screen genie_and_tits_01
    with d1
    hide screen blkfade
    with d5
    stop music fadeout 1.0
    pause
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    show screen blktone 
    with d3
    hide screen hermione_main
    with d3
    $ h_body = "01_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    #$ only_upper = True #No lower body displayed. 
    $ badges = False
    show screen hermione_main
    with d3
    pause
    her "...................................."
    
    
    
    
    
    menu:
        m "..."
        "-Grab them-":
            label no_smacking_tits:
                pass
            hide screen hermione_main
            with d3
            show screen blkfade
            with d5
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            with d1
            hide screen blkfade
            hide screen blktone
            with d5
            pause
            show screen bld1
            with d3
            

            
            if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).

                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her ".............................."
                hide screen h_head2    
                m "You have great tits, [hermione_name]..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "...................................."
                hide screen h_head2 
                m "You like it when I squeeze them like this?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Excuse me, [genie_name], but you are confusing me with one of those lowly harlots again..."
                her2 "I am only letting you fondle me because I am getting paid for it..."
                her "Not because I enjoy it..."
                hide screen h_head2 
                m "I see..."
                m "So, you're more like a prostitute then..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE
                her "[genie_name]!"
                her "Prostitutes are getting paid to have sex with men..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her "I'd never do something like that!"
                hide screen h_head2 
                show screen blktone
                with d3
                ">You squeeze one of the girl's tits tightly and give the other a couple of firm tugs."
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Ah..."
                hide screen h_head2 
                m "Enjoying yourself, [hermione_name]?"
                if whoring >= 9 and whoring <= 11: # LEVEL 04 #  <=================================================================================== FIRST EVENT.
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_120.png"   # HERMIONE
                    her "[genie_name], I am only doing this--"
                    hide screen h_head2 
                    show screen blktone
                    with d3
                    ">You squeeze both of her tits with force..."
                    hide screen blktone
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_132.png"   # HERMIONE
                    her "ah..."
                    hide screen h_head2 
                    m "Tell me you like this, [hermione_name]!"
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_131.png"   # HERMIONE
                    her "[genie_name], I am only letting you do this to me because--"
                    hide screen h_head2 
                    m "I know, know..."
                    m "You are starting to sound like a broken record."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_79.png"   # HERMIONE
                    her "...."
                    hide screen h_head2 
                    show screen blktone
                    with d3
                    show screen blkfade
                    with d7

                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc
                    $ only_upper = False #Bottom is displayed.

            
                    ">You let go of the girl's breasts..."
                else:  # LEVEL 05 # <=================================================================================== SECOND EVENT.
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png"   # HERMIONE
                    her "Ah..."
                    hide screen h_head2
                    show screen blktone
                    with d3
                    ">You squeeze her tits a few more times, then give them a firm tug..."
                    hide screen blktone
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "Ah... [genie_name]..."
                    hide screen h_head2
                    m "What? You do enjoy this, don't you?"
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "No... I..."
                    hide screen h_head2
                    m "Don't you lie to your headmaster, [hermione_name]!"
                    show screen blktone
                    with d3
                    ">You squeeze her tits again..."
                    hide screen blktone 
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png"   # HERMIONE
                    her "Ah..."
                    her "I am not lying, [genie_name]..."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "Why would I enjoy this?"
                    hide screen h_head2
                    m "I don't know [hermione_name]. You tell me."
                    show screen blktone
                    with d3
                    ">You keep massaging her breasts..."
                    hide screen blktone
                    with d3
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png"   # HERMIONE
                    her "Ah... I..."
                    hide screen h_head2
                    m "Yes, what is it?"
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png"   # HERMIONE
                    her "It's... It's nothing, [genie_name]..."
                    hide screen h_head2
                    m "Oh, I think it's something."
                    m "I think you like me squeezing your tits like this."      
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png"   # HERMIONE
                    her "[genie_name], please..."
                    if daytime:
                        her "The classes are about to start..."
                    else: 
                        her "It's getting late..."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png"   # HERMIONE
                    her "Can I go now, [genie_name]? Please?"
                    hide screen h_head2
                    show screen blkfade 
                    with d3
                    m "Sure, go ahead..."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png"   # HERMIONE
                    her "..............."
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png"   # HERMIONE
                    her "[genie_name], your are still... Holding me..."
                    hide screen h_head2
                    m "Oh, right... my bad...."
                    ">You let go of Hermione's breasts..."
                    
                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc
                    $ only_upper = False #Bottom is displayed.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
               
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png"   # HERMIONE
                her "Ah..."
                hide screen h_head2
                m "A bit sensitive today, aren't you?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_128.png"   # HERMIONE
                her "I suppose..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png"   # HERMIONE
                her "Ah..."
                hide screen h_head2
                m "You like it when I squeeze them like this?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_128.png"   # HERMIONE
                her "I do, [genie_name]... Ah..."
                hide screen h_head2
                m "Heh..."
                m "What if I pinch your nipples?"
                show screen blktone
                with d5
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png"   # HERMIONE
                her "!!!"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png"   # HERMIONE
                her "Ah! [genie_name]..."
                hide screen h_head2
                m "And what if I do this?"
                show screen blktone8
                with d3
                ">You grab the girl by her hard nipples and start pulling..."
                hide screen blktone8
                with d3
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png"   # HERMIONE
                her "Ah... Ah... Ah... [genie_name]..."
                hide screen h_head2
                m "What if I pull even harder?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png"   # HERMIONE
                her "Ah... [genie_name], please..."
                hide screen h_head2
                show screen blktone8
                with d3
                ">Hermione clutches the edge of your desk to keep herself form taking a step towards you..."
                hide screen blktone8
                with d3
                m "Good girl..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png"   # HERMIONE
                her "*Panting heavily*"
                hide screen h_head2
                m "Do you enjoy this?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png"   # HERMIONE
                her "You are hurting me, [genie_name]..."
                hide screen h_head2
                m "But do you enjoy it?"
                show screen h_head2                                                                 # HERMIONE
                if whoring <= 17:
                    $ h_body = "01_hp/13_hermione_main/body_140.png"   # HERMIONE
                    her "Ah... Yes, [genie_name]... I don't know why, but I do..."
                else:
                    $ h_body = "01_hp/13_hermione_main/body_138.png"   # HERMIONE
                    her "Ah... Yes, [genie_name]... I love it..."
                hide screen h_head2
                m "Good girl..."
                show screen blktone8
                with d3
                ">You let go of her nipples..."
                hide screen blktone8
                with d3
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png"   # HERMIONE
                her "Ah..."
                hide screen h_head2
                show screen blkfade
                with d5
                m "This will be all for today, [hermione_name]..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png"   # HERMIONE
                her "Oh...?"
                hide screen h_head2
                m "What is it? You look disappointed."
                m "I will pay you of course..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png"   # HERMIONE
                her "That's not it, [genie_name]..."
                her "It's..."
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png"   # HERMIONE
                if daytime:
                    her2 "It's just that I still have some time left before I have to leave for the classes and..."
                else:
                    her "It's not really that late yet, is it?"
                her "uhm..."
                her "..................."
                hide screen h_head2
                m "You want me to hurt you some more, don't you?"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png"   # HERMIONE
                if whoring <= 17:
                    her "I don't \"want to\"... "
                    show screen h_head2                                                                 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_138.png"   # HERMIONE
                    her "But if you insist [genie_name]..."
                    hide screen h_head2
                    m "Well, I do insist... apparently."
                else:
                    her "Yes please [genie_name]"
                    show screen h_head2                                                                 # HERMIONE
                    her "I'll even let you do it for free..."
                    hide screen h_head2
                    m "Well, in that case"
                show screen h_head2                                                                 # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png"   # HERMIONE
                her "Ah..."
                hide screen h_head2
                hide screen blkfade
                with d5
                
                show screen ctc
                pause
                hide screen ctc
                
                #BLACK FADE
                show screen blkfade
                with d7
                ">You spend some more time with Hermione's breasts..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                $ only_upper = False #Bottom is displayed.

        "-Slap them-":
            hide screen hermione_main
            with d5
            ">You give Hermione's tits a loud slap!"
            $ renpy.play('sounds/slap.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            if whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "!!!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/183.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Ouch! It hurts! *SOB!*"
                m "Did you like it though?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Did I... \"like it\, [genie_name]..?"
                her "What girl in her right mind would like to be treated this way?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/184.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                stop music fadeout 1.0
                her "You are a mean and demented old man!"
                hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                show screen blkfade
                with d3
                # RUNS OFF
                $ mad += 20
                m "............"
                m "Well, no points for \"Gryffindor\" then..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                $ only_upper = False #Bottom is displayed.
                hide screen genie_and_tits_01
                call music_block
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                    
            elif whoring >= 12 and whoring <= 14: # LEVEL 05 # <=================================================================================== SECOND EVENT.
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "!!!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/183.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Ouch!"
                her "[genie_name], what did you do this for?"
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "...Of course, not, [genie_name]."
                m "Let's try this again, then."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "What?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3   
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "!!!"
                her "Ouch! Stop hurting me!"
                m "Admit that you enjoy it and I will."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "But I don't..."
                her "And if you plan to keep on doing this to me, [genie_name]..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "...then I think I should leave."
                m "Fine, fine..."
                hide screen hermione_main
                with d3
                jump no_smacking_tits #Jumps to usual tits molesting scene.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/182.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "Ah!!!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/185.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "[genie_name], why did you do that?"
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her ".........."
                her "I am not a pervert..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">You give Hermione's tits another loud smack!"
                hide screen blktone8
                with d3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/186.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "A-ah!!!"
                m "Tell me you like it!"
                her "[genie_name]... I..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d5
                ">You unleash a whole series of slaps!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                ">Hermione's tits bounce allover the place, completely out of control"
                hide screen blktone8
                with d5
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/187.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "A-ah!!! Ah!!! A-a-aha!!!"
                m "You enjoy this. Admit it."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/188.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                her "..........."
                hide screen hermione_main
                hide screen ctc
                with d3
                ">You smack her tits again."
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/187.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                her "A-ah! Yes! I do, I do! A-ah..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/184.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                her "...does this mean I'm a pervert, [genie_name]?"
                m "What?"
                m "Stop being silly, [hermione_name]."
                m "It is completely natural for a girl to enjoy her tits getting smacked around a little."
                her "......"
                her "Are you sure about that, [genie_name]?"
                m "Yes. Believe me, I know."
                hide screen hermione_main
                with d3
                ">You give her tits one more slap!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/187.png" #Sprite of Hermione's upper body.                                                                           #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                her "A-ah... Yes... Thank you, [genie_name]."
                hide screen hermione_main
                with d3
                m "Well... Enough with the slapping for now..."
                jump no_smacking_tits #Jumps to usual tits molesting scene.

    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    stop music fadeout 1.0
    if whoring <= 17:
        m "Yes, [hermione_name].  35 points to \"Gryffindor\"." 
        $ gryffindor +=35
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    $ badges = True
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 11: # If still of level of unlocking - 04
        $ whoring +=1

    $ request_12_points += 1

    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_12_01 = True # HEARTS.
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_12_02 = True # HEARTS.
    if whoring >= 15:
        $ level = "06"
        $ new_request_12_03 = True # HEARTS.


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

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
   
    





###################REQUEST_10 (Level 03) (25 pt.) (Let a classmate touch you). (Available during daytime only).
label new_request_10:
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to go get touched by one of her classmates?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
    
    if request_10_points == 0: # <================================================================================ FIRST TIME
        m "[hermione_name]?"
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Flashing panties
        show screen hermione_main
        with d3
        her "[genie_name]?"
        m "You do like boys your age, don't you?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_03.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "...?"
        m "one of your classmates maybe?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_10.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Well..."
        her "Must I really discuss things like this with you, [genie_name]?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "It's a bit embarrassing..."
        m "Sure, I understand. I don't need to know the details..."
        m "But here is what I need you to do today, [hermione_name]."
        m "Go confront that boy you fancy. The one you think is \"just so dreamy\"..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her ".......?"
        m "And let him touch you..."
        if whoring <=5 or request_02_c_points <= 1: # Counts how many times Hermione been sent to flirt with teachers.
            jump too_much
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Let him... touch me, [genie_name]?"
        m "Yes, touch you. The way boys touch girls?"
        m "How old are you, [hermione_name]? You look mature enough..."
        m "Haven't you had \"the talk\" with your parents already?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "\"The talk\", [genie_name]?"
        m "Yes, \"the talk\"! About how boys are different than the girls...?"
        m "Boys have a \"pee-pee\" and girls like to put that  \"pee-pee\" in their mouths?"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_03.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "!!!"
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "What kind of demented parent would have such a talk with their child?"
        m "I bet Akabur would."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "I beg your parodon, [genie_name]?"
        m "*Khem!* I said, a responsible and caring one!"
        m "Well, in any case. That is your task for today, [hermione_name]."
        m "Find a way to persuade one of your classmates to fondle you a little..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her ".........."
        m "You are a pretty girl, it shouldn't be too hard."
        her "....................."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "How many points would I receive after completing such a task, [genie_name]?"
        m "Hm... Twenty five should do..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Twenty five house points..."
        her "...."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "Well, so be it then..."
        m "Great..."
        hide screen hermione_main                                                                  # HERMIONE
        with d3                                                                                                       # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_05.png"                # HERMIONE
        show screen hermione_main                                                               # HERMIONE
        with d3                                                                                                      # HERMIONE
        her "I'd better go now. The classes are about to start..."
        hide screen hermione_main
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 
            m "[hermione_name]?"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Flashing panties
            show screen hermione_main
            with d3
            her "[genie_name]?"
            m "How about you go let one of your classmates molest you a little again?"
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "........"
            m "Twenty five house points, [hermione_name]."
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_69.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "[genie_name], it's just..."
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_79.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "I do not understand why I must do things like that..."
            m "To help out your house?"
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_66.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "That's not what I meant..."
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_69.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "Oh, never mind..."
            her "The classes are about to start, I'd better go..."
            m "Will you do it?"
            hide screen hermione_main                                                                  # HERMIONE
            with d3                                                                                                       # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_66.png"                # HERMIONE
            show screen hermione_main                                                               # HERMIONE
            with d3                                                                                                      # HERMIONE
            her "I don't know... Maybe..."
            hide screen hermione_main
        elif whoring >= 9 and whoring <= 11: # LEVEL 04
            m "[hermione_name], I need you to go out there, and make one of your classmates molest you a little."
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Flashing panties
            show screen hermione_main
            with d3
            her "I understand, [genie_name]..."
            m "Off you go then."
            her "..........."
            hide screen hermione_main
        elif whoring >= 12: # LEVEL 05+
            m "[hermione_name], I need you to go out there..."
            m "Find a handsome guy and force yourself on him!"
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Flashing panties
            show screen hermione_main
            with d3
            her "You mean like..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "In a sexual way, [genie_name]?"
            m "What? No, I mean just let him get under your uniform that's all..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Oh, I see..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I wonder who it should be this time..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "More than one boy, is not a problem, is it, [genie_name]?"
            m "A problem? Of course not!"
            m "If anything - it is encouraged." 
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Great. I will see you after the classes then, [genie_name]. As usual."
            m "Yes. Good luck."
            hide screen hermione_main

   

    $ request_10 = True

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
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)


    $ hermione_takes_classes = True
    jump day_main_menu

        
label new_request_10_complete: #<==========================================================================EVENING
    
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
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    show screen hermione_02
    with Dissolve(.3)
    
    her "Good evening, [genie_name]."
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
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "......"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Well... Em..."
                m "Speak up, [hermione_name]."
                m "Did you let some lucky guy feel you up or what?"
                    
                if one_out_of_three == 1: ### EVENT (A)
                    her "I did, [genie_name]..."
                    m "So? Tell me more."
                    her "Well, there is not much to tell..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I told that one guy I know that he could touch me a little if he wants..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "He thought I was joking at first..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "So embarrassing..."
                    m "So, did he cop a feel or not?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "He did..."
                    m "Well, where did he touch you, [hermione_name]?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ehm... My legs..."
                    her "And my breasts a little I suppose..."
                    m "That's all?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Yes, [genie_name]..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "It's getting late... I think I'd better leave now..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I'm sorry, [genie_name]..."
                    m "Nothing to be sorry about, [hermione_name]."
                    m "You did good. This will do for now."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 3.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I did, [genie_name]."
                    her "But it was all very awkward and embarrassing..."
                    m "That's the whole point of it, [hermione_name]."
                    m "Tell me where you were touched today..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "Ehm..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well he touched me under my skirt a little..."
                    her "Then I let him rub my..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "...my pussy through the panties, [genie_name]."
                    m "Very good. Then what happened?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_131.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Then he sort of started to touch himself [genie_name]..."
                    her "So, I decided to leave..."
                    m "I see..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "............."
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    her "I did, [genie_name]..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "I led this one guy from \"Hufflepuff\" to an empty classroom and I told him that he can touch me if he wants."
                    her "That I don't mind..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "..........."
                    m "And?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well, he did touch me a little at first..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "......"
                    m "Don't make me pull every word out of you, [hermione_name]!"
                    m "Then what happened?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well..."
                    stop music fadeout 1.0
                    her "I think he was more interested in {size=+5}me{/size} molesting {size=+5}him{/size}..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "He asked me to call him a \"sissy boy\"..."
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "And he kept on reassuring me that he has a very small penis..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "He just kept repeating that *sob!*..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Why would anyone be like this?"
                    her "*Sob!* I Could not stay in his company a moment longer, so I just ran."
                    m "I'm sorry to hear this..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "It was truly awful, [genie_name]..."
                    m "There, there..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_23.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Sob!*"
                    m "Will ten extra points make you feel better?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_19.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Huh? That would be very sweet of you [genie_name]."
                    m "Of course... Ten extra points to \"Gryffindor\"."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_140.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Thank you [genie_name]..."
                    m "And the rest of your payment..."
            
            elif whoring >= 9 and whoring <= 11: # LEVEL 04
                if one_out_of_three == 1: ### EVENT (A)
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well... There is not much to tell..."
                    her "I found this one boy from \"Ravenclaw\"..."
                    her "Led him to one of the empty classrooms in the eastern wing..."
                    her "He thought I wanted to make out with him..."
                    her "But I told him that I just want him to touch me..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "...so he did."
                    m "I see..."
                    m "Well done, [hermione_name]."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Will I be getting my points now?"
                    m "In a minute, [hermione_name]. I have a question I would like to ask you before that."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "???"
                    m "Did you enjoy it?"
                    m "Did it feel good to be touched by that boy?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Oh..."
                    her "Well, he was rather handsome I suppose..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I didn't hate it, if that's what you mean, [genie_name]..."
                    m "I see..."
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well..."
                    her "I'm not sure whether or not this counts, but..."
                    her "During the herbology class today..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I let this one boy slide his hand under my skirt..."
                    her "So while Professor Sprout explained the differences between \"mandrake\" and \"mandragore\"..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Something I already knew of course..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I let my lab partner massage my buttocks..."
                    her "And that is all..."
                    m "Hm..."
                    menu:
                        "\"You can do better than that, [hermione_name].\"":
                            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                            show screen hermione_main                                                                                                                                                                                 #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            her "Yes, I know, [genie_name]. I am sorry."
                            m "Just make sure you try harder next time."
                            her "I will, [genie_name]."
                        "\"Kudos on doing this during class.\"":
                            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                            show screen hermione_main                                                                                                                                                                                 #HERMIONE
                            with d3                                                                                                                                                                                                                        #HERMIONE
                            her "Thank you, [genie_name]."
                            m "I say you deserve to get paid."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "................."
                    m "???"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    
                    her "I don't want to talk about it, [genie_name]..." 
                    m "What happened, [hermione_name]. Spit it out."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "................."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "But... it's so embarrassing..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Do I really have to, [genie_name]?"
                    m "Yes, I happen to love embarrassing things!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "................."
                    her "Well, alright..."
                    her "I approached this one guy that I always found attractive..."
                    her "Managed to muster up enough courage to ask him to follow me..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Normally I wouldn't dare..."
                    her "But the fact that I was doing this as a task entrusted to me by someone else..."
                    her "made it easier somehow..."
                    m "Happy to help, [hermione_name]."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I led him to the library..."
                    her "We found a secluded spot behind one of the book shelves..."
                    her "And I told him that he can touch me wherever he wants..."                 
                    her "And...."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_88.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her ".........."
                    m "What?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "....................."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/Despair_by_erenik.mp3" fadein 1 fadeout 1 # SAD THEME.
                    her "He started to touch my... feet, [genie_name]."
                    m "Huh?"
                    m "Your \"Feet\"? Is that what kids call tits these days?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I'd wish, [genie_name]..."
                    her "He asked me to take off my shoes..."
                    her "Then he..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_21.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "He started to smell my toes, [genie_name]!"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_22.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I felt so... violated!"
                    m "So he didn't touch your tits, or your butt?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_143.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "No, [genie_name]... *sob!*"
                    m "Alright, then what happened?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_142.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Nothing! I couldn't bear the humiliation... I just ran..."
                    her "I even left my shoes behind and had to come back later to pick them up..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Sob!*............"
                    m "Hm..."
                    m "Well, you did get molested..."
                    m "Although in a rather unconventional manner..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_145.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "*Sob!* I wish he would have just touched my breasts like a descent boy would, [genie_name]... *Sob!*"
                    m "There, there..."
                    m "You earned you pay today..."
        
        
        
            elif whoring >= 12: # LEVEL 05+
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "......"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Well..."
                    her "During the potions class today..."
                    her "I wrote a note on a piece of paper..."
                    her "I was about to slide it to my lab partner when..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Professor Snape snatched it right out of my hand..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "He then read it out loud before the entire class..."
                    m "What did the note say?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Well..."
                    her "It said: \"You can touch my butt if you want. I bet professor Snape would never notice.\""
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Everyone was laughing..."
                    her "It was so embarrassing I wanted to die..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "I really hate professor Snape, [genie_name]..."
                    m "What happened then?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "Nothing..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "But when the class was over..."
                    her "Those three nasty-looking boys from \"Slytherin\" cornered me..."
                    her "Actually they weren't mean to me or anything..."
                    her "So we just waited for everyone to leave the classroom..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "And then I let them touch me..."
                    her "They touched me everywhere, [genie_name]..."
                    m "\"Everywhere\", huh?"
                    her "Yes... Everywhere, [genie_name]..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "There were hands under my skirt, under my shirt..."
                    her "And then I started to breathe heavily..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "So one of them just put his hand over my mouth..."
                    her "And their hands were so... thorough..." 
                    her "My head started to spin..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3       
                    her "It was most exhilarating, [genie_name]."
                    m "Very good, [hermione_name]. Very good indeed."
                    
                    
                if one_out_of_three == 2: ### EVENT (B)
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Actually something quite unexpected happened to me today, [genie_name]..."
                    her "Right after the Defence Against the Dark Arts class..."
                    her "This stocky \"Hufflepuff \" boy came up to me..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "He said someone told him that I let boys touch me..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Normally I would deny everything..."
                    her "But I decided not to waste the opportunity..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I took the boy to a quiet spot and let him touch me..."
                    her "I let him run his hands up and down my thighs..."
                    her "I let him fondle my breasts..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "All the usual things..."
                    m "Well done, [hermione_name]."
                    
                if one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well..."
                    her "I did what you told me to do, [genie_name]..."
                    her "But... it sort of... ehm..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Well, it sort of escalated into something else..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "Hm?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "uhm..."
                    her "I sort of... got caught while I was letting this one boy fondle my breasts..."
                    m "You got caught? By one of the teachers?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "No, [genie_name]..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "By the boy's girlfriend..."
                    m "Interesting..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "She was furious with him at first..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "But then..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ehm... She started to touch my breasts as well..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Almost the same way her boyfriend did just a moment ago..."
                    her "Then she turned to him and she said..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "\"I love you baby, and I want to share everything with you...\""
                    her "\"...And that includes your whores.\""
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "I did not appreciate being called a whore of course..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "But that was such a sweet and romantic gesture..."
                    her "Wouldn't you agree, [genie_name]?"
                    m "Totally..."
                    m "Seems that true love {size=+5}does{/size} exist after all."
                    m "Then what happened?"
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "Ehm... Well, they kissed of course..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "And then they both started to touch me again..."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    her "And then he was kind of only touching her and she was only touching him..."
                    her "And they kissed..."
                    her "I suddenly felt like the third wheel in that situation, so I just slipped away quietly..."
                    m "I see..."
                    

    $ gryffindor +=25
    m "The \"Gryffindor\" house gets 25 points!"
    her "Thank you, [genie_name]."
    
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
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)



    $ touched_by_boy = True #Makes sure that Public favours do not get locked after reaching Whoring level 05.
    
    call music_block
    
    $ request_10_points += 1 
    $ request_10 = False 
    $ hermione_sleeping = True
    return

    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
