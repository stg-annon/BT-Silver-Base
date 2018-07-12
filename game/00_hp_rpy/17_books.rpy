label __init_variables:
    if not hasattr(renpy.store,'Copper_Book_OBJ'): #important!
        $ Copper_Book_OBJ = educational_book()
    $ Copper_Book_OBJ.id = "Copper_Book"
    $ Copper_Book_OBJ.name = "\"Copper book of spirit\""
    $ Copper_Book_OBJ.effect = ">New skill unlocked: a 1 out of 3 chance of completing an additional chapter when reading."
    $ Copper_Book_OBJ.chapters = 2
    $ Copper_Book_OBJ.book_description = "\nThis book contains various tips on speed reading. " + str(Copper_Book_OBJ.chapters) + " chapters."
    $ Copper_Book_OBJ.cost = 40
    $ Copper_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Bronze_Book_OBJ'): #important!
        $ Bronze_Book_OBJ = educational_book()
    $ Bronze_Book_OBJ.id = "Bronze_Book"
    $ Bronze_Book_OBJ.name = "\"Bronze book of spirit\""
    $ Bronze_Book_OBJ.effect = ">New skill unlocked: a 2 out of 3 chance of completing an additional chapter when reading." 
    $ Bronze_Book_OBJ.chapters = 4
    $ Bronze_Book_OBJ.book_description = "\nThis book contains various tips on speed reading. "  + str(Bronze_Book_OBJ.chapters) + " chapters."
    $ Bronze_Book_OBJ.cost = 60
    $ Bronze_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Silver_Book_OBJ'): #important!
        $ Silver_Book_OBJ = educational_book()
    $ Silver_Book_OBJ.id = "Silver_Book"
    $ Silver_Book_OBJ.name = "\"Silver book of spirit\""
    $ Silver_Book_OBJ.chapters = 6
    $ Silver_Book_OBJ.book_description = "\nThis book contains various tips on speed reading. " + str(Silver_Book_OBJ.chapters) + " chapters."
    $ Silver_Book_OBJ.effect = ">New skill unlocked: always complete an additional chapter when reading."
    $ Silver_Book_OBJ.cost = 80
    $ Silver_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Golden_Book_OBJ'): #important!
        $ Golden_Book_OBJ = educational_book()
    $ Golden_Book_OBJ.id = "Golden_Book"
    $ Golden_Book_OBJ.name = "\"Golden book of spirit\""
    $ Golden_Book_OBJ.chapters = 8
    $ Golden_Book_OBJ.book_description = "\nThis book contains various tips on speed reading. " + str(Golden_Book_OBJ.chapters) + " chapters."
    $ Golden_Book_OBJ.effect = ">You have mastered your spirit and from now on you can always complete two additional chapters when reading."
    $ Golden_Book_OBJ.cost = 160
    $ Golden_Book_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    
    if not hasattr(renpy.store,'Speedwriting_Beginners_OBJ'): #important!
        $ Speedwriting_Beginners_OBJ = educational_book()
    $ Speedwriting_Beginners_OBJ.id = "Speedwriting_Beginners"
    $ Speedwriting_Beginners_OBJ.name = "\"Speedwriting for beginners\""
    $ Speedwriting_Beginners_OBJ.chapters = 2
    $ Speedwriting_Beginners_OBJ.book_description = "\nThis book contains a bunch of very basic techniques used to improve one's ability to write quickly. " + str(Speedwriting_Beginners_OBJ.chapters) + " chapters."
    $ Speedwriting_Beginners_OBJ.effect = ">New skill unlocked: a 1 out of 3 chance of completing an additional chapter when doing paperwork."
    $ Speedwriting_Beginners_OBJ.cost = 90
    $ Speedwriting_Beginners_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Amateurs_OBJ'): #important!
        $ Speedwriting_Amateurs_OBJ = educational_book()
    $ Speedwriting_Amateurs_OBJ.id = "Speedwriting_Amateurs"
    $ Speedwriting_Amateurs_OBJ.name = "\"Speedwriting for amateurs\""
    $ Speedwriting_Amateurs_OBJ.chapters = 4
    $ Speedwriting_Amateurs_OBJ.book_description = "\nThis book contains intermediate techniques used to improve one's ability to write quickly. " + str(Speedwriting_Amateurs_OBJ.chapters) + " chapters."
    $ Speedwriting_Amateurs_OBJ.effect = ">New skill unlocked: a 2 out of 3 chance of completing an additional chapter when doing paperwork."
    $ Speedwriting_Amateurs_OBJ.cost = 110
    $ Speedwriting_Amateurs_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Advanced_OBJ'): #important!
        $ Speedwriting_Advanced_OBJ = educational_book()
    $ Speedwriting_Advanced_OBJ.id = "Speedwriting_Advanced"
    $ Speedwriting_Advanced_OBJ.name = "\"Speedwriting for advanced writers\""
    $ Speedwriting_Advanced_OBJ.chapters = 6
    $ Speedwriting_Advanced_OBJ.book_description = "\nThis book contains advanced techniques used to improve one's ability to write quickly. " + str(Speedwriting_Advanced_OBJ.chapters) + " chapters."
    $ Speedwriting_Advanced_OBJ.effect = ">New skill unlocked: always complete an additional chapter when doing paperwork."
    $ Speedwriting_Advanced_OBJ.cost = 130
    $ Speedwriting_Advanced_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    if not hasattr(renpy.store,'Speedwriting_Experts_OBJ'): #important!
        $ Speedwriting_Experts_OBJ = educational_book()
    $ Speedwriting_Experts_OBJ.id = "Speedwriting_Experts"
    $ Speedwriting_Experts_OBJ.name = "\"Speedwriting for experts\""
    $ Speedwriting_Experts_OBJ.chapters = 8
    $ Speedwriting_Experts_OBJ.book_description = "\nThis book contains expert techniques used to improve one's ability to read quickly. " + str(Speedwriting_Experts_OBJ.chapters) + " chapters."
    $ Speedwriting_Experts_OBJ.effect = ">You have become a true master of speedwriting and from now on you shall always complete two additional chapters when doing paperwork."
    $ Speedwriting_Experts_OBJ.cost = 150
    $ Speedwriting_Experts_OBJ.picture = "01_hp/18_store/books/1-8.png"
    
    
    
    if not hasattr(renpy.store,'Galadriel_I_OBJ'): #important!
        $ Galadriel_I_OBJ = fiction_book()
    $ Galadriel_I_OBJ.id = "Galadriel_I"
    $ Galadriel_I_OBJ.name = "\"The Tale of Galadriel. Book I.\""
    $ Galadriel_I_OBJ.book_description = "This book tells the story of an elven princess who defies the traditions of her people and chooses to forge her own destiny. Or does it? " + str(Galadriel_I_OBJ.chapters / 2) + " chapters."
    $ Galadriel_I_OBJ.effect = ">Your imagination has improved."
    $ Galadriel_I_OBJ.chapters = 20
    $ Galadriel_I_OBJ.cost = 100
    $ Galadriel_I_OBJ.picture = "01_hp/18_store/books/9.png"
    
    if not hasattr(renpy.store,'Galadriel_II_OBJ'): #important!
        $ Galadriel_II_OBJ = fiction_book()
    $ Galadriel_II_OBJ.id = "Galadriel_II"
    $ Galadriel_II_OBJ.name = "\"The Tale of Galadriel. Book II.\""
    $ Galadriel_II_OBJ.book_description = "This book tells the story of an elven princess who defies the traditions of her people and chooses to forge her own destiny. Or does it? "  + str(Galadriel_II_OBJ.chapters / 2) + " chapters."
    $ Galadriel_II_OBJ.effect = ">Your imagination has improved."
    $ Galadriel_II_OBJ.chapters = 20
    $ Galadriel_II_OBJ.cost = 200
    $ Galadriel_II_OBJ.picture = "01_hp/18_store/books/10.png"
    
    if not hasattr(renpy.store,'Armchairs_OBJ'): #important!
        $ Armchairs_OBJ = fiction_book()
    $ Armchairs_OBJ.id = "Armchairs"
    $ Armchairs_OBJ.name = "\"The game of Armchairs\""
    $ Armchairs_OBJ.book_description = "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape. " + str(Armchairs_OBJ.chapters / 2) + " chapters."
    $ Armchairs_OBJ.effect = ">Your imagination has improved."
    $ Armchairs_OBJ.chapters = 20
    $ Armchairs_OBJ.cost = 250
    $ Armchairs_OBJ.picture = "01_hp/18_store/books/11.png"
    
    if not hasattr(renpy.store,'Dear_Wifu_OBJ'): #important!
        $ Dear_Wifu_OBJ = fiction_book()
    $ Dear_Wifu_OBJ.id = "Dear_Wifu"
    $ Dear_Wifu_OBJ.name = "\"My dear waifu\""
    $ Dear_Wifu_OBJ.book_description = "{size=-4}BY AKABUR{/size}\n" "Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"? " + str(Dear_Wifu_OBJ.chapters) + " chapters."
    $ Dear_Wifu_OBJ.effect = ">Your imagination has improved."
    $ Dear_Wifu_OBJ.chapters = 20
    $ Dear_Wifu_OBJ.cost = 300
    $ Dear_Wifu_OBJ.picture = "01_hp/18_store/books/12.png"
    
    
    $ Galadriel_I_OBJ.chapter_description = [
        "Galadriel - a gentle and gracious elven princess is introduced into the story.",
        "Galadriel's father - King Methis and his childhood friend Mofothelis are introduced into the story.",
        "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis.",
        "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle.",
        "King Methis dismisses her daughter's \"foolish\" complaints. Galadriel decides to run away.",
        "Galadriel manages to leave the royal residence at night unnoticed...",
        "King Methis is furious about his daughter's escape. He decides to personally lead the search party.",
        "Galadriel rides her mare \"white dove\" through the forest. The Princess enjoys her freedom... After a while she meets a rather handsome human nobleman on a horse...",
        "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries. He makes her laugh. Suddenly the nobleman attacks the princess and knocks her out!...",
        "Galadriel comes about. To her horror she realizes that the nobleman is having his way with her. Galadriel is screaming for help but The handsome man keeps on raping her.",
        "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously.",
        "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop.",
        "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen.",
        "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage.",
        "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food.",
        "Galadriel is starting to feel hopeful but it does not last. Soon she realizes what kind of establishment this is: a whorehouse.",
        "The elven princess is forced to work as a whore. She detests her new life but has very little choice.",
        "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasional dwarf - she spreads her legs for everyone.",
        "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel.",
        "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-"
    ]
    
    $ Galadriel_II_OBJ.chapter_description = [
        "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly.",
        "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel.",
        "The Elven Princess-Whore knows nothing of the life outside the of walls of the brothel. But it does not affect her determination to escape.",
        "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel.",
        "Galadriel soon gets lost in the vast city and is forced to spend the night on the street.",
        "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly.",
        "The Pregnant Galadriel offers her company to a couple of filthy looking homeless men in exchange for food. She spends the night with them.",
        "Galadriel realizes that her live back in the brothel was a heaven compared to the live she's been leading for the past several days. She decides to return.",
        "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back.",
        "Galadriel is, yet again, warm, clean and well fed. She is glad to be back and as popular as ever.",
        "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now...",
        "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him.",
        "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her.",
        "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off.",
        "Galadriel recognizes the man as her father - King Methis. Only now he realizes that the pregnant whore he fucked for hours is his daughter.",
        # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
        "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face...",
        "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed.",
        "It takes the elven princess several minutes to realize that she was never pregnant. The entire adventure was nothing but a dream.",
        "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis.",
        "{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}"
    ]

    $ Armchairs_OBJ.chapter_description = [
        "A family of noble northmen is introduced into the story.",
        "The royal family and the king are introduced into the story.",
        "Another family is introduced into the story.",
        "Some incest action between a brother and his sister, the queen, is taking place.",
        "Attempted child murder takes place. The kid barely survives and is now in a coma.",
        "Some more characters are introduced into the story.",
        "Some characters hatch an evil scheme against some other characters.",
        "The king gets poisoned and dies. Some more brother on sister incest takes place.",
        "A certain character you've been especially rooting for gets executed.",
        "Some new characters are introduced into the story.",
        "Some female characters get raped and then killed brutally.",
        "Some more members of the noble family of northmen find their untimely demise.",
        "Some more women get raped. Some of them manage to survive. (Surely only to get raped some more later,.", 
        "The characters you hate clash in an epic battle against the characters you are rooting for.",
        "Most of the characters you hate survive the battle. Every single character you were rooting for is dead.",
        "Some more rapes take place, then some more murders... (You don't even care anymore...)", 
        "A new group of characters is introduced into the story. You sort of starting to root for one of them.",
        "The character you were rooting for falls in love with a pretty girl.",
        "The character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well.",
        "A new race of half-frozen undead monsters is introduced into the story. To be continued..."
    ]


    $ Books_OBJ = silver_book_lib()
    $ Books_OBJ.read_books.extend([
        Copper_Book_OBJ,
        Bronze_Book_OBJ,
        Silver_Book_OBJ,
        Golden_Book_OBJ
    ])
    $ Books_OBJ.write_books.extend([
        Speedwriting_Beginners_OBJ,
        Speedwriting_Amateurs_OBJ,
        Speedwriting_Advanced_OBJ,
        Speedwriting_Experts_OBJ
    ])
    $ Books_OBJ.fiction_books.extend([
        Galadriel_I_OBJ,
        Galadriel_II_OBJ,
        Armchairs_OBJ,
        Dear_Wifu_OBJ
    ])
    
    
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
            $ books_menu_list = Books_OBJ.get_edu()
        "-Fiction books-":
            label fiction_books_menu:
            $ books_menu_list = Books_OBJ.get_fic()
        "-Never mind-":
            jump desk
    python:
        books_menu = []
        for book in books_menu_list:
            if book.purchased:
                if book.done:
                    books_menu.append((book.getMenuTextDone(),book))
                else:
                    books_menu.append((book.getMenuText(),book))
        books_menu.append(("-Never mind-", "nvm"))
        BookOBJ = renpy.display_menu(books_menu)
    if BookOBJ == "nvm":
        jump books_list
    else:
        jump handle_book_selection

