label __init_variables:

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


    # all the metadata for the objects is stored statically any information
    # that needs to be persistent is stored in a separate known dict value
    $ potion_lib = potion_item_library(
        lib = [
            potion_ingredient(
                id = "ing_wormwood",
                name = "Wormwood",
                effect = "",
                description = "Wormwood is sometimes found in the forbidden forest.",
                picture = ""
            ),
            potion_ingredient(
                id = "ing_knotgrass",
                name = "Knotgrass",
                effect = "",
                description = "You can sometimes find Knotgrass by the forbidden forest.",
                picture = ""
            ),
            potion_ingredient(
                id = "ing_aconite_root",
                name = "Root of Aconite",
                effect = "",
                description = "Root of Aconite can be found down by the lake.",
                picture = ""
            ),
            potion_ingredient(
                id = "ing_niffler_fancy",
                name = "Niffler's fancy",
                effect = "",
                description = "Hmm... I think I heard that it's found by the lake.",
                picture = ""
            ),
            potion_ingredient(
                id = "ing_luna_hair",
                name = "Luna's Hair",
                effect = "",
                description = "The hair of Luna Lovegood.",
                picture = ""
            ),
            potion_ingredient(
                id = "ing_cat_hair",
                name = "Cat Hair",
                effect = "",
                description = "The hair of a common cat.",
                picture = ""
            ),
            potion_ingredient(
                id = "ing_basilisk_scale",
                name = "Basilisk Scale",
                effect = "",
                description = "The scale of what appears to be a large snake.",
                picture = ""
            ),


            silver_potion(
                id = "p_transparent_tincture",
                cost = 20,
                whoring_rec = 3,
                name = "Transparent Tincture",
                effect = "",
                description = ""
            ),
            silver_potion(
                id = "p_polyjuice_potion",
                cost = 40,
                whoring_rec = 5,
                name = "Polyjuice Potion",
                effect = "",
                description = ""
            ),
            silver_potion(
                id = "p_expanding_elixir",
                cost = 30,
                whoring_rec = 8,
                name = "Expanding Elixir",
                effect = "",
                description = ""
            ),
            silver_potion(
                id = "p_imperius_potation",
                cost = 45,
                whoring_rec = 14,
                name = "Imperius Potation",
                effect = "",
                description = ""
            ),
            silver_potion(
                id = "p_moreish_mead",
                cost = 60,
                whoring_rec = 14,
                name = "Moreish Mead",
                effect = "",
                description = ""
            ),

            silver_potion(
                id = "p_cum_addiction",
                ingredients = ["ing_wormwood","p_moreish_mead"],
                name = "Cum Addiction Potion",
                effect = "Cum Addiction",
                start_label = "potion_scene_3",
                description = ""
            ),
            silver_potion(
                id = "p_ass_expansion",
                ingredients = ["ing_knotgrass","p_expanding_elixir"],
                name = "Ass Expansion Potion",
                effect = "Ass Expansion",
                start_label = "potion_scene_2_2",
                description = ""
            ),
            silver_potion(
                id = "p_breast_expansion",
                ingredients = ["ing_aconite_root","p_expanding_elixir"],
                name = "Breast Expansion Potion",
                effect = "Breast Expansion",
                start_label = "potion_scene_2_1",
                description = ""
            ),
            silver_potion(
                id = "p_cat_transformation",
                ingredients = ["ing_cat_hair","p_polyjuice_potion"],
                name = "Cat Transformation Potion",
                effect = "Cat Ears",
                start_label = "potion_scene_1",
                description = ""
            ),
            silver_potion(
                id = "p_luna_transformation",
                ingredients = ["ing_luna_hair","p_polyjuice_potion"],
                name = "Luna Transformation Potion",
                effect = "Luna Potion",
                start_label = "potion_scene_6",
                description = ""
            ),
            silver_potion(
                id = "p_lamia_transformation",
                ingredients = ["ing_basilisk_scale","p_polyjuice_potion"],
                name = "Lamia Transformation Potion",
                start_label = "potion_scene_5",
                effect = "Snek",
                description = ""
            ),
            silver_potion(
                id = "p_transparency",
                ingredients = ["ing_niffler_fancy","p_transparent_tincture"],
                name = "Transparency Potion",
                effect = "Transparent Clothes",
                start_label = "potion_scene_4",
                description = ""
            ),
            silver_potion(
                id = "p_hypno",
                ingredients = ["ing_aconite_root","p_imperius_potation"],
                name = "Hypno Potion",
                effect = "Hypno Potion",
                start_label = "potion_scene_8",
                description = ""
            ),
            silver_potion(
                id = "p_clone",
                ingredients = ["p_polyjuice_potion","p_imperius_potation"],
                name = "Clone Potion",
                effect = "Clone Potion",
                start_label = "potion_scene_9",
                description = ""
            ),


            silver_potion(
                id = "p_milk_potion",
                name = "Lactantium",
                effect = "Lactantium",
                start_label = "potion_scene_11",
                description = ""
            ),
            silver_potion(
                id = "p_veritaserum",
                name = "Veritaserum",
                effect = "",
                description = ""
            ),
            silver_potion(
                id = "p_voluptatem",
                name = "Voluptatem",
                effect = "Voluptatem",
                start_label = "potion_scene_7",
                description = ""
            )
        ]
    )


    $ potion_inv = player_potion_invintory()
    if not hasattr(renpy.store,'p_inv'): #important!
        $ p_inv = {} # this stores the id and quantity of items the player has persistently

    return



