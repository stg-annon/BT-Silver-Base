

label update_wardrobe_lists:

### Hair Color ###
    $ wr_her_haircolor = []

    if whoring >= 0:    #brown_dye#
        $ wr_her_haircolor.append("1")
    if whoring >= 6 and "blonde_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("2")
    if whoring >= 6 and "red_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("3")
    if whoring >= 9 and "crimson_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("4")
    if whoring >= 9 and "black_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("5")

    if whoring >= 12 and "green_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("6")
    if whoring >= 12 and "blue_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("7")
    if whoring >= 12 and "purple_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("8")
    if whoring >= 15 and "pink_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("9")
    if whoring >= 18 and "white_dye" in cs_existing_stock:
        $ wr_her_haircolor.append("10")


### Tops ###
    $ wr_her_tops_uniform = [] #ADD school clothing and cheerleader tops,...

    #Uniform
    if whoring >= 0:
        $ wr_her_tops_uniform.append("uni_top_1")
    if whoring >= 4: #get right number
        $ wr_her_tops_uniform.append("uni_top_2")
    if whoring >= 7: #get right number
        $ wr_her_tops_uniform.append("uni_top_3")
    if whoring >= 10: #get right number
        $ wr_her_tops_uniform.append("uni_top_4")
    if whoring >= 13: #get right number
        $ wr_her_tops_uniform.append("uni_top_5")
    if whoring >=19:
        $ wr_her_tops_uniform.append("uni_top_6")
        $ wr_her_tops_uniform.remove("uni_top_3") #remove shirt 3. Looks ugly, no point in having it when she's willing to wear shirt 4.

    if whoring >= 4 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_gryff")
    if whoring >= 7 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_tops_uniform.append("uni_top_cheer_gryff_skimpy")

    if whoring >= 10 and hg_slythCheer_OBJ.purchased: #Add sQuest: Slytherin at heart unlock.
        $ wr_her_tops_uniform.append("uni_top_cheer_slyth")
        $ wr_her_tops_uniform.append("uni_top_cheer_slyth_skimpy")

    #Fancy
    $ wr_her_tops_fancy = []  #ADD sexy clothing
    if whoring >= 7 and "fancy_waitress_beige" in cs_existing_stock:
        $ wr_her_tops_fancy.append("fancy_waitress_beige")
    if whoring >= 10 and "fancy_waitress_green" in cs_existing_stock:
        $ wr_her_tops_fancy.append("fancy_waitress_green")

    #Wicked
    $ wr_her_tops_wicked = [] #ADD kinky clothing items like leather, fishnet
    if whoring >= 19 and "wicked_leather_jacket_short_sleeves" in cs_existing_stock:
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_short_sleeves_open")
    if whoring >= 19 and "wicked_leather_jacket_sleeveless" in cs_existing_stock:
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeveless_open")
    if whoring >= 19 and "wicked_leather_jacket_sleeves" in cs_existing_stock:
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves")
        $ wr_her_tops_wicked.append("wicked_leather_jacket_sleeves_open")

    if whoring >= 22 and hg_rocker_OBJ.purchased:
        $ wr_her_tops_wicked.append("wicked_rocker_top")

    #Muggle
    $ wr_her_tops_normal = [] #ADD Pullovers, Sweaters, Shirts, Muggle Clothing
    if whoring >= 4 and "normal_pullover" in cs_existing_stock:
        $ wr_her_tops_normal.append("normal_pullover")
        $ wr_her_tops_normal.append("normal_pullover_sexy")
    if whoring >= 7 and "normal_purple_sweater" in cs_existing_stock:
        $ wr_her_tops_normal.append("normal_purple_sweater")

    #Misc. Tops
    $ wr_her_tops_misc = []   #ADD Misc top items
    if whoring >= 10: #get right number
        $ wr_her_tops_misc.append("top_banner_gryff")
    if whoring >= 13: #get right number
        $ wr_her_tops_misc.append("top_shirt_gryff_ripped_long_tie")
        $ wr_her_tops_misc.append("top_tie_gryff")
        $ wr_her_tops_misc.append("top_banner_slyth")
    if whoring >= 19 and "top_fishnets" in cs_existing_stock:
        $ wr_her_tops_misc.append("top_fishnets")


