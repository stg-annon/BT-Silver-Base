#LUNA PLOT
#Turned into a bitchy Slytherin by the sorting hat. Willing to do anything for money/fame/status. Incredibly vain

#Don't forget to incorporate the quibbler

#LUNA MECHANICS


label luna_init:
    $ luna_busy = False
    $ luna_known = False
    $ luna_unlocked = False
    $ l_genie_name = "Old man"
    $ luna_name = "Miss Lovegood"

    $ luna_dom = 0
    $ luna_sub = 0
    $ luna_gold = 0
    $ luna_skirt_level = 1
    $ luna_top_level = 1
    $ luna_corruption = 0
    $ luna_arousal = 0

    $ luna_base = "01_hp/13_characters/luna/body/base/base_01.png" 
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_hair = 1
    $ luna_l_arm = 1
    $ luna_r_arm = 1
    $ luna_xpos = 600
    $ luna_ypos = 0
    $ luna_mouth = "01_hp/13_characters/luna/body/face/mouth/mouth_1.png" 
    $ luna_eye = "01_hp/13_characters/luna/body/face/eye/eye_1.png" 
    $ luna_eyebrow = "01_hp/13_characters/luna/body/face/eyebrow/eyebrow_1.png" 
    $ luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_1.png" 
    $ luna_glasses = "01_hp/13_characters/luna/misc/glasses.png" 
    $ luna_top = "01_hp/13_characters/luna/clothes/uniform/top_0.png" 
    $ luna_acc = "01_hp/13_characters/luna/misc/jewel.png" 
    $ luna_skirt = "01_hp/13_characters/luna/clothes/uniform/skirt_0.png" 
    $ luna_panties = "01_hp/13_characters/luna/clothes/underwear/panties.png" 
    $ luna_bra = "01_hp/13_characters/luna/clothes/underwear/bra.png" 
    $ luna_cum = 1
    $ luna_wear_cum = False
    $ luna_wear_cum_under = False
    $ luna_tears = 0
    $ luna_zorder = 5
    $ luna_flip = 1

    $ luna_chibi_image = "01_hp/13_characters/luna/chibis/luna_stand.png" 
    $ luna_chibi_xpos = 500
    $ luna_chibi_ypos = 250
    $ luna_chibi_zorder = 4

    $ luna_wear_glasses = False
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_skirt = True
    $ luna_wear_top = True
    $ luna_wear_acc = True

    $ luna_reverted = False
return

label luna_day_flags:
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_1.png"
    $ luna_busy = False
return

label luna_night_flags:
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_busy = False
return

label luna_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = luna_speed, loiter = False,redux_pause = 0):
    hide screen luna_walk
    hide screen luna_walk_f
    $ walk_xpos = pos1 #(From)
    $ walk_xpos2 = pos2 #(To)
    $ luna_chibi_ypos = 250
    $ luna_speed = speed #Speed of walking animation. (lower = faster)
    hide screen luna_blink
    hide screen luna_blink_f
    if pos1 > pos2: #right to left (luna_walk)
        show screen luna_walk
        $ tmp = luna_speed - redux_pause
        pause tmp
        $ luna_chibi_xpos = pos2
        hide screen luna_walk
        if loiter:
            show screen luna_blink
    else: #left to right (luna_walk_f)
        show screen luna_walk_f
        $ tmp = luna_speed - redux_pause
        pause tmp
        $ luna_chibi_xpos = pos2
        hide screen luna_walk_f
        if loiter:
            show screen luna_blink_f
    return
    
label luna_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen luna_02
        hide screen luna_01_f
        hide screen luna_blink
        hide screen luna_blink_f
        with Dissolve((dissolveTime/10))
    else:
        hide screen luna_02
        hide screen luna_01_f
        hide screen luna_blink
        hide screen luna_blink_f
    return

label luna_door:
    call luna_reset
    $ renpy.play('sounds/door.mp3')
    $ luna_chibi("stand")
    if luna_dom >= luna_sub:
        if luna_dom >= 4:
            call luna_main("[l_genie_name]...", 9, 2, 2, 2)
        else:
            call luna_main("[l_genie_name]...", 8, 2, 3, 3)
    else:
        call luna_main("[l_genie_name]...", 1, 1, 4, 2)

label luna_door_menu:
    menu:
        "-Chit Chat-":
            call luna_chitchat
            jump luna_door_menu
        "-favours-":
            if gold <= 100:
                m "Hmmm, I probably need a bit more gold if I want to ask for any favours..."
                jump luna_door_menu
            jump luna_favour_menu
        "-Never mind-":
            jump luna_away

label luna_favour_menu:
    menu:
        "-Talk to me-" if not luna_reverted:
            jump luna_favour_1
        "-Sit on my lap-" if luna_corruption >= 3 and not luna_reverted:
            jump luna_favour_2
        "-Strip for me-" if luna_corruption >= 5 and not luna_reverted:
            jump luna_favour_3
        "-Touch me-" if luna_corruption >= 9 and not luna_reverted:
            if luna_corruption == 9:
                jump luna_reversion_event
            jump luna_favour_4
        "-Touch me with Hermione-" if luna_corruption >= 11 and not luna_reverted:
            jump luna_favour_5
        #"-Suck it-":
            jump luna_favour_6
        #"-Sex-":
            jump luna_favour_7
        "-Never mind-":
            jump luna_door_menu

label luna_summon:
    $ changeLuna(8, 2, 3, 3)
return

label luna_away:
    call luna_reset
    $ luna_busy = True
    $ renpy.play('sounds/door2.mp3')
    hide screen luna
    hide screen luna_chibi
    with d3
    jump day_main_menu

label luna_reset:
    $ luna_flip = 1
    $ luna_l_arm = 1
    $ luna_r_arm = 1
    $ luna_xpos = 600
    $ luna_ypos = 0
    $ luna_chibi_image = "01_hp/13_characters/luna/chibis/luna_stand.png" 
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_chibi_xpos = 500
    $ luna_chibi_ypos = 250
    $ luna_tears = 0
    $ luna_wear_skirt = True
    $ luna_wear_top = True
    $ luna_wear_cum = False 
    $ luna_wear_cum_under = False 
    return

label luna_no_money:
    call luna_main("You expect me to do it for free?", 8, 2, 3, 3)
    call luna_main("Hmph!", 8, 2, 3, 3)
    jump luna_away

###CHIBIS###------------------------------------------------------




###PLOT###--------------------------------------------------------
#After the sex favour, Luna will either return to normal if you choose the sub route or she will become a slytherin dom if you go the dom route
#All the private favours will then have a 4th level unlocked, tailored to either the sub or dom option
