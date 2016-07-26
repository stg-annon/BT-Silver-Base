label __init_variables:
    if not hasattr(renpy.store,'Copper_Book_OBJ'): #important!
        $ Copper_Book_OBJ = educational_book()
    $ Copper_Book_OBJ.name = "\"Copper book of spirit\""
    $ Copper_Book_OBJ.book_description = "\nThis book contains various tips on how to improve one's efficiency."
    $ Copper_Book_OBJ.effect = ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when reading."
    $ Copper_Book_OBJ.chapters = 10
    $ Copper_Book_OBJ.cost = 40
    $ Copper_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Bronze_Book_OBJ'): #important!
        $ Bronze_Book_OBJ = educational_book()
    $ Bronze_Book_OBJ.name = "\"Bronze book of spirit\""
    $ Bronze_Book_OBJ.book_description = "\nThis book contains various tips on how to improve one's efficiency."
    $ Bronze_Book_OBJ.effect = ">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when reading."
    $ Bronze_Book_OBJ.chapters = 10
    $ Bronze_Book_OBJ.cost = 80
    $ Bronze_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Silver_Book_OBJ'): #important!
        $ Silver_Book_OBJ = educational_book()
    $ Silver_Book_OBJ.name = "\"Silver book of spirit\""
    $ Silver_Book_OBJ.book_description = "\nThis book contains various tips on how to improve one's efficiency."
    $ Silver_Book_OBJ.effect = ">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when reading."
    $ Silver_Book_OBJ.chapters = 10
    $ Silver_Book_OBJ.cost = 90
    $ Silver_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Golden_Book_OBJ'): #important!
        $ Golden_Book_OBJ = educational_book()
    $ Golden_Book_OBJ.name = "\"Golden book of spirit\""
    $ Golden_Book_OBJ.book_description = "\nThis book contains various tips on how to improve one's efficiency."
    $ Golden_Book_OBJ.effect = ">You have mastered your spirit and from now on you shall always complete an additional chapter when reading."
    $ Golden_Book_OBJ.chapters = 10
    $ Golden_Book_OBJ.cost = 100
    $ Golden_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    $ speed_read_books = []
    $ speed_read_books.append(Copper_Book_OBJ)
    $ speed_read_books.append(Bronze_Book_OBJ)
    $ speed_read_books.append(Silver_Book_OBJ)
    $ speed_read_books.append(Golden_Book_OBJ)
    
    
    if not hasattr(renpy.store,'Speedwriting_Beginners_OBJ'): #important!
        $ Speedwriting_Beginners_OBJ = educational_book()
    $ Speedwriting_Beginners_OBJ.name = "\"Speedwriting for beginners\""
    $ Speedwriting_Beginners_OBJ.book_description = "\nThis book contains a bunch of very basic techniques used to improve one's ability to write quickly."
    $ Speedwriting_Beginners_OBJ.effect = ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork."
    $ Speedwriting_Beginners_OBJ.chapters = 10
    $ Speedwriting_Beginners_OBJ.cost = 90
    $ Speedwriting_Beginners_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Amateurs_OBJ'): #important!
        $ Speedwriting_Amateurs_OBJ = educational_book()
    $ Speedwriting_Amateurs_OBJ.name = "\"Speedwriting for amateurs\""
    $ Speedwriting_Amateurs_OBJ.book_description = "\nThis book contains intermediate techniques used to improve one's ability to write quickly."
    $ Speedwriting_Amateurs_OBJ.effect = ">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when doing paperwork."
    $ Speedwriting_Amateurs_OBJ.chapters = 10
    $ Speedwriting_Amateurs_OBJ.cost = 100
    $ Speedwriting_Amateurs_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Advanced_OBJ'): #important!
        $ Speedwriting_Advanced_OBJ = educational_book()
    $ Speedwriting_Advanced_OBJ.name = "\"Speedwriting for advanced writers\""
    $ Speedwriting_Advanced_OBJ.book_description = "\nThis book contains advanced techniques used to improve one's ability to write quickly."
    $ Speedwriting_Advanced_OBJ.effect = ">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when doing paperwork."
    $ Speedwriting_Advanced_OBJ.chapters = 10
    $ Speedwriting_Advanced_OBJ.cost = 130
    $ Speedwriting_Advanced_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Experts_OBJ'): #important!
        $ Speedwriting_Experts_OBJ = educational_book()
    $ Speedwriting_Experts_OBJ.name = "\"Speedwriting for experts\""
    $ Speedwriting_Experts_OBJ.book_description = "\nThis book contains expert techniques used to improve one's ability to read quickly."
    $ Speedwriting_Experts_OBJ.effect = ">You have become a true master of speedwriting and from now on you shall always complete an additional chapter when doing paperwork."
    $ Speedwriting_Experts_OBJ.chapters = 10
    $ Speedwriting_Experts_OBJ.cost = 175
    $ Speedwriting_Experts_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    $ speed_write_books = []
    $ speed_write_books.append(Speedwriting_Beginners_OBJ)
    $ speed_write_books.append(Speedwriting_Amateurs_OBJ)
    $ speed_write_books.append(Speedwriting_Advanced_OBJ)
    $ speed_write_books.append(Speedwriting_Experts_OBJ)
    
    
    if not hasattr(renpy.store,'Galadriel_I_OBJ'): #important!
        $ Galadriel_I_OBJ = fiction_book()
    $ Galadriel_I_OBJ.name = "\"The Tale of Galadriel. Book I.\""
    $ Galadriel_I_OBJ.book_description = "This book tells a story of an elven princess who defies traditions of her people and chooses to forge her own destiny. Or does it?"
    $ Galadriel_I_OBJ.effect = ">Your imagination has improved."
    $ Galadriel_I_OBJ.chapters = 20
    $ Galadriel_I_OBJ.cost = 100
    $ Galadriel_I_OBJ.picture = "01_hp/18_store/books/9.png"
    
    if not hasattr(renpy.store,'Galadriel_II_OBJ'): #important!
        $ Galadriel_II_OBJ = fiction_book()
    $ Galadriel_II_OBJ.name = "\"The Tale of Galadriel. Book II.\""
    $ Galadriel_II_OBJ.book_description = "This book tells a story of an elven princess who defies traditions of her people and chooses to forge her own destiny. Or does it?"
    $ Galadriel_II_OBJ.effect = ">Your imagination has improved."
    $ Galadriel_II_OBJ.chapters = 20
    $ Galadriel_II_OBJ.cost = 200
    $ Galadriel_II_OBJ.picture = "01_hp/18_store/books/10.png"
    
    if not hasattr(renpy.store,'Armchairs_OBJ'): #important!
        $ Armchairs_OBJ = fiction_book()
    $ Armchairs_OBJ.name = "\"The game of Armchairs\""
    $ Armchairs_OBJ.book_description = "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape."
    $ Armchairs_OBJ.effect = ">Your imagination has improved."
    $ Armchairs_OBJ.chapters = 20
    $ Armchairs_OBJ.cost = 250
    $ Armchairs_OBJ.picture = "01_hp/18_store/books/11.png"
    
    if not hasattr(renpy.store,'Dear_Wifu_OBJ'): #important!
        $ Dear_Wifu_OBJ = fiction_book()
    $ Dear_Wifu_OBJ.name = "\"My dear waifu\""
    $ Dear_Wifu_OBJ.book_description = "{size=-4}BY AKABUR{/size}\n" "Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"?"
    $ Dear_Wifu_OBJ.effect = ">Your imagination has improved."
    $ Dear_Wifu_OBJ.chapters = 20
    $ Dear_Wifu_OBJ.cost = 300
    $ Dear_Wifu_OBJ.picture = "01_hp/18_store/books/12.png"
    
    
    $ Galadriel_I_OBJ.chapter_description = []
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel - a gentle and gracious elven princess is introduced into the story.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel's father - King Methis and his childhood friend Mofothelis are introduced into the story.")
    $ Galadriel_I_OBJ.chapter_description.append("King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle.")
    $ Galadriel_I_OBJ.chapter_description.append("King Methis dismisses her daughter's \"foolish\" complaints. Galadriel decides to run away.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel manages to leave the royal residence at night unnoticed...")
    $ Galadriel_I_OBJ.chapter_description.append("King Methis is furious about his daughter's escape. He decides to personally lead the search party.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel rides her mare \"white dove\" through the forest. The Princess enjoys her freedom... After a while she meets a rather handsome human nobleman on a horse...")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel rides alongside the nobleman. They exchange meaningless pleasantries. He makes her laugh. Suddenly the nobleman attacks the princess and knocks her out!...")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel comes about. To her horror she realizes that the nobleman is having his way with her. Galadriel is screaming for help but The handsome man keeps on raping her.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously.")
    $ Galadriel_I_OBJ.chapter_description.append("After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen.")
    $ Galadriel_I_OBJ.chapter_description.append("A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel is starting to feel hopeful but it does not last. Soon she realizes what kind of establishment this is: a whorehouse.")
    $ Galadriel_I_OBJ.chapter_description.append("The elven princess is forced to work as a whore. She detests her new life but has very little choice.")
    $ Galadriel_I_OBJ.chapter_description.append("Galadriel gains popularity quickly. Humans, Dark Elves and even the occasional dwarf - she spreads her legs for everyone.")
    $ Galadriel_I_OBJ.chapter_description.append("The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel.")
    $ Galadriel_I_OBJ.chapter_description.append("Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-")
    
    
    
    $ Galadriel_II_OBJ.chapter_description = []
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly.")
    $ Galadriel_II_OBJ.chapter_description.append("Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel.")
    $ Galadriel_II_OBJ.chapter_description.append("The Elven Princess-Whore knows nothing of the life outside the of walls of the brothel. But it does not affect her determination to escape.")
    $ Galadriel_II_OBJ.chapter_description.append("It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel soon gets lost in the vast city and is forced to spend the night on the street.")
    $ Galadriel_II_OBJ.chapter_description.append("Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly.")
    $ Galadriel_II_OBJ.chapter_description.append("The Pregnant Galadriel offers her company to a couple of filthy looking homeless men in exchange for food. She spends the night with them.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel realizes that her live back in the brothel was a heaven compared to the live she's been leading for the past several days. She decides to return.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel is, yet again, warm, clean and well fed. She is glad to be back and as popular as ever.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now...")
    $ Galadriel_II_OBJ.chapter_description.append("A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him.")
    $ Galadriel_II_OBJ.chapter_description.append("The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her.")
    $ Galadriel_II_OBJ.chapter_description.append("The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel recognizes the man as her father - King Methis. Only now he realizes that the pregnant whore he fucked for hours is his daughter.")
    # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
    $ Galadriel_II_OBJ.chapter_description.append("The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face...")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed.")
    $ Galadriel_II_OBJ.chapter_description.append("It takes the elven princess several minutes to realize that she was never pregnant. The entire adventure was nothing but a dream.")
    $ Galadriel_II_OBJ.chapter_description.append("Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis.")
    $ Galadriel_II_OBJ.chapter_description.append("{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}")
    
    
    
    $ Armchairs_OBJ.chapter_description = []
    $ Armchairs_OBJ.chapter_description.append("A family of noble northmen is introduced into the story.")
    $ Armchairs_OBJ.chapter_description.append("The royal family and the king are introduced into the story.")
    $ Armchairs_OBJ.chapter_description.append("Another family is introduced into the story.")
    $ Armchairs_OBJ.chapter_description.append("Some incest action between a brother and his sister, the queen, is taking place.")
    $ Armchairs_OBJ.chapter_description.append("Attempted child murder takes place. The kid barely survives and is now in a coma.")
    $ Armchairs_OBJ.chapter_description.append("Some more characters are introduced into the story.")
    $ Armchairs_OBJ.chapter_description.append("Some characters hatch an evil scheme against some other characters.")
    $ Armchairs_OBJ.chapter_description.append("The king gets poisoned and dies. Some more brother on sister incest takes place.")
    $ Armchairs_OBJ.chapter_description.append("A certain character you've been especially rooting for gets executed.")
    $ Armchairs_OBJ.chapter_description.append("Some new characters are introduced into the story.")
    $ Armchairs_OBJ.chapter_description.append("Some female characters get raped and then killed brutally.")
    $ Armchairs_OBJ.chapter_description.append("Some more members of the noble family of northmen find their untimely demise.")
    $ Armchairs_OBJ.chapter_description.append("Some more women get raped. Some of them manage to survive. (Surely only to get raped some more later).") 
    $ Armchairs_OBJ.chapter_description.append("The characters you hate clash in an epic battle against the characters you are rooting for.")
    $ Armchairs_OBJ.chapter_description.append("Most of the characters you hate survive the battle. Every single character you were rooting for is dead.")
    $ Armchairs_OBJ.chapter_description.append("Some more rapes take place, then some more murders... (You don't even care anymore...)") 
    $ Armchairs_OBJ.chapter_description.append("A new group of characters is introduced into the story. You sort of starting to root for one of them.")
    $ Armchairs_OBJ.chapter_description.append("The character you were rooting for falls in love with a pretty girl.")
    $ Armchairs_OBJ.chapter_description.append("The character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well.")
    $ Armchairs_OBJ.chapter_description.append("A new race of half-frozen undead monsters is introduced into the story. To be continued...")
    
    
    $ fiction_book_list = []
    $ fiction_book_list.append(Galadriel_I_OBJ)
    $ fiction_book_list.append(Galadriel_II_OBJ)
    $ fiction_book_list.append(Armchairs_OBJ)
    $ fiction_book_list.append(Dear_Wifu_OBJ)
    
    $ book_list = []
    $ book_list.extend(speed_read_books)
    $ book_list.extend(speed_write_books)
    $ book_list.extend(fiction_book_list)
    
    
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
    
    return


