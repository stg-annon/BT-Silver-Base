label cho_menu:
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ changeCho(1, 1, 2, 1)
    menu:
        "-Personal Favours-":
            menu:
                "-Take it Off-":
                    jump cho_favor_1
                "-Play with her butt-" if cho_whoring == 1:
                    jump cho_favor_2
                #"-Make her suck my cock-":
                    jump cho_favor_3
                "-Nevermind-":
                    jump cho_menu
        "-Public Favours-":
            "To be done."
            jump cho_menu
        "-Dismiss Her-":
            hide screen cho_chang
            with d3
            jump day_main_menu

###CHO END EVENT

label cho_end_event:
    hide screen cho_chang
    jump day_main_menu




###ONE OFF EVENTS###

label cho_intro:
    $ cho_known = True
    m "Miss Granger. How would you like to earn some points today?"
    call her_main("What do I have to do?","head_exp/1")
    m "Nothing. Just stand there."
    call her_main("I don't believe you.","head_exp/4")
    m "Well, of course, there's more to it than that. I'm going to molest your butt a little bit as well."
    call her_main("You're not going to spank me again, are you?","head_exp/25")
    m "You don't like it when I slap your butt?"
    call her_main("It's...it's not that. It's just that you're too loud.","head_exp/2")
    call her_main("What would you do if someone walked by while you...while I was 'just standing here'? They might hear.","head_exp/4")
    m "What? Nonsense. These walls are solid unobtanium. They'd have to be some kind of a wizard to notice anything."
    call her_main("That doesn't make any sense!","head_exp/3")
    m "Do you want those points or not?"
    call her_main("Yes, please.","head_exp/15", xpos=140)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 1
    hide screen hermione_walk_01
    hide screen genie
    show screen ctc
    show screen groping_02
    with d1
    menu:
        "-Give her butt a slap-":
            pass
        "-Who are you kidding, slap that ass!-":
            pass
    $ renpy.play('sounds/slap_02.mp3') #SLAP!
    show screen white
    with hpunch
    pause.08
    hide screen white
    show screen bld1
    her "Professor!"
    her ".....What are you-"
    menu:
        "-Give her butt another slap!-":
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            call her_main("Professor!","head_exp/20")
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            call her_main("Not-","head_exp/20")
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            call her_main("So-","head_exp/40")
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            call her_main("Hard!","head_exp/40")
            m "Did you say something, miss granger?"
            call her_main("I said, not so hard.","head_exp/41")
            call her_main("Someone might hear!","head_exp/42")
            m "Miss Granger, please. There's no need to shout."
            menu:
                "-Keep Slapping her Butt-":
                    $ renpy.play('sounds/slap_02.mp3') #SLAP!
                    show screen white
                    with hpunch
                    pause.08
                    hide screen white
                    show screen bld1
                    call her_main("Professor!","head_exp/29")
                    pass
                "-Soothe her tender cheeks-":
                    "You gently slide your hands up Hermione's legs, slipping your hands under her skirt."
                    call her_main("...........","head_exp/28")
                    "Your hands softly carress her skin. You can feel the heat rising from her abused cheeks."
                    call her_main("......","head_exp/27")
                    "You can feel the soft goosebumps forming on the inflamed skin."
                    call her_main("Professor?","head_exp/28")
                    "You notice her breathing becoming more shallow."
                    call her_main("Can we please stop, now?","head_exp/12")
                    m "Doesn't that feel better?"
                    call her_main(".......Yes.","head_exp/10")
                    call her_main("I mean, no.","head_exp/11")
                    menu:
                        "-Listen to the Girl-":
                            pass
                        "-Play with Her Asshole-":
                            "You ignore Hermione and gently slide your hands under her panties."
                            "Your left hand gently pulls her cheek back, exposing the smooth, muscular ring of her asshole."
                            "You extend your middle finger, and gingerly touch the soft, smooth skin."
                            call her_main("!","head_exp/21")
                            call her_main("Prof-","head_exp/22")
                            m "Shhh. Not too loud, girl. Wouldn't want to alarm anyone out in the hall."
                            "Your finger presses against the firm muscle and you begin to trace a slow circle around the ring."
                            call her_main("......","head_exp/7")
                            call her_main("...","head_exp/11")
                            "You can feel Hermione's ass start to twitch."
                            call her_main("I-I think I'm going to-","head_exp/40")
                            "Hermione's tight asshole opens just enough for your finger to pop inside."
        "-Nothing at all-":
            pass
    $ days_since_cho = 0
    $ renpy.play('sounds/door.mp3')
    $ cc_xpos = 550
    call cho_main("Professor Dumbledore! I'm sorry for rushing in without knocking, but I finally have proof the Slytherin team is cheating! Draco and his goons are-", 3, 2, 3, 4)
    $ renpy.play('sounds/scratch.wav')
    hide screen groping_02
    show screen no_groping_02
    call her_main("...","head_exp/30")
    call cho_main("...", 4, 2, 4, 3)
    call her_main("....","head_exp/30")
    call cho_main("....", 4, 2, 4, 2)
    call her_main(".....","head_exp/30")
    m "....."
    call cho_main(".....", 2, 2, 1, 2)
    call her_main("It's not what it looks like!","head_exp/22")
    call cho_main("You lying bitch!", 2, 2, 1, 3)
    call cho_main("men's rights movement my ass!", 2, 2, 2, 4)
    call her_main("...","head_exp/24")
    call her_main("How dare you accuse me of trading favors with Professor Dumbledore!","head_exp/26")
    call her_main("He was merely massaging a pulled muscle in my...in my...leg!","head_exp/19")
    call cho_main("Liar!", 1, 2, 1, 2)
    call her_main("You... you...","head_exp/25")
    call her_main("You flatchested skank!","head_exp/26")
    call cho_main("Two-faced cow!", 5, 2, 1, 3)
    call her_main("C student!","head_exp/26")
    menu:
        "-Tell them to shut up-":
            m "Students! By the sands! Calm yourselves! There is a perfectly reasonable explanation!"
            call her_main("...","head_exp/25")
            call cho_main("...", 2, 2, 1, 2)
            call cho_main("....well?", 2, 2, 1, 3)
            m "Miss Granger was simply helping me clean my office when she pulled a muscle in her leg. It's quite painful. That's why she's so flustered."
            call cho_main("...", 5, 2, 2, 2)
            call cho_main("i can't believe this!", 5, 2, 2, 3)
            hide screen cho_chang
            with d3
            show screen bld1
            with d3
            $ renpy.play('sounds/door.mp3')
            call her_main("You dirty old man!","head_exp/26")
            m "Now see here, young lady. Do not mistake me for some conjurer of cheap tr-"
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            m "Calm yourself, gir-"
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            $ renpy.play('sounds/slap_02.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            call her_main("I'm never selling you another favor again!","head_exp/41")
            $ mad += 15
            hide screen no_groping_02
            show screen genie
            $ walk_xpos=300 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_run
            pause 1
            hide screen hermione_run
            hide screen hermione_main
            $ renpy.play('sounds/door.mp3')
            hide screen bld1
            m "Bitches...."
            if daytime:
                $ hermione_takes_classes = True
                jump day_main_menu
            else:
                $ hermione_sleeping = True
                jump night_main_menu   
    
        "-Stay out of it-":
            call her_main("Nothing! Get out!","head_exp/40")
            call cho_main("Slut!", 5, 2, 1, 3)
            with d3
            hide screen cho_chang
            show screen bld1
            $ renpy.play('sounds/door.mp3')
            call her_main("I can't believe that just happened.","head_exp/15")
            call her_main("What kind of a person just barges into the headmaster's office with out knocking!","head_exp/19")
            call her_main("This was all your fault!","head_exp/25")
            $ mad += 5
            hide screen no_groping_02
            show screen genie
            $ walk_xpos=300 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_run 
            pause 1
            hide screen hermione_run
            hide screen hermione_main
            hide screen bld1
            $ renpy.play('sounds/door.mp3')
            if daytime:
                $ hermione_takes_classes = True
                jump day_main_menu
            else:
                $ hermione_sleeping = True
                jump night_main_menu   


label hermione_cho:
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "-Come in-":
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ hermione_SC.chibi.xpos = 540 #Near the desk.
            show screen hermione_blink #Hermione stands still.
            call her_main("Sir, I just wanted to...","head_exp/2")
            call her_main("...to...","head_exp/4")
            m "By the sands, girl! What?"
            call her_main("I wanted to apologize for what happened.","head_exp/5")
            m "You mean with that girl earlier?"
            menu:
                "-Miss Chang-":
                    m "Miss Chang. Yes?"
                    call her_main("Yes, sir.","head_exp/2")
                    call her_main("She's always trying to compete with me.","head_exp/5")
                    m "Well, girls being girls, you know."
                    call her_main("Yes, sir. But she takes things too far.","head_exp/2")
                    pass
                "-Miss Chong-":
                    m "Miss Chong, was it?"
                    call her_main("Chang, sir.","head_exp/2")
                    m "Of course."
                    pass
            call her_main("I just wanted to tell you that I...","head_exp/5")
            call her_main("I explained everything to Cho.","head_exp/10")
            call her_main("It was so embarassing.","head_exp/15")
            m "And?"
            call her_main("So everything is okay.","head_exp/14")
            call her_main("I told her that you trading me points for cleaning your office.","head_exp/35")
            call her_main("Pretty clever, huh?","head_exp/18")
            m "Yes. Very good, Miss Granger. I assume Miss..."
            menu:
                "-Miss Chang-":
                    m "I assume Miss Chang won't be any trouble, then?"
                    call her_main("Nope!","head_exp/35")
                    m "Splendid."
                    call her_main("Well, I've got to get to class. Bye, sir.","head_exp/2")
                    m "Of course, Miss Granger."
                    hide screen hermione_blink
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3')
                    pass
                "-Miss Ching-":
                    m "I assume she won't be any trouble, then?"
                    m "Miss Ching?"
                    call her_main("Chang","head_exp/5")
                    m "Chong?"
                    call her_main("Her name is Cho Chang!","head_exp/4")
                    m "Ching, Chong, Cho Chang?!"
                    m "That's racist!"
                    call her_main("What?","head_exp/7")
                    m "Don't you have class or something?"
                    hide screen hermione_blink
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3')
                    pass
        "-Not Now, I'm busy-":
                $ days_since_cho = 0
                if daytime:
                    $ hermione_takes_classes = True
                    jump day_main_menu
                else:
                    $ hermione_sleeping = True
                    jump night_main_menu   
            
label end_event:
    if daytime:
        ## set cho unavailable
        jump day_main_menu
    else:
        ## set cho unavailable
        jump night_main_menu   
        
label cho_favor_1:
    menu:
         "-Have Cho get naked-":
            pass
         "-Nevermind-":
             jump cho_menu
    
    if cho_whoring == 0:
         jump cho_favor_1_1
    if cho_whoring >= 1:
        jump cho_favor_1_2


label cho_intro_2:
$ renpy.play ('sounds/knocking.mp3')
menu:
    "Is that you, Miss Granger?":
        "No, it's me. Cho Chang?"
        m "Ah, Miss Chong."
        call cho_main("Chang!", 5, 2, 1, 2)
        m "What?"
        call cho_main("MY name is Chang, sir!", 5, 2, 1, 3)
        m "Ah, well, come in already, Miss Ching."
        jump cho2begin
    "Come in.":
        jump cho2begin
    "Not now, I'm busy.":
        $ days_since_cho = 3
        jump cho_end_event

label cho2begin:
    #enable her character for future reference
    $ cho_met = True
    $ cho_mad = 0
    $ cho_whoring = 0
    $ renpy.play ('sounds/door.mp3')
    $ changeCho(3, 3, 3, 4)
    ">Cho enters and stands in the middle of the room."
    m "Now, what was it you needed?"
    call cho_main("I... um...", 1, 3, 2, 2)
    call cho_main("I know you're buying favors from Hermione.", 2, 3, 1, 2)
    m "And why would you think that?"
    call cho_main("Because I saw you!", 1, 2, 1, 2)
    m "Oh, right."
    m "Well, is there anything else? Or did you merely come to inform me of things I already know."
    call cho_main("Well......", 2, 3, 2, 5)
    m "What is it? Speak up, girl."
    call cho_main("Sir, I want you to buy favors from me, too!", 2, 3, 1, 1)
    m "You do? What happened to being above all of this 'nasty' favor business, and not needing to 'dirty' yourself to win the cup?"
    call cho_main("The Slytherin team is cheating, Sir.", 6, 2, 5, 9)
    m "How does that change anything?"
    call cho_main("It doesn't matter...", 6, 2, 6, 7)
    call cho_main("It doesn't matter how hard i try or how good I am!", 6, 2, 5, 7)
    call cho_main("i can't beat them any other way.", 5, 2, 1, 7)
    $ changeCho(5, 2, 1, 9)
    m "I see."
    m "But...why sell your favors to me, specifically?"
    m "If you suspect that Miss Granger is selling me favors, wouldn't you earn points faster from a less 'occupied' professor?"
    call cho_main("I...um...I looked, but the only other professor trading favors is Snape.", 6, 3, 6, 9)
    call cho_main("AND I will nEver tRade that slytherin scum a single favor!", 6, 2, 5, 10)
    menu:
        "I really don't feel it would be appropriate.":
            m "I really don't feel that it would be appropriate. I'm sure you understand."
            call cho_main("What?!", 4, 2, 4, 7)
            m "I simply can not buy favors from you."
            m "You'll have to go."
            call cho_main("What?", 6, 2, 5, 4)
            m "You'll... have to"
            call cho_main("I can't believe you're going to chose that stupid Gryffindor girl over me!", 2, 2, 1, 3)
            call cho_main("you're a horrIble man. i'm going to coNtact the miNistry of magic and see what they think of their favorite wizard acting like a...like a...", 2, 2, 2, 4)
            call cho_main("CROOK!", 2, 2, 1, 9)
            #Cho storms out
            pause 
            hide screen cho_chang
            $ renpy.play ('sounds/door.mp3')
            m "By Old Crocus' dangly testicles! I hope that doesn't come up again."
            jump cho2end
        "Alright, Miss Chang. I'll let you sell me favors.":
            m "Alright, Miss Chang. I'll let you sell me favors."
            call cho_main("Really?", 1, 1, 1, 1)
            m "Yes. Now, wipe your eyes."
            call cho_main("Sorry, Professor Dumbledor, sir.", 2, 3, 2, 7)
            m "..."
            call cho_main("...", 1, 1, 2, 5)
            m "..."
            call cho_main("Um?...", 1, 3, 1, 7)
            m "Yes?"
            call cho_main("What do I do?", 1, 3, 2, 7)
            menu:
                "\"Take off your vest\"":
                    #Cho removes her vest
                    call cho_main("What? Don't you want to talk a little first?", 4, 3, 4, 7)
                    m "Not really..."
                    m "Besides, Miss Granger is more than happy to show me her-"
                    call cho_main("Fine!", 1, 2, 2, 9)
                    ">Cho quickly pulls off her vest."
                    $ cc_wear_vest = False
                    m "Good..."
                    menu:
                        "\"Now, take off your shirt\"":
                            call cho_main("Okay...", 1, 3, 2, 5)
                            ">Cho quickly removes her tie before starting to undo her shirt."
                            ">Her inexperience is obvious and she struggles for a moment."
                            #Cho removes her shirt
                            $ cc_wear_top = False
                            $ cc_wear_acc = False
                            call cho_main("Sorry, about that.", 1, 3, 1, 7)
                            menu:
                                "\"Not bad\"":
                                    call cho_main("Thanks.", 1, 3, 2, 1)
                                    m "Now take off your skirt..."
                                    call cho_main("Okay...", 1, 3, 1, 7)
                                    ">Cho takes a deep breath then swiftly drops her skirt."
                                    $ cc_wear_skirt = False
                                    jump cho2keepgoing
                                "\"Now your skirt\"":
                                    call cho_main("Okay...", 1, 3, 1, 7)
                                    ">Cho takes a deep breath then swiftly drops her skirt."
                                    $ cc_wear_skirt = False
                                    jump cho2keepgoing
                        "\"Now, take off your skirt\"":
                                call cho_main("Okay...", 1, 3, 1, 7)
                                ">Cho takes a deep breath then swiftly drops her skirt."
                                #Cho removes her skirt
                                $ cc_wear_skirt = False
                                menu:
                                    "-Not bad-":
                                        call cho_main("Thanks.", 1, 3, 2, 1)
                                        m "Now take off your shirt..."
                                        call cho_main("Okay...", 1, 3, 2, 5)
                                        ">Cho quickly removes her tie before starting to undo her shirt."
                                        ">Her inexperience is obvious and she struggles for a moment."
                                        jump cho2keepgoing
                                    "-Now your shirt-":
                                        #Cho is now wearing only her underwear
                                        call cho_main("Okay...", 1, 3, 2, 5)
                                        ">Cho quickly removes her tie before starting to undo her shirt."
                                        ">Her inexperience is obvious and she struggles for a moment."
                                        label cho2keepgoing:
                                        call cho_main("Um, I forgot to ask, but how many points do I get for this?", 2, 3, 1, 7)
                                        m "You're a terrible negotiator."
                                        call cho_main("I know.", 2, 3, 2, 1)
                                        call cho_main("what dO you pay Hermione?", 2, 3, 1, 1)
                                        menu:
                                            "-5 points-":
                                                call cho_main("Just five?", 6, 1, 5, 9)
                                                call cho_main("i bet she looks like a cow compared to me.", 6, 1, 6, 1)
                                                pass
                                            "-15 points-":
                                                call cho_main("{size=-3}(Is that a good price?){/size}", 6, 1, 6, 5)
                                                pass
                                            "-30 points-":
                                                call cho_main("That much, huh?", 1, 1, 2, 7)
                                                pass
                                            "-100 points-":
                                                call cho_main("100?", 4, 3, 4, 3)
                                                call cho_main("but she's so...", 1, 3, 2, 2)
                                                call cho_main("she doesn't even work out!", 1, 2, 1, 2)
                                                pass
                                        call cho_main("How much do you think my body is worth?", 1, 1, 1, 1)
                                        label cho2howmuch:
                                        menu:
                                            "-5 points-":
                                                call cho_main("Just five?", 4, 2, 4, 3)
                                                call cho_main("five measley points!", 6, 2, 5, 4)
                                                menu:
                                                    "-Take it or leave it-":
                                                        call cho_main("You can't be serious.", 6, 2, 5, 4)
                                                        call cho_main("i wake up every morning before dawn and run the quidditch pitch until the sun rises!", 6, 2, 5, 7)
                                                        call cho_main("i keep my body at the absolute peak of human and wizard conditioning!", 6, 2, 6, 7)
                                                        call cho_main("It's worth way more than 5 points.", 6, 2, 5, 9)
                                                        ">Cho gathers up her clothes in a huff."
                                                        call cho_main("I can't believe I thought this would work.", 6, 2, 5, 4)
                                                        hide screen cho_chang
                                                        $ cho_mad +=10
                                                        #Cho storms out
                                                        $ renpy.play ('sounds/door.mp3')
                                                        m "..."
                                                        jump cho2end
                                                    "-Did I say five? I meant more-":
                                                        $ changeCho(6, 2, 5, 4)
                                                        $ cho_mad +=5
                                                        jump cho2howmuch
                                            "-15 points-":
                                                call cho_main("(Is that a good price?)", 6, 3, 6, 5)
                                                call cho_main("i guess that's enough...", 6, 3, 5, 7)
                                                $ cho_points = 15
                                            "-30 points-":
                                                call cho_main("Okay.", 1, 1, 1, 5)
                                                call cho_main("it's a deal.", 1, 1, 2, 1)
                                                $ cho_points = 30
                                            "-100 points-":
                                                call cho_main("100?", 4, 1, 4, 1)
                                                call cho_main("Really?", 4, 1, 4, 7)
                                                call cho_main("that's sooo much, professor.", 1, 1, 2, 5)
                                                call cho_main("Do you want me to take the rest off?", 2, 3, 2, 6)
                                                $ cho_points = 100
                                        $ changeCho(2, 1, 2, 5)
                                        m "Miss Chang, the rest if you would."
                                        call cho_main("Of course, sir.", 1, 1, 1, 5)
                                        ">Cho reaches over her head and pulls her bra off in one smooth motion.{p}Her small, pert breasts barely move as she dips low and pulls her painties down her fit legs."
                                        ">Once finished she leans back proudly and smiles nervously."
                                        $ cc_wear_bra = False
                                        call cho_main("i bet my tight body looks way beTter than Hermione's.", 6, 1, 6, 5)
                                        menu:
                                            "-Yeah, she's gross-":
                                                m  "Miss Granger's body is nothing compared to yours."
                                                call cho_main("Really?", 4, 1, 4, 1)
                                                m  "Her tits sag too much, and her fat hips are disgusting."
                                                call cho_main("She really is a...", 6, 2, 6, 5)
                                                call cho_main("...stupid...", 6, 2, 6, 4)
                                                call cho_main("...fat...", 6, 2, 6, 10)
                                                call cho_main("...cow, isn't she?", 6, 2, 5, 6)
                                                ">From your desk, you can see Cho's hand moving closer to her mound. She's clearly getting wet."
                                            "-I can't choose-":
                                                m  "You're both hot."
                                                call cho_main("I guess.", 6, 2, 6, 9)
                                            "-Nope, you lose-":
                                                m "I'm afraid, Miss Granger is simply more sexy. Jealousy is quite unbecoming of a young witch."
                                                call cho_main("What?", 6, 2, 5, 7)
                                                call cho_main("but she doesn't even Work out. Sir.", 6, 2, 6, 10)
                                                $ cho_mad +=5
                                        menu:
                                            "-Take out your cock and start jerking off behind your desk-":
                                                ">You lean back in your chair and pull your cock out of your robes."
                                                hide screen blktone8
                                                with d3
                                                hide screen genie
                                                show screen genie_jerking_off
                                                with d3
                                                call cho_main("Are you...", 6, 3, 5, 1)
                                                ">Cho's voice is soft and slightly husky. She almost sounds...aroused."
                                                ">You wrap your hand around your thick, veiny cock and begin to jerk off."
                                                call cho_main("Professor...", 6, 1, 5, 6)
                                                menu:
                                                    "-Keep jerking off-":
                                                        ">Your eyes continue to drift over the young quidditch players tight, athletic body."
                                                        ">You lean back in your chair and begin stroking in earnest."
                                                        call cho_main("....", 6, 1, 6, 6)
                                                        ">Cho's innocent eyes are glued to your thick cock."
                                                        call cho_main("...", 6, 1, 5, 6)
                                                        ">The competetive, young seeker looks mesmerized by your actions."
                                                        ">Finally, your eyes meet and she flushes red."
                                                        call cho_main("I-I've never seen one before.", 6, 3, 5, 7)
                                                        call cho_main("are they alWAYs so...BIG?", 6, 3, 5, 1)
                                                        menu:
                                                            "-Tell her to shut up-":
                                                                m "Quiet, girl! Don't ruin this for me."
                                                                call cho_main("...", 6, 3, 6, 5)
                                                                ">At your command the girl closes her mouth and lets you continue undisturbed."
                                                                ">As you continue to stroke your cock you notice Cho shifting her weight.{w=0.4}The tight muscles of her thighs are squeezing in desperate rythym."
                                                                ">You pump your cock faster, matching her rythym"
                                                                call cho_main("I-I think I'm...I'm going to...", 4, 3, 4, 5)
                                                                ">Cho's thighs are squeezing faster and faster."
                                                                call cho_main("Cum!......", 4, 3, 4, 6)
                                                                ">Suddenly, her body goes rigid and her abdominal muscles pulse in waves as orgasm rocks the young girl's body."
                                                                ">Cho's legs, suddenly too weak to hold her lithe body, collapse beneath her and she falls to the floor."
                                                            "-Play along-":
                                                                m  "Only when I'm around students like you, Miss Chang."
                                                                $ changeCho(6, 3, 6, 5)
                                                                ">As you continue to stroke your cock you notice Cho shifting her weight.{w=.04} The tight muscles of her thighs are squeezing in desperate rythym."
                                                                hide screen cho_chang
                                                                m "Miss Chang, what are you doing?"
                                                                call cho_main("I-I'm j-just...I'm just...", 4, 3, 4, 5)
                                                                ">Cho's thighs are squeezing faster and faster."
                                                                call cho_main("Cumming!......", 4, 3, 4, 6)
                                                                ">Suddenly, her body goes rigid and her abdominal muscles pulse in waves as orgasm rocks the young girl's body."
                                                                ">Cho's legs, suddenly too weak to hold her lithe body, collapse beneath her and she falls to the floor."
                                                        "The sight before you is simply too much, and you unleash torrents of cum all over your desk."
                                                        $ cc_ypos = 150
                                                        with d3
                                                        hide screen bld1
                                                        with d3
                                                        show screen genie_jerking_sperm
                                                        with d3
                                                        "By the sands!"
                                                        "Cum coats your otherwise pristine desk. The only sounds in the room are your heavy breaths and the slow *plat* *plat* of your cum dripping off your desk."
                                                        show screen genie_jerking_sperm_02
                                                        with d3
                                                        "Cho looks up at you from the floor."
                                                        call cho_main("...", 6, 3, 6, 5)
                                                        call cho_main("i can'T believe I did that.", 6, 3, 5, 7)
                                                        call cho_main("Can i have my points now!", 1, 1, 2, 1)
                                                        ">Cho jumps back up onto her feet."
                                                        $ cc_ypos = 0
                                                        #go to [End Points]
                                                    "Put it away":
                                                        ">You tactfully tuck your throbbing erection back into your robes."
                                                        #go to [End Points]
                                            "Better not.":
                                                ">You decide not to indulge your baser instincts."
                                                #go to [End Points]
                "\"Suck my cock\"":
                    m "I'd like you to suck my cock, Miss Chang."
                    call cho_main("That's too far. what's wrong with you?", 4, 2, 4, 3)
                    call cho_main("haven't you ever hear of character progression!", 6, 2, 6, 4)
                    call cho_main("you're supposed to start out small!", 6, 2, 5, 4)
                    #Cho storms out
                    $ renpy.play ('sounds/door.mp3')
                    m "By Old Crocus' dangly testicles! I hope that doesn't bite me in the lamp."
                    jump cho_end_event
                    #Go to [END]
                "\"Do you eat ass, Miss Chong?\"":
                            m "Do you eat ass, Miss Chong?"
                            call cho_main("for the last time.", 4, 2, 4, 3)
                            call cho_main("MY name Is CHang, Cho Chang!", 4, 2, 4, 4)
                            call cho_main("...", 6, 2, 5, 9)
                            call cho_main("..", 6, 2, 5, 4)
                            call cho_main(".", 6, 2, 6, 9)
                            call cho_main("Professor.", 6, 2, 5, 7)
                            call cho_main("you're disgusting!", 6, 2, 5, 10)
                            $ cho_mad += 10
                            $ renpy.play ('sounds/door.mp3')
                            g9 "Damn it. I should have know that only internet perverts and shitty writers ruin good porn with assplay."
                            jump cho_end_event
                            #Go to [End]
    show screen genie
    hide screen genie_jerking_off
    with d3
    m "Very good, Miss Chang."
    m "[cho_points] points to Gryffindor!"
    call cho_main("i'm from Ravenclaw, sir.", 6, 2, 5, 9)
    m "Right, what did I say?"
    m "[cho_points] points to Ravenclaw!"
    $ ravenclaw += cho_points
    call cho_main("Thank you, sir...", 6, 2, 6, 9)
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True
    ">Cho quickly puts her clothes on before leaving."
    hide screen cho_chang
    hide screen genie_jerking_sperm_02
    jump cho_end_event

label cho2end:
    hide screen cho_chang
    $ days_since_cho = 3
    $ cho_met = False
    jump cho_end_event

######FAVORS ARE FROM HERE ON######


###Favor 1###
label cho_favor_1_1:
    $ cho_points = 15
    if cho_whoring < 1:
        $ cho_whoring += 1

    m "Miss Chang how would you like to earn 15 house points the easy way?"
    call cho_main("what do i have to do?", 6, 3, 5, 7)
    m "I want to see your body again?"
    call cho_main("you want me to get naked, sir?", 1, 3, 2, 9)
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!!!", 4, 3, 4, 9)
    call cho_main("I'll do it.", 1, 3, 2, 5)
    menu:
        "-Be aggressive-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Get on with it, girl."
            call cho_main("Yes, sir!", 1, 3, 2, 7)
            $ cc_wear_top = False
            $ cc_wear_vest = False
            $ cc_wear_acc = False 
            "Cho grits her teeth and removes her top in one swift motion."
            m "That's better. Now the bottoms."
            call cho_main("Yes, sir.", 1, 3, 1, 9)
            $ cc_wear_skirt = False 
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("(house points...loads of house points....)", 3, 3, 3, 5)
            "Her hands nervously move to her bra."
            $ cc_wear_bra = False
            "She pulls it up, over her head, and lets it fall to the ground."
            $ cc_wear_panties = False 
            "Finally, she pushes her panties over her hips."
            m "Very good."
            call cho_main("........", 3, 3, 3, 4)
            call cho_main("...............", 1, 3, 1, 4)
            call cho_main("......................", 1, 3, 1, 9)
            call cho_main("Um...", 1, 3, 2, 7)
            call cho_main("um...is that enough?", 6, 3, 5, 7)
            menu:
                "-That's enough-":
                    m "You can put your close back on."
                    m "15 points to Ravenclaw."
                    $ ravenclaw += cho_points
                    call cho_main("Thank you, sir...", 6, 2, 6, 9)
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Cho quickly puts her clothes on before leaving."
                    hide screen cho_chang
                    jump cho_end_event
                "-Jerk off-":
                    "You slide your hands under your robes and pull your cock out."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Cho's tight, athletic body sends shivers through you."
                    call cho_main("what are you doing?", 4, 2, 4, 3)
                    call cho_main("i'm not watching you do that for a measly 15 house points.", 6, 2, 5, 7)
                    "Ignoring Cho's protests, your fingers wrap around your thick cock."
                    call cho_main(".......", 6, 3, 5, 9)
                    "Cho takes a deep breath."
                    call cho_main("20 points.", 6, 3, 6, 7)
                    menu:
                        "-Offer 15-":
                            "You look the poor girl in the eyes and continue jerking you cock."
                            m "You'll get 15. No more."
                            call cho_main("Fine.", 6, 2, 5, 9)
                            $ cho_mad += 4
                            jump cho_favor_1_1_1
                        "-20 Sounds good-":
                            $ cho_points = 20
                            "You nod, slowly pumping your cock."
                            m "Sounds good."
                            jump cho_favor_1_1_1
                        "-Give her 25-":
                            $ cho_points = 25
                            "I'll give you 25."
                            call cho_main("Really?", 1, 3, 1, 7)
                            $ cho_mad -= 1
                            jump cho_favor_1_1_1
                            
                            
        "-Be nice-":
            "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
            m "Go on, girl."
            call cho_main("Yes, sir!", 1, 3, 2, 1)
            $ cc_wear_top = False
            $ cc_wear_vest = False
            $ cc_wear_acc = False 
            "Cho flashes a subdued smile and removes her top in one swift motion."
            m "Nice."
            call cho_main("Thank you, sir.", 3, 1, 3, 7)
            $ cc_wear_skirt = False 
            "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
            call cho_main("is this okay?", 1, 3, 1, 9)
            "Her hands nervously move to her bra."
            $ cc_wear_bra = False 
            "She pulls it up, over her head, and lets it fall to the ground."
            call cho_main("what do you think?", 2, 3, 2, 5)
            m "Simply. gorgeous."
            $ cc_wear_panties = False 
            "Finally, she pushes her panties over her hips."
            m "Very nice."
            call cho_main("........", 3, 3, 3, 4)
            call cho_main("...............", 1, 3, 1, 4)
            call cho_main("......................", 1, 3, 1, 9)
            call cho_main("Um...", 1, 3, 2, 7)
            call cho_main("Um...can i put my clothes back on now?", 6, 3, 5, 7)
            menu:
                "-That's enough-":
                    m "You can put your close back on."
                    m "15 points to Ravenclaw."
                    $ ravenclaw += cho_points
                    call cho_main("Thank you, sir...", 6, 2, 6, 9)
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Cho quickly puts her clothes on before leaving."
                    hide screen cho_chang
                    jump cho_end_event
                "-jerk off-":
                    "You slide your hands under your wizard robes and pull your cock out."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Cho's tight, vulnerable body has you incredibly aroused."
                    call cho_main("what are you doing?", 4, 2, 4, 3)
                    call cho_main("i didn't agree to this!", 6, 2, 5, 7)
                    "Ignoring Cho's protests, your fingers wrap around your thick cock."
                    call cho_main(".......", 6, 3, 5, 9)
                    "Cho takes a deep breath."
                    call cho_main("20 points.", 6, 3, 6, 7)
                    menu:
                        "-offer 15-":
                            "You look the poor girl in the eyes and continue jerking you cock."
                            m "You'll get 15. No more."
                            call cho_main("Fine.", 6, 2, 5, 9)
                            $ cho_mad += 2
                            jump cho_favor_1_1_1
                        "-Give her 20-":
                            $ cho_points = 20
                            m "Sounds good."
                            jump cho_favor_1_1_2
                        "-Giver her 25-":
                            $ cho_points = 25
                            m "I'll give you 25."
                            call cho_main("Really?", 1, 3, 1, 7)
                            $ cho_mad -= 2
                            jump cho_favor_1_1_2
                            
label cho_favor_1_1_1: 
    call cho_main("....", 6, 3, 5, 5)
    call cho_main("........", 6, 3, 6, 5)
    call cho_main("........you're...so big and...", 6, 3, 5, 7)
    call cho_main(".....hard.", 6, 3, 6, 6)
    "You can practically feel the girl's eyes on your cock as you drag your hand up and down its length."
    call cho_main("....", 6, 3, 5, 6)
    call cho_main("you're going to spurt soon, aren't you?", 6, 3, 6, 1)
    call cho_main("you're going to shoot it all over again.", 6, 3, 5, 7)
    call cho_main("you mUst think I'm really sexy, don't you?", 6, 3, 6, 9)
    "Precum pours from your engorged tip. Dripping down your hand."
    call cho_main("Oh god...", 6, 3, 5, 5)
    call cho_main("oh god...there's so much.", 6, 3, 6, 5)
    "The quiet pleasure in Cho's eyes pushes you over the edge and begin to cum violently."
    m "You retard!"
    #-Genie chibi Cums-
    with d3
    hide screen bld1
    with d3
    show screen genie_jerking_sperm
    with d3
    call cho_main("....", 6, 2, 5, 4)
    call cho_main("....what did you say?", 6, 2, 5, 7)
    #-Genie Chibi continues to cum-
    m "Shut up. Don't ruin this for me."
    call cho_main("......", 6, 3, 6, 9)
    call cho_main("............", 6, 3, 5, 4)
    #-Genie Chibi stops cumming-
    show screen genie_jerking_sperm_02
    with d3
    call cho_main("Can i have my points now?", 1, 3, 2, 9)
    show screen genie
    hide screen genie_jerking_off
    hide screen genie_jerking_sperm
    with d3
    m "....."
    m "......Very well. [cho_points] to Ravenclaw."
    $ ravenclaw += cho_points
    call cho_main("Thank you, sir...", 6, 3, 5, 1)
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True
    ">Cho quickly puts her clothes on before leaving."
    hide screen cho_chang
    hide screen genie_jerking_sperm_02
    jump cho_end_event
    
label cho_favor_1_1_2:
    "You gaze into Cho's eys, her tight, young body has you harder than a troll's ass."
    call cho_main("....", 6, 3, 5, 5)
    call cho_main("........", 6, 3, 6, 5)
    call cho_main("........you're...so big and...", 6, 3, 5, 7)
    call cho_main(".....hard.", 6, 3, 6, 6)
    "You can practically feel the girl's eyes on your cock as you drag your hand up and down its length."
    call cho_main("are you going to finish soon?", 6, 3, 6, 1)
    call cho_main("and spurt it all over your desk again.", 6, 3, 5, 7)
    "Precum pours from your engorged tip. Dripping down your hand."
    call cho_main("Is my body that good?", 6, 3, 6, 9)
    call cho_main("your dripping everywhere, professor", 6, 3, 5, 5)
    call cho_main("oh god...your balls looks so full. There's so much.", 6, 3, 6, 5)
    "The perverse wonder in Cho's voice pushes you over the edge."
    "You pump your cock like a madman, and cum violently."
    m "Yes, you whore!"
    #-Genie chibi Cums-
    with d3
    hide screen bld1
    with d3
    show screen genie_jerking_sperm
    with d3
    call cho_main("....", 6, 2, 5, 4)
    call cho_main("....what did you say?", 6, 2, 5, 7)
    #-Genie Chibi continues to cum-
    m "YOu...fucking...whore."
    call cho_main("......", 6, 3, 6, 9)
    call cho_main("............", 6, 3, 5, 4)
    #-Genie Chibi stops cumming-
    show screen genie_jerking_sperm_02
    with d3
    "You cum covers the desk in font of you in thick, slimy gobs."
    call cho_main("(Look at it all!)", 4, 3, 4, 5)
    call cho_main("......", 6, 3, 5, 5)
    call cho_main("(i wonder what it tastes li-)", 6, 3, 5, 6)
    call cho_main("!", 4, 3, 4, 5)
    call cho_main("Can i have my points now?", 1, 3, 2, 5)
    show screen genie
    hide screen genie_jerking_off
    hide screen genie_jerking_sperm
    with d3
    m "....."
    m "......Huh? Oh, yeah. Sure. [cho_points] to Ravenclaw."
    $ ravenclaw += cho_points
    call cho_main("Thank you, sir...", 6, 3, 5, 1)
    $ cc_wear_top = True
    $ cc_wear_bra = True
    $ cc_wear_stockings = True 
    $ cc_wear_skirt = True
    $ cc_wear_panties = True
    $ cc_wear_vest = True
    ">Cho quickly puts her clothes on before leaving."
    hide screen cho_chang
    hide screen genie_jerking_sperm_02
    jump cho_end_event



label cho_favor_1_2:
    $ cho_points = 15
    if cho_whoring < 1:
        $ cho_whoring += 1
    m "Miss Chang how would you like to earn 15 house points the easy way?"
    call cho_main("what do i have to do?", 2, 3, 1, 7)
    m "I want to see your body again?"
    call cho_main("you want me to get naked, sir?", 6, 3, 5, 7)
    m "Of course."
    m "If you're not interested, I'm sure Hermione wouldn't mind..."
    call cho_main("!", 4, 3, 1, 3)
    call cho_main("I'll do it.", 1, 1, 2, 1)
    call cho_main("Only...", 2, 3, 1, 7)
    call cho_main("You're not going to...you know...again, are you sir?", 2, 3, 1, 5)
    m "And what would that be, girl?"
    "Cho shifts uncomfortably on her feet."
    call cho_main("Don't make mE say it, Professor.", 2, 3, 2, 7)
    m "Say what, girl?"
    call cho_main("....masturbate.", 2, 3, 1, 5)
    m "What was that?"
    call cho_main("You're not going to jerk off again, are you?", 1, 2, 1, 8)
    menu:
        "-of course-":
            m "Of course. Why else would you be naked."
            "Cho takes a deep breath."
            call cho_main("i want 20 points.", 2, 3, 1, 5)
            menu:
                "-offer 15-":
                    m "You'll get 15. No more."
                    call cho_main("Fine.", 6, 2, 5, 9)
                    $ cho_mad += 3
                    $ cho_points = 15
                    pass
                "-20 sounds good-":
                    m "20 Sounds good to me."
                    call cho_main("Alright.", 1, 3, 2, 9)
                    $ cho_points = 20
                    pass
                "-Give her 25-":
                    m "I'll give you 25."
                    call cho_main("Really?", 1, 3, 1, 7)
                    $ cho_mad -= 1
                    $ cho_points = 25
                    pass
            menu:
                "-Be Aggressive-":
                    "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
                    m "Get on with it, girl."
                    call cho_main("Yes, sir!", 1, 3, 2, 7)
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Cho grits her teeth and removes her top in one swift motion."
                    m "That's better. Now the bottoms."
                    call cho_main("Yes, sir.", 1, 3, 1, 9)
                    $ cc_wear_skirt = False 
                    "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
                    call cho_main("(house points...loads of house points....)", 1, 1, 1, 1)
                    "Her hands nervously move to her bra."
                    $ cc_wear_bra = False
                    "She pulls it up, over her head, and lets it fall to the ground."
                    $ cc_wear_panties = False 
                    "Finally, she pushes her panties over her hips."
                    m "Very good."
                    call cho_main("........", 1, 1, 1, 1)
                    call cho_main("...............", 1, 1, 1, 1)
                    call cho_main("......................", 1, 1, 1, 1)
                    call cho_main("Um...", 1, 1, 1, 1)
                    call cho_main("um...are you going to", 1, 1, 1, 1)
                    call cho_main("um...are you going to...do it?", 1, 1, 1, 1)
                    "You slide your hands under your robes and pull your cock out."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "Cho's athletic, young body has you hard as stone."
                    call cho_main("....", 3, 3, 3, 9)
                    call cho_main("........", 1, 3, 2, 5)
                    call cho_main("........you're...so big and...", 1, 3, 1, 6)
                    call cho_main(".....hard.", 4, 3, 1, 6)
                    "You can practically feel the girl's eyes on your cock as you drag your hand up and down its length."
                    call cho_main("....", 1, 3, 2, 6)
                    call cho_main("you're going to spurt soon, aren't you?", 1, 3, 1, 5)
                    call cho_main("you're going to shoot it all over again.", 1, 3, 2, 6)
                    "Precum pours from your engorged tip. Dripping down your hand."
                    call cho_main("you mUst think I'm really sexy, don't you?", 1, 3, 1, 1)
                    call cho_main("Oh god...", 1, 3, 2, 7)
                    call cho_main("oh god...there's so much.", 1, 3, 1, 6)
                    "The quiet pleasure in Cho's eyes pushes you over the edge and begin to cum violently."
                    m "You retard!"
                    #-Genie chibi Cums-
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    call cho_main("....", 6, 2, 5, 4)
                    call cho_main("....what did you say?", 6, 2, 5, 7)
                    #-Genie Chibi continues to cum-
                    m "Shut up. Don't ruin this for me."
                    call cho_main("......", 1, 3, 2, 5)
                    call cho_main("............", 1, 3, 1, 6)
                    #-Genie Chibi stops cumming-
                    call cho_main("Can i have my points now?", 1, 3, 2, 9)
                    show screen genie
                    hide screen genie_jerking_off
                    hide screen genie_jerking_sperm
                    with d3
                    m "....."
                    m "......Very well. [cho_points] to Ravenclaw."
                    $ ravenclaw += cho_points
                    call cho_main("Thank you, sir...", 6, 3, 5, 1)
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Cho quickly puts her clothes on before leaving."
                    hide screen cho_chang
                    hide screen genie_jerking_sperm_02
                    jump cho_end_event
                "-Be Nice-":
                    "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
                    m "Go on, girl."
                    call cho_main("Yes, sir!", 1, 3, 2, 1)
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Cho flashes a subdued smile and removes her top in one swift motion."
                    m "Nice."
                    call cho_main("Thank you, sir.", 3, 1, 3, 7)
                    $ cc_wear_skirt = False 
                    "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
                    call cho_main("is this okay?", 1, 3, 1, 9)
                    "Her hands nervously move to her bra."
                    $ cc_wear_bra = False 
                    "She pulls it up, over her head, and lets it fall to the ground."
                    call cho_main("what do you think?", 2, 3, 2, 5)
                    m "Simply. gorgeous."
                    $ cc_wear_panties = False 
                    "Finally, she pushes her panties over her hips."
                    m "Very nice."
                    call cho_main("........", 3, 3, 3, 4)
                    call cho_main("...............", 1, 3, 1, 4)
                    call cho_main("......................", 1, 3, 1, 9)
                    call cho_main("Um...", 1, 3, 2, 7)
                    call cho_main("um...are you going to", 1, 3, 1, 5)
                    call cho_main("um...are you going to...do it?", 1, 3, 4, 6)
                    m "Do what?"
                    call cho_main("you're paying extra so you can jerk off if you want!", 3, 2, 3, 7)
                    m "Well, if you insist."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    "You slide your hands under your robes and pull your cock out."
                    "You gaze into Cho's eys, her tight, young body has you harder than a troll's ass."
                    call cho_main("....", 3, 3, 3, 9)
                    call cho_main("........", 1, 3, 2, 5)
                    call cho_main("........you're...so big and...", 1, 3, 1, 6)
                    call cho_main(".....hard.", 4, 3, 1, 6)
                    "You can practically feel the girl's eyes on your cock as you drag your hand up and down its length."
                    call cho_main("are you going to finish soon?", 1, 3, 1, 5)
                    call cho_main("and spurt it all over your desk again.", 1, 3, 2, 6)
                    "Precum pours from your engorged tip. Dripping down your hand."
                    call cho_main("Is my body that good?", 1, 3, 1, 1)
                    call cho_main("your dripping everywhere, prefessor", 1, 3, 2, 7)
                    call cho_main("oh god...your balls looks so full. There's so much.", 1, 3, 1, 6)
                    "The perverse wonder in Cho's voice pushes you over the edge."
                    "You pump your cock like a madman, and cum violently."
                    m "Yes, you whore!"
                    #-Genie chibi Cums-
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    call cho_main("....", 6, 2, 6, 5)
                    call cho_main("....what did you say?", 6, 2, 5, 6)
                    #-Genie Chibi continues to cum-
                    m "YOu...fucking...whore."
                    call cho_main("......", 1, 3, 2, 5)
                    call cho_main("............", 1, 3, 1, 6)
                    #-Genie Chibi stops cumming-
                    "You cum covers the desk in font of you in thick, slimy gobs."
                    show screen genie
                    hide screen genie_jerking_off
                    hide screen genie_jerking_sperm
                    with d3
                    call cho_main("(Look at it all!)", 4, 3, 4, 5)
                    call cho_main("......", 4, 3, 4, 6)
                    call cho_main("(i wonder what it tastes li-)", 6, 3, 5, 5)
                    call cho_main("!", 4, 2, 4, 6)
                    call cho_main("Can i have my points now?", 1, 3, 2, 9)
                    m "....."
                    m "......Huh? Oh, yeah. Sure. [cho_points] to Ravenclaw."
                    $ ravenclaw += cho_points
                    call cho_main("Thank you, sir...", 6, 3, 5, 1)
                    $ cc_wear_top = True
                    $ cc_wear_bra = True
                    $ cc_wear_stockings = True 
                    $ cc_wear_skirt = True
                    $ cc_wear_panties = True
                    $ cc_wear_vest = True
                    ">Cho quickly puts her clothes on before leaving."
                    hide screen cho_chang
                    hide screen genie_jerking_sperm_02
                    jump cho_end_event
        "-I hadn't planned on it-":
            m "I hadn't planned on it."
            call cho_main("Oh.", 1, 1, 2, 9)
            call cho_main("Okay then.", 1, 1, 2, 7)
            menu:
                "-Be Aggressive-":
                    "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
                    m "Get on with it, girl."
                    call cho_main("Yes, sir!", 3, 1, 3, 3)
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Cho grits her teeth and removes her top in one swift motion."
                    m "That's better. Now the bottoms."
                    call cho_main("Yes, sir.", 3, 3, 3, 7)
                    $ cc_wear_skirt = False 
                    "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
                    call cho_main("(House points...loads of house points....)", 3, 3, 3, 4)
                    "Her hands nervously move to her bra."
                    $ cc_wear_bra = False
                    "She pulls it up, over her head, and lets it fall to the ground."
                    $ cc_wear_panties = False 
                    "Finally, she pushes her panties over her hips."
                    m "Very good."
                    call cho_main("........", 3, 3, 3, 4)
                    call cho_main("...............", 1, 3, 1, 4)
                    call cho_main("......................", 1, 3, 1, 9)
                    call cho_main("Um...", 1, 3, 2, 7)
                    call cho_main("um... is this enough?", 1, 3, 1, 5)
                    menu:
                        "-That's enough-":
                            m "You can put your clothes back on."
                            m "15 points to Ravenclaw."
                            $ ravenclaw += cho_points
                            call cho_main("Thank you, sir...", 6, 2, 6, 9)
                            $ cc_wear_top = True
                            $ cc_wear_bra = True
                            $ cc_wear_stockings = True 
                            $ cc_wear_skirt = True
                            $ cc_wear_panties = True
                            $ cc_wear_vest = True
                            ">Cho quickly puts her clothes on before leaving."
                            hide screen cho_chang
                            jump cho_end_event
                        "-Jerk off-":
                            "You slide your hands under your robes and pull your cock out."
                            "Cho's tight, athletic body sends shivers through you."
                            call cho_main("what are you doing?", 4, 2, 4, 3)
                            call cho_main("i'm not watching you do that for a measly 15 house points.", 6, 2, 5, 7)
                            "Ignoring Cho's protests, your fingers wrap around your thick cock."
                            call cho_main(".......", 6, 3, 5, 9)
                            "Cho takes a deep breath."
                            call cho_main("20 points.", 6, 3, 6, 7)
                            menu:
                                "-offer 15-":
                                    "You look the poor girl in the eyes and continue jerking you cock."
                                    m "You'll get 15. No more."
                                    call cho_main("Fine.", 6, 2, 5, 9)
                                    $ cho_mad += 2
                                    $ cho_points = 15
                                    jump cho_favor_1_1_1
                                "-Give her 20-":
                                    m "Sounds good."
                                    $ cho_points = 20
                                    jump cho_favor_1_1_1
                                "-Giver her 25-":
                                    m "I'll give you 25."
                                    call cho_main("Really?", 1, 3, 1, 7)
                                    $ cho_mad -= 2
                                    $ cho_points = 25
                                    jump cho_favor_1_1_1
                "-Play Nice-":
                    "Despite her apparent confidence, Cho's hands shake as she reaches for the edge of her top."
                    m "Go on, girl."
                    call cho_main("Yes, sir!", 1, 3, 2, 1)
                    $ cc_wear_top = False
                    $ cc_wear_vest = False
                    $ cc_wear_acc = False 
                    "Cho flashes a subdued smile and removes her top in one swift motion."
                    m "Nice."
                    call cho_main("Thank you, sir.", 3, 1, 3, 7)
                    $ cc_wear_skirt = False 
                    "Cho hooks her delicate thumbs into the tight band on her skirt and pushes it over the tight curve of her hips."
                    call cho_main("is this okay?", 1, 3, 1, 9)
                    "Her hands nervously move to her bra."
                    $ cc_wear_bra = False 
                    "She pulls it up, over her head, and lets it fall to the ground."
                    call cho_main("what do you think?", 2, 3, 2, 5)
                    m "Simply. gorgeous."
                    $ cc_wear_panties = False 
                    "Finally, she pushes her panties over her hips."
                    m "Very nice."
                    call cho_main("........", 3, 3, 3, 4)
                    call cho_main("...............", 1, 3, 1, 4)
                    call cho_main("......................", 1, 3, 1, 9)
                    call cho_main("Um...", 1, 3, 2, 7)
                    call cho_main("Um...can i put my clothes back on now?", 6, 3, 5, 7)
                    menu:
                                
                        "-That's enough-":
                            m "You can put your close back on."
                            m "15 points to Ravenclaw."
                            $ ravenclaw += cho_points
                            call cho_main("Thank you, sir...", 6, 2, 6, 9)
                            $ cc_wear_top = True
                            $ cc_wear_bra = True
                            $ cc_wear_stockings = True 
                            $ cc_wear_skirt = True
                            $ cc_wear_panties = True
                            $ cc_wear_vest = True
                            ">Cho quickly puts her clothes on before leaving."
                            hide screen cho_chang
                            jump cho_end_event
                        "-jerk off-":
                            "You slide your hands under your wizard robes and pull your cock out."
                            hide screen blktone8
                            with d3
                            hide screen genie
                            show screen genie_jerking_off
                            with d3
                            "Cho's tight, vulnerable body has you incredibly aroused."
                            call cho_main("what are you doing?", 4, 2, 4, 3)
                            call cho_main("i didn't agree to this!", 6, 2, 5, 7)
                            "Ignoring Cho's protests, your fingers wrap around your thick cock."
                            call cho_main(".......", 6, 3, 5, 9)
                            "Cho takes a deep breath."
                            call cho_main("20 points.", 6, 3, 6, 7)
                            menu:
                                "-offer 15-":
                                    "You look the poor girl in the eyes and continue jerking you cock."
                                    m "You'll get 15. No more."
                                    call cho_main("Fine.", 6, 2, 5, 9)
                                    $ cho_mad += 2
                                    jump cho_favor_1_1_1
                                "-Give her 20-":
                                    $ cho_points = 20
                                    m "Sounds good."
                                    jump cho_favor_1_1_2
                                "-Giver her 25-":
                                    $ cho_points = 25
                                    m "I'll give you 25."
                                    call cho_main("Really?", 1, 3, 1, 7)
                                    $ cho_mad -= 2
                                    jump cho_favor_1_1_2

###Favor 2###
label cho_favor_2:
    m "(Right, then I'll just fondle Cho's ass a little.)"
    menu:
        "-Touch her ass-":
            if chof2_first: #have to include new boolean chof2_first=False
                $ chof2_first = False
                g9 "Miss Chang, I'd like to touch your ass."
                call cho_main("My...ass?", 6, 3, 6, 1)
                m "Yes. I'd like to touch it."
                call cho_main("I knew you liked my ass.", 5, 1, 1, 5)
                call cho_main("{size=-4}(i knew he couldn't resist for long.){/size}", 5, 1, 2, 6)
                call cho_main("if you want to touch my firm ass, it's going to cost you.", 3, 1, 3, 3)
                call cho_main("I'll do it for 40 house points.", 1, 1, 2, 7)
                m "That's a lot just to grab a students ass."
                ">Cho twists her lithe, muscular body."
                ">You can see the firm lines of her ass under her uniform."
                call cho_main("come on, PRofessor... isn't it worth it?", 1, 1, 1, 1)
                m "That is a nice ass..."
                m "But I could get Hermione to do it for..."
                menu:
                    "-25 points-":
                        m "I could get Hermione to do it for only 25 points."
                        call cho_main("25?", 4, 2, 1, 3)
                        call cho_main("25? What cheap slag.", 5, 2, 2, 4)
                        call cho_main("I'll do it for 40.", 1, 2, 1, 7)
                        m "Alright, 40. But it better be worth it."
                        jump chofbm
                    "-35 points-":
                        m "I could get Hermione to do it for 35 points."
                        call cho_main("{siZe=-2}35? Really?....{/size}", 6, 2, 5, 9)
                        call cho_main("{size=+2}If her fat ass is worth 35 then mine must be worth 40.{/size}", 3, 2, 3, 8)
                        m "Fine."
                        jump chofbm
                    "-50 points-":
                        m "I could get Hermione to do it for 50 points."
                        call cho_main("50!", 4, 2, 1, 7)
                        call cho_main("50! are you serious! No way.", 6, 2, 5, 1)
                        call cho_main("but, she doesn't even work out...", 6, 3, 6, 9)
                        m "I suppose you're ass will do for now, but I'm only paying you 40 house points."
                        call cho_main("my ass will do?!", 6, 2, 5, 3)
                        call cho_main("i'll show you whose ass is better!", 6, 2, 5, 1)
                        $ cho_mad +5 #new variable cho_mad
                        jump chofbm
                    "-Nothing-":
                        m "I could get Hermione to do it for absolutely nothing."
                        call cho_main("Nothing?", 4, 2, 1, 7)
                        call cho_main("what a little slut.", 6, 1, 6, 5)
                        call cho_main("you'll still haVE to pay me, of course.", 3, 2, 3, 7)
                        call cho_main("40 house Points.", 6, 2, 5, 8)
                        m "Very Well, Miss Chang."
                        jump chofbm
            else:
                    m "Miss Chang. I'd like to touch your butt again."
                    if cho_whoring  == 1: #new variable cho_whoring 
                        call cho_main("welL...okay. but it'll cost you 40 house points", 2, 3, 2, 7)
                        m "Very well. Now come over here, girl."
                        jump chofbm
                    if cho_whoring  == 2:
                        call cho_main("alright, professor.", 1, 3, 2, 5)
                        call cho_main("40 house points, right?", 2, 1, 1, 7)
                        m "Of course, Miss Chang."
                        jump chofbm
                    if cho_whoring  == 3:
                        call cho_main("You do?", 1, 1, 1, 5)
                        call cho_main("are you going to wank off?", 6, 3, 5, 6)
                        menu:
                            "Of course.":
                                m "Of course."
                                call cho_main("i guess I'd better take off my panties.", 6, 3, 6, 6)
                            "No Way.":
                                m "Of course not. What do you take me for, a pervert?"
                                call cho_main("Well...", 6, 1, 2, 1)
                        jump chofbm

label chofbm:
#Cho chibi walks over to Dumbledore's desk and turns around.
    if cho_whoring  == 1:
        $ cho_whoring += 1
        if not chof2_first:
            call cho_main("AlrighT...{w=2} you can touch me a little.", 1, 3, 2, 5)
            ">Cho is standing just inches in front of you, the firm globes of her ass-"
            stop music
            $ renpy.play('sounds/scratch.wav')
            call cho_main("hey! hogwarts, like most respectable institutions for magical learning, is locatED in the UK.", 3, 2, 3, 3)
            call cho_main("please, stick to the metric system.", 3, 2, 3, 4)
            ">Ah, yes...well..."
            #play music fadein 1.5
        else:
            call cho_main("Alright...", 1, 3, 2, 5)
            call cho_main("Alright...you can touch me a little.", 1, 3, 2, 6)
        ">Cho is standing mere centimeters in front of you, the firm globes of her ass barely visible under her skirt."
        ">Cho hands remain firmly planted on the edge of your desk."
        ">You feel her quiver as the tips of your fingers touch her warm thighs."
        ">Cho's hands grip the desk firmly as your hands begin to slide up her legs."
        ">You reach her panties, and feeling the contrast between flesh and soft fabric, you guide your palms over both cheeks."
        ">You give both a series of firm squeezes, appreciating the thick, tight muscle underneath."
        call cho_main("prof-Professor...", 3, 3, 3, 5)
        ">You hear Cho stiffle a nervous cry. Her ass squeezes tight under your palms."
        call cho_main("that's enouGh, right Professor?", 1, 3, 2, 9)
        menu:
            "\"Yes\"":
                m "Yes. I think that did the trick."
                call cho_main("THank you, Professor.", 1, 1, 2, 1)
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                jump chof2end
            "\"Absolutely not!\"":
                m "Absolutely not. I'm paying you 40 house points for this, girl."
                call cho_main("But, sir, I-", 4, 3, 1, 7)
                ">You give Cho's ass an aggressive squeeze."
                m "I'll tell you when it's enough."
                call cho_main("Fine.", 5, 2, 2, 9)
                $ cho_mad += 2
                ">Cho's ass feels smooth and warm under your touch. Nevertheless, you begin to savage the poor girls ass."
                call cho_main("Ow.", 5, 2, 1, 4)
                call cho_main("ow. ow. That hurts!", 5, 2, 1, 7)
                call cho_main("Professor!", 5, 2, 1, 3)
                call cho_main("PRofessor! Professor, please stop.", 5, 2, 1, 8)
                menu:
                    "-Do as she asks-":
                        ">You come to your senses and let the poor girl's ass be."
                        ">Cho quickly pulls her skirt back down, rubbing her tender ass."
                        call cho_main("Thank you, sir.", 3, 1, 3, 4)
                        call cho_main("Thank You, sir. Can i have my house points now?", 2, 3, 1, 7)
                        m "Of course, Miss Chang. You earned them."
                        m "40 points to Ravenclaw."
                        $ ravenclaw += 40
                        jump chof2end
                    "-Keep going-":
                        ">You ignore the foolish girl's cries and continue to abuse her ass, sliding your hands under her panties."
                        call cho_main("Stop!", 4, 2, 1, 3)
                        ">You grab Cho's ass tightly and squeeze with all your might."
                        ">The star quidditch player falls forward over your desk."
                        call cho_main("It hurts!", 4, 3, 1, 3)
                        ">You roll your hands over her ass, then, you guide your thumbs to her tight, little, brown hole."
                        ">You can feel her beginning to fight, as you squeeze tightly and pull her ass open."
                        call cho_main("Professor Dumbledore!", 3, 2, 3, 3)
                        ">You suddenly release her ass and rain your firm hands across her cheeks."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch
                        call cho_main("...", 3, 3, 3, 4)
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white 
                        with hpunch
                        call cho_main("ockk!", 6, 3, 6, 4)
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white
                        with hpunch 
                        call cho_main("(it hurts so bad!)", 4, 3, 1, 1)
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        hide screen white 
                        with hpunch
                        ">Cho's breathing is heavy and her legs shake under your assault."
                        ">A thick, red outline of your hand is bruising on her ass."
                        call cho_main("Ack!", 4, 3, 1, 3)
                        call cho_main("Ack!...", 4, 2, 1, 5)
                        call cho_main("ack!...Professor!", 4, 2, 1, 3)
                        ">Cho finally gains enough control to wrench free of your grasp, and quickly moves away."
                        #Cho chibi walks to the middle of the room.
                        call cho_main("That's too far!", 3, 2, 3, 3)
                        call cho_main("i never agreed to any of that.", 5, 2, 1, 3)
                        call cho_main(".......i want 60 points.", 3, 2, 3, 3)
                        menu:
                            "-She earned 60-":
                                m "Very well. That was more than we agreed to. 60 points to Ravenclaw."
                                call cho_main("Thank you, sir.", 5, 1, 2, 4)
                                $ cho_mad += 5
                                $ ravenclaw += 60
                                jump chof2end
                            "\"That was a bit much. 80 points\"":
                                m "I think I got a little carried away."
                                call cho_main("...", 6, 2, 6, 4)
                                m "80 points to Ravenclaw."
                                call cho_main("Really?", 6, 2, 5, 7)
                                call cho_main("well, i suppose it wasn't that bad...", 6, 3, 6, 9)
                                $ cho_mad +1
                                $ ravenclaw += 80
                                jump chof2end
                            "\"(How dare she!) 0 points!\"":
                                m "How dare you defy your headmaster, Rumbledwarf!"
                                m "If you don't come back here, you'll get nothing."
                                call cho_main("What!", 4, 3, 1, 3)
                                call cho_main("That's not fair!", 4, 2, 1, 3)
                                m "Well?"
                                call cho_main("Fine!", 6, 2, 5, 4)
                                $ cho_mad +15
                                #Cho chibi returns to Dumbledore's desk.
                                ">Cho returns to your desk."
                                ">You catch a glimpse of her furious tears as she presents you her tender ass."
                                ">Wasting no time, you quickly tear the poor girls panties down and plant your hands on her firm flesh."
                                call cho_main("...", 4, 2, 2, 5)
                                pause
                                ">Pulling her cheeks apart, you begin to rub your thumbs across the tight ring of her virgin asshole."
                                call cho_main("...", 6, 3, 6, 5)
                                call cho_main("......", 6, 3, 5, 6)
                                ">You can feel Cho's body tensing up."
                                ">You wet a finger with your saliva and begin to prod her asshole."
                                call cho_main(".........", 4, 3, 4, 5)
                                m "Just relax."
                                ">Finally, you feel it give and your thick digit begins to slowly slide in."
                                call cho_main("Profes-....", 6, 3, 6, 6)
                                ">Cho fights the urge to cry out. Letting you continue."
                                ">It's clear she wants her points more than anything."
                                m "{size=-2}(Don't you worry girl. You'll get your points.){/size}"
                                ">Once your finger is completely buried you begin to pull it back."
                                ">The muscle clings to your finger as it slides out."
                                call cho_main("...", 1, 3, 2, 5)
                                ">You can feel Cho tensing up again."
                                ">Your finger slides in and out of her tight asshole."
                                ">Cho falls forward on the desk. Her breathing is getting faster, more ragged."
                                call cho_main("...", 3, 3, 3, 5)
                                ">Suddenly, you feel her muscular ring pulse, squeezing your finger with unbearable tightness."
                                call cho_main("Professor!", 4, 3, 4, 6)
                                ">Cho cums hard on your finger, before completely collapsing."
                                m "40 points to Ravenclaw."
                                call cho_main("{size=-2}.....yay.{/size}", 6, 3, 5, 5)
                                $ ravenclaw += 40
                                jump chof2end
    if cho_whoring  == 2:
        call cho_main("...", 1, 1, 1, 1)
        call cho_main("......", 1, 1, 1, 1)
        call cho_main("......Aren't you going to touch me?", 1, 1, 1, 1)
        ">Cho pulls up the bottom of her skirt, revealing her ass, then bends forward over your desk."
        call cho_main("Well?", 1, 1, 1, 1)
        ">Cho wiggles her ass at you."
        m "By the sands...."
        ">Your hands fly toward Cho's tight cheeks and grip them firmly."
        ">You give both a series of firm squeezes, practically drinking in the feel of the tight muscle underneath."
        cho_sexy "Prof-Professor..."
        ">You hear Cho stiffle a cry. Her ass squeezes tight under your palms."
        call cho_main("That's not enougH, is it, Professor?", 1, 1, 1, 1)
        menu:
            "No, that's quite enough.":
                m "No, no. That's quite enough. Thank you, Miss Chang."
                call cho_main("....uh. Yes. THank you, Professor.", 1, 1, 1, 1)
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                jump chof2end
            "Not Enough.":
                m "You're right. After all, I'm paying you 40 house points for this, girl."
                call cho_main("Yes, sir. But...", 1, 1, 1, 1)
                m "But what?"
                ">Cho begins to shake her hips suggestively, and move her ass."
                ">She hooks her thumbs in the waist of her panties and pulls them outward."
                cho_sexy "Well, sir. I suppose for 60 points I could take these ANNOYING panties off."
                call cho_main("anD LEt you feEL me, sir...", 1, 1, 1, 1)
                menu:
                    "60 it is.":
                        m "Well then, 60 it is."
                        $ ravenclaw += 60
                        call cho_main("{size=-4}(wow, that was easy.){/size}", 1, 1, 1, 1)
                        call cho_main("{size=-4}(i bet his nasty, old cock is going crazy...){/size}", 1, 1, 1, 1)
                        ">Cho slowly pushes her panties down past her hips, until they finally fall to her feet."
                        ">She steps out of them and spreads her feet wide before putting her hands on your desk."
                        ">The young quidditch star arches her back, thrusting her firm ass toward you."
                        m "Very good, Miss Chang."
                        call cho_main("Thank you, sir.", 1, 1, 1, 1)
                        jump chof2wl2
                    "50 seems more fair.":
                        m "I think 50 points seems more fair. Don't you?"
                        call cho_main("50?", 1, 1, 1, 1)
                        ">Cho begins to wiggle her panties around her ass seductively."
                        call cho_main("Come on, I think it's worth much more than that...", 1, 1, 1, 1)
                        menu:
                            "50 points.":
                                m "50 points."
                                call cho_main("Well, okay.", 1, 1, 1, 1)
                                call cho_main("{size=-4}(60 points was high anyway.){/size}", 1, 1, 1, 1)
                                $ ravenclaw += 50
                                ">Cho pushes her panties down and puts her hands on your desk."
                                jump chof2wl2
                            "Fine. 55 points.":
                                m "Very well, Miss Chang. I'll give you 55 points."
                                call cho_main("hm. 55 points seems fair.", 1, 1, 1, 1)
                                $ ravenclaw += 55
                                ">Cho moves her ass seductively, releasing her panties and placing her hands flat on your desk."
                                call cho_main("but, Professor...", 1, 1, 1, 1)
                                m "Yes?"
                                cho_sexy "I don't think I can reach. Will you help me?"
                                m "Of course, Miss Chang. It's important for the headmaster to take a hands on approach."
                                ">You lean forward and slowly slide Cho's panties down, revealing the girls perfect ass."
                                call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                jump chof2wl2
                            "No.":
                                ">You give Cho's ass an aggressive squeeze."
                                m "No. I don't think so."
                                call cho_main("What?", 1, 1, 1, 1)
                                call cho_main("well...i guess I could do it for 50.", 1, 1, 1, 1)
                                menu:
                                    "Yes.":
                                        m "Very well. 50 house points. You drive a hard bargain, Miss Chong."
                                        call cho_main("MY name Is Chang. And yes, I do.", 1, 1, 1, 1)
                                        $ ravenclaw += 50
                                        $ cho_mad +1
                                        ">Cho quickly pushes her panties off her hips, letting them fall to the ground before bending over your desk."
                                        jump chof2wl2
                                    "No.":
                                        m "No."
                                        call cho_main("Oh, okay.", 1, 1, 1, 1)
                                        ">Cho lets her panties snap back into place. Nevertheless, you begin to gently squeeze the girls firm ass."
                                        call cho_main("...", 1, 1, 1, 1)
                                        call cho_main("......", 1, 1, 1, 1)
                                        call cho_main(".........", 1, 1, 1, 1)
                                        call cho_main("is that enough, sir?", 1, 1, 1, 1)
                                        menu:
                                            "Yes. That's enough.":
                                                ">You nod."
                                                m "Yes. That was fine, Miss Chang."
                                                ">Cho quickly pulls her skirt back down, smoothing her panties."
                                                call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                                m "40 points to Ravenclaw."
                                                $ ravenclaw += 40
                                                jump chof2end
                                            "Keep going.":
                                                ">You ignore the girl's question and continue to molest her ass, sliding your hands under her panties."
                                                call cho_main("I knew you couldn't resist.", 1, 1, 1, 1)
                                                ">You grab Cho's bare ass tightly and give it a quick squeeze."
                                                m "40 points to Ravenclaw."
                                                call cho_main("THank you, Professor.", 1, 1, 1, 1)
                                                $ ravenclaw += 40
                                                jump chof2end

        label chof2wl2:
        ">You stare at Cho's tight, young ass, drinking it in."
        ">It looks like all of her Squidstitching has paid off."
        ">The asian girls ass looks incredible."
        cho_seductive "Well?"
        ">You grab Cho's firm ass in booth hands and squeeze tightly."
        ">Your thick cock strains against your robes."
        menu:
            "-Jerk off-":
                ">You stare at the girl's ass, mezmerized."
                ">You continue to molest her firm ass with one hand, while the other pulls your cock out of your wizard robes."
                call cho_main("what are you doing?", 1, 1, 1, 1)
                ">You begin to pump your cock, squeezing her ass."
                cho_seductive "A-alright, but I want an extra five... {w=.5} no TEN points."
                menu:
                    "Fine.":
                        ">You give your throbbing cock three quick pumps before nodding."
                        m "Fine. You'll get your points, girl."
                        call cho_main("okay, pRofessor. but you'd better stop before...you know.", 1, 1, 1, 1)
                        ">Cho shakes her ass from side to side."
                        ">You give it a light smack as it comes back, stroking your cock."
                        cho_sexy_surprise "..."
                        ">Cho bounces her ass up and down a few times. You slap it hard."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{size=-4}(It hurts...but it also feels good.){/size}", 1, 1, 1, 1)
                        call cho_main("Professor Dumbl-{nw}", 1, 1, 1, 1)
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{size=-4}(OH blimey. that's starting to feel really good.){/size}", 1, 1, 1, 1)
                        ">Every slap brings your cock closer, until you feel a familiar pressure in your magic balls."
                        menu:
                            "-Cum-":
                                ">Finally, it's too much for you, and with one final smack-"
                                $ renpy.play('sounds/slap_02.mp3')
                                show screen white
                                "{size=+4}SLAP!{/size}"
                                #Shake the screen
                                hide screen white 
                                ">Finally, it's too much for you, and with one final smack, your cock erupts all over Cho's ass."
                                m "Arg, you fucking slut!"
                                #Genie cums. - I'd need to know which screen to put here
                                cho_wideEyes "What is {size=+2}that?{/size}"
                                cho_wideEyesLookingBack "{size=+4}Are you cumming?{/size}"
                                ">Your cum splatters across the young girl's ass in thick, messy spurts."
                                call cho_main("Oh, my God...", 1, 1, 1, 1)
                                ">Your wrinkly old balls pull tight and you dump the last of your cum in a fat glob that lands on her asshole."
                                call cho_main("You {size=+2}completely{/size} covered me in your {size=+2}nasty{/size} {size=+3}old{/size} {size=+4}wizard cum!{/size}", 1, 1, 1, 1)
                                call cho_main("i'm a complete mess, you jerk!", 1, 1, 1, 1)
                                call cho_main("You owe me an extra 10 points!", 1, 1, 1, 1)
                                $ cho_mad +=1
                                menu:
                                    "Yes.":
                                        m "Yeah, sure. 10 more points to Ravenclaw."
                                        $ ravenclaw += 10
                                        call cho_main("look at this mess!", 1, 1, 1, 1)
                                        call cho_main("...", 1, 1, 1, 1)
                                        call cho_main("{sIze=-2}...Thank you, sir.{/size}", 1, 1, 1, 1)
                                        ">Cho quickly pulls her panties up over her cum soaked ass and smoothes her skirt."
                                        call cho_main("this should be okay.", 1, 1, 1, 1)
                                        jump chof2end
                                    "Too bad.":
                                        m "It's not my fault you made me cum."
                                        call cho_main("!!", 1, 1, 1, 1)
                                        m "You should be more careful."
                                        call cho_main("you can't be serious!", 1, 1, 1, 1)
                                        call cho_main("your smelly cum is all oveR my ass! i smell like...liKe...like Hermione!", 1, 1, 1, 1)
                                        m "Too bad."
                                        call cho_main("you're nothing but a dirty old wizard!", 1, 1, 1, 1)
                                        ">Cho grabs her panties from the floor and storms off leaving a trail of cum dripping to your door."
                                        $ cho_mad +5
                                        jump chof2end
                            "Better not.":
                                ">You stop at the last moment and put your cock away."
                                ">Your swollen balls throb with pressure."
                                call cho_main("are you okay?", 1, 1, 1, 1)
                                m "I'm a wizard, girl."
                                jump chof2end
                    "I'll give you 15.":
                        ">You give your throbbing cock a few quick pumps before rubbing the head across her ass cheek."
                        m "I'll give you 15."
                        call cho_main("15?...okay, Professor.", 1, 1, 1, 1)
                        ">Cho shakes her ass from side to side, lightly dragging her ass across the tip of your cock."
                        ">You give you cock a quick stroke before guiding it back against Cho's ass."
                        cho_sexy_surprise "What are doing back there..."
                        ">Cho bounces her ass up and down a few times. You slap your cock head against it."
                        call cho_main("{size=-4}(Oh my god...i can'T believe i'm letting an old man rub his cock on my ass.){/size}", 1, 1, 1, 1)
                        call cho_main("Professor Dumbledore, make sure you tell me before you-{w=.5}{nw}", 1, 1, 1, 1)
                        ">You give your cock several good pumps and bring your free hand down across Cho's firm ass."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("Professor Dumbledore, make sure you tell me bEFOre you-CUM!", 1, 1, 1, 1)
                        call cho_main("(Oh blimey!)", 1, 1, 1, 1)
                        ">Then you rub your cock head across her warm, naked ass flesh, dragging a trail of precum."
                        call cho_main("Professor...", 1, 1, 1, 1)
                        ">You slap your bulging cock against her ass again and bury the head between her cheeks."
                        ">You pump your cock like a madman, until you feel a familar pressure in your magic balls."
                        menu:
                            "Cum.":
                                ">Finally, it's too much for you, and with one final pump, your cock erupts between Cho's ass cheeks."
                                m "By Grabthar's Hammer!"
                                #Genie cums. - Find chibi
                                cho_wideEyes "Oh my God...What is that?"
                                cho_wideEyesLookingBack "{size=+2}Are you cumming?{/size}"
                                ">Your cum splatters between the young girl's meaty cheeks in thick, messy spurts."
                                call cho_main("Oh, my God...", 1, 1, 1, 1)
                                ">You pump your cock a few more times and dump the last of your cum in a fat, messy glob right against her asshole."
                                call cho_main("...", 1, 1, 1, 1)
                                call cho_main("my ass feels so gross!", 1, 1, 1, 1)
                                call cho_main("it's sO sticky. You owe me an extra 10 points!", 1, 1, 1, 1)
                                menu:
                                    "Why not?":
                                        m "Yeah, sure. 10 more points to Ravenclaw."
                                        $ ravenclaw += 10
                                        call cho_main("look at this mess!", 1, 1, 1, 1)
                                        call cho_main("...", 1, 1, 1, 1)
                                        call cho_main("{sIze=-2}...Thank you, sir.{/size}", 1, 1, 1, 1)
                                        ">Cho quickly pulls her panties up over her cum soaked ass and smoothes her skirt."
                                        call cho_main("this should be okay.", 1, 1, 1, 1)
                                        jump chof2end
                                    "Too bad.":
                                        m "It's not my fault your ass made me cum."
                                        call cho_main("!!!", 1, 1, 1, 1)
                                        m "You should be more careful."
                                        call cho_main("you can't be serious!", 1, 1, 1, 1)
                                        call cho_main("your smelly cum is all iN my ass! i smell like...liKe...like Hermione!", 1, 1, 1, 1)
                                        m "Too bad."
                                        call cho_main("you're nothing but a dirty old wizard!", 1, 1, 1, 1)
                                        ">Cho grabs her panties from the floor and storms off leaving a trail of cum dripping to your door."
                                        $ cho_mad +5
                                        jump chof2end
                            "Warn Her.":
                                m "I'm almost there!"
                                call cho_main("Really?", 1, 1, 1, 1)
                                ">Suddenly, you feel Cho push back against you."
                                ">Your cock is wrapped tightly within her warm, muscular ass cheecks."
                                cho_sexy "Cum, Professor!"
                                ">Cho's ass rubs up and down, her ass tightly gripping your cock."
                                ">Finally, it's too much for you and with a grunt you bury your cock between her cheeks and cum violently."
                                m "Support Aka-{nw}"
                                cho_sexy "Shut up and cum, you dirty old man!"
                                m "Support Aka-gaaahhhh! You whore!"
                                #Genie cums. - find chibi
                                ">Spurt after nasty spurt of your cum shoots between the young girls ass, bubbling out over the top of her cheeks."
                                call cho_main("my ass feels so dirty!", 1, 1, 1, 1)
                                ">Completely spent, your fall back in your chair."
                                m "Well done girl."
                                call cho_main("thank you professor.", 1, 1, 1, 1)
                                ">Cho slips her panties back on, pulling them up over her cum filled crack."
                                ">Then she lightly pats her sticky ass."
                                call cho_main("Can't make a mess in the Hall, can I?", 1, 1, 1, 1)
                                jump chof2end
    if cho_whoring  ==3:
        ">Cho pulls up the bottom of her skirt, revealing her bare ass, then bends forward over your desk."
        call cho_main("Well?", 1, 1, 1, 1)
        ">Cho wiggles her naked ass at you."
        m "By the sands....you naughty girl."
        ">Your hands fly toward Cho's firm flesh and you grip her bare cheeks firmly."
        ">You give both a series of firm squeezes, practically drinking in the feel of the tight muscle underneath."
        cho_sexy "Dumbledore..."
        ">You hear Cho attempt to stiffle a moan. Her muscualar ass squeezes tight."
        call cho_main("You a want little more, don't you sir?", 1, 1, 1, 1)
        call cho_main("You...{w=1.5} you want to cum, don't you?", 1, 1, 1, 1)
        menu:
            "No, I want to preserve my essence.":
                m "No, Miss Chang. I'm on to you, you succubus!"
                call cho_main("....uh. What?", 1, 1, 1, 1)
                m "40 points to Ravenclaw."
                $ ravenclaw += 40
                call cho_main("....thank you?", 1, 1, 1, 1)
                jump chof2end
            "Of course!":
                m "{size=-4}(I understand. You nasty little girl.){/size}"
                m "You'd better earn these 40 points girl."
                call cho_main("Yes, sir. But...", 1, 1, 1, 1)
                m "But what?"
                ">Cho begins to shake her hips suggestively, and move her ass."
                ">Every so often you get a glimpse of her cute, little asshole."
                ">Cho leans forward, pulling her ass cheeks apart."
                call cho_main("WEll, sir. i suppose for just 65 points I could", 1, 1, 1, 1)
                cho_sexy "Well, sir. I suppose for just 65 points I could put your big, strong cock between these."
                cho_sexy "And rub you up and down until you cum."
                menu: #[No.]
                    "65 it is.":
                        m "Well then, 65 it is."
                        call cho_main("{size=-4}(wow, that was easy.){/size}", 1, 1, 1, 1)
                        call cho_main("{size=-4}(i bet his nasty, old wizard balls are completely full of cum.){/size}", 1, 1, 1, 1)
                        ">Cho arches her back, thusting her firm ass toward you."
                        ">Then the young quidditch star slowly backs into your cock, before wrapping her ass tightly around you."
                        m "Very good, Miss Chang."
                        call cho_main("Thank you, sir.", 1, 1, 1, 1)
                        jump chof2hd
                    "55 feels more right.":
                        m "I think 55 points is much more appropriate. Don't you?"
                        call cho_main("55?", 1, 1, 1, 1)
                        ">Cho begins to bounce and jiggle her ass seductively."
                        call cho_main("Come on, I think it's worth much more than that...", 1, 1, 1, 1)
                        cho_seductively "{size=-4}To cum...{/size}"
                        cho_seductively "{size=-2}To cum right...{/size}"
                        cho_seductively "{size=-1}To cum right{/size}...{w} here."
                        menu:
                            "55 points.":
                                m "55 points."
                                call cho_main("Well, okay.", 1, 1, 1, 1)
                                call cho_main("{size=-4}(60 points was high anyway.){/size}", 1, 1, 1, 1)
                                ">Cho pushes her ass back against you."
                                jump chof2hd
                            "Fine. 60 points.":
                                m "Very well, Miss Chang. I'll give you 60 points."
                                call cho_main("hm. 60 points isn't too bad.", 1, 1, 1, 1)
                                ">Cho moves her ass seductively, pulling her cheeks open wide before settling back against your cock."
                                call cho_main("Professor Dumbledore...", 1, 1, 1, 1)
                                m "Yes?"
                                call cho_main("your cock feels so...", 1, 1, 1, 1)
                                cho_sexy "So thick."
                                ">You lean forward and slowly slide your cock up and down Cho's valley."
                                call cho_main("Mmm. Thank you, sir.", 1, 1, 1, 1)
                                jump chof2hd
                    "No.":
                        ">You slap your stone hard cock against Cho's ass aggressively."
                        m "No. I don't think so."
                        call cho_main("What?", 1, 1, 1, 1)
                        call cho_main("well...i guess I could do it for 50.", 1, 1, 1, 1)
                        menu:
                            "Yes":
                                m "Very well. 50 house points. You drive a hard bargin, Miss Chong."
                                call cho_main("MY name Is Chang. And yes, I do.", 1, 1, 1, 1)
                                $ ravenclaw += 50
                                $ cho_mad +1
                                ">Cho quickly pushes her ass against you."
                                jump chof2hd
                            "No.":
                                m "No."
                                call cho_main("Oh, okay.", 1, 1, 1, 1)
                                ">Cho releases her cheeks, letting her ass clap together."
                                ">She bends over your desk and you begin to gently squeeze the girls firm, naked ass."
                                call cho_main("...", 1, 1, 1, 1)
                                call cho_main("......", 1, 1, 1, 1)
                                call cho_main(".........", 1, 1, 1, 1)
                                call cho_main("is that enough, sir?", 1, 1, 1, 1)
                                menu:
                                    "Yes. That's enough.":
                                        ">You nod."
                                        m "Yes. That was fine, Miss Chang."
                                        ">Cho quickly pulls her skirt back down, smoothing the fabric over her ass."
                                        call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                        m "40 points to Ravenclaw."
                                        $ ravenclaw += 40
                                        jump chof2end
                                    "Keep going.":
                                        ">You ignore the girl's question and continue to molest her ass, sliding your hands deep between her ass cheeks."
                                        call cho_main("I knew you couldn't resist.", 1, 1, 1, 1)
                                        ">You lean forward and give Cho's ass a quick bite before leaning back."
                                        m "40 points to Ravenclaw."
                                        call cho_main("THank you, Professor.", 1, 1, 1, 1)
                                        $ ravenclaw += 40
                                        jump chof2end

        label chof2hd:
        ">You can feel Cho's warmth spreading out over your body from her ass."
        ">You give her firm cheeks a quick slap."
        $ renpy.play('sounds/slap_02.mp3')
        show screen white
        "{size=+4}SLAP!{/size}"
        #Shake the screen
        hide screen white 
        cho_seductive "Professor!"
        ">You grab Cho's firm ass in booth hands and squeeze it tightly around your cock."
        ">Your thick cock strains and throbs."
        call cho_main("let me do all the work.", 1, 1, 1, 1)
        menu:
            "Fuck her ass cheeks.":
                ">You stare at the girl's ass, mezmerized."
                ">Finally, you stand up and push Cho down over your desk."
                call cho_main("sir, what are you doing?", 1, 1, 1, 1)
                ">You squeeze her cheeks tight and begin to pump your cock through the tunnel."
                cho_seductive "A-alright, you can do that, but I want an extra five points."
                menu: #[I'll give you 15] [No more points]
                    "Fine.":
                        ">You give the girl's ass several quick pumps before answering."
                        m "Very well, girl."
                        call cho_main("okay, Professor, but...but warn me before you cum.", 1, 1, 1, 1)
                        ">Cho shakes her ass from side to side, causing your slimy cock to pop free."
                        ">You give Cho's ass a light smack, squeezing your cock with her cheeks."
                        cho_sexySurprise "..."
                        ">You thrust forward enjoying the sensation on your head, then slap Cho hard."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{size=+4}(Oh my god!){/size}", 1, 1, 1, 1)
                        ">You feel Cho's thighs tighten with her ass."
                        call cho_main("{size=+4}(why does it feel so good?){/size}", 1, 1, 1, 1)
                        cho_sexy "{size=+4}(My pussy is tingling with every thrust of his nasty, old cock...){/size}"
                        call cho_main("Professor Dumbl-{w=.5}{nw}", 1, 1, 1, 1)
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        call cho_main("{sizE=+4}(oh! Oh, blimey!){/size}", 1, 1, 1, 1)
                        ">You feel Cho shifting her weight, and then notice her hand squeezed tight between her legs."
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        m "You're enjoying this aren't you?"
                        call cho_main("no! no, I'm not!", 1, 1, 1, 1)
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        m "Liar!"
                        $ renpy.play('sounds/slap_02.mp3')
                        show screen white
                        "{size=+4}SLAP!{/size}"
                        #Shake the screen
                        hide screen white 
                        ">Suddenly, you feel Cho's body start to convulse and her legs begin to shake uncontrollably."
                        call cho_main("proF {w}prof-PRofessor! I'm.{w=.75}{nw}", 1, 1, 1, 1)
                        call cho_main("PRofeSsor! I'm-I'm.{w=.75}{nw}", 1, 1, 1, 1)
                        call cho_main("I'm{W=.5}-I'm CUMMING!", 1, 1, 1, 1)
                        ">Cho's orgasm pushes you over the edge and you feel a familar twitch your wizard balls."
                        menu:
                            "Cum on her cheeks.":
                                "Finally, it's too much for you, and with one final thrust, your cock erupts all over Cho's ass."
                                m "Take it, you whore!"
                                #Genie cums.
                                cho_stupid"..."
                                cho_stupid"......"
                                "Your cum splatters withing the young girl's ass cheeks in thick, messy spurts."
                                cho_stupid"........."
                                "Your wrinkly old balls pull tight and you dump the last of your cum in a fat glob that lands on her asshole."
                                m "(Points) to Ravenclaw."
                                cho_stupid"........yessh."
                            "Cum in her ass.":
                                ">As you thrust forward you feel your head rub against the girls tight ring."
                                ">At the very brink you pull her cheeks open and press your cockhead against the tight entrance."
                                cho_stupid "...ahhh"
                                ">You push forward, fighting against the muscles."
                                cho_stupid "...ahhh....Ohhhh"
                                ">Finally, the ring gives way and your cock *pops* into her ass."
                                cho_stupid "...ahhh....ohhhh...Oomph!"
                                ">The pressure is too much and your cock explodes, dumping your cum safely in Cho's asshole."
                                #Genie cums - find sprite
                                m "Arg! You fucking cum dumpster!"
                                ">Load after load pumps into the girls tight, little hole until you feel her stomach bloat under you."
                                cho_stupid "Gack!"
                                cho_stupid "ooomph!"
                                $ renpy.play('sounds/pop02.mp3')
                                "Your cock pops out of the poor girls ass and you fall back in your chair, exhausted."
                                show screen blktone
                                #Cho chibi is standing in the middle of the room.
                                call cho_main("i don't feel So good...what happened?", 1, 1, 1, 1)
                                menu:
                                    "I filled your ass with cum.":
                                        m "You came so hard you passed out and I filled your ass with cum."
                                        cho _Shocked "..."
                                        cho _Shocked "......"
                                        cho _Shocked "........."
                                        cho_mouthfull "...."
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("i need to go!", 1, 1, 1, 1)
                                        jump chof2end
                                    "I don't know. That was weird.":
                                        m "I don't know. That was weird."
                                        m "But you got your points."
                                        call cho_main("THank you, Prof...", 1, 1, 1, 1)
                                        cho_mouthfull "Prof-"
                                        $ renpy.play('sounds/burp.mp3')
                                        call cho_main("i think i need To go seE moaning Myrtel!", 1, 1, 1, 1)
                                        $ renpy.play('sounds/run.mp3')
                                        jump chof2end
            "Let her.":
                m "As you wish, Miss Chang."
                ">You sit back in your chair and let Cho settle down against your lap."
                call cho_main("does this feel good?", 1, 1, 1, 1)
                ">Cho slowly drags her ass up and down over your cock."
                m "Fantastic, girl."
                ">Cho squeezes her ass around your dripping cock."
                ">The athletic, young quidditch star arches her back and bounces her ass up a down, teasing the tip of your cock."
                m "You tease!"
                ">You suddenly bring your palm down across her meaty cheek."
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}SLAP!{/size}"
                #Shake the screen
                hide screen white 
                cho_sexySurprise "Professor!"
                ">Cho bounces her ass up and down a few more times, before  settling down on your lap."
                call cho_main("{size=-4}(Oh my god...i can'T believe i'm rubbing my ass over an old wizard's cock.){/size}", 1, 1, 1, 1)
                call cho_main("{size=-4}(my ass is so slimy...the smell is so thick...){/size}", 1, 1, 1, 1)
                call cho_main("Professor Dumbledore, m-make sure you tell me before you-", 1, 1, 1, 1)
                ">You can already feel the beginning of your orgasm."
                ">You give the girls tight ass several slaps..."
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}SLAP!{/size}"
                #Shake the screen
                hide screen white 
                call cho_main("Professor Dumbledore, make sure you tell me before you-{w=.75}{nw}", 1, 1, 1, 1)
                $ renpy.play('sounds/slap_02.mp3')
                show screen white
                "{size=+4}SLAP!{/size}"
                #Shake the screen
                hide screen white 
                call cho_main("Professor Dumbledore, make sure you tell me bEFOre you-CUM!", 1, 1, 1, 1)
                call cho_main("{size=+4}(Oh blimey!){/size}", 1, 1, 1, 1)
                ">Cho slides back against your lap and begins to grind against you as you pump your cock between her cheeks."
                cho_arounsed "Professor..."
                ">You can see the top of your cock popping in and out of her ass cleavage, leaving a puddle of slime in the valley."
                ">After several more pumps you feel a familar pressure building..."
                menu:
                    "Cum.":
                        ">Finally, it's too much for you, and with one final thrust, your cock erupts between Cho's ass cheeks."
                        m "Cor' blimey, you bloody wanker!"
                        #Genie cums. - find chibi
                        cho_wideEyes "Oh my God...What is that?"
                        cho_wideEyesLookingBack "{size=+2}Are you cumming?{/size}"
                        ">Your cum splatters between the young girl's meaty cheeks in thick, messy spurts."
                        call cho_main("Oh, my God...", 1, 1, 1, 1)
                        ">You pump your cock a few more times and dump the last of your cum at the top of her ass."
                        call cho_main("...", 1, 1, 1, 1)
                        call cho_main("my ass feels so gross!", 1, 1, 1, 1)
                        call cho_main("it's so sticky.", 1, 1, 1, 1)
                        cho_sexy "It's so sticky. You owe me an extra 10 points!"
                        menu:
                            "Yes.":
                                m "Yeah, sure. 10 more points to Ravenclaw."
                                $ ravenclaw += 10
                                call cho_main("look at this mess!", 1, 1, 1, 1)
                                call cho_main("I'll never get this cleaned up...", 1, 1, 1, 1)
                                call cho_main("{sIze=-2}...Thank you, sir.{/size}", 1, 1, 1, 1)
                                ">Cho stands up. Cum drips down her firm ass, running in long, slimy rivulets down her thighs."
                                call cho_main("{size=-4}(He came so much...){/size}", 1, 1, 1, 1)
                                cho_happy "{size=-4}(I bet Hermione never makes him cum like this.){/size}"
                                ">Cho pulls her skirt back over her sticky ass and smoothes the fabric. Dark stains appear as the cum soaks through."
                                call cho_main("this should be okay.", 1, 1, 1, 1)
                                m "Yes, of course. Though, just to be safe you'd better try to avoid the prefects..."
                                jump chof2end
                            "Too bad.":
                                m "You're the one who made me cum."
                                call cho_main("!!!", 1, 1, 1, 1)
                                m "You should be more careful."
                                call cho_main("you can't be serious!", 1, 1, 1, 1)
                                call cho_main("your smelly cum is all over my arse! i smell like...liKe...like Hermione!", 1, 1, 1, 1)
                                m "Too bad."
                                call cho_main("you're nothing but a dirty old wizard!", 1, 1, 1, 1)
                                "Cho pulls her skirt down and storms off, leaving a trail of cum dripping to your door."
                                $ cho_mad +5
                                jump chof2end
                    "Warn Her.":
                        m "I'm going to cum!"
                        call cho_main("Really?", 1, 1, 1, 1)
                        ">Suddenly, you feel Cho move forward, and her hands quickly pull your cock down between her thighs before pushing back against you."
                        ">Your cock is wrapped tightly within her warm, muscular thighs, pressed tightly against her virgin pussy."
                        ">Cho rocks her hips back and forth, thrusting you through her slippery thighs."
                        cho_sexy "Cum, Professor!"
                        ">You can feel the heat and juice dripping from Cho's pussy, clinging to your cock."
                        ">Finally, it's too much for you and with a grunt you grab the girl's hips and cum violently."
                        m "Arg, you whor-{w=.75}{nw}"
                        cho_sexy "Shut up and cum, you nasty, old wizard!"
                        m "Arg, you whor-errrrrr!"
                        #Genie cums. - find chibi
                        ">Spurt after nasty spurt of your cum shoots between the young girls thight thighs, drenching your desk."
                        cho_sexy "So much cum!"
                        ">Completely spent, your fall back in your chair."
                        m "Good job Ms Chang."
                        call cho_main("thank you professor.", 1, 1, 1, 1)
                        ">Cho carefully straightens her skirt."
                        ">Then she leans back over your desk and runs her finger through your warm, dripping cum."
                        call cho_main("i think you made a bit of a mess...", 1, 1, 1, 1)
                        ">Then, bringing the slimy mess to her soft lips she sucks her finger clean."
                        call cho_main("Oops...", 1, 1, 1, 1)
                        jump chof2end

    label chof2end:
    #cho walking out
    $ renpy.play('sounds/door.mp3')
    hide screen cho_chang
    jump day_main_menu
    
    
    
