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
                    "Favour: \"Talk to me\" {image=heart_0[new_request_01_heart]}   {image=interface/clothes.png}":
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
                    "Favour: \"Breast molester\" {image=heart_0[new_request_04_heart]}   {image=interface/clothes.png}" if imagination >= 2: 
                        jump new_request_04
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Butt molester\" {image=heart_0[new_request_05_heart]}   {image=interface/clothes.png}" if imagination >= 2:
                        jump new_request_05
                        
                    ### LEVEL 03 ### IMAGINATION == 3
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Show them to me!\" {image=heart_0[new_request_08_heart]}   {image=interface/clothes.png}" if imagination >= 3:
                        jump new_request_08
                        
#                    "Favour: \"Show {size=+5}it{/size} to me! (NOT FINISHED YET)":
#                        jump new_request_09
                    
                    ### LEVEL 04 ### IMAGINATION == 3
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Dance for me!\" {image=heart_0[new_request_11_heart]}   {image=interface/clothes.png}" if imagination >= 3:
                        jump new_request_11
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Let me touch them!\" {image=heart_0[new_request_12_heart]}   {image=interface/clothes.png}" if imagination >= 3: # LEVEL 4
                        jump new_request_12
                        
                    ### LEVEL 05 ### IMAGINATION == 4
                    "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Favour: \"touch me!\" {image=heart_0[new_request_16_heart]}   {image=interface/clothes.png}" if imagination >= 4: # LEVEL 5
                        jump new_request_16
                        
                    ### LEVEL 06 ### IMAGINATION == 4
                    "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Suck it!\" {image=heart_0[new_request_22_heart]}   {image=interface/clothes.png}" if imagination >= 4: # LEVEL 6
                        jump new_request_22
                        
                    ### LEVEL 07 ### IMAGINATION == 5
                    "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Let's have sex!\" {image=heart_0[new_request_29_heart]}   {image=interface/clothes.png}" if imagination >= 5: # LEVEL 7
                        jump new_request_29
                    
                    ### LEVEL 08 ###
                    "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Favour:  \"Time for anal!\" {image=heart_0[new_request_31_heart]}   {image=interface/clothes.png}" if imagination >= 5: # LEVEL 8
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
                    "-luna potion-" if "Luna Transformation Potion" in p_inv:
                        if p_potion_names[4] in p_inv:
                            $ p_inv.remove(p_potion_names[4])
                            jump potion_scene_6
                        else:
                            m "I don't have this potion..."
                            jump request_potion_menu
                    ##"-Snek-" if whoring >= 3:
                    ##    jump potion_scene_5
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
    
label end_hg_pf:
    $ renpy.play('sounds/door.mp3') #Sound of a door.
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
    
label could_not_flirt: #Sent here when choose "Favour failed! No points for you!" (Hermione is leaving without getting any points).
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
label could_not_flirt_02: #Sent here when chose "Favour failed! No points for you!"
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ request_02_b_points += 1
    $ request_02_b = False 
    $ hermione_sleeping = True
    
    return   
    
    
### MUSIC BLOCK ###
label music_block:
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    return
    
### YOU LUCK IMAGINATION ###
label vague_idea:
    show screen blktone8
    ">You lack imagination for an idea of this caliber."
    hide screen blktone8
    return
    
