label shaming:
    hide screen hermione_main
    with d3
    m "{size=-4}(Should I...){/size}"
    menu:
        "\"(Fuck it, what's the worst that could happen.)\"":
            pass
        "\"(I'd rather not risk it)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 

    hide screen hermione_main
    with d3
    $ h_body = "01_hp/13_hermione_main/shaming/0100.png"
    show screen hermione_main

    m "Miss Granger."
    her "Yes, Professor?"
    m "I want you to return to my room after hours..."

    if shaming == 0:

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0200.png"
        show screen hermione_main

        her "But Sir!"
        her "That's against school rules."
        m "I'm sure you're talented enough to get here unnoticed."
        her "..."

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0300.png"
        show screen hermione_main

        her "I refuse sir. I don't want to think what would happen if I ran into a teacher."
        m "Not even for... 100 house points?"

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0400.png"
        show screen hermione_main

        her "!!!"

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0500.png"
        show screen hermione_main        

        her "That's a lot of points..."
        her "Those slytherin wenches would be astonished when they wake up."
        her "I-"

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0600.png"
        show screen hermione_main        

        her "Fine, i'll do it."
        m "Fantastic!"
        m "Well then, miss Granger, I'll see you tonight."
        $ shaming_busy = True
    else:

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0700.png"
        show screen hermione_main        

        her "..."
        m "..."

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/0800.png"
        show screen hermione_main        

        her "..."
        m "..."
        "this might have been a bad idea."
        if whoring >20:

            hide screen hermione_main
            with d3
            $ h_body = "01_hp/13_hermione_main/shaming/0900.png"
            show screen hermione_main        
        
            her "...Okay."
            "!!!"
            m "(I can't believe it!)"
            m "(What a slut.)"
            m "Fantastic!"
            m "Well then, miss Granger, I'll see you tonight."
            $ shaming_busy = True
        else:
            jump too_much



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
    jump day_main_menu  

