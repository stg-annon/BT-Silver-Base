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
                #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
                #stop music fadeout 2.0
                
                $ menu_x = 0.2 #Menu is moved to the left side.
                $ h_xpos=410 #Defines position of the Hermione's full length sprite.
                $ h_ypos=0
                
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                show screen bld1
                with d3
                if mad >=1 and mad < 3:
                    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    her ">Looks like Hermione is still a little upset with you..."
                elif mad >=3 and mad < 10:
                    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    ">Hermione is upset with you."
                elif mad >=10 and mad < 20:
                    $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    ">Hermione is very upset with you."
                elif mad >=20 and mad < 40:
                    $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    ">Hermione is mad at you."
                elif mad >=40 and mad < 50:
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    ">Hermione is very mad at you."
                elif mad >=50 and mad < 60:
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    ">Hermione is furious at you."
                elif mad >=60:
                    $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    ">Hermione hates your guts."
                else:
                    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    her "Yes, [genie_name]?"
                
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
                        menu:
                            "-A lollipop candy-([gift_item_inv[1]])" if gift_item_inv[1] >= 1:
                                $ gifted = True 
                                jump giving_candy #28_gifts.rpy
                                
                            "-Chocolate-([gift_item_inv[2]])" if gift_item_inv[2] >= 1:
                                $ gifted = True 
                                jump giving_chocolate #28_gifts.rpy
                            
                            "-Stuffed Owl-([gift_item_inv[3]])" if gift_item_inv[3] >= 1:
                                $ gifted = True 
                                jump giving_owl #28_gifts.rpy
                                
                            "-Butterbeer-([gift_item_inv[4]])" if gift_item_inv[4] >= 1:
                                $ gifted = True 
                                jump giving_beer #28_gifts.rpy
                                
                            "-Educational magazines-([gift_item_inv[5]])" if gift_item_inv[5] >= 1:
                                $ gifted = True 
                                jump giving_mag1 #28_gifts.rpy
                                
                            "-Girly magazines-([gift_item_inv[6]])" if gift_item_inv[6] >= 1:
                                $ gifted = True 
                                jump giving_mag2 #28_gifts.rpy
                                
                            "-Adult magazines-([gift_item_inv[7]])" if gift_item_inv[7] >= 1:
                                $ gifted = True 
                                jump giving_mag3 #28_gifts.rpy
                                
                            "-Porn magazines-([gift_item_inv[8]])" if gift_item_inv[8] >= 1:
                                $ gifted = True 
                                jump giving_mag4 #28_gifts.rpy
                            
                            "-Viktor Krum Poster-([gift_item_inv[9]])" if gift_item_inv[9] >= 1:
                                $ gifted = True 
                                jump giving_krum #28_gifts.rpy
                            
                            "-Sexy lingerie-([gift_item_inv[10]])" if gift_item_inv[10] >= 1:
                                $ gifted = True 
                                jump giving_lingerie #28_gifts.rpy
                            
                            "-A pack of condoms-([gift_item_inv[11]])" if gift_item_inv[11] >= 1:
                                $ gifted = True 
                                jump giving_condoms #28_gifts.rpy
                                
                            "-A jar of anal lubricant-([gift_item_inv[13]])" if gift_item_inv[13] >= 1:
                                $ gifted = True 
                                jump giving_lube #28_gifts.rpy
                            
                            "-A vibrator-([gift_item_inv[12]])" if gift_item_inv[12] >= 1:
                                $ gifted = True 
                                jump giving_vibrator #28_gifts.rpy
                            
                            "-Ball gag and cuffs -([gift_item_inv[14]])" if gift_item_inv[14] >= 1:
                                $ gifted = True 
                                jump giving_ballgag #28_gifts.rpy
                                
                            "-Anal plugs -([gift_item_inv[15]])" if gift_item_inv[15] >= 1:
                                $ gifted = True 
                                jump giving_plug #28_gifts.rpy
                                
                            "- A Thestral strap-on -([gift_item_inv[16]])" if gift_item_inv[16] >= 1:
                                $ gifted = True 
                                jump giving_strapon #28_gifts.rpy
                            
                            "- Lady Speed Stick-2000 -([gift_item_inv[17]])" if gift_item_inv[17] >= 1:
                                $ gifted = True 
                                jump giving_broom #28_gifts.rpy
                                
                            "- Sex doll \"Joanne\" -([gift_item_inv[18]])" if gift_item_inv[18] >= 1:
                                $ gifted = True 
                                jump giving_sexdoll #28_gifts.rpy
                            
                            "-School miniskirt-" if have_miniskirt: # Turns TRUE when you have the skirt in your possession.
                                $ gifted = True
                                jump giving_skirt #28_gifts.rpy
                            
                            "-\"S.P.E.W.\" badge-" if badge_01 == 1:
                                $ gifted = True
                                jump giving_badge_01 #28_gifts.rpy
                            
                            "-Fishnet stockings-" if nets == 1:
                                $ gifted = True
                                jump giving_nets #28_gifts.rpy
                                
                            ##"-Gryffindor Cheerleader Outfit-" if custom_outfit_1_bought == True:
                            ##    $ gifted = True
                            ##    jump giving_gryffindor_cheer #28_gifts.rpy

                            ##"-Slytherin Cheerleader Outfit-" if custom_outfit_2_bought == True:
                            ##    $ gifted = True
                            ##    jump giving_slytherin_cheer #28_gifts.rpy

                            ##"-Maid Outfit-" if custom_outfit_3_bought == True:
                            ##    $ gifted = True
                            ##    jump giving_maid_outfit #28_gifts.rpy

                            ##"-Silk Nightgown-" if custom_outfit_4_bought == True:
                            ##    $ gifted = True
                            ##    jump giving_silk_nightgown #28_gifts.rpy
                                
                            ##"-Jeans-" if cs_existing_stock[0] == True:
                            ##   $ gifted = True
                            ##    jump giving_jeans #28_gifts.rpy
                                
                            ##"-Gryffindor Stockings-" if cs_existing_stock[1] == True:
                            ##    $ gifted = True
                            ##    jump giving_gryffindor_stockings #28_gifts.rpy
                                
                            ##"-Lace Bra and Panties-" if cs_existing_stock[2] == True:
                            ##    $ gifted = True
                            ##    jump giving_lace_bra #28_gifts.rpy
                                
                            ##"-Cup-less Lace Bra-" if cs_existing_stock[3] == True:
                            ##    $ gifted = True
                            ##    jump giving_cupless_bra #28_gifts.rpy
                                
                            ##"-Silk Bra and Panties-" if cs_existing_stock[4] == True:
                            ##    $ gifted = True
                            ##    jump giving_silk_bra #28_gifts.rpy
                                
                            "-The Ball Dress-" if "ball_dress" in outfit_inventory and not gave_the_dress:
                                show screen  blktone
                                with d3
                                m "(I have the feeling that there will be no turning back for me after I give her this dress...)"
                                m "(Am I ready for this?)"
                                hide screen blktone
                                menu:
                                    "\"Yes, I am...\"":
                                        jump giving_thre_dress #27_final_events.rpy
                                    "\"No, not yet...\"":
                                        jump day_time_requests
                                
                              
                                
                            
                            
                            
                            "-Never mind-":
                                jump day_time_requests
                
                    
