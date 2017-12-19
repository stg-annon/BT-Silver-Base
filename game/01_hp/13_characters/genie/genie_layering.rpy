###SCREEN CODE FOR GENIE
screen genie_sprite:
    add genie_sprite_base xpos genie_sprite_xpos ypos genie_sprite_ypos xzoom genie_sprite_flip#Add the base body
    add genie_sprite_exp xpos genie_sprite_xpos ypos genie_sprite_ypos xzoom genie_sprite_flip#Add genie expression

    zorder genie_zorder

label gen_main(text="",face=genie_sprite_exp,body=genie_sprite_base):
    if face != genie_sprite_exp:
        $ genie_sprite_exp = "01_hp/13_characters/genie/exp_" + str(face) + ".png"
    if body != genie_sprite_base:
        $ genie_sprite_base = "01_hp/13_characters/genie/base_" + str(body) + ".png"

    show screen genie_sprite 
    if text != "":
        $ renpy.say(msp,text)
    return

###VARIABLE DECLARATION
label init_genie_layering:
    $ genie_sprite_base = "01_hp/13_characters/genie/base_1.png"
    $ genie_sprite_exp = "01_hp/13_characters/genie/exp_1.png"
    $ genie_sprite_xpos = 200
    $ genie_sprite_ypos = 0
    $ genie_sprite_flip = 1
    $ genie_zorder = 4

    return

