screen luna:
    ### BASE IMAGE
    add luna_base xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the base body
    add "01_hp/13_characters/luna/body/arms/left_"+str(luna_l_arm)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the left arm
    add "01_hp/13_characters/luna/body/arms/right_"+str(luna_r_arm)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the right arm
    add luna_cheeks xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add her blush to base
    add "01_hp/13_characters/luna/body/head/hair_"+str(luna_hair)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the hair base
    ### EMOTIONS
    add luna_mouth xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the mouth
    add "01_hp/13_characters/luna/body/face/eye_white.png"  xpos luna_xpos ypos luna_ypos xzoom luna_flip
    add luna_pupil xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the pupil
    add luna_eye xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the eye outline
    add luna_eyebrow xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the eyebrow
    add "01_hp/13_characters/luna/body/face/tears/tears_"+str(luna_tears)+".png"  xpos luna_xpos ypos luna_ypos xzoom luna_flip
    add "01_hp/13_characters/luna/body/head/hair_"+str(luna_hair)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip #add the hair overlayer

    if luna_wear_cum_under: #Luna cum but under clothes
        add "01_hp/13_characters/luna/misc/cum_"+str(luna_cum)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the top
    ### CLOTHES 
    if luna_wear_glasses:
        add luna_glasses xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the glasses
    if luna_wear_bra and not luna_wear_top:
        add luna_bra xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the bra
    if luna_wear_panties:
        add luna_panties xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the panties
    if luna_wear_skirt:
        add luna_skirt xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the skirt
    if luna_wear_top:
        add luna_top xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the top
    if luna_wear_acc:
        add luna_acc xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the accessory (jewellery)

    ### ARM OVERLAYS
    add "01_hp/13_characters/luna/body/arms/left_"+str(luna_l_arm)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the left arm
    add "01_hp/13_characters/luna/body/arms/right_"+str(luna_r_arm)+"_2.png" xpos luna_xpos ypos luna_ypos xzoom luna_flip#Add the right arm

    if luna_wear_cum:
        add "01_hp/13_characters/luna/misc/cum_"+str(luna_cum)+".png" xpos luna_xpos ypos luna_ypos xzoom luna_flip# Add the top
    ### ZORDER
    zorder luna_zorder

screen luna_chibi:
    add luna_chibi_image xpos luna_chibi_xpos ypos luna_chibi_ypos xzoom luna_flip  
    zorder luna_chibi_zorder


label luna_main(text="",eye=None, pupil=None, eyebrow=None, mouth=None):
    if eye!=None and pupil!=None and eyebrow!=None and mouth!=None:
        $ changeLuna(eye, pupil, eyebrow, mouth)
    if text != "":
        $ renpy.say(lun, text)
    return

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
            if l_chibi == "stand_naked":
                luna_chibi_image = "01_hp/13_characters/luna/chibis/walk/l_walk_n_01.png" 
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
        global luna_skirt 
        global luna_top
        ###HIDE OLD SCREEN
        #renpy.hide_screen("luna")
        #renpy.with_statement(Dissolve(0.5))
        ###UPDATE UNIFORM
        luna_skirt = "01_hp/13_characters/luna/clothes/uniform/skirt_"+str(luna_skirt_level)+".png" 
        luna_top = "01_hp/13_characters/luna/clothes/uniform/top_"+str(luna_top_level)+".png" 

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

        if l_pupil is not None and not luna_unlocked:
            luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_"+str(l_pupil)+".png" 
        if l_pupil is not None and luna_unlocked:
            luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_"+str(l_pupil)+"_G.png" 
        if l_pupil is not None and luna_reverted:
            luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_"+str(l_pupil)+".png" 

        if l_eyebrow is not None:
            luna_eyebrow = "01_hp/13_characters/luna/body/face/eyebrow/eyebrow_"+str(l_eyebrow)+".png" 

        if l_mouth is not None:
            luna_mouth = "01_hp/13_characters/luna/body/face/mouth/mouth_"+str(l_mouth)+".png" 
            
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("luna")
        renpy.with_statement(Dissolve(0.3))