label __init_variables:
    
    if not hasattr(renpy.store,'hermione_outfits_list'):
        $ hermione_outfits_list = outfit_list()
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_maid_OBJ",
            name = "Maid",
            cost = 100,
            wait_time = 2,
            store_image = "maid.png",
            outfit_layers =["maid_stockings.png","maid_skirt.png","maid_top.png","maid_gloves.png"],
            top_layers = ["maid_hat.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_gryffCheer_OBJ",
            name = "Griffindor Cheerleader",
            cost = 200,
            wait_time = 3,
            store_image = "cheer.png",
            outfit_layers = ["cheer_stockings.png","cheer_pants.png","cheer_top.png"],
            actions = [
                hermione_outfit_action(
                    name = "lift_top",
                    layers = [
                        "(OUTFIT_LAYERS)",
                        "cherr_flash.png"
                    ]
                )
            ]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_slythCheer_OBJ",
            name = "Slythrin Cheerleader",
            cost = 200,
            wait_time = 3,
            store_image = "s_cheer.png",
            outfit_layers = ["s_cheer_stockings.png","s_cheer_pants.png","s_cheer_top.png"],
            actions = [
                hermione_outfit_action(
                    name = "lift_top",
                    layers = [
                        "(OUTFIT_LAYERS)",
                        "cherr_flash.png"
                    ]
                )
            ]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_heartDancer_OBJ",
            name = "Heart Dancer",
            cost = 300,
            wait_time = 4,
            store_image = "heart.png",
            outfit_layers = ["heart_legs.png","heart_top.png","heart_collar.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_silkNightgown_OBJ",
            name = "Silk Nightgown",
            cost = 140,
            wait_time = 2,
            store_image = "nightgown.png",
            outfit_layers = ["silk_nightgown.png"],
            breast_layer = "breasts_normal"
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_pirate_OBJ",
            name = "Pirate",
            cost = 75,
            wait_time = 2,
            store_image = "pirate.png",
            outfit_layers = ["pirate_legs.png","pirate_pants.png","pirate_top.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_powerGirl_OBJ",
            name = "Power Girl",
            cost = 350,
            wait_time = 3,
            store_image = "power.png",
            hair_layer = "power_hair",
            outfit_layers = ["power_cape.png","power_top.png","power_gloves.png","power_belt.png","power_cape_top.png"],
            actions = [
                hermione_outfit_action(
                    name = "lift_top",
                    layers = [
                        "(OUTFIT_LAYERS)",
                        "cherr_flash.png"
                    ]
                )
            ]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_msMarvel_OBJ",
            name = "Mrs Marvel",
            cost = 250,
            wait_time = 5,
            store_image = "marvel.png",
            outfit_layers = ["marvel_pants.png","marvel_top.png","marvel_sash.png","marvel_gloves.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_harleyQuinn_OBJ",
            name = "Harley Quinn",
            cost = 300,
            wait_time = 4,
            store_image = "harley.png",
            hair_layer = "harley_hair",
            outfit_layers = ["harley_pants.png","harley_top.png","harley_gloves.png","harley_collar.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_ballDress_OBJ",
            name = "Ball Dress",
            cost = 1500,
            wait_time = 7,
            store_image = "ball_dress.png",
            outfit_layers = ["ball_dress_skirt.png","ball_dress_top.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_christmas_OBJ",
            name = "Christmas Girl",
            cost = 50,
            wait_time = 2,
            store_image = "christmas.png",
            breast_layer = "breasts_normal",
            top_layers = ["christmas_antlers.png"],
            outfit_layers = ["christmas_pants.png","christmas_top.png","christmas_gloves.png","christmas_collar.png"]
        ))
        $ hermione_outfits_list.append(hermione_outfit(
            id = "hg_laraCroft_OBJ",
            name = "Lara Croft",
            cost = 270,
            wait_time = 2,
            store_image = "lara.png",
            outfit_layers = ["lara_pants.png","lara_top.png","lara_gloves.png"]
        ))
    
    return
    
init python:
    class outfit_list(list):
    
        def __contains__(self, id):
            for i in self:
                if i.id == id:
                    return True
            return False
            
        def get(self, id):
            for i in self:
                if i.id == id:
                    return i
            return None
            
        def purchased(self, id):
            if isinstance(id,str):
                for i in self:
                    if i.id == id and i.purchased:
                        return True
                return False
            if isinstance(id,list):
                ans = []
                for i in id:
                    for j in self:
                        if j.id == i:
                            ans.append(j.purchased)
                return any(ans)
        
        def any_purchased(self, id):
            if isinstance(id,list):
                ans = []
                for i in id:
                    for j in self:
                        if j.id == i:
                            ans.append(j.purchased)
                return any(ans)
        
        def all_purchased(self, id):
            if isinstance(id,list):
                ans = []
                for i in id:
                    for j in self:
                        if j.id == i:
                            ans.append(j.purchased)
                return all(ans)
    
    class hermione_outfit(object):
        id = ""
        name = ""
        purchased = False
        cost = 0
        wait_time = 0 #the ammount of time to wait until compleded from clothes store
        top_layers = []
        outfit_layers = []
        actions = []
        hair_layer = ""
        breast_layer = "breasts_nipfix"
        store_image = ""
        root = "01_hp/13_characters/hermione/clothes/custom/"
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        def getMenuText(self):
            return "-"+self.name+"-"
        def getFullPath(self, passed_list):
            list = []
            for i in passed_list:
                list.append(self.root+i)
            return list
        def getOutfitLayers(self):
            return self.getFullPath(self.outfit_layers)
        def getTopLayers(self):
            return self.getFullPath(self.top_layers)
        def getStoreImage(self):
            return self.root+"gui/"+self.store_image
        
        def hasAction(self,action):
            for act in self.actions:
                if act.name == action:
                    return True
            return False
        def getActionLayers(self, action):
            if isinstance(action,str):
                action = self.getActionFromList(action)
            return action.getLayers(self)
        def getActionFromList(self,action):
            for act in self.actions:
                if act.name == action:
                    return act
            
    
    class hermione_outfit_action(hermione_character_action):
        def getLayers(self, parent):
            global h_whoring
            global hg_NoPanties_lvl
            layers = []
            for layer in self.layers:
                if "(OUTFIT_LAYERS)" in layer:
                    layers.extend(parent.getFullPath(parent.outfit_layers))
                else:
                    layers.append(parent.root+layer)
            return layers
    
