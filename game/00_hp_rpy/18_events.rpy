    
label day_event_check:
    #NOT IN USE if day == 4: #Genie says: "I wonder what has become of that two-faced dude?"
    #About two-faced dude    call event_04

    if day == 8:
        call event_08 #Hermione shows up for the first time.
    if day >= 9 and hermione_is_waiting_01 and not event09:
        call event_09 #Second visit from Hermione. Says she sent a letter to the Minestry.
                      #Takes place after first special event with Snape, where he just complains about Hermione.
    if event13_happened and not event14_happened:
        call event_14
    if whoring >= 15 and not event_chairman_happened: #Turns True after an event where Hermione comes and says that she wants to be in the Autumn Ball committee.
        call want_to_rule
    if whoring >= 15 and event_chairman_happened and days_without_an_event >= 2 and not snape_against_chairman_hap: # Turns TRUE after Snape comes and complains that appointing Hermione in the Autumn Ball committee was a mistake.
        call against_the_rule
    if whoring >= 18 and days_without_an_event >= 5 and snape_against_chairman_hap and not have_no_dress_hap: #Turns TRUE after Hermione comes and cries about having no proper dress for the Ball.
        call crying_about_dress # 27_final_events
    if whoring >= 18 and have_no_dress_hap and not sorry_for_hesterics and days_without_an_event >= 1: # Turns TRUE after Hermione comes and apologizes for the day (event) before.
        call sorry_about_hesterics
    #if day == 10:
    #    call event_08_02 #Hermione shows up for the second time. (Shorter skirts notion).
    #if day == 11:
    #    call event_08_03 #Hermione shows up for the third time. (Rules for teachers noton).
    if day >= 12 and not event09 and hermione_is_waiting_01:
        call event_09 #Visit from Hermione after first Special event with Snape (Where Genie proposes plan against her).
    #if day >= 13 and not event10 and hermione_is_waiting_02:
    #    call event_10 #Hermione shows up for the third time. Says that she started "MRM" and sent letter to the ministry.
    if event13_happened and not event14_happened:
        call event_14
    if day == 1 and not bird_examined and not desk_examined and not cupboard_examined and not door_examined and not fireplace_examined:
        call event_01
    return
    
label night_event_check:
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
    return
    
    
    
    
#### GENIE EVENTS ####

#First event in the game. Gennie finds himself at the desk.
label event_01: 
    show screen bld1
    with d3
    m "..................?"
    m "Your majesty?"
    m "......................................................."
    g4 "I did it again, didn't I?"
    g4 "Teleported myself to who knows where..."
    m "What's with those ingredients?"
    m "They seem to be way more potent that I thought."
    m "Well, whatever this place is I have no business here..."
    m "Better undo the spell and return to the shop before the princess gets angry with me again..."
    m "....................."
    m "Although..."
    m "There is something odd about this place... it's..."
    m "It's almost brimming with...."
    g4 "{size=+5}MAGIC?!{/size}"
    m "Yes... magic, I can feel it. So powerful and yet somehow..."
    m "....alien."
    m "Interesting..."
    m "I think I will stick around for a little bit..."
    hide screen bld1
    with d3
    return
    
#owl event
label event_02:
    $ letterQ.send("{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}","hermione_letter_1")
    play sound "sounds/owl.mp3"  #Quiet...
    show screen owl
    show screen bld1
    with d3
    m "What? An owl?"
    hide screen bld1
    with d3
    return
    
    
    
    
#### SNAPE EVENTS ####

#First time genie meets snape
label event_02_1:
    $ snape_SC.xpos = 550 #Defines position of the Snape's full length sprite.
    $ snape_SC.ypos = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snape_SC.chibi.xpos = 750
    show screen snape_chibi_standing #Snape stands still.
    with d5
    pause.3
    show screen bld1
    with d3
    g4 "{size=-3}(An Indigenous life form!?){/size}"
    hide screen bld1
    with d3
    show screen thought(snape_SC.chibi.xpos+40, snape_SC.chibi.ypos-30)
    with d3
    pause 1
    show screen bld1
    with d3
    m "{size=-3}(looks human enough...){/size}"
    m "{size=-3}(Maybe if I just act cool he'll leave...?){/size}"
    hide screen bld1
    with d3
    hide screen snape_chibi_standing
    hide screen thought
    with d3
    
    $ snape_SC.chibi.walk(750,500,4)
    show screen snape_chibi_standing
    pause.5
    show screen bld1
    with d3
    
    $ snape_SC.name = "??? ???"
    $ snape_SC.body = "snape_01"
    $ snape_SC.showScreen()
    show screen ctc
    with d3
    pause
    
    $ snape_SC.say("Albus... Do you have a moment?")
    $ snape_SC.hideScreen()
    hide screen ctc
    
#    show screen ctc
#    pause
#    pat "I hate to ask but its been bugging me for awhile."
#    pat "What is your Guesstimated time of completion for the game?"
#    pat "No pressure to give an answer if you don't want to."
#    show screen snape_main
#    with d3
#    sna "Mister silvarius..."
#    sna "This is your first strike..."
#    sna "If I hear this question from you again, then it will cost your house 100 points."
    
