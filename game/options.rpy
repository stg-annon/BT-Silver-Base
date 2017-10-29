## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:v

    config.autoreload = False # If false, Ren'Py will reload the game once per press of shift+R.

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer =True

    ## These control the width and height of the screen.
    
    # 16:9 = 1080x600
    # 2:4  = 800x600
    
    config.screen_width = 1080 #800
    config.screen_height = 600 #600
    
    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Witch Trainer (Silver)"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "WT Silver"
    config.version = "1.19"

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.threeD(
        ## Theme: 3D
        ## Color scheme: Muted Horror

        ## The color of an idle widget face.
        widget = "#777777",

        ## The color of a focused widget face.
        widget_hover = "#73735C",

        ## The color of the text in a widget.
        widget_text = "#404033",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#000000",

        ## The color of a disabled widget face.
        disabled = "#73735C",

        ## The color of disabled widget text.
        disabled_text = "#8C8C70",

        ## The color of informational labels.
        label = "#1A0001",

        ## The color of a frame containing widgets.
        frame = "#555544",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "title_ani",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "title/title2.jpg",


        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("interface/frame2.png", 12, 12)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    style.window.right_margin = 280
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 65
    style.window.right_padding = 70
    style.window.top_padding = 40
    # style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    style.window.yminimum = 143


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "interface/CREABBB.TTF"

    ## The default size of text.
    style.default.size = 18
    style.default.color = "#402313"

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "interface/click3.mp3"
    style.imagemap.activate_sound = "interface/click3.mp3"

    ## Sounds that are used when entering and exiting the game menu.

    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "music/01 Prologue.mp3"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = Dissolve(.3)

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = Dissolve(.7)

    ## Used when a game is loaded.
    config.after_load_transition = Dissolve(.3)

    ## Used when the window is shown.
    config.window_show_transition = Dissolve(.3)

    ## Used when the window is hidden.
    config.window_hide_transition = Dissolve(.3)

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "WT SILVER"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 40

    ## The default auto-forward time setting.

    config.default_afm_time = 40

    #########################################
    ## More customizations can go here.




    ##Modifies the Menu Choice's BG
    #style.menu_choice_button.background = Frame("choice_bg_idle.jpg",28,9)
    #style.menu_choice_button.hover_background = Frame("choice_bg_hover.jpg",28,9)
    # style.name_button.selected_background = Frame("choice_bg_idle.jpg",28,9)
    # style.name_button.selected_hover_background = Frame("choice_bg_idle.jpg",28,9)
    # style.name_button.insensitive_background = Frame("choice_bg_idle.jpg",28,9)
    # style.menu_choice_button.yminimum = 39 #Sets height, recommended to be the exact height of your image

    ##Modifies the Menu Choice's Text
    #style.menu_choice.color = "#000"
    #style.menu_choice.size = 18
    #style.menu_choice.outlines = [(2, "#000", 0, 0)]
    style.menu_choice.hover_color = "#e9d570"
    style.menu_choice.hover_outlines = [(2, "#402313", 0, 0)]

    #style.file_picker_button.color = "#c25fb9"
 ########################################################################################
    style.say_who_window.background = Frame("interface/PinkBox.png", 15, 15) #Background skin
    style.say_who_window.xalign = 0.0
    style.say_who_window.yalign = 1.0
    #style.say_who_window.xpos = 100 #For precise placement
    #style.say_who_window.ypos = 100 #For precise placement
    style.say_who_window.left_padding = 20
    style.say_who_window.top_padding = 15
    style.say_who_window.right_padding = 15
    style.say_who_window.bottom_padding = 15
    style.say_who_window.xminimum = 150
    style.say_who_window.yminimum = 10
    style.say_who_window.xfill = False




## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "WT_Silver_1.19"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "WT Silver"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.


    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    #build.documentation('*.html')
    #build.documentation('*.txt')


    config.window_icon = "interface/icon.png"

    config.hard_rollback_limit = 100