label handle_book_selection:
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
    else:
        menu:
            "-Read the book-":
                hide screen gift
                jump check_book_order
            "-Never mind-":
                hide screen gift
    if BookOBJ in Books_OBJ.get_edu():
        jump books_on_improvement
    if BookOBJ in Books_OBJ.get_fic():
        jump fiction_books_menu
    else:
        jump books_list

label check_book_order:
    if BookOBJ in Books_OBJ.read_books:
        if (BookOBJ.id == "Copper_Book") or (BookOBJ.id == "Bronze_Book" and Books_OBJ.isDone("Copper_Book")) or (BookOBJ.id == "Silver_Book" and Books_OBJ.isDone("Bronze_Book")) or (BookOBJ.id == "Golden_Book" and Books_OBJ.isDone("Silver_Book")):
            jump reading_book
    
    if BookOBJ in Books_OBJ.write_books:
       if (BookOBJ.id == "Speedwriting_Beginners") or (BookOBJ.id == "Speedwriting_Amateurs" and Books_OBJ.isDone("Speedwriting_Beginners")) or (BookOBJ.id == "Speedwriting_Advanced" and Books_OBJ.isDone("Speedwriting_Amateurs")) or (BookOBJ.id == "Speedwriting_Experts" and Books_OBJ.isDone("Speedwriting_Advanced")):
            jump reading_book
    
    if BookOBJ in Books_OBJ.fiction_books:
        if (BookOBJ.id == "Galadriel_II" and Books_OBJ.isDone("Galadriel_I")):
            jump reading_book
        elif BookOBJ.id != "Galadriel_II":
            jump reading_book
    
    m "Reading books out of order won't do me any good."

    jump books_list