### ALL THE SCREAMS ABOUT RAPE ###
label screams_of_rapings:
    call her_head("NO! What have you done!!?","head_exp/10")
    ">Hermione gives you an unexpectedly strong shove..."
    with hpunch
    call her_head("Why would you do this to me, [genie_name]...?","head_exp/10")
    call her_head("I never agreed to... to...","head_exp/27")
    call her_head("You... you...","head_exp/27")
    with hpunch
    call her_head("{size=+7}YOU RAPED ME!{/size}","head_exp/29")
    g4 "What? Don't be ridiculous, [hermione_name]! I did no such thing!"
    call her_head("Yes you did! Yes you did!","head_exp/29")
    g4 "I most certainly did not!"
    call her_head("No, you did, [genie_name]!","head_exp/29")
    call her_head("Now, you will give me 20--","head_exp/31")
    call her_head("No, 100 house points or I am reporting you to the Ministry of magic!","head_exp/31")
    menu:
        m "(Ah, crap...)"
        "\"Alright, alright... 100 points it is...\"":
            $ gryffindor +=100
            m "One hundred points to \"Gryffindor\" !"
            m "There, it is done..."
            m "Now would you calm yourself down, [hermione_name]?"
            call her_head("No, I will not!","head_exp/29")
            call her_head("I've just been raped!","head_exp/29")
            g4 "Oh, snap out of it [hermione_name], I didn't rape you! All I did was--"
            with hpunch
            call her_head("{size=+7}You raped me!!!{/size}","head_exp/29")
            g4 "By the great desert sands, would you keep it down about the rapes!?"
            g4  "Someone may hear you!"
            call her_head("Good! I want them to hear!","head_exp/29")
            m "Why would you want that? I already paid you!"
            call her_head("Oh... right...","head_exp/32")
            call her_head("But I hate you! I hate you [genie_name]!","head_exp/33")
            $ mad +=30

        "\"You're bluffing, [hermione_name]!\"":
            call her_head("No, I'm not! I'm gonna do it!","head_exp/29")
            g4 "By all means, go ahead..."
            g4 "There was no rape!"
            call her_head("I hate you, [genie_name]!","head_exp/29")
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
    
    call her_walk(400,610,2)
    show screen hermione_stand_f #Hermione stands still.
    with d3

    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        call her_head("...........................","head_exp/12")
        
        
    hide screen hermione_stand_f #Hermione stands still.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with d3
    pause.5

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu        
    
### SCREAM OF PLEASURES ###        
label screams_of_pleasure:
    call her_head("Ah....","head_exp/34")
    call her_head("It's inside of me...")
    call her_head("No, [genie_name], you must stop now...","head_exp/18")
    m "Why? You don't like it?"
    call her_head("It doesn't matter whether I like this or not, [genie_name].")
    call her_head("You know why I'm doing this...")
    call her_head("And it is wrong for me to let you do this to me for a meagre 15 points...")
    ">Hermione pulls away from you..."
    m "Heh... I see..."
    m "Well, in that case..."
    jump ending_of_screams_of_pleasure
    
    
label Day_Request_Block:
    
    
    return
    
label Night_Request_Block:
    ###JOBS###
    if current_job == 1:
        jump maid_responses

    if current_job == 2:
        jump barmaid_responses

    if current_job == 3:
        jump gryffindor_cheer_responses

    if current_job == 4:
        jump slytherin_cheer_responses

    if ears == True:
        jump potion_scene_1_2

    if transparency < 1:
        jump potion_scene_4_2

    if addicted == True:
        jump potion_scene_3_2
    
    
    if request_02_b:
        call new_request_02_b_complete
    if request_02_c:
        call new_request_02_c_complete
    if hg_pf_PantyThief_InProgressFlag:
        call hg_pf_PantyThief_complete
    if request_05:
        call new_request_05_complete
    if request_06:
        call new_request_06_complete
    if request_10:
        call new_request_10_complete
    #if request_13: # SEE THROUGH SHIRT DURING CLASS. NOT USED.
    #    call request_13_complete
    if request_15: #(Flash a nipple to a teacher).
        call new_request_15_complete
    if request_20: #(Grab a classmate's cock).
        call new_request_20_complete
    if request_21: #(Jerk off on tits and put the clothes back on).
        call new_request_21_complete
    if request_23: #(Give handjob to a classmate).
        call new_request_23_complete
    if request_24: #(Flash your tits to a teacher).
        call new_request_24_complete
    if request_25: #(Cum on face and send to class).
        call new_request_25_complete
    if request_26: #(Go to class with mouth full of cum).
        call new_request_26_complete
    if request_27: #(Blow two classmates).
        call new_request_27_complete
    if request_28: #(Handjob to a teacher).
        call new_request_28_complete
    if request_30: #(FUCK A CLASSMATE).
        call new_request_30_complete
    if request_32: #(Put on a slutty dress and go to classes).
        call new_request_32_complete
    if request_33: #(Go to classes with cum covered face).
        call new_request_33_complete
    if pub_q_blowjob_teach:#pub_q_blowjob_teach
        call pub_quest_blowjob_teach_complete
    if pub_q_sex_teach:#pub_q_sex_teach
        call pub_quest_sex_teach_complete
    
    if per_q_the_gamble and per_q_the_gamble_c or per_q_the_gamble_a:
        jump hg_pf_TheGamble_complete
    
    return
    