label books_list:
menu:
    "-Educational books-":
        label books_on_improvement:
        python:
            edu_menu = []
            edu_list = []
            edu_list.extend(speed_read_books)
            edu_list.extend(speed_write_books)
            for i in edu_list:
                if i.purchased:
                    if i.done:
                        edu_menu.append((i.getMenuTextDone(),i))
                    else:
                        edu_menu.append((i.getMenuText(),i))
            edu_menu.append(("-Never mind-", "nvm"))
            result = renpy.display_menu(edu_menu)
        if result == "nvm":
            jump books_list
        else:
            call handle_book_selection(result)
    "-Fiction books-":
        label fiction_books_menu:
        python:
            fic_menu = []
            for i in fiction_book_list:
                if i.purchased:
                    if i.done:
                        fic_menu.append((i.getMenuTextDone(),i))
                    else:
                        fic_menu.append((i.getMenuText(),i))
            fic_menu.append(("-Never mind-", "nvm"))
            result = renpy.display_menu(fic_menu)
        if result == "nvm":
            jump books_list
        else:
            call handle_book_selection(result)
    "-Never mind-":
        jump desk
    
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
    
    
label handle_book_selection(BookOBJ):
    $ the_gift = BookOBJ.picture
    show screen gift
    with d3
    "[BookOBJ.book_description]"
    if BookOBJ.done:
        if result == Armchairs_OBJ:
            m "Why would I want to do this to myself again?"
        else:
            ">You already finished this one."
        hide screen gift
        jump test_new_book
    else:
        menu:
            "-Read the book-":
                hide screen gift
                call check_book_order(BookOBJ)
            "-Never mind-":
                hide screen gift
                if BookOBJ in fiction_book_list:
                    jump fiction_books_menu
                else:
                    jump books_on_improvement
    
