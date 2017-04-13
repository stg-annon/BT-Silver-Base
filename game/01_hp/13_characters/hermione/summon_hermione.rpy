
label summon_hermione:
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
        
        $ hermione_xpos = 550
        $ hermione_ypos = 0
        
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ hermione_SC.chibi.xpos = 540 #Near the desk.
        show screen hermione_blink #Hermione stands still.
        show screen bld1
        with d3
        if mad >=1 and mad < 3:
            $ her_SC.say("","body_03")
            ">Looks like Hermione is still a little upset with you..."
        elif mad >=3 and mad < 10:
            $ her_SC.say("","body_03")
            ">Hermione is upset with you."
        elif mad >=10 and mad < 20:
            $ her_SC.say("","body_09")
            ">Hermione is very upset with you."
        elif mad >=20 and mad < 40:
            $ her_SC.say("","body_05")
            ">Hermione is mad at you."
        elif mad >=40 and mad < 50:
            $ her_SC.say("","body_47")
            ">Hermione is very mad at you."
        elif mad >=50 and mad < 60:
            $ her_SC.say("","body_47")
            ">Hermione is furious at you."
        elif mad >=60:
            $ her_SC.say("","body_47")
            ">Hermione hates your guts."
        else:
            $ her_SC.say("Yes, [genie_name]?","body_01")
        
        label day_time_requests:
        menu:
            "-Talk-":
                label hermione_talk:
                menu:
                    "-Chit chat-" if not chitchated_with_her:
                        $ chitchated_with_her = True #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
                        if mad <= 7:
                            jump hermione_chit_chat
                        else:
                            her "I have nothing to say to you sir..."    
                            jump hermione_talk
                    
                    "-Working-":
                        label working_menu:
                        menu:
                            "-Work as a maid-" if daytime and hermione_outfits_list.purchased("maid"):
                                jump job_1

                            "-Work as a maid-" if daytime and not hermione_outfits_list.purchased("maid"):
                                m "(I'll need an outfit for hermione if I want her to work.)"
                                jump working_menu
                                
                            "{color=#858585}-Work as a maid-{/color}" if not daytime:
                                "This job is only available during the day."
                                jump working_menu
                            
                            "-Work as a cheerleader for Gryffindor-" if daytime and hermione_outfits_list.purchased("griffindor_cheerleader"):
                                jump job_3

                            "-Work as a cheerleader for Gryffindor-" if daytime and not hermione_outfits_list.purchased("griffindor_cheerleader"):
                                m "(I'll need an outfit for hermione if I want her to work.)"
                                jump working_menu
                            
                            "{color=#858585}-Work as a cheerleader for Gryffindor-{/color}" if not daytime:
                                "This job is only available during the day."
                                jump working_menu
                            
                            "-Work as a cheerleader for Slytherin-" if daytime and hermione_outfits_list.purchased("slythrin_cheerleader"):
                                jump job_4

                            "-Work as a cheerleader for Slytherin-" if daytime and not hermione_outfits_list.purchased("slythrin_cheerleader"):
                                m "(I'll need an outfit for hermione if I want her to work.)"
                                jump working_menu
                            
                            "{color=#858585}-Work as a cheerleader for Slytherin-{/color}" if not daytime:
                                "This job is only available during the day."
                                jump working_menu
                                  
                            "-Never mind-":
                                jump hermione_talk     
                    
                    "-Address me only as-":
                        menu:
                            "-Sir-":
                                call genie_change("Sir")
                            "-Dumbledore-":
                                call genie_change("Dumbledore")
                            "-Professor-":
                                call genie_change("Professor")
                            "-Old man-":
                                call genie_change("Old man")
                            "-Genie-":
                                call genie_change("Genie",5)
                            "-My Lord-":
                                call genie_change("My Lord",7)
                            "-Darling-":
                                call genie_change("Darling",10)
                            "-Lord Voldemort-":
                                call genie_change("Lord Voldemort",15)
                            "-Daddy-":
                                call genie_change("Daddy",20)
                            "-Master-":
                                call genie_change("Master",20)
                            "-Custom Input-":
                                call genie_change(renpy.input("(Please enter the name.)").strip(),20)
                            "-Never mind-":
                                pass
                        jump hermione_talk
                    
                    "-From now on I will refer to you as-":
                        menu:
                            "-Miss Granger-":
                                call hermione_change("Miss Granger")
                            "-Girl-":
                                call hermione_change("Girl")
                            "-Good Girl-":
                                call hermione_change("Good Girl",5)
                            "-Slave-":
                                call hermione_change("Slave",10)
                            "-Princess-":
                                call hermione_change("Princess",10)
                            "-Whore-":
                                call hermione_change("Whore",15)
                            "-Little Girl-":
                                call hermione_change("Little Girl",15)
                            "-Slytherin Slut-":
                                call hermione_change("Slytherin Slut",18)
                            "-Mudblood-":
                                call hermione_change("Mudblood",20)
                            "-Custom Input-":
                                call hermione_change(renpy.input("(Please enter the name.)").strip(),20)
                            "-Never mind-":
                                pass
                        jump hermione_talk
                    
                    "-Never mind":
                        jump day_time_requests
            
            "-Tutoring-" if not daytime:
                if mad >=1 and mad < 3:
                    $ her_SC.say("I'm sorry, maybe tomorrow...")
                    jump day_time_requests
                elif mad >=3 and mad < 10:
                    $ her_SC.say("I am not in the mood today...")
                    jump day_time_requests
                    # Question: What to do between 9 and 20? Only "jump l_tutoring_check"?
                elif mad >=20:
                    $ her_SC.say("After what you did, [genie_name]?")
                    $ her_SC.say("I don't think so...")
                    jump day_time_requests
                else:
                    jump l_tutoring_check
            
            "-Buy sexual favours-" if buying_favors_from_hermione_unlocked:
                if mad >=1 and mad < 3:
                    $ her_SC.say("I'm sorry, [genie_name], Maybe some other time...")
                    jump day_time_requests
                elif mad >=  3 and mad < 10:
                    $ her_SC.say("I don't feel like it today...")
                    $ her_SC.say("Maybe in a couple of days...")
                    jump day_time_requests
                elif mad >= 10 and mad < 20:
                    $ her_SC.say("No thank you....")
                    jump day_time_requests
                elif mad >= 20 and mad < 30:
                    $ her_SC.say("After what you did, [genie_name]?")
                    $ her_SC.say("I don't think so...")
                    jump day_time_requests
                elif mad >= 30 and mad < 40:
                    $ her_SC.say("You can't be serious!")
                    jump day_time_requests
                elif mad >= 40:
                    $ her_SC.say("Is this some twisted joke to you, sir?!")
                    $ her_SC.say("After what you did I don't feel like doing this ever again!")
                    jump day_time_requests
                else:
                    jump silver_requests
            
            "-Inventory-":
                $ her_SC.say("",xpos=410)
                call screen wardrobe

                
           # "-Ending \"Your whore\"-":
                # jump your_whore
                
            # "-Ending \"Public whore\"-":
                # $ public_whore_ending = True #If TRUE the game will end with "Public Whore Ending".
                # jump your_whore
            
            "-Dismiss her-":
                $ menu_x = 0.5 #Menu position is back to default. (Center).
                if daytime:
                    $ hermione_takes_classes = True
                    if mad >=3 and mad < 7:
                        $ her_SC.say("...............................")
                    elif mad >=7:
                        $ her_SC.say("*Humph!*...")
                    else:
                        $ her_SC.say("Oh, alright. I will go to classes then.")
                    hide screen bld1
                    hide screen hermione_main
                    hide screen blktone 
                    hide screen hermione_blink
                    hide screen ctc
                    with d3
                    jump day_main_menu
                else:
                    if mad >=3 and mad < 7:
                        $ her_SC.say("...............................")
                    elif mad >=7:
                        $ her_SC.say("Tch...")
                    else:
                        $ her_SC.say("Oh, alright. I will go to bed then.")
                    hide screen bld1
                    hide screen hermione_main
                    hide screen blktone 
                    hide screen hermione_blink
                    hide screen ctc
                    with d3
                    $ hermione_sleeping = True
                    jump night_main_menu
        