#    hide screen snape_main
#    with d3
#    show screen emo
#    her "Professor... *gulp!* I-- I can't breathe!"
#    hide screen emo
#    show screen snape_main
#    with d3
#    sna "I will be with you in a moment, miss Granger..."
#    hide screen snape_main
#    with d3
#    show screen emo
#    her "!!!"
#    hide screen emo
#    show screen snape_main
#    with d3
#    sna "I hope we came to an understanding, here, mister silvarius."
#    sna "Didn't we?"
    

    #m "{size=-3}(\"Albus\"? Is that supposed to be my name or is that's just how the humans of this world greet one another?){/size}"
    menu:
        m "..."
        "\"Actually I'm a bit busy.\"":
            $ snape_SC.say("Well, aren't you always, Albus?","snape_04")
        "\"Of course. What is it?\"":
            pass
        "\"And Albus to you too.\"":
            $ snape_SC.say("What?","snape_05")
            $ snape_SC.say("Albus I'm not in the mood for your... shenanigans.","snape_04")
        "\"Take me to your leader.\"":
            $ snape_SC.say("What?")
            $ snape_SC.say("Hm...?")
            $ snape_SC.say("You mean the minster of magic?")
            $ snape_SC.say("I would rather avoid having to deal with that bureaucrat...","snape_03")
            m "Fine, never mind... How can I be of help?"
            
    $ snape_SC.say("I have something important I need to discuss with you...","snape_06")
    $ snape_SC.say("I think we need to revise our admittance policy.")
    $ snape_SC.hideScreen()
    with d3
    m "................?"
    $ snape_SC.say("Half of my... so-called \"pupils\" are nothing but annoying maggots that make my life miserable on a daily basis.","snape_03")
    $ snape_SC.hideScreen()
    with d3
    m "................"
    $ snape_SC.say("Most of them belong to your precious \"gryffindor\" house of course...","snape_07")
    $ snape_SC.hideScreen()
    with d3
    m "......?"
    $ snape_SC.say("The wretched Weasley family, that noisy Granger girl and of course the hero of all the juvenile delinquents around the globe....")
    $ snape_SC.say("{size=+3}The Potter boy!{/size}","snape_08")
    $ snape_SC.say("Mark my words, Albus. The \"gryffindor house\" will become this school's undoing!","snape_01")
    $ snape_SC.hideScreen()
    m "...................."
    $ snape_SC.say("Nothing but annoying maggots, the lot of them!")
    $ snape_SC.say("And if that wasn't enough, now they spread all sorts of nasty rumours about the teachers!","snape_06")
    $ snape_SC.say("Particularly about yours truly...")
    $ snape_SC.hideScreen()
    m "......................"
    $ snape_SC.say("You don't believe those rumours, do you Albus?","snape_05")
    $ snape_SC.hideScreen()
    menu:
        m ".............."
        "\"Well, of course not!\"":
            $ snape_SC.say("Good...","snape_09")
            $ snape_SC.say("You know me better than that. I wouldn't care for such things...")
        "\"Where there's smoke, there's fire.\"":
            $ snape_SC.say("Albus?! You can't be serious!","snape_10")
            $ snape_SC.say("Those are nothing but filthy lies, I'm telling you!")
    $ snape_SC.hideScreen()
    m "........................."
    $ snape_SC.say("Well, those wretched kids left me completely exhausted, I think I will retire for today.","snape_04")
    $ snape_SC.say("................","snape_09")
    
    stop music fadeout 1.0
    
    $ snape_SC.hideScreen()
    hide screen bld1
    with d3
    
    hide screen snape_chibi_standing
    $ snape_SC.chibi.walk(500,750,3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.5
    show screen bld1
    with d3
    m "Hm..."
    m "So that tall, broody dude mistook me for someone else...?"
    m "Which means I must be shrouded in a concealment spell..."
    m "........."
    m "So basically, I'm a genie disguised as a human, who is in turn disguised as another human..."
    m "No, that's not stupid at all..."
    a4 "Shut it! Nobody understands a true genius."
    
#    who2 "Professor Dumbldore, do you have a minute?"
#    m "{size=-3}(What? Another one?){/size}"
#    who2 "Let me speak to him!"
#    m "Excuse me?"
#    who2 "Y-yes master..."
#    who2 "Greetings to you, oh almighty genie..."
#    with hpunch
#    g4 "{size=+7}What the hell?!{/size}"
#    g4 "{size=+7}Stay away from me, you demon!!!{/size}"
#    g4 "{size=+7}Body snatchers are among us!\nI'm outta here!{/size}"
#    m "...wait a second."
#    m "How did you just call me?"
#    who2 "An almighty genie. That is what you are, is it not?"
#    g4 "How did you... Who the hell are you?"
#    who2 "Oh, but of course. Forgive me my poor manners..."
#    who2 "Master's name is Tom Riddle..."
#    who2 "No! You sniveling maggot! we hate that name!"
#    who2 "We want to be called Lord Voldemort!"
#    who2 "Forgive me, master..."
#    m "Ehm... mr. Lord--"
#    with hpunch
#    who2 "No! No! \"lord\" is not master's name, \"lord\" is master's title, you idiot!"
#    who2 "Watch your tone, worm! That is an immortal being before you."
#    who2 "He may look human, but his powers topple mine by far."
#    who2 "Please take no offense, oh almighty one. My servant is quite dim."
#    menu:
#        m "..."
#        "\"Does the sun take offense from an ant?\"":
#            who2 "And yet it is prudent for an ant to know it's place, wouldn't you agree?"
#        "\"Watch it, mortal! I'll smite you!\"":
#            who2 "My humble apologies. The worthless servant shall be punished properly."
#            who2 "M-master...?"
#        "\"Apology accepted. What do you want?\"":
#            who2 "You are unusually forgiving for a genie. But we shall not test your patience anymore..."
            
#    vol "Correct me if we are wrong, but you came to our world due to an accident..."
#    m ".................."
#    vol "And you find our world intriguing, do you not?"
#    m "You have two faces growing out of your head. So yeah, colour me curious."
#    who2 "Splendid..."
#    who2 "In that case we want to make you an offer..."
#    who2 "We...."
#    who2 "We...."
#    m "???"
#    who2 "We are tired... Cover us..."
#    who2 "Of course, master."
#    m "What? What's going on?"
#    vol "My apologies, oh immortal one. My master needs to rest now."
#    vol "We will visit you again soon..."
#    m "..................."
#    g4 "What the....?"
#    m "Ah, hell. May as well stay for one more day..."
    
    $ days_without_an_event = 0
    
    jump day_start

#Sanpe talks to genie about hermione, snape becomes suspicious
label event_03: 
    $ snape_SC.xpos = 550 #Defines position of the Snape's full length sprite.
    $ snape_SC.ypos = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snape_SC.chibi.walk(750,500,2)
    pause 1.5
    show screen snape_chibi_standing #Snape stands still.
    pause.1
    show screen bld1
    with d3
    m "{size=-3}(That broody guy again...){/size}"
    $ snape_SC.say("Albus!","snape_01")
    m "Hey.......... you..."
    $ snape_SC.say("You need to do something about that Granger girl...")
    $ snape_SC.say("","snape_06")
    $ snape_SC.say("Honestly... I'm running out of ways to punish that... that...")
    $ snape_SC.say("","snape_04")
    $ snape_SC.say("That little witch!")
    menu:
        m "..."
        "\"Granger? Hermione Granger, right?\"":
            $ snape_SC.say("Yes, her...")
            $ snape_SC.say(" She also happens to be a part of the \"Potter gang\".")
        "\"I got your back, Jack, witches be crazy!\"":
            $ snape_SC.say("What...? Albus you behave oddly lately.")
            $ snape_SC.say("Is everything alright?")
            menu:
                m "..."
                "\"Yes, I'm fine. Go on.\"":
                    $ snape_SC.say("If you say so...")
                "\"You know me. I love my shenanigans.\"":
                    $ snape_SC.say("Hm.....")
        "\".....................................................\"":
            pass
    $ snape_SC.say("Remember how back in the days they used to publicly flog the students?")
    $ snape_SC.say("I swear if we could bring that back all of our problems would be solved...")
    $ snape_SC.say("Yes... I would gladly tie that girl to a flogging pole in front of the entire school...")
    $ snape_SC.say("Then lift her skirt up, and...","snape_20")
    $ snape_SC.say("*Khem!* Sadly, nowadays we teachers are severely limited in the disciplinary measures we have at our disposal...","snape_12")
    $ snape_SC.say("I know you are just as powerless as I am in this matter, but I'm telling you, that girl should better stop testing my patience.")
    menu:
        m "..."
        "\"I'll take care of that little whore!\"":
            $ snape_SC.say("...?!","snape_05")
            $ snape_SC.say("Albus...")
            $ snape_SC.say("You are acting strange lately...")
        "\"Nobody ever said this job would be easy.\"":
            $ snape_SC.say("Sometimes I feel like I would rather deal with a classroom full of Dementors...","snape_06")
        "\"You will feel better tomorrow.\"":
            $ snape_SC.say("You are probably right...","snape_06")
    $ snape_SC.say("Hm...")
    $ snape_SC.say("Perhaps I'd better go get some sleep.","snape_06")
    $ snape_SC.say("I need to be in my top shape every morning...")
    $ snape_SC.say("You can't show weakness to those kids or they will swallow you whole...")
    $ snape_SC.say("Good night, Albus.","24")
    
    
    $ snape_SC.hideScreen()
    hide screen bld1
    with d3
    
    hide screen snape_chibi_standing
    $ snape_SC.chibi.walk(500,750,3)
    show screen snape_chibi_standing_f #Snape stands still. (Mirrored).
    pause.2
    $ snape_SC.say(".................")
    $ snape_SC.say("One more thing...")
    show screen bld1
    with d3
    $ snape_SC.say("You should ignore any lies you hear about me and those slytherin girls...")
    m "Got it."
    hide screen bld1
    $ snape_SC.hideScreen()
    hide screen snape_chibi_standing_f #Snape stands still. (Mirrored).
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    jump day_start

#Snape comes in, has a talk with Genie, then the duel starts.
label event_05: 
    $ snape_SC.xpos = 550 #Defines position of the Snape's full length sprite.
    $ snape_SC.ypos = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snape_SC.chibi.walk(750,500,2)
    show screen snape_chibi_standing #Snape stands still.
    show screen bld1
    with d3
    
    $ snape_SC.body = "snape_01"
    $ snape_SC.showScreen()
    show screen ctc
    with d3
    
    $ snape_SC.say("Good evening, Albus.")
    $ snape_SC.say("I want to talk to you about those damn kids again...")
    $ snape_SC.say("But first I want to ask you something...")
    $ snape_SC.say("Did you notice anything strange going on around here lately?","snape_05")
    menu:
        m "..."
        "{size=-2}\"Like you being especially whiny?\"{/size}":
            $ snape_SC.say("What? B-but... Those kids...")
            $ snape_SC.say("Well, perhaps you are right...","snape_06")
        "{size=-2}\"That owl is fetching may mail, man!\"{/size}":
            $ snape_SC.say("An owl? What about it?")
            $ snape_SC.say("That's not what I mean...","snape_25")
            $ snape_SC.say("Well, never mind...","snape_29")
#        "\"I Saw a dude with two faces the other day.\"":
#            who2 "?!"
#            who2 "What's that supposed to mean...?"
        "{size=-2}\"No, not really. It's just business as usual.\"{/size}":
            $ snape_SC.say("Hm... Maybe I'm just being paranoid...")
    $ snape_SC.say("The reason why I'm here today is the \"Potter Gang\"","24")
    $ snape_SC.say("There are only so many points I can subtract from the Gryffindor house, you know...","snape_01")
    $ snape_SC.say("And the Granger girl became the worst of them lately...")
    $ snape_SC.say("She practically leads the onslaught.","snape_06")
    $ snape_SC.say("Speaking of which, has she been sending you any letters lately?","snape_05")
    menu:
        m "..."
        "\"Hermione Granger? No, Nothing from her.\"":
            $ snape_SC.say("I see... So she's been bluffing then.")
            $ snape_SC.say("What an annoying young witch.","snape_16")
        "\"Yes... Every damn day...\"":
            $ snape_SC.say("Really now?")
            $ snape_SC.say("Any lies about me in particular?")
            $ snape_SC.say("I hope you know better than to listen to the likes of her...")
    
    $ snape_SC.say("She would never admit it, but I know she's been spreading those nasty rumours about me around the school...","snape_03")
    $ snape_SC.say("Tsk... Noisy little...... witch.","snape_29")
    $ snape_SC.say("I would never stoop so low as to trade house points in exchange for sexual favours...","snape_09")
    $ snape_SC.say("I mean, sure, we use house points to motivate students, but that's completely different...")
    $ snape_SC.say("I can't speak for the rest of the staff though...")
    $ snape_SC.say("The stories I hear about Minerva McGonagall and those poor Gryffindor freshmen may be true...","snape_13")
    $ snape_SC.say("Well, I just wanted to make sure that you take those rumours about me for what they are...","snape_01")
    $ snape_SC.say("Nasty lies made up by a bunch of spoiled kids.")
    $ snape_SC.say("Oh.... Before I go...")
    $ snape_SC.say("There is one thing I meant to ask you for a while now...")
    $ snape_SC.say(".........................","snape_09")
    $ snape_SC.say("What is my name?","snape_05")
    menu:
        m "..."
        "\"What? What kind of question is that?\"":
            $ snape_SC.say("You are right...","snape_06")
            $ snape_SC.say("Forgive me... I'm just being paranoid I suppose...")
            $ snape_SC.say("But you can never be too cautious with rumours about  \"you know who\" still being alive and all...","snape_05")
        "\"Tall broody guy?\"":
            $ snape_SC.say("Albus, lately you adopted a peculiar sense of humor, that I do not care for in a slightest...","snape_06")
            $ snape_SC.say("Maybe you should spend a little less time in the company of that big oaf Hagrid.")
        "-\{Use magic to get the right answer\}-":
            $ snape_SC.hideScreen()
            with d3
            
            show screen blktone
            with d3
            ">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
            hide screen blktone
            with d3
            
            $ snape_SC.say("!!?","snape_03")
            m "What kind of question is this, Severus?"
            $ d_flag_01 = True
            $ snape_SC.name = "Severus Snape"
            $ snape_SC.say("Forgive me... I'm just being paranoid I suppose...")


    $ snape_SC.say("Well, good night, Albus.","snape_06")
    $ snape_SC.hideScreen()
    hide screen bld1
    with d3
    
    hide screen snape_chibi_standing
    $ snape_SC.chibi.walk(500,750,3)
    show screen snape_chibi_standing_f #Snape stands still. (Mirrored).
    pause.2
    
    stop music fadeout 1.0
    $ snape_SC.sayText("........................")
    hide screen snape_chibi_standing_f
    hide screen bld1
    #hide screen genie
    show screen blkfade
    with d3
    $ renpy.play('sounds/07_run.mp3') 
    pause 2
    g4 "???"
    
    show screen snape_defends
    hide screen blkfade
    with d3
    show screen ctc
    
    play music "music/hitman.mp3" fadein 1 fadeout 1 # TENSE THEME 
    
    pause
    hide screen ctc
    show screen bld1
    with d3
    if d_flag_01:
        $ snape_SC.say_H("Who are you, scum!","head_6")
        g4 "What? It's me... uhm... Abius! I mean, Albus!"
        $ snape_SC.say_H("You cannot fool me.","head_4")
        $ snape_SC.say_H("Just now, you used some sort of alien magic!","head_4")
        $ snape_SC.say_H("Reveal your true self to me now, fiend! Who are you?!","head_6")
    else:
        $ snape_SC.say_H("My name is Severus Snape!","head_1")
        $ snape_SC.name = "Severus Snape"
        $ snape_SC.say_H("Now, who might you be...?","head_1")
        
    g4 "!!!"
    $ snape_SC.say_H("Easy now... Just answer my question.","head_1")
    
    m "Alright, alright, just calm down, would you...?"
    $ snape_SC.say_H("........","head_1")
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait:
    menu:
        m "..."
        "\"I am not your enemy.\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            $ snape_SC.say_H("That the first thing an enemy would say.","head_1")
        "\"I'm just a tourist. I'll be leaving now.\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            $ snape_SC.say_H("You are not going anywhere.","head_1")
        "\"I work for Albis Doombldore!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            $ snape_SC.say_H("It's Albus Dumbledore, you moron!","head_1")
    if d_points == 2:
        pass
    else:
        jump no_wait

    $ snape_SC.say_H("Who sent you here? What did you do with the real Albus?","head_1")
    $ snape_SC.say_H("Shed your disguise and reveal your true self at once, this is your last warning!","head_1")
    $ d_points = 0
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label no_wait_2:
    menu:
        m "..."

        "\"I can't. It's hard to explain...\"" if not d_flag_01:
            $ d_flag_01 = True
            $ d_points +=1
            $ snape_SC.say_H("I have no interest in your explanations. I wouldn't believe a single word you'd say anyway!","head_1")
        "\"Stop threatening me, human!\"" if not d_flag_02:
            $ d_flag_02 = True
            $ d_points +=1
            $ snape_SC.say_H("\"Human\"?","head_1")
            $ snape_SC.say_H("Are you implying that you are {size=+5}not{/size} one?","head_1")
            $ snape_SC.say_H("What are you then?! Dispell your cloaking charm immediately or else!","head_1")
        "\"I mean you no harm, I swear!\"" if not d_flag_03:
            $ d_flag_03 = True
            $ d_points +=1
            $ snape_SC.say_H("Is that so?","head_1")
            $ snape_SC.say_H("Prove it then. Dispel your cloaking charm now!","head_1")

    if d_points == 2:
        pass
    else:
        jump no_wait_2

            
            
    $ snape_SC.say_H("I've heard enough!","head_1")
    g4 "By the great desert sands! Would you let me explain, human?!"
    $ snape_SC.say_H("There is nothing left to explain!","head_1")
    $ snape_SC.say_H("Since you refuse to cooperate, I'll be taking you into custody by force!","head_1")
    g4 "What?! Wait!"
    
    if skip_duel == True:
        jump snape_lost
    
    
    stop music 
    $ renpy.play('sounds/glass_break.mp3') #Sound of a door opening.
    play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1

    $ end_u_1_pic =  "glass"
    pause.1
    show screen end_u_1
    hide screen snape_defends
    pause 3

    
    jump duel
    
#THE TALK AFTER THE DUEL ENDS.
label event_06: 
    $ potions = 0 #Makes sure there are no potions left in the possessions. 
    
    #play music "music/Final Fantasy VII - Victory Fanfare.mp3" fadein 1 fadeout 1 
    stop music fadeout 2.0
    g4 "*Panting*"
    g4 "Ready to talk now?!"
    $ snape_SC.say_H("(...i-impossible...)","head_8")
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    
    $ duel_OBJ.genie = "no_magic"
    
    m "I told you you are no match for me..."
    show screen bld1
    with d3
    m "You did give me a good run for my money though..."
    $ snape_SC.say_H("The way you conjure the spells with your bare hands...","head_1")
    $ snape_SC.say_H("No human could do that... who--","head_1")
    $ snape_SC.say_H("{size=+5}What are you?{/size}","head_4")
    $ snape_SC.say_H("Some sort of shape-shifting demon summoned by \"you know who\"?","head_1")
    m "Summoned by whom?"
    $ snape_SC.say_H("By \"you know who\"!","head_2")
    m "What?"
    $ snape_SC.say_H("......................","head_7")
    m "............................"
    m "Listen, I'm not a demon..."
    m "And I sure as heck don't work for \"I don't know who\"!"
    $ snape_SC.say_H(".............................","head_1")
    m "I've been ehm..."
    m "...Conducting an experiment back in my world, during which something went wrong and I ended up here."
    m "That's all..."
    $ snape_SC.say_H("..........................","head_1")
    $ snape_SC.say_H("What became of to the real Albus Dumbledore then?","head_1")
    m "I'm sure he is fine."
    m "He's Probably feeling as surprised about finding himself in my world as I am about finding myself here..."
    $ snape_SC.say_H("....................................","head_1")
    $ snape_SC.say_H("When did this happen?","head_1")
    m "Four days ago..."
    $ snape_SC.say_H("Can you go back?","head_1")
    m "I think so..."
    $ snape_SC.say_H("Why didn't you then?","head_2")
    m "Not sure..."
    m "The Magic of this world is so bizarre... Perhaps I just got curious."
    $ snape_SC.say_H("...................","head_1")
    $ snape_SC.say_H("You need to fix this...","head_1")
    m "Fix what?"
    $ snape_SC.say_H("Everything. You need to bring back Albus and leave our world.","head_4")
    menu:
        m "..."

        "\"Yes, yes, I know. Off I go then.\"":
            m "Yes, yes, I know..."
            m "Well, off I go then. Sorry for the ruckus."
            $ snape_SC.say_H("No harm done...","head_1")
        "\"But I like it here! Can't I stay?\"":
            $ snape_SC.say_H("Absolutely not.","head_1")
            $ snape_SC.say_H("Whoever you are, you are not from this plane of existence.","head_1")
            $ snape_SC.say_H("Your very presence here upsets the natural order of things.","head_1")
            $ snape_SC.say_H("And these days this school needs a proper headmaster more than ever.","head_1")
    $ snape_SC.say_H("Have a save trip home now.","head_1")
    m "Ehm... Thank you, mr. Severus. Good luck with your students and the \"potter gang\"."
    $ snape_SC.say_H("\"The potter gang\"?","head_1")
    $ snape_SC.say_H("Oh, right, those buggers...","head_7")
    menu:
        "-Undo the spell-":
            pass
    menu:
        "-Undo the spell-":
            pass
    menu:
        "-Undo the spell-":
            pass

    $ snape_SC.say_H("Did it work? Albus, is that really you?","head_1")
    menu:
        m "..."
        "\"Yeah, that's me. So good to be back!\"":
            $ snape_SC.say_H("Glad to have you back, old friend. Are you alright?","head_1")
            m "I'm fine, Severus, thank you."
            $ snape_SC.say_H("How was it, in that other world?","head_1")
            m "A lot of sand and very hot, but other than that quite pleasant."
            $ snape_SC.say_H("I see... Did you miss your brother?","head_1")
            menu:
                m "..."
                "\"Yes, I missed you so much!\"":
                    $ snape_SC.say_H(".......................","head_1")
                    $ snape_SC.say_H("Yeah, right....","head_1")
                "\"I don't have a brother, Severus.\"":
                     $ snape_SC.say_H("........................","head_1")
                     $ snape_SC.say_H("You may not have one, but the real Albus Dumbledore does.","head_1")
                "-Use magic to get the right answer-":
                    show screen bld1
                    with d3
                    ">You use your phenomenal cosmic powers to peek into the very fabric of the universe and get the correct answer."
                    hide screen bld1
                    with d3
                    m "My little brother Aberforth? Why would I miss him?"
                    $ snape_SC.say_H("I can feel it whenever you use your alien magic...","head_1")
        "\"Nope. It's still me. The non-human guy.\"":
            pass


    $ snape_SC.say_H("Why are you still here, creature?","head_1")
    m "I'm not sure... I tried to undo the spell but nothing happened..."


    $ snape_SC.say_H("Marvelous...","head_7")
    $ snape_SC.say_H("What does this mean? So You're staying here for good?","head_1")
    m "Of course not..."
    m "Me being here at all is only possible because the spell is compensating for the unbalance caused by itself..."
    m "said spell will wear off eventually and I shall be pulled back into my world."
    m "Likewise, your Dumbledore-friend shall be pulled back here."
    $ snape_SC.say_H("I see...","head_1")
    $ snape_SC.say_H("How long until the spell wears off?","head_1")
    menu:
        m "..."
        "\"A couple of days.\"":
            $ snape_SC.say_H("I see...","head_1")
        "\"A week or so...\"":
            $ snape_SC.say_H("Hm.... A week, huh...","head_1")
        "\"Could be months...\"":
             $ snape_SC.say_H("That long?","head_1")
             $ snape_SC.say_H("Now isn't that just \"perfect\"?","head_1")
        "\"I have no clue...\"":
            $ snape_SC.say_H(".....................","head_1")
            $ snape_SC.say_H("Splendid...","head_2")

    m "Alright, to be honest I'm not sure where to go from here..."
    m "All this time I thought I could undo the spell whenever I want to..."
    $ snape_SC.say_H("...................................................","head_1")
    $ snape_SC.say_H("..................................","head_1")
    $ snape_SC.say_H("...................","head_1")
    m "Snape?"
    $ snape_SC.say_H("...................................................","head_1")
    m "Severus?"
    $ snape_SC.say_H("Yes, yes...","head_6")
    $ snape_SC.say_H("Listen, it's very late, and too much happened already...","head_1")
    $ snape_SC.say_H("I need to process all of this.","head_7")
    $ snape_SC.say_H("I will come to see you tomorrow, after my classes.","head_1")
    $ snape_SC.say_H("Until then, keep your true identity and our conversation a secret, alright?","head_6")
    m "Not a problem."
    $ snape_SC.say_H("Alright then...","head_1")
    $ snape_SC.say_H("But before I go, I have one more question...","head_1")
    m "I'm listening..."
    $ snape_SC.say_H("........","head_2")
    $ snape_SC.say_H("If you are not a human, then...","head_1")
    $ snape_SC.say_H("What are you?","head_7")
    m "...I'm a genie."
    $ snape_SC.say_H("A genie?","head_1")
    m "Yes, I possess phenomenal cosmic powers and all that..."
    $ snape_SC.say_H("Seriously?","head_1")
    m "Oh, yes."
    $ snape_SC.say_H("Unbelievable...","head_1")
    $ snape_SC.say_H("Well, I'll see you tomorrow.... genie.","head_1")
    m "I'll be here..."
    $ snape_SC.say_H("(A genie? Now that's new...)","head_7")
    
    hide screen duel
    jump day_start
    
#THE TALK WITH SNAPE THE DAY AFTER THE DUEL.
label event_07: 
    $ snape_SC.xpos = 550 #Defines position of the Snape's full length sprite.
    $ snape_SC.ypos = 0
    
    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snape_SC.chibi.walk(750,500,2)
    show screen snape_chibi_standing #Snape stands still.
    show screen bld1
    with d3
    
    show screen ctc
    with d3
    
    $ snape_SC.say("...................","snape_01")
    $ snape_SC.hideScreen()
    with d3
    m "Good evening..."
    $ snape_SC.say("Is the spell still in effect?")
    $ snape_SC.hideScreen()
    with d3
    m "Yes. very much so."
    $ snape_SC.say("I see...")
    $ snape_SC.say("Last night I gave our little.... conundrum some thought.")
    $ snape_SC.say("And I think I came up with a solution...")
    m "Really? Great! I'm listening."
    $ snape_SC.say("Let's just roll with it...","snape_29")
    m "Excuse me?"
    $ snape_SC.say("Well what else could we do?","snape_06")
    $ snape_SC.say("Normally I would alert the ministry of magic and let them take care of this mess...")
    $ snape_SC.say("But I'd rather avoid any dealings with those rotten bureaucrats this time...")
    $ snape_SC.say("Also, losing a headmaster, even temporarily could hurt the school's reputation...","snape_10")
    $ snape_SC.say("And what if your spell wears out tomorrow, or even tonight?")
    $ snape_SC.say("I see no reason to start a commotion...","snape_09")
    m "Hm..."
    $ snape_SC.say("So we shall keep the charade going for now...","snape_03")

    m "By doing what exactly?"
    $ snape_SC.say("Just act like Albus always does: never leave this tower and try to avoid any human contact...","snape_05") 
    m "That...."
    m "Sounds..."
    g4 "Incredibly boring!"
    g4 "What am I supposed to do here?"
    $ snape_SC.say("You are a Genie. Conjure up some sort of entertainment for yourself.","snape_01")
    m "My magic does not working properly here for some reason..."
    m "And my lamp is literally worlds away..."
    $ snape_SC.say("Well, what do you expect me to about that?","snape_03")
    $ snape_SC.say("Send you a couple of girls from Slytherin maybe?")
    g9 "No idea what \"Slytherin\" is but I think that would work..."
    $ snape_SC.say("That was a joke, obviously.","snape_04")
    $ snape_SC.say("Although...","snape_09")
    $ snape_SC.say("Hm...")
    $ snape_SC.say("Well, in any case I don't see how entertaining {size=+7}you{/size} is {size=+7}my{/size} problem.","snape_01")
    m "Oh, but it is!"
    m "I'm immortal and all-powerful..."
    m "Being bored is like the worst thing that could happen to me!"
    g4 "And I have a thing against being cooped up in small spaces with nothing to do!"
    g4 "I may lose my mind..."
    g4 "Oh! Ah! I think it's happening already!"
    $ snape_SC.say(".......","snape_03")
    g4 "I'm losing my mind! It's getting hard to breathe!"
    $ snape_SC.say("....","snape_04")
    g4 "It's so dark..."
    g4 "Are you still here?"
    $ snape_SC.say("....","snape_03")
    m "........."
    $ snape_SC.say("Are you done?","snape_10")
    m "Yes..."
    m "Seriously though, I don't see how this whole affair benefits me at all."
    $ snape_SC.say("Do you have any choice?","snape_01")
    m "I do..."
    m "Instead of sitting here on my ass all day and being quiet I could explore your world..."
    $ snape_SC.say("Hm...","snape_03")
    $ snape_SC.say("Well, alright, what do you want?","snape_01") 
    m "Teach me your magic..."
    $ snape_SC.say("My magic?","snape_05")
    m "Yes... The way you conjure up your spells is..."
    m "Intriguing..."
    $ snape_SC.say("Hm...","snape_04")
    $ snape_SC.say("So be it...","snape_06")
    m "Oh, and send me some of those \"Slytherin\" girls as well.."
    $ snape_SC.say("...............","snape_05")
    $ snape_SC.say(".........................")
    $ snape_SC.say("Ha-ha-ha!!!","snape_28")
    m "What? What did I say?"
    $ snape_SC.say("A-ha-ha-ha-ha...","snape_28")
    $ snape_SC.say("No, no, my apologies...","snape_02")
    $ snape_SC.say("It's just that to me you still look and sound like Albus...")
    $ snape_SC.say("To hear Professor Dumbledore say things like \"Send me those girls up\"...")
    $ snape_SC.say("It's hysterical... ","snape_22")
    $ snape_SC.say("But you would't understand...","snape_09")
    m "Heh..."
    g9 "Send those whores up, Severus. I'm feeling lonely tonight."
    $ snape_SC.say("Ha-ha-ha! Stop it, you're killing me!","snape_28")
    $ snape_SC.say("A-Ha-ha-ha!")
    m "No, I'm serious... Is it possible?"
    $ snape_SC.say("Hm...","snape_02")
    $ snape_SC.say("We'll see...")
    $ snape_SC.say("You being our new headmaster sure presents me with interesting possibilities...")
    $ snape_SC.say("I need some time to figure out how to use our situation for my advantage.")
    m "You mean {size=+7}our{/size} advantage, right?"
    $ snape_SC.say("Oh, yes, yes, of course...","snape_06")
    $ snape_SC.say("Well, I think we are done for today...")
    $ snape_SC.say("Good night... genie.","24")
    m "Yes, good night, Severus."

    $ snape_SC.hideScreen()
    hide screen ctc
    hide screen bld1
    with d3
    
    hide screen snape_chibi_standing #Snape stands still.
    $ sna_walk(500,750,3)
    show screen snape_chibi_standing_f #Snape stands still. (Mirrored).
    pause.2
    $ sna_head(".................","snape_06")
    $ sna_head("\"Send those whores up, Severus!\" Ha-ha-ha..","snape_28")
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_chibi_standing_f #Snape stands still. (Mirrored).
    with d3
    m "Hm... "
    m "I Suppose I'll just curl up in a ball on top of this desk as usual..."
    pause.2
    
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    
    show screen blktone
    with d3
    ">You've unlocked the ability to summon Severus Snape to your office."
    hide screen blktone
    with d3
    
    $ hanging_with_snape = True
    
    jump day_start
    
    
    
    
#### HERMONE EVENT ####
    
### (DAY) GENIE MEETS HERMONE - IN USE.
label event_08: 
    #"EVENT_08"
    stop music fadeout 1.0
    pause 1
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    m "Huh?"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    pause.7
    m "Somebody is knocking on the door..."
    m "Crap... I'm supposed to avoid any human contact!"
    m "Hm... What are the chances that the thing knocking on my door is not human?"
    m "Yeah, quite slim..."
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock*"
    m "Persistent little bastard..."
    $ d_flag_01 = False #When False Genie doesn't know Hermione's name.
    $ d_flag_02 = False #When TRUE Genie knows it's a girl knocking on the door.
    menu:
        m "..."
        "\"Who is it?\"":
            $ d_flag_01 = True
            who "It's me, professor..."
            who "Hermione Granger. Can I come in?"
            m "{size=-4}(It's that wretched woman who's been harassing me with her letters lately...){/size}"
            menu: 
                m "..."
                "\"Go away, please. I'm busy.\"":
                    her "But, professor, I really need to talk to you..."
                    m "..........................................."
                    her "Professor? I'm coming in!"
                    m "{size=-4}(Crap...){/size}"
                "\"Yes, yes, you can come in.\"":
                    pass          
        "\"Come in!\"":
            pass
        "\"Go away!\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "But, professor, I really need to talk to you..."
            m "..........................................."
            who "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"
        "\"................\"":
            $ d_flag_02 = True #When TRUE Genie knows it's a girl knocking on the door.
            who "Professor, are you there?"
            m "{size=-4}(Go away...){/size}"
            who "Professor, I really need to talk to you..."
            m "..........................................."
            her "Professor? I'm coming in!"
            m "{size=-4}(Crap...){/size}"


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 770
    $ hermione_SC.chibi.ypos = 250
    show screen hermione_blink #Hermione stands still.
    with Dissolve(.5)
    pause.3
    if not d_flag_01:
        m "?!!"
    if not d_flag_02: #When TRUE Genie knows it's a girl knocking on the door.
        m "{size=-3}(A girl?){/size}"
        
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    
    call her_walk(610,400,3)
    show screen hermione_blink #Hermione stands still.
    pause.5
    
    show screen bld1
    show screen ctc
    show screen hermione_blink
    with d3
    
    call her_main("","body_01",xpos=370,ypos=0)
    pause
    call her_main("Good morning professor.","body_03")
    hide screen ctc
    menu:
        "\"Good morning... girl.\"":
            her "{size=-4}(\"Girl\"?){/size}"
            pass
        "\"Good morning, Hermione.\"" if d_flag_01:
            pass
        "\"Good morning, Child.\"":
            her "{size=-4}(\"Child\"...?){/size}"
        "\"................................\"":
            pass
    her "I am very busy with my class schedule, but I kept my morning free today so that I could see you, professor."
    her "You probably know why I am here too."
    call her_main("The issue I have been fruitlessly trying to bring to your attention lately.","body_04")
    her "I cannot understand why you are not acting to stop that nonsense, professor!"
    her "This simply cannot continue like that!"
    call her_main("The inequality is starting to affect all of the houses...","body_02")
    her "Simply because we have more integrity than the rest..."
    her "Do you think it's fair that the people who deserve to be in the lead are being pushed back instead?"
    her "Do you think that's fair, professor? Do you?"
    call her_main("","body_03")
    m "{size=-4}(Would you look at that pretty, little thing?){/size}"
    m "{size=-4}(Look at her going on and on about something... She's adorable.){/size}"
    m "{size=-4}(Damn, I haven't seen a woman in weeks.){/size}"
    menu:
        "\"(I will jerk off a little while she talks.)\"":
            $ jerk_off_session = True #Affects next conversation with Snape.
            $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
        "\"(No, that's stupid! I Need to behave!)\"":
            $ d_flag_01 = False #NOT JERKING OFF.
            pass
    if d_flag_01:
        hide screen hermione_main
        hide screen bld1
        with d3
        show screen blktone8
        with d3
        ">You reach under the desk and grab your cock..."
        hide screen blktone8
        with d3
        hide screen genie
        show screen genie_jerking_off
        with d3
    m "Yes, keep on going, dear."
    show screen bld1
    with d3
    call her_main("\"Yes\"?! So you think it's fair?","body_05")
    m "Oh, of course not, I meant \"no\". But Keep on going anyway..."
    call her_main("That's a relief. I'm glad that you agree with me, professor...","body_03")
    call her_main("As I was saying, the whole issue is simply ridiculous and I cannot believe that it is taking place in our day and age!","body_04")
    if d_flag_01:
        hide screen hermione_main
        hide screen bld1
        show screen blktone8
        with d3
        ">*Fap!* *Fap!* *Fap!*"
        ">You keep on stroking you cock..."
        hide screen blktone8
        with d3
        show screen hermione_main
        show screen bld1
        with d3
    else:
        m "I see..."
    her "I mean, I would understand if something like this were to occur during the middle ages..."
    her "But we left the middle ages behind a long time ago, did we not?"
    if d_flag_01:
        g9 "{size=-4}(Would you look at those rosy cheeks? I want to poke'em with my cock.){/size}"
        hide screen hermione_main
        show screen blktone8
        with d3
        ">You keep stroking your cock..."
        hide screen blktone8
        show screen hermione_main
        with d3
    else:
        m "Ehm... I suppose you did. I mean, we did."
    her "So it hurts the whole house-point-distribution system."
    her "But it even doesn't stop there!"
    her "It hurts our entire educational system as well..."
    her "And more importantly the motivation among students is steadily decreasing due to it!"
    if d_flag_01:
        m "{size=-4}(Look at those huge knockers on you, girl!){/size}"
        m "{size=-4}(Yes... I want to squeeze my dick between them...){/size}"
    her "As you can see the situation is dire..."
    call her_main("But we can still set everything right...","body_02")
    her "As the representative of our school's Student Representative Body..."
    her "I have a few suggestions on how to do that more efficiently."
    if not d_flag_01:
        m ".............."
    her "First of all the house point system needs to be reinforced!"
    call her_main("You need to control the point distribution better, sir.","body_03")
    if d_flag_01:
        g4 "{size=-4}(Yes, you are a whore... A nasty little whore... I bet you love to suck cocks... Don't you? Yes, I bet you do...){/size}"
        hide screen hermione_main
        with d3
        show screen blktone8
        with d4
        ">You stroke you diamond-hard cock ferociously!"
        hide screen blktone8 
        with d4
        show screen hermione_main
        with d3
    her "Of course you agree with me on this, professor, do you not?"
    if d_flag_01:
        g4 "{size=-4}*Panting heavily*{/size}"
        call her_main("Professor...?","body_07")
        g4 "{size=-4}(Crap. What does she want now?){/size}"
        g4 "Yes, it's all true. Please keep going..."
        her "Ehm... So, as I was saying..."
        hide screen hermione_main
        with d3
        m "{size=-4}(Oh... That was a good jerkoff session, but I'm getting dangerously close to the \"grand finale\".){/size}" 
        m "{size=-4}(Maybe I should stop before I get myself into trouble.){/size}"
        menu:
            "\"(Yes, time to actually listen to her.)\"":
                show screen genie
                with d3
                $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
                pass
            "\"(No! I want to keep on jerking off!)\"":
                pass
    else:
        m "{size=-4}(Do I? I honestly don't give a damn...){/size}"
        m "Uhm... I suppose I do..."
        her "{size=-4}(\"Suppose\"?){/size}"
        her "{size=-4}(When did Professor Dumbledore become so... apathetic.){/size}"
    call her_main("Another measure you could take in consideration is tightening the control over your staff...","body_04")
    her "Especially the teachers..."
    call her_main("I hope I'm not stepping out of line here, sir, but some of the teachers really do require supervision...","body_03")
    if d_flag_01:
        g4 "{size=-4}(Yes! You little whore! You fucking little whore!) *Panting*{/size}"
    else:
        m "......................."
    call her_main("I understand that you may not have time for this, professor, After all you are the headmaster of our school and a very busy and important man.","body_04")
    her "being a top student is hard on me as well sometimes..."
    if d_flag_01:
        g4 "{size=-4}(She said \"hard-on\"!) *Panting*{/size}"
    her "But you could delegate that task to me..."
    her "Just put your faith in me professor." 
    if d_flag_01: 
        call her_main("Yes, you can do it! Just put it in me, sir!","body_01")
        stop music fadeout 1.0
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=-4}(Oh crap, that did it!) *Argh!*{/size}"
        hide screen hermione_main
        with d3
        hide screen bld1
        with d3
        show screen genie_jerking_sperm
        with d3
        pause 3
        
        show screen bld1
        with d3
        call her_main("Professor?! What is going on...?","body_18")
        show screen genie_jerking_sperm_02
        with d3
        g4 "Ah... YESSSSS.....!"
        her "???"
        g4 "*breathing heavily* Yes! yes...."
        show screen genie
        #show screen genie_jerking_off
        with d3
        m "Yes, girl. It's all exactly as you say and I will.... take care of it all."
    else:
        m "Alright... I will think about your proposal, I promise."
    call her_main("Really?","body_07")
    her "hm..........."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    call her_main("That's a relief! Thank you, professor.","body_04")
    if d_flag_01:
        m "No, no, thank you..."
        call her_main("Hm...","body_07")
    call her_main("My classes are about to start so I'd better go now.","body_04")
    her "Thank you for your time..."
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    if d_flag_01:
        m "{size=-4}(This was awesome...) *Panting*{/size}"
        m "{size=-4}(My pants are ruined though...){/size}"
    else:
        m "................."
        m "(She is cute, but quite a piece of work...)"
    hide screen genie_jerking_sperm_02
    with d3
    $ snape_against_hermione = True #Turns True after event_08. Activates special date with Snape # 01.
    $ event08_happened = True
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    return