label check_book_order(bookOBJ = None):
    if bookOBJ in speed_read_books:
        if (bookOBJ == Copper_Book_OBJ)or(bookOBJ == Bronze_Book_OBJ and Copper_Book_OBJ.done)or(bookOBJ == Silver_Book_OBJ and Bronze_Book_OBJ.done)or(bookOBJ == Golden_Book_OBJ and Silver_Book_OBJ.done):
            call reading_book(BookOBJ)
    
    if bookOBJ in speed_write_books:
       if (bookOBJ == Speedwriting_Beginners_OBJ)or(bookOBJ == Speedwriting_Amateurs_OBJ and Speedwriting_Beginners_OBJ.done)or(bookOBJ == Speedwriting_Advanced_OBJ and Speedwriting_Amateurs_OBJ.done)or(bookOBJ == Speedwriting_Experts_OBJ and Speedwriting_Advanced_OBJ.done):
            call reading_book(BookOBJ)
    
    if bookOBJ in fiction_book_list:
        if (bookOBJ == Galadriel_II_OBJ and Galadriel_I_OBJ.done):
            call reading_book(BookOBJ)
        elif bookOBJ != Galadriel_II_OBJ:
            call reading_book(BookOBJ)
    
    m "Reading books out of order won't do me any good."
    jump test_new_book
    
    
