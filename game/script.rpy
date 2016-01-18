# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    $ init_variables()
    scene black
    call select_start
    return
 
label after_load:
    $ init_variables()
    return
 
    
init:
    
    $ commentaries = False # In the GALLERY turns commentaries ON and OFF.
    
    ### Disposable flags ###
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    $ d_flag_05 = False
    $ d_flag_06 = False
    $ d_flag_07 = False
    $ d_flag_08 = False
    $ d_flag_09 = False

    $ d_points = 0
    
    ### MENU PLACEMENT ###
    $ menu_x = 0.5
    
    $ who = Character('Female voice', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ whom = Character('Male voice', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    $ who2 = Character('???', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    $ aa = Character('AKABUR', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    $ teleport = ImageDissolve("id_teleport.png", 1.0, 0)
    
    $ renpy.music.register_channel("bg_sounds", "sfx", True)
    $ renpy.music.register_channel("weather", "sfx", True)

    # Define some new transitions here.
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbulb2 = Fade(1, 0.5, 1, color='#fff')
    $ flashbb = Fade(0.2, 0.0, 0.8, color='#000')
    $ flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
    $ kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')

    #NVLE STUFF
    $ nvle = Character(color="#000", what_color="#ffffff", kind=nvl)
    $ config.adv_nvl_transition = dissolve
    $ config.nvl_adv_transition = dissolve


    $ config.keymap['hide_windows'].remove('mouseup_2')
    $ config.keymap['hide_windows'].remove('h')
    #$ config.keymap['hide_windows'].remove('joy_hide')

#    init python:
#        def callback(event, **kwargs):
#            if event == "show":
#                renpy.music.play("beep5.mp3", loop="True", channel="sound")
#            elif event == "slow_done" or event == "end":
#                renpy.music.stop(channel="sound")

    # Define some new transitions here.
    $ flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    $ flashbb = Fade(0.2, 0.0, 0.8, color='#000')
    $ flashblood = Fade(0.2, 0.0, 0.8, color='#f02424')
    $ kissiris = Fade(0.2, 0.0, 0.8, color='#fb8dc8')
    $ black_magic = Fade(0.2, 0.0, 0.5, color='#7f3590')
    $ blackfade = Fade(0.9, 0.5, 1, color='#000000')

    
    # MUSIC / SOUNDS
    $ galm = "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3"
    $ JafarsHour = "music/JafarsHour.mp3"
    $ mark = "music/Marketplace.mp3"
    $ palace = "music/EasternJourneybyPike270.mp3"
    $ mrm = "music/PartOfYourWorld.mp3"
    $ wnd = "music/TheEasternWindbyroensb.mp3"
    $ kiss = "music/TheKiss.mp3"
    $ sillyc = "music/SillyCatbyMaverlyn.mp3"
    $ xf = "music/TheXFiles.mp3"
    $ freedom = "music/outlawstarostfreedom.mp3"
    $ palace2 = "music/GoingtoKillMe.mp3"
    $ title = "music/RollIntheLeaves.mp3"
    $ swat = "music/025SWAT.mp3"
    $ hemanmusic = "music/HeMan.mp3"
    
    
###TRANSITIONS###########
define d1 = Dissolve(0.1)
define d2 = Dissolve(0.2)
define d3 = Dissolve(0.3)
define d4 = Dissolve(0.4)
define d5 = Dissolve(0.5)
define d6 = Dissolve(0.6)
define d7 = Dissolve(0.7)
define d8 = Dissolve(0.8)
define d9 = Dissolve(0.9)


# Music
define ms_arabian_nights = "music/Arabian_Nights.mp3"
define ms_bushwick = "music/Bushwick_Tarantella_Loop.mp3"
define ms_croft_manor = "music/Croft_Manor.mp3"
define ms_dice_game = "music/Dice_Game.mp3"
define ms_gtkm = "music/Going_to_Kill_Me.mp3"
define ms_gorilla = "music/Gorilla_Theme.mp3"
define ms_india = "music/India's_Different.mp3"
define ms_jafar = "music/Jafar's_Hour.mp3"
define ms_kabul = "music/Kabul_Flight_Jumpstart.mp3"
define ms_manatees = "music/Music for Manatees.mp3"
define ms_marketplace = "music/Marketplace.mp3"
define ms_outlaw_star = "music/Outlaw_Star_Freedom.mp3"
define ms_ozone = "music/Ozone.ogg"
define ms_sleep_walking = "music/Sleep_Walking.mp3"
define ms_tension = "music/Tension.mp3"
define ms_the_calm_before = "music/The_Calm_Before.mp3"
define ms_the_eastern_wind = "music/The_Eastern_Wind.mp3"
define ms_the_kiss = "music/The_Kiss.mp3"
define ms_the_xfiles = "music/The_X-Files.mp3"
define ms_vision = "music/Vision.mp3"

# Sounds
define sd_boing1 = "sounds/boing.mp3"
define sd_boing2 = "sounds/boing02.mp3"
define sd_boing3 = "sounds/boing03.mp3"
define sd_burp = "sounds/burp.mp3"
define sd_door = "sounds/door.mp3"
define sd_door2 = "sounds/door2.mp3"
define sd_door3 = "sounds/door3.mp3"
define sd_fall = "sounds/fall.wav"
define sd_glitch = "sounds/gltch.mp3"
define sd_iris_run = "sounds/iris_run.mp3"
define sd_kungfupunch = "sounds/kung-fu-punch.mp3"
define sd_magic4 = "sounds/magic4.ogg"
define sd_monster = "sounds/mon.wav"
define sd_monster_dead = "sounds/mondead.wav"
define sd_pistol2 = "sounds/pistol2.mp3"
define sd_pop1 = "sounds/pop01.mp3"
define sd_pop2 = "sounds/pop02.mp3"
define sd_pop3 = "sounds/pop03.mp3"
define sd_punch1 = "sounds/punch01.mp3"
define sd_punch2 = "sounds/punch02.mp3"
define sd_rustling = "sounds/rustling.mp3"
define sd_scratch = "sounds/scratch.wav"
define sd_slap = "sounds/slap.mp3"
define sd_spit = "sounds/spit.mp3"
define sd_win2 = "sounds/win2.mp3"


## ANIMATIONS
        ### INTRO MOVIE ANIMATIONS ###
image title_ani: #Main title animation.
    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/13.png"
    pause.1
    "title/14.png"
    pause.1
    "title/13.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

### second cercle.
    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/02.png"
    pause.1
    "title/03.png"
    pause.1
    "title/04.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    "title/01.png"
    pause.1
    "title/13.png"
    pause.1
    "title/14.png"
    pause.1
    "title/13b.png"
    pause.1
    "title/05b.png"
    pause.1
    "title/06b.png"
    pause.1
    "title/07b.png"
    pause.1
    "title/08b.png"
    pause.1
    "title/09b.png"
    pause.1
    "title/10b.png"
    pause.1
    "title/11b.png"
    pause.1
    "title/12b.png"
    pause.1

    "title/01b.png"
    pause.1
    "title/02b.png"
    pause.1
    "title/03b.png"
    pause.1
    "title/04b.png"
    pause.1
    "title/05b.png"
    pause.1
    "title/06b.png"
    pause.1
    "title/07b.png"
    pause.1
    "title/08b.png"
    pause.1
    "title/09b.png"
    pause.1
    "title/10b.png"
    pause.1
    "title/11b.png"
    pause.1
    "title/12b.png"
    pause.1

    "title/01b.png"
    pause.1
    "title/13b.png"
    pause.1
    "title/14.png"
    pause.1
    "title/13.png"
    pause.1
    "title/05.png"
    pause.1
    "title/06.png"
    pause.1
    "title/07.png"
    pause.1
    "title/08.png"
    pause.1
    "title/09.png"
    pause.1
    "title/10.png"
    pause.1
    "title/11.png"
    pause.1
    "title/12.png"
    pause.1

    repeat

#############################################

image heal:
    "magic/heal01.png"
    pause.06
    "magic/heal02.png"
    pause.06
    "magic/heal03.png"
    pause.06
    "magic/heal04.png"
    pause.06
    "magic/heal05.png"
    pause.06
    "magic/heal06.png"
    pause.06
    "magic/heal07.png"
    pause.06
    "magic/heal08.png"
    pause.06
    "magic/heal09.png"
    pause.06
    "magic/heal10.png"
    pause.06
    "magic/heal11.png"
    pause.06
    "magic/heal12.png"
    pause.06
    "magic/heal13.png"
    pause.06
    "magic/heal14.png"
    pause.06
    "magic/heal15.png"
    pause.06
    "magic/heal16.png"
    pause.06
    "magic/heal17.png"
    pause.06
    "magic/heal18.png"
    pause.06

############################################
#######EMOTIONS #^_^# ########################
############################################

image emo01:
    "01_hp/06_emo/ex01.png"
    pause.1
    "01_hp/06_emo/ex02.png"
    pause.1
    "01_hp/06_emo/ex03.png"
    pause.1
    "01_hp/06_emo/ex04.png"
    pause 2
    "01_hp/06_emo/ex01.png"
    pause.1
    "01_hp/06_emo/ex00.png"

image emo02:
    "01_hp/06_emo/exl01.png"
    pause.05
    "01_hp/06_emo/exl02.png"
    pause.05
    "01_hp/06_emo/exl03.png"
    pause.05
    "01_hp/06_emo/exl04.png"
    pause.05
    "01_hp/06_emo/exl05.png"
    pause.05
    "01_hp/06_emo/exl06.png"

image emoq:
    "01_hp/06_emo/q1.png"
    pause.05
    "01_hp/06_emo/q2.png"
    pause.05
    "01_hp/06_emo/q3.png"
    pause.05
    "01_hp/06_emo/q4.png"
    pause.05
    "01_hp/06_emo/q1.png"
    pause.05
    "01_hp/06_emo/q2.png"
    pause.05
    "01_hp/06_emo/q3.png"
    pause.05
    "01_hp/06_emo/q4.png"

image emom:
    "01_hp/06_emo/emo00.png"
    pause.08
    "01_hp/06_emo/emo01.png"

image excl:
    "01_hp/06_emo/excl01.png"
    pause.08
    "01_hp/06_emo/excl02.png"
    pause.08
    "01_hp/06_emo/excl03.png"
    pause.08
    "01_hp/06_emo/excl04.png"
    pause.08

image qu:
    "01_hp/06_emo/que1.png"
    pause.08
    "01_hp/06_emo/que2.png"
    pause.08
    "01_hp/06_emo/que3.png"
    pause.08
    "01_hp/06_emo/que4.png"
    pause.08
    "01_hp/06_emo/que5.png"
    pause.08
    "01_hp/06_emo/que6.png"

image an:
    "01_hp/06_emo/an1.png"
    pause.2
    "01_hp/06_emo/an2.png"
    pause.2
    "01_hp/06_emo/an3.png"
    pause.2
    "01_hp/06_emo/an2.png"
    pause.2
    repeat

image sal:
    "01_hp/06_emo/s1.png"
    pause.08
    "01_hp/06_emo/s2.png"
    pause.2
    "01_hp/06_emo/s3.png"
    pause.08
    "01_hp/06_emo/s4.png"
    pause.2
    "01_hp/06_emo/s5.png"
    pause.08
    "01_hp/06_emo/s6.png"
    pause 1
    "01_hp/06_emo/00.png"
    pause.08
    repeat

image th:
    "01_hp/06_emo/t1.png"
    pause.2
    "01_hp/06_emo/t2.png"
    pause.2
    "01_hp/06_emo/t3.png"
    pause.2
    "01_hp/06_emo/t4.png"
    pause.2
    repeat

image emo7:
    "01_hp/06_emo/emotion00.png"
    pause.2
    "01_hp/06_emo/emotion01.png"
    pause.2
    "01_hp/06_emo/emotion00.png"
    pause.08
    "01_hp/06_emo/emotion01.png"
    pause.08
    "01_hp/06_emo/emotion00.png"
    pause.08
    "01_hp/06_emo/emotion01.png"
    pause.08

image emo8:
    "01_hp/06_emo/emotion00.png"
    pause.2
    "01_hp/06_emo/emotion03.png"
    pause.2
    "01_hp/06_emo/emotion00.png"
    pause.08
    "01_hp/06_emo/emotion03.png"
    pause.08
    "01_hp/06_emo/emotion00.png"
    pause.08
    "01_hp/06_emo/emotion03.png"
    pause.08

image sur:
    "01_hp/06_emo/sur1.png"
    pause.08
    "01_hp/06_emo/sur2.png"
    pause.08
    "01_hp/06_emo/sur3.png"
    pause.08
    "01_hp/06_emo/sur4.png"
    pause.08
    "01_hp/06_emo/sur5.png"
    pause.08
    "01_hp/06_emo/sur6.png"
    pause.08



image side mage = "characters/mage.png"
image side mage2 = "characters/mage2.png"
image side mage3 = "characters/mage3.png"
image side mage4 = "characters/mage4.png"
image side mage5 = "characters/mage5.png"
image side mage6 = "characters/mage6.png"
image side mage7 = "characters/mage7.png"
image side mage8 = "characters/mage8.png"
image side mage9 = "characters/mage9.png"
image side mage10 = "characters/mage10.png"
image side mage11 = "characters/mage11.png"
image side mage12 = "characters/mage12.png"
image side mage13 = "characters/mage13.png"
image side mage14 = "characters/mage14.png"
image side mage15 = "characters/mage15.png"

image side akaJew1 = "characters/aka.png"
image side akaJew2 = "characters/aka2.png"
image side akaJew3 = "characters/aka3.png"
image side akaJew4 = "characters/aka4.png"
image side akaJew5 = "characters/aka5.png"
image side akaJew6 = "characters/aka6.png"
image side akaJew7 = "characters/aka7.png"


######
image magic = "magic/magic1.png"
image magic2 = "magic/magic2.png"
image magic3 = "magic/magic3.png"
image magic4 = "magic/magic4.png"
image magic5 = "magic/magic5.png"

image bld = "interface/bld.png"
image bld2 = "interface/bld2.png"
image white = "interface/white.jpg"
image white = "interface/white.jpg"
image blkfade = "interface/blackfade.png"
image blkfade = "interface/blackfade.png"
image whitefade = "interface/whitefade.png"
image whitefade = "interface/whitefade.png"
image con1 = "interface/cont1.png"
image blk50 = im.Alpha("interface/blackfade.png", 0.5)
image blk50 = im.Alpha("interface/blackfade.png", 0.5)
    
image ctc3 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2, xpos=0.97, ypos=0.929, xanchor=1.0, yanchor=1.0)
image ctc4 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2, xpos=0.99, ypos=0.995, xanchor=0.8, yanchor=1.0)
image ctc7 = Animation("interface/ctc00.png", 0.2, "interface/ctc01.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc03.png", 0.2, "interface/ctc04.png", 0.5, "interface/ctc03.png", 0.2, "interface/ctc02.png", 0.2, "interface/ctc01.png", 0.2)

## TRANSFORMATION

transform basicfade:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.5 alpha 0.0

transform basicfade2:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0

transform basicfade3:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 0.8 alpha 0.0

transform basicfade4:
        on show:
            alpha 1.0
            linear 0.2 alpha 1.0
        on hide:
            linear 1.2 alpha 0.0




label masterstart:
    stop music fadeout 1
    $ renpy.music.set_volume(1.0, .5, channel=7)

    scene bg meadow
    show sylvie smile
    $ renpy.play('sounds/magic4.ogg')
    scene white
    pause.02
    scene bg meadow
    show magic5
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    pause.05
    scene white
    pause.05
    scene bg meadow
    show sylvie smile
    show whitefade at basicfade, center
    show magic at basicfade, center
    show magic2 at basicfade2, center
    show magic3 at basicfade3, center
    show magic4 at basicfade4, center
    hide magic
    hide magic2
    hide magic3
    hide magic4
    hide whitefade
    show heal

label masterstart2:
    stop music fadeout 1

    show con1 at right
    show ctc7 at right
    pause
    hide con1
    hide ctc7





    
    

image splash:
    "logo/logo00.jpg"
    pause 2
    "logo/logo01.jpg"
    pause 1
    "logo/logo02.jpg"
    pause 1
    "logo/logo03.jpg"
    pause.5
    "logo/logo04.jpg"
    pause 1
    "logo/logo05.jpg"
    pause 1
    "logo/logo06.jpg"

image splash2:
    "logo/logo00.jpg"
    pause 2
    "logo/logo06.jpg"

label splashscreen:
    $ renpy.pause(0)
    scene black
    with Pause(0.9)
    $ renpy.play('sounds/arcade.wav')
    show image "logo/logo07.jpg"
    pause 2
    with dissolve
    with Pause(2.0)

    scene black
    with dissolve
    with Pause(1.0)

    return

label splashscreen2:
    $ renpy.pause(0)
    scene black
    with Pause(0.5)
    $ renpy.play('sounds/logo.ogg')
    show splash
    pause 7
    with dissolve
    with Pause(2.0)

    scene black
    with dissolve
    with Pause(1.0)

    return

    

    



define s = Character(None, color="#402313", ctc="ctc3", ctc_position="fixed")
define m = Character(None, window_left_padding=200, image="mage", color="#402313", ctc="ctc3", ctc_position="fixed")
define g = Character(None, window_left_padding=300, image="mage2", color="#402313", ctc="ctc3", ctc_position="fixed")
define g2 = Character(None, window_left_padding=300, image="mage3", color="#402313", ctc="ctc3", ctc_position="fixed")
define g4 = Character(None, window_left_padding=200, image="mage4", color="#402313", ctc="ctc3", ctc_position="fixed")
define g5 = Character(None, window_left_padding=200, image="mage5", color="#402313", ctc="ctc3", ctc_position="fixed")
define g6 = Character(None, window_left_padding=200, image="mage6", color="#402313", ctc="ctc3", ctc_position="fixed")
define g7 = Character(None, window_left_padding=200, image="mage7", color="#402313", ctc="ctc3", ctc_position="fixed")
define g8 = Character(None, window_left_padding=200, image="mage8", color="#402313", ctc="ctc3", ctc_position="fixed")
define g9 = Character(None, window_left_padding=200, image="mage9", color="#402313", ctc="ctc3", ctc_position="fixed")
define g10 = Character(None, window_left_padding=200, image="mage10", color="#402313", ctc="ctc3", ctc_position="fixed")
define g11 = Character(None, window_left_padding=200, image="mage11", color="#402313", ctc="ctc3", ctc_position="fixed")
define g12 = Character(None, window_left_padding=280, image="mage12", color="#402313", ctc="ctc3", ctc_position="fixed")
define g13 = Character(None, window_left_padding=280, image="mage13", color="#402313", ctc="ctc3", ctc_position="fixed")
define g14 = Character(None, window_left_padding=280, image="mage14", color="#402313", ctc="ctc3", ctc_position="fixed")
define g15 = Character(None, window_left_padding=280, image="mage15", color="#402313", ctc="ctc3", ctc_position="fixed")

define a1 = Character(None, window_left_padding=220, image="akaJew1", color="#402313", ctc="ctc3", ctc_position="fixed")
define a2 = Character(None, window_left_padding=220, image="akaJew2", color="#402313", ctc="ctc3", ctc_position="fixed")
define a3 = Character(None, window_left_padding=220, image="akaJew3", color="#402313", ctc="ctc3", ctc_position="fixed")
define a4 = Character(None, window_left_padding=290, image="akaJew4", color="#402313", ctc="ctc3", ctc_position="fixed")
define a5 = Character(None, window_left_padding=220, image="akaJew5", color="#402313", ctc="ctc3", ctc_position="fixed")
define a6 = Character(None, window_left_padding=220, image="akaJew6", color="#402313", ctc="ctc3", ctc_position="fixed")
define a7 = Character(None, window_left_padding=220, image="akaJew7", color="#402313", ctc="ctc3", ctc_position="fixed")



define eslow = Character(None, color="#402313", what_slow_cps=20)
define centertext = Character(None,
    what_size=20, #Font size
    what_xalign=0.5, #Centers text within the window
    window_xalign=0.5, #Centers the window horizontally
    window_yalign=0.5, #Centers the window vertically
    what_text_align=0.5, #Centers text within the window, just in case
    window_background=None,#Removes the window, so only the text shows
    what_outlines=[(3, "#000000", 2, 2), (3, "#ffffff", 0, 0)],
    #Gives an outline
    what_slow_cps=20 #Speed at which the text appears (slow)
    )