###(DAY) HERMIONE TALKS DRESS CODE - NOT IN USE
label event_08_02:
    "EVENT_08_02"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"
        "\"Yes, come in...\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"
    
    call her_walk(610,400,3)
    show screen hermione_blink #Hermione stands still.
    
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    show screen hermione_blink
    with d3
    call her_main("Good morning, professor Dumbledore.","body_01",xpos=370,ypos=0)
    menu:
        "\"Good morning, miss Granger.\"":
            pass
        "\"Good morning, child.\"":
            her "{size=-5}(\"Child\"? Must you be so condescending all the time?){/size}"
            m "What was that?"
            her "It's nothing sir..."
        "\"Good morning, whore.\"":
            her "Em... What?"
            g4 "{size=-4}(OK, that was stupid. Damage control, damage control!){/size}"
            m "*Khem* Excuse me, something stuck in my throat... Good morning, miss Granger."
            her "{size=-5}(Did he just called me a.... no, no way.){/size}"
            
    her "Professor Dumbledore, I am here to talk to you as the \"MRM\" president..."
    m "............."
    her "We held an emergency assembly yesterday..."
    her "The matter in question was the \"Hogwarts\" uniform for girls..."
    her "We came to the conclusion that the currently employed dress-code is highly inappropriate for an educational institution..." 
    show screen ctc
    pause
    her "///////"
    m "Seriously?"
    hide screen ctc
    her "Yes, professor, I assure you, we are very serious."
    her "The way you force our poor girls to dress is unacceptable..."
    her "Such frivolous attire distracts male students from studying, putting them at a disadvantage..."
    her "All those distractions they have to deal with..."
    her "The poor souls..."
    m "Did any of the boys actually complain about this?"
    her "We won't wait for the issue to manifest, sir! We'll prevent it!"
    her "No individual shall be at a disadvantage based on his or her gender."
    her "This is what they call \"Sexism\" in the muggle world, sir."
    m "Your explanations are getting way too convoluted for my liking, miss Granger."
    m "Tell me what you are proposing exactly, to Put every woman in the school in a burqa?"
    her "Officially doubling the length of the girls' skirts in the school regulations would suffice..."
    menu:

        "{size=-4}\"That is laughable. Request refused!\"{/size}":
            $ d_flag_05 = True #Notion refused. Will take affect in the next event.
            her "What... B-but? We made a decision..."
            m "Miss Granger, I'm sorry to break this to you, but I am still the headmaster of this school..."
            m "And the only decisions that matter are mine!"
            her "So you ignore the voice of the people, sir?"
            m "The only voice I hear is yours, miss Granger."
            her "Don't You know what happens to tyrants who underestimate the power of the masses?"
            her "They get overthrown!"
            m "Careful, now. Your words smell of treason, young lady."
            m "Don't You know what happens to traitors?"
            m "The get hung!"
            her "!!!"
            her "Tsk!"
            her "I will make you take me seriously, professor!"
        
        "{size=-4}\"Boys must study in peace. request approved!\"{/size}":
            her "Splendid. I will everyone know."
            her "Thank you professor."
            hide screen bld1
            hide screen hermione_main
            with Dissolve(.3)
            
            call her_walk(400,610,2)
            
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            with Dissolve(.3)
            pause.5
            m "...................."
           

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "I'm Starting to enjoy our meetings less and less..."
    return

