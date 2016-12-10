#Hermini's Layering
screen hermini_main:
    tag hermini_main
    
    $ hermini_xpos = 500
    $ hermini_ypos = 0
    $ hermini_xpos_diff = 5
    $ hermini_ypos_diff = 66
    $ hermini_zoom_diff = 0.97

    add "01_hp/13_characters/young_hermione/body/head_1.png" xpos hermini_xpos+hermini_xpos_diff ypos hermini_ypos+hermini_ypos_diff zoom hermini_zoom_diff#Add the hair base    
    add "01_hp/13_characters/young_hermione/body/base.png" xpos hermini_xpos ypos hermini_ypos #Add the base body

    #add hermione_body xpos hermini_xpos ypos hermini_ypos
    add "01_hp/13_hermione_main/body_01.png" xpos hermini_xpos+hermini_xpos_diff ypos hermini_ypos+hermini_ypos_diff zoom hermini_zoom_diff#Add emotion
    add "01_hp/13_characters/young_hermione/body/head_2.png" xpos hermini_xpos+hermini_xpos_diff ypos hermini_ypos+hermini_ypos_diff zoom hermini_zoom_diff#Add the hair shadow
    #add hermione_tears xpos hermini_xpos ypos hermini_ypos
    
  ### CLOTHES
    add "01_hp/13_characters/young_hermione/clothes/uniform/robe.png" xpos hermini_xpos ypos hermini_ypos #Add the robe
    
    #add "01_hp/13_characters/hermione/clothes/uniform/skirt_6.png" xpos hermini_xpos ypos hermini_ypos
    #add "01_hp/13_characters/hermione/clothes/uniform/top_5.png" xpos hermini_xpos ypos hermini_ypos

    add "01_hp/13_characters/young_hermione/body/head_2.png" xpos hermini_xpos+hermini_xpos_diff ypos hermini_ypos+hermini_ypos_diff zoom hermini_zoom_diff#Add the hair shadow
    add "01_hp/13_characters/young_hermione/body/hands.png" xpos hermini_xpos ypos hermini_ypos #Add the hands
    ### ZORDER
    zorder hermione_zorder