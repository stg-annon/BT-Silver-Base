

screen wardrobe:
    
    tag wardrobe_menu
    zorder hermione_main_zorder-1

    imagemap:
        cache False

        ## Ground & Hovers ##
        if wardrobe_page == 0: #default
            ground "interface/wardrobe_ground/ground_her.png"
            hover "interface/wardrobe_hover/hover_her.png"
        elif wardrobe_page == 1: #hair
            ground "interface/wardrobe_ground/ground_her_hair.png"
            hover "interface/wardrobe_hover/hover_her_hair.png"
        elif wardrobe_page == 2: #tops
            ground "interface/wardrobe_ground/ground_her_tops.png"
            hover "interface/wardrobe_hover/hover_her_tops.png"
        elif wardrobe_page == 3: #bottoms
            ground "interface/wardrobe_ground/ground_her_bottoms.png"
            hover "interface/wardrobe_hover/hover_her_bottoms.png"
        elif wardrobe_page == 4: #other clothings
            ground "interface/wardrobe_ground/ground_her_stockings.png"
            hover "interface/wardrobe_hover/hover_her_stockings.png"
        elif wardrobe_page == 5: #accessories
            ground "interface/wardrobe_ground/ground_her_accessories.png"
            hover "interface/wardrobe_hover/hover_her_accessories.png"
        elif wardrobe_page == 6: #underwear
            ground "interface/wardrobe_ground/ground_her_underwear.png"
            hover "interface/wardrobe_hover/hover_her_underwear.png"
        elif wardrobe_page == 7: #outfits
            ground "interface/wardrobe_ground/ground_her_outfits.png"
            hover "interface/wardrobe_hover/hover_her_outfits.png"
        elif wardrobe_page == 8: #gifts
            ground "interface/wardrobe_ground/ground_her_gifts.png"
            hover "interface/wardrobe_hover/hover_her_gifts.png"
            


        ## Always Active ##
        hotspot (745+280,10,45,45) clicked [SetVariable("wardrobe_page",0),Jump("close_wardrobe")]    #Close Wardrobe and set to default.
        text ""+hermione_name xalign 0.5 xpos 820 ypos 72 size 18
        text "Toggle" xpos 668 ypos 129 size 12 
        text "Wardrobe" xpos 668 ypos 154+360 size 12

        hotspot (993,10,32,23) clicked Jump("hide_wardrobe")

        
        ## Page Specific Hotspots ##
        if wardrobe_page == 0: #default #Not used yet.
            pass
        else:
            pass
        #    hotspot for Arrows that add +/- to wardrobe_page == 0 (top, left) 
        #    hotspot for Arrows that add +/- to item pages (left, middle)

        #Hair
        if wardrobe_page == 1:
            hotspot (555, 120, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Hair-style & Colour" xpos 118 ypos 100 size 18
        else:
            hotspot (595, 120, 50, 98) clicked [SetVariable("wardrobe_page",1),Show("wardrobe")] #default

        #Tops
        if wardrobe_page == 2:
            hotspot (555, 230, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Top Clothings" xpos 118 ypos 100 size 18
        else:
            hotspot (595, 230, 50, 98) clicked [SetVariable("wardrobe_page",2),Show("wardrobe")] #default

        #Bottoms
        if wardrobe_page == 3:
            hotspot (555, 340, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Bottom Clothings" xpos 118 ypos 100 size 18
        else:
            hotspot (595, 340, 50, 98) clicked [SetVariable("wardrobe_page",3),Show("wardrobe")] #default

        #Other Clothings
        if wardrobe_page == 4:
            hotspot (555, 450, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Other Clothings" xpos 118 ypos 100 size 18
        else:
            hotspot (595, 450, 50, 98) clicked [SetVariable("wardrobe_page",4),Show("wardrobe")] #default

        #Accessories
        if wardrobe_page == 5:
            hotspot (985, 120, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Accessories" xpos 118 ypos 100 size 18
        else:
            hotspot (985, 120, 60, 98) clicked [SetVariable("wardrobe_page",5),Show("wardrobe")] #default

        #Underwear
        if wardrobe_page == 6:
            hotspot (985, 230, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Underwear" xpos 118 ypos 100 size 18
        else:
            hotspot (985, 230, 60, 98) clicked [SetVariable("wardrobe_page",6),Show("wardrobe")] #default

        #Outfits
        if wardrobe_page == 7:
            hotspot (985, 340, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Costumes & Outfits" xpos 118 ypos 100 size 18
        else:
            hotspot (985, 340, 60, 98) clicked [SetVariable("wardrobe_page",7),Show("wardrobe")] #default

        #Gifts
        if wardrobe_page == 8:
            hotspot (985, 450, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Gifts & Quest Items" xpos 118 ypos 100 size 18
        else:
            hotspot (985, 450, 60, 98) clicked [SetVariable("wardrobe_page",8),Show("wardrobe")] #default


### ON/OFF Toggles ###

        ## Top Toggle ##
        if whoring >= 6:
            hotspot (667,150,18,18) clicked Jump("her_top_toggle")
            if hermione_wear_top:
                add "interface/check_02.png" xpos 667 ypos 145 #ypos-5 of hotspot ypos #2nd row Ypos+25
            else:
                add "interface/check_01.png" xpos 667 ypos 145
            text "Top" xpos 688 ypos 154 size 10
        else:
            if hermione_wear_top:
                add "interface/check_02_grey.png" xpos 667 ypos 145 #grayed out
            else:
                add "interface/check_01_grey.png" xpos 667 ypos 145 #grayed out
            text "{color=#858585}Top{/color}" xpos 688 ypos 154 size 10            #grayed out

        ## Bra Toggle ##
        if whoring >= 9:
            hotspot (667+5,150+25,18,18) clicked Jump("her_bra_toggle")
            if hermione_wear_bra:
                add "interface/check_02.png" xpos 667+5 ypos 145+25 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667+5 ypos 145+25
            text "Bra" xpos 688+5 ypos 154+25 size 10
        else:
            if hermione_wear_bra:
                add "interface/check_02_grey.png" xpos 667+5 ypos 145+25 #grayed out
            else:
                add "interface/check_01_grey.png" xpos 667+5 ypos 145+25 #grayed out
            text "{color=#858585}Bra{/color}" xpos 688+5 ypos 154+25 size 10          #grayed out

        ## Bottom Toggle ##
        if whoring >= 6:
            hotspot (667,150+50,18,18) clicked Jump("her_bottom_toggle")
            if hermione_wear_skirt: #rename to "hermione_wear_bottom"
                add "interface/check_02.png" xpos 667 ypos 145+50 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+50
            text "Bottom" xpos 688 ypos 154+50 size 10
        else:
            if hermione_wear_skirt:
                add "interface/check_02_grey.png" xpos 667 ypos 145+50 #grayed out
            else:
                add "interface/check_01_grey.png" xpos 667 ypos 145+50 #grayed out
            text "{color=#858585}Bottom{/color}" xpos 688 ypos 154+50 size 10          #grayed out

        ## Panties Toggle ##
        if whoring >= 9:
            hotspot (667+5,150+75,18,18) clicked Jump("her_panties_toggle")
            if hermione_wear_panties:
                add "interface/check_02.png" xpos 667+5 ypos 145+75 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667+5 ypos 145+75
            text "Panties" xpos 688+5 ypos 154+75 size 10
        else:
            if hermione_wear_panties:
                add "interface/check_02_grey.png" xpos 667+5 ypos 145+75 #grayed out
            else:
                add "interface/check_01_grey.png" xpos 667+5 ypos 145+75 #grayed out
            text "{color=#858585}Panties{/color}" xpos 688+5 ypos 154+75 size 10          #grayed out

        ## Neckwear ##
        if whoring >= 0:
            hotspot (667,150+110,18,18) clicked Jump("her_neckwear_toggle")
            if hermione_wear_neckwear:
                add "interface/check_02.png" xpos 667 ypos 145+110 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+110
            text "Neck" xpos 688 ypos 154+110 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+110   #grayed out
            text "{color=#858585}Neck{/color}" xpos 688 ypos 154+110 size 10          #grayed out

        ## Belt ##
        if whoring >= 0:
            hotspot (667,150+135,18,18) clicked Jump("her_belt_toggle")
            if hermione_wear_belt:
                add "interface/check_02.png" xpos 667 ypos 145+135 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+135
            text "Belt" xpos 688 ypos 154+135 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+135   #grayed out
            text "{color=#858585}Belt{/color}" xpos 688 ypos 154+135 size 10          #grayed out

        ## Gloves ##
        if whoring >= 0:
            hotspot (667,150+160,18,18) clicked Jump("her_gloves_toggle")
            if hermione_wear_gloves:
                add "interface/check_02.png" xpos 667 ypos 145+160 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+160
            text "Gloves" xpos 688 ypos 154+160 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+160   #grayed out
            text "{color=#858585}Gloves{/color}" xpos 688 ypos 154+160 size 10          #grayed out

        ## Stockings Toggle ##
        if whoring >= 0:
            hotspot (667,150+185,18,18) clicked Jump("her_stockings_toggle")
            if hermione_wear_stockings:
                add "interface/check_02.png" xpos 667 ypos 145+185 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+185
            text "Stockings" xpos 688 ypos 154+185 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+185   #grayed out
            text "{color=#858585}Stockings{/color}" xpos 688 ypos 154+185 size 10          #grayed out

        ## Robe Toggle ##
        if whoring >= 0:
            hotspot (667,150+210,18,18) clicked Jump("her_robe_toggle")
            if hermione_wear_robe:
                add "interface/check_02.png" xpos 667 ypos 145+210 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+210
            text "Robe" xpos 688 ypos 154+210 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+210   #grayed out
            text "{color=#858585}Robe{/color}" xpos 688 ypos 154+210 size 10          #grayed out

        ## Outfit Toggle ##
        if whoring >= 0:
            hotspot (667,150+245,18,18) clicked [SetVariable("wardrobe_costume_selection",None),Jump("wardrobe_wear_costume")] #"wardrobe_costume_selection",None #wardrobe_wear_costume
            if not wardrobe_costume_selection:
                add "interface/check_01.png" xpos 667 ypos 145+245 #ypos-5 of hotspot ypos
            else:
                add "interface/check_02.png" xpos 667 ypos 145+245
            text "Outfit" xpos 688 ypos 154+245 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+245   #grayed out
            text "{color=#858585}Outfit{/color}" xpos 688 ypos 154+245 size 10          #grayed out


        ### Wardrobe Toggle ###

        ## Wardrobe Event Toggle ## NOT IN USE
        #hotspot (667,150+360,18,18) clicked Jump("wardrobe_events_toggle")
        #if wardrobe_events_active:
        #    add "interface/check_02.png" xpos 667 ypos 145+360 #ypos-5 of hotspot ypos
        #else:
        #    add "interface/check_01.png" xpos 667 ypos 145+360
        #text "Dialogue" xpos 688 ypos 154+360 size 10

        ## Wardrobe ChitChat Toggle
        hotspot (667,150+385,18,18) clicked Jump("wardrobe_chitchat_toggle")
        if wardrobe_chitchat_active:
            add "interface/check_02.png" xpos 667 ypos 145+385 #ypos-5 of hotspot ypos
        else:
            add "interface/check_01.png" xpos 667 ypos 145+385
        text "Chit-Chat" xpos 688 ypos 154+385 size 10

### Wardrobe Hair ###  

        if wardrobe_page == 1:
            ## Change Hairstlye ##
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),Jump("change_her_hair")]
            hotspot (165, 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),Jump("change_her_hair")]
            add "01_hp/13_characters/hermione/body/head/A_1.png" xpos 10 ypos 105 zoom 0.35
            add "01_hp/13_characters/hermione/body/head/B_1.png" xpos 10+90 ypos 105 zoom 0.35

            for i in range(0,len(wr_her_haircolor)):
                $ row = i // 5
                $ col = i % 5

                hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_hair_color",(wr_her_haircolor[i])),Jump("change_her_hair")]
                add "interface/wardrobe_icons/dyes/dye_"+wr_her_haircolor[i]+".png" xpos 75+(90*col) ypos (138+92+(92*row)) zoom 0.70
        else:
            pass


### Wardrope Tops ###

        if wardrobe_page == 2:

            #Uniform
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
            add "01_hp/13_characters/hermione/clothes/uniform/top/1.png" xpos 15 ypos 60 zoom 0.35
            text "Uniform" xpos 76 ypos 140+75 size 10
            #Fancy
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",1),Show("wardrobe")]
            add "interface/wardrobe_icons/tops/tops_fancy.png" xpos 15+90 ypos 60 zoom 0.35
            text "Fancy" xpos 76+90 ypos 140+75 size 10
            #Wicked
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",2),Show("wardrobe")]
            add "interface/wardrobe_icons/tops/tops_wicked.png" xpos 15+180 ypos 60 zoom 0.35
            text "Wicked" xpos 76+180 ypos 140+75 size 10
            #Muggle
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",3),Show("wardrobe")]
            add "interface/wardrobe_icons/tops/tops_muggle.png" xpos 15+270 ypos 60 zoom 0.35
            text "Muggle" xpos 76+270 ypos 140+75 size 10
            #Misc
            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",4),Show("wardrobe")]
            add "interface/wardrobe_icons/tops/tops_misc.png" xpos 15+360 ypos 60 zoom 0.35
            text "Misc." xpos 76+360 ypos 140+75 size 10

            #Uniforms
            if wardrobe_tops_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "01_hp/13_characters/hermione/clothes/uniform/top/1.png" xpos 15 ypos 60 zoom 0.35
                text "Uniform" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_her_tops_uniform)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_choice",(i+1)), Jump("equip_top")]
                    add "01_hp/13_characters/hermione/clothes/tops/"+wr_her_tops_uniform[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Fancy
            if wardrobe_tops_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/tops/tops_fancy.png" xpos 15+90 ypos 60 zoom 0.35
                text "Fancy" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_her_tops_fancy)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_choice",(i+1)), Jump("equip_top")]
                    add "01_hp/13_characters/hermione/clothes/tops/"+wr_her_tops_fancy[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Wicked
            if wardrobe_tops_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/tops/tops_wicked.png" xpos 15+180 ypos 60 zoom 0.35
                text "Wicked" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_her_tops_wicked)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_choice",(i+1)), Jump("equip_top")]
                    add "01_hp/13_characters/hermione/clothes/tops/"+wr_her_tops_wicked[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Muggle
            if wardrobe_tops_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/tops/tops_muggle.png" xpos 15+270 ypos 60 zoom 0.35
                text "Muggle" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_her_tops_normal)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_choice",(i+1)), Jump("equip_top")]
                    add "01_hp/13_characters/hermione/clothes/tops/"+wr_her_tops_normal[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Misc
            if wardrobe_tops_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_tops_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/tops/tops_misc.png" xpos 15+360 ypos 60 zoom 0.35
                text "Misc." xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_her_tops_misc)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("top_choice",(i+1)), Jump("equip_top")]
                    add "01_hp/13_characters/hermione/clothes/tops/"+wr_her_tops_misc[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

        else:
            pass


### Wardrobe Bottoms ###

        if wardrobe_page == 3:

            #Uniform
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
            add "interface/wardrobe_icons/bottoms/bottoms_uniform.png" xpos 15 ypos 17 zoom 0.35
            text "Uniform" xpos 76 ypos 140+75 size 10
            #Uniform Low
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",1),Show("wardrobe")]
            add "interface/wardrobe_icons/bottoms/bottoms_uniform_low.png" xpos 15+90 ypos 17 zoom 0.35
            text "Uniform Low" xpos 76+90 ypos 140+75 size 10
            #Skirts
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",2),Show("wardrobe")]
            add "interface/wardrobe_icons/bottoms/bottoms_skirts.png" xpos 15+180 ypos 17 zoom 0.35
            text "Skirts" xpos 76+180 ypos 140+75 size 10
            #Pants
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",3),Show("wardrobe")]
            add "interface/wardrobe_icons/bottoms/bottoms_pants.png" xpos 15+270 ypos 17 zoom 0.35
            text "Pants" xpos 76+270 ypos 140+75 size 10
            #Misc
            #hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",4),Show("wardrobe")]
            #add "interface/wardrobe_icons/bottoms/bottoms_misc.png" xpos 15+360 ypos 17 zoom 0.35
            #text "Misc." xpos 76+360 ypos 140+75 size 10

            #Uniforms
            if wardrobe_bottoms_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/bottoms/bottoms_uniform.png" xpos 15 ypos 17 zoom 0.35
                text "Uniform" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_her_bottoms_uniform)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("skirt_choice",(i+1)), Jump("equip_skirt")]
                    add "01_hp/13_characters/hermione/clothes/bottoms/"+wr_her_bottoms_uniform[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35

            #Uniform Low
            if wardrobe_bottoms_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/bottoms/bottoms_uniform_low.png" xpos 15+90 ypos 17 zoom 0.35
                text "Uniform Low" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_her_bottoms_uniform_low)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("skirt_choice",(i+1)), Jump("equip_skirt")]
                    add "01_hp/13_characters/hermione/clothes/bottoms/"+wr_her_bottoms_uniform_low[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35

            #Skirts
            if wardrobe_bottoms_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/bottoms/bottoms_skirts.png" xpos 15+180 ypos 17 zoom 0.35
                text "Skirts" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_her_bottoms_skirts)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("skirt_choice",(i+1)), Jump("equip_skirt")]
                    add "01_hp/13_characters/hermione/clothes/bottoms/"+wr_her_bottoms_skirts[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35

            #Pants
            if wardrobe_bottoms_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/bottoms/bottoms_pants.png" xpos 15+270 ypos 17 zoom 0.35
                text "Pants" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_her_bottoms_pants)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("skirt_choice",(i+1)), Jump("equip_skirt")]
                    add "01_hp/13_characters/hermione/clothes/bottoms/"+wr_her_bottoms_pants[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35

            #Misc
            #if wardrobe_bottoms_category == 4:
            #    hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_bottoms_category",0),Show("wardrobe")]
            #    add "interface/wardrobe_icons/bottoms/bottoms_misc.png" xpos 15+360 ypos 17 zoom 0.35
            #    text "Misc." xpos 76+360 ypos 140+75 size 10
            #    for i in range(0,len(wr_her_bottoms_misc)):
            #        $ row = i // 5
            #        $ col = i % 5

            #        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("skirt_choice",(i+1)), Jump("equip_skirt")]
            #        add "01_hp/13_characters/hermione/clothes/bottoms/"+wr_her_bottoms_misc[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35


        else:
            pass


## Wardrobe Other Clothings ##

        if wardrobe_page == 4:

            #Neckwear
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
            add "interface/wardrobe_icons/stockings/neckwear.png" xpos 15 ypos 60 zoom 0.35
            text "Neckwear" xpos 76 ypos 140+75 size 10
            #Belts
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",1),Show("wardrobe")]
            add "interface/wardrobe_icons/stockings/belts.png" xpos 15+90 ypos 40 zoom 0.35
            text "Belts" xpos 76+90 ypos 140+75 size 10
            #Gloves
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",2),Show("wardrobe")]
            add "interface/wardrobe_icons/stockings/gloves.png" xpos 15+180 ypos 30 zoom 0.35
            text "Gloves" xpos 76+180 ypos 140+75 size 10
            #Stockings
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",3),Show("wardrobe")]
            add "interface/wardrobe_icons/stockings/stockings.png" xpos -85+270 ypos -195 zoom 0.7
            text "Stockings" xpos 76+270 ypos 140+75 size 10
            #Robes
            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",4),Show("wardrobe")]
            add "interface/wardrobe_icons/stockings/robes.png" xpos 45+360 ypos 75 zoom 0.25
            text "Robes" xpos 76+360 ypos 140+75 size 10

            #Neckwear
            if wardrobe_stockings_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/stockings/neckwear.png" xpos 15 ypos 60 zoom 0.35
                text "Neckwear" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_her_neckwears)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wr_her_neckwear_choice",wr_her_neckwears[i]),Jump("equip_neckwear")]
                    add "01_hp/13_characters/hermione/clothes/neckwear/"+str(wr_her_neckwears[i])+".png" xpos 15+(90*col) ypos 60+92+(92*row) zoom 0.35

            #Belts
            if wardrobe_stockings_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/stockings/belts.png" xpos 15+90 ypos 40 zoom 0.35
                text "Belts" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_her_belts)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wr_her_belt_choice",wr_her_belts[i]),Jump("equip_belt")]
                    add "01_hp/13_characters/hermione/clothes/belts/"+str(wr_her_belts[i])+".png" xpos 15+(90*col) ypos 40+92+(92*row) zoom 0.35

            #Gloves
            if wardrobe_stockings_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/stockings/gloves.png" xpos 15+180 ypos 30 zoom 0.35
                text "Gloves" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_her_gloves)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wr_her_gloves_choice",wr_her_gloves[i]),Jump("equip_gloves")]
                    add "01_hp/13_characters/hermione/clothes/gloves/"+str(wr_her_gloves[i])+".png" xpos 15+(90*col) ypos 30+92+(92*row) zoom 0.35

            #Stockings
            if wardrobe_stockings_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/stockings/stockings.png" xpos -85+270 ypos -195 zoom 0.7
                text "Stockings" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_her_stockings)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wr_her_stockings_choice",wr_her_stockings[i]),Jump("equip_stockings")]
                    add "01_hp/13_characters/hermione/clothes/stockings/"+str(wr_her_stockings[i])+".png" xpos -25+(90*col) ypos -75+92+(92*row) zoom 0.5

            #Robes
            if wardrobe_stockings_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_stockings_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/stockings/robes.png" xpos 45+360 ypos 75 zoom 0.25
                text "Robes" xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_her_robes)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wr_her_robe",wr_her_robes[i]),Jump("wardrobe_wear_robe")]
                    add "01_hp/13_characters/hermione/clothes/robe/"+str(wr_her_robes[i])+".png" xpos 45+(90*col) ypos 77+92+(92*row) zoom 0.25
        else:
            pass