#                    "-Ending \"Your whore\"-":
#                        jump your_whore
                        
#                    "-Ending \"Public whore\"-":
#                        $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
#                        jump your_whore
                        
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
                        menu:
                            
                            "-Clothing-":
                                menu:
                                
                                    "-Put the fishnets on-" if not ne_01 and nets == 7:
                                        jump nets_put
                            
                                    "-Take the fishnets off-" if ne_01 and nets == 7:
                                        jump nets_take
                                                            
                                    "-Put the jeans on-" if cs_existing_stock[0] and custom_skirt != 1:
                                        jump jeans_on
                            
                                    "-Take the jeans off-" if custom_skirt == 1:
                                        jump jeans_off
                                                            
                                    "-Put the Gryffindor Stockings on-" if cs_existing_stock[0] and stockings != 2:
                                        jump g_stockings_on
                            
                                    "-Take the Gryffindor Stockings off-" if stockings == 2:
                                        jump g_stockings_off
                                                            
                                    "-Put the Lace Bra and Panties on-" if custom_bra != 1:
                                        jump lace_on
                            
                                    "-Take the Lace Bra and Panties off-" if custom_bra == 1:
                                        jump lace_off
                                                                                                             
                                    "-Put the Cup-less Lace Bra on-" if not ne_01 and nets == 7:
                                        jump cupless_on
                            
                                    "-Take the Cup-less Lace Bra off-" if ne_01 and nets == 7:
                                        jump cupless_off
                                                                                                             
                                    "-Put the Silk Bra and Panties on-" if custom_bra != 3:
                                        jump silk_on
                            
                                    "-Take the Silk Bra and Panties off-" if custom_bra == 3:
                                        jump silk_off
                            
                                    "-Don't wear a top-" if wear_shirts:
                                        jump bra_on
                            
                                    "-Put some clothes on-" if not wear_shirts:
                                        jump bra_off
                                    
                                    "-Never mind-":
                                        jump day_time_requests
                                       
                            "-Accessories-":
                                menu:
                                    "-Put the badge on-" if not ba_01 and badge_01 == 7:
                                        jump badge_put
                            
                                    "-Take the badge off-" if ba_01 and badge_01 == 7:
                                        jump badge_take
                                        
                                    "-Put the glasses on-" if not glasses_worn:
                                        jump give_glasses
                            
                                    "-Take the glasses off-" if glasses_worn:
                                        jump take_glasses

                                    "-Put freckles on-" if not freckles:
                                        $ freckles = True
                                        jump day_time_requests
                            
                                    "-Take the freckles off-" if freckles:
                                        $ freckles = False
                                        jump day_time_requests

                                    "-Never mind-":
                                        jump day_time_requests
                                       
                            "-Hair-":
                                menu:
                                    "-Dye your hair brown-" if not hair_color == 0:
                                        jump dye_brown

                                    "-Dye your hair blonde-" if not hair_color == 1:
                                        jump dye_blonde
                            
                                    "-Dye your hair red-" if not hair_color == 2:
                                        jump dye_red
                            
                                    "-Dye your hair black-" if not hair_color == 3:
                                        jump dye_black
                                    
                                    "-Dye your hair blue-" if not hair_color == 4:
                                        jump dye_blue

                                    "-Dye your hair orange-" if not hair_color == 5:
                                        jump dye_orange

                                    "-Wear your hair up-" if not hair_style == "B":
                                        jump hair_up

                                    "-Wear your hair down-" if hair_style == "B":
                                        jump hair_down

                                    "-Never mind-":
                                        jump day_time_requests
                            "-Never mind":
                                jump day_time_requests
                                       
                            ##"-Collars-":
                            ##    menu:
                            ##    
                            ##        "-Take off the collar-" if collar >= 1:
                            ##            $ collar = 0
                            ##            jump day_time_requests
                            ##
                            ##        "-Put on the slave collar-":
                            ##            $ collar = 1
                            ##            jump day_time_requests
                            ##
                            ##        "-Put on the slut collar-":
                            ##            $ collar = 2
                            ##            jump day_time_requests
                            ##
                            ##        "-Put on the whore collar-":
                            ##            $ collar = 3
                            ##            jump day_time_requests
                            ##           
                            ##        
                            ##        "-Never mind-":
                            ##            jump day_time_requests
                                       
                    "-Working-":
                        label working_menu:
                        menu:
                            
                            "-Work as a maid-" if "maid" in outfit_inventory and daytime:
                                jump job_1
                                
                            "{color=#858585}-Work as a maid-{/color}" if not daytime and "maid" in outfit_inventory:
                                "This job is only available during the day."
                                jump day_time_requests
                            
                            "-Work as a cheerleader for Gryffindor-" if daytime and "gryffindor_cheerleader" in outfit_inventory:
                                jump job_3
                            
                            "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                                "This job is only available during the day."
                                jump day_time_requests
                            
                            "-Work as a cheerleader for Slytherin-" if daytime and "slytherin_cheerleader" in outfit_inventory:
                                jump job_4
                            
                            "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                                "This job is only available during the day."
                                jump day_time_requests
                                  
                            "-Never mind-":
                                jump day_time_requests     
                                       
                                       
                              
                        
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
                    
                    
                    
                    "-Dismiss her-":
