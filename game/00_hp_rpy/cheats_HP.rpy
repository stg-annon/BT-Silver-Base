label cheats_ht:
    menu:
        "-Test new main-":
            jump new_main_menu
        "-Gold-":
            $ gold += 50000
            "Obtained 50,000g."
            jump cheats_ht
        "-Reset Hermione's mood-":
            $ mad = 0
            "Hermione is no longer mad at you."
            jump cheats_ht
        "-Ticket-":
            $ vouchers += 1
            "Obtained Voucher."
            jump cheats_ht
        "-Books-" if day >= 16:
            $ books = ["book_1", "book_2", "book_3", "book_4",  "book_5", "book_6", "book_7", "book_8", "book_9", "book_10", "book_11", "book_12", "book_13", "book_14", "book_15", "book_16", "book_17"]
            "Obtained Books."
            jump cheats_ht
        "-Cheat Reading (off)-" if not cheat_reading:
            $ cheat_reading = True
            jump cheats_ht
        "-Cheat Reading (on)-"if cheat_reading:
            $ cheat_reading = False
            jump cheats_ht
        
        "-Slytherin Points-":
            $ slytherin +=10000
            "10,000 to Slytherin!"
            jump cheats_ht
        
        "-force public requests-":
            $ force_unlock_pub_favors = True
            $ lock_public_favors = False
            "Public favours unlocked!"
            jump cheats_ht
        
        "-Imagination":
             menu:
                "Have you used this cheat already today? (Using it more than once can break the game)"
                "-Yes-":
                    jump cheats_ht 
                "-No-":
                    $ imagination += 1
                    "Your imagination grows!"
                    jump cheats_ht 
        "-Map-":
            "Map added to inventory!"
            $ cataloug_found = True
            jump cheats_ht       
        "-Nevermind-":
            jump day_main_menu
