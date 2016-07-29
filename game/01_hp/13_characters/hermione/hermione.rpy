label __init_variables:
    
    $ h_whoring = 0
    $ h_reputation = 21
    
    $ hermione_zorder = 5
    
    $ hg_NoPanties_lvl = 9
    
    if not hasattr(renpy.store,'hermione_xpos'): #important!
        $ hermione_xpos = 370
    if not hasattr(renpy.store,'hermione_ypos'): #important!
        $ hermione_ypos = 0
    if not hasattr(renpy.store,'hermione_head_xpos'): #important!
        $ hermione_head_xpos = 390
    if not hasattr(renpy.store,'hermione_head_ypos'): #important!
        $ hermione_head_ypos = 235
    
    $ hermione_body = "01_hp/13_characters/hermione/body/face/body_01.png"
    $ hermione_tears = "01_hp/13_characters/hermione/body/face/tears/00_blank.png"
    $ hermione_base = "01_hp/13_characters/hermione/body/base/hermione_base.png"
    $ hermione_legs  = "01_hp/13_characters/hermione/body/legs/legs_1.png"
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_nipfix.png"
    $ hermione_left_arm = "01_hp/13_characters/hermione/body/arms/left/left_1.png"
    $ hermione_right_arm = "01_hp/13_characters/hermione/body/arms/right/right_1.png"
    $ hermione_emote = "01_hp/13_characters/emote/00_blank.png"
    
    $ h_body = "body_01"
    $ h_tears = "00_blank"
    
    $ h_display_tears = False
    
    if not hasattr(renpy.store,'hermione_hair_a'): #important!
        $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/A_1.png"
    if not hasattr(renpy.store,'hermione_hair_b'): #important!
        $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/A_1_2.png"
    if not hasattr(renpy.store,'h_hair_style'): #important!
        $ h_hair_style = "A"
    if not hasattr(renpy.store,'h_hair_color'): #important!
        $ h_hair_color = 1
    
    if not hasattr(renpy.store,'hermione_bra'): #important!
        $ hermione_bra = "01_hp/13_characters/hermione/clothes/underwear/base_bra_white_1.png"
    if not hasattr(renpy.store,'hermione_panties'): #important!
        $ hermione_panties = "01_hp/13_characters/hermione/clothes/underwear/base_panties_1.png"
    $ hermione_panties_overlay = "01_hp/13_characters/hermione/overlays/00_blank.png"
    if not hasattr(renpy.store,'hermione_skirt'): #important!
        $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/skirt_1.png"
    if not hasattr(renpy.store,'hermione_top'): #important!
        $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_1.png"
    
    if not hasattr(renpy.store,'h_bra'): #important!
        $ h_bra = "base_bra_white_1"
    if not hasattr(renpy.store,'h_panties'): #important!
        $ h_panties = "base_panties_1"
    if not hasattr(renpy.store,'h_skirt'): #important!
        $ h_skirt = "skirt_1"
    if not hasattr(renpy.store,'h_top'): #important!
        $ h_top = 1
    if not hasattr(renpy.store,'h_skirt_color'): #important!
        $ h_skirt_color = ""
    $ hermione_wear_bra = True
    $ hermione_wear_panties = True
    $ hermione_wear_skirt = True
    $ hermione_wear_top = True
    
    if not hasattr(renpy.store,'h_request_wear_panties'): #important!
        $ h_request_wear_panties = False
    
    
    $ hermione_robe = "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png"
    $ hermione_badge = "01_hp/13_characters/hermione/accessories/badges/spew_badge.png"
    $ hermione_stockings = "01_hp/13_characters/hermione/clothes/stockings/00_blank.png"
    
    $ h_badge = "spew_badge"
    $ h_stocking = "00_blank"
    
    $ hermione_wear_robe = False
    $ hermione_badges = False
    
    
    $ h_breasts = "breasts_nipfix"
    $ h_bra_nip_fix = ["cup_bra","silk_bra","latex_bra"]
    
    $ h_can_color = ["A","B"]
    
    $ hermione_tattoos = []
    
    $ hermione_perm_expand = False
    
    ## Chibi Vars
    $ hermione_chibi_stand = "01_hp/16_hermione_chibi/walk/h_walk_a_01.png"
    $ hermione_chibi_blink = "ch_hem blink_a"
    $ hermione_chibi_blink_f = "ch_hem blink_a_flip"
    $ hermione_chibi_walk = "ch_hem walk_a"
    $ hermione_chibi_walk_f = "ch_hem walk_a_flip"
    $ hermione_chibi_zorder = 3
    
    ## Action Vars
    if not hasattr(renpy.store,'hermione_action'): #important!
        $ hermione_action = False
    
    $ hermione_action_bra = hermione_bra
    $ hermione_action_panties = hermione_panties
    $ hermione_action_top = hermione_top
    $ hermione_action_skirt = hermione_skirt
    
    $ hermione_action_left_arm = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermione_action_right_arm = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermione_action_a = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermione_action_b = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    
    $ h_action_right_arm = "00_blank.png"
    $ h_action_left_arm = "00_blank.png"
    $ h_action_a = "00_blank.png"
    $ h_action_b = "00_blank.png"
    
    $ h_action_show_arms = False
    $ h_action_show_bra = True
    $ h_action_show_panties = True
    $ h_action_show_top = True
    $ h_action_show_skirt = True
    
    ## Emote Vars
    $ hermione_emote_anger = False
    $ hermione_emote_exclam = False
    $ hermione_emote_hearts = False
    $ hermione_emote_question = False
    $ hermione_emote_sweat = False
    $ hermione_emote_suprize = False
    $ hermione_anger = ["body_51","body_76","body_86","body_110","body_218","body_351","body_346","body_345","body_343","body_317","body_309","head_exp/24"]
    $ hermione_exclam = ["head_exp/30"]
    $ hermione_hearts = []
    $ hermione_question = []
    $ hermione_sweat = ["body_24","body_34","body_57","body_108","body_208","body_340","head_exp/9"]
    $ hermione_suprize = ["body_80","body_80b","body_335"]
    
    
    
    $ u_h_animation = ""
    $ u_h_animation_paused = ""
    $ u_h_ani_xpos = 0
    $ u_h_ani_ypos = 0
    
    
    
    ## Custom Clothes/Outfits Vars
    if not hasattr(renpy.store,'custom_outfit'): #important!
        $ custom_outfit = 0
    if not hasattr(renpy.store,'hermione_costume'): #important!
        $ hermione_costume = False
    if not hasattr(renpy.store,'hermione_costume_action_a'): #important!
        $ hermione_costume_action_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    
    return
    
