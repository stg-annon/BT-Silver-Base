label door:
    menu:
        "-Examine the door-" if not door_examined:
            $ door_examined = True
            hide screen genie
            $ tt_xpos=550
            $ tt_ypos=110
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "A sturdy looking door..."
            m "I wonder what's behind it."
            label examining_the_door:
            menu:
                "-Knock on the door-":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/knocking.mp3')
                    "*Knock-knock-knock*"
                    "..................."
                    hide screen blktone8
                    with d3
                    m "No reply..."
                    jump examining_the_door
                "-Put your ear on it-":
                    show screen blktone8
                    with d3
                    ">You put your ear on the door and listen intently..."
                    m "I don't hear anything."
                    hide screen blktone8
                    with d3
                    jump examining_the_door
                "-Kick the door-":
                    show screen blktone8
                    with d3
                    $ renpy.play('sounds/kick.ogg')
                    pause.2
                    with hpunch
                    "*Thump!*"
                    ".............................."
                    hide screen blktone8
                    with d3
                    m "This door could take a thousand kicks like that and it still wouldn't break..." 
                    m "It doesn't look like it's locked though..."
                    jump examining_the_door
                "-Leave it alone-":
                    m "Who knows what kind of dangers could be lurking behind that door?"
                    m "I think I'll let it be for now..."
                    pass
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.2)
            jump day_main_menu
        "-Explore the Castle-" if door_examined:
            if cataloug_found:
                hide screen main_menu_01
                call screen map_screen
            else:
                m "I would almost certainly get lost without a map"
                m "Maybe there is one hidden somewhere in this room"
                jump day_main_menu
                
        "{color=#858585}-Summon Hermione-{/color}" if summoning_hermione_unlocked and hermione_takes_classes or hermione_sleeping:
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Hermione is taking classes."
                $ cust_char_1_enabled = True
                $ cust_char_2_enabled = True
                $ cust_char_3_enabled = True
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Hermione is already asleep."
                hide screen bld1
                with d3
                jump night_main_menu
        
        "-Summon Hermione-" if summoning_hermione_unlocked and not hermione_takes_classes and not hermione_sleeping:
            if hermione_takes_classes:
                show screen bld1
                with d3
                ">Hermione is taking classes."
                hide screen bld1
                with d3
                jump day_main_menu
            elif hermione_sleeping:
                show screen bld1
                with d3
                ">Hermione is already asleep."
                hide screen bld1
                with d3
                jump night_main_menu
                
            else:
                call update_her_uniform
                
                #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                #stop music fadeout 2.0
                
                $ menu_x = 0.2 #Menu is moved to the left side.
                
                $ hermione_xpos = 410
                $ hermione_ypos = 0
                
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_blink #Hermione stands still.
                show screen bld1
                with d3
                if mad >=1 and mad < 3:
                    call her_main("","body_03")
                    ">Looks like Hermione is still a little upset with you..."
                elif mad >=3 and mad < 10:
                    call her_main("","body_03")
                    ">Hermione is upset with you."
                elif mad >=10 and mad < 20:
                    call her_main("","body_09")
                    ">Hermione is very upset with you."
                elif mad >=20 and mad < 40:
                    call her_main("","body_05")
                    ">Hermione is mad at you."
                elif mad >=40 and mad < 50:
                    call her_main("","body_47")
                    ">Hermione is very mad at you."
                elif mad >=50 and mad < 60:
                    call her_main("","body_47")
                    ">Hermione is furious at you."
                elif mad >=60:
                    call her_main("","body_47")
                    ">Hermione hates your guts."
                else:
                    call her_main("Yes, [genie_name]?","body_01")
                
                label day_time_requests:
                menu:
                    "-Talk-":
                        label hermione_talk:
                        menu:
                            "-Chit chat-" if not chitchated_with_her:
                                $ chitchated_with_her = True #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
                                if mad <= 7:
                                    jump chit_chat
                                else:
                                    her "I have nothing to say to you sir..."    
                                    jump hermione_talk
                            
                            "-Working-":
                                label working_menu:
                                menu:
                                    "-Work as a maid-" if "maid" in outfit_inventory and daytime:
                                        jump job_1
                                        
                                    "{color=#858585}-Work as a maid-{/color}" if not daytime and "maid" in outfit_inventory:
                                        "This job is only available during the day."
                                        jump working_menu
                                    
                                    "-Work as a cheerleader for Gryffindor-" if daytime and "gryffindor_cheerleader" in outfit_inventory:
                                        jump job_3
                                    
                                    "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                                        "This job is only available during the day."
                                        jump working_menu
                                    
                                    "-Work as a cheerleader for Slytherin-" if daytime and "slytherin_cheerleader" in outfit_inventory:
                                        jump job_4
                                    
                                    "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                                        "This job is only available during the day."
                                        jump working_menu
                                          
                                    "-Never mind-":
                                        jump hermione_talk     
                            
                            "-Address me only as-":
                                menu:
                                    "-Sir-":
                                        $ genie_name = "Sir"
                                        jump genie_change
                                    "-Dumbledore-":
                                        $ genie_name = "Dumbledore"
                                        jump genie_change
                                    "-Professor-":
                                        $ genie_name = "Professor"
                                        jump genie_change
                                    "-Old man-":
                                        $ genie_name = "Old man"
                                        jump genie_change
                                    "-Genie-":
                                        if whoring >=5:
                                            $ genie_name = "Genie"
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-My Lord-":
                                        if whoring >=7:
                                            $ genie_name = "My Lord"
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-Darling-":
                                        if whoring >=10:
                                            $ genie_name = "Darling"
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-Lord Voldemort-":
                                        if whoring >=15:
                                            $ genie_name = "Lord Voldemort"
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-Daddy-":
                                        if whoring >=20:
                                            $ genie_name = "Daddy"
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-Master-":
                                        if whoring >=20:
                                            $ genie_name = "Master"
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-Custom Input-":
                                        $ temp_name = renpy.input("(Please enter the name.)")
                                        $ temp_name = temp_name.strip()
                                        if hermione_name == "":
                                            $ genie_name = "Sir"
                                        if whoring >=20:
                                            $ genie_name = temp_name
                                            jump genie_change
                                        else:
                                            jump genie_change_fail
                                    "-Never mind-":
                                        jump hermione_talk
                            
                            "-From now on I will refer to you as-":
                                menu:
                                    "-Miss Granger-":
                                        $ hermione_name = "Miss Granger"
                                        jump hermione_change
                                    "-Girl-":
                                        $ hermione_name = "Girl"
                                        jump hermione_change
                                    "-Good Girl-":
                                        if whoring >=5:
                                            $ hermione_name = "Good Girl"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Slave-":
                                        if whoring >=10:
                                            $ hermione_name = "Slave"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Princess-":
                                        if whoring >=10:
                                            $ hermione_name = "Princess"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Whore-":
                                        if whoring >=15:
                                            $ hermione_name = "Whore"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Little Girl-":
                                        if whoring >=15:
                                            $ hermione_name = "Little Girl"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Slytherin Slut-":
                                        if whoring >=18:
                                            $ hermione_name = "Slytherin Slut"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Mudblood-":
                                        if whoring >=20:
                                            $ hermione_name = "Mudblood"
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Custom Input-":
                                        $ temp_name = renpy.input("(Please enter the name.)")
                                        $ temp_name = temp_name.strip()
                                        if hermione_name == "":
                                            $ hermione_name = "Miss granger"
                                        if whoring >=20:
                                            $ hermione_name = temp_name
                                            jump hermione_change
                                        else:
                                            jump hermione_change_fail
                                    "-Never mind-":
                                        jump hermione_talk
                            
                            "-Never mind":
                                jump day_time_requests
                    
                    "-Tutoring-" if not daytime:
                        if mad >=1 and mad < 3:
                            her "I'm sorry, maybe tomorrow..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "I am not in the mood today..."
                            jump day_time_requests
                        elif mad >=20:
                            her "After what you did, [genie_name]?"
                            her "I don't think so..."
                            jump day_time_requests
                        else:
                            jump l_tutoring_check
                    
                    "-Buy sexual favours-" if buying_favors_from_hermione_unlocked:
                        if mad >=1 and mad < 3:
                            her "I'm sorry, [genie_name], Maybe some other time..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "I don't feel like it today..."
                            her "Maybe in a couple of days..."
                            jump day_time_requests
                        elif mad >=10 and mad < 20:
                            her "No thank you...."
                            jump day_time_requests
                        elif mad >=20 and mad < 30:
                            her "After what you did, [genie_name]?"
                            her "I don't think so..."
                            jump day_time_requests
                        elif mad >=30 and mad < 40:
                            her "You can't be serious!"
                            jump day_time_requests
                        elif mad >=40:
                            her "Is this some twisted joke to you, sir?!"
                            her "After what you did I don't feel like doing this ever again!"
                            jump day_time_requests
                        else:
                            jump new_personal_request
                    
                    "-Give her a present-" if not gifted:
                        jump her_gift_menu
                    
                    "-Wardrobe-" if dress_code:
                        if mad >=1 and mad < 3:
                            her "I'm sorry, [genie_name]. Maybe some other time..."
                            jump day_time_requests
                        elif mad >=3 and mad < 10:
                            her "What's wrong with my current attire?"
                            jump day_time_requests
                        elif mad >=10 and mad < 20:
                            her "No, thank you...."
                            jump day_time_requests
                        elif mad >=20 and mad < 30:
                            her "I don't think so..."
                            jump day_time_requests
                        elif mad >=30 and mad < 40:
                            her "No!"
                            jump day_time_requests
                        elif mad >=40:
                            her "I will never let you tell me what to wear again, sir!"
                            jump day_time_requests
                        else:
                            pass
                        label day_request_wardrobe:
                        menu:
                            "-Hair-":
                                label day_request_hair:
                                menu:
                                    "-Wear your hair up-" if not h_hair_style == "B":
                                        call her_main("Sure, let me just go change it.","body_01")
                                        call set_h_hair_style("B")
                                        jump day_request_hair
                                        
                                    "-Wear your hair down-" if not h_hair_style == "A":
                                        call her_main("Sure, let me just go change it.","body_01")
                                        call set_h_hair_style("A")
                                        jump day_request_hair
                                        
                                    "-Dye your hair-":
                                        label day_request_hair_dye:
                                        menu:
                                            "-Dye Brown-" if not h_hair_color == 1:
                                                call her_main("Brown seems so boring now.","body_01")
                                                call set_h_hair_color(1)
                                                jump day_request_hair_dye
                                                
                                            "-Dye Blonde-" if not h_hair_color == 2:
                                                call her_main("Why do you want me to change my hair?","body_01")
                                                m "I don't know, I suppose I just have a thing for blondes"
                                                her "well I've always heard blondes have more fun!"
                                                call set_h_hair_color(2)
                                                jump day_request_hair_dye
                                                
                                            "-Dye Red-" if not h_hair_color == 3:
                                                call her_main("this'll be fun, Maybe I'll look like Batwoman!","body_01")
                                                m "You read comics?"
                                                her "no, i just play certain games"
                                                m "What?"
                                                call set_h_hair_color(3)
                                                jump day_request_hair_dye
                                                
                                            "-Dye Black-" if not h_hair_color == 4:
                                                call her_main("I have been feeling a bit depressed recently.","body_01")
                                                her "I wonder if it's because of all the favors I've been doing"
                                                m "Don't worry about it"
                                                call set_h_hair_color(4)
                                                jump day_request_hair_dye
                                                
                                            "-Dye Blue-" if not h_hair_color == 5:
                                                call her_main("Blue?","body_01")
                                                m "Why not?"
                                                her "Just seems a bit attention seeking..."
                                                call set_h_hair_color(5)
                                                jump day_request_hair_dye
                                                
                                            "-Dye Orange-" if not h_hair_color == 6:
                                                call her_main("Orange?","body_01")
                                                m "That's what I said."
                                                her "Alright, well just let me change it."
                                                call set_h_hair_color(6)
                                                jump day_request_hair_dye
                                                
                                            "-Never mind-":
                                                jump day_request_hair
                                        
                                    "-Never mind-":
                                        jump day_request_wardrobe
                            
                            "-Clothing-":
                                label day_request_clothing:
                                menu:
                                    "-Don't wear a top-" if hermione_wear_top:
                                        call h_top_off
                                        jump day_request_clothing
                                        
                                    "-Put top back on-" if not hermione_wear_top:
                                        call h_top_on
                                        jump day_request_clothing
                                        
                                    "-Don't wear a skirt-" if hermione_wear_skirt:
                                        call h_skirt_off
                                        jump day_request_clothing
                                        
                                    "-Put skirt back on-" if not hermione_wear_skirt:
                                        call h_skirt_on
                                        jump day_request_clothing
                                        
                                    "-Stop wearing panties-" if h_request_wear_panties and whoring >= 6:
                                        call h_panties_off
                                        jump day_request_clothing
                                        
                                    "-Wear panties-" if not h_request_wear_panties and whoring >= 6:
                                        call h_panties_on
                                        jump day_request_clothing
                                        
                                    "-Stockings-":
                                        label day_request_clothing_stockings:
                                        menu:
                                            "-Put the fishnets on-" if "fishnet_stockings" in cs_existing_stock and h_stocking != "fishnet_a":
                                                call set_h_stockings("fishnet_a")
                                                jump day_request_clothing_stockings
                                                
                                            "-Take the fishnets off-" if "fishnet_stockings" in cs_existing_stock and h_stocking == "fishnet_a":
                                                call set_h_stockings
                                                jump day_request_clothing_stockings
                                                
                                            "-Put the Gryffindor Stockings on-" if "gryffindor_stockings" in cs_existing_stock and h_stocking != "gryff":
                                                jump equip_gryyf_stockings
                                                jump day_request_clothing_stockings
                                                
                                            "-Take the Gryffindor Stockings off-" if "gryffindor_stockings" in cs_existing_stock and h_stocking == "gryff":
                                                call set_h_stockings
                                                jump day_request_clothing_stockings
                                                
                                            "-Never mind-":
                                                jump day_request_clothing
                                        
                                    "-Underwear-":
                                        label day_request_clothing_underwear:
                                        menu:
                                            "-Put the Lace Bra and Panties on-" if "lace_set" in cs_existing_stock and h_bra != "lace_bra":
                                                call set_h_underwear("lace_bra","lace_panties")
                                                jump day_request_clothing_underwear
                                                
                                            "-Take the Lace Bra and Panties off-" if "lace_set" in cs_existing_stock and h_bra == "lace_bra":
                                                call set_h_underwear("base_bra_white_1","base_panties_1")
                                                jump day_request_clothing_underwear
                                                
                                            "-Put the Cup-less Lace Bra on-" if "cup_set" in cs_existing_stock and h_bra != "cup_bra":
                                                call set_h_underwear("cup_bra","cup_panties")
                                                jump day_request_clothing_underwear
                                                
                                            "-Take the Cup-less Lace Bra off-" if "cup_set" in cs_existing_stock and h_bra == "cup_bra":
                                                call set_h_underwear("base_bra_white_1","base_panties_1")
                                                jump day_request_clothing_underwear
                                                
                                            "-Put the Silk Bra and Panties on-" if "silk_set" in cs_existing_stock and h_bra != "silk_bra":
                                                call set_h_underwear("silk_bra","silk_panties")
                                                jump day_request_clothing_underwear
                                                
                                            "-Take the Silk Bra and Panties off-" if "silk_set" in cs_existing_stock and h_bra == "silk_bra":
                                                call set_h_underwear("base_bra_white_1","base_panties_1")
                                                jump day_request_clothing_underwear
                                                
                                            "-Put the Latex and Panties on-" if "latex_set" in cs_existing_stock and h_bra != "latex_bra":
                                                call set_h_underwear("latex_bra","latex_panties")
                                                jump day_request_clothing_underwear
                                                
                                            "-Take the Latex and Panties off-" if "latex_set" in cs_existing_stock and h_bra == "latex_bra":
                                                call set_h_underwear("base_bra_white_1","base_panties_1")
                                                jump day_request_clothing_underwear
                                            
                                            "-Never mind-":
                                                jump day_request_clothing
                                        
                                    "-Put the jeans on-" if "jeans_long" in cs_existing_stock and h_skirt != "jeans_long":
                                         jump equip_jeans
                                        
                                    "-Take the jeans off-" if h_skirt == "jeans_long":
                                         call set_h_skirt("base_skirt")
                                         jump day_request_clothing
                                        
                                    "-Put the short jeans on-" if "short_jeans" in cs_existing_stock and h_skirt != "jeansshort":
                                         call set_h_skirt("jeansshort")
                                         jump day_request_clothing
                                        
                                    "-Take the short jeans off-"if h_skirt == "jeansshort":
                                         call set_h_skirt("base_skirt")
                                         jump day_request_clothing
                                        
                                    "-Never mind-":
                                        jump day_request_wardrobe
                            
                            "-Accessories-":
                                label day_request_accessories:
                                menu:
                                    "-Put \"S.P.E.W.\" badge on-" if "SPEW_badge" in cs_existing_stock and h_badge != "SPEW_badge":
                                        call h_badge_on("SPEW_badge")
                                        jump day_request_accessories
                                        
                                    "-Take \"S.P.E.W.\" badge off-" if "SPEW_badge" in cs_existing_stock and h_badge == "SPEW_badge":
                                        call h_badge_off
                                        jump day_request_accessories
                                        
                                    "-Put I <3 C.U.M.\" badge on-" if "CUM_badge" in cs_existing_stock and h_badge != "CUM_badge":
                                        call h_badge_on("CUM_badge")
                                        jump day_request_accessories
                                        
                                    "-Take I <3 C.U.M.\" badge off-" if "CUM_badge" in cs_existing_stock and h_badge == "CUM_badge":
                                        call h_badge_off
                                        jump day_request_accessories
                                        
                                    "-Never mind-":
                                        jump day_request_wardrobe
                            
                            "-Collars-" if False:
                                label day_request_collars:
                                menu:
                                    "-Take off the collar-" if collar >= 1:
                                        $ collar = 0
                                        jump day_request_collars
                                    "-Put on the slave collar-":
                                        $ collar = 1
                                        jump day_request_collars
                                    "-Put on the slut collar-":
                                        $ collar = 2
                                        jump day_request_collars
                                    "-Put on the whore collar-":
                                        $ collar = 3
                                        jump day_request_collars
                                    "-Never mind-":
                                        jump day_request_wardrobe
                                        
                            "-Overlays-":
                                label day_request_overlays:
                                menu:
                                
                                    "{color=#858585}-Thigh Grool Locked-{/color}" if dribble_equippable == False:
                                        "You should try equipping the Gryffindor Stockings between 3 and 6 whoring"
                                        jump day_request_overlays
                                    
                                    "{color=#858585}-Damp Panties Locked-{/color}" if wetpanties_equippable == False:
                                        "You should try equipping the Gryffindor Stockings between 3 and 6 whoring"
                                        jump day_request_overlays
                                    
                                    "-Thigh Grool On-" if dribble_equippable == True and hermione_dribble == False:
                                        $ hermione_dribble = True
                                        call update_her_uniform
                                        jump day_request_overlays
                                    "-Thigh Grool Off-" if dribble_equippable == True and hermione_dribble == True:
                                        $ hermione_dribble = False
                                        call update_her_uniform
                                        jump day_request_overlays
                                    
                                    "-Damp Panties On-" if wetpanties_equippable == True and hermione_wetpanties == False:
                                        $ hermione_wetpanties = True
                                        call update_her_uniform
                                        jump day_request_overlays
                                        
                                    "-Damp Panties Off-" if wetpanties_equippable == True and hermione_wetpanties == True:
                                        $ hermione_wetpanties = False
                                        call update_her_uniform
                                        jump day_request_overlays  
                                        
                                    "-Never mind":
                                        jump day_time_requests
                                    
                            "-Never mind":
                                jump day_time_requests
                    
