label __init_variables:
    $ heretic = 0
    $ heretic_01 = False
    $ heretic_02 = False
    $ heretic_03 = False
    $ heretic_busy = False
    $ hermione_desperate_done = False
    return
    
label heritic_intro:
    $ ce_base = True
    $ ce_top = True
    $ ce_arms = True
    $ ce_head_ypos = 235
    return
    
label heritic_event:
    $ ce_base = False
    $ ce_top = False
    $ ce_arms = False
    return

    
label heretic:
    $ ce_name = "heretic"
    $ menu_x = 0.5
    call heritic_intro
    hide screen hermione_main
    hide screen custom_event_h
    with d3
    m "{size=-4}(Is she really going to let me do this?){/size}"
    menu:
        "\"(I've got her well trained.  Why not?)\"":
            pass
        "\"(Not right now.)\"":
            jump silver_requests
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1
    m "Alright then..."
    if heretic == 0: #First time this event taking place.
        m "Miss Granger, do you know what a dildo is?"
        call ce_her_head("I... I'm familiar with the concept.","c")
        m "Have you used one before?"
        call ce_her_head("Excuse me?","q")
        m "There's no need to be embarrassed, girl, just tell me if you've ever used a dildo before."
        if whoring >=16:
            call ce_her_head("...yes I have.","e")
            g9 "Excellent, well you'll be using one today."
        else:
            call ce_her_head("...Of course not professor.","e")
            m "Well you'll be using one today."
    else:
        if whoring >=18:
            call ce_her_head("Well... if it's for the good of Gryffindor.","na")
        else:
            call ce_her_head("This again?","e")
            #### CONTINUE ####

