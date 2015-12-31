label new_personal_request:
    if slytherin > gryffindor or slytherin == gryffindor:
        show screen hermione_main
        $ menu_x = 0.2 #Default: 0.5
        
        label not_now:
        menu:
            "-Custom favours-":
                jump new_custom_request

            "-Personal favours-":
                label not_now2:
                ### LEVEL 01 ###
                menu:
                    "Favour: \"Talk to me\" {image=heart_0[new_request_01_heart]}":
                        jump new_request_01

                    "Favour: \"Nice panties\" {image=heart_0[new_request_02_heart]}": # LEVEL 1
                        jump new_request_02
                  
                    ### LEVEL 02 ###
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Panty thief\" {image=heart_0[new_request_03_heart]}" if imagination >= 2:
                        jump new_request_03
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Breast molester\" {image=heart_0[new_request_04_heart]}" if imagination >= 2: 
                        jump new_request_04
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Butt molester\" {image=heart_0[new_request_05_heart]}" if imagination >= 2:
                        jump new_request_05
                        
                    ### LEVEL 03 ### IMAGINATION == 3
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Show them to me!\" {image=heart_0[new_request_08_heart]}" if imagination >= 3:
                        jump new_request_08
                        
#                    "Favour: \"Show {size=+5}it{/size} to me! (NOT FINISHED YET)":
#                        jump new_request_09
                    
                    ### LEVEL 04 ### IMAGINATION == 3
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Dance for me!\" {image=heart_0[new_request_11_heart]}" if imagination >= 3:
                        jump new_request_11
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Let me touch them!\" {image=heart_0[new_request_12_heart]}" if imagination >= 3: # LEVEL 4
                        jump new_request_12
                        
                    ### LEVEL 05 ### IMAGINATION == 4
                    "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Favour: \"touch me!\" {image=heart_0[new_request_16_heart]}" if imagination >= 4: # LEVEL 5
                        jump new_request_16
                        
                    ### LEVEL 06 ### IMAGINATION == 4
                    "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Suck it!\" {image=heart_0[new_request_22_heart]}" if imagination >= 4: # LEVEL 6
                        jump new_request_22
                        
                    ### LEVEL 07 ### IMAGINATION == 5
                    "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Let's have sex!\" {image=heart_0[new_request_29_heart]}" if imagination >= 5: # LEVEL 7
                        jump new_request_29
                    
                    ### LEVEL 08 ###
                    "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Favour:  \"Time for anal!\" {image=heart_0[new_request_31_heart]}" if imagination >= 5: # LEVEL 8
                        jump new_request_31
                    
                    "-Cancel-":
                        jump new_personal_request
                
            "{color=#858585}-Public favours-{/color}" if not daytime:
                show screen blktone
                hide screen hermione_main
                with d3
                ">Public favours are available during the daytime only."
                hide screen blktone
                show screen hermione_main
                with d3
                jump not_now
            "-Public favours-" if daytime:
                if lock_public_favors:
                    her "Em... [genie_name]..."
                    her "I do not mind to keep selling you the favours..."
                    her "But only as long as we keep them private..."
                    jump new_personal_request
                else:
                    label not_now3:
                    menu:
                        ### LEVEL 01 ### 
                        "Favour: \"She's a flirt\"" if daytime:
                            jump new_request_02_b
                            
                        ### LEVEL 02 ### IMAGINATION == 2
                        "{color=#858585}-A vague idea-{/color}" if imagination < 2:
                            call vague_idea
                            jump not_now3
                        "Favour: \"She's bait\"" if daytime  and imagination >= 2:
                            jump new_request_02_c
                        
                        ### LEVEL 03 ### IMAGINATION == 3
                        "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Let a classmate molest you.\"" if imagination >= 3: # LEVEL 3
                            jump new_request_10
                        
                        ### LEVEL 04 ### IMAGINATION == 3
                        "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Flash your tits to a classmate.\"" if imagination >= 3: # LEVEL 4
                            jump new_request_15
                        
                        
                        ### LEVEL 05 ### IMAGINATION == 4
                        "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Kiss a girl.\"" if imagination >= 4: # LEVEL 5
                            jump new_request_20
                            
                        ### LEVEL 06 ### IMAGINATION == 4
                        "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Give a handjob to a classmate.\"" if imagination >= 4: # LEVEL 6
                            jump new_request_23
                            
                        ### LEVEL 07 ### IMAGINATION == 5
                        "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Give a blowjob to a classmate\"" if imagination >= 5:# LEVEL 7
                            jump new_request_24
                                
                         ### LEVEL 08 ### IMAGINATION == 5
                        "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Have sex with a classmate\"" if imagination >= 5:# LEVEL 8
                            jump new_request_30
                        
                        "-Cancel-":
                            jump new_personal_request
            "{color=#858585}-Potions-{/color}" if not daytime:
                show screen blktone
                hide screen hermione_main
                with d3
                ">Potions are available during the daytime only."
                hide screen blktone
                show screen hermione_main
                with d3
                jump not_now
            "-Potions-" if daytime:
                label request_potion_menu:
                menu:
                    "-Cat Ears-" if "Cat Transformation Potion" in p_inv:
                        if p_potion_names[3] in p_inv:
                            $ p_inv.remove(p_potion_names[3])
                            jump potion_scene_1
                        else:
                            m "I don't have this potion..."
                            jump request_potion_menu
                    "-Ass Expansion" if "Ass Expansion Potion" in p_inv:
                        if p_potion_names[1] in p_inv:
                            $ p_inv.remove(p_potion_names[1])
                            jump potion_scene_2_2
                        else:
                            m "I don't have this potion..."
                            jump request_potion_menu
                    "-Breast Expansion-" if "Breast Expansion Potion" in p_inv:
                        if p_potion_names[2] in p_inv:
                            $ p_inv.remove(p_potion_names[2])
                            jump potion_scene_2_1
                        else:
                            m "I don't have this potion..."
                            jump request_potion_menu
                    "-Cum Addiction-" if "Cum Addiction Potion" in p_inv:
                        if p_potion_names[0] in p_inv:
                            $ p_inv.remove(p_potion_names[0])
                            jump potion_scene_3
                        else:
                            m "I don't have this potion..."
                            jump request_potion_menu
                    "-Transparent Clothes-" if "Transparency Potion" in p_inv:
                        if p_potion_names[6] in p_inv:
                            $ p_inv.remove(p_potion_names[6])
                            jump potion_scene_4
                        else:
                            m "I don't have this potion..."
                            jump request_potion_menu
                    ##"-Snek-" if whoring >= 3:
                    ##    jump potion_scene_5
                    ##"-Polyjuice Potion-" if whoring >= 10:
                    ##    jump potion_scene_6
                    "-Nevermind -":
                        jump new_personal_request
            "-Public Shaming-" if collar >= 1:
                "Not coded yet. Sorry."
                jump new_personal_request
                ##menu:
                    ##"-Walk naked around the school-":
                    ##    jump public_event_1
                    ##"-Walk around the school with cum on your face-":
                    ##    jump public_event_2
                    ##"-Be lead around on a leash-":
                    ##    jump public_event_3
                    
            "-Never mind-":
                jump day_time_requests
    
        
        
        
        
                   
                    
                    
                        
                 
                     
                    
                   
                        
#                    "...flash your panties to a teacher.{image=3_stars_00.png}" if request_07_points == 0:
#                        jump new_request_07
#                    "...flash your panties to a teacher.{image=3_stars_01.png}" if request_07_points == 1:
#                        jump new_request_07
#                    "...flash your panties to a teacher.{image=3_stars_02.png}" if request_07_points == 2:
#                        jump new_request_07
#                    "...flash your panties to a teacher.{image=3_stars.png}" if request_07_points >= 3:
#                        jump new_request_07
                        
                    

#                    "\"Let me stick a finger up your butt.\"{image=3_stars_00.png}" if request_17_points == 0:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars_01.png}" if request_17_points == 1:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars_02.png}" if request_17_points == 2:
#                        jump new_request_17
#                    "\"Let me stick a finger up your butt.\"{image=3_stars.png}" if request_17_points >= 3:
#                        jump new_request_17
                        
#                    "\"Touch my cock a little.\"{image=3_stars_00.png}" if request_18_points == 0:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars_01.png}" if request_18_points == 1:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars_02.png}" if request_18_points == 2:
#                        jump new_request_18
#                    "\"Touch my cock a little.\"{image=3_stars.png}" if request_18_points >= 3:
#                        jump new_request_18
                    
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_00.png}" if request_19_points == 0:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_01.png}" if request_19_points == 1:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars_02.png}" if request_19_points == 2:
#                        jump new_request_19
#                    "\"Rub my cock against your cheeks.\"{image=3_stars.png}" if request_19_points >= 3:
#                        jump new_request_19
                        
                    
                   
#                    "\"Let me cum on your tits\"{image=3_stars_00.png}" if request_21_points == 0: # LEVEL 6
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars_01.png}" if request_21_points == 1:
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars_02.png}" if request_21_points == 2:
#                        jump new_request_21
#                    "\"Let me cum on your tits\"{image=3_stars.png}" if request_21_points >= 3:
#                        jump new_request_21
                            
                    


            
            

    else:
        her "The Gryffindors are in the lead. I don't need to do this."
        jump day_time_requests
                
################
### LEVEL 01 ###                
###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    hide screen hermione_main
    with d3
    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"
    menu:
        "\"(Yes, let's do that.)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request

    m "\"(Should I ask her to dress up?)\""
    menu:
        "\"(Yes, let's do it!)\"":
            m "[hermione_name], before I request a favor, I'd like you to dress up."
            $ changeHermioneMainScreen(hg_pth+"body_10.png")
            her "As what?"
            menu:
                "-A maid-" if "maid" in outfit_invintory:
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 1
                    $ stockings = 1
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                "-A Cheerleader-" if "gryffindor_cheerleader" in outfit_invintory:
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 2
                    $ stockings = 2
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                "-A Slytherin Cheerleader-" if "slytherin_cheerleader" in outfit_invintory:
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
                "-Ms Marvel-" if "ms_marvel" in outfit_invintory:
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 8
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                "-A heart dancer-" if "heart_dancer" in outfit_invintory:
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 4
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                "-power girl-" if "power_girl" in outfit_invintory:
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 7
                    $ panties = False
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass  
                "-Harley Quinn-" if "harley_quinn" in outfit_invintory:
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 9
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass                           
        "\"(Not right now.)\"":
            pass
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Alright then..."
    m "Just tell me some news about you."
    hide screen hermione_main
    with d3
    $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
    show screen hermione_main
    with d3
    if request_01 == 0: #First time this event taking place.
        her "Ehm... Alright..."
        her "I just stand here and talk then...? Like this?"
    else:
        her "Here in the middle, right? I remember..."
    hide screen hermione_main
    with d3
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen blktone 
    with d3
    show screen ctc
    show screen hermione_main
    with Dissolve(.3)
    pause
    
    m "Well?"
    if request_01 == 0 and whoring <=5: #First time this event taking place.
        $  new_request_01_01 = True #Hearts on menu buttons.
        $ new_request_01_heart = 1
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Em... very well..."
        ">Hermione is feeling confused..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "..................."
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
            $ level = "02"
            $  new_request_01_02 =True #Hearts on menu buttons.
            $ new_request_01_heart = 2
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "My life has been quite uneventful lately to be honest..."
        her "Apart from that day when I failed that test..."
        her "Still can't believe it happened..."
        menu: 
            "-Jerk off while she is talking-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                hide screen blktone
                with d3
                ">You reach under the desk and crab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                hide screen hermione_main
                with d3
                $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "[genie_name], what are you doing?"
                m "What, oh it's nothing. Just scratching my leg."
                m "You were saying?"
                hide screen hermione_main
                with d3
                $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Yes... Well, that test I failed..."
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Yes, what a tragedy that was..."
                her "Exactly! I'm glad you understand, [genie_name]."
                pass
        her "Come to think of it, I don't feel like talking about it anymore..."
        m "Alright, what else has happened lately?"
        her "Em... Well, I'm doing pretty well at herbology lately..."
        her "I mean, I always score the top marks, but I have been studying really hard anyway..."
        her "And now I sort of feel like sometimes I know more than professor Sprout herself..."
        if d_flag_01:
            m "{size=-4}(Yes... ah...){/size}"
        else:
            m "(Professor Sprout... He-he, what a ridiculous name...)"
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMION
        her "Did you say something [genie_name]?"
        m "It's nothing, keep going..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Well, some students are making fun of professor Quirell behind his back..."
        her "But I disapprove of such behavior of course."
        if d_flag_01:
            m "{size=-4}(Come on! Say something naughty!){/size}"
        else:
            m ".................."
        her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..."
        her "I'm very happy about that..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I think, given time, we will be able to make a real difference..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, it is so invigorating to know that you are doing the right thing!"
        her "Would't you agree profe         ssor?"
        if d_flag_01:
            m "{size=-4}(Dammit. Now she killed the mood completely...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            pass
        else:
            m "Zzzz........"
            
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name]?"
        m "Yes, yes, I'm totally listening..."
        m "This is all very self righteous, er..."
        m "I mean, very invigorating and stuff..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".........................."
  
    elif whoring >= 6: #LEVEL 03
        $  new_request_01_03 = True #Hearts on menu buttons.
        $ new_request_01_heart = 3
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "My life has been quite uneventful lately to be honest..."
        her "Hm..."
        her "There is a fierce competition going on between the \"Slytherin\" and the \"Gryffindor\" house."
        her "To be honest, [genie_name], there should be none..."
        her "\"Gryffindor\" would have been in the lead if not for those \"Slytherin\" harlots..."
        her "The things I hear those girls do simply to get a few extra points..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "How despicable!"
        m "What does this make you then, [hermione_name]?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Exactly!"
        m "Huh?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "I have to work even harder to compensate for the damage those nasty girls are doing..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370).
        show screen hermione_main
        with d3
        her "Thank you for helping me out, [genie_name]."
        menu: 
            "-Start jerking off-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                hide screen hermione_main
                with d3
                $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "[genie_name], what are you doing?"
                her "You are not.....?"
                hide screen hermione_main
                with d3
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Are you...?"
                m "What, it's nothing. Keep going."
                hide screen hermione_main
                with d3
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                show screen hermione_main
                with d3
                her "Hm..."
                m "{size=-4}(Is she onto me? Nah...){/size}"
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Don't mention it."
                pass
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Well, like I was saying..."
        her "I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points..."
        if d_flag_01:
            m "{size=-4}(What a slut... ah... Yes...){/size}"
        else:
            m "Ten points, huh?"
        her "Yes..."
        if d_flag_01:
            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "And these two other girls..."
            her "There is a rumor that they are actually sleeping with professor snape..."
            m "{size=-4}(Yes... Those little, nasty, \"slytherin\" sluts!){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "Also there was this one girl, who gave a teacher a handjob, right during class..."
            m "{size=-4}(Yes... This is good stuff, go on!){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "And this other girl, she sucked off a teacher!"
            m "{size=-4}(Yes! Yes!){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "And another girl let a teacher cum in her mouth..."
            her "And she swallowed it all and loved it!"
            m "{size=-4}(Wait... Is she making this up?){/size}"
            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "I'm a nasty girl too, you know..."
            g4 "What?!"
            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/body_65.png" #Sprite of Hermione's upper body.
            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            show screen hermione_main
            with d3
            her "I just want to suck a cock..."
            her "I want men to cum on my face like in those videos I saw!"
            g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"
            hide screen hermione_main
            with d3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Argh! YES!"
            hide screen hermione_main
            with d3
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            if False:
                "hermione upset about cum being wasted"
            else:
                if whoring <= 10:
                    $ mad = +7
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                    show screen bld1
                    with d3
                    show screen hermione_main
                    with d3
                    her "I knew it! You were touching yourself, [genie_name]!"
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    #show screen genie_jerking_off
                    with d3
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "This is disgusting! How could you!?"
                    her "[genie_name], you are the headmaster! You are supposed to set a good example!"
                    m "Hey, little missy, are you going to judge me or do you want your points?"
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "My points please, I believe I earned those."
                    m "Yes you did."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Ew... I feel so dirty now..."
                    hide screen genie_jerking_sperm_02
                    with d3
                else:
                    $ h_body = "01_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.
                    show screen bld1
                    with d3
                    show screen hermione_main
                    with d3
                    her "I knew it! You were touching yourself, [genie_name]!"
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    #show screen genie_jerking_off
                    with d3
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "How could you [genie_name]? In front of a young innocent student!"
                    m "Hey, little missy, what you were saying wasn't exactly innocent"
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "I don't know what you're talking about..."
                    m "I'm sure. Do you want your points or not?"
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "{size=-4}he sure did cum a lot{image=textheart.png}{/size}"
                    hide screen genie_jerking_sperm_02
                    with d3
        else:
            her "We need to put an end to this behavior, [genie_name]!"
            m "Yeah, sure..."
            her "So you agree with me then?"
            her "I think we need to implement a new penalty system to punish girls who are known to sell favours..."
            m "(All I heard was \"punish girls\"...)"
            her "This will also help the boys in our school to feel less discriminated against!"
            m "The boys?"
            m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
            her "I'm so glad that you understand my concerns, [genie_name]."
            m "Yes, yes, sure..."
        
        
                
                
        

    stop music fadeout 2.0
    
    if whoring >= 11:
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        her "Oh, don't worry about the points, we were just having a nice talk."
        m "Really? What about \"Gryffindor\" winning the cup?"
        her "It's just 5 points [genie_name]."
        m "If you say so."
        her "Will this be all then?"
        m "Yes, you can go now."
    else:
        $ gryffindor +=5
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        show screen hermione_main
        hide screen hermione_01_f #Hermione stands still.
        with d3
        her "Will this be all then?"
        if whoring >= 0 and whoring <= 2: #LEVEL 01
            her "*sigh of relief*"
        m "Yes, you can go now."
    if request_01 == 0:
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Another 5 points... The Guys will be so happy."
        her "Thank you, [genie_name]."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
    $ request_01 += 1
    
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)

    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ panties = True
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
        
###################REQUEST_02 (Level 01)
label new_request_02: #SHOW ME YOUR PANTIES
    hide screen hermione_main
    with d3
    m "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    show screen hermione_main
    her "So, what will it be [genie_name]?"
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."             
    if request_02 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.  
        $ new_request_02_01 =  True #Hearts.
        call her_main("My... panties...?","body_14")
        call her_main("[genie_name]!","body_47")
        m "I know, I know, this a little weird..."
        call her_main(" {size=+7}A little !?{/size}","body_48")
        her "This is completely inappropriate!"
        m "Listen, we need to go through this phase before we get to the good stuff, alright?"
        call her_main("The \"good stuff\"? [genie_name] I don't understand...","body_31")
        m "What don't you understand, [hermione_name]?"
        m "Do you need these points or not?"
        call her_main("I do...","body_31")
        m "Lift up your skirt then..."
        call her_main(".............","body_47")
    else:
        if request_02 >= 1: #Not the first time
            call her_main("Oh... again?","body_29")
            m "Just do it..."
        call her_main("..................","body_29")
        

    hide screen bld1
    hide screen hermione_main
    with d5
    $ skirt_up = True
    $ menu_x = 0.5 #Default menu position restored.
    if whoring >= 6: # NO PANTIES
        show screen hermione_03_b
        with d3
    else:
        show screen hermione_03 #Hermione lifts her skirt
        with d3
        
    #play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her_[8] "........................"
    elif whoring >= 3 and whoring <= 5: #LEVEL 02
        her_[14] "....................."
    elif whoring >= 6: #LEVEL 03 and up.
        her_[18] ".........................."
        g4 "!!?"
        
        
    

    


    if whoring >= 0 and whoring <= 2: #LEVEL 01   <============================= Fist event.
        $ new_request_02_01 =  True #Hearts.
        show screen bld1
        with d3
        show screen blktone
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_49.png" #Flashing panties
        show screen hermione_main
        show screen ctc
        with d3
        pause
        
        her "....................."
        menu:
            "-Stare at her face-":
                ">You study Hermione's face..."
                pause
                ">You wonder what's going through her mind right now."
                call her_main(".......................","body_51")
                pause
            "-Stare at her panties-":
                ">That's a plain girlish underwear..."
                pause
                call her_main(".......................","body_51")
               

    elif whoring >= 3 and whoring <= 5: #LEVEL 02  <====================================================================== SECOND EVENT!
        $ new_request_02_02 =  True #Hearts.
        show screen bld1
        with d3
        show screen blktone
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_52.png" #Flashing panties
        show screen hermione_main
        show screen ctc
        with d3
        pause
        her "Here, [genie_name]..."
        menu:
            "\"You don't look too embarrassed...\"":
                call her_main("That's not true...","body_53")
                call her_main("But this is a small price to pay if the \"Gryffindors\" keep the cup this year.","body_54")
                her "I know everyone will be so happy..."
                pause
            "\"I like your panties...\"":
                call her_main("Thank you, [genie_name]...","body_53")
            "-Keep looking into her eyes-":
                call her_main("..............................","body_55")
                her "...........................?"
                call her_main("................................","body_56")
                call her_main("[genie_name], please... You are embarrassing me.","body_57")
                

    elif whoring >= 9: #LEVEL 04 and up. <====================================================================== FINAL EVENT! (No panties).
        $ new_request_02_03 =  True #Hearts.
        show screen bld1
        with d3
        show screen blktone
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_58.png" #Flashing panties
        show screen hermione_main
        show screen ctc
        with d3
        pause
        g4 "Where are your panties, [hermione_name]?"
        call her_main("Oh, lately I just don't feel like wearing them...","body_59")
        menu:
            "\"You little slut!\"":
                her "Hm..."
                call her_main("I suppose I am...","body_58")
                her "Do I get extra points for that?"
                menu:
                    "\"Absolutely!\"":
                        m "Absolutely!"
                        $ gryffindor +=10
                        m "Ten additional points to \"Gryffindor\"!" 
                        call her_main("Thank you, [genie_name]!","body_60")
                    "\"Absolutely not!\"":
                        $ mad +=5
                        call her_main("Why not!?","body_62")
                        m "Sluts aren't paid"
                        m "That's what makes them sluts"
                        call her_main("well are you even going to pay me 5 points?","body_61")   
                        m "Are you a slut or are you a prostitute?"
                        her "{size=-4}...a slut {/size}"
                        m "Good girl"
            "\"Good! Five points!\"":
                pass
    
    
    
    
    stop music fadeout 4.0
    
    label request_02_done:
    if whoring <= 8:
        $ gryffindor +=5
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        pause
        
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite.
    hide screen ctc
    hide screen hermione_main
    with d3
    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
    $ skirt_up = False
    show screen hermione_02 #Hermione stands still.
    show screen hermione_main
    with fade
    
    stop music fadeout 4.0


    her "will this be all then?"
    m "Yes, you can go now."

    if request_02 == 0: #First time.
        hide screen hermione_main
        with d3
        $ h_xpos=300 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Another 5 points..."
        her "Can't wait to tell the guys!"
        hide screen hermione_main
        with d3
        $ h_xpos=300 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Only that I can't actually tell them about any of this..."
    
    if daytime:
        her "Well, my classes are about to start..."
    else:
        her "It's getting pretty late, [genie_name]... I should go..."

    
    hide screen hermione_main
    with d3
    hide screen bld1
    hide screen blktone 
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
    
    

    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###



    if whoring <= 2:
        $ whoring +=1
    $ request_02 += 1
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_02_b (LEVEL 01) ### FLIRT WITH CLASSMATES ###
label new_request_02_b:
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
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    with d3
    her "Yes?"
    
    if request_02_b_points == 0 and whoring <= 5: ### LEVEL 01 and LEVEL 02
        ### LEVEL 01 ### <===============================================================FIRST EVENT!
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        m "What is your opinion on the boys of the \"Slytherin\" house?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I detest them, [genie_name]."
        m "Well, too bad. Because I want you to get really friendly with a few of them today."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
        show screen hermione_main
        with d3
        her "If I must..."
        her "Yes, I think I can manage to be civil with them for one day."
        m "Yes, and when I say \"get friendly with them...\""
        m "I actually mean that I need you to flirt with them..."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Flirt?!"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
        show screen hermione_main
        with d3
        her "[genie_name]!"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I'm not even going to ask why you'd be interested in this, [genie_name]..."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
        show screen hermione_main
        with d3
        her "But why \"Slytherin\"?"
        her "If you need me to be flirtatious today, I think I can manage that..."
        her "But, please, can't be another house?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_44.png" #Flashing panties
        show screen hermione_main
        with d3
        her "The \"Gryffindors\" maybe?"
        m "I am only trying to protect your reputation, [hermione_name]."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Flashing panties
        show screen hermione_main
        with d3
        her "[genie_name]?"
        m "Do you value the opinion the \"Slytherin\" students have of you?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I couldn't care less about the opinions of those Neanderthals."
        m "What about the students of the \"Gryffindor\" house?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Their opinion means the world to me--"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Oh, I see..."
        m "Exactly... Just looking out for you [hermione_name]."
        her "Em... Thank you [genie_name]..."
        call music_block
    
    else:
        if whoring <= 2: ### LEVEL 01
            m "I need you to go make some new friends at \"Slytherin\" house."
            her "You mean you need me to flirt with the \"Slytherin\" boys again [genie_name]?"
            m "That's exactly what I need you to do today, [hermione_name]."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Must I really do this [genie_name]?"
            m "We have been through this, [hermione_name]."
            m "Going to the \"Slytherin\" boys is in your best interests."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Yes, I know, [genie_name]."
            her "But why must I this at all?"
            m "Nobody is forcing you, [hermione_name]..."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_05.png" #Flashing panties
            show screen hermione_main
            with d3
            her "You don't need to remind me of that, [genie_name]..."
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
            $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Alright if I must... [genie_name]..."


        else: #if whoring >= 3 and whoring >= 6: ### LEVEL 02 and higher ## <=========================================================== SECOND EVENT!
            m "I need you to flirt with some boys of the \"Slytherin\" house today."
            her "I will see what I can do, [genie_name]."
            m "Great. I'll be expecting your report today after classes."

    
    her "Well, I'd better go now. Classes are about to start..."
    $ request_02_b = True

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
   
        
        
