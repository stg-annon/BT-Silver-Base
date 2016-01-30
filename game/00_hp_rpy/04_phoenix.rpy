label phoenix:
    if bird_interact == 2: # Counts how many times you have interacted with the bird.
        stop music fadeout 3.0
        $ bird_interact += 1 # Counts how many times you have interacted with the bird.
        show screen blktone8
        with d7
        "I've removed Akabur's message from the game."
        "Interacting with the bird now brings about some scenes."
        "Sometimes it'll be as easy as petting her.  Others, you might need to make Hermione more horny."
        "I've also implemented a talk button (although I haven't fully figured out how to use it)."
        "You can get different scenes for talking to her multiple times (there are a few depending on Hermione's whoring level)."
        "Please remember to check back on the /vg/ page for more updates!"
        "Hope you enjoy it!"
        hide screen blktone8
        with d3
        call music_block
        jump day_main_menu
    menu:
        "-Examine-" if not bird_examined:
            $ bird_examined = True
            hide screen genie
            $ tt_xpos=270
            $ tt_ypos=90
            show screen genie_stands
            show screen chair_02 #Empty chair near the desk.
            show screen desk
            with Dissolve(0.5)
            m "Hm....."
            m "Even this weird looking bird radiates magic..."
            show screen genie
            hide screen genie_stands
            hide screen chair_02 #Empty chair near the desk.
            hide screen desk
            with Dissolve(0.5)
            jump day_main_menu
        "-Feed the bird-" if not phoenix_is_feed and bird_examined:
            $ phoenix_is_feed = True
            jump feeding
        "-Pet the bird-" if bird_examined:
            jump petting
        "-Talk to the bird-" if bird_examined and fawkes_intro_done: #FIXED CODE DUPLICATION HERE
            jump talkingfawkes
        "-Never mind-":
            call screen main_menu_01


### FEEDING ###
label feeding:
    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
    hide screen genie
    show screen feeding
    with Dissolve(0.3)
    pause 1
    show screen phoenix_food
    $ genie_speaks = renpy.random.randint(1, 3) #Determines what phrase if any Genie will use.
    if genie_speaks == 1:
        m "There you go..."
    elif genie_speaks == 2 and fawkes_intro_done:
        m "So do you even like this stuff?"
        faw "It keeps me alive."
        m "That's a great outlook on life."
    elif genie_speaks == 3 and fawkes_intro_done:
        faw "Have you ever wondered if dogs get tired of having the same dogfood every day?"
        m "Not really."
        faw "Well I sure wish you could buy me new food!"
        g4 "There isn't any in the shop!"
        m "Sometimes I wonder why I put up with you..."
    else:
        pause .5
    show screen genie
    hide screen feeding
    with Dissolve(0.3)
    call screen main_menu_01