#                    "-Ending \"Your whore\"-":
#                        jump your_whore
#                        
#                    "-Ending \"Public whore\"-":
#                        $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
#                        jump your_whore
                    
                    "-Dismiss her-":
                        $ menu_x = 0.5 #Menu position is back to default. (Center).
                        if daytime:
                            $ hermione_takes_classes = True
                            if mad >=3 and mad <= 6:
                                her "..............................."
                            elif mad >=7:
                                her "*Humph!*..."
                            else:
                                her "Oh, alright. I will go to classes then."
                            hide screen bld1
                            hide screen hermione_main
                            hide screen blktone 
                            hide screen hermione_blink
                            hide screen ctc
                            with d3
                            jump day_main_menu
                        else:
                            if mad >=3 and mad <= 6:
                                her "..............................."
                            elif mad >=7:
                                her "Tch..."
                            else:
                                her "Oh, alright. I will go to bed then."
                            hide screen bld1
                            hide screen hermione_main
                            hide screen blktone 
                            hide screen hermione_blink
                            hide screen ctc
                            with d3
                            $ hermione_sleeping = True
                            jump night_main_menu
                            
        "{color=#858585}-Summon Snape-{/color}" if hanging_with_snape and snape_busy:
            ">Professor Snape is unavailable."
            if daytime:
                jump day_main_menu
            else: 
                jump night_main_menu
            
        "-Summon Snape-" if hanging_with_snape and not snape_busy:
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
            jump summon_snape
        "-Never mind-":
            jump day_main_menu
    
label genie_change:
    call her_main("Ok, from now on I'll call you [genie_name]","body_01")
    jump hermione_talk
    
label genie_change_fail:
    call her_main("I'm not calling you that!","body_30")
    jump hermione_talk
    
label hermione_change:
    call her_main("Fine, call me whatever you want [genie_name]","body_01")
    jump hermione_talk
    
label hermione_change_fail:
    call her_main("I'm not letting you call me that!","body_30")
    jump hermione_talk
    