### FIRST QUEST DAY ###
    if whoring <= 14:
        jump too_much
    else:
        call ce_her_head("You want to watch me masturbate?","s")
        call ce_her_head("Er...I have class to get to.","h")
        g9 "Perfect, because you'll need this."
        call ce_her_head("Oh my god, it's as big as my forearm!","s")
        call ce_her_head("Do you expect me to use this for you?","h")
        m "In a way. Put it in, girl."
        call ce_her_head("How many house points is this worth, sir?","c")
        m "I'll give you 50."
        call ce_her_head("Only 50? What if I hurt myself?","q")
        m "It's magically enchanted, there's no risk of injury."
        call ce_her_head("Really? Where did you get this?")
        m "Do you plan on getting one for yourself?"
        call ce_her_head("If I told you yes...{p}Would you give me more house points?","c")
        g4 "Miss Granger, would you rather get to class, or sit here and haggle?"
        call ce_her_head("Fine.")
        ">Hermione slips the dildo under her skirt, struggling to insert the vibrator into herself."
        call ce_her_head("I think it's too big, sir","h")
        m "Nonsense, keep trying."
        ">Changing her strategy, Hermione drops to her knees and rests the base of the cock against the floor. She starts rocking back and forth to wiggle the dick deeper inside her."
        g9 "Lift your skirt, bitch, I want to watch."
        
        call heritic_event
        show screen blktone
        call ce_her_main("","p_jt",140)
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro
        
        ">Complying, Hermione flips her skirt up to reveal her engorged snatch."
        call ce_her_head("Oh my god... mmmmhh","v")
        g9 "Enjoying yourself?"
        call ce_her_head("Of course not. This is all for the... ahn... glory of Gryffindor.","e")
        g4 "Looks like you're enjoying yourself now, slut."
        call ce_her_head("Please sir, don't call me a slut. It's so...{p}{size=-2}degrading.{/size}","v")
        call ce_her_head("{size=-4}(I am a slut.){/size}","e")
        call ce_her_head("{size=-4}(Look what I've become!!!){/size}")
        call ce_her_head("{size=-5}(Masturbating in front of Professor Dumbledore for house points.){/size}")
        call ce_her_head("{size=-4}(I'm nothing but a common whore.){/size}")
        call ce_her_head("{size=-4}(I wish it didn't feel so good.){/size}","v")
        m "I'm sure. You better hurry up if you want to get to class."
        ">With that, Hermione's motions become frantic. Bouncing up and down, tears of frustration well up in the corners of her eyes."
        call ce_her_head("I can't... it won't go any deeper.","e")
        m "Allow me."
        
        call heritic_event
        show screen blktone
        call ce_her_main("","p_di",140)
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro
        
        ">With a few idle movements of your one free hand, you forces the dildo to shoot up inside of Hermione."
        call ce_her_head("AAAAHHH!","a")
        ">Hermione falls sideways onto the floor as a puddle of her fluids pools around her."
        m "Good girl. Now off you go."
        call ce_her_head("Can't I stay here for a bit?","v")
        call ce_her_head("{size=-4}(So you can cum on my...){/size}","a")
        call ce_her_head("{size=-4}(OH GOD! Get it together Hermione!){/size}","s")
        g9 "So you can keep fucking yourself while I watch?"
        call ce_her_head("Of course not. I just need a moment.","c")
        m  "What are you doing?"
        call ce_her_head("Taking this dildo out, sir.","n")
        menu:
            "\"(That gives me an idea.)\"":
                g4 "No, you leave that where it is."
                if whoring >= 16:
                    call ce_her_head("But sir, I have class.","c")
                    g9 "I know."
                    call ce_her_head("You mean...")
                    call ce_her_head("SIR!","s")
                    call ce_her_head("You expect me to walk around all day with this...{p}inside of me?","i")
                    m "That's exactly what I expect."
                    call ce_her_head("...","e")
                    g9 "You had better hurry. Wouldn't want to be late for class."
                    
                    call heritic_event
                    show screen blktone
                    call ce_her_main("","p_us",140)
                    show screen ctc
                    pause
                    hide screen custom_event_h
                    with d3
                    call heritic_intro
                    
                    call ce_her_head("Sir, it's sticking out of the bottom of my skirt!","e")
                    g9 "I know. Off you go."
                    call ce_her_head("{size=-4}(Oh god... I can barely walk... What if somebody notices?){/size}","e")
                    $ heretic_busy = True
                else:
                    jump too_much
            "\"(That's enough.)\"":
                m "Alright, you can go. Fifty points to Gryffindor."
                $ gryffindor +=50
                call ce_her_head("Uh, sir... Could you help me?","e")
                
                call heritic_event
                show screen blktone
                call ce_her_main("","p_jt",140)
                show screen ctc
                pause
                hide screen custom_event_h
                with d3
                call heritic_intro
                
                ">You wave your hand. The dildo erupts out of Hermione, who begins spasming in ecstacy again."
                m "Now say thank you."
                call ce_her_head("Th...thaan...thank you...siiir.","a")
                m "Hurry along Miss Granger, I haven't got all day."
                ">Hermione slowly rises off the floor and lurches out of the room on shaky legs."
                if whoring <= 16:
                    $ whoring +=1
        hide screen bld1
        hide screen custom_event_h
        hide screen blktone
        hide screen hermione_02
        hide screen ctc
        with d3
        
        call her_walk(400,610,2)
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
    $ menu_x = 0.5
    call her_walk(520,400,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    show screen hermione_02
    pause 0.5
    show screen bld1
    with Dissolve(.3)
    $ exposure = renpy.random.randint(1, 10)
    
    if exposure <= 3: #Caught By Harry
        m "Good evening Miss Granger."
        
        call heritic_event
        show screen blktone
        call ce_her_main("","p_nd",140)
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro
        
        call ce_her_head("Hello sir.","n")
        m "So I see you didn't live up to you end of the bargain."
        call ce_her_head("Sir! I would never cheat!","i")
        call ce_her_head("Especially when Gryffindor's honor is at stake!")
        g4 "Then where is the dildo, girl?!"
        call ce_her_head("It's... err...","n")
        
        call heritic_event
        show screen blktone
        call ce_her_main("","p_dd",140)
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro
        
        ">Hermione pulls up her skirt to reveal the dildo lodged deeply in her cunt."
        g4 "Would you care to explain yourself, or are you ready to admit what a whore you are?"
        call ce_her_head("I had no choice, sir.","na")
        m "You could have taken it out."
        call ce_her_head("Err...","e")
        m "Well, did you enjoy yourself today Miss Granger?"
        call ce_her_head("It was...","na")
        call ce_her_head("It was terrible sir.","i")
        m "What was so terrible about it, girl?"
        call ce_her_head("...I can't","e")
        m "Do you want your points or not?"
        call ce_her_head("Please sir, it was mortifying.")
        m "I'm waiting."
        call ce_her_head("...")
        call ce_her_head("I... As soon as I left I ran into Harry. He could...{p}I mean he didn't say anything{p}but I saw him staring at it.")
        m "Well, what did you do?"
        call ce_her_head("I... I knew I couldn't leave it dangling out...{p}and... I mean he already saw it...")
        g4 "Spit it out girl!"
        call ce_her_head("Harry fucked me with the dildo!","v")
        g9 "Oh you filthy whore."
        call ce_her_head("I needed help,{p}and we've been through so much together...")
        call ce_her_head("He must think I'm such a whore.","e")
        g9 "Did you tell him why you had a massive magical cock sticking out of you?"
        call ce_her_head("No. It's better he thinks I'm a slut.{p}I can't imagine him knowing I'm a traitor.{p}to him, or the cause!")
        g9 "Did you enjoy yourself?"
        call ce_her_head("How could you ask me that sir? I was humiliated.","i")
        m "You didn't answer the question."
        call ce_her_head("...","e")
        m "Well?"
        call ce_her_head("Can I go now sir?")
        g4 "Once you answer the question."
        call ce_her_head("...It wasn't terrible...")
        g9 "Did you cum?"
        call ce_her_head("You said I could go, sir.","i")
        menu:
            "\"Press Her.\"":
                g4 "You can go when I tell you to leave. Tell me Miss Granger, did you cum when your friend played with your pussy?"
                if whoring <= 17:
                    call ce_her_head("Sir, you said I could leave! I don't mind being subjected to your sick perversions if order to help out my house, but I draw the line here!","f")
                    g4 "Miss Granger..."
                    call ce_her_head("I'm not finished! You forced me to humiliate myself, and what do I have to show for it?")
                    m "...Fifty point to gryffindor."
                    $ gryffindor +=50
                    call ce_her_head("Good night, Sir.","i")
                    $ mad += 10
                    jump q7y8f5
                else:
                    call ce_her_head("...yes.","e")
                    g4 "Speak up, girl."
                    call ce_her_head("YES!","sl")
                    m "Details, girl."
                    call ce_her_head("He... he pushed me up against a wall.{p}Then he ground the dildo into my pussy.")
                    show screen genie_jerking_off
                    ">You start stroking your cock under the desk."
                    call ce_her_head("He... he said he always thought I was a slut.{p}and then kissed me.","n")
                    call ce_her_head("Oh god, I can still feel his tongue down my throat...","a")
                    call ce_her_head("He forced the dildo all the way in with the his palm.{p}I came so much I stained his shirt sleeve.","sl")
                    g9 "Then what?"
                    call ce_her_head("...","e")
                    g4 "Come on, girl, out with it."
                    call ce_her_head("I sucked him off.","v")
                    g9 "Oh you little bitch."
                    call ce_her_head("I felt the massive bulge when we were pressed up{p}against the wall, and he had helped me... you know...","sl")
                    g9 "Cum your brains out?"
                    call ce_her_head("Yes... I... Can I be honest with you sir?","na")
                    m "I hope so."
                    call ce_her_head("I wanted so desperately to taste it.","v")
                    g11 "YES!"
                    show screen white
                    pause.1
                    hide screen white
                    pause.2
                    show screen genie_jerking_sperm
                    ">You finally cum from the excitement of knowing what she's done."
                    call ce_her_head("Did you enjoy that, sir?","p")
                    hide screen genie_jerking_sperm
                    show screen genie
                    hide screen genie_jerking_off
                    g9 "Absolutely."
                    call ce_her_head("Good. Can I get paid now?")
                    m "Fifty points to gryffindor."
                    call ce_her_head("And sir...","pr")
                    call ce_her_head("You know I only said those things{p}because you wanted me to.{p}right?")
                    m "Whatever you say, Miss Granger."
                    call ce_her_head("I'm not that kind of girl, sir.")
                    call ce_her_head("Harry didn't really use your dildo on me...{p}I went to the bathroom and did it myself.")
                    g9 "Whatever the case, it was a wonderful story."
                    jump q7y8f5
            "\"Let her leave.\"":
                label q7y8f5:
                m "Well done Miss Granger."
                call ce_her_head("Thank you sir.","p")
                m "Fifty points to Gryffindor."
                $ gryffindor +=50
                call ce_her_head("Thank you sir,{p}now if you'll excuse me I need to lay down.")
                if whoring >= 18:
                    m "Where are you going?"
                    call ce_her_head("Sir?","q")
                    g4 "The dildo, girl."
                    call ce_her_head("Oh, right. Err... You see sir, it's stuck.","e")
                    m "Well I can help with..."
                    call ce_her_head("No need, sir.","h")
                    m "Miss Granger, I can't let you leave with my dildo."
                    call ce_her_head("...Please?","q")
                    m "Please what?"
                    call ce_her_head("...Please may I keep the dildo, sir?","sl")
                    g9 "Hm... Very well slut, as long as you walk back to Gryffindor tower with it inside you."
                    call ce_her_head("I was plan...")
                    call ce_her_head("Err... If you say so, sir.","na")
                hide screen bld1
                hide screen custom_event_h
                hide screen blktone
                hide screen hermione_02
                hide screen ctc
                with d3
                
                call her_walk(400,610,2)
                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                with Dissolve(.3)
                
                call music_block
                $ heretic_busy = False
                $ hermione_sleeping = True
                jump night_main_menu
                
    elif exposure >= 4 and exposure <=9: #Accidental Exposure
        m "Hello, Miss Granger."
        call ce_her_head("Hello sir.","pe")
        call ce_her_head("...")
        m "Well?"
        call ce_her_head("There's nothing to talk about.","pr")
        m "So spending an entire day with a dildo inside you is a normal day for you?"
        call ce_her_head("What am I supposed to say?")
        call ce_her_head("I went to class,{p}I ate with friends,{p}I tried to hide the giant rod between my legs.","h")
        m "Welcome to my world."
        call ce_her_head("Are you making fun of me, sir?","i")
        m "Not at the moment. Tell me, girl, did anybody notice?"
        if whoring <=15:
            call ce_her_head("Of course not. As soon as I left I cast a disillusionment charm on it.","d")
            m "What?"
            call ce_her_head("Well, they can't see something that's invisible, sir.")
        else:
            call ce_her_head("...","h")
            m "So, yes. Who and when."
            call ce_her_head("...I don't know his name, sir.{p}He was a first year who was tying his shoe while I walked by.","e")
            call ce_her_head("He...well he saw it.")
            m "What did this boy do?"
            call ce_her_head("He ran off. I think he was embarrassed.","pe")
            m "Is that all?"
            call ce_her_head("Yes, sir.","pr")
            call ce_her_head("I can be quite subtle if I want to be.","d")
            m "Not to mention dull."
        m "Did anything interesting happen to you today?"
        call ce_her_head("I did...Err...No, not really.","h")
        menu:
            "\"Press Her.\"":
                m "Come now, girl,you want to earn these points, right?"
                if whoring <= 17:
                    call ce_her_head("I got a perfect score on a herbology exam today.","p")
                    call ce_her_head("Which, isn't that surprising, but I was a bit...distracted.","na")
                    call ce_her_head("Not that you would care about my test scores...","i")
                    m "{size=-4}*Snoring*{/size}"
                    call ce_her_head("Professor!","s")
                    m "Hm? Wha? Right, uh... 50 points to Gryffindor."
                    $ gryffindor +=50
                    call ce_her_head("Good night, sir.","i")
                    
                    hide screen bld1
                    hide screen custom_event_h
                    hide screen blktone
                    hide screen hermione_02
                    hide screen ctc
                    with d3
                    
                    call her_walk(400,610,2)
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    with Dissolve(.3)
                    
                    call music_block
                    $ heretic_busy = False
                    $ hermione_sleeping = True
                    jump night_main_menu
                else:
                    call ce_her_head("...Well...{p}I have divination today, and it's all so dull.{p}Not to mention Professor Trelawney is a fraud.","i")
                    m "Get on with it, girl!"
                    call ce_her_head("...")
                    call ce_her_head("As I was saying, I was in divination class.")
                    call ce_her_head("Professor Trelawney was droning on about something or other.")
                    call ce_her_head("You have to understand, that room is very comfortable, sir.{p}It's only lit by candle light, the room is heavily incenced...","na")
                    call ce_her_head("And I was lounging among all those very soft pillows.","sl")
                    m "You didn't."
                    call ce_her_head("I think I did, sir.","p")
                    m "Hermione Granger masturbated in class?"
                    call ce_her_head("Only a bit.","sl")
                    call ce_her_head("It was quite easy, I only really had to rock back and forth.{p}The toy did the rest.")
                    m "Miss Granger, you certainly have come a long way."
                    call ce_her_head("I came quite a bit there as well.")
                    m "You delightful little slut, did you enjoy yourself?"
                    call ce_her_head("Sir, you shouldn't call your students sluts...","na")
                    call ce_her_head("I did. More than I expected actually...{p}Especially since I was sitting between Ron and Harry.","sl")
                    m "Did they notice?"
                    call ce_her_head("I have no idea.","n")
                    m "You hope they did, don't you?"
                    call ce_her_head("Of course not!{p}Fantasy is one thing, but if they actually noticed I would be mortified.","e")
                    jump q7y8f5
            "\"Let her leave\"":
                jump q7y8f5
    else: #Caught By Draco
        m "Good evening, Miss Granger."
        
        call heritic_event
        show screen blktone
        call ce_her_main("","p_m",140)
        show screen ctc
        pause
        hide screen custom_event_h
        with d3
        call heritic_intro
        
        m "My goodness, interesting day?"
        call ce_her_head("Can I just get paid, sir?","mash")
        m "You're going to have to do better than that."
        call ce_her_head("...Draco Malfoy.")
        m "What about him?"
        call ce_her_head("He's a Slytherin cretin, a racist, he's...","ma")
        call ce_her_head("He's a monster, sir.")
        m "What makes you say this, girl?"
        call ce_her_head("...","me")
        call ce_her_head("Please... I just want to be done with this, sir...","mash")
        menu:
            "\"Press Her\"":
                m "Once you tell me what happened, girl."
                if whoring >=21:
                    call ce_her_head("He molested me, Sir.","mash")
                    m "Oh?"
                    call ce_her_head("Coming out of potions class. He saw the... he saw me and decided to...")
                    m "Go on."
                    call ce_her_head("He brought me over to a secluded part of the dungeons.{p}He threatened to tell the whole school about...","mm")
                    call ce_her_head("He pushed me up against a wall...{p}and fucked me with the toy until my legs gave out.")
                    call ce_her_head("Then he made me... I had to play with myself for him.")
                    m "That's a fantastic idea! Masturbate while you tell me."
                    call ce_her_head("What?","me")
                    m "You heard me, girl. You're already full, make use of it."
                    call ce_her_head("Yes sir...","mn")
                    show screen genie_jerking_off
                    show screen hermione_03_b
                    call ce_her_head("I had to lick his shoes till they shined.")
                    call ce_her_head("The whole time he was calling me a mudblood...{p}and Gryffinwhore...")
                    call ce_her_head("After I did that,{p}he pulled me up by my hair and started jerking off in my face.")
                    m "Why didn't you suck him off, girl?"
                    call ce_her_head("...","me")
                    call ce_her_head("I tried to at first...","mash")
                    m "As I suspected, Miss Granger, you are truly a filty bitch."
                    call ce_her_head("I really tried! I just wanted it to be over.","mf")
                    call ce_her_head("But he told me my filthy muggle tongue{p}wasn't worthy to touch his perfect pureblood prick.")
                    m "You have to respect a man that uses alliteration to describe his cock."
                    call ce_her_head("It wasn't lost on me, Sir.","mn")
                    m "What next, girl?"
                    call ce_her_head("He made me stick out my tongue.","mash")
                    m "Show me."
                    call ce_her_head("...","mo")
                    m "Did he make you drink his cum?"
                    call ce_her_head("*nods*")
                    menu:
                        "\"Let her continue.\"":
                            m "Continue."
                            call ce_her_head("It was so degrading...","mn")
                            call ce_her_head("I had to swish it in my mouth for five minutes before he let me swallow it.","mb")
                            jump g67x8a384
                        "\"Make her drink your cum.\"":
                            m "Come over here, Miss Granger."
                            call ce_her_head("Sir...{p}If you expect me to suck your cock after a day like this...{p}you'll need to pay me tripple!","mf")
                            m "What? That's absurd!"
                            call ce_her_head("You try being huminiated by Draco Malfoy for hours!{p}See if you're up for being facefucked!")
                            label g67x8a384:
                            m "That's enough for now, girl. Fifty points to Gryffindor."
                            $ gryffindor +=50
                            call ce_her_head("Thank you sir.","me")
                            hide screen genie_jerking_off
                            hide screen hermione_03_b
                            hide screen bld1
                            hide screen custom_event_h
                            hide screen blktone
                            hide screen hermione_02
                            hide screen ctc
                            with d3
                            
                            call her_walk(400,610,2)
                            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                            with Dissolve(.3)
                            
                            call music_block
                            $ heretic_busy = False
                            $ hermione_sleeping = True
                            jump night_main_menu
                elif whoring >=18 and whoring <=20:
                    call ce_her_head("We were in potions class, and he must have noticed the dildo...","me")
                    call ce_her_head("All of a sudden it just starts vibrating.","mash")
                    call ce_her_head("I know that son of a deatheater was behind it.","mf")
                    m "What else, Miss Granger?"
                    call ce_her_head("Err...do I have to, sir.","me")
                    m "Yes."
                    call ce_her_head("...He started fucking me.","mm")
                    m "What?"
                    call ce_her_head("With the dildo. Right in the middle of class.")
                    call ce_her_head("I tried to stop him...but...","mn")
                    m "You must not have tried that hard."
                    call ce_her_head("I couldn't focus, sir. I would have stopped him if I could.","me")
                    m "What next, Miss Granger"
                    call ce_her_head("I was trying not to draw any attention to myself.","mm")
                    call ce_her_head("Professor Snape called on me though...{p}I had to try to recite the recepie for Wingot's Elixer while...")
                    m "While Mr. Malfoy was fucking you with a dildo."
                    call ce_her_head("...")
                    m "Well?"
                    call ce_her_head("...I came halfway through.","mn")
                    m "You're a nasty little slut, Miss Granger."
                    call ce_her_head("It wasn't... I couldn't help it!","me")
                    call ce_her_head("He was, err, I mean it was...","mn")
                    m "Just admit it Miss Granger, admit you liked it."
                    call ce_her_head("I'll never admit it!","me")
                    call ce_her_head("Err, I mean it was criminal! I want to press charges!","ma")
                    m "Do you mean that, Miss Granger?"
                    call ce_her_head("Sir, Draco Malfoy raped me in the middle of a classroom.","mf")
                    call ce_her_head("{size=+3}I demand justice!{/size}")
                    m "Well if you really feel that way I'll just call him up to the office and we'll sort this whole thing out."
                    call ce_her_head("Err... No, that's alright sir.","me")
                    m "Are you sure? You did just demand justice, Miss Granger."
                    call ce_her_head("Well... I'll get justice some other way.","ma")
                    m "Should we keep up this charade, or do you just want to get paid?"
                    call ce_her_head("...Just pay me, sir.","me")
                    jump q7y8f5
                else:
                    call ce_her_head("I just... I can't sir.","mm")
                    $ mad += 5
                    hide screen bld1
                    hide screen custom_event_h
                    hide screen blktone
                    hide screen hermione_02
                    hide screen ctc
                    with d3
                    
                    call her_walk(400,610,2)
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    with Dissolve(.3)
                    
                    call music_block
                    $ heretic_busy = False
                    $ hermione_sleeping = True
                    jump night_main_menu
            "\"Let her leave.\"":
                jump q7y8f5