label cum_block:
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause.1
    hide screen white
    with hpunch
    return
    
#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    stop music fadeout 2.0
    call her_main("[genie_name]??!","body_48",xpos=120)
    her "How could you ask for such a thing!?"
    call her_main("I think I better leave.","body_34",xpos=120)
    
    $ mad += 7
    
    hide screen blktone
    hide screen bld1
    hide screen hermione_main
    hide screen hermione_stand_f #Hermione stands still.
    with d3
    
    call her_walk(400,610,2)
    
    call reset_hermione_main
    jump end_hg_pf

label very_no:
    stop music fadeout 2.0
    call her_main("Absolutely not!","body_12",xpos=120)
    her "I'll show you that my integrity and honour as a Gryffindor cannot be bought!"
    call her_main("I'm leaving this instant.","body_30",xpos=120)
    
    $ mad += 7
    
    hide screen blktone
    hide screen bld1
    hide screen hermione_main
    hide screen hermione_stand_f #Hermione stands still.
    with d3
    
    call her_walk(400,610,2)
    
    call reset_hermione_main
    jump end_hg_pf
    
    
    
    
    
    
    
    
########################################
####                                ####
####        UNUSED REQUESTS         ####
####                                ####
########################################
    
    
    
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
        call her_main("Really?","body_03",xpos=370)
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

    
#                    "-Personal requests (lv.1)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Stand there. (I touch myself.)(5pt.)": #Request_01 (Level 01)
#                                    jump request_01
#                                "Lift your skirt.(5pt.)": #Request_02 (Level 01)
#                                    jump request_02
#                                "Flirt with 3 classmates.(5pt.)" if daytime: #Request_02_b (Level 01)
#                                    jump request_02_b
#                                "Flirt with a teacher.(5pt.)" if daytime:  #Request_02_c (Level 01)
#                                    jump request_02_c
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 02###    
#                    "-Personal requests (lv.2)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Take her panties.(15pt.)" if daytime: #Request_03 (Level 02)
#                                    jump request_03
#                                "Touch her tits through her clothes. (15pt)": #Request_04 (Level 02)
#                                    jump request_04
#                                "Touch her butt though her clothes.(15pt)": #Request_05 (Level 02)
#                                    jump request_05
#                                "Flash panties to a classmate. (15pt)" if daytime: #Request_06 (Level 02)
#                                    jump request_06
#                                "Flash panties to a teacher.(15pt)" if daytime: #Request_07 (Level 02)
#                                    jump request_07
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 03###
#                    "-Personal requests (lv.3)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Show me your tits. (25pt)":#Request_08 (Level 03)
#                                    jump request_08
#                                "Show me your pussy.(25pt)":#Request_09 (Level 03):
#                                    jump request_09
#                                "Flash a nipple to a classmate. (25pt)." if daytime:#Request_10 (Level 03)
#                                    jump request_10
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                                    
#                    ###LEVEL 04###
#                    "-Personal requests (lv.4)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Strip completely.(35pt)":#Request_11 (Level 04)
#                                    jump request_11
#                                "Play with her tits.(35pt)":#Request_12 (Level 04):
#                                    jump request_12   
#                                "Wear a see-through shirt.(35pt)" if daytime:#Request_13 (Level 04):
#                                    jump request_13   
#                                "wear Cum-soaked panties": #Request_14 (Level 04) #To be added later when ability to jerk off and cum on panties added.
#                                    pass
#                                "Flash a nipple to a teacher.(35pt)" if daytime:#Request_15 (Level 04):
#                                    jump request_15   
#                                "Cancel.":
#                                    jump day_time_requests                    
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                    ###LEVEL 05###
#                    "-Personal requests (lv.5)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Finger her pussy.(45pt)":#Request_16 (Level 05)
#                                    jump request_16
#                                "Finger her butthole.(45pt)":#Request_17 (Level 05)
#                                    jump request_17
#                                "Handjob.(45pt)":#Request_18 (Level 05)
#                                    jump request_18
#                                "Rub your dick against her cheeks.(45pt)": #Request_19 (Level 05)
#                                    jump request_19
#                                "Grab a classmate's cock.(45pt)" if daytime: #Request_20 (Level 05)
#                                    jump request_20
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests
#                     
#                    ###LEVEL 06###
#                    "-Personal requests (lv.6)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Cum on tits.(55pt)":#Request_21 (Level 06)
#                                    jump request_21
#                                "Blowjob.(55pt)":#Request_22 (Level 06)
#                                    jump request_22
#                                "Give a handjob to a classmate.(55pt)" if daytime:#Request_23 (Level 06)
#                                    jump request_23
#                                "Flash your tits to a teacher.(55pt)" if daytime:#Request_24 (Level 06)
#                                    jump request_24
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
#                    
#                    ###LEVEL 07###
#                    "-Personal requests (lv.7)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Cum on face.(65pt)":#Request_25 (Level 07)
#                                    jump request_25
#                                "Cum in her mouth before class.(65pt)" if daytime:#Request_26 (Level 07)
#                                    jump request_26
#                                "Blow two classmates.(65pt)" if daytime:#Request_27 (Level 07)
#                                    jump request_27
#                                "Give a handjob to a teacher.(65pt)" if daytime:#Request_28 (Level 07)
#                                    jump request_28
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests  
#                            
#                    ###LEVEL 08###
#                    "-Personal requests (lv.8)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Sex.(75pt)":#Request_29 (Level 08)
#                                    jump request_29
#                                "Blow a teacher.(75pt)" if daytime: #Request_30 (Level 08)
#                                    jump request_30
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
#                    
#                    ###LEVEL 09###
#                    "-Personal requests (lv.9)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Anal sex.(85pt)" if not daytime:#Request_31 (Level 09)
#                                    jump request_31
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
#                    
#                    ###LEVEL 10###
#                    "-Personal requests (lv.10)":
#                        if slytherin > gryffindor or slytherin == gryffindor:
#                            menu:
#                                "Wear a revealing outfit to class.(100pt)" if daytime:#Request_32 (Level 10)
#                                    jump request_32
#                                "Cum covered face.(100pt)" if daytime:#Request_33 (Level 10)
#                                    jump request_33
#                                "Cancel.":
#                                    jump day_time_requests
#                        else:
#                            her "The Gryffindors are in the lead. I don't need to do this."
#                            jump day_time_requests 
#                    
#                    
#                    
#                    "-Dismiss her-":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
    
    
################
### LEVEL 01 ###                
###################REQUEST_01
label request_01: #LV.1 (Whoring = 0 - 2)
    "Hermione is looking at you with interest and blushes."
    "You dismiss Hermione."
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

    
###################REQUEST_02 (Level 01)
label request_02:
    "Hermione reluctantly lifts her skirt and shows you her panties. She is blushing a lot."
    "You dismiss Hermione."
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        

