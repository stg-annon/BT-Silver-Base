label new_personal_request:
    if slytherin > gryffindor or slytherin == gryffindor:
        show screen hermione_main
        $ menu_x = 0.2 #Default: 0.5
        
        
        label not_now:
        menu:
            "-Custom favours-":
                jump new_custom_request
            
            "-Personal favours-":
                
                $ hg_pf_TalkToMe_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_TalkToMe_ID])+".png"
                $ hg_pf_NicePanties_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_NicePanties_ID])+".png"
                $ hg_pf_PantyThief_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_PantyThief_ID])+".png"
                $ hg_pf_BreastMolester_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_BreastMolester_ID])+".png"
                $ hg_pf_ButtMolester_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_ButtMolester_ID])+".png"
                $ hg_pf_ShowThemToMe_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_ShowThemToMe_ID])+".png"
                $ hg_pf_DanceForMe_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_DanceForMe_ID])+".png"
                $ hg_pf_LetMeTouchThem_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_LetMeTouchThem_ID])+".png"
                $ hg_pf_TouchMe_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_TouchMe_ID])+".png"
                $ hg_pf_SuckIt_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_SuckIt_ID])+".png"
                $ hg_pf_LetsHaveSex_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_LetsHaveSex_ID])+".png"
                $ hg_pf_TimeForAnal_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_TimeForAnal_ID])+".png"
                $ hg_pf_TheGamble_MH = "interface/heart_0"+str(hg_pf_hearts[hg_pf_TheGamble_ID])+".png"
                
                label not_now2:
                ### LEVEL 01 ###
                menu:
                    "Favour: \"Talk to me\" {image=[hg_pf_TalkToMe_MH]}   {image=interface/clothes.png}":
                        jump hg_pf_TalkToMe

                    "Favour: \"Nice panties\" {image=[hg_pf_NicePanties_MH]}": # LEVEL 1
                        jump hg_pf_NicePanties
                  
                    ### LEVEL 02 ###
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "{color=#858585}Favour: \"Panty thief\" {image=[hg_pf_PantyThief_MH]}{/color}" if imagination >= 2 and not daytime:
                        call cust_excuse("\"Panty thief\" is only available during the daytime only.")
                        jump not_now2
                    "Favour: \"Panty thief\" {image=[hg_pf_PantyThief_MH]}" if imagination >= 2 and daytime:
                        jump hg_pf_PantyThief
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Breast molester\" {image=[hg_pf_BreastMolester_MH]}   {image=interface/clothes.png}" if imagination >= 2: 
                        jump hg_pf_BreastMolester
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination == 1:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Butt molester\" {image=[hg_pf_ButtMolester_MH]}   {image=interface/clothes.png}" if imagination >= 2:
                        jump hg_pf_ButtMolester
                        
                    ### LEVEL 03 ### IMAGINATION == 3
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Show them to me!\" {image=[hg_pf_ShowThemToMe_MH]}   {image=interface/clothes.png}" if imagination >= 3:
                        jump hg_pf_ShowThemToMe
                        