label reading_book:
    stop music fadeout 2.0
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        
    if fire_in_fireplace:   #Shows Genie reading a book near the fireplace.
        hide screen chair
        hide screen genie
        show screen reading_near_fire
        with Dissolve(0.3)
    else:                   #Shows Genie reading a book near the window.
        hide screen chair
        hide screen genie
        show screen reading
        with Dissolve(0.3)
    
    if raining:
        ">You read a book called [BookOBJ.name], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [BookOBJ.name]..."

    call read_book
    if _return == "DONE":
        jump book_complete
    call book_speed_check
    $ speed_check = _return
    if speed_check >= 1:
        call read_book
        if _return == "DONE":
            jump book_complete
    if speed_check == 2:
        call read_book
        if _return == "DONE":
            jump book_complete


    if raining:
        if not fire_in_fireplace:
            ">The rain outside of the tower calms your mood and you feel like keeping on reading..."
            ">You try to keep on reading but after a while you realize that the air in your chambers is too damp for your liking."
        else:
            ">The rain outside of your tower calms your mood and you feel like keeping on reading..."
            call read_book
            if _return == "DONE":
                jump book_complete
    
    if fire_in_fireplace:
        show screen done_reading_by_fire
        hide screen reading_near_fire
    else:
        show screen done_reading  
        hide screen reading
    
    if daytime:
        jump night_start
    else: 
        jump day_start