###(DAY) HERMIONE DEMANDS ACTION - NOT IN USE
label event_08_03:
    "EVENT_08_03"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    m "Who is--"
    her "Professor, I'm coming in..."
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    show screen hermione_blink #Hermione stands still.
    pause.5
    show screen bld1
    show screen hermione_blink
    with d3
    
    call her_main("Good morning, professor Dumbledore.","body_01",xpos=370,ypos=0)
    menu:
        "\"Good morning, miss Granger.\"":
            pass
        "\"Good morning, child.\"":
            her "{size=-5}(\"Child\"? Must you be so condescending all the time? Nasty old prick!){/size}"
            m "What was that?"
            her "nothing sir..."
        "\"Good morning, miss president.\"":
            her "{size=-4}(Is he being sarcastic?){/size}"
            

    if not d_flag_05:
        her "You promised me to take action, professor..."
        her "But nothing changed since our last conversation..."
        menu:

            "\"I lied...\"":
                her "B-but..."
                her "But you are the headmaster, sir. You word should mean something..."

            "\"I forgot\"":
                her "You forgot, sir?"
                her "Did you really?"
                her "Or Maybe you just didn't care enough to remember?"
            "\"I just don't care.\"":
                her "B-but....?"
                her "Professor Dumbledore, this is a serious matter!"

    else:
        her "Professor Dumbledore, you rejected the offer I made you last time we met..."
        her "And now we reap the results..."
    her "The boys are still having a hard time concentrating on their studies..."
    m "Oh, I do have a cure for that!"
    m "Lets put a paper bag over every girl's head!"
    her "That would be mistreatment of a human being based on her gender..."
    her "Another example of sexism..."
    her "Or better yet \"Misogyny\"."
    m "\"Misogyny\" is a general dislike towards women, miss Granger."
    m "A healthy male is biologically incapable of disliking all the females of his kind..."
    m "Otherwise humanity would've gone extinct a long time ago already..."
    her "Professor, we have no time for semantics."
    her "The entire school is in peril!"
    m "Is it...?"
    her "The \"MRM\" had another meeting yesterday, and--"
    m "No, not again..."
    m "are there are any male members in your little \"Men's rights movement\"?"
    her "That is beside the point..."
    m "Right..."
