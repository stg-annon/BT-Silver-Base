label cheats_ht:
    menu:
        "-Turn on Cheats-":
            menu:
                "This will show you helpful tips throughout the game."
                "-Turn on-":
                    $ cheats_active = True
                    jump cheats_ht
                "-Turn off-":
                    $ cheats_active = False
                    jump cheats_ht
        "-Hermione Cheats-":
            label cheats_ht_hermione:
            menu:
                "-Reset Hermione's mood-":
                    $ mad = 0
                    ">Hermione is no longer mad at you."
                    jump cheats_ht_hermione
                "-Max Whoring-":
                    $ whoring = 24
                    ">Hermione is now a giant slut."
                    jump cheats_ht_hermione
                    
                "-Increase Whoring-":
                    $ whoring += 1
                    ">Hermione became more depraved..."
                    jump cheats_ht_hermione
                "-Decrease Whoring-":
                    $ whoring -= 1
                    "Hermione recovered some of her dignity"
                    jump cheats_ht_hermione
                "-force public requests-":
                    $ force_unlock_pub_favors = True
                    $ touched_by_boy = True
                    $ lock_public_favors = False
                    ">Public favours unlocked!"
                    jump cheats_ht_hermione
                "-Add all costumes-":
                    python:
                        for i in hermione_outfits_list:
                            i.purchased = True
                    ">All of Hermione's costumes have been unlocked"
                    jump cheats_ht
                "-Toggle Breast Expansion-":
                    if hermione_perm_expand:
                        $ hermione_perm_expand = False
                        "Hermione's breasts shrink..."
                    else:
                        $ hermione_perm_expand = True
                        "Hermione's breasts grow..."
                    jump cheats_ht

                "-Toggle Futa Hermione-":
                    if hermione_futa:
                        $ hermione_futa = False
                        "Hermione's cock shrinks away..."
                    else:
                        $ hermione_futa = True
                        "Hermione's grows a... dick!"
                    jump cheats_ht
                "-never mind-":
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
                "-never mind-":
                    jump cheats_ht
        "-Add all normal potions-":
            $ p_inv = ["Cat Transformation Potion", "Ass Expansion Potion", "Breast Expansion Potion", "Cum Addiction Potion", "Transparency Potion","Luna Transformation Potion", "Hypno Potion"] #all potions
            ">All potions added (Does not include Snape's potions)"
            jump cheats_ht
        "-Gold (+50,000g)-":
            $ gold += 50000
            "Obtained 50,000g."
            jump cheats_ht
        "-Slytherin Points (+10,000)-":
            $ slytherin +=10000
            "10,000 to Slytherin!"
            jump cheats_ht
        "-Reset ALL Luna content-":
            $ hat_known = False
            call luna_init
            ">Luna content reset!"
            jump cheats_ht
        "-Map-":
            "Map added to inventory!"
            $ cataloug_found = True
            jump cheats_ht
        "-Never mind-":
            jump day_main_menu
