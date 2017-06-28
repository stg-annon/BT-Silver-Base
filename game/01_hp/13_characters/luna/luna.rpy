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

    $ luna_arrousal = 0
    $ luna_corruption = 0

    $ luna_base = "01_hp/13_characters/luna/body/base/base_01.png" 
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_hair = "01_hp/13_characters/luna/body/head/hair_01.png" 
    $ luna_xpos = 600
    $ luna_ypos = 0
    $ luna_mouth = "01_hp/13_characters/luna/body/face/mouth/mouth_1.png" 
    $ luna_eye = "01_hp/13_characters/luna/body/face/eye/eye_1.png" 
    $ luna_eyebrow = "01_hp/13_characters/luna/body/face/eyebrow/eyebrow_1.png" 
    $ luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_1.png" 
    $ luna_glasses = "01_hp/13_characters/luna/misc/glasses.png" 
    $ luna_top = "01_hp/13_characters/luna/clothes/uniform/top.png" 
    $ luna_acc = "01_hp/13_characters/luna/misc/jewel.png" 
    $ luna_skirt = "01_hp/13_characters/luna/clothes/uniform/skirt.png" 
    $ luna_panties = "01_hp/13_characters/luna/clothes/underwear/panties.png" 
    $ luna_bra = "01_hp/13_characters/luna/clothes/underwear/bra.png" 
    $ luna_zorder = 5

    $ luna_chibi_image = "01_hp/13_characters/luna/chibis/luna_stand.png" 
    $ luna_chibi_xpos = 500
    $ luna_chibi_ypos = 250

    $ luna_wear_glasses = False
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_skirt = True
    $ luna_wear_top = True
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
    $ luna_chibi("stand")
    call luna_main("[l_genie_name]...", 8, 2, 3, 3)

label luna_door_menu:
    menu:
        "-Chit Chat-":
            "To be done."
            jump luna_door_menu
        "-favours-":
            jump luna_favour_menu
        "-Never mind-":
            jump luna_away

label luna_favour_menu:
    menu:
        "-Talk to me-":
            jump luna_favour_1
        #"-Strip for me-":
            jump luna_favour_2
        #"-Lap Dance-":
            jump luna_favour_3
        #"-Touch her-":
            jump luna_favour_4
        #"-Have sex with her-":
            jump luna_favour_5
        #"-Have anal sex with her-":
            jump luna_favour_6
        "-Never mind-":
            jump luna_door_menu

label luna_summon:
    $ changeLuna(8, 2, 3, 3)
return

label luna_away:
    $ luna_busy = True
    $ renpy.play('sounds/door.mp3')
    hide screen luna
    hide screen luna_chibi
    with d3
    jump day_main_menu

label luna_no_money:
    call luna_main("You expect me to do it for free?", 8, 2, 3, 3)
    call luna_main("Hmph!", 8, 2, 3, 3)
    jump luna_away


###FAVOURS###------------------------------------------------------