#    her "That is irrelevant..."
#    m "How is it irrelavant? That's the only thing that {size=+7}IS{/size} relevant!"
    her "Let me finish my sentence, please."
    her "I am officially addressing you as the \"MRM\" president now..."
    her "And as a representative of this school's student body..."
    her "We demand these new regulations to be enforced..."
    her "Number one..."
    her "No teacher is allowed to raise a voice towards a student or call the said student an unflattering name..."
    m "What?"
    her "Number two..."
    her "All the school ghosts have to be confined to the abandoned tower in the north wing of the school."
    m "You have school ghosts? That's pretty cool!"
    her "Number three..."
    her "Every teacher, and especially Professor Severus Snape need to take a qualification test every three months..."
    m "Is that all?"
    her "That is all, sir."
    menu:
        m "..."
        "\"Fine. Your demands shall be satisfied.\"":
            her "Thank you, professor."
            her "I, as a representative of the student's will, thank you for your cooperation."
        "\"Sounds like bullshit. You're dismissed.\"":
            her "What? I..."
            her "But this is... you can't..."
            m "Dismissed!"
            her "Tsk..."       
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "...................."
    
    $ snape_against_hermione = True #Turns True after event_08_03. Activates event_09 when hanging out with Snape next time.

    
    return

###(DAY) HERMIONE SENDS LETTER TO MINESTRY - IN USE
label event_09:
                #Takes place after first special event with Snape, where he just complains about Hermione.
    
    #"EVENT_09"
    stop music fadeout 3.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    call her_walk(610,400,3,redux_pause=0.5)
    
    show screen hermione_blink #Hermione stands still.
    pause.5
    show screen bld1
    with d3
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    
    show screen hermione_blink
    with d3
    call her_main("","body_03",xpos=370,ypos=0)
    show screen ctc
    pause
    call her_main("Good morning, professor Dumbledore.","body_04")
    hide screen ctc
    menu:

        "\"Good morning, child.\"":
            call her_main("{size=-4}(Again with the \"child\"...){/size}","body_09")
            call her_main("Sir, I would appreciate it if you would treat me as an equal...","body_04")
            m "{size=-4}(I'm literally millions of years older than you, witch. We are anything but equal.){/size}"
            m "...................."
            call her_main("................","body_09")
        "\"Good morning, miss Granger.\"":
            her "Ehm... so, about the reason of me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            pass
    
    her "I see that no matter what I do I simply cannot get through to you, sir."
    call her_main("So in light of your negligence towards your duties I decided to take the initiative myself!","body_04")
    m "Did you now...?"
    her "Yes! We, the proud students of Hogwarts, detest sexism..."
    her "No individual shall be treated differently based on his or her gender."
    m "But--"
    call her_main("Please, let me finish, professor!","body_05")
    call her_main("I'm organizing the \"Men's rights movements\" in our school!","body_04")
    g4 "Oh, boy, this is just so typical!"
    g4 "Blame everything on--"
    stop music fadeout 1.0
    m "Wait, did you say {size=+5}MEN'S{/size} rights movement?"
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    call her_main("You have no idea how hard it is to be a boy in our school these days...","body_11")
    menu:
        "\"Didn't see this one coming...\"":
            call her_main("No, you did not, because you, as an authority figure, refuse to listen to us, sir!","body_04")
            her "But we will make you hear us..."
        "{size=-3}\"That's literally the dumbest idea I've ever heard.\"{/size}":
            call her_main("I knew you would say something like that...","body_07")

    call her_main("Did you know that some of the girls in this school are now selling favours for house points...?","body_09")
    her "Sometimes even for good grades..."
    m "Really?"
    call her_main("Nobody from the \"Gryffindor\" house of course...","body_04")
    her "And that's what puts us at a disadvantage - our integrity!"
    her "As for the boys - they have to work ten times harder than the girls simply to pass a test..."
    her "Or, if they are lucky enough, to get one meagre house-point..."
    call her_main("This is sexism in its purest form!","body_02")
    menu:
        m "..."
        "\"What you want me to do?\"":
            call her_main("Nothing!","body_03")
            m "Great. I'm good at that."
        "\"I'm Not sure what to say...\"":
            call her_main("You do not need to say anything anymore, professor.","body_03")
        "\"You are being ridiculous!\"":
            call her_main("Am I? Well, we'll see...","body_07")

    call her_main("I already sent a letter to the ministry of magic.","body_04")
    with hpunch
    g4 "{size=+7}You did what?!{/size}"
    m "{size=-4}(Wait, do I really give a damn about that?){/size}"
    her "I'm sorry, but you left me no choice, professor."

    her "Now, if you excuse me I must get to my classes..."
    hide screen bld1
    hide screen hermione_main
    with d3
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with d3
    pause.5
    m "...................."
    

    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    return

