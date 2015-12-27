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
        
        
        

        "-Jerk 0ff on Hermione's panties-" if request_03: #True when Hermione has no panties on.
            jump jerk_off
        "-Doze off-" if daytime and not day == 1:
            jump night_start
        "-Go to sleep-" if not daytime and not day == 1:
            jump day_start
            

        "-Never mind-":
            call screen main_menu_01
            
            

        
  
            
            


    
### READING ###

######################################
### BOOK 01 ########################## "\"Copper book of spirit\"" #1/8 (small) chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_01:
    
    call reading_block
    
    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book01], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book01]."
   
    call chap_finished
    
    call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished
            call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished
            call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."

#===#############################################


    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished
            call chapter_check_book_01 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
   
label chapter_check_book_01: #Checks if the chapter just finished was the last one.
    if book_01_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

       
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter, You finished the entire book."
        ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork.."

        $ concentration += 1
        $ book_01_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return
    
    
######################################
### BOOK 02 ########################## "\"Bronze book of spirit\""
######################################
label reading_book_02:
    
    call reading_block
    
    hide screen gift
    with d3
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book02], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book02]..."
   
    call chap_finished_02
    
    call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_02
            call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_02
            call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_02
            call chapter_check_book_02 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_02: 
    $ book_02_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_02_units]\" of the book."
    return
    
###
label chapter_check_book_02: #Checks if the chapter just finished was the last one.
    if book_02_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter. You finished the entire book."
        ">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when doing paperwork.."

        $ concentration += 1
        $ book_02_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
######################################
### BOOK 03 ########################## "\"Silver book of spirit\""
######################################
label reading_book_03:
    
    call reading_block
    
    hide screen gift
    
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book03], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book03]..."
   
    call chap_finished_03
    
    call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_03
            call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_03
            call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_03
            call chapter_check_book_03 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_03: 
    $ book_03_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_03_units]\" of the book."
    return
    
###
label chapter_check_book_03: #Checks if the chapter just finished was the last one.
    if book_03_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter. You finished the entire book."
        ">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when doing paperwork."

        $ concentration += 1
        $ book_03_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
 
######################################
### BOOK 04 ########################## "\"Golden book of spirit\""
######################################
label reading_book_04:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book03], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book03]..."
   
    call chap_finished_04
    
    call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_04
            call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_04
            call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_04
            call chapter_check_book_04 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_04: 
    $ book_04_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_04_units]\" of the book."
    return
    
###
label chapter_check_book_04: #Checks if the chapter just finished was the last one.
    if book_04_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        #">New skill unlocked: a sure chance of completing an additional chapter when doing paperwork."
        ">You have mastered your spirit and from now on you shall always complete an additional chapter when doing paperwork."


        $ concentration += 1
        $ book_04_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
    
 
 
    