## Wardrobe Accessories ##

        if wardrobe_page == 5:

            #Head
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
            add "interface/wardrobe_icons/accessories/cat_ears.png" xpos -10 ypos 40 zoom 0.5
            text "Head" xpos 76 ypos 140+75 size 10
            #Body
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",1),Show("wardrobe")]
            add "01_hp/18_store/29.png" xpos 0+90 ypos 90 zoom 0.3
            text "Body" xpos 76+90 ypos 140+75 size 10
            #Piercings
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",2),Show("wardrobe")]
            add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130+180 ypos -120
            text "Piercings" xpos 76+180 ypos 140+75 size 10
            #Tattoos
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",3),Show("wardrobe")]
            add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130+270 ypos -120
            text "Tattoos" xpos 76+270 ypos 140+75 size 10
            #Potions
            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",4),Show("wardrobe")]
            add "01_hp/18_store/32.png" xpos 0+360 ypos 90 zoom 0.3
            text "Potions" xpos 76+360 ypos 140+75 size 10

            ## Head Items ##
            if wardrobe_accessories_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/accessories/cat_ears.png" xpos -10 ypos 40 zoom 0.5
                text "Head" xpos 76 ypos 140+75 size 10

                if "tiara" in cs_existing_stock:
                    hotspot (75, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",2),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/tiara.png" xpos -130 ypos -120+92
                if "reading_glasses" in cs_existing_stock:
                    hotspot (75+90, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",4),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/reading_glasses.png" xpos -130+90 ypos -120+92
                if "vintage_glasses" in cs_existing_stock:
                    hotspot (75+180, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",5),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/vintage_glasses.png" xpos -130+180 ypos -120+92
                if "cat_ears" in cs_existing_stock:
                    hotspot (75+270, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",7),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/cat_ears.png" xpos -10+270 ypos 40+92 zoom 0.5
                if "elf_ears" in cs_existing_stock:
                    hotspot (75+360, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",9),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/elf_ears.png" xpos -130+360 ypos -120+92

                if "freckles" in cs_existing_stock:
                    hotspot (75, 140+184, 83, 85) clicked [SetVariable("wardrobe_acc_item",3),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/freckles.png" xpos -130 ypos -120+184
                if "fake_cum" in cs_existing_stock:
                    hotspot (75+90, 140+184, 83, 85) clicked [SetVariable("wardrobe_acc_item",6),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/fake_cum.png" xpos -130+90 ypos -120+184


            ## Body Items ##
            if wardrobe_accessories_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "01_hp/18_store/29.png" xpos 0+90 ypos 90 zoom 0.3
                text "Body" xpos 76+90 ypos 140+75 size 10

                if "SPEW_badge" in cs_existing_stock:
                    hotspot (75, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",0),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130 ypos -120+92
                if "CUM_badge" in cs_existing_stock:
                    hotspot (75+90, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",1),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/cum_badge.png" xpos -130+90 ypos -120+92

            ##  Piercings ##
            if wardrobe_accessories_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130+180 ypos -120
                text "Piercings" xpos 76+180 ypos 140+75 size 10

            ##  Tattoos ##
            if wardrobe_accessories_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130+270 ypos -120
                text "Tattoos" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_her_tattoo_list)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("tattoo_choice",(wr_her_tattoo_list[i])), Jump("equip_tattoo")]
                    add "01_hp/13_characters/hermione/body/tattoo/"+wr_her_tattoo_list[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            ## Potions Category ##
            if wardrobe_accessories_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "01_hp/18_store/32.png" xpos 0+360 ypos 90 zoom 0.3
                text "Potions" xpos 76+360 ypos 140+75 size 10

                if "transparency" in cs_existing_stock:
                    hotspot (75, 140+92, 83, 85) clicked [SetVariable("wardrobe_acc_item",8),Jump("wardrobe_give_acc")]
                    add "01_hp/18_store/32.png" xpos 0 ypos 90+92 zoom 0.3
                    text "Transparency" xpos 76 ypos 140+75+92 size 10

        else:
            pass


## Wardrobe Underwear ##
 
        if wardrobe_page == 6:

            #Bras
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
            add "interface/wardrobe_icons/underwear/underwear_bra.png" xpos 15 ypos 60 zoom 0.35
            text "Bras" xpos 76 ypos 140+75 size 10
            #Panties
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",1),Show("wardrobe")]
            add "interface/wardrobe_icons/underwear/underwear_panties.png" xpos 15+90 ypos 17 zoom 0.35
            text "Panties" xpos 76+90 ypos 140+75 size 10
            #Corsets
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",2),Show("wardrobe")]
            add "interface/wardrobe_icons/underwear/underwear_corset.png" xpos 15+180 ypos 40 zoom 0.35
            text "Corsets" xpos 76+180 ypos 140+75 size 10
            #Garterbelts
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",3),Show("wardrobe")]
            add "interface/wardrobe_icons/underwear/underwear_garterbelt.png" xpos 15+270 ypos 17 zoom 0.35
            text "Garterbelts" xpos 76+270 ypos 140+75 size 10
            #Misc
            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",4),Show("wardrobe")]
            add "interface/wardrobe_icons/underwear/underwear_misc.png" xpos 15+360 ypos 60 zoom 0.35
            text "Misc." xpos 76+360 ypos 140+75 size 10

            #Bras
            if wardrobe_underwear_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/underwear/underwear_bra.png" xpos 15 ypos 60 zoom 0.35
                text "Bras" xpos 76 ypos 140+75 size 10
                for i in range(0,len(wr_her_bras)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_her_bras[i])), Jump("equip_bra")]
                    add "01_hp/13_characters/hermione/clothes/underwear/"+wr_her_bras[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Panties
            if wardrobe_underwear_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/underwear/underwear_panties.png" xpos 15+90 ypos 17 zoom 0.35
                text "Panties" xpos 76+90 ypos 140+75 size 10
                for i in range(0,len(wr_her_panties)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_her_panties[i])), Jump("equip_panties")]
                    add "01_hp/13_characters/hermione/clothes/underwear/"+wr_her_panties[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35

            #Corsets
            if wardrobe_underwear_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/underwear/underwear_corset.png" xpos 15+180 ypos 40 zoom 0.35
                text "Corsets" xpos 76+180 ypos 140+75 size 10
                for i in range(0,len(wr_her_corsets)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_her_corsets[i])), Jump("equip_corset")]
                    add "01_hp/13_characters/hermione/clothes/underwear/"+wr_her_corsets[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35

            #Garterbelts
            if wardrobe_underwear_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/underwear/underwear_garterbelt.png" xpos 15+270 ypos 17 zoom 0.35
                text "Garterbelts" xpos 76+270 ypos 140+75 size 10
                for i in range(0,len(wr_her_garterbelts)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_her_garterbelts[i])), Jump("equip_garterbelt")]
                    add "01_hp/13_characters/hermione/clothes/underwear/"+wr_her_garterbelts[i]+".png" xpos 15+(90*col) ypos (17+92+(92*row)) zoom 0.35


            #Misc #For stuff like pasties
            if wardrobe_underwear_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_underwear_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/underwear/underwear_misc.png" xpos 15+360 ypos 60 zoom 0.35
                text "Misc." xpos 76+360 ypos 140+75 size 10
                for i in range(0,len(wr_her_bra_misc)):
                    $ row = i // 5
                    $ col = i % 5

                    hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("underwear_choice",(wr_her_bra_misc[i])), Jump("equip_bra")]
                    add "01_hp/13_characters/hermione/clothes/underwear/"+wr_her_bra_misc[i]+".png" xpos 15+(90*col) ypos (60+92+(92*row)) zoom 0.35 #Temp

                #Add underwear_panties_misc after underwear_bra_misc
        else:
            pass


## Wardrobe Outfits ## 

        if wardrobe_page == 7:

            #Outfits
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
            add "01_hp/23_clothes_store/cs_gui/maid.png" xpos 75 ypos 116 zoom 0.18
            text "Outfits" xpos 76 ypos 140+75 size 10
            #Costumes
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",1),Show("wardrobe")]
            add "01_hp/23_clothes_store/cs_gui/pirate.png" xpos 75+90 ypos 116 zoom 0.18
            text "Costumes" xpos 76+90 ypos 140+75 size 10
            #One-Pieces
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",2),Show("wardrobe")]
            add "01_hp/23_clothes_store/cs_gui/nightgown.png" xpos 75+180 ypos 116 zoom 0.18
            text "One-Piece" xpos 76+180 ypos 140+75 size 10
            #Swimsuits
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",3),Show("wardrobe")]
            add "01_hp/23_clothes_store/cs_gui/mannequin.png" xpos 75+270 ypos 116 zoom 0.18
            text "Swimsuits" xpos 76+270 ypos 140+75 size 10
            #Dresses
            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",4),Show("wardrobe")]
            add "01_hp/23_clothes_store/cs_gui/ball_dress.png" xpos 75+360 ypos 116 zoom 0.18
            text "Dresses" xpos 76+360 ypos 140+75 size 10


            #Outfits
            if wardrobe_outfits_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "01_hp/23_clothes_store/cs_gui/maid.png" xpos 75 ypos 116 zoom 0.18
                text "Outfits" xpos 76 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_her_outfits)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_outfits):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_outfits[index]), Jump("wardrobe_wear_costume")]
                        add "01_hp/23_clothes_store/cs_gui/"+wr_her_outfits[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #Costumes
            if wardrobe_outfits_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "01_hp/23_clothes_store/cs_gui/pirate.png" xpos 75+90 ypos 116 zoom 0.18
                text "Costumes" xpos 76+90 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_her_costumes)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_costumes):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_costumes[index]), Jump("wardrobe_wear_costume")]
                        add "01_hp/23_clothes_store/cs_gui/"+wr_her_costumes[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #One-Pieces
            if wardrobe_outfits_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "01_hp/23_clothes_store/cs_gui/nightgown.png" xpos 75+180 ypos 116 zoom 0.18
                text "One-Pieces" xpos 76+180 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_her_onepieces)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_onepieces):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_onepieces[index]), Jump("wardrobe_wear_costume")]
                        add "01_hp/23_clothes_store/cs_gui/"+wr_her_onepieces[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #Swimsuits
            if wardrobe_outfits_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "01_hp/23_clothes_store/cs_gui/mannequin.png" xpos 75+270 ypos 116 zoom 0.18
                text "Swimsuits" xpos 76+270 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_her_swimsuits)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_swimsuits):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_swimsuits[index]), Jump("wardrobe_wear_costume")]
                        add "01_hp/23_clothes_store/cs_gui/"+wr_her_swimsuits[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1

            #Dresses
            if wardrobe_outfits_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_outfits_category",0),Show("wardrobe")]
                add "01_hp/23_clothes_store/cs_gui/ball_dress.png" xpos 75+360 ypos 116 zoom 0.18
                text "Dresses" xpos 76+360 ypos 140+75 size 10
                $ index = 0
                for i in range(0,len(wr_her_dresses)):
                    $ row = i // 5
                    $ col = i % 5

                    if index < len(hg_purchased_dresses):

                        hotspot ((75+(90*col)), (230+(92*row)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_dresses[index]), Jump("wardrobe_wear_costume")]
                        add "01_hp/23_clothes_store/cs_gui/"+wr_her_dresses[i]+".png" xpos 75+(90*col) ypos 116+92+(92*row) zoom 0.18
                        $ index = index+1
        

        else:
            pass


## Wardrobe Gifts ##

        if wardrobe_page == 8:
            # note that gift_items are indices (starting with 0) but the
            # image files are starting with/off by 1.

            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
            add "01_hp/18_store/gifts/2.png" xpos 0 ypos 90 zoom 0.3      #Gifts
            text "Sweets" xpos 76 ypos 140+75 size 10

            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",1),Show("wardrobe")]
            add "01_hp/18_store/gifts/7.png" xpos 0+90 ypos 90 zoom 0.3  #Magazines
            text "Magazines" xpos 76+90 ypos 140+75 size 10

            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",2),Show("wardrobe")]
            add "01_hp/18_store/gifts/4.png" xpos 0+180 ypos 90 zoom 0.3  #Beverage
            text "Beverages" xpos 76+180 ypos 140+75 size 10

            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",3),Show("wardrobe")]
            add "01_hp/18_store/gifts/3.png" xpos 0+270 ypos 90 zoom 0.3 #Sex Toys
            text "Toys" xpos 76+270 ypos 140+75 size 10

            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",4),Show("wardrobe")]
            add "01_hp/18_store/01.png" xpos 0+360 ypos 90 zoom 0.3
            text "Quest Items" xpos 76+360 ypos 140+75 size 10

            #Sweets
            if wardrobe_gifts_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
                add "01_hp/18_store/gifts/2.png" xpos 0 ypos 90 zoom 0.3      #Gifts
                text "Sweets" xpos 76 ypos 140+75 size 10

                for i in range(0,18): #0,18
                    $ row = i // 5    #6
                    $ col = i % 5     #6
                    if gift_item_inv[i] > 0:
                        hotspot ((75+(90*col)), (140+92+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",i),Jump("wardrobe_give_gift")] #75 was 21
                    add "01_hp/18_store/gifts/"+str(i+1)+".png" xpos 0+(90*col) ypos (90+92+(92*row)) zoom 0.30 #0 was -60
                    text str(gift_item_inv[i]) xpos 75+(90*col) ypos (210+92+(92*row))

            #Magazines
            if wardrobe_gifts_category == 1: 
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]   
                add "01_hp/18_store/gifts/7.png" xpos 0+90 ypos 90 zoom 0.3  #Magazines
                text "Magazines" xpos 76+90 ypos 140+75 size 10

            #Beverages
            if wardrobe_gifts_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
                add "01_hp/18_store/gifts/4.png" xpos 0+180 ypos 90 zoom 0.3  #Beverage
                text "Beverages" xpos 76+180 ypos 140+75 size 10

            #Toys
            if wardrobe_gifts_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
                add "01_hp/18_store/gifts/3.png" xpos 0+270 ypos 90 zoom 0.3 #Sex Toys
                text "Toys" xpos 76+270 ypos 140+75 size 10

            #Quest Items
            if wardrobe_gifts_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_gifts_category",0),Show("wardrobe")]
                add "01_hp/18_store/01.png" xpos 0+360 ypos 90 zoom 0.3
                text "Quest Items" xpos 76+360 ypos 140+75 size 10

                #Collar Event
                if collar == 0 and whoring >= 24:
                    hotspot (75+270, 140+92, 83, 85) clicked [Jump("start_collar_event")]
                    add "01_hp/13_characters/hermione/accessories/collars/collar_0.png" xpos -40+270 ypos 55+92 zoom 0.5
                    text "Collar Event" xpos 76+270 ypos 140+75+92 size 10
                else:
                    add "01_hp/13_characters/hermione/accessories/collars/collar_5.png" xpos -40+270 ypos 55+92 zoom 0.5

                #Dress/Start End Event
                if whoring >= 24 and have_no_dress_hap and not gave_the_dress:
                    hotspot (75+360, 140+92, 83, 85) clicked [Jump("giving_the_dress")]
                    add "01_hp/23_clothes_store/cs_gui/ball_dress.png" xpos 70+370 ypos 116+92 zoom 0.18
                    text "End" xpos 76+360 ypos 140+65+92 size 10
                    text "Event" xpos 76+360 ypos 140+75+92 size 10
                else:
                    add "01_hp/23_clothes_store/cs_gui/ball_dress_b.png" xpos 70+370 ypos 116+92 zoom 0.18


        else:
            pass

screen wardrobe_potions: #(Removed)
        
        for i in range(0,6):
            hotspot ((21+(90*i)), 140, 83, 85):
                hovered [SetVariable("potion_name",p_potion_names[i])]
                clicked [SetVariable("wardrobe_potion",i+1),Jump("wardrobe_give_potion")]
        
        for i in range(1,7):
            add "01_hp/25_mo/potion_"+str(i)+".png" xpos -80+(90*i) ypos 135 zoom 0.8
        for i in range(7,11):
            add "01_hp/25_mo/potion_"+str(i)+".png" xpos -80+(90*(i-6)) ypos 225 zoom 0.8
        
#








