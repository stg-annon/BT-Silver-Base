label day_01:
    "*Knock-knock-knock!*"
    her "Hello, professor. Did you want to see me?"
    m "Go away!"
    jump day_main_menu
    
    
label day_02_2:    
    her "Professor Snape gave me a bad grade for no good reason today!"
    menu:
        "That's no big deal.":
            $ teachers_pet +=1
            
        "I'll talk with him.":
            $ genies_slut = 0
            her "Thank you!"
        "You need show respect more to your teachers!":
            pass
            
label day_07:
    her "I'm a little worried about the exam today."
    m "Don't worry, you'll be fine!"
    "Hermione leaves"
    jump day_main_menu
    
label day_07_02:
    if knowledge >= 5:
        $ test_aced = True
    elif knowledge >= 3:
        $ test_passed = True
    else:
        $ test_failed = True
    her "I wonder how I did on my test..."
    jump home_assignment #Moment after all cutscenes, before you sent Hermione home.
    
label day_09:
    her "Today I will know my test results. I'm so worried!"
    "Hermione leaves."
    jump day_main_menu
    
label day_09_02:
    if test_aced:
        her "I aced the test!!!"
    elif test_passed:
        her "Well, I didn't fail..."
    elif test_failed:
        her "I failed the test! How terrible!"
    $ test_aced = False
    $ test_passed = False
    $ test_failed = False
    jump home_assignment

        