###################REQUEST_02_b (Level 01)
label request_02_b:
    "Hermione agrees to try and flirt with 3 classmates."
    "You dismiss Hermione."
    $ request_02_b = True
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
label request_02_b_complete:
    "Hermione returns from her classes. She tells you about the guys she flirted with."
    $ request_02_b = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
###################REQUEST_02_c (Level 01)
label request_02_c:
    "Hermione agrees to try and flirt with a teacher."
    "You dismiss Hermione."
    $ request_02_c = True
    if whoring <= 2:
        $ whoring +=1
    $ gryffindor +=5
    "gryffindor got +5 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
label request_02_c_complete:
    "Hermione returns from her classes. She tells you about flirting with her teacher."
    $ request_02_c = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return    
    
    
################
### LEVEL 02 ###    
###################REQUEST_03 (Level 02) (Available during daytime only).
label request_03: #(Whoring = 3 - 5)
    if whoring <=2:
        jump too_much
        
    if whoring >= 3: #Level 02
        "Hermione hesitantly pulls her panties down and hands them over to you."
        "You dismiss Hermione."
        $ request_03 = True #True when Hermione has no panties on.
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        $ hermione_takes_classes = True
        "gryffindor got +15 points."
        jump day_main_menu
        
label request_03_complete:
    "Hermione returns from her classes. You give her her panties back."
    $ request_03 = False #When False - you gave her her panties back.
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return