label book_speed_check:
    if s_reading_lvl == 1: #33% chance
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing purpose only.
        if speed_dummies == 1: #Success.
            ">Implementing some tricks you picked up in the \"Speed reading for dummies\" book allows you to save time and keep on reading."
            return 1
    if s_reading_lvl == 2: #66% chance
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing purpose only.
        if speed_dummies > 1: #Success.
            ">Implementing speed reading techniques allows you to save time and keep on reading."
            return 1
    if s_reading_lvl == 3: #100% chance
        ">Implementing speed reading techniques allows you to save time and keep on reading."
        return 1
    if s_reading_lvl > 3: #Double 100% chance
        ">Implementing advanced speed reading techniques lets you blaze through the book."
        return 2
    return 0
    

label read_book:
    if BookOBJ.progress >= BookOBJ.chapters:
        return "DONE" #prevents cases where book is done but read_book was called
    call read_chapter
    if BookOBJ.progress >= BookOBJ.chapters:
        return "DONE" #this is here to indicate completeing a book without escapeing the call otherwise renpy would treat a jump or call as a recursive action
    else:
        ">There are still some chapters left."
        if cheat_reading:
            #">You are a cheater so you get to keep on reading."
            call read_book
    return
    
label read_chapter:
    $ BookOBJ.progress += 1 
    if BookOBJ in Books_OBJ.read_books or BookOBJ in Books_OBJ.write_books:
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You've completed \"chapter [BookOBJ.progress]\" of the book."
    elif BookOBJ in Books_OBJ.fiction_books:
        if BookOBJ.id == "Dear_Wifu":
            call waifu
        else:
            $tmp_desc = BookOBJ.getChapterDesc()
            "[tmp_desc]"
            if not (BookOBJ.progress >= BookOBJ.chapters):
                $ BookOBJ.progress += 1
                $tmp_desc = BookOBJ.getChapterDesc()
                "[tmp_desc]"
        
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">You've completed \"chapter [BookOBJ.progress]\" of the book."""
    return