######################################
### BOOK 05 ##########################
######################################
label reading_book_05:
    stop music fadeout 2.0
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...


    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        ">You read a book called [book05], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book05]..."
   
    call chap_finished_05
    
    call chapter_check_book_05 #Checks if the chapter just finished was the last one.
    
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_05
            call chapter_check_book_05 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed both speed reading books.
            call chap_finished_05
            call chapter_check_book_05 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################    
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_05
            call chapter_check_book_05 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."

    if fire_in_fireplace:
        hide screen reading_near_fire
        stop bg_sounds #"sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_05: 
    
    $ book_05_units +=1
    
    if book_05_units == 1:
        "Chapter [book_05_units]" "Galadriel - a gentle and gracious elven princess is introduced into the story."
    if book_05_units == 2:
        "Chapter [book_05_units]" "Galadriel's father - King Methis and his childhood friend Mofothelis are introduced into the story."
    if book_05_units == 3:
        "Chapter [book_05_units]" "King Methis makes an announcement. His daughter, princess Galadriel is to be wed to chancellor Mofothelis."
    if book_05_units == 4:
        "Chapter [book_05_units]" "Galadriel refuses to marry a man who is thrice her age and whom, up until now, she considered only as her uncle."
    if book_05_units == 5:
        "Chapter [book_05_units]" "King Methis dismisses her daughter's \"foolish\" complaints. Galadriel decides to run away."
    if book_05_units == 6:
        "Chapter [book_05_units]" "Galadriel manages to leave the royal residence at night unnoticed..."
    if book_05_units == 7:
        "Chapter [book_05_units]" "King Methis is furious about his daughter's escape. He decides to personally lead the search party."
    if book_05_units == 8:
        "Chapter [book_05_units]" "Galadriel rides her mare \"white dove\" through the forest. The Princess enjoys her freedom... After a while she meets a rather handsome human nobleman on a horse..."
    if book_05_units == 9:
        "Chapter [book_05_units]" "Galadriel rides alongside the nobleman. They exchange meaningless pleasantries. He makes her laugh. Suddenly the nobleman attacks the princess and knocks her out!..."
    if book_05_units == 10:
        "Chapter [book_05_units]" "Galadriel comes about. To her horror she realizes that the nobleman is having his way with her. Galadriel is screaming for help but The handsome man keeps on raping her."
    if book_05_units == 11:
        "Chapter [book_05_units]" "Galadriel tries to fight the nobleman off. Only now she notices that about half a dozen men are surrounding them. The men are sneering viciously."
    if book_05_units == 12:
        "Chapter [book_05_units]" "After the nobleman is done with Galadriel, every one of his men in turn has a go at the elven princess. Galadriel cries and begs them to stop."
    if book_05_units == 13:
        "Chapter [book_05_units]" "Galadriel finds herself in a cage at some sort of market. Her hands are tied, Her noble garments are ripped to shreds and her hair is full of twigs and dry semen."
    if book_05_units == 14:
        "Chapter [book_05_units]" "A fat, rich looking man buys Galadriel and brings her to his house. The princess does not cry anymore. She is happy to be out of the cage."
    if book_05_units == 15:
        "Chapter [book_05_units]" "Galadriel is allowed to take a bath after which a servant brings her clean clothes and some food."
    if book_05_units == 16:
        "Chapter [book_05_units]" "Galadriel is starting to feel hopeful but it does not last. Soon she realizes what kind of establishment this is: a whorehouse."
    if book_05_units == 17:
        "Chapter [book_05_units]" "The elven princess is forced to work as a whore. She detests her new life but has very little choice."
    if book_05_units == 18:
        "Chapter [book_05_units]" "Galadriel gains popularity quickly. Humans, Dark Elves and even the occasional dwarf - she spreads her legs for everyone."
    if book_05_units == 19:
        "Chapter [book_05_units]" "The fame of the young and beautiful elven whore spreads. Galadriel accepts her new life in the brothel."
    if book_05_units == 20:
        "Chapter [book_05_units]" "Suddenly and abruptly everything changes. Galadriel finds out that she is pregnant. -End of book one-"


     
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_05_units]\" of the book."
    return
    
###
label chapter_check_book_05: #Checks if the chapter just finished was the last one.
    if book_05_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02 
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ book_05_complete = True
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Your imagination has improved."
        $ imagination +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
    
