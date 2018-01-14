

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
        elif wardrobe_page == 4: #stockings & gloves
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
        hotspot (742+280,10,42,41) clicked [SetVariable("wardrobe_page",0),Jump("close_wardrobe")]    #Close Wardrobe and set to default.
        text "Hermione Granger" xpos 720 ypos 72 size 18
        text "Toggle" xpos 668 ypos 129 size 12 

        
        ## Page Specific Hotspots ##
        if wardrobe_page == 0: #default #Not used yet.
            #text "Stats" xpos 195 ypos 96 size 26
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

        #Stockings
        if wardrobe_page == 4:
            hotspot (555, 450, 90, 98) clicked [SetVariable("wardrobe_page",0),Show("wardrobe")]
            text "Stockings & Gloves" xpos 118 ypos 100 size 18
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
            text "Bras & Panties" xpos 118 ypos 100 size 18
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
        if whoring >= 9:
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
        if whoring >= 15 and not hermione_wear_top:
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
        if whoring >= 9:
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
        if whoring >= 15 and not hermione_wear_skirt:
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

        ## Gloves Toggle ##
        if whoring >= 0:
        #    hotspot (667,150+100,18,18) clicked Jump("her_gloves_toggle")
        #    if h_stocking == "00_blank":
        #        add "interface/check_01.png" xpos 667 ypos 145+100 #ypos-5 of hotspot ypos
        #    else:
        #        add "interface/check_02.png" xpos 667 ypos 145+100
        #    text "Gloves" xpos 688 ypos 154+100 size 10
        #else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+100   #grayed out
            text "{color=#858585}Gloves{/color}" xpos 688 ypos 154+100 size 10          #grayed out

        ## Stockings Toggle ##
        if whoring >= 0:
            hotspot (667,150+125,18,18) clicked Jump("her_stockings_toggle")
            if h_stocking == "00_blank":
                add "interface/check_01.png" xpos 667 ypos 145+125 #ypos-5 of hotspot ypos
            else:
                add "interface/check_02.png" xpos 667 ypos 145+125
            text "Stockings" xpos 688 ypos 154+125 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+125   #grayed out
            text "{color=#858585}Stockings{/color}" xpos 688 ypos 154+125 size 10          #grayed out

        ## Outfit Toggle ##
        if whoring >= 0:
            hotspot (667,150+150,18,18) clicked [SetVariable("wardrobe_costume_selection",None),Jump("wardrobe_wear_costume")] #"wardrobe_costume_selection",None #wardrobe_wear_costume
            if not wardrobe_costume_selection:
                add "interface/check_01.png" xpos 667 ypos 145+150 #ypos-5 of hotspot ypos
            else:
                add "interface/check_02.png" xpos 667 ypos 145+150
            text "Outfit" xpos 688 ypos 154+150 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+150   #grayed out
            text "{color=#858585}Outfit{/color}" xpos 688 ypos 154+150 size 10          #grayed out

        ## Robe Toggle ##
        if whoring >= 0:
            hotspot (667,150+175,18,18) clicked Jump("her_robe_toggle")
            if hermione_wear_robe:
                add "interface/check_02.png" xpos 667 ypos 145+175 #ypos-5 of hotspot ypos
            else:
                add "interface/check_01.png" xpos 667 ypos 145+175
            text "Robe" xpos 688 ypos 154+175 size 10
        else:
            add "interface/check_01_grey_full.png" xpos 667 ypos 145+175   #grayed out
            text "{color=#858585}Robe{/color}" xpos 688 ypos 154+175 size 10          #grayed out


### Wardrobe Hair ###  

        if wardrobe_page == 1:
            ## Change Hairstlye ##
            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","A"),Jump("change_her_hair")]
            hotspot (165, 140, 83, 85) clicked [SetVariable("wardrobe_hair_style","B"),Jump("change_her_hair")]
            add "01_hp/13_characters/hermione/body/head/A_1.png" xpos 10 ypos 105 zoom 0.35
            add "01_hp/13_characters/hermione/body/head/B_1.png" xpos 10+90 ypos 105 zoom 0.35

            for i in range(0,10): #Add more for every haircolor. Page MAX=20
                $ row = i // 5
                $ col = i % 5

                hotspot ((75+(90*col)), (230+(90*row)), 83, 85) clicked [SetVariable("wardrobe_hair_color",(i+1)),Jump("change_her_hair")]
                add "interface/wardrobe_icons/dyes/dye_"+str(i+1)+".png" xpos 75+(90*col) ypos (230+(90*row)) zoom 0.70
        else:
            pass


