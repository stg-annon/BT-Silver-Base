

####NIGHT STARTS HERE###<<<<<<<<<<<-----------------------------------------------------------------------------------------------------###
###=====================================================================================================================================###
label night_start:
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC


###RESET STUFF
$ only_upper = False #When true, legs are not displayed in the hermione_main screen.
$ no_blinking = False #When True - blinking animation is not displayed.
$ sperm_on_tits = False #Sperm on tits when Hermione pulls her shirt up.
$ aftersperm = False #Shows cum stains on Hermione's uniform.
$ uni_sperm = False


call luna_night_flags
$ daytime = False
$ snape_busy = False
$ hermione_takes_classes = False
$ chitchated_with_snape = False #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
$ chitchated_with_her = False #Prevents you from chitchatting with Hermione more then once per time of day. Turns back to False every night. (And every day).
$ gifted = False #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.

stop bg_sounds #Stops playing the fire SFX.
stop weather #Stops playing the rain SFX.

scene black

hide screen blkfade
hide screen notes #A bunch of notes poping out with a "win" sound effect.
hide screen done_reading #Hiding genie sitting with closed book in his hands.
hide screen done_reading_02 #Done reading by the fire
hide screen new_window #Hiding clear sky bg.
hide screen cloud #THE CLOUD.

hide screen lightening #Hide lighting so it wouldn't get stuck during clear sky weather and such.
###WEATHER
if wather_generator >= 81 and wather_generator <= 90: # RAIN WITH LIGHTENING.
    show image "01_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation
elif wather_generator >= 1 and wather_generator <= 30: #Clear sky with stars.
    show image "01_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 41 and wather_generator <= 50: #Clear sky with stars 02. (floating cloud during the day).
    show image "01_hp/07_weather/night_sky.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 31 and wather_generator <= 40: #CLEAR FULL MOON.
    show image "01_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")# CLEAR WEATHER.

elif wather_generator >= 51 and wather_generator <= 60: #FULL MOON WITH CLOUDS
    show screen cloud_night_01
    show screen cloud_night_02
    show screen cloud_night_03
    show image "01_hp/07_weather/night_sky_02.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")

elif wather_generator >= 61 and wather_generator <= 80: #HEAVY CLOUDS.
    show image "01_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    $ lighting_generator = renpy.random.randint(1, 2)
    if lighting_generator == 1:
        show lightening at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Lighting

elif wather_generator >= 91 and wather_generator <= 100: #RAIN.
    show image "01_hp/07_weather/night_sky_04.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Cloudy background
    show rain at Position(xpos=290, ypos=218, xanchor="center", yanchor="center") #Rain animation





if package_is_here:
    hide screen package
hide screen room #Hiding main room BG.
show screen room_night #Showing main room NIGHT BG.
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

show screen door
show screen cupboard
show screen chair
show screen fireplace
show screen phoenix
show screen candle_01
show screen candlefire_01 #CANDLE FIRE.
show screen candle_02
show screen candlefire_02 #CANDLE FIRE.
if package_is_here:
    show screen package
show screen genie

#hide screen statistics
#show screen statistics

hide screen points
show screen points

if got_mail or mail_from_her or letters >= 1:
    show screen owl
with fade







call points_changes #Makes changes in the Slytherin house points.
call points_changes_gryffindor #Makes changes in the Gryffindor (And the rest of the houses) house points. (07_points_gry.rpy)
# call snape_bonus # Not in use anymore.

### NIGHT REQUESTS ###
call Night_Request_Block


call c_r_night


label night_resume:

### NIGHT EVENTS ###
if day == 1:
    call event_02
if day == 2:
    call event_03
if day == 4:
    call event_05
if day == 5:
    call event_07
if days_without_an_event == 1 and hermione_is_waiting_02 and not event11_happened:
#if day == 6:
    call event_11
if days_without_an_event == 1 and event11_happened and not event12_happened:
#if day == 7:
    call event_12
if days_without_an_event == 1 and event12_happened and not event13_happened:
#if day == 8:
    call event_13
if day >= 15 and day <=20 and not event15_happened:
#if day == 9:
    call event_15

if gave_the_dress and days_without_an_event >= 2: #$ gave_the_dress = True #Turns True when Hermione has the dress.
    jump good_bye_snape















label night_main_menu:


if phoenix_is_feed:
    show screen phoenix_food

show screen animation_feather
call screen main_menu_01