#                    "Favour: \"Show {size=+5}it{/size} to me! (NOT FINISHED YET)":
#                        jump new_request_09
                    
                    ### LEVEL 04 ### IMAGINATION == 3
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Dance for me!\" {image=[hg_pf_DanceForMe_MH]}   {image=interface/clothes.png}" if imagination >= 3:
                        jump hg_pf_DanceForMe
                        
                    "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Let me touch them!\" {image=[hg_pf_LetMeTouchThem_MH]}   {image=interface/clothes.png}" if imagination >= 3: # LEVEL 4
                        jump hg_pf_LetMeTouchThem
                        
                    ### LEVEL 05 ### IMAGINATION == 4
                    "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Favour: \"touch me!\" {image=[hg_pf_TouchMe_MH]}   {image=interface/clothes.png}" if imagination >= 4: # LEVEL 5
                        jump hg_pf_TouchMe
                        
                    ### LEVEL 06 ### IMAGINATION == 4
                    "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Suck it!\" {image=[hg_pf_SuckIt_MH]}   {image=interface/clothes.png}" if imagination >= 4: # LEVEL 6
                        jump hg_pf_SuckIt
                        
                    ### LEVEL 07 ### IMAGINATION == 5
                    "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Favour: \"Let's have sex!\" {image=[hg_pf_LetsHaveSex_MH]}   {image=interface/clothes.png}" if imagination >= 5: # LEVEL 7
                        jump hg_pf_LetsHaveSex
                    
                    ### LEVEL 08 ###
                    "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                        call vague_idea
                        jump not_now2
                    "Favour:  \"Time for anal!\" {image=[hg_pf_TimeForAnal_MH]}   {image=interface/clothes.png}" if imagination >= 5: # LEVEL 8
                        jump hg_pf_TimeForAnal
                    
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
                    
                    $ hg_pr_FlirtClassmate_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_FlirtClassmate_ID])+".png"
                    $ hg_pr_FlirtTeacher_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_FlirtTeacher_ID])+".png"
                    $ hg_pr_ClassmateTouchYou_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_ClassmateTouchYou_ID])+".png"
                    $ hg_pr_FlashClassmate_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_FlashClassmate_ID])+".png"
                    $ hg_pr_KissAGirl_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_KissAGirl_ID])+".png"
                    $ hg_pr_HandjobClassmate_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_HandjobClassmate_ID])+".png"
                    $ hg_pr_BlowjobClassmate_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_BlowjobClassmate_ID])+".png"
                    $ hg_pr_BlowjobTeacher_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_BlowjobTeacher_ID])+".png"
                    $ hg_pr_SexWithClassmate_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_SexWithClassmate_ID])+".png"
                    $ hg_pr_SexWithTeacher_CHK = "interface/check_"+str(hg_pr_complete[hg_pr_SexWithTeacher_ID])+".png"
                    
                    label not_now3:
                    menu:
                        ### LEVEL 01 ### 
                        "Favour: \"She's a flirt\" {image=[hg_pr_FlirtClassmate_CHK]}" if daytime:
                            jump hg_pr_FlirtClassmate
                            
                        ### LEVEL 02 ### IMAGINATION == 2
                        "{color=#858585}-A vague idea-{/color}" if imagination < 2:
                            call vague_idea
                            jump not_now3
                        "Favour: \"She's bait\" {image=[hg_pr_FlirtTeacher_CHK]}" if daytime  and imagination >= 2:
                            jump hg_pr_FlirtTeacher
                        
                        ### LEVEL 03 ### IMAGINATION == 3
                        "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Let a classmate molest you.\" {image=[hg_pr_ClassmateTouchYou_CHK]}" if imagination >= 3: # LEVEL 3
                            jump hg_pr_ClassmateTouchYou
                        
                        ### LEVEL 04 ### IMAGINATION == 3
                        "{color=#858585}-A vague idea-{/color}" if imagination < 3:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Flash your tits to a classmate.\" {image=[hg_pr_FlashClassmate_CHK]}" if imagination >= 3: # LEVEL 4
                            jump hg_pr_FlashClassmate
                        
                        
                        ### LEVEL 05 ### IMAGINATION == 4
                        "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Kiss a girl.\" {image=[hg_pr_KissAGirl_CHK]}" if imagination >= 4: # LEVEL 5
                            jump hg_pr_KissAGirl
                            
                        ### LEVEL 06 ### IMAGINATION == 4
                        "{color=#858585}-A vague idea-{/color}" if imagination < 4:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Give a handjob to a classmate.\" {image=[hg_pr_HandjobClassmate_CHK]}" if imagination >= 4: # LEVEL 6
                            jump hg_pr_HandjobClassmate
                            
                        ### LEVEL 07 ### IMAGINATION == 5
                        "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Give a blowjob to a classmate\" {image=[hg_pr_BlowjobClassmate_CHK]}" if imagination >= 5:# LEVEL 7
                            jump hg_pr_BlowjobClassmate
                                
                         ### LEVEL 08 ### IMAGINATION == 5
                        "{color=#858585}-A vague idea-{/color}" if imagination < 5:
                            call vague_idea
                            jump not_now3
                        "Favour: \"Have sex with a classmate\" {image=[hg_pr_SexWithClassmate_CHK]}" if imagination >= 5:# LEVEL 8
                            jump hg_pr_SexWithClassmate
                        
                        "-Cancel-":
                            jump new_personal_request
            "{color=#858585}-Potions-{/color}" if not daytime:
                call cust_excuse("Potions are available during the daytime only.")
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
            
    else:
        her "The Gryffindors are in the lead. I don't need to do this."
        jump day_time_requests
    
label end_hg_pf_old:
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
    
    
label end_hg_pf:
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
    
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
        $ hermione_takes_classes = True
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
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
    
    if hg_pr_SexWithClassmate_AltFlag:#Hermione does not show up. This sends to label where she shows up next morning.
        call hg_pr_SexWithClassmate_Alt
    
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
    
    
    if hg_pf_PantyThief_InProgressFlag:
        call hg_pf_PantyThief_complete
    if hg_pf_TheGamble_Flag and hg_pf_TheGamble_FlagC or hg_pf_TheGamble_FlagA:
        jump hg_pf_TheGamble_complete
    
    if hg_pr_InProgress[hg_pr_FlirtClassmate_ID]:
        call hg_pr_FlirtClassmate_complete
    if hg_pr_InProgress[hg_pr_FlirtTeacher_ID]:
        call hg_pr_FlirtTeacher_complete
    if hg_pr_InProgress[hg_pr_ClassmateTouchYou_ID]:
        call hg_pr_ClassmateTouchYou_complete
    if hg_pr_InProgress[hg_pr_FlashClassmate_ID]:
        call hg_pr_FlashClassmate_complete
    if hg_pr_InProgress[hg_pr_KissAGirl_ID]:
        call hg_pr_KissAGirl_complete
    if hg_pr_InProgress[hg_pr_HandjobClassmate_ID]:
        call hg_pr_HandjobClassmate_complete
    if hg_pr_InProgress[hg_pr_BlowjobClassmate_ID]:
        call hg_pr_BlowjobClassmate_complete
    if hg_pr_InProgress[hg_pr_BlowjobTeacher_ID]:
        call hg_pr_BlowjobTeacher_complete
    if hg_pr_InProgress[hg_pr_SexWithClassmate_ID]:
        call hg_pr_SexWithClassmate_complete
    if hg_pr_InProgress[hg_pr_SexWithTeacher_ID]:
        call hg_pr_SexWithTeacher_complete
        
    
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
    
    
    
