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
    
    $ use_cust_hair = True
    
    return
    
screen custom_event_h:
    
    if use_cust_hair:
        add hermione_hair_a xpos ce_xpos ypos ce_ypos
    else:
        pass
        # add head_base_a xpos ce_xpos ypos ce_ypos
    
    add ce_h_body xpos ce_xpos ypos ce_ypos
    
    # add cust_a xpos ce_xpos ypos ce_ypos
    # add cust_b xpos ce_xpos ypos ce_ypos
    # add cust_c xpos ce_xpos ypos ce_ypos
    # add cust_d xpos ce_xpos ypos ce_ypos
    # add cust_e xpos ce_xpos ypos ce_ypos
    # add cust_f xpos ce_xpos ypos ce_ypos
    
    
    if use_cust_hair:
        add hermione_hair_b xpos ce_xpos ypos ce_ypos
    
    zorder ce_zorder
    
screen custom_event_head_h:
    
    if use_cust_hair:
        add hermione_hair_a xpos ce_head_xpos ypos ce_head_ypos
    else:
        pass
        # add head_base_a xpos ce_head_xpos ypos ce_head_ypos
    
    add ce_h_body xpos ce_head_xpos ypos ce_head_ypos
    
    # add cust_a xpos ce_head_xpos ypos ce_head_ypos
    # add cust_b xpos ce_head_xpos ypos ce_head_ypos
    # add cust_c xpos ce_head_xpos ypos ce_head_ypos
    # add cust_d xpos ce_head_xpos ypos ce_head_ypos
    # add cust_e xpos ce_head_xpos ypos ce_head_ypos
    # add cust_f xpos ce_head_xpos ypos ce_head_ypos
    
    
    if use_cust_hair:
        add hermione_hair_b xpos ce_head_xpos ypos ce_head_ypos
    
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
        her "[text]"
    hide screen custom_event_head_h
    return