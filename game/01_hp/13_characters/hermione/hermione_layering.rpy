screen hermione_main:
    tag hermione_main
    
    $ hermione_xpos_offset = hermione_xpos+140

    if hermione_buttplugs:
        add hermione_buttplug xpos hermione_xpos_offset ypos hermione_ypos # add glasses

    if ears or cat_ears:
        add "01_hp/25_mo/ears_"+str(h_hair_color-1)+"_"+str(h_hair_style)+".png" xpos hermione_xpos_offset ypos hermione_ypos # add cat ears
    
    add hermione_base xpos hermione_xpos_offset ypos hermione_ypos #Add the base body
    add hermione_legs xpos hermione_xpos_offset ypos hermione_ypos
    
    if hermione_action and h_action_show_arms:
        add hermione_action_right_arm xpos hermione_xpos_offset ypos hermione_ypos
    elif not hermione_action:
        add hermione_right_arm xpos hermione_xpos_offset ypos hermione_ypos
    
    add hermione_breasts xpos hermione_xpos_offset ypos hermione_ypos
    
    if hermione_action and h_action_show_arms:
        add hermione_action_left_arm xpos hermione_xpos_offset ypos hermione_ypos
    elif not hermione_action:
        add hermione_left_arm xpos hermione_xpos_offset ypos hermione_ypos
    
    use hermione_tattoo_layer
    
    add hermione_hair_a xpos hermione_xpos_offset ypos hermione_ypos #Add the hair shadow
    add hermione_body xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_tears xpos hermione_xpos_offset ypos hermione_ypos
    
  ### CLOTHES
    add hermione_stockings xpos hermione_xpos_offset ypos hermione_ypos
    
    if hermione_dribble:
        add "01_hp/13_characters/hermione/body/legs/dripping.png" xpos hermione_xpos_offset ypos hermione_ypos

    if hermione_squirt:
        add "01_hp/13_characters/hermione/body/legs/squirting.png" xpos hermione_xpos_offset ypos hermione_ypos
    
    if not hermione_costume and not hermione_action:
        use hermione_uniform
    if hermione_costume:
        use hermione_costume
    if hermione_action:
        use hermione_action
    
    if hermione_costume:
        for i in hermoine_outfit_GLBL.getTopLayers():
            add i xpos hermione_xpos_offset ypos hermione_ypos
    
    if uni_sperm:
        add u_sperm xpos hermione_xpos_offset ypos hermione_ypos
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos hermione_xpos_offset ypos hermione_ypos
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos hermione_xpos_offset ypos hermione_ypos
    
    # ACCESORIES
    if hermione_badges and hermione_wear_top and not hermione_costume:
        add hermione_badge xpos hermione_xpos_offset ypos hermione_ypos # add badge on top
    if hermione_wear_glasses:
        add hermione_glasses xpos hermione_xpos_offset ypos hermione_ypos # add glasses
    if hermione_hats:
        add hermione_hat xpos hermione_xpos_offset ypos hermione_ypos # add glasses
    if hermione_freckles:
        add "01_hp/13_characters/hermione/accessories/head/freckles.png" xpos hermione_xpos_offset ypos hermione_ypos # add freckles
    if hermione_cum:
        add "01_hp/13_hermione_main/auto_14.png" xpos hermione_xpos_offset ypos hermione_ypos # add fake cum   
    if ears or cat_ears:
        add "01_hp/25_mo/ears_"+str(h_hair_color-1)+"_2_"+str(h_hair_style)+".png" xpos hermione_xpos_offset ypos hermione_ypos # add cat ears
    if elf_ears and h_hair_style == "B":
        add "01_hp/13_characters/hermione/accessories/head/elf_ears.png" xpos hermione_xpos_offset ypos hermione_ypos # add elf ears  
    
    if hermione_wear_robe:
        add hermione_robe xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_emote xpos hermione_xpos_offset ypos hermione_ypos
    
    ### ZORDER
    zorder hermione_zorder

screen hermione_ass:
    tag hermione_ass

    add "01_hp/13_characters/hermione/body/ass/hermione_ass_01.png" xpos 500 ypos 0
    if hermione_ass_cum:
        add "01_hp/13_characters/hermione/body/ass/ass_cum_01.png" xpos 500 ypos 0
    zorder hermione_zorder
    
screen hermione_main_obj:
    tag hermione_main
    $ herm = hermione_SC
    $ x = herm.xpos+140
    $ y = herm.ypos
    
    add hermione_base xpos x ypos y #Add the base body
    add hermione_legs xpos x ypos y
    
    if hermione_action and h_action_show_arms:
        add hermione_action_right_arm xpos x ypos y
    elif not hermione_action:
        add hermione_right_arm xpos x ypos y
    
    add hermione_breasts xpos x ypos y
    
    if hermione_action and h_action_show_arms:
        add hermione_action_left_arm xpos x ypos y
    elif not hermione_action:
        add hermione_left_arm xpos x ypos y
    
    use hermione_tattoo_layer
    
    add hermione_hair_a xpos x ypos y #Add the hair shadow
    add hermione_body xpos x ypos y
    add hermione_tears xpos x ypos y
    
  ### CLOTHES
    add hermione_stockings xpos x ypos y
    
    if hermione_dribble:
        add "01_hp/13_characters/hermione/body/legs/dripping.png" xpos x ypos y

    if hermione_squirt:
        add "01_hp/13_characters/hermione/body/legs/squirting.png" xpos x ypos y
    
    if not hermione_costume and not hermione_action:
        use hermione_uniform
    if herm.costume != None:
        for layer in herm.costume:
            add layer xpos x ypos y
    if hermione_action:
        use hermione_action
    
    if hermione_costume:
        for i in hermoine_outfit_GLBL.getTopLayers():
            add i xpos x ypos y
    
    if uni_sperm:
        add u_sperm xpos x ypos y
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos x ypos y
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos x ypos y
    
    # ACCESORIES
    if hermione_badges and hermione_wear_top and not hermione_costume:
        add hermione_badge xpos x ypos y # add badge on top
    if hermione_wear_glasses:
        add hermione_glasses xpos x ypos y # add glasses
    if hermione_hats:
        add hermione_hat xpos x ypos y # add glasses
    if hermione_freckles:
        add "01_hp/13_characters/hermione/accessories/head/freckles.png" xpos x ypos y # add freckles
    if hermione_cum:
        add "01_hp/13_hermione_main/auto_14.png" xpos x ypos y # add fake cum   
    if elf_ears and h_hair_style == "B":
        add "01_hp/13_characters/hermione/accessories/head/elf_ears.png" xpos x ypos y # add elf ears  

    
    if hermione_wear_robe:
        add hermione_robe xpos x ypos y
    add hermione_emote xpos x ypos y
    
    ### ZORDER
    zorder hermione_zorder