######################################
### BOOK 05_b ##########################
######################################
label reading_book_05_b: ### TALE OF GALADRIEL. BOOK TWO.
    
    ### SOUNDS BLOCK ###
    stop music fadeout 1.0
    if raining:
        play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if fire_in_fireplace:
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/day.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    if not daytime and not raining and not fire_in_fireplace:
        play bg_sounds "sounds/night.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    ### END OF BLOCK ###

    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book05b], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book05b]"
   
    call chap_finished_05_b
    
    call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
    
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_05_b
            call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed both speed reading books.
            call chap_finished_05_b
            call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################    
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_05_b
            call chapter_check_book_05_b #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_05_b: 
    
    $ book_05_b_units +=1
    
    if book_05_b_units == 1:
        "Chapter [book_05_b_units]" "Galadriel has been pregnant for several months now. To the princess' own surprise her popularity grows seemingly in direct correlation to the size of her belly."
    if book_05_b_units == 2:
        "Chapter [book_05_b_units]" "Although Galadriel maintains the appearance of an obedient whore, in truth she contemplates her escape from the brothel."
    if book_05_b_units == 3:
        "Chapter [book_05_b_units]" "The Elven Princess-Whore knows nothing of the life outside the of walls of the brothel. But it does not affect her determination to escape."
    if book_05_b_units == 4:
        "Chapter [book_05_b_units]" "It takes a lot of preparation and careful planning but Galadriel manages to successfully escape from the brothel."
    if book_05_b_units == 5:
        "Chapter [book_05_b_units]" "Galadriel soon gets lost in the vast city and is forced to spend the night on the street."
    if book_05_b_units == 6:
        "Chapter [book_05_b_units]" "Food is hard to come by on the streets. Galadriel fights a pack of stray dogs over some scraps and one of them bites her hand badly."
    if book_05_b_units == 7:
        "Chapter [book_05_b_units]" "The Pregnant Galadriel offers her company to a couple of filthy looking homeless men in exchange for food. She spends the night with them."
    if book_05_b_units == 8:
        "Chapter [book_05_b_units]" "Galadriel realizes that her live back in the brothel was a heaven compared to the live she's been leading for the past several days. She decides to return."
    if book_05_b_units == 9:
        "Chapter [book_05_b_units]" "Galadriel's owner - the fat, wealthy man does not punish Galadriel for escaping. He is happy to have one of his most popular girls back."
    if book_05_b_units == 10:
        "Chapter [book_05_b_units]" "Galadriel is, yet again, warm, clean and well fed. She is glad to be back and as popular as ever."
    if book_05_b_units == 11:
        "Chapter [book_05_b_units]" "Galadriel keeps servicing the clients throughout the rest of her pregnancy. The baby is due any day now..."
    if book_05_b_units == 12:
        "Chapter [book_05_b_units]" "A wealthy man wearing a mask booked Galadriel for an entire day. Galadriel is wondering about the man's true identity rather lazily while pleasuring him."
    if book_05_b_units == 13:
        "Chapter [book_05_b_units]" "The mystery man spends the entire day by having his way with Galadriel. Her engorged breasts drip milk heavily as the man fucks her."
    if book_05_b_units == 14:
        "Chapter [book_05_b_units]" "The masked man splatters Galadriel's face with cum for the second time today. He then chooses to reveal his identity and takes his mask off."
    if book_05_b_units == 15:
        "Chapter [book_05_b_units]" "Galadriel recognizes the man as her father - King Methis. Only now he realizes that the pregnant whore he fucked for hours is his daughter."
    # Only now he realizes that the pregnant whore he fucked for hours is his daughter.
    if book_05_b_units == 16:
        "Chapter [book_05_b_units]" "The man embraces his speechless child. Galadriel's eyes have a vacant look in them as her father's semen drips down her face..."
    if book_05_b_units == 17:
        "Chapter [book_05_b_units]" "Galadriel screams in terror. To her surprise she finds herself back in the royal residence and in her own bed."
    if book_05_b_units == 18:
        "Chapter [book_05_b_units]" "It takes the elven princess several minutes to realize that she was never pregnant. The entire adventure was nothing but a dream."
    if book_05_b_units == 19:
        "Chapter [book_05_b_units]" "Galadriel rushes to her father's chambers and embraces him. The girl is relived to have her old life \"back\". She happy agrees to marry chancellor Mofothelis."
    if book_05_b_units == 20:
        "Chapter [book_05_b_units]" "{size=-1}Galadriel is at the altar. She is content and happy. Suddenly she notices something that fills her heart with horror. There is a scar on her hand. The mark of a dog's bite. -The End-{/size}"
    
     
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_05_b_units]\" of the book."
    
    return
    
###
label chapter_check_book_05_b: #Checks if the chapter just finished was the last one.
    if book_05_b_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02 
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ book_05_b_complete = True
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Your imagination has improved."
        $ imagination +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
        
        
######################################
### BOOK 06 ##########################
######################################
label reading_book_06:
    
    call reading_block
 
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book06], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book06]..."
   
    call chap_finished_06
    
    call chapter_check_book_06 #Checks if the chapter just finished was the last one.
    ">There are still some chapters left."