###################REQUEST_04 (Level 02) (Touch tits's through fabric.)
label request_04:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione lets you fondle her tits a little."
        "You dismiss Hermione."
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu
            
###################REQUEST_05 (Level 02) (Touch butt through fabric.)
label request_05:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione lets you fondle her butt a little."
        "You dismiss Hermione."
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
        if daytime:
            $ hermione_takes_classes = True
            jump day_main_menu
        else:
            $ hermione_sleeping = True
            jump night_main_menu

###################REQUEST_06 (Level 02) (Flash panties to classmate.)
label request_06:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione agrees to try and flash her panties to a classmate."
        "You dismiss Hermione."
        $ request_05 = True
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
        $ hermione_takes_classes = True
        jump day_main_menu
       
label request_05_complete:
    "Hermione returns from classes. She tells you about her attempts to flash her panties to a classmate."
    $ request_05 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    

###################REQUEST_07 (Level 02) (Flash panties to a teacher).(Daytime only).
label request_07:
    if whoring <=2:
        jump too_much
    if whoring >= 3: #Level 02
        "Hermione agrees to try and flash her panties to a teacher."
        "You dismiss Hermione."
        $ request_06 = True
        if whoring <= 5:
            $ whoring +=1
        $ gryffindor +=15
        "gryffindor got +15 points."
        $ hermione_takes_classes = True
        jump day_main_menu
        

label request_06_complete:
    "Hermione returns from her classes and tells you about her attempts to flash her panties to a teacher."
    $ request_06 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return
    
################
### LEVEL 03 ###
###################REQUEST_08 (Level 03) (Show me tits).
label request_08: #LV.3 (Whoring = 6 - 8)
    if whoring <=5:
        jump too_much
    "Hermione shows you her tits."
    "You dismiss Hermione."
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    "gryffindor got +25 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_09 (Level 03) (Show me pussy).
label request_09: #LV.3 (Whoring = 6 - 8)
    if whoring <=5:
        jump too_much
    "Hermione shows you her pussy."
    "You dismiss Hermione."
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    "gryffindor got +25 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_10 (Level 03) (25 pt.) (Flash nipple to a classmate). (Available during daytime only).
label request_10:
    if whoring <=5:
        jump too_much
    "Hermione agrees to try and flash her nipple to a classmate."
    "You dismiss Hermione."
    $ request_10 = True 
    if whoring <= 8:
        $ whoring +=1
    $ gryffindor +=25
    $ hermione_takes_classes = True
    "gryffindor got +25 points."
    jump day_main_menu
        
label request_10_complete:
    "Hermione returns from classes. She tells you how she flashed her nipple to a classmate."
    $ request_10 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

################
### LEVEL 04 ###
###################REQUEST_11 (Level 04) (Get naked.) (Day/Night)
label request_11: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione undresses before you and Then puts her clothes back on."
    "You dismiss Hermione."
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    "gryffindor got +35 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night)
label request_12: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione bares her tits. You play with them for a while."
    "You dismiss Hermione."
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    "gryffindor got +35 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_13 (Level 04) (35 pt.) (Wear see-though shirt to classes). (Available during daytime only).
label request_13: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione agrees to put on a see-through shirt and go to class."
    "You dismiss Hermione."
    $ request_13 = True 
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "gryffindor got +35 points."
    jump day_main_menu
        
label request_13_complete:
    "Hermione returns from her classes and tells you how everyone was starring at her tits today."
    $ request_13 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

