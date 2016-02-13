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
    jump phoenix_menu