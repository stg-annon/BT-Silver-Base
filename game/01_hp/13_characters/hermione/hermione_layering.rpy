screen hermione_main_new:
    
    add hermione_base xpos hermione_xpos ypos hermione_ypos #Add the base body
    add hermione_legs xpos hermione_xpos ypos hermione_ypos
    add hermione_right_arm xpos hermione_xpos ypos hermione_ypos
    add hermione_breasts xpos hermione_xpos ypos hermione_ypos
    add hermione_left_arm xpos hermione_xpos ypos hermione_ypos
    add hermione_hair_a xpos hermione_xpos ypos hermione_ypos #Add the hair shadow
    add h_body xpos hermione_xpos ypos hermione_ypos
    
  ### CLOTHES
    if not hermione_custom_outfit:
        ### SKIRT
        if hermione_wear_skirt:
            add hermione_skirt xpos hermione_xpos ypos hermione_ypos # Add the skirt
        elif hermione_wear_panties:
            add hermione_panties xpos hermione_xpos ypos hermione_ypos # Add the panties
        ### TOP
        if hermione_wear_top:
            add hermione_top xpos hermione_xpos ypos hermione_ypos # Add the top
        elif hermione_wear_bra:
            add hermione_bra xpos hermione_xpos ypos hermione_ypos # Add the bra
    else:
        add hermione_custom_a xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_b xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_c xpos hermione_xpos ypos hermione_ypos
        add hermione_custom_d xpos hermione_xpos ypos hermione_ypos
    
    add hermione_hair_b xpos hermione_xpos ypos hermione_ypos
    
    ### ZORDER
    zorder hermione_zorder
    
label h_outfit(outfit_id):
    $ custom_outfit = outfit_id
    hide screen hermione_main_new
    if custom_outfit == 0:
        $ hermione_custom_outfit = False
        $ hermione_hair_a = hair_a_tmp
        $ hermione_hair_b = hair_b_tmp
    else:
        if "01_hp/13_characters/hermione/clothes/custom/" not in hermione_hair_a or "01_hp/13_characters/hermione/clothes/custom/" not in hermione_hair_b:
            $ hair_a_tmp = hermione_hair_a
            $ hair_b_tmp = hermione_hair_b
        
        if hermione_custom_hair_list[custom_outfit] != "":
            $ hermione_hair_a = "01_hp/13_characters/hermione/clothes/custom/"+str(hermione_custom_hair_list[custom_outfit])+".png"
            $ hermione_hair_b = "01_hp/13_characters/hermione/clothes/custom/"+str(hermione_custom_hair_list[custom_outfit])+"_2.png"
        else:
            $ hermione_hair_a = hair_a_tmp
            $ hermione_hair_b = hair_b_tmp
        
        if hermione_custom_outfit_list[custom_outfit][0] != "":
            $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[custom_outfit][0]
        else:
            $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        if hermione_custom_outfit_list[custom_outfit][1] != "":
            $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[custom_outfit][1]
        else:
            $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        if hermione_custom_outfit_list[custom_outfit][2] != "":
            $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[custom_outfit][2]
        else:
            $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
        
        if hermione_custom_outfit_list[custom_outfit][3] != "":
            $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[custom_outfit][3]
        else:
            $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
            
        if hermione_custom_outfit_list[custom_outfit][4] != "":
            $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/"+hermione_custom_outfit_list[custom_outfit][3]
        else:
            $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
            
        $ hermione_custom_outfit = True
    show screen hermione_main_new
    return
    
label update_her_uniform:
    if not hermione_wear_top and not hermione_wear_bra:
        if not hermione_perm_expand:
            $ h_breasts = 2
        else:
            $ h_breasts = 3
    else:
        $ h_breasts = 1
        if whoring <= 3:# shirt_00
            $ h_top = 1
        elif whoring >= 4 and whoring <= 7:# shirt_01
            $ h_top = 2
        elif whoring >= 8 and whoring <= 14:# shirt_02
            $ h_top = 3
        elif whoring >= 15 and whoring <= 20:# shirt_03
            $ h_top = 4
        elif whoring >= 21:
            if day_random <= 4:# shirt_04
                $ h_top = 5
            if day_random >= 5:# shirt_05
                $ h_top = 6
    if whoring <= 5:
        $ h_skirt = 1
    if whoring >= 6 and whoring <= 11:
        $ h_skirt = 2
    if whoring >= 12 and whoring <= 19:
        $ h_skirt = 3
    if whoring >= 20:
        $ h_skirt = 4
    
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_"+str(h_breasts)+".png"
    $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/skirt_"+str(h_skirt)+".png"
    $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_"+str(h_top)+".png"
    
    
    $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
    $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
    
    return
    