label shaming_night:

    $ walk_xpos=520 #Animation of walking chibi. (From)
    $ walk_xpos2=400 #Coordinates of it's movement. (To)
    $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    show screen hermione_chibi_robe 
    with d4
    pause 1.7 
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=320
    $ h_ypos=0
    $ ne = False


    if shaming == 0: #First time this event taking place.
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/1000.png"
        show screen hermione_main        

        m "Good evening, Miss Granger."
        her "Good evening, Professor."
        her "So what do you want me to do?"
        m "It's nothing special."
        m "First of all, please take off your robe."
        her "Of course, Sir."

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/1100.png"
        show screen hermione_main      

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/1200.png"
        show screen hermione_main      

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/1300.png"
        show screen hermione_main   

        m "..."
        m "..."
        her "What's this strange feeling?"
        m "Nothing, dear."
        ">you take out your cock and start rubbing it."

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen g_c_u
        show screen desk
        show screen desk_02


        if whoring < 15:

            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/shaming/1400.png"
            show screen hermione_main   

            her "P-Professor?!"
            her "What are you doing?"
            m "Stroking my dick."

            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/shaming/1500.png"
            show screen hermione_main   

            her "Professor I'm really not comfortable with you jerking off in front of me..."
            m "I don't care."
        else:

            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/shaming/1600.png"
            show screen hermione_main   

            "Hermione notices what you are doing."
            "But she doesn't object."
        m "You see, Miss Granger..."
        m "You have been an absolute tease towards me over the past few weeks..."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/1700.png"
        show screen hermione_main   

        her "...?"
        m "Prancing about the school, pretending to be a pure and innocent pupil."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/1800.png"
        show screen hermione_main   

        her "Professor?"
        m "But once you're behind my door, you turn into nothing more than a filthy whore!"
        m "Doing whatever I want, as long as you get some house points in return."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/1900.png"
        show screen hermione_main   

        her "!!!"
        m "Whores like you should be punished!"
        m "I'm going to use you as my cumbucket."
        ">Hermoine is fuming."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2000.png"
        show screen hermione_main   

        her "oh yeah?"
        her "I'm just gonna leave."
        m "Go ahead, try."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2100.png"
        show screen hermione_main   

        her "..."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2200.png"
        show screen hermione_main   

        her "!!!"

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2300.png"
        show screen hermione_main    
               
        her "what's going on?"
        m "I cast a simple binding spell just a couple of minutes ago."
        m "Try as you might you won't be able to leave."
        m "Now, miss Granger,"
        m "Please take off your shirt."

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2400.png"
        show screen hermione_main   
        show screen ctc
        pause 

        her "..."
        ">hermoine stares at you with a look that could burn holes through walls."

        hide screen hermione_main
        
        hide screen hermione_02
        show screen hermione_04
        
        $ h_body = "01_hp/13_hermione_main/shaming/2500.png"
        $ only_upper = True
        $ badges = False
        show screen hermione_main   
        pause

        m "Oh yeah look at those perfect titties..."
        m "All the way off, miss Granger."
 
        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2600.png"
        show screen hermione_main   

        hide screen hermione_04
        $ hermione_chibi_xpos = 400
        #$ hermione_chibi_ypos = 0
        $ h_c_u_pic = "01_hp/08_animation_02/03_no_shirt_01.png"
        show screen h_c_u

        ">She throws the shirt on your desk."
        m "Now the panties, Miss Granger"

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/2700.png"
        show screen hermione_main   

        her "No."
        m "Excuse me?"

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/2800.png"
        show screen hermione_main   

        her "I refuse."
        m "If you think that will stop me, you've got the wrong idea, slut."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/2900.png"
        show screen hermione_main   
        
        show screen ctc
        pause 

        ">You conjure up some pink fluffy cuffs and bind Hermione's hands together."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/3000.png"
        show screen hermione_main   

        her "P-P-Professor!"
        her "This is too much!"
        her "You must stop this."
        m "I mustn't do anything, miss Granger, I'm the headmaster of this school."
        m "I'm in complete control of this situation, and you're powerless!"
        m "Immobilized in my room, with practically every person in the castle asleep."
        m "I'm going to enjoy this..."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/3100.png"
        show screen hermione_main   

        "You reach under her skirt."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/3200.png"
        show screen hermione_main   
        
        show screen ctc
        pause 

        "and slowly pull down her panties."
        "You use the opportunity to slide a finger across Hermione's pussy"
        if whoring > 12:
            "You notice that your finger is a bit damp"
        elif whoring > 20:
            "you notice that your finger is surprisingly sticky"
        her "p-p-p..."
        m "?"

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/3300.png"
        show screen hermione_main   

        her "p-please stop professor."
        her "I beg you..."
        her "I'll behave."
        her "Just let me go and I'll behave."
        her "I'll do whatever you want just let me go."
        m "No way."
        m "It's too late for that."
        "With a quick tug you tear off her skirt"

        if whoring > 20:
            "For a second you thought you could hear a low moan."
            "But Hermione's face still looks distressed."

        hide screen h_c_u
        $ hermione_chibi_xpos = 400
        #$ hermione_chibi_ypos = 0
        $ h_c_u_pic = "01_hp/08_animation_02/07_dance_01.png"
        show screen h_c_u

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/3400.png"
        show screen hermione_main   
        show screen ctc
        pause         


        "Hermione starts sobbing."


        "You resume jerking your cock."
        ">hermione is glancing at your dick."
        her "Please Professor, I'll do anything, just don't do this to me."
        m "Keep your mouth shut, wench."
        
        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/3600.png"
        show screen hermione_main   
        show screen ctc

        her "!!!"
        her "MMHHHM!! MHHHMMMH!"
        m "much better"

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/3700.png"
        show screen hermione_main   

        "Tears are running down Hermione's cheecks."
        m "This is perfect"
        m "I'm going to..."

        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/3800.png"
        show screen hermione_main   
        pause .1
        hide screen white
        with hpunch

        $ genie_cum_chibi_xpos = 5
        $ genie_cum_chibi_ypos = 10
        $ g_c_c_u_pic = "genie_cum_03"
        show screen g_c_c_u
        show screen ctc
        pause 
        hide screen g_c_c_u


        m "AHHHhhhhh"

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/3900.png"
        show screen hermione_main   

        "Hermione is still sobbing."
        "You are instantly rock hard again"
        if whoring > 22:
            "You notice that she seems to be rubbing her thighs together."

        m "You fucking slut"
        m "This is your destiny"

        hide screen hermione_main
        
        $ h_body = "01_hp/13_hermione_main/shaming/4000.png"
        show screen hermione_main 

        m "My personal cumbucket"
        m "It's coming..."

        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/4100.png"
        show screen hermione_main   
        pause .1
        hide screen white
        with hpunch

        $ genie_cum_chibi_xpos = 5
        $ genie_cum_chibi_ypos = 10
        $ g_c_c_u_pic = "genie_cum_03"
        show screen g_c_c_u
        show screen ctc
        pause 
        hide screen g_c_c_u

        m "HAaaahh"
        m "That did the trick"

        hide screen g_c_u
        $ genie_chibi_xpos = 290
        $ genie_chibi_ypos = 250
        $ g_c_u_pic = "01_hp/05_props/walk_03.png"
        show screen g_c_u


        "Hermione is looking pretty lifeless"
        m "..."
        m "(Oh dear)"
        m "(I might have overdone it a little)"

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/4200.png"
        show screen hermione_main 

        "You take off the gag"
        m "One Hundred House points for Gryffindor"
        $ gryffindor +=100
        her "..."
        m "You can go now, Miss Granger"
        if whoring < 5:
            her "..."
            m "wait, don't you need to..."
            "Hermione leaves"
            m "yeah I definitely overdid it"
            m "I hope she's okay..."

            $ shaming_clothed = False
            $ mad = +50

        elif whoring < 15:
            her "I trusted you, Professor!"
            m "What's wrong, Didn't I just give you a shitload of points in return?"
            m "I'd be glad if I were you..."
            "Hermione grabs her robe."

            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/shaming/4300.png"
            show screen hermione_main  
            show screen ctc
            pause 

            "And leaves after shooting a nastly look towards you."

            $ shaming_clothed = True

            $ mad = +15

        else:

            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/shaming/4400.png"
            show screen hermione_main 

            her "Thanks, Professor"
            m "You suddenly look awefully cheerful."
            m "Weren't you..?"
            her "Oh please Professor."
            her "I was just playing along."
            her "I realized what you were up to the moment you cast that binding spell."
            her "...Gryffindor needs the points after all."
            m "..."

            menu:
                "-Punish her arrogance-":
                    "With a swing of your hands, Hermione's clothes disappear from your desk"

                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/shaming/4700.png"
                    show screen hermione_main 

                    her "!!!"
                    her "Where have my clothes gone??"
                    m "I teleported them back to your room"
                    
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/shaming/4800.png"
                    show screen hermione_main 

                    her "But I can't go back looking like this?!"
                    m "Oh I'm sure you can."
                    m "Everybody is fast asleep, the only one that might see you is Peeves, and you can hear him coming from a mile away."
                    her "But Professor!"
                    m "OHMYGOD IS IT THIS LATE ALREADY!"
                    m "I've got important things to do, goodbye miss Granger."
                    "You quickly shove her out of the door and lock it."

                    hide screen hermione_main
                    hide screen h_c_u


                    "Hermione is kicking the door."
                    her "Professor, please let me back in."
                    her "I don't want to be found like this."
                    m "Well you better hurry back to your room then, miss Granger."
                    m "..."
                    m "..."
                    "You hear Hermione dashing away..."
                    $ shaming_clothed = False
                    $ mad = +10

                "-That's enough for one night-":
                    "You take off the cuffs."
                    m "cover yourself and go to bed, tomorrow is another day"

                    hide screen hermione_main
                    
                    $ h_body = "01_hp/13_hermione_main/shaming/4600.png"
                    show screen hermione_main 
                    
                    show screen ctc
                    pause 
                    $ shaming_clothed = True

        $ shaming_01 = True
        $ shaming_busy = False    

        hide screen g_c_u
        hide screen desk
        hide screen desk_02
        show screen genie

        if shaming_clothed:
            $ walk_xpos=400 #Animation of walking chibi. (From)
            $ walk_xpos2=610 #Coordinates of it's movement. (To)
            $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
            show screen hermione_chibi_robe_f 
            pause 2
            hide screen hermione_chibi_robe_f


    else:  
        # "Hermione's face is noticably flushed."
        # "An awkward silence falls"
        # m "So uhhhh..."
        # m "...How are the prom preparations?"
        # m "(Why does she keeps fiddling with her robe...)"
        # her "Everything is progressing smoothly..."
        # m "That's nice..."
        # her "..."
        # m "..."
        # her "Should I undress, Professor?"
        # m "But of course, Miss Granger."
        # her "..."

        # m "!!!"
        # m "Whoa..."
        # m "Where did you get that from?"
        # her "Oh this?"
        # her "It's Ginny Weasley's, Apparently Harry is into these kind of things."
        # her "I 'persuaded' her to let me borrow it for a night."
        # her "Do you like it?"
        # m "I fucking LOVE it!"
        # m "Why did you though?"
        # her "I wanted to reward you for everything you've done for me."
        # her "No house points involved, just you and me..."
        # her "My body is yours for the rest of the night."

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/6000.png"
        $ h_xpos=320
        $ h_ypos=0
        $ only_upper = True
        $ badges = False
        $ ne = False
        show screen hermione_main        

        m "Good evening, Miss Granger."
        her "Good evening, Professor."
        m "..."
        her "..."
        "An awkward silence falls"
        m "(This is bizarre. What’s with the eyes and the robe? Did I tell her to go get gang-banged by the slytherin house and forget?)"
        m "Uh… Why are you here? I don’t remember asking for you."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/6100.png"
        show screen hermione_main

        her "I came to see you."
        m "That's nice..."
        her "..."
        m "...Are you feeling alright?"
        her "Yes, I feel fine."
        m "Then why are you just standing there with that look on your face?"
        her "Do you wish something of me?"
        m "I think you have that backwards."
        her "What?"
        m "Nevermind. Take that ridiculous robe off."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/6200.png"
        show screen hermione_main
        with d3

        "Hermione peels off her robe to expose a very revealing sling bikini."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/6300.png"
        show screen hermione_main
        hide screen hermione_02_b
        $ hermione_chibi_xpos = 400
        #$ hermione_chibi_ypos = 0
        $ h_c_u_pic = "01_hp/08_animation_02/07_dance_01.png"
        show screen h_c_u
        show screen ctc
        pause

        m "Miss Granger?"
        her "Yes sir?"
        m "Why are you dressed like a whore?"
        her "Because I am a whore sir."
        m "I know you are, but this is…"
        her "Do you like it?"
        m "I do, actually. Where did you get it?"
        her "It was a gift from my master."
        m "I don’t remember getting you that."
        her "Oh no sir, it was a gift from my master."
        m "You have another master? I know you’re a slut, but that seems quite out of character."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/6400.png"
        show screen hermione_main

        her "I am a slut sir, a filthy bitch. Make me your cock-puppet and fuck my throat."
        m "(Woah. I think I broke her. Hang on, what’s this?)"

        "Peeking out from behind the bikini is the edge of a tattoo just below her waist"

        m "Miss Granger, pull aside your bikini for me."
        her "Yes sir."

        "Hermione pulls the top of the bikini open to reveal her breasts to Genie"

        m "Not your tits you silly bitch, your cunt."
        her "Oh god, yes sir, tell me what a filthy fuck-toy I am."


        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/6600.png"
        show screen hermione_main
        pause
        "Hermione reveals her dripping wet pussy with a rapturous expression on her face."

        m "(Ah… It’s all beginning to make sense… Someone has inscribed Miss Granger with a magical tattoo, and probably put a few other spells on her as well… "
        m "Probably someone from Slytherin house, but that’s just a wild guess. I should get Severus in here and see if he knows anything about it.)"
        m "Miss Granger, put your robe back on and fetch Professor Snape."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/6700.png"
        show screen hermione_main

        her "Don’t you want to fuck me first?"
        m "…"
        her "Please?"
        m "Just go get Snape and don’t act like a massive whore until I tell you to."
        her "Yes Professor."

        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/shaming/6800.png"
        show screen hermione_main
        show screen ctc
        pause
        hide screen hermione_main

        "Hermione redresses and leaves your chambers. A few minutes later Hermione returns with Snape close behind her."

        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=610 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        show screen hermione_chibi_robe_f 
        pause 2
        hide screen hermione_chibi_robe_f

        pause

        $ walk_xpos=520 #Animation of walking chibi. (From)
        $ walk_xpos2=400 #Coordinates of it's movement. (To)
        $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        show screen hermione_chibi_robe
        with d4
        pause 1.7 
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02_b #Hermione stands still.
        pause.5
        show screen bld1
        with Dissolve(.3)

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/24.png"
        show screen snape_main

        sna "Hello 'Albus'… You called for me."
        m "Hello Snape, someone’s put a curse on Miss Granger."
        sna "Hm. A pity it wasn’t me. Why do you need me? I’ve seen your magic at work, you could easily remove a simple mind altering hex."
        m "I could, but I was hoping you could help me discover who the culprit is."
        sna "I suppose, but only for the sake of our friendship. Personally, I like this subservient side of Miss Granger."
        m "You’ll love this then. Miss Granger, show Professor Snape your new tattoo."

        "Without a complaint, Hermione eagerly sheds her robe and pulls her bikini aside to reveal a massive dildo shaped like a dog’s dick lodged in her snatch."

        hide screen hermione_main
        $ h_xpos = 280
        $ h_body = "01_hp/13_hermione_main/shaming/6900.png"
        hide screen hermione_02_b
        $ hermione_chibi_xpos = 400
        #$ hermione_chibi_ypos = 0
        $ h_c_u_pic = "01_hp/08_animation_02/07_dance_01.png"
        show screen h_c_u
        show screen hermione_main
        pause 

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/snape_11.png"
        show screen snape_main

        sna "I…Wha…Genie…is this a joke?"
        m "Miss Granger, I told you not to act like a massive whore until I told you to."
        her "I tried sir, but I ran into Master Malfoy on the way to fetch Professor Snape, and…well…"
        m "Well that solves it. Snape… Snape?"
        sna "…"
        m "Snape!"

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/snape_03.png"
        show screen snape_main    
           
        sna "This is an illusion. It must be."
        m "No illusion Severus. It appears this Malfoy character has put a few spells on Miss Granger, turned her into a cock hungry zombie, and then shoved a dog dick inside her. Kids these days."
        sna "I…"
        m "Oh snap out of it Severus. This kind of thing happens all the time in Akabur games."
        a4 "Don’t drag me into this."

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/snape_05.png"
        show screen snape_main  

        sna "What on earth was that?"
        m "Just ignore him. Now, tell me a bit about this Malfoy character."

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/24.png"
        show screen snape_main   

        sna "Draco Malfoy. He’s the son of a rather prominent ex-death-eater, and a dear friend of mine. A good student, if not rather… mischievous."
        m "And a man of good taste it seems. Perhaps we can let him in on this little plan of ours so he doesn’t ruin it for everyone."
        sna "An excellent idea. Malfoy’s ability to keep secrets is unrivaled. Well then, what shall we do with her?"
        m "Well, my guess is she won’t remember anything that happens here tonight. Why don’t we have her put on a show?"
        sna "And to think, I tried to kill you once."
        m "Funny how things work out. Miss Granger, put that dildo on the table please."
        her "Of course Professor."

        "Hermione tugs at the dildo, to find it lodged deeply inside her."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/7000.png"
        show screen hermione_main

        her "Professor… I think it’s stuck…"
        m "Well pull harder girl."
        her "Oh god… I can feel it… AH!"


        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/7100.png"
        show screen hermione_main
        pause

        "With an audible pop the dildo rockets out of Hermione’s slit. She falls to the ground and starts convulsing."

        hide screen snape_main
        hide screen hermione_02
        $ hermione_chibi_xpos = -20
        $ hermione_chibi_ypos = 75
        $ s_sprite = "01_hp/10_snape_main/snape_26.png"
        $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
        show screen h_c_u
        show screen snape_main   

        sna "My god, is she dying?"
        m "No, she’s just cumming. Do you mind if I jerk off?"

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/snape_20.png"
        show screen snape_main   
        sna "Not at all, I think I’ll join you."

        hide screen genie
        $ genie_chibi_xpos = 0
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        $ snape_chibi_xpos = -20
        $ snape_chibi_ypos = 10
        $ s_c_u_pic = "jerking_off_03_ani" #Snape.
        show screen chair_02
        show screen g_c_u
        show screen s_c_u
        show screen desk_02
        hide screen blkfade

        hide screen hermione_main
        hide screen snape_main

        "Genie and Snape jerk off over Hermione. From the look on her face she is nearly catatonic with excitement."


        hide screen hermione_main
        $ h_xpos=390 
        $ h_ypos=150
        $ h_body = "01_hp/13_hermione_main/shaming/7200.png"
        show screen hermione_main

        her "Please…Please let me taste them…"
        "Without waiting, Snape grabs Hermione by the hair and rams his cock down her throat."

        m "That’s the spirit, but I was hoping to hear her beg more."
        sna "Ha! I have an idea. Oh Miss Granger, you stuck up, know it all, cock gobbling whore."
        her "Mys?"

        sna "Beg for cock as I fuck your slutty little throat."



        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/7300.png"
        show screen hermione_main

        "Tears begun streaming down her face as Hermione struggles to enunciate her pleas for cock."
        her "Mys Prfussur. Pleeth thuk mye in evury wun ov may thluddy vuk-howes. Ah need cahk do vive. *Gag* Ah Exzitht to thurviz dick."
        m "Holy fuck Severus, you’re a genius! Beg for the dildo bitch!"
        her "Provethor Dumbldor, *gag* vill may azhowe viv vog vick!"
        m "Pull out Severus, I want to hear this properly."

        hide screen hermione_main
        $ h_body = "01_hp/13_hermione_main/shaming/7400.png"
        show screen hermione_main

        her "OH GOD FILL MY ASS WITH DOGGIE COCK! I NEED THICK RED CANINE COCK SHOVED UP ME! I WANT TO BE MOUNTED AND RODE AND MADE A REAL BITCH!"
        sna "Oh my god!"

        "Snape grabs Hermione by the back of the head and slams her face into his crotch. Genie grabs the dildo and rams it up Hermione’s anal cavity."
 
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        hide screen hermione_main
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ h_ypos=0
        $ h_body = "01_hp/13_hermione_main/shaming/7500.png"
        $ genie_cum_chibi_xpos =  0
        $ genie_cum_chibi_ypos  = 10
        $ g_c_c_u_pic = "genie_cum_03"
        $ h_body = "01_hp/13_hermione_main/shaming/7500.png"
        $ snape_cum_chibi_xpos =  0
        $ snape_cum_chibi_ypos  = 10
        $ s_c_c_u_pic = "snape_cum_01"
        show screen s_c_c_u
        show screen g_c_c_u
        show screen hermione_main   
        hide screen white
        with hpunch
        pause


        "As her asshole closes around the knot she climaxes. Her eyes roll back, her throat spasms, and snape’s thick jizz erupts out of her nose."

        hide screen hermione_main
        "She falls back to the ground, cum dripping out of her mouth."

        hide screen s_c_c_u
        hide screen g_c_c_u


        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/snape_14.png"
        show screen snape_main   

        sna "Oh my god…"
        m "Yeah, I didn’t really expect that."

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/snape_19.png"
        show screen snape_main   

        sna "This is the greatest moment of my life."
        m "I mean, I really just did not expect that."
        sna "Genie, I don’t think you understand. For the first time in my miserable life… I think I’m actually happy!"
        m "Yeah, brutal revenge sex is pretty incredible therapy."

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/23.png"
        show screen snape_main   

        hide screen chair_02
        hide screen g_c_u
        hide screen s_c_u
        hide screen desk_02
        show screen genie 

        sna "Thank you my friend. If there’s anything I can ever do for you, please don’t hesitate."
        m "Well, you can take Miss Granger back to her room for starters."
        sna "Of course. I’ll wipe her memory as well."
        m "Hmm… Can you make her think this was all a dream?"
        sna "Oh you are truly wicked my friend. What do you want to do with this?" 

        "Snape gestures to the dildo"

        m "I’ll hold onto it. It might come in handy for latter sessions with Miss Granger."

        hide screen snape_main
        $ s_sprite = "01_hp/10_snape_main/24.png"
        show screen snape_main   

        sna "Of course. Do you want me to talk to Draco?"
        m "Yes. Tell him to be a bit more discrete when doing this sort of thing."
        sna "Certainly. Well, good bye Genie. We should do this more often."
        m "I think we can arrange that…"

        hide screen snape_main
        hide screen hermione_main
        hide screen h_c_u

    $ hermione_chibi_ypos = 250
    $ shaming += 1
    $ shaming_busy = False    
    $ shaming_02 = True
    $ shaming_03 = True
     
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    $ only_upper = False
    
    jump custom_request_wrapup