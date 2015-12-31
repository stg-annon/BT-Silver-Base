    
### SCREENS ###
screen main_menu_01:
    imagebutton: # DOOR
        xpos 758 
        ypos 315
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "01_hp/05_props/01_door.png"
        hover "01_hp/05_props/01_door_02.png"
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("door")]
        
 
        
    imagebutton: # CUPBOARD
        xpos 120 
        ypos 280
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "01_hp/05_props/02_cupboard.png"
        hover "01_hp/05_props/02_cupboard_02.png"
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("cupboard")]
        
    if package_is_here:
        imagebutton: # THE PACKAGE
                xpos 260 
                ypos 235
                xanchor "center"
                yanchor "center"
                idle "01_hp/05_props/owl_06.png" 
                hover "01_hp/05_props/owl_06_2.png"
                #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ] 
                #unhovered [Hide("gui_tooltip")]
                action [Hide("main_menu_01"), Hide("package"), Jump("mail_02")]


    imagebutton: # GENIE
        xpos 230
        ypos 336
        focus_mask True
        xanchor "center"
        yanchor "center"
        idle "newanimation"
        hover "01_hp/05_props/11_genie_02.png"
        hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195, my_tt_ypos=210) ] 
        #hovered [Show("config_afterchoices_skip_idle.png", xpos=46, ypos=518) ]
        unhovered [Hide("gui_tooltip")]
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("desk")]
    
    imagebutton: # PHOENIX
        xpos 400 
        ypos 225
        #focus_mask True
        xanchor "center"
        yanchor "center"
        idle "pho_01" 
        hover "01_hp/05_props/06_phoenix_02.png"
        #hovered [Show("gui_tooltip", my_picture="exclaim_01", my_tt_xpos=195, my_tt_ypos=210) ] 
        #hovered [Show("config_afterchoices_skip_idle.png", xpos=46, ypos=518) ]
        #unhovered [Show("gui_tooltip", my_picture="feather", my_tt_xpos=360, my_tt_ypos=140, xanchor="center", yanchor="center") ]
        action [Hide("main_menu_01"), Hide("animation_feather"), Jump("phoenix")]
        
    imagebutton: # FIREPLACE
        xpos 553 
        ypos 277
        #focus_mask True
        xanchor "center"
        yanchor "center"
        idle "01_hp/05_props/03_fireplace_02.png" 
        hover "01_hp/05_props/03_fireplace_03.png"
        action [Hide("main_menu_01"), Jump("fireplace")]
     
    if letters >= 1: #Adds one letter in waiting list to be read. Displays owl with envelope.:
        imagebutton: # OWL
            xpos 315 
            ypos 270
            focus_mask True
            xanchor "center"
            yanchor "center"
            idle "owl_01" 
            hover "01_hp/05_props/owl_04.png"
            #hovered [Show("gui_tooltip", my_picture="hoot", my_tt_xpos=250, my_tt_ypos=180) ] 
            #unhovered [Hide("gui_tooltip")]
            action [Hide("main_menu_01"), Jump("mail")]
    


###MO SCREENS
screen map_screen:
    zorder hermione_main_zorder-1
    
    imagemap:
        ground "01_hp/25_mo/map_ground.png"
        idle "01_hp/25_mo/map_idle.png"
        hover "01_hp/25_mo/map_hover.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        hotspot (192, 229, 38, 20) clicked Jump("map_attic")   # attic
        hotspot (272, 373, 63, 41) clicked Jump("clothes_store")# clothes
        hotspot (25, 374, 102, 66) clicked Jump("map_forest") # forest
        hotspot (302, 523, 112, 49) clicked Jump("map_lake")   # lake
        hotspot (273, 459, 75, 8) clicked Jump("map_dorms")  # dorms
        #hotspot (656, 232, 106, 33) clicked Jump("inn_menu")   # inn
        #hotspot (376, 84, 111, 57) clicked Jump("map_pitch") # pitch
        hotspot (307, 240, 59, 37) clicked Jump("shop_menu")  # shop
        hotspot (33, 535, 39, 39) clicked Jump("day_main_menu")# return
        
screen room_back:
    if daytime:
        add "01_hp/25_mo/room_bg1.png"
    else:
        add "01_hp/25_mo/room_bg2.png"
    zorder 0

screen shop_screen:
    if daytime:
        add "01_hp/25_mo/room_bg1.png"
    else:
        add "01_hp/25_mo/room_bg2.png"
    add "01_hp/25_mo/shop_screen.png"
    imagebutton: # Books
        xpos 0 
        ypos 0
        focus_mask True
        idle "01_hp/25_mo/books1.png"
        hover "01_hp/25_mo/books2.png"
        action [Jump("shop_books")]
    imagebutton: # Return Button
        xpos 750 
        ypos 550
        focus_mask True
        idle "interface/continue.png"
        hover "interface/continue2.png"
        action [Jump("day_main_menu")]
    imagebutton: # Tentacle Scroll
        xpos 0 
        ypos 0
        focus_mask True
        idle "01_hp/25_mo/scroll_3_1.png"
        hover "01_hp/25_mo/scroll_3_2.png"
        action [Jump("tentacle_shop_scene")]
    imagebutton: # Potions
        xpos 0 
        ypos 0
        focus_mask True
        idle "01_hp/25_mo/potion_1_1.png"
        hover "01_hp/25_mo/potion_1_2.png"
        action [Jump("shop_potion_menu")]
    imagebutton: # Gift Box
        xpos 0 
        ypos 0
        focus_mask True
        idle "01_hp/25_mo/gift_1.png"
        hover "01_hp/25_mo/gift_2.png"
        action [Jump("gifts_menu")]
    imagebutton: # Scrolls 1
        xpos 0 
        ypos 0
        focus_mask True
        idle "01_hp/25_mo/scroll_1_1.png"
        hover "01_hp/25_mo/scroll_1_2.png"
        action [Jump("sscrolls")]
    imagebutton: # Scrolls 2
        xpos 0 
        ypos 0
        focus_mask True
        idle "01_hp/25_mo/scroll_2_1.png"
        hover "01_hp/25_mo/scroll_2_2.png"
        action [Jump("sscrolls2")]
    
screen cs_p1:
    
    tag clothes_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/18_store/cs_gui/c_s_ground.png"
        idle "01_hp/18_store/cs_gui/c_s_idle-1.png"
        hover "01_hp/18_store/cs_gui/c_s_hover-1.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        
        hotspot (56, 57, 156, 234) clicked [SetVariable("clothes_store_selection",1),Jump("cs_select")]
        hotspot (233, 57, 156, 234) clicked [SetVariable("clothes_store_selection",2),Jump("cs_select")]
        hotspot (409, 57, 156, 234) clicked [SetVariable("clothes_store_selection",3),Jump("cs_select")]
        hotspot (585, 57, 156, 234) clicked [SetVariable("clothes_store_selection",4),Jump("cs_select")]
        hotspot (56, 312, 156, 234) clicked [SetVariable("clothes_store_selection",5),Jump("cs_select")]
        hotspot (233, 312, 156, 234) clicked [SetVariable("clothes_store_selection",6),Jump("cs_select")]
        hotspot (409, 312, 156, 234) clicked [SetVariable("clothes_store_selection",7),Jump("cs_select")]
        hotspot (585, 312, 156, 234) clicked [SetVariable("clothes_store_selection",8),Jump("cs_select")]
        
        #hotspot (16, 552, 34, 34) clicked Return("left")
        hotspot (745, 552, 34, 34) clicked [SetVariable("clothes_store_curr_page",2),Show("cs_p2")]
        hotspot (742, 11, 42, 41) clicked [SetVariable("clothes_store_selection",-1),Jump("cs_select")]
    
screen cs_p2:
    
    tag clothes_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/18_store/cs_gui/c_s_ground.png"
        idle "01_hp/18_store/cs_gui/c_s_idle-2.png"
        hover "01_hp/18_store/cs_gui/c_s_hover-2.png"
        # (X upper-left corner, Y upper-left corner, width, height).
        
        hotspot (56, 57, 156, 234) clicked [SetVariable("clothes_store_selection",1),Jump("cs_select")]
        # hotspot (233, 57, 156, 234) clicked [SetVariable("clothes_store_selection",2),Jump("cs_select")]
        # hotspot (409, 57, 156, 234) clicked [SetVariable("clothes_store_selection",3),Jump("cs_select")]
        # hotspot (585, 57, 156, 234) clicked [SetVariable("clothes_store_selection",4),Jump("cs_select")]
        # hotspot (56, 312, 156, 234) clicked [SetVariable("clothes_store_selection",5),Jump("cs_select")]
        # hotspot (233, 312, 156, 234) clicked [SetVariable("clothes_store_selection",6),Jump("cs_select")]
        # hotspot (409, 312, 156, 234) clicked [SetVariable("clothes_store_selection",7),Jump("cs_select")]
        # hotspot (585, 312, 156, 234) clicked [SetVariable("clothes_store_selection",8),Jump("cs_select")]
        
        hotspot (16, 552, 34, 34) clicked [SetVariable("clothes_store_curr_page",1),Show("cs_p1")]
        #hotspot (745, 552, 34, 34) clicked [SetVariable("clothes_store_curr_page",3),Show("cs_p3")]
        hotspot (742, 11, 42, 41) clicked [SetVariable("clothes_store_selection",-1),Jump("cs_select")]
    
# screen cs_p3:
    
    # tag clothes_menu
    # zorder hermione_main_zorder-1
    
    # imagemap:
        # cache False
        # ground "01_hp/18_store/cs_gui/c_s_ground.png"
        # idle "01_hp/18_store/cs_gui/c_s_idle-3.png"
        # hover "01_hp/18_store/cs_gui/c_s_hover-3.png"
        # # (X upper-left corner, Y upper-left corner, width, height).
        
        # hotspot (56, 57, 156, 234) clicked [SetVariable("clothes_store_selection",1),Jump("cs_select")]
        # hotspot (233, 57, 156, 234) clicked [SetVariable("clothes_store_selection",2),Jump("cs_select")]
        # hotspot (409, 57, 156, 234) clicked [SetVariable("clothes_store_selection",3),Jump("cs_select")]
        # hotspot (585, 57, 156, 234) clicked [SetVariable("clothes_store_selection",4),Jump("cs_select")]
        # hotspot (56, 312, 156, 234) clicked [SetVariable("clothes_store_selection",5),Jump("cs_select")]
        # hotspot (233, 312, 156, 234) clicked [SetVariable("clothes_store_selection",6),Jump("cs_select")]
        # hotspot (409, 312, 156, 234) clicked [SetVariable("clothes_store_selection",7),Jump("cs_select")]
        # hotspot (585, 312, 156, 234) clicked [SetVariable("clothes_store_selection",8),Jump("cs_select")]
        
        # hotspot (16, 552, 34, 34) clicked [SetVariable("clothes_store_curr_page",2),Show("cs_p2")]
        # hotspot (745, 552, 34, 34) clicked [SetVariable("clothes_store_curr_page",4),Show("cs_p4")]
        # hotspot (742, 11, 42, 41) clicked [SetVariable("clothes_store_selection",-1),Jump("cs_select")]
    