###################REQUEST_15 (Level 04) (35 pt.) (Flash a nipple to a teacher). (Available during daytime only).
label request_15: #LV.4 (Whoring = 9 - 11)
    if whoring <=8:
        jump too_much
    "Hermione agrees to try and flash a nipple to a teacher."
    "You dismiss Hermione."
    $ request_15 = True 
    if whoring <= 11:
        $ whoring +=1
    $ gryffindor +=35
    $ hermione_takes_classes = True
    "gryffindor got +35 points."
    jump day_main_menu
        
label request_15_complete:
    "Hermione returns from her classes. She tells you how she flashed her nipples to a teacher."
    $ request_15 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then."
    return

################
### LEVEL 05 ###   
###################REQUEST_16 (Level 05) (Finger her pussy) (Day/Night)
label request_16: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione lets you finger her pussy."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_17 (Level 05) (Stick a finger up her but thole.) (Day/Night)
label request_17: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione lets you stick a finger up her butthole."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu


###################REQUEST_18 (Level 05) (Handjob) (Day/Night)
label request_18: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione gives you a handjob."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_19 (Level 05) (Rub your dick against her cheeks.) (Day/Night)
label request_19: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione sits still while you rub your cock against her face."
    "You dismiss Hermione."
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    "gryffindor got +45 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_20 (Level 05) (45 pt.) (Grab a classmate's cock). (Available during daytime only).
label request_20: #LV.5 (Whoring = 12 - 14)
    if whoring <=11:
        jump too_much
    "Hermione agrees to try and grab a classmate's cock."
    "You dismiss Hermione."
    $ request_20 = True 
    if whoring <= 14:
        $ whoring +=1
    $ gryffindor +=45
    $ hermione_takes_classes = True
    "gryffindor got +45 points."
    jump day_main_menu
        
label request_20_complete:
    "Hermione returns from her classes and tells you how she grabbed the cock of one of her classmates."
    $ request_20 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
###################REQUEST_21 (Level 06) (55 pt.) (Cum on tits). 
#As this request levels up, there are an option appears to offer some extra points if Hermione will put her clothes
#on top of her sperm covered tits and go to classes like that.
label request_21: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione bares her tits. You jerk off and cum all over them."
    "You dismiss Hermione."
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label request_22: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione gives you a blowjob."
    "You dismiss Hermione."
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_23 (Level 06) (55 pt.) (Give handjob to a classmate). (Available during daytime only).
label request_23: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione agrees to try and give a handjob to a classmate."
    "You dismiss Hermione."
    $ request_23 = True 
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    jump day_main_menu
        
label request_23_complete:
    "Hermione returns from her classes and tells you how she gave a handjob to one of her classmates during class."
    $ request_23 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return

###################REQUEST_24 (Level 06) (55 pt.) (Flash your tits to a teacher). (Available during daytime only).
label request_24: #LV.6 (Whoring = 15 - 17)
    if whoring <=14:
        jump too_much
    "Hermione agrees to try and flash her tits to a teacher."
    "You dismiss Hermione."
    $ request_24 = True 
    if whoring <= 17:
        $ whoring +=1
    $ gryffindor +=55
    $ hermione_takes_classes = True
    "gryffindor got +55 points."
    jump day_main_menu
        
label request_24_complete:
    "Hermione returns from her classes. She tells you how she flashed her tits to a teacher."
    $ request_24 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
###################REQUEST_25 (Level 07) (65 pt.) (Cum on face). 
label request_25: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione sits still while you jerk off in her face."
    "You dismiss Hermione."
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
        
###################REQUEST_26 (Level 07) (65 pt.) (Cum in open mouth before class). (Available during daytime only).
label request_26: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione sits still with her mouth wide open while you jerk off and cum in it. You tell her to only swallow it when she gets to class."
    "You dismiss Hermione with her mouth full of your cum."
    $ request_26 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    jump day_main_menu
        
label request_26_complete:
    "Hermione returns from her classes and tells you that she couldn't speak to her classmates because her mouth was filled with your cum."
    $ request_26 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then."
    return

###################REQUEST_27 (Level 07) (65 pt.) (Blow two classmates). (Available during daytime only).
label request_27: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione agrees to try and blow two classmates during classes."
    "You dismiss Hermione."
    $ request_27 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    jump day_main_menu
        
