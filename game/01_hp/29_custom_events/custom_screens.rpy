label __init_variables:
    
    if not hasattr(renpy.store,'ce_name'): #important!
        $ ce_name = "NO_NAME_GIVEN"
    if not hasattr(renpy.store,'ce_h_body'): #important!
        $ ce_h_body = "01_hp/29_custom_events/blank.png"
    if not hasattr(renpy.store,'ce_body_filename'): #important!
        $ ce_body_filename = "blank"
    $ ce_zorder = 5
    
    $ ce_xpos = 370
    $ ce_ypos = 0
    
    $ ce_head_xpos = 390
    $ ce_head_ypos = 340
    
    $ ce_hair = True
    $ ce_base = False
    $ ce_skirt = False
    $ ce_panties = False
    $ ce_top = False
    $ ce_bra = False
    $ ce_arms = False
    
    $ ce_hair_style = "A"
    $ ce_hair_color = "1"
    $ ce_breasts = 1
    
    $ ce_hair_a = "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+".png"
    $ ce_hair_b = "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+"_2.png"
    
    $ cust_a = "01_hp/29_custom_events/common/body.png"
    $ cust_b = "01_hp/29_custom_events/common/arms.png"
    $ cust_c = "01_hp/29_custom_events/common/breasts_"+str(ce_breasts)+".png"
    $ cust_d = "01_hp/29_custom_events/common/panties.png"
    $ cust_e = "01_hp/29_custom_events/common/bra.png"
    $ cust_f = "01_hp/29_custom_events/common/skirt.png"
    $ cust_g = "01_hp/29_custom_events/common/top.png"
    
    
    return
    
screen custom_event_h:
    
    if ce_hair:
        add "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+".png" xpos ce_xpos ypos ce_ypos
    
    if ce_base:
        add cust_a xpos ce_xpos ypos ce_ypos
    if ce_arms:
        add cust_b xpos ce_xpos ypos ce_ypos
    if ce_breasts:
        add cust_c xpos ce_xpos ypos ce_ypos
    
    add ce_h_body xpos ce_xpos ypos ce_ypos
    
    if ce_skirt:
        add cust_f xpos ce_xpos ypos ce_ypos
    elif ce_panties:
        add cust_d xpos ce_xpos ypos ce_ypos
    if ce_top:
        add cust_g xpos ce_xpos ypos ce_ypos
    elif ce_bra:
        add cust_e xpos ce_xpos ypos ce_ypos
    
    if ce_hair:
        add "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+"_2.png" xpos ce_xpos ypos ce_ypos
    
    zorder ce_zorder
    
screen custom_event_head_h:
    
    if ce_hair:
        add "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+".png" xpos ce_head_xpos ypos ce_head_ypos
    
    if ce_base:
        add cust_a xpos ce_head_xpos ypos ce_head_ypos
    if ce_arms:
        add cust_b xpos ce_head_xpos ypos ce_head_ypos
    if ce_breasts:
        add cust_c xpos ce_head_xpos ypos ce_head_ypos
    
    add ce_h_body xpos ce_head_xpos ypos ce_head_ypos
    
    if ce_skirt:
        add cust_f xpos ce_head_xpos ypos ce_head_ypos
    elif ce_panties:
        add cust_d xpos ce_head_xpos ypos ce_head_ypos
    if ce_top:
        add cust_g xpos ce_head_xpos ypos ce_head_ypos
    elif ce_bra:
        add cust_e xpos ce_head_xpos ypos ce_head_ypos
    
    if ce_hair:
        add "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+"_2.png" xpos ce_head_xpos ypos ce_head_ypos
    
    zorder 8
    
label ce_her_main(text = "", body=ce_body_filename,xpos = ce_xpos,ypos = ce_ypos, eventName = ce_name):
    hide screen custom_event_h
    if xpos != ce_xpos:
        $ ce_xpos = xpos
    if ypos != ce_ypos:
        $ ce_ypos = ypos
    if eventName != ce_name:
        $ ce_name = eventName
    if body != ce_body_filename:
        $ ce_body_filename = body
    $ ce_h_body = "01_hp/29_custom_events/"+str(ce_name)+"/resources/"+str(ce_body_filename)+".png"
    show screen custom_event_h
    with d3
    if text != "":
        if "[tmp_name]" in text or "[genie_name]" in text:
            if "[tmp_name]" in text:
                $ text1,text2 = text.split("[tmp_name]")
                $ text = (text1 + tmp_name + text2)
            if "[genie_name]" in text:
                $ text1,text2 = text.split("[genie_name]")
                $ text = (text1 + genie_name + text2)
        her "[text]"
    return
    
label ce_her_head(text = "", body="", eventName = ce_name):
    if eventName != ce_name:
        $ ce_name = eventName
    if body != "":
        $ ce_h_body = "01_hp/29_custom_events/"+str(ce_name)+"/resources/"+str(body)+".png"
    show screen custom_event_head_h
    if text != "":
        if "[tmp_name]" in text or "[genie_name]" in text:
            if "[tmp_name]" in text:
                $ text1,text2 = text.split("[tmp_name]")
                $ text = (text1 + tmp_name + text2)
            if "[genie_name]" in text:
                $ text1,text2 = text.split("[genie_name]")
                $ text = (text1 + genie_name + text2)
        her2 "[text]"
    hide screen custom_event_head_h
    return