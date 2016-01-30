label __init_variables:
    $ h_body = "01_hp/13_characters/hermione/body/face/body_01.png"
    $ hermione_base = "01_hp/13_characters/hermione/body/base/hermione_base.png"
    $ hermione_legs  = "01_hp/13_characters/hermione/body/legs/legs_1.png"
    $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_1.png"
    $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/A_1.png"
    $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/A_1_2.png"
    $ hermione_left_arm = "01_hp/13_characters/hermione/body/arms/left/left_1.png"
    $ hermione_right_arm = "01_hp/13_characters/hermione/body/arms/right/right_1.png"
    
    $ h_hair_style = "A"
    $ h_hair_color = 1
    
    $ hermione_xpos = 370
    $ hermione_ypos = 0
    
    $ hermione_zorder = 8
    
    $ hermione_bra = "01_hp/13_characters/hermione/clothes/underwear/base_bra_white_1.png"
    $ hermione_panties = "01_hp/13_characters/hermione/clothes/underwear/base_panties_1.png"
    $ hermione_skirt = "01_hp/13_characters/hermione/clothes/uniform/skirt_1.png"
    $ hermione_top = "01_hp/13_characters/hermione/clothes/uniform/top_1.png"
    
    $ hermione_custom_a = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    $ hermione_custom_b = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    $ hermione_custom_c = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    $ hermione_custom_d = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    $ hermione_custom_e = "01_hp/13_characters/hermione/clothes/custom/00_blank.png"
    
    $ hermiome_action_a = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    $ hermiome_action_b = "01_hp/13_characters/hermione/clothes/uniform/action/00_blank.png"
    
    $ hermione_wear_bra = True
    $ hermione_wear_panties = True
    $ hermione_wear_skirt = True
    $ hermione_wear_top = True
    
    $ hermione_perm_expand = False
    $ hermione_custom_outfit = False
    $ hermione_action = False
    
    $ h_breasts = 1
    $ h_top = 1
    $ h_skirt = 1
    $ h_action_a = "00_blank.png"
    $ h_action_b = "00_blank.png"
    
    if not hasattr(renpy.store,'hair_a_tmp'): #important!
        $ hair_a_tmp = ""
    if not hasattr(renpy.store,'hair_b_tmp'): #important!
        $ hair_b_tmp = ""
    # 1 maid
    # 2 gryff cheer
    # 3 sly cheer
    # 4 heart dancer
    # 7 power girl
    # 8 mrs marvel
    # 9 harley
    # 10 ball dress
    # 11 christmas
    # 12 lara croft 
    
    $ hermione_custom_hair_list = []
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("power_hair")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("harley_hair")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    $ hermione_custom_hair_list.append("")
    
    
    $ hermione_custom_outfit_list = [[0 for i in xrange(5)] for i in xrange(16)]
    
    $ hermione_custom_outfit_list [1][0] = "maid_stockings.png" 
    $ hermione_custom_outfit_list [1][1] = "maid_skirt.png"
    $ hermione_custom_outfit_list [1][2] = "maid_top.png"
    $ hermione_custom_outfit_list [1][3] = "maid_gloves.png"
    $ hermione_custom_outfit_list [1][4] = "maid_hat.png"
    
    $ hermione_custom_outfit_list [2][0] = "cheer_stockings.png" 
    $ hermione_custom_outfit_list [2][1] = "cheer_pants.png"
    $ hermione_custom_outfit_list [2][2] = "cheer_top.png"
    $ hermione_custom_outfit_list [2][3] = ""
    $ hermione_custom_outfit_list [2][4] = ""
    
    $ hermione_custom_outfit_list [3][0] = "s_cheer_stockings.png" 
    $ hermione_custom_outfit_list [3][1] = "s_cheer_pants.png"
    $ hermione_custom_outfit_list [3][2] = "s_cheer_top.png"
    $ hermione_custom_outfit_list [3][3] = ""
    $ hermione_custom_outfit_list [3][4] = ""
    
    $ hermione_custom_outfit_list [4][0] = "heart_legs.png" 
    $ hermione_custom_outfit_list [4][1] = "heart_top.png"
    $ hermione_custom_outfit_list [4][2] = "heart_collar.png"
    $ hermione_custom_outfit_list [4][3] = ""
    $ hermione_custom_outfit_list [4][4] = ""
    
    $ hermione_custom_outfit_list [5][0] = "" 
    $ hermione_custom_outfit_list [5][1] = ""
    $ hermione_custom_outfit_list [5][2] = ""
    $ hermione_custom_outfit_list [5][3] = ""
    $ hermione_custom_outfit_list [5][4] = ""
    
    $ hermione_custom_outfit_list [6][0] = "" 
    $ hermione_custom_outfit_list [6][1] = ""
    $ hermione_custom_outfit_list [6][2] = ""
    $ hermione_custom_outfit_list [6][3] = ""
    $ hermione_custom_outfit_list [6][4] = ""
    
    $ hermione_custom_outfit_list [7][0] = "power_costume.png" 
    $ hermione_custom_outfit_list [7][1] = ""
    $ hermione_custom_outfit_list [7][2] = ""
    $ hermione_custom_outfit_list [7][3] = ""
    $ hermione_custom_outfit_list [7][4] = ""
    
    $ hermione_custom_outfit_list [8][0] = "marvel_pants.png" 
    $ hermione_custom_outfit_list [8][1] = "marvel_top.png"
    $ hermione_custom_outfit_list [8][2] = "marvel_sash.png"
    $ hermione_custom_outfit_list [8][3] = "marvel_gloves.png"
    $ hermione_custom_outfit_list [8][4] = ""
    
    $ hermione_custom_outfit_list [9][0] = "harley_pants.png" 
    $ hermione_custom_outfit_list [9][1] = "harley_top.png"
    $ hermione_custom_outfit_list [9][2] = "harley_gloves.png"
    $ hermione_custom_outfit_list [9][3] = "harley_collar.png"
    $ hermione_custom_outfit_list [9][3] = ""
    $ hermione_custom_outfit_list [9][4] = ""
    
    $ hermione_custom_outfit_list [10][0] = "ball_dress_skirt.png" 
    $ hermione_custom_outfit_list [10][1] = "ball_dress_top.png"
    $ hermione_custom_outfit_list [10][2] = ""
    $ hermione_custom_outfit_list [10][3] = ""
    $ hermione_custom_outfit_list [10][4] = ""
    
    $ hermione_custom_outfit_list [11][0] = "christmas_pants.png" 
    $ hermione_custom_outfit_list [11][1] = "christmas_top.png"
    $ hermione_custom_outfit_list [11][2] = "christmas_gloves.png"
    $ hermione_custom_outfit_list [11][3] = "christmas_collar.png"
    $ hermione_custom_outfit_list [11][4] = "christmas_antlers.png"
    
    $ hermione_custom_outfit_list [12][0] = "lara_pants.png" 
    $ hermione_custom_outfit_list [12][1] = "lara_top.png"
    $ hermione_custom_outfit_list [12][2] = "lara_gloves.png"
    $ hermione_custom_outfit_list [12][3] = ""
    $ hermione_custom_outfit_list [12][4] = ""
    
    return