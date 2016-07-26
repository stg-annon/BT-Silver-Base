label desk:
    menu:
        "-Examine-" if not desk_examined:
            $ desk_examined = True
            m "A desk of some sort..."
            jump day_main_menu
        "-Do paperwork-" if finished_report < 6 and not got_paycheck and not day == 1 and work_unlock2:
            jump paperwork
        "{color=#858585}-Do paperwork-{/color}" if finished_report >= 6 and not got_paycheck:
            m "I've completed six reports this week already."
            jump desk
        "{color=#858585}-Do paperwork-{/color}" if got_paycheck: # When TRUE paycheck is in the mail.
            m "I need to get paid first."
            jump desk
         
        #"-Book collection- {image=book.png}" if not day == 1 and cataloug_found: 
        "-Book collection-" if not day == 1 and cataloug_found: 
            jump books_list
        
        
        #"-The muggle oddities-" if have_catalogue: #Real thing
        #"-DAHR's oddities-" if cataloug_found: 
        #    if order_placed or package_is_here:
        #        show screen bld1
        #        with d3
        #        dahr "Please be patient. The owl has been dispatched."
        #        hide screen bld1
        #        with d3
        #        jump desk
        #   else:
        #         jump the_oddities
        
        
        "-Doze off-" if daytime and not day == 1:
            jump night_start
        "-Go to sleep-" if not daytime and not day == 1:
            jump day_start
        
        #"-Jerk 0ff on Hermione's panties-" if hg_ps_PantyThief_OBJ.inProgress: #True when Hermione has no panties on.
        #    jump jerk_off
        "-Jerk Off-":
            jump jerk_off
        
        "-Never mind-":
            call screen main_menu_01
    
    
### PAPERWORK ###
label paperwork:
    stop music fadeout 1.0
    if daytime:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else: 
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        stop bg_sounds 
    
    
    hide screen genie
    show screen paperwork
    with Dissolve(0.3)
    ">You do some paperwork."
    
    call finished_working_chapter #Chapter finished. $ report_chapters += 1
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
        
    if daytime: # Makes sure that check happens only at nighttime. 
        pass
    else:
        if wather_generator >= 31 and wather_generator <= 40: # FULL MOON
            call f_moon_bonus
        if wather_generator >= 51 and wather_generator <= 60: # FULL MOON
            call f_moon_bonus
           
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### CONCENTRATION CHECK ###========================================================================
    if concentration == 1:
        $ concentraton_check = renpy.random.randint(1, 6) #Copper book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 2:
        $ concentraton_check = renpy.random.randint(1, 4) #Bronze book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 3:
        $ concentraton_check = renpy.random.randint(1, 2) #Silver book.
        if concentraton_check == 1:
            call concentration_label
    if concentration == 4:                                                               #Golden book.
        call concentration_label
#    if concentration == 5:
#        $ concentraton_check = renpy.random.randint(1, 2) #Platinum book.
#        if concentraton_check == 1:
#            call concentration_label
#    if concentration == 6:
#            call concentration_label
    ###==============================================================================================
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
    
    ### SPEEDWRITING CHECK ###========================================================================
    if speedwriting == 1:
        $ speedwriting_check = renpy.random.randint(1, 6) #"\"Speedwriting for dummies.\"" # 1/10 chance
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 2:
        $ speedwriting_check = renpy.random.randint(1, 4) #"\"Speedwriting for beginners.\"" # 1/8 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 3:
        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up.
        if speedwriting_check == 1:
            call speedwriting_label
    if speedwriting == 4:
            call speedwriting_label
#    if speedwriting == 5:
#        $ speedwriting_check = renpy.random.randint(1, 2) #"\"Speedwriting for experts.\"" # 1/2 chance of it to pop up.
#        if speedwriting_check == 1:
#            call speedwriting_label
#    if speedwriting == 6:
#        call speedwriting_label #""\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up.
    
    call report_chapters_check #Checks whether or not the completed chapter was the final one.
            

    show screen genie
    hide screen paperwork
    
    
    
    if daytime:
        jump night_start
    else: 
        jump day_start    
    
### 
label report_chapters_check:
    if report_chapters >= 7:
        ">You've completed a report."
        $ report_chapters = 0
        $ finished_report += 1
    return
### FULL MOON BONUS ###
label f_moon_bonus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">The Full moon makes you feel more productive.\n>You finished [report_chapters] chapters so far."
    return
###
label finished_working_chapter:
    $ report_chapters += 1
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You finished [report_chapters] chapters so far."
    return
### CONCENTRATION
label concentration_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You maintain perfect concentration during your work.\n>And finish another chapter of the report.\n>You finished [report_chapters] chapters so far."
    return
### SPEEDWRITING
label speedwriting_label:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    $ report_chapters += 1
    ">You use your speedwriting skills.\n>And finish another chapter of the report.\n>You finished [report_chapters] chapters so far."
    return
    
    
    
    
    