label potion_menu:
    python:
        potion_menu = []
        for potion in potion_lib.getCraftable():
            if potion_inv.canCraft(potion):
                potion_menu.append((potion.getCraftingMenu(),potion))
            else:
                potion_menu.append((potion.getMissingIngMenu(),potion.ingredients))
        potion_menu.append(("-Never mind-", "nvm"))
        PotionOBJ = renpy.display_menu(potion_menu)
    if PotionOBJ == "nvm":
        jump cupboard
    elif isinstance(PotionOBJ, silver_potion):
        $ renpy.say( None, PotionOBJ.getMixingMsg() )
        if PotionOBJ.id == "p_cum_addiction":
            ">...but it's missing the most important part."
            menu:
                "-Cum into the Potion-":
                    # TODO: add jerk_off here at some point
                    ">you cum into the potion"
        $ renpy.say(None,">You received the item: \""+PotionOBJ.name+"\".")
        python:
            for ingredient in PotionOBJ.ingredients:
                potion_inv.remove(ingredient)
        $ potion_inv.add(PotionOBJ.id)
    else:
        show screen blktone8
        ">You lack the required materials to make this."
        $ missing_items = []
        $ tmp_txt = "You still need "
        python:
            for item in PotionOBJ:
                if not potion_inv.has(item):
                    missing_items.append(item)
            for i in range(len(missing_items)):
                tmp_txt += "{size=+5}{b}"+potion_lib.getName(missing_items[i])+"{/b}{/size}"
                if len(missing_items) > 1:
                    if i < len(missing_items)-2:
                        tmp_txt += ", "
                    if i == len(missing_items)-2:
                        tmp_txt += " and "
        $ tmp_txt += " to craft this"
        $ renpy.say(None, tmp_txt)
        #$ renpy.say(None,"You need {size=+5}{b}"+potion_lib.getName(PotionOBJ[0])+"{/b}{/size} and {size=+5}{b}"+potion_lib.getName(PotionOBJ[1])+"{/b}{/size} to craft this")
        hide screen blktone8
    jump potion_menu


init python:
    
    class silver_potion_obj(object):
        id = ""

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def __repr__(self):
            return self.id
        
        def __eq__(self, other):
            if isinstance(other, self.__class__): 
                return self.id == other.id
            else:
                return False
        def __ne__(self, other):
            return not self.__eq__(other)

    class silver_potion(silver_potion_obj):
        id = ""
        cost = 0
        ingredients = []
        name = ""
        effect = ""
        description = ""
        picture = ""
        whoring_rec = 0
        start_label = None

        def getStoreMenuText(self):
            return "-"+self.name+"- ("+self.cost+" g.)"
        def getFailBuyRecMenu(self):
            return "{color=#858585}-"+self.name+"- ("+self.cost+" g.){/color}"
        def getMissingIngMenu(self):
            return "{color=#858585}-craft: \""+self.name+"\"-{/color}"
        def getCraftingMenu(self):
            return "-craft: \""+self.name+"\"-"
        def getMixingMsg(self):
            global potion_lib
            return ">You mix the {i}"+potion_lib.getName(self.ingredients[0])+"{/i} with the {i}"+potion_lib.getName(self.ingredients[1])+"{/i}"


    class potion_ingredient(silver_potion_obj):
        id = ""
        cost = 0
        name = ""
        effect = ""
        description = ""
        picture = ""


    class potion_item_library(object):
        lib = []

        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)

        def getName(self,id):
            for item in self.lib:
                if item.id == id:
                    return item.name
            return None

        def validId(self, id):
            for item in self.lib:
                if item.id == id:
                    return True
            return False

        def getIdFromName(self, name):
            for item in self.lib:
                if item.name == name:
                    return item.id
            return None

        def getCraftable(self):
            craftable = []
            for item in self.lib:
                if hasattr(item, 'ingredients') and len(item.ingredients) > 0:
                    craftable.append(item)
            return craftable

        def getBuyable(self):
            buyable = []
            for item in self.lib:
                if hasattr(item, 'cost') and item.cost > 0:
                    buyable.append(item)
            return buyable

        def getRequests(self):
            requests = []
            for item in self.lib:
                if hasattr(item, 'start_label') and item.start_label != None:
                    requests.append(item)
            return requests



    class player_potion_invintory(object):

        def canCraft(self, potion):
            global p_inv
            for ing_id in potion.ingredients:
                if ing_id in p_inv.keys():
                    if p_inv[ing_id] < 1:
                        return False
                else:
                    return False
            return True

        def has(self, potion):
            global p_inv
            if isinstance(potion, silver_potion):
                potion = potion.id
            return potion in p_inv.keys()

        def add(self, potion, quant=1):
            global p_inv, potion_lib
            if isinstance(potion, silver_potion):
                potion = potion.id
            if potion_lib.getIdFromName(potion) != None:
                potion = potion_lib.getIdFromName(potion)
            if potion_lib.validId(potion):
                if potion in p_inv.keys():
                    p_inv[potion] = p_inv[potion] + quant
                else:
                    p_inv[potion] = quant
                return True
            else:
                return False

        def extend(self, list):
            for item in list:
                self.add(item)

        def remove(self, potion, quant=1):
            global p_inv
            if isinstance(potion, silver_potion):
                potion = potion.id
            if potion in p_inv.keys():
                p_inv[potion] = p_inv[potion] - quant
                if p_inv[potion] < 1:
                    p_inv.pop(potion, None)
                return True
            else:
                return False
