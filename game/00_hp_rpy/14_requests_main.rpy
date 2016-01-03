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
                    "Favour: \"Suck it!\" {image=heart_0[new_request_22_heart]}   {image=interface/clothes.png}" if imagination >= 4: # LEVEL 6
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

    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
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
    hide screen hermione_02
    hide screen ctc
    with d3

    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f
    
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
    
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    # $ hermione_chibi_xpos = 610 #Near the desk.
    
    call her_walk(400,610,2)
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
    
### SCREAM OF PLEASURES ###        
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
    if request_03:
        call new_request_03_complete
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
        jump per_quest_the_gamble_complete
    
    return
    
    
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
    