label new_request_02_b_complete:
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
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well..."
                    her "There was this one freshman boy..."
                    her "........."
                    m "I'm listening..."
                    her "Well... I went to him and I said \"Hey, handsome!\"."
                    m "And?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He showed me his tongue and ran off, [genie_name]."
                    m "Did you try to lure him in with a lolipop?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I did not, [genie_name]..."
                    her "The thought never crossed my mind, but--"
                    m "That was a joke, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name]?"
                    m "I didn't send you out there to harass little kids!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "............."
                    m "I told you to flirt with boys {size=+5}your{/size} age!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I wanted to at first, but..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I guess I got scared..."
                    her "I mean I despise those \"Slytherins\" way too much to flirt with them, [genie_name]!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_05.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I would have to fight my gag-reflex the entire time!"
                    menu:
                        "\"Fine. Just try harder next time.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_06.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Thank you, [genie_name]."
                            her "I will, I promise!"
                        "\"Favour failed! No points for you!\"":
                            stop music fadeout 1.0
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "I understand..."
                            m "Get out of my sight..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Yes, [genie_name]...Sorry, [genie_name]..."
                            jump could_not_flirt
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, I tried to complement an upperclassman..."
                    m "Did he appreciate it?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_76.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He called me a \"Gryffindor whore\", [genie_name]!"
                    m "I see..."
                    m "What did you do then?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well that was not the proper way to address a fellow \"Hogwarts\" student..."
                    her "So I told him that I would report him."
                    m "A truly captivating story..."
                    m "Anything else?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes, there was also this one student at the library..."
                    her "He was obviously struggling with a problem..."
                    her "So I offered my help..."
                    m "And?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_76.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He called me a \"Patronizing Gryffindor Whore\", [genie_name]..."
                    m "Did you threaten to report him as well?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Of course, [genie_name]."
                    m "*sigh*"
                    m "Anything else?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, there was one more incident but the outcome was pretty much the same..."
                    m "\"The Gryffindor whore\"?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her ".........yes, [genie_name]."
                    m "You are doing it all wrong, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I am sorry, [genie_name]. I thought this would be easy..."
                    menu:
                        "\"Well, at least you are trying.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Apparently flirting is not my forte..."
                        "\"Favour failed! No points of you!\"":
                            stop music fadeout 1.0
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            $ mad +=15
                            her "You are not going to pay me, [genie_name]?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_21.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "But, you promised!"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_20.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "................"
                            call music_block
                            jump could_not_flirt
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, the \"Slytherin\" quidditch team was practicing in the stadium today..."
                    her "I thought I could sneak into the bleachers and cheer them on..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But..."
                    m "Yes?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_77.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "A whole flock of those \"Slytherin\" harlots was already there, [genie_name]."
                    her "They were cheering and yelling..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And one of them even exposed herself in an inappropriate manner to the players, [genie_name]..."
                    her "I cannot believe our school accepts such behavior..."
                    m "So... how did this captivating drama end?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I just left [genie_name]..."
                    menu:
                        m "Hm..."
                        "\"Well, here are your points.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Thank you, [genie_name]..."               
                            
                        "\"Favour failed! No points for you!\"":
                            stop music fadeout 1.0
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "I don't feel like I deserved any this time anyway..."
                            call music_block
                            jump could_not_flirt
                    
                    
                    
                    
            elif whoring >= 3 and whoring <= 5: ### LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, there was this one guy at the library..."
                    her "He was obviously struggling with some assignment, so I offered my help..."
                    m "And?"
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, to my surprise he accepted it..."
                    her "He let me finish the assignment for him..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "While I was working he made a couple of inappropriate comments but I just smiled in response..."
                    m "So, basically, he was the one doing the flirting..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_24.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "well... yes."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But, despite my better judgment I did encourage his improper behavior..."
                    m "By being quiet?"
                    her "Yes [genie_name]..."
                    her "I mean, this does amount to something, right?"
                    m "Meh..."
                    m "What else do you have for me?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Right..."
                    her "Later in a corridor these two other guys complemented my appearance in a very vulgar manner..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But I just smiled at them..."
                    m "You were on the receiving end again, then..."
                    m "This is not what I ordered you to do, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I know, [genie_name]!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But I am so busy. Between the \"MRM\" meetings and the classes..."
                    her "I barely have any time--"
                    m "Is this all you got for me this time then?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "No, [genie_name]."
                    her "Just an hour ago or so I ran into Draco Malfoy, [genie_name]."
                    m "No way!!! (No idea who that is...)"
                    her "I forced myself to be friendly with him and..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "We ended up having a decent conversation for a change." 
                    m "I see... That \"Dark-oh\" guy..."
                    m "Was he looking at your legs at all?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "What?"
                    m "Did he stare at your legs or not, [hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Em... He might have..."
                    m "What about your tits?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name]!!!"
                    m "Fine. You get your points. Keep up the good work."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
 
                elif one_out_of_three == 2: ### EVENT (B)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well..."
                    her "This morning I did flirt with this one guy..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Then after the second period there was this other guy..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_28.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And then something bizarre happened..."
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her "This angry-looking guy from the \"Slythetin\" came to me and asked me out on a date..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I told him \"no\" at first, but we ended up taking a walk together."
                    m "Did you enjoy yourself, [hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I think I did [genie_name]... To my own astonishment..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "There was something about his \"devil-may-care\" attitude..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He was so confident and calm and..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I still loathe the \"Slytherin\" house of course!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_73.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But..."
                    her "Maybe some of the students got there by mistake?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Could the \"sorting hat\" make... miscalculations ?"
                    menu:
                        "\"Just take your points and go!\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "................"
                        "\"The almighty hat is never wrong!\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Yes, of course... Everybody knows that..."
                        "\"Could what make what?\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Oh, nevermind me, [genie_name]."
                            her "Everyone knows that the \"Sorting Hat\" is never wrong."
                    
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Five guys, [genie_name]!"
                    m "Really?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "This one guy this morning."
                    her "Then another two right after the first period."
                    her "And then another one before the third period."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And after that I had a surprisingly pleasant conversation with one more."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "That last one was quite smart and well mannered too."
                    her "............................"
                    her "................"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But I still refuse to change my opinion about the \"Slytherin\" house, [genie_name]."
                    m "I'm not asking you to, [hermione_name]."
                    her "I am only doing this to help my own house!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_32.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "The proud house of \"Gryffndor\"!"
                    m "Alright, alright, calm down, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3

            elif whoring >= 6: # LEVEL 03 and higher.
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Eleven boys, [genie_name]!"
                    m "Eleven? Really? Your personal best, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Let's see..."
                    her "Those two handsome guys right before the first period started..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_64.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Then I exchanged a few rather inappropriate messages with this other guy, during the the first period."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "After that there was this one other guy..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_73.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Then those three guys..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Then one more right before the last period..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And finally this last guy that walked me right to your tower, [genie_name]..."
                    m "So, eleven then?"
                    m "Those \"Slytherin\" boys are really starting to like you, huh?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I suppose so..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_73.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, not all of them were nice to me at first..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_64.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But I use this trick to \"tame\" them."
                    m "A trick?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes... Whenever a boy from \"Slytherin\" is being mean to me or calls me a name..."
                    her "I just swallow my pride and smile in response."
                    m "Hm..."
                    m "So, if for example, somebody were to call you a \"whore\" you would just smile at them?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, yes, [genie_name]..."
                    m "Yeah, I'm sure that wins them over."
                    m "Great job, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Two dates, seven quite pleasant conversations..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And I even let this one guy kiss me..."
                    m "Quite impressive, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I think so too, [genie_name]. Thank you."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Oh, and there was also this little freshman kid..."
                    her "I tried to flirt with him too, but we ended up just chatting..."
                    her "He kept calling me \"Miss Hermione\"..."
                    her "So adorable..."
                    m "Well I didn't send you to harass little kids, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I didn't haras--"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name]! Seven flirts and two dates amount to something, don't they?"
                    m "Oh, absolutely."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Then I would like to receive my payment now..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name], I am sorry, but..."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I hate those \"Slytherin\" tramps, [genie_name]!"
                    m "Tell me what happened."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I don't want to talk about it..."
                    m "Tell me what happened, [hermione_name]!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_76.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I don't want to talk about it, [genie_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Please don't make me..."
                    menu:
                        "\"Fine. I'll let it go for today.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Thank you, [genie_name]."
                            m "No luck with the flirting today then?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Oh, quite the opposite, [genie_name]."
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            her "One of the boys actually took me to the \"Slytherin\" common room today..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_03.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "There were at least a dozen of them there..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "All of the boys knew who I was..."
                            her "I was the center of attention at first..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_78.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "And it felt sort of wonderful..."
                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Then a bunch of those \"Slytherin\" harlots stumbled in and..."
                            m "And?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Well, they started saying stuff and doing things..."
                            her "Anyway, I had to leave..."
                            m "I see..."
                            m "Well, I say you deserve your points anyway, [hermione_name]."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                            show screen hermione_main
                            with d3

                        "\"Tell me now, or lose the points!\"":
                            $ mad +=10
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "[genie_name], please, I don't want to discuss this with you, [genie_name]."
                            m "No one is forcing you, [hermione_name]."
                            m "You are free to leave."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "{size=-4}(Stubborn old man!){/size}"
                            jump could_not_flirt
                            
                            
    
    $ gryffindor +=5
    m "The \"Gryffindor\" house gets 5 points!"
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




    $ request_02_b_points += 1
    $ request_02_b = False 
    $ hermione_sleeping = True
    
    $ p_level_02_active = True #When turns TRUE public favors of level 02 become available. 
    
    if whoring <= 2:
        $ whoring +=1
        
    call music_block
    
    return        
    
label could_not_flirt: #Sent here when choose "Favour failed! No points for you!" (Hermione is leaving without getting any points).
    hide screen blkfade
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen chair_02
    hide screen hermione_02
    hide screen jerking_off_01 #Hermione topless. Genie jerking off.
    hide screen ctc
    show screen genie
    with d3

    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ request_02_b_points += 1
    $ request_02_b = False 
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    return
    

#################################################################################################################################
### LEVEL 02 ####################################################################################################################    
###################REQUEST_02_c (LEVEL02) ### FLIRT WITH TEACHERS ###
label new_request_02_c:
    
    hide screen hermione_main 
    with d3
    m "{size=-4}(Tell her to be flirtatious with her teachers today?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request

    m "[hermione_name], I want you to be especially flirtatious with your teachers today."
    if whoring <=2 or request_02_b_points <= 1: # request_02_b_points - counts how many times Hermione was sent to flirt with boys. 
        jump too_much
   

    if request_02_c_points == 0 and whoring <= 8: ### up to LEVEL 03
    ### LEVEL 03 ### <===============================================================FIRST EVENT!
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I will do my best, [genie_name]!"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I am glad you finally decided to act, [genie_name]!"
        m "Huh?"
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
        show screen hermione_main
        with d3
        her "You are finally ready to investigate the teachers who made a habit out of buying favours from the students, aren't you?" 
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I am honoured to pose as bait in this noble endeavor."
        m "Ehm... Yeah, that's exactly what I'm doing."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Splendid! You can count on me, [genie_name]!"
    else:
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I shall provide you with a detailed report later tonight, [genie_name]."
        m "I will be waiting..."
    

    
    her "Well, I'd better go now. Classes are about to start..."
    $ request_02_c = True

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


    
    
label new_request_02_c_complete:  ### FLIRTING WITH TEACHERS COMPLETE ###
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
            m "Tell me how many teachers did you flirt with, [hermione_name]?"
            m "Give me the details."
            show screen blktone
            with d3
    
            if  whoring >= 3 and whoring <= 5: ### LEVEL 02 <===================================================================== EVENT LEVEL 01
                if one_out_of_three == 1: ### EVENT (A)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, I tried flirting with Professor Flitwick..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But it didn't really work..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her ".............................."
                    m "How exciting..."
                    m "Is this all you have for me today, [hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Y-yes..."
                    her "But [genie_name], I know for a fact that professor Flitwick is \"dirty\"!"
                    her "Everyone knows that because of his height..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He sometimes... ehm..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He likes to look up girl's skirts, [genie_name]!"
                    m "Don't we all?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "What?"
                    m "I said, don't we all hate it and must be outraged by the a man like Professor Flick-flick."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Er... It's \"Professor Flitwick\", [genie_name]."
                    m "Right. Putting him on my \"Naughty boys list\" as we speak."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_17.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "......................"
                    m "Well, I hate to admit it but you did a lousy job of today's favour, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "................................"
                    menu:
                        "\"No points for you!\"":

                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_28.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "But [genie_name], I did my best!"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_67.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "You are going back on your promise [genie_name]!"
                            m "......................."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_32.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            stop music fadeout 1.0
                            her "How unbecoming of a school headmaster!"
                            m "You are dismissed, [hermione_name]."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_76.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Tsk!"
                            $ mad += 18
                            call music_block
                            jump could_not_flirt_02
                        "\"Here are your point's though.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_28.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Really?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Thank you so much [genie_name]!"
                           
                elif one_out_of_three == 2: ### EVENT (B)
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her ".................."
                    her "............................"
                    m "[hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes, [genie_name]... I'm sorry... I just..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "............"
                    m "Did you do what I asked you to do?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I tried, [genie_name]. I really did..."
                    m "Who did you try to flirt with?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "........."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Professor Snape, [genie_name]."
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    m "Severus? Interesting..."
                    m "How did it go?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "It was awful [genie_name]..."
                    her "I am sorry, but I really hate professor Snape, [genie_name]!"
                    m "I'm sure the feeling is mutual..."
                    m "Tell me what happened."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Nothing happened, [genie_name]. He just laughed at me..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I may not have much feminine charm, but I tried to be nice..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And he just started laughing in my face!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "...it is really scary to see professor Snape laugh..."
                    her "........"
                    her "I am awful at flirting, I am sorry [genie_name]..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But I know that professor Snape is \"dirty\"!"
                    her "If you were to send someone else to him the outcome would be different, I know it!"
                    m "Someone else?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes! Someone with more experience at this..."
                    her "Someone..."
                    her "Someone, uhm..."
                    m "Sluttier?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes, I suppose..."
                    m "Don't you give up, [hermione_name]. We will make a slut err--"
                    m "I mean a woman out of you yet!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_79.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "..................."
                    menu:
                        "\"...But you get no points this time\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "But I did my best..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "And I feel so humiliated now..."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "But I understand and won't argue with your decision..."
                            call music_block
                            jump could_not_flirt_02
                        "\"Here are your points, [hermione_name].\"":
                            pass
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I tried to flirt with mr.Filch, [genie_name]..."
                    m "I see. {size=-5}(No idea who that is.){/size}"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "Yes, I know that technically mr.Filch is not a teacher..."
                    m "Huh?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_01.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But he is part of the school's staff..."
                    her "And we did hit it off quite well too!"
                    her "He was surprisingly sweet."
                    her "But I don't think he is \"dirty\", [genie_name]."
                    m "Gotcha... Mr.Fil{size=+7}TH{/size} is off the list then."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "It's \"Mr.Filch\", [genie_name]..."
                    m "What did I say?"
                    
                    
            elif whoring >= 6 and whoring <= 8: ### LEVEL 03 <=======================================================================================EVENT LEVEL 02
                if one_out_of_three == 1: ### EVENT (A)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, professor Slughorn invited me over to one of his..."
                    her "Rather disturbing tea-parties..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "There were plenty of girls..."
                    her "But all of them were much younger then me..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_17.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Almost every guest was a freshman..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "We had tea and some cake..."
                    her "Everything was pretty harmless..."
                    m "Did you flirt with the man or not?"
                    her "I did..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_17.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Or at least I tried..."
                    her "Professor Slughorn seems to be more interested in much younger girls..."
                    m "You almost sound jealous, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_18.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "What?!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "That is preposterous!"
                    m "Here are your points..."
                    her "...................."
          
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_80.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I had an amazing day, [genie_name]!"
                    m "Do tell, [hermione_name]..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I had a class with professor Lockhart today..."
                    her "[genie_name] Lockhart is so charming and smart and..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_78.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And perfect..."
                    m "Please spare me your schoolgirl crush, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_80.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name] Lockhart was even kind enough to give me his autograph..."
                    m "How kind of him indeed."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes, I can't wait to show it to the girls!"
                    m "Hm... Can I see it?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name]?"
                    m "The Autograph, [hermione_name]. Can I see it?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well... Em... It's in a rather private area, [genie_name]."
                    m "What? Well, then professor Goldenheart surely is \"dirty\"!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "It's professor Lockhart, [genie_name]..."
                    her "And... Ehm..."
                    her "Well, it's not {size=+5}that{/size} private..."
                    m "Show it to me then!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "No, [genie_name]! That would be inappropriate!"
                    menu: 
                        "{size=-3}\"Lockhart will be out of this school in no time!\"{/size}":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_72.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Because of me?"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_67.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "[genie_name], please!"
                            m "Show me!"
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_32.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "No, it's embarrassing!"
                            menu:
                                "\"Fine. Here are your points.\"":
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her "Thank you for understanding, [genie_name]."
                                "\"Show me or I won't pay you!\"":
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_72.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her "What?!"
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_73.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her "..............."
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her ".................."
                                    hide screen hermione_main
                                    with d3
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her "Well, alright, but only to clear my idol's name..."
                                    hide screen hermione_main
                                    with d3
                                    show screen blktone8
                                    with d5
                                    her_[12] "Here...."
                                    m "Hm..."
                                    hide screen blktone8 
                                    with d5
                                    $ only_upper = True #Skirt lifted.
                                    $ autograph = True #Autograph shown.
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_51.png" #Flashing panties
                                    show screen hermione_main
                                    hide screen ctc
                                    show screen ctc
                                    with d3
                                    pause
                                    hide screen hermione_main
                                    with d3
                                    $ h_body = "01_hp/13_hermione_main/body_50.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her "As you can see Professor Lockhart is nothing but an embodiment of everything pure and courageous!"
                                    pause
                                    m "Do I? From this?"
                                    her "You should not worry about professor Lockhart, [genie_name]."
                                    her "He is not \"dirty\"."
                                    m "Ah, what do I care..."
                                    hide screen hermione_main
                                    with d3     
                                    $ h_body = "01_hp/13_hermione_main/body_51.png" #Flashing panties
                                    show screen hermione_main
                                    with d3
                                    her "............?"
                                    hide screen hermione_main 
                                    with d3
                                    $ only_upper = False #Skirt lifted.
                                    $ autograph = False #Autograph shown.
                                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                                    show screen hermione_main
                                    with fade
                                    pause
                                    hide screen ctc
                                    $ mad += 18
                        "\"FIne... Here are your points.\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "Thank you for understanding, [genie_name]."
                            
                elif one_out_of_three == 3: ### EVENT (C)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_15.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, I spent quite some time by flirting with mr.Filch today."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "What a well read and exceptionally well mannered gentleman mr.Filch is."
                    m "........"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But I don't think anyone knows him like that..."
                    her "I don't think anyone knows mr.Filch like I do."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_06.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I feel like he really opened up to me, [genie_name]."
                    m "Right..."
                    m "This, mr.Fli{size=+7}nt{/size}--"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "It's mr.Filch, [genie_name]."
                    m "Yeah, whatever... Is he a teacher here then?"
                    her "Mr.Filch? A teacher? No, [genie_name]..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_06.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He is the caretaker..."
                    m "A caretaker...?"
                    m "You mean he is a janitor?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well..."
                    m "[hermione_name], I did not send you out there to charm school janitors!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But mr.Filch is part of the school staff, [genie_name]!"
                    menu:
                        "\"Just take your points and go!\"":
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_03.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "........................."
                        "\"Favour failed! No points for you!\"":
                            $ mad +=15
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "But [genie_name]?"
                            m "You are dismissed, [hermione_name]."
                            hide screen hermione_main
                            with d3
                            $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                            $ h_body = "01_hp/13_hermione_main/body_05.png" #Flashing panties
                            show screen hermione_main
                            with d3
                            her "........................................."
                            jump could_not_flirt_02


            elif whoring >= 9: # LEVEL 04 and higher.
                if one_out_of_three == 1: ### EVENT (A) LEVEL04 <============================================================================
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "............................."
                    her "....................................."
                    m "[hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name], I....."
                    m "What is it? What happened?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well..."
                    her "It's mr.Filch, [genie_name]..."
                    m "The janitor?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I flirted with him a little..."
                    her "And it went great at first..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "......................."
                    m "................?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And then..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Not sure if I should..."
                    m "[hermione_name], if you are not going to speak up, you may as well leave."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_32.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "He showed me his \"thing\", [genie_name]!"
                    m "His what?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "His... manhood, [genie_name]."
                    g9 "Way to go, Janitor-guy!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_72.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "What?!"
                    m "*Khem* I mean, this is unspeakable!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_21.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes... Vile crooked thing all covered in veins..."
                    m "Spare me the grisly details, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_20.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Why would he do such a thing?"
                    her "One second we were just talking and then..."
                    m "Well, your noble  sacrifice shall not go unnoticed, [hermione_name]!"
                    m "Fifteen points to \"Gryf--"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_19.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Professor, please wait."
                    m "Huh?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, aren't you going to do something about this?"
                    m "Well..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "What if I am not the first victim..?"
                    her "Some unfortunate freshman could be traumatized for life!"
                    m "And who wouldn't be really?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Does this mean you will take action, [genie_name]?"
                    m "uhm... Yeah, sure..."
                    m "There! Putting it on my \"to-do-list\"..."
                    m "\"Take care of the creepy janitor-guy and his crooked cock.\"..."
                    m "Yes, first thing tomorrow."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Thank you [genie_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_75.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Can I have my points now?"
    
                elif one_out_of_three == 2: ### EVENT (B)
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_76.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Professor Snape!"
                    m "Ehm... Yeah, I'm pretty sure it's Dumbledore or something..."
                    hide screen hermione_main
                    with d3
                    
                    g4 "{size=-5}(Wait, did {size=+7}he{/size} just put me under another disguise?){/size}"
                    g4 "{size=-5}(So do I look like that Professor Snape guy now?){/size}"
                    g4 "{size=-5}(By the great desert sands! Akabur, you need to learn restrain yourself!){/size}"
                    a5 "{size=-5}(Would you hear the girl out first! Geez...){/size}"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name]? Who are you talking to?"
                    m "Em... I'm communicating with a spirit from another dimension..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_17.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her ".....??!"
                    hide screen hermione_main
                    with d3
                    a6 "{size=-5}(Stick to the script, you bastard!){/size}"
                    g4 "Yes, a particularly annoying spirit... Annoying and dumb!"
                    a6 "{size=-5}(You......!){/size}"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name], please, you need to listen to me!"
                    m "Yes, yes, [hermione_name], I'm listening."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I just confirmed that professor Snape is corrupted and \"dirty\", [genie_name]!"
                    m "Tell me what happened."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, during the classes today..."
                    her "I have been doing my best to attract professor Snape's attention..."
                    her "I have been giving him \"dreamy looks\"..."
                    her "And I've been eyeing his crotch..."
                    m "You..."
                    m "Eyed his crotch?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_04.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes... It's when you stare at a man's crotch and imagine that you are looking at something you want badly..."
                    m "Where do you get this stuff?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_10.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Women's magazines..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, anyway, it worked, [genie_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "As soon as the class was over, professor Snape grabbed my buttocks, [genie_name]!"
                    m "The fiend!"
                    m "Did you enjoy it, though?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "[genie_name], I am only doing this--"
                    m "Go \"Gryffindors\"! honour and all that. Yes, I remember."
                    m "Here are your points."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                    show screen hermione_main
                    with d3
  
                elif one_out_of_three == 3: ### EVENT (C)
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Professor Lockhart!"
                    m "Got it! Adding him to the \"Naughty list\"!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "No, [genie_name], it's not that..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Or..."
                    her "I'm not sure..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I used to adore him..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "But he..."
                    her "He just..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_20.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "How is this possible?"
                    her "I can't believe this..."
                    hide screen hermione_main
                    with d3
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    m "{size=-4}(Agh! The suspense is killing me!){/size}" 
                    m "{size=-4}(Did he force her to blow him?){/size}"
                    m "{size=-4}(Did he rape her?){/size}"
                    g4 "What was it, [hermione_name]? Speak up!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Huh?"
                    m "What did Professor Lockhart do to you?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Ehm... Nothing, [genie_name]..."
                    m "Nothing?!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes, I sort of cornered mr.Lockhart today..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And I also may have sort of made a pass at him..."
                    m "Seriously?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Yes... Not sure what had gotten into me, [genie_name]..."
                    m "Way to go, [hermione_name]!"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_32.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Hear me out first [genie_name], please!"
                    m "My apologies. Please continue."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "Well, I always knew that mr.Lockhart was a true gentleman and..."
                    her "And... and I just wanted to clear his name from any suspicions once and for all..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "..............."
                    her "Well mr.Lockhart did not reject me..."
                    m "You are killing me [hermione_name]!"
                    m "He didn't reject you, he didn't rape you..."
                    m "What the hell happened then?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "............."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    her "I made him cry, [genie_name]..."
                    m "..............wait.......what?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_28.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "He gave me a bewildered look and then started to sob..."
                    her "He looked like he was genuinely afraid of me, [genie_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "I think..."
                    her "I think mr.Lockhart might be afraid of women..."
                    m "Afraid of women?"
                    m "What is that supposed to mean?"
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "That he is into boys, [genie_name]?"
                    m "Oh..."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_44.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "............"
                    m "..........."
                    m "Well, I bet it was a traumatizing experience for you, [hermione_name]."
                    hide screen hermione_main
                    with d3
                    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "It was, [genie_name]..."
                    m "Well, I hope these points will make you feel better."
                    
                    
                    
    $ gryffindor +=15
    m "The \"Gryffindors\" gets 15 points!"
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

    call music_block

    $ p_level_03_active = True #When turns TRUE public favors of level 03 become available. 

    
    if whoring <= 5:  # (if whoring >= 3 and whoring <= 5) - LEVEL 02
        $ whoring +=1

    $ request_02_c_points += 1 #Leveling up the event.
    $ request_02_c = False 
    $ hermione_sleeping = True

    return    
    
label could_not_flirt_02: #Sent here when chose "Favour failed! No points for you!"
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
    
    $ request_02_b_points += 1
    $ request_02_b = False 
    $ hermione_sleeping = True
    
    return   
    
    
    
    
    
    
    
    
    
    
    
    
    
################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your panties" ###############################
label new_request_03: #(Whoring = 3 - 5)
    if whoring <=2:
        jump too_much
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
    show screen hermione_main
    with d3
    her "I am listening, [genie_name]."
    m "I will need your panties..."   
    hide screen hermione_main
    with d3
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite. Left: 370 Center: 120
    $ h_ypos=0
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    show screen blktone 
    show screen ctc
    show screen hermione_main
    with Dissolve(.3)
    pause
    
    
    
    if request_03 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_01 = True # HEARTS.
        $ new_request_03_heart = 1
        $ request_03 += 1
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
        show screen hermione_main
        with d3
        her "W-what?"
        her "My... panties...?"
        her "[genie_name], this is..."
        m "This is the favour I will be buying from you today, [hermione_name]..."
        m "If you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You need my...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
        show screen hermione_main
        with d3
        her "...panties, [genie_name]?"
        m "Yes I do..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
        show screen hermione_main
        with d3
        her "May I ask what you are planning to do with them...?"
        m "Ehm...I'm conducting research..."
        her "But this is kind of inappropriate, don't you think?"
        m "But don't you hate it that some of the girls from \"Slytherin\"..."
        m "Are selling favours for house points, [hermione_name]?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Yes I do!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
        show screen hermione_main
        with d3
        her "(Those \"Slythering\" tramps have no dignity.)"
        hide screen hermione_main
        with d3
        m "Well, there you go then!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Huh?"
        m "Beat them at their own game!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
        show screen hermione_main
        with d3
        her "What?"
        m "Yes! Don't just put the \"Gryffindor\" house back on top..."
        m "But do it by beating them at their own game!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Flashing panties
        show screen hermione_main
        with d3
        her "[genie_name]..."
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
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_body = "01_hp/13_hermione_main/body_67.png" #Flashing panties
        show screen hermione_main
        with d3
        
        her "Just take them [genie_name]..."
        m "What? When did you?"
        her "Your speech was so moving..."
        her "You are so right, [genie_name]! I shall beat them at their own game!"
        her "My classes are about to start, so I should probably go now..."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "01_hp/13_hermione_main/body_23.png" #Flashing panties
        show screen hermione_main
        with d3
        her "..........."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
        show screen hermione_main
        with d3
        her "...I hope nobody will notice that I have no underwear on today..."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Oh, and I will be back tonight to pick them up, [genie_name]."
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
        show screen hermione_main
        with d3
        her "............."
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
        if request_03 >= 1:
            her "Again, [genie_name]?"
            m "Yes again..."
        her "Here..."
        if whoring >= 12: #LEVEL 05
            hide screen hermione_main
            with d3
            ">Hermione pulls her panties out of her pocket..."
            m "What?"
            hide screen hermione_main
            with d3
            $ h_xpos=120 #Defines position of the Hermione's full length sprite.
            $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Yes, I had a feeling that you might ask for these today, [genie_name]."
            m "A feeling?"
            hide screen hermione_main
            with d3
            $ h_xpos=120 #Defines position of the Hermione's full length sprite.
            $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
            show screen hermione_main
            with d3
            her "Well, to be completely honest I just do not bother to wear them much anymore..."
        else:
            hide screen hermione_main
            with d3
            ">Hermione takes off her panties and hands them over to you..."
        hide screen hermione_main
        with d3
        ">Hermione's panties acquired."
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Well, the classes are about to start, so I'd better go now..."

 
        
    label request_03_ends:
        
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
    
    $ request_03 = True #True when Hermione has no panties on.
    if whoring <= 5:
        $ whoring +=1
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###


    jump day_main_menu
        
