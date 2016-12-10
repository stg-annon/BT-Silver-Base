#LUNA PLOT
#Luna is misinterpreting her own teenage arousal as a result of a group of wrackspurts that have decided to terrorise her.
#Genie is able to determine the true cause of her arousal and informs her that they only cure for her arousal is to perform certain activites together


#Don't forget to incorporate the quibbler

#LUNA MECHANICS
#Functions on a different mechanic from hermione. She still has a 'whoring' stat but instead of anger she has arousal
#Certain activities will cause Luna to gain arousal and others will cause her to lose it
#Any favors that focus on her will lose arousal as she will achieve a 'release'
#Any favors that focus on genie will cause her to gain arousal
#If her arousal is too high she won't do the genie favors and conversely if it is too low then she will not do the favors that focus on her

label luna_init:
    $ luna_busy = False
    $ luna_known = False
    $ luna_unlocked = False
    $ l_genie_name = "Professor"
    $ luna_name = "Miss Lovegood"

    $ luna_arrousal = 0
    $ luna_corruption = 0

    $ luna_base = "01_hp/13_characters/luna/body/base/base_01.png" 
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_1.png" 
    $ luna_hair = "01_hp/13_characters/luna/body/head/hair_01.png" 
    $ luna_xpos = 600
    $ luna_ypos = 0
    $ luna_mouth = "01_hp/13_characters/luna/body/face/mouth/mouth_1.png" 
    $ luna_eye = "01_hp/13_characters/luna/body/face/eye/eye_1.png" 
    $ luna_eyebrow = "01_hp/13_characters/luna/body/face/eyebrow/eyebrow_1.png" 
    $ luna_pupil = "01_hp/13_characters/luna/body/face/pupil/pupil_1.png" 
    $ luna_glasses = "01_hp/13_characters/luna/misc/glasses.png" 
    $ luna_top = "01_hp/13_characters/luna/clothes/uniform/top.png" 
    $ luna_acc = "01_hp/13_characters/luna/misc/jewel.png" 
    $ luna_skirt = "01_hp/13_characters/luna/clothes/uniform/skirt.png" 
    $ luna_panties = "01_hp/13_characters/luna/clothes/underwear/panties.png" 
    $ luna_bra = "01_hp/13_characters/luna/clothes/underwear/bra.png" 
    $ luna_zorder = 5

    $ luna_chibi_image = "01_hp/13_characters/luna/chibis/luna_stand.png" 
    $ luna_chibi_xpos = 400
    $ luna_chibi_ypos = 250

    $ luna_wear_glasses = False
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_skirt = True
    $ luna_wear_top = True
return

label luna_day_flags:
    $ luna_cheeks = "01_hp/13_characters/luna/base/cheeks_01.png"
    $ luna_busy = False
return

label luna_night_flags:
    $ luna_cheeks = "01_hp/13_characters/luna/base/cheeks_01.png"
    $ luna_busy = False
return

label luna_walk(pos1 = walk_xpos, pos2 = walk_xpos2, speed = luna_speed, loiter = False,redux_pause = 0):
    hide screen luna_walk
    hide screen luna_walk_f
    $ walk_xpos = pos1 #(From)
    $ walk_xpos2 = pos2 #(To)
    $ luna_chibi_ypos = 250
    $ luna_speed = speed #Speed of walking animation. (lower = faster)
    hide screen luna_blink
    hide screen luna_blink_f
    if pos1 > pos2: #right to left (luna_walk)
        show screen luna_walk
        $ tmp = luna_speed - redux_pause
        pause tmp
        $ luna_chibi_xpos = pos2
        hide screen luna_walk
        if loiter:
            show screen luna_blink
    else: #left to right (luna_walk_f)
        show screen luna_walk_f
        $ tmp = luna_speed - redux_pause
        pause tmp
        $ luna_chibi_xpos = pos2
        hide screen luna_walk_f
        if loiter:
            show screen luna_blink_f
    return
    
label luna_walk_end_loiter(dissolveTime = 3):
    if dissolveTime > 0:
        hide screen luna_02
        hide screen luna_01_f
        hide screen luna_blink
        hide screen luna_blink_f
        with Dissolve((dissolveTime/10))
    else:
        hide screen luna_02
        hide screen luna_01_f
        hide screen luna_blink
        hide screen luna_blink_f
    return

label luna_door:
    call luna_summon
    lun "Hello [l_genie_name]!"
    menu:
        "-Sexual favours-":
            jump luna_favour_menu
        "-Never mind-":
            jump luna_away

label luna_favour_menu:
    menu:
        "-Focus on Luna-":
            jump luna_favour_luna
        "-Focus on me-":
            jump luna_favour_genie
        "-Never mind-":
            jump luna_door

label luna_favour_luna:
    menu:
        "-Talk to her-":
            jump luna_favour_1
        "-Make her touch herself-":
            jump luna_favour_3
        "-Make her touch herself in class-" if daytime:
            jump luna_favour_5
        "-Make her touch herself in class-" if not daytime:
            ">This favour is only available during the day."
            jump luna_favour_luna

        "-Touch her-":
            jump luna_favour_7
        "-Have sex with her-":
            jump luna_favour_9
        "-Have anal sex with her-":
            jump luna_favour_11
        "-Never mind-":
            jump luna_door

label luna_favour_luna:
    menu:
        "-Talk to me-":
            jump luna_favour_2
        "-Strip for me-":
            jump luna_favour_4
        "-Strip in class-" if daytime:
            jump luna_favour_6
        "-Strip in class-" if not daytime:
            ">This favour is only available during the day."
            jump luna_favour_luna

        "-Dress up for me-":
            jump luna_favour_8
        "-Touch me-":
            jump luna_favour_10
        "-Suck me-":
            jump luna_favour_12
        "-Titfuck her-":
            jump luna_favour_13
        "-Never mind-":
            jump luna_door

