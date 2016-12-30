
####NIGHT STARTS HERE###<<<<<<<<<<<-----------------------------------------------------------------------------------------------------###
###=====================================================================================================================================###
label night_start:

$ daytime = False #True when it is daytime. Turns False during nighttime.

show screen blkfade
with d3

### MUSIC/SOUNDS ###
stop bg_sounds #Stops playing the fire SFX.
stop weather_sound #Stops playing the rain SFX.
play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC

### WEATHER ###
$ show_weather()

hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen done_reading #Hiding genie sitting with closed book in his hands.
hide screen done_reading_02 #Done reading by the fire

hide screen blkfade

###RESET STUFF
$ only_upper = False #When true, legs are not displayed in the hermione_main screen.
$ no_blinking = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm = False #Shows cum stains on Hermione's uniform.
$ uni_sperm = False

call luna_night_flags
$ snape_busy = False
$ hermione_takes_classes = False
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.


show screen room #main room BG.
hide screen genie
hide screen owl
hide screen owl_02

show screen genie

#hide screen statistics
#show screen statistics

hide screen points
show screen points

with fade

call points_changes #Makes changes in the Slytherin house points.
call points_changes_gryffindor #Makes changes in the Gryffindor (And the rest of the houses) house points. (07_points_gry.rpy)
# call snape_bonus # Not in use anymore.

### NIGHT REQUESTS ###
call Night_Request_Block


call c_r_night


label night_resume:

call night_event_check

if gave_the_dress and days_without_an_event >= 2: #$ gave_the_dress = True #Turns True when Hermione has the dress.
    jump good_bye_snape

label night_main_menu:

call screen main_menu_01