screen hermione_clone:
    tag hermione_clone
    
    $ hermione_clone_xpos = 500
    
    add hermione_base xpos hermione_clone_xpos ypos hermione_ypos #Add the base body
    add hermione_legs xpos hermione_clone_xpos ypos hermione_ypos
    
    if hermione_action and h_action_show_arms:
        add hermione_action_right_arm xpos hermione_clone_xpos ypos hermione_ypos
    elif not hermione_action:
        add hermione_right_arm xpos hermione_clone_xpos ypos hermione_ypos
    
    add hermione_breasts xpos hermione_clone_xpos ypos hermione_ypos
    
    if hermione_action and h_action_show_arms:
        add hermione_action_left_arm xpos hermione_clone_xpos ypos hermione_ypos
    elif not hermione_action:
        add hermione_left_arm xpos hermione_clone_xpos ypos hermione_ypos
    
    add "01_hp/13_characters/hermione/body/head/B_2.png" xpos hermione_clone_xpos ypos hermione_ypos #Add the hair shadow
    add hermione_body xpos hermione_clone_xpos ypos hermione_ypos
    add hermione_tears xpos hermione_clone_xpos ypos hermione_ypos
    
  ### CLOTHES
    add "01_hp/13_characters/hermione/clothes/stockings/fishnet_a.png" xpos hermione_clone_xpos ypos hermione_ypos
    
    add "01_hp/13_characters/hermione/clothes/uniform/skirt_6.png" xpos hermione_clone_xpos ypos hermione_ypos
    add "01_hp/13_characters/hermione/clothes/uniform/top_5.png" xpos hermione_clone_xpos ypos hermione_ypos

    add "01_hp/13_characters/hermione/body/head/B_2_2.png" xpos hermione_clone_xpos ypos hermione_ypos #Add the hair shadow
    ### ZORDER
    zorder hermione_zorder
    
    
screen hermione_tattoo_layer:
    for i in range(0,len(hermione_tattoos)):
        add "01_hp/13_characters/hermione/body/tattoo/"+str(hermione_tattoos[i])+".png" xpos hermione_xpos_offset ypos hermione_ypos
    zorder hermione_zorder
    
screen hermione_uniform:
    tag hermione_main
    ### PANTIES
    if hermione_wear_panties or h_request_wear_panties:
        add hermione_panties xpos hermione_xpos_offset ypos hermione_ypos alpha transparency # Add the panties
        add hermione_panties_overlay xpos hermione_xpos_offset ypos hermione_ypos
    ### TOP
    if hermione_wear_top:
        add hermione_top xpos hermione_xpos_offset ypos hermione_ypos alpha transparency # Add the top
    elif hermione_wear_bra:
        add hermione_bra xpos hermione_xpos_offset ypos hermione_ypos alpha transparency # Add the bra
    ### SKIRT
    if hermione_wear_skirt:
        add hermione_skirt xpos hermione_xpos_offset ypos hermione_ypos alpha transparency # Add the skirt
    ### COLLAR 
    if collar == 1:
        add "01_hp/13_characters/hermione/accessories/collars/collar_1.png" xpos hermione_xpos_offset ypos hermione_ypos # Add the collar
    if collar == 2:
        add "01_hp/13_characters/hermione/accessories/collars/collar_2.png" xpos hermione_xpos_offset ypos hermione_ypos # Add the collar
    if collar == 3:  
        add "01_hp/13_characters/hermione/accessories/collars/collar_3.png" xpos hermione_xpos_offset ypos hermione_ypos # Add the collar
    add hermione_hair_b xpos hermione_xpos_offset ypos hermione_ypos
    zorder hermione_zorder
    
screen hermione_costume:
    tag hermione_main
    for i in hermoine_outfit_GLBL.getOutfitLayers():
        add i xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_hair_b xpos hermione_xpos_offset ypos hermione_ypos
    #add hermione_costume_e xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_costume_action_a xpos hermione_xpos_offset ypos hermione_ypos
    zorder hermione_zorder
    
screen hermione_action:
    tag hermione_main
    if h_action_show_skirt:
        add hermione_action_skirt xpos hermione_xpos_offset ypos hermione_ypos
    elif h_action_show_panties or h_request_wear_panties:
        add hermione_action_panties xpos hermione_xpos_offset ypos hermione_ypos
    if h_action_show_top:
        add hermione_action_top xpos hermione_xpos_offset ypos hermione_ypos
    elif h_action_show_bra:
        add hermione_action_bra xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_hair_b xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_action_a xpos hermione_xpos_offset ypos hermione_ypos
    add hermione_action_b xpos hermione_xpos_offset ypos hermione_ypos
    zorder hermione_zorder
        