label her_main(text="",face=h_body,tears="", xpos = hermione_xpos, ypos = hermione_ypos):
    hide screen hermione_main
    #with d3
    if xpos != hermione_xpos:
        if xpos == 370:
            $ hermione_xpos = 510
        elif xpos == 120:
            $ hermione_xpos = 140
        else:
            $ hermione_xpos = xpos
    if ypos != hermione_ypos:
        $ hermione_ypos = ypos
    if face != h_body:
        $ h_body = face
        #$ hermione_body = her_path + str(face) + ".png"
    $ h_tears = tears
    call h_update
    show screen hermione_main
    with d1
    if text != "":
        if "[tmp_name]" in text or "[genie_name]" or "[hermione_name]" in text:
            if "[tmp_name]" in text:
                $ text = text.replace("[tmp_name]",tmp_name)
            if "[genie_name]" in text:
                $ text = text.replace("[genie_name]",genie_name)
            if "[hermione_name]" in text:
                $ text = text.replace("[hermione_name]",hermione_name)
        her "[text]"
    return
    
label her_head(text="",face=h_body,tears=""):
    if face != h_body:
        $ h_body = face
        # $ h_body = her_path + str(face) + ".png"
    $ h_tears = tears
    call h_update
    show screen hermione_head #h_head2
    if text != "":
        if "[tmp_name]" in text or "[genie_name]" in text:
            if "[tmp_name]" in text:
                $ text = text.replace("[tmp_name]",tmp_name)
            if "[genie_name]" in text:
                $ text = text.replace("[genie_name]",genie_name)
            if "[hermione_name]" in text:
                $ text = text.replace("[hermione_name]",hermione_name)
        her2 "[text]"
    hide screen hermione_head #h_head2
    return
    