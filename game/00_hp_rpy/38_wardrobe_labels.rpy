
label __init_variables:

    if not hasattr(renpy.store,'wardrobe_active'): #important!
        $ wardrobe_active = 0

    if not hasattr(renpy.store,'wardrobe_page'): #important!
        $ wardrobe_page = 0

    if not hasattr(renpy.store,'wardrobe_accessories_category'): #important!
        $ wardrobe_accessories_category = 0

    if not hasattr(renpy.store,'wardrobe_gifts_category'): #important!
        $ wardrobe_gifts_category = 0

    return


label reset_wardrobe_vars:
    $ wardrobe_active = 1                 #1=True #hides dissolve from "her_main"
    $ wardrobe_page = 0                   #default page
    $ wardrobe_accessories_category = 0   #default page
    $ wardrobe_gifts_category = 0         #default page
    return


label close_wardrobe:
    $ hermione_xpos = 510 #Hermione position reset when closing inventory.
    call her_main("","body_01") #reset hermione face to default
    jump day_time_requests


### Hair ###
label change_her_hair():
    call set_her_hair(wardrobe_hair_style,wardrobe_hair_color)
    call screen wardrobe

label set_her_hair(hair_style="A", color=1):
    hide screen hermione_main
    $ h_hair_style = hair_style
    $ h_hair_color = color
    call update_her_hair                     #Hermione_layering.rpy
    show screen hermione_main
    return
    
label set_h_hair_style(hair_style = "A"):
    hide screen hermione_main
    $ h_hair_style = hair_style
    call update_her_hair                     #Hermione_layering.rpy
    show screen hermione_main
    return
    
label set_h_hair_color(hair_color = 1):
    hide screen hermione_main
    $ h_hair_color = hair_color
    call update_her_hair                     #Hermione_layering.rpy
    show screen hermione_main
    return

label update_her_hair:
    if hermione_costume and hermoine_outfit_GLBL.hair_layer != "":
        $ hermione_hair_a = "01_hp/13_characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+".png"
        $ hermione_hair_b = "01_hp/13_characters/hermione/clothes/custom/"+hermoine_outfit_GLBL.hair_layer+"_2.png"
    else:
        $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+".png"
        $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/"+str(h_hair_style)+"_"+str(h_hair_color)+"_2.png"
    return


### Toggles ##

## Tops ##

# Top Toggle #
label her_top_toggle:
    hide screen hermione_main
    if hermione_wear_top:
        $ hermione_wear_top = False
    else:
        $ hermione_wear_top = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

## Bottoms ##

# Bottom Toggle #
label her_bottom_toggle:
    hide screen hermione_main
    if hermione_wear_skirt: #rename "skirt" to "bottom"
        $ hermione_wear_skirt = False
    else:
        $ hermione_wear_skirt = True
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe


## Stockings ##

# Stockings Toggle #
label her_stockings_toggle:
    hide screen hermione_main
    if h_stocking == "00_blank": #rename
        $ h_stocking = "gryff"
    else:
        $ h_stocking = "00_blank"
    call update_her_uniform
    show screen hermione_main
    call screen wardrobe

# Stockings Selection #
label wardrobe_wear_stockings:
    call set_h_stockings(wr_her_stockings_choice)
    
    hide screen wardrobe
    call screen wardrobe

label set_h_stockings(stocking = "00_blank"):
    hide screen hermione_main
    if stocking == h_stocking:
        $ h_stocking = "00_blank"
    else:
        $ h_stocking = stocking
    call update_her_uniform
    show screen hermione_main
    return


## Accessories ##

# Accessories Toggle # 
# ADD Toggles

# Accessories Selection #
label wardrobe_give_acc:
    call give_her_acc(wardrobe_acc_item)
    hide screen wardrobe
    call screen wardrobe


## Robes ##

# Robe Toggle #
label her_robe_toggle:
    hide screen hermione_main
    if hermione_wear_robe:
        $ hermione_wear_robe = False
    else:
        $ hermione_wear_robe = True
    call update_her_uniform
    show screen hermione_main
    hide screen wardrobe
    call screen wardrobe 

# Robe Selection #
label wardrobe_wear_robe:
    if hermione_wear_robe:
        $ hermione_wear_robe = False
    else:
        $ hermione_wear_robe = True
    call set_h_robe(wr_her_robe)
    hide screen wardrobe
    call screen wardrobe

label set_h_robe(hermione_robe = "00_blank"):
    hide screen hermione_main
    call update_her_uniform
    show screen hermione_main
    return


## Underwear ##

# Bra Toggle #
label her_bra_toggle:
    hide screen hermione_main
    if hermione_wear_bra: #Toggle OFF
        $ hermione_wear_bra = False
        call update_her_uniform
        if whoring >= 15 and whoring < 18:      #level 6
            call her_main_rndm_annoyed_wBlush
        elif whoring >= 18 and whoring < 21:    #level 7
            call her_main_rndm_naughty_wBlush
        else:                                   #level 8
            call her_main_rndm_naughty
    else: #Toggle ON
        $ hermione_wear_bra = True
        call update_her_uniform
        if whoring >= 15 and whoring < 18:      #level 6
            call her_main_rndm_annoyed
        elif whoring >= 18 and whoring < 21:    #level 7
            call her_main_rndm_neutral
        else:                                   #level 8
            call her_main_rndm_happy
    hide screen wardrobe
    call screen wardrobe

# Panties Toggle #
label her_panties_toggle:
    hide screen hermione_main
    if hermione_wear_panties:
        $ hermione_wear_panties = False
    else:
        $ hermione_wear_panties = True
    call update_her_uniform
    show screen hermione_main
    hide screen wardrobe
    call screen wardrobe

# Underwear Selection #
label wardrobe_wear_underwear:
    call set_h_underwear(wr_her_stockings)
    hide screen underwear
    call screen underwear

label set_h_underwear(bra="base_bra_white_1", panties="base_panties_1"):
    hide screen hermione_main
    $ h_bra = bra
    $ h_panties = panties
    call update_her_uniform
    show screen hermione_main
    return


## Outfits ##

# Outfit Toggle #
label her_outfit_toggle:
    hide screen hermione_main
    if wardrobe_costume_selection:
        $ wardrobe_costume_selection = False
    else:
        $ wardrobe_costume_selection = True
    call update_her_uniform
    show screen hermione_main
    hide screen wardrobe
    call screen wardrobe 

# Outfit Selection #
label wardrobe_wear_costume:
    hide screen hermione_main
    call h_outfit_OBJ(wardrobe_costume_selection)
    show screen hermione_main
    hide screen wardrobe
    call screen wardrobe
    
label change_uniform:
    call equip_bot(wardrobe_tops_selection) #37_clothing_events.rpy
    hide screen wardrobe
    call screen wardrobe


## Gifts ##

# Gifts Selection #
label wardrobe_give_gift:
    call give_her_gift(wardrobe_gift_item)
    hide screen wardrobe
    call screen wardrobe

# Potions Selection #
label wardrobe_give_potion:
    hide screen wardrobe_gifts
    $ renpy.jump("potion_scene_"+str(wardrobe_potion))