#                        if daytime:
#                            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
#                        else:
#                            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1
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
                            hide screen hermione_02
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
                            hide screen hermione_02
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
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    her "Ok, from now on I'll call you [genie_name]"
    jump hermione_talk


label genie_change_fail:
    $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
    her "I'm not calling you that!"
    jump hermione_talk

label hermione_change:
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.
    her "Fine, call me whatever you want [genie_name]"
    jump hermione_talk


label hermione_change_fail:
    $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
    her "I'm not letting you call me that!"
    jump hermione_talk
                
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





#############This massage shows when you make a request, and Hermione refuses because she is not slutty enough yet.
label too_much:
    stop music fadeout 2.0
    hide screen hermione_main
    with d3
    $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
    $ h_body = "01_hp/13_hermione_main/body_48.png" #Flashing panties
    show screen hermione_main
    with d3
    her "[genie_name]??!"
    her "How could ask for such a thing!?"
    hide screen hermione_main
    with d3
    $ h_xpos=120 #Defines position of the Hermione's full length sprite. center: 120. Right: 370.
    $ h_body = "01_hp/13_hermione_main/body_34.png" #Flashing panties
    show screen hermione_main
    with d3
    her "I think I better leave."

    hide screen blktone
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    # $ hermione_chibi_xpos = 610 #Near the desk.
    
    call her_walk(400,610,2)
    
    with Dissolve(.3)    
    
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ mad += 7
    
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