#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_06
            call chapter_check_book_06 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_06
            call chapter_check_book_06 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################       
    
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_06
            call chapter_check_book_06 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_06: 
    
    $ book_06_units +=1
    
    if book_06_units == 1:
        "\"Chapter [book_06_units]\"\nA family of noble northmen is introduced into the story."
    if book_06_units == 2:
        "\"Chapter [book_06_units]\"\nThe royal family and the king are introduced into the story."
    if book_06_units == 3:
        "\"Chapter [book_06_units]\"\nAnother family is introduced into the story."
    if book_06_units == 4:
        "\"Chapter [book_06_units]\"\nSome incest action between a brother and his sister, the queen, is taking place."
    if book_06_units == 5:
        "\"Chapter [book_06_units]\"\nAttempted child murder takes place. The kid barely survives and is now in a coma."
    if book_06_units == 6:
        "\"Chapter [book_06_units]\"\nSome more characters are introduced into the story."
    if book_06_units == 7:
        "\"Chapter [book_06_units]\"\nSome characters hatch an evil scheme against some other characters."
    if book_06_units == 8:
        "\"Chapter [book_06_units]\"\nThe king gets poisoned and dies. Some more brother on sister incest takes place."
    if book_06_units == 9:
        "\"Chapter [book_06_units]\"\nA certain character you've been especially rooting for gets executed."
    if book_06_units == 10:
        "\"Chapter [book_06_units]\"\nSome new characters are introduced into the story."
    if book_06_units == 11:
        "\"Chapter [book_06_units]\"\nSome female characters get raped and then killed brutally."
    if book_06_units == 12:
        "\"Chapter [book_06_units]\"\nSome more members of the noble family of northmen find their untimely demise."
    if book_06_units == 13:   
        "\"Chapter [book_06_units]\"\nSome more women get raped. Some of them manage to survive. (Surely only to get raped some more later)." 
    if book_06_units == 14:
        "\"Chapter [book_06_units]\"\nThe characters you hate clash in an epic battle against the characters you are rooting for."
    if book_06_units == 15:
        "\"Chapter [book_06_units]\"\nMost of the characters you hate survive the battle. Every single character you were rooting for is dead."
    if book_06_units == 16:
        "\"Chapter [book_06_units]\"\nSome more rapes take place, then some more murders... (You don't even care anymore...)" 
    if book_06_units == 17:
        "\"Chapter [book_06_units]\"\nA new group of characters is introduced into the story. You sort of starting to root for one of them."
    if book_06_units == 18:
        "\"Chapter [book_06_units]\"\nThe character you were rooting for falls in love with a pretty girl."
    if book_06_units == 19:
        "\"Chapter [book_06_units]\"\nThe character you were rooting for gets brutally murdered. His girl gets raped and then murdered as well."
    if book_06_units == 20:
        "\"Chapter [book_06_units]\"\nA new race of half-frozen undead monsters is introduced into the story. To be continued..."
        
    
        
    
     
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_06_units]\" of the book."
    return
    
###
label chapter_check_book_06: #Checks if the chapter just finished was the last one.
    if book_06_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

      
        ">That was the last chapter. You finished the entire book."
        g4 "What a pile of garbage! I hate the guy who wrote this crap!"
        m "Although all those rapes gave me a few ideas..."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">Your imagination has improved."
        $ imagination +=1
        $ book_06_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
    
######################################
### BOOK 07 ########################## MY DEAR WAIFU ###
######################################
label reading_book_07:
    
    call reading_block
    
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book07], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book07]..."
   
    call chap_finished_07
    
    call chapter_check_book_07 #Checks if the chapter just finished was the last one.
    
    ">There are still some chapters left."

#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_07
            call chapter_check_book_07 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
#        $ speed_dummies = renpy.random.randint(1, 2) 
#        #$ speed_dummies = 1 #Here for testing porpoise only.
#        if speed_dummies == 1: #Success.
        call yes_book_09 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
        call chap_finished_07
        call chapter_check_book_07 #Checks if the chapter just finished was the last one.
        ">There are still some chapters left."
