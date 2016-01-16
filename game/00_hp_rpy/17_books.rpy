label __init_variables:
    if not hasattr(renpy.store,'book_progress'): #important!
        $ book_progress = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    if not hasattr(renpy.store,'book_done'): #important!
        $ book_done = [False,False,False,False,False,False,False,False,False,False,False,False,False]
    if not hasattr(renpy.store,'cheat_reading'): #important!
        $ cheat_reading = False
    if not hasattr(renpy.store,'books'): #important!
        $ books = []
    
    ### GENIE STATS ###============================
    if not hasattr(renpy.store,'imagination'): #important!
        $ imagination = 1 #+1 for every completed book. Unlocks new sexual favors to buy. 1 point of imagination = 1 level of whoring.
    if not hasattr(renpy.store,'concentration'): #important!
        $ concentration = 0 #+1 for every completed book on concentration. Pops up during paperwork.
    if not hasattr(renpy.store,'speedwriting'): #important!
        $ speedwriting = 0 #+1 for every completed book on speedwriting. Pops up during paperwork.
    if not hasattr(renpy.store,'s_reading_lvl'): #important!
        $ s_reading_lvl = 0
    
    #$ books = ["book_1", "book_2", "book_3", "book_4",  "book_5", "book_6", "book_7", "book_8", "book_9", "book_10", "book_11", "book_12", "book_13", "book_14", "book_15", "book_16", "book_17"]
    #All books.
    
    $ copper_book_id = 1
    $ bronze_book_id = 2
    $ silver_book_id = 3
    $ golden_book_id = 4
    
    $ speed_beginners_book_id = 5
    $ speed_amateurs_book_id = 6
    $ speed_advanced_book_id = 7
    $ speed_experts_book_id = 8
    
    $ galadriel_1_book_id = 9
    $ galadriel_2_book_id = 10
    $ armchairs_book_id = 11
    $ waifu_book_id = 12
    
    $ speed_reading_books = [1,2,3,4]
    $ speed_writing_books = [5,6,7,8]
    $ fiction_books = [9,10,11,12]
    
    
    $ book_name = []
    $ book_name.append("")#null
    $ book_name.append("\"Copper book of spirit\"")
    $ book_name.append("\"Bronze book of spirit\"")
    $ book_name.append("\"Silver book of spirit\"")
    $ book_name.append("\"Golden book of spirit\"")
    $ book_name.append("\"Speedwriting for beginners\"")
    $ book_name.append("\"Speedwriting for amateurs\"")
    $ book_name.append("\"Speedwriting for advanced writers\"")
    $ book_name.append("\"Speedwriting for experts\"")
    $ book_name.append("\"The Tale of Galadriel. Book I.\"")
    $ book_name.append("\"The Tale of Galadriel. Book II.\"")
    $ book_name.append("\"The game of Armchairs\"")
    $ book_name.append("\"My dear waifu\"")
    
    
    $ book_description = []
    $ book_description.append("")#null
    $ book_description.append("\nThis book contains various tips on how to improve one's efficiency.")
    $ book_description.append("\nThis book contains various tips on how to improve one's efficiency.")
    $ book_description.append("\nThis book contains various tips on how to improve one's efficiency.")
    $ book_description.append("\nThis book contains various tips on how to improve one's efficiency.")
    $ book_description.append("\nThis book contains a bunch of very basic techniques used to improve one's ability to write quickly.")
    $ book_description.append("\nThis book contains intermediate techniques used to improve one's ability to write quickly.")
    $ book_description.append("\nThis book contains advanced techniques used to improve one's ability to write quickly.")
    $ book_description.append("\nThis book contains expert techniques used to improve one's ability to read quickly.")
    $ book_description.append("This book tells a story of an elven princess who defies traditions of her people and chooses to forge her own destiny. Or does it?")
    $ book_description.append("This book tells a story of an elven princess who defies traditions of her people and chooses to forge her own destiny. Or does it?")
    $ book_description.append("An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape.")
    $ book_description.append("{size=-4}BY AKABUR{/size}\n" "Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"?")
    
    
    $ book_effect = []
    $ book_effect.append("")#null
    $ book_effect.append(">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when reading.")
    $ book_effect.append(">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when reading.")
    $ book_effect.append(">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when reading.")
    $ book_effect.append(">You have mastered your spirit and from now on you shall always complete an additional chapter when reading.")
    $ book_effect.append(">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.")
    $ book_effect.append(">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when doing paperwork.")
    $ book_effect.append(">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when doing paperwork.")
    $ book_effect.append(">You have become a true master of speedwriting and from now on you shall always complete an additional chapter when doing paperwork.")
    $ book_effect.append(">Your imagination has improved.")
    $ book_effect.append(">Your imagination has improved.")
    $ book_effect.append(">Your imagination has improved.")
    $ book_effect.append(">Your imagination has improved.")
    
    
    $ book_chapters = []
    $ book_chapters.append(0)#null
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(10)
    $ book_chapters.append(20)
    $ book_chapters.append(20)
    $ book_chapters.append(20)
    $ book_chapters.append(20)
    
    
    $ book_chapter_description = [[0 for i in xrange(21)] for i in xrange(21)]
    $ book_chapter_description[9][1]= "Galadriel - a gentle and gracious elven princess is introduced into the story."
    $ book_chapter_description[9][2]= "Galadriel's father - King Methis and his childhood friend Mofothelis are introduced into the story."
    $ book_chapter_description[9][3]= "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis."
    $ book_chapter_description[9][4]= "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle."
    $ book_chapter_description[9][5]= "King Methis dismisses her daughter's \"foolish\" complaints. Galadriel decides to run away."
    $ book_chapter_description[9][6]= "Galadriel manages to leave the royal residence at night unnoticed..."
    $ book_chapter_description[9][7]= "King Methis is furious about his daughter's escape. He decides to personally lead the search party."
    $ book_chapter_description[9][8]= "Galadriel rides her mare \"white dove\" through the forest. The Princess enjoys her freedom... After a while she meets a rather handsome human nobleman on a horse..."
    $ book_chapter_description[9][9]= "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries. He makes her laugh. Suddenly the nobleman attacks the princess and knocks her out!..."
    $ book_chapter_description[9][10]= "Galadriel comes about. To her horror she realizes that the nobleman is having his way with her. Galadriel is screaming for help but The handsome man keeps on raping her."
    $ book_chapter_description[9][11]= "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously."
    $ book_chapter_description[9][12]= "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop."
    $ book_chapter_description[9][13]= "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen."
    $ book_chapter_description[9][14]= "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage."
    $ book_chapter_description[9][15]= "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food."
    $ book_chapter_description[9][16]= "Galadriel is starting to feel hopeful but it does not last. Soon she realizes what kind of establishment this is: a whorehouse."
    $ book_chapter_description[9][17]= "The elven princess is forced to work as a whore. She detests her new life but has very little choice."
    $ book_chapter_description[9][18]= "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasional dwarf - she spreads her legs for everyone."
    $ book_chapter_description[9][19]= "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel."
    $ book_chapter_description[9][20]= "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-"
    
    $ book_chapter_description[10][1]= "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly."
    $ book_chapter_description[10][2]= "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel."
    $ book_chapter_description[10][3]= "The Elven Princess-Whore knows nothing of the life outside the of walls of the brothel. But it does not affect her determination to escape."
    $ book_chapter_description[10][4]= "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel."
    $ book_chapter_description[10][5]= "Galadriel soon gets lost in the vast city and is forced to spend the night on the street."
    $ book_chapter_description[10][6]= "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly."
    $ book_chapter_description[10][7]= "The Pregnant Galadriel offers her company to a couple of filthy looking homeless men in exchange for food. She spends the night with them."
    $ book_chapter_description[10][8]= "Galadriel realizes that her live back in the brothel was a heaven compared to the live she's been leading for the past several days. She decides to return."
    $ book_chapter_description[10][9]= "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back."
    $ book_chapter_description[10][10]= "Galadriel is, yet again, warm, clean and well fed. She is glad to be back and as popular as ever."
    $ book_chapter_description[10][11]= "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now..."
    $ book_chapter_description[10][12]= "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him."
    $ book_chapter_description[10][13]= "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her."
    $ book_chapter_description[10][14]= "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off."
    $ book_chapter_description[10][15]= "Galadriel recognizes the man as her father - King Methis. Only now he realizes that the pregnant whore he fucked for hours is his daughter."
    # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
    $ book_chapter_description[10][16]= "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face..."
    $ book_chapter_description[10][17]= "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed."
    $ book_chapter_description[10][18]= "It takes the elven princess several minutes to realize that she was never pregnant. The entire adventure was nothing but a dream."
    $ book_chapter_description[10][19]= "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis."
    $ book_chapter_description[10][20]= "{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}"
    
    $ book_chapter_description[11][1] = "A family of noble northmen is introduced into the story."
    $ book_chapter_description[11][2] = "The royal family and the king are introduced into the story."
    $ book_chapter_description[11][3] = "Another family is introduced into the story."
    $ book_chapter_description[11][4] = "Some incest action between a brother and his sister, the queen, is taking place."
    $ book_chapter_description[11][5] = "Attempted child murder takes place. The kid barely survives and is now in a coma."
    $ book_chapter_description[11][6] = "Some more characters are introduced into the story."
    $ book_chapter_description[11][7] = "Some characters hatch an evil scheme against some other characters."
    $ book_chapter_description[11][8] = "The king gets poisoned and dies. Some more brother on sister incest takes place."
    $ book_chapter_description[11][9] = "A certain character you've been especially rooting for gets executed."
    $ book_chapter_description[11][10] = "Some new characters are introduced into the story."
    $ book_chapter_description[11][11] = "Some female characters get raped and then killed brutally."
    $ book_chapter_description[11][12] = "Some more members of the noble family of northmen find their untimely demise."
    $ book_chapter_description[11][13] = "Some more women get raped. Some of them manage to survive. (Surely only to get raped some more later)." 
    $ book_chapter_description[11][14] = "The characters you hate clash in an epic battle against the characters you are rooting for."
    $ book_chapter_description[11][15] = "Most of the characters you hate survive the battle. Every single character you were rooting for is dead."
    $ book_chapter_description[11][16] = "Some more rapes take place, then some more murders... (You don't even care anymore...)" 
    $ book_chapter_description[11][17] = "A new group of characters is introduced into the story. You sort of starting to root for one of them."
    $ book_chapter_description[11][18] = "The character you were rooting for falls in love with a pretty girl."
    $ book_chapter_description[11][19] = "The character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well."
    $ book_chapter_description[11][20] = "A new race of half-frozen undead monsters is introduced into the story. To be continued..."
    
    return


label books_list:
menu:
    "-Educational books-":
        label books_on_improvement:
        menu:
            ###-1-###"\"Copper book of spirit\""
            "-Book: \"Copper book of spirit\"-" if "book_1" in books and book_progress[1] <= book_chapters[1]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency. Do you want to read it today?"
                menu:
                    "-Read the book-":
                        hide screen gift
                        call reading_book_block(1)
                        #jump reading_book_01
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Copper book of spirit\"-{image=check_08}" if "book_1" in books and book_progress[1] == book_chapters[1]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency. Do you want to read it now?"
                m "I already finished this one."
                m "It taught me a new skill: a 1 out of 6 chance of completing an additional chapter when doing paperwork."
                hide screen gift
                jump books_on_improvement
                
            ###-2-###"\"Bronze book of spirit\""   
            "-Book: \"Bronze book of spirit\"-" if "book_2" in books and book_progress[2] <= book_chapters[2]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency. Do you want to read it now?"
                menu:
                    "-Read the book-":
                        if "book_1" in books and book_progress[1] == book_chapters[1]:
                            hide screen gift
                            call reading_book_block(2)
                            #jump reading_book_02
                        else:
                            call gal_proper
                            jump books_on_improvement
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Bronze book of spirit\"-{image=check_08}" if "book_2" in books and book_progress[2] == book_chapters[2]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                m "It taught me a new skill: 1 out of 4 chance of completing an additional chapter when doing paperwork."
                hide screen gift
                jump books_on_improvement
            
            ###-3-###"\"Silver book of spirit\""  
            "-Book: \"Silver book of spirit\"-" if "book_3" in books and book_progress[3] <= book_chapters[3]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency. Do you want to read it today?"
                menu:
                    "-Read the book-":
                        if "book_2" in books and book_progress[2] == book_chapters[2]:
                            hide screen gift
                            call reading_book_block(3)
                            #jump reading_book_03
                        else:
                            call gal_proper
                            jump books_on_improvement
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Silver book of spirit\"-{image=check_08}" if "book_3" in books and book_progress[3] == book_chapters[3]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                m "It taught me a new skill: a 1out of 2 chance of completing an additional chapter when doing paperwork."
                hide screen gift
                jump books_on_improvement
                
            ###-4-###"\"Golden book of spirit\"" 
            "-Book: \"Golden book of spirit\"-" if "book_4" in books and book_progress[4] <= book_chapters[4]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                menu:
                    "-Read the book-":
                        if "book_3" in books and book_progress[3] == book_chapters[3]:
                            hide screen gift
                            call reading_book_block(4)
                            #jump reading_book_04
                        else:
                            call gal_proper
                            jump books_on_improvement
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Golden book of spirit\"-{image=check_08}" if "book_4" in books and book_progress[4] == book_chapters[4]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                g4 "I have mastered my spirit!"
                g9 "My spirit is my bitch!"
                hide screen gift
                jump books_on_improvement
            
            ###-5-###"\"Speedwriting for beginners\""
            "-Book: \"Speedwriting for beginners\"-" if "book_5" in books and book_progress[5] <= book_chapters[5]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains a bunch of very basic techniques used to improve one's ability to write quickly."
                menu:
                    "-Read the book-":
                        hide screen gift
                        call reading_book_block(5)
                        #jump reading_book_5
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Speedwriting for beginners\"-{image=check_08}" if "book_5" in books and book_progress[5] == book_chapters[5]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                m "It taught me a new skill: a 1 out of 6 chance of completing an additional chapter when doing paperwork."
                hide screen gift
                jump books_on_improvement
        
            ###-6-###"\"Speedwriting for amateurs\""
            "-Book: \"Speedwriting for amateurs\"-" if "book_6" in books and book_progress[6] <= book_chapters[6]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains intermediate techniques used to improve one's ability to write quickly."
                menu:
                    "-Read the book-":
                        if "book_5" in books and book_progress[5] == book_chapters[5]:
                            hide screen gift
                            call reading_book_block(6)
                            #jump reading_book_6
                        else:
                            call gal_proper
                            jump books_on_improvement
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Speedwriting for amateurs\"-{image=check_08}" if "book_6" in books and book_progress[6] == book_chapters[6]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                m "It taught me a new skill: a 1 out of 4 chance of completing an additional chapter when doing paperwork."
                hide screen gift
                jump books_on_improvement
                
            ###-7-###"\"Speedwriting for advanced writers\""
            "-Book: \"Speedwriting for advanced writers\"-" if "book_7" in books and book_progress[7] <= book_chapters[7]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains advanced techniques used to improve one's ability to write quickly."
                menu:
                    "-Read the book-":
                        if "book_6" in books and book_progress[6] == book_chapters[6]:
                            hide screen gift
                            call reading_book_block(7)
                            #jump reading_book_7
                        else:
                            call gal_proper
                            jump books_on_improvement
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Speedwriting for advanced writers\"-{image=check_08}" if "book_7" in books and book_progress[7] == book_chapters[7]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                m "It taught me a new skill: a 1 out of 2 chance of completing an additional chapter when doing paperwork."

                
                #m "It taught me a new skill: a decent chance of completing an additional chapter when doing paperwork."
                hide screen gift
                jump books_on_improvement
                
            ###-8-###"\"Speedwriting for experts.\""
            "-Book: \"Speedwriting for experts\"-" if "book_8" in books and book_progress[8] <= book_chapters[8]-1:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains expert techniques used to improve one's ability to write quickly."
                menu:
                    "-Read the book-":
                        if "book_7" in books and book_progress[7] == book_chapters[7]:
                            hide screen gift
                            call reading_book_block(8)
                            #jump reading_book_8
                        else:
                            call gal_proper
                            jump books_on_improvement
                    "-Never mind-":
                        hide screen gift
                        jump books_on_improvement
            "-Book: \"Speedwriting for experts\"-{image=check_08}" if "book_8" in books and book_progress[8] == book_chapters[8]:
                $ the_gift = "01_hp/18_store/books/1-8.png" # Copper book of spirit.
                show screen gift
                with d3
                ">This book contains various tips on how to improve one's efficiency."
                m "I already finished this one."
                m "I am a true master of speedwriting now..."
                hide screen gift
                jump books_on_improvement
                
            "-Never mind-":
                jump books_list
    "-Fiction books-":
        label fiction_books_menu:
        menu:
            ###-9-###05"\"The Tale of Galadriel\""    
            "-Book: \"The Tale of Galadriel. Book I.\"-" if "book_9" in books and book_progress[9] <= book_chapters[9]-1:
                $ the_gift = "01_hp/18_store/books/9.png" # THE TALE OF GALADRIEL. BOOK ONE.
                show screen gift
                ">This book contains a rather lengthy tale, describing the life and adventures of a young elven female by the name of Galadriel in great detail."
                with d3
                menu:
                    "-Read the book-":
                        hide screen gift
                        call reading_book_block(9)
                        #jump reading_book_9
                    "-Never mind-":
                        hide screen gift
                        jump  fiction_books_menu
            "-Book: \"The Tale of Galadriel. Book I.\"-{image=check_08}" if "book_9" in books and book_progress[9] == book_chapters[9]:
                $ the_gift = "01_hp/18_store/books/9.png" # THE TALE OF GALADRIEL. BOOK ONE.
                show screen gift
                ">This book contains a rather lengthy tale, describing the life and adventures of a young elven female by the name of Galadriel in great detail."
                ">You already finished this one."
                hide screen gift
                jump  fiction_books_menu
            
            ###-10-###05_b"\"The Tale of Galadriel. BOOK TWO.\""    
            "-Book: \"The Tale of Galadriel. Book II.\"-" if "book_10" in books and book_progress[10] <= book_chapters[10]-1:
                $ the_gift = "01_hp/18_store/books/10.png" # THE TALE OF GALADRIEL. BOOK TWO.
                show screen gift
                ">This book contains a rather lengthy tale, describing the life and adventures of a young elven female by the name of Galadriel in great detail."
                with d3
                menu:
                    "-Read the book-":
                        if "book_9" in books and book_progress[9] == book_chapters[9]: # MAKES SURE YOU DON'T READ PART II BEFORE PART I.
                            hide screen gift
                            call reading_book_block(10)
                            #jump reading_book_10_alt      
                        else:
                            call gal_proper
                            jump  fiction_books_menu
                            
                    "-Never mind-":
                        hide screen gift
                        jump  fiction_books_menu
            "-Book: \"The Tale of Galadriel. Book II.\"-{image=check_08}" if "book_10" in books and book_progress[10] == book_chapters[10]:
                $ the_gift = "01_hp/18_store/books/10.png" # THE TALE OF GALADRIEL. BOOK TWO.
                show screen gift
                ">This book contains a rather lengthy tale, describing the life and adventures of a young elven female by the name of Galadriel in great detail."
                ">You already finished this one."
                hide screen gift
                jump  fiction_books_menu
                
            ###-11-###06"\"The game of chairs\""    
            "-Book: \"The game of Armchairs\"-" if "book_11" in books and book_progress[11] <= book_chapters[11]-1:
                $ the_gift = "01_hp/18_store/books/11.png" # GAME OF THRONES.
                show screen gift
                with d3
                "\"The game of Armchairs\"\nAn epic tale of betrayal, murder and rape, then some more murder, some more betrayal and some more rape."
                menu:
                    "-Read the book-":
                        hide screen gift
                        call reading_book_block(11)
                        #jump reading_book_11
                    "-Never mind-":
                        hide screen gift
                        jump fiction_books_menu
            "-Book: \"The game of Armchairs\"-{image=check_08}" if "book_11" in books and book_progress[11] == book_chapters[11]:
                $ the_gift = "01_hp/18_store/books/11.png" # GAME OF THRONES.
                show screen gift
                "\"The game of Armchairs\"\nAn epic tale of betrayal, murder and rape, then some more murder, some more betrayal and some more rape."
                m "Why would I want to do this to myself again?"
                hide screen gift
                jump fiction_books_menu
                
            ###-12-###07"\"My dear waifu\""
            "-Book: \"My dear waifu\"-" if "book_12" in books and book_progress[12] <= book_chapters[12]-1 and not waifu_book_completed:
                $ the_gift = "01_hp/18_store/books/12.png" # MY DEAR WAIFU.
                show screen gift
                with d3
                "\"My Dear waifu\" {size=-4}BY AKABUR{/size}" "Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"?"
                menu:
                    "-Read the book-":
                        if dear_waifu_completed_once and book_progress[12] == book_chapters[12]:
                            m "I don't think reading this book again will give me any new ideas. Should I just read it for fun though?"
                            menu:
                                "-Read the book again-":
                                    hide screen gift
                                    call reading_book_block(12)
                                    #jump reading_book_07
                                "-Never mind-":
                                    hide screen gift
                                    jump fiction_books_menu
                        else:
                            hide screen gift
                            call reading_book_block(12)
                            #jump reading_book_07
                    "-Never mind-":
                        hide screen gift
                        jump fiction_books_menu
            "-Book: \"My dear waifu\"-{image=check_08}" if "book_12" in books and waifu_book_completed:
                $ the_gift = "01_hp/18_store/books/12.png" # MY DEAR WAIFU.
                show screen gift
                with d3
                "\"My Dear waifu\" {size=-4}BY AKABUR{/size}" "Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"?"
                menu:
                    "-Read the book-":
                        if dear_waifu_completed_once and book_progress[12] == 0:
                            m "I don't think reading this book again will give me any new ideas."
                            hide screen gift
                            jump fiction_books_menu
                    "-Never mind-":
                        hide screen gift
                        jump fiction_books_menu
                
            "-Never mind-":
                jump books_list
    "-Never mind-":
        jump desk

        
label speed_reading_check(bookID = -1):
    if s_reading_lvl == 1: #30% chance
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            ">Implementing some tricks you picked up in the \"Speed reading for dummies\" book allows you to save time and keep on reading."
            call check_book(bookID)
    if s_reading_lvl == 2: #50% chance
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            ">Implementing speed reading techniques allows you to save time and keep on reading."
            call check_book(bookID)
    if s_reading_lvl > 2: #100% chance
        ">Implementing speed reading techniques allows you to save time and keep on reading."
        call check_book(bookID)
    return
    
label chap_finished(bookID = -1):
    if bookID in speed_reading_books or bookID in speed_writing_books:
        $ book_progress[bookID] += 1 
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        $ tmp = book_progress[bookID]
        ">You've completed \"chapter [tmp]\" of the book."
    elif bookID in fiction_books:
        $ book_progress[bookID] += 1 
        
        if not bookID == 12:
            $tmp_chap = book_progress[bookID]
            $tmp_desc = book_chapter_description[bookID][book_progress[bookID]]
            "Chapter [tmp_chap]" "[tmp_desc]"
        else:
            call waifu
        
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        $ tmp = book_progress[bookID]
        ">You've completed \"chapter [tmp]\" of the book."
    return
    
label chapter_check_book(bookID =-1):
    if book_progress[bookID] == book_chapters[bookID]:
        call book_done_a_check_fire
        
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">That was the last chapter, You finished the entire book."
        if bookID == 11: 
            g4 "What a pile of garbage! I hate the guy who wrote this crap!"
            m "Although all those rapes gave me a few ideas..."
        
        if bookID in fiction_books:
            $ renpy.play('sounds/win_04.mp3')   #Not loud.
            hide screen notes
            show screen notes
            ">Your imagination has improved."
            $ imagination +=1
        else:
            $ tmp = book_effect[bookID]
            ">[tmp]" # ex. ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."
            
            if bookID in speed_reading_books:
                $ s_reading_lvl += 1
            if bookID in speed_writing_books:
                $ speedwriting += 1
                $ concentration += 1
        
        $ book_done[bookID] = True
        
        call book_done_b_check_fire
    else:
        return
    
label book_done_a_check_fire:
    if fire_in_fireplace:
        show screen done_reading_02  
        hide screen reading_near_fire
    else:
        show screen done_reading  
        hide screen reading
    return
    
label book_done_b_check_fire:
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading
    
    if daytime:
        jump night_start
    else: 
        jump day_start
    return
    
label check_book(bookID):
    call chap_finished(bookID)
    call chapter_check_book(bookID)
    ">There are still some chapters left."
    if cheat_reading:
        #">You are a cheater so you get to keep on reading."
        call check_book(bookID)
    return
    
label reading_book_block(bookID = -1):
    stop music fadeout 2.0
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    $ tmp = book_name[bookID]
    if raining:
        ">You read a book called [tmp], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [tmp]..."
    
    call check_book(bookID)
    call speed_reading_check(bookID)
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call check_book(bookID)
    
    call book_done_b_check_fire
    return
    
label reading_block:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        call fire_out #Shows Genie reading a book near the window.
    if daytime and not raining:
        #play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        play weather "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining:
        play weather "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    return
    
label no_fire: #Message you see that says you are reading a book during rain.
    ">The rain outside of the tower calms your mood and you feel like keeping on reading..."
    ">You try to keep on reading but after a while you realize that the air in your chambers is too damp for your liking."
    return
    
label yes_fire: #Message you see that says you are reading a book during rain near fireplace.
    ">The rain outside of your tower calms your mood and you feel like keeping on reading..."
    return
    
label fire_in: #Shows Genie reading a book near the fireplace.
    hide screen chair
    hide screen genie
    show screen reading_near_fire
    with Dissolve(0.3)
    return
    
label fire_out: #Shows Genie reading a book near the window.
    hide screen chair
    hide screen genie
    show screen reading
    with Dissolve(0.3)
    return
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Reading books out of order won't do me any good."
    hide screen gift
    return
    
