#LUNA PLOT
#Luna is misinterpreting her own teenage arousal as a result of a group of wrackspurts that have decided to terrorise her.
#Genie is able to determine the true cause of her arousal and informs her that they only cure for her arousal is to perform certain activites together


#Don't forget to incorporate the quibbler

#LUNA MECHANICS
#Functions on a different mechanic from hermione. She still has a 'whoring' stat but instead of anger she has arousal
#Certain activities will cause Luna to gain arousal and others will cause her to lose it
#Any favors that focus on her will lose arousal as she will achieve a 'release'
#Any favors that focus on genie will cause her to gain arousal
#If her arousal is too high she won't do the genie favors and conversely if it is too low then she will not do the favors that focus on her

label luna_init:
    $ luna_busy = False
    $ luna_known = False
    $ luna_unlocked = False
    $ l_genie_name = "Professor"
    $ luna_name = "Miss Lovegood"

    $ luna_arrousal = 0
    $ luna_corruption = 0

    $ luna_base = "01_hp/26_luna/base/base_01.png" 
    $ luna_cheeks = "01_hp/26_luna/base/cheeks_01.png"
    $ luna_hair = "01_hp/26_luna/base/hair_01.png" 
    $ luna_xpos = 300
    $ luna_ypos = 0
    $ luna_mouth = "01_hp/26_luna/mouth/mouth_01.png" 
    $ luna_eye = "01_hp/26_luna/eye/eye_01.png" 
    $ luna_eyebrow = "01_hp/26_luna/eye/eyebrow_01.png" 
    $ luna_pupil = "01_hp/26_luna/eye/pupil_01.png" 
    $ luna_top = "01_hp/26_luna/clothes/uniform/top.png" 
    $ luna_acc = "01_hp/26_luna/misc/jewel.png" 
    $ luna_skirt = "01_hp/26_luna/clothes/uniform/skirt.png" 
    $ luna_panties = "01_hp/26_luna/clothes/underwear/panties.png" 
    $ luna_bra = "01_hp/26_luna/clothes/underwear/bra.png" 
    $ luna_zorder = 5

    $ luna_chibi_image = "01_hp/26_luna/chibis/luna_stand.png" 
    $ luna_chibi_xpos = 400
    $ luna_chibi_ypos = 250

    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_skirt = True
    $ luna_wear_top = True
return

label luna_day_flags:
    $ luna_busy = False
return

label luna_night_flags:
    $ luna_busy = False
return


label luna_door:
    call luna_summon
    lun "Hello [l_genie_name]!"
    menu:
        "-Sexual favours-":
            jump luna_favour_menu
        "-Never mind-":
            jump luna_away

label luna_favour_menu:
    menu:
        "-Focus on Luna-":
            jump luna_favour_luna
        "-Focus on me-":
            jump luna_favour_genie
        "-Never mind-":
            jump luna_door

label luna_favour_luna:
    menu:
        "-Talk to her-":
            jump luna_favour_1
        "-Make her touch herself-":
            jump luna_favour_3
        "-Make her touch herself in class-" if daytime:
            jump luna_favour_5
        "-Make her touch herself in class-" if not daytime:
            ">This favour is only available during the day."
            jump luna_favour_luna

        "-Touch her-":
            jump luna_favour_7
        "-Have sex with her-":
            jump luna_favour_9
        "-Have anal sex with her-":
            jump luna_favour_11
        "-Never mind-":
            jump luna_door

label luna_favour_luna:
    menu:
        "-Talk to me-":
            jump luna_favour_2
        "-Strip for me-":
            jump luna_favour_4
        "-Strip in class-" if daytime:
            jump luna_favour_6
        "-Strip in class-" if not daytime:
            ">This favour is only available during the day."
            jump luna_favour_luna

        "-Dress up for me-":
            jump luna_favour_8
        "-Touch me-":
            jump luna_favour_10
        "-Suck me-":
            jump luna_favour_12
        "-Titfuck her-":
            jump luna_favour_13
        "-Never mind-":
            jump luna_door

label luna_summon:
    $ changeLuna(1, 1, 4, 1)
return
label luna_away:
    $ luna_busy = True
    $ renpy.play('sounds/door.mp3')
    hide screen luna
    jump day_main_menu

label luna_intro_1:
    lun "Hello Professor."
    menu:
        "\"Hello child\"":
            pass
        "\"Hello girl\"":
            pass
        "\"Hello Ms Lovegood\"":
            pass
    lun "I came here to day to ask about the Quibbler. I was wondering if we could get some new ink colors, the ones we have at the moment don't quite work for the new article that I am working on."

###FAVOURS###------------------------------------------------------

label luna_favour_1: ###TALK TO HER
    jump luna_away
label luna_favour_2: ###TALK TO ME
    jump luna_away
label luna_favour_3: ###MAKE HER TOUCH HERSELF
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