label reading_book(bookID = None):

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
    
    if raining:
        ">You read a book called [bookID.name], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [bookID.name]..."
    
    call read_book(bookID)
    call book_speed_check(bookID)
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call read_book(bookID)
    
    call book_done_b_check_fire
    return
    
    
    
    
    
    
    
    
label book_speed_check(bookOBJ = None):
    if s_reading_lvl == 1: #30% chance
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing purpose only.
        if speed_dummies == 1: #Success.
            ">Implementing some tricks you picked up in the \"Speed reading for dummies\" book allows you to save time and keep on reading."
            call read_book(bookOBJ)
    if s_reading_lvl == 2: #50% chance
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing purpose only.
        if speed_dummies == 1: #Success.
            ">Implementing speed reading techniques allows you to save time and keep on reading."
            call read_book(bookOBJ)
    if s_reading_lvl > 2: #100% chance
        ">Implementing speed reading techniques allows you to save time and keep on reading."
        call read_book(bookOBJ)
    return
    

label read_book(bookOBJ):
    call read_chapter(bookOBJ)
    if bookOBJ.progress >= bookOBJ.chapters:
        call book_complete(bookOBJ)
        return
    ">There are still some chapters left."
    if cheat_reading:
        #">You are a cheater so you get to keep on reading."
        call read_book(bookOBJ)
    return
    
    
