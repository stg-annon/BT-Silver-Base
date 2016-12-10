screen luna:
    ### BASE IMAGE
    add luna_base xpos luna_xpos ypos luna_ypos #Add the base body
    add luna_cheeks xpos luna_xpos ypos luna_ypos #Add her blush to base
    add luna_hair xpos luna_xpos ypos luna_ypos #Add the hair shadow
    ### EMOTIONS
    add luna_mouth xpos luna_xpos ypos luna_ypos #Add the mouth
    add "01_hp/13_characters/luna/body/face/eye_white.png"  xpos luna_xpos ypos luna_ypos
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
                luna_chibi_image = "01_hp/13_characters/luna/chibis/luna_stand.png" 
            if l_chibi == "stand_topless":
                luna_chibi_image = "01_hp/13_characters/luna/chibis/luna_stand_topless.png" 
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
                # luna_cheeks = "01_hp/13_characters/luna/base/cheeks_01.png"
            # elif l_cheeks == 2:
                # luna_cheeks = "01_hp/13_characters/luna/base/cheeks_02.png"
            # else:
                # luna_cheeks = luna_cheeks

        if l_eye is not None:
            luna_eye = "01_hp/13_characters/luna/body/face/eye/eye_"+str(l_eye)+".png" 

        if l_pupil is not None:
            luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_"+str(l_pupil)+".png" 

        if l_eyebrow is not None:
            luna_eyebrow = "01_hp/13_characters/luna/body/face/eyebrow/eyebrow_"+str(l_eyebrow)+".png" 

        if l_mouth is not None:
            luna_mouth = "01_hp/13_characters/luna/body/face/mouth/mouth_"+str(l_mouth)+".png" 
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luna")
        renpy.with_statement(Dissolve(0.5))