label new_request_03_complete: # WHORING LEVEL 02 <=================
    
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 2.5
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
    
    "Good evening, [genie_name]..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Here are your panties.\"":
            if have_cum_soaced_panties:
                jump panties_soaked_in_cum
            else:
                her "Thank you, [genie_name]."
                her "And my payment?"
                m "Of course."
        "\"How was your day, [hermione_name]?\"":
            if  whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
                $ new_request_03_01 = True # HEARTS.
                $ new_request_03_heart = 1
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_15.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Oh..."
                her "Quite ordinary actually..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite.
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Although I could not help but worry that somebody would notice somehow..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                show screen hermione_main
                with d3
                her "....."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Can I have my panties back now?"
                m "Of course..."
                hide screen hermione_main
                with d3
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    hide screen hermione_main
                    with d3
                    $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                    $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And my payment?"
                    m "Yes, yes..."
            elif whoring >= 6 and whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
                $ new_request_03_02 = True # HEARTS.
                $ new_request_03_heart = 2
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_15.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Oh..."
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                show screen hermione_main
                with d3
                her "I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_12.png" #Flashing panties
                show screen hermione_main
                with d3
                her "I felt bad that I had to give the speech without any underwear on..."
                menu:
                    "\"You little hypocrite!\"":
                        $ mad +=5
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
                        show screen hermione_main
                        with d3
                        her "[genie_name]?"
                        m "You sold your panties to me this morning..."
                        m "And a couple of hours later you already publicly condemned that exact behaviour..."
                        #m "What would you call this?"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "01_hp/13_hermione_main/body_69.png" #Flashing panties
                        show screen hermione_main
                        with d3
                        #her "I know you are right, [genie_name]..."
                        her "(But we need the points...)"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                        show screen hermione_main
                        with d3
                        her "Can I have my payment now please?"
                        m "What about your panties?"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                        show screen hermione_main
                        with d3
                        her "Oh, them too of course..." 
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            pass
                    "\"It's for the grater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so corrupted..."
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                        show screen hermione_main
                        with d3
                        her "I shall remain a symbol of righteousness to my peers, no matter what!"
                        hide screen hermione_main
                        with d3
                        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                        $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                        show screen hermione_main
                        with d3
                        her "Can I have my panties back now, please?"
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            her "And my payment."
            elif whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
                $ new_request_03_03 = True # HEARTS.
                $ new_request_03_heart = 3
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_16.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Another ordinary day at hogwarts..."
                her "Nothing worth mentioning happened today..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Although I have to admit..."
                her "It was oddly empowering to have no underwear on..."
                her "Hm..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
                show screen hermione_main
                with d3
                her "Can I have my panties back now please?"
                m "Of course..."
                hide screen hermione_main
                with d3
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    hide screen hermione_main
                    with d3
                    $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                    $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
                    show screen hermione_main
                    with d3
                    her "And my payment?"
                    m "Yes, yes..."
    label back_from_panties:
    if whoring >= 9 and have_cum_soaced_panties == True:
        m "You can go now."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png"
        show screen hermione_main
        with d3
        her "What about my points?"
        m "You still want points after I just gave you a gift?"
        her "What gift?"
        m "You're wearing it"
        her "What, semen soaked panties?"
        m "if you'd prefer the points then just take them off"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_29.png"
        show screen hermione_main
        with d3
        her "well... I am already wearing them"
        m "then say thank you for the gift"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_17.png"
        show screen hermione_main
        with d3
        her "Thank you, [genie_name]..."
        m "You can go now."
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



    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her panties back.
    $ hermione_sleeping = True
    $ have_cum_soaced_panties = False #TRUE when you have the panties in your possession (before you return them to Hermione).

    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    return    
### PANTIES SOAKED IN CUM ###
label panties_soaked_in_cum:
    
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Hm....?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Flashing panties
        show screen hermione_main
        with d3
        her "[genie_name]? What is this?"
        her "What have you done to them?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
        show screen hermione_main
        with d3
        her "They are covered in something slimy..."
        menu:
            "\"An experiment went wrong\"":
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                show screen hermione_main
                with d3
                her "An experiment went wrong, [genie_name]?"
                m "Yes... Or maybe I should rather say..."
                g9 "\"An experiment went very right\"? He-he..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Flashing panties
                show screen hermione_main
                with d3
                her ".....................?"
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Some top secret research I'm conducting."
                m "I can't discuss it with a student."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_05.png" #Flashing panties
                show screen hermione_main
                with d3
                her "................................"
            "\"You gave them to me like this!\"":
                her "I most certainly did not, [genie_name]!"
                her ".........................."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Well, these will require some serious cleaning before I can put them on again..."
        m "Or you could put them on now."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_14.png" #Flashing panties
        show screen hermione_main
        with d3
        her "What?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I really would rather not, [genie_name]..."
        menu:
            "\"Put them on or lose the points!\"":
                $ mad +=7
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_72.png" #Flashing panties
                show screen hermione_main
                with d3
                her "What?"
                her "[genie_name], you are joking, right?"
                m "I am not..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                show screen hermione_main
                with d3
                her "B-but..."
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_33.png" #Flashing panties
                show screen hermione_main
                with d3
                her "........................................"
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                show screen hermione_main
                with d3
                her "(Must you always have your way, [genie_name]?)"
                m "What was that, [hermione_name]?"
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
                show screen hermione_main
                with d3
                her "It's nothing, [genie_name]."
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
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
                show screen hermione_main
                with d3
                her "......................"
            "\"Well, suit yourself...\"":
                pass
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Flashing panties
        show screen hermione_main
        with d3
        her "My panties..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Flashing panties
        show screen hermione_main
        with d3
        her "What happened to them [genie_name]?"
        menu: 
            "\"An experiment went wrong.\"":
                her "Hm..."
                her "I see..."
            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."
        hide screen hermione_main
        with d3
        ">Hermione gives her cum-soaked underwear a quizzical look..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Seems like these will require some serious cleaning before I can put them on again..."
        m "Why not put them on now?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Hm....?"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Well, I suppose I could wear them one more time before putting them into laundry..."
        hide screen hermione_main
        with d3
        show screen blktone8
        with d3
        ">Hermione puts the panties on..."
        hide screen blktone8
        with d3
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
        show screen hermione_main
        with d3
        her "(This feels funny...)"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_44.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Will this be all, [genie_name]?"
    if whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Flashing panties
        show screen hermione_main
        with d3
        her "My panties..."
        if request_03 >= 1:
            her "They are covered in something slimy again..."
        else:
            her "They are covered in something slimy..."
        her "And they smell funny..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Hm... That smell..."
        her "It's familiar somehow..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Flashing panties
        show screen hermione_main
        with d3
        her "What exactly did you do to them, [genie_name]?"
        menu:
            "\"An experiment went wrong\"":
                her "An experiment, huh?"
                her "Of what nature?"
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_46.png" #Flashing panties
                show screen hermione_main
                with d3
                her "No, don't answer that... I think I know..."
            "\"You gave them to me like this!\"":
                her "I don't think so, [genie_name]."
                her "But it's alright if you don't want to tell me, [genie_name]..."
                her "I think I know exactly what happened to them..."
            "\"I came all over them!\"":
                hide screen hermione_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
                $ h_body = "01_hp/13_hermione_main/body_64.png" #Flashing panties
                show screen hermione_main
                with d3
                her "I knew it..."
                her "They reek of semen!"
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_68.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Hm..."
        her "Seems like these will require some serious cleaning before I can put them on..."
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_64.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Unless you want me to put them on now, [genie_name]...?"
        menu: 
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Well, if I must..."
            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"
        
        hide screen hermione_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
        $ h_body = "01_hp/13_hermione_main/body_74.png" #Flashing panties
        show screen hermione_main
        with d3
        her "I am only doing this to give my house a fair chance at winning the cup this year..."
        m "Right..."
        hide screen hermion_main
        with d3
        show screen blktone8
        with d3
        ">Hermione swiftly slides her drenched panties on..."
        hide screen blktone8
        with d3

    jump back_from_panties
    
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    hide screen hermione_main 
    with d3
    m "{size=-4}(I will molest her tits a little. Won't even ask her to bare them for me. Pretty harmless stuff.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    
    
    if whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
        $ new_request_04_01 = True # Hearts. 
        $ new_request_04_heart = 1
        hide bld1
        with d3
        m "Come closer [hermione_name]..."
        her_[2] "Ehm... alright..."
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

        her_[2] "[genie_name].....?"
        menu: 
            m "..."
            "\"I'm gonna molest your tits now.\"":
                her_[3] "What? What do you mean, [genie_name]--?"
                ">Hermione takes a hesitant step back..."
                ">You reach out swiftly and grab both of her tits through her uniform..."
            "-Just reach out and grab her tits.-":
                ">You reach out with both of your hands and grab the [hermione_name]'s tits!"
        stop music fadeout 1.0
        with hpunch
        her_[7] "!!!?"
        her_[8] "[genie_name]?!"
        ">Hermione tries to pull away from you, but you hold her firmly by her breasts..."
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her_[9] "[genie_name], what are you--?"
        ">She tries to pull away again."
        ">You squeeze her tits like a vice."
        her_[10] "[genie_name], you're hurting me!"
        g4 "Then stand still, [hermione_name]!"
        her_[11] "B-but..."
        m "All I want to do is squeeze your tits a little, then you will get your points!"
        her_[12] "B-but... this is..."
        m "Just stand still..."
        m "go to your happy place or something..."
        her_[11] "M-my happy place...?"
        ">You feel the girl's shapely breasts in your palms..."
        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause
        her_[13] "............................"
        menu:
            "-Squeeze her tits with all of your strength-":
                show screen blktone
                with d5
                ">You put strength into your hold..."
                her_[12] "my..........."
                ">You squeeze her tits even harder..."
                her_[13] "[genie_name], you're hurting them..."
                m "Be quiet [hermione_name]..."
                her_[12] "aw.............."
                ">You squeeze her ample tits with all your strength."
                her_[10]"Ah! It hurts!"
                her_[10] "They're gonna burst! Please stop it!"
                m "They are not going to burst, you silly girl..."
                ">You losen your grip a little..."
                her_[13] "It hurts..."
                m "You will be fine..."
                her_[4] "........."

            "-Give her tits a tender massage-":
                show screen blktone
                with d5
                ">You start massaging Hermione's beasts through her uniform..."
                her_[13] "[genie_name]...?"
                m "The points, [hermione_name]... You need the points. Concentrate on that."
                her_[4] "Yes..."
                her_[15] "Yes, for the honour of the \"gryffindor\" house..."
                "*Squeeze-squeeze!*"
                ">You keep massaging her tits..."
                ">You give one of her breasts a few pinches trying to locate the nipple..."
                her_[13] "[genie_name]... you're pinching me...?"
                ">Your attempts prove to be fruitless though. The fabric of the uniform is quite thick..."
                her_[15] "\"gryffindor\" ............"

            "-Let her go and give her the points-":
                show screen blktone
                with d5
                m "Well if you gonna make a drama out of this, you might as well leave..."
                show screen blkfade
                with d5
                ">You unhand the girl's breasts..."
                her_[14] "Really?"
                m "Yes, yes... I will even give you your points..."
                her_[14] "Err... thank you, [genie_name]..."
                m "But you didn't earn them today..."
                her_[12] "Aw........."

    if whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
        if whoring >= 6 and whoring <= 8: # LEVEL 03.
            $ new_request_04_02 = True # Hearts.
            $ new_request_04_heart = 2
        else:
            $ new_request_04_03 = True # Hearts.
            $ new_request_04_heart = 3
        stop music fadeout 2.0
        m "Come closer [hermione_name]... I want to give your tits a massage..."
        her_[14] "As you say, [genie_name]..."
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
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        ">Hermione is starting to pull her uniform up..."
        m "No, leave it on. I want to massage them while you are fully dressed..."
        her_[14] "Oh, I see..."
        ">Hermione stands in front of you expectantly..."
        ">You reach out for her ample breasts..."
        ">And start massaging them firmly..."

        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause

        "*squeeze-squeeze-squeeze*"
        her_[16] "................"
        menu:
            "\"Do you enjoy this, [hermione_name]?\"":
                her_[14] "What...?"
                her_[14] "Oh, I don't mind it..."
                "*squeeze-squeeze-squeeze*"
                ">You keep massaging her soft tits..."
                if whoring <= 12:
                    her_[16] "I mean, this is not a big deal, as long as I am getting paid..."
                    ">You keep on massaging her tits through her uniform..."
                    her_[1] "A small price to pay for the honour of my house, really......{image=textheart.png}"
                else:
                    m "Really? It seems to me as if you love it"
                    her_[16] "I wouldn't say that I love it"
                    ">You keep on massaging her tits through her uniform..."
                    m "What would you say then [hermione_name]?"
                    her_[6] "I just like it, {size=-4}a lot{image=textheart.png}{/size}"
            "-Pull on them abruptly with force-":
                show screen blktone8
                with d3
                ">You give Hermione's tits a sudden but firm pull..."
                with vpunch
                her_[9] "Ouch...."
                ">You pull on her tits again. This time much stronger."
                with vpunch
                her_[9] "Ouch! [genie_name], what are you trying to do...?"
                ">You jerk the girl down by her tits with all your strength..."
                with vpunch
                with vpunch
                ">Hermione almost loses balance..."
                her_[17] "*Panting* What are you doing, [genie_name]...?"
                her_[18] "You don't need to be so rough with me....{image=textheart.png}"
        
        
        

    


    if whoring <= 5:
        $ whoring +=1
        
    show screen blkfade 
    with d3
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    hide screen bld1
    hide screen chair_02 #Genie's chair.
    hide screen groping_03
    hide screen blktone8
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    ">You let go of Hermione's breasts..."
    m "This will do for now."
    her_[4] "................"
    
    hide screen blkfade 
    with d3
    
    if whoring <= 12:
        $ gryffindor +=15
        m "The \"Gryffindor\" house gets 15 points!"
    else:
        m "you may leave now [hermione_name]"
    
    $ request_04_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her ".................."
    her "Thank you [genie_name]..."
    if daytime:
        her "Now if you don't mind I'd better go. The classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."
    
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    if whoring >= 13:
        her_[12] "(What about my points?)"
        if whoring >= 20:
            her_[16] "(eh, who cares)"
        else:
            her_[2] "(I'll just ask him about it next time)"
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###


    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_05 (Level 02) (BUTT MOLESTER).
label new_request_05:
    hide screen hermione_main 
    with d3
    m "{size=-4}(I'll just molest her butt a little.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request

    
    if whoring <=2:
        jump too_much
        
    if whoring >= 3 and whoring <= 5:
        $ level = "02"
        $ new_request_05_01 = True # HEARTS.
        $ new_request_05_heart = 1
    elif whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_05_02 = True # HEARTS.
        $ new_request_05_heart = 2
    elif whoring >= 9:
        $ level = "04"
        $ new_request_05_03 = True # HEARTS.
        $ new_request_05_heart = 3
        
        
    if whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. <=================================================================================== FIRST EVENT.
        
        hide bld1
        with d3
        m "Come closer, child. Let me molest your butt a little."
        if request_05_points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            her_[7] "[genie_name]!?"
            m "Relax, [hermione_name]. It will be the easiest 15 points you've ever made, I promise."
            her_[8] "But...."
            m "All I am going to do is squeeze your little butt a couple of times..."
            her_[4] "This is inappropriate, [genie_name]................"
            m "Nobody needs to know how exactly you got the points..."
            her_[12] "(These 15 points could really make a difference...)"
            her_[19] "(Darn it.....!)"
        else:
            her_[4] "Again.....?"
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
        her_[4] ".................."
        her_[4] "Do you want me to turn around then, [genie_name]?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around, [hermione_name].\"":
                her_[4] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_[4] "............."
                her_[4] "..........................."
                her_[25] "[genie_name], I would like to be done with this sooner rather then later..."
                m "Don't rush me [hermione_name]... Let me savour the moment..."
                her_[4] "............................."
                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        her_[22] "!!!!!!!!!!!!!"
                        her_[22] "[genie_name]!!?"
                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                her_[25] "......................."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                her_[21] "!!!!!!!!!!!!!"
                                her_[15] "[genie_name], what are you doing!?"
                                her_[15] "You said all you were going to do is touch!"
                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        her_[25] "......................."
                                        pass
                                    "-Give her butt another slap-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        her_[15] "Ouch! It hurts!"
                                        her_[20] "This is so demeaning!"
                                        her_[20] "You said all you were going to do is touch..."
                                        #her_[20] "Why are you doing this, [genie_name]?"
                                        g4 "Just stand still, [hermione_name]!"
                                        her_[19] "I don't think so, [genie_name]!"
                                        her_[24] "No amount of points are worth this humiliation!"
                                        her_[23] "You are abusing your power, [genie_name]!"
                                        g4 "What?"
                                        her_[19] "I'm leaving!"
                                        menu:
                                            g4 "Tsk..."
                                            "\"I... I apologize...\"":
                                                her_[25] "Just don't do this anymore, [genie_name]..."
                                                pass
                                            "\"You are not getting any points for this!\"":
                                                $ mad += 30
                                                her_[20] "Ha! See if I care, [genie_name]!"
                                                ### Takes place aftre you refuse to pay her the points.
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_walk_01_f 
                                                with fade
                                                pause 2
                                                hide screen hermione_walk_01_f 
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                with Dissolve(.3)
                                                pause.5
                                                g4 "Tsk! (You little brat!)"
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu
                                            "\"I'm subtracting points from you then!\"":
                                                $ mad += 20
                                                her_[22] "You can't be serious!?"
                                                $ gryffindor -=10
                                                g4 "The \"Gryffindor\" house, minus 10 points!"
                                                g4 "There! It's done!"
                                                her_[24] "Gr..........."
                                                her_[24] "........................"
                                                her_[27] "This is not fair..."
                                                m "What? Hey, wait, don't you start crying on me..."
                                                her_[29] "I hate you, [genie_name]! I hate you!"
                                                
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_run
                                                with fade
                                                pause.9
                                                hide screen hermione_run
                                                with Dissolve(.3)
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                m ".............."
                                                menu:
                                                    "\"Dammit. Now I feel like crap...\"":
                                                        $ mad -= 5
                                                        m "Dammit... Now I feel like crap..."
                                                        m "But who could resist slapping that little behind of her's?"
                                                    "\"She made me do this, that brat!\"":
                                                        $ mad += 9
                                                        m "She made me do this, that brat!"
                                                        m "Acting all wounded now..."
                                                        m "I bet she actually enjoyed the slapping and just won't admit it..."
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                pause
                show screen groping_02
                with d7
                her_[7] "!!!!!!?"
                m "What is it, [hermione_name]?"
                her_[15] "It's nothing [genie_name]..."
                her_[15] "It's just... "
                her_[15] "I can't believe this is really happening..."
                her_[15] "This is so... inappropriate..."
                m "Relax, [hermione_name]. It's not like you are enjoying this..."
                her_[19] "What? Of course not! This is depraved..."
                her_[19] "I am making this sacrifice for the the honour of my house..."
                m "Yes, concentrate on that..."
                her_[20] "...................."
                show screen bld1
                with d3
                pause
                her_[17] "But, [genie_name]..."
                her_[5] "Why are {size=+7}you{/size} doing this?"
                menu: 
                    m "Hm..."
                    "\"I have my reasons...\"":
                        her_[12] "Oh..."
                        her_[25] "Hm..."
                    "\"In the name of science of course!\"":
                        her_[3] "Really?!"
                        her_[3] "Is this a research of some kind?"
                        m "Yeah, sure, I'm researching ehm... er..."
                        m "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..."
                        her_[3] "I see..."
                        her_[2] "Well, if it is for a research then I am glad to be of help..."
                    "-Just squeeze her butt cheeks tighter-":
                        ">You give Hermione's butt cheeks a couple of extra firm squeezes."
                        her_[5] "...................."
                        her_[12] "(Shall I just be quiet then.....?)"
                show screen blktone8
                with d3
                ">You keep on playing with Hermione's buttocks..."
                ">You slide your hands up and down her inner tighs..."
                her_[15] "................"
                label connection_of_rapes:
                menu:
                    "-Slide your hands under her panties-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        her_[7] "[genie_name]... What are you...?"
                        m "That's alright, just think about those 15 points your house is about to receive..."
                        her_[12] "............."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                her_[7] "[genie_name]? No! What are you...?"
                                ">Hermione tries to pull away from you..."
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">Also it is relatively dry... Doesn't look like Hermione's taking any pleasure in this..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_[7] "[genie_name]? No! What are you doing!?"
                                ">Hermione tries to pull away from you..."
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        her_[30] "!!?"
                                        ">It's very tight and warm inside..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            "\"No. Just stand still, [hermione_name].\"":
                her_[4] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                her_[1] "[genie_name], please hurry up, before someone discovers us like this..."
                m "What is the problem, [hermione_name]?"
                m "You know you are doing this for your house."
                her_[4] "I do know."
                her_[4] "But not everyone would see it that way..."
                her_[4] "So let us be done with this as quick as possible..."
                her_[5] "Please..."
                m "Well, if you insist..."
                show screen groping_01
                with d7
                her_[7] "!!!"
                m "What is it?"
                her_[5] "It's nothing, [genie_name]. Your hands are cold, that's all..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                her_[4] "........................."
                ">You give her buttocks a good squeeze..."
                her_[19] "................."
                m "Don't look away, [hermione_name]. I want you to look into my eyes."
                her_[19] "I would rather not, [genie_name]..."
                menu:
                    m "..."
                    "\"Fine. Just keep standing still then.\"":
                        her_[15] "Thank you [genie_name]..."
                        ">You massage her buttocks lightly..."
                        her_[15] "...................."
                        ">And keep enjoying the sensation of her ass under your hands..."
                        her_[19] "....................."
                        ">Then you give Hermione's butt one last squeeze."
                        her_[19] "....................."
                    "\"Open your eyes, or lose the points!\"":
                        $ mad += 7
                        her_[19] "Tsk! {size=-5}(You perverted old--{/size}"
                        m "Did you say something, [hermione_name]?"
                        her_[8] "It's nothing, [genie_name]."
                        ">You massage her buttocks lightly..."
                        ">Hermione maintains the eye contact as she's been told..."
                        her_[8] "...................."
                        her_[4] "..............................."
                        m "What did I tell you about looking away?"
                        her_[19] "Yes, I remember..."
                        her_[8] "................................."
                        her_[25] "..................................."
                        her_[25] ".................................................."
                        ">You keep on enjoying the sensation of her soft ass-cheeks under your fingertips..."
                        her_[8] "....................."
                        jump connection_of_rapes
    
        
    elif whoring >= 6: # LEVEL 04 # Hermione is hesitant. <=================================================================================== SECOND EVENT.
        $ new_request_05_02 = True # HEARTS.
        $ new_request_05_heart = 2
        hide screen bld1
        with d3
        m "Come closer, [hermione_name]. Let me molest your butt a little."
        her_[17] "If I must..."
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
        her_[18] "Do you want me to turn around then, [genie_name]?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around, [hermione_name].\"":
                her_[18] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_[35] "............."
                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        her_[22] "!!!!!!!!!!!!!"
                        her_[18] "[genie_name]....?"
                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                her_[18] "It's Ok..."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                her_[21] "!!!!!!!!!!!!!"
                                her_[18] "[genie_name], what are you doing!?"
                                her_[18] "You said all you are going to do is touch!"
                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        her_[18] "It's not a big deal..."
                                        pass
                                    "-Give her butt another slap-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        her_[34] "[genie_name], not so loud, please..."
                                        her_[34] "What if somebody hears us?"
                                        m "Alright, alright... proceeding with groping then..."
                                        her_[18] "................"

                pause
                show screen groping_02
                with d7
                her_[18] "..................."
                m "You are being awfully quiet today, [hermione_name]."
                her_[18] "Am I...?"
                if whoring <= 13:
                    her_[35] "Well, you know me, [genie_name]..."
                    her_[35] "I'm just happy to be able to do my part for the \"Gryffindor\" house...."
                her_[35] "Please don't mind it and continue..."
                her_[18] "(...to grope me...)"
                show screen blktone8
                with d3
                ">You keep on playing with Hermione's ass..."
                ">And continue sliding your hands up and down her inner tighs..."
                her_[18] "................"
                label connection_of_rapes_02:
                menu:
                    "-Slide your hands under her panties-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        her_[17]"[genie_name]... What are you...?"
                        if whoring <= 13:
                            m "It's alright, just think about those 15 points your house is about to receive..."
                        else:
                            m "It's alright, just try to relax and enjoy yourself"
                        her_[17] "As you say..."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                her_[18] "[genie_name]?" 
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">it is quite wet as well...  Seems like Hermione's taking pleasure in this..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_[18] "[genie_name]? What are planning on doing?"
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        her_[36] "ah... your finger is up my..."
                                        ">It's very tight and warm inside..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            "\"No. Just stand still, [hermione_name].\"":
                her_[4] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                her_[1] "[genie_name], please hurry up, before someone discovers us like this..."
                m "What's the problem, [hermione_name]?"
                m "You know you are doing this for your house."
                her_[4] "I do know."
                her_[4] "But not everyone would see it that way..."
                her_[4] "So let us be done with this as quick as possible..."
                her_[5] "Please..."
                m "Well, if you insist..."
                show screen groping_01
                with d7
                her_[7] "!!!"
                m "What is it?"
                her_[5] "nothing, [genie_name]. Your hands are cold, that's all..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                her_[4] "........................."
                ">And give her Ass a good squeeze..."
                her_[19] "................."
                m "Don't look away, girl. I want you to look into my eyes."
                her_[19] "I would rather not, [genie_name]..."
                menu:
                    m "..."
                    "\"Fine. Just keep on standing still then.\"":
                        her_[15] "Thank you [genie_name]..."
                        ">You massage her ass-cheeks lightly..."
                        her_[15] "...................."
                        ">And keep enjoying the sensation of her butt under your hands..."
                        her_[19] "....................."
                        ">Then You give Hermione's butt one last squeeze."
                        her_[19] "....................."
                    "\"Open your eyes, or you'll lose the points!\"":
                        $ mad += 20
                        her_[19] "Tsk! {size=-5}(You perverted old--{/size}"
                        m "Did you say something, [hermione_name]?"
                        her_[8] "It's nothing, [genie_name]."
                        ">You massage her ass-cheeks lightly..."
                        ">Hermione maintains eye contact as she's been told..."
                        her_[8] "...................."
                        her_[4] "..............................."
                        m "What did I tell you about looking away?"
                        her_[19] "Yes, I remember..."
                        her_[8] "................................."
                        her_[25] "..................................."
                        her_[25] ".................................................."
                        ">You keep enjoying the sensation of her soft buttocks under your fingertips..."
                        her_[8] "....................."
                        jump connection_of_rapes_02  
        
        
        
        
        
        
        
  
  
  
  
  
  
  
  
    
        
    label ending_of_screams_of_pleasure:
    if whoring <= 5:
        $ whoring +=1
    show screen blkfade 
    with d5
    
    stop music fadeout 1.0
    ">You let go of her ass..."
    m "This will do for now."
    
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with d1
    
    hide screen blkfade
    with d3
    if whoring <= 13:
        $ gryffindor +=15
        m "The \"Gryffindors\" get 15 points!"
    else:
        m "good night [hermione_name]"
    $ request_05_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her ".................."
    her "Thank you [genie_name]..."
    if daytime:
        her "Now if you don't mind I'd better go. The classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    
    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        her_[12] "..........................."
        
        
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5

    call music_block # Lunches apropriete BGM day/night.

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

