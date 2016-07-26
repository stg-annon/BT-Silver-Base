label jerk_off:
#    $ cum_on_panties = True #True when choose to cum on Hermione's panties.
#    m "Hm... Who shall be my target?"
#    menu:
#        "\"Princess Jasmine!\"":
#            m "Yes, the princess... That dirty slut!"
#            $ jerking_off_to_jasmine = True #Princess Jasmine has been chosen as a target for a jerk-off session
#            pass
#        "\"Lara Croft\"":
#            $ jerking_off_to_lara = True
#            pass
#        "-Cancel-":
#            jump desk
    m "How should I finish this thing?"   
    label how_to_finish:
    menu:
        "{color=#858585}...(LOCKED)...{/color}" if not hg_ps_PantyThief_OBJ.inProgress:
            ">You lack the item required for this option."
            jump  how_to_finish
        "-Hermione's panties-" if hg_ps_PantyThief_OBJ.inProgress:
            $ cum_on_panties = True #True when choose to cum on Hermione's panties.
        "-On the floor!-":
            $ cum_on_the_floor = True #TRUE when chosen to cum on the floor.
            pass
        "-Cancel-":
            jump jerk_off


### JERKING OFF ###
show screen blkfade
with d5
">You decide to spend some time by jerking off..."
if jerking_off_to_jasmine:
    ">You fantasize about Princess Jasmine..."
if jerking_off_to_lara:
    ">You fantasize about Lara Croft..."

">You are ready to cum..."
if cum_on_the_floor:
    ">You cum on the floor."
if cum_on_panties:
    $ hg_ps_PantyThief_SoakedPantiesFlag = True #TRUE when you have the panties in your possession (before you return them to Hermione).
    ">You cum all over Hermione's panties, and then use them to wipe the cum off the floor..."
    ">You received the item: \"Cum-soaked panties\"."
 
hide screen blkfade
with d5
#m "This was a pretty sweet jerk-off session..."
    
### SETTING ALL THE FLAGS BACK TO DEFAULT ###
$ jerking_off_to_jasmine = False #Turns TRUE when Princess Jasmine has been chosen as a target for a jerk-off session.
$ jerking_off_to_lara = False 
$ cum_on_the_floor = False #TRUE when chosen to cum on the floor.
$ cum_on_panties = False #True when choose to cum on Hermione's panties.



if daytime:
    jump night_start
else: 
    jump day_start
