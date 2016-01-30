label __init_variables:
    $ heretic = 0
    $ heretic_01 = False
    $ heretic_02 = False
    $ heretic_03 = False
    $ heretic_busy = False
    $ hermione_desperate_done = False
    return

label heretic:
    hide screen hermione_main
    with d3
    m "{size=-4}(Is she really going to let me do this?){/size}"
    menu:
        "\"(I've got her well trained.  Why not?)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    m "Alright then..."
    if heretic == 0: #First time this event taking place.
        m "Miss Granger, do you know what a dildo is?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/c.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "I... I'm familiar with the concept."
        hide screen h_head
        m "Have you used one before?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/q.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Excuse me?"
        hide screen h_head
        m "There's no need to be embarrassed, girl, just tell me if you've ever used a dildo before."
        if whoring >=16:
            $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "...yes I have."
            hide screen h_head
            g9 "Excellent, well you'll be using one today."
        else:
            $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "...Of course not professor."
            hide screen h_head
            m "Well you'll be using one today."
    else:
        if whoring >=18:
            $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "Well... if it's for the good of Gryffindor."
            hide screen h_head
        else:
            $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "This again?"
            hide screen h_head
            #### CONTINUE ####

### FIRST QUEST DAY ###
    if whoring <= 14:
        jump too_much
    else:
        $ h_body = "01_hp/29_cust_events/heretic/resources/s.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "You want to watch me masturbate?"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Er...I have class to get to."
        hide screen h_head
        g9 "Perfect, because you'll need this."
        $ h_body = "01_hp/29_cust_events/heretic/resources/s.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Oh my god, it's as big as my forearm!"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Do you expect me to use this for you?"
        hide screen h_head
        m "In a way. Put it in, girl."
        $ h_body = "01_hp/29_cust_events/heretic/resources/c.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "How many house points is this worth, sir?"
        hide screen h_head
        m "I'll give you 50."
        $ h_body = "01_hp/29_cust_events/heretic/resources/q.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Only 50? What if I hurt myself?"
        hide screen h_head
        m "It's magically enchanted, there's no risk of injury."
        show screen h_head
        her "Really? Where did you get this?"
        hide screen h_head
        m "Do you plan on getting one for yourself?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/c.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "If I told you yes...{p}Would you give me more house points?"
        hide screen h_head
        g4 "Miss Granger, would you rather get to class, or sit here and haggle?"
        show screen h_head
        her "Fine."
        hide screen h_head
        ">Hermione slips the dildo under her skirt, struggling to insert the vibrator into herself."
        $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "I think it's too big, sir"
        hide screen h_head
        m "Nonsense, keep trying."
        ">Changing her strategy, Hermione drops to her knees and rests the base of the cock against the floor. She starts rocking back and forth to wiggle the dick deeper inside her."
        g9 "Lift your skirt, bitch, I want to watch."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/29_cust_events/heretic/resources/p_jt.png"
        $ h_xpos=140
        $ h_ypos=0
        $ only_upper = True
        $ badges = False
        show screen hermione_main
        show screen blktone
        show screen ctc
        pause
        ">Complying, Hermione flips her skirt up to reveal her engorged snatch."
        $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Oh my god... mmmmhh"
        hide screen h_head
        g9 "Enjoying yourself?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Of course not. This is all for the... ahn... glory of Gryffindor."
        hide screen h_head
        g4 "Looks like you're enjoying yourself now, slut."
        $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Please sir, don't call me a slut. It's so...{p}{size=-2}degrading.{/size}"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "{size=-4}(I am a slut.){/size}"
        her "{size=-4}(Look what I've become!!!){/size}"
        her "{size=-5}(Masturbating in front of Professor Dumbledore for house points.){/size}"
        her "{size=-4}(I'm nothing but a common whore.){/size}"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "{size=-4}(I wish it didn't feel so good.){/size}"
        hide screen h_head
        m "I'm sure. You better hurry up if you want to get to class."
        hide screen h_head
        ">With that, Hermione's motions become frantic. Bouncing up and down, tears of frustration well up in the corners of her eyes."
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "I can't... it won't go any deeper."
        hide screen h_head
        m "Allow me."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/29_cust_events/heretic/resources/p_di.png"
        $ h_xpos=140
        $ h_ypos=0
        show screen hermione_main
        show screen blktone
        show screen ctc
        pause
        ">With a few idle movements of your one free hand, you forces the dildo to shoot up inside of Hermione."
        $ h_body = "01_hp/29_cust_events/heretic/resources/a.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "AAAAHHH!"
        hide screen h_head
        ">Hermione falls sideways onto the floor as a puddle of her fluids pools around her."
        m "Good girl. Now off you go."
        $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Can't I stay here for a bit?"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/a.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "{size=-4}(So you can cum on my...){/size}"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/s.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "{size=-4}(OH GOD! Get it together Hermione!){/size}"
        hide screen h_head
        g9 "So you can keep fucking yourself while I watch?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/c.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Of course not. I just need a moment."
        hide screen h_head
        m  "What are you doing?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/n.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Taking this dildo out, sir."
        hide screen h_head
        menu:
            "\"(That gives me an idea.)\"":
                if whoring >= 16:
                    g4 "No, you leave that where it is."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/c.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "But sir, I have class."
                    hide screen h_head
                    g9 "I know."
                    show screen h_head
                    her "You mean..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/s.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "SIR!"
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "You expect me to walk around all day with this...{p}inside of me?"
                    hide screen h_head
                    m "That's exactly what I expect."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "..."
                    hide screen h_head
                    g9 "You had better hurry. Wouldn't want to be late for class."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/29_cust_events/heretic/resources/p_us.png"
                    $ h_xpos=140
                    $ h_ypos=0
                    show screen hermione_main
                    show screen blktone
                    show screen ctc
                    pause
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Sir, it's sticking out of the bottom of my skirt!"
                    hide screen h_head
                    g9 "I know. Off you go."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "{size=-4}(Oh god... I can barely walk... What if somebody notices?){/size}"
                    hide screen h_head
                    $ heretic_busy = True
                else:
                    jump too_much
            "\"(That's enough.)\"":
                m "Alright, you can go. Fifty points to Gryffindor."
                $ gryffindor +=50
                $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                $ h_xpos=390
                $ h_ypos=340
                show screen h_head
                her "Uh, sir... Could you help me?"
                hide screen h_head
                hide screen hermione_main
                with d3
                $ h_body = "01_hp/29_cust_events/heretic/resources/p_jt.png"
                $ h_xpos=140
                $ h_ypos=0
                show screen hermione_main
                show screen blktone
                show screen ctc
                pause
                hide screen h_head
                ">You wave your hand. The dildo erupts out of Hermione, who begins spasming in ecstacy again."
                m "Now say thank you."
                $ h_body = "01_hp/29_cust_events/heretic/resources/a.png"
                $ h_xpos=390
                $ h_ypos=340
                show screen h_head
                her "Th...thaan...thank you...siiir."
                hide screen h_head
                m "Hurry along Miss Granger, I haven't got all day."
                ">Hermione slowly rises off the floor and lurches out of the room on shaky legs."
                if whoring <= 16:
                    $ whoring +=1
        hide screen bld1
        hide screen hermione_main
        hide screen blktone
        hide screen hermione_02
        hide screen ctc
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=610 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01_f
        pause 2
        hide screen hermione_walk_01_f
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        with Dissolve(.3)
        call music_block
        $ hermione_takes_classes = True
        $ only_upper = False
        $ badges = True
        jump day_main_menu
        #### END THE SCENE ####
