label hp:
    stop music fadeout 1
#    $ select = renpy.imagemap("screens/s2pot04.png", "screens/s2pot04b.png", [
#                                            (492, 400, 637, 600, "no"),
#                                            (647, 400, 799, 600, "yes"),
#                                                ])
#    if select == "no":
#        jump fromcsoon
#    if select == "yes":
#        pass

    show screen blkfade

    show image "01_hp/01_bg/00.png"
    pause.1
    scene blkfade
    show image "01_hp/01_bg/00.png"
    hide blkfade with Dissolve(.3)
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    hide screen blkfade
    show magic5
    pause.05
    scene white
    pause.05
    pause.05
    scene white
    pause.05
    show image "01_hp/01_bg/00.png"
    show whitefade at basicfade, center
    #show magic at basicfade, center
    #show magic2 at basicfade2, center
    show magic3 at basicfade3, center
    #show magic4 at basicfade4, center # OVAL
    hide magic
    hide magic2
    hide magic3
    hide magic4
    #hide whitefade
    show heal
    stop music fadeout 1
    pause 1
    hide whitefade
    with d3
    pause 1






###THE GAME STARTS###
$ day = 0



### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
$ day_of_week = 0 #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
$ report_chapters = 0 #Shows how many chapters of a current report has been completed so far. Resets to zero when report is finished.
$ finished_report = 0 #Shows amount of completed reports.

$ got_mail = False #Turns true is you have WORK mail waiting. Owl will be displayed.
$ got_package = False #Turns TRUE when package from the "Muggle Oddities" catalog has arrived.
$ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
$ mail_from_her = False #Turns TRUE when there is a mail from Hermione. Basically the same as $ got_mail = True.
$ letter_text = []
$ letters = 0 #Shows how many letters are waiting to be read. +1 every new letter arrives. -1 Every time you read one letter.

### GETTING LETTERS ###
$ letter_from_hermione_02 = False #Turns true when you get second letter from Hermione.

###SNAPE STATS###
$ snape_busy = False #When True, you can't summon Snape.
$ snape_friendship = 0 #Get's +1 after every evening spent is Snape's company.
$ snape_events = 0 #Get's +1 point every time a special event with Snape happens.


$ level = "00" #Hermione's whoring level.

$ hermione_takes_classes = False #Turns True when Hermione becomes unavailable for summon after performing personal request in the morning.
$ hermione_sleeping = False



$ tutoring_events = 0 #Get's +1 point every time a tutoring special event happens.
$ knowledge = 0
$ whoring = 0 #Default: 0
$ teachers_pet = 0
$ classmates_pet = 0
$ being_mean = 0 #+1 every time you are being mean to hermione.



$ dates = 0 #Tracks how many times Hermione been tutored.

### default position of table ###
$ table_position_x = 0
$ table_position_y = 0

### PATH SHORTCUTS ###
$ hg_pth = "01_hp/13_characters/hermione/"

### CHITCHATS WITH SNAPE ###
$ chitchat_event_01_happened = False
$ chitchat_event_02_happened = False
$ chitchat_event_03_happened = False
$ chitchat_event_04_happened = False
$ chitchat_event_05_happened = False
$ chitchat_event_06_happened = False
$ chitchat_event_07_happened = False


### SPECIAL DATES WITH SNAPE ###

$ date_with_snape_02_happened = False #Second date with Snape. They decide to de-throne Hermione.
                                      #Turns true after event_09

###Miscellaneous flags###
$ hold_all_the_events_please = False #When TRUE all the story events will be put on hold.
$ jerk_off_session = False #Turns True when you choose to jerk off while Hermione talks (Event_08)

$ tutoring_offer_made = False #If you offered her to tutor her (In event_12). Affects conversation in the next event.

$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night.


$ snape_against_hermione = False #Turns True after event_01. Activates event_11 when hanging out with Snape next time.
$ snape_against_hermione_02 = False #Turns True after event_09. Activates second event when hanging out with Snape.

$ hermione_is_waiting_01 = False #Turns True at the end of first special event with Snape. Triggers next visit from Hermione (event_09)
$ hermione_is_waiting_02 = False #Turns True at the end of second special event with Snape. Triggers next visit from Hermione

