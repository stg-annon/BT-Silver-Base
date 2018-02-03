

label open_guide:
    $ renpy.play('sounds/scroll.mp3')
    $ guide_page = 0
    $ guide_show_hint = False
    $ guide_show_next_step = False
    #call update_tip_of_the_day
    $ sQuest_get_map.started = 1 #Testing Purpose only
    $ sQuest_buy_at_shop.started = 1 #Testing Purpose only
    call update_quests
    call update_tip_of_the_day
    call blk_tone
    call screen guide
    label guide_return_point:
        $ renpy.play('sounds/scroll.mp3')
        call hide_blk_tone
        call screen main_menu_01
    

label give_quest_reward:
    call blk_tone
    $ renpy.play('sounds/win2.mp3') 
    show screen notes
    show screen gift
    with d3
    hide screen notes
    pause
    $ menu_y = 0.75 #makes the menu lower so it isn't writing over the image.
    menu:
        "[quest_reward_text]"
        "-Done Reading-":
            pass
    hide screen gift
    $ menu_y = 0.5 #return to default menu align
    with d1
    call hide_blk_tone
    return
