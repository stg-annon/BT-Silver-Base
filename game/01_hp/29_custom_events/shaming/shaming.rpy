label __init_variables:
    $ shaming = 0
    $ shaming_busy = False
    $ shaming_01 = False
    $ shaming_02 = False
    $ shaming_03 = False
    return
    
label shaming_intro:
    
    $ ce_base = True
    $ ce_skirt = True
    $ ce_top = True
    $ ce_arms = True
    
    $ ce_breasts = 1
    
    $ ce_hair_a = hermione_hair_a
    $ ce_hair_b = hermione_hair_b
    
    $ cust_a = "01_hp/29_custom_events/common/body.png"
    $ cust_b = "01_hp/29_custom_events/common/arms.png"
    $ cust_c = "01_hp/29_custom_events/common/breasts_"+str(ce_breasts)+".png"
    $ cust_f = hermione_skirt
    $ cust_g = hermione_top
    
    return
    
label shaming_event:
    
    $ ce_base = False
    $ ce_skirt = False
    $ ce_top = False
    $ ce_arms = False
    
    $ ce_breasts = 1
    
    $ ce_hair_a = "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+".png"
    $ ce_hair_b = "01_hp/29_custom_events/common/hair/"+str(ce_hair_style)+"_"+str(ce_hair_color)+"_2.png"
    
    $ cust_a = "01_hp/29_custom_events/common/body.png"
    $ cust_b = "01_hp/29_custom_events/common/arms.png"
    $ cust_c = "01_hp/29_custom_events/common/breasts_"+str(ce_breasts)+".png"
    $ cust_d = "01_hp/29_custom_events/common/panties.png"
    $ cust_e = "01_hp/29_custom_events/common/bra.png"
    $ cust_f = "01_hp/29_custom_events/common/skirt.png"
    $ cust_g = "01_hp/29_custom_events/common/top.png"
    
    return
    
label shaming:
    $ ce_name = "shaming"
    call shaming_intro
    hide screen hermione_main
    hide screen custom_event_h
    with d3
    m "{size=-4}(Should I...){/size}"
    menu:
        "\"(Fuck it, what's the worst that could happen.)\"":
            pass
        "\"(I'd rather not risk it)\"":
            jump new_personal_request
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    
    call ce_her_main("","0100")
    
    m "Miss Granger."
    her "Yes, Professor?"
    m "I want you to return to my room after hours..."

    if shaming == 0:
        call ce_her_main("But Sir!","0200")
        her "That's against school rules."
        m "I'm sure you're talented enough to get here unnoticed."
        her "..."
        call ce_her_main("I refuse sir. I don't want to think what would happen if I ran into a teacher.","0300")
        m "Not even for... 100 house points?"
        call ce_her_main("!!!","0400")
        call ce_her_main("That's a lot of points...","0500")
        her "Those slytherin wenches would be astonished when they wake up."
        her "I-"
        call ce_her_main("Fine, i'll do it.","0600")
        m "Fantastic!"
        m "Well then, miss Granger, I'll see you tonight."
        $ shaming_busy = True
    else:
        call ce_her_main("...","0700")
        m "..."
        call ce_her_main("...","0800")
        m "..."
        "this might have been a bad idea."
        if whoring >20:
            call ce_her_main("...Okay.","0900")
            "!!!"
            m "(I can't believe it!)"
            m "(What a slut.)"
            m "Fantastic!"
            m "Well then, miss Granger, I'll see you tonight."
            $ shaming_busy = True
        else:
            jump too_much
    
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
    jump day_main_menu  