### First Quest Night ###
label heretic_night:
    $ walk_xpos=520
    $ walk_xpos2=400
    $ hermione_speed = 02.0
    $ renpy.play('sounds/door.mp3')
    show screen hermione_walk_01
    with d4
    pause 1.7
    $ hermione_chibi_xpos = 400
    show screen hermione_02
    pause 0.5
    show screen bld1
    with Dissolve(.3)
    $ exposure = renpy.random.randint(1, 10)
    if exposure <= 3: #Caught By Harry
        m "Good evening Miss Granger."
        with d3
        $ h_body = "01_hp/29_cust_events/heretic/resources/p_nd.png"
        $ h_xpos=140
        $ h_ypos=0
        $ only_upper = True
        $ badges = False
        show screen hermione_main
        show screen blktone
        show screen ctc
        pause
        $ h_body = "01_hp/29_cust_events/heretic/resources/n.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Hello sir."
        hide screen h_head
        m "So I see you didn't live up to you end of the bargain."
        $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Sir! I would never cheat!"
        her "Especially when Gryffindor's honor is at stake!"
        hide screen h_head
        g4 "Then where is the dildo, girl?!"
        $ h_body = "01_hp/29_cust_events/heretic/resources/n.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "It's... err..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/29_cust_events/heretic/resources/p_dd.png"
        $ h_xpos=140
        $ h_ypos=0
        show screen hermione_main
        show screen blktone
        show screen ctc
        pause
        hide screen h_head
        ">Hermione pulls up her skirt to reveal the dildo lodged deeply in her cunt."
        g4 "Would you care to explain yourself, or are you ready to admit what a whore you are?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "I had no choice, sir."
        hide screen h_head
        m "You could have taken it out."
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        $ only_upper = False
        $ badges = True
        show screen h_head
        her "Err..."
        hide screen h_head
        m "Well, did you enjoy yourself today Miss Granger?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "It was..."
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "It was terrible sir."
        hide screen h_head
        m "What was so terrible about it, girl?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "...I can't"
        hide screen h_head
        m "Do you want your points or not?"
        show screen h_head
        her "Please sir, it was mortifying."
        hide screen h_head
        m "I'm waiting."
        show screen h_head
        her "..."
        her "I... As soon as I left I ran into Harry. He could...{p}I mean he didn't say anything{p}but I saw him staring at it."
        hide screen h_head
        m "Well, what did you do?"
        show screen h_head
        her "I... I knew I couldn't leave it dangling out...{p}and... I mean he already saw it..."
        hide screen h_head
        g4 "Spit it out girl!"
        $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Harry fucked me with the dildo!"
        hide screen h_head
        g9 "Oh you filthy whore."
        show screen h_head
        her "I needed help,{p}and we've been through so much together..."
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "He must think I'm such a whore."
        hide screen h_head
        g9 "Did you tell him why you had a massive magical cock sticking out of you?"
        show screen h_head
        her "No. It's better he thinks I'm a slut.{p}I can't imagine him knowing I'm a traitor.{p}to him, or the cause!"
        hide screen h_head
        g9 "Did you enjoy yourself?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "How could you ask me that sir? I was humiliated."
        hide screen h_head
        m "You didn't answer the question."
        $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "..."
        hide screen h_head
        m "Well?"
        show screen h_head
        her "Can I go now sir?"
        hide screen h_head
        g4 "Once you answer the question."
        show screen h_head
        her "...It wasn't terrible..."
        hide screen h_head
        g9 "Did you cum?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "You said I could go, sir."
        hide screen h_head
        menu:
            "\"Press Her.\"":
                g4 "You can go when I tell you to leave. Tell me Miss Granger, did you cum when your friend played with your pussy?"
                if whoring <= 17:
                    $ h_body = "01_hp/29_cust_events/heretic/resources/f.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Sir, you said I could leave! I don't mind being subjected to your sick perversions if order to help out my house, but I draw the line here!"
                    hide screen h_head
                    g4 "Miss Granger..."
                    show screen h_head
                    her "I'm not finished! You forced me to humiliate myself, and what do I have to show for it?"
                    hide screen h_head
                    m "...Fifty point to gryffindor."
                    $ gryffindor +=50
                    $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Good night, Sir."
                    $ mad += 10
                    jump q7y8f5
                else:
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...yes."
                    hide screen h_head
                    g4 "Speak up, girl."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "YES!"
                    hide screen h_head
                    m "Details, girl."
                    show screen h_head
                    her "He... he pushed me up against a wall.{p}Then he ground the dildo into my pussy."
                    hide screen h_head
                    show screen genie_jerking_off
                    ">You start stroking your cock under the desk."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/n.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "He... he said he always thought I was a slut.{p}and then kissed me."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/a.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Oh god, I can still feel his tongue down my throat..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "He forced the dildo all the way in with the his palm.{p}I came so much I stained his shirt sleeve."
                    hide screen h_head
                    g9 "Then what?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "..."
                    hide screen h_head
                    g4 "Come on, girl, out with it."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I sucked him off."
                    hide screen h_head
                    g9 "Oh you little bitch."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I felt the massive bulge when we were pressed up{p}against the wall, and he had helped me... you know..."
                    hide screen h_head
                    g9 "Cum your brains out?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Yes... I... Can I be honest with you sir?"
                    hide screen h_head
                    m "I hope so."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/v.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I wanted so desperately to taste it."
                    hide screen h_head
                    g11 "YES!"
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen genie_jerking_sperm
                    ">You finally cum from the excitement of knowing what she's done."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/p.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Did you enjoy that, sir?"
                    hide screen genie_jerking_sperm
                    show screen genie
                    hide screen genie_jerking_off
                    hide screen h_head
                    g9 "Absolutely."
                    show screen h_head
                    her "Good. Can I get paid now?"
                    hide screen h_head
                    m "Fifty points to gryffindor."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/pr.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "And sir..."
                    her "You know I only said those things{p}because you wanted me to.{p}right?"
                    hide screen h_head
                    m "Whatever you say, Miss Granger."
                    show screen h_head
                    her "I'm not that kind of girl, sir."
                    her "Harry didn't really use your dildo on me...{p}I went to the bathroom and did it myself."
                    hide screen h_head
                    g9 "Whatever the case, it was a wonderful story."
                    jump q7y8f5
            "\"Let her leave.\"":
                label q7y8f5:
                m "Well done Miss Granger."
                $ h_body = "01_hp/29_cust_events/heretic/resources/p.png"
                $ h_xpos=390
                $ h_ypos=340
                show screen h_head
                her "Thank you sir."
                hide screen h_head
                m "Fifty points to Gryffindor."
                $ gryffindor +=50
                show screen h_head
                her "Thank you sir,{p}now if you'll excuse me I need to lay down."
                hide screen h_head
                if whoring >= 18:
                    m "Where are you going?"
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/q.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Sir?"
                    hide screen h_head
                    g4 "The dildo, girl."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Oh, right. Err... You see sir, it's stuck."
                    hide screen h_head
                    m "Well I can help with..."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "No need, sir."
                    hide screen h_head
                    m "Miss Granger, I can't let you leave with my dildo."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/q.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...Please?"
                    hide screen h_head
                    m "Please what?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...Please may I keep the dildo, sir?"
                    hide screen h_head
                    g9 "Hm... Very well slut, as long as you walk back to Gryffindor tower with it inside you."
                    show screen h_head
                    her "I was plan..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Err... If you say so, sir."
                    hide screen h_head
                hide screen bld1
                hide screen hermione_main
                hide screen blktone
                hide screen hermione_02
                hide screen ctc
                with d3
                $ walk_xpos=400
                $ walk_xpos2=610
                $ hermione_speed = 02.0
                show screen hermione_walk_01_f
                pause 2
                hide screen hermione_walk_01_f
                $ renpy.play('sounds/door.mp3')
                with Dissolve(.3)
                call music_block
                $ heretic_busy = False
                $ hermione_sleeping = True
                jump night_main_menu
    elif exposure >= 4 and exposure <=9: #Accidental Exposure
        m "Hello, Miss Granger."
        $ h_body = "01_hp/29_cust_events/heretic/resources/pe.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Hello sir."
        her "..."
        hide screen h_head
        m "Well?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/pr.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "There's nothing to talk about."
        hide screen h_head
        m "So spending an entire day with a dildo inside you is a normal day for you?"
        show screen h_head
        her "What am I supposed to say?"
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her"I went to class,{p}I ate with friends,{p}I tried to hide the giant rod between my legs."
        hide screen h_head
        m "Welcome to my world."
        $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Are you making fun of me, sir?"
        hide screen h_head
        m "Not at the moment. Tell me, girl, did anybody notice?"
        if whoring <=15:
            $ h_body = "01_hp/29_cust_events/heretic/resources/d.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "Of course not. As soon as I left I cast a disillusionment charm on it."
            hide screen h_head
            m "What?"
            show screen h_head
            her "Well, they can't see something that's invisible, sir."
        else:
            $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "..."
            hide screen h_head
            m "So, yes. Who and when."
            $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "...I don't know his name, sir.{p}He was a first year who was tying his shoe while I walked by."
            her "He...well he saw it."
            hide screen h_head
            m "What did this boy do?"
            $ h_body = "01_hp/29_cust_events/heretic/resources/pe.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "He ran off. I think he was embarrassed."
            hide screen h_head
            m "Is that all?"
            $ h_body = "01_hp/29_cust_events/heretic/resources/pr.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "Yes, sir."
            hide screen h_head
            $ h_body = "01_hp/29_cust_events/heretic/resources/d.png"
            $ h_xpos=390
            $ h_ypos=340
            show screen h_head
            her "I can be quite subtle if I want to be."
            hide screen h_head
            m "Not to mention dull."
        m "Did anything interesting happen to you today?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/h.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "I did...Err...No, not really."
        $ only_upper = False
        $ badges = True
        hide screen h_head
        menu:
            "\"Press Her.\"":
                m "Come now, girl,you want to earn these points, right?"
                if whoring <= 17:
                    $ h_body = "01_hp/29_cust_events/heretic/resources/p.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I got a perfect score on a herbology exam today."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Which, isn't that surprising, but I was a bit...distracted."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Not that you would care about my test scores..."
                    hide screen h_head
                    m "{size=-4}*Snoring*{/size}"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/s.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Professor!"
                    hide screen h_head
                    m "Hm? Wha? Right, uh... 50 points to Gryffindor."
                    $ gryffindor +=50
                    $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Good night, sir."
                    hide screen h_head
                    hide screen bld1
                    hide screen hermione_main
                    hide screen blktone
                    hide screen hermione_02
                    hide screen ctc
                    with d3
                    $ walk_xpos=400
                    $ walk_xpos2=610
                    $ hermione_speed = 02.0
                    show screen hermione_walk_01_f
                    pause 2
                    hide screen hermione_walk_01_f
                    $ renpy.play('sounds/door.mp3')
                    with Dissolve(.3)
                    call music_block
                    $ heretic_busy = False
                    $ hermione_sleeping = True
                    jump night_main_menu
                else:
                    $ h_body = "01_hp/29_cust_events/heretic/resources/i.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...Well...{p}I have divination today, and it's all so dull.{p}Not to mention Professor Trelawney is a fraud."
                    hide screen h_head
                    m "Get on with it, girl!"
                    show screen h_head
                    her "..."
                    her "As I was saying, I was in divination class."
                    her "Professor Trelawney was droning on about something or other."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "You have to understand, that room is very comfortable, sir.{p}It's only lit by candle light, the room is heavily incenced..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "And I was lounging among all those very soft pillows."
                    hide screen h_head
                    m "You didn't."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/p.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I think I did, sir."
                    hide screen h_head
                    m "Hermione Granger masturbated in class?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Only a bit."
                    her "It was quite easy, I only really had to rock back and forth.{p}The toy did the rest."
                    hide screen h_head
                    m "Miss Granger, you certainly have come a long way."
                    show screen h_head
                    her "I came quite a bit there as well."
                    hide screen h_head
                    m "You delightful little slut, did you enjoy yourself?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/na.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Sir, you shouldn't call your students sluts..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/sl.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I did. More than I expected actually...{p}Especially since I was sitting between Ron and Harry."
                    hide screen h_head
                    m "Did they notice?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/n.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I have no idea."
                    hide screen h_head
                    m "You hope they did, don't you?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/e.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Of course not!{p}Fantasy is one thing, but if they actually noticed I would be mortified."
                    hide screen h_head
                    jump q7y8f5
            "\"Let her leave\"":
                jump q7y8f5
    else: #Caught By Draco
        m "Good evening, Miss Granger."
        with d3
        $ h_body = "01_hp/29_cust_events/heretic/resources/p_m.png"
        $ h_xpos=140
        $ h_ypos=0
        show screen hermione_main
        show screen blktone
        show screen ctc
        pause
        m "My goodness, interesting day?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/mash.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Can I just get paid, sir?"
        hide screen h_head
        m "You're going to have to do better than that."
        show screen h_head
        her "...Draco Malfoy."
        hide screen h_head
        m "What about him?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/ma.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "He's a Slytherin cretin, a racist, he's..."
        her "He's a monster, sir."
        hide screen h_head
        m "What makes you say this, girl?"
        $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "..."
        hide screen h_head
        $ h_body = "01_hp/29_cust_events/heretic/resources/mash.png"
        $ h_xpos=390
        $ h_ypos=340
        show screen h_head
        her "Please... I just want to be done with this, sir..."
        hide screen h_head
        menu:
            "\"Press Her\"":
                m "Once you tell me what happened, girl."
                if whoring >=21:
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mash.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "He molested me, Sir."
                    hide screen h_head
                    m "Oh?"
                    show screen h_head
                    her "Coming out of potions class. He saw the... he saw me and decided to..."
                    hide screen h_head
                    m "Go on."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mm.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "He brought me over to a secluded part of the dungeons.{p}He threatened to tell the whole school about..."
                    her "He pushed me up against a wall...{p}and fucked me with the toy until my legs gave out."
                    her "Then he made me... I had to play with myself for him."
                    hide screen h_head
                    m "That's a fantastic idea! Masturbate while you tell me."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "What?"
                    hide screen h_head
                    m "You heard me, girl. You're already full, make use of it."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mn.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Yes sir..."
                    show screen genie_jerking_off
                    show screen hermione_03_b
                    her "I had to lick his shoes till they shined."
                    her "The whole time he was calling me a mudblood...{p}and Gryffinwhore..."
                    her "After I did that,{p}he pulled me up by my hair and started jerking off in my face."
                    hide screen h_head
                    m "Why didn't you suck him off, girl?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mash.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I tried to at first..."
                    hide screen h_head
                    m "As I suspected, Miss Granger, you are truly a filty bitch."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mf.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I really tried! I just wanted it to be over."
                    her "But he told me my filthy muggle tongue{p}wasn't worthy to touch his perfect pureblood prick."
                    hide screen h_head
                    m "You have to respect a man that uses alliteration to describe his cock."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mn.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "It wasn't lost on me, Sir."
                    hide screen h_head
                    m "What next, girl?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mash.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "He made me stick out my tongue."
                    hide screen h_head
                    m "Show me."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mo.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "..."
                    hide screen h_head
                    m "Did he make you drink his cum?"
                    show screen h_head
                    her "*nods*"
                    hide screen h_head
                    menu:
                        "\"Let her continue.\"":
                            m "Continue."
                            $ h_body = "01_hp/29_cust_events/heretic/resources/mn.png"
                            $ h_xpos=390
                            $ h_ypos=340
                            show screen h_head
                            her "It was so degrading..."
                            $ h_body = "01_hp/29_cust_events/heretic/resources/mb.png"
                            $ h_xpos=390
                            $ h_ypos=340
                            show screen h_head
                            her "I had to swish it in my mouth for five minutes before he let me swallow it."
                            hide screen h_head
                            jump g67x8a384
                        "\"Make her drink your cum.\"":
                            m "Come over here, Miss Granger."
                            $ h_body = "01_hp/29_cust_events/heretic/resources/mf.png"
                            $ h_xpos=390
                            $ h_ypos=340
                            show screen h_head
                            her "Sir...{p}If you expect me to suck your cock after a day like this...{p}you'll need to pay me tripple!"
                            hide screen h_head
                            m "What? That's absurd!"
                            show screen h_head
                            her "You try being huminiated by Draco Malfoy for hours!{p}See if you're up for being facefucked!"
                            hide screen h_head
                            label g67x8a384:
                            m "That's enough for now, girl. Fifty points to Gryffindor."
                            $ gryffindor +=50
                            $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                            $ h_xpos=390
                            $ h_ypos=340
                            show screen h_head
                            her "Thank you sir."
                            hide screen h_head
                            hide screen genie_jerking_off
                            hide screen hermione_03_b
                            hide screen bld1
                            hide screen hermione_main
                            hide screen blktone
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            $ walk_xpos=400
                            $ walk_xpos2=610
                            $ hermione_speed = 02.0
                            show screen hermione_walk_01_f
                            pause 2
                            hide screen hermione_walk_01_f
                            $ renpy.play('sounds/door.mp3')
                            with Dissolve(.3)
                            call music_block
                            $ heretic_busy = False
                            $ hermione_sleeping = True
                            jump night_main_menu
                elif whoring >=18 and whoring <=20:
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "We were in potions class, and he must have noticed the dildo..."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mash.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "All of a sudden it just starts vibrating."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mf.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I know that son of a deatheater was behind it."
                    hide screen h_head
                    m "What else, Miss Granger?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Err...do I have to, sir."
                    hide screen h_head
                    m "Yes."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mm.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...He started fucking me."
                    hide screen h_head
                    m "What?"
                    show screen h_head
                    her "With the dildo. Right in the middle of class."
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mn.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I tried to stop him...but..."
                    hide screen h_head
                    m "You must not have tried that hard."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I couldn't focus, sir. I would have stopped him if I could."
                    hide screen h_head
                    m "What next, Miss Granger"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mm.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I was trying not to draw any attention to myself."
                    her "Professor Snape called on me though...{p}I had to try to recite the recepie for Wingot's Elixer while..."
                    hide screen h_head
                    m "While Mr. Malfoy was fucking you with a dildo."
                    show screen h_head
                    her "..."
                    hide screen h_head
                    m "Well?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mn.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...I came halfway through."
                    hide screen h_head
                    m "You're a nasty little slut, Miss Granger."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "It wasn't... I couldn't help it!"
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mn.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "He was, err, I mean it was..."
                    hide screen h_head
                    m "Just admit it Miss Granger, admit you liked it."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I'll never admit it!"
                    hide screen h_head
                    $ h_body = "01_hp/29_cust_events/heretic/resources/ma.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Err, I mean it was criminal! I want to press charges!"
                    hide screen h_head
                    m "Do you mean that, Miss Granger?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mf.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Sir, Draco Malfoy raped me in the middle of a classroom."
                    her "{size=+3}I demand justice!{/size}"
                    hide screen h_head
                    m "Well if you really feel that way I'll just call him up to the office and we'll sort this whole thing out."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Err... No, that's alright sir."
                    hide screen h_head
                    m "Are you sure? You did just demand justice, Miss Granger."
                    $ h_body = "01_hp/29_cust_events/heretic/resources/ma.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "Well... I'll get justice some other way."
                    hide screen h_head
                    m "Should we keep up this charade, or do you just want to get paid?"
                    $ h_body = "01_hp/29_cust_events/heretic/resources/me.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "...Just pay me, sir."
                    hide screen h_head
                    jump q7y8f5
                else:
                    $ h_body = "01_hp/29_cust_events/heretic/resources/mm.png"
                    $ h_xpos=390
                    $ h_ypos=340
                    show screen h_head
                    her "I just... I can't sir."
                    $ mad += 5
                    hide screen bld1
                    hide screen hermione_main
                    hide screen blktone
                    hide screen hermione_02
                    hide screen ctc
                    with d3
                    $ walk_xpos=400
                    $ walk_xpos2=610
                    $ hermione_speed = 02.5
                    show screen hermione_walk_01_f
                    pause 2
                    hide screen hermione_walk_01_f
                    $ renpy.play('sounds/door.mp3')
                    with Dissolve(.3)
                    call music_block
                    $ heretic_busy = False
                    $ hermione_sleeping = True
                    jump night_main_menu
            "\"Let her leave.\"":
                jump q7y8f5
