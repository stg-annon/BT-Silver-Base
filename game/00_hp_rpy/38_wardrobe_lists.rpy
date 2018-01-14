

label update_wardrobe_lists:

### Hair Color ###
#    $ wr_her_haircolor = ["dye_1"]







### Tops ###
    $ wr_her_tops = ["1"] #Page MAX=25

    if whoring >= 3: #get right number
        $ wr_her_tops.append("2")
    if whoring >= 6: #get right number
        $ wr_her_tops.append("3")
    if whoring >= 9: #get right number
        $ wr_her_tops.append("4")
    if whoring >= 12: #get right number
        $ wr_her_tops.append("5")
    if whoring >= 18: #get right number
        $ wr_her_tops.append("6")


### Bottoms ###
    $ wr_her_bottoms = ["skirt_1"] #Page MAX=25

    ## Skirts ##
    if whoring >= 3: #get right number
        $ wr_her_bottoms.append("skirt_2")
    if whoring >= 6: #get right number
        $ wr_her_bottoms.append("skirt_3")
    if whoring >= 9: #get right number
        $ wr_her_bottoms.append("skirt_4")
    if whoring >= 12: #get right number
        $ wr_her_bottoms.append("skirt_5")
    #if micro_skirt unlocked/purchased:
    #    $ wr_her_bottoms.append("skirt_6") #micro skirt
    #ADD japan_pant

    ## Jeans ##
    if "jeans_long" in cs_existing_stock:
        $ wr_her_bottoms.append("jeans_long")
    if "jeans_short" in cs_existing_stock:
        $ wr_her_bottoms.append("jeans_short")
    #ADD rocker_skirt


### Stockings ###
    $ wr_her_stockings = []

    if "gryffindor_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("gryffindor_stockings")
    if "fishnet_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("fishnet_stockings")
    if "lace_stockings" in cs_existing_stock:
        $ wr_her_stockings.append("lace_stockings")


### Robes ###
    $ wr_her_robes = ["gryff_robe","gryff_robe_off"]
    if whoring >= 3:
        $ wr_her_robes.append("gryff_robe_shirt_none")
    if whoring >= 6:
        $ wr_her_robes.append("gryff_robe_gap_wide")
    if whoring >= 9:
        $ wr_her_robes.append("gryff_quidditch")


    if whoring >= 6:
        $ wr_her_robes.append("slyth_robe")
        $ wr_her_robes.append("slyth_robe_off")
        $ wr_her_robes.append("slyth_robe_shirt_none")
    if whoring >= 9:
        $ wr_her_robes.append("slyth_robe_gap_wide")
    if whoring >= 12:
        $ wr_her_robes.append("slyth_quidditch")




    return