screen hermione_head:
    tag hermione_head
    
    
    $ hermione_head_xpos_offset = hermione_head_xpos+140

    if ears or cat_ears:
        add "01_hp/25_mo/ears_"+str(h_hair_color-1)+"_"+str(h_hair_style)+".png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # add cat ears
    
    add hermione_base xpos hermione_head_xpos_offset ypos hermione_head_ypos #Add the base body
    add hermione_legs xpos hermione_head_xpos_offset ypos hermione_head_ypos
    add hermione_right_arm xpos hermione_head_xpos_offset ypos hermione_head_ypos
    add hermione_breasts xpos hermione_head_xpos_offset ypos hermione_head_ypos
    add hermione_left_arm xpos hermione_head_xpos_offset ypos hermione_head_ypos
    add hermione_hair_a xpos hermione_head_xpos_offset ypos hermione_head_ypos #Add the hair shadow
    
    add hermione_body xpos hermione_head_xpos_offset ypos hermione_head_ypos
    add hermione_tears xpos hermione_head_xpos_offset ypos hermione_head_ypos
    
  ### CLOTHES
    add hermione_stockings xpos hermione_head_xpos_offset ypos hermione_head_ypos
    if not hermione_costume:
        ### SKIRT
        if hermione_wear_skirt:
            add hermione_skirt xpos hermione_head_xpos_offset ypos hermione_head_ypos alpha transparency # Add the skirt
        elif hermione_wear_panties or h_request_wear_panties:
            add hermione_panties xpos hermione_head_xpos_offset ypos hermione_head_ypos alpha transparency # Add the panties
        ### TOP
        if hermione_wear_top:
            add hermione_top xpos hermione_head_xpos_offset ypos hermione_head_ypos alpha transparency # Add the top
        elif hermione_wear_bra:
            add hermione_bra xpos hermione_head_xpos_offset ypos hermione_head_ypos alpha transparency # Add the bra
        ### COLLAR 
        if collar == 1:
            add "01_hp/13_characters/hermione/accessories/collars/collar_1.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # Add the collar
        if collar == 2:
            add "01_hp/13_characters/hermione/accessories/collars/collar_2.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # Add the collar
        if collar == 3:  
            add "01_hp/13_characters/hermione/accessories/collars/collar_3.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # Add the collar
    else:
        for i in hermoine_outfit_GLBL.getOutfitLayers():
            add i xpos hermione_head_xpos_offset ypos hermione_head_ypos
        add hermione_costume_action_a xpos hermione_head_xpos_offset ypos hermione_head_ypos
    
    add hermione_hair_b xpos hermione_head_xpos_offset ypos hermione_head_ypos
    
    if hermione_costume:
        for i in hermoine_outfit_GLBL.getTopLayers():
            add i xpos hermione_head_xpos_offset ypos hermione_head_ypos

    # ACCESORIES
    if hermione_badges and hermione_wear_top and not hermione_costume:
        add hermione_badge xpos hermione_head_xpos_offset ypos hermione_head_ypos # add badge on top
    if hermione_wear_glasses:
        add hermione_glasses xpos hermione_head_xpos_offset ypos hermione_head_ypos # add glasses
    if hermione_hats:
        add hermione_hat xpos hermione_head_xpos_offset ypos hermione_head_ypos # add glasses
    if hermione_freckles:
        add "01_hp/13_characters/hermione/accessories/head/freckles.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # add freckles
    if hermione_cum:
        add "01_hp/13_hermione_main/auto_14.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # add fake cum 
    if ears or cat_ears:
        add "01_hp/25_mo/ears_"+str(h_hair_color-1)+"_2_"+str(h_hair_style)+".png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # add cat ears  
    if elf_ears and h_hair_style == "B":
        add "01_hp/13_characters/hermione/accessories/head/elf_ears.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos # add elf ears  
    
    if uni_sperm:
        add u_sperm xpos hermione_head_xpos_offset ypos hermione_head_ypos
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos
    elif aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos hermione_head_xpos_offset ypos hermione_head_ypos
    
    if hermione_wear_robe:
        add hermione_robe xpos hermione_head_xpos_offset ypos hermione_head_xpos_offset
    add hermione_emote xpos hermione_head_xpos_offset ypos hermione_head_ypos
    
    ### ZORDER
    zorder 8
    
    
label set_hermione_robe(robe = ""):
    hide screen hermione_main
    with d3
    call h_robe(robe)
    return
    
label h_robe(robe = ""):
    if robe == "":
        $ hermione_wear_robe = False
    else:
        $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/"+str(robe)
        $ hermione_wear_robe = True
    return
    
## Outfit Blocks
label set_hermione_outfit(outfit):
    show screen blkfade
    hide screen hermione_main
    with d3
    call h_outfit_OBJ(outfit)
    pause .5
    hide screen blkfade
    with d5
    return
    
label h_outfit_OBJ(outfit):
    if outfit == None:
        call update_her_uniform
        $ hermione_costume = False
        call h_update_hair
    else:
        $ hermione_costume = True
        
        $ hermoine_outfit_GLBL = outfit
        call h_update_hair
        
        if transparency < 1:
            if not hermione_perm_expand:
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png" 
            else:
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png"
        else:
            $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/"+outfit.breast_layer+".png"
        
    return
    
## Action Blocks
label set_hermione_action(action = ""):
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    call h_action(action)
    return
    