### ALL THE SCREAMS ABOUT RAPE ###
label screams_of_rapings:
her_[10] "NO! What have you done!!?"
">Hermione gives you an unexpectedly strong shove..."
with hpunch
her_[10] "Why would you do this to me, [genie_name]...?"
her_[27] "I never agreed to... to..."
her_[27] "You... you..."
with hpunch
her_[29] "{size=+7}YOU RAPED ME!{/size}"
g4 "What? Don't be ridiculous, [hermione_name]! I did no such thing!"
her_[29] "Yes you did! Yes you did!"
g4 "I most certainly did not!"
her_[29] "No, you did, [genie_name]!"
her_[31] "Now, you will give me 20--"
her_[31] "No, 100 house points or I am reporting you to the Ministry of magic!"
menu:
    m "(Ah, crap...)"
    "\"Alright, alright... 100 points it is...\"":
        $ gryffindor +=100
        m "One hundred points to \"Gryffindor\" !"
        m "There, it is done..."
        m "Now would you calm yourself down, [hermione_name]?"
        her_[29] "No, I will not!"
        her_[29] "I've just been raped!"
        g4 "Oh, snap out of it [hermione_name], I didn't rape you! All I did was--"
        with hpunch
        her_[29] "{size=+7}You raped me!!!{/size}"
        g4 "By the great desert sands, would you keep it down about the rapes!?"
        g4  "Someone may hear you!"
        her_[29] "Good! I want them to hear!"
        m "Why would you want that? I already paid you!"
        her_[32] "Oh... right..."
        her_[33] "But I hate you! I hate you [genie_name]!"
        $ mad +=30

    "\"You're bluffing, [hermione_name]!\"":
        her_[29] "No, I'm not! I'm gonna do it!"
        g4 "By all means, go ahead..."
        g4 "There was no rape!"
        her_[29] "I hate you, [genie_name]!"
        $ mad +=50


hide screen bld1
hide screen ctc
hide screen hermione_main
show screen genie
hide screen groping_01
hide screen groping_02
hide screen blkfade
hide screen blktone8
with Dissolve(.3)
$ walk_xpos=400 #Animation of walking chibi. (From)
$ walk_xpos2=610 #Coordinates of it's movement. (To)
$ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
show screen hermione_walk_01_f 
pause 2
hide screen hermione_walk_01_f 
$ hermione_chibi_xpos = 610 #Near the desk.
show screen hermione_01_f #Hermione stands still.
with Dissolve(.3)

if whoring >= 3 and whoring <= 5: #First level. Not happy.
    her_[12] "..........................."
    
    
hide screen hermione_01_f #Hermione stands still.
with Dissolve(.3)
$ renpy.play('sounds/door.mp3') #Sound of a door opening.
with Dissolve(.3)
pause.5

if daytime:
    $ hermione_takes_classes = True
    jump day_main_menu
else:
    $ hermione_sleeping = True
    jump night_main_menu        
    
########### SCREAM OF PLEASURES ###        
label screams_of_pleasure:
    her_[34] "Ah...."
    her_[34] "It's inside of me..."
    her_[18] "No, [genie_name], you must stop now..."
    m "Why? You don't like it?"
    her_[18] "It doesn't matter whether I like this or not, [genie_name]."
    her_[18] "You know why I'm doing this..."
    her_[18] "And it is wrong for me to let you do this to me for a meagre 15 points..."
    ">Hermione pulls away from you..."
    m "Heh... I see..."
    m "Well, in that case..."
    jump ending_of_screams_of_pleasure

    

###################REQUEST_06 (Level 02) (Flash panties to classmate.) #################################################################################
label new_request_06:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        m "I want you to do something for me during class today: flash your panties to one of your classmates."
        if request_06_points == 0: #One star.
            her "Oh..."
            "Hermione reluctantly agrees."
        elif request_06_points == 1: #Two stars.
            her "If i must..."
            "Hermione agrees."
            
        elif request_06_points == 2: #Three stars.
            her "Of course..."
            "Hermione agrees. She is very eager."
            
        elif request_06_points >= 3: #Master.
            her "Of course, [genie_name]."
            ">Hermione agrees cheerfully."
        

        "You dismiss Hermione."
        $ request_05 = True
        $ hermione_takes_classes = True
        
        if whoring <= 5:
            $ whoring +=1
            
        if request_05_points <= 2:
            $ gryffindor +=15
            "gryffindor got +15 points."
        else:
            $ gryffindor +=5
            "gryffindor got +5 points."

        jump day_main_menu
       
label new_request_05_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_06_points == 0: #One star.
        her "Uhm... I tried to flash my panties to one of my classmates but instead I think five or six of them caught a glimpse. So embarrassing..."
    elif request_06_points == 1: #Two stars.
        her "I managed to flash my panties to one of the classmates."
    elif request_06_points == 2: #Three stars.
        her "I managed to show my panties to a classmate and he took a very long look too."
    elif request_06_points >= 3: #Three stars.
        her "I managed to show my panties to a classmate his look lingered there for quite a while."
        her "It was great!"
    
    "You dismiss Hermione."
    $ request_06_points += 1 #Leveling up the event.
    $ request_05 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."     
    return


###################REQUEST_07 (Level 02) (Flash panties to a teacher).(Daytime only). #######################################################################
label new_request_07:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        m "I want you to do something for me during class today: flash your panties to one of your teachers."
        if request_07_points == 0: #One star.
            her "Oh..."
            "Hermione reluctantly agrees."
            
        elif request_07_points == 1: #Two stars.
            her "If i must..."
            "Hermione agrees."
            
        elif request_07_points == 2: #Three stars.
            her "Of course..."
            "Hermione reluctantly agrees. She is very eager."
            
        elif request_07_points >= 3: #Master.
            her "Of course, [genie_name]."
            ">Hermione agrees cheerfully."
        

        "You dismiss Hermione."
        $ request_06 = True
        if whoring <= 5:
            $ whoring +=1
        
        if request_05_points <= 2:
            $ gryffindor +=15
            "gryffindor got +15 points."
        else:
            $ gryffindor +=5
            "gryffindor got +5 points."
        $ hermione_takes_classes = True
        jump day_main_menu
        

label new_request_06_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_07_points == 0: #One star.
        her "Em... I tried to flash my panties to one of the teacher but he wasn't looking, so instead I think five or six of my classmates acught a glimpse. So embarrassing."
    elif request_07_points == 1: #Two stars.
        her "I managed to flash my panties to one of the teachers."
    elif request_07_points == 2: #Three stars.
        her "I managed to show my panties to a teacher, he took a very long look too."
    elif request_07_points >= 3: #Three stars.
        her "I managed to show my panties to a teacher he took a very long look too."
        her "It was great!"
    
    $ request_07_points += 1 
    $ request_06 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

#####################################################################################################################################################################
### LEVEL 03 ###########################################################################################################################################################
###################REQUEST_08 (Level 03) (Show me tits). #####################################################################################################################
label new_request_08: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main 
    with d3
    if request_08_points == 0:
        m "{size=-4}(I feel like gazing upon those titties.){/size}"
    else:
        m "{size=-4}(I feel like gazing upon those titties again.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    if whoring <=5:
        jump too_much
        
    if "power_girl" in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                m "Power girl."
                if whoring >= 15:
                    $ changeHermioneMainScreen(hg_pth+"body_30.png")
                    her "In that ridiculous costume?"
                    m "It's not that bad. It has a nice cape."
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
                    $ custom_outfit = 7
                    $ panties = False
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
        
    $ current_payout = 25 #Used when haggling about price of th favor.
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        
    if request_08_points == 0 and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "[hermione_name]?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "Yes, [genie_name]..."
        m "How much will it cost me to see your tits?"
        stop music fadeout 1.0
        call her_main("How much will it cost you to...?","body_14")
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("[genie_name]!","body_30")
        m "Hm... I thought your house could use some extra points..."
        m "But I guess I was wrong..."
        call her_main(".........?","body_31")
        m "Please don't mind me..."
        m "All I want to do is help you..."
        call her_main(".............","body_29")
        call her_main("200 house points, [genie_name].","body_33")
        m "So if I give you 200 house points, [hermione_name]..."
        m "You will shamelessly bare your melons before me?"
        call her_main("[genie_name]! No need to be so vulgar!","body_47")
        her "I think I'd better go..."
        menu:
            "\"Wait. 200 points are yours. Show me!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                call her_main("Really?","body_14")
                m "Well?"
                call her_main("......................................","body_29")
                her "You have to promise me not to touch them, [genie_name]."
                m "Sure, sure..."
                call her_main("I am only doing this for the honour of my house, [genie_name]!","body_32")

            "\"I will give you 5 points to see your tits.\"":
                call her_main("Five?!","body_72")
                call her_main("[genie_name], I am not going to expose myself for a meagre five points!","body_76")
                m "Well, your tits sure aren't worth 200, [hermione_name]!"
                call her_main("(They aren't?)","body_73")
                call her_main("Maybe one hundred then?","body_69")
                menu:
                    "\"Fine. 100 it is! Bare them already!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "So be it... For a hundred points..."
                    "\"25 house points that's my final offer!\"":
                        her "..............."
                        her "Well, so be it..."
            "\"Fine, leave. I don't care...\"":
                $mad = +12
                her "Tsk!"
                call music_block
                jump could_not_flirt
                
                
        hide screen blktone
        with d3
        hide screen bld1
        with d3
        hide screen hermione_main
        with d5
        $ menu_x = 0.5 #Default menu position restored.
        show screen ctc
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        pause
        show screen hermione_04
        with fade
        pause
        show screen bld1
        with d3
        m "Hm..."
        her_[12] "{size=-5}(My breasts are completely exposed...){/size}"
        m "Come closer [hermione_name], let me take a better look..."
        her_[4] "............"
        
        hide screen bld1
        with d3

        show screen blkfade #Completely black screen.
        with Dissolve(1)
        pause.5
        ">Hermione slowly walks towards your desk."
        ">With every step she takes her ample tits bounce a little..."
       
        hide screen hermione_04 #Stands with tits out.
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        her_[1] "............"
        m "Very good..."
        her_[4] "....."
        
        $ badges = False
        $ lift_shirt = True
    
        show screen blktone 
        with d3
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #$ only_upper = True #No lower body displayed. 
        show screen hermione_main
        with d3
        pause
        her "...................................."
        
        
        
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
            m "[hermione_name]?"
            her_[2] "Yes, [genie_name]?"
            m "I need to see your tits."
            her_[4] "............"
            her_[4] "Do you promise not to touch, [genie_name]?"
            m "Of course."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            hide screen hermione_main
            with d5
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Hermione slowly walks towards your desk."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Very good..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            show screen blktone 
            with d3
            hide screen hermione_main
            with d3
            if whoring >= 17:
                $ h_body = "01_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
            else:
                $ h_body = "01_hp/13_hermione_main/body_81.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #$ only_upper = True #No lower body displayed. 
            $ badges = False # Hides any badges from hermione_main screen.
            $ lift_shirt = True

            show screen hermione_main
            with d3
            pause
            her "...................................."
            
            
            
            
            
            
        elif whoring >= 9: # LEVEL 04 and higher# <=================================================================================== SECOND EVENT and THIRD EVENT. (HERMIONE IS INDIFFERENT) 
            m "I need to see your tits, [hermione_name]."
            if whoring >= 17:
                her_[16] "Of course [genie_name]?"
            else:
                her_[15] "Are you only going to watch, [genie_name]?"
                m "Of course..."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            hide screen hermione_main
            with d5
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Hermione slowly walks towards your desk."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Very good..."
            show screen blktone 
            with d3
            hide screen hermione_main
            with d3
            
            if custom_outfit == 7:
                $ custom_outfit = 7.2
            else:
                $ badges = False # Hides the layer with badges.
                $ lift_shirt = True
            
            $ h_body = "01_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #$ only_upper = True #No lower body displayed. 
            show screen hermione_main
            with d3
            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    menu:
        "\"Break your promise. Grab the tits!\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. HERMIONE OUTRAGED.
                hide screen hermione_main
                $ only_upper = False #No lower body displayed. 
                with d3
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                her_[7] "[genie_name], what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                
                m "Relax, [hermione_name]. Just stand still!"
                m "Oh... Those are some nice titties you've got..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_[13] "No, [genie_name], please! You mustn't do this..."
                m "This won't take long, just stand still."
                her_[24] "[genie_name], I didn't agree to this!"
                with hpunch
                her_[23] "You must unhand me now!!!"
                show screen blkfade
                with d5
                ">Hermione pulls away from you and covers up hastily."
                her_[19] "I think I'd better go..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                m "Go ahead, [hermione_name]. You are not getting paid if you do..."
                her_[19] "But I showed you my..."
                her_[24] "And you touched me..."
                her_[23] "And I am getting nothing?"
                m "You are dismissed, [hermione_name]..."
                her_[19]  "Gr.................."
                her_[19] "{size=-5}(Burn in hell, you wretched old---{/size}"
                $ mad += 22
                call music_block
                jump could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT. A BIT ANGRY.
                hide screen hermione_main
                with d3
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                her_[7] "[genie_name], what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Relax, [hermione_name]. Just stand still!"
                her_[4] "I didn't agree to this, [genie_name]..."
                her_[4] "I don't think you should..."
                m "Don't you like it...?"
                her_[12] "What?"
                m "Don't you like it how I squeeze and pull on your breasts?"
                her_[12] "..............."
                m "Admit it, you like it a little bit..."
                her_[12] "{size=-5}(So strange to see my breasts in someone else's hands...){/size}"
                her_[13] "[genie_name], I am letting you do this to me to help my house out, nothing more!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_[4] "Please, unhand me now!"
                show screen blkfade
                with d5
                ">Hermione pulls away from you suddenly and covers up."
                her_[4] "You promised not to touch, [genie_name]..."
                m "It was hard to resist..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                her_[1] "............."
                her_[9] "Can I get paid now please?"
                m "Sure..."
                $ mad += 9
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT. ENJOYS A LITTLE.
                hide screen hermione_main
                with d3
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                her_[7] "[genie_name], what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Relax, [hermione_name]. Just stand still!"
                her_[12] "But..."
                her_[13] "ah...{image=textheart.png}"
                her_[12] "I didn't agree to this..."
                m "But you like it, don't you?"
                if whoring >= 17:
                    her_[17] "I love it [genie_name]!{image=textheart.png}"
                else:
                    her_[13] "I do not, [genie_name]!{image=textheart.png}"
                show screen blktone
                with d3
                ">You give her tits a couple of firm squeezes..."
                hide screen blktone
                with d3
                if whoring >= 17:
                    her_[18] "[genie_name], you promised not to touch..."
                    m "I know, I know... But it's hard to resist..."
                    her_[6] "................."
                else:
                    her_[15] "[genie_name], you promised not to touch..."
                    m "I know, I know... But it's hard to resist..."
                    her_[20] "................."
                her_[6] "....................ah...{image=textheart.png}"
                her_[6] "[genie_name], you need to stop now..."
                m "Just a bit longer..."
                show screen blktone8
                with d3
                ">You keep on massaging the girl's breasts..."
                hide screen blktone8
                with d3
                her_[37] "[genie_name]... please, stop this..."
                m "Why? Because you like it too much?"
                her_[18] "No it's not that..."
                her_[17] "I mean..."
                show screen blktone8
                with d3
                ">You pull the tits in opposite directions and then squish them together..."
                hide screen blktone8
                with d3
                her_[38] "Ah...{image=textheart.png} [genie_name], I really need to go..."
                if daytime:
                    her_[17] "That's right... the classes are about to start..."
                else:
                    her_[17] "It is getting late..."
                m "Well, alright..."
                show screen blkfade
                with d5
                ">You let go of the girl's breasts..."
                ">Hermione covers up..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                if if whoring >= 17:
                    her_[18] "Please don't think I forgot that you broke your promise, [genie_name]."
                else:
                    her_[25] "Please don't think I forgot that you broke your promise, [genie_name]."
                m "Right..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                if if whoring >= 17:
                    her_[17] "Thank you [genie_name]."
                else:
                    her_[35] "Can I have my payment now?"
                    $ mad +=7
   
        "\"Keep promise. Admire visually.\"":
            ">You take a long look at Hermione's naked tits..."
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                pause
                menu:
                    "-Nod your head in approval-":
                        ">You Look at the girl's tits for a while and then nod in approval..."
                        her "......................"
                    "-Shake your head in disapproval-":
                        $ mad += 3
                        ">You Look at the girl's tits for a while and then shake your head in disappointment..."
                        her ".....................?"
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                pause
                menu:
                    "\"A Nice set of tits you got there.\"":
                        call her_main("","body_83")
                        pause
                        her "Thank--"
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        call her_main("...........","body_82")
                        call her_main("You are being inappropriate, [genie_name].","body_81")
                        
                    "\"Hm... I've seen better.\"":
                        $ mad += 7
                        her "Tsk..."
                        her "Are we done then?"
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                pause
                menu:
                    "\"You have great tits, [hermione_name].\"":
                        call her_main("You really think so [genie_name]?","body_82")
                        call her_main("I am glad you like them, [genie_name]...","body_84")
                    "\"Your tits are alright I suppose...\"":
                        call her_main("Huh?","body_82")
                        her "Does this mean you don't like them, [genie_name]?"
                        call her_main("I'm sorry...","body_85")
            ">You stare at her breasts for a while longer..."
            pause
            m "Alright, you can cover up, [hermione_name]..."
            her "............."
            hide screen hermione_main
            with d3
            $ only_upper = False #No lower body displayed. 
            show screen blkfade
            with d3
            ">Hermione covers up..."
            $ badges = True # Shows layer with badges.
            $ lift_shirt = False
            hide screen chair_02 #Genie's chair.
            hide screen genie_and_tits_01
            hide screen bld1
            hide screen blktone
            show screen genie
            show screen bld1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_02 #Hermione stands still.
            with d5

        "\"Start jerking off.\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                $ mad += 2
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_[30] "[genie_name]?!!"
                m "Just stand still, [hermione_name]..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                ">You stare at Hermione's breasts with hunger..."
                her_[13] "[genie_name], what are you...?"
                ">You keep stroking your hard cock..."
                her_[12] "[genie_name], no..."
                her_[12] "You must... Put it away..."
                m "Stop whining [hermione_name]. I'm not touching you, am I?"
                her_[19] "But..."
                her_[20] "But I didn't agree to this!"
                her_[19]"I..."
                her_[19] "I think I'd better leave now!"
                menu:
                    "\"Leave now, and you'll get no points!\"":
                        $ only_upper = False
                        her_[21] "After {size=+5}this{/size}? Are you kidding me, [genie_name]?"
                        her_[21] "I showed you my..."
                        her_[25] ".........."
                        her_[24] "I am not going to sell you a single favour anymore, [genie_name]!"
                        show screen blkfade
                        with d3
                        ">Hermione pulls away from you and covers up..."
                        g4 "Don't you dare to leave me in this state, [hermione_name]!"
                        her_[10] "I am not setting a foot into your office ever again, [genie_name]!"
                        g4 "Come on, now. Just say something dirty! I'm almost there!"
                        her_[27] "You are a horrible person, [genie_name]..."
                        $ mad += 30
                        call music_block
                        jump could_not_flirt
                    "\"Alright, alright. That's enough for now.\"":
                        $ mad +=9
                        $ only_upper = False
                        pass
                    "-Start jerking your cock faster-":
                        $ mad += 35
                        $ only_upper = False
                        ">You start jerking your cock furiously!"
                        her_[23] "No, [genie_name], stop!"
                        ">You jerk it even faster!"
                        her_[25] "[genie_name], think I will be leaving now..."
                        g4 "No, wait, I'm almost there!"
                        show screen blkfade
                        with d3
                        her_[10] "Ew! [genie_name]!"
                        her_[10] "I'm leaving!"
                        call music_block
                        jump could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                her_[30] "[genie_name]?"
                ">You stare at Hermione's breasts with hunger..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                her_[13] "[genie_name], I didn't agree to this..."
                m "What are you complaining about, [hermione_name]?"
                m "I'm not even touching you..."
                her_[13] "Yes, but you are... touching yourself, [genie_name]."
                ">You pick up the pace..."
                m "just stand still, [hermione_name]."
                m "It will be over soon."
                her_[13] ".................."
                her_[12] "(It's so big...)"
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                her_[12] ".............."
                her_[17] "well, so be it..."
                her_[17] "You can keep touching yourself, [genie_name]..."
                her_[1] "But you must promise me not to..."
                her_[5] "Not to... em..."
                her_[4] "Not to discharge..."
                her_[8] "Not in front of me, [genie_name]..."
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                her_[19] "......................."
                ">You start to stroke your cock even harder..."
                g4 "Yes, I know you want this! Yes!"
                her_[19] "................"
                show screen blkfade 
                with d3
                ">You are about to cum..."
                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        her_[15] "..............."
                        ">Hermione covers up..."
                    "-Just start cumming-":
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        g4 "Argh! You whore!"
                        her_[21] "Proff-- ??"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_[23] "[genie_name], no, you promised!"
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_[10] "[genie_name], how could you...?"
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        if custom_outfit == 0:
                            $ badges = False # Turns off badges from hermione_main screen.
                        $ sperm_on_tits = True
                        $ h_body = "01_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        pause
                        her "My uniform..."
                        her "It's ruined...."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        her "................"
                        her "I need to clean myslef up..."
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        
                        $ badges = True # Turns badges back on from hermione_main screen.
                        $ lift_shirt = False
                        
                        show screen hermione_main
                        with d3
                        pause
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "How could you do this to mr, [genie_name]?!"
                        her "You gave me your word!"
                        hide screen hermione_main
                        with d3
                        $ mad += 45
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                her_[6] "[genie_name]?"
                ">You stare at Hermione's breasts with hunger..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                if whoring >= 17:
                    her_[16] "ah..."
                    her_[17] "It's so big..."
                    her_[18] "You just couldn't help yourself, could you [genie_name]?"
                    her_[16] ".................."
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    her_[16] ".............."
                    her_[17] "well, so be it..."
                    her_[1] "But you must promise me not to..."
                    her_[5] "Not to... ehm..."
                    her_[6] "Not to cum on me, [genie_name]..."
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    her_[16] "......................."
                    ">You start to stroke your cock even harder..."
                    g4 "Yes, I know you want this! Yes!"
                    her_[16] "................"
                    show screen blkfade 
                    with d3
                    # SAME AS PREVIOUS EVENT^^^
                else:
                    her_[13] "[genie_name], actually I never agreed to this..."
                    m "What are you complaining about, [hermione_name]?"
                    m "I'm not even touching you..."
                    her_[13] "Yes, but you are... touching yourself, [genie_name]."
                    #">You pick up the pace..."
                    m "Just stand still, bitch."
                    m "It will be over soon."
                    her_[13] ".................."
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    her_[12] ".............."
                    her_[17] "well, so be it..."
                    her_[1] "But you must promise me not to..."
                    her_[5] "Not to... ehm..."
                    her_[4] "Not to discharge..."
                    her_[4] "Not in front of me, [genie_name]..."
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    her_[12] "......................."
                    ">You start to stroke your cock even harder..."
                    g4 "Yes, I know you want this! Yes!"
                    her_[12] "................"
                    show screen blkfade 
                    with d3
                    # SAME AS PREVIOUS EVENT^^^
                menu:
                    g4 "Argh! (I'm about to cum!)"
                    "-Hold it in-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        her_[12] "..............."
                        her_[12] "Ehm... I read that that is bad for you, [genie_name]..."
                        m "Huh?"
                        her_[13] "It is bad for your health to just hold it in like this..."
                        her_[12] "Em..."
                        her_[14] "If you want to you can--"
                        g4 "Argh! You whore!"
                        her_[7] "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_[9] "[genie_name], I didn't mean that you can release your... semen on me, [genie_name]..."
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_[18] "Well, what's done is done I suppose..."
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        $ sperm_on_tits = True
                        $ h_body = "01_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        if custom_outfit == 0:
                            $ badges = False # Hides any badges from hermione_main screen.
                        show screen hermione_main
                        with d3
                        pause
                        her "My uniform is ruined though..."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Thank you [genie_name]."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Now I need to clean myself up..."
                        pause
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        $ badges = True # Shows badges on hermione_main screen.
                        $ lift_shirt = False
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        show screen hermione_main
                        pause
                        her "Well, this should do for now..."
                        hide screen hermione_main
                        with d3
                    "-Just start cumming-":
                        g4 "Argh! You whore!"
                        her_[7] "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_[13] "ah...{image=textheart.png} It's so hot...{image=textheart.png}"
                        her_[9] "[genie_name], you promised..."
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_[15] "Well, what's done is done I suppose..."
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        $ badges = True # Hides any badges from hermione_main screen.
                        $ lift_shirt = False
                        $ sperm_on_tits = True
                        $ h_body = "01_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        pause
                        her "My uniform is ruined though..."
                        m "Don't worry, I'm sure no one will notice."
                        m "You did good."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_84.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Thank you [genie_name]."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_83.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Now I need to clean myself up..."
                        pause
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        $ badges = True # Turns the badges layer back on.
                        $ lift_shirt = False
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.
                        hide screen blkfade
                        with d5
                        $ badges = True # Hides any badges from hermione_main screen.
                        if custom_outfit == 7.2:
                            $ custom_outfit = 7
                        show screen hermione_main
                        pause
                        her "Well, this should do for now..."
                        hide screen hermione_main
                        with d3
                        

    
    $ badges = True # Hides any badges from hermione_main screen.
    $ lift_shirt = False
    hide screen jerking_off_01                   
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with fade
    
    hide screen blkfade
    with d3

    if whoring <= 16:
        $ gryffindor +=current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"
    stop music fadeout 10.0

   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    if whoring <= 16:
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
    else:
        $ h_body = "01_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.
    show screen hermione_main
    with d3
    her ".................."
    her "Thank you [genie_name]..."
    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    
    if whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_08_01 = True # HEARTS.
        $ new_request_08_heart = 1
    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_08_02 = True # HEARTS.
        $ new_request_08_heart = 2
    if whoring >= 12:
        $ level = "05"
        $ new_request_08_03 = True # HEARTS.
        $ new_request_08_heart = 3

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ panties = True
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_walk_01_f 
    $ hermione_chibi_xpos = 610 #Near the desk.
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)    
        
    if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.    
        her_[12] "(How humiliating... What have I become...?)"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)
    elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
        her_[12] "........................"
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    elif whoring >= 17 and aftersperm: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        her_[6] "{size=-5}(That was so exhilarating...){/size}"
        her_[37] "{size=-5}(I wonder if anyone will notice my uniform!){/size}"
        her_[37] "{size=-5}(What will people think of me?){/size}"
        her_[16] "................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        her_[6] "{size=-5}(That was so humiliating...){/size}"
        her_[24] "{size=-5}(No, Hermione, you silly girl!){/size}"
        her_[24] "{size=-5}(We are doing this to protect the honour of our house!){/size}"
        her_[16] "................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  
    else:
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        hide screen hermione_01_f #Hermione stands still.
        with Dissolve(.3)  


        
    if whoring <= 8:
        $ whoring +=1
        

    $ request_08_points += 1
        
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
    
    
###################REQUEST_09 (Level 03) (Show me pussy).###############################################################################################
label new_request_09: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main 
    with d3
    if request_09_points == 0:
        m "{size=-4}(Should I ask the girl to show me her pussy?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to show me her pussy again?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    
    if request_09_points == 0 and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "[hermione_name]..."
        m "I would like to award \"Gryffindor\" with  25 house points today."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Really?"
        her "Thank you so much, [genie_name]!"
        m "Yes, but I will require your help..."
        her "Of course, [genie_name]! Anything!"
        m "I need to to lift your skirt..."
        her "...?"
        m "Pull down your panties..."
        her "?!!"
        m "And show me your pussy!"
        if whoring <=5:
            jump too_much
        her "[genie_name]!"
        her "This this is a completely new level of inappropriate, even for you, [genie_name]!"
        her "How can ask such for a thing of your pupil?"
        m "So that's how you feel then? I see..."
        m "I will be awarding those points to some other house then I suppose..."
        m "\"Slytherin\" perhaps?"
        her "................"
        m "But you know, no pressure..."
        her "[genie_name]..."
        her "The fate of my house is very important to me..."
        m "Is it really?"
        m "Why don't you show it to me then?"
        m "Yes. Show me how important it is to you exactly [hermione_name]."
        her "But this is so inappropriate..."
        m "Are we still in any position to discuss what is appropriate and what is not, [hermione_name]?"
        her ".................."
        m "I would say that ship has sailed a long time ago..."
        her ".............."
        m "All I want to do is take a quick peek..."
        her "But why? Why must I do this, [genie_name]?"
        m "A minute of your time and \"Gryffindor\" gets 25 house points..."
        m "A pretty nice deal, wouldn't you agree?"
        her "I suppose..."
    else:
        m "[hermione_name]?"
        her "Yes..."
        m "I need to see your pussy..."
        if whoring >= 6 and whoring <= 8: #LEVEL 03 <=========================================================================================== FIRST EVENT
            her "Agh... Not that again, [genie_name]..."
            her "{size=-5}...so embarrassing...{/size}"
            m "25 house points, [hermione_name]..."
            her ".............."
        if whoring >= 9 and whoring <= 11: #LEVEL 04 <=========================================================================================== SECOND EVENT
            her "*Sigh*... If I must..."      
        if whoring >= 12 and whoring <= 14: # LEVEL 05 <=========================================================================================== THIRD EVENT
            her "Really?"
            her "Well, alright..."

  
