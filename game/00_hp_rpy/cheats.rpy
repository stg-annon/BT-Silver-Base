label cheats_ht:
    menu:
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
            $ books = ["book_01", "book_02", "book_03", "book_04",  "book_05", "book_06", "book_07", "book_08", "book_09", "book_10", "book_11", "book_12", "book_13", "book_14", "book_15", "book_16", "book_17"]
            "Obtained Books."
            jump cheats_ht
        

        "-Slytherin Points-":
            $ slytherin +=10000
            "10,000 to Slytherin!"
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
        "-Nevermind-":
            jump day_main_menu
            
label cheats_pt:
    menu:
        "-Gold-":
            $ gold +=50000
            "Obtained 50,000g"
            jump cheats_pt
        "-Nevermind-":
            jump house