$ phoenix_is_feed = False #When True the graphic of bird food being displayed on top of the phoenix food can.
$ fire_in_fireplace = False #When True there is a fire going in the fireplace.

$ summoning_hermione_unlocked = False #Unlocks after event_14. Adds "Summon Hermione" button to the door.
$ tutoring_hermione_unlocked = False #Unlocks after event_14.
$ buying_favors_from_hermione_unlocked = False


$ hanging_with_snape = False #Turns true when "hanging with Snape during the night time" becomes available. (Snape becomes available for summons).
$ have_catalogue = False #Turns True when you obtain "The muggle oddities" catalog. (The button shows).


$ gifts12 = []

$ hermione_desperate_done = False
$ fawkes_intro_done = False


### GENIE STATS ###============================
$ job_lvl = 1 #Show how many reports you are allowed to complete per week.
### ===========================================


### MUGGLE ODDITIES ### =========================================================================
$ order_placed = False #TRUE when and order has been placed on an item.
$ days_in_delivery = 0 # +1 day, every day since the orer has been made (when order_placed = True).
$ days_in_delivery2 = 0 # +1 day, every day since the orer has been made (when order_placed = True).
$ package_is_here = False # Turns true when days_in_delivery >= 5. Package is displayed.


#hg = hermione granger
#pf = personal favor (sexual)
#pr = public request
#ps = public shaming


### LEVELING UP ###

# Hermione levels
$ hg_whoring = 0
$ hg_whoring_lvl = 0



    
#Flirt with 3 classmates.
#Flirt with a teacher.
#(Goes to class without panties).
#(Flash panties to a classmate).
#(Flash panties to a teacher).
#(Flash a nipple to a classmate).
#(Wear a see-through shirt to class).
#(Flash a nipple to a teacher).
#(Grab a classmate's cock).
#(Jerk off on tits and put the clothes back on).
#(Give handjob to a classmate).
#(Flash your tits to a teacher).
#(Cum on face and send to class).
#(Go to class with mouth full of cum).
#(Blow two classamates).
#(Handjob to a teacher).
#(Blowjob to a teacher).
#(Put on a slutty dress and go to classes).
#(Go to classes with cum covered face).

###MITTY TEST VARS###
$ request_jeans = False
$ hermione_dribble = False
$ request_gryyf_stockings = False
$ dribble_equippable = False
$ hermione_wetpanties = False
$ wetpanties_equippable = False

# EVENTS #==============================================================================================================================================
### EVENT 01 ####
$ desk_examined = False #Turns True when you did examine you desk on day one.
$ cupboard_examined = False
$ bird_examined = False
$ door_examined = False
$ fireplace_examined = False
$ bought_glasses = False
$ glasses_worn = False
$ legs_03 = False
$ micro_skirt = False
$ glasses = False
$ hair_color = 0
$ wear_shirts = True
$ wear_bra = False
$ badges = True
$ collar = 0
$ custom_01_worn = False
$ custom_02_worn = False
$ custom_03_worn = False
$ custom_04_worn = False
$ custom_05_worn = False
$ custom_06_worn = False
$ custom_07_worn = False
$ custom_08_worn = False
$ custom_09_worn = False
$ custom_10_worn = False
$ scene_number = 1
$ cust_char_1_enabled = False
$ cust_char_2_enabled = False
$ cust_char_3_enabled = False
#Custom Variables Previously Defined at desk
$ current_job = 0
$ custom_breast = 0
$ custom_bra = 0
$ pitch_open = True
$ maid_working_unlocked = True
$ inn_first = True
$ stockings = 0
$ attic_open = False
$ custom_outfit_old = 0
$ show_attic = True
$ show_clothes_store = True
$ clothes_intro_done = False
$ show_forest = True
$ show_inn = True
$ show_pitch = True
$ tentacle_cosmetic = False
$ maid = True
$ cheerleader = True
$ custom_skirt = False
$ custom_shirt = False
$ transparency = 1
$ genie_name = "sir"
$ hermione_name = "miss granger"
$ tent_scroll = False
$ v_tutoring = 0
$ hermione_desperate_done = False
$ bought_glasses = False
$ glasses_worn = False
$ legs_03 = False
$ micro_skirt = False
$ glasses = False
$ ears = False
$ wear_shirts = True
$ gave_tinyminiskirt = False
$ wear_bra = False
$ scene_number = 1
$ shirt_random = 1
$ badges = True
$ collar = 0
$ cust_char_1_enabled = False
$ cust_char_2_enabled = False
$ cust_char_3_enabled = False
$ fawkes_intro_done = True
$ custom_outfit_1_bought = False
$ custom_outfit_2_bought = False
$ custom_outfit_3_bought = False
$ custom_outfit_4_bought = False
$ cs_existing_stock = [False,False,False,False,False]
$ addicted = False
$ freckles = False
$ lift_shirt = False
$ book_hold = False
$ skirt_up = False
$ panties = True
$ temp_panties = True
$ fingering = False
$ robe = 0
###DEFINE LUNA
call luna_init