label request_27_complete:
    "Hermione returns from her classes. She tells you how she gave a blowjob to two classmates during classes."
    $ request_27 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then."
    return

###################REQUEST_28 (Level 07) (65 pt.) (Give handjob to a teacher). (Available during daytime only).
label request_28: #LV.7 (Whoring = 18 - 20)
    if whoring <=17:
        jump too_much
    "Hermione agrees to try and give a handjob to a teacher during classes."
    "You dismiss Hermione."
    $ request_28 = True 
    if whoring <= 20:
        $ whoring +=1
    $ gryffindor +=65
    $ hermione_takes_classes = True
    "gryffindor got +65 points."
    jump day_main_menu
        
label request_28_complete:
    "Hermione returns from classes and tells you how she gave a handjob to a teacher during classes."
    $ request_28 = False 
    $ hermione_sleeping = True
    her "Oh, alright. I will go to bed then, Sir."
    return
    
################
### LEVEL 08 ###
###################REQUEST_29 (Level 08) (75 pt.) (Sex). 
label request_29: #LV.8 (Whoring = 21 - 23)
    if whoring <=20:
        jump too_much
    if daytime:
        "You have sex with Hermione and send her to her classes afterwards."
    else:
        "You have sex with Hermione."
        "You send her to bed."
    if whoring <= 23:
        $ whoring +=1
    $ gryffindor +=75
    "gryffindor got +75 points."
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_30 (Level 08) (75 pt.) (Blow a teacher). (Available during daytime only).
label request_30: #LV.8 (Whoring = 21 - 23)
    if whoring <=20:
        jump too_much
    "Hermione agrees to try and blow a teacher."
    "You dismiss Hermione."
    $ request_30 = True 
    if whoring <= 23:
        $ whoring +=1
    $ gryffindor +=75
    $ hermione_takes_classes = True
    "gryffindor got +75 points."
    jump day_main_menu
        
label request_30_complete:
    "Hermione returns from her classes. She tells you how she gave a blowjob to a teacher during classes."
    $ request_30 = False 
    $ hermione_sleeping = True
    her "Oh, alright, Sir. I will go to bed then, Sir."
    return

################
### LEVEL 09 ###
###################REQUEST_31 (Level 09) (85 pt.) (Anal sex). (Nighttime)
label request_31: #LV.9 (Whoring = 24 - 26)
    if whoring <=23:
        jump too_much
    "You have anal sex with Hermione."
    "You order her to go to bed afterwards."
    if whoring <= 26:
        $ whoring +=1
    $ gryffindor +=85
    "gryffindor got +85 points."
    $ hermione_sleeping = True
    jump day_start


################
### LEVEL 10 ###
###################REQUEST_32 (Level 10) (100 pt.) (Wear a very revealing outfit to class). (Daytime only)
label request_32: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    "Hermione puts on a very slutty outfit and goes to her classes."
    $ request_32 = True
    if whoring <= 29:
        $ whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "gryffindor got +100 points."
    jump day_main_menu

label request_32_complete:
    "Hermione returns from classes. She tells you that people treated her like a whore today."
    $ request_32 = False 
    $ hermione_sleeping = True
    her "Oh, as you wish, Sir. I will go to bed then, Sir."
    return

###################REQUEST_33 (Level 10) (100 pt.) THIS REQUEST IS NOW CAN ONLY BE ACCESSED THROUGH REQUEST_25 (CUM ON FACE) when whoring > 26. (Go to class with cum on your face). (Daytime only)
label request_33: #LV.10 (Whoring = 27 - 29)
    if whoring <=26:
        jump too_much
    "You cum all over hermione's face and send her to her classes."
    $ request_33 = True
    if whoring <= 29:
        $ whoring +=1
    $ gryffindor +=100
    $ hermione_takes_classes = True
    "gryffindor got +100 points."
    jump day_main_menu

label request_33_complete:
    "Hermione returns from her classes. She tells you that people treated her like trash and laughed at her today."
    $ request_33 = False 
    $ hermione_sleeping = True
    her "Oh, as you wish, Sir. I will go to bed then, Sir."
    return

