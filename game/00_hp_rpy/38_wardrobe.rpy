screen wardrobe:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (37, 30, 67, 82) clicked Show("wardrobe_gifts") 
        #("wardrobe_gifts")
        #("wardrobe_hair") 

        text "Hair" xpos 45 ypos 100 size 15
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Gifts" xpos 400 ypos 100 size 15
        text "Potions" xpos 475 ypos 100 size 15


screen wardrobe_hair:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"

        hotspot (37, 30, 67, 82) clicked Show("wardrobe_hair")
        
        $ tmp_x = 21
        $ tmp_y = 48
        for i in  range(1,6):
            $ tmp_x = 21
            $ tmp_y += 91
            for j in range(1,7):
                hotspot (tmp_x, tmp_y, 83, 85) clicked [SetVariable("column_index_selected",j),SetVariable("row_index_selected",i),Jump("change_hair")]
                $ tmp_x += 90
        
        # for i in range(0,6):
            # hotspot (20+(90*i), 140, 87, 84) clicked [SetVariable("hair_color_menu",i+1),SetVariable("hair_style_menu","A"),Jump("change_hair")]
            # hotspot (20+(90*i), 232, 87, 84) clicked [SetVariable("hair_color_menu",i+1),SetVariable("hair_style_menu","B"),Jump("change_hair")]
        
        for i in range(0,6):
            add "01_hp/13_characters/hermione/body/head/A_"+str(i+1)+".png" xpos -45+(90*i) ypos 105 zoom 0.35
            add "01_hp/13_characters/hermione/body/head/B_"+str(i+1)+".png" xpos -45+(90*i) ypos 205 zoom 0.35

        text "Hair" xpos 45 ypos 100 size 15 bold 1
        text "Uniform" xpos 115 ypos 100 size 15
        text "Costumes" xpos 200 ypos 100 size 15
        text "Accs." xpos 310 ypos 100 size 15
        text "Gifts" xpos 400 ypos 100 size 15
        text "Potions" xpos 475 ypos 100 size 15
        
label change_hair_test:
    $ tmp = "Perform action ROW:"+str(row_index_selected)+"  COL:"+str(column_index_selected)
    "[tmp]"
    call screen wardrobe
    
label change_hair():
    call her_main("Sure, let me just go change it.","body_01")
    $ h_hair_style = hair_style_menu
    $ h_hair_color = hair_color_menu 
    hide screen wardrobe_hair
    call screen wardrobe_hair
    
    
screen wardrobe_gifts:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1
    
    imagemap:
        cache False
        ground "01_hp/25_mo/wardrobe_ground.png"
        hover "01_hp/25_mo/wardrobe_hover.png"
        
    for i in range(1,7):
        add "01_hp/18_store/gifts/"+str(i)+".png" xpos -150+(90*i) ypos 90 zoom 0.30
    for i in range(7,13):
        add "01_hp/18_store/gifts/"+str(i)+".png" xpos -150+(90*(i-6)) ypos 180 zoom 0.30
    for i in range(13,18):
        add "01_hp/18_store/gifts/"+str(i)+".png" xpos -150+(90*(i-12)) ypos 270 zoom 0.30
        
    text "Hair" xpos 45 ypos 100 size 15
    text "Uniform" xpos 115 ypos 100 size 15
    text "Costumes" xpos 200 ypos 100 size 15
    text "Accs." xpos 310 ypos 100 size 15
    text "Gifts" xpos 400 ypos 100 size 15 bold 1
    text "Potions" xpos 475 ypos 100 size 15
    
    