label shaming_night:

    call her_walk(520,400,2)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)

    $ h_xpos=320
    $ h_ypos=0
    $ ne = False


    if shaming == 0: #First time this event taking place.
        call ce_her_main("","1000",320)        
        m "Good evening, Miss Granger."
        her "Good evening, Professor."
        her "So what do you want me to do?"
        m "It's nothing special."
        m "First of all, please take off your robe."
        her "Of course, Sir."

        call ce_her_main("","1100")      
        pause .1
        call ce_her_main("","1200")    
        pause .1  
        call ce_her_main("","1300") 
        pause .1  
        
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
            call ce_her_main("P-Professor?!","1400")
            her "What are you doing?"
            m "Stroking my dick."
            call ce_her_main("Professor I'm really not comfortable with you jerking off in front of me...","1500")
            m "I don't care."
        else:
            call ce_her_main("","1600")
            "Hermione notices what you are doing."
            "But she doesn't object."
        m "You see, Miss Granger..."
        m "You have been an absolute tease towards me over the past few weeks..."
        call ce_her_main("...?","1700")
        m "Prancing about the school, pretending to be a pure and innocent pupil."
        call ce_her_main("Professor?","1800")
        m "But once you're behind my door, you turn into nothing more than a filthy whore!"
        m "Doing whatever I want, as long as you get some house points in return."
        call ce_her_main("!!!","1900")
        m "Whores like you should be punished!"
        m "I'm going to use you as my cumbucket."
        ">Hermoine is fuming."
        call ce_her_main("oh yeah?","2000")
        her "I'm just gonna leave."
        m "Go ahead, try."
        call ce_her_main("...","2100")
        call ce_her_main("!!!","2200")
        call ce_her_main("what's going on?","2300")
        m "I cast a simple binding spell just a couple of minutes ago."
        m "Try as you might you won't be able to leave."
        m "Now, miss Granger,"
        m "Please take off your shirt."
        call ce_her_main("","2400")   
        show screen ctc
        pause 
        her "..."
        ">hermoine stares at you with a look that could burn holes through walls."
        hide screen hermione_02
        hide screen custom_event_h
        with d3
        call shaming_event
        show screen hermione_04
        call ce_her_main("","2500")   
        pause
        m "Oh yeah look at those perfect titties..."
        m "All the way off, miss Granger."
        call ce_her_main("","2600")
        
        hide screen hermione_04
        $ hermione_chibi_xpos = 400
        #$ hermione_chibi_ypos = 0
        $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/03_no_shirt_01.png"
        show screen h_c_u
        
        ">She throws the shirt on your desk."
        m "Now the panties, Miss Granger"
        hide screen custom_event_h
        with d3
        $ ce_h_anger = True
        call ce_her_main("No.","2700")
        $ ce_h_anger = False
        m "Excuse me?"
        hide screen custom_event_h
        with d3
        $ ce_h_anger = True
        call ce_her_main("I refuse.","2800")
        $ ce_h_anger = False
        m "If you think that will stop me, you've got the wrong idea, slut."
        call ce_her_main("","2900")
        show screen ctc
        pause 
        ">You conjure up some pink fluffy cuffs and bind Hermione's hands together."
        call ce_her_main("P-P-Professor!","3000")
        her "This is too much!"
        her "You must stop this."
        m "I mustn't do anything, miss Granger, I'm the headmaster of this school."
        m "I'm in complete control of this situation, and you're powerless!"
        m "Immobilized in my room, with practically every person in the castle asleep."
        m "I'm going to enjoy this..."
        call ce_her_main("","3100")
        "You reach under her skirt."
        call ce_her_main("","3200")
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
        call ce_her_main("p-please stop professor.","3300")
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
        $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/07_dance_01.png"
        show screen h_c_u
        call ce_her_main("","3400")   
        show screen ctc
        pause
        "Hermione starts sobbing."
        "You resume jerking your cock."
        ">hermione is glancing at your dick."
        her "Please Professor, I'll do anything, just don't do this to me."
        m "Keep your mouth shut, wench."
        call ce_her_main("","3600")   
        show screen ctc
        her "!!!"
        her "MMHHHM!! MHHHMMMH!"
        m "much better"
        call ce_her_main("","3700")   
        "Tears are running down Hermione's cheecks."
        m "This is perfect"
        m "I'm going to..."
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        call ce_her_main("","3800")   
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
        call ce_her_main("","3900")   
        "Hermione is still sobbing."
        "You are instantly rock hard again"
        if whoring > 22:
            "You notice that she seems to be rubbing her thighs together."
        m "You fucking slut"
        m "This is your destiny"
        call ce_her_main("","4000") 
        m "My personal cumbucket"
        m "It's coming..."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        call ce_her_main("","4100")   
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
        call ce_her_main("","4200") 
        "You take off the gag"
        m "One Hundred House points for Gryffindor"
        $ gryffindor +=100
        her "..."
        m "You can go now, Miss Granger"
        if whoring < 5:
            her "..."
            m "wait, don't you need to..."
            "Hermione leaves"
            hide screen custom_event_h
            hide screen h_c_u
            with d3
            m "yeah I definitely overdid it"
            m "I hope she's okay..."
            $ shaming_clothed = False
            $ mad = +50
        elif whoring < 15:
            her "I trusted you, Professor!"
            m "What's wrong, Didn't I just give you a shitload of points in return?"
            m "I'd be glad if I were you..."
            "Hermione grabs her robe."
            call ce_her_main("","4300")  
            show screen ctc
            pause 
            "And leaves after shooting a nastly look towards you."
            $ shaming_clothed = True
            $ mad = +15
        else:
            call ce_her_main("Thanks, Professor","4400")
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
                    call ce_her_main("!!!","4700")
                    her "Where have my clothes gone??"
                    m "I teleported them back to your room"
                    call ce_her_main("But I can't go back looking like this?!","4800")
                    m "Oh I'm sure you can."
                    m "Everybody is fast asleep, the only one that might see you is Peeves, and you can hear him coming from a mile away."
                    her "But Professor!"
                    m "OHMYGOD IS IT THIS LATE ALREADY!"
                    m "I've got important things to do, goodbye miss Granger."
                    "You quickly shove her out of the door and lock it."
                    hide screen custom_event_h
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
                    call ce_her_main("","4600") 
                    show screen ctc
                    pause 
                    $ shaming_clothed = True
        $ shaming_01 = True
        $ shaming_busy = False
        hide screen g_c_u
        hide screen h_c_u
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
        hide screen custom_event_h
        with d3
        $ ce_hair_a = "B"
        $ ce_hair_b = 1
        
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
        
        
        call ce_her_main("I came to see you.","6000",320)     
        m "Good evening, Miss Granger."
        her "Good evening, Professor."
        m "..."
        her "..."
        "An awkward silence falls"
        m "(This is bizarre. What’s with the eyes and the robe? Did I tell her to go get gang-banged by the slytherin house and forget?)"
        m "Uh… Why are you here? I don’t remember asking for you."
        call ce_her_main("I came to see you.","6100")
        m "That's nice..."
        her "..."
        m "...Are you feeling alright?"
        her "Yes, I feel fine."
        m "Then why are you just standing there with that look on your face?"
        her "Do you wish something of me?"
        m "I think you have that backwards."
        her "What?"
        m "Nevermind. Take that ridiculous robe off."
        call ce_her_main("","6200")
        with d3
        "Hermione peels off her robe to expose a very revealing sling bikini."
        
        call ce_her_main("","6300")
        hide screen hermione_02_b
        $ hermione_chibi_xpos = 400
        #$ hermione_chibi_ypos = 0
        $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/07_dance_01.png"
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
        call ce_her_main("I am a slut sir, a filthy bitch. Make me your cock-puppet and fuck my throat.","6400")
        m "(Woah. I think I broke her. Hang on, what’s this?)"
        "Peeking out from behind the bikini is the edge of a tattoo just below her waist"
        m "Miss Granger, pull aside your bikini for me."
        her "Yes sir."
        "Hermione pulls the top of the bikini open to reveal her breasts to Genie"
        m "Not your tits you silly bitch, your cunt."
        her "Oh god, yes sir, tell me what a filthy fuck-toy I am."
        
        call ce_her_main("","6600")
        pause
        
        "Hermione reveals her dripping wet pussy with a rapturous expression on her face."
        m "(Ah… It’s all beginning to make sense… Someone has inscribed Miss Granger with a magical tattoo, and probably put a few other spells on her as well… "
        m "Probably someone from Slytherin house, but that’s just a wild guess. I should get Severus in here and see if he knows anything about it.)"
        m "Miss Granger, put your robe back on and fetch Professor Snape."
        call ce_her_main("Don’t you want to fuck me first?","6700")
        m "…"
        her "Please?"
        m "Just go get Snape and don’t act like a massive whore until I tell you to."
        her "Yes Professor."
        
        call ce_her_main("","6800")
        show screen ctc
        pause
        hide screen custom_event_h

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

        hide screen hermione_02_b
        $ hermione_chibi_xpos = 400
        $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/07_dance_01.png"
        show screen h_c_u
        call ce_her_main("","6900",280)
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
        call ce_her_main("Professor… I think it’s stuck…","7000")
        m "Well pull harder girl."
        her "Oh god… I can feel it… AH!"
        call ce_her_main("","7100")
        pause
        "With an audible pop the dildo rockets out of Hermione’s slit. She falls to the ground and starts convulsing."
        
        hide screen snape_main
        hide screen hermione_02
        $ hermione_chibi_xpos = -20
        $ hermione_chibi_ypos = 75
        $ s_sprite = "01_hp/10_snape_main/snape_26.png"
        $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/08_sits.png"
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
        hide screen custom_event_h
        hide screen snape_main
        
        "Genie and Snape jerk off over Hermione. From the look on her face she is nearly catatonic with excitement."
        call ce_her_main("","7200",390,150)
        her "Please…Please let me taste them…"
        "Without waiting, Snape grabs Hermione by the hair and rams his cock down her throat."
        m "That’s the spirit, but I was hoping to hear her beg more."
        sna "Ha! I have an idea. Oh Miss Granger, you stuck up, know it all, cock gobbling whore."
        her "Mys?"
        sna "Beg for cock as I fuck your slutty little throat."
        call ce_her_main("","7300")
        "Tears begun streaming down her face as Hermione struggles to enunciate her pleas for cock."
        her "Mys Prfussur. Pleeth thuk mye in evury wun ov may thluddy vuk-howes. Ah need cahk do vive. *Gag* Ah Exzitht to thurviz dick."
        m "Holy fuck Severus, you’re a genius! Beg for the dildo bitch!"
        her "Provethor Dumbldor, *gag* vill may azhowe viv vog vick!"
        m "Pull out Severus, I want to hear this properly."
        call ce_her_main("OH GOD FILL MY ASS WITH DOGGIE COCK! I NEED THICK RED CANINE COCK SHOVED UP ME! I WANT TO BE MOUNTED AND RODE AND MADE A REAL BITCH!","7400")
        sna "Oh my god!"
        "Snape grabs Hermione by the back of the head and slams her face into his crotch. Genie grabs the dildo and rams it up Hermione’s anal cavity."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white
        hide screen custom_event_h
        $ genie_cum_chibi_xpos =  0
        $ genie_cum_chibi_ypos  = 10
        $ g_c_c_u_pic = "genie_cum_03"
        $ snape_cum_chibi_xpos =  0
        $ snape_cum_chibi_ypos  = 10
        $ s_c_c_u_pic = "snape_cum_01"
        show screen s_c_c_u
        show screen g_c_c_u
        call ce_her_main("","7500",140,0)
        hide screen white
        with hpunch
        pause
        
        "As her asshole closes around the knot she climaxes. Her eyes roll back, her throat spasms, and snape’s thick jizz erupts out of her nose."
        hide screen custom_event_h
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
        hide screen custom_event_h
        hide screen h_c_u

    $ hermione_chibi_ypos = 250
    $ shaming += 1
    $ shaming_busy = False    
    $ shaming_02 = True
    $ shaming_03 = True
     
    hide screen bld1
    hide screen custom_event_h
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    


    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    $ only_upper = False
    
    jump custom_request_wrapup