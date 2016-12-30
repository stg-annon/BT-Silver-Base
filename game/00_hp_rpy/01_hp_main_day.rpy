
###DAY STARTS HERE###<<<<<<<<<<<<<<<<<<<-----------------------------------------------------------------------------------###
###========================================================================================================================###
label day_start:

$ daytime = True #True when it is daytime. Turns False during nighttime.

show screen blkfade
with d3

### MUSIC/SOUNDS ###
stop bg_sounds #Stops playing the fire SFX.
stop weather_sound #Stops playing the rain SFX.
play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME

### WEATHER
$ weather_gen = renpy.random.randint(1, 6)
$ show_weather()


hide screen genie
hide screen owl
hide screen owl_02
hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.

hide screen room

#show image im.Alpha("01_hp/01_bg/01_main_room.png", 0.5) #Transparent Background.
show screen room #Showing main room BG.
show screen genie

hide screen done_reading
hide screen done_reading_02

### CLEANUP ANY LEFTOVER SCREENS ###
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.


call reset_hermione_main


hide screen blkfade

$ hermione_sleeping = False
$ hermione_takes_classes = False
$ snape_busy = False
$ fire_in_fireplace = False

### EVENTS RELATED FLAGS ###
$ days_without_an_event +=1

### MENU PLACEMENT ###
$ menu_x = 0.5 #Just to make sure that menu is displayed in the center of the screen by default.

$ flip = False
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.

$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
$ gifted    = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ searched  = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
$ temp_name = "Day - "+str(day)+"\nWhoring - "+str(whoring)
$ save_name = temp_name


### RESETING STUFF ###
call luna_day_flags
$ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.
$ only_upper    = False #When true, legs are not displayed in the hermione_main screen.
$ only_upper    = False #When False legs are displayed in the hermione_main acreen.
$ autograph     = False #Displays professor Lockhart's autograph on Hermione's leg.
$ no_blinking   = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm    = False #Shows cum stains on Hermione's uniform.
$ uni_sperm     = False

$ day_random = renpy.random.randint(0, 10)


if whoring >=  0 and whoring <  3:
    $ level = "01"
if whoring >=  3 and whoring <  6:
    $ level = "02"
if whoring >=  6 and whoring <  9:
    $ level = "03"
if whoring >=  9 and whoring < 12:
    $ level = "04"
if whoring >= 12 and whoring < 15:
    $ level = "05"
if whoring >= 15 and whoring < 18:
    $ level = "06"
if whoring >= 18 and whoring < 21:
    $ level = "07"
if whoring >= 21 and whoring < 24:
    $ level = "08"
if whoring >= 24 and whoring < 27:
    $ level = "09"
if whoring >= 27 and whoring < 30:
    $ level = "10"
if whoring >= 12 and not touched_by_boy and not force_unlock_pub_favors: #Turns true if sent Hermione to get touched by a boy at least once.
    $ lock_public_favors = True #Turns True if reached whoring level 05 while public event "Touched by boy" never attempted. Locks public events.


$ generating_snape_bonus = renpy.random.randint(1, 2) #Determines whether ot not Snape bonus will be added to the Slytherin house.
$ generating_points = renpy.random.randint(1, 2) #Determines whether or not point will be awarded to Slytherin on this day. # MAKE NO CHANGES HERE. BEING USED AS "ONE_OUT_OF_TWO".
$ generating_points_gryffindor = renpy.random.randint(1, 10) #Addying point to Gryffindor (07_points_gry.rpy)
$ generating_points_hufflepuff = renpy.random.randint(1, 10) #Addying point to Hufflepuff (07_points_gry.rpy)
$ generating_points_ravenclaw = renpy.random.randint(1, 10) #Addying point to Ravenclaw (07_points_gry.rpy)

$ one_out_of_three = renpy.random.randint(1, 3) #Generating one number out of three for various porpoises.
$ i_of_iv = renpy.random.randint(1, 4) #Generating one number out of three for various porpoises.
$ one_of_five = renpy.random.randint(1, 5) #Generating one number out of three for various porpoises.
$ i_of_vii = renpy.random.randint(1, 7)
$ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
$ one_of_tw = renpy.random.randint(1, 20) #Generating one number out of three for various porpoises.


### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True #When TRUE the paycheck is in the mail. Can't do paper work.
        $ letterQ.send("","finished_report") #Adds one letter in waiting list to be read. Displays owl with envelope.
$ day_of_week += 1

    
### ODDITIES/LETTERS ####
if deliveryQ.got_mail() or letterQ.got_mail():
    play sound "sounds/owl.mp3"  #Quiet...
    
### DAY MAIL ###
if day == 1:
    $ letterQ.send("{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}","hermione_letter_1")
if day == 2:
    $ letterQ.send("{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}","hermione_letter_2")   
if day >= 12 and not reports_unlocked: # LETTER THAT UNLOCKS PAPERWORK BUTTON.
    $ letterQ.send("{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nWe remind you that only upon providing us with a completed report we will be able to make a payment in your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}","unlock_reports")
if outfit_order_placed and not outfit_ready:
    call outfit_purchase_check

#hide screen statistics
#show screen statistics

hide screen points
show screen points
with fade

### HERMIONE ###
if mad > 0:
    $ mad -= 1

$ day +=1
$ deliveryQ.transit_decrement()


if skip_duel == True:
    $ day = 5
    $ bird_examined = True 
    $ desk_examined = True
    $ cupboard_examined = True 
    $ door_examined = True
    $ fireplace_examined = True
    $ skip_duel = False
    
### EVENTS
call day_event_check
    
call Day_Request_Block
    
if collar == 5:
    jump collar_scene

    
    

label day_main_menu:

if day == 1 and daytime and bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
    show screen bld1
    with d3
    m "It's getting darker already..."
    m "Did I just spend an entire day with examining this room?"
    hide screen bld1
    with d3
    jump night_start

# show screen animation_feather
call screen main_menu_01
