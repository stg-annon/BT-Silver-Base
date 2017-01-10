
init python:
    
    # Actions are intended to be used with hermoines uniform not with outfits
    class hermione_character_action(silver_character_action):
        left_arm = "left_1.png"
        right_arm = "right_1.png"
        full_torso = False
        layers = []
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def getLayers(self, parent):
            global h_whoring
            global hg_NoPanties_lvl
            layers = []
            for layer in self.layers:
                if "(TOP_LEVEL)" in layer:
                    layers.append(parent.root+layer.replace("(TOP_LEVEL)",str(parent.uniform.top)))
                elif "(BOT_LEVEL)" in layer:
                    layers.append(parent.root+layer.replace("(BOT_LEVEL)",str(parent.uniform.bot)))
                elif "(BRA)" in layer:
                    layers.append(parent.root+layer.replace("(BRA)",str(parent.uniform.bra)))
                elif "(TORSO)" in layer:
                    layers.append(parent.root+layer.replace("(TORSO)",str(parent.body.torso)))
                elif "(PANTIES)" in layer and h_whoring < hg_NoPanties_lvl:
                    layers.append(parent.root+layer.replace("(PANTIES)",str(parent.uniform.panties)))
                else:
                    layers.append(parent.root+layer)
            return layers
    

label __init_variables:
    
    $ herm_actions = []
    $ herm_actions.append(
        hermione_character_action(
            name = "hold_book",
            left_arm = "",
            right_arm = "",
            layers = [
                "clothes/uniform/bot/(BOT_LEVEL).png",
                "clothes/uniform/action/hold_book_(TOP_LEVEL).png"
            ]
        )
    )
    $ herm_actions.append(
        hermione_character_action(
            name = "lift_skirt",
            left_arm = "",
            right_arm = "",
            layers = [
                "clothes/uniform/action/lift_skirt_fix.png",
                "clothes/underwear/(PANTIES)",
                "clothes/uniform/action/lift_skirt_top_(TOP_LEVEL).png",
                "clothes/uniform/action/lift_skirt_(BOT_LEVEL).png"
            ]
        )
    )
    $ herm_actions.append(
        hermione_character_action(
            name = "lift_top",
            left_arm = "",
            right_arm = "",
            layers = [
                "clothes/uniform/bot/(BOT_LEVEL).png",
                "body/torso/(TORSO)",
                "clothes/uniform/action/lift_top_(BOT_LEVEL).png"
            ]
        )
    )
    $ herm_actions.append(
        hermione_character_action(
            name = "lift_top_bra",
            left_arm = "",
            right_arm = "",
            layers = [
                "clothes/uniform/bot/(BOT_LEVEL).png",
                "clothes/underwear/(BRA)",
                "clothes/uniform/action/lift_top_(BOT_LEVEL).png"
            ]
        )
    )
    $ herm_actions.append(
        hermione_character_action(
            name = "lift_breasts",
            left_arm = "",
            right_arm = "",
            layers = [
                "body/breasts/breasts_normal.png",
                "body/arms/both/lift_breasts.png"
            ]
        )
    )
    $ herm_actions.append(
        hermione_character_action(
            name = "covering",
            left_arm = "",
            right_arm = "",
            layers = [
                "body/breasts/breasts_nipfix.png",
                "body/arms/both/covering.png"
            ]
        )
    )
    $ herm_actions.append(
        hermione_character_action(
            name = "pinch",
            left_arm = "",
            right_arm = "",
            layers = [
                "body/breasts/breasts_nonips.png",
                "body/arms/both/fingering_and_pinching.png"
            ]
        )
    )
    return