screen cg:
    add cg_image

screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos
    
screen animation_feather: #Falling feather animation
    add "feather" xpos 360 ypos 140
    zorder 3
    
screen rum_screen: #Rummaging through the cumpboard.
    add "01_hp/05_props/02_cupboard_03.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=192, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "rum" xpos 20 ypos 110
    zorder 1
    
screen feeding: #FEEDING THE PHOENIX.
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "feeding" xpos 270 ypos 75
    zorder 1
    
screen petting: #PETTING THE PHOENIX.
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "petting" xpos 250 ypos 65
    zorder 1

screen sad_phoenix: #SAD SMILEY THAT SHOWS WHEN YOU PET THE BIRD.
    add "sad_01" xpos 423 ypos 130
    zorder 1
    
screen notes: #A bunch of notes poping out with a "win" sound effect.
    add "notes" xpos 320 ypos 330
    zorder 1
#################################################################
#########JJ  Flower production/dismissal  #######################
screen H_Flowers_in:  #  Hermione waves her wand and produces flowers 
    add "flower_appear" xpos 198 ypos 233
    zorder 1

screen H_Flowers_out:  #  Hermione waves her wand and flowers vanish
    add "vanish_effect_flower" xpos 198 ypos 235
    zorder 5

screen G_Flowers_in:  #  Genie produces flowers 
    add "bouquet_appear" xpos 198 ypos 235
    zorder 1

screen G_Flowers_out:  #  Genie flowers vanish
    add "vanish_effect_bouquet" xpos 198 ypos 235
    zorder 5
#########JJ  Chibi Animations - Everyon'e favorite  #############
screen her_wand_slow:  # Hermione rubs wand slowly
    add "rub_wand_slow_ani" 
#################################################################
screen hermione_02_w: #Hermione stands still wearing a robe.
    tag hermione
    add "01_hp/08_animation_02/h_Wand_01s.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
screen hermione_02_wSlow: #Hermione rubs wand between her legs slowly.
    tag hermione
    add "rub_wand_slow_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
screen hermione_02_wFast: #Hermione rubs wand between her legs quickly.
    tag hermione
    add "rub_wand_fast_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
screen hermione_02_wf1: #Hermione finishes rubbing the wand - eyes closed.
    tag hermione
    add "01_hp/08_animation_02/h_Wand_01f.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
screen hermione_02_wf2: #Hermione finishes rubbing the wand - eyes opened. 
    tag hermione
    add "01_hp/08_animation_02/h_Wand_02s.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
##################################################################
screen paperwork: #GENIE DOING PAPERWORK BEHIND HIS DESK.
    add "paperwork_02" xpos 84 ypos 205


screen reading_near_fire: #GENIE READING A BOOK BY THE FIRE.
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "reading_near_fire" xpos 290 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen reading: #GENIE READING A BOOK.
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "reading" xpos 290 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.

screen done_reading: #DONE READING THE BOOK.
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add im.Flip("01_hp/animation/reading_07.png", horizontal=True) xpos 290 ypos 205
    zorder 4 #Because otherwise the bird food would be on top.
    
screen done_reading_02: #DONE READING THE BOOK BY THE FIRE.
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=180, ypos=300, xanchor="center", yanchor="center")
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    add "01_hp/animation/reading_07.png" xpos 290 ypos 205

    zorder 4 #Because otherwise the bird food would be on top.
    
screen genie_jerking_off: #Genie sitting behind his desk and jerking off...
    add "genie_jerking_off" xpos 78 ypos 205
    zorder 2 
    tag chibi_genie
    
screen genie_jerking_sperm: #Genie cumming under the desk.
    add "genie_jerking_sperm_ani" xpos 78 ypos 205
    tag after_jerk
    zorder 2 
    
screen genie_jerking_sperm_02 :
    add "01_hp/animation/jerking_sperm_11.png" xpos 78 ypos 205
    tag after_jerk
    zorder 2 


    
screen candlefire_01:
    add "candle_fire" xpos 100 ypos 43
    zorder 2

screen candlefire_02:
    add "candle_fire_02" xpos 583 ypos 108
    zorder 2
   
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
screen phoenix_food: #Phoenix's food.
    add "01_hp/05_props/06_phoenix_food.png" xpos 350 ypos 49 
    zorder 3
    
screen fireplace_fire: #FIREPLACE FIRE.
    add "fireplace_fire" xpos 436 ypos 141
    zorder 3
    
    
    
screen room: #MAIN ROOM BG. #ну, тут все просто. Кстати, здесь zorder по умолчанию равен 0
    #zorder -2
    add "01_hp/01_bg/01_main_room.png"
screen room_night: #MAIN ROOM NIGHT BG. 
    add "01_hp/01_bg/01_main_room_02.png"
    
screen door:    
    add "01_hp/05_props/01_door.png" at Position(xpos=758, ypos=315, xanchor="center", yanchor="center")
screen cupboard:
    add "01_hp/05_props/02_cupboard_00.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
screen chair:
    add "01_hp/05_props/04_chair.png" at Position(xpos=653, ypos=300, xanchor="center", yanchor="center")
screen chair_02:
    add "01_hp/05_props/04_chair_02.png" at Position(xpos=192, ypos=300, xanchor="center", yanchor="center")
screen fireplace:
    add "01_hp/05_props/03_fireplace.png" at Position(xpos=553, ypos=277, xanchor="center", yanchor="center")
screen phoenix:
    add "01_hp/05_props/06_phoenix.png" at Position(xpos=400, ypos=225, xanchor="center", yanchor="center")
screen candle_01:
    add "01_hp/05_props/07_candle.png" at Position(xpos=693, ypos=225, xanchor="center", yanchor="center")
screen candle_02:
    add "01_hp/05_props/08_candle.png" at Position(xpos=210, ypos=160, xanchor="center", yanchor="center")
screen genie:
    tag chibi_genie
    add "01_hp/05_props/11_genie_00.png" at Position(xpos=230, ypos=336, xanchor="center", yanchor="center")
    #add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
screen owl: #DEFAULT OWL WITH ENVELOPE IN IT'S MOUTH.   
    add "01_hp/05_props/owl_01.png" at Position(xpos=315, ypos=270, xanchor="center", yanchor="center")
screen owl_02: #OWL. No Envelope.   
    add "01_hp/05_props/owl_05.png" at Position(xpos=315, ypos=270, xanchor="center", yanchor="center")
screen package: #PACKAGE.   
    add "01_hp/05_props/owl_06.png" at Position(xpos=260, ypos=235, xanchor="center", yanchor="center")
screen owl_03: #OWL SITTING ON A PACKAGE.
    add "01_hp/05_props/owl_05.png" at Position(xpos=310, ypos=235, xanchor="center", yanchor="center")
    
screen dumbledore: # DUMBLEDORE AND HIS DESK.
    tag chibi_genie
    add "01_hp/05_props/dum.png" at Position(xpos=230, ypos=336, xanchor="center", yanchor="center")

### EMO
screen thought: #Thinking emotion over a chibi.
    tag emo
    add "thought" xpos tt_xpos ypos tt_ypos
    zorder 2

### SNAPE CHIBI
screen snape_01: #Snape stands still near the door.
    tag snape
    add "01_hp/09_snape_ani/snape_0130.png" at Position(xpos=610, ypos=210)
    
screen snape_01_f: #Snape stands still near the door. (Mirrored).
    tag snape
    add im.Flip("01_hp/09_snape_ani/snape_0130.png", horizontal=True) at Position(xpos=610, ypos=210)
    
screen snape_02: #Snape stands still near the desk.
    tag snape
    add "01_hp/09_snape_ani/snape_0130.png" at Position(xpos=360, ypos=210) 
    zorder 3



    
    
screen snape_walk_01: #Default Snape walk animation. 
    tag snape
    add "snape_walk_01" at custom_walk(walk_xpos, walk_xpos2)
    #at Position(xpos=680, ypos=345, xanchor="center", yanchor="center")
    zorder 4

screen snape_walk_01_f: #Default Snape walk animation. (Mirrored).
    tag snape
    add "snape_walk_01_f" at custom_walk(walk_xpos, walk_xpos2)
    zorder 4

    
    
### HERMIONE CHIBI ###
screen hermione_01: #Hermione stands still.
    tag hermione
    if not wear_shirts:
        add "01_hp/16_hermione_chibi/walk/h_walk_n_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring <= 3:# shirt_00
        add "01_hp/16_hermione_chibi/walk/h_walk_a_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 4 and whoring <= 7:# shirt_01
        add "01_hp/16_hermione_chibi/walk/h_walk_d_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 8 and whoring <= 14:# shirt_02
        add "01_hp/16_hermione_chibi/walk/h_walk_e_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 15 and whoring <= 20:# shirt_03
        add "01_hp/16_hermione_chibi/walk/h_walk_f_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 21:
        if day_random <= 4:# shirt_04
            add "01_hp/16_hermione_chibi/walk/h_walk_g_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
        if day_random >= 5:# shirt_05
            add "01_hp/16_hermione_chibi/walk/h_walk_h_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 4

screen hermione_01_f: #Hermione stands still. (MIRRORED)
    tag hermione
    if not wear_shirts:
        add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_n_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring <= 3:# shirt_00
        add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_a_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 4 and whoring <= 7:# shirt_01
        add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_d_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 8 and whoring <= 14:# shirt_02
        add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_e_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 15 and whoring <= 20:# shirt_03
        add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_f_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 21:
        if day_random <= 4:# shirt_04
            add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_g_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
        if day_random >= 5:# shirt_05
            add im.Flip("01_hp/16_hermione_chibi/walk/h_walk_h_01.png", horizontal=True) at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 4