label book_complete:
    if fire_in_fireplace:
        show screen done_reading_by_fire
    else:
        show screen done_reading

    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">That was the last chapter, You finished the entire book."
    if BookOBJ.id == "Dear_Wifu":
        jump waifu_completed
    if BookOBJ.id == "Armchairs":
        g4 "What a pile of garbage! I hate the guy who wrote this crap!"
        m "Although all those rapes gave me a few ideas..."
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    "[BookOBJ.effect]" # ex. ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."
        
    if BookOBJ in Books_OBJ.fiction_books:
        $ imagination += 1
    if BookOBJ in Books_OBJ.read_books:
        $ s_reading_lvl += 1
    if BookOBJ in Books_OBJ.write_books:
        $ speedwriting += 1
        $ concentration += 1
    
    $ BookOBJ.done = True

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading
    
    if daytime:
        jump night_start
    else: 
        jump day_start
    
    
init python:
    class silver_book_lib(object):
        read_books = []
        write_books = []
        fiction_books = []
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def get_all(self):
            all_books = []
            all_books.extend(self.read_books)
            all_books.extend(self.write_books)
            all_books.extend(self.fiction_books)
            return all_books
        def get_edu(self):
            edu_books = []
            edu_books.extend(self.read_books)
            edu_books.extend(self.write_books)
            return edu_books
        def get_fic(self):
            return self.fiction_books
            
        
        def purchase(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    book.purchased = True
        
        def get_purchased(self):
            purchased_books = []
            for book in self.get_all():
                if book.purchased:
                    purchased_books.append(book)
            return purchased_books
        
        def isDone(self, id=""):
            for book in self.get_all():
                if book.id == id:
                    return book.done
            return None


    class silver_book(object):
        id = ""
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
           return self.chapter_description[self.progress-1] #"Chapter "+str(self.progress)+": "+