###(DAY) HERMIONE MAKES THREATS - NOT IN USE
label event_09_2:
    "EVENT_09"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I'll come back tomorrow then..."
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well alright..."
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event09 = True #You let Hermione in. This event will stop looping now.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    call her_walk(610,400,3,redux_pause=0.5)
    
    show screen hermione_blink #Hermione stands still.
    with d3
    pause.5
    show screen bld1
    with d3
    
    show screen hermione_blink
    with d3
    call her_main("Good morning, professor Dumbledore.","body_01",xpos=370,ypos=0)
    menu:
        "\"Good morning, miss Granger.\"":
            pass
        "\"Good morning, child.\"":
            her "{size=-5}(\"Child\"? Must you be so condescending all the time? Nasty old prick!){/size}"
            m "What was that?"
            her "nothing sir..."
        "\"...............\"":
            her "...................."
            
            
    her "My classes are about to start so I don't have much time..."
    her "Being a top student is not easy, so I hope you understand that the Other kids in our school are looking up to me."
    #m "{size=-4}(Is that so...?){/size}"
    her "I realize that you are a important very person as well..."
    her "But do you think you could spare a little of your time to actually perform your duties as the headmaster of this school?"
    menu:
        "\"Excuse me?\"":
            her "Yes, I refuse to sugarcoat this any longer!"
        "\"...................\"":
            pass
    her "I brought so many problems this school has to your attention..."
    her "And you, sir, ignored every single one of them!"
    her "Did you know that some of the girls from \"Slytherin\" offer sexual favours in exchange for house points?"
    m "Do they?"
    her "What message does it send to the rest of the houses?"
    her "Students don't have to work hard anymore, don't have to study, all they need to do is show a little skin..."
    her "This is deplorable!"
    her "I'm warning, professor..."
    menu:
        "\" You are \"Warning me\" miss Granger?\"":
            her "Yes, professor. I am warning you."
            her "If you are not willing to listen to me, I will find someone who will!"
        "\"..............................................................\"":
            pass
    her "If you will not take action soon you will be leaving me no choice, professor..."
    her "I will have to contact the ministry of magic..."
    m "{size=-4}(The ministry of magic? Should I care?){/size}"
    menu:

        "\"Calm down, miss Granger, please.\"":
            her "I cannot stay calm in the face of your ignorance, sir!"
        "\"I hear you. I will take action, I promise.\"":
            her "Really? Well I am glad we finally came to an understanding, sir."
            her "Or are you just going to ignore my pleas as usual?"
        "\"Out of my office, girl! Out, I said!!!\"":
            her "What?"
            m "Get out of my office!"
            her "B-but..."
            with hpunch
            g4 "{size=+7}OUT I SAID!!!{/size}"
            her "{size=-6}(Wow... Never seen old man lose it like that...){/size}"
            her "{size=-6}(I'd better leave before he has a hart attack or something...){/size}"
            her "..............."
            jump pissed_me_off

    her "Oh... I am already late for my classes. I must go now."
    m "You have a nice day... {size=-5}witch!{/size}"
    her "Thank you, professor."
    label pissed_me_off:
    hide screen bld1
    hide screen hermione_main
    with d3
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with d3
    pause.5
    m "...................."
    
    $ hermione_is_waiting_01 = False #Makes sure this event is not repeated.
    $ snape_against_hermione_02 = True #Turns True after event_09. Activates second event when hanging out with Snape.
    return

###(DAY) HERMIONE TAKES MATTERS INTO HER OWN HANDS - NOT IN USE
label event_10:
    #Hermione says that she sent the letter to the Ministry of Magic."
    "EVENT_10"
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come by later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come by later.\"":
            her "But..."
            her "Well alright..."
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"

    $ event10 = True #You let Hermione in. This event will stop looping now.
    $ walk_xpos=610 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_walk_01 
    with d4
    pause 2.5
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    show screen hermione_blink
    with d3
    call her_main("Good morning, professor Dumbledore.","body_01",xpos=370,ypos=0)
    menu:
        "\"Good morning, child.\"":
            her "{size=-4}(Again with the \"child\"...){/size}"
            her "Sir, I would appreciate it if you could treat me as an equal..."
            m "{size=-4}(I'm literally millions years older then you, witch. We are anything but equal.){/size}"
        "\"Good morning, miss Granger.\"":
            her "Em... so, to the reason of me being here today then..."
        "\"Yeah, yeah, whatever...\"":
            her "Em..."
    her "I see that no matter what I do I simply cannot get through to you, sir."
    her "So in light of your negligence towards your duties as a headmaster of this school..."
    her "I decided to take initiative in my own hands!"
#    m "Did you now...?"
#    her "Yes! And since I detest sexism..."
#    m "You do, do you?"
#    her "Yes, I do. No individual shall be treated differently based on his or her gender."
#    m "This doesn't make any sence, girl!"
#    her "Let me finish, professor!"
#    her "I'm organizing a \"Men's rights movement\" in our school!"
#    m "Oh, this is just typical! Blame everything on--"
#    m "Wait, did you say {size=+5}MEN'S{/size} rights?"
#    her "You have no idea how hard it is to be a boy in our school these days..."
#    menu:
#        "\"Didn't see this one coming...\"":
#            her "No, you did not, because you refuse to listen to me, sir!"
#        "\"Literally stupidest thing I've ever heard.\"":
#            her "I knew you will say something like that..."
    her "Half of the girls in this school are now selling favours for house points..."
    her "Sometimes even for good grades..."
    her "Nobody from the \"Gryffindor\" house of course..."
    her "And that's what puts us into disadvantage - our integrity!"
    her "Unthinkable..."
    her "As for the boys - they have to work ten times harder then the girls simply to pass a test..."
    her "Or, if they are lucky enough, get one meager house-point..."
    her "This is sexism in it's purest form!"
    menu:
        "\"What do you want {size=+7}me{/size} to do?\"":
            her "Nothing!"
        "\"Not sure what to say...\"":
            her "You do not need to say anything anymore, professor."
        "\"You are being ridiculous!\"":
            her "Am I? Well, we'll see..."
    her "I already sent a letter to the ministry of magic."
    with hpunch
    g4 "{size=+7}You did what?!{/size}"
    m "{size=-4}(Wait, do I really give a damn about that?){/size}"
    her "I am sorry, but you left me no choice, professor."
    her "Now, if you excuse me I must get to my classes..."

    hide screen bld1
    hide screen hermione_main
    with d3
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    m "The little woman quite literary sucks out all the happiness out of me..."
   
    $ hermione_takes_classes = True
   
    $ hermione_is_waiting_02 = False #Makes sure this event is not repeated.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    return

