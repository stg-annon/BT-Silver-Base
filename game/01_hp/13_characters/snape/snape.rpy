
label sna_main(text="",face=""):
    hide screen snape_main
    with d3
    if face != "":
        $ s_sprite = "01_hp/13_characters/snape/main/"+str(face)+".png"
    show screen snape_main
    with d3
    if text != "":
        if "[hermione_name]" in text or "[genie_name]" in text:
            if "[genie_name]" in text:
                $ text = text.replace("[genie_name]",genie_name)
            if "[hermione_name]" in text:
                $ text = text.replace("[hermione_name]",hermione_name)
        sna "[text]"
    return
    
label sna_head(text="",face="",xpos=s_head_xpos ,ypos=s_head_ypos):
    if xpos != s_head_xpos:
        $ s_head_xpos = xpos+140
    if ypos != s_head_ypos:
        $ s_head_ypos = ypos
    if face != "":
        $ s_sprite = "01_hp/13_characters/snape/main/"+str(face)+".png"
    show screen s_head
    if text != "":
        sna2 "[text]"
    hide screen s_head
    return
    
label snape_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = snape_speed, loiter = False,redux_pause = 0):
    hide screen snape_walk_01
    hide screen snape_walk_01_f
    $ pos1 = pos1+140
    $ pos2 = pos2+140
    $ walk_xpos = pos1 #(From)
    $ walk_xpos2 = pos2 #(To)
    $ snape_chibi_ypos = 250
    $ snape_speed = speed #Speed of walking animation. (lower = faster)
    if pos1 > pos2: #right to left (snape_walk_01)
        show screen snape_walk_01
        $ tmp = snape_speed - redux_pause
        pause tmp
        $ snape_chibi_xpos = pos2
        hide screen snape_walk_01
        if loiter:
            show screen snape_01
    else: #left to right (snape_walk_01_f)
        show screen snape_walk_01_f
        $ tmp = snape_speed - redux_pause
        pause tmp
        $ snape_chibi_xpos = pos2
        hide screen snape_walk_01_f
        if loiter:
            show screen snape_01_f
    return
    