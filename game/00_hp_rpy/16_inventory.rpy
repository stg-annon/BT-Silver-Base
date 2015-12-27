label inventory:
    menu:
        "-Books-":
            if "book_01" in books: 
                menu:
                    "-Read book # 1-" if book_01_units <= 19:
                        pass
                    "-Read book # 1 (Finished)-" if book_01_units == 20:
                        ">You already finished this one."
                        
            "You don't own a single book."
            jump inventory
        "-Gifts-":
            pass
        "-Never mind-":
            jump cupboard