label day_request_wardrobe:
    menu:
        "-Hair-":
            label day_request_hair:
            menu:
                "-Wear your hair up-" if not h_hair_style == "B":
                    call her_main("Sure, let me just go change it.","body_01")
                    call set_h_hair_style("B")
                    jump day_request_hair
                    
                "-Wear your hair down-" if not h_hair_style == "A":
                    call her_main("Sure, let me just go change it.","body_01")
                    call set_h_hair_style("A")
                    jump day_request_hair
                    
                "-Dye your hair-":
                    label day_request_hair_dye:
                    menu:
                        "-Dye Brown-" if not h_hair_color == 1:
                            call her_main("Brown seems so boring now.","body_01")
                            call set_h_hair_color(1)
                            jump day_request_hair_dye
                            
                        "-Dye Blonde-" if not h_hair_color == 2:
                            call her_main("Why do you want me to change my hair?","body_01")
                            m "I don't know, I suppose I just have a thing for blondes"
                            her "well I've always heard blondes have more fun!"
                            call set_h_hair_color(2)
                            jump day_request_hair_dye
                            
                        "-Dye Red-" if not h_hair_color == 3:
                            call her_main("this'll be fun, Maybe I'll look like Batwoman!","body_01")
                            m "You read comics?"
                            her "no, i just play certain games"
                            m "What?"
                            call set_h_hair_color(3)
                            jump day_request_hair_dye
                            
                        "-Dye Black-" if not h_hair_color == 4:
                            call her_main("I have been feeling a bit depressed recently.","body_01")
                            her "I wonder if it's because of all the favors I've been doing"
                            m "Don't worry about it"
                            call set_h_hair_color(4)
                            jump day_request_hair_dye
                            
                        "-Dye Blue-" if not h_hair_color == 5:
                            call her_main("Blue?","body_01")
                            m "Why not?"
                            her "Just seems a bit attention seeking..."
                            call set_h_hair_color(5)
                            jump day_request_hair_dye
                            
                        "-Dye Orange-" if not h_hair_color == 6:
                            call her_main("Orange?","body_01")
                            m "That's what I said."
                            her "Alright, well just let me change it."
                            call set_h_hair_color(6)
                            jump day_request_hair_dye
                            
                        "-Never mind-":
                            jump day_request_hair
                    
                "-Never mind-":
                    jump day_request_wardrobe
        
        "-Clothing-":
            label day_request_clothing:
            menu:
                "-Don't wear a top-" if hermione_wear_top:
                    call h_top_off
                    jump day_request_clothing
                    
                "-Put top back on-" if not hermione_wear_top:
                    call h_top_on
                    jump day_request_clothing
                    
                "-Don't wear a skirt-" if hermione_wear_skirt:
                    call h_skirt_off
                    jump day_request_clothing
                    
                "-Put skirt back on-" if not hermione_wear_skirt:
                    call h_skirt_on
                    jump day_request_clothing
                    
                "-Stop wearing panties-" if h_request_wear_panties and whoring >= 6:
                    call h_panties_off
                    jump day_request_clothing
                    
                "-Wear panties-" if not h_request_wear_panties and whoring >= 6:
                    call h_panties_on
                    jump day_request_clothing
                    
                "-Stockings-":
                    label day_request_clothing_stockings:
                    menu:
                        "-Put the fishnets on-" if "fishnet_stockings" in cs_existing_stock and h_stocking != "fishnet_a":
                            call set_h_stockings("fishnet_a")
                            jump day_request_clothing_stockings
                            
                        "-Take the fishnets off-" if "fishnet_stockings" in cs_existing_stock and h_stocking == "fishnet_a":
                            call set_h_stockings
                            jump day_request_clothing_stockings
                            
                        "-Put the Gryffindor Stockings on-" if "gryffindor_stockings" in cs_existing_stock and h_stocking != "gryff":
                            if request_gryyf_stockings == False and whoring <= 6:
                                jump equip_gryyf_stockings
                            else:
                                call set_h_stockings("gryff")
                                jump day_request_clothing_stockings
                            
                        "-Take the Gryffindor Stockings off-" if "gryffindor_stockings" in cs_existing_stock and h_stocking == "gryff":
                            call set_h_stockings
                            jump day_request_clothing_stockings
                            
                        "-Never mind-":
                            jump day_request_clothing
                    
                "-Underwear-":
                    label day_request_clothing_underwear:
                    menu:
                        "-Put the Lace Bra and Panties on-" if "lace_set" in cs_existing_stock and h_bra != "lace_bra":
                            call set_h_underwear("lace_bra","lace_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Lace Bra and Panties off-" if "lace_set" in cs_existing_stock and h_bra == "lace_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                            
                        "-Put the Cup-less Lace Bra on-" if "cup_set" in cs_existing_stock and h_bra != "cup_bra":
                            call set_h_underwear("cup_bra","cup_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Cup-less Lace Bra off-" if "cup_set" in cs_existing_stock and h_bra == "cup_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                            
                        "-Put the Silk Bra and Panties on-" if "silk_set" in cs_existing_stock and h_bra != "silk_bra":
                            call set_h_underwear("silk_bra","silk_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Silk Bra and Panties off-" if "silk_set" in cs_existing_stock and h_bra == "silk_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                            
                        "-Put the Latex and Panties on-" if "latex_set" in cs_existing_stock and h_bra != "latex_bra":
                            call set_h_underwear("latex_bra","latex_panties")
                            jump day_request_clothing_underwear
                            
                        "-Take the Latex and Panties off-" if "latex_set" in cs_existing_stock and h_bra == "latex_bra":
                            call set_h_underwear
                            jump day_request_clothing_underwear
                        
                        "-Never mind-":
                            jump day_request_clothing
                    
                "-Put the jeans on-" if "jeans_long" in cs_existing_stock and h_skirt != "jeans_long":
                    if request_jeans == False:
                        jump equip_jeans
                    else:
                        call set_h_skirt("jeans_long")
                        jump day_request_clothing
                    
                "-Take the jeans off-" if h_skirt == "jeans_long":
                     call set_h_skirt
                     jump day_request_clothing
                    
                "-Put the short jeans on-" if "jeans_short" in cs_existing_stock and h_skirt != "jeans_short":
                     call set_h_skirt("jeans_short")
                     jump day_request_clothing
                    
                "-Take the short jeans off-"if h_skirt == "jeans_short":
                     call set_h_skirt
                     jump day_request_clothing
                    
                "-Never mind-":
                    jump day_request_wardrobe
        
        "-Accessories-":
            label day_request_accessories:
            menu:
                "-Put \"S.P.E.W.\" badge on-" if "SPEW_badge" in cs_existing_stock and h_badge != "SPEW_badge":
                    call h_badge_on("SPEW_badge")
                    jump day_request_accessories
                    
                "-Take \"S.P.E.W.\" badge off-" if "SPEW_badge" in cs_existing_stock and h_badge == "SPEW_badge":
                    call h_badge_off
                    jump day_request_accessories
                    
                "-Put I <3 C.U.M.\" badge on-" if "CUM_badge" in cs_existing_stock and h_badge != "CUM_badge":
                    call h_badge_on("CUM_badge")
                    jump day_request_accessories
                    
                "-Take I <3 C.U.M.\" badge off-" if "CUM_badge" in cs_existing_stock and h_badge == "CUM_badge":
                    call h_badge_off
                    jump day_request_accessories
                    
                "-Never mind-":
                    jump day_request_wardrobe
        
        "-Collars-" if False:
            label day_request_collars:
            menu:
                "-Take off the collar-" if collar >= 1:
                    $ collar = 0
                    jump day_request_collars
                "-Put on the slave collar-":
                    $ collar = 1
                    jump day_request_collars
                "-Put on the slut collar-":
                    $ collar = 2
                    jump day_request_collars
                "-Put on the whore collar-":
                    $ collar = 3
                    jump day_request_collars
                "-Never mind-":
                    jump day_request_wardrobe
                    
        "-Overlays-":
            label day_request_overlays:
            menu:
            
                "{color=#858585}-Thigh Grool Locked-{/color}" if dribble_equippable == False:
                    "You should try equipping the Gryffindor Stockings between 3 and 6 whoring"
                    jump day_request_overlays
                
                "{color=#858585}-Damp Panties Locked-{/color}" if wetpanties_equippable == False:
                    "You should try equipping the Gryffindor Stockings between 3 and 6 whoring"
                    jump day_request_overlays
                
                "-Thigh Grool On-" if dribble_equippable == True and hermione_dribble == False:
                    $ hermione_dribble = True
                    call update_her_uniform
                    jump day_request_overlays
                "-Thigh Grool Off-" if dribble_equippable == True and hermione_dribble == True:
                    $ hermione_dribble = False
                    call update_her_uniform
                    jump day_request_overlays
                
                "-Damp Panties On-" if wetpanties_equippable == True and hermione_wetpanties == False:
                    $ hermione_wetpanties = True
                    call update_her_uniform
                    jump day_request_overlays
                    
                "-Damp Panties Off-" if wetpanties_equippable == True and hermione_wetpanties == True:
                    $ hermione_wetpanties = False
                    call update_her_uniform
                    jump day_request_overlays  
                    
                "-Never mind":
                    jump day_time_requests
                    
