label new_custom_request:
    if slytherin > gryffindor or slytherin == gryffindor:
        $ h_body = "01_hp/13_hermione_main/crstart.png"
        show screen hermione_main
        $ menu_x = 0.2 #Default: 0.5

        $ only_upper_fixer = only_upper
        $ badges_fixer = badges
        $ ne_fixer = ne

        $ only_upper = False
        $ badges = True
        $ ne = False

        label not_now_custom:
        menu:

            ### LEVEL 01 ###

            #sit on my lap
                #level 1: she awkwardly sits on your knees (whoring 0-5)
                #level 2: she sits further back and can feel your boner (whoring 5-15)
                    #she complains (whoring <8)
                    #she grinds a bit (whoring >12)
                #level 3: she sits with her stomach facing you (whoring 15-20)
                    #she jerks you off (whoring >20)

            #masturbate for me
                #level 1: she grinds the corner of your desk (whoring 10)
                #level 2: lies on your desk and performs (whoring 14)
                #level 3: let her use the dildo (whoring 16)

            #tell me about your sexlife (sequel to 'talk to me' favour)
                #level 1: virgin, clumsily talks about how she fantasizes about some boys (whoring 8)
                #level 2: kissing and touching in empty classrooms (whoring 13)
                #level 3: quickies in toilets inbetween classes (whoring 18)

            #let me finger you (ties into 'show me your panties' favour)
                #level 1:
                #level 2:
                #level 3:

            "{color=#858585}--A vague idea-{/color}-" if imagination == 1:
                call vague_idea
                jump not_now_custom
            "{color=#858585}Favour: \"Show her who's in charge\"" if not daytime:
                show screen blktone
                "This custom favour is only available during the day"
                hide screen blktone
                jump not_now_custom
            "Favour: \"Show her who's in charge\" {image=heart_00}" if daytime and not shaming_01 and not shaming_02 and not shaming_03:
                jump shaming
            "Favour: \"Show her who's in charge\" {image=heart_01}" if daytime and shaming_01 and not shaming_02 and not shaming_03:
                jump shaming
            "Favour: \"Show her who's in charge\" {image=heart_02}" if daytime and shaming_02 and not shaming_03:
                jump shaming
            "Favour: \"Show her who's in charge\" {image=heart_03}" if daytime and shaming_03:
                jump shaming

            ### LEVEL 02 ###

            "{color=#858585}--A vague idea-{/color}-" if imagination == 1:
                call vague_idea
                jump not_now_custom
            "Favour: \"Use her as a Dildo Container\" {image=heart_00}" if daytime and not heretic_01 and not heretic_02 and not heretic_03:
                jump heretic
            "Favour: \"Use her as a Dildo Container\" {image=heart_01}" if daytime and heretic_01 and not heretic_02 and not heretic_03:
                jump heretic
            "Favour: \"Use her as a Dildo Container\" {image=heart_02}" if daytime and heretic_02 and not heretic_03:
                jump heretic
            "Favour: \"Use her as a Dildo Container\" {image=heart_03}" if daytime and heretic_03:
                jump heretic

            ### LEVEL 03 ### IMAGINATION == 3


            ### LEVEL 04 ### IMAGINATION == 3


            ### LEVEL 05 ### IMAGINATION == 4


            ### LEVEL 06 ### IMAGINATION == 4


            ### LEVEL 07 ### IMAGINATION == 5
            
            # "{color=#404033}Favour: \"Rubber Cement\"":
                # jump rcement
            
            "-Never mind-":

                $ only_upper = only_upper_fixer
                $ badges = badges_fixer
                $ ne = ne_fixer

                jump new_personal_request

    else:
        her "The Gryffindors are in the lead. I don't need to do this."
        jump day_time_requests




###############################


'custom request variables have been defined'
jump desk

label c_r_night:


### IF-CLAUSES ###

if shaming_busy:
    call shaming_night
if heretic_busy:
    call heretic_night

###############################


jump night_resume

label custom_request_wrapup:

    # $ only_upper = only_upper_fixer
    # $ badges = badges_fixer
    # $ ne = ne_fixer

    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu
