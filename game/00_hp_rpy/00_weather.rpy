init python:
    def show_weather():
        global weather_animations
        global weather_gen
        global raining
        raining = False
        weather_animations = []
        lighting_gen = renpy.random.randint(1, 2)
        if weather_gen == 5 or (weather_gen == 4 and lighting_gen == 1):
            weather_animations.append("lightening")
        if weather_gen > 4:
            raining = True
            weather_animations.append("rain")
            renpy.music.play("sounds/rain.mp3", "weather_sound", fadeout=1.0, fadein=1.0)
        renpy.show_screen("weather")
    
    def hide_weather():
        renpy.hide_screen("weather")
    
init -2:
    transform cloud_move: #http://www.renpy.org/wiki/atl
        xpos 548
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

        linear 15.0 xpos 190 # linear
        pause 7
        repeat
    
    transform cloud_night_move_01: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 548
        choice:
            ypos 130
        choice:
            ypos 150
        choice:
            ypos 150
        linear 30.0 xpos 190 # linear
        pause 2
        repeat

    transform cloud_night_move_02: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 548
        choice:
            ypos 150
        choice:
            ypos 170
        linear 70.0 xpos 190 # linear
        pause 2
        repeat

    transform cloud_night_move_03: #CLOUD NIGHT 01. http://www.renpy.org/wiki/atl
        xpos 548
        ypos 160
        linear 50.0 xpos 190 # linear
        pause 2
        repeat
    
image rain: #Rain.
    "01_hp/07_weather/rain_01.png"
    pause.1
    "01_hp/07_weather/rain_02.png"
    pause.1
    "01_hp/07_weather/rain_03.png"
    pause.1
    repeat

image lightening: #Lightening during rain behind the window.
    pause 20
    "01_hp/07_weather/lightining_01.png"
    pause.1
    "01_hp/07_weather/lightining_02.png"
    pause.1
    "01_hp/07_weather/lightining_03.png"
    pause.1
    "01_hp/07_weather/lightining_04.png"
    pause.1
    "01_hp/07_weather/lightining_05.png"
    pause.1
    "01_hp/07_weather/lightining_06.png"
    pause.1
    "01_hp/07_weather/lightining_05.png"
    pause.1
    "01_hp/07_weather/lightining_06.png"
    pause.1
    "01_hp/07_weather/lightining_05.png"
    pause 20
    repeat
    
screen weather:
    zorder -1
    if daytime:
        if weather_gen < 5:# (cloud across sky)
            add "01_hp/07_weather/sky.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
            add "01_hp/07_weather/cloud_small.png" at cloud_move
        if weather_gen == 4:# (heavy clouds)
            add "01_hp/07_weather/cloudy.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 5:# (rain)
            add "01_hp/07_weather/cloudy.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 6:# (rain and lighting)
            add "01_hp/07_weather/cloudy.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
    else:
        ## Weather Types
        if weather_gen == 1:# (clear sky)
            add "01_hp/07_weather/night_sky.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 2:# (Clear sky with moon)
            add "01_hp/07_weather/night_sky_02.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 3:# (clouds across moon)
            add "01_hp/07_weather/night_sky_02.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
            add "01_hp/07_weather/night_cloud_02.png" at cloud_night_move_01
            add "01_hp/07_weather/night_cloud_01.png" at cloud_night_move_02
            add "01_hp/07_weather/night_cloud_03.png" at cloud_night_move_03
        if weather_gen == 4:# (heavy clouds)
            add "01_hp/07_weather/night_sky_04.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 5:# (rain)
            add "01_hp/07_weather/night_sky_04.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        if weather_gen == 6:# (rain and lighting)
            add "01_hp/07_weather/night_sky_04.png" at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
        
    for img in weather_animations:
        add img at Position(xpos=430, ypos=218, xanchor="center", yanchor="center")
    
    
    
    
    
