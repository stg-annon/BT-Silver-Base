

label update_wardrobe_lists:

### Hair Color ###
#    $ wr_her_haircolor = ["dye_1"]







### Tops ###
    $ wr_her_tops_uniform = [] #ADD school clothing and cheerleader tops,...

    if whoring >= 0:
        $ wr_her_tops_uniform.append("uni_top_1")
    if whoring >= 3: #get right number
        $ wr_her_tops_uniform.append("uni_top_2")
    if whoring >= 6: #get right number
        $ wr_her_tops_uniform.append("uni_top_3")
    if whoring >= 9: #get right number
        $ wr_her_tops_uniform.append("uni_top_4")
    if whoring >= 12: #get right number
        $ wr_her_tops_uniform.append("uni_top_5")
    if whoring >=18:
        $ wr_her_tops_uniform.append("uni_top_6")
        $ wr_her_tops_uniform.remove("uni_top_3") #remove shirt 3. Looks ugly, no point in having it when she's willing to wear shirt 4.

    $ wr_her_tops_fancy = []  #ADD sexy clothing
    if whoring >= 3: #get right number
        $ wr_her_tops_fancy.append("fancy_waitress_beige")
    if whoring >= 9: #get right number
        $ wr_her_tops_fancy.append("fancy_waitress_green")

    $ wr_her_tops_wicked = [] #ADD kinky clothing items like leather, fishnet
    if whoring >= 12: #get right number
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves_open")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless_open")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves_open")
    if whoring >= 18: #get right number
        $ wr_her_tops_wicked.append("wicked_corset")
        $ wr_her_tops_wicked.append("wicked_corset_with_net")

    $ wr_her_tops_normal = [] #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    if whoring >= 6: #get right number
        $ wr_her_tops_normal.append("normal_pullover")
        $ wr_her_tops_normal.append("normal_pullover_sexy")
    if whoring >= 9: #get right number
        $ wr_her_tops_normal.append("normal_purple_sweater")
        $ wr_her_tops_normal.append("normal_sports")
        $ wr_her_tops_normal.append("normal_sweater")

    $ wr_her_tops_misc = []   #ADD Misc top items
    if whoring >= 9: #get right number
        $ wr_her_tops_misc.append("top_banner_gryff")
    if whoring >= 12: #get right number
        $ wr_her_tops_misc.append("top_shirt_gryff_ripped_long_tie")
        $ wr_her_tops_misc.append("top_tie_gryff")
        $ wr_her_tops_misc.append("top_banner_slyth")
    if whoring >= 18: #get right number
        $ wr_her_tops_misc.append("top_fishnets")


### Bottoms ###
    $ wr_her_bottoms_uniform = [] #Page MAX=25

    ## Skirts ##
    if whoring >= 0:
        $ wr_her_bottoms_uniform.append("uni_skirt_1")
    if whoring >= 3: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_2")
    if whoring >= 6: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_3")
    if whoring >= 9: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_4")
    if whoring >= 12: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_5")

    $ wr_her_bottoms_uniform_low = []  #Add low hanging school skirts
    #if micro_skirt unlocked/purchased:
    #    $ wr_her_bottoms_uniform_low.append("uni_skirt_5_low") #micro skirt

    $ wr_her_bottoms_skirts = [] #Add skirts
    #ADD japan_pant

    $ wr_her_bottoms_pants = [] #Add pants

    #if "pants_jeans_long" in cs_existing_stock:
    $ wr_her_bottoms_pants.append("pants_jeans_long")
    #if "pants_jeans_short" in cs_existing_stock:
    $ wr_her_bottoms_pants.append("pants_jeans_short")
    #ADD rocker_skirt

    $ wr_her_bottoms_misc = []   #ADD Misc bottom items

### Stockings ###

    #Neckwear
    $ wr_her_neckwears = []

    #Belts
    $ wr_her_belts = []

    #Gloves
    $ wr_her_gloves = []

    #Stockings
    $ wr_her_stockings = []

    if "gryff_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("gryff_stockings")
    if "gryff_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("gryff_stockings_vibe")
    if "gryff_cheer_stockings_short" in cs_existing_stock:
        $ wr_her_stockings.append("gryff_cheer_stockings_short")
    if "gryff_cheer_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("gryff_cheer_stockings")
    if "gryff_cheer_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("gryff_cheer_stockings_vibe")

    if "slyth_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("slyth_stockings")
    if "slyth_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("slyth_stockings_vibe")
    if "slyth_cheer_stockings_short" in cs_existing_stock:
        $ wr_her_stockings.append("slyth_cheer_stockings_short")
    if "slyth_cheer_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("slyth_cheer_stockings")
    if "slyth_cheer_stockings_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("slyth_cheer_stockings_vibe")
    #ADD Ravenclaw Blue. And maybe Hufflepuff.



    if "lace_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("lace_stockings")

    if "fishnet_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("fishnet_stockings")

    #Robes
    $ wr_her_robes = ["gryff_robe_shirt_none","gryff_robe_off"]
    if whoring >= 3:
        $ wr_her_robes.append("gryff_robe_gap_wide")
    if whoring >= 6:
        $ wr_her_robes.append("gryff_robe_seethrough")
    if whoring >= 9:
        $ wr_her_robes.append("gryff_quidditch")


    if whoring >= 6:
        $ wr_her_robes.append("slyth_robe_shirt_none")
        $ wr_her_robes.append("slyth_robe_off")
        $ wr_her_robes.append("slyth_robe_gap_wide")
    if whoring >= 9:
        $ wr_her_robes.append("slyth_robe_seethrough")
    if whoring >= 12:
        $ wr_her_robes.append("slyth_quidditch")


### Underwear ###
    $ wr_her_bras = []

    $ wr_her_panties = []

    $ wr_her_corsets = []

    $ wr_her_garterbelts = []

    $ wr_her_underwear_misc = []


### Outfits ###
    $ wr_her_outfits = []

    $ wr_her_costumes = []

    $ wr_her_onepieces = []

    $ wr_her_swimsuits = []

    $ wr_her_dresses = []
    
    if "Heart Dancer" in hermione_outfits_list: #doesn't work. in what list is the purchased outfit stored?
        $ wr_her_dresses.append("Heart Dancer")
    if "Ball Dress" in hermione_outfits_list:
        $ wr_her_dresses.append("Ball Dress")




    return