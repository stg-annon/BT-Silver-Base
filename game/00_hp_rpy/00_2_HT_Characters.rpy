###HARRY POTTER CHARACTERS###
init python:
    # Character tables
    
    ### SNAPE HEAD ###
    sna_ = [""]
    for i in range(1,26):
        sna_.append("")
        sna_[i] = Character("Severus Snape", color="#402313", window_right_padding=270, show_side_image=Image("01_hp/13_characters/snape/head/head_" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")
    
    
    ### HERMIONE HEAD (OLD) ###
    her_ = [""]
    for i in range(1,43):
        her_.append("")
        her_[i] = Character("Hermione", color="#402313", window_right_padding=270, show_side_image=Image("01_hp/15_hermione_head/" + str(i) + ".png", xalign=1.0, yalign=0.0), show_two_window=True, show_who_xalign=0.5, ctc="ctc3", ctc_position="fixed")


    fem = Character('Female Student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal = Character('Male Student # 1', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    mal2 = Character('Male Student # 2', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    ann = Character('The Announcer', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly1 = Character('Slytherin student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sly2 = Character('Another Slytherin student', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr1 = Character('Somebody from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    cr2 = Character('Another voice from the crowd', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
     
    
    ###HARRY POTTER CHARACTERS###
    her = Character('Hermione', color="#402313", window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed")
    her2 = Character('Hermione', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).
    sna = Character('Severus Snape', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    sna2 = Character('Severus Snape', color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed")  #Text box used for "head only" speech. (Because it has padding).
    vol = Character('Lord Voldemort', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    l = Character('Lola', color="#402313", window_right_padding=230, show_two_window=True, ctc="ctc3", ctc_position="fixed") #Text box used for "head only" speech. (Because it has padding).    $ bought_mag3 = False #Affects 15_mail.rpy
    g3 = Character('Genie', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")

    ###Custom Characters for WT:Silver
    spo = Character('Professor Sprout', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    maf = Character('Madam Mafkin', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    hoo = Character('Madam Hooch', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    abe = Character('Aberforth', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    lun = Character('Luna', color="#402313", show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    
    
    
define dum = Character(None, window_left_padding=240, image="dum1", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum2 = Character(None, window_left_padding=240, image="dum2", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum3 = Character(None, window_left_padding=240, image="dum3", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum4 = Character(None, window_left_padding=240, image="dum4", color="#402313", ctc="ctc3", ctc_position="fixed")
define dum5 = Character(None, window_left_padding=240, image="dum5", color="#402313", ctc="ctc3", ctc_position="fixed")
    
    
## FAWKES ##
define faw = Character('Fawkes',
    color="#f21111",
    window_right_padding=270,
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
   
    
    
define pat = Character('silvarius2000',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/11_misc/pat.png", xalign=1.0, yalign=1.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define dahr = Character(None,
    color="#402313",
    window_left_padding=230,
    show_side_image=Image("01_hp/18_store/dahr.png", xalign=0.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc4",
    ctc_position="fixed")

#######################################################################
##  Additions by JJ for replacement tutoring section  JJ 01/03/2015  ##

define her_wLeft = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesLeft.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wMad = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesMad.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wShut = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesShut.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wWLeft = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesWideLeft.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wWOpen = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandEyesWideOpen.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wDown = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandLookDown.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wOneopen = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandOneShutDrop.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")

define her_wTears = Character('Hermione',
    color="#402313",
    window_right_padding=270,
    show_side_image=Image("01_hp/15_hermione_head/HermioneWandOneShutTears.png", xalign=1.0, yalign=0.0),
    show_two_window=True,
    show_who_xalign=0.5,
    ctc="ctc3",
    ctc_position="fixed")
#######   JJ End additions           ##############################
###################################################################