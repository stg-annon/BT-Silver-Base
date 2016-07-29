label cheats_ht:
    menu:
        "-Test new main-":
            jump new_main_menu
        "-Hermione Cheats-":
            label cheats_ht_hermione:
            menu:
                "-Reset Hermione's mood-":
                    $ mad = 0
                    "Hermione is no longer mad at you."
                    jump cheats_ht_hermione
                "-Max Whoring-":
                    $ whoring = 22
                    "Hermione is now a giant slut"
                    jump cheats_ht_hermione
                    
                "-Increase Whoring-":
                    $ whoring += 1
                    "Hermione became more depraved"
                    jump cheats_ht_hermione
                "-Decrease Whoring-":
                    $ whoring -= 1
                    "Hermione recovered some of her dignity"
                    jump cheats_ht_hermione
                "-force public requests-":
                    $ force_unlock_pub_favors = True
                    $ lock_public_favors = False
                    "Public favours unlocked!"
                    jump cheats_ht_hermione
                "-Add all costumes-":
                    python:
                        for i in hermione_outfits_list:
                            i.purchased = True
                    "All of hermioine's costumes have been unlocked"
                    jump cheats_ht
                "-Reset Clothing Scenes-":
                    $ request_jeans = False
                    $ hermione_dribble = False
                    $ request_gryyf_stockings = False
                    $ dribble_equippable = False
                    $ hermione_wetpanties = False
                    $ wetpanties_equippable = False
                    "Clothing scenes reset! Try equipping the jeans or gryffindor stockings at various whoring levels"
                    jump cheats_ht_hermione
                "-back-":
                    jump cheats_ht
        "-Book Cheats-":
            label cheats_ht_books:
            menu:
                "-Max Imagination":
                    $ imagination = 5
                    "Your imagination grows!"
                    jump cheats_ht_books
                "-Cheat Reading (off)-" if not cheat_reading:
                    $ cheat_reading = True
                    jump cheats_ht_books
                "-Cheat Reading (on)-"if cheat_reading:
                    $ cheat_reading = False
                    jump cheats_ht_books
                "-All Books-" if day >= 16:
                    python:
                        for i in book_list:
                            i.purchased = True
                    "Obtained All Books."
                    jump cheats_ht_books
                "-back-":
                    jump cheats_ht
        "-Add all potions-":
            $ p_inv = ["Cat Transformation Potion", "Ass Expansion Potion", "Breast Expansion Potion", "Cum Addiction Potion", "Transparency Potion","Luna Transformation Potion"] #all potions
            jump cheats_ht
        "-Gold (+50,000g)-":
            $ gold += 50000
            "Obtained 50,000g."
            jump cheats_ht
        "-Ticket-":
            $ vouchers += 1
            "Obtained Voucher."
            jump cheats_ht
        "-Slytherin Points (+10,000)-":
            $ slytherin +=10000
            "10,000 to Slytherin!"
            jump cheats_ht
        "-Map-":
            "Map added to inventory!"
            $ cataloug_found = True
            jump cheats_ht
        "-Nevermind-":
            jump day_main_menu