#    if whoring >= 6 and whoring <= 8: #LEVEL 03 <=========================================================================================== FIRST EVENT

#    if whoring >= 9 and whoring <= 11: #LEVEL 04 <=========================================================================================== SECOND EVENT
  
#    if whoring >= 12 and whoring <= 14: # LEVEL 05 <=========================================================================================== THIRD EVENT
    

        
    
    
    
    
    if whoring <=5:
        jump too_much
        

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    m "Show me your pussy..."
    if request_09_points == 0: #One star.
        her "Oh... "
        ">Hermione pulls her up her skirt and pulls down her panties. She is blushing and looks angry."
    
    elif request_09_points == 1: #Two stars.
        her "...yes, [genie_name]."
        ">Hermione pulls her up her skirt and pulls down her panties. She looks impatient."
        
    elif request_09_points == 2: #Three stars.
        her "Of course, [genie_name]..."
        ">Hermione pulls her up her skirt and pulls down her panties. She looks very nonchalant."
        
    elif request_09_points >= 3: #Master.
        her "Here you go, Headmaster."
        ">Hermione pulls her up her skirt and pulls down her panties. She is smiling lightly."
    
    "You dismiss Hermione."
        
    if whoring <= 8:
        $ whoring +=1

    if request_09_points <= 2:
        $ gryffindor +=25
        "gryffindor got +25 points."
    else:
        $ gryffindor +=7
        "gryffindor got +7 points."
       
    $ request_09_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu    
    

    
