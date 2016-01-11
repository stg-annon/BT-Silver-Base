screen luna:
    ### BASE IMAGE
    add luna_base xpos luna_xpos ypos luna_ypos #Add the base body
    add luna_cheeks xpos luna_xpos ypos luna_ypos #Add her blush to base
    add luna_hair xpos luna_xpos ypos luna_ypos #Add the hair shadow
    ### EMOTIONS
    add luna_mouth xpos luna_xpos ypos luna_ypos #Add the mouth
    add "01_hp/26_luna/eye/eye_white.png"  xpos luna_xpos ypos luna_ypos
    add luna_pupil xpos luna_xpos ypos luna_ypos #Add the pupil
    add luna_eye xpos luna_xpos ypos luna_ypos #Add the eye outline
    add luna_eyebrow xpos luna_xpos ypos luna_ypos #Add the eyebrow
    ### CLOTHES 
    if luna_wear_glasses:
        add luna_glasses xpos luna_xpos ypos luna_ypos # Add the glasses
    if luna_wear_bra:
        add luna_bra xpos luna_xpos ypos luna_ypos # Add the bra
    if luna_wear_panties:
        add luna_panties xpos luna_xpos ypos luna_ypos # Add the panties
    if luna_wear_skirt:
        add luna_skirt xpos luna_xpos ypos luna_ypos # Add the skirt
    if luna_wear_top:
        add luna_top xpos luna_xpos ypos luna_ypos # Add the top
    #add luna_acc xpos luna_xpos ypos luna_ypos # Add the accessory
    ### ZORDER
    zorder luna_zorder

screen luna_chibi:
    add luna_chibi_image xpos luna_chibi_xpos ypos luna_chibi_ypos

