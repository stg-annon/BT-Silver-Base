### THIS IS WHERE WE DECLARE VARIABLES AND STUFF FOR 4 HOUSES

label FH_init:
###DECLARE CHO CHANG STUFF
    $ cc_base = "01_hp/13_characters/cho_chang/base/base_01.png" 
    $ cc_arms = "01_hp/13_characters/cho_chang/base/side_arms.png" 
    $ cc_l_hand = "01_hp/13_characters/cho_chang/base/left_hand.png" 
    $ cc_hair = "01_hp/13_characters/cho_chang/base/hair_01.png" 
    $ cc_hair_shadow = "01_hp/13_characters/cho_chang/base/hair_shadow.png" 
    $ cc_xpos = 300
    $ cc_ypos = 0
    $ cc_mouth = "01_hp/13_characters/cho_chang/mouth/mouth_01.png" 
    $ cc_eye = "01_hp/13_characters/cho_chang/eye/eye_01.png" 
    $ cc_eyebrow = "01_hp/13_characters/cho_chang/eye/eyebrow_01.png" 
    $ cc_pupil = "01_hp/13_characters/cho_chang/eye/pupil_01.png" 
    $ cc_vest = "01_hp/13_characters/cho_chang/clothes/uniform/vest.png" 
    $ cc_top = "01_hp/13_characters/cho_chang/clothes/uniform/top.png" 
    $ cc_acc = "01_hp/13_characters/cho_chang/clothes/uniform/tie.png" 
    $ cc_skirt = "01_hp/13_characters/cho_chang/clothes/uniform/skirt.png" 
    $ cc_stock = "01_hp/13_characters/cho_chang/clothes/uniform/stockings.png" 
    $ cc_zorder = 5

    

    ##Favour stuff
    $ chof2_first = True

    ##Stats
    $ cho_whoring = 0
    $ cho_mad = 0
    $ cho_points = 0

    ##Flags
    $ cho_busy = False
    $ days_since_cho = 0
    $ cho_known = False
    $ cho_met = False


###DECLARE SUSAN STUFF
    $ sus_hair = "01_hp/13_characters/susan_bones/base/hair_01.png" 
    $ sus_base = "01_hp/13_characters/susan_bones/base/base_01.png" 
    $ sus_breast = "01_hp/13_characters/susan_bones/base/breasts_02.png" 
    $ sus_legs = "01_hp/13_characters/susan_bones/base/legs_01.png"
    $ sus_arms = "01_hp/13_characters/susan_bones/base/arm_01.png" 
    $ sus_arm_2 = "01_hp/13_characters/susan_bones/base/blank.png" 
    $ sus_left_arm = "01_hp/13_characters/susan_bones/base/l_arm_01.png" 
    $ sus_arm_base = "01_hp/13_characters/susan_bones/base/arm_base.png" 
    $ sus_hair_shadow = "01_hp/13_characters/susan_bones/base/hair_shadow.png" 
    $ sus_xpos = 300
    $ sus_ypos = 0
    $ sus_mouth = "01_hp/13_characters/susan_bones/mouth/mouth_01.png" 
    $ sus_eye = "01_hp/13_characters/susan_bones/eye/eye_01.png" 
    $ sus_eyebrow = "01_hp/13_characters/susan_bones/eye/eyebrow_01.png" 
    $ sus_pupil = "01_hp/13_characters/susan_bones/eye/pupil_01.png"  
    $ sus_vest = "01_hp/13_characters/susan_bones/clothes/uniform/vest.png" 
    $ sus_top = "01_hp/13_characters/susan_bones/clothes/uniform/top.png" 
    $ sus_acc = "01_hp/13_characters/susan_bones/clothes/uniform/tie.png" 
    $ sus_skirt = "01_hp/13_characters/susan_bones/clothes/uniform/skirt.png" 
    $ sus_stock = "01_hp/13_characters/susan_bones/clothes/uniform/stockings.png" 
    $ sus_zorder = 5

    $ sus_known = False
    $ sus_met = False


    #Susan's scene stats:
    $ sus_anger = 0
    $ sus_boredom = 0
    $ sus_arousal = 0

    #Susan's general stats:
    $ sus_corruption = 0 
    $ sus_obedience = 0

    #call define_susan_pool #This loads the set of responses for Susan

    return


label FH_day:
    if cho_known:
        $ days_since_cho += 1

    return