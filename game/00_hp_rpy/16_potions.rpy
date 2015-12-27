label declare_potion_vars:
    
    $ p_base = ["Polyjuice Potion", "Expanding Elixir", "Moreish Mead", "Transparent Tincture", "Coloring Concoction"] #base potion names
    $ p_items = ["Wormwood", "Knotgrass", "Root of Aconite", "Niffler's fancy", "Cat Hair", "Luna's Hair", "Basilisk Scale"] #item names
    
    
    #v==SAVE THIS==v#
    $ p_inv = ["Wormwood","Wormwood","Wormwood","Wormwood","Moreish Mead","Moreish Mead","Moreish Mead","Moreish Mead","Moreish Mead"] #filled with testing items
    #^==SAVE THIS==^#
    
    #$ p_inv.remove("ITEM") to remove an item
    
    $ p_potion_names = []
    $ p_potion_names.append("Cum Addiction Potion")
    $ p_potion_names.append("Ass Expansion Potion")
    $ p_potion_names.append("Breast Expansion Potion")
    $ p_potion_names.append("Cat Transformation Potion")
    $ p_potion_names.append("Luna Transformation Potion")
    $ p_potion_names.append("Lamia Transformation Potion")
    $ p_potion_names.append("Transparency Potion")
    
    
    $ p_cum_addiction = ["Wormwood","Moreish Mead"]
    $ p_ass_expansion = ["Knotgrass","Expanding Elixir"]
    $ p_breast_expansion = ["Root of Aconite","Expanding Elixir"]
    $ p_cat_transformation = ["Cat Hair","Polyjuice Potion"]
    $ p_luna_transformation = ["Luna's Hair","Polyjuice Potion"]
    $ p_lamia_transformation = ["Basilisk Scale","Polyjuice Potion"]
    $ p_transparency = ["Niffler's fancy","Transparent Tincture"]
    
    $ p_ingredients = [[0 for i in xrange(3)] for i in xrange(8)]
    $ p_ingredients[0] = ["Wormwood","Moreish Mead"]
    $ p_ingredients[1] = ["Knotgrass","Expanding Elixir"]
    $ p_ingredients[2] = ["Root of Aconite","Expanding Elixir"]
    $ p_ingredients[3] = ["Cat Hair","Polyjuice Potion"]
    $ p_ingredients[4] = ["Luna's Hair","Polyjuice Potion"]
    $ p_ingredients[5] = ["Basilisk Scale","Polyjuice Potion"]
    $ p_ingredients[6] = ["Niffler's fancy","Transparent Tincture"]
    
return