### Wardrope Tops ###

        if wardrobe_page == 2:
            ## Hermione ##
            #ADD if hermione...: 
            for i in range(0,len(wr_her_tops)): #List MAX = 25, add *tops_2 for a page 2.
                $ row = i // 5
                $ col = i % 5

                hotspot ((75+(90*col)), (140+(90*row)), 83, 85) clicked [SetVariable("top_choice",(i+1)), Jump("equip_top")]
                add "01_hp/13_characters/hermione/clothes/uniform/top/"+wr_her_tops[i]+".png" xpos 15+(90*col) ypos (60+(90*row)) zoom 0.35
            #ADD elif for other girls.
        else:
            pass


### Wardrobe Bottoms ###

        if wardrobe_page == 3:
            ## Hermione ##
            #ADD if hermione:
            for i in range(0,len(wr_her_bottoms)):
                $ row = i // 5
                $ col = i % 5

                hotspot ((75+(90*col)), (140+(90*row)), 83, 85) clicked [SetVariable("skirt_choice",(i+1)), Jump("equip_skirt")]
                add "01_hp/13_characters/hermione/clothes/uniform/bot/"+wr_her_bottoms[i]+".png" xpos 15+(90*col) ypos (20+(90*row)) zoom 0.35
            #ADD elif for other girls.
        else:
            pass


## Wardrobe Stockings ##

        if wardrobe_page == 4:
            ## Hermione ##
            for i in range(0,len(wr_her_stockings)):
                hotspot ((75+(90*i)), 140, 83, 85) clicked [SetVariable("wr_her_stockings_choice",wr_her_stockings[i]),Jump("wardrobe_wear_stockings")]
        
            for i in range(0,len(wr_her_stockings)):
                add "01_hp/13_characters/hermione/clothes/stockings/"+str(wr_her_stockings[i])+".png" xpos -85+(90*i) ypos -195 zoom 0.7
        else:
            pass