label luna_summon:
    $ changeLuna(1, 1, 4, 1)
return

label luna_away:
    $ luna_busy = True
    $ renpy.play('sounds/door.mp3')
    hide screen luna
    jump day_main_menu

label luna_intro_1:
    $ luna_wear_glasses = True
    lun "Hello, Professor!"
    m "Hello, Luna."
    lun "Professor, I need your help with something."
    m "(Damn, she’s fine!) Yes girl, what is it?"
    lun "I’ve asked the other teachers and they all laugh at me, but I need help with some wrackspurts."

    menu: 
        "\"Wrackspurts?... Is that some sort of wizard STD?\"":
            lun "Hahaha, I guess you could say that, Professor! "
            lun "Wrackspurts are invisible creatures which float into a person’s ear and make their brain go fuzzy."
            lun "You can only view them wearing these spectrespecs!"

            m "I see... (This bitch is crazy)"
            m "Well Miss Lovegood what can we do about it?"
            lun "I am not sure professor, normally thinking positive thoughts is enough to remove them, but I am having trouble with these. If my father, Xenophilius -"
            "*Genie jumps from the table*"
            m "DID YOU JUST CAST A SPELL ON ME?!"
            lun "Professor?"
            m "EXPLAIN YOURSELF!"
            lun "I am sorry Professor, I am not sure what-"
            m "XENOFIUS! What does it do?"
            lun "Xenofius? I’ve not heard of that spell before, Professor."
            m "The spell... That you just... Never mind."
            lun "(A Secret spell?) Professor, your magic is the strongest in Hogwarts and these wrackspurts are really getting to me."
        "\"I am afraid I can’t help you Miss Lovegood.\"":
            lun "Oh please, Professor! You’re the only one powerful enough to help."
            "*You can see Luna is rocking her pelvis as though she were grinding the air*"
            m "Miss Lovegood, I am afraid I don’t know what a wrackspurt is, let alone how to cure it."
            lun "Well, professor; wrackspurts are detailed on page 6 of The Quibbler! Here!"
            "*Luna hands you a Quibbler*"
            m "*Reading* “Rotfang conspiracy... 300 ways to tie up a ghost... “ Ah! Wrackspurts..."
            "\"Invisible creatures which float into a person’s ears, making his/her brain go fuzzy\""
            "*Luna points to her spectrespecs* "
            lun "I can see them, Professor."
            m "Yes, well...(No wonder Hermione called her Loony Lovegood)."
        "\"What in Agrabah are you wearing?\"":
            lun "Oh! These are my spectrespecs, professor!"
            m "(Please don’t be mind-reading, please don’t be mind-reading-)"
            lun "They help me see the wrackspurts."
            m "(Thank the great  desert sands!)"
            lun "And this is my butter beer necklace."
            m "(Damn, her tits are huge!... I wonder if I could...)"
            menu:
                "-Start Masturbating-":
                    m "( I am sure she won’t notice)"
                    lun "You know... To keep away the Nargles!"
                    m "(Those perfect lips!)"
                    lun "Hmmm, they still seem rather fond of my shoes though."
                    m "(Damn, her voice is dreamy. I can’t wait to listen to her choking on my cock)"
                    lun "And several pairs of my underwear are missing too."
                    m "(Yes, yes, almost there!)"
                    lun "Though Father says that’s most likely the work of a Blithering Cumdrinker"
                    m  "ARGH!"
                    lun "Don’t be scared, Professor, they only go after women’s underwear."
                    m "(Wow, she was completely oblivious. This is going to be easier than I thought!)"
                    m "Ah, yes girl. Now what were you saying again?"
                    lun "Oh, the wrackspurts! Yes, Professor, they’re proving to be quite a pain."
                "-No, I better not.-":
                    lun "You know... To keep away the Nargles!"
                    m "(What is she blabbering about?)"
                    lun "Hmmm, they still seem rather fond of my shoes though."
                    m "Right, sure. Now what were you saying again, something about wrackspurts?"
                    lun "Oh, the wrackspurts! Yes, Professor, they’re proving to be quite a pain."

    "*Luna is visibly grinding her pelvis against her thighs.*"
    m "(Is she really?... Ohhh). Miss Lovegood, I think I can help you."
    lun "Oh, Joy, professor! "
    m "Your case is exceptionally rare, Miss Lovegood and I will need to see you frequently in order to completely ensure that your crack squirts *ahem* are gone."
    lun "Wrackspurts, professor."
    m "Yes, your rack squirts. Run along now girl, I shall see you in my office tomorrow."
    lun "Very well, professor!"
    "*Luna skips out of the room, squeezing her legs together as she prances*"
    m "(This is going to be fun!)"
    $ luna_wear_glasses = True
    jump luna_away

###FAVOURS###------------------------------------------------------

label luna_favour_1: ###TALK TO HER

    jump luna_away
label luna_favour_2: ###TALK TO ME
    jump luna_away
label luna_favour_3: ###MAKE HER TOUCH HERSELF
    jump luna_away
label luna_favour_4:
    jump luna_away
label luna_favour_5:
    jump luna_away
label luna_favour_6:
    jump luna_away
label luna_favour_7:
    jump luna_away
label luna_favour_8:
    jump luna_away
label luna_favour_9:
    jump luna_away
label luna_favour_10:
    jump luna_away
label luna_favour_11:
    jump luna_away
label luna_favour_12:
    jump luna_away
label luna_favour_13:
    jump luna_away

###CHIBIS###------------------------------------------------------