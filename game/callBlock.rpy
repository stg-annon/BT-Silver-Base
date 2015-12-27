label select_start:
    jump start_ht
    # menu:
        # "-Play Witch Trainer-":
            # jump start_ht
        # "-Play Princess Trainer-":
            # jump start_pt
        # "-Quit-":
            # return
label load_persistant_variables:
    call load_ht_persistant_vars
    # call load_pt_persistant_vars
    return
    
label declare_game_variables:
    call declare_ht_vars
    # call declare_pt_vars
    return