screen hermione_02: #Hermione stands still and blinks.
    tag hermione
    if not wear_shirts:
        add "ch_hem blink_n" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring <= 3:# shirt_00
        add "ch_hem blink_a" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 4 and whoring <= 7:# shirt_01
        add "ch_hem blink_d" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 8 and whoring <= 14:# shirt_02
        add "ch_hem blink_e" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 15 and whoring <= 20:# shirt_03
        add "ch_hem blink_f" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    elif whoring >= 21:
        if day_random <= 4:# shirt_04
            add "ch_hem blink_g" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
        if day_random >= 5:# shirt_05
            add "ch_hem blink_h" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    zorder 4
    
    
screen hermione_walk_01:
    tag hermione
    if not wear_shirts:
        add "ch_hem walk_n" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring <= 3:# shirt_00
        add "ch_hem walk_a" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 4 and whoring <= 7:# shirt_01
        add "ch_hem walk_d" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 8 and whoring <= 14:# shirt_02
        add "ch_hem walk_e" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 15 and whoring <= 20:# shirt_03
        add "ch_hem walk_f" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 21:
        if day_random <= 4:# shirt_04
            add "ch_hem walk_g" at custom_walk_02(walk_xpos, walk_xpos2)
        if day_random >= 5:# shirt_05
            add "ch_hem walk_h" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder 4
    
screen hermione_walk_01_f: #Hermione walking animation. facing right. (Leaving tower).
    tag hermione
    if not wear_shirts:
        add "ch_hem walk_n_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring <= 3:# shirt_00
        add "ch_hem walk_a_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 4 and whoring <= 7:# shirt_01
        add "ch_hem walk_d_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 8 and whoring <= 14:# shirt_02
        add "ch_hem walk_e_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 15 and whoring <= 20:# shirt_03
        add "ch_hem walk_f_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    elif whoring >= 21:
        if day_random <= 4:# shirt_04
            add "ch_hem walk_g_flip" at custom_walk_02(walk_xpos, walk_xpos2)
        if day_random >= 5:# shirt_05
            add "ch_hem walk_h_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder 4
    
screen hermione_run: #Hermione running. facing right. (Leaving tower).
    tag hermione
    add "ch_hem run_f" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder 4
    
screen hermione_chibi_robe: #Hermione. Chibi. Walking. Wearing a robe.
    tag hermione
    if not wear_shirts:
        add "ch_hem walk_robe_n" at custom_walk_02(walk_xpos, walk_xpos2)
    else:
        add "ch_hem walk_robe" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder 4

screen hermione_chibi_robe_f: #Hermione. Chibi. Walking. Wearing a robe.
    tag hermione
    if not wear_shirts:
        add "ch_hem walk_robe_n_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    else:
        add "ch_hem walk_robe_flip" at custom_walk_02(walk_xpos, walk_xpos2)
    zorder 4

    
    
    
screen hermione_02_b: #Hermione stands still wearing a robe.
    tag hermione
    add "01_hp/16_hermione_chibi/walk/h_walk_robe_01.png" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
screen hermione_03: #Hermione lifts her skirt
    tag hermione
    add "01_hp/16_hermione_chibi/panties_00.png" at Position(xpos=350, ypos=190)
    
screen hermione_03_b: #Hermione lifts her skirt. NO PANTIES.
    tag hermione
    add "01_hp/16_hermione_chibi/panties_01.png" at Position(xpos=350, ypos=190)

screen hermione_04: #Hermione lifts her shirt. Showing tits.
    tag hermione
    add "01_hp/16_hermione_chibi/tits_00.png" at Position(xpos=350, ypos=190)

screen hermione_04_b: #Hermione lifts her shirt. Showing tits. CLOSER TO THE DESK
    tag hermione
    add "01_hp/16_hermione_chibi/tits_00.png" at Position(xpos=250, ypos=190)


    
    
### GENIE CHIBI ###

screen genie_walk: #Default Genie walk animation. 
    tag chibi_genie
    add "genie_walk_ani" at genie_walk(walk_xpos, walk_xpos2)
  

### SNAPE FULL
screen snape_main: #Snape. Full size.
    tag big_snape
    add s_sprite xpos tt_xpos ypos tt_ypos
    #zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
    zorder 3 #Otherwise candle light is shown on top.
    


### SNAPE EMOTIONS
screen s_emo_01: #Closed eyes and closed mouth.
    tag semo
    add "01_hp/10_snape_main/s_emo_01.png" xpos tt_xpos ypos tt_ypos
    zorder 2 #Otherwise candle light is shown on top.
















### MISC SCREENS
screen bld1:
    add "01_hp/11_misc/bld.png"
    zorder 3
screen ctc:
    zorder 7
    add "ctc4"
screen points: #House points screen.
    add "01_hp/11_misc/points_02.png" at Position(xpos=0, ypos=1)  
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 146 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его        
        text "{size=-5}[slytherin]{/size}" #сумма текстом
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 10 xpos 252 ypos 11#отступ для текста, если надо прямо в левом углу — убираем его        
        text "{size=-5}[gryffindor]{/size}" #сумма текстом
    hbox: 
        spacing 10 xpos 365 ypos 11
        text "{size=-5}[hufflepuff]{/size}" 
    hbox: 
        spacing 10 xpos 37 ypos 11
        text "{size=-5}[ravenclaw]{/size}" 
##########################################################################################
#######   JJ  addition of Hermione Whoring/Mad level   ###################################
    hbox:
        spacing 10 xpos 490 ypos 11
        text "{size=-5}{color=#0033CC}W[whoring]{color=#A00000}  M[mad]{/color}{/size}"
##########################################################################################

    hbox: ### DAYS COUNTER ###
        spacing 10 xpos 630 ypos 10
        text "{size=-3}[day]{/size}" 
    
    hbox: ### DGOLD COUNTER ###
        spacing 10 xpos 734 ypos 10
        text "{size=-4}[gold]{/size}" 


screen gift:
    zorder 5
    add "01_hp/18_store/00.png" 
    add the_gift
    




    











screen letter:
    zorder 4
    add "01_hp/11_misc/letter.png" at Position(xpos=200, ypos=30)  
    hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
        spacing 40 xpos 270 ypos 80 xmaximum 250#отступ для текста, если надо прямо в левом углу — убираем его        
        text letter_text
screen blkfade:
    zorder 5
    add "interface/blackfade.png"
    
screen blktone:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.5)

screen blktone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/blackfade.png", 0.8)

screen whitetone8:
    zorder 5 #Otherwise bird's food will be on top.
    add im.Alpha("interface/white.jpg", 0.8)
    
screen white:
    zorder 3
    add "interface/white.jpg"
    
screen emo: #Character talking off screen.
    #zorder 3 
    add "emo8" at Position(xpos=700, ypos=100, xanchor=0, yanchor=0) 



        ### ADDING HOUSE POINTS ###
screen adding_03_points:
    add "what_03_points" at Position(xpos=131, ypos=0)

        ### GRYFFINDOR POINTS ###
screen gryffindor_03_points:
    add "what_03_points" at Position(xpos=238, ypos=0)
screen gryffindor_01_points:
    add "what_01_points" at Position(xpos=238, ypos=0)
screen gryffindor_02_points:
    add "what_02_points" at Position(xpos=238, ypos=0)
screen gryffindor_05_points:
    add "what_05_points" at Position(xpos=238, ypos=0)
screen gryffindor_15_points:
    add "what_15_points" at Position(xpos=238, ypos=0)
    
    
### Hufflepuff POINTS ###
screen hufflepuff_03_points:
    add "what_03_points" at Position(xpos=348, ypos=0)
screen hufflepuff_01_points:
    add "what_01_points" at Position(xpos=348, ypos=0)
screen hufflepuff_02_points:
    add "what_02_points" at Position(xpos=348, ypos=0)
screen hufflepuff_05_points:
    add "what_05_points" at Position(xpos=348, ypos=0)
screen hufflepuff_15_points:
    add "what_15_points" at Position(xpos=348, ypos=0)
    
### Ravenclaw POINTS ###
screen ravenclaw_03_points:
    add "what_03_points" at Position(xpos=22, ypos=0)
screen ravenclaw_01_points:
    add "what_01_points" at Position(xpos=22, ypos=0)
screen ravenclaw_02_points:
    add "what_02_points" at Position(xpos=22, ypos=0)
screen ravenclaw_05_points:
    add "what_05_points" at Position(xpos=22, ypos=0)
screen ravenclaw_15_points:
    add "what_15_points" at Position(xpos=22, ypos=0)
    
    
### UNIVERSAL POINTS AWARDING SCREEN FOR EVERY HOUSE ###

screen s_p_u: # SLYTHERIN
    add s_p_u_pic at Position(xpos=131, ypos=0)
    
screen g_p_u: # GRYFFINDOR
    add g_p_u_pic at Position(xpos=238, ypos=0)
    
screen h_p_u: # HUFFLEPUFF 
    add h_p_u_pic at Position(xpos=348, ypos=0)
    
screen r_p_u: # RAVENCLAW
    add r_p_u_pic at Position(xpos=22, ypos=0)
    
### MAIN SCREEN FOR ADDING POINTS ###


    

### EVENT 01 ###
screen genie_stands:
    add "01_hp/animation/feeding_01.png" xpos tt_xpos ypos tt_ypos
    
screen genie_stands_f: #Genie stands. Facing left.
    add im.Flip("01_hp/animation/feeding_01.png", horizontal=True) xpos tt_xpos ypos tt_ypos  

screen desk: #Genie's desk.
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 
    
screen desk_02: #Genie's desk.
    add "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center") 


### DUEL ###

screen snape_defends:
    add "ch_sna defend" at Position(xpos=-90, ypos=-5)
    zorder 7

### DAMAGE ###
screen minus_100:
    add "minus_100" at Position(xpos=640, ypos=120)

screen minus_300:
    add "minus_300" at Position(xpos=640, ypos=120)
    
    
screen minus_500:
    add "minus_500" at Position(xpos=640, ypos=120)
    
