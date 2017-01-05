label __init_variables:
    
    $ reset_books = False
    #$ reset_books = True
    
    if not hasattr(renpy.store,'Dear_Wifu_OBJ'): #important!
        $ Dear_Wifu_OBJ = fiction_book(
            id = "Dear_Wifu",
            name = "\"My dear waifu\"",
            book_description = "{size=-4}BY AKABUR{/size}\n" "Relive the glory of your high school days. Your step sister Shea, teacher Ms.Stevens or the mysterious library girl? Who will become your ultimate \"waifu\"?",
            effect = ">Your imagination has improved.",
            chapters = 20,
            cost = 300,
            picture = "01_hp/18_store/books/12.png"
        )
    
    if not hasattr(renpy.store,'books_OBJ'): #important!
        $ books_OBJ = silver_book_lib(
            read_books = [
                educational_book(
                    id = "Copper_Book",
                    name = "\"Copper book of spirit\"",
                    book_description = "\nThis book contains various tips on how to improve one's efficiency.",
                    effect = ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when reading.",
                    chapters = 10,
                    cost = 40,
                    picture = "01_hp/18_store/books/1-8.png"
                ),
                educational_book(
                    id = "Bronze_Book",
                    name = "\"Bronze book of spirit\"",
                    book_description = "\nThis book contains various tips on how to improve one's efficiency.",
                    effect = ">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when reading.",
                    chapters = 10,
                    cost = 80,
                    picture = "01_hp/18_store/books/1-8.png"
                ),
                educational_book(
                    id = "Silver_Book",
                    name = "\"Silver book of spirit\"",
                    book_description = "\nThis book contains various tips on how to improve one's efficiency.",
                    effect = ">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when reading.",
                    chapters = 10,
                    cost = 90,
                    picture = "01_hp/18_store/books/1-8.png"
                ),
                educational_book(
                    id = "Golden_Book",
                    name = "\"Golden book of spirit\"",
                    book_description = "\nThis book contains various tips on how to improve one's efficiency.",
                    effect = ">You have mastered your spirit and from now on you shall always complete an additional chapter when reading.",
                    chapters = 10,
                    cost = 100,
                    picture = "01_hp/18_store/books/1-8.png"
                )
            ],
            write_books = [
                educational_book(
                    id = "Speedwriting_Beginners",
                    name = "\"Speedwriting for beginners\"",
                    book_description = "\nThis book contains a bunch of very basic techniques used to improve one's ability to write quickly.",
                    effect = ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.",
                    chapters = 10,
                    cost = 90,
                    picture = "01_hp/18_store/books/1-8.png"
                ),
                educational_book(
                    id = "Speedwriting_Amateurs",
                    name = "\"Speedwriting for amateurs\"",
                    book_description = "\nThis book contains intermediate techniques used to improve one's ability to write quickly.",
                    effect = ">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when doing paperwork.",
                    chapters = 10,
                    cost = 100,
                    picture = "01_hp/18_store/books/1-8.png"
                ),
                educational_book(
                    id = "Speedwriting_Advanced",
                    name = "\"Speedwriting for advanced writers\"",
                    book_description = "\nThis book contains advanced techniques used to improve one's ability to write quickly.",
                    effect = ">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when doing paperwork.",
                    chapters = 10,
                    cost = 130,
                    picture = "01_hp/18_store/books/1-8.png"
                ),
                educational_book(
                    id = "Speedwriting_Experts",
                    name = "\"Speedwriting for experts\"",
                    book_description = "\nThis book contains expert techniques used to improve one's ability to read quickly.",
                    effect = ">You have become a true master of speedwriting and from now on you shall always complete an additional chapter when doing paperwork.",
                    chapters = 10,
                    cost = 175,
                    picture = "01_hp/18_store/books/1-8.png"
                )
            ],
            fiction_books = [
                fiction_book(
                    id = "Galadriel_I",
                    name = "\"The Tale of Galadriel. Book I.\"",
                    book_description = "This book tells a story of an elven princess who defies traditions of her people and chooses to forge her own destiny. Or does it?",
                    effect = ">Your imagination has improved.",
                    chapters = 20,
                    cost = 100,
                    picture = "01_hp/18_store/books/9.png",
                    chapter_description = [
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
                        "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-",
                    ]
                ),
                fiction_book(
                    id = "Galadriel_II",
                    name = "\"The Tale of Galadriel. Book II.\"",
                    book_description = "This book tells a story of an elven princess who defies traditions of her people and chooses to forge her own destiny. Or does it?",
                    effect = ">Your imagination has improved.",
                    chapters = 20,
                    cost = 200,
                    picture = "01_hp/18_store/books/10.png",
                    chapter_description = [
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
                        "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face...",
                        "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed.",
                        "It takes the elven princess several minutes to realize that she was never pregnant. The entire adventure was nothing but a dream.",
                        "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis.",
                        "{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}",
                    ]
                ),
                fiction_book(
                    id = "Armchairs",
                    name = "\"The game of Armchairs\"",
                    book_description = "An epic tale of betrayal, murder and rape. Then some more murder, some more betrayal and some more rape.",
                    effect = ">Your imagination has improved.",
                    chapters = 20,
                    cost = 250,
                    picture = "01_hp/18_store/books/11.png",
                    chapter_description = [
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
                        "Some more rapes take place, then some more murders... (You don't even care anymore...,", 
                        "A new group of characters is introduced into the story. You sort of starting to root for one of them.",
                        "The character you were rooting for falls in love with a pretty girl.",
                        "The character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well.",
                        "A new race of half-frozen undead monsters is introduced into the story. To be continued...",
                    ]
                ),
                Dear_Wifu_OBJ
            ]
        )
    
    if not hasattr(renpy.store,'cheat_reading'): #important!
        $ cheat_reading = False
    
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
    "-Educational books-" :
        label books_on_improvement:
        python:
            edu_menu = []
            for i in books_OBJ.get_edu():
                if i.purchased:
                    if i.done:
                        edu_menu.append((i.getMenuTextDone(),i))
                    else:
                        edu_menu.append((i.getMenuText(),i))
            edu_menu.append(("-Never mind-", "nvm"))
            bookOBJ = renpy.display_menu(edu_menu)
        if bookOBJ == "nvm":
            jump books_list
        else:
            jump handle_book_selection
    "-Fiction books-":
        label fiction_books_menu:
        python:
            fic_menu = []
            for i in books_OBJ.get_fic():
                if i.purchased:
                    if i.done:
                        fic_menu.append((i.getMenuTextDone(),i))
                    else:
                        fic_menu.append((i.getMenuText(),i))
            fic_menu.append(("-Never mind-", "nvm"))
            bookOBJ = renpy.display_menu(fic_menu)
        if bookOBJ == "nvm":
            jump books_list
        else:
            jump handle_book_selection
    "-Never mind-":
        jump desk
        