label luna_favour_1: ###TALK TO ME
    m "{size=-4}(All I'll do is have a nice little conversation with her...){/size}"
    if luna_corruption == 0:
        $ luna_corruption += 1
    if luna_corruption >= 0: #FIRST TIME (change to == once later events are done)
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            m "Ok then..."
            m "Tell me a little about yourself, [luna_name]."
            call luna_main("*hmph* I assume you'll be paying me for this [l_genie_name].", 7, 1, 2, 2)
            menu:
                "-5 gold-":
                    m "How does five gold sound [luna_name]?"
                    call luna_main("five gold! Who do you think I am!", 8, 1, 2, 4)
                    m "A student with no source of income."
                    call luna_main("I am luna lovegood! You should be paying a hundred gold just to look at me!", 9, 2, 3, 3)
                    m "How does ten gold sound then?"
                    call luna_main("Perhaps if you'd offered that to being with...", 7, 1, 2, 2)
                    call luna_main("But now I'm far too upset to hold a conversation for such a low amount.", 7, 2, 2, 4)
                    m "would twenty gold calm you down?"
                    call luna_main("well, I suppose it would.", 3, 3, 1, 1)
                    $ current_payout = 20
                    m "Good, well now that we've got that sorted out..."
                "-10 gold-":
                    m "Will ten gold be enough for a conversation with your headmaster?"
                    call luna_main("I suppose so...", 6, 1, 1, 2)
                    call luna_main("Just don't try anything funny.", 7, 2, 2, 3)
                    $ current_payout = 10
                    m "Scouts honor. Now..."
                "-50 gold-":
                    $ current_payout = 50
                    m "How does fifty gold sound [luna_name]?"
                    call luna_main("{size=+10}(FIFTY GOLD!){/size}", 4, 1, 1, 17)
                    call luna_main("*Hmph* I suppose that's a fair amount.", 2, 3, 1, 1)
                    call luna_main("Just don't think it buys you anything other than a conversation.", 7, 1, 2, 2)
                    m "Of course not. Speaking of which..."
            call luna_main("Fine, fine, I'll start...", 3, 3, 1, 2)
            call luna_main("My school life so far has been painfully dull.", 1, 1, 2, 3)
            call luna_main("I've been under appreciated by everyone in this damn place.", 1, 2, 2, 2)
            call luna_main("No one seems to take me seriously...", 7, 3, 2, 2)
            menu: 
                "-Jerk off while she is talking-": # offended and stops unless you paid her 50 or offer to pay her more
                    hide screen luna
                    hide screen blktone
                    with d3
                    ">You reach under the desk and grab your cock..."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    pause                    
                    call luna_main("what are you doing [l_genie_name]!?", 9, 1, 5, 3)
                    m "What, oh it's nothing. Simply adjusting my robe, that's all."
                    if current_payout < 50:
                        call luna_main("This is exactly what I mean!", 8, 1, 3, 3)
                        call luna_main("Even the headmaster of this damn school thinks he can get away with touching himself in front of me for only [current_payout] gold!", 8, 2, 3, 3)
                        show screen genie
                        with d3
                        "You quickly tuck your cock back into your robe."
                        m "i can assure you I was doing no such thing!"
                        call luna_main("whatever... I'm leaving", 8, 2, 3, 3)
                        m "What! Already?"
                        call luna_main("Would you rather I stay and call the ministry of magic [l_genie_name]?", 8, 1, 3, 3)
                        m "Fair enough."
                        call luna_main("I mean if you're going to try this on you could at least offer a little more than [current_payout] gold...", 9, 1, 2, 4)
                        jump luna_away
                    call luna_main("...", 6, 2, 1, 2)
                    call luna_main("{size=-5}(Well I suppose he did offer fifty gold...){/size}", 6, 2, 1, 1)
                    call luna_main("As I was saying, no one seems to even notice me.", 7, 1, 2, 2)
                    call luna_main("The teachers are too busy playing favourites with the \"gryffindor\" and \"slytherin\" students.", 7, 2, 2, 4)
                    call luna_main("The girls are all self obsessesed.", 7, 3, 2, 3)
                    m "You don't say."
                    call luna_main("and The boys are off chasing anything that shows a little skin...", 8, 2, 2, 3)
                    m "well, maybe you should fight fire with fire."
                    call luna_main("what!? and parade myself around like some tart?", 4, 2, 2, 6)
                    m "{size=-4}(Yes... a nasty, little tart!){/size}"
                    call luna_main("I bet you'd enjoy that wouldn't you [l_genie_name]...", 5, 1, 2, 1)
                    m "{size=-4}(Yes...){/size}"
                    call luna_main("another one of your precious students, dressing like a slut.", 5, 2, 1, 1)
                    m "{size=-2}(Yes......){/size}"
                    call luna_main("showing off her body for anyone that will look.", 6, 2, 2, 11)
                    m "{size=+2}(Yes.........){/size}"
                    call luna_main("You probably want me to act like those \"slytherin\" sluts too...", 6, 1, 2, 1)
                    m "{size=+4}(Yes! Yes!){/size}"
                    call luna_main("willing to show it all for a few points...", 6, 1, 2, 5)
                    g4 "{size=+4}(almost there...){/size}"
                    call luna_main("is that what you want [l_genie_name]? a nice little slytherin slut?", 6, 1, 2, 1)
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                    hide screen luna
                    with d3
                    show screen white 
                    pause.1
                    hide screen white
                    pause.2
                    show screen white 
                    pause .1
                    hide screen white
                    with hpunch
                    g4 "Argh! YES!"
                    hide screen luna
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    show screen bld1
                    with d3
                    call luna_main("That's it, [l_genie_name], just let it all out...", 5, 1, 1, 1)
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    hide screen bld1
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("You couldn't help yourself could you?", 5, 2, 5, 1)
                    m "ah... I guess not."
                    call luna_main("Well, I expect a bonus.", 2, 2, 5, 2)
                    m "I'm already paying you fifty gold!"
                    call luna_main("That was just for the conversation. If you expect me to stand here and watch you cum all over yourself, that costs extra.", 8, 2, 3, 3)
                    m "Fine, I'll make it 70 gold."
                    $ current_payout = 70
                    call luna_main("Well I'm glad someone appreciates me.", 5, 2, 5, 1)
                    call luna_main("(Even if it is a filthy old pervert...)", 3, 2, 5, 2)
                "-Participate in the conversation-":
                    m "I can't see why..."
                    call luna_main("Even my father doesn't treat me like he should.", 7, 2, 2, 2)
                    m "And how is that?"
                    call luna_main("Like the princess I am!", 5, 1, 1, 4)
                    m "(Not this again...)"
                    call luna_main("As it is he's barely selling any copies of his newspaper.", 8, 2, 3, 3)
                    call luna_main("It's ridiculous! I should be showered in gifts and gold...", 9, 2, 3, 2)
    call luna_main("Speaking of which...", 5, 1, 2, 2)    
    m "Alright, alright. Here's your gold."
    $ gold -= current_payout
    ">You hand Luna [current_payout] gold."
    call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)     
    ">Luna leaves your office."  
    hide screen genie_jerking_sperm_02     
    jump luna_away
label luna_favour_2: ###STRIP FOR ME
    jump luna_away
label luna_favour_3: 
    jump luna_away
label luna_favour_4:
    jump luna_away
label luna_favour_5:
    jump luna_away
label luna_favour_6:
    jump luna_away
label luna_favour_7:
    jump luna_away
label luna_favour_8:
    jump luna_away
label luna_favour_9:
    jump luna_away
label luna_favour_10:
    jump luna_away
label luna_favour_11:
    jump luna_away
label luna_favour_12:
    jump luna_away
label luna_favour_13:
    jump luna_away

###CHIBIS###------------------------------------------------------