###(NIGHT) HERMIONE ALMOST FAILED A TEST - IN USE
label event_11: 
    #"EVENT_11"
    stop music fadeout 1.0
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    her "Professor, I'm coming in!"
    m "...."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    $ walk_xpos=570 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.1 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    # show screen hermione_walk_01 
    show screen hermione_chibi_robe #Hermione. Chibi. Walking. Wearing a robe.
    with d4
    pause 1.8
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    #show screen hermione_blink #Hermione stands still.
    show screen hermione_02_b #Hermione stands still wearing a robe.
    show screen bld1
    show screen ctc
    with Dissolve(.3)
    
    $ robeon = True #Hermione is wearing a robe.
    
    call her_main("","body_09",xpos=370,ypos=0)
    pause
    call her_main("Good evening professor.","body_12")
    hide screen ctc
    menu:
        "\"-stare full of hatred-\"":
            call her_main("You can stare at me all you want, sir.","body_07")
            her "It will not make the problems of this school go away."
        "*sigh of exasperation*":
            call her_main("Is this a bad time?","body_03")
            call her_main("Well, since I'm already here...","body_02")
        "\"....................................\"":
            call her_main("Professor?","body_02")
            m "Yes, yes..."
    call her_main("Something... bizarre has happened today...","body_04")
    call her_main("I'm Not sure how to describe this...","body_07")
    call her_main("................................","body_09")
    call her_main("I think I almost failed a test...","body_12")
    menu:
        "\"That happens to students sometimes.\"":
            call her_main("To other students, yes. But not to me, sir!","body_12")
            call her_main("Never to me...","body_13")
        "\"(Way to go, Snape!)\"":
            call her_main("Excuse me?","body_03")
            m "What?"
            m "Oh, I said, that's too bad. How're you holding up?"
            call her_main(".................","body_07")
        "\"So why tell me?\"":
            her "Because... this is not an ordinary event!"

    her "I'm not sure what is going on here..."
    m "An evil scheme against you, miss Granger?"
    call her_main("This is not a laughing matter, sir.","body_03")
    call her_main("You should consider me a \"measuring stick\" for our educational system.","body_04")
    her "If I \"almost\" fail a test, the rest of the students will definitely fail it."
    m "Is that so...?"
    call her_main("Yes, professor. Something went terribly wrong today...","body_07")
    call her_main(".................................","body_12")
    call her_main("But what if it did not?","body_11")
    her "What if all the tests will be this difficult from now on?"
    call her_main("I need to study harder!","body_10")
    label cant_say:
    menu:
        "\"I could tutor you, miss Granger.\"":
            call her_main("You professor?","body_14")
            call her_main("Oh, thank you for your offer but I don't think that would be necessary, sir.","body_15")
            call her_main("The best tutor is a book, and I have the entire Hogwarts library at my disposal.","body_16")
        "\"A wise decision, miss Granger.\"":
            call her_main("Thank you, professor.","body_15")
        "\"You need to put my cock in your mouth.\"":
            m "You need to put my co--"
            call her_main("Huh?","body_15")
            m "{size=-4}(No, I can't actually say that...){/size}"
            call her_main("......?","body_17")
            jump cant_say
    m "............"
    call her_main("Well, if there is nothing else, I have a studying schedule to keep.","body_16")
    m "By all means..."
    
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    show screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    #show screen hermione_walk_01_f 
    pause 2
    hide screen hermione_chibi_robe_f #Hermione. Chibi. Walking. Wearing a robe.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    pause.5
    
    $ robeon = False #Hermione is NOT wearing a robe.
    $ only_upper = False #Otherwise skirt shows up under the robe.
    
    $ event11_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1

    return

###(NIGHT) HERMIONE MIGHT HAVE FAILED A TEST - IN USE
label event_12:
    #"EVENT_12"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    show screen hermione_blink #Hermione stands still.
    with d3
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    her "Professor! I need to talk to you!"
    m "(So She doesn't even bother to knock anymore?)"
    show screen bld1
    with Dissolve(.3)
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    call her_main("Professor, something awful happened today!","body_11")
    her "I failed a test today..."
    her "I cannot believe this is happening!"
    call her_main("How this even possible?!","body_18")
    menu:
        "\"You should study more, girl!\"":
            call her_main("But I did study all night!","body_19")
        "\"There, there... It'll be alright.\"":
            call her_main("No it won't! This is a catastrophe!","body_20") 

    call her_main("And the worst part is that I think I might be the only one who has failed...","body_21")
    call her_main("How will this make me look?","body_22")
    call her_main("I will know for sure when we get the results though...","body_23")
    call her_main("Yes, I'm sure everyone else failed as well...","body_13")
    call her_main("I mean, they must have, right?","body_11")
    call her_main(".....................","body_13")
    call her_main("....right?","body_11")
    menu:
        "{size=-3}\"Of course. You are a top student after all.\"{/size}":
            call her_main("Exactly...","body_09")
            her "Or at least I used to be until today..."
            call her_main("I cannot believe this is happening!","body_20")
        "{size=-3}\"You could get smarter if I tutor you.\"{/size}":
            $ tutoring_offer_made = True #Affects conversation in the next event.
            call her_main("hm...","body_17")
            call her_main("Yes, that could help I suppose...","body_13")
            call her_main("I appreciate your offer, professor, but...","body_14")
            her "May I think about it?"
            m "Don't take too long..."
        "{size=-3}\"I suppose we'll know soon enough.\"{/size}":
            call her_main("Yes, I suppose we will...","body_15")

    call her_main("I'm sorry, professor, I'm probably just overreacting anyway...","body_24")
    call her_main("But you must understand that my reputation is at stake here!","body_14")
    call her_main("There's gotta be something wrong with the test...","body_12")
    her "And although I failed I probably still got the most points in the test..."
    her "As usual..."
    call her_main("Well I'd better go now. We have another \"MRM\" meeting today.","body_04")
    her "I will let you know about the new ideas we will come up with tonight."
    m "I can hardly wait..."



    hide screen bld1
    hide screen hermione_main
    with d3
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with d3
    pause.5
    
    $ event12_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    return #call day_start

