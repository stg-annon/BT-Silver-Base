label phoenix:
    if bird_interact == 2: # Counts how many times you have interacted with the bird.
        stop music fadeout 3.0
        $ bird_interact += 1 # Counts how many times you have interacted with the bird.
        show screen blktone8
        with d7
        m "Here you are."
        hide screen blktone8
        with d3
        call music_block
        jump day_main_menu
    jump phoenix_menu