label read_chapter(bookOBJ = None):
    $ bookOBJ.progress += 1 
    if bookOBJ in speed_read_books or bookOBJ in speed_write_books:
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You've completed \"chapter [bookOBJ.progress]\" of the book."
    elif bookOBJ in fiction_book_list:
        if bookOBJ == Dear_Wifu_OBJ:
            call waifu
            call chapter_check_waifu
        else:
            $tmp_desc = bookOBJ.getChapterDesc()
            "[tmp_desc]"
        
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">You've completed \"chapter [bookOBJ.progress]\" of the book."
    return
    

label book_complete(bookOBJ = None):
    call book_done_a_check_fire
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">That was the last chapter, You finished the entire book."
    if bookOBJ == Armchairs_OBJ: 
        g4 "What a pile of garbage! I hate the guy who wrote this crap!"
        m "Although all those rapes gave me a few ideas..."
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    "[bookOBJ.effect]" # ex. ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."
        
    if bookOBJ in fiction_book_list:
        $ imagination += 1
    if bookOBJ in speed_reading_books:
        $ s_reading_lvl += 1
    if bookOBJ in speed_writing_books:
        $ speedwriting += 1
        $ concentration += 1
    
    $ bookOBJ.done = True
    call book_done_b_check_fire
    return
    
    
init python:
    class silver_book(object):
        cost = 0
        chapters = 0
        progress = 0
        done = False
        purchased = False
        name = ""
        effect = ""
        book_description = ""
        picture = ""
        def getMenuText(self):
            return "-"+str(self.name)+"-"
        def getMenuTextDone(self):
            return "-"+str(self.name)+"-{image=check_08}"
        def getStoreMenuText(self):
            return "-"+str(self.name)+"- ("+str(self.cost)+" g.)"
        def getMenuTextPurchased(self):
            return "{color=#858585}-"+str(self.name)+"- ("+str(self.cost)+" g.){/color}"
    
    class educational_book(silver_book):
        pass
    
    class fiction_book(silver_book):
        chapter_description = []
        def getChapterDesc(self):
           return "Chapter "+str(self.progress)+": "+self.chapter_description[self.progress-1]
           
           