##################################################################################################################################
### LEVEL 04 #####################################################################################################################
###################REQUEST_11 (Level 04) (DANCE FOR ME AND SNAPE) (Day/Night) ################################################################
label new_request_11: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3
   
    m "{size=-4}(Ask her to dance for me?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request

    if "heart_dancer" in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                m "A Dancer."
                if whoring >= 15:
                    $ changeHermioneMainScreen(hg_pth+"body_30.png")
                    her "A Dancer?"
                    m "Don't worry, your nipples will be covered."
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
                    $ custom_outfit = 4
                    $ stockings = 0
                    $ panties = False
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass

    $ current_payout = 35 #Because will have option to pay extra.

    if request_11_points == 0: #<==============================EVENT 01
        
        m "[hermione_name], I need you to dance for me a little."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "You want me to..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "...dance for you, [genie_name]?"
        if whoring <=8:
            jump too_much
        $ new_request_11_01 = True # HEARTS
        $ new_request_11_heart = 1
        m "Yes... You think you could manage that?"
        her "Ehm... I suppose so..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Is this your official wish, [genie_name]?"
        with hpunch
        g4 "What did you just say!?"
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "I mean, favour. Is this an official favour [genie_name]?"
        show screen whitetone8
        hide screen blktone
        with Dissolve(1)
        hide screen hermione_main
        with Dissolve(1)
        g4 "(\"Is this your official wish, master....?\")"
        m "(Man, this sure brings back memories...)"
        m "(Agrabah and genie the joker...)"
        m "(A pre-akabur era of my life...)"
        m "(Simpler times...)"
        g4 "(The bastard ruined my life!)"
        her "Em... [genie_name]?"
        hide screen whitetone8
        with Dissolve(1)
        show screen hermione_main
        with d3
        call music_block
        her "[genie_name]..?"
        m "Hermione, right..."
        m "Got lost in my thoughts for a moment there..."
        her "So am I getting paid for this?"
        m "Of course, [hermione_name]!"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "So... Just a little dancing then..."
        m "Whenever you're ready..."
        her "................."
        hide screen hermione_main
        with d3
        ">Hermione starts dancing..."
        stop music fadeout 1.0
        hide screen blktone
        $ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos = 240 #Default: 250
        show screen clothed_dance #Hermione stands still.
        with fade
        m "Hm..."
        her_[12] "{size=-5}(...........................................){/size}"
        her_[4] "{size=-5}(This is silly...){/size}"
        ">Hermione looks embarrassed but she keeps on \"dancing\"..."
        m "..................."
        her_[4] "{size=-5}(...........................................){/size}"
        m "Alright, you can start undressing now."
        show screen hermione_02 #Hermione stands still.
        with hpunch
        her_[7] "??!"
        her_[8] "I thought all I had to do was dance?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Really? That's adorable."
        m "Now start taking off those clothes."
        her_[12] "You want me to... strip for you...?"
        m "Yes. And I expect you to do it today, [hermione_name]."
        her_[19] "[genie_name]!"
        m "don't you raise your voice at me, [hermione_name]!"
        her_[7] ".....!!?"
        m "Nobody is forcing you to do this."
        m "I am doing you a favour!"
        m "If you don't need the points, please feel free to leave."
        her_[8] "....................."
        her_[12] "......................................."
        ">Hermione is starting to dance again..."
        show screen clothed_dance #Hermione stands still.
        with fade
        her_[15] "{size=-5}(...........................................){/size}"
        m "What are you waiting for then?"
        m "Start with the vest."
        her_[12] "............................................................."
        ">Hermione gives you a confused look and then takes off her vest..."
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        her_[19] "{size=-5}(Am I really going to do this?){/size}"
        menu:
            m "......................."
            "\"Now get rid of your skirt!\"":
                her_[19] "................................."
                show screen blktone
                with d3
                ">Hermione starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                hide screen blktone
                with d3
                her_[19] "{size=-5}(Here it comes then...){/size}"
                her_[24] "{size=-5}(For the honour of the \"Gryffindor\"....){/size}"
                ">Hermione takes of her  skirt..."
                show screen ctc
                pause
                show screen no_skirt_dance
                with d3
                pause
                m "..............."
                her_[19] "{size=-5}(.........................................){/size}"
                ">Hermione keeps on dancing..."
                m "Alright, your shirt is next!"
                her_[20] "My shirt....?"
                show screen blktone
                with d3
                ">Hermione looks extremely embarrassed..."
                ">She clumsily fumbles with the buttons of her shirt..."
                hide screen blktone
                with d3
                m "What's the problem, [hermione_name]?"
                her_[19] "I'm sorry, [genie_name]..."
                her_[19] "It's stuck..."
                her_[19] "It won't budge..."
                her_[28] "Why won't it budge?! *sob*"
                her_[28] "No, I can't do this, [genie_name]! *sob*"
                m "What?"
                her_[28] "I thought I could, but..."
                her_[28] "Stripping for you, [genie_name]?"
                her_[28] "People look up to me in this school!"
                her_[28] "I have a reputation...*sob*"
                her_[29] "And if I do this..."
            "\"Now take off your shirt!\"":
                her_[19] "................................."
                show screen blktone
                with d3
                ">Hermione starts to unbutton her shirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the last button is undone and she has no choice but to take the shirt off..."
                hide screen blktone
                with d3
                her_[19] "{size=-5}(Alright, here it comes...){/size}"
                her_[19] "{size=-5}(For the honour of the \"Gryffindor\"!){/size}"
                show screen blktone
                with d3
                ">Hermione takes off her shirt..."
                hide screen blktone
                with d3
                show screen ctc
                pause
                show screen no_shirt_dance
                with d3
                pause
                her_[40] "{size=-5}(I actually did it...){/size}"
                her_[40] "{size=-5}([genie_name] can see my breasts while I'm dancing for him...){/size}"
                her_[40] "{size=-5}(This is so demeaning...){/size}"
                her_[40] "{size=-5}(But I am doing this for my house...){/size}"
                m "Not bad...."
                her_[40] "{size=-5}(.........................................){/size}"
                show screen blktone
                with d3
                ">Hermione is topless now..."
                ">She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
                ">It seems like she's desperately trying to prevent her breasts from bouncing or swaying..."
                hide screen blktone
                with d3
                m "Alright, your skirt is next!"
                her_[40] "...................."
                show screen blktone
                with d3
                ">Hermione looks extremely embarrassed..."
                show screen blktone8
                with d3
                ">She fumbles with the zipper of her skirt..."
                m "What's the problem, [hermione_name]?"
                her_[40] "I'm sorry, [genie_name]..."
                her_[40] "It's stuck..."
                her_[40] "It won't budge..."
                her_[40] "Why won't it budge?! *sob*"
                her_[41] "No, I can't do this, [genie_name]! *sob*"
                m "What?"
                her_[41] "I thought I could, but..."
                her_[41] "Stripping for points, [genie_name]?"
                her_[41] "People look up to me in this school!"
                her_[41] "I have reputation...*sob*"
                her_[42] "And If I do this..."
                
        show screen blkfade 
        with d3
        hide screen blktone8    
        ">Hermione quickly puts her uniform back on..."
        stop music fadeout 1.0
        show screen hermione_02 #Hermione stands still.
        hide screen blkfade
        with d3
        her_[31] "[genie_name], I think I'd better go now... *Sob!*"
        menu:
            "\"Alright. I had fun. Here are your points.\"":
                $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                show screen hermione_main
                her "Really? I didn't ruin it completely then?"
                hide screen hermione_main
                pause.2 #Otherwise a bug occurs. 
                $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
            "\"Sure. You will receive no points though.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                show screen hermione_main
                her "[genie_name]... I may not be very good at this..."
                her "But I did my best... I think I deserve some--"
                hide screen hermione_main
                m "Just make sure you try harder next time, [hermione_name]."
                $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                show screen hermione_main
                her "Next time?!"
                $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                her2 "I assure you, [genie_name], there will be no next time..."
                hide screen hermione_main
                m "We'll see..."
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                show screen hermione_main
                her "Tsk!"
                hide screen hermione_main
                pause.2 #Otherwise a bug occurs. 
                $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ mad += 35
                call music_block
                jump could_not_flirt

    if request_11_points == 1: #<====================================================================================================================EVENT 02 
        $ new_request_11_02 = True # HEARTS 
        $ new_request_11_heart = 2
        m "[hermione_name], I need you to dance for me."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "That again, [genie_name]...?"
        m "You will get paid accordingly of course..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "............................"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "And you expect me to... ehm..."
        m "Take your clothes off. Naturally."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        stop music fadeout 1.0
        her "......................"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Well, why not?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Yes, I don't see why not!"
        m "Hm...? {size=-4}(Look at her, so eager all of a sudden...){/size}"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "After all, as a pupil I am meant to obey your every order, isn't that right, [genie_name]?!"
        m "...................."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "If the Headmaster tells me to strip for him, Then I shall strip!!!"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Do I find this extremely inappropriate, disgraceful and humiliating?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Of course not. What nonsense!"
        m ".............."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Ha! Might as well do this the proper way!"
        hide screen hermione_main
        with d3
        hide screen blktone 
        with d3
        m "??!"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause 5
        g4 "!!!!!!"
        ">To your surprise Hermione just hops onto your desk and starts dancing franticly..."
        hide screen blkfade
        $ hermione_chibi_xpos = 210 #Near the desk: 400.
        $ hermione_chibi_ypos = 180 #Default: 250
        show screen clothed_dance #Hermione stands still.
        show screen ctc
        with fade
        pause
        show screen bld1
        show screen blktone
        with d3
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
        show screen hermione_main
        her2 "If I must degrade myself in order to protect the honour of my house..."
        hide screen hermione_main
        ">Hermione is starting to take off her vest..."
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Flashing panties
        show screen hermione_main
        her "So be it then!"
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Flashing panties
        her "Just..."
        $ h_body = "01_hp/13_hermione_main/body_88.png" #Flashing panties
        her "*groan*"
        hide screen hermione_main
        show screen blktone8
        hide screen blktone
        with d3
        ">Her vest seems to be stuck somehow, but the girl keeps pulling on at the fabric with anger..."
        show screen hermione_main
        her "Why won't it....?!"
        $ h_body = "01_hp/13_hermione_main/body_81.png" #Flashing panties
        her "There!"
        hide screen hermione_main
        ">Hermione finally manages to untangle herself and sends the vest flying to the other side of the room..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        show screen bld1
        with d3
        show screen hermione_main
        hide screen ctc
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
        her "The skirt is next, right?"
        hide screen hermione_main
       
        menu:
            m "..."
            "\"Yes, that's right. Take it off!\"":
                show screen hermione_main
                her "Of course!"
                $ h_body = "01_hp/13_hermione_main/body_87.png" #Flashing panties
                her "Here it goes!"
                hide screen hermione_main
                pause.1
                show screen blktone8
                with d3
                ">Hermione sends her skirt flying across the room, just like she did with her vest a moment earlier..."
            "\"You need to calm down, [hermione_name]. \"":
                show screen hermione_main
                her2 "Well, {size=+7}EXCUSE ME{/size}, [genie_name]!"
                her2 "You told me to strip for you, but you never told me your preferences in regards to the pace!"
                hide screen hermione_main
                m "Well, I'm telling you now, [hermione_name]!"
                show screen hermione_main
                her2 "Too late!"
                hide screen hermione_main
                pause.1
                show screen blktone8
                with d3
                ">And sure enough Hermione sends the skirt flying across the room, just like she did with her vest a moment earlier..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        show screen no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "{size=-4}(Wow, she is getting really worked up over this...){/size}"
        m "{size=-4}(Maybe it was still too early to--{/size}"
        $ h_body = "01_hp/13_hermione_main/body_66.png" 
        show screen hermione_main
        her "My shirt?!!"
        $ h_body = "01_hp/13_hermione_main/body_86.png" 
        her "{size=+9}I don't need it!{/size}"
        hide screen hermione_main
        pause.1
        show screen blktone8
        with d5
        ">Hermione's shirt suddenly hits the floor."
        g4 "{size=-4}(When did she??!){/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_shirt_no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        show screen hermione_main
        hide screen ctc
        her "Do you enjoy this, [genie_name]?"
        $ h_body = "01_hp/13_hermione_main/body_30.png" 
        her2 "Shall I shake my breasts for you like one of those harlots?"
        hide screen hermione_main
        m "Well---"
        show screen hermione_main
        her2 "Of course! Why wouldn't I degrade myself for your pleasure?!"
        $ h_body = "01_hp/13_hermione_main/body_86.png" 
        her2 "This is completely {size=+7}acceptable!{/size}"
        hide screen hermione_main
        pause.1
        show screen blktone
        with d3
        ">Hermione is starting to shake her naked breasts rather clumsily..."
        ">As you watch the girl's tits sway right and left before your face you find yourself fighting the urge to..."
        menu:
            m "..."
            "-Grab them!-":
                g9 "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}"
                g9 "{size=-4}(Maybe pull on them a little, yes...){/size}"
            "-Slap them!-":
                m "{size=-4}(I want to slap the crap out of her fun bags.){/size}"
                g9 "{size=-4}(Yes, just slap them around a little...){/size}"
            "-Bite on them!":
                m "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}"
                m "{size=-4}(No, it's not weird!){/size}"
                m "{size=-4}(Just a couple of gentle love-bites!){/size}"
                g9 "{size=-4}(Yes... Maybe more than just a couple...){/size}"
            "-Motorboat them!-":
                m "{size=-4}(I just want to put my face right in between them!){/size}"
                g9 "{size=-4}(Yes, To motorboat these titties would be the best!){/size}"
        ">While you are lost in thought, Hermione keeps on dancing..."
        
        if custom_outfit == 0:
            $ badges = False # Turns off the badges layer.
        
        $ h_body = "01_hp/13_hermione_main/body_89.png" 
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ h_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        show screen hermione_main
        her2 "(Dancing naked in front of the headmaster...)"
        her2 "(If my parents knew about this they would lose their minds...)"
        $ h_body = "01_hp/13_hermione_main/body_90.png"
        her2 "(Especially my father...)"
        hide screen hermione_main
        ">Hermione is starting to shake her tits again...)"
        show screen hermione_main
        her "(Hermione Granger - the stripper...)"
        $ h_body = "01_hp/13_hermione_main/body_91.png"
        her2 "(Forgive me father...)"
        hide screen hermione_main
        pause.1
        show screen blktone8
        hide screen blktone
        with d3
        ">Hermione puts her hands on her tits and starts squeezing them..."
        ">You can only assume that she means to look seductive, but she just looks awkward and ashamed."
        show screen hermione_main
        her2 "(I used to be a top student... Used to have standards...)"
        hide screen hermione_main
        ">Hermione clutches her tits even harder and then gives them a couple of twists..."
        ">It almost looks as if she is mad at her own breasts and trying to punish them..."
        ">You find the thought strangely arousing..."
        $ h_body = "01_hp/13_hermione_main/body_92.png"
        show screen hermione_main
        $ h_c_u_pic = "01_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        her "Well, I hope you enjoyed yourself, [genie_name]!"
        hide screen hermione_main
        m "What?"
        $ h_body = "01_hp/13_hermione_main/body_93.png"
        show screen hermione_main
        her "I would like to get paid now..."
        hide screen hermione_main
        m "Aren't you forgetting something, [hermione_name]?"
        $ h_body = "01_hp/13_hermione_main/body_92.png"
        show screen hermione_main
        her2 "[genie_name]...?"
        hide screen hermione_main
        m "Your panties...?"
        $ h_body = "01_hp/13_hermione_main/body_94.png"
        show screen hermione_main
        her "My panties?"
        her "But, they always leave them on!"
        hide screen hermione_main
        m "Who exactly are \"they\"?"
        m "Strippers in kid's cartoons?"
        m "Stripping is stripping, [hermione_name]!"
        m "Now take off your panties!"
        $ h_body = "01_hp/13_hermione_main/body_95.png"
        show screen hermione_main
        her "................"
        hide screen hermione_main
        ">Hermione looks horror-struck. All of her anger is gone..."
        $ h_body = "01_hp/13_hermione_main/body_90.png"
        show screen hermione_main
        her "................."
        hide screen hermione_main
        ">Without saying another word..."
        ">She starts to pull down her panties..."
        g9 "......................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        hide screen blktone8
        hide screen bld1
        show screen snape_walk_01 
        with d3
        pause 1.5
        stop music 
        $ renpy.play('sounds/scratch.wav')
        show screen snape_02 #Snape stands still.
        
        $ tt_xpos=330 #Defines position of the Snape's full length sprite. (Default 300). 140 - center.
        $ tt_ypos=340#(Default 0). Right bottom corner: 340
        $ s_sprite = "01_hp/10_snape_main/snape_01.png"
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. Works for all full size sprites.
        show screen s_head
        $ h_c_u_pic = "01_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        
        
        
        sna2 "Listen, Genie. I've been thinki--"
        $ s_sprite = "01_hp/10_snape_main/snape_11.png"
        with hpunch
        sna2 "................................................................................................................................................................................"
        $ h_body = "01_hp/13_hermione_main/body_96.png"
        show screen h_head
        with hpunch
        her "(Professor Snape???????!)"
        $ s_sprite = "01_hp/10_snape_main/snape_12.png"
        show screen s_head
        sna2 "Miss Granger?"
        show screen h_head
        her "(No, no... This is not happening. Please...)"
        hide screen h_head
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "...................................."
        show screen bld1
        with d3
        menu:
            m "..."
            "\"Severus, I am busy right now.\"":
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Yes... I can see that..."
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "{size=-7}(I want to die!){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "I shall postpone our conversation for later then, Geni-- *khem!* Albus."
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                sna "Miss Granger..."
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her ".........................................."
                hide screen h_head
            "\"Severus! Please, come join us.\"":
                $ mad += 37
                $ snape_invated_to_watch = True #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
                $ s_sprite = "01_hp/10_snape_main/snape_14.png"
                show screen s_head
                sna "Seriously?"
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "([genie_name], no, please.............................)"
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "A very tempting offer indeed..."
                $ h_body = "01_hp/13_hermione_main/body_95.png"
                show screen h_head
                her "!!!!!!......."
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna2 "Well, maybe some other time..."
                $ h_body = "01_hp/13_hermione_main/body_99.png"
                show screen h_head
                her "{size=-5}(There will be no other time!){/size}"
                her "{size=-5}(I will stop selling favours from now on, I swear!){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "I shall postpone our conversation then, Geni-- *khem!* Albus."
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                sna2 "Miss Granger..."
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "................................."
                hide screen h_head
        show screen blkfade 
        with d3
        hide screen snape_walk_01 
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause 1.5

        
        ">Snape leaves..."
        ">Hermione hastily hops off your desk."
        ">She starts putting her clothes back on rather frantically..."
        $ h_body = "01_hp/13_hermione_main/body_98.png"
        show screen h_head
        her "My shirt! Where is my shirt?!"
        hide screen h_head
        m "It's over there, by the fireplace..."
        $ h_body = "01_hp/13_hermione_main/body_85.png"
        show screen h_head
        her2 "................................"
        hide screen h_head
        pause 2
        $ h_body = "01_hp/13_hermione_main/body_33.png"
        show screen h_head
        
        $ badges = True # Turns the badges layer back ON.
        
        her "........................"
        $ h_body = "01_hp/13_hermione_main/body_34.png"
        stop music fadeout 2.0
        her "Can I just get my points now, please?"
        hide screen h_head
        hide screen snape_02 #Snape stands still.
        pause.1
        $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. On top of EVERYTHING = 8.
        $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        $ hermione_chibi_ypos = 250 #Default: 250. Another number is 180
            
    if request_11_points >= 2: #<====================================================================================================================EVENT 03
        $ new_request_11_03 = True # HEARTS
        $ new_request_11_heart = 3
        if snape_invated_to_watch: #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
            m "(Hm... Should I invite that Professor Snape guy to watch as well?)"
            menu:
                "\"Yes! Hermione needs an audience!\"":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        with d3
                        m "Miss, Granger, I will be buying another favour from you today."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Of course, [genie_name]."
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "...professor Snape?"
                        her "May I ask, why, [genie_name]?"
                        m "Oh, I just think you could use a bigger audience for your striptease performance."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "My striptease performance...?!!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "With all due respect, [genie_name]..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "{size=-5}(Which I have oh so little left for you...){/size}"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "I refuse to degrade myself for professor Snape's amusement!"
                        m "No, no, you got it all wrong, [hermione_name]."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Hm..?"
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "!!!"
                        m "Yes, I want to catch him in the act!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "[genie_name], I didn't realize..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "I see now..."
                        her "I am sorry for doubting you [genie_name]..."
                        m "No biggy. Now go find professor Snape and bring him here."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Right away [genie_name]!"
                        label fetching_snape:
                        hide screen hermione_main
                        with d3
                        hide screen bld1
                        with d3
                        hide screen hermione_02 #Hermione stands still.
                        $ walk_xpos=400 #Animation of walking chibi. (From)
                        $ walk_xpos2=610 #Coordinates of it's movement. (To)
                        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01_f 
                        pause 2
                        hide screen hermione_walk_01_f 
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        with Dissolve(.3)
                        pause.2
                        show screen blkfade
                        with d5
                        stop music fadeout 1.0
                        ">...................{w}...................{w}...................{w}..................."
                        hide screen blkfade
                        with d5
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=360 #Coordinates of it's movement. (To)
                        $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                        show screen snape_walk_01 
                        
                        pause 4
                        show screen snape_02 #Snape stands still.

                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ hermione_chibi_xpos = 610
                        $ hermione_chibi_ypos = 250
                        show screen hermione_02 #Hermione stands still.
                        with Dissolve(.5)
                        pause.3
                        
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=500 #Coordinates of it's movement. (To) 400 - near desk.
                        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01 
                        pause 3
                        $ hermione_chibi_xpos = 500 #Near the desk - 400
                        show screen hermione_02 #Hermione stands still.
                        pause.5
                        show screen ctc
                        pause
                        show screen bld1
                        with Dissolve(.3)
                        $ tt_xpos=180 #Defines position of the Snape's full length sprite. Default - 300
                        $ tt_ypos=0
                        $ s_sprite = "01_hp/10_snape_main/snape_01.png"
                        show screen snape_main
                        show screen ctc
                        with Dissolve(.3)
                        
                    else:
                        hide screen blktone
                        with d3
                        m "Miss, Granger, I will be buying another favour from you today."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Of course, [genie_name]."
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "...professor Snape?"
                        her "may I ask, why, [genie_name]?"
                        m "Oh, I just want you to dance for us."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "!!!"
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "But didn't we already establish that last time I did this?"
                        m "Well, ehm... sure..."
                        m "But I will need more proof if I am to take this issue to the ministry of magic!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "....."
                        m "So, what do you say [hermione_name]?"
                        m "One more dance for the greater good?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Well, alright..."
                        m "Good. Go find professor Snape then."
                        jump fetching_snape
                    
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Genie... err, I mean Albus, you wanted to see me?"
                    m "Yes. Are you in the mood for a little striptease?"
                    hide screen snape_main
                    with d3
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
                    show screen snape_main
                    with d3
                    sna "Oh...?"
                    sna "Miss Granger here will be performing I assume?"
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her ".............."
                    m "Yes, our little mynx is more than happy to take off her clothes for our entertainment."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "............"
                    m "Aren't you [hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Yes, [genie_name]."
                    m "Let's get started then!"
                    hide screen hermione_main
                    hide screen snape_main
                    
                    pause
                    
                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 1
                    $ h_body = "01_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "............."

                    
                    
                    $ s_head_xpos = 330 # x = 330,
                    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "......................"
                    hide screen s_head2
                    m ".........................."
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    show screen s_c_u
                    $ s_c_u_pic = "01_hp/09_snape_ani/snape_0130.png"
                    $ snape_chibi_xpos = 290 #Default 360.
                    $ snape_chibi_ypos = 210
                    with fade
                    pause
                    show screen bld1
                    with d3
                    m "So... Severus... How's life?"
                    $ s_sprite = "01_hp/10_snape_main/snape_09.png"
                    show screen s_head2
                    sna "Well, you know... same old, same old..."
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png"
                    sna " The Students are causing me grief..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    sna2 "In fact, miss Granger here managed to cause me more stress than any other student..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_68.png"
                    her "..............................."
                    hide screen h_head2
                    m "Oh, I am sure she is very sorry about that..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_74.png"
                    her "{size=-4}(Not even a little bit!){/size}"
                    hide screen h_head2
                    m "And will make up for it today, won't you [hermione_name]?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_53.png"
                    her "Uhm... Yes, [genie_name]."
                    hide screen h_head2
                    hide screen ctc
                    pause.2
                    show screen blktone
                    with d3
                    ">Hermione takes her vest off and starts to sway her hips seductively."
                    hide screen blktone
                    with d3

                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_87.png"
                    her "..................."
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "Hm... You are being suspiciously quiet [hermione_name]."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_48.png"
                    her "{size=-4}(Oh no! Is he onto us?){/size}"
                    $ h_body = "01_hp/13_hermione_main/body_57.png"
                    her2 "I am just doing what the headmaster told me, [genie_name]..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you do every other day?"
                    hide screen s_head2
                    m "Severus..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "No, Albus I want to hear little miss perfect's answer."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_57.png"
                    her2 "I just want you to have a good time, [genie_name]..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Oh! It's \"[genie_name]\" now, isn't I?"
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png"
                    sna2 "What happened to \"snape'o'doodle\" and \"Professor Snivellus\"??!"
                    hide screen s_head2
                    g9 "{size=-5}( \"snape'o'doodle\, heh... that's funny.){/size}"
                    show screen h_head2 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_57.png" # HERMIONE
                    her "............."
                    $ s_sprite = "01_hp/10_snape_main/snape_08.png"
                    show screen s_head2
                    sna2 "Yes, I know what are you calling me behind my back, you wretched girl!"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_86.png"
                    her2 "Well, maybe that's because you deserve it... [genie_name]."
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "What?!"
                    sna "How dare you....?"
                    $ s_sprite = "01_hp/10_snape_main/snape_15.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Who do you think you are? You filthy mu--"
                    show screen h_head2 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_62.png" # HERMIONE
                    her2 "[genie_name], one of your staff is verbally abusing me!"
                    her2 "Are you going to allow this?"
                    $ s_sprite = "01_hp/10_snape_main/snape_08.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Verbally abusing...?! You have some nerve, girl!"
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna2 "Albus, will you allow her to talk back to a teacher like that?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_62.png" # HERMIONE
                    her "[genie_name]!"
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Albus!"
                    hide screen s_head2
                    menu:
                        m "..."
                        "\"[hermione_name], show some respect!\"":
                            $ mad += 9
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_61.png" # HERMIONE
                            her "What?"
                            her "But [genie_name]!"
                            hide screen h_head2  
                            m "Young lady, you {size=+4}will{/size} calm down now."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_66.png" # HERMIONE
                            her "Tsk!"
                            hide screen h_head2      
                            m "And take off your skirt already, would you?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......."
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "..........."
                            hide screen s_head2  
                        "\"Severus, you started this.\"":
                            $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                            show screen s_head2  
                            sna "What? Me?!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_52.png" # HERMIONE
                            her "Thank you, [genie_name]."
                            $ s_sprite = "01_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, you are spoiling the girl! She must be taught a lesson!"
                            hide screen s_head2 
                            m "...............Severus."
                            g4 "Did you hit your head?!"
                            $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I beg your pardon?"
                            hide screen s_head2 
                            g4 "The girl is already stripping for you!"
                            g4 "What punishment are you talking about?"
                            $ s_sprite = "01_hp/10_snape_main/snape_16.png" #SNAPE
                            show screen s_head2  
                            sna "Tsk... How about a flogging?" 
                            hide screen s_head2
                            g4 "Severus!"
                            $ s_sprite = "01_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Alright, alright, I see your point..."
                            hide screen s_head2
                            m "[hermione_name], are you going to strip or did you climb on my desk to get a better view?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "Ehm..."
                            hide screen h_head2
                            m "Take of your skirt, [hermione_name]!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "Yes, [genie_name]..."
                            hide screen h_head2
                        "\"Both of you, calm the fuck down.\"":
                            m "You, tall-dark-and-handsome, calm down a bit, would you?"
                            $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I beg your pardon?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Yes! You tell him profess--"
                            hide screen h_head2     
                            m "You as well, you perverted little mynx!"
                            m "Calm down and take your skirt off already."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_79.png" # HERMIONE
                            her "I am not perverted..."
                            hide screen h_head2     
                            m "The skirt, [hermione_name]!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......"
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2  
                            sna "............."
                            hide screen s_head2     
                    
                    show screen blktone
                    with d3
                    ">Hermione swiftly takes off her \"Hogwarts\" skirt..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen s_head2
                    sna "Hm..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                    her "........................"
                    hide screen h_head2
                    m "Yes, much better!"
                    show screen blktone
                    with d3
                    ">Hermione keeps on dancing, while she's Wearing nothing but her shirt now..."
                    menu:
                        m "..."
                        "\"Severus, what about that Potter boy?\"":
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "(.....?)"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2
                            sna "What about him?"
                            hide screen s_head2
                            m "Is he still causing you grief?"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Oh..."
                            sna "Not really, no..."
                            $ s_sprite = "01_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "To be honest I never really had a problem with the boy himself..."
                            sna2 "Although I did plan to make his life here miserable because of his father..."
                            $ s_sprite = "01_hp/10_snape_main/snape_02.png" #SNAPE
                            show screen s_head2    
                            sna2 "But lately I have way more interesting projects to occupy myself with..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "..................."  
                            hide screen h_head2   
                        "\"Severus, what about the Weasleys?\"":
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "What about them?"
                            hide screen s_head2   
                            m "Are they still causing you trouble?"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... More than ever."
                            hide screen s_head2
                            m "Hm...?"
                            m "You seem surprisingly indifferent about that..."
                            $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "That's because I know that they will get what they deserve eventually..."
                            hide screen s_head2
                            m "Revenge? Cool! What do you have in mind?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "!!!"
                            $ s_sprite = "01_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm... Can't discuss this with \"the enemy\" present."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Tsk!"
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "All I can say is that it involves their beloved little sister Ginny..."
                            hide screen s_head2  
                            m "Ginny? Hm... What a curious name for a girl..."
                            m "............."
                            m "So, you plan to fuck her then?"
                            $ s_sprite = "01_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "!!?"
                            $ s_sprite = "01_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, please, not in front of the girl!"
                            hide screen s_head2  
                            m "Alright, alright..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "{size=-5}(Ginny...){/size}"
                            hide screen h_head2 
                        "\"How would you grade Hermione's butt?\"":
                            $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "miss Hermione's buttocks?" 
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "!!!............"
                            hide screen h_head2      
                            m "Sure! As you would grade a paper."
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm..."
                            hide screen s_head2  
                            pause.1
                            ">Professor Snape gives Hermione's buttocks an appraising look..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                            her ".........?"
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I would say..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_59.png" # HERMIONE
                            her "............?!"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... \"{size=+5}F-{/size}\"."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                            her "(What?!)"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Unsatisfactory..."
                            sna2 "Look at that pitiful thing. Tiny and skinny... That's a boy's butt."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_51.png" # HERMIONE
                            her "!!!!!!!!!!"
                            hide screen h_head2   
                            
                    show screen blktone
                    with d3
                    ">One after another, Hermione undoes the buttons of her shirt and then takes it off..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    m "Alright! We Finally get to the good stuff!"
                    $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                    show screen s_head2       
                    sna "Hm..."
                    
                    if custom_outfit == 0:
                        $ badges = False # Hides the layer with badges.
                    
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                    her "........"
                    hide screen h_head2   
                    menu:
                        m "..."
                        "-Start jerking off-":
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_94.png"
                            her "[genie_name]?!"
                            hide screen h_head2
                            m "It's alright, [hermione_name]. Don't mind me..."
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Oh, we're doing it like this then?"
                            sna "Well, don't mind if I do..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                            $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                            her "!!!"
                            hide screen h_head2    
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            $ snape_chibi_xpos = -185
                            $ snape_chibi_ypos = 10
                            $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_95.png"
  
                            her "No, guys... err I mean, sirs... Ehm, professors!"
                            hide screen h_head2
                            m "Don't you mind us [hermione_name], just keep on doing your thing."
                            show screen h_head2
                            her "But..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                            her2 "No! I refuse to dance with those things pointed at me!"
                            her2 "You need to put them away or the dance is over!"
                            hide screen h_head2    
                            m "You aren't in any position to give us orders, [hermione_name]."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_110.png" # HERMIONE
                            her2 "that was not an order, [genie_name]. It was an ultimatum."
                            hide screen h_head2    
                            menu:
                                m "..."
                                "\"Alright Severus, let's be civil...\"":
                                    $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                                    show screen s_head2                                                          #SNAPE
                                    sna2 "I see Miss Granger manages to remain exceptionally stubborn in any situation..."
                                    hide screen s_head2  
                                    show screen blkfade
                                    with d3
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    show screen s_c_u
                                    $ s_c_u_pic = "01_hp/09_snape_ani/snape_0130.png"
                                    $ snape_chibi_xpos = 290 #Default 360.
                                    $ snape_chibi_ypos = 210
                                    pause.3
                                    hide screen blkfade 
                                    with d3
                                    jump civil_with_snape
                                    
                                "\"(Pst! Remember why we are doing this!)\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_104.png" # HERMIONE
                                        her "Oh, right..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "What was that?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her "Please don't mind what I just said..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm...?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her2 "I do not mind you touching yourself in front of me..."
                                        her2 "Yes, I do not mind it at all..."
                                        her "I will just keep on dancing then..."
                                        hide screen h_head2
                                        hide screen ctc
                                        pause.1
                                        show screen blktone
                                        with d3
                                        show screen blktone8
                                        with d3
                                        ">You keep on jerking off while you're watching Hermione dance..."
                                        ">Hermione squeezes her breasts and shakes her hips slightly..."
                                        hide screen blktone8
                                        with d3
                                        m "Yes, [hermione_name]. Very good."
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "*Khem!* Acceptable performance, miss Granger."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "...................."
                                        hide screen h_head2
                                        m "Heh..."
                                        hide screen h_head2
                                        m "How would you grade her tits then?"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "......"
                                        $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm......"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_103.png" # HERMIONE
                                        her "........"
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"B+\"!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "!!!"
                                        hide screen h_head2
                                        m "Really?"
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Yes. I do give credit where credit is due."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                                        her "(Professor...)"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                                        her "(Time for my finishing act then!)"
                                        hide screen h_head2 
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione bends over and slides her panties down."
                                        ">Her movements lack grace..."
                                        ">But a pretty pussy is always a welcome sight nonetheless..."
                                        ">You show your appreciation by stroking your cook even faster..."
                                        
                                       
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        show screen ctc
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        
                                        $ s_sprite = "01_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes... Yes!!!"
                                        sna2 "Now shake those B+ titties for me, you harlot!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "......."
                                        hide screen h_head2       
                                        hide screen ctc
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione suddenly breaks into a series of rather complex pirouettes."
                                        $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes, such grace..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "That lithe young body!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "........."
                                        $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Oh, yes!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                                        hide screen h_head2     
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione seems very focused on her dancing routine..."
                                        hide screen blktone8
                                        with d3
                                        $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes, and now another pirouette!"
                                        sna "Magnificent!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "I would applaud you but one of my hands is very busy at the moment."
                                        hide screen s_head2  
                                        m "{size=-4}(Was that an attempt at a joke?){/size}"
                                        m "{size=-4}(Man, horny Snape is weird...){/size}"
                                        show screen blktone8
                                        with d3
                                        ">Hermione performs another set of movements and pirouettes..."
                                        ">Gives a little curtsy bow to the imaginary public..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                        ">And then slumps down on her butt exhausted."
                                        
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        show screen ctc
                                        pause
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_102.png"
                                        her "Whew... This was--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING WHORE!"
                                        hide screen hermione_main
                                        with d3
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "01_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "01_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        
                                        $ s_sprite = "01_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Good job, you harlot!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Here is your reward!"
                                        hide screen s_head2     
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ snape_chibi_xpos = -210
                                        $ snape_chibi_ypos = 10
                                        $ snape_cum_chibi_xpos =  -210
                                        $ snape_cum_chibi_ypos  = 10
                                        $ s_c_c_u_pic = "snape_cum_01"
                                        show screen s_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "01_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "01_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        $ u_sperm = "01_hp/13_hermione_main/auto_05.png"
                                        her "!!!!!!!!!!!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Oh... Yes..."
                                        hide screen s_head2 
                                        g4 "Little slut!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "..............................."
                                
                                        $ s_c_c_u_pic = "01_hp/08_animation_02/11_cum_18.png"
                                        $ g_c_c_u_pic = "01_hp/08_animation_02/09_cum_18.png"
                                        $ s_sprite = "01_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ha-ha-ha! This is magnificent!"
                                        hide screen s_head2
                                        g9 "I know, right!?"
                                        show screen bld1
                                        with d3
                                        $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                        $ s_c_u_pic = "01_hp/08_animation_02/10_jerking_01.png" # Snape stands still with his dick in hand.
                                        $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes... We should do this more often."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "................."
                                        $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Your performance was acceptable, miss Granger..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "Thank you................"
                                        $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "But if I were to grade it..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "..........."
                                        $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm...."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "............"
                                        $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"{size=+5}F+{/size}\"!"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_112.png" # HERMIONE
                                        stop music
                                        her "{size=+5}WHAT?!!!{/size}"
                                        $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Yes... Quite a few things could use some improvement actually."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_110.png" # HERMIONE
                                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                        her "I cannot believe this!"
                                        hide screen h_head2 
                                        pause
                                        show screen blkfade 
                                        with d3
                                        hide screen h_c_u 
                                        hide screen s_c_c_u
                                        hide screen g_c_c_u
                                        show screen genie
                                        $ snape_chibi_xpos = -60
                                        $ snape_chibi_ypos = 10
                                        $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                                        hide screen chair_02
                                        hide screen g_c_u
                                        hide screen desk_02
                                        $ hermione_chibi_xpos = 300 #Near the desk: 400. (210 - standing on desk.)
                                        $ hermione_chibi_ypos = 260#Default: 250. (180- standing on desk.)
                                        show screen h_c_u 
                                        $ h_c_u_pic = "01_hp/08_animation_02/07_dance_03.png"
                                        ">Hermione furiously jumps off your desk."
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ flip = True # Flips hermione_main screen.
                                        $ u_sperm = "01_hp/13_hermione_main/auto_05.png"
                                        $ h_body = "01_hp/13_hermione_main/body_101.png"
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                                        if custom_outfit == 0:
                                            $ only_upper = True #No legs shown.
                                        show screen bld1
                                        with d5
                                        show screen hermione_main
                                        with d3
                                        pause
                                        hide screen ctc
                                        her "I demand a higher grade than that!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2      
                                        sna2 "You do not demand a grade miss Granger, you earn it."
                                        hide screen s_head2     
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_107.png"          #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "I did earn it!"
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_103.png"               #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "And could you at least have the decency to stop touching yourself, [genie_name]!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2     
                                        sna2 "Tch..."
                                        hide screen s_head2   
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3   
                                        m "(Are they for real?)"
                                        show screen ctc
                                        pause
                                        show screen blkfade
                                        with d7
                                        hide screen ctc
                                        hide screen s_c_u
                                        hide screen h_c_u
                                        $ hermione_chibi_xpos = 400 #Near the desk.
                                        $ hermione_chibi_ypos = 250 #Default: 250
                                        show screen hermione_02 #Hermione stands still.
                                        ">You watch Snape with his dick still hanging out and the cum-covered Hermione argue loudly about her imaginary grade."
                                        ">After a while Professor Snape agrees to change Hermione's grade from \"F+\" to \"D-\"."
                                        ">Then he beats a hasty retreat before Hermione has a chance to start another argument..."
                                        hide screen blkfade
                                        with d5
                                        $ flip = False # Flips hermione_main
                                        $ only_upper = False #Show legs.
                                        $ aftersperm = True #Show cum stains.
                                        $ uni_sperm = False #Don't show cum.
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_29.png"#Sprite of Hermione's upper body.                    #HERMIONE
                                        $ badges = True
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "Well..."
                                        her "Was our mission a success, [genie_name]?"
                                        menu:
                                            m "..."
                                            "\"Huh? What mission?\"":
                                                $ mad += 7
                                                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                $ h_body = "01_hp/13_hermione_main/body_32.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                her "I only agreed to this so that you could catch professor Snape in the act, [genie_name]!"
                                                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                $ h_body = "01_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                her "So that we would have definite proof that he is \"dirty\"!"
                                                m "Oh, that mission..."
                                                m "Yes. Mission accomplished!"
                                            "\"Yes! Thanks to you!\"":
                                                pass
                                        m "Good job. [hermione_name]."
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "I am happy to have been of help, [genie_name]!"
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_34.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "...Can I get paid now, please?"
                                        

                                    else:
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "Oh..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "No, I can't! This is just not worth it!"
                                        hide screen ctc
                                        hide screen h_head2  
                                        pause.1
                                        show screen blkfade
                                        with d5
                                        ">Hermione jumps off the desk and starts to put her clothes back on."
                                        $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Well, this was awfully anticlimactic..."
                                        hide screen s_head2  
                                        g4 "You don't say..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "May as well leave now I suppose. I will talk to you later, Albus."
                                        hide screen s_head2  
                                        m "Yes, later, Severus."
                                        $ s_sprite = "01_hp/10_snape_main/snape_04.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Miss Granger..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "Professor..."
                                        hide screen h_head2          
                                       # her "I would like to get paid now."
                                        show screen ctc
                                        pause.4
                                        hide screen s_c_u
                                        hide screen ctc
                                        ">Professor Snape leaves..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        stop music fadeout 1.0
                                        her "...................."
                                        hide screen h_head2
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                        show screen h_head2                                                              # HERMIONE
                                        
                                        $ badges = True # Turns badges back on.
                                        
                                        $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                                        her "...Can I get paid now... [genie_name]...?"
                                        hide screen h_head2   

                        "-Just keep on watching-":
                            label civil_with_snape:
                                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                            # JUST WATCHING.
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "I will just keep on dancing then..."
                            hide screen h_head2 
                            hide screen ctc
                            pause.1
                            show screen blktone8
                            with d3
                            ">Hermione squeezes her breasts and shakes her hips slightly..."
                            hide screen blktone8
                            with d3
                            m "Yes, [hermione_name]. Very good."
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "*Khem!* Acceptable performance, miss Granger."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "...."
                            hide screen h_head2    
                            m "Heh..."
                            m "How would you grade her tits then?"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "......"
                            $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm......"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "........"
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "\"B+\"!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                            her "!!!"
                            hide screen h_head2
                            m "Really?"
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes. I do give credit where it's due."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_95.png" # HERMIONE
                            her "(Professor...)"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "(Time for my finishing act then!)"
                            hide screen h_head2   
                            pause.1
                            show screen blktone8
                            with d3
                            ">Hermione bends over and slides her panties down."
                            ">Her movements lack grace..."
                            ">But a pretty pussy is always a welcome sight nonetheless..."
                            hide screen blktone
                            with d3
                            $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... Yes..."
                            sna2 "Now shake those B+ titties for me, you harlot!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                            her "......."
                            hide screen h_head2       
                            show screen blktone8
                            with d3
                            ">Hermione suddenly breaks into a series of rather complex pirouettes."
                            $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes, such grace..."
                            $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "That lithe, young body!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                            hide screen h_head2 
                            ">Hermione seems very focused on her dancing routine..."
                            $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2
                            sna "Yes, and now another pirouette!"
                            sna "Magnificent!"
                            hide screen s_head2
                            show screen blkfade
                            with d3
                            ">Hermione performs another set of movements and pirouettes..."
                            ">Gives a little curtsy bow to the imaginary public..."
                            ">And then slumps down on her butt exhausted."
                            $ hermione_chibi_xpos = -210 #400 = Near the desk.
                            $ hermione_chibi_ypos = 10
                            $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                            show screen h_c_u
                            hide screen blkfade
                            with d3
                            hide screen blktone8
                            with d3
                            $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Good job, you harlot!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_105.png" # HERMIONE
                            her "............."
                            if daytime:
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Well, my class is about to start so I will be leaving now."
                                sna2 "Don't you have potion class with me today, MIss Granger?"
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Yes, [genie_name]..."
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Well, don't be late, girl..."
                                hide screen s_head2      
                            else:
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Well, it is getting rather late. I think I will be leaving now."
                                sna2 "Good night, Albus."
                                hide screen s_head2    
                                m "Severus."
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Harlot."
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Professor..."
                                hide screen h_head2      


                            show screen ctc
                            pause
                            show screen blkfade
                            hide screen s_c_u
                            hide screen ctc
                            with d5
                            ">Professor Snape leaves..."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                            stop music fadeout 1.0
                            her "...................."
                            hide screen h_head2
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            $ badges = True
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                            her "May I... may get paid now... [genie_name]...?"
                            hide screen h_head2   


                "\"Nah... That's not a good idea...\"":
                    label no_snape_watching:  
                    hide screen blktone
                    with d3
                    m "[hermione_name], how about another strip?"     
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her ".............."
                    her "I would really rather not, [genie_name]..."
                    m "Why? You are getting quite good at it."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "........................."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Thirty five house points?"
                    m "Sure! The usual rate."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "..................."
                    hide screen hermione_main
                    with d3
                    hide screen bld1
                    with d3
                    pause
                    #Walks to the door
                    
                    $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01_f 
                    pause 2
                    hide screen hermione_walk_01_f 
                    $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    $ h_c_u_pic = "01_hp/animation/h_walk_01.png" 
                    show screen h_c_u
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = "01_hp/animation/h_walk_03.png" 
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = "01_hp/animation/h_walk_01.png" 
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
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d5

                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 5
                    $ h_body = "01_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "Just for the record..."
                    $ h_body = "01_hp/13_hermione_main/body_17.png"
                    her2 "I still consider this a highly inappropriate favour to be buying from one of your students, [genie_name]."
                    hide screen h_head2
                    m "Right. And an equally inappropriate favour to be selling to your headmaster. Woulnd't you agree?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_69.png"
                    her ".........."
                    hide screen h_head2
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    with fade
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_87.png"
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her ".............."
                    $ h_body = "01_hp/13_hermione_main/body_85.png"
                    her2 "What if my parents were to find out about this, [genie_name]?"
                    her2 "Mother would never understand..."
                    $ h_body = "01_hp/13_hermione_main/body_44.png"
                    her "As for my father..."
                    hide screen h_head2
                    menu:
                        m "..."
                        "{size=-3}\"Your father would be proud of you!\"{/size}":
                            show screen h_head2
                            her "I doubt it..."
                            her "Yes, I am doing this for the right reasons, but..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_61.png"
                            her "He would never see it that way..."
                            her "He must never know about this..."
                            hide screen h_head2
                        "{size=-3}\"Your father would spank you hard!\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_48.png"
                            her "He would not!"
                            $ h_body = "01_hp/13_hermione_main/body_44.png"
                            her "And I am too old for that anyways..."
                            hide screen h_head2
                            g9 "I would say that you are in the perfect age for that..."
                            show screen h_head2
                            her "Huh?"
                            $ h_body = "01_hp/13_hermione_main/body_57.png"
                            her "I do not know what you mean, [genie_name]."
                            hide screen h_head2
                        "{size=-3}\"Your father would disown you!\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_34.png"
                            her "You are probably right, [genie_name]..."
                            $ h_body = "01_hp/13_hermione_main/body_22.png"
                            her "(Oh father, I am so sorry...)"
                            $ h_body = "01_hp/13_hermione_main/body_21.png"
                            her "he must never find out..."
                            hide screen h_head2
                        "{size=-3}\"Your father love to would watch you strip!\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_33.png"
                            her "He would not! He would be ashamed of me!"
                            hide screen h_head2
                            m "Are you sure about that?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_32.png"
                            her "absolutely! My father is a man of integrity!"
                            hide screen h_head2
                            m "But he {size=+4}is{/size} a {size=+4}man{/size}, right?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "....................."
                            $ h_body = "01_hp/13_hermione_main/body_29.png"
                            her "My father must never know about this..."
                            hide screen h_head2
                    show screen blktone
                    with d3
                    ">Hermione is starting to sway her hips rather seductively while she slides her skirt down..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_31.png"
                    her "[genie_name]?"
                    hide screen h_head2
                    m "Huh?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_44.png"
                    her "Can I ask you a question?"
                    hide screen h_head2
                    m "Go ahead..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_33.png"
                    her "..............."
                    $ h_body = "01_hp/13_hermione_main/body_57.png"
                    her "Have you ever been in love...?"
                    hide screen h_head2
                    menu:
                        m "..."
                        "\"Don't be ridiculous! Love is a lie!\"":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_29.png"
                            her "I am sorry you think that way, [genie_name]!"
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "But you couldn't be more wrong!"
                            $ h_body = "01_hp/13_hermione_main/body_54.png"
                            her2 "I believe that true love is what makes the earth turn!"
                            hide screen h_head2
                            m "Actually the conservation of angular momentum is responsible for that."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_44.png"
                            her "Huh?"
                            hide screen h_head2
                            m "Never mind. Just take off your shirt already?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "............"      
                            hide screen h_head2
                        "\"Be quiet and keep on dancing!\"":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "But you said I could ask you a question..."
                            hide screen h_head2
                            m "And you did, didn't you?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_31.png"
                            her "!!!............"
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her2 "...................................."
                            hide screen h_head2
                            m "Now, hush and take your shirt off."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_69.png"
                            her "........"
                            hide screen h_head2
                        "\"Yes... a very long time ago...\"":
                            hide screen h_head2
                            m "Yes... a very long time ago..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_31.png"
                            her2 "!!!!!??.............................."
                            hide screen h_head2
                            m "Her name was Eden..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_45.png"
                            her "Was she beautiful?"
                            hide screen h_head2
                            m "She was so much more than that..."
                            m "She was smart, green and perfect..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_87.png"
                            her "She was... \"green\"...?"
                            $ h_body = "01_hp/13_hermione_main/body_47.png"
                            her2 "Are you making fun of me, [genie_name]?"
                            hide screen h_head2
                            m "Oh, you humans know nothing of true love..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_55.png"
                            her ".....................................?"
                            hide screen h_head2
                            m "Err... I mean, take off that shirt, [hermione_name]!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_69.png"
                            her "................."
                            hide screen h_head2
                        "\"I feel like I'm in love right now!\"":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_69.png"
                            her "You don't have to be vulgar, [genie_name]."
                            hide screen h_head2
                            m "Oh, but I mean it!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_66.png"
                            her "[genie_name], please!"
                            $ h_body = "01_hp/13_hermione_main/body_55.png"
                            her "I am one of your students!"
                            $ h_body = "01_hp/13_hermione_main/body_57.png"
                            her "And you are older than my father!"
                            hide screen h_head2
                            m "{size=-4}(You have no idea, girl.){/size}"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_55.png"
                            her2 "Although some scientists insist that what we consider \"love\" is actually nothing but a chemical reaction..."
                            $ h_body = "01_hp/13_hermione_main/body_16.png"
                            her2 "And when a man is experiencing sexual arousal, the same type of hormones--"
                            hide screen h_head2
                            m "[hermione_name]!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_15.png"
                            her "Yes, [genie_name]?"
                            hide screen h_head2
                            m "Did you forget where you are?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_24.png"
                            her "Oh, my apologies, [genie_name]... I get distracted sometimes."
                            hide screen h_head2
                            m "Take off your shirt already, would you?!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_29.png"
                            her "Right..."
                            hide screen h_head2
                    show screen blktone
                    with d3
                    ">Hermione undoes the last button of her shirt and takes it off somewhat gracefully..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    g9 "Yes! The tits!"
                    
                    if custom_outfit == 0:
                        $ badges = False# Hides any badges from hermione_main screen.
                    
                    show screen h_head2
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    $ h_body = "01_hp/13_hermione_main/body_90.png"
                    her "Must you be so vulgar, [genie_name]?"
                    hide screen h_head2
                    menu: 
                        "-Take your cock out, start jerking off-":
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_94.png"
                            her "[genie_name]?!"
                            hide screen h_head2
                            m "It's alright, [hermione_name]. Don't mind me..."
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_95.png"
                            her "B-but..."
                            her "Your..."
                            hide screen h_head2
                            m "Yes... Ah, yes, this is good..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_98.png"
                            her "[genie_name]!!!"
                            her "I must insist that you put away your..."
                            $ h_body = "01_hp/13_hermione_main/body_99.png"
                            her "...thing."
                            hide screen h_head2
                            menu:
                                m "..."
                                "\"I said, keep on dancing, [hermione_name]!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_99.png"
                                        her "But..."
                                        her "............................."
                                        $ h_body = "01_hp/13_hermione_main/body_101.png"
                                        her2 "Well, alright, but only if you will promise me not to....finish, [genie_name]."
                                        hide screen h_head2
                                        menu:
                                            m "..."
                                            "-Promise her to hold it-":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    show screen h_head2
                                                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                                                    her "Well, alright then..."
                                                    hide screen h_head2
                                            "-Give her no such promise-":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Not to finish\"? That would be like torture!"
                                                m "Please keep your sadistic urges to yourself, [hermione_name]."
                                                show screen h_head2
                                                $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                her "I don't have any... sadistic urges, [genie_name]!"
                                                her "I just don't want to..."
                                                hide screen h_head2
                                                g9 "Yes... Those are some nice tits you have..."
                                                show screen h_head2
                                                $ h_body = "01_hp/13_hermione_main/body_97.png"
                                                her "............"
                                                hide screen h_head2
                                                g9 "A-ah... Yes..."
                                                show screen h_head2
                                                $ h_body = "01_hp/13_hermione_main/body_97.png"
                                                her ".........."
                                                $ h_body = "01_hp/13_hermione_main/body_99.png"
                                                her "Fine! Have it your way, [genie_name]!"
                                                $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                her "{size=-5}(As usual...){/size}"
                                                hide screen h_head2
                                        show screen blktone
                                        with d3
                                        ">You keep on wanking while you watch Hermione's dance..."
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_90.png"
                                        her "Time for the finishing act I suppose..."
                                        hide screen h_head2
                                        m "Yes, [hermione_name]! Take them off!"
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_91.png"
                                        her "........"
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Hermione bends over slightly and slides her panties down..."
                                        ">You can see that she is doing her best to be graceful..."
                                        ">But she looks rather ridiculous in her attempts to act like a professional stripper..."
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        ">Nonetheless you decide to show her some appreciation..."
                                        ">By stroking your cock even faster!"
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_91.png"
                                        her ".........."
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Suddenly Hermione breaks into a whole series of rather complex pirouettes..."
                                        m "{size=-4}(This looks quite impressive actually...){/size}"
                                        ">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements..."
                                        m "{size=-4}(Did she practice this?){/size}"
                                        g9 "Oh, what do I care?"
                                        ">You stroke your diamond-hard cock furiously."
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_102.png"
                                        her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                                        hide screen h_head2
                                        ">Hermione performs another set of movements that could be considered classy..."
                                        ">if not for her naked tits bouncing all over the place..."
                                        g9 "Yes, yes, you little whore!"
                                        ">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                        ">And then Hermione slumps on her butt, completely exhausted."
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        pause
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_102.png"
                                        her "Whew... This was--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING CUNT!"
                                        hide screen hermione_main
                                        with d3
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "01_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "01_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        show screen bld1
                                        with d3
                                        $ h_body = "01_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        her "[genie_name]!!!"
                                        $ g_c_c_u_pic = "01_hp/08_animation_02/09_cum_18.png"
                                        hide screen h_head2
                                        if d_flag_07: #Promised to hold it.
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_97.png" # HERMIONE
                                            her "No, [genie_name]! You promised!"
                                            hide screen h_head2
                                            g4 "Oh, man... This was pretty intense..."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_98.png" # HERMIONE
                                            her "You went back on your word, [genie_name]!"
                                            hide screen h_head2
                                            m "Huh? What are you talking about?"
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_113.png" # HERMIONE
                                            her "How could you do this to me, [genie_name]?"
                                            hide screen h_head2
                                            m "Oh, calm down, [hermione_name]."
                                            m "You earned your points today."
                                            m "Now, just get dressed and leave before somebody discovers you like this."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_114.png" # HERMIONE
                                            her "*sob!*........................"
                                            hide screen h_head2        
                                            $ mad += 50
                                            show screen blkfade 
                                            with d3
                                            $ uni_sperm = False #Sperm layer is not displayed.
                                            $ aftersperm = True #Aftersperm layer is displayed. 
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_12.png" # HERMIONE
                                            her "...Can I just get paid now, [genie_name]... please?"
                                            hide screen h_head2   
                                            jump done_with_dancing
                                        else:
                                            $ h_body = "01_hp/13_hermione_main/body_97.png"
                                            show screen h_head2  
                                            her "it's so hot..."
                                            hide screen h_head2  
                                            $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                            m "Aha... Yeah... This feels great..."
                                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                                            show screen h_head2  
                                            her "You came all over me..."
                                            her "I am your pupil and..."
                                            $ h_body = "01_hp/13_hermione_main/body_106.png"
                                            show screen h_head2  
                                            her "You just came on me..."
                                            hide screen h_head2  
                                            g9 "I know! Pretty exciting stuff, huh?!"
                                            $ h_body = "01_hp/13_hermione_main/body_107.png"
                                            show screen h_head2  
                                            her "Nothing of that sort!"
                                            #her "You should not have done this, [genie_name]!"
                                            her2 "You should have restrained yourself like a proper headmaster would!"
                                            hide screen h_head2  
                                            m "Really? What did you expect me to do?"
                                            m "Aim at the wall or just put it back in my pants and start cumming?"
                                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                                            show screen h_head2
                                            her "........"
                                            $ h_body = "01_hp/13_hermione_main/body_101.png"
                                            show screen h_head2
                                            her "Still, you should not have..."
                                            $ h_body = "01_hp/13_hermione_main/body_102.png"
                                            show screen h_head2
                                            her "I agreed to perform a striptease for you..."
                                            her "But I didn't agree to be defiled like this."
                                            hide screen h_head2  
                                            m "I think I know where this is going..."
                                            $ h_body = "01_hp/13_hermione_main/body_100.png"
                                            show screen h_head2
                                            her "I demand to be paid extra!"
                                            hide screen h_head2  
                                            m "Of course you do..."
                                            menu:
                                                m "..."
                                                "\"You get 1 extra point.\"":
                                                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "One extra point?"
                                                    $ h_body = "01_hp/13_hermione_main/body_98.png"
                                                    her2 "One meagre extra point for letting you do this to me?"
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    her "Now, that is just insulting, [genie_name]!"
                                                    hide screen h_head2  
                                                    m "One extra point, [hermione_name]. Take it or leave it."
                                                    $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "............."
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    her "I'll take it."
                                                    hide screen h_head2  
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You get 10 extra points.\"":
                                                    $ current_payout = 45
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Ten extra points [genie_name]?"
                                                    her "But that is not even nearly enough!"
                                                    hide screen h_head2  
                                                    m "Ten extra points. Take'em or leave'em [hermione_name]."
                                                    $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "..............."
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Well, alright... Better than nothing I suppose..."
                                                    hide screen h_head2  
                                                    $ mad += 11
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You get 25 extra points.\"":
                                                    $ current_payout = 60
                                                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her2 "Yes, I believe this would be an appropriate amount."
                                                    hide screen h_head2  
                                                    m "are we good then?"
                                                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her "Yes, [genie_name]. Thank you [genie_name]."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You get 50 extra points.\"":
                                                    $ current_payout = 85
                                                    $ h_body = "01_hp/13_hermione_main/body_95.png"
                                                    show screen h_head2
                                                    her "Seriously?!"
                                                    $ h_body = "01_hp/13_hermione_main/body_94.png"
                                                    her "Oh, I don't know what to say..."
                                                    hide screen h_head2  
                                                    m "I enjoyed your performance [hermione_name]."
                                                    show screen h_head2
                                                    $ h_body = "01_hp/13_hermione_main/body_109.png"
                                                    her "Thank you [genie_name]..."
                                                    hide screen h_head2  
                                                    m "I also enjoyed plastering your agile little body with cum..."
                                                    $ h_body = "01_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "[genie_name]......"
                                                    hide screen h_head2  
                                                    m "So, just allow me to show my appreciation."
                                                    m "Fifty extra points. Well deserved, [hermione_name]."
                                                    $ h_body = "01_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "Thank very much, [genie_name]."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You're not getting shit!\"":
                                                    stop music fadeout 1.0
                                                    $ h_body = "01_hp/13_hermione_main/body_104.png"
                                                    show screen h_head2
                                                    her "What? Not even my usual pay?"
                                                    hide screen h_head2  
                                                    menu:
                                                        m "..."
                                                        "\"Oh, no, you are still getting that.\"":
                                                            $ mad += 30
                                                            $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "How generous of you, [genie_name]." 
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                            jump done_with_dancing
                                                        "\"No, not even that!\"":
                                                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                            $ h_body = "01_hp/13_hermione_main/body_104.png"
                                                            show screen h_head2
                                                            her "!!!?"
                                                            her "I danced for you, [genie_name]..."
                                                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                                                            her "I degraded myself for your amusement..."
                                                            $ h_body = "01_hp/13_hermione_main/body_107.png"
                                                            her "I let you cum on me..."
                                                            $ h_body = "01_hp/13_hermione_main/body_110.png"
                                                            with hpunch
                                                            her "And I get NOTHING?!"
                                                            hide screen h_head2  
                                                            m "You are dismissed, [hermione_name]!"
                                                            $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "Oh, this is a new low even for you, [genie_name]!"
                                                            hide screen h_head2  
                                                            m "I said you are dismissed."
                                                            $ h_body = "01_hp/13_hermione_main/body_110.png"
                                                            show screen h_head2
                                                            her "*GROAN!*"
                                                            $ mad += 90
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
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
                                                            call music_block
                                                            jump could_not_flirt #Leaves without getting any points.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        $ h_body = "01_hp/13_hermione_main/body_103.png"
                                        show screen h_head2
                                        stop music fadeout 1.0
                                        her "No, [genie_name]!"
                                        hide screen h_head2  
                                        m "Huh?"
                                        show screen blkfade
                                        with d7
                                        ">Hermione jumps off your desk and starts to put her clothes back on while glaring at you..."
                                        m "Oh, come on! Don't leave me like that!"
                                        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                                        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                                        $ h_body = "01_hp/13_hermione_main/body_101.png"
                                        show screen h_head2
                                        her "The dance is over [genie_name]!"
                                        hide screen h_head2
                                        pause 1
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_79.png"
                                        her "I would like to get paid now!"
                                        hide screen h_head2
                                        m "Stubborn [hermione_name]..."
                                        ">You reluctantly put your cock away..."
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_79.png"
                                        her "I would like to get paid now."
                                        hide screen h_head2
                                        jump done_with_dancing
                                "\"Fine. There is no need for drama!\"": 
                                    $ h_body = "01_hp/13_hermione_main/body_103.png"
                                    show screen h_head2
                                    her2 "......................"
                                    hide screen h_head2
                                    pause.1
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    hide screen blkfade
                                    with fade
                                    pause
                                    show screen bld1
                                    with d3
                                    pass

                        "-Show some manners, just watch-":
                            pass
                    # JUST WATCHING.
                    show screen blktone
                    with d3
                    ">You watch Hermione Dance..."
                    $ h_body = "01_hp/13_hermione_main/body_97.png"
                    show screen h_head2
                    her "(Time for the finishing act I suppose...)"
                    hide screen h_head2
                    m "Yes, [hermione_name]! Take them off!"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_90.png"
                    her "........"
                    hide screen h_head2
                    show screen blktone8
                    with d3
                    ">Hermione bends over slightly and slides her panties down..."
                    ">You can see that she is doing her best to be graceful..."
                    ">But she looks rather ridiculous in her attempts to act like a professional stripper..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_109.png"
                    her ".........."
                    hide screen h_head2
                    ">Suddenly Hermione breaks into a whole series of rather complex pirouettes..."
                    hide screen h_head2
                    m "{size=-4}(This looks quite impressive actually...){/size}"
                    ">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements..."
                    m "{size=-4}(Did she practice this?){/size}"
                    g9 "Oh, why would I care?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                    hide screen h_head2
                    ">Hermione performs another set of movements that could be considered classy if not for her naked tits bouncing all over the place..."
                    g9 "Yes, yes, you little harlot!"
                    
                    show screen blkfade
                    with d3
                    $ hermione_chibi_xpos = -210 #400 = Near the desk.
                    $ hermione_chibi_ypos = 10
                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                    ">A few more movements, a couple of gestures and a little curtsy bow to the imaginary audience and Hermione slumps on her butt completely exhausted."
                    show screen h_c_u
                    hide screen blktone
                    with d3
                    hide screen blktone8
                    with d3
                    hide screen blkfade
                    with d3
                    hide screen bld1 
                    with d3
                    pause
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_108.png"
                    show screen bld1
                    with d3
                    her "Whew... This was rather exciting..."
                    hide screen h_head2 
                    menu:
                        m "..."
                        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
                            m "Good job [hermione_name]!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_109.png"
                            her "Really?"
                            hide screen h_head2
                            m "Yes! You have a lot of talent for this!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_108.png"
                            her "Thank you [genie_name]."
                            hide screen h_head2
                        "{size=-3}\"Hm... This was quite awful...\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                            her "Oh... I'm sorry..."
                            hide screen h_head2
                            m "That's OK... You just need to practice more..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_107.png"
                            her "Em... I will keep that in mind, [genie_name]..."
                            hide screen h_head2
                        "{size=-3}\".................................................\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_108.png"
                            her "......................."
                            hide screen h_head2

                    
                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                    hide screen bld1
                    show screen ctc
                    with d3
                    pause
                    show screen blkfade
                    with d7
                    pause.5

                            
        else: #Stripping only for Genie.
            jump no_snape_watching 

        
        
        
    label done_with_dancing:
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
    
    $ badges = True # Shows any badges from hermione_main screen.
    
    m "Yes, [hermione_name]. [current_payout] to the \"Gryffindor\" house." 
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    
    her "Thank you, [genie_name]..."

    if whoring <= 11:
        $ whoring +=1

    $ request_11_points += 1

    
    

    $ sperm_on_tits = False
    $ uni_sperm = False

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)

    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ panties = True
    
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


    

        

    
#############################################################################################################################
### LEVEL 05 ################################################################################################################   
###################REQUEST_16 (Level 05) (HANDJOB) (Day/Night) #####################################################
label new_request_16: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main 
    with d3
    if request_16_points == 0:
        m "{size=-4}(Should I ask her for a handjob?){/size}"
    else:
        m "{size=-4}(Should I ask the [hermione_name] to give me another handjob?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
    $ current_payout = 45 #Used when haggling about price of th favor.  
    if request_16_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, [genie_name]?"
        m "Do you know what a \"handjob\" is?"
        if whoring <=11:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "Why?"
        m "I feel like getting one..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "[genie_name]!"
        m "Just another favour. No big deal, right?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "......"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "{size=-7}I want 100 house points for this...{/size}"
        m "Huh? What was that?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "I want 100 house points for this!!!"
        m "100 house points, huh?"
        m "And you will stroke my cock and everything?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                    
        her "{size=-7}Yes...{/size}"
        m "Sorry, I couldn't hear you..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                 
        her "Yes, I said yes! I will stroke your cock, [genie_name]!"
        label back_to_handjob_choices:
        menu:
            m "..."
            "\"You will get 15 house points.\"":
                $ mad +=7
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "For 15 house points I suppose I could let you molest me a little, but that is all you'll be getting, [genie_name]."
                her "I will not stoop as low as to sell handjobs for 15 house points."
                her "That is just insulting, [genie_name]."
                jump back_to_handjob_choices
            "\"you will get 45 house points.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "....."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "45 house points...?"
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "Yes, it is a yes, [genie_name]."
                m "Great!"
            "\"you will get 100 house points.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "100 house points?!"
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "Is that a \"yes\" then?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_75.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "Of course!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_80.png" #Sprite of Hermione's upper body.                    #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "If it will bring \"Gryffindor\" 100 house points, I don't mind touching your... thing a little."
        # GENIE STANDS WITH HIS COCK OUT
       
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
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
        pause
        show screen bld1
        with d3
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
        her "..........."
        hide screen h_head2
        m "Whenever you're ready, [hermione_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
        her "Right..."
        hide screen h_head2
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3
        label event_01_round_02:
        ">Hermione puts her slender hands on your cock..."
        m "Good. Now stroke it."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
        her "Right..."
        hide screen h_head2 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d3
        show screen ctc
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen ctc
        show screen bld1
        with d3
        g9 "Nice..."
        if request_16_points == 0:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
            her "!!!"
            her "Are you about to finish, [genie_name]?!"
            hide screen h_head2 
            m "About to finish?"
            m "Don't be ridiculous [hermione_name], we are just getting started."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Oh..."
            her "......"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "You will give me a warning though, won't you, [genie_name]?"
            hide screen h_head2 
        else:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
            her "[genie_name]...?"
            hide screen h_head2    
            m "What is it?"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Will you warn me before... uhm... you now..."
            hide screen h_head2    
        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Of course I'll let you know when it's time.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Thank you, [genie_name]."
                hide screen h_head2 
            "\"I myself don't always know when...\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Really? But I thought..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "Well, never mind then..."
                hide screen h_head2 
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
        her "........"
        hide screen h_head2 
        m "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
        her "............."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
        her "Err... [genie_name]?"
        hide screen h_head2 
        m "Yes, what is it?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
        her "How long do you think this will take?"
        hide screen h_head2 
        m "Why?"
        if daytime:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Well, it's just that my classes are about to start..."
        else: 
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
            her2 "Well, it's just that I have this paper that I need to finish..."
            her2 "It's due tomorrow, and it's getting pretty late..."
        hide screen h_head2 
        m "Do you need the points or not?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
        her "I do, [genie_name]! I'm sorry..."
        her "I will just keep on stroking it then..."
        hide screen h_head2 
        m "Well, there is something you could do to speed up the process..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
        her "Really? What is it [genie_name]?"
        hide screen h_head2 
        menu:
            m "..."
            "\"Tell me how much of a whore you are!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_47.png" # HERMIONE
                her "What?"
                her "But I'm not..."
                hide screen h_head2 
                m "No need to be honest, [hermione_name]."
                m "Just make things up."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Really?"
                hide screen h_head2 
                m "Sure. Just have fun with it."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Well, in that case..."
                her "I am a... whore."
                hide screen h_head2 
                m "Heh... good. Go on."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "I am a big whore..."
                hide screen h_head2 
                m "Yes, you are."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_79.png" # HERMIONE
                her "I am the biggest whore in England!"
                her2 "I try to act innocent, but in truth all I think about is cock!"
                hide screen h_head2 
                m "Yes, you little slut!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                her "Yes! I am a slut!"
                her "I crave cock all the time."
                hide screen h_head2 
                m "Very nice!"
                m "But, like I said, you don't have to be honest."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "What?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                her "[genie_name], those things I say are not true!"
                hide screen h_head2 
                g9 "Heh... I know. I'm just messing with you."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" # HERMIONE
                her "[genie_name]!"
                hide screen h_head2 
                m "You are doing a great job, though. Keep at it!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "....."
                her "I love cock..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_88.png" # HERMIONE
                her "And I love... spunk..."
                her "And semen... and sperm..."
                her "I love to drink sperm..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_65.png" # HERMIONE
                her "I want you to feed me your sperm, [genie_name]!"
                hide screen h_head2 
                g4 "!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_64.png" # HERMIONE
                her2 "Or better yet, pump me full of it, [genie_name]!"
                hide screen ctc
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"
            
            "\"Stick your tongue out and look at me!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                her "What?"
                hide screen h_head2 
                m "Just do it, slut."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_38.png" # HERMIONE
                her "Like this?"
                hide screen h_head2 
                m "Yes, good. Keep looking into my eyes and stroke my cock."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her "....................."
                hide screen h_head2 
                m "Yes... Good..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her "..........."
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her2 "I can't keep my mouth open for so long, [genie_name]. I will start to drool..."
                hide screen h_head2 
                m "But I want you to drool..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "What? But I will look silly!"
                hide screen h_head2 
                m "That's the point, [hermione_name]!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                her "......."
                hide screen h_head2 
                m "Don't you want to be done with this as soon as possible?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "............"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her "A-ha....."
                hide screen h_head2 
                m "Good, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her ".............."
                hide screen h_head2 
                m "Yes, keep on stroking my cock."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her ".................."
                hide screen h_head2
                g4 "Oh... I just want to slide my cock into that wet hole of a mouth of yours!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_40.png" # HERMIONE
                her "................."
                hide screen h_head2 
                m "No, keep on looking at me!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her "....................."
                hide screen h_head2 
                m "Yes, you little slut!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_116.png" # HERMIONE
                her "......................"
                hide screen h_head2 
                m "I want to cum in that mouth, yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_116.png" # HERMIONE
                her "................"
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"
            "\"Give my cock a kiss!\"":
                show screen h_head2                                                               # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_47.png" # HERMIONE
                her "Excuse me?"
                hide screen h_head2 
                m "You know, just a little kiss, right on the tip."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_47.png" # HERMIONE
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "...with my lips?"
                hide screen h_head2 
                m "Sure... That will speed things up, I'm telling you."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "*sigh!*.............."
                her "Well, I might as well, I suppose..."
                hide screen h_head2 
                ">Hermione gives the tip of your engorged cock a tender kiss."
                
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Like this?"
                hide screen h_head2 
                m "Wasn't that bad, was it?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                her "No, I suppose not..."
                hide screen h_head2 
                m "Can you do it again, then?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "I could..."
                hide screen h_head2 
                m "Do it!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Well, alright..."
                hide screen h_head2
                ">Hermione gives your cock another kiss..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                ">This time she lingers a moment longer..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                hide screen h_head2 
                m "Good... Now do it again and just stay there for a while."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "You mean with my lips touching your... cock, [genie_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                her "No, I will look stupid..."
                hide screen h_head2 
                m "Don't be silly, [hermione_name]. Nobody is watching."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "You are, [genie_name]."
                hide screen h_head2 
                m "But that's the whole point!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_79.png" # HERMIONE
                her "......"
                hide screen h_head2 
                m "It will make me cum in no time!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                her "..............."
                hide screen h_head2 
                m "And then you can just get out and and take care of your business today."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" # HERMIONE
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Well, alright then...."
                hide screen h_head2
                ">Hermione reaches down with her lips again..."
                ">She touches the tip of your cock with her lips and keeps them there..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                hide screen h_head2 
                show screen blktone
                with d3
                m "Very good..."
                m "Now touch it with your tongue."
                her "??!"
                hide screen h_head2 
                m "That's the last thing I will be asking of you today."
                her "............"
                ">You feel the tip of Hermione's tongue warily rubbing against the head of your cock..."
                hide screen h_head2 
                m "Yes, like this..."
                ">Hermione wiggles her tongue a little...."
                hide screen h_head2 
                m "Yes... Good..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "So, did it work? Are you ready to... finish, [genie_name]?"
                hide screen h_head2 
                g4 "{size=-4}(Surprisingly, yes! I'm about to cum! Should I warn her?){/size}"
                hide screen blktone
        menu:
            m "..."
            "-Give her a warning-":
                g4 "Here it comes, [hermione_name]! You better be ready!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "What? So soon?!"
                hide screen h_head2 
                g4 "{size=+5}Yeah, you did a great job!!!{/size}"
                g4 "{size=+5}You little whore!!!{/size}"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade 
                with d5
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "No, [genie_name], wait, I--"
                hide screen h_head2 
                g4 "{size=+5}Too late for that, slut!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "*whimper*"
                hide screen h_head2       
                ">Hermione suddenly slides your already dripping cock under her shirt..."
                g4 "?!!"
                ">The sensation of her warm skin against your cock overwhelms you and you begin to ejaculate like a mad-man."
                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                
                
                
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                stop music fadeout 1.0
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2                
                m "..........................."
                show screen h_head2                   
                $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2    
                m "....................?"
                show screen h_head2                   
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "......................."
                hide screen h_head2    
                m "...What the fuck just happened?"
                show screen bld1
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "I don't know... I suppose I just panicked..."
                hide screen h_head2    
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                    her2 "My classes are about to start and I didn't want you to ruin my uniform, [genie_name]..."
                    hide screen h_head2 
                    m "So you'll go to classes like this now?"
                    m "With your clothes all sperm-soaked from the inside?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                    her2 "What choice do I have?"
                    her2 "I can't just skip a class..."
                    hide screen h_head2
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                    her2 "At this hour The \"Gryffindor\" common room will be full of people..."
                    her2 "I didn't want to have to return there all covered in your... spunk, [genie_name]."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                    her2 "Oh, it's getting pretty late..."
                    hide screen h_head2 
                    m "So you will go like this, instead?"
                    m "With your clothes all sperm-soaked from the inside?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                    her "What choice do I have?"
                    hide screen h_head2     
                    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                ">Hermione releases your still pulsating cock."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Ew... Your sperm, [genie_name]..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "It's everywhere under my uniform..."
                hide screen h_head2          
                m "Just put it in your mouth next time."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_79.png" # HERMIONE
                her "I... don't think so, [genie_name]."
                her "I really need to go. Can I just get paid now?"
                hide screen h_head2   
                
                
                
                
                
                