label handle_book_selection:
    $ the_gift = bookOBJ.picture
    show screen gift
    with d3
    "[bookOBJ.book_description]"
    if bookOBJ.done:
        if bookOBJ == Armchairs_OBJ:
            m "Why would I want to do this to myself again?"
        else:
            ">You already finished this one."
        hide screen gift
        return
        jump books_list
    else:
        menu:
            "-Read the book-":
                hide screen gift
                jump check_book_order
            "-Never mind-":
                hide screen gift
                jump books_list
    
label check_book_order:
    if bookOBJ in books_OBJ.read_books:
        if (bookOBJ.id == "Copper_Book")or(bookOBJ.id == "Bronze_Book" and books_OBJ.isDone("Copper_Book"))or(bookOBJ.id == "Silver_Book" and books_OBJ.isDone("Bronze_Book"))or(bookOBJ.id == "Golden_Book" and books_OBJ.isDone("Silver_Book")):
            jump reading_book
    
    if bookOBJ in books_OBJ.write_books:
       if (bookOBJ.id == "Speedwriting_Beginners")or(bookOBJ.id == "Speedwriting_Amateurs" and books_OBJ.isDone("Speedwriting_Beginners"))or(bookOBJ.id == "Speedwriting_Advanced" and books_OBJ.isDone("Speedwriting_Amateurs"))or(bookOBJ.id == "Speedwriting_Experts" and books_OBJ.isDone("Speedwriting_Advanced")):
            jump reading_book
    
    if bookOBJ in books_OBJ.fiction_books:
        if (bookOBJ.id == "Galadriel_II" and books_OBJ.isDone("Galadriel_I")):
            jump reading_book
        elif bookOBJ.id != "Galadriel_II":
            jump reading_book
    
    m "Reading books out of order won't do me any good."
    
    jump books_list
    
    
