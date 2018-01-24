

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
    $ the_gift = "01_hp/18_store/01.png"
    show screen gift
    with d3
    "[quest_reward_text]"
    hide screen notes
    hide screen gift
    with d1
    call hide_blk_tone
    return