label h_action(action =  ""):
    $ hermione_action = False
    $ h_action_show_arms = False
    $ h_action_show_top = True
    $ h_action_show_skirt = True
    $ h_action_show_bra = True
    
    $ override = False
    
    if hermione_wear_panties or h_request_wear_panties or whoring < hg_NoPanties_lvl:
        $ h_action_show_panties = True
    else:
        $ h_action_show_panties = False
    if hermione_wear_bra:
        $ h_action_show_bra = True
    else:
        $ h_action_show_bra = False
    
    $ h_action_a = "00_blank.png"
    $ h_action_b = "00_blank.png"
    $ h_action_left_arm = "left_1.png"
    $ h_action_right_arm = "right_1.png"
    call set_h_action_vars
    call update_her_uniform
    call h_update_body
    
    if action == "" or action == "none" or action == 0:
        pass
    else:
        if hermione_costume:
            if action in hermoine_outfit_GLBL.actions:
                $ h_action_a = hermoine_outfit_GLBL.getActionImage(action)
        else:
            $ hermione_action = True
            $ hermione_action_bra = hermione_bra
            $ hermione_action_panties = hermione_panties
            $ hermione_action_top = hermione_top
            $ hermione_action_skirt = hermione_skirt
            
            if action == "lift_skirt":
                $ h_action_show_skirt = False
                $ h_action_show_arms = True
                if h_top >= 2 and h_top <= 4:
                    $ hermione_action_top = "01_hp/13_characters/hermione/clothes/uniform/action/lift_skirt_top_"+str(h_top)+".png"
                if whoring <= 5:
                    $ h_action_a = "lift_skirt_1.png"
                if whoring >= 6 and whoring <= 11:
                    $ h_action_a = "lift_skirt_2.png"
                if whoring >= 12 and whoring <= 19:
                    $ h_action_a = "lift_skirt_3.png"
                if whoring >= 20:
                    $ h_action_a = "lift_skirt_4.png"
                $ h_action_left_arm = "half_arm.png"
                $ h_action_right_arm = "00_blank.png"

            if action == "lift_skirt_naked":
                $ h_action_show_skirt = False
                $ h_action_show_arms = True
                $ h_action_show_top = False
                $ h_action_show_bra = False
                if whoring <= 5:
                    $ h_action_a = "lift_skirt_1.png"
                if whoring >= 6 and whoring <= 11:
                    $ h_action_a = "lift_skirt_2.png"
                if whoring >= 12 and whoring <= 19:
                    $ h_action_a = "lift_skirt_3.png"
                if whoring >= 20:
                    $ h_action_a = "lift_skirt_4.png"
                $ h_action_left_arm = "half_arm.png"
                $ h_action_right_arm = "00_blank.png"
                if not hermione_perm_expand:
                    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png" 
                else:
                    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png" 
                
            if action == "lift_top":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                if whoring <= 3:# shirt_00
                    $ h_action_a = "lift_top_1.png"
                elif whoring >= 4 and whoring <= 20:
                    $ h_action_a = "lift_top_2-4.png"
                elif whoring >= 21:
                    if day_random <= 4:# shirt_04
                        $ h_action_a = "lift_top_5_3.png"
                    if day_random >= 5:# shirt_05
                        $ h_action_a = "lift_top_6.png"
                if hermione_perm_expand:
                    $ h_action_b = "lift_top_expand_perm_overlay.png"
                else:
                    $ h_action_b = "lift_top_normal_overlay.png"
            
            if action == "hold_book":
                $ h_action_show_top = False
                if whoring <= 3:# shirt_00
                    $ h_action_a = "hold_book_1.png"
                elif whoring >= 4 and whoring <= 7:# shirt_01
                    $ h_action_a = "hold_book_2.png"
                elif whoring >= 8 and whoring <= 14:# shirt_02
                    $ h_action_a = "hold_book_3.png"
                elif whoring >= 15 and whoring <= 20:# shirt_03
                    $ h_action_a = "hold_book_4.png"
                elif whoring >= 21:
                    if day_random <= 4:# shirt_04
                        $ h_action_a = "hold_book_5.png"
                    if day_random >= 5:# shirt_05
                        $ h_action_a = "hold_book_6.png"
            
            if action == "expand_breasts" or action == "expand_all":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ h_action_show_arms = True
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded.png" 
            
            if action == "expand_ass" or action == "expand_all":
                $ h_action_show_skirt = False
                $ h_action_show_panties = False
                $ h_action_show_arms = True
                if whoring >= hg_NoPanties_lvl:
                    $ hermione_legs = "01_hp/13_characters/hermione/body/legs/expanded_ass.png"
                else:
                    $ hermione_legs = "01_hp/13_characters/hermione/body/legs/expanded_ass_panties.png"
            
            if action == "lift_breasts":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ override = True
                if not hermione_perm_expand:
                    $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/lift_breasts.png"
                else:
                    $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/lift_breasts_large.png"

            if action == "lift_breasts_naked":
                $ h_action_show_skirt = False
                $ h_action_show_panties = False
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ override = True
                if not hermione_perm_expand:
                    $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/lift_breasts.png"
                else:
                    $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/lift_breasts_large.png"
                
            if action == "lift_breasts_large":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ override = True
                $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/lift_breasts_large.png"
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_nipfix.png" 
                
            if action == "hands_behind":
                $ h_action_show_top = False
                $ h_action_show_skirt = False
                $ h_action_show_arms = True
                $ override = True
                $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/left/behind.png"
                $ hermione_action_right_arm = "01_hp/13_characters/hermione/body/arms/right/hand_behind.png"
                $ hermione_action_left_arm = "01_hp/13_characters/hermione/body/arms/left/00_blank.png"
                
            if action == "covering":
                $ h_action_show_top = False
                $ h_action_show_skirt = False
                $ h_action_show_bra = False
                $ h_action_show_panties = False
                $ override = True
                $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/covering.png"
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_nipfix.png" 

            if action == "fingering":
                $ h_action_show_top = False
                $ h_action_show_skirt = False
                $ h_action_show_bra = False
                $ h_action_show_panties = False
                $ h_action_show_arms = True
                $ override = True
                $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/finger.png"
                $ hermione_action_right_arm = "01_hp/13_characters/hermione/body/arms/right/right_1.png"
                $ hermione_action_left_arm = "01_hp/13_characters/hermione/body/arms/left/00_blank.png"
                if not hermione_perm_expand:
                    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png" 
                else:
                    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png"

            if action == "covering_top":
                $ h_action_show_top = False
                $ h_action_show_bra = False
                $ h_action_show_panties = False
                $ h_action_show_arms = True
                $ override = True
                $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/finger.png"
                $ hermione_action_right_arm = "01_hp/13_characters/hermione/body/arms/right/right_1.png"
                $ hermione_action_left_arm = "01_hp/13_characters/hermione/body/arms/left/00_blank.png"
                if not hermione_perm_expand:
                    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png" 
                else:
                    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png"
                
            if action == "pinch":
                $ h_action_show_top = False
                $ h_action_show_skirt = False
                $ h_action_show_bra = False
                $ h_action_show_panties = False
                $ override = True
                $ hermione_action_a = "01_hp/13_characters/hermione/body/arms/both/fingering_and_pinching.png"
                $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_nonips.png" 
            
            if action == "hands_cuffed":
                $ h_action_show_top = False
                $ h_action_show_arms = True
                $ override = True
                $ hermione_action_right_arm = "01_hp/13_characters/hermione/body/arms/left/00_blank.png"
                $ hermione_action_left_arm = "01_hp/13_characters/hermione/body/arms/left/cuffed.png"
                
            if action == "hands_free":
                $ h_action_show_arms = True
                $ h_action_left_arm = "left_1.png"
                $ h_action_right_arm = "right_1.png"
    
    if not override:
        call set_h_action_vars
    
    if action == "hold_book":
        $ hermione_action_b = hermione_hair_b
    
    if hermione_wetpanties == True and action == "lift_skirt" and hermione_wear_panties == True:
        $ hermione_action_b = "01_hp/13_characters/hermione/overlays/pantystain.png"
        
    return
    
label set_h_action_vars:
    $ hermione_action_right_arm = "01_hp/13_characters/hermione/body/arms/right/"+str(h_action_right_arm)
    $ hermione_action_left_arm = "01_hp/13_characters/hermione/body/arms/left/"+(h_action_left_arm)
    $ hermione_action_a = "01_hp/13_characters/hermione/clothes/uniform/action/"+str(h_action_a)
    $ hermione_action_b = "01_hp/13_characters/hermione/clothes/uniform/action/"+str(h_action_b)
    $ hermione_costume_action_a = "01_hp/13_characters/hermione/clothes/custom/"+str(h_action_a)
    return
    
    
## Control Blocks
label h_update:
    $ hermione_body = "01_hp/13_hermione_main/"+str(h_body)+".png"
    #$ hermione_body = "01_hp/13_characters/hermione/body/face/"+str(h_body)+".png"
    
    if h_tears != "":
        $ hermione_tears = "01_hp/13_characters/hermione/body/face/tears/"+str(h_tears)+".png"
    else:
        $ hermione_tears = "01_hp/13_characters/hermione/body/face/tears/00_blank.png"
    
    if h_body in hermione_anger or hermione_emote_anger:
        $ hermione_emote = "01_hp/13_characters/emote/01.png"
    elif h_body in hermione_exclam or hermione_emote_exclam:
        $ hermione_emote = "01_hp/13_characters/emote/02.png"
    elif h_body in hermione_hearts or hermione_emote_hearts:
        $ hermione_emote = "01_hp/13_characters/emote/03.png"
    elif h_body in hermione_question or hermione_emote_question:
        $ hermione_emote = "01_hp/13_characters/emote/04.png"
    elif h_body in hermione_sweat or hermione_emote_sweat:
        $ hermione_emote = "01_hp/13_characters/emote/05.png"
    elif hermione_body in hermione_suprize or hermione_emote_suprize:
        $ hermione_emote = "01_hp/13_characters/emote/06.png"
    else:
        $ hermione_emote = "01_hp/13_characters/emote/00_blank.png"
    return
   
label h_update_body:
    if not hermione_wear_top:
        if not hermione_wear_bra:
            if not hermione_perm_expand:
                $ h_breasts = "breasts_normal" # normal breasts
            else:
                $ h_breasts = "breasts_expanded" # expanded breasts
        elif h_bra in h_bra_nip_fix:
            $ h_breasts = "breasts_normal" # normal breasts
        else:
            $ h_breasts = "breasts_nipfix" # nipple corrected breasts
    else:
        $ h_breasts = "breasts_nipfix"

    if transparency < 1:
        if not hermione_perm_expand:
            $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png" 
        else:
            $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_expanded_large.png"
    else:
        $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/"+str(h_breasts)+".png"
    $ hermione_legs = "01_hp/13_characters/hermione/body/legs/legs_1.png"
    return
    
label h_update_hair:
    if hermione_costume and hermoine_outfit_GLBL.hair_layer != "":
        $ hermione_hair_a = "01_hp/13_characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+".png"
        $ hermione_hair_b = "01_hp/13_characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+"_2.png"
    else:
        $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
    return
    
label update_her_uniform:
    
    ### TOP
    #if whoring <= 3:# top 1
    #    $ h_top = 1
    #elif whoring >= 4 and whoring <= 7:# top 2
    #    $ h_top = 2
    #elif whoring >= 8 and whoring <= 14:# top 3
    #    $ h_top = 3
    #elif whoring >= 15 and whoring <= 20:# top 4
    #    $ h_top = 4
    #elif whoring >= 21:
    #    if day_random <= 4:# top 5
    #        $ h_top = 5
    #    if day_random >= 5:# top 6
    #        $ h_top = 6
    
    ### SKIRT  - Removed to accomodate the custom skirt levels
    #if "skirt_" in h_skirt:
    #    if whoring <= 5: # skirt 1
    #        $ h_skirt = "skirt_1"
    #    if whoring >= 6 and whoring <= 11: # skirt 2
    #        $ h_skirt = "skirt_2"
    #    if whoring >= 12 and whoring <= 19: # skirt 3
    #        $ h_skirt = "skirt_3"
    #    if whoring >= 20: # skirt 4
    #        $ h_skirt = "skirt_4"
    #        
        #$ h_skirt += h_skirt_color
        
        
    ### PANTIES
    if whoring >= hg_NoPanties_lvl:
        $ hermione_wear_panties = False
    if hermione_wetpanties:
        $ hermione_panties_overlay = "01_hp/13_characters/hermione/overlays/pantystain.png"
    else:
        $ hermione_panties_overlay = "01_hp/13_characters/hermione/overlays/00_blank.png"
        
    
    $ hermione_bra = "01_hp/13_characters/hermione/clothes/underwear/"+str(h_bra)+".png"
    $ hermione_stockings = "01_hp/13_characters/hermione/clothes/stockings/"+str(h_stocking)+".png"
    $ hermione_panties = "01_hp/13_characters/hermione/clothes/underwear/"+str(h_panties)+".png"
    $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/bot/"+h_skirt_color+str(h_skirt)+".png"
    $ hermione_badge = "01_hp/13_characters/hermione/accessories/badges/"+str(h_badge)+".png"
    if hermione_perm_expand and str(h_top) == '5':
        $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_5_B.png"
    elif hermione_perm_expand:
        $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_6_B.png"
    else:
        $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_"+str(h_top)+".png"
    
    if custom_skirt == 1: # jeans
        $ hermione_skirt = "01_hp/23_clothes_store/existing_stock/jeans.png"
        
    if custom_skirt == 5: # short_jeans
        $ hermione_skirt = "01_hp/23_clothes_store/existing_stock/jeans_short.png"
    
    call update_chibi_uniform
    call h_update_body
    
    return
    
label update_chibi_uniform:
    $ h_top = str(h_top)

    if not wear_shirts:
        $ hermione_chibi_blink = "ch_hem blink_n"
        $ hermione_chibi_blink_f = "ch_hem blink_n_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_n_01.png"
        $ hermione_chibi_walk = "ch_hem walk_n"
        $ hermione_chibi_walk_f = "ch_hem walk_n_flip"
        
        
    elif h_top == '1':# shirt_00
        $ hermione_chibi_blink = "ch_hem blink_a"
        $ hermione_chibi_blink_f = "ch_hem blink_a_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png"
        $ hermione_chibi_walk = "ch_hem walk_a"
        $ hermione_chibi_walk_f = "ch_hem walk_a_flip"
    elif h_top == '2':# shirt_01
        $ hermione_chibi_blink = "ch_hem blink_d"
        $ hermione_chibi_blink_f = "ch_hem blink_d_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_d_01.png"
        $ hermione_chibi_walk = "ch_hem walk_d"
        $ hermione_chibi_walk_f = "ch_hem walk_d_flip"
    elif h_top == '3':# shirt_02
        $ hermione_chibi_blink = "ch_hem blink_e"
        $ hermione_chibi_blink_f = "ch_hem blink_e_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_e_01.png"
        $ hermione_chibi_walk = "ch_hem walk_e"
        $ hermione_chibi_walk_f = "ch_hem walk_e_flip"
    elif h_top == '4':# shirt_03
        $ hermione_chibi_blink = "ch_hem blink_f"
        $ hermione_chibi_blink_f = "ch_hem blink_f_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_f_01.png"
        $ hermione_chibi_walk = "ch_hem walk_f"
        $ hermione_chibi_walk_f = "ch_hem walk_f_flip"
    elif h_top == '5':# shirt_04
        $ hermione_chibi_blink = "ch_hem blink_g"
        $ hermione_chibi_blink_f = "ch_hem blink_g_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_g_01.png"
        $ hermione_chibi_walk = "ch_hem walk_g"
        $ hermione_chibi_walk_f = "ch_hem walk_g_flip"
    elif h_top == '6':# shirt_05
        $ hermione_chibi_blink = "ch_hem blink_h"
        $ hermione_chibi_blink_f = "ch_hem blink_h_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_h_01.png"
        $ hermione_chibi_walk = "ch_hem walk_h"
        $ hermione_chibi_walk_f = "ch_hem walk_h_flip"
        
    return
    
label reset_hermione_main:
    show screen hermione_blank_main
    show screen hermione_blank_head
    show screen hermione_blank_chibi
    hide screen hermione_blank_main
    hide screen hermione_blank_head
    hide screen hermione_blank_chibi
    
    $ aftersperm = False #Show cum stains on Hermione's uniform.
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with d3
    call h_outfit_OBJ(None)
    call h_action("none")
    call update_her_uniform
    call h_update_body
    call h_update_hair
    return
    
    
label new_main_menu: # testing menu found in cheats or jumped to
    show screen hermione_main
    menu:
        "-update main-":
            call update_her_uniform
            jump new_main_menu
        "-tattoos-":
            $ hermione_tattoos.append("thigh/free")
            $ hermione_tattoos.append("thigh/tribal")
            $ hermione_tattoos.append("pubic/nocondoms")
            jump new_main_menu
        "-robes-":
            menu:
                "-off-":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/00_blank.png"
                    $ hermione_wear_robe = False
                    jump new_main_menu
                "-gryff robe basic-":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe gap-":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_gap.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe wide gap":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_gap_wide.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe off":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_off.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe no shirt":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe_shirt_none.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
                "-gryff robe quidditch":
                    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_quidditch.png"
                    $ hermione_wear_robe = True
                    jump new_main_menu
        "-outfits-":
            label new_main_menu_outfit:
            menu:
                "-action-" if False:
                    menu:
                        "-none-":
                            call h_action("")
                            jump new_main_menu_outfit
                        "-lift top-":
                            call h_action("lift_top")
                            jump new_main_menu_outfit
                        "-back-":
                            jump new_main_menu_outfit
                "-No Outfit-":
                    call h_outfit_OBJ(None)
                    jump new_main_menu_outfit
                "-Defined Outfits-":
                    label defined_outfits_menu:
                    python:
                        def_menu = []
                        for i in hermione_outfits_list:
                            def_menu.append((i.getMenuText(),i))
                        def_menu.append(("-Never mind-", "nvm"))
                        result = renpy.display_menu(def_menu)
                    if result == "nvm":
                        jump new_main_menu_outfit
                    else:
                        call h_outfit_OBJ(result)
                        jump defined_outfits_menu
                "-Back-":
                    jump new_main_menu
        
        "-hair-":
            label new_main_menu_hair:
            menu:
                "-Hair A-":
                    call set_h_hair(style="A")
                    jump new_main_menu_hair
                "-Hair B-":
                    call set_h_hair(style="B")
                    jump new_main_menu_hair
                "-Color-":
                    menu:
                        "-Brown-":
                            call set_h_hair(color=1)
                            jump new_main_menu_hair
                        "-Blonde-":
                            call set_h_hair(color=2)
                            jump new_main_menu_hair
                        "-Red-":
                            call set_h_hair(color=3)
                            jump new_main_menu_hair
                        "-Black-":
                            call set_h_hair(color=4)
                            jump new_main_menu_hair
                        "-Blue-":
                            call set_h_hair(color=5)
                            jump new_main_menu_hair
                        "-Orange-":
                            call set_h_hair(color=6)
                            jump new_main_menu_hair
                "-Back-":
                    jump new_main_menu
        
        "-Actions-":
            label new_main_menu_actions:
            menu:
                "-Lift top-":
                    call h_action("lift_top")
                    jump new_main_menu_actions
                "-Lift Skirt-":
                    call h_action("lift_skirt")
                    jump new_main_menu_actions
                "-Hold Book-":
                    call h_action("hold_book")
                    jump new_main_menu_actions
                "-Expand All-":
                    call h_action("expand_all")
                    jump new_main_menu_actions
                "-Expand Breasts-":
                    call h_action("expand_breasts")
                    jump new_main_menu_actions
                "-Expand Ass-":
                    call h_action("expand_ass")
                    jump new_main_menu_actions
                "-Lift Breasts-":
                    call h_action("lift_breasts")
                    jump new_main_menu_actions
                "-Lift Breasts Large-":
                    call h_action("lift_breasts_large")
                    jump new_main_menu_actions
                "-Arms Behind-":
                    call h_action("hands_behind")
                    jump new_main_menu_actions
                "-Arms cuffed-":
                    call h_action("hands_cuffed")
                    jump new_main_menu_actions
                "-Covering-":
                    call h_action("covering")
                    jump new_main_menu_actions
                "-Pinch-":
                    call h_action("pinch")
                    jump new_main_menu_actions
                "-No Action-":
                    call h_action("")
                    jump new_main_menu_actions
                "-Back-":
                    jump new_main_menu
        
        "-Base clothes-":
            label new_main_menu_base_clothes:
            menu:
                "-Toggle Top-":
                    if hermione_wear_top:
                        $ hermione_wear_top = False
                    else:
                        $ hermione_wear_top = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                "-Toggle Bra-":
                    if hermione_wear_bra:
                        $ hermione_wear_bra = False
                    else:
                        $ hermione_wear_bra = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                "-Toggle Skirt-":
                    if hermione_wear_skirt:
                        $ hermione_wear_skirt = False
                    else:
                        $ hermione_wear_skirt = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                "-Toggle Panties-":
                    if hermione_wear_panties:
                        $ hermione_wear_panties = False
                    else:
                        $ hermione_wear_panties = True
                    call update_her_uniform
                    jump new_main_menu_base_clothes
                    
                    
                "-Back-":
                    jump new_main_menu
        
        "-Underwear-":
            label new_main_menu_underwear:
            menu:
                "-normal-":
                    $ h_bra = "base_bra_white_1"
                    $ h_panties = "base_panties_1"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-cup-":
                    $ h_bra = "cup_bra"
                    $ h_panties = "cup_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-lace-":
                    $ h_bra = "lace_bra"
                    $ h_panties = "lace_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-silk-":
                    $ h_bra = "silk_bra"
                    $ h_panties = "silk_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-latex-":
                    $ h_bra = "latex_bra"
                    $ h_panties = "latex_panties"
                    call update_her_uniform
                    jump new_main_menu_underwear
                "-Back-":
                    jump new_main_menu
        
        "-Stockings-":
            label new_main_menu_stocking:
            menu:
                "-none-":
                    $ h_stocking = "00_blank"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-black-":
                    $ h_stocking = "black"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-fishnet_a-":
                    $ h_stocking = "fishnet_a"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-fishnet_b-":
                    $ h_stocking = "fishnet_b"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-gryff-":
                    $ h_stocking = "gryff"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-gryff_vibe-":
                    $ h_stocking = "gryff_vibe"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-lace-":
                    $ h_stocking = "lace"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-latex-":
                    $ h_stocking = "latex"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-slyth_vibe-":
                    $ h_stocking = "slyth_vibe"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-white-":
                    $ h_stocking = "white"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-pantyhose grey-":
                    $ h_stocking = "pantyhose grey"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-pantyhose tan-":
                    $ h_stocking = "pantyhose tan"
                    call update_her_uniform
                    jump new_main_menu_stocking
                "-Back-":
                    jump new_main_menu
        
        "-Toggle perm expand-":
            if hermione_perm_expand:
                $ hermione_perm_expand = False
            else:
                $ hermione_perm_expand = True
            call update_her_uniform
            jump new_main_menu            
            
        "-Hide Menu-":
            show screen ctc
            pause
            jump new_main_menu
        
        "-Never mind-":
            hide screen hermione_main
            jump day_main_menu
    
label set_h_animation(ani=u_h_animation, xpos = u_h_ani_xpos, ypos = u_h_ani_ypos):
    if ani != u_h_animation:
        $ u_h_animation = ani
    if ani == "sex_ani":
        $ u_h_ani_xpos = -210
        $ u_h_ani_ypos = 10
    if ani == "blowjob_ani":
        $ u_h_animation_paused = "hand_ani"
        $ u_h_ani_xpos = -150
        $ u_h_ani_ypos = 10
    return

label play_h_animation:
    hide screen u_h_ani_scr_pause
    if u_h_animation == "sex_ani":
        hide screen genie
        show screen chair_02
    if ani == "blowjob_ani":
        hide screen genie
        show screen chair_02
    #if:
    
    show screen u_h_animation
    return
    
label pause_u_animation:
    hide screen u_h_ani_scr
    show screen u_h_ani_scr_pause
    with d2
    return
    
label end_h_animation:
    if u_h_animation == "sex_ani":
        show screen genie
        hide screen chair_02
        hide screen u_h_animation
    #if:
    return
    
label set_defined_menu_vars:
    python:
        tmp_list_a = []
        tmp_list_b = []
        for i in range(0,hermione_defined_outfit_list_size):
            if hermione_outfit_names[i] not in ["null",""]:
                tmp_list_a.append(hermione_outfit_names[i])
                tmp_list_b.append(i)
        
        h_menu_list = [[0 for i in xrange(2)] for i in xrange(len(tmp_list_a)+1)]
        for i in range(0,len(tmp_list_a)):
            h_menu_list[i][0] = tmp_list_a[i]
            h_menu_list[i][1] = tmp_list_b[i]
        h_menu_list[len(h_menu_list)-1][0] = "-nevermind-"
        h_menu_list[len(h_menu_list)-1][1] = -1
    return
    
screen u_h_ani_scr:
    add u_h_animation at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
    
screen u_h_ani_scr_pause:
    add u_h_animation_paused at Position(xpos=u_ani_xpos, ypos=u_ani_ypos)
    
    
label h_uniform_levels:


    ### TOP
    if uniform_level == 0:
        $ hermione_chibi_blink = "ch_hem blink_n"
        $ hermione_chibi_blink_f = "ch_hem blink_n_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_n_01.png"
        $ hermione_chibi_walk = "ch_hem walk_n"
        $ hermione_chibi_walk_f = "ch_hem walk_n_flip"
    elif uniform_level == 1:
        $ h_top = 1
        $ h_skirt = "skirt_1"
        $ hermione_chibi_blink = "ch_hem blink_a"
        $ hermione_chibi_blink_f = "ch_hem blink_a_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png"
        $ hermione_chibi_walk = "ch_hem walk_a"
        $ hermione_chibi_walk_f = "ch_hem walk_a_flip"
    elif uniform_level == 2:
        $ h_top = 2
        $ hermione_chibi_blink = "ch_hem blink_d"
        $ hermione_chibi_blink_f = "ch_hem blink_d_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_d_01.png"
        $ hermione_chibi_walk = "ch_hem walk_d"
        $ hermione_chibi_walk_f = "ch_hem walk_d_flip"
    elif uniform_level == 3:
        $ h_top = 3
        $ h_skirt = "skirt_2"
        $ hermione_chibi_blink = "ch_hem blink_e"
        $ hermione_chibi_blink_f = "ch_hem blink_e_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_e_01.png"
        $ hermione_chibi_walk = "ch_hem walk_e"
        $ hermione_chibi_walk_f = "ch_hem walk_e_flip"
    elif uniform_level == 4:
        $ h_top = 4
        $ h_skirt = "skirt_3"
        $ hermione_chibi_blink = "ch_hem blink_f"
        $ hermione_chibi_blink_f = "ch_hem blink_f_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_f_01.png"
        $ hermione_chibi_walk = "ch_hem walk_f"
        $ hermione_chibi_walk_f = "ch_hem walk_f_flip"
    elif uniform_level == 5:
        $ h_top = 5
        $ h_skirt = "skirt_4"
        $ hermione_chibi_blink = "ch_hem blink_g"
        $ hermione_chibi_blink_f = "ch_hem blink_g_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_g_01.png"
        $ hermione_chibi_walk = "ch_hem walk_g"
        $ hermione_chibi_walk_f = "ch_hem walk_g_flip"
    elif uniform_level == 6:
        $ h_top = 6
        $ h_skirt = "skirt_4"
        $ hermione_chibi_blink = "ch_hem blink_h"
        $ hermione_chibi_blink_f = "ch_hem blink_h_flip"
        $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_h_01.png"
        $ hermione_chibi_walk = "ch_hem walk_h"
        $ hermione_chibi_walk_f = "ch_hem walk_h_flip"
    
    
    
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
                   