label cho_favor_3:

        m "Miss Chang, do you know what a blowjob is?"
        call cho_main("?", 1, 1, 1, 1)
        call cho_main("you want me to put my mouth on your...", 1, 1, 1, 1)
        call cho_main("you want me to put my mouth on your...penis?", 1, 1, 1, 1)
        m "I just thought you'd like the chance to keep up with Miss Granger."
        call cho_main("you don't mean she's been-", 1, 1, 1, 1)
        menu:
            "-Absolutely-":
                m "I suppose Miss Granger is just more competitive than you."
                call cho_main("...", 1, 1, 1, 1)
                call cho_main("(i can't believe it.)", 1, 1, 1, 1)
                call cho_main("(What a...)", 1, 1, 1, 1)
                call cho_main("(what a...stupid whore.)", 1, 1, 1, 1)
                call cho_main("i can do it too!", 1, 1, 1, 1)
                call cho_main("i'll only charge you 60 points.", 1, 1, 1, 1)
                menu:
                    "-I'll give you 70 points-":
                        m "I'll give you 80."
                        call cho_main("Really?", 1, 1, 1, 1)
                        call cho_main("Really? 70 points?", 1, 1, 1, 1)
                        call cho_main("Okay.", 1, 1, 1, 1)
                        $ cho_mad -= 1
                        $ cho_points = 70
                        jump cho_favor_3_1
                        
                    "-Okay, 60-":
                        m "60, sounds good."
                        call cho_main("Okay.", 1, 1, 1, 1)
                        $ cho_points = 60
                        jump cho_favor_3_1
                    
                    "-Mrs. Granger only charges 55...-":
                        m "Ms. Granger only charges 55..."
                        call cho_main("55?...", 1, 1, 1, 1)
                        call cho_main("55?...why would she-", 1, 1, 1, 1)
                        call cho_main("I'll do it for 50!", 1, 1, 1, 1)
                        $ cho_points = 50
                        jump cho_favor_3_1
                        
            "-Of course not-":
                m "Don't be crazy. Of course, not."
                m "Ms. Granger has standards."
                call cho_main("...", 1, 1, 1, 1)
                m "She's just been earning a lot of points lately."
                call cho_main("She is?", 1, 1, 1, 1)
                m "Well, she is the school's top student..."
                call cho_main("I'll do it for 60 points.", 1, 1, 1, 1)

                menu:
                    "-I'll give you 70 points-":
                        m "I'll give you 80."
                        call cho_main("Really?", 1, 1, 1, 1)
                        call cho_main("Really? 70 points?", 1, 1, 1, 1)
                        call cho_main("Okay.", 1, 1, 1, 1)
                        $ cho_mad -= 1
                        $ cho_points = 70
                        jump cho_favor_3_1
                        
                    "-Okay, 60-":
                        m "60, sounds good."
                        call cho_main("Okay.", 1, 1, 1, 1)
                        $ cho_points = 60
                        jump cho_favor_3_1
                    
                    "-You'll get 40-":
                        m "I'll give you 40 points."
                        call cho_main("40! I get more than that for...well, the other things you make me do.", 1, 1, 1, 1)
                        call cho_main("I'll do it for 50.", 1, 1, 1, 1)
                        
                        menu:
                            "-Okay-":
                                m "Deal."
                                $ cho_points = 50
                                jump cho_favor_3_1
                            
                            "-No way-":
                                m "No way, girl. You're not worth more than 40."
                                call cho_main("Fine!", 1, 1, 1, 1)
                                $ cho_mad += 10
                                m "And try not to look so miserable about it."
                                $ cho_mad += 10
                                call cho_main("(Asshole.)", 1, 1, 1, 1)
                                call cho_main("(how am i even supposed to do this?)", 1, 1, 1, 1)
                                $ cho_points = 40
                                jump cho_favor_3_1

        m "I asume you're familar with the ancient Chinese art of 'SukiSuki'."
        call cho_main("What?", 1, 1, 1, 1)
        m "I want a blowjob."
        if cho_mad >= 6:
            jump cho_mad_blowjob
        call cho_main("Okay. but i'm only doing this tO help my House.", 1, 1, 1, 1)
        call cho_main("And i want [cho_points] points.", 1, 1, 1, 1)
        m "Yes, yes. Now get sucking."
        jump cho_favor_3_1

label cho_favor_3_1:

    call cho_main("Um...", 1, 1, 1, 1)
    call cho_main("um...What do I...", 1, 1, 1, 1)
    
    menu:
        "-Are you serious?-":
            m "Are you serious?"
            call cho_main("Of course i'm serious! i'm not a wHore like Hermione.", 1, 1, 1, 1)
            m "You just suck my cock in your mouth like candy."
            call cho_main("(LiKe cAndy? ew. now way that nasty, old...worm tastes like candy...)", 1, 1, 1, 1)
            call cho_main("([cho_points]! [cho_points]!)", 1, 1, 1, 1)
            "Cho drops awkwardly to her knees and opens her mouth, thrusting out her tongue."
            call cho_main("hoh's hhisss hHohessor?(How's this professor?)", 1, 1, 1, 1)
            "You feel your cock twitch under your robes at the sight of your student on her knees like a whore."
            m "Yes...that will do nicely."
            "You pull your throbbing cock out of your wizard's robes and stand over Cho."
            "The erotic sight causes pre-cum to ooze from the tip of your meaty wand."
            "Cho flinches as your cock bobs past her nose."
            call cho_main("ee! 'e 'arehul!(Be careful!)", 1, 1, 1, 1)
            "The head of your cock briefly touches the very tip of Cho's pointed nose, leaving a line of pre-cum stretching between you."
            call cho_main("huhhhh...", 1, 1, 1, 1)
            call cho_main("'uT ith at?(what is that?)", 1, 1, 1, 1)
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and guide your cock into her mouth."
            call cho_main("(eww. it tastes weird...)", 1, 1, 1, 1)
            m "Yessss....That's better."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
            call cho_main("Hmmm.", 1, 1, 1, 1)
            m "Hold on."
            "You slowly push your cock further into the young girls mouth."
            call cho_main("Hmmmm!", 1, 1, 1, 1)
            "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
            "Suddenly your cock bottoms out at the back of Cho's throat."
            call cho_main("*cough* *ack!*", 1, 1, 1, 1)
            "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
            call cho_main("Bleh!", 1, 1, 1, 1)
            call cho_main("Bleh!...", 1, 1, 1, 1)
            call cho_main("Oh my god!", 1, 1, 1, 1)
            call cho_main("I'm sorry, Professor!", 1, 1, 1, 1)
            
            menu:
                "-15 points-":
                    m "Fine! Just do it!"
                    call cho_main("Okay.", 1, 1, 1, 1)
                    "Cho leans forward and begins to quickly bobs her head over your cock."
                    "Her inexperienced mouth only manages to cover your bulbous head, but the constant stimulation quickly drives you over the edge."
                    m "You fucking whore!"
                    "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                    "Her cheeks begin to bulge with the heavy load."
                    "When it's over your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                    call cho_main("Hmmm!", 1, 1, 1, 1)
                    "Cho looks around for a place to spit your load."

                "-5 points-":
                    m "I'll give you 5 points."
                    call cho_main("...deal.", 1, 1, 1, 1)
                    "Cho leans forward and begins to quickly bobs her head over your cock."
                    "Her inexperienced mouth fumbles around your head, but the constant stimulation quickly drives you over the edge."
                    m "Yes, take it!"
                    "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                    "Her cheeks begin to bulge with the heavy load."
                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                    call cho_main("Hmmm!", 1, 1, 1, 1)
                    "Cho looks around for a place to spit your load."

                    menu:
                        "-Give her an empty wine glass-":
                            "The only object in your office is a wine glass left over from your nightly chats with Severis."
                            "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                            call cho_main("Blehgff...", 1, 1, 1, 1)
                            "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                            "In a few moments it's completely full."
                            call cho_main("Thank you, sir.", 1, 1, 1, 1)
                            "#gain item [Cum Goblet]"
                            m "Yes...well, [cho_points] to Ravenclaw."
                            jump cho_end_event

                        "-Make her swallow it.-":
                            m "Hey, I'm paying extra so you'd better swallow it."
                            call cho_main("fmMmhm mt?!(Swallow it?!)", 1, 1, 1, 1)
                            m "You want your points, don't you?"
                            call cho_main("(now way, you gross, old pervert!)", 1, 1, 1, 1)
                            call cho_main("(i'm gonna throw up!)", 1, 1, 1, 1)
                            "Cho's eyes are getting red, and her overstuffed cheeks flush."
                            $ renpy.play('sounds/gulp.mp3')
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("Blahg...", 1, 1, 1, 1)
                            call cho_main("Is...", 1, 1, 1, 1)
                            call cho_main("is...is that okay?", 1, 1, 1, 1)
                            m "Very good. [cho_points] to Ravenclaw."
                            call cho_main("THank you, Profe-", 1, 1, 1, 1)
                            $ renpy.play('sounds/burp.mp3')
                            call cho_main("...", 1, 1, 1, 1)
                            jump cho_end_event
                "-Fuck you!-":
                    m "(What a bitch!)"
                    m "You greedy whore!"
                    "You grab your cock and quickly stroke it."
                    "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                    call cho_main("W-what?...", 1, 1, 1, 1)
                    m "[cho_points] to Ravenclaw. Now, get out of my office."
                    call cho_main("but I can't go out like this!", 1, 1, 1, 1)
                    m "Get out."
                    call cho_main("...", 1, 1, 1, 1)
                    call cho_main("...Fine!", 1, 1, 1, 1)
                    $ cho_mad += 10
                    #Cho storms out.
                    m "Bitches..."
                    jump cho_end_event
            
        "-Put my cock in your mouth.-":
            m "You just put my cock in your mouth."
            call cho_main("i know that!", 1, 1, 1, 1)
            call cho_main("i kNow that! but after that...", 1, 1, 1, 1)
            m "You just suck on it and rub it with your tongue."
            call cho_main("(rub it with mY toNgue? ew. that sounds gross...)", 1, 1, 1, 1)
            call cho_main("([cho_points]! [cho_points]!)", 1, 1, 1, 1)
            "Cho drops awkwardly to her knees and opens her mouth, thrusting out her tongue."
            call cho_main("'oo cahn puh i' In 'ow...(you can put it in now...)", 1, 1, 1, 1)
            "You feel your cock thicken under your robes."
            m "Don't mind if I do..."
            "You pull your throbbing cock out of your robes and stand over Cho."
            "pre-cum oozes from the tip of your thick cock."
            "Cho flinches as your head bobs past her nose."
            call cho_main("ee! 'e 'arehul!(Be careful!)", 1, 1, 1, 1)
            "You slimy pre-cum touches the very tip of Cho's pointed nose, leaving a dangling line of slime stretching between you."
            call cho_main("huhhhh...", 1, 1, 1, 1)
            call cho_main("'uT ith at?(what is that?)", 1, 1, 1, 1)
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and guide your cock into her mouth."
            call cho_main("(eww. it tastes weird...)", 1, 1, 1, 1)
            m "Yessss....That's better."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
            call cho_main("Hmmm.", 1, 1, 1, 1)
            m "Hold on."
            "You slowly push your cock further into the young girls mouth."
            call cho_main("Hmmmm!", 1, 1, 1, 1)
            "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
            "Suddenly your cock bottoms out at the back of Cho's throat."
            call cho_main("*cough* *ack!*", 1, 1, 1, 1)
            "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
            call cho_main("Bleh!", 1, 1, 1, 1)
            call cho_main("Bleh!...", 1, 1, 1, 1)
            call cho_main("Oh my god!", 1, 1, 1, 1)
            call cho_main("I'm sorry, Professor!", 1, 1, 1, 1)
            
            menu:
                "-That's probably enough-":
                    m "Maybe, I went a little too far."
                    jump cho_end_event

                "-Keep going-":
                    m "You don't get your points if you didn't finish."
                    call cho_main("I'm sorry, Professor!", 1, 1, 1, 1)
                    m "That's quite all right, girl."
                    "You shove your cock back in her mouth, this time careful not to go too deep."
                    "Cho's tongue rolls around your cock with amateurish effort, getting in the way more than helping."
                    "To your surprise the thought of her inexperience brings you to the edge."
                    
                    menu:
                        "-Cum-":
                            "#Genie cums in Cho's mouth."
                            call cho_main("Hmmmmm!", 1, 1, 1, 1)
                            m "By the profits of Disney..."
                            call cho_main("Hmmmm!...", 1, 1, 1, 1)
                            call cho_main("hmmmm!...Mmmmm!", 1, 1, 1, 1)
                            "In a panic Cho tries to swallow your cum, but it catches at the back of her throat"
                            call cho_main("Blehg!", 1, 1, 1, 1)
                            "Your cum spews out of Cho's mouth and drips down her chin in a thick torrent of slime."
                            call cho_main("(oh god...that was so nasty..)", 1, 1, 1, 1)
                            call cho_main("Gross! You owe me extra for that!", 1, 1, 1, 1)

                            menu:
                                "-Fine 5 extra points-":
                                    m "Very well, Ms. Chang. [cho_points] to Ravenclaw."
                                    call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                    $ cho_points += 5
                                    jump cho_end_event

                                "-What? Absolutely not.-":
                                    m "What? Absolutely not."
                                    call cho_main("That's not fair!", 1, 1, 1, 1)
                                    m "Take it or leave it, Ms. Chong."
                                    call cho_main("MY name is Chang, you old jerk!", 1, 1, 1, 1)
                                    m "Do you want your points or not?"
                                    call cho_main("yes, please.", 1, 1, 1, 1)
                                    m "[cho_points] to Ravenclaw."
                                    jump cho_end_event
                        "-Warn Her-":
                            m "I'm going to cum!"
                            call cho_main("Hm!", 1, 1, 1, 1)
                            call cho_main("hm!...Blehrg!", 1, 1, 1, 1)
                            "Cho spits your slippery cock out of her mouth."
                            "You wait for her to finish you off, but instead she crosses her arms."
                            call cho_main("i want 15 more points.", 1, 1, 1, 1)
                            m "What?!"
                            call cho_main("you Just said i had to suck yOur cock. if you wanT to cum, i want 15 more points.", 1, 1, 1, 1)
                            
                            menu:
                                "-15 points-":
                                    m "Fine! Just do it!"
                                    call cho_main("Okay.", 1, 1, 1, 1)
                                    "Cho leans forward and begins to quickly bobs her head over your cock."
                                    "Her inexperienced mouth only manages to cover your bulbous head, but the constant stimulation quickly drives you over the edge."
                                    m "You fucking whore!"
                                    "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                                    "Her cheeks begin to bulge with the heavy load."
                                    "When it's over your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!", 1, 1, 1, 1)
                                    "Cho looks around for a place to spit your load."

                                "-5 points-":
                                    m "I'll give you 5 points."
                                    call cho_main("...deal.", 1, 1, 1, 1)
                                    "Cho leans forward and begins to quickly bobs her head over your cock."
                                    "Her inexperienced mouth fumbles around your head, but the constant stimulation quickly drives you over the edge."
                                    m "Yes, take it!"
                                    "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                                    "Her cheeks begin to bulge with the heavy load."
                                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!", 1, 1, 1, 1)
                                    "Cho looks around for a place to spit your load."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                            "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                            call cho_main("Blehgff...", 1, 1, 1, 1)
                                            "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "In a few moments it's completely full."
                                            call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                            "#gain item [Cum Goblet]"
                                            m "Yes...well, [cho_points] to Ravenclaw."
                                            jump cho_end_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it."
                                            call cho_main("fmMmhm mt?!(Swallow it?!)", 1, 1, 1, 1)
                                            m "You want your points, don't you?"
                                            call cho_main("(now way, you gross, old pervert!)", 1, 1, 1, 1)
                                            call cho_main("(i'm gonna throw up!)", 1, 1, 1, 1)
                                            "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...", 1, 1, 1, 1)
                                            call cho_main("Is...", 1, 1, 1, 1)
                                            call cho_main("is...is that okay?", 1, 1, 1, 1)
                                            m "Very good. [cho_points] to Ravenclaw."
                                            call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...", 1, 1, 1, 1)
                                            jump cho_end_event
                                "-Fuck you!-":
                                    m "(What a bitch!)"
                                    m "You greedy whore!"
                                    "You grab your cock and quickly stroke it."
                                    "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                                    call cho_main("W-what?...", 1, 1, 1, 1)
                                    m "[cho_points] to Ravenclaw. Now, get out of my office."
                                    call cho_main("but I can't go out like this!", 1, 1, 1, 1)
                                    m "Get out."
                                    call cho_main("...", 1, 1, 1, 1)
                                    call cho_main("...Fine!", 1, 1, 1, 1)
                                    $ cho_mad += 10
                                    #Cho storms out.
                                    m "Bitches..."
                                    jump cho_end_event
        "-Let's go slow-":
            m "Let's just go slow."
            call cho_main("THank you, Professor Dumbledore.", 1, 1, 1, 1)
            call cho_main("Do i just...you know, suck on it?", 1, 1, 1, 1)
            m "Yes. Think of it like candy."
            call cho_main("(LiKe candy? That might be okay...)", 1, 1, 1, 1)
            call cho_main("(just ignore the fact that that the wrinkly, old cock in my mouth belongs to a crusty, old wizard...)", 1, 1, 1, 1)
            call cho_main("([cho_points]! cho_points]!)", 1, 1, 1, 1)
            "Cho drops awkwardly to her knees and opens her mouth, thrusting out her tongue."
            call cho_main("I' I' 'ood 'o'esser?(is this good, professor?)", 1, 1, 1, 1)
            "You gently carress Cho's warm cheek with the back of your hand."
            call cho_main("(Wow...that was nice.)", 1, 1, 1, 1)
            $ cho_mad -= 1
            m "Yes, girl...that will do nicely."
            "You pull your throbbing cock out of your robes and stand over Cho."
            "The erotic sight causes pre-cum to ooze from the tip of your cock."
            "Cho's eyes flinch as your cock bobs over her face."
            "Her long Asian lashes blink fast as she fight the reflex to pull away."
            "A slimy stream of pre-cum drips down onto her face."
            call cho_main("ee! 'e 'arehul!(Be careful!)", 1, 1, 1, 1)
            "The tip of your cock briefly Cho's tongue, leaving a line of pre-cum stretching between you."
            call cho_main("huhhhh...", 1, 1, 1, 1)
            call cho_main("'uT ith at?(what is that?)", 1, 1, 1, 1)
            "Cho's mouth drips with with saliva."
            "You arch your cock toward her tongue and slowly rub your cock across it."
            call cho_main("(it tastes weird...)", 1, 1, 1, 1)
            m "Yessss....That's good."
            "You let you cock rest there for a moment. Basking in the warmth of Cho's breath and the soft, slipperiness of her tongue."
            call cho_main("Hmmm.", 1, 1, 1, 1)
            m "Shhh. It's okay, girl."
            "You slowly slide your cock into the young girls mouth."
            call cho_main("Hmmmm....", 1, 1, 1, 1)
            "The sensations are incredible, and soon your head is wrapped in warm, slippery wetness."
            "You leave it there for a moment."
            call cho_main("(This isn't bad...)", 1, 1, 1, 1)
            "You pull your cock back, out of Cho's mouth."
            call cho_main("Mmm.", 1, 1, 1, 1)
            call cho_main("Mmm....", 1, 1, 1, 1)
            "Cho opens her mouth wide, letting spit drip from her tongue."
            
            menu:
                "-That's probably enough-":
                    m "That's probably enough for now."
                    m "[cho_points] to Ravenclaw."
                    jump cho_end_event

                "-Keep going-":
                    m "We're almost done, girl."
                    call cho_main("(this is definitely worth [cho_points]...)", 1, 1, 1, 1)
                    "You gently guide your cock back in her mouth, careful not to go too deep."
                    "Cho's tongue rolls around your cock with sweet effort, slipping around your head."
                    "To your surprise her tongue finds your hole, and the assault brings you to the edge."
                    
                    menu:
                        "-Cum-":
                            #Genie cums in Cho's mouth.
                            call cho_main("Hmmmmm!", 1, 1, 1, 1)
                            m "G-good...girl..."
                            call cho_main("Hmmmm!...", 1, 1, 1, 1)
                            call cho_main("hmmmm!...Mmmmm!", 1, 1, 1, 1)
                            "In a panic Cho tries to swallow your cum, but it catches at the back of her throat"
                            call cho_main("Blehg!", 1, 1, 1, 1)
                            "Your cum spews out of Cho's mouth and drips down her chin in a thick torrent of slime."
                            call cho_main("(oh god...there was so much..)", 1, 1, 1, 1)
                            call cho_main("Gross!", 1, 1, 1, 1)
                            call cho_main("gross! warn me next time, okay?", 1, 1, 1, 1)
                            m "That was great. [cho_points] to Ravenclaw."
                            jump cho_end_event

                        "-Warn Her-":
                            m "I'm getting close!"
                            call cho_main("Hm?", 1, 1, 1, 1)
                            call cho_main("hm?...Blehrg!", 1, 1, 1, 1)
                            "Cho spits your slippery cock out of her mouth."
                            "You wait for her to finish you off, but instead she looks up at you with a smile."
                            call cho_main("if you give me 5 extRa points i'll eat it.", 1, 1, 1, 1)
                            m "You'll eat it?"
                            call cho_main("WeLl, yeah. I mean, it's gRoss, but I need the points...", 1, 1, 1, 1)
                            
                            menu:
                                "-15 points-":
                                    m "I'll give you 15 points."
                                    call cho_main("what? Really?", 1, 1, 1, 1)
                                    call cho_main("Okay.", 1, 1, 1, 1)
                                    "Cho dives forward and sucks your cock into her mouth."
                                    "Her tongue wraps around your bulbous head, and twists back and forth."
                                    call cho_main("(Mmm. It is like candy!)", 1, 1, 1, 1)
                                    m "By the power of GreySkull!"
                                    #Genie cums in Cho's mouth.
                                    "Your balls pull tight against your body and your cock begins to twitch."
                                    "Suddenly, you grab Cho's head and drive deeper into her soft lips, dumping your cum at the back of her mouth."
                                    "You feel her trying to swallow, but her cheeks begin to bulge with the heavy load."
                                    "When it's over your cock pops out of the smiling girl's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!", 1, 1, 1, 1)
                                    "Cho looks around for a place to spit your load."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                            "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                            call cho_main("Blehgff...", 1, 1, 1, 1)
                                            "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "In a few moments it's completely full."
                                            call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                            #gain item [Cum Goblet]
                                            m "Yes...well, [cho_points] to Ravenclaw."
                                            jump cho_end_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it all."
                                            call cho_main("fmMmhm mt?!(Swallow it all?!)", 1, 1, 1, 1)
                                            m "You want your points, don't you?"
                                            call cho_main("(i'm seriously going to throw up...)", 1, 1, 1, 1)
                                            call cho_main("Mm hhmm!", 1, 1, 1, 1)
                                            "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...", 1, 1, 1, 1)
                                            call cho_main("...", 1, 1, 1, 1)
                                            call cho_main("...All gone.", 1, 1, 1, 1)
                                            m "Very good. [cho_points] to Ravenclaw."
                                            call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...", 1, 1, 1, 1)
                                            jump cho_end_event
                                "-5 points-":
                                    m "Sure, I'll give you 5 points."
                                    call cho_main("You will?", 1, 1, 1, 1)
                                    "Cho leans forward and begins to quickly bobs her head over your cock."
                                    "Her inexperienced mouth works enthusiastically around your cock."
                                    "Before long, you can feel the cum churning in your enchanted nut sack."
                                    m "It's magically delicious!"
                                    #Genie cums in Cho's mouth.
                                    Cho_WideEyes"!..."
                                    Cho_WideEyes"(What?)"
                                    "Cho's cheeks begin to bulge with the heavy load, causing her to forget your mad outburst."
                                    "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                    call cho_main("Hmmm!", 1, 1, 1, 1)
                                    "Cho looks around for a place to spit your load."

                                    menu:
                                        "-Give her an empty wine glass-":
                                            "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                            "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                            call cho_main("Blehgff...", 1, 1, 1, 1)
                                            "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                            "In a few moments it's completely full."
                                            call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                            #gain item [Cum Goblet]
                                            m "Yes...well, [cho_points] to Ravenclaw."
                                            jump cho_end_event
                                        "-Make her swallow it.-":
                                            m "Hey, I'm paying extra so you'd better swallow it."
                                            call cho_main("fmMmhm mt?!(Swallow it?!)", 1, 1, 1, 1)
                                            m "You want your points, don't you?"
                                            call cho_main("(now way, you gross, old pervert!)", 1, 1, 1, 1)
                                            call cho_main("(i'm gonna throw up!)", 1, 1, 1, 1)
                                            "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                            $ renpy.play('sounds/gulp.mp3')
                                            $ renpy.play('sounds/gulp.mp3')
                                            call cho_main("Blahg...", 1, 1, 1, 1)
                                            call cho_main("Is...", 1, 1, 1, 1)
                                            call cho_main("is...is that okay?", 1, 1, 1, 1)
                                            m "Very good. [cho_points] to Ravenclaw."
                                            call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                            $ renpy.play('sounds/burp.mp3')
                                            call cho_main("...", 1, 1, 1, 1)
                                            jump cho_end_event
                                "-Fuck you!-":
                                    m "(I didn't know Chong was a Jewish name?!)"
                                    m "You greedy whore!"
                                    "You grab your cock and pound it like Anne Frank."
                                    m "After a few fast pumps your cock explodes."
                                    #Genie cums.
                                    "After a few fast pumps your cock explodes, coating Cho in your non-kosher cum."
                                    call cho_main("W-what?...", 1, 1, 1, 1)
                                    m "[cho_points] to Ravenclaw. Now, get out of my office."
                                    call cho_main("but I can't go out like this!", 1, 1, 1, 1)
                                    m "Get out."
                                    call cho_main("...", 1, 1, 1, 1)
                                    call cho_main("...Fine!", 1, 1, 1, 1)
                                    $ cho_mad += 10
                                    #Cho storms out.
                                    m "Bitches..."
                                    jump cho_end_event

label cho_favor_3_2:

        m "Ms. Chang, I'd like you to give me another blowjob."
        if cho_mad > 10:
            jump cho_mad_blowjob
            
        call cho_main("[cho_points] points.", 1, 1, 1, 1)
        m "Of course."
        "Cho drops to her knees and waits patiently."
        call cho_main("whenever you're ready.", 1, 1, 1, 1)
        m "Open your mouth."
        "Cho obeys, opening her mouth and thrusting out her tongue."
        call cho_main("On 'ea'y...(I'm ready...)", 1, 1, 1, 1)
        "Your cock throbs under your robes."
        m "This is why I got into teaching..."
        "You pull your throbbing cock out of your robes and stand over Cho."
        "Cho's mouth drips with with saliva."
        "You slap your cock against her tongue a few times before guiding it cock into her mouth."
        call cho_main("(what's he doing...)", 1, 1, 1, 1)
        m "Yessss....That's better."
        "You let you cock rest there for a moment. Basking in the warmth of Cho's mouth."
        call cho_main("Hmmm.", 1, 1, 1, 1)
        m "Hold on."
        "You slowly push your cock deeper into the young girls mouth."
        call cho_main("Hmmmm!", 1, 1, 1, 1)
        "The sensations are incredible, and your head is wrapped in warm, slippery wetness."
        "Suddenly your cock bottoms out at the back of Cho's throat."
        call cho_main("*cough* *ack!*", 1, 1, 1, 1)
        "You pull your cock back just as a thick stream of slime spills out of Cho's mouth."
        call cho_main("Bleh!", 1, 1, 1, 1)
        call cho_main("Bleh!...", 1, 1, 1, 1)
        call cho_main("Oh my god!", 1, 1, 1, 1)
        call cho_main("I'm sorry, Professor!", 1, 1, 1, 1)
        menu:
                    "-Be Nice-":
                        m "That's perfectly alright, Ms. Chang."
                        m "We'll just consider this part of your education."
                        call cho_main("Thank you, sir.", 1, 1, 1, 1)
                        "Cho gently wraps her mouth around your cock."
                        "Then, flattening her tongue, she takes your cock to the back of her mouth."
                        "You can feel the the entrance to her throat tickle the lips at the tip of your head."
                        m "Very good. Now just relax."
                        call cho_main("Mmhm.", 1, 1, 1, 1)
                        "Cho's tongue twitches under your cock as she tries her best to relax her throat."
                        m "Mmm. Good. Now, try to swallow."
                        call cho_main("*GuL* *Gul* *Glug*", 1, 1, 1, 1)
                        "Finally, you feel the head of your cock pop into her throat."
                        "The sensation of her tight flesh squeezing around your length is incredible."
                        call cho_main("...", 1, 1, 1, 1)
                        call cho_main("......", 1, 1, 1, 1)
                        call cho_main("..........", 1, 1, 1, 1)
                        call cho_main("*cough* *sputTer* ack! i almost had it.", 1, 1, 1, 1)
                        call cho_main("Let me try again.", 1, 1, 1, 1)
                        "Cho takes you back into her mouth."
                        "There's a determined look to her eye."
                        call cho_main("*Gul* *gulp* *Gluck*", 1, 1, 1, 1)
                        "Your cock pop's back into her throat."
                        "You can feel Cho struggling to hold herself down."
                        "Her throat is fighting around you, squeezing in violent pulses."
                        "The sensations are too much."

                        menu:

                            "-Cum-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Gluuuuuuh!*", 1, 1, 1, 1)
                                m "Yessss..."
                                call cho_main("*Glurck!*...", 1, 1, 1, 1)
                                call cho_main("*GlUrck!*...*gluglugulgh...*", 1, 1, 1, 1)
                                "Cho struggles to swallow as your cum pumps down her throat, but she gags, vomiting your slimy cum."
                                call cho_main("Blehg!", 1, 1, 1, 1)
                                "A torrent of slime spews out of Cho's mouth and drips down her chin splattering her uniform."
                                call cho_main("(oh god...that was so nasty..)", 1, 1, 1, 1)
                                call cho_main("gross! My uniform! You owe me extra, you jerk!", 1, 1, 1, 1)

                                menu:

                                    "-Fine 5 extra points-":
                                        m "Fine, Ms. Chang. [cho_points] to Ravenclaw."
                                        call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                        jump cho_end_event

                                    "-What? Absolutely not.-":
                                        m "Absolutely not."
                                        call cho_main("but! You're not fair!", 1, 1, 1, 1)
                                        m "Take it or leave it, Ms. Chong."
                                        call cho_main("MY name is Chang, you old jerk!", 1, 1, 1, 1)
                                        Cho_Sad"It's not even a hard name..."
                                        m "DO you want your points or not?"
                                        call cho_main("yes, please.", 1, 1, 1, 1)
                                        m "[cho_points] to Ravenclaw."
                                        jump cho_end_event

                            "-Warn Her-":
                                m "I'm going to cum!"
                                call cho_main("Hm!", 1, 1, 1, 1)
                                call cho_main("hm!...Blehrg!", 1, 1, 1, 1)
                                "Cho pulls back, dragging your slippery cock out of her throat."
                                "You catch your breath and wait patiently for her to finish you off."
                                "But instead she crosses her arms. and smirks cleverly."
                                call cho_main("15 points.", 1, 1, 1, 1)
                                m "What?!"
                                call cho_main("the original deal was just for a blowjob. if you wanT to cum, i want 15 more points.", 1, 1, 1, 1)

                                menu:

                                    "-15 points-":
                                        m "Whatever, girl! Just do it!"
                                        call cho_main("Okay.", 1, 1, 1, 1)
                                        "Cho leans forward and sucks your cock back into her mouth."
                                        "Unexpectedly, she drives forward, roughly shoving your cock back down her throat."
                                        "The sudden stimulation coupled with her slutty expression drives you over the edge."
                                        m "Take it your plebeian whore!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's throat, and your balls pull tight as you begin to dump your cum in her throat."
                                        "The poor girl tries to swallow, but she can't take it all. She pulls back collecting the rest in her mouth."
                                        "Her cheeks bulge with the heavy load."
                                        "When it's over your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!", 1, 1, 1, 1)
                                        "Cho looks around for a place to spit your load."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                                "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                                call cho_main("Blehgff...", 1, 1, 1, 1)
                                                "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "In a few moments it's completely full."
                                                call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [cho_points] to Ravenclaw."
                                                jump cho_end_event

                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it all."
                                                call cho_main("fMmmhm mt?(Swallow it?)", 1, 1, 1, 1)
                                                m "You want your points, don't you?"
                                                call cho_main("(OF course, I do.)", 1, 1, 1, 1)
                                                call cho_main("(just pretend it's pudding.)", 1, 1, 1, 1)
                                                "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                                call cho_main("(salty, slimy pudding....)", 1, 1, 1, 1)
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...", 1, 1, 1, 1)
                                                call cho_main("Was...", 1, 1, 1, 1)
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Was...that what you wanted?", 1, 1, 1, 1)
                                                m "Yes. [cho_points] to Ravenclaw."
                                                call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1)
                                                jump cho_end_event
                                    "-5 points-":
                                        m "I'll give you 5 points."
                                        call cho_main("...deal.", 1, 1, 1, 1)
                                        "Cho leans forward and begins to quickly bobs her head over your cock."
                                        "Her mouth fumbles quickly around your head."
                                        "Suddenly, she wraps her hands around your balls and tugs down gently."
                                        "The sensation is suprisingly pleasant."
                                        m "Yes, take it!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's mouth, dumping your cum in her mouth."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over your cock slips out of the Cho's lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!", 1, 1, 1, 1)
                                        "Cho looks around for a place to spit your load."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Professor Snape."
                                                "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                                call cho_main("Blehgff...", 1, 1, 1, 1)
                                                "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "In a few moments it's completely full."
                                                call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [cho_points] to Ravenclaw."
                                                jump cho_end_event
                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fmMmhm mt?!(Swallow it?!)", 1, 1, 1, 1)
                                                m "You want your points, don't you?"
                                                call cho_main("(now way, you gross, old pervert!)", 1, 1, 1, 1)
                                                call cho_main("(i'm gonna throw up!)", 1, 1, 1, 1)
                                                "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...", 1, 1, 1, 1)
                                                call cho_main("Is...", 1, 1, 1, 1)
                                                call cho_main("is...is that okay?", 1, 1, 1, 1)
                                                m "Very good. [cho_points] to Ravenclaw."
                                                call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1)
                                                jump cho_end_event
                                    "-Fuck you!-":
                                        m "(What a bitch!)"
                                        m "You greedy whore!"
                                        "You grab your cock and quickly stroke it."
                                        "After a few fast pumps your cock explodes."
                                        #Genie cums.
                                        "After a few fast pumps your cock explodes, coating Cho in your smelly cum."
                                        call cho_main("W-what?...", 1, 1, 1, 1)
                                        m "[cho_points] to Ravenclaw. Now, get out of my office."
                                        call cho_main("but I can't go out like this!", 1, 1, 1, 1)
                                        m "Get out."
                                        call cho_main("...", 1, 1, 1, 1)
                                        call cho_main("...Fine!", 1, 1, 1, 1)
                                        $ cho_mad += 10
                                        #Cho storms out.
                                        m "Bitches..."
                                        jump cho_end_event


                        jump cho_end_event

                    "-Be mean-":
                        m "You talk too much."
                        call cho_main("I'm sor-MMPH", 1, 1, 1, 1)
                        "You shove your cock back in her mouth, enjoying the sputtering tightness."
                        m "That's quite all right, girl."
                        "Cho's tongue thrashes violently around your cock effort, getting in the way more than helping."
                        "You hold Cho's head and forcefully push your cock toward the back of her throat."
                        call cho_main("mmmph! Mmmm!", 1, 1, 1, 1)
                        "To your surprise the frantic writhing of her tongue feels incredible."
                        "Your cock finally pops into her tight oesophagus, and you hold it there, enjoying the warm tightness."
                        m "That's the spot..."
                        "You feel Cho pushing you back, but you're close to cumming."
                        
                        menu:

                            "-Cum-":
                                #Genie cums in Cho's mouth.
                                call cho_main("*Glllll!* *Glp!*", 1, 1, 1, 1)
                                m "By the profits of Disney..."
                                call cho_main("*glp!* *Gack!*", 1, 1, 1, 1)
                                call cho_main("Hmmmm!", 1, 1, 1, 1)
                                "Cho's hands pull tight on your robes as she tries desperately to swallow your load, but your thick cum catches at the back of her throat"
                                call cho_main("Blehg!", 1, 1, 1, 1)
                                "Your cum spews out of Cho's mouth."
                                "The thick slime drips down her chin, soaking her uniform."
                                call cho_main("(oh god...he almost killed me...)", 1, 1, 1, 1)
                                call cho_main("You-you...asshole! You almost made Me drown! You better pay extra!", 1, 1, 1, 1)

                                menu:

                                    "-I was pretty rough. 10 extra points.-":
                                        m "Alright, Ms. Chang. [cho_points] to Ravenclaw."
                                        call cho_main("ThAt's all? i want more next time.", 1, 1, 1, 1)
                                        jump cho_end_event

                                    "-What? Absolutely not.-":
                                        m "What? Absolutely not."
                                        call cho_main("but you almost killed me!", 1, 1, 1, 1)
                                        call cho_main("I couldn't breathe!", 1, 1, 1, 1)
                                        m "Take it or leave it, Ms. Chong."
                                        call cho_main("MY name is Chang, you old jerk!", 1, 1, 1, 1)
                                        m "DO you want your points or not?"
                                        call cho_main("yes, please.", 1, 1, 1, 1)
                                        m "[cho_points] to Ravenclaw."
                                        jump cho_end_event

                            "-Warn Her-":
                                m "I'm going to cum!"
                                call cho_main("Hm!", 1, 1, 1, 1)
                                call cho_main("hm!...Blehrg!", 1, 1, 1, 1)
                                "Cho wrestles free of your grasp and spits your slippery cock out of her mouth."
                                "Your slimy cock slaps against her face, leaving a line of spit and cockslime across her nose."
                                call cho_main("i want 15 more points.", 1, 1, 1, 1)
                                m "What?!"
                                call cho_main("i only agreed to a blowjob. Cumming Is extra. i want 15 more points.", 1, 1, 1, 1)
                                
                                menu:

                                    "-15 points-":
                                        m "It's a deal, now finish it!"
                                        call cho_main("Okay.", 1, 1, 1, 1)
                                        "Cho leans forward and gives your cock a few quick strokes before sucking the head into her mouth."
                                        "She continues to pump your cock while her tongue swirls around your head."
                                        "Soon the constant stimulation drives you over the edge."
                                        m "You whore!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's mouth, dumping your cum across her tongue."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over your cock pops out of the poor girls lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!", 1, 1, 1, 1)
                                        "Cho looks around for a place to spit your load."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                                "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                                call cho_main("Blehgff...", 1, 1, 1, 1)
                                                "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "In a few moments it's completely full."
                                                call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [cho_points] to Ravenclaw."
                                                jump cho_end_event

                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fmMmhm mt?!(Swallow it?!)", 1, 1, 1, 1)
                                                m "You want your points, don't you?"
                                                call cho_main("(now way, you gross, old pervert!)", 1, 1, 1, 1)
                                                call cho_main("(i'm gonna throw up!)", 1, 1, 1, 1)
                                                "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...", 1, 1, 1, 1)
                                                call cho_main("Is...", 1, 1, 1, 1)
                                                call cho_main("is...is that okay?", 1, 1, 1, 1)
                                                m "Very good. [cho_points] to Ravenclaw."
                                                call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1)
                                                jump cho_end_event
                                    "-5 points-":
                                        m "I'll give you 5 points."
                                        call cho_main("...deal.", 1, 1, 1, 1)
                                        "Cho leans forward and begins to stroke your cock."
                                        "THen, pumping your cock with her fist, she leans forwards and plants a sloppy kiss on your head."
                                        "Her lips linger on your slit and she teases it with her tongue."
                                        "The intense stimulation finally pushes you over the edge."
                                        m "Yes, take it!"
                                        #Genie cums in Cho's mouth.
                                        "Your cock twitches in Cho's hand, and you begin to cum."
                                        "Cho purses her lips, letting your load fill her mouth."
                                        "Her cheeks begin to bulge with the heavy load."
                                        "When it's over your cock slips away from Cho's lips, leaving her struggling with the massive mouthful."
                                        call cho_main("Hmmm!", 1, 1, 1, 1)
                                        "Cho looks around for a place to spit your load."

                                        menu:

                                            "-Give her an empty wine glass-":
                                                "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                                "You pass Ms. Chang the glass just she loses a little stream of cum over her lips."
                                                call cho_main("Blehgff...", 1, 1, 1, 1)
                                                "You cum slowly pours out of the girls little mouth, oozing into the wine glass."
                                                "In a few moments it's completely full."
                                                call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                                #gain item [Cum Goblet]
                                                m "Yes...well, [cho_points] to Ravenclaw."
                                                jump cho_end_event
                                            "-Make her swallow it.-":
                                                m "Hey, I'm paying extra so you'd better swallow it."
                                                call cho_main("fMmmhm mt?(Swallow it?)", 1, 1, 1, 1)
                                                m "You want your points, don't you?"
                                                call cho_main("(Yes.)", 1, 1, 1, 1)
                                                call cho_main("(This is so gross...)", 1, 1, 1, 1)
                                                "Cho's eyes are getting red, and her overstuffed cheeks flush."
                                                $ renpy.play('sounds/gulp.mp3')
                                                $ renpy.play('sounds/gulp.mp3')
                                                call cho_main("Blahg...", 1, 1, 1, 1)
                                                call cho_main("Is...", 1, 1, 1, 1)
                                                call cho_main("is...is that okay?", 1, 1, 1, 1)
                                                m "Very good. [cho_points] to Ravenclaw."
                                                call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                                $ renpy.play('sounds/burp.mp3')
                                                call cho_main("...", 1, 1, 1, 1)
                                                jump cho_end_event
                                    "-Fuck you!-":
                                        m "(Just who's in charge here?!)"
                                        m "You greedy bitch!"
                                        "You grab your cock and force it into Cho's mouth."
                                        call cho_main("Hmm!*Gluck!*", 1, 1, 1, 1)
                                        "You drive cruelly deep, bursting into her throat, and being to pump hard."
                                        call cho_main("*gack* *gack* *gack* *Gack!*", 1, 1, 1, 1)
                                        "After a few fast pumps you feel your balls pull tight."
                                        m "You fucking whore!"
                                        "With a cruel smile, you pull your cock out of Cho's abused throat."
                                        #Genie cums.
                                        "Your cock explodes, coating the defiant girl in your smelly cum."
                                        call cho_main("...", 1, 1, 1, 1)
                                        m "[cho_points] to Ravenclaw. Now, get out of my office."
                                        call cho_main("......", 1, 1, 1, 1)
                                        m "Get out."
                                        call cho_main("...", 1, 1, 1, 1)
                                        call cho_main("...O-okay...", 1, 1, 1, 1)
                                        $ cho_mad += 10
                                        #Cho shuffles out.
                                        m "Bitches..."
                                        jump cho_end_event