#                g4 "You whore! You little nasty wore!"
#                g4 "There! Allover your fucking belly and tits!"
#                her "Ah! It's so hot!"
#                hide screen h_head2 
#                g4 "Oh, yes, this is so good!"
#                her "Ah..."
#                hide screen h_head2 
#                m "..............."
#                her "............"
#                hide screen h_head2 
#                m "I think I'm done..."
#                her "Oh..."
#                ">Hermione releases your still pulsating cock."
#                her "Ew... Your sperm, [genie_name]..."
#                her "It's everywhere under my uniform..."
#                hide screen h_head2 
#                m "What possessed you to put my cock there, [hermione_name]?"
                

            "-Just start cumming-":
                hide screen ctc
                with hpunch
                g4 "ARGH!"
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "WHAT?!"
                hide screen h_head2               
                g4 "Take this!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                
                
                  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2          
                m "Yes... I Feel so much better now..."
                pause
                $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
                
                $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                $ h_xpos=130 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ h_body = "01_hp/13_hermione_main/body_19.png" #Flashing panties
                show screen hermione_main
                with d5
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with fade                                                                                                                                                                                                                      #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                 
                her "[genie_name]! What have you done?!"
                m "What?"
                if d_flag_01: #If TRUE Genie promised to warn her.
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ mad += 11
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    with d3                 
                    her "You promised to give me a warning, [genie_name]!"
                    m "Oh, that's right... My bad."
                    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                    with d3                                                                                                                                                                                                                        #HERMIONE
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                    show screen hermione_main                                                                                                                                                                                 #HERMIONE
                    her "My uniform is ruined..."
                    her "...I would like to get paid now."
                    hide screen hermione_main     
                    with d3
                    $ uni_sperm = False
                else:
                    if daytime:
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "My uniform is ruined now!"
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "My classes are about to start and I can't go looking like this!"
                        m "Of course you can, just wipe it off or something..."
                        m "Nobody will even notice."
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "...I would like to get paid now."
                        hide screen hermione_main     
                        with d3
                        $ uni_sperm = False
                    else:
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "My uniform is ruined!"
                        her "Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                        m "Why not? You look hot, [hermione_name]!"
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "[genie_name]!!!"
                        m "Alright, alright. Just wipe it off or something."
                        m "Nobody will even notice."
                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                        with d3                                                                                                                                                                                                                        #HERMIONE
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                        her "...I would like to get paid now."
                        hide screen hermione_main     
                        with d3
                        $ uni_sperm = False
        #her "Can I just get paid now?"

    elif request_16_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, [genie_name]?"
        m "Do you know what a \"handjob\" is?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "You have asked me that already, [genie_name]."
        m "Ah, that's right."
        m "Well, I want you to play with my cock again."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], you are being vulgar again..."
        m "Fine, fine."
        m "[hermione_name], I would like to buy another favour from you today."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Of course, [genie_name]."
        g9 "The favour being you playing with my cock!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".............."
        m "Oh, come on. For the honour of the \"Gryffindors\"?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "............."
        g9 "Play with my cock for the honour of the \"Gryffindors\", [hermione_name]!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                               
        her "Stop saying that, [genie_name]..."
        #Genie with his cock out
        m "Come on [hermione_name], it's not like I'm asking you to do this for free."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                 #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                               
        her "......."
        stop music fadeout 4.0
        

        hide screen hermione_main            
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        
                                                                                                                                                                               #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone

        jump event_01_round_02


    elif request_16_points >= 2: # THIRD EVENT <========================================================================================================= EVENT 03

        $ new_request_16_03 = True #  Hearts

        $ new_request_16_heart = 3
        
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                    #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                    
        her "[genie_name]?"
        m "You don't mind giving me another handjob, do you?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        if whoring <= 16:
            $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                    
            her "As long as I am getting paid..."
            m "Well, come here then. Time to earn those points."
        else:
            $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                    #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                    
            her "Of course not [genie_name]..."
            m "Well, come here then."
        
        
        hide screen hermione_main            
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone
        
        
        
        ">Hermione puts her slender hands on your cock..."
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=290 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_68.png" # HERMIONE
        stop music fadeout 3.0
        her "Do you like it when I do it like this, [genie_name]?"
        hide screen h_head2         
        g9 "Actually, yes! Very nice!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        hide screen h_head2 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3

        m "Yes, yes, like that..."
        m "Hm... You are getting pretty good at this."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
        her "Thank you, [genie_name]."
        her2 "I figured the better I do this, the sooner it'll be over."
        hide screen h_head2      
        m "Hm..."
        menu:
            m "..."
            "\"What do you think of my cock?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Huh?"
                her2 "Oh, that's right..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her2 "I need to compliment your penis! I completely forgot about that!"
                hide screen h_head2         
                m "Well, you don't have to--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her "[genie_name], let me be honest with you..."
                hide screen h_head2         
                m "Yes?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_111.png" # HERMIONE
                her "You have the biggest penis I have ever seen!"
                hide screen h_head2         
                m "Well I suppo--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                her "Not done yet!"
                hide screen h_head2         
                m "Apologies."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Your penis is so big it almost scares me!"
                hide screen h_head2      
                g9 "You little mynx. You know exactly what to say..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "And yet I lust for it..."
                her2 "Any woman would be happy to have your huge penis inside of her!"
                hide screen h_head2         
                m "...you're good!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                her "There is more!"
                hide screen h_head2         
                m "By all means..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                her2 "I think your magnificent cock is a blessing to this world!"
                hide screen h_head2         
                m "Well, I wouldn't go that far--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                her2 "Listen to me, [genie_name]!"
                her2 "I think a statue dedicated to your magnificent penis shall be erected in every city!"
                her2 "So that people of the world could worship your phallus freely!"
                hide screen h_head2         
                m "OK, I think I've heard enough."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Too much?"
                hide screen h_head2         
                m "Yeah, just a bit."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Sorry..."
                hide screen h_head2         
                m "No biggie. Just keep on stroking it."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "................."
                hide screen h_head2  
                show screen blktone
                with d3
                ">Hermione keeps on stroking your cock."
                ">She is doing a great job of it too."  
                hide screen blktone
                with d3
                m "Yes, yes... Like that."
                
            "\"Call yourself a whore, [hermione_name]!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Excuse me?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_17.png" # HERMIONE
                her2 "Oh, that's right! I'm supposed to degrade myself, right?"
                hide screen h_head2  
                m "Well, you don't have to, but..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "That's alright, I don't mind."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                her "Alright then! I am a whore!"
                hide screen h_head2  
                m "Good. Glad we established that."
                m "Now I want you to say..."
                menu:
                    m "..."
                    "\"I am a worthless slut!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Of course."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "I am a worthless slut."
                        her "A dirty little slut, that's what I am."
                        hide screen h_head2  
                        m "Yes! Good!"
                    "\"I live to suck cock!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Em..."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                        her2 "I live to suck penis, er... I mean cock..."
                        hide screen h_head2  
                        m "Really? Well why don't you suck on this one then?"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_111.png" # HERMIONE
                        her2 "[genie_name], I am just repeating after you..."
                        hide screen h_head2  
                        m "Really? Could've fooled me...."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                        her2 "...................."
                        hide screen h_head2
                        m ".................."
                    "\"I love to swallow cum!\"":
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "I love to... ehm... swallow cum."
                        hide screen h_head2  
                        m "You hesitated there for a moment."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "Yes, I know...."
                        her "Let me try again..."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                        her "I love to swallow cum!"
                        her "It is truly the best to swallow cum!"
                        her "I love it!"
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "..................................."
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                        her "How was that, [genie_name]?"
                        hide screen h_head2  
                        m "Perfect." 
            "\"This is really good. Did you practice?\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Hm?"
                her "Sort of... Well not really..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "I had a talk with the girls, and..."
                hide screen h_head2    
                m "About handjobs?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Among other things..."
                hide screen h_head2    
                m "So those girls of yours, they know a lot about such things?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "Actually, yes. I was surprised myself."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_68.png" # HERMIONE
                her2 "All sorts of weird sexual things seem to be happening lately in our school..."
                her "Can't say I approve of that..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her "But they did teach me quite a few... tricks."
                hide screen h_head2    
                m "Really? Like what?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her "Well, let's see..."
                her "If I put one of my hands here..."
                her "And another one here..."
                hide screen h_head2    
                m "Oh, I see... Yes, this feels quite good."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Does it?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_68.png" # HERMIONE
                her "So Ginny was right about this one..."
                hide screen h_head2
                g4 "What did you just say?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her "Ginny Weasley, she taught me this one."
                hide screen h_head2    
                m "Oh, right..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "She said any boy would fall in love with me if I did this to him..."
                her2 "There is also this thing when I form a ring with my fingers..."
                her2 "And then I put one finger here..."
                hide screen h_head2    
                m "Hm... I don't feel anything..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Really?"
                her "Hm..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her "Oh! That's right!"
                her "The finger goes here! Silly me!"
                hide screen h_head2    
                with hpunch
                with kissiris
                g4 "Oh!!! By the great desert sands, yes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Really? That good?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "What if I keep doing this but stick my finger here and press a little..."
                hide screen h_head2    
                g4 "[hermione_name], you are killing me!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_80.png" # HERMIONE
                her "Really? Really?!"
                her "This is actually quite fun!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Err... I mean..."
                her "I am only doing this to help my house of course..."
                hide screen h_head2    
                m "Yes, yes... The \"Gryffindor\" honour and all that."
                m "You just keep massaging that spot..."
                m "Oh, yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her "..............."
                hide screen h_head2
        m "Yes... Keep stroking it."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
        her ".............."
        hide screen h_head2
        m "Now I want you to say..."
        menu:
            m "..."
            "{size=-4}\"I fantasize about being raped by my father.\"{/size}":
                $ mad += 11
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_77.png" # HERMIONE
                her "I do not!"
                hide screen h_head2
                m "I know. Just say it."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_76.png" # HERMIONE
                her "My father? That's disgusting, [genie_name]!"
                hide screen h_head2
                m "Humour me."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_79.png" # HERMIONE
                her "..........."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "Well..."
                her "Sometimes I fantasize about being raped..."
                her "......."
                hide screen h_head2
                m "I see. And in those fantasies of yours..."
                m "Who is doing the raping?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "My father...?"
                hide screen h_head2
                m "Do you enjoy it?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "No. I cry and beg for him to stop!"
                hide screen h_head2
                m "Heh... Nice."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "......."
                hide screen h_head2
                m "Well, this wasn't that hard, was--"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_67.png" # HERMIONE
                her "I scream for my Mommy but she is still at work..."
                hide screen h_head2
                m "Huh?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her "My daddy takes me to my room..."
                her "He throws me on my bed!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "I cry \"No, daddy, please, I'm still a virgin!\""
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                $ g_c_u_pic= "01_hp/08_animation_02/12_handjob_01.png"
                her "But He doesn't listen! He rips my panties off!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_22.png" # HERMIONE
                her "I beg him to stop! I scream and I scream!"
                hide screen h_head2
                m "Uhm, [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
                her "Yes?"
                hide screen h_head2
                m "You are not stroking my cock anymore..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" # HERMIONE
                her "Oh, I am sorry, [genie_name]."
                her "I got lost in thought..."
                $ g_c_u_pic = "handjob_ani"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "But everything I just said is not true of course!"
                her "I never have fantasies like that!"
                hide screen h_head2
                m "Right."
            "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
                her "What?!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_17.png" # HERMIONE
                her "That's disgusting."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_16.png" # HERMIONE
                her "Dogs carry {size=+5}STD{/size}s, [genie_name]."
                hide screen h_head2
                m "Actually, human and canine {size=+5}STD{/size}s are species specific..."
                m "Means that they can only be spread to the same species."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_08.png" # HERMIONE
                her "............"
                hide screen h_head2
                m "Also I hear that many women do enjoy getting \"knotted\" quite a bit."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" # HERMIONE
                her "What does getting \"knotted\" mean?"
                hide screen h_head2
                m "Ehm... Well..."
                m "Ah, it doesn't matter."
                m "Just say the thing!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_03.png" # HERMIONE
                her "Fine!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_08.png" # HERMIONE
                her "Sometimes I get lonely and let my dog mount me."
                hide screen h_head2
                m "That sounded so fake..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" # HERMIONE
                her "Because we don't even own a dog!"
                hide screen h_head2
                m "Fine, whatever, let's just move on then..."
            "{size=-4}\"-Manual user input-\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.

                $ jasname = renpy.input("(Use keyboard to enter the phrase.)")

                $ jasname = jasname.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if jasname == "":
                    $ jasname="I'm a whore."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                    her2 "Hm...?"
                    her2 "Should I just say \"I'm a whore\" as usual?"
                    hide screen h_head2
                if one_out_of_three == 1:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "I don't want to say that..."
                    hide screen h_head2
                    m "Oh, just do it, [hermione_name]."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "..........."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "He-he..."
                    hide screen h_head2
                elif one_out_of_three == 2:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "Huh?"
                    her2 "What does That have to do with anything?"
                    hide screen h_head2
                    m "Just say it."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "......"
                    hide screen h_head2
                    m "Come on, humour me."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "He-he..."
                    hide screen h_head2
                elif one_out_of_three == 3:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
                    her "..........."
                    her2 "Do I really have to?"
                    hide screen h_head2
                    m "Just say it."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_30.png" # HERMIONE
                    her2 "[jasname]"
                    hide screen h_head2
                    g9 "He-he..."
        
        #CUMMING
        m "Hm..."
        m "I love that thing you do with the palm of your hand!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
        her2 "You noticed...?"
        her2 "Shall I do it some more then?"
        hide screen h_head2 
        show screen blkfade
        with d3
        ">Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently..."
        m "Oh yes!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(I think this is it! Should I give her a waring?){/size}"
        menu:
            m "..."
            "\"(Yes, I must warn her).\"":
                g4 "I think I'm about to--"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
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
              
                
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                
                
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                

                
                
                g4 "Argh! You whore!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 "Yes, [genie_name]! Just let it out!"
                hide screen h_head2       
                g4 "Argh! Fucking slut!"
                #Cuming.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_64.png" # HERMIONE
                her2 "Ah!! It's so hot!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "And it's getting everywhere! So much of it!"
                her2 "...[genie_name]."
                hide screen h_head2       
                g4 "Argh!!!"
                m "............"
                m "I think I am done..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "Ah, alright..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
                her2 ".............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her2 "You came so much this time, [genie_name]..."
                hide screen h_head2    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d5
                ">Hermione releases your still pulsating cock."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                hide screen blkfade
                with d5
                
               
                
                
                
                
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                    her2 "Well, I think I'd better go now... my Classes are about to start."
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                    her2 "Well, I think I'd better go now...  It's getting late."
                hide screen h_head2       
                m "Will you be alright in those clothes?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "What?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_68.png" # HERMIONE
                her "Oh. Yes, I will be fine..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "It may soak through a little here and there, but I doubt that anyone will notice."
                hide screen h_head2    
                m "Hm... You could just put it in your mouth next time, and avoid the trouble..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "And swallow your hot spunk like that, [genie_name]?"
                hide screen h_head2    
                m "Would keep your clothes clean."
                show screen h_head2                                                             # HERMIONE
                if whoring <= 15:
                    $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                    her "With all due respect [genie_name]..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                    her2 "Not for the meagre 45 points..."
                    her2 "Speaking of which. Can I get may payment now please?"
                    hide screen h_head2    
                else:
                    $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                    her "Maybe next time..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                    her2 "Can I get may payment now please?"
                    hide screen h_head2    
                

            "\"(Nah... no need).\"":
                g4 "Here! Take this, whore!"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                with hpunch
                g4 "ARGH!"
                show screen blkfade
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "WHAT?!"
                hide screen h_head2               
                g4 "Take this!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                
                
                  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!!!!!!!!!!"
                hide screen h_head2 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_119.png" # HERMIONE
                her2 "......................."
                hide screen h_head2          
                m "Yes... I Feel so much better now..."
                pause
                $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
                
                $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                $ h_xpos=130 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ h_body = "01_hp/13_hermione_main/body_19.png" #Flashing panties
                show screen hermione_main
                with d5
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with fade                                                                                                                                                                                                                      #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE          
                her "[genie_name]! What have you done?"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "What?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                  #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her "You came all over me [genie_name]..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                     #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her "What a mess..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                         #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her2 "[genie_name], you should have warned me."
                m "It's your fault, [hermione_name]!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                     #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her2 "My fault?"
                m "Yes! You got me going too well..."
                m "I forgot about everything else..."     
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE     
                her2 "Oh..."
                her2 "Well, what's done is done..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                            #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her "I will just wipe it off and hope that nobody will notice..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                   #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE      
                her2 "Can I get my payment now?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with fade   
    
    label done_with_handjob:
                
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
    
    m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"." 
    $ gryffindor +=current_payout
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 14:
        $ whoring +=1

    
    
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_16_01 = True #  Hearts
        $ new_request_16_heart = 1
    if whoring >= 15 and whoring <= 17:
        $ level = "06"
        $ new_request_16_02 = True #  Hearts
        $ new_request_16_heart = 2
    

    $ request_16_points += 1

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
   

        
        