## Wardrobe Accessories ##

        if wardrobe_page == 5:

            hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
            add "interface/wardrobe_icons/accessories/cat_ears.png" xpos -10 ypos 40 zoom 0.5
            text "Head" xpos 76 ypos 140+75 size 10
            #Badges
            hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",1),Show("wardrobe")]
            add "01_hp/18_store/29.png" xpos 0+90 ypos 90 zoom 0.3
            text "Body" xpos 76+90 ypos 140+75 size 10
            #
            hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",2),Show("wardrobe")]
            add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130+180 ypos -120
            text "Tattoos" xpos 76+180 ypos 140+75 size 10
            #Potions
            hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",3),Show("wardrobe")]
            add "01_hp/18_store/32.png" xpos 0+270 ypos 90 zoom 0.3
            text "Potions" xpos 76+270 ypos 140+75 size 10
            #Robes
            hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",4),Show("wardrobe")]
            add "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png" xpos -10+415 ypos 75 zoom 0.25
            text "Robes" xpos 76+360 ypos 140+75 size 10

            ## Head Items Category 0 ##
            if wardrobe_accessories_category == 0:
                hotspot (75, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/accessories/cat_ears.png" xpos -10 ypos 40 zoom 0.5
                text "Head" xpos 76 ypos 140+75 size 10

                if "tiara" in cs_existing_stock:
                    hotspot (75, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",2),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/tiara.png" xpos -130 ypos -120+90
                if "reading_glasses" in cs_existing_stock:
                    hotspot (75+90, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",4),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/reading_glasses.png" xpos -130+90 ypos -120+90
                if "vintage_glasses" in cs_existing_stock:
                    hotspot (75+180, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",5),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/vintage_glasses.png" xpos -130+180 ypos -120+90
                if "cat_ears" in cs_existing_stock:
                    hotspot (75+270, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",7),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/cat_ears.png" xpos -10+270 ypos 40+90 zoom 0.5
                if "elf_ears" in cs_existing_stock:
                    hotspot (75+360, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",9),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/elf_ears.png" xpos -130+360 ypos -120+90

                if "freckles" in cs_existing_stock:
                    hotspot (75, 140+180, 83, 85) clicked [SetVariable("wardrobe_acc_item",3),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/freckles.png" xpos -130 ypos -120+180
                if "fake_cum" in cs_existing_stock:
                    hotspot (75+90, 140+180, 83, 85) clicked [SetVariable("wardrobe_acc_item",6),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/fake_cum.png" xpos -130+90 ypos -120+180


            ## Body Items Category=1 ##
            if wardrobe_accessories_category == 1:
                hotspot (75+90, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "01_hp/18_store/29.png" xpos 0+90 ypos 90 zoom 0.3
                text "Body" xpos 76+90 ypos 140+75 size 10

                if "SPEW_badge" in cs_existing_stock:
                    hotspot (75, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",0),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130 ypos -120+90
                if "CUM_badge" in cs_existing_stock:
                    hotspot (75+90, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",1),Jump("wardrobe_give_acc")]
                    add "interface/wardrobe_icons/accessories/cum_badge.png" xpos -130+90 ypos -120+90

            ##  Category 3 ##
            if wardrobe_accessories_category == 2:
                hotspot (75+180, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "interface/wardrobe_icons/accessories/spew_badge.png" xpos -130+180 ypos -120
                text "Tattoos" xpos 76+180 ypos 140+75 size 10

            ## Potions Category 3 ##
            if wardrobe_accessories_category == 3:
                hotspot (75+270, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "01_hp/18_store/32.png" xpos 0+270 ypos 90 zoom 0.3
                text "Potions" xpos 76+270 ypos 140+75 size 10

                if "transparency" in cs_existing_stock:
                    hotspot (75, 140+90, 83, 85) clicked [SetVariable("wardrobe_acc_item",8),Jump("wardrobe_give_acc")]
                    add "01_hp/18_store/32.png" xpos 0 ypos 90+90 zoom 0.3
                    text "Transparency" xpos 76 ypos 140+75+90 size 10

            ## Robes Category 4 ##
            if wardrobe_accessories_category == 4:
                hotspot (75+360, 140, 83, 85) clicked [SetVariable("wardrobe_accessories_category",0),Show("wardrobe")]
                add "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png" xpos -10+415 ypos 75 zoom 0.25
                text "Robes" xpos 76+360 ypos 140+75 size 10

                #if "transparency" in cs_existing_stock:
                #    hotspot (75, 230, 83, 85) clicked [SetVariable("hermione_robe","01_hp/13_characters/hermione/clothes/robe/gryff_robe.png"),Jump("wardrobe_give_acc")]
                #    add "01_hp/13_characters/hermione/clothes/robe/gryff_robe.png" xpos -10 ypos 75+90 zoom 0.25
        else:
            pass


## Wardrobe Underwear ##
 
        if wardrobe_page == 6:
            pass



## Wardrobe Outfits ## 

        if wardrobe_page == 7:
            $ hg_purchased_outfits = []
            for i in hermione_outfits_list:
                if i.purchased:
                    $ hg_purchased_outfits.append(i)
        
            $ index = 0
            for i in range(0,5): #5
                for j in range(0,5): #6
                    if index < len(hg_purchased_outfits):
                        hotspot ((75+(90*j)), (140+(92*i)), 83, 85) clicked [SetVariable("wardrobe_costume_selection",hg_purchased_outfits[index]),Jump("wardrobe_wear_costume")]
                        add hg_purchased_outfits[index].getStoreImage() xpos (75+(90*j)) ypos (116+(92*i)) zoom 0.18 #75 was 13
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
                        hotspot ((75+(90*col)), (140+90+(92*row)), 83, 85) clicked [SetVariable("wardrobe_gift_item",i),Jump("wardrobe_give_gift")] #75 was 21
                    add "01_hp/18_store/gifts/"+str(i+1)+".png" xpos 0+(90*col) ypos (90+90+(90*row)) zoom 0.30 #0 was -60
                    text str(gift_item_inv[i]) xpos 75+(90*col) ypos (210+90+(90*row))

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
                    hotspot (75+270, 140+90, 83, 85) clicked [Jump("start_collar_event")]
                    add "01_hp/13_characters/hermione/accessories/collars/collar_0.png" xpos -40+270 ypos 55+90 zoom 0.5
                    text "Collar Event" xpos 76+270 ypos 140+75+90 size 10
                else:
                    add "01_hp/13_characters/hermione/accessories/collars/collar_5.png" xpos -40+270 ypos 55+90 zoom 0.5

                #Dress/Start End Event
                if whoring >= 24 and have_no_dress_hap and not gave_the_dress:
                    hotspot (75+360, 140+90, 83, 85) clicked [Jump("giving_the_dress")]
                    add "01_hp/23_clothes_store/cs_gui/ball_dress.png" xpos 70+370 ypos 116+90 zoom 0.18
                    text "End" xpos 76+360 ypos 140+65+90 size 10
                    text "Event" xpos 76+360 ypos 140+75+90 size 10
                else:
                    add "01_hp/23_clothes_store/cs_gui/ball_dress_b.png" xpos 70+370 ypos 116 zoom 0.18


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