label potion_menu:
    menu:
        "-craft: \"[p_potion_names[0]]\"-" if set(p_cum_addiction).issubset(set(p_inv)):
            ">You mix the {i}[p_cum_addiction[0]]{/i} with the {i}[p_cum_addiction[1]]{/i}"
            ">...but it's missing the most important part."
            menu:
                "-Cum into the Potion-":
                    #add jerk_off here at some point
                    ">you cum into the potion"
                    ">You received the item: \"[p_potion_names[0]]\"."
                    $ p_inv.remove(p_cum_addiction[0])
                    $ p_inv.remove(p_cum_addiction[1])
                    $ p_inv.append(p_potion_names[0])
                    jump potion_menu
        "{color=#858585}-craft: \"[p_potion_names[0]]\"-{/color}" if not set(p_cum_addiction).issubset(set(p_inv)):
            call p_lack_materials(0)
            jump potion_menu
        
        "-craft: \"[p_potion_names[1]]\"-" if set(p_ass_expansion).issubset(set(p_inv)):
            ">You mix the {i}[p_ass_expansion[0]]{/i} with the {i}[p_ass_expansion[1]]{/i}"
            ">You received the item: \"[p_potion_names[1]]\"."
            $ p_inv.remove(p_ass_expansion[0])
            $ p_inv.remove(p_ass_expansion[1])
            $ p_inv.append(p_potion_names[1])
            jump potion_menu
        "{color=#858585}-craft: \"[p_potion_names[1]]\"-{/color}" if not set(p_ass_expansion).issubset(set(p_inv)):
            call p_lack_materials(1)
            jump potion_menu
        
        "-craft: \"[p_potion_names[2]]\"-" if set(p_breast_expansion).issubset(set(p_inv)):
            ">You mix the {i}[p_breast_expansion[0]]{/i} with the {i}[p_breast_expansion[1]]{/i}"
            ">You received the item: \"[p_potion_names[2]]\"."
            $ p_inv.remove(p_breast_expansion[0])
            $ p_inv.remove(p_breast_expansion[1])
            $ p_inv.append(p_potion_names[2])
        "{color=#858585}-craft: \"[p_potion_names[2]]\"-{/color}" if not set(p_breast_expansion).issubset(set(p_inv)):
            call p_lack_materials(2)
            jump potion_menu
        
        "-craft: \"[p_potion_names[3]]\"-" if set(p_cat_transformation).issubset(set(p_inv)):
            ">You mix the {i}[p_cat_transformation[0]]{/i} with the {i}[p_cat_transformation[1]]{/i}"
            ">You received the item: \"[p_potion_names[3]]\"."
            $ p_inv.remove(p_cat_transformation[0])
            $ p_inv.remove(p_cat_transformation[1])
            $ p_inv.append(p_potion_names[3])
        "{color=#858585}-craft: \"[p_potion_names[3]]\"-{/color}" if not set(p_cat_transformation).issubset(set(p_inv)):
            call p_lack_materials(3)
            jump potion_menu
        
        "-craft: \"[p_potion_names[4]]-" if set(p_luna_transformation).issubset(set(p_inv)):
            ">You mix the {i}[p_luna_transformation[0]]{/i} with the {i}[p_luna_transformation[1]]{/i}"
            ">You received the item: \"[p_potion_names[4]]\"."
            $ p_inv.remove(p_luna_transformation[0])
            $ p_inv.remove(p_luna_transformation[1])
            $ p_inv.append(p_potion_names[4])
        "{color=#858585}-craft: \"[p_potion_names[4]]\"-{/color}" if not set(p_luna_transformation).issubset(set(p_inv)):
            call p_lack_materials(4)
            jump potion_menu
        
        "-craft: \"[p_potion_names[5]]-" if set(p_lamia_transformation).issubset(set(p_inv)):
            ">You mix the {i}[p_lamia_transformation[0]]{/i} with the {i}[p_lamia_transformation[1]]{/i}"
            ">You received the item: \"[p_potion_names[5]]\"."
            $ p_inv.remove(p_lamia_transformation[0])
            $ p_inv.remove(p_lamia_transformation[1])
            $ p_inv.append(p_potion_names[5])
        "{color=#858585}-craft: \"[p_potion_names[5]]\"-{/color}" if not set(p_lamia_transformation).issubset(set(p_inv)):
            call p_lack_materials(5)
            jump potion_menu
        
        "-craft: \"[p_potion_names[6]]-" if set(p_transparency).issubset(set(p_inv)):
            ">You mix the {i}[p_transparency[0]]{/i} with the {i}[p_transparency[1]]{/i}"
            ">You received the item: \"[p_potion_names[6]]\"."
            $ p_inv.remove(p_transparency[0])
            $ p_inv.remove(p_transparency[1])
            $ p_inv.append(p_potion_names[6])
        "{color=#858585}-craft: \"[p_potion_names[6]]\"-{/color}" if not set(p_transparency).issubset(set(p_inv)):
            call p_lack_materials(6)
            jump potion_menu
        "-Never mind-":
            jump cupboard
        
        # "-craft: \"[p_potion_names[POT_INDEX_HERE]]\"-" if set(POT_ARRAY_HERE).issubset(set(p_inv)):
            # ">You mix the {i}[POT_ARRAY_HERE[0]]{/i} with the {i}[POT_ARRAY_HERE[1]]{/i}"
            # ">You received the item: \"[p_potion_names[POT_INDEX_HERE]]\"."
            # $ p_inv.remove(POT_ARRAY_HERE[0])
            # $ p_inv.remove(POT_ARRAY_HERE[1])
            # $ p_inv.append(p_potion_names[POT_INDEX_HERE])
        # "{color=#858585}-craft: \"[p_potion_names[POT_INDEX_HERE]]\"-{/color}" if not set(POT_ARRAY_HERE).issubset(set(p_inv)):
            # call p_lack_materials(POT_INDEX_HERE)
            # jump potion_menu
        
        
label p_lack_materials(potion_id):
    show screen blktone8
    ">You lack the required materials to make this."
    $ tmp_str = "You need {size=+5}{b}"+str(p_ingredients[potion_id][0])+"{/b}{/size} and {size=+5}{b}"+str(p_ingredients[potion_id][1])+"{/b}{/size} to craft this"
    ">[tmp_str]"
    hide screen blktone8
    return
    

    #base potions:
    # Polyjuice potion (Luna, Cat, Lamia)
    # Expanding Elixir (Breast, Ass)
    # Moreish mead (cum)
    # Transparent tincture (Transparency potion)
    # Coloring concoction (hair colors)
    
    # Cum addiction = Moreish mead? + wormwood + your cum
    # Ass expansion = Expanding Elixir + knotgrass
    # Breast expansion = Expanding Elixir + Root of aconite
    # Cat potion = Polyjuice + Cat hair
    # Luna potion = Polyjuice + Luna's hair
    # Lamia potion = Polyjuice + Basilisk scale
    # Transparency potion = Transparent tincture + Niffler's fancy
    
    # Cum addiction: wormwood+your cum (jerk off into it)
    # Ass expansion: knotgrass
    # Breast expansion: Root of aconite
    # Luna potion: Luna's hair
    # Transparency potion:  Niffler's fancy
    # Lamia potion: Basilisk scale

    
    # wormwood = forbidden forest
    # knotgrass = ?
    # root_of_aconite =?
    # cat_hair
    # luna_hair = brush from room?
    # basilisk_scale = ?