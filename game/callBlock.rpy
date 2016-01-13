label select_start:
    jump start_ht
    # menu:
        # "-Play Witch Trainer-":
            # jump start_ht
        # "-Play Princess Trainer-":
            # jump start_pt
        # "-Quit-":
            # return
    
init python:
    def init_variables():
        initvarlabels = [label for label in renpy.get_all_labels() if label.endswith('__init_variables') ]
        for l in initvarlabels:
            renpy.call_in_new_context(l) 