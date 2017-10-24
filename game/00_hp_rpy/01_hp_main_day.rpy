
###DAY STARTS HERE###<<<<<<<<<<<<<<<<<<<-----------------------------------------------------------------------------------###
###========================================================================================================================###
label day_start:

    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY THEME

call reset_hermione_main

$ flip = False
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.

$ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
$ gifted    = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
$ searched  = False #Turns true after you search the cupboard. Turns back to False every day. Makes sure you can only search the cupboard once a day.
$ temp_name = "Day - "+str(day)+"\nWhoring - "+str(whoring)
$ save_name = temp_name

### MENU PLACEMENT ###
$ menu_x = 0.5 #Just to make sure that menu is displayed in the center of the screen by default.

### RESETING STUFF ###
call luna_day_flags
$ only_upper    = False #When true, legs are not displayed in the hermione_main screen.
$ autograph     = False #Displays professor Lockhart's autograph on Hermione's leg.
$ no_blinking   = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm    = False #Shows cum stains on Hermione's uniform.
$ uni_sperm     = False

$ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.
$ only_upper = False #When False legs are displayed in the hermione_main acreen.
$ day_random = renpy.random.randint(0, 10)


stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

hide screen blkfade
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen phoenix_food
hide screen done_reading
hide screen done_reading_02
hide screen candlefire_01 #CANDLE FIRE.
hide screen candlefire_02 #CANDLE FIRE.
hide screen lightening #Hide lighting so it won't get stuck during clear sky weather and such.
hide screen cloud_night_01 #NIGHT CLOUDS.
hide screen cloud_night_02 #NIGHT CLOUDS.
hide screen cloud_night_03 #NIGHT CLOUDS.
hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.

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
else:
    $ lock_public_favors = False


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

### CUPBOARD MONEY GENERATOR ###

$ gold1 = renpy.random.randint(1, 10) # Money you find in the cupboard when Whoring Level: 1-2.
$ gold2 = renpy.random.randint(10, 40) # Money you find in the cupboard when Whoring Level: 3-4.
$ gold3 = renpy.random.randint(20, 50) # Money you find in the cupboard when Whoring Level: 5-6.
$ gold4 = renpy.random.randint(30, 90) # Money you find in the cupboard when Whoring Level: 7+.



$ daytime = True #True when it is daytime. Turns False during nighttime.
$ hermione_sleeping = False
$ hermione_takes_classes = False
$ snape_busy = False
$ fire_in_fireplace = False
hide screen fireplace_fire

### EVENTS RELATED FLAGS ###
$ days_without_an_event +=1


### PAPERWORK (MONEY-MAKING) RELATED FLAGS ###
if day_of_week == 7: #Counts days of the week. Everyday +1. When day_of_week = 7 resets to zero.
    $ day_of_week = 0
    if finished_report >= 1:
        $ got_paycheck = True #When TRUE the paycheck is in the mail. Can't do paper work.
        $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        #$ got_mail = True comented out because being replaced with $ letters += 1
$ day_of_week += 1

### HERMIONE ###
if mad >= 1:
    $ mad -= 1



### MUGGLE ODDITIES RELATED FLAGS ###
#if order_placed: #TRUE when and order has been placed on an item.
#    $ days_in_delivery +=1
#    if days_in_delivery >= 3: # BY DEAFULT WAS 5. Changed for testing.
#        $ package_is_here = True
#        $ order_placed = False


if deliveryQ.got_mail():
    $ package_is_here = True


### MUGGLE ODDITIES RELATED FLAGS ### VERSION TWO. This one randomizes delivery waiting days.
# if order_placed: #TRUE when and order has been placed on an item.
    # $ days_in_delivery2 -=1
    # if days_in_delivery2 <= 0 or next_day:
        # $ next_day = False
        # $ package_is_here = True
        # $ order_placed = False



scene black
$ raining = False #No rain before the weather has been chosen at the beginning of every day.
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.


$ wather_generator = renpy.random.randint(1, 100)
#$ wather_generator = 99 #THIS LINE IS FOR TESTING. 99 = Rain.
if wather_generator >=  1 and wather_generator < 41: # CLEAR WEATHER.
    show screen new_window #<<<------------------------------------------!!!!!!!!!!!
    #show image "01_hp/01_bg/03_weather.png"