###SCREENS### NO NEED FOR THIS ONE ANYMORE. (SHOWS WHORING THOUGH).
screen statistics: #http://www.renpy.org/doc/html/screens.html
    hbox: 
        spacing 10 xpos 630 ypos 2
        text "{size=-3}Day: [day]\nWhoring: [whoring]\nLevel: [level]\nKnowledge: [knowledge]\nSlytherin [slytherin]\nGryffindor [gryffindor]\nS.Freind: [snape_friendship]\nDay of week: [day_of_week]\nConcentration: [concentration]\nSpeedwriting: [speedwriting]{/size}" #сумма текстом



jump day_start


pause
show ch_hem 01 at Position(xpos=732, ypos=350, xanchor="center", yanchor="center")
pause


show ch_hem walk_a at Move((732, 350), (300, 350), 5.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)
pause 5.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause

show ch_hem run_f at Move((300, 350), (732, 350), 2.0,
                  xanchor="center", yanchor="center") with Dissolve(.1)

pause 2.0

show ch_hem blink at Position(xpos=300, ypos=350, xanchor="center", yanchor="center") with Dissolve(.1)
pause










### INIT ###

init -2:

    $ l_blush = False # Turns on blushing in the l_head screen. (Lola).
    $ l_things = False # Turns on cheerful emotion symbol in l_screen. (Lola).
    $ l_question = False # Turns on question mark emotion symbol in l_screen. (Lola).
    $ l_drop = False # Turns on drop emotion symbol in l_screen. (Lola).
    $ l_hearts = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_exclamation = False # Turns on hearts emotion symbol in l_screen. (Lola).
    $ l_tears = False # Turns on tears in l_screen. (Lola).

    $ config.autoreload = False
    
    transform universal_chibi_walk(x,x2,speed,y): #Universal transform for all chibis
        xpos x
        ypos y
        linear speed xpos x2 # linear
    
    transform custom_walk_02(x,x2): #Same custom walk but for Hermione.
        xpos x
        ypos 250
        linear hermione_speed xpos x2 # linear

    transform custom_walk(x,x2): # http://www.renpy.org/wiki/atl 
        xpos x
        ypos 210
        linear snape_speed xpos x2 # linear
        
    transform genie_walk(x,x2): #http://www.renpy.org/wiki/atl 
        xpos x
        ypos 260
        linear snape_speed xpos x2 # linear
        


    transform cloud_move: #http://www.renpy.org/wiki/atl
        xpos 408
        choice:
            ypos 150
        choice:
            ypos 160
        choice:
            ypos 170
        choice:
            ypos 190
        choice:
            ypos 200

        linear 15.0 xpos 50 # linear
        pause 7
        repeat


    transform cloud_night_move_01: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408
        choice:
            ypos 130
        choice:
            ypos 150
        choice:
            ypos 150
        linear 30.0 xpos 50 # linear
        pause 2
        repeat

    transform cloud_night_move_02: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408
        choice:
            ypos 150
        choice:
            ypos 170
        linear 70.0 xpos 50 # linear
        pause 2
        repeat

    transform cloud_night_move_03: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 408
        ypos 160
        linear 50.0 xpos 50 # linear
        pause 2
        repeat