label cho_favor_3_3:
    m "Suck my cock."
    
    if cho_mad > 10:
        jump cho_mad_blowjob

    call cho_main("Okay!", 1, 1, 1, 1)
    m "Don't you want some points or something?"
    call cho_main("What?", 1, 1, 1, 1)
    call cho_main("Oh, yeah.", 1, 1, 1, 1)
    call cho_main("That'll be [cho_points] points.", 1, 1, 1, 1)
    
    menu:

        "-Let's do this-":
            
            m "Get on your knees and open your mouth."
            "Cho slides down to her knees and opens her mouth, sticking out her tongue."
            "The sigh of your student on her knees with her young mouth open, her soft tongue drooling over her chin is enough to drive you wild."
            "Your cock strains against your robes, leaking pre-cum all over the inside."
            call cho_main("RIke 'ish?(Like this?)", 1, 1, 1, 1)
            m "Very good, Ms. Chang."
            call cho_main("Honk 'ou.(Thank you.)", 1, 1, 1, 1)
            "You pull your rigid cock out of your robes, letting it bob just centimetres from Cho's mouth."
            "You rock your hips back and forth, teasing her."
            call cho_main("...", 1, 1, 1, 1)
            call cho_main("......", 1, 1, 1, 1)
            call cho_main("......'ey! 'Ut it in!(hey! Put it in!)", 1, 1, 1, 1)
            m "Beg."
            call cho_main("What?", 1, 1, 1, 1)
            m "Beg me for it."
            call cho_main("OkAy. um... g-give it to me.", 1, 1, 1, 1)
            call cho_main("please. put your cock in my...mouth?", 1, 1, 1, 1)
            
            menu:
                
                "-You call that begging?-":
                    m "You call that begging?"
                    call cho_main("...", 1, 1, 1, 1)
                    m "Come on. You can do better than that."
                    call cho_main("please. let me suck your cock.", 1, 1, 1, 1)
                    "You lean forward, letting your slit touch her nose."
                    "Your pre-cum leaves a slimy strand tangling between you."
                    m "You can do better than that."
                    call cho_main("...", 1, 1, 1, 1)
                    call cho_main("......", 1, 1, 1, 1)
                    call cho_main(".........", 1, 1, 1, 1)
                    call cho_main("............please, fuck my mouth!", 1, 1, 1, 1)
                    call cho_main("treat my slutty little mouth like a pussy.", 1, 1, 1, 1)
                    call cho_main("please, please, please let me suck your perfect, old man cock!", 1, 1, 1, 1)
                    call cho_main("i'll lick your balls and slurp up every drop of your slimy stuff.", 1, 1, 1, 1)
                    call cho_main("please, let me be your little cock sucking whore.", 1, 1, 1, 1)
                    m "That was...good."
                    pass

                "-Very good.-":
                    m "Very good, girl."
                    call cho_main("Thank you.", 1, 1, 1, 1)
                    pass

            "You finally lean forward, letting Cho take your cock in her mouth."
            call cho_main("*chomp* *ommph* *Sluuurp*", 1, 1, 1, 1)
            "Cho begins to worship your throbbing flesh wand, bobbing her head savagely."
            "You can feel her uvula tickling your head as she pushes herself down your cock."
            call cho_main("*oomph* *Gluck*", 1, 1, 1, 1)
            "Your cock prods the back of her throat, and Cho's movements suddenly stop as she fights her gag reflex."
            call cho_main("*gack!* *Cough*", 1, 1, 1, 1)
            "A mouthful of slime and spit spills out around your cock."
            call cho_main("Oh my god...i almost had it that time.", 1, 1, 1, 1)
            "Cho's mouth drips with with saliva."
            "You slap your cock against her tongue a few times before guiding it back into her slippery fuck hole."
            call cho_main("(Cheeky old man...)", 1, 1, 1, 1)
            m "Practice makes perfect."
            "Cho sinks down, pushing your cock deeper into her mouth."
            call cho_main("Hmmm.", 1, 1, 1, 1)
            m "Hold on."
            "Cho ignores you. Pushing herself down. Your cock presses against her throat."
            call cho_main("hmmmm!*Gluck!*", 1, 1, 1, 1)
            "Suddenly, your cock pops into her throat."
            call cho_main("Mmmm!", 1, 1, 1, 1)
            "The sensations are incredible. Tightness squeezes all around your cock. It's almost too much."
            "Cho begins to bob quickly up and down, dragging your sensative head through her throat."
            call cho_main("*UgG* *Gug* *Gug!*", 1, 1, 1, 1)
            "The girl's efforts begin to pay off and you feel yourself getting close."
            
            menu:

                "-Cum-":
                    ##Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*", 1, 1, 1, 1)
                    $ renpy.play('sounds/gulp.mp3')
                    m "I AM THE CHOSEN ONE!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*", 1, 1, 1, 1)
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Hmmmm!", 1, 1, 1, 1)
                    "Cho takes a finger and gently pushes the last of your cum into her mouth, smacking her lips"
                    call cho_main("You know, Professor Dumbledore, sir, your cum's not that bad.", 1, 1, 1, 1)
                    call cho_main("well, for A geezer, I mean.", 1, 1, 1, 1)
                    m "Thank you?"
                    call cho_main("i'll take my points now.", 1, 1, 1, 1)
                    m "..."
                    m "...Yes, of course. [cho_points] to Ravenclaw."
                    jump cho_end_event


                "-Warn Her-":
                    m "I'm going to cum!"
                    call cho_main("Hm?", 1, 1, 1, 1)
                    call cho_main("hm!...Blehrg!", 1, 1, 1, 1)
                    "Cho pushes against your legs and drags your slimy cock out of her tight throat."
                    "Your nasty cock pops out of her lips and bops her nose, leaving a dangling line of spit and pre-cum connecting you."
                    call cho_main("do you want me to eat it?", 1, 1, 1, 1)
                    m "What?"
                    "Cho leans forward and presses her lips against your cock."
                    call cho_main("i'll swallow all of that tasty cum if you want.", 1, 1, 1, 1)
                    call cho_main("and i won't even charge extra...", 1, 1, 1, 1)
                                
                    menu:

                        "-Cum in her mouth.-":
                            m "I want to cum in your mouth."
                            call cho_main("Okay.", 1, 1, 1, 1)
                            "Cho leans forward and gives your cock a few quick strokes before sucking the head into her wet mouth."
                            "She continues to pump your cock while her tongue swirls around your head, playing with your slit."
                            "Soon the constant stimulation drives you over the edge."
                            m "You slut!"
                            #Genie cums in Cho's mouth.
                            "Your balls pull tight and your cum begins to pump into her mouth.."
                            call cho_main("Hmmmmmm....", 1, 1, 1, 1)
                            call cho_main("(Holy shit!)", 1, 1, 1, 1)
                            "Cho struggles to hold your load in her mouth."
                            "A small stream of cum is already trickling down her lips."
                            "Cho looks up into your eyes, pleadingly."
                            
                            menu:

                                "-Give her an empty wine glass-":
                                    "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                    "You pass Ms. Chang the glass just she loses another little stream of cum over her lips."
                                    call cho_main("Blehgff...", 1, 1, 1, 1)
                                    "You cum slowly pours out of the little witch's mouth, oozing into the wine glass."
                                    "In a few moments it's completely full."
                                    call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                    "Cho licks around the rim of the goblet cleaning it for you."
                                    #gain item [Cum Goblet]
                                    m "[cho_points] to Ravenclaw."
                                    jump cho_end_event

                                "-Make her swallow it.-":
                                    m "Swallow it all."
                                    call cho_main("fMmmhm mt?(Swallow it?)", 1, 1, 1, 1)
                                    m "Yes. Swallow it like a whore."
                                    call cho_main("(Yes, sir!)", 1, 1, 1, 1)
                                    call cho_main("(mmmm...it's so thick and slimy.)", 1, 1, 1, 1)
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Muh...", 1, 1, 1, 1)
                                    call cho_main("...", 1, 1, 1, 1)
                                    call cho_main("...Yummy.", 1, 1, 1, 1)
                                    m "You whore. [cho_points] to Ravenclaw."
                                    call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...", 1, 1, 1, 1)
                                    jump cho_end_event

                        "-Cum in her throat-":
                            m "I want to cum down your throat."
                            call cho_main("Yeah?", 1, 1, 1, 1)
                            "Cho leans forward swallowing your cock to the root."
                            "She rest for a moment, getting used to your size."
                            "Then, she begins to fuck her throat with your cock."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*", 1, 1, 1, 1)
                            m "By Gandalf's gay balls..."
                            call cho_main("*Hnnnng!*", 1, 1, 1, 1)
                            "Cho goes deep and it's suddenly too much."
                            "Your cock twitches and you being to cum."
                            #Genie cums in Cho's mouth.
                            call cho_main("!", 1, 1, 1, 1)
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...", 1, 1, 1, 1)
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(god, this old man...)", 1, 1, 1, 1)
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(So much...)", 1, 1, 1, 1)
                            "When it's over your cock slips away from Cho's lips, leaving her dazed."
                            call cho_main("THank you, Dumblesir...", 1, 1, 1, 1)
                            m "[cho_points] to Ravenclaw."
                            jump cho_end_event

                        "-Cum on her face.-":

                                m "I want to cum on your face."
                                call cho_main("you want to cover my stupid face in your cum?", 1, 1, 1, 1)
                                call cho_main("Okay.", 1, 1, 1, 1)
                                "Cho grabs your cock and forces it into her mouth."
                                call cho_main("Mmm!*Gluck!*", 1, 1, 1, 1)
                                "Cho pumps your cock in her mouth fiercely, ravaging her own throat."
                                call cho_main("*gack* *gack* *gack* *Gack!*", 1, 1, 1, 1)
                                "Finally, you feel your balls begin to tighten."
                                m "I'm almost-"
                                "Cho spits your cock out of her mouth and begins to stroke your cock."
                                call cho_main("CuM for me, Professor!", 1, 1, 1, 1)
                                ##Genie cums.
                                "Your cock explodes, coating the proud, young witch in your old wizard jizz."
                                call cho_main("Yes...", 1, 1, 1, 1)
                                call cho_main("Oh my god...", 1, 1, 1, 1)
                                call cho_main("that was amazing.", 1, 1, 1, 1)
                                m "[cho_points] to Ravenclaw."
                                call cho_main("...", 1, 1, 1, 1)
                                call cho_main("...i'm completely covereD, aren't I?", 1, 1, 1, 1)
                                m "Get out."
                                call cho_main("...", 1, 1, 1, 1)
                                call cho_main("okay, Professor.", 1, 1, 1, 1)
                                jump cho_end_event


        "-I want to fuck your face.-":
            m "I want to fuck your face."
            call cho_main("What?...", 1, 1, 1, 1)
            m "I want to use your mouth like a pussy."
            call cho_main("Professor!", 1, 1, 1, 1)
            call cho_main("PRofessor! that sounds so dirty.", 1, 1, 1, 1)
            m "Get on your knees and open your mouth."
            call cho_main("Well...", 1, 1, 1, 1)
            call cho_main("well...i am getting [chO_poinTs] house Points...", 1, 1, 1, 1)
            "Cho slides down to her knees and opens her mouth, sticking out her tongue."
            call cho_main("ah Oo 'ea'y?(are you Ready?)", 1, 1, 1, 1)
            "Your cock throbs against your heavy robes."
            m "That's good, girl."
            "You pull out your thick wizard dick and slap it threateningly against your palm."
            call cho_main("(So scary...)", 1, 1, 1, 1)
            "You carefully guide your cock into Cho's soft, wet mouth."
            call cho_main("Hmmm...", 1, 1, 1, 1)
            call cho_main("Hmmm...(it's so thick!)", 1, 1, 1, 1)
            "The young witch's mouth is warm and surprisingly accommodating."
            "You push your cock deeper into her mouth."
            "You stop when your feel your thick head rest against the entrance to her throat."
            call cho_main("*Hrk!*", 1, 1, 1, 1)
            call cho_main("*Hrk!* *Ack!*", 1, 1, 1, 1)
            call cho_main("*Hrk!* *Ack!* *Glg*...", 1, 1, 1, 1)
            m "By the sands!"
            "To your surprise Cho forces her head forward, choking herself on your wizard dick."
            "It takes you a moment to catch your breath."
            "Then you grab Cho's head in your hands and hold tightly."
            m "There's a good witch..."
            "You drag your cock back, out of the slippery tightness of Cho's throat, stopping at the entrance."
            "Then you thrust deep, driving your cock all the way to the hilt."
            call cho_main("AALG! HHHGGGGG!", 1, 1, 1, 1)
            call cho_main("AALG! HHhgGggG! (god he's choking me!)", 1, 1, 1, 1)
            "The young witch's throat feels too good, and you begin to fuck her throat in earnest."
            call cho_main("*glug* *GluG* *glg* *Gluck*", 1, 1, 1, 1)
            call cho_main("(Oh my god....)", 1, 1, 1, 1)
            call cho_main("*GlG* *Glg* *Glg*", 1, 1, 1, 1)
            call cho_main("(My throat...)", 1, 1, 1, 1)
            call cho_main("(My throat...feels so good...)", 1, 1, 1, 1)
            
            menu:

                "-Cum-":
                    #Genie cums in Cho's mouth.
                    call cho_main("*uugg!* *Glp!*", 1, 1, 1, 1)
                    $ renpy.play('sounds/gulp.mp3')
                    m "I AM THE CHOSEN ONE!"
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("*glp!* *Gack!*", 1, 1, 1, 1)
                    $ renpy.play('sounds/gulp.mp3')
                    call cho_main("Hmmmm!", 1, 1, 1, 1)
                    "Cho takes a finger and gently pushes the last of your cum into her mouth, smacking her lips"
                    call cho_main("You know, Professor Dumbledore, sir, your cum's not that bad.", 1, 1, 1, 1)
                    call cho_main("well, for A geezer, I mean.", 1, 1, 1, 1)
                    m "Thank you?"
                    call cho_main("i'll take my points now.", 1, 1, 1, 1)
                    m "..."
                    m "...Yes, of course. [cho_points] to Ravenclaw."
                    jump cho_end_event


                "-Warn Her-":
                    m "I'm going to cum!"
                    call cho_main("Hm?", 1, 1, 1, 1)
                    call cho_main("hm!...Blehrg!", 1, 1, 1, 1)
                    "Cho pushes against your legs and drags your slimy cock out of her tight throat."
                    "Your nasty cock pops out of her lips and bops her nose, leaving a dangling line of spit and pre-cum connecting you."
                    call cho_main("do you want me to eat it?", 1, 1, 1, 1)
                    m "What?"
                    "Cho leans forward and presses her lips against your cock."
                    call cho_main("i'll swallow all of that tasty cum if you want.", 1, 1, 1, 1)
                    call cho_main("and i won't even charge extra...", 1, 1, 1, 1)
                                
                    menu:

                        "-Cum in her mouth.-":
                            m "I want to cum in your mouth."
                            call cho_main("Okay.", 1, 1, 1, 1)
                            "Cho leans forward and gives your cock a few quick strokes before sucking the head into her wet mouth."
                            "She continues to pump your cock while her tongue swirls around your head, playing with your slit."
                            "Soon the constant stimulation drives you over the edge."
                            m "You slut!"
                            #Genie cums in Cho's mouth.
                            "Your balls pull tight and your cum begins to pump into her mouth.."
                            call cho_main("Hmmmmmm....", 1, 1, 1, 1)
                            call cho_main("(Holy shit!)", 1, 1, 1, 1)
                            "Cho struggles to hold your load in her mouth."
                            "A small stream of cum is already trickling down her lips."
                            "Cho looks up into your eyes, pleadingly."
                            
                            menu:

                                "-Give her an empty wine glass-":
                                    "The only object in your office is a wine glass left over from your nightly chats with Severis."
                                    "You pass Ms. Chang the glass just she loses another little stream of cum over her lips."
                                    call cho_main("Blehgff...", 1, 1, 1, 1)
                                    "You cum slowly pours out of the little witch's mouth, oozing into the wine glass."
                                    "In a few moments it's completely full."
                                    call cho_main("Thank you, sir.", 1, 1, 1, 1)
                                    "Cho licks around the rim of the goblet cleaning it for you."
                                    #gain item [Cum Goblet]
                                    m "[cho_points] to Ravenclaw."
                                    jump cho_end_event

                                "-Make her swallow it.-":
                                    m "Swallow it all."
                                    call cho_main("fMmmhm mt?(Swallow it?)", 1, 1, 1, 1)
                                    m "Yes. Swallow it like a whore."
                                    call cho_main("(Yes, sir!)", 1, 1, 1, 1)
                                    call cho_main("(mmmm...it's so thick and slimy.)", 1, 1, 1, 1)
                                    $ renpy.play('sounds/gulp.mp3')
                                    $ renpy.play('sounds/gulp.mp3')
                                    call cho_main("Muh...", 1, 1, 1, 1)
                                    call cho_main("...", 1, 1, 1, 1)
                                    call cho_main("...Yummy.", 1, 1, 1, 1)
                                    m "You whore. [cho_points] to Ravenclaw."
                                    call cho_main("THank you, Profe-", 1, 1, 1, 1)
                                    $ renpy.play('sounds/burp.mp3')
                                    call cho_main("...", 1, 1, 1, 1)
                                    jump cho_end_event

                        "-Cum in her throat-":
                            m "I want to cum down your throat."
                            call cho_main("Yeah?", 1, 1, 1, 1)
                            "Cho leans forward swallowing your cock to the root."
                            "She rest for a moment, getting used to your size."
                            "Then, she begins to fuck her throat with your cock."
                            call cho_main("*gluck* *gluck* *gluck* *Gluck*", 1, 1, 1, 1)
                            m "By Gandalf's gay balls..."
                            call cho_main("*Hnnnng!*", 1, 1, 1, 1)
                            "Cho goes deep and it's suddenly too much."
                            "Your cock twitches and you being to cum."
                            #Genie cums in Cho's mouth.
                            call cho_main("!", 1, 1, 1, 1)
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("!...", 1, 1, 1, 1)
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(god, this old man...)", 1, 1, 1, 1)
                            $ renpy.play('sounds/gulp.mp3')
                            call cho_main("(So much...)", 1, 1, 1, 1)
                            "When it's over your cock slips away from Cho's lips, leaving her dazed."
                            call cho_main("Thank", 1, 1, 1, 1)
                            call cho_main("Thank you", 1, 1, 1, 1)
                            call cho_main("THank you, Dumblesir...", 1, 1, 1, 1)
                            m "[cho_points] to Ravenclaw."
                            jump cho_end_event

                        "-Cum on her face.-":

                                m "I want to cum on your face."
                                call cho_main("you want to cover my stupid face in your cum?", 1, 1, 1, 1)
                                call cho_main("Okay.", 1, 1, 1, 1)
                                "Cho grabs your cock and forces it into her mouth."
                                call cho_main("Mmm!*Gluck!*", 1, 1, 1, 1)
                                "Cho pumps your cock in her mouth fiercely, ravaging her own throat."
                                call cho_main("*gack* *gack* *gack* *Gack!*", 1, 1, 1, 1)
                                "Finally, you feel your balls begin to tighten."
                                m "I'm almost-"
                                "Cho spits your cock out of her mouth and begins to stroke your cock."
                                call cho_main("CuM for me, Professor!", 1, 1, 1, 1)
                                ##Genie cums.
                                "Your cock explodes, coating the proud, young witch in your old wizard jizz."
                                call cho_main("Yes...", 1, 1, 1, 1)
                                call cho_main("Oh my god...", 1, 1, 1, 1)
                                call cho_main("that was amazing.", 1, 1, 1, 1)
                                m "[cho_points] to Ravenclaw."
                                call cho_main("...", 1, 1, 1, 1)
                                call cho_main("...i'm completely covereD, aren't I?", 1, 1, 1, 1)
                                m "Get out."
                                call cho_main("...", 1, 1, 1, 1)
                                call cho_main("okay, Professor.", 1, 1, 1, 1)
                                jump cho_end_event
            

        "-Ms. Chong, do you eat ass?-":
            m "Ms. Chong, do you eat ass?"
            call cho_main("are you asking or telling?", 1, 1, 1, 1)
            m "Get over here."
            "Cho playfully hops over to you, stopping just in front of your desk."
            call cho_main("Well?", 1, 1, 1, 1)
            m "(What's she doing?)"
            m "(Maybe she's trying to tell me something...)"

            menu:

                "-Treat her like a slut.-":
                    "Words are for Socialists and pussies."
                    "You suddenly grab Cho by the hair and drag her down to her knees."
                    call cho_main("!", 1, 1, 1, 1)
                    call cho_main("Profes-", 1, 1, 1, 1)
                    "Before she can say another word you pull your wizard robes open and jam your cock in her mouth."
                    call cho_main("(Yessss...)", 1, 1, 1, 1)
                    call cho_main("*Hrk!*", 1, 1, 1, 1)
                    call cho_main("*Hrk!* *Ack!*", 1, 1, 1, 1)
                    call cho_main("*Hrk!* *Ack!* *Glg*...", 1, 1, 1, 1)
                    "You can feel Cho's tongue thrashing violently around your head as she fights your hands."
                    call cho_main("*oomph* *Gluck*", 1, 1, 1, 1)
                    "Your cock prods the back of her throat, and Cho's movements suddenly stop as she focuses on fighting her gag reflex."
                    call cho_main("*gack!* *Cough*", 1, 1, 1, 1)
                    "A mouthful of slime and spit shoots out around your cock as she chokes around it."
                    call cho_main("(i'm going to die...)", 1, 1, 1, 1)
                    call cho_main("(You nasty, old man...)", 1, 1, 1, 1)
                    "Cho's chin drips with with tangled cords of slime."
                    "Your balls slap against her face as you pound her slippery fuck hole."
                    call cho_main("(I'm such a whore...)", 1, 1, 1, 1)
                    m "That's good, you fucking whore."
                    call cho_main("(Yes!)", 1, 1, 1, 1)
                    "Suddenly, you feel Cho's hands tightly gripping your ass, and you realize that you haven't had to hold her down."
                    "The crazed young witch desperately fucks her face against your cock."
                    "You cock feels amazing, but you have other plans."
                    "You grab Cho's hands and push her down."
                    $ renpy.play('sounds/pop.mp3')
                    "Your cock pops out of her throat, and she falls back on her haunches."
                    m "Get over here and lick my ass."
                    call cho_main("yes, Professor!", 1, 1, 1, 1)
                    "Cho crawls under your robes and leans back."
                    "Suddenly, you feel a slimy, wet sensation as Cho tongue probes your hairy asshole."
                    m "That's it."
                    m "That's it. That's it..."
                    "While Cho's tongue twists and tickles your asshole you pump your thick meat wand."
                    "Cho's hands push your own away and she begins to pound your cock while tongueing your ass."
                    m "By the Jews of Akabur..."
                    "Cho's hands work in concert with her tongue and it's not long before you find yourself on the edge."
                    #Genie Cums.
                    "Your cock explodes in Cho's soft, slippery hands as her tongue presses deep into your ass."
                    "Thick, heavy ropes of your cum shoot across the room, coating the floor at your feet."
                    call cho_main("Wow!", 1, 1, 1, 1)
                    call cho_main("wow! that was intense...", 1, 1, 1, 1)
                    m "Good work, Ms. Chong. [cho_points] to Ravenclaw..."
                    call cho_main("THank you, Professor Dumbledore.", 1, 1, 1, 1)
                    jump cho_end_event
                    
                    