label new_main_menu:
    menu:
        "-Outfit 0-":
            call h_outfit(0)
            jump new_main_menu
        "-Outfit 1-":
            call h_outfit(1)
            jump new_main_menu
        "-Outfit 2-":
            call h_outfit(2)
            jump new_main_menu
        "-Outfit 3-":
            call h_outfit(3)
            jump new_main_menu
        "-Outfit 4-":
            call h_outfit(4)
            jump new_main_menu
        "-Outfit 7-":
            call h_outfit(7)
            jump new_main_menu
        "-Outfit 8-":
            call h_outfit(8)
            jump new_main_menu
        "-Outfit 9-":
            call h_outfit(9)
            jump new_main_menu
        "-Outfit 10-":
            call h_outfit(10)
            jump new_main_menu
        "-Outfit 11-":
            call h_outfit(11)
            jump new_main_menu
        "-Outfit 12-":
            call h_outfit(12)
            jump new_main_menu
        "-Hair A-":
            $ h_hair_style = "A"
            call update_her_uniform
            jump new_main_menu
        "-Hair B-":
            $ h_hair_style= "B"
            call update_her_uniform
            jump new_main_menu
        "-Never mind-":
            jump day_main_menu
    
init python:
    def changeHermione( hair_color=None,
                        hair_style=None,
                        face=None,
                        
                        x_pos=None,
                        y_pos=None):
        ###DEFINE GLOBAL VARIABLES
        global h_xpos
        global h_ypos
        global h_base
        global h_body
        global h_hair_color
        global h_hair_style
        ###HIDE OLD SCREEN
        renpy.hide_screen("hermione_main_new")
        renpy.with_statement(Dissolve(0.5))
        ###MANUAL POSITION CONTROL
        if x_pos is not None:
            h_xpos = x_pos
        else:
            h_xpos = luna_xpos
        if y_pos is not None:
            h_ypos = y_pos
        else:
            h_ypos = h_ypos
        
        
        if hair_color is not None and (hair_color >= 1 and hair_color <= 6):
            h_hair_color = hair_color
        else:
            h_hair_color = h_hair_color
            
        if hair_style is not None and (hair_style == "A" or hair_style == "B"):
            h_hair_style = hair_style
        else:
            h_hair_style = h_hair_style
        
        hermione_hair_a = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        hermione_hair_b = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
        
        if face is not None:
            h_body = h_body
    
    
    
    def changeHermioneDialoug(   image_name,
                                    hid_char_list=None,
                                    hid_dialog_list=None,
                                    x_pos=370,
                                    y_pos=0,
                                    hide_trans=Dissolve(0.3),
                                    show_trans=Dissolve(0.3),
                                    char_list=None,
                                    dialog_list=None):
        # SCOPE THESE VARIABLES TO GLOBAL SO WE CAN REALLY
        # UPDATE THEM
        global h_xpos
        global h_ypos
        global h_body
        renpy.hide_screen("hermione_main")
        if hide_trans is not None:
            renpy.with_statement(hide_trans)
        #dialog if present
        if hid_char_list is not None:
            if len(hid_char_list) == 1:
                #single character
                for i in range(0,len(hid_dialog_list)):
                    renpy.say(hid_char_list[0],hid_dialog_list[i])
            elif len(hid_char_list) > 1:
                #multiple characters
                for i in range(0,len(hid_char_list)):
                    renpy.say(hid_char_list[i],hid_dialog_list[i])
        h_xpos = x_pos
        h_ypos = y_pos
        if image_name is not None:
            h_body = image_name

        renpy.show_screen("hermione_main")
        if show_trans is not None:
            renpy.with_statement(show_trans)
        #dialog if present
        if char_list is not None:
            if len(char_list) == 1:
                #single character
                for i in range(0,len(dialog_list)):
                    renpy.say(char_list[0],dialog_list[i])
            elif len(char_list) > 1:
                #multiple characters
                for i in range(0,len(char_list)):
                    renpy.say(char_list[i],dialog_list[i])
                   