screen minus_0:
    add "minus_0" at Position(xpos=640, ypos=120)

screen minus_0_genie:
    add "minus_0" at Position(xpos=310, ypos=120)
screen minus_400_genie:
    add "minus_400" at Position(xpos=310, ypos=120)
screen minus_50_genie:
    add "minus_50" at Position(xpos=310, ypos=120)

screen plus_300:
    add "plus_300" at Position(xpos=310, ypos=120)



### HANGING WITH SNAPE ###

screen with_snape:
    add "01_hp/05_props/with_snape.png"
    tag hanging_with_snape
    zorder 3
screen with_snape_animated:
    add "genie_jerking_sperm"
    tag hanging_with_snape
    zorder 3

    
    
### HERMIONE MAIN ###
screen hermione_main: #Screen that shows a full sprite of HERMIONE.
    #tag big_hermione
    
    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "01_hp/13_hermione_main/body/head/"+str(hair_style)+"_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos
    if ears == True and hair_color >= 0:
        add "01_hp/25_mo/ears_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos #The hair. 
    
    add "01_hp/13_hermione_main/body/hermione_base.png" xpos h_xpos ypos h_ypos
    
    if lift_shirt == True or book_hold == True or skirt_up == True or fingering == True:
        pass
    else:
        add "01_hp/13_hermione_main/body/arms/left/left_0.png" xpos h_xpos ypos h_ypos
        add "01_hp/13_hermione_main/body/arms/right/right_0.png" xpos h_xpos ypos h_ypos
    
    if transparency < 1 or not wear_shirts or lift_shirt:
        add "01_hp/13_hermione_main/body/breasts/breasts_1.png" xpos h_xpos ypos h_ypos
    elif wear_shirts:
        add "01_hp/13_hermione_main/body/breasts/breasts_0.png" xpos h_xpos ypos h_ypos
        
    
    
    # if lift_shirt == True or book_hold == True or skirt_up == True or fingering == True:
        # add "01_hp/13_hermione_main/customs/base_3.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency < 1 or not wear_shirts:
        # add "01_hp/13_hermione_main/customs/base.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency == 1:
        # add "01_hp/13_hermione_main/customs/base_2.png" xpos h_xpos ypos h_ypos #Add her base 

    if collar >= 1 and not badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos h_xpos ypos h_ypos

    add h_body xpos h_xpos ypos h_ypos #Add her emotion

    if freckles == True:
        add "01_hp/25_mo/freckles.png" xpos h_xpos ypos h_ypos

    if not only_upper:
        add "01_hp/13_hermione_main/legs/base_01.png" xpos h_xpos ypos h_ypos #Add her legs

    if stockings == 1:
        add "01_hp/25_mo/maid_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 2:
        add "01_hp/25_mo/cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 3:
        add "01_hp/25_mo/stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 4:
        add "01_hp/25_mo/s_cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 5:
        add "01_hp/25_mo/h_cheer_stockings_2.png" xpos h_xpos ypos h_ypos
    else:
        if ne: # Desplays a fishnets in hermione_main screen.
            if ne_01:
                add "01_hp/13_hermione_main/nets.png" xpos h_xpos ypos h_ypos # FISHNETS.
                if not legs_02 and not only_upper and not legs_03: # Long skirt is on.
                    add "01_hp/13_hermione_main/patch.png" xpos h_xpos ypos h_ypos # Patch
    if fingering == True:
        add "01_hp/13_hermione_main/shirts/arm.png" xpos h_xpos ypos h_ypos
    if not only_upper:
        if whoring <= 12 or custom_bra >0 and panties:
            if custom_bra == 1:
                add im.Alpha("01_hp/25_mo/lace_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 2:
                add im.Alpha("01_hp/25_mo/cup_panties.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 3:
                add im.Alpha("01_hp/25_mo/silk_pants.png", transparency) xpos h_xpos ypos h_ypos
            else:
                add im.Alpha("01_hp/13_hermione_main/legs/pants.png", transparency) xpos h_xpos ypos h_ypos

        if custom_skirt >= 1 or custom_outfit >= 1 and custom_outfit <= 19 and not skirt_up:
            if custom_outfit == 1:
                add im.Alpha("01_hp/25_mo/maid_skirt.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_pants.png", transparency) xpos h_xpos ypos h_ypos            
            elif custom_outfit == 3:
                add im.Alpha("01_hp/25_mo/s_cheer_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 4:
                add im.Alpha("01_hp/25_mo/heart_legs.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 5:
                add im.Alpha("01_hp/25_mo/h_cheer_pants_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 8:
                add im.Alpha("01_hp/25_mo/marvel_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 9:
                add im.Alpha("01_hp/25_mo/harley_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 1:
                add im.Alpha("01_hp/25_mo/jeans.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 2:
                add im.Alpha("01_hp/25_mo/ass_exp1.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 3:
                add im.Alpha("01_hp/25_mo/ass_exp2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 4:
                add im.Alpha("01_hp/25_mo/snake.png", transparency) xpos h_xpos ypos h_ypos
        elif not skirt_up and custom_outfit <= 19:
            if whoring <= 5:
                add im.Alpha("01_hp/13_hermione_main/legs/legs_01.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 6 and whoring <= 11: #Mini skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_02.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 12 and whoring <= 19: #Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_03.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 20 and whoring <= 23: #Mini Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_04.png", transparency) xpos h_xpos ypos h_ypos
            else: #Mini Mini Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_05.png", transparency) xpos h_xpos ypos h_ypos
    if autograph:
        add "01_hp/13_hermione_main/auto.png" xpos h_xpos ypos h_ypos #Displays an autograph on her leg.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.

    if custom_bra >=1 and badges and custom_outfit <= 0:
        if custom_bra == 1:
            add im.Alpha("01_hp/25_mo/lace_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 2:
            add im.Alpha("01_hp/25_mo/cup_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3 and wear_shirts:
            add im.Alpha("01_hp/25_mo/silk_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3:
            add im.Alpha("01_hp/25_mo/silk_bra_2.png", transparency) xpos h_xpos ypos h_ypos
    if h_tears:
        add u_tears_pic xpos h_xpos ypos h_ypos #Universal tears layer.

    if skirt_up == True:
        if wear_shirts and badges:
            add "01_hp/13_hermione_main/shirts/skirt_up.png" xpos h_xpos ypos h_ypos #Displays sperm.
        elif fingering == True:
            add "01_hp/13_hermione_main/shirts/skirt_up_3.png" xpos h_xpos ypos h_ypos #Displays sperm.
        else:
            add "01_hp/13_hermione_main/shirts/skirt_up_2.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif fingering == True and not wear_shirts:
        add "01_hp/13_hermione_main/shirts/fingering_06.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif book_hold and not wear_shirts:
        add "01_hp/13_hermione_main/shirts/book_04.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit >= 1 or custom_breast >= 1:
            if custom_outfit == 1 and not robeon:
                add im.Alpha("01_hp/25_mo/maid_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 3:
                add im.Alpha("01_hp/25_mo/s_cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 4:
                add im.Alpha("01_hp/25_mo/heart_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 5:
                add im.Alpha("01_hp/25_mo/h_cheer_top_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 6:
                add im.Alpha("01_hp/25_mo/jumper.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 7:
                add im.Alpha("01_hp/25_mo/power_costume.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 7.2:
                add im.Alpha("01_hp/25_mo/power_costume_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 8:
                add im.Alpha("01_hp/25_mo/marvel_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("01_hp/25_mo/marvel_sash.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 9:
                add im.Alpha("01_hp/25_mo/harley_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("01_hp/25_mo/harley_collar.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_breast == 1:
                add "01_hp/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 2:
                add "01_hp/25_mo/tit_exp_2.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 3:
                add "01_hp/25_mo/tit_exp_3.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 4:
                add "01_hp/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
                add "01_hp/25_mo/expanded_shirt.png" xpos h_xpos ypos h_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "01_hp/13_hermione_main/shirts/book_01.png" xpos h_xpos ypos h_ypos #Displays sperm.
                else:
                    add "01_hp/13_hermione_main/shirts/book_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_01.png" xpos h_xpos ypos h_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_02.png" xpos h_xpos ypos h_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_03.png" xpos h_xpos ypos h_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_04.png" xpos h_xpos ypos h_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_04.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_05.png" xpos h_xpos ypos h_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_05.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_00.png" xpos h_xpos ypos h_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "01_hp/13_hermione_main/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif lift_shirt == True:
        add "01_hp/13_hermione_main/shirts/shirt_up.png" xpos h_xpos ypos h_ypos
    if collar >= 1 and badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos h_xpos ypos h_ypos


    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair_2.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair_2.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "01_hp/13_hermione_main/body/head/"+str(hair_style)+"_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos
    
    
    if ears == True and hair_color >= 0:
        add "01_hp/25_mo/ears_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos #The hair.  

    if glasses_worn:
        add "01_hp/13_hermione_main/glasses.png" xpos h_xpos ypos h_ypos #The glasses.

    if custom_outfit == 1:
        add "01_hp/25_mo/maid_hat.png" xpos h_xpos ypos h_ypos
        add "01_hp/25_mo/maid_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 4:
        add "01_hp/25_mo/heart_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 8:
        add "01_hp/25_mo/marvel_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_gloves.png" xpos h_xpos ypos h_ypos

    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos h_xpos ypos h_ypos #Universal sperm.        
    if badges and not robeon and custom_outfit == 0 and wear_shirts:
        if ba_01 and whoring <= 12:
            add "01_hp/13_hermione_main/badge.png" xpos h_xpos ypos h_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "01_hp/25_mo/cum_badge.png" xpos h_xpos ypos h_ypos
    if robeon:
        add "01_hp/13_hermione_main/robe.png" xpos h_xpos ypos h_ypos #The Robe.
    if robe == 1:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 2:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 3:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 4:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    if tentacle_cosmetic == True:
        add "01_hp/25_mo/tentacles.png" xpos h_xpos ypos h_ypos #The Tentacles.
    
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in anger or emote_anger:
        add "01_hp/13_hermione_main/body/emote/00.png" xpos h_xpos ypos h_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in exclam or emote_exclam:
        add "01_hp/13_hermione_main/body/emote/01.png" xpos h_xpos ypos h_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in hearts or emote_hearts:
        add "01_hp/13_hermione_main/body/emote/02.png" xpos h_xpos ypos h_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in question or emote_question:
        add "01_hp/13_hermione_main/body/emote/03.png" xpos h_xpos ypos h_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in sweat or emote_sweat:
        add "01_hp/13_hermione_main/body/emote/04.png" xpos h_xpos ypos h_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in suprize or emote_suprize:
        add "01_hp/13_hermione_main/body/emote/05.png" xpos h_xpos ypos h_ypos #Custom
    
    zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
    
screen hermione_main2:
    
    add "01_hp/13_hermione_main/body/hermione_base.png" xpos h_xpos ypos h_ypos
    
    
    
    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "01_hp/13_hermione_main/body/head/"+str(hair_style)+"_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos
    if ears == True and hair_color >= 0:
        add "01_hp/25_mo/ears_"+str(hair_color)+".png" xpos h_xpos ypos h_ypos #The hair. 
    
    
    if leg_pos >= 0:
        add "01_hp/13_hermione_main/body/legs/legs_"+str(leg_pos)+".png" xpos h_xpos ypos h_ypos
    
    
    
    if right_arm_pos >= 0:
        add "01_hp/13_hermione_main/body/arms/right/right_"+str(right_arm_pos)+".png" xpos h_xpos ypos h_ypos
    
    
    
    if left_arm_pos >= 0:
        add "01_hp/13_hermione_main/body/arms/left/left_"+str(left_arm_pos)+".png" xpos h_xpos ypos h_ypos
    
    
    
    if her_breasts >= 0:
        add "01_hp/13_hermione_main/body/breasts/breasts_"+str(her_breasts)+".png" xpos h_xpos ypos h_ypos
    
    
    
    add h_body xpos h_xpos ypos h_ypos #Add her emotion
    
    

    
    
    # if lift_shirt == True or book_hold == True or skirt_up == True or fingering == True:
        # add "01_hp/13_hermione_main/customs/base_3.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency < 1 or not wear_shirts:
        # add "01_hp/13_hermione_main/customs/base.png" xpos h_xpos ypos h_ypos #Add her base 
    # elif transparency == 1:
        # add "01_hp/13_hermione_main/customs/base_2.png" xpos h_xpos ypos h_ypos #Add her base 

    if collar >= 1 and not badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos h_xpos ypos h_ypos


    if freckles == True:
        add "01_hp/25_mo/freckles.png" xpos h_xpos ypos h_ypos

    if not only_upper:
        add "01_hp/13_hermione_main/legs/base_01.png" xpos h_xpos ypos h_ypos #Add her legs

    if stockings == 1:
        add "01_hp/25_mo/maid_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 2:
        add "01_hp/25_mo/cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 3:
        add "01_hp/25_mo/stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 4:
        add "01_hp/25_mo/s_cheer_stockings.png" xpos h_xpos ypos h_ypos
    elif stockings == 5:
        add "01_hp/25_mo/h_cheer_stockings_2.png" xpos h_xpos ypos h_ypos
    else:
        if ne: # Desplays a fishnets in hermione_main screen.
            if ne_01:
                add "01_hp/13_hermione_main/nets.png" xpos h_xpos ypos h_ypos # FISHNETS.
                if not legs_02 and not only_upper and not legs_03: # Long skirt is on.
                    add "01_hp/13_hermione_main/patch.png" xpos h_xpos ypos h_ypos # Patch
    if fingering == True:
        add "01_hp/13_hermione_main/shirts/arm.png" xpos h_xpos ypos h_ypos
    if not only_upper:
        if whoring <= 12 or custom_bra >0 and panties:
            if custom_bra == 1:
                add im.Alpha("01_hp/25_mo/lace_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 2:
                add im.Alpha("01_hp/25_mo/cup_panties.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_bra == 3:
                add im.Alpha("01_hp/25_mo/silk_pants.png", transparency) xpos h_xpos ypos h_ypos
            else:
                add im.Alpha("01_hp/13_hermione_main/legs/pants.png", transparency) xpos h_xpos ypos h_ypos

        if custom_skirt >= 1 or custom_outfit >= 1 and custom_outfit <= 19 and not skirt_up:
            if custom_outfit == 1:
                add im.Alpha("01_hp/25_mo/maid_skirt.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_pants.png", transparency) xpos h_xpos ypos h_ypos            
            elif custom_outfit == 3:
                add im.Alpha("01_hp/25_mo/s_cheer_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 4:
                add im.Alpha("01_hp/25_mo/heart_legs.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 5:
                add im.Alpha("01_hp/25_mo/h_cheer_pants_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 8:
                add im.Alpha("01_hp/25_mo/marvel_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 9:
                add im.Alpha("01_hp/25_mo/harley_pants.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 1:
                add im.Alpha("01_hp/25_mo/jeans.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 2:
                add im.Alpha("01_hp/25_mo/ass_exp1.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 3:
                add im.Alpha("01_hp/25_mo/ass_exp2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_skirt == 4:
                add im.Alpha("01_hp/25_mo/snake.png", transparency) xpos h_xpos ypos h_ypos
        elif not skirt_up and custom_outfit <= 19:
            if whoring <= 5:
                add im.Alpha("01_hp/13_hermione_main/legs/legs_01.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 6 and whoring <= 11: #Mini skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_02.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 12 and whoring <= 19: #Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_03.png", transparency) xpos h_xpos ypos h_ypos
            elif whoring >= 20 and whoring <= 23: #Mini Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_04.png", transparency) xpos h_xpos ypos h_ypos
            else: #Mini Mini Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_05.png", transparency) xpos h_xpos ypos h_ypos
    if autograph:
        add "01_hp/13_hermione_main/auto.png" xpos h_xpos ypos h_ypos #Displays an autograph on her leg.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.

    if custom_bra >=1 and badges and custom_outfit <= 0:
        if custom_bra == 1:
            add im.Alpha("01_hp/25_mo/lace_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 2:
            add im.Alpha("01_hp/25_mo/cup_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3 and wear_shirts:
            add im.Alpha("01_hp/25_mo/silk_bra.png", transparency) xpos h_xpos ypos h_ypos
        elif custom_bra == 3:
            add im.Alpha("01_hp/25_mo/silk_bra_2.png", transparency) xpos h_xpos ypos h_ypos
    if h_tears:
        add u_tears_pic xpos h_xpos ypos h_ypos #Universal tears layer.

    if skirt_up == True:
        if wear_shirts and badges:
            add "01_hp/13_hermione_main/shirts/skirt_up.png" xpos h_xpos ypos h_ypos #Displays sperm.
        elif fingering == True:
            add "01_hp/13_hermione_main/shirts/skirt_up_3.png" xpos h_xpos ypos h_ypos #Displays sperm.
        else:
            add "01_hp/13_hermione_main/shirts/skirt_up_2.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif fingering == True and not wear_shirts:
        add "01_hp/13_hermione_main/shirts/fingering_06.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif book_hold and not wear_shirts:
        add "01_hp/13_hermione_main/shirts/book_04.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit >= 1 or custom_breast >= 1:
            if custom_outfit == 1 and not robeon:
                add im.Alpha("01_hp/25_mo/maid_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 3:
                add im.Alpha("01_hp/25_mo/s_cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 4:
                add im.Alpha("01_hp/25_mo/heart_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 5:
                add im.Alpha("01_hp/25_mo/h_cheer_top_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 6:
                add im.Alpha("01_hp/25_mo/jumper.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 7:
                add im.Alpha("01_hp/25_mo/power_costume.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 7.2:
                add im.Alpha("01_hp/25_mo/power_costume_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 8:
                add im.Alpha("01_hp/25_mo/marvel_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("01_hp/25_mo/marvel_sash.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 9:
                add im.Alpha("01_hp/25_mo/harley_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("01_hp/25_mo/harley_collar.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_breast == 1:
                add "01_hp/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 2:
                add "01_hp/25_mo/tit_exp_2.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 3:
                add "01_hp/25_mo/tit_exp_3.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 4:
                add "01_hp/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
                add "01_hp/25_mo/expanded_shirt.png" xpos h_xpos ypos h_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "01_hp/13_hermione_main/shirts/book_01.png" xpos h_xpos ypos h_ypos #Displays sperm.
                else:
                    add "01_hp/13_hermione_main/shirts/book_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_01.png" xpos h_xpos ypos h_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_02.png" xpos h_xpos ypos h_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_03.png" xpos h_xpos ypos h_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_04.png" xpos h_xpos ypos h_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_04.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_05.png" xpos h_xpos ypos h_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_05.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_00.png" xpos h_xpos ypos h_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "01_hp/13_hermione_main/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    elif lift_shirt == True:
        add "01_hp/13_hermione_main/shirts/shirt_up.png" xpos h_xpos ypos h_ypos
    if collar >= 1 and badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos h_xpos ypos h_ypos


    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair_2.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair_2.png" xpos h_xpos ypos h_ypos
    elif hair_color >= 0:
        add "01_hp/13_hermione_main/body/head/"+str(hair_style)+"_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos
    
    
    if ears == True and hair_color >= 0:
        add "01_hp/25_mo/ears_"+str(hair_color)+"_2.png" xpos h_xpos ypos h_ypos #The hair. 
    
    
    if glasses_worn:
        add "01_hp/13_hermione_main/glasses.png" xpos h_xpos ypos h_ypos #The glasses.

    if custom_outfit == 1:
        add "01_hp/25_mo/maid_hat.png" xpos h_xpos ypos h_ypos
        add "01_hp/25_mo/maid_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 4:
        add "01_hp/25_mo/heart_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 8:
        add "01_hp/25_mo/marvel_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_gloves.png" xpos h_xpos ypos h_ypos

    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos h_xpos ypos h_ypos #Universal sperm.        
    if badges and not robeon and custom_outfit == 0 and wear_shirts:
        if ba_01 and whoring <= 12:
            add "01_hp/13_hermione_main/badge.png" xpos h_xpos ypos h_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "01_hp/25_mo/cum_badge.png" xpos h_xpos ypos h_ypos
    if robeon:
        add "01_hp/13_hermione_main/robe.png" xpos h_xpos ypos h_ypos #The Robe.
    if robe == 1:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 2:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 3:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    elif robe == 4:
        add im.Alpha("01_hp/13_hermione_main/shirts/robe_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
    if tentacle_cosmetic == True:
        add "01_hp/25_mo/tentacles.png" xpos h_xpos ypos h_ypos #The Tentacles.
    
    if face_exp in anger or emote_anger:
        add "01_hp/13_hermione_main/body/emote/00.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in exclam or emote_exclam:
        add "01_hp/13_hermione_main/body/emote/01.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in hearts or emote_hearts:
        add "01_hp/13_hermione_main/body/emote/02.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in question or emote_question:
        add "01_hp/13_hermione_main/body/emote/03.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in sweat or emote_sweat:
        add "01_hp/13_hermione_main/body/emote/04.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
    if face_exp in suprize or emote_suprize:
        add "01_hp/13_hermione_main/body/emote/05.png" xpos main_scr_xpos ypos main_scr_ypos #Custom
        
    zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
    
    
screen c_scene: #Custom Scenes
    tag head
    if scene_number == 1:
        add "01_hp/26_cg/scene_01.png" xpos 0 ypos 0
    if scene_number == 2:
        add "01_hp/26_cg/scene_02.png" xpos 0 ypos 0
    if scene_number == 3:
        add "01_hp/26_cg/scene_03.png" xpos 0 ypos 0
    if scene_number == 4:
        add "01_hp/26_cg/scene_04.png" xpos 0 ypos 0
    zorder 3
 
 
 
screen ch_potion:
   add "ch_hem potion" xpos 355 ypos 250
   zorder 0
 
screen ch_hotdog:
  add "ch_hem hotdog" xpos -210 ypos 10
  zorder 0
 
 
 
 
### HERMIONE HEAD ONLY ###
screen h_head: #Screen that shows a full sprite of HERMIONE.
    tag head
    if not only_upper:
        add "01_hp/13_hermione_main/legs_01.png" xpos h_xpos ypos h_ypos
    
    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair.png" xpos h_xpos ypos h_ypos
    elif hair_color == 0:
        add "01_hp/13_hermione_main/hair/hair_00.png" xpos h_xpos ypos h_ypos #The hair.    
    elif hair_color == 1:
        add "01_hp/13_hermione_main/hair/hair_01.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 2:
        add "01_hp/13_hermione_main/hair/hair_02.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 3:
        add "01_hp/13_hermione_main/hair/hair_03.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 4:
        add "01_hp/13_hermione_main/hair/hair_04.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 5:
        add "01_hp/13_hermione_main/hair/hair_05.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 6:
        add "01_hp/13_hermione_main/hair/hair_06.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 7:
        add "01_hp/13_hermione_main/hair/hair_07.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 8:
        add "01_hp/13_hermione_main/hair/hair_08.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 9:
        add "01_hp/13_hermione_main/hair/hair_09.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 10:
        add "01_hp/13_hermione_main/hair/hair_10.png" xpos h_xpos ypos h_ypos #The hair.

    if ears == True and hair_color == 0:
        add "01_hp/25_mo/ears_0.png" xpos h_xpos ypos h_ypos #The hair.    
    
    if ears == True and hair_color == 1:
        add "01_hp/25_mo/ears_1.png" xpos h_xpos ypos h_ypos #The hair.   
    
    if ears == True and hair_color == 2:
        add "01_hp/25_mo/ears_2.png" xpos h_xpos ypos h_ypos #The hair.   

    if ears == True and hair_color == 3:
        add "01_hp/25_mo/ears_3.png" xpos h_xpos ypos h_ypos #The hair.   

    if ears == True and hair_color == 6:
        add "01_hp/25_mo/ears_6.png" xpos h_xpos ypos h_ypos #The hair.   

    if transparency < 1 and badges or not wear_shirts:
        add "01_hp/13_hermione_main/customs/base.png" xpos h_xpos ypos h_ypos #Add her base 

    if collar >= 1 and badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos h_xpos ypos h_ypos

    add h_body xpos h_xpos ypos h_ypos

    if freckles == True:
        add "01_hp/25_mo/freckles.png" xpos h_xpos ypos h_ypos

    if h_tears:
        add u_tears_pic xpos h_xpos ypos h_ypos #Universal tears layer.
    if not badges and level == "01":
        add "01_hp/13_hermione_main/shirts/shirt_00.png" xpos h_xpos ypos h_ypos #The shirts.
    if badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit >= 1 or custom_breast >= 1:
            if custom_outfit == 1 and not robeon:
                add im.Alpha("01_hp/25_mo/maid_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 3:
                add im.Alpha("01_hp/25_mo/s_cheer_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 4:
                add im.Alpha("01_hp/25_mo/heart_top.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 5:
                add im.Alpha("01_hp/25_mo/h_cheer_top_2.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 6:
                add im.Alpha("01_hp/25_mo/jumper.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 7:
                add im.Alpha("01_hp/25_mo/power_costume.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 8:
                add im.Alpha("01_hp/25_mo/marvel_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("01_hp/25_mo/marvel_sash.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_outfit == 9:
                add im.Alpha("01_hp/25_mo/harley_top.png", transparency) xpos h_xpos ypos h_ypos
                add im.Alpha("01_hp/25_mo/harley_collar.png", transparency) xpos h_xpos ypos h_ypos
            elif custom_breast == 1:
                add "01_hp/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 2:
                add "01_hp/25_mo/tit_exp_2.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 3:
                add "01_hp/25_mo/tit_exp_3.png" xpos h_xpos ypos h_ypos
            elif custom_breast == 4:
                add "01_hp/25_mo/tit_exp_1.png" xpos h_xpos ypos h_ypos
                add "01_hp/25_mo/expanded_shirt.png" xpos h_xpos ypos h_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "01_hp/13_hermione_main/shirts/book_01.png" xpos h_xpos ypos h_ypos #Displays sperm.
                else:
                    add "01_hp/13_hermione_main/shirts/book_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_00.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_01.png" xpos h_xpos ypos h_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_01.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_02.png" xpos h_xpos ypos h_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_02.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_03.png" xpos h_xpos ypos h_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_03.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_04.png" xpos h_xpos ypos h_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_04.png", transparency) xpos h_xpos ypos h_ypos #The shirts.
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_05.png" xpos h_xpos ypos h_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_05.png", transparency) xpos h_xpos ypos h_ypos #The shirts. 
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_00.png" xpos h_xpos ypos h_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "01_hp/13_hermione_main/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if collar >= 1 and badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos h_xpos ypos h_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos h_xpos ypos h_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos h_xpos ypos h_ypos
    if custom_outfit == 1:
        add "01_hp/25_mo/maid_hat.png" xpos h_xpos ypos h_ypos
        add "01_hp/25_mo/maid_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 4:
        add "01_hp/25_mo/heart_collar.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 8:
        add "01_hp/25_mo/marvel_gloves.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_gloves.png" xpos h_xpos ypos h_ypos

    if robeon:
        add "01_hp/13_hermione_main/robe.png" xpos h_xpos ypos h_ypos #The Robe.
    if badges:
        if ba_01 and whoring <= 12:
            add "01_hp/13_hermione_main/badge.png" xpos h_xpos ypos h_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "01_hp/25_mo/cum_badge.png" xpos h_xpos ypos h_ypos

    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair_2.png" xpos h_xpos ypos h_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair_2.png" xpos h_xpos ypos h_ypos
    elif hair_color == 0:
        add "01_hp/13_hermione_main/hair/hair_00_2.png" xpos h_xpos ypos h_ypos #The hair.    
    elif hair_color == 1:
        add "01_hp/13_hermione_main/hair/hair_01_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 2:
        add "01_hp/13_hermione_main/hair/hair_02_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 3:
        add "01_hp/13_hermione_main/hair/hair_03_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 4:
        add "01_hp/13_hermione_main/hair/hair_04_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 5:
        add "01_hp/13_hermione_main/hair/hair_05_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 6:
        add "01_hp/13_hermione_main/hair/hair_06_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 7:
        add "01_hp/13_hermione_main/hair/hair_07_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 8:
        add "01_hp/13_hermione_main/hair/hair_08_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 9:
        add "01_hp/13_hermione_main/hair/hair_09_2.png" xpos h_xpos ypos h_ypos #The hair.
    elif hair_color == 10:
        add "01_hp/13_hermione_main/hair/hair_10_2.png" xpos h_xpos ypos h_ypos #The hair.    

    if glasses_worn:
        add "01_hp/13_hermione_main/glasses.png" xpos h_xpos ypos h_ypos #The glasses.
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos h_xpos ypos h_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos h_xpos ypos h_ypos #Universal sperm.
    if ne: # Desplays a fishnets in hermione_main screen.
        if ne_01:
            add "01_hp/13_hermione_main/nets.png" xpos h_xpos ypos h_ypos #The Robe.

    if tiara:
        add "01_hp/13_hermione_main/auto_09.png" xpos h_xpos ypos h_ypos # Tiara
    if tentacle_cosmetic == True:
        add "01_hp/25_mo/tentacles.png" xpos h_xpos ypos h_ypos #The Tentacles.
    zorder 8
    
    
screen h_head2: #Screen that shows Hermione's head.
    tag head
    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair.png" xpos her_head_xpos ypos her_head_ypos
    elif hair_color >= 0:
        add "01_hp/13_hermione_main/body/head/"+str(hair_style)+"_"+str(hair_color)+".png" xpos her_head_xpos ypos her_head_ypos
    if ears == True and hair_color >= 0:
        add "01_hp/25_mo/ears_"+str(hair_color)+".png" xpos her_head_xpos ypos her_head_ypos #The hair. 
    

    if transparency < 1 and badges:
        add "01_hp/13_hermione_main/customs/base.png" xpos her_head_xpos ypos her_head_ypos #Add her base 

    if transparency == 1 and badges:
        add "01_hp/13_hermione_main/customs/base_2.png" xpos her_head_xpos ypos her_head_ypos #Add her base 

    if collar >= 1 and not badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos her_head_xpos ypos her_head_ypos

    add h_body xpos her_head_xpos ypos her_head_ypos #Add her emotion

    if freckles == True:
        add "01_hp/25_mo/freckles.png" xpos her_head_xpos ypos her_head_ypos

    if not only_upper:
        add "01_hp/13_hermione_main/legs/base_01.png" xpos her_head_xpos ypos her_head_ypos #Add her legs

    if stockings == 1:
        add "01_hp/25_mo/maid_stockings.png" xpos her_head_xpos ypos her_head_ypos
    elif stockings == 2:
        add "01_hp/25_mo/cheer_stockings.png" xpos her_head_xpos ypos her_head_ypos
    elif stockings == 3:
        add "01_hp/25_mo/stockings.png" xpos her_head_xpos ypos her_head_ypos
    else:
        if ne: # Desplays a fishnets in hermione_main screen.
            if ne_01:
                add "01_hp/13_hermione_main/nets.png" xpos her_head_xpos ypos her_head_ypos # FISHNETS.
                if not legs_02 and not only_upper and not legs_03: # Long skirt is on.
                    add "01_hp/13_hermione_main/patch.png" xpos her_head_xpos ypos her_head_ypos # Patch
    
    if not only_upper:
        if whoring <= 12 or custom_bra >=0:
            if custom_bra == 1:
                add im.Alpha("01_hp/25_mo/lace_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_bra == 3:
                add im.Alpha("01_hp/25_mo/silk_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
            else:
                add im.Alpha("01_hp/13_hermione_main/legs/pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
        if custom_skirt >= 1 or custom_outfit >= 1:
            if custom_outfit == 1:
                add im.Alpha("01_hp/25_mo/maid_skirt.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_pants.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_skirt == 1:
                add im.Alpha("01_hp/25_mo/jeans.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_skirt == 2:
                add im.Alpha("01_hp/25_mo/jeans_2.png", transparency) xpos her_head_xpos ypos her_head_ypos
        else:
            if whoring <= 5:
                add im.Alpha("01_hp/13_hermione_main/legs/legs_01.png", transparency) xpos her_head_xpos ypos her_head_ypos
            if whoring >= 6 and whoring <= 11: #Mini skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_02.png", transparency) xpos her_head_xpos ypos her_head_ypos
            if whoring >= 12 and whoring <= 19: #Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_03.png", transparency) xpos her_head_xpos ypos her_head_ypos
            if whoring >= 20: #Mini Micro skirt.
                add im.Alpha("01_hp/13_hermione_main/legs/legs_04.png", transparency) xpos her_head_xpos ypos her_head_ypos
    if autograph:
        add "01_hp/13_hermione_main/auto.png" xpos her_head_xpos ypos her_head_ypos #Displays an autograph on her leg.
    if aftersperm: #Shows cum stains on Hermione's uniform.
        add "01_hp/13_hermione_main/auto_03.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.


    if custom_bra >=1 and badges and custom_outfit <= 0:
        if custom_bra == 1:
            add im.Alpha("01_hp/25_mo/lace_bra.png", transparency) xpos her_head_xpos ypos her_head_ypos
        elif custom_bra == 2:
            add im.Alpha("01_hp/13_hermione_main/shirts/bra_01.png", transparency) xpos her_head_xpos ypos her_head_ypos
        elif custom_bra == 3:
            add im.Alpha("01_hp/25_mo/silk_bra.png", transparency) xpos her_head_xpos ypos her_head_ypos
    if h_tears:
        add u_tears_pic xpos her_head_xpos ypos her_head_ypos #Universal tears layer.


    if badges and wear_shirts: #Determine what top she will wear
        if custom_shirt == True or custom_outfit >= 1 or custom_breast >= 1:
            if custom_outfit == 1 and not robeon:
                add im.Alpha("01_hp/25_mo/maid_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 2:
                add im.Alpha("01_hp/25_mo/cheer_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 3:
                add im.Alpha("01_hp/25_mo/s_cheer_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 4:
                add im.Alpha("01_hp/25_mo/heart_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 5:
                add im.Alpha("01_hp/25_mo/h_cheer_top_2.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 6:
                add im.Alpha("01_hp/25_mo/jumper.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 7:
                add im.Alpha("01_hp/25_mo/power_costume.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 8:
                add im.Alpha("01_hp/25_mo/marvel_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
                add im.Alpha("01_hp/25_mo/marvel_sash.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_outfit == 9:
                add im.Alpha("01_hp/25_mo/harley_top.png", transparency) xpos her_head_xpos ypos her_head_ypos
                add im.Alpha("01_hp/25_mo/harley_collar.png", transparency) xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 1:
                add "01_hp/25_mo/tit_exp_1.png" xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 2:
                add "01_hp/25_mo/tit_exp_2.png" xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 3:
                add "01_hp/25_mo/tit_exp_3.png" xpos her_head_xpos ypos her_head_ypos
            elif custom_breast == 4:
                add "01_hp/25_mo/tit_exp_1.png" xpos her_head_xpos ypos her_head_ypos
                add "01_hp/25_mo/expanded_shirt.png" xpos her_head_xpos ypos her_head_ypos
        else: 
            if book_hold == True and wear_shirts:
                if whoring <= 10:
                    add "01_hp/13_hermione_main/shirts/book_01.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
                else:
                    add "01_hp/13_hermione_main/shirts/book_02.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
            elif whoring <= 3:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_00.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_01.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 4 and whoring <= 7:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_01.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_02.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 8 and whoring <= 14:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_02.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_03.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 15 and whoring <= 20:
                if not fingering:
                    add im.Alpha("01_hp/13_hermione_main/shirts/shirt_03.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                else:  
                    add "01_hp/13_hermione_main/shirts/fingering_04.png" xpos her_head_xpos ypos her_head_ypos
            elif whoring >= 21:
                if day_random <= 4:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_04.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts.
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_05.png" xpos her_head_xpos ypos her_head_ypos    
                if day_random >= 5:
                    if not fingering:
                        add im.Alpha("01_hp/13_hermione_main/shirts/shirt_05.png", transparency) xpos her_head_xpos ypos her_head_ypos #The shirts. 
                    else:  
                        add "01_hp/13_hermione_main/shirts/fingering_00.png" xpos her_head_xpos ypos her_head_ypos   
                    if day_random >= 7 and lock_public_favors == False:
                        add "01_hp/13_hermione_main/auto_03.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
    if collar >= 1 and badges:
        if collar == 1:
            add "01_hp/13_hermione_main/customs/collar_1.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 2:
            add "01_hp/13_hermione_main/customs/collar_2.png" xpos her_head_xpos ypos her_head_ypos
        if collar == 3:
            add "01_hp/13_hermione_main/customs/collar_3.png" xpos her_head_xpos ypos her_head_ypos

    if custom_outfit == 7 or custom_outfit == 7.2:
        add "01_hp/25_mo/power_hair_2.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_hair_2.png" xpos her_head_xpos ypos her_head_ypos
    elif hair_color >= 0:
        add "01_hp/13_hermione_main/body/head/"+str(hair_style)+"_"+str(hair_color)+"_2.png" xpos her_head_xpos ypos her_head_ypos
    
    
    if ears == True and hair_color >= 0:
        add "01_hp/25_mo/ears_"+str(hair_color)+"_2.png" xpos her_head_xpos ypos her_head_ypos #The hair.  
   

    if glasses_worn:
        add "01_hp/13_hermione_main/glasses.png" xpos her_head_xpos ypos her_head_ypos #The glasses.

    if custom_outfit == 1:
        add "01_hp/25_mo/maid_hat.png" xpos her_head_xpos ypos her_head_ypos
        add "01_hp/25_mo/maid_gloves.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit == 4:
        add "01_hp/25_mo/heart_collar.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit == 8:
        add "01_hp/25_mo/marvel_gloves.png" xpos her_head_xpos ypos her_head_ypos
    elif custom_outfit == 9:
        add "01_hp/25_mo/harley_gloves.png" xpos her_head_xpos ypos her_head_ypos
        
    if sperm_on_tits: #Sperm on tits when Hermione pulls her shirt up.
        add "01_hp/13_hermione_main/auto_02.png" xpos her_head_xpos ypos her_head_ypos #Displays sperm.
    if uni_sperm:
        add u_sperm xpos her_head_xpos ypos her_head_ypos #Universal sperm.        
    if badges and not robeon and custom_outfit == 0:
        if ba_01 and whoring <= 12:
            add "01_hp/13_hermione_main/badge.png" xpos her_head_xpos ypos her_head_ypos #The Robe.
        elif ba_01 and whoring >= 13:
            add "01_hp/25_mo/cum_badge.png" xpos her_head_xpos ypos her_head_ypos
    if robeon:
        add "01_hp/13_hermione_main/robe.png" xpos her_head_xpos ypos her_head_ypos #The Robe.
    if tentacle_cosmetic == True:
        add "01_hp/25_mo/tentacles.png" xpos her_head_xpos ypos her_head_ypos #The Tentacles.
    
    
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in anger or emote_anger:
        add "01_hp/13_hermione_main/body/emote/00.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in exclam or emote_exclam:
        add "01_hp/13_hermione_main/body/emote/01.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in hearts or emote_hearts:
        add "01_hp/13_hermione_main/body/emote/02.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in question or emote_question:
        add "01_hp/13_hermione_main/body/emote/03.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in sweat or emote_sweat:
        add "01_hp/13_hermione_main/body/emote/04.png" xpos her_head_xpos ypos her_head_ypos #Custom
    if int(str(h_body.split("/")[-1].split("_")[-1]).replace(".png","")) in suprize or emote_suprize:
        add "01_hp/13_hermione_main/body/emote/05.png" xpos her_head_xpos ypos her_head_ypos #Custom
    
    zorder 8  
    
    
    
screen s_head: #Snape. Head.
    tag head
    add s_sprite xpos tt_xpos ypos tt_ypos # x = 330, Right bottom corner: y = 340
    zorder 8
   
screen s_head2: #Snape. Head.
    tag head
    add s_sprite xpos s_head_xpos ypos s_head_ypos # x = 330, Right bottom corner: y = 340
    zorder 8
    
    
screen custom_character_1: #Screen that shows a full sprite of Susan
    #tag susan_main
    add "01_hp/24_custom_characters/custom_character_1/hair/hair_00.png" xpos h_xpos ypos h_ypos #Add the hair.
    add custom_character_1_emo xpos h_xpos ypos h_ypos #Add the emotion.
    if not only_upper:
        add "01_hp/24_custom_characters/custom_character_1/legs/base_01.png" xpos h_xpos ypos h_ypos #Add the legs.
        add "01_hp/24_custom_characters/custom_character_1/legs/legs_02.png" xpos h_xpos ypos h_ypos #Add the legs.
    add "01_hp/24_custom_characters/custom_character_1/shirts/shirt_00.png" xpos h_xpos ypos h_ypos #Add the shirt.
    zorder 5 #(5) Otherwise candle light is shown on top.
    
    
screen custom_character_2: #Screen that shows a full sprite of Cho
    #tag cho_main
    add "01_hp/24_custom_characters/custom_character_2/hair/hair_00.png" xpos h_xpos ypos h_ypos #Add the hair.
    add custom_character_2_emo xpos h_xpos ypos h_ypos #Add the emotion.
    if not only_upper:
        add "01_hp/24_custom_characters/custom_character_2/legs/base_01.png" xpos h_xpos ypos h_ypos #Add the legs.
        add "01_hp/24_custom_characters/custom_character_2/legs/legs_03.png" xpos h_xpos ypos h_ypos #Add the legs.
    add "01_hp/24_custom_characters/custom_character_2/shirts/shirt_00.png" xpos h_xpos ypos h_ypos #Add the shirt.
    zorder 5 #(5) Otherwise candle light is shown on top.
    
    
screen custom_character_3: #Screen that shows a full sprite of Astoria
    #tag astoria_main
    add "01_hp/24_custom_characters/custom_character_3/hair/hair_00.png" xpos h_xpos ypos h_ypos #Add the hair.
    add custom_character_3_emo xpos h_xpos ypos h_ypos #Add the emotion.
    if not only_upper:
        add "01_hp/24_custom_characters/custom_character_3/legs/base_01.png" xpos h_xpos ypos h_ypos #Add the legs.
        add "01_hp/24_custom_characters/custom_character_3/legs/legs_04.png" xpos h_xpos ypos h_ypos #Add the legs.
    add "01_hp/24_custom_characters/custom_character_3/shirts/shirt_00.png" xpos h_xpos ypos h_ypos #Add the shirt.
    zorder 5 #(5) Otherwise candle light is shown on top.
    
    

### GROPING ###

screen groping_01: #Facing Genie.
    tag favor
    add "groping_01" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    
screen groping_02: #Facing Genie.
    tag favor
    add "groping_02" at Position(xpos=-200, ypos=10)
    add "groping_02_blinking" at Position(xpos=-200, ypos=10)
    
screen no_groping_01: #Facing Genie.
    tag favor
    add "01_hp/animation/grope_05.png" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    
screen no_groping_02: #Facing Genie.
    tag favor
    add "01_hp/animation/grope_b_05.png" at Position(xpos=-200, ypos=10)
    add "groping_02_blinking" at Position(xpos=-200, ypos=10)
    
### MOLESTING TITS FULLY CLOTHED ###

screen groping_03: #Facing Genie.
    tag favor
    add "groping_03_ani" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    
### MOLESTING NAKED TITS ###

screen groping_naked_tits: 
    tag favor
    add "groping_naked_tits_ani" at Position(xpos=-200, ypos=10)
    add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 1 #Otherwise chair is on top.
    
### JERKING OFF ###

screen jerking_off_01: 
    tag favor
    add "jerking_off_ani" at Position(xpos=-200, ypos=10)
    if not no_blinking: #When True - blinking animation is not displayed. 
        add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 1 #Otherwise chair is on top.

### SPERM ###
screen jerking_off_cum: 
    add "jerking_off_cum_ani" at Position(xpos=-200, ypos=10)
    #add "groping_01_blinking" at Position(xpos=-200, ypos=10)
    zorder 2 #Otherwise there is a bug with blinking.

### ADMIRING TITS ###
screen genie_and_tits_01: #Genie sitting, looking ar naked tits. Hermione stands right in front of him. (Behind the desk even).
    tag favor
    add "01_hp/05_props/admire_tits_00.png" at Position(xpos=-200, ypos=10)

### HERMIONE DANCING FULLY CLOTHED ###
screen clothed_dance: #Hermione stands still.
    tag hermione
    add "clothed_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

### HERMIONE DANCING NO VEST ###
screen no_vest_dance: #Hermione stands still.
    tag hermione
    add "no_vest_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE DANCING NO VEST ###
screen no_skirt_dance: #Hermione stands still.
    tag hermione
    add "no_skirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE DANCING NO VEST ###
screen no_shirt_dance: #Hermione stands still.
    tag hermione
    add "no_shirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE DANCING NO SKIRT NO SHIRT ###
screen no_shirt_no_skirt_dance: #Hermione stands still.
    tag hermione
    add "no_shirt_no_skirt_dance_ani" at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)
    
### HERMIONE CHIBI UNIVERSAL SCREEN ###
screen h_c_u: 
    tag hermione
    add h_c_u_pic at Position(xpos=hermione_chibi_xpos, ypos=hermione_chibi_ypos)

###  GENIE CHIBI UNIVERSAL SCREEN ###
screen g_c_u: 
    tag genie
    add g_c_u_pic at Position(xpos=genie_chibi_xpos, ypos=genie_chibi_ypos)
    
###  SNAPE CHIBI UNIVERSAL SCREEN ###
screen s_c_u: 
    tag snape
    add s_c_u_pic at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos) # (xpos=360, ypos=210) 
    zorder 3
      
 

    
    
    

###  GENIE'S CUM UNIVERSAL SCREEN ###
screen g_c_c_u: 
    add g_c_c_u_pic at Position(xpos=genie_cum_chibi_xpos, ypos=genie_cum_chibi_ypos)

###  SNAPE'S CUM UNIVERSAL SCREEN ###
screen s_c_c_u: 
    add s_c_c_u_pic at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)



### ENDING UNIVERSAL 01 ###
screen end_u_1: 
    add end_u_1_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    tag ending
    zorder 2
    
### ENDING UNIVERSAL 02 ###
screen end_u_2: 
    add end_u_2_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    tag ending
    zorder 2
    
### ENDING UNIVERSAL 03 ###
screen end_u_3: 
    add end_u_3_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    zorder 2

### ENDING UNIVERSAL 04 ###
screen end_u_4: 
    add end_u_4_pic #at Position(xpos=snape_cum_chibi_xpos, ypos=snape_cum_chibi_ypos)
    zorder 2


screen new_window: #WEATHER BG. CLEAR SKY. #тут тоже просто — делаем zorder -2, чтобы заглушка была ниже остальных скринов — ведь облако должно плыть между ней и комнатой 
    zorder -2
    add "01_hp/01_bg/03_weather.png"
    
screen cloud: # zorder -1, т.к. должно быть выше заглушки, но ниже комнаты
    zorder -1
    add "01_hp/07_weather/cloud_small.png" at cloud_move # это значит, что изображение подчиняется методу движения cloud_move, который прописан дальше

screen cloud_night_01: 
    #zorder -1
    add "01_hp/07_weather/night_cloud_02.png" at cloud_night_move_01
    
screen cloud_night_02: 
    #zorder -1
    add "01_hp/07_weather/night_cloud_01.png" at cloud_night_move_02
    
screen cloud_night_03: 
    #zorder -1
    add "01_hp/07_weather/night_cloud_03.png" at cloud_night_move_03
    
    
    
screen credits_chibi: # ONE CHIBI
    zorder 5   
    add dermo at Position(xpos=280, ypos=140)
    
    
screen credits_chibi2: # TWO CHIBIs
    zorder 5   
    add dermo at Position(xpos=150, ypos=140)
    
screen uni_cr: # UNIVERSAL CREDITS CHIBI
    zorder 5
    add dermo at Position(xpos=xder, ypos=yder)
    
    
    
    
    
### LOLA ###

screen l_head: #Screen that shows a full sprite of HERMIONE.
    tag head
    zorder 8
    add lola_body xpos lx ypos ly
    add lola_face xpos lx ypos ly
    if l_blush:
        add "01_hp/22_lola/blush.png" xpos lx ypos ly
    if l_things:
        add "01_hp/22_lola/things.png" xpos lx ypos ly
    if l_question:
        add "01_hp/22_lola/question.png" xpos lx ypos ly
    if l_drop:
        add "01_hp/22_lola/drop.png" xpos lx ypos ly
    if l_hearts:
        add "01_hp/22_lola/hearts.png" xpos lx ypos ly
    if l_exclamation:
        add "01_hp/22_lola/exclamation.png" xpos lx ypos ly
    if l_tears:
        add "01_hp/22_lola/tears.png" xpos lx ypos ly
    
###SILVER STUFF
screen luna:
    ### BASE IMAGE
    add luna_base xpos luna_xpos ypos luna_ypos #Add the base body
    add luna_hair xpos luna_xpos ypos luna_ypos #Add the hair shadow
    ### EMOTIONS
    add luna_mouth xpos luna_xpos ypos luna_ypos #Add the mouth
    add "01_hp/26_luna/eye/eye_white.png"  xpos luna_xpos ypos luna_ypos
    add luna_pupil xpos luna_xpos ypos luna_ypos #Add the pupil
    add luna_eye xpos luna_xpos ypos luna_ypos #Add the eye outline
    add luna_eyebrow xpos luna_xpos ypos luna_ypos #Add the eyebrow
    ### CLOTHES 
    add luna_bra xpos luna_xpos ypos luna_ypos # Add the bra
    add luna_panties xpos luna_xpos ypos luna_ypos # Add the panties
    add luna_skirt xpos luna_xpos ypos luna_ypos # Add the skirt
    add luna_top xpos luna_xpos ypos luna_ypos # Add the top
    #add luna_acc xpos luna_xpos ypos luna_ypos # Add the accessory
    ### ZORDER
    zorder luna_zorder

init python: ###Method Definition for new characters
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
        global luna_eye 
        global luna_pupil
        global luna_eyebrow
        global luna_mouth
        global luna_eyebrow
        ###HIDE OLD SCREEN
        renpy.hide_screen("luna")
        #renpy.with_statement(Dissolve(0.5))
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
    
###THANKS TO CLEANZO FOR WRITING THIS CODE
    def changeHermioneMainScreen(   image_name,
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
                   
    def cg(image):
        global cg_image
        ###HIDE OLD SCREEN
        renpy.hide_screen("cg")
        #renpy.with_statement(Dissolve(0.5))
        if image is not None:
            cg = image
        ###DISPLAY THE UPDATED SCREEEN
        renpy.show_screen("cg")
        renpy.with_statement(Dissolve(0.3))