label reading_book:
    stop music fadeout 2.0
    if raining:
        play weather_sound "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
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
        ">You read a book called [bookOBJ.name], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [bookOBJ.name]..."
    
    call read_book
    if bookOBJ.progress >= bookOBJ.chapters:
        jump book_complete
    call book_speed_check
    
    if raining:
        if not fire_in_fireplace:
            ">The rain outside of the tower calms your mood and you feel like keeping on reading..."
            ">You try to keep on reading but after a while you realize that the air in your chambers is too damp for your liking."
        else:
            ">The rain outside of your tower calms your mood and you feel like keeping on reading..."
            call read_book
            if bookOBJ.progress >= bookOBJ.chapters:
                jump book_complete
    
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading
    
    if daytime:
        jump night_start
    else: 
        jump day_start
    
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
    
label book_done_a_check_fire:
    if fire_in_fireplace:
        show screen done_reading_02  
        hide screen reading_near_fire
    else:
        show screen done_reading  
        hide screen reading
    return
    
    
    
label read_book:
    call read_chapter
    if bookOBJ.progress >= bookOBJ.chapters:
        return
    else:
        ">There are still some chapters left."
        if cheat_reading:
            #">You are a cheater so you get to keep on reading."
            call read_book
    return
    
    
label book_speed_check:
    if s_reading_lvl == 1: #30% chance
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing purpose only.
        if speed_dummies == 1: #Success.
            ">Implementing some tricks you picked up in the \"Speed reading for dummies\" book allows you to save time and keep on reading."
            call read_book
            if bookOBJ.progress >= bookOBJ.chapters:
                jump book_complete
    if s_reading_lvl == 2: #50% chance
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing purpose only.
        if speed_dummies == 1: #Success.
            ">Implementing speed reading techniques allows you to save time and keep on reading."
            call read_book
            if bookOBJ.progress >= bookOBJ.chapters:
                jump book_complete
    if s_reading_lvl > 2: #100% chance
        ">Implementing speed reading techniques allows you to save time and keep on reading."
        call read_book
        if bookOBJ.progress >= bookOBJ.chapters:
            jump book_complete
    return
    

    
    
label read_chapter:
    $ bookOBJ.progress += 1 
    if bookOBJ in books_OBJ.read_books or bookOBJ in books_OBJ.write_books:
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You've completed \"chapter [bookOBJ.progress]\" of the book."
    elif bookOBJ in books_OBJ.fiction_books:
        if bookOBJ.id == "Dear_Wifu":
            call waifu
        else:
            $tmp_desc = bookOBJ.getChapterDesc()
            "[tmp_desc]"
        
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">You've completed \"chapter [bookOBJ.progress]\" of the book."
    return
    

label book_complete:
    call book_done_a_check_fire
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">That was the last chapter, You finished the entire book."
    if bookOBJ.id == "Dear_Wifu":
        jump waifu_completed
    if bookOBJ.id == "Armchairs":
        g4 "What a pile of garbage! I hate the guy who wrote this crap!"
        m "Although all those rapes gave me a few ideas..."
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    "[bookOBJ.effect]" # ex. ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."
        
    if bookOBJ in books_OBJ.fiction_books:
        $ imagination += 1
    if bookOBJ in books_OBJ.read_books:
        $ s_reading_lvl += 1
    if bookOBJ in books_OBJ.write_books:
        $ speedwriting += 1
        $ concentration += 1
    
    $ bookOBJ.done = True
    
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
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
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
           
           