### Bottoms ###
    $ wr_her_bottoms_uniform = [] #Page MAX=25

    #Uniform
    if whoring >= 0:
        $ wr_her_bottoms_uniform.append("uni_skirt_1")
    if whoring >= 4: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_2")
    if whoring >= 10: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_3")
    if whoring >= 16: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_4")
    if whoring >= 19: #get right number
        $ wr_her_bottoms_uniform.append("uni_skirt_5")

    if whoring >= 4 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_bottoms_uniform.append("uni_skirt_cheer_gryff")
    if whoring >= 10 and hg_slythCheer_OBJ.purchased: #Add sQuest: Slytherin at heart unlock.
        $ wr_her_bottoms_uniform.append("uni_skirt_cheer_slyth")

    #Uniform Low
    $ wr_her_bottoms_uniform_low = []  #Add low hanging school skirts

    if whoring >= 0:
        $ wr_her_bottoms_uniform_low.append("uni_skirt_1_low")
    if whoring >= 7:
        $ wr_her_bottoms_uniform_low.append("uni_skirt_2_low")
    if whoring >= 16: #shows panties
        $ wr_her_bottoms_uniform_low.append("uni_skirt_3_low")
    #if micro_skirt unlocked/purchased:
    #    $ wr_her_bottoms_uniform_low.append("uni_skirt_4_low") #micro skirt

    #Skirts
    $ wr_her_bottoms_skirts = [] #Add skirts
    if whoring >= 10 and "skirt_belted_mini" in cs_existing_stock:
        $ wr_her_bottoms_skirts.append("skirt_belted_mini")
    if whoring >= 19 and "skirt_belted_micro" in cs_existing_stock:
        $ wr_her_bottoms_skirts.append("skirt_belted_micro")
    #ADD japan_pant

    #Pants
    $ wr_her_bottoms_pants = [] #Add

    if "pants_jeans_long" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_jeans_long")
    if "pants_jeans_short" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_jeans_short")
    if whoring >= 19 and "pants_retro_shorts" in cs_existing_stock:
        $ wr_her_bottoms_pants.append("pants_retro_shorts")
    if whoring >= 22 and hg_rocker_OBJ.purchased:
        $ wr_her_bottoms_pants.append("pants_rocker")

    #Bottoms Misc
    $ wr_her_bottoms_misc = []   #ADD Misc bottom items

### Other Clothings ###

    #Neckwear
    $ wr_her_neckwears = []

    if whoring >= 0:
        $ wr_her_neckwears.append("neck_scarf_gryff")
    if whoring >= 4:
        $ wr_her_neckwears.append("neck_tie_gryff")
    if whoring >= 10:
        $ wr_her_neckwears.append("neck_leather_collar")
    if whoring >= 19:
        $ wr_her_neckwears.append("neck_bondage_collar")

    if whoring >= 7 and hg_ballDress_OBJ.purchased:
        $ wr_her_neckwears.append("neck_pearl_necklace")
    if whoring >= 16 and hg_christmas_OBJ.purchased:
        $ wr_her_neckwears.append("neck_xmas")

    #$ wr_her_neckwears.append("neck_miss_hogwarts") #mQuest reward (after end of game)
    #$ wr_her_neckwears.append("neck_goggles") #sQuest reward
    if collar == 1:
        $ wr_her_neckwears.append("neck_slave_shackle") #sQuest collar reward
    if collar == 2:
        $ wr_her_neckwears.append("neck_slut_shackle") #sQuest collar reward
    if collar == 3:
        $ wr_her_neckwears.append("neck_whore_shackle") #sQuest collar reward

    #Belts
    $ wr_her_belts = []

    if whoring >= 0:
        $ wr_her_belts.append("belt_scarf_gryff")
    if whoring >= 24:
        $ wr_her_belts.append("belt_band_of_condoms")

    #Gloves
    $ wr_her_gloves = []

    if whoring >= 0:
        $ wr_her_gloves.append("gloves_gryff")
    if whoring >= 10:
        $ wr_her_gloves.append("gloves_lace_white")
    if whoring >= 19:
        $ wr_her_gloves.append("gloves_latex_black")

    if whoring >= 4 and hg_christmas_OBJ.purchased:
        $ wr_her_gloves.append("gloves_xmas_red")
    if whoring >= 13 and hg_maid_OBJ.purchased:
        $ wr_her_gloves.append("gloves_french_maid")
    if whoring >= 13 and hg_laraCroft_OBJ.purchased:
        $ wr_her_gloves.append("gloves_treasure_hunter")
    if whoring >= 19 and hg_powerGirl_OBJ.purchased:
        $ wr_her_gloves.append("gloves_latex_hero_blue")
    if whoring >= 22 and hg_harleyQuinn_OBJ.purchased:
        $ wr_her_gloves.append("gloves_leather_red")
    #$ wr_her_gloves.append("gloves_egyptian") #ADD Egypt Outfit

    #Stockings
    $ wr_her_stockings = []

    if "stockings_gryff" in cs_existing_stock:
        $ wr_her_stockings.append("stockings_gryff")
        #if whoring  >= 22 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_gryff_vibe") #Will be in accessories instead
    if whoring >= 7 and hg_gryffCheer_OBJ.purchased:
        $ wr_her_stockings.append("stockings_gryff_cheer")
        $ wr_her_stockings.append("stockings_gryff_cheer_short")
        #if whoring  >= 22 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_gryff_cheer_vibe") #Will be in accessories instead

    if whoring >= 10 and "stockings_slyth" in cs_existing_stock: #Add sQuest: Slytherin at heart unlock.
        $ wr_her_stockings.append("stockings_slyth")
        #if whoring  >= 22 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_slyth_vibe") #Will be in accessories instead
    if whoring >= 9 and hg_slythCheer_OBJ.purchased:
        $ wr_her_stockings.append("stockings_slyth_cheer")
        $ wr_her_stockings.append("stockings_slyth_cheer_short")
        #if whoring  >= 22 and "vibrators" in cs_existing_stock:
        #    $ wr_her_stockings.append("stockings_slyth_cheer_vibe") #Will be in accessories instead
    #ADD Ravenclaw Blue. And maybe Hufflepuff.


    if whoring >= 7:
        $ wr_her_stockings.append("stockings_pantyhose_tan")
        $ wr_her_stockings.append("stockings_pantyhose_grey")
    if whoring >= 16:
        $ wr_her_stockings.append("stockings_black")
        $ wr_her_stockings.append("stockings_white")
    if whoring >= 19:
        $ wr_her_stockings.append("stockings_latex_black")

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


    if whoring >= 10:
        $ wr_her_robes.append("slyth_robe_shirt_none")
        $ wr_her_robes.append("slyth_robe_off")
        $ wr_her_robes.append("slyth_robe_gap_wide")
    if whoring >= 13:
        $ wr_her_robes.append("slyth_robe_seethrough")
    if whoring >= 16:
        $ wr_her_robes.append("slyth_quidditch")