#===#############################################
    
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_07
            call chapter_check_book_07 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_07: 
    
    $ book_07_units +=1
    
    call waifu
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_07_units]\" of the book."
    return
    
###
label chapter_check_book_07: #Checks if the chapter just finished was the last one.
    if book_07_units == 20:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

      
        ">That was the last chapter. You finished the entire book."
        if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
            m "Wow! What a great book! That was intense!"
            
            #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
            if not found_dahrs_ticket_once:
                m "Hm...?"
                m "What is that...? A bookmark?"
                $ the_gift = "01_hp/18_store/06.png" # The DAHR's ticket.
                show screen gift
                with d3
                $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                ">You found a DAHR's voucher."
                hide screen gift
                with d3
                m "Hm..."
                $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                $ waifu_book_completed = True
        elif shea_waifu and shea >= 8: 
            if not complited_shea_already: #Finished with Shea for the first time.
                m "Not bad. I really grew to care about that Shea girl..."
                g9 "Well, her and her anal virginity..."
                $ complited_shea_already = True
            else: #Finished with Shea for the second time.
                m "So I ended up with Shea again, huh?"
                m "Hm... Maybe I should try and make different choices next time...?"
        elif victoria_waifu and victoria >= 7:
            if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                m "Not bad, not bad. That Ms. Stevens Lady turned out to be one dirty slut..."
                $ complited_stevens_already = True
            else: #Finished with Shea for the second time.
                m "So I ended up with Ms.Stevens again?"
                m "Hm... Maybe I should try and make different choices next time...?"
        elif leena_waifu and leena >= 8:
            if not complited_leena_already: #Finished with Leena for the first time.
                g9 "Sweet! I love happy endings!"
                $ complited_leena_already = True
            else: #Finished with Shea for the second time.
                m "So I ended up with that blond chick again?"
                m "Hm... Maybe I should try and make different choices next time...?"

        else:
            m "Hm... What an anticlimactic ending..."
            #m "Maybe I should read it again sometime."
        
        if not dear_waifu_completed_once:
            $ dear_waifu_completed_once = True # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
            $ renpy.play('sounds/win_04.mp3')   #Not loud.
            hide screen notes
            show screen notes
            ">Your imagination has improved."
            $ imagination +=1
        $ book_07_units = 0 #RESTING THE BOOK FOR ANOTHER PLAYTHORUGH.
        $ shea = 0 #RESETING SHEA'S POINTS FOR THE NEXT PLAYTHOURGH.
        $ victoria = 0
        $ leena = 0
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
    
    
        
######################################
### BOOK 08 ##########################
######################################
label reading_book_08:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book08], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book08]..."
   
    call chap_finished_08
    
    call chapter_check_book_08 #Checks if the chapter just finished was the last one.
            
   
    


    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_08
            call chapter_check_book_08 #Checks if the chapter just finished was the last one.
      
    ">There are still some chapters left."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_08: 
    $ book_08_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_08_units]\" of the book."
    return
    
###
label chapter_check_book_08: #Checks if the chapter just finished was the last one.
    if book_08_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">New skill unlocked: big chance of completing an additional chapter when reading."
        $ book_08_complete = True
        $ s_reading_lvl +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
    
    
######################################
### BOOK 09 ########################## Speed reading for experts
######################################
label reading_book_09:
    
    call reading_block ### Plays sound effects appropriate for reading. 

    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book09], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book09]..."
   
    call chap_finished_09
    
    call chapter_check_book_09 #Checks if the chapter just finished was the last one.
            
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_09
            call chapter_check_book_09 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################       

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_09
            call chapter_check_book_09 #Checks if the chapter just finished was the last one.

    
    ">There are still some chapters left."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_09: 
    $ book_09_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You've completed \"chapter [book_09_units]\" of the book."
    return
    