###(NIGHT) HERMIONE DID FAIL A TEST [BREAKDOWN] - IN USE
label event_13: 
    #"EVENT_13"
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    show screen hermione_blink #Hermione stands still.
    with d3
    
    her "....................."
    m "???"
    her "............"
    m "Miss Granger?" 
    her "..............................."
    m "Miss Granger?!!" 
    show screen bld1
    with d3
    call her_main("","body_26")
    show screen ctc
    pause
    her "Huh?"
    hide screen ctc
    her "Oh, I am already here?"
    her "I'm sorry sir... I..."
    her ".................."
    her "It seems that I did..."
    her "I did... uhm..."
    her "... I failed that test after all."
    her "I..."
    call her_main("I am sorry, professor...","body_27")
    her "I'm not sure why I am here..."
    her "I think I'd better go..."
    m "..................."
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=610+140 #Coordinates of it's movement. (To)
    $ hermione_speed = 01.0 #The speed of moving the walking animation across the screen.
    hide screen bld1
    with d3
    show screen hermione_run

    pause.9
    hide screen hermione_run
    with Dissolve(.3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
  
    pause.3
    m "............."
    m "She will be alright..."
    m "I think..."
    
    
    
    
    
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_SC.chibi.xpos = 400 #Middle of the room.
#    show screen hermione_stand_f #Hermione stands still.
#    with d3
#    her "................."
#    $ walk_xpos=400 #Animation of walking chibi. (From)
#    $ walk_xpos2=510 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f 
#    pause 2
#    hide screen hermione_walk_01_f 
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    $ hermione_SC.chibi.xpos = 500 #Middle of the room.
#    show screen hermione_stand_f #Hermione stands still.
#    with Dissolve(.3)
#    her "................"
    
#    $ walk_xpos=500 #Animation of walking chibi. (From)
#    $ walk_xpos2=610 #Coordinates of it's movement. (To)
#    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
#    show screen hermione_walk_01_f 
#    pause 2
#    hide screen hermione_walk_01_f 
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
#    with Dissolve(.3)
#    pause.5



    $ event13_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    return#call day_start

###(DAY) HERMIONE APOLOGIES FOR BREAKDOWN [START TUTORING] - IN USE
label event_14: 
    #"EVENT_14"
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    show screen hermione_blink
    with d3
    
    show screen bld1
    with d3
    
    call her_main("Good morning, Professor.","body_01",xpos=370,ypos=0)
    m "How can I help you today, miss Granger?"
    call her_main("Well, first of all I am terribly sorry about yesterday's display, sir...","body_04")
    call her_main("I never failed a test in my life, so I wasn't sure how to react...","body_08")
    call her_main("But I am all better now...","body_04")
    m "I see..." 
    her "I will not take much of your time, I promise..."
    if tutoring_offer_made:
        her "I am here to take you up on your offer."
        menu:
            "\"What offer?\"":
                her "A while back you offered to tutor me, sir..."
                menu:
                    "\"Oh... That offer has expired.\"":
                        call her_main("It...","body_14")
                        her "Expired, sir?"
                        her "B-but...."
                        call her_main("But I require tutoring, and you are the smartest wizard I know...","body_11")
                        call her_main("Please, sir, I really need your help.","body_28")
                        menu:
                            "\"Show me your tits and it's a deal!\"":
                                call her_main("m-my...?","body_18")
                                call her_main("............","body_29")
                                her "....."
                                with hpunch
                                call her_main("{size=+5}Professor Dumbledore!!!{/size}","body_30")
                                m "{size=-5}(Well, at least I tried...){/size}"
                                her "I am not some \"Slytherin\" floozy!"
                                m "Of course not, miss Granger."
                                m "It was a test... You passed. Good job."
                                call her_main("What...?","body_31")
                                call her_main("Oh, of course. I'm so silly sometimes. Sorry about the yelling, sir.","body_24")
                                m "My offer is still valid. If you want me to then I can tutor you."
                                call her_main("..............","body_29")
                            "\"Well, alright, alright...\"":
                                pass
                    "\"Oh, that's right. Great.\"":
                        pass

            "\"Splendid! Starting today?\"":
                pass
    else:
        call her_main("I... uhm...","body_07")
        her "Sir Dumbledore, I hope this is not too much to ask..."
        m "Yes?"
        her "Ehm... would it be alright if..."
        her "..............."
        call her_main("do You think you could tutor me a little, sir?","body_09")
        menu:
            "\"I suppose that is possible\"":
                pass
            "\"Hm... I'm quite busy actually.\"":
                call her_main("Sir, please, you are the smartest wizard I know!","body_11")
                m "{size=-4}(You have no idea, little witch.){/size}"
                m "Well, it could be arranged, I suppose..."
    call her_main("Thank you, sir. I am very grateful.","body_01")
    call her_main("Just let me know when, and I will bring my books!","body_16")
    call her_main("I must study even harder from now on...","body_09")
    call her_main("And I'll be taking private lessons from you sir, as often as possible.","body_06")
    call her_main("But that's not all...","body_07")
    her "The \"MRM\" shall investigate our education system much closer now..."
    her "I think some sort of foul-play might be taking place..."
    m "No way!"
    her "I have a list of suspects already but I will get back to you on this later...."
    m "Ehm... alright..."
    call her_main("Oh, the classes are about to start. I'd better go...","body_10")
    
    hide screen bld1
    hide screen hermione_main
    with d3
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with d3
    pause.5
    
    stop music fadeout 1.0

    $ event14_happened = True #Allows next event to start.
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    ">You unlocked an ability to summon Hermione Granger to your office."
    hide screen blktone
    with d3
    $ summoning_hermione_unlocked = True #Unlocks after event_14. Adds "Summon Hermione" button to the door.
    $ hermione_takes_classes = True
    $ tutoring_hermione_unlocked = True
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1

    return

###() HERMIONE ASKS TO BUY POINTS [START FAVOURS]
label event_15: 
    
    #"EVENT_15"
    
#    $ slytherin +=49
#    hide screen s_p_u
#    $ s_p_u_pic = "what_49_points"
#    show screen s_p_u
    
    $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
    "*Knock-knock-knock!*"
    menu:
        "\"Who is it?\"":
            her "It's me, Hermione Granger." 
            m "(It's that young witch again...)" 
            her "Can I come in, sir?"
            menu:
                m "..."
                "\"Absolutely not! I'm busy! Come back later!\"":
                    her "But..."
                    her "Alright... I will come back tomorrow then..."
                    return
                "\"Of course. Come on in.\"":
                    pass
        "\"I'm busy. Come back later.\"":
            her "But..."
            her "Well, alright..."
            return
        "\"Yes, come in.\"":
            pass
        "\"...................................\"":
            $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
            "*Knock-knock-knock!*"
            m "............................."
            her "Professor, I'm coming in..."
            m "{size=-4}(Crap!){/size}"
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    show screen hermione_blink
    with d3
    
    call her_main("Good evening, professor...","body_13",xpos=370,ypos=0)
    her "........................"
    call her_main("........................","body_29")
    her "........................"
    call her_main("Ehm......","body_31")
    call her_main(".................","body_29")
    m "What is it, miss Granger?"
    call her_main("Well, ehm...","body_31")
    her "You see... The \"Gryffindor\" house is not in the lead anymore..."
    call her_main("And... everyone is working so hard...","body_29")
    her "And they look up to me for help but I don't know what to do..."
    m "............................"
    her "Professor Dumbledore...."
    stop music fadeout 2.0
    call her_main("I want you to buy a favour from me!","body_32")
    call her_main("","body_33")
    menu:
        "\"You mean like a sexual favour?\"":
            call her_main("Ehm... I'm not sure...","body_34")
            her "The kind that would gain our house additional points..."
            call her_main("I could write an essay for you or...","body_31")
            call her_main("Or maybe clean your tower..?","body_34")
            m "{size=-4}(Clean my tower? Heh... There's gotta be dirty joke in there somewhere...){/size}"
            m "Well, alright then, I think we can figure something out."
        "\"Well, if you insist...\"":
            pass
        "\"I don't think so, miss Granger.\"":
            call her_main("B-but... We need the points...","body_31")
            her "Professor, please, I am really desperate..."
            m "Desperate you say..?"
            m "Well alright..."
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    call her_main("Thank you, professor...","body_01")
    
    label choose_favor_agagin:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    her "So... What will it be?"
    menu:
        "\"Show me your tongue...\"":
            $ d_flag_01 = True
            pass
        "\"Stand there. Let me look at you.\"":
            $ d_flag_02 = True
            pass
        "\"Make a silly face...\"":
            $ d_flag_03 = True
            pass
        "\"Say \"I've been a bad girl\".\"":
            $ d_flag_04 = True
            pass

    her "Em..."
    her "How many house points will I get for that...?"
    
    $ current_payout = 0
    menu:
        "\"1 point.\"":
            if d_flag_02: #STAND THERE
                $ current_payout = 1
            else:
                her "I don't think it's worth it then..."
                jump choose_favor_agagin
        "\"10 points.\"":
            if d_flag_02: #STAND THERE
                $ current_payout = 10
            else:
                her "I don't think it's worth it then..."
                jump choose_favor_agagin
        "\"20 points.\"":
            $ current_payout = 20
            her "So little...?"
            pass
        "\"40 points.\"":
            $ current_payout = 40
            pass
    
    call her_main("Em, alright...",xpos=140)
    if d_flag_01: #SHOW TONGUE
        call her_main("M-my... tongue, sir?","body_24")
        m "Yes, girl, open your mouth and show me your tongue."
        call her_main("{size=-7}(What a weirdo...){/size}","body_12")
        call her_main("Ehm... well, alright then...","body_07")
        call her_main("Here...","body_08")
        call her_main(".............","body_35")
        her "............."
        call her_main(".................","body_36")
        show screen ctc
        pause
        menu: 
            "\"Very good. Here are your points.\"":
                pass
            "\"Not good enough. You can do better\"":
                call her_main("...............","body_12")
                her "Alright, I will try to do better, sir..."
                call her_main("How about this?","body_11")
                call her_main("A-a-ah..................","body_37")
                call her_main("............................","body_38")
                call her_main("......................................","body_39")
                her "..................................................."
                her "...................................................................."
                call her_main(".......................................................................................................","body_40")

    if d_flag_02: #STAND THERE
        call her_main("So, I just have to stand here then...?","body_06")
        m "Good... Now turn around... slowly."
        her "uhm... alright..."
        hide screen hermione_main
        hide screen bld1
        with d3
        pause.5
        show screen hermione_stand_f #Hermione stands still.
        with Dissolve(.7)

        call her_head(".................................","head_exp/2")
        menu:
            m "Hm..."
            "\"The uniform suits you, miss Granger...\"":
                call her_head("............","head_exp/1")
                call her_head("Thank you, professor Dumbledore...","head_exp/5")
            "\"You have a nice body, miss Granger...\"":
                call her_head("!!?","head_exp/3")
                call her_head("..............","head_exp/4")
                call her_head("Thank you, professor...")
            "\"That's enough. Here are your points...\"":
                show screen hermione_stand #Hermione stands still.
                with Dissolve(.7)
                pause.5
                show screen bld1
                with d3
                jump stupid_enogh
        
        m "Very good, you can turn back now..."
        show screen hermione_stand #Hermione stands still.
        with Dissolve(.7)
        pause.7
        show screen hermione_main
        show screen bld1
        with d3
        her "................."
    
#    if d_flag_02: #Pretend to be a monkey.
#        her "A monkey then..."
#        her "ooh ooh...."
#        her "ooh ooh ooh...."
#        m "Good, but you can do better..."
#        her "ooh ooh ooh...."
#        her "ooh ooh ooh... eee eee eee aah aah aah..."
#        m "Very well..."
    
    if d_flag_03: #STUPID FACE
        call her_main("A silly face then...","body_24")
        her "Let's see..."
        label stupid_faces:
        call her_main("How about this one?","body_41")
        menu:
            "\"Good! Very stupid! I mean, silly.\"":
                jump event_15_done
            "\"Not stupid enough.\"":
                pass
        call her_main(".........","body_12")
        call her_main("What about this one then?","body_43")
        menu:
            "\"Ha-ha! You look like an idiot!\"":
                jump event_15_done
            "\"No, not stupid enough.\"":
                pass
        call her_main(".........","body_12")
        call her_main("What if I do it like this?","body_42")
        menu:
            "\"Good! Very stupid.\"":
                jump event_15_done
            "\"Not stupid enough.\"":
                jump stupid_faces
    
    if d_flag_04: #BAD GIRL
        call her_main("I...","body_07",xpos=140)
        her "I have been a very bad girl..."
        g9 "Have you been a very, very, very bad girl?"
        her "Yes, sir..."
        her "I have been very, very, very, very bad..."
        label to_early_for_sucking_cocks:
        menu:
            g9 "..."
            "\"Do you need to be punished?\"":
                call her_main("Do I need to... be punished?","body_11")
                call her_main("Ehm...","body_13")
                her "....................."
                call her_main("Well, I am not perfect, if that's what you mean, sir...","body_12")
                call her_main("But do I need to be punished... hm?","body_13")
                call her_main("Is this really for me to decide...? I mean...","body_07")
                her "What does this have to do with anything?"
                m "You are overanalyzing this, girl."
                m "Just say that you need to be punished!"
                call her_main("Fine. I need to be punished!","body_05")
                call her_main("{size=-5}(And I truly do think so sometimes...){/size}","body_33")
                m "That's a good girl."
                call her_main("................??","body_44")
                m "Now that wasn't hard at all, was it?"
                call her_main("n-no , sir...","body_29")
                m "Alrighty, then..."
            "\"Do you want to get spanked?\"":
                call her_main("Do I want to...","body_11")
                call her_main("Get s-spanked??","body_18")
                call her_main("Tsk!","body_05")
                call her_main("Professor, I don't think I'm comfortable with--","body_04")
                m "My bad, let me rephrase the question..."
                m "How badly do you need those points?"
                call her_main("..................","body_09")
                call her_main("Yes, sir. I do need to get spanked.","body_04")
                m "Alright, that's good enough for now..."
                call her_main("{size=-4}(For now?){/size}","body_07")
            "\"Come here and suck my cock!\"":
                m "{size=-5}(Too early for this... I need to reel her in first.){/size}"
                jump to_early_for_sucking_cocks
    
    label event_15_done:
    m "[current_payout] points to the \"Gryffindor\" house."
    $ gryffindor += current_payout
    
    call her_main("Yay!..............","body_24",xpos=140)
    her "This was quite easy..."
    her "You think you could buy some more favours from me in the future, professor?"
    menu:
        "\"I don't think that's a good idea.\"":
            call her_main("Please, professor...","body_28")
            her "We really need those points..."
            m "......."
            call her_main("You are an esteemed wizard and to be honest...","body_29")
            her "The only person in this school whom I don't mind asking for this..."
            m "Well, when you put it that way..."
        "\"That's a possibility...\"":
            pass
            
    call her_main("Thank you professor. Thank you so much.","body_06")
    call her_main("Well, I suppose, I'd better go now...","body_01")
    m "............"

    hide screen bld1
    hide screen hermione_main
    with d3
    
    call her_walk(400,610,2)
    
    show screen hermione_stand_f #Hermione stands still.
    with d3

    if d_flag_01: #Show me your tongue
        her "{size=-4}(Hm...){/size}"
        her "{size=-4}(Students show teachers their tongues all the time...){/size}"
        her "{size=-4}(Although that's usually when the teacher is not looking...){/size}"
        her "{size=-4}(But there is nothing wrong with what I did today...){/size}"
        her "{size=-4}(I earned my house extra points...){/size}"
    if d_flag_02: #Stand still...
        her "{size=-4}(I can just stand there and let the professor look at me...){/size}"
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}"
#        her "{size=-4}(ooh ooh ooh... eee eee eee aah aah aah...){/size}"
#        her "{size=-4}(I'm a monkey... I'm a money... I need to practice more...){/size}"
    if d_flag_03:
        her "{size=-4}(Stupid face...){/size}"
        her "{size=-4}(Stupid face...){/size}"
        her "{size=-4}(I need to practice this.){/size}"
    if d_flag_04:
        her "{size=-4}(I'm a bad girl...){/size}"
        her "{size=-4}(I am very bad...){/size}"
        her "{size=-4}(Yes, I can say things like that easily...){/size}"
        her "{size=-4}(There is nothing wrong with that... nothing at all...){/size}"
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen hermione_stand_f #Hermione stands still.
    with d3
    stop music fadeout 1.0
    
    show screen blktone
    with d3
    show screen notes
    $ renpy.play('sounds/win2.mp3') 
    ">You unlocked an ability to buy sexual favours from Hermione Granger."
    hide screen blktone
    with d3
    
    $ buying_favors_from_hermione_unlocked = True 
    $ days_without_an_event = 0 #Resets the counter. This counts how many days have passed since this event happened.
    $ event15_happened = True #Turns TRUE after event_15
    jump day_start
    
    
    
    
#### LEGACY/UNUSED EVENT ####
label event_04: # NOT IN USE
    m "Well, it's been three days now..."
    m "I wonder what has become of that two-faced dude?"
    return

    
init python:
    class wt_silver_event(object):
        day_wait = 0
        completed = False
        
        
    
    
    
    
    