### Underwear ###
    #Bra
    $ wr_her_bras = []

    if whoring >= 10:
        $ wr_her_bras.append("bra_white")
        $ wr_her_bras.append("bra_silk_black")
        $ wr_her_bras.append("bra_lace_turquoise")

    if whoring >= 16:
        $ wr_her_bras.append("bra_bikini_string_blue")
        $ wr_her_bras.append("bra_bikini_string_black")

    if whoring >= 19:
        $ wr_her_bras.append("bra_french_maid")
        $ wr_her_bras.append("bra_leather_black")

    #Panties
    $ wr_her_panties = []

    if whoring >= 10:
        $ wr_her_panties.append("panties_white")
        $ wr_her_panties.append("panties_silk_black")
        $ wr_her_panties.append("panties_lace_turquoise")

    if whoring >= 16:
        $ wr_her_panties.append("panties_stringbikini_blue")
        $ wr_her_panties.append("panties_bikini_string_black")
        $ wr_her_panties.append("panties_latex_black")

    if whoring >= 19:
        $ wr_her_panties.append("panties_french_maid")
        $ wr_her_panties.append("panties_fishnet_gstring")

    #Corsets
    $ wr_her_corsets = []

    if whoring >= 19: #and "corset_black" in cs_existing_stock:
        $ wr_her_corsets.append("corset_black")

    #Garterbelts
    $ wr_her_garterbelts = []

    if whoring >= 10: #and "garterbelt_lace_black" in cs_existing_stock:
        $ wr_her_garterbelts.append("garterbelt_lace_black")

    #Underwear Misc.
    $ wr_her_bra_misc = []

    if whoring >= 19:
        $ wr_her_bra_misc.append("underwear_misc_seethru_bandeau")
    if whoring >= 22:
        $ wr_her_bra_misc.append("underwear_misc_insulating_tape")
    if whoring >= 22 and "top_fishnets" in cs_existing_stock:
        $ wr_her_bra_misc.append("top_fishnets")

    $ wr_her_panties_misc = []


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
    $ wr_her_tattoo_list = []

    ###Free tattoos
    $ wr_her_tattoo_list.append("thigh/signature")

    if whoring >= 10:
        $ wr_her_tattoo_list.append("torso/twist")
        $ wr_her_tattoo_list.append("thigh/tribal")

    if whoring >= 15:
        $ wr_her_tattoo_list.append("thigh/free")

    if whoring >= 17:
        $ wr_her_tattoo_list.append("pubic/10g_raised")
        $ wr_her_tattoo_list.append("pubic/10g")
        $ wr_her_tattoo_list.append("pubic/cock_hole")
        $ wr_her_tattoo_list.append("pubic/inheat")

    if whoring >= 21:
        $ wr_her_tattoo_list.append("pubic/deatheater")
        $ wr_her_tattoo_list.append("pubic/mudblood")
        $ wr_her_tattoo_list.append("pubic/fuck_me")
        $ wr_her_tattoo_list.append("pubic/deposit")

    if whoring >= 24:
        $ wr_her_tattoo_list.append("pubic/Cumslut")
        $ wr_her_tattoo_list.append("pubic/cum_here")
        $ wr_her_tattoo_list.append("pubic/cunt")
        $ wr_her_tattoo_list.append("pubic/mudblood")
        $ wr_her_tattoo_list.append("pubic/punk_mudblood")


    return