###
label chapter_check_book_09: #Checks if the chapter just finished was the last one.
    if book_09_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">New skill unlocked: big chance of completing an additional chapter when reading."


        $ book_09_complete = True
        $ s_reading_lvl +=1
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return        
    
    
######################################
### BOOK 10 ########################## "\"Platinum book of spirit\""
######################################
label reading_book_10:
    hide screen gift
    call reading_block
    
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book10], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book10]..."
   
    call chap_finished_10 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_10
            call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 2) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_10
            call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_10
            call chapter_check_book_10 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_10: 
    $ book_10_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_10_units]\" of the book."
    return
    
###
label chapter_check_book_10: #Checks if the chapter just finished was the last one.
    if book_10_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes

        ">New skill unlocked: a big chance of completing an additional chapter when doing paperwork."

        $ concentration += 1
        $ book_10_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
######################################
### BOOK 11 ########################## "\"Adamantium book of spirit\""
######################################
label reading_book_11:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book11], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book11]..."
   
    call chap_finished_11 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_11
            call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_11
            call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_11
            call chapter_check_book_11 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_11: 
    $ book_11_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_11_units]\" of the book."
    return
    
###
label chapter_check_book_11: #Checks if the chapter just finished was the last one.
    if book_11_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You have mastered your spirit and from now on you shall always complete an additional chapter when doing paperwork."

        $ concentration += 1
        $ book_11_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
    
 
######################################
### BOOK 12 ########################## "\"Speedwriting for dummies.\""
######################################
label reading_book_12:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book12], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book12]..."
   
    call chap_finished_12 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            
    ">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_12
            call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_12
            call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
#===#############################################

    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_12
            call chapter_check_book_12 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_12: 
    $ book_12_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You've completed \"chapter [book_12_units]\" of the book."
    return
    
###
label chapter_check_book_12: #Checks if the chapter just finished was the last one.
    if book_12_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">New skill unlocked: a 1 out of 6 chance of completing an additional chapter when doing paperwork."

        $ speedwriting += 1
        $ book_12_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return    
        
######################################
### BOOK 13 ########################## "\"Speedwriting for beginners.\""
######################################
label reading_book_13:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book13], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book13]."
   
    call chap_finished_13 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_13 #Checks if the chapter just finished was the last one.
            

    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_13
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_13
            
#===#############################################
    
    call chapter_check_book_13 #Checks if the chapter just finished was the last one.
    ">There are still some chapters left."
   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_13
            call chapter_check_book_13 #Checks if the chapter just finished was the last one.
            ">There are still some chapters left."
    

    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_13: 
    $ book_13_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_13_units]\" of the book."
    return
    
###
label chapter_check_book_13: #Checks if the chapter just finished was the last one.
    if book_13_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">New skill unlocked: a 1 out of 4 chance of completing an additional chapter when doing paperwork."

        $ speedwriting += 1
        $ book_13_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return             
    
    
######################################
### BOOK 14 ########################## "\"Speedwriting for intermediate.\"" # 1/6 chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_14:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book14], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book14]..."
   
    call chap_finished_14 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_14 #Checks if the chapter just finished was the last one.
            
    #">There are still some chapters left."
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_14
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_14
            
#===#############################################
    
    call chapter_check_book_14 #Checks if the chapter just finished was the last one.

   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_14
            call chapter_check_book_14 #Checks if the chapter just finished was the last one.
            
    
    ">There are still some chapters left."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_14: 
    $ book_14_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_14_units]\" of the book."
    return
    
###
label chapter_check_book_14: #Checks if the chapter just finished was the last one.
    if book_14_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">New skill unlocked: a 1 out of 2 chance of completing an additional chapter when doing paperwork."

        $ speedwriting += 1
        $ book_14_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                 
            
    
######################################
### BOOK 15 ########################## "\"Speedwriting for advanced.\"" # 1/4 chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_15:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book15], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book15]..."
   
    call chap_finished_15 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_15 #Checks if the chapter just finished was the last one.
            
  
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_15
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_15
            
#===#############################################
    
    call chapter_check_book_15 #Checks if the chapter just finished was the last one.
   
   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_15
            call chapter_check_book_15 #Checks if the chapter just finished was the last one.

    
    ">There are still some chapters left."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_15: 
    $ book_15_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_15_units]\" of the book."
    return
    