label cho_mad_blowjob:
    call cho_main("i can't believe you, you old pervert.", 1, 1, 1, 1)
    call cho_main("Fine.", 1, 1, 1, 1)
    call cho_main("Fine. I'll do it.", 1, 1, 1, 1)
    "Cho drops to her knees and reaches into your robes grabbing your semi-hard cock."
    call cho_main("You're not even hard yet.", 1, 1, 1, 1)
    "Cho leans forward and gathering saliva in her mouth she spits a messy dollop across your cockhead."
    "The angry young witch begins to roughly pump your hardening cock."
    m "Take it easy."
    call cho_main("take it easy?", 1, 1, 1, 1)
    "Cho leans forward and sucks your cock into her mouth."
    "Her tongue assaults your sensitive head, writhing against your glans."
    "Then she begins to bob her head back and forth, sucking hard."
    m "That's good."
    "Cho spits your cock out and pumps it with fast, rough strokes."
    call cho_main("are you going to cum yet, you old jerk?", 1, 1, 1, 1)
    m "I'm almost there."
    "Cho takes your cock back into her mouth, sucking and bobbing."
    "Soon you reach your limit, but before you can cum Cho feels your shaft twitch and pulls back."
    call cho_main("Cumming so soon?", 1, 1, 1, 1)
    "Cho squeezes your cock uncomfortably hard and pumps your shaft so fast that you mind reals from the twin sensations of pleasure and pain."
    ##Genie cums
    "Suddenly, your cock throbs and just as you begin to cum Cho bends your twitching cock down, forcing you to cum on the floow at your feet."
    m "Ah! Cho, you Teenage Bitch!"
    "As the last few drops of your cum splatter against the floor of your office, Cho releases your abused cock."
    "She shakes the spit and pre-cum off her hand before glaring daggers at you."
    call cho_main("well? my house Points?", 1, 1, 1, 1)
    m "Fine. But you're only getting [points-5], you little bitch..."
    $ cho_mad += 5
    m "[points-5] to Ravenclaw."
    call cho_main("Jerk.", 1, 1, 1, 1)
    jump cho_end_event