elif wather_generator >= 41 and wather_generator < 61: # Floating cloud
    show screen new_window #<<<------------------------------------------!!!!!!!!!!!
    show screen cloud #THE CLOUD.
    #show image "01_hp/01_bg/03_weather.png"
    #show cloud_01 at Position(xpos=280, ypos=215, xanchor="center", yanchor="center")
elif wather_generator >= 61 and wather_generator < 81: # CLOUDY WEATHER
    show image "01_hp/07_weather/cloudy.png" at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 81 and wather_generator < 91: # RAIN
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "01_hp/07_weather/cloudy.png" at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 91 and wather_generator < 101: # RAIN WITH LIGHTENING.
    #play weather "sounds/rain.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ raining = True
    show image "01_hp/07_weather/cloudy.png" at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290+140, ypos=218, xanchor="center", yanchor="center") #Rain animation


#show image im.Alpha("01_hp/01_bg/01_main_room.png", 0.5) #Transparent Background.




hide screen room_night #Hiding NIGHT BG from last night.
show screen room #Showing main room BG.

hide screen door
hide screen cupboard
hide screen chair
hide screen fireplace
hide screen phoenix
hide screen candle_01
hide screen candle_02
hide screen genie
hide screen owl
hide screen owl_02
hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.
if package_is_here:
    hide screen package


show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candle_02



### DAY MAIL ###
if day == 2:
    $ letter_from_hermione_02 = True #Turns true when you get second letter from Hermione.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if day == 12: # LETTER THAT UNLOCKS PAPERWORK BUTTON.
    $ work_unlock = True # Send a letter that will unlock an ability to write reports.
    $ letters += 1 #Adds one letter in waiting list to be read. Displays owl with envelope.

if outfit_order_placed and not outfit_ready:
    call outfit_purchase_check

if package_is_here:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen package
show screen genie

if got_mail or mail_from_her or letters >= 1:
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl




#hide screen statistics
#show screen statistics

hide screen points
show screen points

with fade

$ day +=1


### EVENTS

#NOT IN USE if day == 4: #Genie says: "I wonder what has become of that two-faced dude?"
#About two-faced dude    call event_04

if day == 8:
    call event_08 #Hermione shows up for the first time.
if day >= 9 and hermione_is_waiting_01 and not event09:
    call event_09 #Second visit from Hermione. Says she sent a letter to the Minestry.
                  #Takes place after first special event with Snape, where he just complains about Hermione.
if event13_happened and not event14_happened:
    call event_14

if whoring >= 15 and not event_chairman_happened: #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
    call want_to_rule

if whoring >= 15 and event_chairman_happened and days_without_an_event >= 2 and not snape_against_chairman_hap: # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
    call against_the_rule

if whoring >= 18 and days_without_an_event >= 5 and snape_against_chairman_hap and not have_no_dress_hap: #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
    call crying_about_dress # 27_final_events

if whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics and days_without_an_event >= 1: # Turns TRUE after Hermione comes and apologizes for the day (event) before.
    call sorry_about_hesterics

#HAT EVENT
if whoring >= 21 and not hat_known:
    call hat_intro

### NOT IN USE
#if day == 10:
#    call event_08_02 #Hermione shows up for the second time. (Shorter skirts notion).
#if day == 11:
#    call event_08_03 #Hermione shows up for the third time. (Rules for teachers noton).
if day >= 12 and not event09 and hermione_is_waiting_01:
    call event_09 #Visit from Hermione after first Special event with Snape (Where Genie proposes plan against her).
### NOT IN USE
#if day >= 13 and not event10 and hermione_is_waiting_02:
#    call event_10 #Hermione shows up for the third time. Says that she started "MRM" and sent letter to the ministry.
if event13_happened and not event14_happened:
    call event_14

if skip_duel == True:
    $ day = 5
    $ bird_examined = True 
    $ desk_examined = True
    $ cupboard_examined = True 
    $ door_examined = True
    $ fireplace_examined = True
    $ skip_duel = False
    
### EVENTS ### (COMMENTED OUT FOR THE TESTING PORPOISES) ===============================================================================================================================
if day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined:
    call event_01


if collar == 5:
    jump collar_scene


call Day_Request_Block

label day_main_menu:


if phoenix_is_feed:
    show screen phoenix_food
    

if day == 1 and daytime and bird_examined and desk_examined and cupboard_examined and door_examined and fireplace_examined:
    show screen bld1
    with d3
    m "It's getting darker already..."
    m "Did I just spend an entire day with examining this room?"
    hide screen bld1
    with d3
    jump night_start

show screen animation_feather
call screen main_menu_01