init python: ###Method Definition for new characters
    def luna_chibi( l_chibi=None, 
                    l_xpos=None,
                    l_ypos=None):

        ###DEFINE GLOBAL VARIABLES
        global luna_chibi_image
        global luna_chibi_xpos
        global luna_chibi_ypos
        ###HIDE OLD SCREEN
        renpy.hide_screen("luna_chibi")
        renpy.with_statement(Dissolve(0.5))

        if l_xpos is not None:
            luna_chibi_xpos = l_xpos

        if l_ypos is not None:
            luna_chibi_ypos = l_ypos

        if l_chibi is not None:
            if l_chibi == "stand":
                luna_chibi_image = "01_hp/26_luna/chibis/luna_stand.png" 
            if l_chibi == "stand_topless":
                luna_chibi_image = "01_hp/26_luna/chibis/luna_stand_topless.png" 
            else:
                luna_chibi_image = luna_chibi_image

        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luna_chibi")
        renpy.with_statement(Dissolve(0.5))

    def changeLuna( l_eye=None, 
                    l_pupil=None, 
                    l_eyebrow=None, 
                    l_mouth=None, 
                    x_pos=None, 
                    y_pos=None): # Luna
        ###DEFINE GLOBAL VARIABLES
        global luna_xpos
        global luna_ypos
        global luna_base
        global luna_cheeks
        global luna_eye
        global luna_pupil
        global luna_eyebrow
        global luna_mouth
        global luna_eyebrow
        ###HIDE OLD SCREEN
        renpy.hide_screen("luna")
        renpy.with_statement(Dissolve(0.5))
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            luna_xpos = x_pos
        else:
            luna_xpos = luna_xpos
        if y_pos is not None:
            luna_ypos = luna_ypos
        else:
            luna_ypos = luna_ypos
        ###MANUAL EMOTION AND BASE IMAGE CONTROL
        # if l_cheeks is not None:
            # if l_cheeks == 1:
                # luna_cheeks = "01_hp/26_luna/base/cheeks_01.png"
            # elif l_cheeks == 2:
                # luna_cheeks = "01_hp/26_luna/base/cheeks_02.png"
            # else:
                # luna_cheeks = luna_cheeks

        if l_eye is not None:
            if l_eye == 1:
                luna_eye = "01_hp/26_luna/eye/eye_01.png" 
            elif l_eye == 2:
                luna_eye = "01_hp/26_luna/eye/eye_02.png" 
            elif l_eye == 3:
                luna_eye = "01_hp/26_luna/eye/eye_03.png" 
            elif l_eye == 4:
                luna_eye = "01_hp/26_luna/eye/eye_04.png" 
            elif l_eye == 5:
                luna_eye = "01_hp/26_luna/eye/eye_05.png" 
            elif l_eye == 6:
                luna_eye = "01_hp/26_luna/eye/eye_06.png" 
            elif l_eye == 7:
                luna_eye = "01_hp/26_luna/eye/eye_07.png" 
            elif l_eye == 8:
                luna_eye = "01_hp/26_luna/eye/eye_08.png" 
            elif l_eye == 9:
                luna_eye = "01_hp/26_luna/eye/eye_09.png" 
            elif l_eye == 10:
                luna_eye = "01_hp/26_luna/eye/eye_10.png" 
            else:
                luna_eye = luna_eye

        if l_pupil is not None:
            if l_pupil == 1:
                luna_pupil = "01_hp/26_luna/eye/pupil_01.png" 
            elif l_pupil == 2:
                luna_pupil = "01_hp/26_luna/eye/pupil_02.png" 
            elif l_pupil == 3:
                luna_pupil = "01_hp/26_luna/eye/pupil_03.png" 
            elif l_pupil == 4:
                luna_pupil = "01_hp/26_luna/eye/pupil_04.png" 
            elif l_pupil == 5:
                luna_pupil = "01_hp/26_luna/eye/pupil_05.png" 
            elif l_pupil == 6:
                luna_pupil = "01_hp/26_luna/eye/pupil_06.png" 
            elif l_pupil == 7:
                luna_pupil = "01_hp/26_luna/eye/pupil_07.png" 
            else:
                luna_pupil = luna_pupil

        if l_eyebrow is not None:
            if l_eyebrow == 1:
                luna_eyebrow = "01_hp/26_luna/eye/eyebrow_01.png" 
            elif l_eyebrow == 2:
                luna_eyebrow = "01_hp/26_luna/eye/eyebrow_02.png" 
            elif l_eyebrow == 3:
                luna_eyebrow = "01_hp/26_luna/eye/eyebrow_03.png" 
            elif l_eyebrow == 4:
                luna_eyebrow = "01_hp/26_luna/eye/eyebrow_04.png" 
            elif l_eyebrow == 5:
                luna_eyebrow = "01_hp/26_luna/eye/eyebrow_05.png" 
            else:
                luna_eyebrow = luna_eyebrow

        if l_mouth is not None:
            if l_mouth == 1:
                luna_mouth = "01_hp/26_luna/mouth/mouth_01.png" 
            elif l_mouth == 2:
                luna_mouth = "01_hp/26_luna/mouth/mouth_02.png" 
            elif l_mouth == 3:
                luna_mouth = "01_hp/26_luna/mouth/mouth_03.png" 
            elif l_mouth == 4:
                luna_mouth = "01_hp/26_luna/mouth/mouth_04.png" 
            elif l_mouth == 5:
                luna_mouth = "01_hp/26_luna/mouth/mouth_05.png" 
            elif l_mouth == 6:
                luna_mouth = "01_hp/26_luna/mouth/mouth_06.png" 
            elif l_mouth == 7:
                luna_mouth = "01_hp/26_luna/mouth/mouth_07.png" 
            elif l_mouth == 8:
                luna_mouth = "01_hp/26_luna/mouth/mouth_08.png" 
            elif l_mouth == 9:
                luna_mouth = "01_hp/26_luna/mouth/mouth_09.png" 
            elif l_mouth == 10:
                luna_mouth = "01_hp/26_luna/mouth/mouth_10.png" 
            elif l_mouth == 11:
                luna_mouth = "01_hp/26_luna/mouth/mouth_11.png" 
            elif l_mouth == 12:
                luna_mouth = "01_hp/26_luna/mouth/mouth_12.png" 
            elif l_mouth == 13:
                luna_mouth = "01_hp/26_luna/mouth/mouth_13.png" 
            elif l_mouth == 14:
                luna_mouth = "01_hp/26_luna/mouth/mouth_14.png" 
            elif l_mouth == 15:
                luna_mouth = "01_hp/26_luna/mouth/mouth_15.png" 
            elif l_mouth == 16:
                luna_mouth = "01_hp/26_luna/mouth/mouth_16.png" 
            elif l_mouth == 17:
                luna_mouth = "01_hp/26_luna/mouth/mouth_17.png" 
            elif l_mouth == 18:
                luna_mouth = "01_hp/26_luna/mouth/mouth_18.png" 
            elif l_mouth == 19:
                luna_mouth = "01_hp/26_luna/mouth/mouth_19.png" 
            elif l_mouth == 20:
                luna_mouth = "01_hp/26_luna/mouth/mouth_20.png" 
            else:
                luna_mouth = luna_mouth
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luna")
        renpy.with_statement(Dissolve(0.5))