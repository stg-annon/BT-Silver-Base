

label update_wardrobe_lists:

### Hair Color ###
#    $ wr_her_haircolor = ["dye_1"]







### Tops ###
    $ wr_her_tops_uniform = [] #ADD school clothing and cheerleader tops,...

    #Uniform
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

    if whoring >= 6 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_gryff")
    if whoring >= 9 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_gryff_skimpy")

    if whoring >= 15 and hg_slythCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_slyth")
    if whoring >= 15 and hg_slythCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_slyth_skimpy")

    #Fancy
    $ wr_her_tops_fancy = []  #ADD sexy clothing
    if whoring >= 3: #get right number
        $ wr_her_tops_fancy.append("fancy_waitress_beige")
    if whoring >= 9: #get right number
        $ wr_her_tops_fancy.append("fancy_waitress_green")

    #Wicked
    $ wr_her_tops_wicked = [] #ADD kinky clothing items like leather, fishnet
    if whoring >= 12: #get right number
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves_open")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless_open")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves_open")

    if whoring >= 21 and hg_rocker_OBJ.purchased: #get right number
        $ wr_her_tops_wicked.append("wicked_rocker_top")

    $ wr_her_tops_normal = [] #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    if whoring >= 6: #get right number
        $ wr_her_tops_normal.append("normal_pullover")
        $ wr_her_tops_normal.append("normal_pullover_sexy")
    if whoring >= 9: #get right number
        $ wr_her_tops_normal.append("normal_purple_sweater")

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

    #Uniform
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

    if whoring >= 6 and hg_gryffCheer_OBJ.purchased: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_cheer_gryff")
    if whoring >= 15 and hg_slythCheer_OBJ.purchased: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_cheer_slyth")

    #Uniform Low
    $ wr_her_bottoms_uniform_low = []  #Add low hanging school skirts

    if whoring >= 0:
        $ wr_her_bottoms_uniform_low.append("uni_skirt_1_low")
    if whoring >= 3: #get right number
        $ wr_her_bottoms_uniform_low.append("uni_skirt_2_low")
    if whoring >= 6: #get right number
        $ wr_her_bottoms_uniform_low.append("uni_skirt_3_low")
    if whoring >= 9: #get right number
        $ wr_her_bottoms_uniform_low.append("uni_skirt_4_low")
    #if micro_skirt unlocked/purchased:
    #    $ wr_her_bottoms_uniform_low.append("uni_skirt_5_low") #micro skirt

    #Skirts
    $ wr_her_bottoms_skirts = [] #Add skirts
    if whoring >= 9:
        $ wr_her_bottoms_skirts.append("skirt_belted_mini")
    if whoring >= 18:
        $ wr_her_bottoms_skirts.append("skirt_belted_micro")
    #ADD japan_pant

    #Pants
    $ wr_her_bottoms_pants = [] #Add

    if "pants_jeans_long" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_jeans_long")
    if "pants_jeans_short" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_jeans_short")
    if whoring >= 18:
        $ wr_her_bottoms_pants.append("pants_retro_shorts")
    if whoring >= 21 and hg_rocker_OBJ.purchased:
        $ wr_her_bottoms_pants.append("pants_rocker")

    #Bottoms Misc
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

    if "stockings_gryff" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff")
    if "stockings_gryff_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff_vibe")
    if "stockings_gryff_cheer_short" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff_cheer_short")
    if "stockings_gryff_cheer" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff_cheer")
    if "stockings_gryff_cheer_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff_cheer_vibe")

    if "stockings_slyth" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_slyth")
    if "stockings_slyth_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_slyth_vibe")
    if "stockings_slyth_cheer_short" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_slyth_cheer_short")
    if "stockings_slyth_cheer" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_slyth_cheer")
    if "stockings_slyth_cheer_vibe" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_slyth_cheer_vibe")
    #ADD Ravenclaw Blue. And maybe Hufflepuff.



    if "stockings_lace_black" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_lace_black")

    if "stockings_fishnet_black" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_fishnet_black")

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

    #Outfits
    $ wr_her_outfits = []
    $ hg_purchased_outfits = []
    if hg_maid_OBJ.purchased:
        $ wr_her_outfits.append("maid")
        $ hg_purchased_outfits.append(hg_maid_OBJ)
    if hg_gryffCheer_OBJ.purchased:
        $ wr_her_outfits.append("cheer")
        $ hg_purchased_outfits.append(hg_gryffCheer_OBJ)
    if hg_slythCheer_OBJ.purchased:
        $ wr_her_outfits.append("s_cheer")
        $ hg_purchased_outfits.append(hg_slythCheer_OBJ)
    if hg_christmas_OBJ.purchased:
        $ wr_her_outfits.append("christmas")
        $ hg_purchased_outfits.append(hg_christmas_OBJ)
    if hg_present_OBJ.purchased:
        $ wr_her_outfits.append("present")
        $ hg_purchased_outfits.append(hg_present_OBJ)
    if hg_rocker_OBJ.purchased:
        $ wr_her_outfits.append("rocker")
        $ hg_purchased_outfits.append(hg_rocker_OBJ)
    if hg_japan_OBJ.purchased:
        $ wr_her_outfits.append("japan")
        $ hg_purchased_outfits.append(hg_japan_OBJ)

    #Costumes
    $ wr_her_costumes = []
    $ hg_purchased_costumes = []
    if hg_pirate_OBJ.purchased:
        $ wr_her_costumes.append("pirate")
        $ hg_purchased_costumes.append(hg_pirate_OBJ)
    if hg_powerGirl_OBJ.purchased:
        $ wr_her_costumes.append("power")
        $ hg_purchased_costumes.append(hg_powerGirl_OBJ)
    if hg_msMarvel_OBJ.purchased:
        $ wr_her_costumes.append("marvel")
        $ hg_purchased_costumes.append(hg_msMarvel_OBJ)
    if hg_harleyQuinn_OBJ.purchased:
        $ wr_her_costumes.append("harley")
        $ hg_purchased_costumes.append(hg_harleyQuinn_OBJ)
    if hg_laraCroft_OBJ.purchased:
        $ wr_her_costumes.append("lara")
        $ hg_purchased_costumes.append(hg_laraCroft_OBJ)
    if hg_tifa_OBJ.purchased:
        $ wr_her_costumes.append("tifa")
        $ hg_purchased_costumes.append(hg_tifa_OBJ)
    if hg_witch_OBJ.purchased:
        $ wr_her_costumes.append("witch")
        $ hg_purchased_costumes.append(hg_witch_OBJ)

    #One-Pieces
    $ wr_her_onepieces = []
    $ hg_purchased_onepieces = []
    if hg_silkNightgown_OBJ.purchased:
        $ wr_her_onepieces.append("nightgown")
        $ hg_purchased_onepieces.append(hg_silkNightgown_OBJ)

    #Swimsuits
    $ wr_her_swimsuits = []
    $ hg_purchased_swimsuits = []
    #if .purchased:
    #    $ wr_her_swimsuits.append("")
    #    $ hg_purchased_swimsuits.append()

    #Dresses
    $ wr_her_dresses = []
    $ hg_purchased_dresses = []
    if hg_heartDancer_OBJ.purchased:
        $ wr_her_dresses.append("heart")
        $ hg_purchased_dresses.append(hg_heartDancer_OBJ)
    if hg_ballDress_OBJ.purchased:
        $ wr_her_dresses.append("ball_dress")
        $ hg_purchased_dresses.append(hg_ballDress_OBJ)


    ###TATTOOS
    $ wr_tattoo_list = []

    ###Free tattoos
    $ wr_tattoo_list.append("thigh/signature")

    if whoring >= 10:
        $ wr_tattoo_list.append("torso/twist")
        $ wr_tattoo_list.append("thigh/tribal")

    if whoring >= 15:
        $ wr_tattoo_list.append("thigh/free")

    if whoring >= 17:
        $ wr_tattoo_list.append("pubic/10g_raised")
        $ wr_tattoo_list.append("pubic/10g")
        $ wr_tattoo_list.append("pubic/cock_hole")
        $ wr_tattoo_list.append("pubic/inheat")

    if whoring >= 21:
        $ wr_tattoo_list.append("pubic/deatheater")
        $ wr_tattoo_list.append("pubic/mudblood")
        $ wr_tattoo_list.append("pubic/fuck_me")
        $ wr_tattoo_list.append("pubic/deposit")

    if whoring >= 24:
        $ wr_tattoo_list.append("pubic/Cumslut")
        $ wr_tattoo_list.append("pubic/cum_here")
        $ wr_tattoo_list.append("pubic/cunt")
        $ wr_tattoo_list.append("pubic/mudblood")
        $ wr_tattoo_list.append("pubic/punk_mudblood")


    return