label hermione_chit_chat:
    $ one_of_ten = renpy.random.randint(1, 10) #Generating random int from 1-10
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            $ her_SC.say("Maybe, if I'd work harder, I could squeeze a few more classes into my schedule...",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 2:
            $ her_SC.say("Actually I don't mind it to be called a \"know-it-all\".",4)
            $ her_SC.say("I think it's rather flattering...")
            $ her_SC.setFace(3)
        elif one_of_ten == 3:
            $ her_SC.say("The basilisk, also known as the king of serpents.",4)
            $ her_SC.say("Herpo the Foul was the first to breed a Basilisk.")
            $ her_SC.say("He accomplished that by--")
            $ her_SC.say("Oh, I'm sorry, professor, we have another test tomorrow...",10)
            $ her_SC.say("I Just want to make sure that I'm ready...")
            $ her_SC.setFace(1)
        elif one_of_ten == 4:
            $ her_SC.say("If my body wouldn't require sleep...",10)
            $ her_SC.say("I would be able to spend twice as much time with studying!?",18)
            $ her_SC.say("I wonder if there's a spell for that...",14)
            $ her_SC.setFace(3)
        elif one_of_ten == 5:
            $ her_SC.say("So far professor Trelawney did not taught me a single piece of any actual knowledge, sir.",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 6:
            $ her_SC.say("If only more students were honest, responsible and diligent like me.",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 7:
            $ her_SC.say("Personally, I think that every single one of us should work harder to make our world a better place.")
            $ her_SC.say("How can some people be so ignorant to the world's problems?",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 8:
            $ her_SC.say("It's been raining quite a lot lately...",10)
            $ her_SC.setFace(1)
        elif one_of_ten == 9:
            $ her_SC.say("Very few people know this...",10)
            $ her_SC.say("...But I really like chocolate.",6)
            $ her_SC.setFace(1)
        elif one_of_ten == 10:
            $ her_SC.say("I am sorry sir, but I don't really have time for idle chat chats...",6)
            $ her_SC.setFace(3)
    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            $ her_SC.say("I read somewhere that a full moon often makes it easier to concentrate at a task at hand...",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 2:
            $ her_SC.say("I love nothing more than to curl up by a fireplace during a rainstorm with a good book...",6)
            $ her_SC.setFace(1)
        elif one_of_ten == 3:
            $ her_SC.say("A peculiar rumour concerning professor Snape has been circulating in the school lately...",10)
            $ her_SC.say("No, I probably shouldn't...",15)
            $ her_SC.setFace(3)
        elif one_of_ten == 4:
            $ her_SC.say("Despite the questionable nature of the favours you have been buying from me lately, sir...",4)
            $ her_SC.say("I am grateful to you for your help...")
            $ her_SC.say("Gryffindor needs those points now more than ever...",9)
            $ her_SC.setFace(3)
        elif one_of_ten == 5:
            $ her_SC.say("Why Quidditch is so popular among the girls is simply beyond me...",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 6:
            $ her_SC.say("The \"Men's Rights Movement\" is steadily gaining popularity.",4)
            $ her_SC.say("It's very fulfilling to know that you are helping to improve our society.")
            $ her_SC.setFace(3)
        elif one_of_ten == 7:
            $ her_SC.say("The Hogwarts school library is considered to be quite extensive...",4)
            $ her_SC.say("Still, I can't help but wish that it'd be bigger...",8)
            $ her_SC.setFace(3)
        elif one_of_ten == 8:
            $ her_SC.say("As one of the top students in this school I have a reputation to keep...",10)
            $ her_SC.say("People look up to me...")
            $ her_SC.say("...So, your discretion is very appreciated, sir.",31)
            $ her_SC.setFace(29)
        elif one_of_ten == 9:
            $ her_SC.say("That favour I sold you the other say, sir...",11)
            $ her_SC.say(".......",33)
            $ her_SC.say("I only agreed to it because the needs of my house always come first.",87)
            $ her_SC.say("I just wanted you to know that, sir...",120)
        elif one_of_ten == 10:
            $ her_SC.say("The \"Autumn Ball\" is still several months away...",4)
            $ her_SC.say("But some girls are already discussing what kind of dress they are going to wear...",11)
            $ her_SC.setFace(185)
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            $ her_SC.say("Do you remember when you asked me to show you my panties for the first time sir?",4)
            $ her_SC.say("I was so furious with you then...")
            $ her_SC.say("Now I see that I was just being selfish...",9)
            $ her_SC.say("After all, the honour of my house is at stake here...")
            $ her_SC.say("And that shall be my one and only concern!",7)
        elif one_of_ten == 2:
            $ her_SC.say("The rate at which the Slytherin house has been gaining points lately is simply ridiculous.",4)
            $ her_SC.say("I think professor Snape might be behind it.",5)
            $ her_SC.say("You should look into this, sir.",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 3:
            $ her_SC.say("Ashwinder eggs, rose thorns, moonstone...",10)
            $ her_SC.say("Huh? Am I thinking out loud again?",11)
            $ her_SC.say("I apologize...",24)
            $ her_SC.say("It's just that we have another test soon...",13)
        elif one_of_ten == 4:
            $ her_SC.say("I dislike the entire house of Slytherin with all my heart, sir.",77)
        elif one_of_ten == 5:
            $ her_SC.say("Hogwarts has really become a second home to me lately...",16)
            $ her_SC.say("I don't even miss my parents nearly as much anymore...",71)
            $ her_SC.say("Come to think of it I don't miss them at all...",18)
            $ her_SC.say("I'm an awful daughter...",118)
        elif one_of_ten == 6:
            $ her_SC.say("*Yawn!* I read about this technique that supposedly allows you to cut your sleep time in half...",70)
            $ her_SC.say("It don't think it's working though.... *Yawn!*",73)
        elif one_of_ten == 7:
            $ her_SC.say("Even after I graduate from Hogwarts I plan to keep on working hard.",4)
            $ her_SC.say("If I give it my all I can make this world a better place, I know it!",2)
            $ her_SC.setFace(3)
        elif one_of_ten == 8:
            $ her_SC.say("Somehow I have the feeling that this year will become a pivotal turning point in my life...",11)
            $ her_SC.setFace(13)
        elif one_of_ten == 9:
            $ her_SC.say("Some of the less traveled school corridors are not very well lit and rather dusty...",4)
            $ her_SC.say("Please take care of this, sir...")
            $ her_SC.setFace(3)
        elif one_of_ten == 10:
            $ her_SC.say("I've read about this thing called \"Time-Turner\".",14)
            $ her_SC.say("It allows the user to control the flow of time...")
            $ her_SC.say("Having a device like that would do wonders for my schedule...",16)
            $ her_SC.setFace(17)
    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            $ her_SC.say("My \"men's rights movement\" has been losing its popularity lately...",11)
            $ her_SC.say("It's as if people don't even care!",12)
        elif one_of_ten == 2:
            $ her_SC.say("Thank you for buying all those favours from me, sir.",4)
            $ her_SC.say("Some of them were borderline inappropriate, sure...",7)
            $ her_SC.say("But I don't mind sacrificing my dignity if it will allow Gryffindor to compete with Slytherin on equal ground.",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 3:
            $ her_SC.say("Quidditch is stupid!",77)
            $ her_SC.say("There. I said it.",17)
        elif one_of_ten == 4:
            $ her_SC.say("Sir, there is something about professor Snape that I think you should know...",2)
            $ her_SC.say(".................",10)
            $ her_SC.say(".........................",9)
            $ her_SC.say("uhm... Never mind...",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 5:
            $ her_SC.say("Some of the Slytherin girls sell sexual favours almost openly these days...",4)
            $ her_SC.say("You need to put an end to such practices, sir.",2)
            $ her_SC.say("(I can barely keep up...)",69)
        elif one_of_ten == 6:
            $ her_SC.say("Life works in mysterious ways...",10)
            $ her_SC.say("Wouldn't you agree, sir?",8)
            $ her_SC.setFace(13)
        elif one_of_ten == 7:
            $ her_SC.say("Slytherins...",76)
            $ her_SC.setFace(77)
        elif one_of_ten == 8:
            $ her_SC.say("I've been spending so much time in your office lately, sir...",10)
            $ her_SC.say("If I'm not careful some people may think that I have become your pet...",11)
            $ her_SC.say("I meant to say the teacher's pet...",34)
            $ her_SC.setFace(33)
        elif one_of_ten == 9:
            $ her_SC.say("My favourite colours?",2)
            $ her_SC.say("scarlet and gold of course!",2)
            $ her_SC.setFace(3)
        elif one_of_ten == 10:
            $ her_SC.say("Is it weird that my best friends are boys?",10)
            $ her_SC.setFace(1)
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            $ her_SC.say("Sir, with all due respect...",7)
            $ her_SC.say("Professor Snape's debauchery is getting out of hand!")
            $ her_SC.say("You must do something, sir.",11)
            $ her_SC.setFace(3)
        elif one_of_ten == 2:
            $ her_SC.say("I am willing to go to great lengths to insure the superiority of my house...",4)
            $ her_SC.say("But that does not mean that I take pleasure in selling myself out to you in exchange for house points, sir.")
            $ her_SC.say("{size=-4}(Like some sort of prostitute-witch...){/size}",118)
        elif one_of_ten == 3:
            $ her_SC.say("What will it be today, sir?",79)
        elif one_of_ten == 4:
            $ her_SC.say("lately I have not been studying nearly as much as I used to...",11)
            $ her_SC.say("Am I losing my motivation?",10)
            $ her_SC.setFace(13)
        elif one_of_ten == 5:
            $ her_SC.say("My least favourite subject?",8)
            $ her_SC.say("Divination.",9)
        elif one_of_ten == 6:
            $ her_SC.say("My father used to say: \"Magic is just science we don't understand yet\".",14)
            $ her_SC.say("He could't be more wrong of course...",10)
            $ her_SC.setFace(13)
        elif one_of_ten == 7:
            $ her_SC.say("Despite everything...",4)
            $ her_SC.say("I am thankful that you keep on buying favours from me, sir...",10)
            $ her_SC.setFace(13)
        elif one_of_ten == 8:
            $ her_SC.say("It's quite cold outside today, isn't it?",14)
            $ her_SC.setFace(15)
        elif one_of_ten == 9:
            $ her_SC.say("The \"Autumn Ball\" will be soon...",14)
            $ her_SC.setFace(15)
        elif one_of_ten == 10:
            $ her_SC.say("People hardly show up for my \"men's rights movement\" meetings at all anymore...",10)
            $ her_SC.setFace(13)
    if whoring >= 15 and whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            $ her_SC.say("Would you like me to show you my breasts today, sir?",87)
            $ her_SC.say("Yes... I would willingly expose myself to you, professor...",78)
            $ her_SC.say("That's how selfless I am!",79)
        elif one_of_ten == 2:
            $ her_SC.say("I can't help but feel bad for the house elves who do my laundry...",14)
            $ her_SC.say("I mean, all those dreadful semen stains...",87)
            $ her_SC.setFace(118)
        elif one_of_ten == 3:
            $ her_SC.say("it Doesn't matter how many times you ask me this, sir...",2)
            $ her_SC.say("The answer shall remain the same...")
            $ her_SC.say("I have nothing but resentment for the \"Slytherins\"!",47)
            $ her_SC.setFace(69)
        elif one_of_ten == 4:
            $ her_SC.say("When I think about all the favours I sold you over these last months, sir...",2)
            $ her_SC.say("Although I do feel a little bit embarrassed...",87)
            $ her_SC.say("I also feel very proud of myself.",120)
        elif one_of_ten == 5:
            $ her_SC.say("I still dedicate a lot of my time to studying...",14)
            $ her_SC.say("But not nearly as much of it as I used to...")
            $ her_SC.say("Somehow I just don't enjoy studying at all anymore...",11)
            $ her_SC.setFace(13)
        elif one_of_ten == 6:
            $ her_SC.say("Gryffindor shall get the house cup this year!",4)
            $ her_SC.say("{size=-4}(Even if it should cost me my dignity...){/size}",118)
            $ her_SC.setFace(120)
        elif one_of_ten == 7:
            $ her_SC.say("I don't mind the autumn weather...",14)
            $ her_SC.say("But my favourite season is winter.",16)
            $ her_SC.setFace(15)
        elif one_of_ten == 8:
            $ her_SC.say("I used to look down on girls who spend too much time with worrying about the way they look...",14)
            $ her_SC.say("But I was wrong to do so...")
            $ her_SC.say("I am starting to understand how important it really is for a girl to look pretty.")
            $ her_SC.say("...............",29)
            $ her_SC.say("I've been on a diet lately...",122)
            $ her_SC.setFace(34)
            $ her_SC.setFace(33)
        elif one_of_ten == 9:
            $ her_SC.say("Lately I've been feeling rather confident around the boys...",14)
            $ her_SC.say("I think I have you to thank for that, sir.",6)
        elif one_of_ten == 10:
            $ her_SC.say("My favourite subject?",14)
            $ her_SC.say("Hm...",13)
            $ her_SC.say("I suppose that would be \"charms\"...",14)
            $ her_SC.setFace(15)
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            $ her_SC.say("Just let me know what will be required of me today, sir.",4)
            $ her_SC.setFace(3)
        elif one_of_ten == 2:
            $ her_SC.say("I barely study at all anymore...",11)
            $ her_SC.say("Despite that my popularity among the other students seems to be growing...")
            $ her_SC.say("Hm...",13)
        elif one_of_ten == 3:
            $ her_SC.say("I wouldn't say \"no\" to a bottle of butterbeer right about now...",64)
            $ her_SC.setFace(68)
        elif one_of_ten == 4:
            $ her_SC.say("What is it sir? Do you have another present for me?",6)
            $ her_SC.say("Oh... I see...",12)
        elif one_of_ten == 5:
            $ her_SC.say("I am doing well, thank you for asking.",6)
        elif one_of_ten == 6:
            $ her_SC.say("Do I look fat to you sir?",11)
            $ her_SC.say("I wonder if the diet is working...",29)
        elif one_of_ten == 7:
            $ her_SC.say("I remember that I used to say that books were my friends...",16)
            $ her_SC.say("Now that sounds so lame.",24)
            $ her_SC.setFace(15)
        elif one_of_ten == 8:
            $ her_SC.say("Add ashwinder egg to cauldron...",4)
            $ her_SC.say("Then add horseshoe reddish and heat...")
            $ her_SC.say("Then juice a squill bulb...")
            $ her_SC.say("Or was it a dash of thyme first?",10)
            $ her_SC.say("..............",13)
            $ her_SC.say("Oh, who cares?",24)
            $ her_SC.setFace(6)
        elif one_of_ten == 9:
            $ her_SC.say("Do You think I am wearing enough makeup, sir?",14)
            $ her_SC.say("Wearing too much would look vulgar...")
            $ her_SC.say("But wearing too little would make me look plain...",13)
            $ her_SC.say("I don't want to look plain!",12)
        elif one_of_ten == 10:
            $ her_SC.say("Would you like to see my tits today, sir?",64)
            $ her_SC.say("25 house points, please.",111)
            $ her_SC.setFace(120)
    if whoring >= 21: # WHORING LEVEL 08+.
        if one_of_ten == 1:
            $ her_SC.say("Do You have any adult magazines you don't need, sir?",189)
            $ her_SC.setFace(188)
        elif one_of_ten == 2:
            $ her_SC.say("I am sorry to bother you with this, sir...",31)
            $ her_SC.say("But do you have any condoms?")
            $ her_SC.say("This is not for me of course... I'm asking for a friend...",34)
        elif one_of_ten == 3:
            $ her_SC.say("It's been getting so cold lately...",14)
            $ her_SC.say("I hope it's going to start snowing soon...",6)
        elif one_of_ten == 4:
            $ her_SC.say("Jump and scream for the Gryffindor team!",127)
            $ her_SC.say("So daring and bold, sporting red and gold!",80)
            $ her_SC.setFace(6)
        elif one_of_ten == 5:
            $ her_SC.say("I hope the ball goes smoothly...",10)
            $ her_SC.setFace(13)
        elif one_of_ten == 6:
            $ her_SC.say("I wonder what Ginny is going to wear for the ball...",6)
        elif one_of_ten == 7:
            $ her_SC.say("Considering the nature of the favours you keep buying from me sir...",16)
            $ her_SC.say("I seldom bother to put on underwear at all anymore...",11)
        elif one_of_ten == 8:
            $ her_SC.say("Sir, could you put your penis in my mouth?",117)
            $ her_SC.say("Sir, I am begging you...",135)
            $ her_SC.say("Fifty five points, please!",111)
            $ her_SC.setFace(122)
        elif one_of_ten == 9:
            $ her_SC.say("A read this one article about the positive effects of semen on a woman's skin...",127)
            $ her_SC.say("I wonder where their information is coming from...",128)
            $ her_SC.say("Did the magazine conduct research of some sort?",122)
            $ her_SC.setFace(128)
        elif one_of_ten == 10:
            $ her_SC.say("It goes like this...",127)
            $ her_SC.say("First Gryffindor, then Ravenclaw, then Hufflepuff...")
            $ her_SC.say("And Slytherin is not even on the list!",186)
            $ her_SC.setFace(120)
    jump day_time_requests
    
        
label genie_change(name="",whoring_lvl=0):
    if whoring >= whoring_lvl:
        if name == "":
            $ genie_name = "Sir"
        else:
            $ genie_name = name
        $ her_SC.say("Ok, from now on I'll call you [genie_name]","body_01")
    else:
        $ her_SC.say("I'm not calling you that!","body_30")
    $ her_SC.say("","body_01")
    return
    
label hermione_change(name="",whoring_lvl=0):
    if whoring >= whoring_lvl:
        if name == "":
            $ hermione_name = "Miss granger"
        else:
            $ hermione_name = name
        $ her_SC.say("Fine, call me whatever you want [genie_name]","body_01")
    else:
        $ her_SC.say("I'm not letting you call me that!","body_30")
    $ her_SC.satFace("","body_01")
    return
    