### KISS SUCK! ###

label kiss_suck: #Jumps here after event #03 and if WHORING >= LEVEL 07
    ">Hermione swiftly puts the tip of your cock on her lips, as if to give it a kiss..."
    ">The simple gesture makes your dick practically explode with pleasure and waves of cum."
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    g4 "{size=+5}ARGH! YES!!!{/size}"
    $ genie_chibi_xpos = 60 #-185 behind the desk.
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "kiss_cum_ani"
    
    hide screen blkfade
    with d3
    show screen ctc
    hide screen bld1
    with d3
    pause
    
    
    
    show screen bld1
    with d3
                        
   
    her2 "*Gulp!-Gulp!-Gulp!*"
    hide screen h_head2          
    g4 "Argh! You little whore!"
    g4 "Yes, you slut! Dink my cum! Drink all of it!"
    her2 "*Gulp!-Gulp!-Gulp!*"
    g4 "Argh... Yes!"
    ">You notice that Hermione is barely able to keep up with the amount of hot cum your cock is pumping into her mouth."
    her2 "*Gulp!-Gulp!-Gulp!*"
    g4 "Ah..."
    g4 "This feels great..."
    her2 "*Gulp!* *Gulp!* *Gulp!*"
    m "I think that's it, [hermione_name]..."
    m "You can let go now..."
    pause
    show screen blkfade
    with d5
    show screen hermione_01 
    hide screen chair_02
    hide screen desk_02
    hide screen g_c_u
    show screen genie
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                                                                                                                                                                                         #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_125.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3       
    show screen ctc
    pause
    her2 "........................................."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_126.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "GULP!!!"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_39.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "Gu-ah-a..."
    hide screen blkfade
    with d3
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "I swallowed it all, [genie_name]!"
    m "Good girl..."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her "At one point I thought I was going to choke..."
    her2 "There was so much of it..."
    hide screen h_head2
    m "Well, the deed is done, and your uniform is perfectly clean."
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                   #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    her2 "Yes! I know! It's So much easier this way!"
    if daytime:
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                   #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main       
        with d3                                                                                                                                                                                                                                 #HERMIONE
        her "I can just go to classes now as if nothing ever happened."
    else:
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                   #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                  
        with d3 #HERMIONE
        her "I can just go and spend some time with the guys in the common room now and nobody will know..."
    hide screen h_head2
    m "Yes... With your belly full of semen..."
    hide screen hermione_main                                                                                                                                                                                     #HERMIONE
    with d3                                                                                                                                                                                                                           #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                           #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                    #HERMIONE
    show screen hermione_main                                                                                                                                                                                      #HERMIONE
    with d3                                                                                                                                                                                                                             #HERMIONE
    her2 "[genie_name]!"
    her2 "...Can I just get paid now, please, [genie_name]?"
    hide screen h_head2
    jump done_with_handjob #^^^ (<-That's to a smiley. That's a arrow up).
    
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
###################REQUEST_17 (Level 05) (Stick a finger up her butthole.) (Day/Night)
label new_request_17: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
        
    m "Come here and let me stick a finger up your butt."
    if request_17_points == 0: #One star.
        her "Oh... "
        ">Hermione agrees reluctantly."
    elif request_17_points == 1: #Two stars.
        her "...yes, [genie_name]."
        ">Hermione agrees."
    elif request_17_points == 2: #Three stars.
        ">Hermione agrees nonchalantly."
    elif request_17_points >= 3: #Master.
        her "Here you go, [genie_name]."
        ">Hermione agrees eagerly."
        
    "You dismiss Hermione."
        
    if whoring <= 14:
        $ whoring +=1

    if request_17_points <= 2:
        $ gryffindor +=45
        "gryffindor got +45 points."
    else:
        $ gryffindor +=11
        "gryffindor got +11 points."
       
    $ request_17_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label new_request_18: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
        
    m "Come here and touch my cock a little."
    if request_18_points == 0: #One star.
        her "Oh... "
        ">Hermione agrees reluctantly."
    elif request_18_points == 1: #Two stars.
        her "...yes, [genie_name]."
        ">Hermione agrees."
    elif request_18_points == 2: #Three stars.
        ">Hermione agrees nonchalantly."
    elif request_18_points >= 3: #Master.
        her "Here you go, [genie_name]."
        ">Hermione agrees eagerly."
        
    "You dismiss Hermione."
        
    if whoring <= 14:
        $ whoring +=1

    if request_18_points <= 2:
        $ gryffindor +=45
        "gryffindor got +45 points."
    else:
        $ gryffindor +=11
        "gryffindor got +11 points."
       
    $ request_18_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
    
###################REQUEST_19 (Level 05) (Rub her dick against her cheeks.) (Day/Night)
label new_request_19: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    
    m "Come here and let me rub my cock against your cheeks."
    if request_19_points == 0: #One star.
        her "Oh... "
        ">Hermione agrees reluctantly."
    elif request_19_points == 1: #Two stars.
        her "...yes, [genie_name]."
        ">Hermione agrees."
    elif request_19_points == 2: #Three stars.
        ">Hermione agrees nonchalantly."
    elif request_19_points >= 3: #Master.
        her "Here you go, [genie_name]."
        ">Hermione agrees eagerly."
        
    "You dismiss Hermione."
        
    if whoring <= 14:
        $ whoring +=1

    if request_19_points <= 2:
        $ gryffindor +=45
        "gryffindor got +45 points."
    else:
        $ gryffindor +=11
        "gryffindor got +11 points."
       
    $ request_19_points += 1
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        

    
    
    
#############################################################################################################################################
### LEVEL 06 ################################################################################################################################       
###################REQUEST_21 (Level 06) (55 pt.) (Cum on tits). ############################################################################ 
#As this request levels up, there are an option appears to offer some extra points if Hermione will put her clothes
#on top of her sperm covered tits and go to classes like that.
label new_request_21: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    
    m "Come here and let me jerk off on your tits."
    if request_21_points == 0: #One star.
        her "Oh... "
        ">Hermione agrees reluctantly."
        ">You cum on her bare tits."
    elif request_21_points == 1: #Two stars.
        her "...yes, [genie_name]."
        ">Hermione agrees."
        ">You cum on her bare tits."
    elif request_21_points == 2: #Three stars.
        ">Hermione agrees nonchalantly."
        ">You cum on her bare tits."

    elif request_21_points >= 3: #Master.
        her "As you wish, head...master."
        ">Hermione agrees eagerly."
        ">You cum on her bare tits."
    
    her "Could I have a towel to clean myself up?"
    menu:
        "\"There you go.\"":
            ">You hand Hermione a towel and she wipes your sperm off."
        "\"Just go like this.\"":
            m "Just button up your shirt and go like this."
            
            if request_21_points <= 1:
                her "What? No I cant, Please, gimme a towel, [genie_name]."
                ">You hand Hermione a towel and she wipes your sperm off."
           
            else:
                her "What? But..."
                her "Well alright, but only if i get paid extra for this."
                menu:
                    "-Pay her extra-":
                        m "Fine..."
                        her "Alright then..."
                        ">Hermione buttons up her shirt."
                        $ gryffindor +=10
                        "gryffindor got +10 points."
                        $ request_21 = True
                    "-Never mind-":
                        ">You hand Hermione a towel and she wipes your sperm off."
            
    "You dismiss Hermione."
        
    if whoring <= 14:
        $ whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=55
        "gryffindor got +55 points."
    else:
        $ gryffindor +=12
        "gryffindor got +12 points."
       
    $ request_21_points += 1 
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
        
label new_request_21_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_21_points == 3: #One star.
        her "Ehm... During classes I've been sitting there with my breasts covered in cum under my shirt. So embarrassing..."
    elif request_21_points >= 4: #Two stars.
        her "During classes I've been sitting there with my breasts covered in cum under my shirt. I had the best time of my life."
             

    
    $ request_21 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return        
        
        
    

    

#############################################################################################################################################
### LEVEL 07 ################################################################################################################################  
#############################################################################################################################################
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label new_request_25: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    
    m "Come here and let me jerk off on your face."
    if request_25_points == 0: #One star.
        her "Oh... "
        ">Hermione agrees reluctantly."
        ">You cum on her bare face."
    elif request_25_points == 1: #Two stars.
        her "...yes, [genie_name]."
        ">Hermione agrees."
        ">You cum on her bare face."
    elif request_25_points == 2: #Three stars.
        ">Hermione agrees nonchalantly."
        ">You cum on her bare face."

    elif request_25_points >= 3: #Master.
        her "Of course, head...master."
        ">Hermione agrees eagerly."
        ">You cum on her face."
    
    her "Could I have a towel to clean myself up?"
    menu:
        "\"There you go.\"":
            ">You hand Hermione a towel and she wipes your sperm off."
        "\"Just go like this.\"":
            m "Just go to classes with your face covered in my cum."
            
            if whoring <=26:
                her "What? No I cant. Please, gimme a towel, [genie_name]."
                ">You hand Hermione a towel and she wipes your sperm off."
           
            else:
                her "What? But..."
                her "Well alright, but only if i get paid extra for this."
                menu:
                    "-Pay her extra-":
                        m "Fine..."
                        her "Alright then..."
                        ">Hermione doesn't touch her cum covered face."
                        $ gryffindor +=30
                        "gryffindor got +30 points."
                        $ request_25 = True
                    "-Never mind-":
                        ">You hand Hermione a towel and she wipes your sperm off."
            
    "You dismiss Hermione."
        
    if whoring <= 20:
        $ whoring +=1

    if request_21_points <= 2:
        $ gryffindor +=65
        "gryffindor got +65 points."
    else:
        $ gryffindor +=14
        "gryffindor got +14 points."
       
    $ request_25_points += 1 
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
        
        
        
label new_request_25_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    her "Ehm... I spent big part of the day with cum on my face. People were asking questions."
    
    
    $ request_25 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return        
        

###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label new_request_26: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    m "I want you to cum in your mouth before you go to class."
    if request_26_points == 0: #One star.
        her "Oh..."
        "Hermione reluctantly agrees."
    elif request_26_points == 1: #Two stars.
        her "If i must..."
        "Hermione agrees."
    elif request_26_points == 2: #Three stars.
        her "Of course... [genie_name]."
        "Hermione agrees. She is very eager."    
    elif request_26_points >= 3: #Master.
        her "Of course, head...master"
        ">Hermione agrees cheerfully."
    
    "You dismiss Hermione."
    
    $ request_26 = True 
    if whoring <= 20:
        $ whoring +=1
        
    if request_26_points <= 2:
        $ gryffindor +=65
        "gryffindor got +65 points."
    else:
        $ gryffindor +=14
        "gryffindor got +14 points."

    $ hermione_takes_classes = True
    jump day_main_menu
        

label new_request_26_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_26_points == 0: #One star.
        her "Ehm... I spent half of the first class with your cum in my mouth."
    elif request_26_points == 1: #Two stars.
        her "Something else about cum. LVL 2"
    elif request_26_points == 2: #Three stars.
        her "LVL3"
    elif request_26_points >= 3: #Three stars.
        her "LVL4"
        her "It was great!"
    
    $ request_26_points += 1 
    $ request_26 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label new_request_27: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    m "I want you to do something for me during class today: blow two classmates"
    if request_27_points == 0: #One star.
        her "Oh..."
        "Hermione reluctantly agrees."
    elif request_27_points == 1: #Two stars.
        her "If i must..."
        "Hermione agrees."
    elif request_27_points == 2: #Three stars.
        her "Of course, [genie_name]"
        "Hermione agrees. She is very eager."    
    elif request_27_points >= 3: #Master.
        her "Of course head...master"
        ">Hermione agrees cheerfully."
    
    "You dismiss Hermione."
    
    $ request_27 = True 
    if whoring <= 20:
        $ whoring +=1
        
    if request_27_points <= 2:
        $ gryffindor +=65
        "gryffindor got +65 points."
    else:
        $ gryffindor +=14
        "gryffindor got +14 points."

    $ hermione_takes_classes = True
    jump day_main_menu
        

label new_request_27_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_27_points == 0: #One star.
        her "Em... Lvl.1."
    elif request_27_points == 1: #Two stars.
        her "Something else about LVL 2"
    elif request_27_points == 2: #Three stars.
        her "LVL3"
    elif request_27_points >= 3: #Three stars.
        her "LVL4"
        her "It was great!"
    
    $ request_27_points += 1 
    $ request_27 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
    
###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label new_request_28: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    m "I want you to do something for me during class today: give a handjob to a teacher."
    if request_28_points == 0: #One star.
        her "Oh..."
        "Hermione reluctantly agrees."
    elif request_28_points == 1: #Two stars.
        her "If i must..."
        "Hermione agrees."
    elif request_28_points == 2: #Three stars.
        her "Of course, [genie_name]."
        "Hermione agrees. She is very eager."    
    elif request_28_points >= 3: #Master.
        her "Of course head...master."
        ">Hermione agrees cheerfully."
    
    "You dismiss Hermione."
    
    $ request_28 = True 
    if whoring <= 20:
        $ whoring +=1
        
    if request_28_points <= 2:
        $ gryffindor +=65
        "gryffindor got +65 points."
    else:
        $ gryffindor +=14
        "gryffindor got +14 points."

    $ hermione_takes_classes = True
    jump day_main_menu

        
label new_request_28_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_28_points == 0: #One star.
        her "Em... Lvl.1."
    elif request_28_points == 1: #Two stars.
        her "Something else about LVL 2"
    elif request_28_points == 2: #Three stars.
        her "LVL3"
    elif request_28_points >= 3: #Three stars.
        her "LVL4"
        her "It was great!"
    
    $ request_28_points += 1 
    $ request_28 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    


   
    
    


    
###############################################################################################################################################
### LEVEL 10 ##################################################################################################################################
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only) ####################################
label new_request_32: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    m "I want you to do something for me during class today: wear this dress."
    if request_32_points == 0: #One star.
        her "Oh..."
        "Hermione reluctantly agrees."
    elif request_32_points == 1: #Two stars.
        her "If i must..."
        "Hermione agrees."
    elif request_32_points == 2: #Three stars.
        her "Of course, [genie_name]."
        "Hermione agrees. She is very eager."    
    elif request_32_points >= 3: #Master.
        her "Of course, head...master."
        ">Hermione agrees cheerfully."
    
    "Hermione puts on a very slutty outfit and goes to classes."
    
    $ request_32 = True 
    if whoring <= 29:
        $ whoring +=1
        
    if request_32_points <= 2:
        $ gryffindor +=100
        "gryffindor got +100 points."
    else:
        $ gryffindor +=23
        "gryffindor got +23 points."

    $ hermione_takes_classes = True
    jump day_main_menu


label new_request_32_complete:
    "Hermione returns from her classes."
    m "How was your day, [hermione_name]?"
    if request_32_points == 0: #One star.
        her "Em... Lvl.1. She tells you how people treated her like a whore today."
    elif request_32_points == 1: #Two stars.
        her "Something else about LVL 2. She tells you how people treated her like a whore today."
    elif request_32_points == 2: #Three stars.
        her "LVL3. She tells you how people treated her like a whore today."
    elif request_32_points >= 3: #Three stars.
        her "LVL4. She tells you how people treated her like a whore today."
        her "It was great!"
    
    $ request_32_points += 1
    $ request_32 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
    
    

    
    
    
    
    
### MUSIC BLOCK ###
label music_block:
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    return
    ### END OF BLOCK ###    
    
    


### YOU LUCK IMAGINATION ###
label vague_idea:
    show screen blktone8
    ">You lack imagination for an idea of this caliber."
    hide screen blktone8
    return




    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    

        
        
        
        
  
    
    
    

        
        
        
        
        
        
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
