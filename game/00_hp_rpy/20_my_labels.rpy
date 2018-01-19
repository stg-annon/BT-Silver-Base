
### Misc Labels ###
label blk_tone:
    show screen bld1
    show screen blktone
    with d3
    return
label hide_blk_tone:
    hide screen bld1
    hide screen blktone
    with d3
    return
label ctc_wPause:
    show screen ctc
    with d3
    pause
    hide screen ctc
    with d1
    return


### Snape Labels ###
label snape_reset: #Resets all the flags for the Snape's full length sprite.
    $ s_eyes_01 = False        #Triggers different set of eyes emotions to show.
    $ s_eyes_02 = False        #Triggers different set of eyes emotions to show.
    $ s_eyes_closed_01 = False #Triggers different set of eyes emotions to show.
    $ s_eyes_closed_02 = False #Triggers different set of eyes emotions to show.
    $ s_eyes_weird = False     #Triggers different set of eyes emotions to show.
    return