###
label chapter_check_book_15: #Checks if the chapter just finished was the last one.
    if book_15_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You have become a true master of speedwriting and from now on you shall always complete an additional chapter when doing paperwork."
        #">New skill unlocked: a decent chance of completing an additional chapter when doing paperwork."

        $ speedwriting += 1
        $ book_15_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                 
                
######################################
### BOOK 16 ########################## "\"Speedwriting for experts.\"" # 1/2 chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_16:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book16], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book16]..."
   
    call chap_finished_16 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_16 #Checks if the chapter just finished was the last one.
            
    
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_16
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_16
            
#===#############################################
    
    call chapter_check_book_16 #Checks if the chapter just finished was the last one.

   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_16
            call chapter_check_book_16 #Checks if the chapter just finished was the last one.
       
    
    ">There are still some chapters left."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_16: 
    $ book_16_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_16_units]\" of the book."
    return
    
###
label chapter_check_book_16: #Checks if the chapter just finished was the last one.
    if book_16_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">That was the last chapter. You finished the entire book."
        ">New skill unlocked: a big chance of completing an additional chapter when working."
       
        $ speedwriting += 1
        $ book_16_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                 
                
                
######################################
### BOOK 17 ########################## "\"Speedwriting for maniacs.\"" # 1 (sure) chance of it to pop up. Completes extra chapter during work.
######################################
label reading_book_17:
    
    call reading_block
    
    hide screen gift
    if fire_in_fireplace:
        call fire_in #Shows Genie reading a book near the fireplace.
    else:
        call fire_out #Shows Genie reading a book near the window.

    if raining:
        ">You read a book called [book17], while listening to the sound of raindrops bombarding the roof of your tower."
    else:
        ">You read a book called [book17]..."
   
    call chap_finished_17 #Basicly $ book_04_units +=1 and "Chapter completed" message.
    
    call chapter_check_book_17 #Checks if the chapter just finished was the last one.
            
 
    
#===### SPEED READING FOR DUMMIES BONUS CHECK ###
    if s_reading_lvl == 1: #First book (book_08) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 6) 
        #$ speed_dummies = 1 #Here for testing porpoise only.
        if speed_dummies == 1: #Success.
            call yes_book_08 #DON'T CHANGE! KEEP IT 08. Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_17
            
    if s_reading_lvl == 2: #Second book(book_09) on speed reading completed.
        $ speed_dummies = renpy.random.randint(1, 3) 
        if speed_dummies == 1: #Success.
            call yes_book_09 #DON'T CHANGE! KEEP IT 09 Message you see that says you are completed one more chapter because of the "Speed reading for dummies" book.
            call chap_finished_17
            
#===#############################################
    
    call chapter_check_book_17 #Checks if the chapter just finished was the last one.
    
   
    if raining:
        if not fire_in_fireplace:
            call no_fire #Message you see that says you are reading a book during rain.
        else:
            call yes_fire #Message you see that says you are reading a book during rain near fireplace.
            call chap_finished_17
            call chapter_check_book_17 #Checks if the chapter just finished was the last one.
        
    
    ">There are still some chapters left."
    if fire_in_fireplace:
        hide screen reading_near_fire
    else:
        hide screen reading

    if daytime:
        jump night_start
    else: 
        jump day_start
        
######    
label chap_finished_17: 
    $ book_17_units +=1 
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">You've completed \"chapter [book_17_units]\" of the book."
    return
    
###
label chapter_check_book_17: #Checks if the chapter just finished was the last one.
    if book_17_units == 10:
        if fire_in_fireplace:
            show screen done_reading_02
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">It was the last chapter. You finished the entire book."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        hide screen notes
        show screen notes
        ">You have become a true master of speedwriting and from now on you shall always complete an additional chapter when doing paperwork."

        $ speedwriting += 1
        $ book_17_complete = True
        
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return                     
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
        
 
     
    
    
    
            
    
    
        
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
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
    
    
### READING GALADRIEL BOOKS IN PROPER ORDER ###
label gal_proper:
    m "Reading books out of order won't do me any good."
    hide screen gift
    return
    
    
    
