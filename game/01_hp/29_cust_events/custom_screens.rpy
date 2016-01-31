label __init_variables:

    return
    
    
    
screen custom_event:
    
    if use_cust_hair:
        add hermione_hair_a xpos c_e_xpos ypos c_e_ypos
    else:
        add head_base_a xpos c_e_xpos ypos c_e_ypos
    
    add cust_a xpos c_e_xpos ypos c_e_ypos
    add cust_b xpos c_e_xpos ypos c_e_ypos
    add cust_c xpos c_e_xpos ypos c_e_ypos
    add cust_d xpos c_e_xpos ypos c_e_ypos
    add cust_e xpos c_e_xpos ypos c_e_ypos
    add cust_f xpos c_e_xpos ypos c_e_ypos
    
    
    if use_cust_hair:
        add hermione_hair_b xpos c_e_xpos ypos c_e_ypos
    
    zorder c_e_zorder