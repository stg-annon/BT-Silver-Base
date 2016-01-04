label end_hermione_personal_request:
    $ renpy.play('sounds/door.mp3') #Sound of a door.
    with Dissolve(.3)
    
    ### MUSIC BLOCK ###
    if daytime:
        play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 # DAY MUSIC
    else:
        play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    ### END OF BLOCK ###
    
    if daytime:
        $ hermione_takes_classes = True
        jump day_main_menu
    else:
        $ hermione_sleeping = True
        jump night_main_menu

###################REQUEST_01 JUST STAND THERE.
label new_request_01: #LV.1 (Whoring = 0 - 2)
    hide screen hermione_main
    with d3
    m "{size=-4}(All I'll do is have an innocent conversation with her...){/size}"
    menu:
        "\"(Yes, let's do that.)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    if ("maid" or "gryffindor_cheerleader" or "slytherin_cheerleader" or "ms_marvel" or "heart_dancer" or "power_girl" or "harley_quinn") in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                menu:
                    "-A maid-" if "maid" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 1
                        $ stockings = 1
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass
                    "-A Cheerleader-" if "gryffindor_cheerleader" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 2
                        $ stockings = 2
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass
                    "-A Slytherin Cheerleader-" if "slytherin_cheerleader" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 3
                        $ stockings = 4
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass
                    "-Ms Marvel-" if "ms_marvel" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 8
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass
                    "-A heart dancer-" if "heart_dancer" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 4
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass
                    "-power girl-" if "power_girl" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 7
                        $ panties = False
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass  
                    "-Harley Quinn-" if "harley_quinn" in outfit_invintory:
                        her "Fine, let me go change."
                        show screen blkfade
                        hide screen hermione_main
                        with d3
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ temp_stockings = stockings 
                        $ temp_outfit = custom_outfit
                        $ custom_outfit = 9
                        hide  screen blkfade
                        show screen hermione_main
                        with d3
                        pass                           
            "\"(Not right now.)\"":
                pass
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    m "Alright then..."
    m "Just tell me some news about you."
    
    $ menu_x = 0.5 #Menu is moved to the left side.
    call her_main("","body_08")
    
    if request_01 == 0: #First time this event taking place.
        her "Ehm... Alright..."
        her "I just stand here and talk then...? Like this?"
    else:
        her "Here in the middle, right? I remember..."
    
    hide screen hermione_main
    with d3
    $ h_xpos = 140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_ypos = 0
    show screen blktone 
    with d3
    show screen ctc
    with d3
    call her_main("","body_01")
    
    pause
    
    m "Well?"
    if request_01 == 0 and whoring <=5: #First time this event taking place.
        $  new_request_01_01 = True #Hearts on menu buttons.
        $ new_request_01_heart = 1
        call her_main("Em... very well...","body_11")
        ">Hermione is feeling confused..."
        call her_main("...................","body_12")
    if whoring >= 0 and  whoring <= 5: #LEVEL 01 and LEVEL 02
        if whoring >= 3 and whoring <= 5:
            $ level = "02"
            $  new_request_01_02 =True #Hearts on menu buttons.
            $ new_request_01_heart = 2
        call her_main("My life has been quite uneventful lately to be honest...","body_12")
        her "Apart from that day when I failed that test..."
        her "Still can't believe it happened..."
        menu: 
            "-Jerk off while she is talking-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                hide screen blktone
                with d3
                ">You reach under the desk and crab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                
                pause
                
                hide screen hermione_main
                with d3
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                
                call her_main("[genie_name], what are you doing?","body_14")
                m "What, oh it's nothing. Just scratching my leg."
                m "You were saying?"
                call her_main("Yes... Well, that test I failed...","body_14")
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Yes, what a tragedy that was..."
                her "Exactly! I'm glad you understand, [genie_name]."
                pass
        her "Come to think of it, I don't feel like talking about it anymore..."
        m "Alright, what else has happened lately?"
        her "Em... Well, I'm doing pretty well at herbology lately..."
        her "I mean, I always score the top marks, but I have been studying really hard anyway..."
        her "And now I sort of feel like sometimes I know more than professor Sprout herself..."
        if d_flag_01:
            m "{size=-4}(Yes... ah...){/size}"
        else:
            m "(Professor Sprout... He-he, what a ridiculous name...)"
        
        call her_main("Did you say something [genie_name]?","body_07")
        m "It's nothing, keep going..."
        call her_main("Well, some students are making fun of professor Quirell behind his back...","body_14")
        her "But I disapprove of such behavior of course."
        if d_flag_01:
            m "{size=-4}(Come on! Say something naughty!){/size}"
        else:
            m ".................."
        her "Oh, and my \"Men's Rights Movement\" group is gaining popularity..."
        her "I'm very happy about that..."
        call her_main("I think, given time, we will be able to make a real difference...","body_16")
        call her_main("Yes, it is so invigorating to know that you are doing the right thing!","body_06")
        her "Would't you agree professor?"
        if d_flag_01:
            m "{size=-4}(Dammit. Now she killed the mood completely...){/size}"
            show screen genie
            with d3
            $ d_flag_01 = False #NOT JERKING OFF ANY MORE.
            pass
        else:
            m "Zzzz........"
            
        call her_main("[genie_name]?","body_05")
        m "Yes, yes, I'm totally listening..."
        m "This is all very self righteous, er..."
        m "I mean, very invigorating and stuff..."
        call her_main("..........................","body_07")
  
    elif whoring >= 6: #LEVEL 03
        $  new_request_01_03 = True #Hearts on menu buttons.
        $ new_request_01_heart = 3
        call her_main("My life has been quite uneventful lately to be honest...","body_12")
        her "Hm..."
        her "There is a fierce competition going on between the \"Slytherin\" and the \"Gryffindor\" house."
        her "To be honest, [genie_name], there should be none..."
        her "\"Gryffindor\" would have been in the lead if not for those \"Slytherin\" harlots..."
        her "The things I hear those girls do simply to get a few extra points..."
        call her_main("How despicable!","body_04")
        m "What does this make you then, [hermione_name]?"
        call her_main("Exactly!","body_03")
        m "Huh?"
        call her_main("I have to work even harder to compensate for the damage those nasty girls are doing...","body_04")
        call her_main("Thank you for helping me out, [genie_name].","body_03")
        menu: 
            "-Start jerking off-":
                $ d_flag_01 = True #If TRUE genie jerks off under the desk.    
                hide screen hermione_main
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                
                pause
                
                hide screen hermione_main
                with d3
                $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                
                call her_main("[genie_name], what are you doing?","body_14")
                her "You are not.....?"
                call her_main("Are you...?","body_29")
                m "What, it's nothing. Keep going."
                call her_main("Hm...","body_07")
                m "{size=-4}(Is she onto me? Nah...){/size}"
            "-Participate in the conversation-":
                $ d_flag_01 = False #NOT JERKING OFF.
                m "Don't mention it."
                pass
                
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                
        call her_main("Well, like I was saying...","body_16")
        her "I heard that this one girl sold one of the professors some naughty pictures of herself for ten house points..."
        if d_flag_01:
            m "{size=-4}(What a slut... ah... Yes...){/size}"
        else:
            m "Ten points, huh?"
        her "Yes..."
        if d_flag_01:
            call her_main("And these two other girls...","body_29")
            her "There is a rumor that they are actually sleeping with professor snape..."
            m "{size=-4}(Yes... Those little, nasty, \"slytherin\" sluts!){/size}"
            call her_main("Also there was this one girl, who gave a teacher a handjob, right during class...","body_45")
            m "{size=-4}(Yes... This is good stuff, go on!){/size}"
            call her_main("And this other girl, she sucked off a teacher!","body_29")
            m "{size=-4}(Yes! Yes!){/size}"
            call her_main("And another girl let a teacher cum in her mouth...","body_46")
            her "And she swallowed it all and loved it!"
            m "{size=-4}(Wait... Is she making this up?){/size}"
            call her_main("I'm a nasty girl too, you know...","body_64")
            g4 "What?!"
            call her_main("I just want to suck a cock...","body_65")
            her "I want men to cum on my face like in those videos I saw!"
            g4 "{size=-4}(You little slut! That did it!) *Argh!*{/size}"
            hide screen hermione_main
            with d3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            g4 "Argh! YES!"
            hide screen hermione_main
            with d3
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            #pause 3
            pause
            if False:
                "hermione upset about cum being wasted"
            else:
                if whoring <= 10:
                    $ mad = +7
                    show screen bld1
                    with d3
                    call her_main("I knew it! You were touching yourself, [genie_name]!","body_47")
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    #show screen genie_jerking_off
                    with d3
                    call her_main("This is disgusting! How could you!?","body_32")
                    her "[genie_name], you are the headmaster! You are supposed to set a good example!"
                    m "Hey, little missy, are you going to judge me or do you want your points?"
                    call her_main("My points please, I believe I earned those.","body_34")
                    m "Yes you did."
                    call her_main("Ew... I feel so dirty now...","body_47")
                    hide screen genie_jerking_sperm_02
                    with d3
                else:
                    show screen bld1
                    with d3
                    call her_main("I knew it! You were touching yourself, [genie_name]!","body_64")
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    #show screen genie_jerking_off
                    with d3
                    call her_main("How could you [genie_name]? In front of a young innocent student!","body_30")
                    m "Hey, little missy, what you were saying wasn't exactly innocent"
                    call her_main("I don't know what you're talking about...","body_46")
                    m "I'm sure. Do you want your points or not?"
                    call her_main("{size=-4}he sure did cum a lot{image=textheart}{/size}","body_06")
                    hide screen genie_jerking_sperm_02
                    with d3
        else:
            her "We need to put an end to this behavior, [genie_name]!"
            m "Yeah, sure..."
            her "So you agree with me then?"
            her "I think we need to implement a new penalty system to punish girls who are known to sell favours..."
            m "(All I heard was \"punish girls\"...)"
            her "This will also help the boys in our school to feel less discriminated against!"
            m "The boys?"
            m "Oh, right... Nobody wants to buy sexual favours from them... Poor bastards."
            her "I'm so glad that you understand my concerns, [genie_name]."
            m "Yes, yes, sure..."
        
        
                
                
        

    stop music fadeout 2.0
    
    if whoring >= 11:
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        her "Oh, don't worry about the points, we were just having a nice talk."
        m "Really? What about \"Gryffindor\" winning the cup?"
        her "It's just 5 points [genie_name]."
        m "If you say so."
        her "Will this be all then?"
        m "Yes, you can go now."
    else:
        $ gryffindor +=5
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        show screen hermione_main
        hide screen hermione_01_f #Hermione stands still.
        with d3
        her "Will this be all then?"
        if whoring >= 0 and whoring <= 2: #LEVEL 01
            her "*sigh of relief*"
        m "Yes, you can go now."
    if request_01 == 0:
        call her_main("Another 5 points... The Guys will be so happy.","body_01")
        her "Thank you, [genie_name]."

    label request_01_done:
    if whoring <= 2:
            $ whoring +=1
 
    $ request_01 += 1
    
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)

    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ panties = True
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    jump end_hermione_personal_request
        
###################REQUEST_02 (Level 01)
label new_request_02: #SHOW ME YOUR PANTIES
    hide screen hermione_main
    with d3
    m "{size=-4}(I will ask her to show me her panties. Plain and simple.){/size}"
    $ menu_x = 0.5 #Default menu position restored.
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    show screen hermione_main
    her "So, what will it be [genie_name]?"
    m "Nothing drastic, really..."
    m "I just want you to show me your panties."             
    if request_02 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.  
        $ new_request_02_01 =  True #Hearts.
        call her_main("My... panties...?","body_14")
        call her_main("[genie_name]!","body_47")
        m "I know, I know, this a little weird..."
        call her_main(" {size=+7}A little !?{/size}","body_48")
        her "This is completely inappropriate!"
        m "Listen, we need to go through this phase before we get to the good stuff, alright?"
        call her_main("The \"good stuff\"? [genie_name] I don't understand...","body_31")
        m "What don't you understand, [hermione_name]?"
        m "Do you need these points or not?"
        call her_main("I do...","body_31")
        m "Lift up your skirt then..."
        call her_main(".............","body_47")
    else:
        if request_02 >= 1: #Not the first time
            call her_main("Oh... again?","body_29")
            m "Just do it..."
        call her_main("..................","body_29")
        

    hide screen bld1
    hide screen hermione_main
    with d5
    $ skirt_up = True
    $ menu_x = 0.5 #Default menu position restored.
    if whoring >= 6: # NO PANTIES
        show screen hermione_03_b
        with d3
    else:
        show screen hermione_03 #Hermione lifts her skirt
        with d3
        
    #play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 

    if whoring >= 0 and whoring <= 2: #LEVEL 01
        her_[8] "........................"
    elif whoring >= 3 and whoring <= 5: #LEVEL 02
        her_[14] "....................."
    elif whoring >= 6: #LEVEL 03 and up.
        her_[18] ".........................."
        g4 "!!?"
        
        
    

    


    if whoring >= 0 and whoring <= 2: #LEVEL 01   <============================= Fist event.
        $ new_request_02_01 =  True #Hearts.
        
        hide screen hermion_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_ypos=0 #Defines position of the Hermione's full length sprite.
        
        show screen bld1
        with d3
        show screen blktone
        with d3
        call her_main("","body_49")
        show screen ctc
        with d3
        pause
        
        her "....................."
        menu:
            "-Stare at her face-":
                ">You study Hermione's face..."
                pause
                ">You wonder what's going through her mind right now."
                call her_main(".......................","body_51")
                pause
            "-Stare at her panties-":
                ">That's a plain girlish underwear..."
                pause
                call her_main(".......................","body_51")
               

    elif whoring >= 3 and whoring <= 5: #LEVEL 02  <====================================================================== SECOND EVENT!
        $ new_request_02_02 =  True #Hearts.
        
        hide screen hermion_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_ypos=0 #Defines position of the Hermione's full length sprite.
        
        show screen bld1
        with d3
        show screen blktone
        with d3
        call her_main("","body_52")
        show screen ctc
        with d3
        pause
        her "Here, [genie_name]..."
        menu:
            "\"You don't look too embarrassed...\"":
                call her_main("That's not true...","body_53")
                call her_main("But this is a small price to pay if the \"Gryffindors\" keep the cup this year.","body_54")
                her "I know everyone will be so happy..."
                pause
            "\"I like your panties...\"":
                call her_main("Thank you, [genie_name]...","body_53")
            "-Keep looking into her eyes-":
                call her_main("..............................","body_55")
                her "...........................?"
                call her_main("................................","body_56")
                call her_main("[genie_name], please... You are embarrassing me.","body_57")
                

    elif whoring >= 9: #LEVEL 04 and up. <====================================================================== FINAL EVENT! (No panties).
        $ new_request_02_03 =  True #Hearts.
        
        hide screen hermion_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        $ h_ypos=0 #Defines position of the Hermione's full length sprite.
        
        show screen bld1
        with d3
        show screen blktone
        with d3
        call her_main("","body_58")
        show screen ctc
        with d3
        pause
        g4 "Where are your panties, [hermione_name]?"
        call her_main("Oh, lately I just don't feel like wearing them...","body_59")
        menu:
            "\"You little slut!\"":
                her "Hm..."
                call her_main("I suppose I am...","body_58")
                her "Do I get extra points for that?"
                menu:
                    "\"Absolutely!\"":
                        m "Absolutely!"
                        $ gryffindor +=10
                        m "Ten additional points to \"Gryffindor\"!" 
                        call her_main("Thank you, [genie_name]!","body_60")
                    "\"Absolutely not!\"":
                        $ mad +=5
                        call her_main("Why not!?","body_62")
                        m "Sluts aren't paid"
                        m "That's what makes them sluts"
                        call her_main("well are you even going to pay me 5 points?","body_61")   
                        m "Are you a slut or are you a prostitute?"
                        her "{size=-4}...a slut {/size}"
                        m "Good girl"
            "\"Good! Five points!\"":
                pass
    
    
    
    
    stop music fadeout 4.0
    
    label request_02_done:
    if whoring <= 8:
        $ gryffindor +=5
        m "Five points to \"Gryffindor\" [hermione_name]. Well done." 
        pause
    
    hide screen ctc
    hide screen hermione_main
    with d3
    $ h_xpos=120 #Defines position of the Hermione's full length sprite.
    $ hermione_chibi_xpos = 400 #Near the desk.
    
    $ skirt_up = False
    show screen hermione_02 #Hermione stands still.
    with fade
    call her_main("","body_31")
    
    stop music fadeout 4.0
    
    her "will this be all then?"
    m "Yes, you can go now."

    if request_02 == 0: #First time.
        call her_main("Another 5 points...","body_13")
        her "Can't wait to tell the guys!"
        call her_main("Only that I can't actually tell them about any of this...","body_12")
    
    if daytime:
        her "Well, my classes are about to start..."
    else:
        her "It's getting pretty late, [genie_name]... I should go..."

    
    hide screen hermione_main
    with d3
    hide screen bld1
    hide screen blktone 
    hide screen ctc
    with d3
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    if whoring <= 2:
        $ whoring +=1
    $ request_02 += 1
    
    jump end_hermione_personal_request
        
################### REQUEST_03 (Level 02) (Available during daytime only). "Give me your panties" ###############################
label new_request_03: #(Whoring = 3 - 5)
    hide screen hermione_main
    with d3
    m "{size=-4}(I could ask her to take off her panties and give them to me before she leaves for classes today.){/size}"
    $ menu_x = 0.5 #Default position of the menu. Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    m "[hermione_name]?"
    call her_main("I am listening, [genie_name].")
    m "I will need your panties..."
    
    if whoring <=2:
        jump too_much
    
    hide screen hermione_main
    with d3
    $ menu_x = 0.5 #Menu is moved to the left side.
    $ h_xpos=120 #Defines position of the Hermione's full length sprite. Left: 370 Center: 120
    $ h_ypos=0
    
    show screen blktone 
    show screen ctc
    with d3
    
    if request_03 == 0 and whoring <= 5: #First time this event taking place. and LEVEL 02.   <===================================== ONE TIME EVENT.
        stop music fadeout 10.0
        $ new_request_03_01 = True # HEARTS.
        $ new_request_03_heart = 1
        $ request_03 += 1
        
        call her_main("W-what?","body_11")
        her "My... panties...?"
        her "[genie_name], this is..."
        m "This is the favour I will be buying from you today, [hermione_name]..."
        m "If you are not interested you are more than welcome to leave."
        her "No, I am interested. I am.... it's just..."
        her "You need my...."
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("...panties, [genie_name]?","body_47")
        m "Yes I do..."
        call her_main("May I ask what you are planning to do with them...?","body_66")
        m "Ehm...I'm conducting research..."
        her "But this is kind of inappropriate, don't you think?"
        m "But don't you hate it that some of the girls from \"Slytherin\"..."
        m "Are selling favours for house points, [hermione_name]?"
        call her_main("Yes I do!","body_47")
        call her_main("(Those \"Slythering\" tramps have no dignity.)","body_12")
        m "Well, there you go then!"
        call her_main("Huh?","body_66")
        m "Beat them at their own game!"
        call her_main("What?","body_14")
        m "Yes! Don't just put the \"Gryffindor\" house back on top..."
        m "But do it by beating them at their own game!"
        call her_main("[genie_name]...","body_11")
        m "A headmaster cannot play favourites, but you know how I feel about \"Gryffindor\"..."
        m "I wish I could give you the points but that would ruin the system..."
        show screen blktone8
        hide screen hermione_main
        with d3
        ">Suddenly Hermione extends her arm to you..."
        ">You see that she is clutching a little piece of fabric in her fist..."
        #">Her panties? You can't help but wonder when she managed to take them off..."
        m "??!"
        ">You acquired Hermione's panties..."
        hide screen blktone8
        with d3
        call her_main("Just take them [genie_name]...","body_67")
        m "What? When did you?"
        her "Your speech was so moving..."
        her "You are so right, [genie_name]! I shall beat them at their own game!"
        her "My classes are about to start, so I should probably go now..."
        
        hide screen hermione_main
        with d3
        $ h_xpos=370 #Right: 370 Center: 120
        
        call her_main("...........","body_23")
        call her_main("...I hope nobody will notice that I have no underwear on today...","body_29")
        call her_main("Oh, and I will be back tonight to pick them up, [genie_name].","body_31")
        m "Of course. Your panties will be right here on my desk, waiting for you..."
        call her_main(".............","body_34")
        jump request_03_ends

    else: #<========================================================================================== FIRST EVENT!
        if request_03 >= 1:
            her "Again, [genie_name]?"
            m "Yes again..."
        her "Here..."
        if whoring >= 12: #LEVEL 05
            hide screen hermione_main
            with d3
            ">Hermione pulls her panties out of her pocket..."
            m "What?"
            call her_main("Yes, I had a feeling that you might ask for these today, [genie_name].","body_45")
            m "A feeling?"
            call her_main("Well, to be completely honest I just do not bother to wear them much anymore...","body_68")
        else:
            hide screen hermione_main
            with d3
            ">Hermione takes off her panties and hands them over to you..."
        hide screen hermione_main
        with d3
        ">Hermione's panties acquired."
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Flashing panties
        show screen hermione_main
        with d3
        her "Well, the classes are about to start, so I'd better go now..."

 
        
    label request_03_ends:
        
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3

    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    $ request_03 = True #True when Hermione has no panties on.
    if whoring <= 5:
        $ whoring +=1
    
    jump end_hermione_personal_request
    
label new_request_03_complete: # WHORING LEVEL 02 <=================
    
    # $ walk_xpos=610 #Animation of walking chibi. (From)
    # $ walk_xpos2=400 #Coordinates of it's movement. (To)
    # $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    # $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    # show screen hermione_walk_01 
    # with d4
    # pause 2.5
    # $ hermione_chibi_xpos = 400 #Near the desk.
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_walk(610,400,3)
    
    show screen hermione_02 #Hermione stands still.
    pause.5
    show screen bld1
    with Dissolve(.3)
    
    hide screen hermion_main
    with d3
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    
    call her_main("Good evening, [genie_name]...","body_01")
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
    menu:
        "\"Here are your panties.\"":
            if have_cum_soaced_panties:
                jump panties_soaked_in_cum
            else:
                her "Thank you, [genie_name]."
                her "And my payment?"
                m "Of course."
        "\"How was your day, [hermione_name]?\"":
            if  whoring <= 5: #LEVEL 02. EVENT LEVEL: 01
                $ new_request_03_01 = True # HEARTS.
                $ new_request_03_heart = 1
                
                hide screen hermion_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite.
                
                call her_main("Oh...","body_15")
                her "Quite ordinary actually..."
                call her_main("Although I could not help but worry that somebody would notice somehow...","body_13")
                call her_main(".....","body_29")
                call her_main("Can I have my panties back now?","body_31")
                m "Of course..."
                hide screen hermione_main
                with d3
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    call her_main("And my payment?","body_31")
                    m "Yes, yes..."
            elif whoring >= 6 and whoring <= 8: #LEVEL 03. EVENT LEVEL 02.
                $ new_request_03_02 = True # HEARTS.
                $ new_request_03_heart = 2
                
                hide screen hermion_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite.
                
                call her_main("Oh...","body_15")
                her "It was quite ordinary really..."
                her "I spent some time with my classmates..."
                her "And we had a short \"MRM\" meeting after that..."
                call her_main("I gave a short speech on \"Why it is wrong to sell sexual favours in exchange for house points\"...","body_16")
                call her_main("I felt bad that I had to give the speech without any underwear on...","body_12")
                menu:
                    "\"You little hypocrite!\"":
                        $ mad +=5
                        call her_main("[genie_name]?","body_14")
                        m "You sold your panties to me this morning..."
                        m "And a couple of hours later you already publicly condemned that exact behaviour..."
                        #m "What would you call this?"
                        #call her_main("I know you are right, [genie_name]...","body_69")
                        call her_main("(But we need the points...)","body_69")
                        call her_main("Can I have my payment now please?","body_66")
                        m "What about your panties?"
                        call her_main("Oh, them too of course...","body_34") 
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            pass
                    "\"It's for the grater good...\"":
                        her "Exactly!"
                        her "We need those points badly..."
                        her "It is not my fault that the system is so corrupted..."
                        call her_main("I shall remain a symbol of righteousness to my peers, no matter what!","body_16")
                        call her_main("Can I have my panties back now, please?","body_31")
                        if have_cum_soaced_panties:
                            jump panties_soaked_in_cum
                        else:
                            her "And my payment."
            elif whoring >= 9: #LEVEL 04. EVENT LEVEL 03.
                $ new_request_03_03 = True # HEARTS.
                $ new_request_03_heart = 3
                
                hide screen hermion_main
                with d3
                $ h_xpos=120 #Defines position of the Hermione's full length sprite.
                
                call her_main("Another ordinary day at hogwarts...","body_16")
                her "Nothing worth mentioning happened today..."
                call her_main("Although I have to admit...","body_29")
                her "It was oddly empowering to have no underwear on..."
                her "Hm..."
                call her_main("Can I have my panties back now please?","body_45")
                m "Of course..."
                hide screen hermione_main
                with d3
                ">You give Hermione her panties back..."
                if have_cum_soaced_panties:
                    jump panties_soaked_in_cum
                else:
                    call her_main("And my payment?","body_45")
                    m "Yes, yes..."
    label back_from_panties:
    if whoring >= 9 and have_cum_soaced_panties == True:
        m "You can go now."
        call her_main("What about my points?","body_30")
        m "You still want points after I just gave you a gift?"
        her "What gift?"
        m "You're wearing it"
        her "What, semen soaked panties?"
        m "if you'd prefer the points then just take them off"
        call her_main("well... I am already wearing them","body_29")
        m "then say thank you for the gift"
        call her_main("Thank you, [genie_name]...","body_17")
        m "You can go now."
        her "Good night, [genie_name]."
    else:
        $ gryffindor +=15
        m "Fifteen points to \"Gryffindor\" [hermione_name]. Well deserved." 
        her "Thank you, [genie_name]..."
        m "You can go now."
        her "Good night, [genie_name]."
        #m "Yes, good night..."
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    
    $ request_03_points += 1 #Leveling up the event.
    $ request_03 = False #When False - you gave her her panties back.
    $ have_cum_soaced_panties = False #TRUE when you have the panties in your possession (before you return them to Hermione).
    
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)
    
    $ hermione_sleeping = True
    play music "music/Music for Manatees.mp3" fadein 1 fadeout 1 # NIGHT MUSIC
    
    return
label panties_soaked_in_cum:### PANTIES SOAKED IN CUM ###
    
    if whoring >= 3 and whoring <= 5: # LEVEL 02
        hide screen hermion_main
        with d3
        $ h_xpos=120 #Defines position of the Hermione's full length sprite.
        
        call her_main("Hm....?","body_71")
        call her_main("[genie_name]? What is this?","body_05")
        her "What have you done to them?"
        call her_main("They are covered in something slimy...","body_07")
        menu:
            "\"An experiment went wrong\"":
                call her_main("An experiment went wrong, [genie_name]?","body_02")
                m "Yes... Or maybe I should rather say..."
                g9 "\"An experiment went very right\"? He-he..."
                call her_main(".....................?","body_07")
                her "What kind of experiment was it?"
                m "What? Oh..."
                m "Some top secret research I'm conducting."
                m "I can't discuss it with a student."
                call her_main("................................","body_05")
            "\"You gave them to me like this!\"":
                her "I most certainly did not, [genie_name]!"
                her ".........................."
        call her_main("Well, these will require some serious cleaning before I can put them on again...","body_71")
        m "Or you could put them on now."
        call her_main("What?","body_14")
        call her_main("I really would rather not, [genie_name]...","body_13")
        menu:
            "\"Put them on or lose the points!\"":
                $ mad +=7
                call her_main("What?","body_72")
                her "[genie_name], you are joking, right?"
                m "I am not..."
                call her_main("B-but...","body_31")
                call her_main("........................................","body_33")
                call her_main("(Must you always have your way, [genie_name]?)","body_47")
                m "What was that, [hermione_name]?"
                call her_main("It's nothing, [genie_name].","body_30")
                her "Putting my panties back on!"
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">Hermione hesitantly puts on her panties..."
                ">A tiny stream of cum trickles down one of her legs..."
                ">Hermione looks very uncomfortable..."
                hide screen blktone8
                with d3
                call her_main("......................","body_34")
            "\"Well, suit yourself...\"":
                pass
    if whoring >= 6 and whoring <= 8: # LEVEL 03 (SECOND EVENT)
        call her_main("My panties...","body_71")
        call her_main("What happened to them [genie_name]?","body_73")
        menu: 
            "\"An experiment went wrong.\"":
                her "Hm..."
                her "I see..."
            "\"You gave them to me like this!\"":
                her "Did I? Oh, well..."
        hide screen hermione_main
        with d3
        ">Hermione gives her cum-soaked underwear a quizzical look..."
        call her_main("Seems like these will require some serious cleaning before I can put them on again...","body_71")
        m "Why not put them on now?"
        call her_main("Hm....?","body_17")
        call her_main("Well, I suppose I could wear them one more time before putting them into laundry...","body_71")
        hide screen hermione_main
        with d3
        show screen blktone8
        with d3
        ">Hermione puts the panties on..."
        hide screen blktone8
        with d3
        call her_main("(This feels funny...)","body_34")
        call her_main("Will this be all, [genie_name]?","body_44")
    if whoring >= 9: #LEVEL 04+ (THIRD EVENT)
        call her_main("My panties...","body_71")
        if request_03 >= 1:
            her "They are covered in something slimy again..."
        else:
            her "They are covered in something slimy..."
        her "And they smell funny..."
        call her_main("Hm... That smell...","body_29")
        her "It's familiar somehow..."
        call her_main("What exactly did you do to them, [genie_name]?","body_45")
        menu:
            "\"An experiment went wrong\"":
                her "An experiment, huh?"
                her "Of what nature?"
                call her_main("No, don't answer that... I think I know...","body_46")
            "\"You gave them to me like this!\"":
                her "I don't think so, [genie_name]."
                her "But it's alright if you don't want to tell me, [genie_name]..."
                her "I think I know exactly what happened to them..."
            "\"I came all over them!\"":
                call her_main("I knew it...","body_64")
                her "They reek of semen!"
        call her_main("Hm...","body_68")
        her "Seems like these will require some serious cleaning before I can put them on..."
        call her_main("Unless you want me to put them on now, [genie_name]...?","body_64")
        menu: 
            "\"Yes! Put them on now, [hermione_name]!\"":
                her "Well, if I must..."
            "\"I don't care. Do what you want.\"":
                her "Why not put them on one more time?"
        
        call her_main("I am only doing this to give my house a fair chance at winning the cup this year...","body_74")
        m "Right..."
        hide screen hermion_main
        with d3
        show screen blktone8
        with d3
        ">Hermione swiftly slides her drenched panties on..."
        hide screen blktone8
        with d3

    jump back_from_panties
        
###################REQUEST_04 (Level 02) (Touch tits's through fabric.)###############################
label new_request_04:
    hide screen hermione_main 
    with d3
    m "{size=-4}(I will molest her tits a little. Won't even ask her to bare them for me. Pretty harmless stuff.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    
    
    if whoring <=2: # LEVEL 01 # Hermione refuses.
        jump too_much
        
    elif whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. 
        $ new_request_04_01 = True # Hearts. 
        $ new_request_04_heart = 1
        hide bld1
        with d3
        m "Come closer [hermione_name]..."
        her_[2] "Ehm... alright..."
        hide screen bld1
        with d3
        
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        hide screen hermione_walk_01
        
        her_[2] "[genie_name].....?"
        menu: 
            m "..."
            "\"I'm gonna molest your tits now.\"":
                her_[3] "What? What do you mean, [genie_name]--?"
                ">Hermione takes a hesitant step back..."
                ">You reach out swiftly and grab both of her tits through her uniform..."
            "-Just reach out and grab her tits.-":
                ">You reach out with both of your hands and grab the [hermione_name]'s tits!"
        stop music fadeout 1.0
        with hpunch
        her_[7] "!!!?"
        her_[8] "[genie_name]?!"
        ">Hermione tries to pull away from you, but you hold her firmly by her breasts..."
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her_[9] "[genie_name], what are you--?"
        ">She tries to pull away again."
        ">You squeeze her tits like a vice."
        her_[10] "[genie_name], you're hurting me!"
        g4 "Then stand still, [hermione_name]!"
        her_[11] "B-but..."
        m "All I want to do is squeeze your tits a little, then you will get your points!"
        her_[12] "B-but... this is..."
        m "Just stand still..."
        m "go to your happy place or something..."
        her_[11] "M-my happy place...?"
        ">You feel the girl's shapely breasts in your palms..."
        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause
        her_[13] "............................"
        menu:
            "-Squeeze her tits with all of your strength-":
                show screen blktone
                with d5
                ">You put strength into your hold..."
                her_[12] "my..........."
                ">You squeeze her tits even harder..."
                her_[13] "[genie_name], you're hurting them..."
                m "Be quiet [hermione_name]..."
                her_[12] "aw.............."
                ">You squeeze her ample tits with all your strength."
                her_[10]"Ah! It hurts!"
                her_[10] "They're gonna burst! Please stop it!"
                m "They are not going to burst, you silly girl..."
                ">You losen your grip a little..."
                her_[13] "It hurts..."
                m "You will be fine..."
                her_[4] "........."

            "-Give her tits a tender massage-":
                show screen blktone
                with d5
                ">You start massaging Hermione's beasts through her uniform..."
                her_[13] "[genie_name]...?"
                m "The points, [hermione_name]... You need the points. Concentrate on that."
                her_[4] "Yes..."
                her_[15] "Yes, for the honour of the \"gryffindor\" house..."
                "*Squeeze-squeeze!*"
                ">You keep massaging her tits..."
                ">You give one of her breasts a few pinches trying to locate the nipple..."
                her_[13] "[genie_name]... you're pinching me...?"
                ">Your attempts prove to be fruitless though. The fabric of the uniform is quite thick..."
                her_[15] "\"gryffindor\" ............"

            "-Let her go and give her the points-":
                show screen blktone
                with d5
                m "Well if you gonna make a drama out of this, you might as well leave..."
                show screen blkfade
                with d5
                ">You unhand the girl's breasts..."
                her_[14] "Really?"
                m "Yes, yes... I will even give you your points..."
                her_[14] "Err... thank you, [genie_name]..."
                m "But you didn't earn them today..."
                her_[12] "Aw........."

    if whoring >= 6: # LEVEL 03 and higher # Hermione doesn't mind. <============================================================================EVENT LEVEL: 03
        if whoring >= 6 and whoring <= 8: # LEVEL 03.
            $ new_request_04_02 = True # Hearts.
            $ new_request_04_heart = 2
        else:
            $ new_request_04_03 = True # Hearts.
            $ new_request_04_heart = 3
        stop music fadeout 2.0
        m "Come closer [hermione_name]... I want to give your tits a massage..."
        her_[14] "As you say, [genie_name]..."
        
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        hide screen hermione_walk_01
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        ">Hermione is starting to pull her uniform up..."
        m "No, leave it on. I want to massage them while you are fully dressed..."
        her_[14] "Oh, I see..."
        ">Hermione stands in front of you expectantly..."
        ">You reach out for her ample breasts..."
        ">And start massaging them firmly..."

        hide screen genie
        show screen ctc
        show screen bld1
        show screen chair_02 #Genie's chair.
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        pause

        "*squeeze-squeeze-squeeze*"
        her_[16] "................"
        menu:
            "\"Do you enjoy this, [hermione_name]?\"":
                her_[14] "What...?"
                her_[14] "Oh, I don't mind it..."
                "*squeeze-squeeze-squeeze*"
                ">You keep massaging her soft tits..."
                if whoring <= 12:
                    her_[16] "I mean, this is not a big deal, as long as I am getting paid..."
                    ">You keep on massaging her tits through her uniform..."
                    her_[1] "A small price to pay for the honour of my house, really......{image=textheart}"
                else:
                    m "Really? It seems to me as if you love it"
                    her_[16] "I wouldn't say that I love it"
                    ">You keep on massaging her tits through her uniform..."
                    m "What would you say then [hermione_name]?"
                    her_[6] "I just like it, {size=-4}a lot{image=textheart}{/size}"
            "-Pull on them abruptly with force-":
                show screen blktone8
                with d3
                ">You give Hermione's tits a sudden but firm pull..."
                with vpunch
                her_[9] "Ouch...."
                ">You pull on her tits again. This time much stronger."
                with vpunch
                her_[9] "Ouch! [genie_name], what are you trying to do...?"
                ">You jerk the girl down by her tits with all your strength..."
                with vpunch
                with vpunch
                ">Hermione almost loses balance..."
                her_[17] "*Panting* What are you doing, [genie_name]...?"
                her_[18] "You don't need to be so rough with me....{image=textheart}"
    
    if whoring <= 5:
        $ whoring +=1
        
    show screen blkfade 
    with d3
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    hide screen bld1
    hide screen chair_02 #Genie's chair.
    hide screen groping_03
    hide screen blktone8
    show screen genie
    show screen hermione_01 #Hermione stands still.


    stop music fadeout 1.0
    ">You let go of Hermione's breasts..."
    m "This will do for now."
    her_[4] "................"
    
    hide screen blkfade 
    with d3
    
    if whoring <= 12:
        $ gryffindor +=15
        m "The \"Gryffindor\" house gets 15 points!"
    else:
        m "you may leave now [hermione_name]"
    
    $ request_04_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    hide screen hermione_main
    with d3
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    
    call her_main("..................","body_29")
    her "Thank you [genie_name]..."
    if daytime:
        her "Now if you don't mind I'd better go. The classes are about to start."
    else:
        her "I'd better go now. It's getting pretty late..."
    
    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    call her_walk(400,610,2)
    
    if whoring >= 13:
        show screen hermione_01_f
        her_[12] "(What about my points?)"
        if whoring >= 20:
            her_[16] "(eh, who cares)"
        else:
            her_[2] "(I'll just ask him about it next time)"
        hide screen hermione_01_f
    
    jump end_hermione_personal_request
    
###################REQUEST_05 (Level 02) (BUTT MOLESTER).
label new_request_05:
    hide screen hermione_main 
    with d3
    m "{size=-4}(I'll just molest her butt a little.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request

    
    if whoring <=2:
        jump too_much
        
    if whoring >= 3 and whoring <= 5:
        $ level = "02"
        $ new_request_05_01 = True # HEARTS.
        $ new_request_05_heart = 1
    elif whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_05_02 = True # HEARTS.
        $ new_request_05_heart = 2
    elif whoring >= 9:
        $ level = "04"
        $ new_request_05_03 = True # HEARTS.
        $ new_request_05_heart = 3
        
        
    if whoring >= 3 and whoring <= 5: # LEVEL 02 # Hermione is hesitant. <=================================================================================== FIRST EVENT.
        
        hide bld1
        with d3
        m "Come closer, child. Let me molest your butt a little."
        if request_05_points == 0 and whoring <= 5: #First time
            stop music fadeout 5.0
            her_[7] "[genie_name]!?"
            m "Relax, [hermione_name]. It will be the easiest 15 points you've ever made, I promise."
            her_[8] "But...."
            m "All I am going to do is squeeze your little butt a couple of times..."
            her_[4] "This is inappropriate, [genie_name]................"
            m "Nobody needs to know how exactly you got the points..."
            her_[12] "(These 15 points could really make a difference...)"
            her_[19] "(Darn it.....!)"
        else:
            her_[4] "Again.....?"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        her_[4] ".................."
        her_[4] "Do you want me to turn around then, [genie_name]?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around, [hermione_name].\"":
                her_[4] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_[4] "............."
                her_[4] "..........................."
                her_[25] "[genie_name], I would like to be done with this sooner rather then later..."
                m "Don't rush me [hermione_name]... Let me savour the moment..."
                her_[4] "............................."
                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        her_[22] "!!!!!!!!!!!!!"
                        her_[22] "[genie_name]!!?"
                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                her_[25] "......................."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                her_[21] "!!!!!!!!!!!!!"
                                her_[15] "[genie_name], what are you doing!?"
                                her_[15] "You said all you were going to do is touch!"
                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        her_[25] "......................."
                                        pass
                                    "-Give her butt another slap-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        her_[15] "Ouch! It hurts!"
                                        her_[20] "This is so demeaning!"
                                        her_[20] "You said all you were going to do is touch..."
                                        #her_[20] "Why are you doing this, [genie_name]?"
                                        g4 "Just stand still, [hermione_name]!"
                                        her_[19] "I don't think so, [genie_name]!"
                                        her_[24] "No amount of points are worth this humiliation!"
                                        her_[23] "You are abusing your power, [genie_name]!"
                                        g4 "What?"
                                        her_[19] "I'm leaving!"
                                        menu:
                                            g4 "Tsk..."
                                            "\"I... I apologize...\"":
                                                her_[25] "Just don't do this anymore, [genie_name]..."
                                                pass
                                            "\"You are not getting any points for this!\"":
                                                $ mad += 30
                                                her_[20] "Ha! See if I care, [genie_name]!"
                                                ### Takes place aftre you refuse to pay her the points.
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_walk_01_f 
                                                with fade
                                                pause 2
                                                hide screen hermione_walk_01_f 
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                with Dissolve(.3)
                                                pause.5
                                                g4 "Tsk! (You little brat!)"
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu
                                            "\"I'm subtracting points from you then!\"":
                                                $ mad += 20
                                                her_[22] "You can't be serious!?"
                                                $ gryffindor -=10
                                                g4 "The \"Gryffindor\" house, minus 10 points!"
                                                g4 "There! It's done!"
                                                her_[24] "Gr..........."
                                                her_[24] "........................"
                                                her_[27] "This is not fair..."
                                                m "What? Hey, wait, don't you start crying on me..."
                                                her_[29] "I hate you, [genie_name]! I hate you!"
                                                
                                                $ walk_xpos=300 #Animation of walking chibi. (From)
                                                $ walk_xpos2=610 #Coordinates of it's movement. (To)
                                                $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                                                hide screen no_groping_02
                                                hide screen bld1
                                                show screen genie
                                                show screen hermione_run
                                                with fade
                                                pause.9
                                                hide screen hermione_run
                                                with Dissolve(.3)
                                                $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                                                m ".............."
                                                menu:
                                                    "\"Dammit. Now I feel like crap...\"":
                                                        $ mad -= 5
                                                        m "Dammit... Now I feel like crap..."
                                                        m "But who could resist slapping that little behind of her's?"
                                                    "\"She made me do this, that brat!\"":
                                                        $ mad += 9
                                                        m "She made me do this, that brat!"
                                                        m "Acting all wounded now..."
                                                        m "I bet she actually enjoyed the slapping and just won't admit it..."
                                                $ request_05_points += 1
                                                if daytime:
                                                    $ hermione_takes_classes = True
                                                    jump day_main_menu
                                                else:
                                                    $ hermione_sleeping = True
                                                    jump night_main_menu     
        
                pause
                show screen groping_02
                with d7
                her_[7] "!!!!!!?"
                m "What is it, [hermione_name]?"
                her_[15] "It's nothing [genie_name]..."
                her_[15] "It's just... "
                her_[15] "I can't believe this is really happening..."
                her_[15] "This is so... inappropriate..."
                m "Relax, [hermione_name]. It's not like you are enjoying this..."
                her_[19] "What? Of course not! This is depraved..."
                her_[19] "I am making this sacrifice for the the honour of my house..."
                m "Yes, concentrate on that..."
                her_[20] "...................."
                show screen bld1
                with d3
                pause
                her_[17] "But, [genie_name]..."
                her_[5] "Why are {size=+7}you{/size} doing this?"
                menu: 
                    m "Hm..."
                    "\"I have my reasons...\"":
                        her_[12] "Oh..."
                        her_[25] "Hm..."
                    "\"In the name of science of course!\"":
                        her_[3] "Really?!"
                        her_[3] "Is this a research of some kind?"
                        m "Yeah, sure, I'm researching ehm... er..."
                        m "Well, you wouldn't understand, this is some pretty advanced wizardry stuff..."
                        her_[3] "I see..."
                        her_[2] "Well, if it is for a research then I am glad to be of help..."
                    "-Just squeeze her butt cheeks tighter-":
                        ">You give Hermione's butt cheeks a couple of extra firm squeezes."
                        her_[5] "...................."
                        her_[12] "(Shall I just be quiet then.....?)"
                show screen blktone8
                with d3
                ">You keep on playing with Hermione's buttocks..."
                ">You slide your hands up and down her inner tighs..."
                her_[15] "................"
                label connection_of_rapes:
                menu:
                    "-Slide your hands under her panties-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        her_[7] "[genie_name]... What are you...?"
                        m "That's alright, just think about those 15 points your house is about to receive..."
                        her_[12] "............."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                her_[7] "[genie_name]? No! What are you...?"
                                ">Hermione tries to pull away from you..."
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">Also it is relatively dry... Doesn't look like Hermione's taking any pleasure in this..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_[7] "[genie_name]? No! What are you doing!?"
                                ">Hermione tries to pull away from you..."
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        her_[30] "!!?"
                                        ">It's very tight and warm inside..."
                                        jump screams_of_rapings
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            "\"No. Just stand still, [hermione_name].\"":
                her_[4] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                her_[1] "[genie_name], please hurry up, before someone discovers us like this..."
                m "What is the problem, [hermione_name]?"
                m "You know you are doing this for your house."
                her_[4] "I do know."
                her_[4] "But not everyone would see it that way..."
                her_[4] "So let us be done with this as quick as possible..."
                her_[5] "Please..."
                m "Well, if you insist..."
                show screen groping_01
                with d7
                her_[7] "!!!"
                m "What is it?"
                her_[5] "It's nothing, [genie_name]. Your hands are cold, that's all..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                her_[4] "........................."
                ">You give her buttocks a good squeeze..."
                her_[19] "................."
                m "Don't look away, [hermione_name]. I want you to look into my eyes."
                her_[19] "I would rather not, [genie_name]..."
                menu:
                    m "..."
                    "\"Fine. Just keep standing still then.\"":
                        her_[15] "Thank you [genie_name]..."
                        ">You massage her buttocks lightly..."
                        her_[15] "...................."
                        ">And keep enjoying the sensation of her ass under your hands..."
                        her_[19] "....................."
                        ">Then you give Hermione's butt one last squeeze."
                        her_[19] "....................."
                    "\"Open your eyes, or lose the points!\"":
                        $ mad += 7
                        her_[19] "Tsk! {size=-5}(You perverted old--{/size}"
                        m "Did you say something, [hermione_name]?"
                        her_[8] "It's nothing, [genie_name]."
                        ">You massage her buttocks lightly..."
                        ">Hermione maintains the eye contact as she's been told..."
                        her_[8] "...................."
                        her_[4] "..............................."
                        m "What did I tell you about looking away?"
                        her_[19] "Yes, I remember..."
                        her_[8] "................................."
                        her_[25] "..................................."
                        her_[25] ".................................................."
                        ">You keep on enjoying the sensation of her soft ass-cheeks under your fingertips..."
                        her_[8] "....................."
                        jump connection_of_rapes
    
        
    elif whoring >= 6: # LEVEL 04 # Hermione is hesitant. <=================================================================================== SECOND EVENT.
        $ new_request_05_02 = True # HEARTS.
        $ new_request_05_heart = 2
        hide screen bld1
        with d3
        m "Come closer, [hermione_name]. Let me molest your butt a little."
        her_[17] "If I must..."
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        pause.5
        her_[18] "Do you want me to turn around then, [genie_name]?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        menu:
            m "Hm..."
            "\"Yes. Turn around, [hermione_name].\"":
                her_[18] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_02
                with d1
                hide screen blkfade
                with d5
                pause
                her_[35] "............."
                menu:
                    m "Hm..."
                    "-Give her butt a squeeze-":
                        pass
                    "-Give her butt a slap-":
                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                        show screen white
                        with hpunch
                        pause.08
                        hide screen white
                        show screen bld1
                        her_[22] "!!!!!!!!!!!!!"
                        her_[18] "[genie_name]....?"
                        menu:
                            "\"Fine, fine... I just couldn't resist....\"":
                                her_[18] "It's Ok..."
                                pass
                            "-Give her butt another slap-":
                                $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                show screen white
                                with hpunch
                                pause.08
                                hide screen white
                                show screen bld1
                                her_[21] "!!!!!!!!!!!!!"
                                her_[18] "[genie_name], what are you doing!?"
                                her_[18] "You said all you are going to do is touch!"
                                menu:
                                    "\"Fine, fine... I just couldn't resist....\"":
                                        her_[18] "It's not a big deal..."
                                        pass
                                    "-Give her butt another slap-":
                                        $ renpy.play('sounds/slap_02.mp3') #SLAP!
                                        show screen white
                                        with hpunch
                                        pause.08
                                        hide screen white
                                        show screen bld1
                                        her_[34] "[genie_name], not so loud, please..."
                                        her_[34] "What if somebody hears us?"
                                        m "Alright, alright... proceeding with groping then..."
                                        her_[18] "................"

                pause
                show screen groping_02
                with d7
                her_[18] "..................."
                m "You are being awfully quiet today, [hermione_name]."
                her_[18] "Am I...?"
                if whoring <= 13:
                    her_[35] "Well, you know me, [genie_name]..."
                    her_[35] "I'm just happy to be able to do my part for the \"Gryffindor\" house...."
                her_[35] "Please don't mind it and continue..."
                her_[18] "(...to grope me...)"
                show screen blktone8
                with d3
                ">You keep on playing with Hermione's ass..."
                ">And continue sliding your hands up and down her inner tighs..."
                her_[18] "................"
                label connection_of_rapes_02:
                menu:
                    "-Slide your hands under her panties-":
                        ">You slowly slide one of your hands under the fabric of the girl's panties..."
                        her_[17]"[genie_name]... What are you...?"
                        if whoring <= 13:
                            m "It's alright, just think about those 15 points your house is about to receive..."
                        else:
                            m "It's alright, just try to relax and enjoy yourself"
                        her_[17] "As you say..."
                        menu:
                            "-Prod her pussy with one of your fingers-":
                                show screen blkfade
                                with d3
                                ">You slide one of your fingers down and place it against the girl's little slit..."
                                her_[18] "[genie_name]?" 
                                menu:
                                    "-Force your finger into her pussy!-":
                                        ">You force one of your fingers into her little pussy..."
                                        ">It's very tight and warm..."
                                        ">it is quite wet as well...  Seems like Hermione's taking pleasure in this..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Prod her butt-hole instead-":
                                show screen blkfade
                                with d3
                                ">You place your one of your thumbs against the girl's little butt-hole..."
                                her_[18] "[genie_name]? What are planning on doing?"
                                menu:
                                    "-Force your thumb into her butt-hole-":
                                        ">You force one of your thumbs into her little butt-hole..."
                                        with hpunch
                                        her_[36] "ah... your finger is up my..."
                                        ">It's very tight and warm inside..."
                                        jump screams_of_pleasure
                                    "-Let the girl go...-":
                                        pass
                            "-Stop pushing your luck. Dismiss the girl-":
                                pass
                    "-No. That's enough for today. Dismiss her-":
                        pass
            "\"No. Just stand still, [hermione_name].\"":
                her_[4] "As you say, [genie_name]..."
                hide screen hermione_walk_01
                hide screen genie
                show screen ctc
                show screen no_groping_01
                with d1
                hide screen blkfade
                with d5
                pause
                her_[1] "[genie_name], please hurry up, before someone discovers us like this..."
                m "What's the problem, [hermione_name]?"
                m "You know you are doing this for your house."
                her_[4] "I do know."
                her_[4] "But not everyone would see it that way..."
                her_[4] "So let us be done with this as quick as possible..."
                her_[5] "Please..."
                m "Well, if you insist..."
                show screen groping_01
                with d7
                her_[7] "!!!"
                m "What is it?"
                her_[5] "nothing, [genie_name]. Your hands are cold, that's all..."
                show screen bld1 
                with d3
                show screen blktone8
                with d3
                ">You run your hands up and down Hermione's legs..."
                her_[4] "........................."
                ">And give her Ass a good squeeze..."
                her_[19] "................."
                m "Don't look away, girl. I want you to look into my eyes."
                her_[19] "I would rather not, [genie_name]..."
                menu:
                    m "..."
                    "\"Fine. Just keep on standing still then.\"":
                        her_[15] "Thank you [genie_name]..."
                        ">You massage her ass-cheeks lightly..."
                        her_[15] "...................."
                        ">And keep enjoying the sensation of her butt under your hands..."
                        her_[19] "....................."
                        ">Then You give Hermione's butt one last squeeze."
                        her_[19] "....................."
                    "\"Open your eyes, or you'll lose the points!\"":
                        $ mad += 20
                        her_[19] "Tsk! {size=-5}(You perverted old--{/size}"
                        m "Did you say something, [hermione_name]?"
                        her_[8] "It's nothing, [genie_name]."
                        ">You massage her ass-cheeks lightly..."
                        ">Hermione maintains eye contact as she's been told..."
                        her_[8] "...................."
                        her_[4] "..............................."
                        m "What did I tell you about looking away?"
                        her_[19] "Yes, I remember..."
                        her_[8] "................................."
                        her_[25] "..................................."
                        her_[25] ".................................................."
                        ">You keep enjoying the sensation of her soft buttocks under your fingertips..."
                        her_[8] "....................."
                        jump connection_of_rapes_02  
        
        
        
        
        
        
        
  
  
  
  
  
  
  
  
    
        
    label ending_of_screams_of_pleasure:
    if whoring <= 5:
        $ whoring +=1
    show screen blkfade 
    with d5
    
    stop music fadeout 1.0
    ">You let go of her ass..."
    m "This will do for now."
    
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with d1
    
    hide screen blkfade
    with d3
    if whoring <= 13:
        $ gryffindor +=15
        m "The \"Gryffindors\" get 15 points!"
    else:
        m "good night [hermione_name]"
    $ request_05_points += 1
   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    hide screen hermione_main
    with d3
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    
    call her_main("..................","body_29")
    her "Thank you [genie_name]..."
    if daytime:
        her "Now if you don't mind I'd better go. The classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    # $ hermione_chibi_xpos = 610 #Near the desk.
    
    call her_walk(400,610,2)
    
    if whoring >= 3 and whoring <= 5: #First level. Not happy.
        show screen hermione_01_f #Hermione stands still.
        her_[12] "..........................."
        hide screen hermione_01_f #Hermione stands still.
        
    jump end_hermione_personal_request
        
###################REQUEST_08 (Level 03) (Show me tits). #####################################################################################################################
label new_request_08: #LV.3 (Whoring = 6 - 8)
    hide screen hermione_main 
    with d3
    if request_08_points == 0:
        m "{size=-4}(I feel like gazing upon those titties.){/size}"
    else:
        m "{size=-4}(I feel like gazing upon those titties again.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    if whoring <=5:
        jump too_much
        
    if "power_girl" in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                m "Power girl."
                if whoring >= 15:
                    $ changeHermioneMainScreen(hg_pth+"body_30.png")
                    her "In that ridiculous costume?"
                    m "It's not that bad. It has a nice cape."
                    $ changeHermioneMainScreen(hg_pth+"body_34.png")
                    her "..."
                    $ changeHermioneMainScreen(hg_pth+"body_33.png")
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 7
                    $ panties = False
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass
        
    hide screen hermione_main
    with d3
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_ypos = 0
    $ current_payout = 25 #Used when haggling about price of th favor.
        
    if request_08_points == 0 and whoring <= 11: # LEVEL 04 # FIRST TIME.
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]...","body_03")
        m "How much will it cost me to see your tits?"
        stop music fadeout 1.0
        call her_main("How much will it cost you to...?","body_14")
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        call her_main("[genie_name]!","body_30")
        m "Hm... I thought your house could use some extra points..."
        m "But I guess I was wrong..."
        call her_main(".........?","body_31")
        m "Please don't mind me..."
        m "All I want to do is help you..."
        call her_main(".............","body_29")
        call her_main("200 house points, [genie_name].","body_33")
        m "So if I give you 200 house points, [hermione_name]..."
        m "You will shamelessly bare your melons before me?"
        call her_main("[genie_name]! No need to be so vulgar!","body_47")
        her "I think I'd better go..."
        menu:
            "\"Wait. 200 points are yours. Show me!\"":
                $ current_payout = 200 #Used when haggling about price of th favor.
                call her_main("Really?","body_14")
                m "Well?"
                call her_main("......................................","body_29")
                her "You have to promise me not to touch them, [genie_name]."
                m "Sure, sure..."
                call her_main("I am only doing this for the honour of my house, [genie_name]!","body_32")

            "\"I will give you 5 points to see your tits.\"":
                call her_main("Five?!","body_72")
                call her_main("[genie_name], I am not going to expose myself for a meagre five points!","body_76")
                m "Well, your tits sure aren't worth 200, [hermione_name]!"
                call her_main("(They aren't?)","body_73")
                call her_main("Maybe one hundred then?","body_69")
                menu:
                    "\"Fine. 100 it is! Bare them already!":
                        $ current_payout = 100 #Used when haggling about price of th favor.
                        her "................."
                        her "So be it... For a hundred points..."
                    "\"25 house points that's my final offer!\"":
                        her "..............."
                        her "Well, so be it..."
            "\"Fine, leave. I don't care...\"":
                $mad = +12
                her "Tsk!"
                call music_block
                jump could_not_flirt
                
                
        hide screen blktone
        with d3
        hide screen bld1
        with d3
        hide screen hermione_main
        with d5
        $ menu_x = 0.5 #Default menu position restored.
        show screen ctc
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        pause
        show screen hermione_04
        with fade
        pause
        show screen bld1
        with d3
        m "Hm..."
        her_[12] "{size=-5}(My breasts are completely exposed...){/size}"
        m "Come closer [hermione_name], let me take a better look..."
        her_[4] "............"
        
        hide screen bld1
        with d3

        show screen blkfade #Completely black screen.
        with Dissolve(1)
        pause.5
        ">Hermione slowly walks towards your desk."
        ">With every step she takes her ample tits bounce a little..."
       
        hide screen hermione_04 #Stands with tits out.
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        her_[1] "............"
        m "Very good..."
        her_[4] "....."
        
        $ badges = False
        $ lift_shirt = True
    
        show screen blktone 
        with d3
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        #$ only_upper = True #No lower body displayed. 
        call her_main("","body_81")
        pause
        her "...................................."
        
        
        
    else:
        if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
            m "[hermione_name]?"
            her_[2] "Yes, [genie_name]?"
            m "I need to see your tits."
            her_[4] "............"
            her_[4] "Do you promise not to touch, [genie_name]?"
            m "Of course."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            hide screen hermione_main
            with d5
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Hermione slowly walks towards your desk."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Very good..."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            show screen blktone 
            with d3
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #$ only_upper = True #No lower body displayed. 
            $ badges = False # Hides any badges from hermione_main screen.
            $ lift_shirt = True
            
            if whoring >= 17:
                call her_main("","body_84")
            else:
                call her_main("","body_81")
            
            pause
            her "...................................."
            
            
            
            
            
            
        elif whoring >= 9: # LEVEL 04 and higher# <=================================================================================== SECOND EVENT and THIRD EVENT. (HERMIONE IS INDIFFERENT) 
            m "I need to see your tits, [hermione_name]."
            if whoring >= 17:
                her_[16] "Of course [genie_name]?"
            else:
                her_[15] "Are you only going to watch, [genie_name]?"
                m "Of course..."
            hide screen blktone
            with d3
            hide screen bld1
            with d3
            hide screen hermione_main
            with d5
            $ menu_x = 0.5 #Default menu position restored.
            show screen ctc
            pause
            show screen hermione_04
            with fade
            pause
            show screen bld1
            with d3
            m "Hm..."
            m "Come closer [hermione_name], let me take a better look..."
            hide screen bld1
            with d3
            show screen blkfade #Completely black screen.
            with Dissolve(1)
            pause.5
            ">Hermione slowly walks towards your desk."
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen ctc
            show screen genie_and_tits_01
            with d1
            hide screen blkfade
            with d5
            pause
            show screen bld1
            with d3
            m "Very good..."
            show screen blktone 
            with d3
            
            hide screen hermione_main
            with d3
            $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
            #$ only_upper = True #No lower body displayed. 
            
            if custom_outfit == 7:
                $ custom_outfit = 7.2
            else:
                $ badges = False # Hides the layer with badges.
                $ lift_shirt = True
            
            call her_main("","body_84")
            pause
            her "...................................."
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    menu:
        "\"Break your promise. Grab the tits!\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT. HERMIONE OUTRAGED.
                hide screen hermione_main
                $ only_upper = False #No lower body displayed. 
                with d3
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                her_[7] "[genie_name], what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                
                m "Relax, [hermione_name]. Just stand still!"
                m "Oh... Those are some nice titties you've got..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_[13] "No, [genie_name], please! You mustn't do this..."
                m "This won't take long, just stand still."
                her_[24] "[genie_name], I didn't agree to this!"
                with hpunch
                her_[23] "You must unhand me now!!!"
                show screen blkfade
                with d5
                ">Hermione pulls away from you and covers up hastily."
                her_[19] "I think I'd better go..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                m "Go ahead, [hermione_name]. You are not getting paid if you do..."
                her_[19] "But I showed you my..."
                her_[24] "And you touched me..."
                her_[23] "And I am getting nothing?"
                m "You are dismissed, [hermione_name]..."
                her_[19]  "Gr.................."
                her_[19] "{size=-5}(Burn in hell, you wretched old---{/size}"
                $ mad += 22
                call music_block
                jump could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT. A BIT ANGRY.
                hide screen hermione_main
                with d3
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                her_[7] "[genie_name], what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Relax, [hermione_name]. Just stand still!"
                her_[4] "I didn't agree to this, [genie_name]..."
                her_[4] "I don't think you should..."
                m "Don't you like it...?"
                her_[12] "What?"
                m "Don't you like it how I squeeze and pull on your breasts?"
                her_[12] "..............."
                m "Admit it, you like it a little bit..."
                her_[12] "{size=-5}(So strange to see my breasts in someone else's hands...){/size}"
                her_[13] "[genie_name], I am letting you do this to me to help my house out, nothing more!"
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_[4] "Please, unhand me now!"
                show screen blkfade
                with d5
                ">Hermione pulls away from you suddenly and covers up."
                her_[4] "You promised not to touch, [genie_name]..."
                m "It was hard to resist..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                her_[1] "............."
                her_[9] "Can I get paid now please?"
                m "Sure..."
                $ mad += 9
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT. ENJOYS A LITTLE.
                hide screen hermione_main
                with d3
                $ only_upper = False #No lower body displayed. 
                show screen blkfade
                with d3
                ">You reach out and dig your fingers into the girl's ample flesh..."
                her_[7] "[genie_name], what are you doing?"
                hide screen blkfade
                hide screen blktone8
                hide screen blktone
                show screen chair_02 #Genie's chair.
                hide screen bld1
                show screen groping_naked_tits
                with fade
                pause
                show screen bld1
                with d3
                m "Relax, [hermione_name]. Just stand still!"
                her_[12] "But..."
                her_[13] "ah...{image=textheart}"
                her_[12] "I didn't agree to this..."
                m "But you like it, don't you?"
                if whoring >= 17:
                    her_[17] "I love it [genie_name]!{image=textheart}"
                else:
                    her_[13] "I do not, [genie_name]!{image=textheart}"
                show screen blktone
                with d3
                ">You give her tits a couple of firm squeezes..."
                hide screen blktone
                with d3
                if whoring >= 17:
                    her_[18] "[genie_name], you promised not to touch..."
                    m "I know, I know... But it's hard to resist..."
                    her_[6] "................."
                else:
                    her_[15] "[genie_name], you promised not to touch..."
                    m "I know, I know... But it's hard to resist..."
                    her_[20] "................."
                her_[6] "....................ah...{image=textheart}"
                her_[6] "[genie_name], you need to stop now..."
                m "Just a bit longer..."
                show screen blktone8
                with d3
                ">You keep on massaging the girl's breasts..."
                hide screen blktone8
                with d3
                her_[37] "[genie_name]... please, stop this..."
                m "Why? Because you like it too much?"
                her_[18] "No it's not that..."
                her_[17] "I mean..."
                show screen blktone8
                with d3
                ">You pull the tits in opposite directions and then squish them together..."
                hide screen blktone8
                with d3
                her_[38] "Ah...{image=textheart} [genie_name], I really need to go..."
                if daytime:
                    her_[17] "That's right... the classes are about to start..."
                else:
                    her_[17] "It is getting late..."
                m "Well, alright..."
                show screen blkfade
                with d5
                ">You let go of the girl's breasts..."
                ">Hermione covers up..."
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                if if whoring >= 17:
                    her_[18] "Please don't think I forgot that you broke your promise, [genie_name]."
                else:
                    her_[25] "Please don't think I forgot that you broke your promise, [genie_name]."
                m "Right..."
                hide screen blkfade
                hide screen chair_02 #Genie's chair.
                hide screen groping_naked_tits
                hide screen bld1
                show screen genie
                $ hermione_chibi_xpos = 400 #Near the desk.
                show screen hermione_02 #Hermione stands still.
                with d5
                pause
                show screen bld1
                if if whoring >= 17:
                    her_[17] "Thank you [genie_name]."
                else:
                    her_[35] "Can I have my payment now?"
                    $ mad +=7
   
        "\"Keep promise. Admire visually.\"":
            ">You take a long look at Hermione's naked tits..."
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                pause
                menu:
                    "-Nod your head in approval-":
                        ">You Look at the girl's tits for a while and then nod in approval..."
                        her "......................"
                    "-Shake your head in disapproval-":
                        $ mad += 3
                        ">You Look at the girl's tits for a while and then shake your head in disappointment..."
                        her ".....................?"
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                pause
                menu:
                    "\"A Nice set of tits you got there.\"":
                        call her_main("","body_83")
                        pause
                        her "Thank--"
                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        call her_main("...........","body_82")
                        call her_main("You are being inappropriate, [genie_name].","body_81")
                        
                    "\"Hm... I've seen better.\"":
                        $ mad += 7
                        her "Tsk..."
                        her "Are we done then?"
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                pause
                menu:
                    "\"You have great tits, [hermione_name].\"":
                        call her_main("You really think so [genie_name]?","body_82")
                        call her_main("I am glad you like them, [genie_name]...","body_84")
                    "\"Your tits are alright I suppose...\"":
                        call her_main("Huh?","body_82")
                        her "Does this mean you don't like them, [genie_name]?"
                        call her_main("I'm sorry...","body_85")
            ">You stare at her breasts for a while longer..."
            pause
            m "Alright, you can cover up, [hermione_name]..."
            her "............."
            hide screen hermione_main
            with d3
            $ only_upper = False #No lower body displayed. 
            show screen blkfade
            with d3
            ">Hermione covers up..."
            $ badges = True # Shows layer with badges.
            $ lift_shirt = False
            hide screen chair_02 #Genie's chair.
            hide screen genie_and_tits_01
            hide screen bld1
            hide screen blktone
            show screen genie
            show screen bld1
            $ hermione_chibi_xpos = 400 #Near the desk.
            show screen hermione_02 #Hermione stands still.
            with d5

        "\"Start jerking off.\"":
            if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.
                $ mad += 2
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her_[30] "[genie_name]?!!"
                m "Just stand still, [hermione_name]..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                ">You stare at Hermione's breasts with hunger..."
                her_[13] "[genie_name], what are you...?"
                ">You keep stroking your hard cock..."
                her_[12] "[genie_name], no..."
                her_[12] "You must... Put it away..."
                m "Stop whining [hermione_name]. I'm not touching you, am I?"
                her_[19] "But..."
                her_[20] "But I didn't agree to this!"
                her_[19]"I..."
                her_[19] "I think I'd better leave now!"
                menu:
                    "\"Leave now, and you'll get no points!\"":
                        $ only_upper = False
                        her_[21] "After {size=+5}this{/size}? Are you kidding me, [genie_name]?"
                        her_[21] "I showed you my..."
                        her_[25] ".........."
                        her_[24] "I am not going to sell you a single favour anymore, [genie_name]!"
                        show screen blkfade
                        with d3
                        ">Hermione pulls away from you and covers up..."
                        g4 "Don't you dare to leave me in this state, [hermione_name]!"
                        her_[10] "I am not setting a foot into your office ever again, [genie_name]!"
                        g4 "Come on, now. Just say something dirty! I'm almost there!"
                        her_[27] "You are a horrible person, [genie_name]..."
                        $ mad += 30
                        call music_block
                        jump could_not_flirt
                    "\"Alright, alright. That's enough for now.\"":
                        $ mad +=9
                        $ only_upper = False
                        pass
                    "-Start jerking your cock faster-":
                        $ mad += 35
                        $ only_upper = False
                        ">You start jerking your cock furiously!"
                        her_[23] "No, [genie_name], stop!"
                        ">You jerk it even faster!"
                        her_[25] "[genie_name], think I will be leaving now..."
                        g4 "No, wait, I'm almost there!"
                        show screen blkfade
                        with d3
                        her_[10] "Ew! [genie_name]!"
                        her_[10] "I'm leaving!"
                        call music_block
                        jump could_not_flirt
            elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                her_[30] "[genie_name]?"
                ">You stare at Hermione's breasts with hunger..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                her_[13] "[genie_name], I didn't agree to this..."
                m "What are you complaining about, [hermione_name]?"
                m "I'm not even touching you..."
                her_[13] "Yes, but you are... touching yourself, [genie_name]."
                ">You pick up the pace..."
                m "just stand still, [hermione_name]."
                m "It will be over soon."
                her_[13] ".................."
                her_[12] "(It's so big...)"
                m "Yes... Yes, like this..."
                m "Yes, with your tits all naked..."
                her_[12] ".............."
                her_[17] "well, so be it..."
                her_[17] "You can keep touching yourself, [genie_name]..."
                her_[1] "But you must promise me not to..."
                her_[5] "Not to... em..."
                her_[4] "Not to discharge..."
                her_[8] "Not in front of me, [genie_name]..."
                m "Fine, whatever..."
                m "Oh, you little slut. You nasty little slut!"
                her_[19] "......................."
                ">You start to stroke your cock even harder..."
                g4 "Yes, I know you want this! Yes!"
                her_[19] "................"
                show screen blkfade 
                with d3
                ">You are about to cum..."
                menu:
                    "-Hold it as promised-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        her_[15] "..............."
                        ">Hermione covers up..."
                    "-Just start cumming-":
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        g4 "Argh! You whore!"
                        her_[21] "Proff-- ??"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_[23] "[genie_name], no, you promised!"
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_[10] "[genie_name], how could you...?"
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        if custom_outfit == 0:
                            $ badges = False # Turns off badges from hermione_main screen.
                        $ sperm_on_tits = True
                        call her_main("","body_85")
                        pause
                        her "My uniform..."
                        her "It's ruined...."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        her "................"
                        her "I need to clean myslef up..."
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        with d3
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        hide screen blkfade
                        with d5
                        
                        $ badges = True # Turns badges back on from hermione_main screen.
                        $ lift_shirt = False
                        
                        call her_main("","body_47")
                        pause
                        #play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                        her "How could you do this to mr, [genie_name]?!"
                        her "You gave me your word!"
                        hide screen hermione_main
                        with d3
                        $ mad += 45
            elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
                hide screen hermione_main
                with d3
                ">You take your cock out and start stroking it..."
                show screen blkfade
                hide screen bld1
                with d3
                her_[6] "[genie_name]?"
                ">You stare at Hermione's breasts with hunger..."
                hide screen hermione_walk_01
                hide screen genie
                hide screen bld1
                show screen chair_02 #Genie's chair.
                hide screen blkfade
                hide screen blktone
                show screen jerking_off_01
                with d5
                pause
                
                show screen bld1
                with d3
                if whoring >= 17:
                    her_[16] "ah..."
                    her_[17] "It's so big..."
                    her_[18] "You just couldn't help yourself, could you [genie_name]?"
                    her_[16] ".................."
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    her_[16] ".............."
                    her_[17] "well, so be it..."
                    her_[1] "But you must promise me not to..."
                    her_[5] "Not to... ehm..."
                    her_[6] "Not to cum on me, [genie_name]..."
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    her_[16] "......................."
                    ">You start to stroke your cock even harder..."
                    g4 "Yes, I know you want this! Yes!"
                    her_[16] "................"
                    show screen blkfade 
                    with d3
                    # SAME AS PREVIOUS EVENT^^^
                else:
                    her_[13] "[genie_name], actually I never agreed to this..."
                    m "What are you complaining about, [hermione_name]?"
                    m "I'm not even touching you..."
                    her_[13] "Yes, but you are... touching yourself, [genie_name]."
                    #">You pick up the pace..."
                    m "Just stand still, bitch."
                    m "It will be over soon."
                    her_[13] ".................."
                    m "Yes... Yes, like this..."
                    m "Yes, with your tits all naked..."
                    her_[12] ".............."
                    her_[17] "well, so be it..."
                    her_[1] "But you must promise me not to..."
                    her_[5] "Not to... ehm..."
                    her_[4] "Not to discharge..."
                    her_[4] "Not in front of me, [genie_name]..."
                    m "Fine, whatever..."
                    m "Oh, you little slut. You nasty little slut!"
                    her_[12] "......................."
                    ">You start to stroke your cock even harder..."
                    g4 "Yes, I know you want this! Yes!"
                    her_[12] "................"
                    show screen blkfade 
                    with d3
                    # SAME AS PREVIOUS EVENT^^^
                menu:
                    g4 "Argh! (I'm about to cum!)"
                    "-Hold it in-":
                        g4 "Oh, alright..."
                        g4 "I'd better stop now I suppose..."
                        her_[12] "..............."
                        her_[12] "Ehm... I read that that is bad for you, [genie_name]..."
                        m "Huh?"
                        her_[13] "It is bad for your health to just hold it in like this..."
                        her_[12] "Em..."
                        her_[14] "If you want to you can--"
                        g4 "Argh! You whore!"
                        her_[7] "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_[9] "[genie_name], I didn't mean that you can release your... semen on me, [genie_name]..."
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_[18] "Well, what's done is done I suppose..."
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        $ sperm_on_tits = True
                        if custom_outfit == 0:
                            $ badges = False # Hides any badges from hermione_main screen.
                        call her_main("","body_85")
                        pause
                        her "My uniform is ruined though..."
                        m "Don't worry, I will give you your house points, [hermione_name]."
                        m "You did good."
                        call her_main("Thank you [genie_name].","body_84")
                        call her_main("Now I need to clean myself up...","body_83")
                        pause
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        $ badges = True # Shows badges on hermione_main screen.
                        $ lift_shirt = False
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        hide screen blkfade
                        with d5
                        call her_main("","body_45")
                        pause
                        her "Well, this should do for now..."
                        hide screen hermione_main
                        with d3
                    "-Just start cumming-":
                        g4 "Argh! You whore!"
                        her_[7] "???"
                        show screen white 
                        pause.1
                        hide screen white
                        pause.2
                        show screen white 
                        pause .1
                        hide screen white
                        with hpunch
                        g4 "Argh! YES!"
                        hide screen bld1
                        with d3
                        $ no_blinking = True #When True - blinking animation is not displayed. 
                        show screen jerking_off_cum
                        hide screen blkfade
                        hide screen bld1
                        with d3
                        pause
                        show screen bld1
                        with d3
                        her_[13] "ah...{image=textheart} It's so hot...{image=textheart}"
                        her_[9] "[genie_name], you promised..."
                        g4 "Oh, this is great, yes..."
                        $ no_blinking = False #When True - blinking animation is not displayed. 
                        hide screen jerking_off_cum
                        with d3
                        her_[15] "Well, what's done is done I suppose..."
                        m "Oh, this was quite amazing..."
                        show screen blktone8
                        with d3
                        $ badges = True # Hides any badges from hermione_main screen.
                        $ lift_shirt = False
                        $ sperm_on_tits = True
                        $ h_body = "01_hp/13_hermione_main/body_85.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        pause
                        her "My uniform is ruined though..."
                        m "Don't worry, I'm sure no one will notice."
                        m "You did good."
                        call her_main("Thank you [genie_name].","body_84")
                        call her_main("Now I need to clean myself up...","body_83")
                        pause
                        hide screen hermione_main
                        with d3
                        show screen blkfade
                        with d3
                        show screen genie
                        hide screen jerking_off_01
                        hide screen chair_02
                        show screen hermione_02
                        $ badges = True # Turns the badges layer back on.
                        $ lift_shirt = False
                        $ sperm_on_tits = False
                        $ only_upper = False
                        $ aftersperm = True
                        hide screen blkfade
                        with d5
                        $ badges = True # Hides any badges from hermione_main screen.
                        if custom_outfit == 7.2:
                            $ custom_outfit = 7
                        call her_main("","body_45")
                        pause
                        her "Well, this should do for now..."
                        hide screen hermione_main
                        with d3
                        

    
    $ badges = True # Hides any badges from hermione_main screen.
    $ lift_shirt = False
    hide screen jerking_off_01                   
    hide screen blktone8
    hide screen ctc
    hide screen bld1
    hide screen groping_01
    hide screen groping_02
    show screen hermione_02
    show screen genie
    with fade
    
    hide screen blkfade
    with d3

    if whoring <= 16:
        $ gryffindor +=current_payout
        m "The \"Gryffindor\" house gets [current_payout] points!"
    stop music fadeout 10.0

   
   
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    hide screen blkfade
    with Dissolve(1)
    
    hide screen hermion_main
    with d3
    $ h_xpos=370 #Defines position of the Hermione's full length sprite.
    $ h_ypos=0
    
    if whoring <= 16:
        call her_main("..................","body_29")
    else:
        call her_main("..................","body_74")
    her "Thank you [genie_name]..."
    if daytime:
        her "Now if you don't mind I'd better go. my classes are about to start."
    else:
        her "I'd better go now then. It's getting pretty late..."
    
    if whoring >= 6 and whoring <= 8:
        $ level = "03"
        $ new_request_08_01 = True # HEARTS.
        $ new_request_08_heart = 1
    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_08_02 = True # HEARTS.
        $ new_request_08_heart = 2
    if whoring >= 12:
        $ level = "05"
        $ new_request_08_03 = True # HEARTS.
        $ new_request_08_heart = 3

    hide screen bld1
    hide screen hermione_main
    with Dissolve(.3)
    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ panties = True
    
    if whoring <= 8:
        $ whoring +=1
    $ request_08_points += 1
    $ aftersperm = False #Shows cum stains on Hermione's uniform.
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    # $ hermione_chibi_xpos = 610 #Near the desk.
    
    call her_walk(400,610,2)
    
    show screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)    
    if whoring >= 6 and whoring <= 8: # LEVEL 03 # <=================================================================================== FIRST EVENT.    
        her_[12] "(How humiliating... What have I become...?)"
    elif whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== SECOND EVENT.
        her_[12] "........................"
    elif whoring >= 17 and aftersperm: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        her_[6] "{size=-5}(That was so exhilarating...){/size}"
        her_[37] "{size=-5}(I wonder if anyone will notice my uniform!){/size}"
        her_[37] "{size=-5}(What will people think of me?){/size}"
        her_[16] "................................."
    elif whoring >= 12: # LEVEL 05 # <=================================================================================== THIRD EVENT.
        her_[6] "{size=-5}(That was so humiliating...){/size}"
        her_[24] "{size=-5}(No, Hermione, you silly girl!){/size}"
        her_[24] "{size=-5}(We are doing this to protect the honour of our house!){/size}"
        her_[16] "................................."
    hide screen hermione_01_f #Hermione stands still.
    with Dissolve(.3)

    jump end_hermione_personal_request
        
###################REQUEST_11 (Level 04) (DANCE FOR ME AND SNAPE) (Day/Night) ################################################################
label new_request_11: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3
   
    m "{size=-4}(Ask her to dance for me?){/size}"

    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request

    if "heart_dancer" in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                m "A Dancer."
                if whoring >= 15:
                    $ changeHermioneMainScreen(hg_pth+"body_30.png")
                    her "A Dancer?"
                    m "Don't worry, your nipples will be covered."
                    $ changeHermioneMainScreen(hg_pth+"body_34.png")
                    her "..."
                    $ changeHermioneMainScreen(hg_pth+"body_33.png")
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 4
                    $ stockings = 0
                    $ panties = False
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass

    $ current_payout = 35 #Because will have option to pay extra.

    if request_11_points == 0: #<==============================EVENT 01
        
        m "[hermione_name], I need you to dance for me a little."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "You want me to..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "...dance for you, [genie_name]?"
        if whoring <=8:
            jump too_much
        $ new_request_11_01 = True # HEARTS
        $ new_request_11_heart = 1
        m "Yes... You think you could manage that?"
        her "Ehm... I suppose so..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Is this your official wish, [genie_name]?"
        with hpunch
        g4 "What did you just say!?"
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "I mean, favour. Is this an official favour [genie_name]?"
        show screen whitetone8
        hide screen blktone
        with Dissolve(1)
        hide screen hermione_main
        with Dissolve(1)
        g4 "(\"Is this your official wish, master....?\")"
        m "(Man, this sure brings back memories...)"
        m "(Agrabah and genie the joker...)"
        m "(A pre-akabur era of my life...)"
        m "(Simpler times...)"
        g4 "(The bastard ruined my life!)"
        her "Em... [genie_name]?"
        hide screen whitetone8
        with Dissolve(1)
        show screen hermione_main
        with d3
        call music_block
        her "[genie_name]..?"
        m "Hermione, right..."
        m "Got lost in my thoughts for a moment there..."
        her "So am I getting paid for this?"
        m "Of course, [hermione_name]!"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "So... Just a little dancing then..."
        m "Whenever you're ready..."
        her "................."
        hide screen hermione_main
        with d3
        ">Hermione starts dancing..."
        stop music fadeout 1.0
        hide screen blktone
        $ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos = 240 #Default: 250
        show screen clothed_dance #Hermione stands still.
        with fade
        m "Hm..."
        her_[12] "{size=-5}(...........................................){/size}"
        her_[4] "{size=-5}(This is silly...){/size}"
        ">Hermione looks embarrassed but she keeps on \"dancing\"..."
        m "..................."
        her_[4] "{size=-5}(...........................................){/size}"
        m "Alright, you can start undressing now."
        show screen hermione_02 #Hermione stands still.
        with hpunch
        her_[7] "??!"
        her_[8] "I thought all I had to do was dance?"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Really? That's adorable."
        m "Now start taking off those clothes."
        her_[12] "You want me to... strip for you...?"
        m "Yes. And I expect you to do it today, [hermione_name]."
        her_[19] "[genie_name]!"
        m "don't you raise your voice at me, [hermione_name]!"
        her_[7] ".....!!?"
        m "Nobody is forcing you to do this."
        m "I am doing you a favour!"
        m "If you don't need the points, please feel free to leave."
        her_[8] "....................."
        her_[12] "......................................."
        ">Hermione is starting to dance again..."
        show screen clothed_dance #Hermione stands still.
        with fade
        her_[15] "{size=-5}(...........................................){/size}"
        m "What are you waiting for then?"
        m "Start with the vest."
        her_[12] "............................................................."
        ">Hermione gives you a confused look and then takes off her vest..."
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        her_[19] "{size=-5}(Am I really going to do this?){/size}"
        menu:
            m "......................."
            "\"Now get rid of your skirt!\"":
                her_[19] "................................."
                show screen blktone
                with d3
                ">Hermione starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                hide screen blktone
                with d3
                her_[19] "{size=-5}(Here it comes then...){/size}"
                her_[24] "{size=-5}(For the honour of the \"Gryffindor\"....){/size}"
                ">Hermione takes of her  skirt..."
                show screen ctc
                pause
                show screen no_skirt_dance
                with d3
                pause
                m "..............."
                her_[19] "{size=-5}(.........................................){/size}"
                ">Hermione keeps on dancing..."
                m "Alright, your shirt is next!"
                her_[20] "My shirt....?"
                show screen blktone
                with d3
                ">Hermione looks extremely embarrassed..."
                ">She clumsily fumbles with the buttons of her shirt..."
                hide screen blktone
                with d3
                m "What's the problem, [hermione_name]?"
                her_[19] "I'm sorry, [genie_name]..."
                her_[19] "It's stuck..."
                her_[19] "It won't budge..."
                her_[28] "Why won't it budge?! *sob*"
                her_[28] "No, I can't do this, [genie_name]! *sob*"
                m "What?"
                her_[28] "I thought I could, but..."
                her_[28] "Stripping for you, [genie_name]?"
                her_[28] "People look up to me in this school!"
                her_[28] "I have a reputation...*sob*"
                her_[29] "And if I do this..."
            "\"Now take off your shirt!\"":
                her_[19] "................................."
                show screen blktone
                with d3
                ">Hermione starts to unbutton her shirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the last button is undone and she has no choice but to take the shirt off..."
                hide screen blktone
                with d3
                her_[19] "{size=-5}(Alright, here it comes...){/size}"
                her_[19] "{size=-5}(For the honour of the \"Gryffindor\"!){/size}"
                show screen blktone
                with d3
                ">Hermione takes off her shirt..."
                hide screen blktone
                with d3
                show screen ctc
                pause
                show screen no_shirt_dance
                with d3
                pause
                her_[40] "{size=-5}(I actually did it...){/size}"
                her_[40] "{size=-5}([genie_name] can see my breasts while I'm dancing for him...){/size}"
                her_[40] "{size=-5}(This is so demeaning...){/size}"
                her_[40] "{size=-5}(But I am doing this for my house...){/size}"
                m "Not bad...."
                her_[40] "{size=-5}(.........................................){/size}"
                show screen blktone
                with d3
                ">Hermione is topless now..."
                ">She keeps on dancing but seems very restricted in her movements now. Even more so than before..."
                ">It seems like she's desperately trying to prevent her breasts from bouncing or swaying..."
                hide screen blktone
                with d3
                m "Alright, your skirt is next!"
                her_[40] "...................."
                show screen blktone
                with d3
                ">Hermione looks extremely embarrassed..."
                show screen blktone8
                with d3
                ">She fumbles with the zipper of her skirt..."
                m "What's the problem, [hermione_name]?"
                her_[40] "I'm sorry, [genie_name]..."
                her_[40] "It's stuck..."
                her_[40] "It won't budge..."
                her_[40] "Why won't it budge?! *sob*"
                her_[41] "No, I can't do this, [genie_name]! *sob*"
                m "What?"
                her_[41] "I thought I could, but..."
                her_[41] "Stripping for points, [genie_name]?"
                her_[41] "People look up to me in this school!"
                her_[41] "I have reputation...*sob*"
                her_[42] "And If I do this..."
                
        show screen blkfade 
        with d3
        hide screen blktone8    
        ">Hermione quickly puts her uniform back on..."
        stop music fadeout 1.0
        show screen hermione_02 #Hermione stands still.
        hide screen blkfade
        with d3
        her_[31] "[genie_name], I think I'd better go now... *Sob!*"
        menu:
            "\"Alright. I had fun. Here are your points.\"":
                $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
                show screen hermione_main
                her "Really? I didn't ruin it completely then?"
                hide screen hermione_main
                pause.2 #Otherwise a bug occurs. 
                $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
            "\"Sure. You will receive no points though.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
                $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ h_body = "01_hp/13_hermione_main/body_02.png" #Flashing panties
                show screen hermione_main
                her "[genie_name]... I may not be very good at this..."
                her "But I did my best... I think I deserve some--"
                hide screen hermione_main
                m "Just make sure you try harder next time, [hermione_name]."
                $ h_body = "01_hp/13_hermione_main/body_31.png" #Flashing panties
                show screen hermione_main
                her "Next time?!"
                $ h_body = "01_hp/13_hermione_main/body_47.png" #Flashing panties
                her2 "I assure you, [genie_name], there will be no next time..."
                hide screen hermione_main
                m "We'll see..."
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Flashing panties
                show screen hermione_main
                her "Tsk!"
                hide screen hermione_main
                pause.2 #Otherwise a bug occurs. 
                $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
                $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
                $ mad += 35
                call music_block
                jump could_not_flirt

    if request_11_points == 1: #<====================================================================================================================EVENT 02 
        $ new_request_11_02 = True # HEARTS 
        $ new_request_11_heart = 2
        m "[hermione_name], I need you to dance for me."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "That again, [genie_name]...?"
        m "You will get paid accordingly of course..."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "............................"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        show screen hermione_main
        with d3
        her "And you expect me to... ehm..."
        m "Take your clothes off. Naturally."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        stop music fadeout 1.0
        her "......................"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "Well, why not?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Yes, I don't see why not!"
        m "Hm...? {size=-4}(Look at her, so eager all of a sudden...){/size}"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "After all, as a pupil I am meant to obey your every order, isn't that right, [genie_name]?!"
        m "...................."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "If the Headmaster tells me to strip for him, Then I shall strip!!!"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Do I find this extremely inappropriate, disgraceful and humiliating?"
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Of course not. What nonsense!"
        m ".............."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        show screen hermione_main
        with d3
        her "Ha! Might as well do this the proper way!"
        hide screen hermione_main
        with d3
        hide screen blktone 
        with d3
        m "??!"
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(1)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause 5
        g4 "!!!!!!"
        ">To your surprise Hermione just hops onto your desk and starts dancing franticly..."
        hide screen blkfade
        $ hermione_chibi_xpos = 210 #Near the desk: 400.
        $ hermione_chibi_ypos = 180 #Default: 250
        show screen clothed_dance #Hermione stands still.
        show screen ctc
        with fade
        pause
        show screen bld1
        show screen blktone
        with d3
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center.
        $ h_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
        show screen hermione_main
        her2 "If I must degrade myself in order to protect the honour of my house..."
        hide screen hermione_main
        ">Hermione is starting to take off her vest..."
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Flashing panties
        show screen hermione_main
        her "So be it then!"
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Flashing panties
        her "Just..."
        $ h_body = "01_hp/13_hermione_main/body_88.png" #Flashing panties
        her "*groan*"
        hide screen hermione_main
        show screen blktone8
        hide screen blktone
        with d3
        ">Her vest seems to be stuck somehow, but the girl keeps pulling on at the fabric with anger..."
        show screen hermione_main
        her "Why won't it....?!"
        $ h_body = "01_hp/13_hermione_main/body_81.png" #Flashing panties
        her "There!"
        hide screen hermione_main
        ">Hermione finally manages to untangle herself and sends the vest flying to the other side of the room..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_vest_dance
        with d3
        pause
        show screen bld1
        with d3
        show screen hermione_main
        hide screen ctc
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Flashing panties
        her "The skirt is next, right?"
        hide screen hermione_main
       
        menu:
            m "..."
            "\"Yes, that's right. Take it off!\"":
                show screen hermione_main
                her "Of course!"
                $ h_body = "01_hp/13_hermione_main/body_87.png" #Flashing panties
                her "Here it goes!"
                hide screen hermione_main
                pause.1
                show screen blktone8
                with d3
                ">Hermione sends her skirt flying across the room, just like she did with her vest a moment earlier..."
            "\"You need to calm down, [hermione_name]. \"":
                show screen hermione_main
                her2 "Well, {size=+7}EXCUSE ME{/size}, [genie_name]!"
                her2 "You told me to strip for you, but you never told me your preferences in regards to the pace!"
                hide screen hermione_main
                m "Well, I'm telling you now, [hermione_name]!"
                show screen hermione_main
                her2 "Too late!"
                hide screen hermione_main
                pause.1
                show screen blktone8
                with d3
                ">And sure enough Hermione sends the skirt flying across the room, just like she did with her vest a moment earlier..."
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        show screen no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "{size=-4}(Wow, she is getting really worked up over this...){/size}"
        m "{size=-4}(Maybe it was still too early to--{/size}"
        $ h_body = "01_hp/13_hermione_main/body_66.png" 
        show screen hermione_main
        her "My shirt?!!"
        $ h_body = "01_hp/13_hermione_main/body_86.png" 
        her "{size=+9}I don't need it!{/size}"
        hide screen hermione_main
        pause.1
        show screen blktone8
        with d5
        ">Hermione's shirt suddenly hits the floor."
        g4 "{size=-4}(When did she??!){/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        show screen no_shirt_no_skirt_dance
        with d3
        pause
        show screen bld1
        with d3
        show screen hermione_main
        hide screen ctc
        her "Do you enjoy this, [genie_name]?"
        $ h_body = "01_hp/13_hermione_main/body_30.png" 
        her2 "Shall I shake my breasts for you like one of those harlots?"
        hide screen hermione_main
        m "Well---"
        show screen hermione_main
        her2 "Of course! Why wouldn't I degrade myself for your pleasure?!"
        $ h_body = "01_hp/13_hermione_main/body_86.png" 
        her2 "This is completely {size=+7}acceptable!{/size}"
        hide screen hermione_main
        pause.1
        show screen blktone
        with d3
        ">Hermione is starting to shake her naked breasts rather clumsily..."
        ">As you watch the girl's tits sway right and left before your face you find yourself fighting the urge to..."
        menu:
            m "..."
            "-Grab them!-":
                g9 "{size=-4}(Yes, just get my hands on these ample titties, that's what I want to do!){/size}"
                g9 "{size=-4}(Maybe pull on them a little, yes...){/size}"
            "-Slap them!-":
                m "{size=-4}(I want to slap the crap out of her fun bags.){/size}"
                g9 "{size=-4}(Yes, just slap them around a little...){/size}"
            "-Bite on them!":
                m "{size=-4}(Is it weird that I feel like sinking my teeth into her tits?){/size}"
                m "{size=-4}(No, it's not weird!){/size}"
                m "{size=-4}(Just a couple of gentle love-bites!){/size}"
                g9 "{size=-4}(Yes... Maybe more than just a couple...){/size}"
            "-Motorboat them!-":
                m "{size=-4}(I just want to put my face right in between them!){/size}"
                g9 "{size=-4}(Yes, To motorboat these titties would be the best!){/size}"
        ">While you are lost in thought, Hermione keeps on dancing..."
        
        if custom_outfit == 0:
            $ badges = False # Turns off the badges layer.
        
        $ h_body = "01_hp/13_hermione_main/body_89.png" 
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box.
        $ h_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ h_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        show screen hermione_main
        her2 "(Dancing naked in front of the headmaster...)"
        her2 "(If my parents knew about this they would lose their minds...)"
        $ h_body = "01_hp/13_hermione_main/body_90.png"
        her2 "(Especially my father...)"
        hide screen hermione_main
        ">Hermione is starting to shake her tits again...)"
        show screen hermione_main
        her "(Hermione Granger - the stripper...)"
        $ h_body = "01_hp/13_hermione_main/body_91.png"
        her2 "(Forgive me father...)"
        hide screen hermione_main
        pause.1
        show screen blktone8
        hide screen blktone
        with d3
        ">Hermione puts her hands on her tits and starts squeezing them..."
        ">You can only assume that she means to look seductive, but she just looks awkward and ashamed."
        show screen hermione_main
        her2 "(I used to be a top student... Used to have standards...)"
        hide screen hermione_main
        ">Hermione clutches her tits even harder and then gives them a couple of twists..."
        ">It almost looks as if she is mad at her own breasts and trying to punish them..."
        ">You find the thought strangely arousing..."
        $ h_body = "01_hp/13_hermione_main/body_92.png"
        show screen hermione_main
        $ h_c_u_pic = "01_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        her "Well, I hope you enjoyed yourself, [genie_name]!"
        hide screen hermione_main
        m "What?"
        $ h_body = "01_hp/13_hermione_main/body_93.png"
        show screen hermione_main
        her "I would like to get paid now..."
        hide screen hermione_main
        m "Aren't you forgetting something, [hermione_name]?"
        $ h_body = "01_hp/13_hermione_main/body_92.png"
        show screen hermione_main
        her2 "[genie_name]...?"
        hide screen hermione_main
        m "Your panties...?"
        $ h_body = "01_hp/13_hermione_main/body_94.png"
        show screen hermione_main
        her "My panties?"
        her "But, they always leave them on!"
        hide screen hermione_main
        m "Who exactly are \"they\"?"
        m "Strippers in kid's cartoons?"
        m "Stripping is stripping, [hermione_name]!"
        m "Now take off your panties!"
        $ h_body = "01_hp/13_hermione_main/body_95.png"
        show screen hermione_main
        her "................"
        hide screen hermione_main
        ">Hermione looks horror-struck. All of her anger is gone..."
        $ h_body = "01_hp/13_hermione_main/body_90.png"
        show screen hermione_main
        her "................."
        hide screen hermione_main
        ">Without saying another word..."
        ">She starts to pull down her panties..."
        g9 "......................................."
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snapes_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        hide screen blktone8
        hide screen bld1
        show screen snape_walk_01 
        with d3
        pause 1.5
        stop music 
        $ renpy.play('sounds/scratch.wav')
        show screen snape_02 #Snape stands still.
        
        $ tt_xpos=330 #Defines position of the Snape's full length sprite. (Default 300). 140 - center.
        $ tt_ypos=340#(Default 0). Right bottom corner: 340
        $ s_sprite = "01_hp/10_snape_main/snape_01.png"
        $ hermione_main_zorder = 8 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. Works for all full size sprites.
        show screen s_head
        $ h_c_u_pic = "01_hp/08_animation_02/05_panties_01.png"
        show screen h_c_u
        
        
        
        sna2 "Listen, Genie. I've been thinki--"
        $ s_sprite = "01_hp/10_snape_main/snape_11.png"
        with hpunch
        sna2 "................................................................................................................................................................................"
        $ h_body = "01_hp/13_hermione_main/body_96.png"
        show screen h_head
        with hpunch
        her "(Professor Snape???????!)"
        $ s_sprite = "01_hp/10_snape_main/snape_12.png"
        show screen s_head
        sna2 "Miss Granger?"
        show screen h_head
        her "(No, no... This is not happening. Please...)"
        hide screen h_head
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "...................................."
        show screen bld1
        with d3
        menu:
            m "..."
            "\"Severus, I am busy right now.\"":
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "Yes... I can see that..."
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "{size=-7}(I want to die!){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "I shall postpone our conversation for later then, Geni-- *khem!* Albus."
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                sna "Miss Granger..."
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her ".........................................."
                hide screen h_head
            "\"Severus! Please, come join us.\"":
                $ mad += 37
                $ snape_invated_to_watch = True #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
                $ s_sprite = "01_hp/10_snape_main/snape_14.png"
                show screen s_head
                sna "Seriously?"
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "([genie_name], no, please.............................)"
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna "A very tempting offer indeed..."
                $ h_body = "01_hp/13_hermione_main/body_95.png"
                show screen h_head
                her "!!!!!!......."
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                show screen s_head
                sna2 "Well, maybe some other time..."
                $ h_body = "01_hp/13_hermione_main/body_99.png"
                show screen h_head
                her "{size=-5}(There will be no other time!){/size}"
                her "{size=-5}(I will stop selling favours from now on, I swear!){/size}"
                $ s_sprite = "01_hp/10_snape_main/snape_12.png"
                show screen s_head
                sna2 "I shall postpone our conversation then, Geni-- *khem!* Albus."
                $ s_sprite = "01_hp/10_snape_main/snape_13.png"
                sna2 "Miss Granger..."
                $ h_body = "01_hp/13_hermione_main/body_97.png"
                show screen h_head
                her "................................."
                hide screen h_head
        show screen blkfade 
        with d3
        hide screen snape_walk_01 
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        pause 1.5

        
        ">Snape leaves..."
        ">Hermione hastily hops off your desk."
        ">She starts putting her clothes back on rather frantically..."
        $ h_body = "01_hp/13_hermione_main/body_98.png"
        show screen h_head
        her "My shirt! Where is my shirt?!"
        hide screen h_head
        m "It's over there, by the fireplace..."
        $ h_body = "01_hp/13_hermione_main/body_85.png"
        show screen h_head
        her2 "................................"
        hide screen h_head
        pause 2
        $ h_body = "01_hp/13_hermione_main/body_33.png"
        show screen h_head
        
        $ badges = True # Turns the badges layer back ON.
        
        her "........................"
        $ h_body = "01_hp/13_hermione_main/body_34.png"
        stop music fadeout 2.0
        her "Can I just get my points now, please?"
        hide screen h_head
        hide screen snape_02 #Snape stands still.
        pause.1
        $ hermione_main_zorder = 5 #Zorder of the screen hermione_main. 5 puts it on top of everything but behind the speech box. On top of EVERYTHING = 8.
        $ h_ypos=0 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340
        $ hermione_chibi_xpos = 400 #Near the desk.
        show screen hermione_02 #Hermione stands still.
        $ hermione_chibi_ypos = 250 #Default: 250. Another number is 180
            
    if request_11_points >= 2: #<====================================================================================================================EVENT 03
        $ new_request_11_03 = True # HEARTS
        $ new_request_11_heart = 3
        if snape_invated_to_watch: #Turns TRUE when Hermione is stripping and Snape walks in on you. Allows to invite him to watch her strip next time.
            m "(Hm... Should I invite that Professor Snape guy to watch as well?)"
            menu:
                "\"Yes! Hermione needs an audience!\"":
                    if not invited_snape_once_already:
                        $ invited_snape_once_already = True #Makes sure this event takes place only once.
                        hide screen blktone
                        with d3
                        m "Miss, Granger, I will be buying another favour from you today."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Of course, [genie_name]."
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "...professor Snape?"
                        her "May I ask, why, [genie_name]?"
                        m "Oh, I just think you could use a bigger audience for your striptease performance."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "My striptease performance...?!!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "With all due respect, [genie_name]..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "{size=-5}(Which I have oh so little left for you...){/size}"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "I refuse to degrade myself for professor Snape's amusement!"
                        m "No, no, you got it all wrong, [hermione_name]."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Hm..?"
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "!!!"
                        m "Yes, I want to catch him in the act!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "[genie_name], I didn't realize..."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "I see now..."
                        her "I am sorry for doubting you [genie_name]..."
                        m "No biggy. Now go find professor Snape and bring him here."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Right away [genie_name]!"
                        label fetching_snape:
                        hide screen hermione_main
                        with d3
                        hide screen bld1
                        with d3
                        hide screen hermione_02 #Hermione stands still.
                        
                        # $ walk_xpos=400 #Animation of walking chibi. (From)
                        # $ walk_xpos2=610 #Coordinates of it's movement. (To)
                        # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                        # show screen hermione_walk_01_f 
                        # pause 2
                        # hide screen hermione_walk_01_f 
                        
                        call her_walk(400,610,2)
                        
                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        with Dissolve(.3)
                        pause.2
                        show screen blkfade
                        with d5
                        stop music fadeout 1.0
                        ">...................{w}...................{w}...................{w}..................."
                        hide screen blkfade
                        with d5
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=360 #Coordinates of it's movement. (To)
                        $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                        show screen snape_walk_01 
                        
                        pause 4
                        show screen snape_02 #Snape stands still.

                        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                        $ hermione_chibi_xpos = 610
                        $ hermione_chibi_ypos = 250
                        show screen hermione_02 #Hermione stands still.
                        with Dissolve(.5)
                        pause.3
                        
                        $ walk_xpos=610 #Animation of walking chibi. (From)
                        $ walk_xpos2=500 #Coordinates of it's movement. (To) 400 - near desk.
                        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                        show screen hermione_walk_01 
                        pause 3
                        $ hermione_chibi_xpos = 500 #Near the desk - 400
                        show screen hermione_02 #Hermione stands still.
                        pause.5
                        show screen ctc
                        pause
                        show screen bld1
                        with Dissolve(.3)
                        $ tt_xpos=180 #Defines position of the Snape's full length sprite. Default - 300
                        $ tt_ypos=0
                        $ s_sprite = "01_hp/10_snape_main/snape_01.png"
                        show screen snape_main
                        show screen ctc
                        with Dissolve(.3)
                        
                    else:
                        hide screen blktone
                        with d3
                        m "Miss, Granger, I will be buying another favour from you today."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.
                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                        show screen hermione_main
                        with d3
                        her "Of course, [genie_name]."
                        m "But before that, do you think you could go and fetch professor Snape for me?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "...professor Snape?"
                        her "may I ask, why, [genie_name]?"
                        m "Oh, I just want you to dance for us."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "!!!"
                        m "I want to prove that professor Snape is dirty, and I need your help."
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "But didn't we already establish that last time I did this?"
                        m "Well, ehm... sure..."
                        m "But I will need more proof if I am to take this issue to the ministry of magic!"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "....."
                        m "So, what do you say [hermione_name]?"
                        m "One more dance for the greater good?"
                        hide screen hermione_main
                        with d3
                        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                        show screen hermione_main
                        with d3
                        her "Well, alright..."
                        m "Good. Go find professor Snape then."
                        jump fetching_snape
                    
                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Genie... err, I mean Albus, you wanted to see me?"
                    m "Yes. Are you in the mood for a little striptease?"
                    hide screen snape_main
                    with d3
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
                    show screen snape_main
                    with d3
                    sna "Oh...?"
                    sna "Miss Granger here will be performing I assume?"
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her ".............."
                    m "Yes, our little mynx is more than happy to take off her clothes for our entertainment."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "............"
                    m "Aren't you [hermione_name]?"
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.
                    $ h_xpos=380 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Yes, [genie_name]."
                    m "Let's get started then!"
                    hide screen hermione_main
                    hide screen snape_main
                    
                    pause
                    
                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 1
                    $ h_body = "01_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "............."

                    
                    
                    $ s_head_xpos = 330 # x = 330,
                    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "......................"
                    hide screen s_head2
                    m ".........................."
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    show screen s_c_u
                    $ s_c_u_pic = "01_hp/09_snape_ani/snape_0130.png"
                    $ snape_chibi_xpos = 290 #Default 360.
                    $ snape_chibi_ypos = 210
                    with fade
                    pause
                    show screen bld1
                    with d3
                    m "So... Severus... How's life?"
                    $ s_sprite = "01_hp/10_snape_main/snape_09.png"
                    show screen s_head2
                    sna "Well, you know... same old, same old..."
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png"
                    sna " The Students are causing me grief..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    sna2 "In fact, miss Granger here managed to cause me more stress than any other student..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_68.png"
                    her "..............................."
                    hide screen h_head2
                    m "Oh, I am sure she is very sorry about that..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_74.png"
                    her "{size=-4}(Not even a little bit!){/size}"
                    hide screen h_head2
                    m "And will make up for it today, won't you [hermione_name]?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_53.png"
                    her "Uhm... Yes, [genie_name]."
                    hide screen h_head2
                    hide screen ctc
                    pause.2
                    show screen blktone
                    with d3
                    ">Hermione takes her vest off and starts to sway her hips seductively."
                    hide screen blktone
                    with d3

                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_87.png"
                    her "..................."
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png"
                    show screen s_head2
                    sna "Hm... You are being suspiciously quiet [hermione_name]."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_48.png"
                    her "{size=-4}(Oh no! Is he onto us?){/size}"
                    $ h_body = "01_hp/13_hermione_main/body_57.png"
                    her2 "I am just doing what the headmaster told me, [genie_name]..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Aren't you going to lecture me on the \"corruption that is taking over Hogwarts\" like you do every other day?"
                    hide screen s_head2
                    m "Severus..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "No, Albus I want to hear little miss perfect's answer."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_57.png"
                    her2 "I just want you to have a good time, [genie_name]..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png"
                    show screen s_head2
                    sna2 "Oh! It's \"[genie_name]\" now, isn't I?"
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png"
                    sna2 "What happened to \"snape'o'doodle\" and \"Professor Snivellus\"??!"
                    hide screen s_head2
                    g9 "{size=-5}( \"snape'o'doodle\, heh... that's funny.){/size}"
                    show screen h_head2 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_57.png" # HERMIONE
                    her "............."
                    $ s_sprite = "01_hp/10_snape_main/snape_08.png"
                    show screen s_head2
                    sna2 "Yes, I know what are you calling me behind my back, you wretched girl!"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_86.png"
                    her2 "Well, maybe that's because you deserve it... [genie_name]."
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "What?!"
                    sna "How dare you....?"
                    $ s_sprite = "01_hp/10_snape_main/snape_15.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Who do you think you are? You filthy mu--"
                    show screen h_head2 # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_62.png" # HERMIONE
                    her2 "[genie_name], one of your staff is verbally abusing me!"
                    her2 "Are you going to allow this?"
                    $ s_sprite = "01_hp/10_snape_main/snape_08.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Verbally abusing...?! You have some nerve, girl!"
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna2 "Albus, will you allow her to talk back to a teacher like that?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_62.png" # HERMIONE
                    her "[genie_name]!"
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                    show screen s_head2 #SNAPE
                    sna "Albus!"
                    hide screen s_head2
                    menu:
                        m "..."
                        "\"[hermione_name], show some respect!\"":
                            $ mad += 9
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_61.png" # HERMIONE
                            her "What?"
                            her "But [genie_name]!"
                            hide screen h_head2  
                            m "Young lady, you {size=+4}will{/size} calm down now."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_66.png" # HERMIONE
                            her "Tsk!"
                            hide screen h_head2      
                            m "And take off your skirt already, would you?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......."
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "..........."
                            hide screen s_head2  
                        "\"Severus, you started this.\"":
                            $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                            show screen s_head2  
                            sna "What? Me?!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_52.png" # HERMIONE
                            her "Thank you, [genie_name]."
                            $ s_sprite = "01_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, you are spoiling the girl! She must be taught a lesson!"
                            hide screen s_head2 
                            m "...............Severus."
                            g4 "Did you hit your head?!"
                            $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I beg your pardon?"
                            hide screen s_head2 
                            g4 "The girl is already stripping for you!"
                            g4 "What punishment are you talking about?"
                            $ s_sprite = "01_hp/10_snape_main/snape_16.png" #SNAPE
                            show screen s_head2  
                            sna "Tsk... How about a flogging?" 
                            hide screen s_head2
                            g4 "Severus!"
                            $ s_sprite = "01_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Alright, alright, I see your point..."
                            hide screen s_head2
                            m "[hermione_name], are you going to strip or did you climb on my desk to get a better view?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "Ehm..."
                            hide screen h_head2
                            m "Take of your skirt, [hermione_name]!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "Yes, [genie_name]..."
                            hide screen h_head2
                        "\"Both of you, calm the fuck down.\"":
                            m "You, tall-dark-and-handsome, calm down a bit, would you?"
                            $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I beg your pardon?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Yes! You tell him profess--"
                            hide screen h_head2     
                            m "You as well, you perverted little mynx!"
                            m "Calm down and take your skirt off already."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_79.png" # HERMIONE
                            her "I am not perverted..."
                            hide screen h_head2     
                            m "The skirt, [hermione_name]!"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "......"
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2  
                            sna "............."
                            hide screen s_head2     
                    
                    show screen blktone
                    with d3
                    ">Hermione swiftly takes off her \"Hogwarts\" skirt..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen s_head2
                    sna "Hm..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                    her "........................"
                    hide screen h_head2
                    m "Yes, much better!"
                    show screen blktone
                    with d3
                    ">Hermione keeps on dancing, while she's Wearing nothing but her shirt now..."
                    menu:
                        m "..."
                        "\"Severus, what about that Potter boy?\"":
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "(.....?)"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2
                            sna "What about him?"
                            hide screen s_head2
                            m "Is he still causing you grief?"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Oh..."
                            sna "Not really, no..."
                            $ s_sprite = "01_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "To be honest I never really had a problem with the boy himself..."
                            sna2 "Although I did plan to make his life here miserable because of his father..."
                            $ s_sprite = "01_hp/10_snape_main/snape_02.png" #SNAPE
                            show screen s_head2    
                            sna2 "But lately I have way more interesting projects to occupy myself with..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "..................."  
                            hide screen h_head2   
                        "\"Severus, what about the Weasleys?\"":
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "What about them?"
                            hide screen s_head2   
                            m "Are they still causing you trouble?"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... More than ever."
                            hide screen s_head2
                            m "Hm...?"
                            m "You seem surprisingly indifferent about that..."
                            $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "That's because I know that they will get what they deserve eventually..."
                            hide screen s_head2
                            m "Revenge? Cool! What do you have in mind?"
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                            her "!!!"
                            $ s_sprite = "01_hp/10_snape_main/snape_06.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm... Can't discuss this with \"the enemy\" present."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "Tsk!"
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "All I can say is that it involves their beloved little sister Ginny..."
                            hide screen s_head2  
                            m "Ginny? Hm... What a curious name for a girl..."
                            m "............."
                            m "So, you plan to fuck her then?"
                            $ s_sprite = "01_hp/10_snape_main/snape_08.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "!!?"
                            $ s_sprite = "01_hp/10_snape_main/snape_17.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna2 "Albus, please, not in front of the girl!"
                            hide screen s_head2  
                            m "Alright, alright..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                            her "{size=-5}(Ginny...){/size}"
                            hide screen h_head2 
                        "\"How would you grade Hermione's butt?\"":
                            $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "miss Hermione's buttocks?" 
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_69.png" # HERMIONE
                            her "!!!............"
                            hide screen h_head2      
                            m "Sure! As you would grade a paper."
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm..."
                            hide screen s_head2  
                            pause.1
                            ">Professor Snape gives Hermione's buttocks an appraising look..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                            her ".........?"
                            $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "I would say..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_59.png" # HERMIONE
                            her "............?!"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... \"{size=+5}F-{/size}\"."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                            her "(What?!)"
                            $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Unsatisfactory..."
                            sna2 "Look at that pitiful thing. Tiny and skinny... That's a boy's butt."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_51.png" # HERMIONE
                            her "!!!!!!!!!!"
                            hide screen h_head2   
                            
                    show screen blktone
                    with d3
                    ">One after another, Hermione undoes the buttons of her shirt and then takes it off..."
                    hide screen blktone
                    with d3
                   
                    show screen ctc
                    hide screen bld1
                    with d3
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    m "Alright! We Finally get to the good stuff!"
                    $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                    show screen s_head2       
                    sna "Hm..."
                    
                    if custom_outfit == 0:
                        $ badges = False # Hides the layer with badges.
                    
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                    her "........"
                    hide screen h_head2   
                    menu:
                        m "..."
                        "-Start jerking off-":
                            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                            
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_94.png"
                            her "[genie_name]?!"
                            hide screen h_head2
                            m "It's alright, [hermione_name]. Don't mind me..."
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Oh, we're doing it like this then?"
                            sna "Well, don't mind if I do..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                            $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.
                            her "!!!"
                            hide screen h_head2    
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            $ snape_chibi_xpos = -185
                            $ snape_chibi_ypos = 10
                            $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_95.png"
  
                            her "No, guys... err I mean, sirs... Ehm, professors!"
                            hide screen h_head2
                            m "Don't you mind us [hermione_name], just keep on doing your thing."
                            show screen h_head2
                            her "But..."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                            her2 "No! I refuse to dance with those things pointed at me!"
                            her2 "You need to put them away or the dance is over!"
                            hide screen h_head2    
                            m "You aren't in any position to give us orders, [hermione_name]."
                            show screen h_head2                                                             # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_110.png" # HERMIONE
                            her2 "that was not an order, [genie_name]. It was an ultimatum."
                            hide screen h_head2    
                            menu:
                                m "..."
                                "\"Alright Severus, let's be civil...\"":
                                    $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                                    show screen s_head2                                                          #SNAPE
                                    sna2 "I see Miss Granger manages to remain exceptionally stubborn in any situation..."
                                    hide screen s_head2  
                                    show screen blkfade
                                    with d3
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    show screen s_c_u
                                    $ s_c_u_pic = "01_hp/09_snape_ani/snape_0130.png"
                                    $ snape_chibi_xpos = 290 #Default 360.
                                    $ snape_chibi_ypos = 210
                                    pause.3
                                    hide screen blkfade 
                                    with d3
                                    jump civil_with_snape
                                    
                                "\"(Pst! Remember why we are doing this!)\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_104.png" # HERMIONE
                                        her "Oh, right..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "What was that?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her "Please don't mind what I just said..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_05.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm...?"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_108.png" # HERMIONE
                                        her2 "I do not mind you touching yourself in front of me..."
                                        her2 "Yes, I do not mind it at all..."
                                        her "I will just keep on dancing then..."
                                        hide screen h_head2
                                        hide screen ctc
                                        pause.1
                                        show screen blktone
                                        with d3
                                        show screen blktone8
                                        with d3
                                        ">You keep on jerking off while you're watching Hermione dance..."
                                        ">Hermione squeezes her breasts and shakes her hips slightly..."
                                        hide screen blktone8
                                        with d3
                                        m "Yes, [hermione_name]. Very good."
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "*Khem!* Acceptable performance, miss Granger."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "...................."
                                        hide screen h_head2
                                        m "Heh..."
                                        hide screen h_head2
                                        m "How would you grade her tits then?"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "......"
                                        $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm......"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_103.png" # HERMIONE
                                        her "........"
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"B+\"!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "!!!"
                                        hide screen h_head2
                                        m "Really?"
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Yes. I do give credit where credit is due."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                                        her "(Professor...)"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                                        her "(Time for my finishing act then!)"
                                        hide screen h_head2 
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione bends over and slides her panties down."
                                        ">Her movements lack grace..."
                                        ">But a pretty pussy is always a welcome sight nonetheless..."
                                        ">You show your appreciation by stroking your cook even faster..."
                                        
                                       
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        show screen ctc
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        
                                        $ s_sprite = "01_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes... Yes!!!"
                                        sna2 "Now shake those B+ titties for me, you harlot!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "......."
                                        hide screen h_head2       
                                        hide screen ctc
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione suddenly breaks into a series of rather complex pirouettes."
                                        $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes, such grace..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "That lithe young body!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "........."
                                        $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Oh, yes!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                                        hide screen h_head2     
                                        pause.1
                                        show screen blktone8
                                        with d3
                                        ">Hermione seems very focused on her dancing routine..."
                                        hide screen blktone8
                                        with d3
                                        $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes, and now another pirouette!"
                                        sna "Magnificent!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_13.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "I would applaud you but one of my hands is very busy at the moment."
                                        hide screen s_head2  
                                        m "{size=-4}(Was that an attempt at a joke?){/size}"
                                        m "{size=-4}(Man, horny Snape is weird...){/size}"
                                        show screen blktone8
                                        with d3
                                        ">Hermione performs another set of movements and pirouettes..."
                                        ">Gives a little curtsy bow to the imaginary public..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                        ">And then slumps down on her butt exhausted."
                                        
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        show screen ctc
                                        pause
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_102.png"
                                        her "Whew... This was--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING WHORE!"
                                        hide screen hermione_main
                                        with d3
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "01_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "01_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        
                                        $ s_sprite = "01_hp/10_snape_main/snape_18.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Good job, you harlot!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Here is your reward!"
                                        hide screen s_head2     
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ snape_chibi_xpos = -210
                                        $ snape_chibi_ypos = 10
                                        $ snape_cum_chibi_xpos =  -210
                                        $ snape_cum_chibi_ypos  = 10
                                        $ s_c_c_u_pic = "snape_cum_01"
                                        show screen s_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "01_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "01_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        $ u_sperm = "01_hp/13_hermione_main/auto_05.png"
                                        her "!!!!!!!!!!!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Oh... Yes..."
                                        hide screen s_head2 
                                        g4 "Little slut!"
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "..............................."
                                
                                        $ s_c_c_u_pic = "01_hp/08_animation_02/11_cum_18.png"
                                        $ g_c_c_u_pic = "01_hp/08_animation_02/09_cum_18.png"
                                        $ s_sprite = "01_hp/10_snape_main/snape_21.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Ha-ha-ha! This is magnificent!"
                                        hide screen s_head2
                                        g9 "I know, right!?"
                                        show screen bld1
                                        with d3
                                        $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                        $ s_c_u_pic = "01_hp/08_animation_02/10_jerking_01.png" # Snape stands still with his dick in hand.
                                        $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Yes... We should do this more often."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_106.png" # HERMIONE
                                        her "................."
                                        $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Your performance was acceptable, miss Granger..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "Thank you................"
                                        $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "But if I were to grade it..."
                                        show screen h_head2                                                             # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "..........."
                                        $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Hm...."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        her "............"
                                        $ s_sprite = "01_hp/10_snape_main/snape_10.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "\"{size=+5}F+{/size}\"!"
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_112.png" # HERMIONE
                                        stop music
                                        her "{size=+5}WHAT?!!!{/size}"
                                        $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "Yes... Quite a few things could use some improvement actually."
                                        show screen h_head2                                                               # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_110.png" # HERMIONE
                                        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                        her "I cannot believe this!"
                                        hide screen h_head2 
                                        pause
                                        show screen blkfade 
                                        with d3
                                        hide screen h_c_u 
                                        hide screen s_c_c_u
                                        hide screen g_c_c_u
                                        show screen genie
                                        $ snape_chibi_xpos = -60
                                        $ snape_chibi_ypos = 10
                                        $ s_c_u_pic = "jerking_off_03_ani" #Snape.
                                        hide screen chair_02
                                        hide screen g_c_u
                                        hide screen desk_02
                                        $ hermione_chibi_xpos = 300 #Near the desk: 400. (210 - standing on desk.)
                                        $ hermione_chibi_ypos = 260#Default: 250. (180- standing on desk.)
                                        show screen h_c_u 
                                        $ h_c_u_pic = "01_hp/08_animation_02/07_dance_03.png"
                                        ">Hermione furiously jumps off your desk."
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ flip = True # Flips hermione_main screen.
                                        $ u_sperm = "01_hp/13_hermione_main/auto_05.png"
                                        $ h_body = "01_hp/13_hermione_main/body_101.png"
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                                        if custom_outfit == 0:
                                            $ only_upper = True #No legs shown.
                                        show screen bld1
                                        with d5
                                        show screen hermione_main
                                        with d3
                                        pause
                                        hide screen ctc
                                        her "I demand a higher grade than that!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_09.png" #SNAPE
                                        show screen s_head2      
                                        sna2 "You do not demand a grade miss Granger, you earn it."
                                        hide screen s_head2     
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_107.png"          #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "I did earn it!"
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_103.png"               #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "And could you at least have the decency to stop touching yourself, [genie_name]!"
                                        $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                                        show screen s_head2     
                                        sna2 "Tch..."
                                        hide screen s_head2   
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3   
                                        m "(Are they for real?)"
                                        show screen ctc
                                        pause
                                        show screen blkfade
                                        with d7
                                        hide screen ctc
                                        hide screen s_c_u
                                        hide screen h_c_u
                                        $ hermione_chibi_xpos = 400 #Near the desk.
                                        $ hermione_chibi_ypos = 250 #Default: 250
                                        show screen hermione_02 #Hermione stands still.
                                        ">You watch Snape with his dick still hanging out and the cum-covered Hermione argue loudly about her imaginary grade."
                                        ">After a while Professor Snape agrees to change Hermione's grade from \"F+\" to \"D-\"."
                                        ">Then he beats a hasty retreat before Hermione has a chance to start another argument..."
                                        hide screen blkfade
                                        with d5
                                        $ flip = False # Flips hermione_main
                                        $ only_upper = False #Show legs.
                                        $ aftersperm = True #Show cum stains.
                                        $ uni_sperm = False #Don't show cum.
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_29.png"#Sprite of Hermione's upper body.                    #HERMIONE
                                        $ badges = True
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "Well..."
                                        her "Was our mission a success, [genie_name]?"
                                        menu:
                                            m "..."
                                            "\"Huh? What mission?\"":
                                                $ mad += 7
                                                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                $ h_body = "01_hp/13_hermione_main/body_32.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                her "I only agreed to this so that you could catch professor Snape in the act, [genie_name]!"
                                                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                                $ h_body = "01_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                                with d3                                                                                                                                                                                                                        #HERMIONE
                                                her "So that we would have definite proof that he is \"dirty\"!"
                                                m "Oh, that mission..."
                                                m "Yes. Mission accomplished!"
                                            "\"Yes! Thanks to you!\"":
                                                pass
                                        m "Good job. [hermione_name]."
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_33.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "I am happy to have been of help, [genie_name]!"
                                        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                        #HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_34.png"#Sprite of Hermione's upper body.                                                                   #HERMIONE
                                        show screen hermione_main                                                                                                                                                                                 #HERMIONE
                                        with d3                                                                                                                                                                                                                        #HERMIONE
                                        her "...Can I get paid now, please?"
                                        

                                    else:
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                                        her "Oh..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_97.png" # HERMIONE
                                        her "No, I can't! This is just not worth it!"
                                        hide screen ctc
                                        hide screen h_head2  
                                        pause.1
                                        show screen blkfade
                                        with d5
                                        ">Hermione jumps off the desk and starts to put her clothes back on."
                                        $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Well, this was awfully anticlimactic..."
                                        hide screen s_head2  
                                        g4 "You don't say..."
                                        $ s_sprite = "01_hp/10_snape_main/snape_03.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna2 "May as well leave now I suppose. I will talk to you later, Albus."
                                        hide screen s_head2  
                                        m "Yes, later, Severus."
                                        $ s_sprite = "01_hp/10_snape_main/snape_04.png" #SNAPE
                                        show screen s_head2                                                          #SNAPE
                                        sna "Miss Granger..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                                        her "Professor..."
                                        hide screen h_head2          
                                       # her "I would like to get paid now."
                                        show screen ctc
                                        pause.4
                                        hide screen s_c_u
                                        hide screen ctc
                                        ">Professor Snape leaves..."
                                        show screen h_head2                                                              # HERMIONE
                                        $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                        stop music fadeout 1.0
                                        her "...................."
                                        hide screen h_head2
                                        pause.5
                                        ">.................{w}.................{w}.................{w}................."
                                        show screen h_head2                                                              # HERMIONE
                                        
                                        $ badges = True # Turns badges back on.
                                        
                                        $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                                        her "...Can I get paid now... [genie_name]...?"
                                        hide screen h_head2   

                        "-Just keep on watching-":
                            label civil_with_snape:
                                play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                            # JUST WATCHING.
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "I will just keep on dancing then..."
                            hide screen h_head2 
                            hide screen ctc
                            pause.1
                            show screen blktone8
                            with d3
                            ">Hermione squeezes her breasts and shakes her hips slightly..."
                            hide screen blktone8
                            with d3
                            m "Yes, [hermione_name]. Very good."
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "*Khem!* Acceptable performance, miss Granger."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "...."
                            hide screen h_head2    
                            m "Heh..."
                            m "How would you grade her tits then?"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "......"
                            $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Hm......"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_90.png" # HERMIONE
                            her "........"
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "\"B+\"!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_94.png" # HERMIONE
                            her "!!!"
                            hide screen h_head2
                            m "Really?"
                            $ s_sprite = "01_hp/10_snape_main/snape_12.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes. I do give credit where it's due."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_95.png" # HERMIONE
                            her "(Professor...)"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "(Time for my finishing act then!)"
                            hide screen h_head2   
                            pause.1
                            show screen blktone8
                            with d3
                            ">Hermione bends over and slides her panties down."
                            ">Her movements lack grace..."
                            ">But a pretty pussy is always a welcome sight nonetheless..."
                            hide screen blktone
                            with d3
                            $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes... Yes..."
                            sna2 "Now shake those B+ titties for me, you harlot!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_99.png" # HERMIONE
                            her "......."
                            hide screen h_head2       
                            show screen blktone8
                            with d3
                            ">Hermione suddenly breaks into a series of rather complex pirouettes."
                            $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Yes, such grace..."
                            $ s_sprite = "01_hp/10_snape_main/snape_20.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "That lithe, young body!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_102.png" # HERMIONE
                            her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                            hide screen h_head2 
                            ">Hermione seems very focused on her dancing routine..."
                            $ s_sprite = "01_hp/10_snape_main/snape_19.png" #SNAPE
                            show screen s_head2
                            sna "Yes, and now another pirouette!"
                            sna "Magnificent!"
                            hide screen s_head2
                            show screen blkfade
                            with d3
                            ">Hermione performs another set of movements and pirouettes..."
                            ">Gives a little curtsy bow to the imaginary public..."
                            ">And then slumps down on her butt exhausted."
                            $ hermione_chibi_xpos = -210 #400 = Near the desk.
                            $ hermione_chibi_ypos = 10
                            $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                            show screen h_c_u
                            hide screen blkfade
                            with d3
                            hide screen blktone8
                            with d3
                            $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                            show screen s_head2                                                          #SNAPE
                            sna "Good job, you harlot!"
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_105.png" # HERMIONE
                            her "............."
                            if daytime:
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Well, my class is about to start so I will be leaving now."
                                sna2 "Don't you have potion class with me today, MIss Granger?"
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Yes, [genie_name]..."
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2                                                          #SNAPE
                                sna2 "Well, don't be late, girl..."
                                hide screen s_head2      
                            else:
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Well, it is getting rather late. I think I will be leaving now."
                                sna2 "Good night, Albus."
                                hide screen s_head2    
                                m "Severus."
                                $ s_sprite = "01_hp/10_snape_main/snape_22.png" #SNAPE
                                show screen s_head2    
                                sna2 "Harlot."
                                show screen h_head2                                                              # HERMIONE
                                $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                                her2 "Professor..."
                                hide screen h_head2      


                            show screen ctc
                            pause
                            show screen blkfade
                            hide screen s_c_u
                            hide screen ctc
                            with d5
                            ">Professor Snape leaves..."
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_91.png" # HERMIONE
                            stop music fadeout 1.0
                            her "...................."
                            hide screen h_head2
                            pause.5
                            ">.................{w}.................{w}.................{w}................."
                            $ badges = True
                            show screen h_head2                                                              # HERMIONE
                            $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                            her "May I... may get paid now... [genie_name]...?"
                            hide screen h_head2   


                "\"Nah... That's not a good idea...\"":
                    label no_snape_watching:  
                    hide screen blktone
                    with d3
                    m "[hermione_name], how about another strip?"     
                    $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her ".............."
                    her "I would really rather not, [genie_name]..."
                    m "Why? You are getting quite good at it."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "........................."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "Thirty five house points?"
                    m "Sure! The usual rate."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    show screen hermione_main
                    with d3
                    her "..................."
                    hide screen hermione_main
                    with d3
                    hide screen bld1
                    with d3
                    pause
                    #Walks to the door
                    
                    # $ walk_xpos=400 #Animation of walking chibi. (From) 400 = desk.
                    # $ walk_xpos2=650 #Coordinates of it's movement. (To) 610 = door.
                    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
                    # show screen hermione_walk_01_f 
                    # pause 2
                    # hide screen hermione_walk_01_f 
                    # $ hermione_chibi_xpos = 650 # Position of the chibi (Near the door).
                    
                    call her_walk(400,650,2)
                    $ h_c_u_pic = "01_hp/animation/h_walk_01.png" 
                    show screen h_c_u
                    pause.5
                   
                    $ tt_xpos=670
                    $ tt_ypos=200
                    show screen thought 
                    with Dissolve(.3)
                    pause.5
                    hide screen thought
                    pause.5
                   
                    $ h_c_u_pic = "01_hp/animation/h_walk_03.png" 
                    $ renpy.play('sounds/09_lock.wav') #Sound of a door opening.
                    pause.4
                    $ h_c_u_pic = "01_hp/animation/h_walk_01.png" 
                    show screen ctc
                    pause
                    m "??!"
                    hide screen h_c_u
                    hide screen ctc
                    $ walk_xpos=650 #Animation of walking chibi. (From)
                    $ walk_xpos2=400 #Coordinates of it's movement. (To)
                    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen hermione_walk_01 
                    pause 3
                    $ hermione_chibi_xpos = 400 #Near the desk.
                    show screen hermione_02 #Hermione stands still.
                    show screen bld1
                    with Dissolve(.3)
                    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                    $ h_ypos=0
                    $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.
                    show screen hermione_main
                    with d3
                    her "Just in case..."
                    stop music fadeout 1.0
                    hide screen hermione_main
                    with d5

                    show screen blkfade
                    with Dissolve(1)
                    $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
                    pause 5
                    $ h_body = "01_hp/13_hermione_main/body_16.png"
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    show screen h_head2
                    her2 "Just for the record..."
                    $ h_body = "01_hp/13_hermione_main/body_17.png"
                    her2 "I still consider this a highly inappropriate favour to be buying from one of your students, [genie_name]."
                    hide screen h_head2
                    m "Right. And an equally inappropriate favour to be selling to your headmaster. Woulnd't you agree?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_69.png"
                    her ".........."
                    hide screen h_head2
                    hide screen blkfade
                    hide screen bld1
                    $ hermione_chibi_xpos = 210 #Near the desk: 400.
                    $ hermione_chibi_ypos = 180 #Default: 250
                    show screen clothed_dance #Hermione stands still.
                    show screen ctc
                    with fade
                    pause
                    show screen no_vest_dance
                    with d3
                    pause
                    show screen bld1
                    hide screen ctc
                    with d3
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_87.png"
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    her ".............."
                    $ h_body = "01_hp/13_hermione_main/body_85.png"
                    her2 "What if my parents were to find out about this, [genie_name]?"
                    her2 "Mother would never understand..."
                    $ h_body = "01_hp/13_hermione_main/body_44.png"
                    her "As for my father..."
                    hide screen h_head2
                    menu:
                        m "..."
                        "{size=-3}\"Your father would be proud of you!\"{/size}":
                            show screen h_head2
                            her "I doubt it..."
                            her "Yes, I am doing this for the right reasons, but..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_61.png"
                            her "He would never see it that way..."
                            her "He must never know about this..."
                            hide screen h_head2
                        "{size=-3}\"Your father would spank you hard!\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_48.png"
                            her "He would not!"
                            $ h_body = "01_hp/13_hermione_main/body_44.png"
                            her "And I am too old for that anyways..."
                            hide screen h_head2
                            g9 "I would say that you are in the perfect age for that..."
                            show screen h_head2
                            her "Huh?"
                            $ h_body = "01_hp/13_hermione_main/body_57.png"
                            her "I do not know what you mean, [genie_name]."
                            hide screen h_head2
                        "{size=-3}\"Your father would disown you!\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_34.png"
                            her "You are probably right, [genie_name]..."
                            $ h_body = "01_hp/13_hermione_main/body_22.png"
                            her "(Oh father, I am so sorry...)"
                            $ h_body = "01_hp/13_hermione_main/body_21.png"
                            her "he must never find out..."
                            hide screen h_head2
                        "{size=-3}\"Your father love to would watch you strip!\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_33.png"
                            her "He would not! He would be ashamed of me!"
                            hide screen h_head2
                            m "Are you sure about that?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_32.png"
                            her "absolutely! My father is a man of integrity!"
                            hide screen h_head2
                            m "But he {size=+4}is{/size} a {size=+4}man{/size}, right?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "....................."
                            $ h_body = "01_hp/13_hermione_main/body_29.png"
                            her "My father must never know about this..."
                            hide screen h_head2
                    show screen blktone
                    with d3
                    ">Hermione is starting to sway her hips rather seductively while she slides her skirt down..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_31.png"
                    her "[genie_name]?"
                    hide screen h_head2
                    m "Huh?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_44.png"
                    her "Can I ask you a question?"
                    hide screen h_head2
                    m "Go ahead..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_33.png"
                    her "..............."
                    $ h_body = "01_hp/13_hermione_main/body_57.png"
                    her "Have you ever been in love...?"
                    hide screen h_head2
                    menu:
                        m "..."
                        "\"Don't be ridiculous! Love is a lie!\"":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_29.png"
                            her "I am sorry you think that way, [genie_name]!"
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "But you couldn't be more wrong!"
                            $ h_body = "01_hp/13_hermione_main/body_54.png"
                            her2 "I believe that true love is what makes the earth turn!"
                            hide screen h_head2
                            m "Actually the conservation of angular momentum is responsible for that."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_44.png"
                            her "Huh?"
                            hide screen h_head2
                            m "Never mind. Just take off your shirt already?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "............"      
                            hide screen h_head2
                        "\"Be quiet and keep on dancing!\"":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her "But you said I could ask you a question..."
                            hide screen h_head2
                            m "And you did, didn't you?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_31.png"
                            her "!!!............"
                            $ h_body = "01_hp/13_hermione_main/body_50.png"
                            her2 "...................................."
                            hide screen h_head2
                            m "Now, hush and take your shirt off."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_69.png"
                            her "........"
                            hide screen h_head2
                        "\"Yes... a very long time ago...\"":
                            hide screen h_head2
                            m "Yes... a very long time ago..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_31.png"
                            her2 "!!!!!??.............................."
                            hide screen h_head2
                            m "Her name was Eden..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_45.png"
                            her "Was she beautiful?"
                            hide screen h_head2
                            m "She was so much more than that..."
                            m "She was smart, green and perfect..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_87.png"
                            her "She was... \"green\"...?"
                            $ h_body = "01_hp/13_hermione_main/body_47.png"
                            her2 "Are you making fun of me, [genie_name]?"
                            hide screen h_head2
                            m "Oh, you humans know nothing of true love..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_55.png"
                            her ".....................................?"
                            hide screen h_head2
                            m "Err... I mean, take off that shirt, [hermione_name]!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_69.png"
                            her "................."
                            hide screen h_head2
                        "\"I feel like I'm in love right now!\"":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_69.png"
                            her "You don't have to be vulgar, [genie_name]."
                            hide screen h_head2
                            m "Oh, but I mean it!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_66.png"
                            her "[genie_name], please!"
                            $ h_body = "01_hp/13_hermione_main/body_55.png"
                            her "I am one of your students!"
                            $ h_body = "01_hp/13_hermione_main/body_57.png"
                            her "And you are older than my father!"
                            hide screen h_head2
                            m "{size=-4}(You have no idea, girl.){/size}"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_55.png"
                            her2 "Although some scientists insist that what we consider \"love\" is actually nothing but a chemical reaction..."
                            $ h_body = "01_hp/13_hermione_main/body_16.png"
                            her2 "And when a man is experiencing sexual arousal, the same type of hormones--"
                            hide screen h_head2
                            m "[hermione_name]!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_15.png"
                            her "Yes, [genie_name]?"
                            hide screen h_head2
                            m "Did you forget where you are?"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_24.png"
                            her "Oh, my apologies, [genie_name]... I get distracted sometimes."
                            hide screen h_head2
                            m "Take off your shirt already, would you?!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_29.png"
                            her "Right..."
                            hide screen h_head2
                    show screen blktone
                    with d3
                    ">Hermione undoes the last button of her shirt and takes it off somewhat gracefully..."
                    hide screen blktone
                    with d3
                    hide screen bld1
                    with d3
                    show screen ctc
                    pause
                    show screen no_shirt_no_skirt_dance
                    with d3
                    pause
                    hide screen ctc
                    show screen bld1
                    with d3
                    g9 "Yes! The tits!"
                    
                    if custom_outfit == 0:
                        $ badges = False# Hides any badges from hermione_main screen.
                    
                    show screen h_head2
                    $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                    $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                    $ h_body = "01_hp/13_hermione_main/body_90.png"
                    her "Must you be so vulgar, [genie_name]?"
                    hide screen h_head2
                    menu: 
                        "-Take your cock out, start jerking off-":
                            hide screen bld1
                            show screen ctc
                            with d3
                            pause
                            show screen blkfade
                            with d6
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_94.png"
                            her "[genie_name]?!"
                            hide screen h_head2
                            m "It's alright, [hermione_name]. Don't mind me..."
                            
                            
                            hide screen genie
                            hide screen no_shirt_no_skirt_dance
                            $ genie_chibi_xpos = -185
                            $ genie_chibi_ypos = 10
                            $ g_c_u_pic = "jerking_off_02_ani"
                            show screen chair_02
                            show screen g_c_u
                            show screen desk_02
                            show screen no_shirt_no_skirt_dance
                            hide screen blkfade
                            with fade
                            pause
                            show screen bld1
                            with d3
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_95.png"
                            her "B-but..."
                            her "Your..."
                            hide screen h_head2
                            m "Yes... Ah, yes, this is good..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_98.png"
                            her "[genie_name]!!!"
                            her "I must insist that you put away your..."
                            $ h_body = "01_hp/13_hermione_main/body_99.png"
                            her "...thing."
                            hide screen h_head2
                            menu:
                                m "..."
                                "\"I said, keep on dancing, [hermione_name]!\"":
                                    if whoring >= 15: #LEVEL 06. You jerk off your cock and Hermione is OK with it.
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_99.png"
                                        her "But..."
                                        her "............................."
                                        $ h_body = "01_hp/13_hermione_main/body_101.png"
                                        her2 "Well, alright, but only if you will promise me not to....finish, [genie_name]."
                                        hide screen h_head2
                                        menu:
                                            m "..."
                                            "-Promise her to hold it-":
                                                    $ d_flag_07 = True #Promised to hold it.
                                                    show screen h_head2
                                                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                                                    her "Well, alright then..."
                                                    hide screen h_head2
                                            "-Give her no such promise-":
                                                $ d_flag_07 = False #Did not promise to hold it.
                                                m "\"Not to finish\"? That would be like torture!"
                                                m "Please keep your sadistic urges to yourself, [hermione_name]."
                                                show screen h_head2
                                                $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                her "I don't have any... sadistic urges, [genie_name]!"
                                                her "I just don't want to..."
                                                hide screen h_head2
                                                g9 "Yes... Those are some nice tits you have..."
                                                show screen h_head2
                                                $ h_body = "01_hp/13_hermione_main/body_97.png"
                                                her "............"
                                                hide screen h_head2
                                                g9 "A-ah... Yes..."
                                                show screen h_head2
                                                $ h_body = "01_hp/13_hermione_main/body_97.png"
                                                her ".........."
                                                $ h_body = "01_hp/13_hermione_main/body_99.png"
                                                her "Fine! Have it your way, [genie_name]!"
                                                $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                her "{size=-5}(As usual...){/size}"
                                                hide screen h_head2
                                        show screen blktone
                                        with d3
                                        ">You keep on wanking while you watch Hermione's dance..."
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_90.png"
                                        her "Time for the finishing act I suppose..."
                                        hide screen h_head2
                                        m "Yes, [hermione_name]! Take them off!"
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_91.png"
                                        her "........"
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Hermione bends over slightly and slides her panties down..."
                                        ">You can see that she is doing her best to be graceful..."
                                        ">But she looks rather ridiculous in her attempts to act like a professional stripper..."
                                        hide screen blktone8 
                                        hide screen blktone
                                        with d3
                                        hide screen bld1
                                        with d3
                                        pause
                                        $ h_c_u_pic = "no_panties_dance_ani"
                                        hide screen no_shirt_no_skirt_dance
                                        show screen h_c_u
                                        with d3
                                        pause
                                        show screen bld1
                                        with d3
                                        show screen blktone
                                        with d3
                                        ">Nonetheless you decide to show her some appreciation..."
                                        ">By stroking your cock even faster!"
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_91.png"
                                        her ".........."
                                        hide screen h_head2
                                        show screen blktone8
                                        with d3
                                        ">Suddenly Hermione breaks into a whole series of rather complex pirouettes..."
                                        m "{size=-4}(This looks quite impressive actually...){/size}"
                                        ">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements..."
                                        m "{size=-4}(Did she practice this?){/size}"
                                        g9 "Oh, what do I care?"
                                        ">You stroke your diamond-hard cock furiously."
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_102.png"
                                        her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                                        hide screen h_head2
                                        ">Hermione performs another set of movements that could be considered classy..."
                                        ">if not for her naked tits bouncing all over the place..."
                                        g9 "Yes, yes, you little whore!"
                                        ">A few more movements, a couple of gestures and a little curtsy bow to the imaginary public..."
                                        show screen blkfade
                                        with d3
                                        $ hermione_chibi_xpos = -210 #400 = Near the desk.
                                        $ hermione_chibi_ypos = 10
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                        ">And then Hermione slumps on her butt, completely exhausted."
                                        hide screen blktone
                                        with d3
                                        hide screen blktone8
                                        with d3
                                        hide screen blkfade
                                        with d3
                                        hide screen bld1 
                                        with d3
                                        pause
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_102.png"
                                        her "Whew... This was--"
                                        hide screen h_head2
                                        with hpunch
                                        g4 "ARGH! YOU FUCKING CUNT!"
                                        hide screen hermione_main
                                        with d3
                                        show screen white 
                                        pause.1
                                        hide screen white
                                        pause.2
                                        show screen white 
                                        pause .1
                                        hide screen white
                                        with hpunch
                                        $ genie_chibi_xpos = -210
                                        $ genie_chibi_ypos = 10
                                        $ genie_cum_chibi_xpos =  -210
                                        $ genie_cum_chibi_ypos  = 10
                                        $ g_c_c_u_pic = "genie_cum_03"
                                        $ h_c_u_pic = "01_hp/08_animation_02/08_sits_02.png"
                                        show screen g_c_c_u
                                        pause
                                        $ uni_sperm = True #Triggers universal sperm to show on hermione_main screen.
                                        $ h_body = "01_hp/13_hermione_main/body_104.png"
                                        $ u_sperm = "01_hp/13_hermione_main/auto_04.png"
                                        show screen h_head2  
                                        her "??!!!"
                                        hide screen h_head2
                                        show screen bld1
                                        with d3
                                        $ h_body = "01_hp/13_hermione_main/body_97.png"
                                        show screen h_head2  
                                        her "[genie_name]!!!"
                                        $ g_c_c_u_pic = "01_hp/08_animation_02/09_cum_18.png"
                                        hide screen h_head2
                                        if d_flag_07: #Promised to hold it.
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_97.png" # HERMIONE
                                            her "No, [genie_name]! You promised!"
                                            hide screen h_head2
                                            g4 "Oh, man... This was pretty intense..."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_98.png" # HERMIONE
                                            her "You went back on your word, [genie_name]!"
                                            hide screen h_head2
                                            m "Huh? What are you talking about?"
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_113.png" # HERMIONE
                                            her "How could you do this to me, [genie_name]?"
                                            hide screen h_head2
                                            m "Oh, calm down, [hermione_name]."
                                            m "You earned your points today."
                                            m "Now, just get dressed and leave before somebody discovers you like this."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_114.png" # HERMIONE
                                            her "*sob!*........................"
                                            hide screen h_head2        
                                            $ mad += 50
                                            show screen blkfade 
                                            with d3
                                            $ uni_sperm = False #Sperm layer is not displayed.
                                            $ aftersperm = True #Aftersperm layer is displayed. 
                                            stop music fadeout 5.0
                                            ">.................{w}.................{w}.................{w}................."
                                            show screen h_head2                                                              # HERMIONE
                                            $ h_body = "01_hp/13_hermione_main/body_12.png" # HERMIONE
                                            her "...Can I just get paid now, [genie_name]... please?"
                                            hide screen h_head2   
                                            jump done_with_dancing
                                        else:
                                            $ h_body = "01_hp/13_hermione_main/body_97.png"
                                            show screen h_head2  
                                            her "it's so hot..."
                                            hide screen h_head2  
                                            $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png" # Genie stands still with his dick in hand.
                                            m "Aha... Yeah... This feels great..."
                                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                                            show screen h_head2  
                                            her "You came all over me..."
                                            her "I am your pupil and..."
                                            $ h_body = "01_hp/13_hermione_main/body_106.png"
                                            show screen h_head2  
                                            her "You just came on me..."
                                            hide screen h_head2  
                                            g9 "I know! Pretty exciting stuff, huh?!"
                                            $ h_body = "01_hp/13_hermione_main/body_107.png"
                                            show screen h_head2  
                                            her "Nothing of that sort!"
                                            #her "You should not have done this, [genie_name]!"
                                            her2 "You should have restrained yourself like a proper headmaster would!"
                                            hide screen h_head2  
                                            m "Really? What did you expect me to do?"
                                            m "Aim at the wall or just put it back in my pants and start cumming?"
                                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                                            show screen h_head2
                                            her "........"
                                            $ h_body = "01_hp/13_hermione_main/body_101.png"
                                            show screen h_head2
                                            her "Still, you should not have..."
                                            $ h_body = "01_hp/13_hermione_main/body_102.png"
                                            show screen h_head2
                                            her "I agreed to perform a striptease for you..."
                                            her "But I didn't agree to be defiled like this."
                                            hide screen h_head2  
                                            m "I think I know where this is going..."
                                            $ h_body = "01_hp/13_hermione_main/body_100.png"
                                            show screen h_head2
                                            her "I demand to be paid extra!"
                                            hide screen h_head2  
                                            m "Of course you do..."
                                            menu:
                                                m "..."
                                                "\"You get 1 extra point.\"":
                                                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "One extra point?"
                                                    $ h_body = "01_hp/13_hermione_main/body_98.png"
                                                    her2 "One meagre extra point for letting you do this to me?"
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    her "Now, that is just insulting, [genie_name]!"
                                                    hide screen h_head2  
                                                    m "One extra point, [hermione_name]. Take it or leave it."
                                                    $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "............."
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    her "I'll take it."
                                                    hide screen h_head2  
                                                    $ mad += 30
                                                    $ current_payout = 36
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You get 10 extra points.\"":
                                                    $ current_payout = 45
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Ten extra points [genie_name]?"
                                                    her "But that is not even nearly enough!"
                                                    hide screen h_head2  
                                                    m "Ten extra points. Take'em or leave'em [hermione_name]."
                                                    $ h_body = "01_hp/13_hermione_main/body_103.png"
                                                    show screen h_head2
                                                    her "..............."
                                                    $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                    show screen h_head2
                                                    her "Well, alright... Better than nothing I suppose..."
                                                    hide screen h_head2  
                                                    $ mad += 11
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You get 25 extra points.\"":
                                                    $ current_payout = 60
                                                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her2 "Yes, I believe this would be an appropriate amount."
                                                    hide screen h_head2  
                                                    m "are we good then?"
                                                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                                                    show screen h_head2
                                                    her "Yes, [genie_name]. Thank you [genie_name]."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You get 50 extra points.\"":
                                                    $ current_payout = 85
                                                    $ h_body = "01_hp/13_hermione_main/body_95.png"
                                                    show screen h_head2
                                                    her "Seriously?!"
                                                    $ h_body = "01_hp/13_hermione_main/body_94.png"
                                                    her "Oh, I don't know what to say..."
                                                    hide screen h_head2  
                                                    m "I enjoyed your performance [hermione_name]."
                                                    show screen h_head2
                                                    $ h_body = "01_hp/13_hermione_main/body_109.png"
                                                    her "Thank you [genie_name]..."
                                                    hide screen h_head2  
                                                    m "I also enjoyed plastering your agile little body with cum..."
                                                    $ h_body = "01_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "[genie_name]......"
                                                    hide screen h_head2  
                                                    m "So, just allow me to show my appreciation."
                                                    m "Fifty extra points. Well deserved, [hermione_name]."
                                                    $ h_body = "01_hp/13_hermione_main/body_108.png"
                                                    show screen h_head2
                                                    her "Thank very much, [genie_name]."
                                                    hide screen h_head2  
                                                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                                                    hide screen bld1
                                                    with d3
                                                    pause
                                                    show screen blkfade
                                                    with d7
                                                    pause.5
                                                    $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                    jump done_with_dancing
                                                "\"You're not getting shit!\"":
                                                    stop music fadeout 1.0
                                                    $ h_body = "01_hp/13_hermione_main/body_104.png"
                                                    show screen h_head2
                                                    her "What? Not even my usual pay?"
                                                    hide screen h_head2  
                                                    menu:
                                                        m "..."
                                                        "\"Oh, no, you are still getting that.\"":
                                                            $ mad += 30
                                                            $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "How generous of you, [genie_name]." 
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            $ aftersperm = True #Show cum stains on Hermione's uniform.
                                                            jump done_with_dancing
                                                        "\"No, not even that!\"":
                                                            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                                                            $ h_body = "01_hp/13_hermione_main/body_104.png"
                                                            show screen h_head2
                                                            her "!!!?"
                                                            her "I danced for you, [genie_name]..."
                                                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                                                            her "I degraded myself for your amusement..."
                                                            $ h_body = "01_hp/13_hermione_main/body_107.png"
                                                            her "I let you cum on me..."
                                                            $ h_body = "01_hp/13_hermione_main/body_110.png"
                                                            with hpunch
                                                            her "And I get NOTHING?!"
                                                            hide screen h_head2  
                                                            m "You are dismissed, [hermione_name]!"
                                                            $ h_body = "01_hp/13_hermione_main/body_101.png"
                                                            show screen h_head2
                                                            her "Oh, this is a new low even for you, [genie_name]!"
                                                            hide screen h_head2  
                                                            m "I said you are dismissed."
                                                            $ h_body = "01_hp/13_hermione_main/body_110.png"
                                                            show screen h_head2
                                                            her "*GROAN!*"
                                                            $ mad += 90
                                                            hide screen h_head2  
                                                            hide screen bld1
                                                            with d3
                                                            pause
                                                            show screen blkfade
                                                            with d7
                                                            pause.5
                                                            hide screen h_c_u
                                                            hide screen g_c_u
                                                            hide screen g_c_c_u # Genie's sperm. Universal.
                                                            hide screen ctc
                                                            hide screen chair_02
                                                            hide screen desk_02
                                                            show screen genie
                                                            show screen bld1
                                                            $ hermione_chibi_xpos = 400 #Near the desk.
                                                            $ hermione_chibi_ypos = 250 #Default: 250
                                                            show screen hermione_02 #Hermione stands still.
                                                            pause.1
                                                            hide screen blkfade
                                                            with d3
                                                            call music_block
                                                            jump could_not_flirt #Leaves without getting any points.
                                                        

                                    else: # You jerk off your cock and Hermione is NOT OK with it.
                                        $ h_body = "01_hp/13_hermione_main/body_103.png"
                                        show screen h_head2
                                        stop music fadeout 1.0
                                        her "No, [genie_name]!"
                                        hide screen h_head2  
                                        m "Huh?"
                                        show screen blkfade
                                        with d7
                                        ">Hermione jumps off your desk and starts to put her clothes back on while glaring at you..."
                                        m "Oh, come on! Don't leave me like that!"
                                        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                                        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                                        $ h_body = "01_hp/13_hermione_main/body_101.png"
                                        show screen h_head2
                                        her "The dance is over [genie_name]!"
                                        hide screen h_head2
                                        pause 1
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_79.png"
                                        her "I would like to get paid now!"
                                        hide screen h_head2
                                        m "Stubborn [hermione_name]..."
                                        ">You reluctantly put your cock away..."
                                        show screen h_head2
                                        $ h_body = "01_hp/13_hermione_main/body_79.png"
                                        her "I would like to get paid now."
                                        hide screen h_head2
                                        jump done_with_dancing
                                "\"Fine. There is no need for drama!\"": 
                                    $ h_body = "01_hp/13_hermione_main/body_103.png"
                                    show screen h_head2
                                    her2 "......................"
                                    hide screen h_head2
                                    pause.1
                                    hide screen no_shirt_no_skirt_dance
                                    show screen genie
                                    hide screen chair_02
                                    hide screen g_c_u
                                    hide screen desk_02
                                    show screen no_shirt_no_skirt_dance
                                    hide screen blkfade
                                    with fade
                                    pause
                                    show screen bld1
                                    with d3
                                    pass

                        "-Show some manners, just watch-":
                            pass
                    # JUST WATCHING.
                    show screen blktone
                    with d3
                    ">You watch Hermione Dance..."
                    $ h_body = "01_hp/13_hermione_main/body_97.png"
                    show screen h_head2
                    her "(Time for the finishing act I suppose...)"
                    hide screen h_head2
                    m "Yes, [hermione_name]! Take them off!"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_90.png"
                    her "........"
                    hide screen h_head2
                    show screen blktone8
                    with d3
                    ">Hermione bends over slightly and slides her panties down..."
                    ">You can see that she is doing her best to be graceful..."
                    ">But she looks rather ridiculous in her attempts to act like a professional stripper..."
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_109.png"
                    her ".........."
                    hide screen h_head2
                    ">Suddenly Hermione breaks into a whole series of rather complex pirouettes..."
                    hide screen h_head2
                    m "{size=-4}(This looks quite impressive actually...){/size}"
                    ">Hermione gives her breasts a squeeze followed by another series of rather complex (and naughty) movements..."
                    m "{size=-4}(Did she practice this?){/size}"
                    g9 "Oh, why would I care?"
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_102.png"
                    her "{size=-5}(Three-two-one... Three-two-one... And step!){/size}"
                    hide screen h_head2
                    ">Hermione performs another set of movements that could be considered classy if not for her naked tits bouncing all over the place..."
                    g9 "Yes, yes, you little harlot!"
                    
                    show screen blkfade
                    with d3
                    $ hermione_chibi_xpos = -210 #400 = Near the desk.
                    $ hermione_chibi_ypos = 10
                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                    ">A few more movements, a couple of gestures and a little curtsy bow to the imaginary audience and Hermione slumps on her butt completely exhausted."
                    show screen h_c_u
                    hide screen blktone
                    with d3
                    hide screen blktone8
                    with d3
                    hide screen blkfade
                    with d3
                    hide screen bld1 
                    with d3
                    pause
                    show screen h_head2
                    $ h_body = "01_hp/13_hermione_main/body_108.png"
                    show screen bld1
                    with d3
                    her "Whew... This was rather exciting..."
                    hide screen h_head2 
                    menu:
                        m "..."
                        "{size=-3}\"Good job, [hermione_name]! You sure know how to dance!\"{/size}":
                            m "Good job [hermione_name]!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_109.png"
                            her "Really?"
                            hide screen h_head2
                            m "Yes! You have a lot of talent for this!"
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_108.png"
                            her "Thank you [genie_name]."
                            hide screen h_head2
                        "{size=-3}\"Hm... This was quite awful...\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_105.png"
                            her "Oh... I'm sorry..."
                            hide screen h_head2
                            m "That's OK... You just need to practice more..."
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_107.png"
                            her "Em... I will keep that in mind, [genie_name]..."
                            hide screen h_head2
                        "{size=-3}\".................................................\"{/size}":
                            show screen h_head2
                            $ h_body = "01_hp/13_hermione_main/body_108.png"
                            her "......................."
                            hide screen h_head2

                    
                    $ h_c_u_pic = "01_hp/08_animation_02/08_sits.png"
                    hide screen bld1
                    show screen ctc
                    with d3
                    pause
                    show screen blkfade
                    with d7
                    pause.5

                            
        else: #Stripping only for Genie.
            jump no_snape_watching 

        
        
        
    label done_with_dancing:
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    $ badges = True # Shows any badges from hermione_main screen.
    
    m "Yes, [hermione_name]. [current_payout] to the \"Gryffindor\" house." 
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    
    her "Thank you, [genie_name]..."

    if whoring <= 11:
        $ whoring +=1

    $ request_11_points += 1

    
    

    $ sperm_on_tits = False
    $ uni_sperm = False

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)

    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    $ panties = True
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.
    call music_block
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
        
###################REQUEST_12 (Level 04) (Play with her tits.) (Day/Night) ############################################################################
label new_request_12: #LV.4 (Whoring = 9 - 11)
    hide screen hermione_main 
    with d3
    if request_12_points == 0:
        m "{size=-4}(I feel like playing with those titties.){/size}"
    else:
        m "{size=-4}(I feel like playing with those titties again.){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    if whoring <=8:
        jump too_much
        
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
        
    if request_12_points == 0 and whoring <= 14: # LEVEL 05 (one level higher then level at which it unlocks - 04) # FIRST TIME.
        m "[hermione_name]."
        call her_main("Yes, [genie_name]?","body_01")
        m "How about selling me another favour today?"
        call her_main("Uhm... Alright...","body_02")
        her "What will it be, [genie_name]?"
        m "Well, how about you come closer and bare your tits for me...?"
        call her_main("!!!","body_31")
        m "I want to give them a good squeeze."
        call her_main("[genie_name]! Don't you think this is too much?","body_66")
        m "You think?"
        her "I am not one of those harlots from \"Slytherin\", you know..."
        m "I know... You are from \"Gryfonmon\"... or something..." #<- GRYFFINDOR MISSPELLED ON PERPOUSE   I KNOW
        call her_main("And if I don't feel like it I don't have to sell you a single favour, [genie_name]!","body_29")
        m "Of course..."
        call her_main("...................","body_69")
        m "I'll give you 35 house points for this."
        call her_main(".......................","body_66")
        her "All you are going to do is watch, [genie_name]?"
        m "Well, I feel more like touching, actually..."
        her "...................................."


    else: # Intro. Not first time.
        if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # NOT A WHORE YET.
            m "[hermione_name]..."
            call her_main("[genie_name]?","body_01")
            m "I feel like playing with your tits a little..."
            call her_main("[genie_name]... I'd prefer it if you wouldn't make me such offers...","body_79")
            m "Why? Too hard to resist?"
            her "Nothing like that, [genie_name]."
            m "I'll give you 35 house points for this..."
            call her_main("..................","body_69")
            her "Well, alright... You can touch them a little..."
        elif whoring >= 15: # LEVEL 06 and higher # NASTY WHORE.
            m "[hermione_name]..."
            call her_main("[genie_name]?","body_01")
            m "I feel like playing with your tits a little..."
            call her_main("Of course [genie_name]...","body_78")
    
    hide screen hermione_main
    with d3
    hide screen blktone
    with d3
    hide screen bld1
    with d3
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=280 #Coordinates of it's movement. (To)
    $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 1
    show screen blkfade
    with Dissolve(1)
    pause.5


    hide screen hermione_walk_01
    hide screen genie
    show screen ctc
    #show screen chair_02 #Genie's chair.
    hide screen genie
    show screen genie_and_tits_01
    with d1
    hide screen blkfade
    with d5
    stop music fadeout 1.0
    pause
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    show screen blktone 
    with d3
    hide screen hermione_main
    with d3
    $ h_body = "01_hp/13_hermione_main/body_82.png" #Sprite of Hermione's upper body.
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    #$ only_upper = True #No lower body displayed. 
    $ badges = False
    $ lift_shirt = True
    show screen hermione_main
    with d3
    pause
    her "...................................."
    
    
    
    
    
    menu:
        m "..."
        "-Grab them-":
            label no_smacking_tits:
                pass
            hide screen hermione_main
            with d3
            show screen blkfade
            with d5
            hide screen hermione_04 #Stands with tits out.
            hide screen genie
            show screen groping_naked_tits
            with d1
            hide screen blkfade
            hide screen blktone
            with d5
            pause
            show screen bld1
            with d3
            

            
            if whoring >= 9 and whoring <= 14: # LEVEL 04 AND LEVEL 05 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).

                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                call her_head("..............................","body_118")    
                m "You have great tits, [hermione_name]..."
                call her_head("....................................","body_118") 
                m "You like it when I squeeze them like this?"
                call her_head("Excuse me, [genie_name], but you are confusing me with one of those lowly harlots again...","body_120")
                call her_head("I am only letting you fondle me because I am getting paid for it...","body_120")
                call her_head("Not because I enjoy it...","body_120")
                m "I see..."
                m "So, you're more like a prostitute then..."
                call her_head("[genie_name]!","body_119")
                call her_head("Prostitutes are getting paid to have sex with men...","body_119")
                call her_head("I'd never do something like that!","body_120") 
                show screen blktone
                with d3
                ">You squeeze one of the girl's tits tightly and give the other a couple of firm tugs."
                hide screen blktone
                with d3
                call her_head("Ah...","body_131") 
                m "Enjoying yourself, [hermione_name]?"
                if whoring >= 9 and whoring <= 11: # LEVEL 04 #  <=================================================================================== FIRST EVENT.
                    call her_head("[genie_name], I am only doing this--","body_120") 
                    show screen blktone
                    with d3
                    ">You squeeze both of her tits with force..."
                    hide screen blktone
                    with d3
                    call her_head("ah...","body_132") 
                    m "Tell me you like this, [hermione_name]!"
                    call her_head("[genie_name], I am only letting you do this to me because--","body_131") 
                    m "I know, know..."
                    m "You are starting to sound like a broken record."
                    call her_head("....","body_79") 
                    show screen blktone
                    with d3
                    show screen blkfade
                    with d7

                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc
                    $ only_upper = False #Bottom is displayed.

            
                    ">You let go of the girl's breasts..."
                else:  # LEVEL 05 # <=================================================================================== SECOND EVENT.
                    call her_head("Ah...","body_87")
                    show screen blktone
                    with d3
                    ">You squeeze her tits a few more times, then give them a firm tug..."
                    hide screen blktone
                    with d3
                    call her_head("Ah... [genie_name]...","body_31")
                    m "What? You do enjoy this, don't you?"
                    call her_head("No... I...","body_31")
                    m "Don't you lie to your headmaster, [hermione_name]!"
                    show screen blktone
                    with d3
                    ">You squeeze her tits again..."
                    hide screen blktone 
                    with d3
                    call her_head("Ah...","body_87")
                    call her_head("I am not lying, [genie_name]...","body_87")
                    call her_head("Why would I enjoy this?","body_31")
                    m "I don't know [hermione_name]. You tell me."
                    show screen blktone
                    with d3
                    ">You keep massaging her breasts..."
                    hide screen blktone
                    with d3
                    call her_head("Ah... I...","body_31")
                    m "Yes, what is it?"
                    call her_head("It's... It's nothing, [genie_name]...","body_117")
                    m "Oh, I think it's something."
                    m "I think you like me squeezing your tits like this."
                    call her_head("[genie_name], please...","body_118")
                    if daytime:
                        call her_head("Classes are about to start...","body_118")
                    else: 
                        call her_head("It's getting late...","body_118")
                    call her_head("Can I go now, [genie_name]? Please?","body_117")
                    show screen blkfade 
                    with d3
                    m "Sure, go ahead..."
                    call her_head("...............","body_118")
                    call her_head("[genie_name], your are still... Holding me...","body_117")
                    m "Oh, right... my bad...."
                    ">You let go of Hermione's breasts..."
                    
                    show screen genie
                    hide screen groping_naked_tits
                    hide screen ctc
                    $ only_upper = False #Bottom is displayed.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
               
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                call her_head("Ah...","body_121")
                m "A bit sensitive today, aren't you?"
                call her_head("I suppose...","body_128")
                call her_head("Ah...","body_131")
                m "You like it when I squeeze them like this?"
                call her_head("I do, [genie_name]... Ah...","body_128")
                m "Heh..."
                m "What if I pinch your nipples?"
                show screen blktone
                with d5
                call her_head("!!!","body_117")
                call her_head("Ah! [genie_name]...","body_131")
                m "And what if I do this?"
                show screen blktone8
                with d3
                ">You grab the girl by her hard nipples and start pulling..."
                hide screen blktone8
                with d3
                call her_head("Ah... Ah... Ah... [genie_name]...","body_132")
                m "What if I pull even harder?"
                call her_head("Ah... [genie_name], please...","body_130")
                show screen blktone8
                with d3
                ">Hermione clutches the edge of your desk to keep herself form taking a step towards you..."
                hide screen blktone8
                with d3
                m "Good girl..."
                call her_head("*Panting heavily*","body_123")
                m "Do you enjoy this?"
                call her_head("You are hurting me, [genie_name]...","body_139")
                m "But do you enjoy it?"
                if whoring <= 17:
                    call her_head("Ah... Yes, [genie_name]... I don't know why, but I do...","body_140")
                else:
                    call her_head("Ah... Yes, [genie_name]... I love it...","body_138")
                m "Good girl..."
                show screen blktone8
                with d3
                ">You let go of her nipples..."
                hide screen blktone8
                with d3
                call her_head("Ah...","body_138")
                show screen blkfade
                with d5
                m "This will be all for today, [hermione_name]..."
                call her_head("Oh...?","body_139")
                m "What is it? You look disappointed."
                m "I will pay you of course..."
                call her_head("That's not it, [genie_name]...","body_141")
                call her_head("It's...","body_141")
                if daytime:
                    call her_head("It's just that I still have some time left before I have to leave for the classes and...","body_139")
                else:
                    call her_head("It's not really that late yet, is it?","body_139")
                call her_head("uhm...","body_141")
                call her_head("...................","body_141")
                m "You want me to hurt you some more, don't you?"
                if whoring <= 17:
                    call her_head("I don't \"want to\"... ","body_139")
                    call her_head("But if you insist [genie_name]...","body_138")
                    m "Well, I do insist... apparently."
                else:
                    call her_head("Yes please [genie_name]","body_139")
                    call her_head("I'll even let you do it for free...","body_139")
                    m "Well, in that case"
                call her_head("Ah...","body_138")
                hide screen blkfade
                with d5
                
                show screen ctc
                pause
                hide screen ctc
                
                #BLACK FADE
                show screen blkfade
                with d7
                ">You spend some more time with Hermione's breasts..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                $ only_upper = False #Bottom is displayed.

        "-Slap them-":
            hide screen hermione_main
            with d5
            ">You give Hermione's tits a loud slap!"
            $ renpy.play('sounds/slap.mp3') #SLAP!
            show screen white
            with hpunch
            pause.08
            hide screen white
            show screen bld1
            if whoring >= 9 and whoring <= 11: # LEVEL 04 # <=================================================================================== FIRST EVENT. (HERMIONE IS UNWILLING).
                call her_head("!!!","182")
                call her_head("Ouch! It hurts! *SOB!*","183")
                m "Did you like it though?"
                call her_head("Did I... \"like it\, [genie_name]..?","body_81")
                her "What girl in her right mind would like to be treated this way?"
                stop music fadeout 1.0
                call her_head("You are a mean and demented old man!","184")
                hide screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3
                show screen blkfade
                with d3
                # RUNS OFF
                $ mad += 20
                m "............"
                m "Well, no points for \"Gryffindor\" then..."
                
                show screen genie
                hide screen groping_naked_tits
                hide screen ctc
                $ only_upper = False #Bottom is displayed.
                hide screen genie_and_tits_01
                call music_block
                jump could_not_flirt #Sent here when choose "Favor failed! No points for you!" (Hermione is leaving without getting any points).
                
                    
            elif whoring >= 12 and whoring <= 14: # LEVEL 05 # <=================================================================================== SECOND EVENT.
                call her_head("!!!","182")
                call her_head("Ouch!","183")
                her "[genie_name], what did you do this for?"
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                call her_head("...Of course, not, [genie_name].","body_83")
                m "Let's try this again, then."
                call her_head("What?","body_82")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3   
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                call her_head("!!!","182")
                her "Ouch! Stop hurting me!"
                m "Admit that you enjoy it and I will."
                call her_head("But I don't...","body_85")
                her "And if you plan to keep on doing this to me, [genie_name]..."
                call her_head("...then I think I should leave.","body_81")
                m "Fine, fine..."
                hide screen hermione_main
                with d3
                jump no_smacking_tits #Jumps to usual tits molesting scene.

            elif whoring >= 15: # LEVEL 06 and higher # <=================================================================================== THIRD EVENT. 
                call her_head("Ah!!!","182")
                call her_head("[genie_name], why did you do that?","185")
                m "Dunno... Seemed like a good idea..."
                m "Did you like it?"
                call her_head("..........","body_82")
                her "I am not a pervert..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d3
                ">You give Hermione's tits another loud smack!"
                hide screen blktone8
                with d3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.08
                hide screen white
                call her_head("A-ah!!!","186")
                m "Tell me you like it!"
                her "[genie_name]... I..."
                hide screen hermione_main
                with d3
                show screen blktone8
                with d5
                ">You unleash a whole series of slaps!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                ">Hermione's tits bounce allover the place, completely out of control"
                hide screen blktone8
                with d5
                call her_head("A-ah!!! Ah!!! A-a-aha!!!","187")
                m "You enjoy this. Admit it."
                call her_head("...........","188")
                hide screen hermione_main
                hide screen ctc
                with d3
                ">You smack her tits again."
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                call her_head("A-ah! Yes! I do, I do! A-ah...","187")
                call her_head("...does this mean I'm a pervert, [genie_name]?","184")
                m "What?"
                m "Stop being silly, [hermione_name]."
                m "It is completely natural for a girl to enjoy her tits getting smacked around a little."
                her "......"
                her "Are you sure about that, [genie_name]?"
                m "Yes. Believe me, I know."
                hide screen hermione_main
                with d3
                ">You give her tits one more slap!"
                $ renpy.play('sounds/slap.mp3') #SLAP!
                show screen white
                with hpunch
                pause.05
                hide screen white
                pause.3
                call her_head("A-ah... Yes... Thank you, [genie_name].","187")
                hide screen hermione_main
                with d3
                m "Well... Enough with the slapping for now..."
                jump no_smacking_tits #Jumps to usual tits molesting scene.

    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    stop music fadeout 1.0
    if whoring <= 17:
        m "Yes, [hermione_name].  35 points to \"Gryffindor\"." 
        $ gryffindor +=35
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    $ badges = True
    $ lift_shirt = False
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 11: # If still of level of unlocking - 04
        $ whoring +=1

    $ request_12_points += 1

    if whoring >= 9 and whoring <= 11:
        $ level = "04"
        $ new_request_12_01 = True # HEARTS.
        $ new_request_12_heart = 1
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_12_02 = True # HEARTS.
        $ new_request_12_heart = 2
    if whoring >= 15:
        $ level = "06"
        $ new_request_12_03 = True # HEARTS.
        $ new_request_12_heart = 3


    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ aftersperm = False #Show cum stains on Hermione's uniform.
    
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    jump end_hermione_personal_request      
        
###################REQUEST_16 (Level 05) (HANDJOB) (Day/Night) #####################################################
label new_request_16: #LV.5 (Whoring = 12 - 14)
    hide screen hermione_main 
    with d3
    if request_16_points == 0:
        m "{size=-4}(Should I ask her for a handjob?){/size}"
    else:
        m "{size=-4}(Should I ask the [hermione_name] to give me another handjob?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    $ current_payout = 45 #Used when haggling about price of th favor.
    
    hide screen hermione_main
    with d3
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if request_16_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]."
        call her_main("Yes, [genie_name]?","body_01")
        m "Do you know what a \"handjob\" is?"
        if whoring <=11:
            jump too_much
        call her_main("Why?","body_79")
        m "I feel like getting one..."
        call her_main("[genie_name]!","body_47")
        m "Just another favour. No big deal, right?"
        call her_main("......","body_66")
        call her_main("{size=-7}I want 100 house points for this...{/size}","body_34")
        m "Huh? What was that?"
        call her_main("I want 100 house points for this!!!","body_32")
        m "100 house points, huh?"
        m "And you will stroke my cock and everything?"
        call her_main("{size=-7}Yes...{/size}","body_66")
        m "Sorry, I couldn't hear you..."
        call her_main("Yes, I said yes! I will stroke your cock, [genie_name]!","body_32")
        label back_to_handjob_choices:
        menu:
            m "..."
            "\"You will get 15 house points.\"":
                $ mad +=7
                call her_main("For 15 house points I suppose I could let you molest me a little, but that is all you'll be getting, [genie_name].","body_69")
                her "I will not stoop as low as to sell handjobs for 15 house points."
                her "That is just insulting, [genie_name]."
                jump back_to_handjob_choices
            "\"you will get 45 house points.\"":
                call her_main(".....","body_69")
                call her_main("45 house points...?","body_87")
                her "This could put \"Gryffindor\" back in the lead..."
                m "Is that a \"yes\"?"
                call her_main("Yes, it is a yes, [genie_name].","body_79")
                m "Great!"
            "\"you will get 100 house points.\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                $ current_payout = 100 #Used when haggling about price of th favor.
                $ mad = 0
                call her_main("100 house points?!","body_72")
                her "This will definitely put \"Gryffindor\" in the lead!"
                m "Is that a \"yes\" then?"
                call her_main("Of course!","body_75")
                call her_main("If it will bring \"Gryffindor\" 100 house points, I don't mind touching your... thing a little.","body_80")
        # GENIE STANDS WITH HIS COCK OUT
       
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02

        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        call her_head("...........","body_31")
        m "Whenever you're ready, [hermione_name]."
        call her_head("Right...","body_34")
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3
        label event_01_round_02:
        ">Hermione puts her slender hands on your cock..."
        m "Good. Now stroke it."
        call her_head("Right...","body_34") 
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d3
        show screen ctc
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen ctc
        show screen bld1
        with d3
        g9 "Nice..."
        if request_16_points == 0:
            call her_head("!!!","body_48")
            call her_head("Are you about to finish, [genie_name]?!")
            m "About to finish?"
            m "Don't be ridiculous [hermione_name], we are just getting started."
            call her_head("","")
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
            her "Oh..."
            her "......"
            call her_head("You will give me a warning though, won't you, [genie_name]?","body_44") 
        else:
            call her_head("[genie_name]...?","body_34")    
            m "What is it?"
            call her_head("Will you warn me before... uhm... you now...","body_34")
        $ d_flag_01 = False #If TRUE Genie promised to warn her.
        menu:
            m "..."
            "\"Of course I'll let you know when it's time.\"":
                $ d_flag_01 = True #If TRUE Genie promised to warn her.
                call her_head("Thank you, [genie_name].","body_33") 
            "\"I myself don't always know when...\"":
                call her_head("Really? But I thought...","body_31")
                call her_head("Well, never mind then...","body_33") 
        call her_head("........","body_31") 
        m "............."
        call her_head(".............","body_33")
        call her_head("Err... [genie_name]?") 
        m "Yes, what is it?"
        call her_head("How long do you think this will take?","body_31") 
        m "Why?"
        if daytime:
            call her_head("Well, it's just that my classes are about to start...","body_44")
        else: 
            call her_head("Well, it's just that I have this paper that I need to finish...","body_44")
            call her_head("It's due tomorrow, and it's getting pretty late...")
        m "Do you need the points or not?"
        call her_head("I do, [genie_name]! I'm sorry...","body_74")
        call her_head("I will just keep on stroking it then...")
        m "Well, there is something you could do to speed up the process..."
        call her_head("Really? What is it [genie_name]?","body_45") 
        menu:
            m "..."
            "\"Tell me how much of a whore you are!\"":
                call her_head("What?","body_47")
                call her_head("But I'm not...")
                m "No need to be honest, [hermione_name]."
                m "Just make things up."
                call her_head("Really?","body_44") 
                m "Sure. Just have fun with it."
                call her_head("Well, in that case...","body_87")
                call her_head("I am a... whore.")
                m "Heh... good. Go on."
                call her_head("I am a big whore...","body_87") 
                m "Yes, you are."
                call her_head("I am the biggest whore in England!","body_79")
                call her_head("I try to act innocent, but in truth all I think about is cock!")
                m "Yes, you little slut!"
                call her_head("Yes! I am a slut!","body_69")
                call her_head("I crave cock all the time.")
                m "Very nice!"
                m "But, like I said, you don't have to be honest."
                call her_head("What?","body_48")
                call her_head("[genie_name], those things I say are not true!","body_44") 
                g9 "Heh... I know. I'm just messing with you."
                call her_head("[genie_name]!","body_66") 
                m "You are doing a great job, though. Keep at it!"
                call her_head(".....","body_87")
                call her_head("I love cock...")
                call her_head("And I love... spunk...","body_88")
                call her_head("And semen... and sperm...")
                call her_head("I love to drink sperm...")
                call her_head("I want you to feed me your sperm, [genie_name]!","body_65") 
                g4 "!!!"
                call her_head("Or better yet, pump me full of it, [genie_name]!","body_64")
                hide screen ctc
                hide screen h_head2 
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"
            
            "\"Stick your tongue out and look at me!\"":
                call her_head("What?","body_45") 
                m "Just do it, slut."
                call her_head("Like this?","body_38") 
                m "Yes, good. Keep looking into my eyes and stroke my cock."
                call her_head(".....................","body_115") 
                m "Yes... Good..."
                call her_head("...........","body_115")
                call her_head("...........")
                call her_head("I can't keep my mouth open for so long, [genie_name]. I will start to drool...","body_31") 
                m "But I want you to drool..."
                call her_head("What? But I will look silly!","body_31") 
                m "That's the point, [hermione_name]!"
                call her_head(".......","body_29") 
                m "Don't you want to be done with this as soon as possible?"
                call her_head("............","body_33")
                call her_head("A-ha.....","body_115") 
                m "Good, [hermione_name]."
                call her_head("..............","body_115") 
                m "Yes, keep on stroking my cock."
                call her_head("..................","body_115")
                g4 "Oh... I just want to slide my cock into that wet hole of a mouth of yours!"
                call her_head(".................","body_40") 
                m "No, keep on looking at me!"
                call her_head(".....................","body_115") 
                m "Yes, you little slut!"
                call her_head("......................","body_116") 
                m "I want to cum in that mouth, yes..."
                call her_head("................","body_116") 
                with hpunch
                g4 "{size=-4}(Here it comes! Should I warn her?){/size}"
            "\"Give my cock a kiss!\"":
                call her_head("Excuse me?","body_47") 
                m "You know, just a little kiss, right on the tip."
                call her_head(".............","body_47")
                call her_head("...with my lips?","body_48") 
                m "Sure... That will speed things up, I'm telling you."
                call her_head("*sigh!*..............","body_87")
                call her_head("Well, I might as well, I suppose...")
                ">Hermione gives the tip of your engorged cock a tender kiss."
                
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                call her_head("Like this?","body_87") 
                m "Wasn't that bad, was it?"
                call her_head("No, I suppose not...","body_44") 
                m "Can you do it again, then?"
                call her_head("I could...","body_33") 
                m "Do it!"
                call her_head("Well, alright...","body_31")
                ">Hermione gives your cock another kiss..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                ">This time she lingers a moment longer..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3

                hide screen h_head2 
                m "Good... Now do it again and just stay there for a while."
                call her_head("You mean with my lips touching your... cock, [genie_name]?","body_31")
                call her_head("No, I will look stupid...","body_29") 
                m "Don't be silly, [hermione_name]. Nobody is watching."
                call her_head("You are, [genie_name].","body_87") 
                m "But that's the whole point!"
                call her_head("......","body_79") 
                m "It will make me cum in no time!"
                call her_head("...............","body_69") 
                m "And then you can just get out and and take care of your business today."
                call her_head(".............","body_66")
                call her_head("Well, alright then....","body_87")
                ">Hermione reaches down with her lips again..."
                ">She touches the tip of your cock with her lips and keeps them there..."
                $ g_c_u_pic = "kiss_ani"
                $ renpy.play('sounds/kiss.mp3') 
                with kissiris
                pause
                show screen blktone
                with d3
                m "Very good..."
                m "Now touch it with your tongue."
                her "??!"
                m "That's the last thing I will be asking of you today."
                her "............"
                ">You feel the tip of Hermione's tongue warily rubbing against the head of your cock..."
                m "Yes, like this..."
                ">Hermione wiggles her tongue a little...."
                m "Yes... Good..."
                show screen blkfade
                with d3
                $ g_c_u_pic = "handjob_ani"
                hide screen blkfade
                with d3
                call her_head("So, did it work? Are you ready to... finish, [genie_name]?","body_87") 
                g4 "{size=-4}(Surprisingly, yes! I'm about to cum! Should I warn her?){/size}"
                hide screen blktone
        menu:
            m "..."
            "-Give her a warning-":
                g4 "Here it comes, [hermione_name]! You better be ready!"
                call her_head("What? So soon?!","body_48") 
                g4 "{size=+5}Yeah, you did a great job!!!{/size}"
                g4 "{size=+5}You little whore!!!{/size}"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade 
                with d5
                call her_head("No, [genie_name], wait, I--","body_117") 
                g4 "{size=+5}Too late for that, slut!{/size}"
                call her_head("*whimper*","body_118")       
                ">Hermione suddenly slides your already dripping cock under her shirt..."
                g4 "?!!"
                ">The sensation of her warm skin against your cock overwhelms you and you begin to ejaculate like a mad-man."
                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                
                
                
                
                call her_head("!!!!!!!!!!!","body_48") 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                stop music fadeout 1.0
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                call her_head(".......................","body_119")                
                m "..........................."
                call her_head(".......................","body_119")    
                m "....................?"
                call her_head(".......................","body_118")    
                m "...What the fuck just happened?"
                show screen bld1
                with d3
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                call her_head("I don't know... I suppose I just panicked...","body_34")
                if daytime:
                    call her_head("My classes are about to start and I didn't want you to ruin my uniform, [genie_name]...","body_34") 
                    m "So you'll go to classes like this now?"
                    m "With your clothes all sperm-soaked from the inside?"
                    call her_head("What choice do I have?","body_118")
                    call her_head("I can't just skip a class...")
                else:
                    call her_head("At this hour The \"Gryffindor\" common room will be full of people...","body_34")
                    call her_head("I didn't want to have to return there all covered in your... spunk, [genie_name].")
                    call her_head("Oh, it's getting pretty late...","body_117") 
                    m "So you will go like this, instead?"
                    m "With your clothes all sperm-soaked from the inside?"
                    call her_head("What choice do I have?","body_118")     
                    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                ">Hermione releases your still pulsating cock."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                call her_head("Ew... Your sperm, [genie_name]...","body_118")
                call her_head("It's everywhere under my uniform...","body_117")          
                m "Just put it in your mouth next time."
                call her_head("I... don't think so, [genie_name].","body_79")
                call her_head("I really need to go. Can I just get paid now?")
                
                
#                g4 "You whore! You little nasty wore!"
#                g4 "There! Allover your fucking belly and tits!"
#                her "Ah! It's so hot!"
#                hide screen h_head2 
#                g4 "Oh, yes, this is so good!"
#                her "Ah..."
#                hide screen h_head2 
#                m "..............."
#                her "............"
#                hide screen h_head2 
#                m "I think I'm done..."
#                her "Oh..."
#                ">Hermione releases your still pulsating cock."
#                her "Ew... Your sperm, [genie_name]..."
#                her "It's everywhere under my uniform..."
#                hide screen h_head2 
#                m "What possessed you to put my cock there, [hermione_name]?"
                

            "-Just start cumming-":
                hide screen ctc
                with hpunch
                g4 "ARGH!"
                show screen blkfade
                with d3
                call her_head("WHAT?!","body_48")               
                g4 "Take this!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                
                
                  
                call her_head("!!!!!!!!!!!","body_48") 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                call her_head(".......................","body_119")          
                m "Yes... I Feel so much better now..."
                pause
                
                hide screen hermion_main
                with d3
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
                $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                
                call her_main("","body_19")
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                
                call her_main("[genie_name]! What have you done?!","body_32")
                m "What?"
                if d_flag_01: #If TRUE Genie promised to warn her.
                    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                    $ mad += 11
                    call her_main("You promised to give me a warning, [genie_name]!","body_47")
                    m "Oh, that's right... My bad."
                    call her_main("My uniform is ruined...","body_69")
                    her "...I would like to get paid now."
                    hide screen hermione_main     
                    with d3
                    $ uni_sperm = False
                else:
                    if daytime:
                        call her_main("My uniform is ruined now!","body_69")
                        call her_main("My classes are about to start and I can't go looking like this!","body_87")
                        m "Of course you can, just wipe it off or something..."
                        m "Nobody will even notice."
                        call her_main("...I would like to get paid now.","body_79")
                        hide screen hermione_main     
                        with d3
                        $ uni_sperm = False
                    else:
                        call her_main("My uniform is ruined!","body_69")
                        her "Am I supposed to go back to the \"Gryffindor\" common room looking like this?!"
                        m "Why not? You look hot, [hermione_name]!"
                        call her_main("[genie_name]!!!","body_79")
                        m "Alright, alright. Just wipe it off or something."
                        m "Nobody will even notice."
                        call her_main("...I would like to get paid now.","body_79")
                        hide screen hermione_main     
                        with d3
                        $ uni_sperm = False
        #her "Can I just get paid now?"

    elif request_16_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "[hermione_name]?"
        call her_main("Yes, [genie_name]?","body_01")
        m "Do you know what a \"handjob\" is?"
        call her_main("You have asked me that already, [genie_name].","body_66")
        m "Ah, that's right."
        m "Well, I want you to play with my cock again."
        call her_main("[genie_name], you are being vulgar again...","body_120")
        m "Fine, fine."
        m "[hermione_name], I would like to buy another favour from you today."
        call her_main("Of course, [genie_name].","body_69")
        g9 "The favour being you playing with my cock!"
        call her_main("..............","body_66")
        m "Oh, come on. For the honour of the \"Gryffindors\"?"
        call her_main(".............","body_47")
        g9 "Play with my cock for the honour of the \"Gryffindors\", [hermione_name]!"
        call her_main("Stop saying that, [genie_name]...","body_86")
        #Genie with his cock out
        m "Come on [hermione_name], it's not like I'm asking you to do this for free."
        call her_main(".......","body_69")
        stop music fadeout 4.0
        

        hide screen hermione_main            
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        
                                                                                                                                                                               #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone

        jump event_01_round_02


    elif request_16_points >= 2: # THIRD EVENT <========================================================================================================= EVENT 03
        $ new_request_16_03 = True #  Hearts
        $ new_request_16_heart = 3
        
        m "[hermione_name]?"
        call her_main("[genie_name]?","body_01")
        m "You don't mind giving me another handjob, do you?"
        if whoring <= 16:
            call her_main("As long as I am getting paid...","body_68")
            m "Well, come here then. Time to earn those points."
        else:
            call her_main("Of course not [genie_name]...","body_68")
            m "Well, come here then."
        
        
        hide screen hermione_main            
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause.1
        show screen blkfade
        with Dissolve(1)
        pause.3

        hide screen genie
        $ genie_chibi_xpos = 5 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "jerking_off_02_ani"
        show screen chair_02
        show screen g_c_u
        show screen desk_02
        hide screen blktone
        
        
        
        ">Hermione puts her slender hands on your cock..."
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=290 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        stop music fadeout 3.0
        call her_head("Do you like it when I do it like this, [genie_name]?","body_68")
        g9 "Actually, yes! Very nice!"
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        #Stroking the cock.
        $ genie_chibi_xpos = 60 #-185 behind the desk.
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "handjob_ani"
        hide screen hermione_walk_01 
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3

        m "Yes, yes, like that..."
        m "Hm... You are getting pretty good at this."
        call her_head("Thank you, [genie_name].","body_74")
        call her_head("I figured the better I do this, the sooner it'll be over.")
        m "Hm..."
        menu:
            m "..."
            "\"What do you think of my cock?\"":
                call her_head("Huh?","body_31")
                call her_head("Oh, that's right...")
                call her_head("I need to compliment your penis! I completely forgot about that!","body_34")         
                m "Well, you don't have to--"
                call her_head("[genie_name], let me be honest with you...","body_120")         
                m "Yes?"
                call her_head("You have the biggest penis I have ever seen!","body_111")         
                m "Well I suppo--"
                call her_head("Not done yet!","body_30")         
                m "Apologies."
                call her_head("Your penis is so big it almost scares me!","body_118")      
                g9 "You little mynx. You know exactly what to say..."
                call her_head("And yet I lust for it...","body_121")
                call her_head("Any woman would be happy to have your huge penis inside of her!")
                m "...you're good!"
                call her_head("There is more!","body_30")         
                m "By all means..."
                call her_head("I think your magnificent cock is a blessing to this world!","body_30")         
                m "Well, I wouldn't go that far--"
                call her_head("Listen to me, [genie_name]!","body_30")
                call her_head("I think a statue dedicated to your magnificent penis shall be erected in every city!")
                call her_head("So that people of the world could worship your phallus freely!")
                m "OK, I think I've heard enough."
                call her_head("Too much?","body_122")         
                m "Yeah, just a bit."
                call her_head("Sorry...","body_34")         
                m "No biggie. Just keep on stroking it."
                call her_head(".................","body_121")  
                show screen blktone
                with d3
                ">Hermione keeps on stroking your cock."
                ">She is doing a great job of it too."  
                hide screen blktone
                with d3
                m "Yes, yes... Like that."
                
            "\"Call yourself a whore, [hermione_name]!\"":
                call her_head("Excuse me?","body_31")
                call her_head("Oh, that's right! I'm supposed to degrade myself, right?","body_17")  
                m "Well, you don't have to, but..."
                call her_head("That's alright, I don't mind.","body_120")
                call her_head("Alright then! I am a whore!","body_45")  
                m "Good. Glad we established that."
                m "Now I want you to say..."
                menu:
                    m "..."
                    "\"I am a worthless slut!\"":
                        call her_head("Of course.","body_122")
                        call her_head("I am a worthless slut.","body_121")
                        call her_head("A dirty little slut, that's what I am.")
                        m "Yes! Good!"
                    "\"I live to suck cock!\"":
                        call her_head("Em...","body_122")
                        call her_head("I live to suck penis, er... I mean cock...","body_45")  
                        m "Really? Well why don't you suck on this one then?"
                        call her_head("[genie_name], I am just repeating after you...","body_111")  
                        m "Really? Could've fooled me...."
                        call her_head("....................","body_122")
                        m ".................."
                    "\"I love to swallow cum!\"":
                        call her_head("I love to... ehm... swallow cum.","body_122")  
                        m "You hesitated there for a moment."
                        call her_head("Yes, I know....","body_122")
                        call her_head("Let me try again...")
                        call her_head("I love to swallow cum!","body_121")
                        call her_head("It is truly the best to swallow cum!")
                        call her_head("I love it!")
                        call her_head("...................................","body_123")
                        call her_head("How was that, [genie_name]?","body_122")  
                        m "Perfect." 
            "\"This is really good. Did you practice?\"":
                call her_head("Hm?","body_74")
                call her_head("Sort of... Well not really...")
                call her_head("I had a talk with the girls, and...","body_122")
                m "About handjobs?"
                call her_head("Among other things...","body_80")    
                m "So those girls of yours, they know a lot about such things?"
                call her_head("Actually, yes. I was surprised myself.","body_48")
                call her_head("All sorts of weird sexual things seem to be happening lately in our school...","body_68")
                call her_head("Can't say I approve of that...")
                call her_head("But they did teach me quite a few... tricks.","body_74")    
                m "Really? Like what?"
                call her_head("Well, let's see...","body_124")
                call her_head("If I put one of my hands here...")
                call her_head("And another one here...")
                m "Oh, I see... Yes, this feels quite good."
                call her_head("Does it?","body_122")
                call her_head("So Ginny was right about this one...","body_68")
                g4 "What did you just say?"
                call her_head("Ginny Weasley, she taught me this one.","body_74")    
                m "Oh, right..."
                call her_head("She said any boy would fall in love with me if I did this to him...","body_124")
                call her_head("There is also this thing when I form a ring with my fingers...")
                call her_head("And then I put one finger here...")
                m "Hm... I don't feel anything..."
                call her_head("Really?","body_118")
                her "Hm..."
                call her_head("Oh! That's right!","body_124")
                call her_head("The finger goes here! Silly me!")
                with hpunch
                with kissiris
                g4 "Oh!!! By the great desert sands, yes!"
                call her_head("Really? That good?","body_80")
                call her_head("What if I keep doing this but stick my finger here and press a little...","body_124")    
                g4 "[hermione_name], you are killing me!"
                call her_head("Really? Really?!","body_80")
                call her_head("This is actually quite fun!")
                call her_head("Err... I mean...","body_122")
                call her_head("I am only doing this to help my house of course...")
                m "Yes, yes... The \"Gryffindor\" honour and all that."
                m "You just keep massaging that spot..."
                m "Oh, yes..."
                call her_head("...............","body_124")
        m "Yes... Keep stroking it."
        call her_head("..............","body_122")
        m "Now I want you to say..."
        menu:
            m "..."
            "{size=-4}\"I fantasize about being raped by my father.\"{/size}":
                $ mad += 11
                call her_head("I do not!","body_77")
                m "I know. Just say it."
                call her_head("My father? That's disgusting, [genie_name]!","body_76")
                m "Humour me."
                call her_head("...........","body_79")
                call her_head("Well...","body_87")
                call her_head("Sometimes I fantasize about being raped...")
                call her_head(".......")
                m "I see. And in those fantasies of yours..."
                m "Who is doing the raping?"
                call her_head("My father...?","body_117")
                m "Do you enjoy it?"
                call her_head("No. I cry and beg for him to stop!","body_118")
                m "Heh... Nice."
                call her_head(".......","body_118")
                m "Well, this wasn't that hard, was--"
                call her_head("I scream for my Mommy but she is still at work...","body_67")
                m "Huh?"
                call her_head("My daddy takes me to my room...","body_33")
                call her_head("He throws me on my bed!")
                call her_head("I cry \"No, daddy, please, I'm still a virgin!\"","body_32")
                $ g_c_u_pic= "01_hp/08_animation_02/12_handjob_01.png"
                call her_head("But He doesn't listen! He rips my panties off!","body_123")
                call her_head("I beg him to stop! I scream and I scream!","body_22")
                m "Uhm, [hermione_name]?"
                call her_head("Yes?","body_21")
                m "You are not stroking my cock anymore..."
                call her_head("Oh, I am sorry, [genie_name].","body_24")
                call her_head("I got lost in thought...")
                $ g_c_u_pic = "handjob_ani"
                call her_head("But everything I just said is not true of course!","body_31")
                call her_head("I never have fantasies like that!")
                m "Right."
            "{size=-4}\"Sometimes I get lonely and let my dog mount me.\"{/size}":
                call her_head("What?!","body_18")
                call her_head("That's disgusting.","body_17")
                call her_head("Dogs carry {size=+5}STD{/size}s, [genie_name].","body_16")
                m "Actually, human and canine {size=+5}STD{/size}s are species specific..."
                m "Means that they can only be spread to the same species."
                call her_head("............","body_08")
                m "Also I hear that many women do enjoy getting \"knotted\" quite a bit."
                call her_head("What does getting \"knotted\" mean?","body_07")
                m "Ehm... Well..."
                m "Ah, it doesn't matter."
                m "Just say the thing!"
                call her_head("Fine!","body_03")
                call her_head("Sometimes I get lonely and let my dog mount me.","body_08")
                m "That sounded so fake..."
                call her_head("Because we don't even own a dog!","body_07")
                m "Fine, whatever, let's just move on then..."
            "{size=-4}\"-Manual user input-\"{/size}":

                # The phrase in the brackets is the text that the game will display to prompt 
                # the player to enter the name they've chosen.

                $ tmp_name = renpy.input("(Use keyboard to enter the phrase.)")

                $ tmp_name = tmp_name.strip()
                # The .strip() instruction removes any extra spaces the player may have typed by accident.

                #  If the player can't be bothered to choose a name, then we
                #  choose a suitable one for them:
                if tmp_name == "":
                    $ tmp_name="I'm a whore."
                    call her_head("Hm...?","body_29")
                    call her_head("Should I just say \"I'm a whore\" as usual?")
                if one_out_of_three == 1:
                    call her_head("I don't want to say that...","body_29")
                    m "Oh, just do it, [hermione_name]."
                    call her_head("...........","body_29")
                    call her_head("[tmp_name]","body_30")
                    g9 "He-he..."
                elif one_out_of_three == 2:
                    call her_head("Huh?","body_29")
                    call her_head("What does That have to do with anything?")
                    m "Just say it."
                    call her_head("......","body_29")
                    m "Come on, humour me."
                    call her_head("[tmp_name]","body_30")
                    g9 "He-he..."
                    hide screen h_head2
                elif one_out_of_three == 3:
                    call her_head("...........","body_29")
                    call her_head("Do I really have to?")
                    m "Just say it."
                    call her_head("[tmp_name]","body_30")
                    g9 "He-he..."
        
        #CUMMING
        m "Hm..."
        m "I love that thing you do with the palm of your hand!"
        call her_head("You noticed...?","body_122")
        call her_head("Shall I do it some more then?")
        show screen blkfade
        with d3
        ">Hermione presses her palm against the tip of your pulsating cock and starts rubbing it very gently..."
        m "Oh yes!!!"
        stop music fadeout 1.0
        g4 "{size=-5}(I think this is it! Should I give her a waring?){/size}"
        menu:
            m "..."
            "\"(Yes, I must warn her).\"":
                g4 "I think I'm about to--"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                ">Hermione swiftly pulls her shirt up..."
                ">She then pushes your already dribbling cock against her belly and covers it up again..."
                ">The sensation of her skin under your engorged cock almost makes you lightheaded..."
                ">Hermione placed your cock a bit higher than you would expect..."
                ">You can feel her incredibly soft tits rubbing against the tip of your cock..."
               
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
              
                
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                
                
                
                call her_head("!!!!!!!!!!!","body_48") 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "undershirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                pause 
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                

                
                
                g4 "Argh! You whore!"
                call her_head("Yes, [genie_name]! Just let it out!","body_124")       
                g4 "Argh! Fucking slut!"
                #Cuming.
                call her_head("Ah!! It's so hot!","body_64")
                call her_head("And it's getting everywhere! So much of it!","body_121")
                call her_head("...[genie_name].")
                hide screen h_head2       
                g4 "Argh!!!"
                m "............"
                m "I think I am done..."
                call her_head("Ah, alright...","body_122")
                call her_head("..............","body_124")
                call her_head("You came so much this time, [genie_name]...","body_121")    
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d5
                ">Hermione releases your still pulsating cock."
                
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                show screen genie
                hide screen g_c_u
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                hide screen blkfade
                with d5
                
               
                
                
                
                
                if daytime:
                    call her_head("Well, I think I'd better go now... my Classes are about to start.","body_45")
                else:
                    call her_head("Well, I think I'd better go now...  It's getting late.","body_45")       
                m "Will you be alright in those clothes?"
                call her_head("What?","body_87")
                call her_head("Oh. Yes, I will be fine...","body_68")
                call her_head("It may soak through a little here and there, but I doubt that anyone will notice.","body_74")    
                m "Hm... You could just put it in your mouth next time, and avoid the trouble..."
                call her_head("And swallow your hot spunk like that, [genie_name]?","body_122")    
                m "Would keep your clothes clean."
                if whoring <= 15:
                    call her_head("With all due respect [genie_name]...","body_120")
                    call her_head("Not for the meagre 45 points...","body_122")
                    call her_head("Speaking of which. Can I get may payment now please?")
                else:
                    call her_head("Maybe next time...","body_122")
                    call her_head("Can I get may payment now please?","body_122")    
                

            "\"(Nah... no need).\"":
                g4 "Here! Take this, whore!"
                if whoring >= 18: # LEVEL 07
                    jump kiss_suck
                else:
                    pass
                with hpunch
                g4 "ARGH!"
                show screen blkfade
                with d3
                call her_head("WHAT?!","body_48")               
                g4 "Take this!"

                hide screen h_head2 
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+5}ARGH! YES!!!{/size}"
                
                
                
                  
                call her_head("!!!!!!!!!!!","body_48") 
                
                

                $ genie_chibi_xpos = 60 #-185 behind the desk.
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "on_shirt_cum_ani"
                hide screen hermione_walk_01 
                hide screen blkfade
                with d3
                show screen ctc
                hide screen bld1
                with d3
                pause
                show screen bld1
                with d3
                        
                $ aftersperm = True
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=300 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                call her_head(".......................","body_119")          
                m "Yes... I Feel so much better now..."
                pause
                $ g_c_u_pic = "01_hp/08_animation_02/15_cum_21.png"
                
                hide screen hermion_main
                with d3
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
                $ u_sperm = "01_hp/13_hermione_main/auto_06.png"
                $ uni_sperm = True
                
                call her_main("","body_19")
                pause
                her ".........."
                m "Well, I think that's about it..."
                show screen hermione_01 
                hide screen chair_02
                hide screen desk_02
                hide screen g_c_u
                show screen genie
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                call her_main("[genie_name]! What have you done?","body_32")
                m "What?"
                call her_main("You came all over me [genie_name]...","body_32")
                call her_main("What a mess...","body_118")
                call her_main("[genie_name], you should have warned me.","body_120")
                m "It's your fault, [hermione_name]!"
                call her_main("My fault?","body_117")
                m "Yes! You got me going too well..."
                m "I forgot about everything else..."     
                call her_main("Oh...","body_122")
                her "Well, what's done is done..."
                call her_main("I will just wipe it off and hope that nobody will notice...","body_123")
                call her_main("Can I get my payment now?","body_122")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3   
    
    label done_with_handjob:
                
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    m "Yes, [hermione_name]. [current_payout] to \"Gryffindor\"." 
    $ gryffindor +=current_payout
    
    hide screen hermione_01_f #Hermione stands still.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3   
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    call her_main("Thank you, [genie_name]...","body_13")
    
    $ request_16_points += 1
    
    if whoring <= 14:
        $ whoring +=1
    
    if whoring >= 12 and whoring <= 14:
        $ level = "05"
        $ new_request_16_01 = True #  Hearts
        $ new_request_16_heart = 1
    if whoring >= 15 and whoring <= 17:
        $ level = "06"
        $ new_request_16_02 = True #  Hearts
        $ new_request_16_heart = 2
    
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ aftersperm = False #Show cum stains on Hermione's uniform.
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    jump end_hermione_personal_request         
        
###################REQUEST_22 (Level 06) (55 pt.) (Blowjob). 
label new_request_22: #LV.6 (Whoring = 15 - 17)
    hide screen hermione_main 
    with d3
    if request_22_points == 0:
        m "{size=-4}(Should I ask her for a blowjob?){/size}"
    else:
        m "{size=-4}(Should I ask the girl to give me another blowjob?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
    if "slytherin_cheerleader" in outfit_invintory:
        m "\"(Should I ask her to dress up?)\""
        menu:
            "\"(Yes, let's do it!)\"":
                m "[hermione_name], before I request a favor, I'd like you to dress up."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "As what?"
                m "A Slytherin Cheerleader."
                if whoring >= 10:
                    $ changeHermioneMainScreen(hg_pth+"body_30.png")
                    her "A Slytherin?"
                    m "Just for a minute."
                    $ changeHermioneMainScreen(hg_pth+"body_34.png")
                    her "..."
                    $ changeHermioneMainScreen(hg_pth+"body_33.png")
                    her "Fine, let me go change."
                    show screen blkfade
                    hide screen hermione_main
                    with d3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ temp_stockings = stockings 
                    $ temp_outfit = custom_outfit
                    $ custom_outfit = 3
                    $ stockings = 4
                    hide  screen blkfade
                    show screen hermione_main
                    with d3
                    pass
                else:
                    jump too_much
            "\"(Not right now.)\"":
                pass

    if request_22_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, [genie_name]?"
        m "I plan to grant \"Gryffindor\" 55 house points today..."
        m "If you suck me off..."
        if whoring <=14: # LEVEL 05
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Oh..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Alright."
        m "Really? Just like that?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes. I know I'm supposed feel outraged..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But somehow I do not..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I suppose I am just glad that I can help out my house..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And if to do that I must put your penis in my mouth so be it..."
        m "Well, alright then."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Although, now when I say it out loud like this..."
        m "Too late! You already said \"yes\"!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I know..."
        label blowjob_jumping:
        
        # BLOWJOB
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
#        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
#        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE


        

        
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Yes..."
        m "Try to take it deeper now..."
        her "*Gulp!* *Gobble!* *Gobble!*"
        m "Yes, like that. Good."
        her "*Slurp!* *Gltch!* *Gulp!*"
        m "Yes, that's a good girl."
        menu:
            m "Hm..."
            "\"Whatever happened to your \"MRM\" thing?\"":
                her "*Slurp?*"
                
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her "Oh, well..."
                her "We are still active, but..."
                hide screen h_head2       
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gobble!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her2 "But we are not getting as popular and as much support as I thought we would..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Slurp!* *Gulp!* *Gulp!*"
                m "Oh... This is good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Hm..."
                m "So you don't mind selling me sexual favours, letting me play with your tits and such..."
                her "*Gobble!* *Gltch!* *Slurp!*"
                m "And then condemn such behavior in front of the other students."
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "You perverted, little hypocrite."
                her "*Gulp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "That's not what we stand for, [genie_name]."
                hide screen h_head2
                m "What do you mean?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_16.png" # HERMIONE
                her2 "The \"MRM\" is about gender equality."
                her2 "We are not as much against selling sexual favours to the teachers..."
                her2 "As we are against the gender inequality that the selling of sexual favour creates..."
                hide screen h_head2
                m "Hm..."
                m "This conversation is starting to bore me..."
                m "Suck on my cock some more before we continue."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Of course, [genie_name]."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Gobble!* *Slurp!* *Slurp!*"
                m "Yes, much better..."
                m "But you still disapprove of selling the favours, right?"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "Yes, it is frowned upon..."
                hide screen h_head2 
                m "And yet, you are the biggest offender by far."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her "But what choice do I have?"
                her2 "I've been put in a very difficult position..."
                hide screen h_head2
                m "The cock, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her "Right, sorry..."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                hide screen h_head2
                her "*Slurp!* *Gulp!* *Gltch!*"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "This one time we had a meeting right after I sold you another favour, [genie_name]."
                her2 "I had to give a speech with my uniform all messy and stained."
                her2 "It felt awful that I had to do that..."
                hide screen h_head2     
                m "You did enjoy it a little bit though..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE  
                her "Well..."
                hide screen h_head2        
                m "Just admit it."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "..............."
                hide screen h_head2
                m "Yes, I knew it. You took pleasure in it, you little perv."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
                her2 "I suppose it was embarrassing and exciting at the same time..."
                her2 "And it made me feel even worse about myself."
                hide screen h_head2
                m "You poor thing."
                m "Cock back in the mouth."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her "Yes, [genie_name]."
                hide screen h_head2
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                

            "\"Your parents must be proud of you...\"":
                her "*Slurp--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_75.png" # HERMIONE
                her "Yes, I believe they are..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "With me being an excellent student despite being muggle-born and all..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                her2 "Although at first they were against sending me to some \"Bogus boarding school\"."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_74.png" # HERMIONE
                her2 "Took some effort to convince them that \"Hogwarts\" is a respectable institution."
                hide screen h_head2     
                m "Yes, a respectable institution indeed."
                m "Cock back in your mouth [hermione_name]."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gulp!* *Gobble!*"
                hide screen h_head2     
                m "Yes, just keep at it for a while..."
                her "*Slurp!* *Gltch!* *Gulp!*"
                hide screen h_head2     
                m "Good, good..."
                m "So, what would your folks say if they were to see you now, [hermione_name]?"
                her "*Slurp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her "They would not understand of course..."
                her "But I do not care."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
                her2 "I am not afraid to \"get my hands dirty\" and do what needs to be done."
                hide screen h_head2     
                m "A bit rebellious, aren't you?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Hm... I suppose I am."
                hide screen h_head2     
                m "Back to sucking then. Teach your folks a lesson."
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Slurp!*"
                

            "\"Tell me about the \"Gryffindor\" house.\"":
                her "*Slurp--"
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani"
                show screen h_c_u
                hide screen g_c_u
                with d3
                $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
                $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_13.png" # HERMIONE
                her "What can I say that you don't already know, [genie_name]?"
                hide screen h_head2     
                m "Yes... Ehm... I know everything of course."
                m "But I want to see how much you know."
                m "To test your knowledge on the subject."
                show screen blktone
                with d3
                ">As soon as you mention \"test\" Hermone's eyes light up with excitement."
                hide screen blktone
                with d3
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_80.png" # HERMIONE
                her "OK. But I need a moment gather my thoughts..."
                hide screen h_head2  
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Gulp!*"
                m "Oh, yes... Take as much time as you need, [hermione_name]."
                her "*Slurp!* *Gulp!* *Slurp!*"
                her "*Gulp--"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                hide screen ctc
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
                her2 "The \"Gryffindor\" house was founded by Godric Gryffindor, thus the name."
                her2 "The heraldic animal of \"Gryffindor\" is the lion..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her "And it's colors are red and gold."
                hide screen h_head2   
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING 
                her "*Gulp!* *Slurp!* *Slurp!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "Professor Minerva McGonagall is the headmaster of our house."
                her2 "The \"Gryffindor\" house emphasizes the traits of courage..."
                her2 "As well as \"daring, nerve and chivalry\"..."
                her2 "And thus its members are generally regarded as brave but reckless..."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Slurp!* *Slurp!*"
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her2 "\"Gryffindor\" corresponds roughly to the element of fire..."
                her2 "And for that reason the colours of red and gold were chosen."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Slurp!* *Gulp!* *Slurp!*"
                m "Hm..."
                m "Well, I thought I could turn this around somehow to make fun of you..."
                hide screen h_head2     
                her "*Slurp??*"
                m "Well, with your house representing courage and righteousness and such..."
                m "And you being a nasty slut..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_86.png" # HERMIONE
                her "[genie_name]!"
                hide screen h_head2     
                hide screen h_head2     
                m "But to be honest..."
                m "\"Daring, nerve, fire, recklessness\"..."
                m "That sort of describes your personality quite well..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_45.png" # HERMIONE
                her "[genie_name]..."
                hide screen h_head2     
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                her "*Gobble!!* *Gltch!!* *Gobble!!!*"
                m "Good girl..."
        
        m "Good..."
        her "*Gobble!* *Slurp!* *Slurp!*"
        m "Good... Back and forth, back and forth... Good girl."
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" # HERMIONE
        her "[genie_name]... I am a... whore."
        hide screen h_head2  
        m "What?"
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Slurp-Slurp-Slurp!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her2 "I truly am a slut and deeply enjoy sucking your cock."
        hide screen h_head2  
        m "Oh, yes, yes... Say more things like that."
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING
        her "*Slurp!* *Gulp!* *Slurp!*"
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Please, [genie_name]. Cum for me."
        hide screen h_head2  
        with hpunch
        g4 "Argh! You little...!!!"
        g4 "{size=-4}(Here it comes. Should I give her a warning?){/size}"
        menu:
            m "..."
            "-Warn her-":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Yes, I love to suck and --"
                hide screen h_head2  
                g4 "Heads up, [hermione_name]! Here it comes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
                her "!!!"
                hide screen h_head2      
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                ">Hermione quickly puts your cock back in her mouth and continues to suck on it with great passion."
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}ARGH!{/size}"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "And some more!"
                her "*Gulp!* *Gulp!* *Gulp!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Well, I think that's it."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_126.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Are you alright there, [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes, [genie_name]..."
                her "You came so much..."
                hide screen h_head2  
                m "You managed to swallow it all though."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes... I thought I would choke..."
                her2 "But I made a promise to myself that I won't let go of your penis no matter what!"
                hide screen h_head2  
                m "Good girl."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Thank you, [genie_name]."
                her "But, still... You came so much..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "I almost feel as if I just got fed..."
                her "My stomach is so full..."
                hide screen h_head2  
                g9 "Yes, I fed you with my cum!"
                if daytime:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "I think I may skip the meal and go straight to class today."
                else:
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her2 "Yes. I think I may skip supper tonight..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "Can I get paid now?"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
            "-Don't bother-":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                her "Yes, I love to suck and --"
                hide screen h_head2  
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Whore!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                hide screen h_head2
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen ctc
                hide screen bld1
                with d3
                pause
                hide screen ctc
                show screen bld1
                with d3
                
                #Cumming.
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "[genie_name]..."
                hide screen h_head2  
                g4 "Don't you move now, [hermione_name]."
                g4 "Yes, just be still and take it."
                g4 "Argh! You little slut! You make me cum hard, [hermione_name]!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Whew..."
                $ g_c_u_pic = "cum_on_face_blink_ani"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_33.png" # HERMIONE
                her ".............."
                hide screen h_head2  
                m "Alright, I'm done..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "................."
                if daytime:
                    her "My classes are about to start..."
                else:
                    pass
                hide screen h_head2  
                m "Just wipe it off and you'll be alright."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............"
                hide screen h_head2  
                m "Unless, you don't want to."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Huh?"
                hide screen h_head2  
                m "And would rather go outside looking like this."
                m "Let everyone see what a nasty little slut you are."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                her "Of course not, [genie_name]!"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                stop music fadeout 1.0
                if daytime:
                    m "You better go before you are late for your classes..."
                else:
                    m "It's getting late..."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
                    her "Yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_44.png" # HERMIONE
                her "Can I get paid before I leave, [genie_name]?"
                hide screen h_head2
                $ aftersperm = True

        
        
    elif request_22_points == 1: #  <============================================================== EVENT 02
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "[genie_name]?"
        m "How about another blowjob?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        her "[genie_name], how dare you propose such a thing to one of your pupils!"
        m "Wha...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "This is unbecoming of a man of your standing."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "You should be ashamed of yourself [genie_name]!"
        menu:
            m "???"
            "\"Fine. No points to you then! Leave!\"":
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "[genie_name], calm down, please."
                m "You are dismissed, [hermione_name]."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "[genie_name], please, I didn't mean any of the things I said."
                m "What?"
            "\"Ehm... I am sorry?\"":
                stop music fadeout 1.0
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                her "*Giggle*"
                m "Huh?"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                         
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "I got you... [genie_name]."
                m "What?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "Well, so much has happened lately..."
        her2 "I had so many new experiences that kind of changed the way I look at things..."
        her2 "So I was just trying to imagine how the \"old me\" would've reacted to this."
        m "So..."
        g4 "You were messing with me then?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "uhm... I'm sorry [genie_name], I didn't mean to..."
        g4 "You nasty little girl! You must be punished!"
        g9 "I'll punish you with my cock!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                         
        her "..............................."

        jump blowjob_jumping
  
    elif request_22_points >= 2: # <============================================================== EVENT 03
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        m "Suck my dick, [hermione_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                         #HERMIONE                                                                                                                                                                                                                                          
        her "Of course..."
        # Sucking.
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3
        
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Yes, good girl..."
        her "*Slurp!* *Gobble!* *Slurp!*"
        
        $ renpy.play('sounds/knocking.mp3') #Sound someone knocking on the door.
        "> *Knock-knock-knock!*"
        her "{size=+7}!!!{/size}"
        m "Hm?"
        if daytime:
            m "Who could that be?"
        else:
            m "Who could that be at this hour?"
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=235 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        if not luna_known:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
            her "([genie_name], what should I do?)"
            hide screen h_head2
            m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
            sna "Albus? Are you there? I need to talk to you."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
            her "(It's professor Snape!)"
            her "([genie_name], please, send him away, I beg you!)"
            hide screen h_head2
            menu:
                m "..."
                "\"Please, come on in, Severus.\"":
                    $ mad = 30
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_76.png" # HERMIONE
                    stop music fadeout 1.0
                    her "([genie_name], no!)"
                    hide screen h_head2
                    show screen blktone
                    with d3
                    with hpunch
                    ">Hermione gives your balls a firm twist full of frustration."
                    hide screen blktone
                    with d3
                    g4 "Ouch!"
                    hide screen bld1
                    with d3
                    # SNAPE COMES IN
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ walk_xpos=610 #Animation of walking chibi. (From)
                    $ walk_xpos2=360 #Coordinates of it's movement. (To)
                    $ snapes_speed = 04.0 #The speed of moving the walking animation across the screen.
                    show screen snape_walk_01 
                    pause 4
                    show screen snape_02 #Snape stands still.
                    show screen bld1
                    with d3
                    $ s_head_xpos = 330 # x = 330,
                    $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
                    $ s_sprite = "01_hp/10_snape_main/snape_01.png"
                    show screen s_head2

                    play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
                    sna "Good, you are here."
                    hide screen s_head2
                    
                    $ g_c_u_pic = "blowjob_ani" # sucking
                    hide screen h_c_u   # SUCKING
                    show screen g_c_u # SUCKING
                    with d3                      #  SUCKING
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Listen, there is something I want to discuss..."
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Hm...?"
                    sna "Genie? Are you alright?"
                    hide screen s_head2
                    her "{size=-4}(Ginny!!? Is she here as well?!){/size}"
                    her "{size=-4}(No, please! I will die of shame!){/size}"
                    m "Yes, Severus, I am fine..."
                    her "{size=-4}(What? *Slurp...?* *Slurp...?* *Gulp...?*){/size}"
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "What are you... looking at?"
                    hide screen s_head2
                    m "Ehm... Just admiring...{w} the cupboard."
                    m "Please continue..."
                    $ s_sprite = "01_hp/10_snape_main/snape_05.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "..............."
                    hide screen s_head2
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    m "Did you want to discuss something?"
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Yes. That Hermione girl."
                    hide screen s_head2
                    her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                    m "Oh... What about her?"
                    $ s_sprite = "01_hp/10_snape_main/snape_04.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna2 "You promised that you would take care of the little witch."
                    hide screen s_head2
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    $ s_sprite = "01_hp/10_snape_main/snape_04.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "But she is still being a major pain in my arse!"
                    sna "Her tactics have changed..."
                    $ s_sprite = "01_hp/10_snape_main/snape_03.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna2 "But the amount of grief she manages to bring me is the same..."
                    hide screen s_head2
                    m "I see... ah..."
                    $ s_sprite = "01_hp/10_snape_main/snape_10.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "I swear, that girl is driving me crazy!"
                    hide screen s_head2
                    g4 "Yeah, she is driving me crazy as well... ah..."
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    $ s_sprite = "01_hp/10_snape_main/snape_04.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Will you take care of this then?"
                    hide screen s_head2
                    m "Yes. She'll get what she deserves."
                    $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                    show screen s_head2                                                          # SNAPE
                    sna "Good. That is all I wanted to hear."
                    if daytime:
                        hide screen s_head2
                        m "Well, have a good day, Severus."
                        $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                        show screen s_head2                                                          # SNAPE
                        sna "Yes, thank you."
                    else:
                        hide screen s_head2
                        m "Good night, Severus."
                        $ s_sprite = "01_hp/10_snape_main/snape_06.png" # SNAPE
                        show screen s_head2                                                          # SNAPE
                        sna "Right..."
                    # SNAPE LEAVES
                    hide screen s_head2
                    hide screen ctc
                    
                    hide screen bld1
                    with d3
                    $ walk_xpos=360 #Animation of walking chibi. (From desk)
                    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
                    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
                    show screen snape_walk_01_f 
                    pause 3
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    hide screen snape_walk_01_f 
                    with d4
                    pause.5
                    show screen ctc
                    stop music fadeout 1.0
                    pause
                    hide screen ctc
                    show screen blkfade
                    with d5
        
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."
                    ">Seeing her being so confused and vulnerable and yet continuing to perform her task diligently pushes you over the edge."
                    g4 "(Here it comes!)"
                    jump blowjob_cum_scene

                    
                "\"I am busy right now, Severus.\"":
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                    her "(Thank you, [genie_name].)"
                    hide screen h_head2                                                          
                    sna "Busy? With what?"
                    sna "All you do is sit on you arse all day."
                    sna "I really need to talk to you about something."
                    m "I said I am busy, Severus."
                    m "Understood? I am \"busy\"!"
                    sna "Oh... You mean \"Busy\" busy? Gotcha!"
                    sna "Well, I'll talk to you later then."
        else:
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
            her "([genie_name], what should I do?)"
            hide screen h_head2
            m "Just keep sucking my cock, [hermione_name]. This doesn't concern you."
            lun "[l_genie_name]? Are you there? I need to talk to you."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
            her "(It's Luna Lovegood!)"
            her "([genie_name], please, send her away, I beg you!)"
            hide screen h_head2
            menu:
                m "..."
                "\"Please, come on in, [luna_name].\"":
                    $ mad += 5
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_76.png" # HERMIONE
                    stop music fadeout 1.0
                    her "([genie_name], no!)"
                    hide screen bld1
                    hide screen h_head2
                    with d3
                    # SNAPE COMES IN
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    $ luna_chibi("stand")
                    $ changeLuna(1, 1, 4, 1)
                    show screen bld1
                    with d3
                    lun "Thank goodness you are here [l_genie_name]!"
                    
                    $ g_c_u_pic = "blowjob_ani" # sucking
                    hide screen h_c_u   # SUCKING
                    show screen g_c_u # SUCKING
                    with d3                      #  SUCKING
                    her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                    $ changeLuna(1, 1, 4, 1)                                                         # SNAPE
                    lun "I think I need some more help with these wrackspurts..."
                    $ changeLuna(1, 1, 4, 1)                                                     # SNAPE
                    lun "They're affecting me so much, Even right now all I can imagine is something inappropriate going on behind you."
                    m "Don't worry [luna_name], I'm fine..."
                    her "{size=-4}(What? *Slurp...?* *[luna_name]...?* *Gulp...?*){/size}"                                                # SNAPE
                    lun "What are you... doing?"
                    menu:
                        "-Tell the truth-":
                            m "Miss Granger is helping me relieve me of a particularly nasty wrackspurt afflication as we speak."
                            $ changeLuna(1, 1, 4, 1)
                            lun "You mean that she is behind your desk..."
                            $ changeLuna(1, 1, 4, 1)
                            lun "Releiving you as we speak."
                            ">Hermione's face goes crimson with shame but she continues her efforts."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            m "Yes, that's correct."
                            lun "Well in that case I think I best be off. It seems that you're busy tending to other students."
                            m "Thank you [luna_name]"
                            if daytime:
                                m "Well, have a good day.."
                                $ changeLuna(1, 1, 4, 1)                                                       # SNAPE
                                lun "Yes, thank you. I know that you will..."
                            else:
                                m "Good night, [luna_name]."
                                $ changeLuna(1, 1, 4, 1)                                                        # SNAPE
                                lun "Goodnight [l_genie_name].."
                                $ changeLuna(1, 1, 4, 1)   
                                lun "Goodnight hermione..."

                        "-Lie-":
                            m "Ehm... Just admiring...{w} the cupboard."
                            m "Please continue..."                                                      # SNAPE
                            lun "..............."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            m "Did you want to discuss something?"
                            $ changeLuna(1, 1, 4, 1)                                        # SNAPE
                            lun "Yes. These wrackspurts."
                            hide screen s_head2
                            her "{size=-4}(*Slurp...!* *Gobble...!* *Gulp...!*){/size}"
                            m "Oh... What about them?"
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"                            # SNAPE
                            lun "No matter what I do I can't seem to be rid of them!"
                            $ changeLuna(1, 1, 4, 1)                         # SNAPE
                            lun "They only seem to be getting worse!"
                            m "I see... ah..."
                            $ changeLuna(1, 1, 4, 1)                                                      # SNAPE
                            lun "They're driving me crazy, I won't be able to cope much longer"
                            g4 "Yeah, they're driving me crazy as well... ah..."
                            her "{size=-4}(*Slurp...* *Slurp...* *Gulp...*){/size}"
                            $ changeLuna(1, 1, 4, 1)                            # SNAPE
                            lun "Will you take care of them then?"
                            m "Yes. I'll find a way to deal with the infestation soon."
                            $ changeLuna(1, 1, 4, 1)                                                   # SNAPE
                            lun "Thank you [l_genie_name]."
                            if daytime:
                                m "Well, have a good day, [luna_name]."
                                $ changeLuna(1, 1, 4, 1)                                                       # SNAPE
                                lun "Yes, thank you."
                            else:
                                m "Good night, [luna_name]."                                                     # SNAPE
                                lun "Goodnight [l_genie_name]..."
                    # SNAPE LEAVES
                    hide screen luna
                    
                    hide screen bld1
                    with d3
                    show screen blkfade
                    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
                    hide screen luna_chibi
                    with d4
                    show screen ctc
                    stop music fadeout 1.0
                    hide screen ctc
                    hide screen blkfade
                    with d5
                
                    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                    ">Hermione doesn't say a thing. Her face is crimson due to a mix of embarrassment, guilt and excitement."

                            
                "\"I am busy right now, [luna_name].\"":
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
                    her "(Thank you, [genie_name].)"
                    hide screen h_head2                                                          
                    lun "Busy? How so?"
                    lun "Are you helping another student fight off the wrackspurts?"
                    m "Yes, that's exactly what I'm doing."
                    lun "Oh... well, I'll visit you later then."
                #">Hermione keeps sucking on your cock with a rather fierce determination."
                
            $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
            $ hermione_chibi_ypos = 10
            $ h_c_u_pic = "hand_ani" # Not sucking
            hide screen h_c_u   # SUCKING
            show screen g_c_u # SUCKING
            with d3                      #  SUCKING                
            #">Hermione is working hard to please you..."
            her "*Slurp!* *Slurp!* *Gulp!*"
            show screen blktone
            with d3
            ">Hermione keeps sucking on your cock with a rather fierce determination."
            ">Her technique is lacking but she makes up for it with the effort she puts it."
            hide screen blktone
            with d3
            m "Yes... I love your eager, little mouth girl..."
            her "*Gobble!* *Gobble!* *Gobble!*"
            $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
            $ hermione_chibi_ypos = 10
            $ h_c_u_pic = "hand_ani" # Not sucking
            show screen h_c_u   # NOT SUCKING
            hide screen g_c_u # NOT SUCKING
            with d3                      #  NOT SUCKING
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
            her "[genie_name]?"
            hide screen h_head2          
            m "Hm?"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
            her "Are you going to cum on my face today?"
            her "Or do you plan to cum in my mouth?"
            hide screen h_head2
            menu:
                "\"I Plan to splatter your face with cum!\"":
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her "I see..."
                    hide screen h_head2
                    m "Why do you ask?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                    her2 "Oh... I just read in a book that semen contains a lot of antioxidants..."
                    her "It's good for the skin..."
                    hide screen h_head2
                    m "Great. One facial coming up."
                    m "Back to work now."
                "\"I Plan to fill your mouth with cum!\"":
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                    her "I see..."
                    hide screen h_head2
                    m "Why do you ask?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her "Well, I am trying to watch my calorie-intake..."
                    her2 "I just wonder how much calories your load contains, [genie_name]."
                    her2 "Maybe I should skip my next meal..."
                    hide screen h_head2
                    m "[hermione_name]."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her "Yes?"
                    hide screen h_head2
                    m "Dick back in the mouth."
                "\"I don't plan so far ahead.\"":
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her "I see..."
                    hide screen h_head2
                    m "Don't you like surprises?"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her "Not really..."
                    her "I rather enjoy planning ahead actually..."
                    hide screen h_head2
                    m "Well some things in life are just unpredictable."
                    m "There is only one way to find out for sure."
                    
                "\"What would you like?\"":
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
                    her "If it is all the same to you, [genie_name]..."
                    if generating_points == 1:
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "I would like you to cum on my face, [genie_name]."
                        her2 "I read that it's good for the skin."
                    else:
                        show screen h_head2                                                             # HERMIONE
                        $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                        her2 "I would like you to cum in my mouth."
                        her2 "You usually cum so much so I think I will be able to just skip my next meal..."
                        her2 "And do some homework instead."
                    hide screen h_head2
                    m "Well, we'll see about that."
                    m "Back to sucking now."
                    
                    
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING   
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Hm..."
        m "You are getting better at this [hermione_name]."
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Ok, say something nasty now..."
        her "*Slurp--?"
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        show screen h_c_u   # NOT SUCKING
        hide screen g_c_u # NOT SUCKING
        with d3                      #  NOT SUCKING
        show screen h_head2                                                             # HERMIONE
        if whoring <= 20:
            $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
            her "uhm..."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
            her "I eat cockroaches?"
            hide screen h_head2
            m "What the fuck?"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
            her "T-they are pretty nasty, [genie_name]..."
            hide screen h_head2
            m "No, [hermione_name], I mean something dirty!"
            m "And don't you dare to say \"mud\"!"
            m "I mean dirty in a sexual way!"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
            her "Oh... Ehm..."
            hide screen h_head2
            m "Ah, never mind, the moment is gone..."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
            her "Ehm... I'm sorry, [genie_name]."
            hide screen h_head2
            m "Yeah, whatever. Make it up to me by sucking my cock harder."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png" # HERMIONE
            her "Of course, [genie_name]."
            hide screen h_head2
        else:
            $ h_body = "01_hp/13_hermione_main/body_129.png" # HERMIONE
            her "I'm a slut [genie_name]."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE
            her "A slut for your cum."
            hide screen h_head2
            m "That's it [hermione_name]."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_124.png" # HERMIONE
            her "It's all I can think about [genie_name]."
            her "Sucking your dirty old cock..."
            hide screen h_head2
            m "Well you better get back to it then [hermione_name]"
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
            her "Thank you [genie_name]."
            hide screen h_head2
            m "You're welcome cumslut."
            show screen h_head2                                                             # HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_78.png" # HERMIONE
            her "..."
            hide screen h_head2
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani" # Not sucking
        hide screen h_c_u   # SUCKING
        show screen g_c_u # SUCKING
        with d3                      #  SUCKING   
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Yes, like this... Good..."
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "You know what? I think we are almost there."
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Yes, definitely."
        her "*Slurp!* *Gobble!* *Gobble!*"
        m "Alright, [hermione_name], this is the final stretch."
        g4 "Show me what you've got."
        her "!!! *Gobble-goble-slurp-goble!* !!!"
        g4 "Yes, like that!"
        her "{size=+5}!!! *Gobble-gobble-slurp-gobble!* !!!{/size}"
        g4 "{size=+5}Yes! Yes! Yes! Yes!{/size}"
        g4 "Ghr!!!"
                
        menu:
            g4 "!!!"
            "-Cum in her mouth-":
                hide screen blkfade
                with d3
                g4 "Here it comes, [hermione_name]! get ready to swallow fast!"
                her "!!!"
                
                hide screen h_head2      
                show screen ctc
                pause
                show screen blkfade
                with d3
                $ g_c_u_pic = "cum_in_mouth_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}ARGH!{/size}"
                g4 "Eat my cum, slut!"
                #Cumming.
                her "*Gulp!-Gulp!-Gulp!*"
                with hpunch
                g4 "Yes! Down your fucking throat!"
                her "*Gulp-gulp-gulp-gulp-gulp!*"
                hide screen blkfade
                hide screen bld1
                with d3
                show screen ctc
                stop music fadeout 1.0
                pause
                hide screen ctc
                show screen bld1
                with d3
                m "Well, I think that's it."
                m "You can let go now..."
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_125.png" # HERMIONE
                her "..........................."
                her "................"
                her "........"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "*GULP!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_115.png" # HERMIONE
                her "Gua-ha..."
                hide screen h_head2  
                m "You alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                her "Yes, [genie_name]..."
                hide screen h_head2  
                m "Going to skip your next meal?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "I think so..."
                her "You always cum so much, [genie_name]..."
                hide screen h_head2  
                m "Heh... And who's fault is that??"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "............." #Smile.
                her "Can I get paid now?"
                if whoring >= 20:
                    hide screen h_head2  
                    if daytime:
                        m "What, even after I just gave you lunch?"
                    else:
                        m "What, even after I fed you dinner"
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_17.png" # HERMIONE
                    her "............." #Smile.
                    her "Fine, I suppose this was worth a meal"
                hide screen h_head2  
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3

                
            "-Cum on her face-":
                show screen bld1
                hide screen blkfade
                $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ hermione_chibi_ypos = 10
                $ h_c_u_pic = "hand_ani" # Not sucking
                show screen h_c_u   # NOT SUCKING
                hide screen g_c_u # NOT SUCKING
                with d3                      #  NOT SUCKING
                g4 "Ready for your facial, [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes [genie_name]!"
                hide screen h_head2      
                g4 "Here it comes then!"
                
                hide screen h_head2  
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+7}Whore!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "!!?"
                hide screen h_head2
                
                $ g_c_u_pic = "cum_on_face_ani"
                hide screen h_c_u   # SUCKING
                show screen g_c_u # SUCKING
                with d3                      #  SUCKING
                show screen ctc
                hide screen bld1
                with d3
                pause
                hide screen ctc
                show screen bld1
                with d3
                
                #Cumming.
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_48.png" # HERMIONE
                her "[genie_name]..."
                hide screen h_head2  
                g4 "All over your fucking face!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Aaah!"
                $ g_c_u_pic = "cum_on_face_blink_ani"
                hide screen h_head2  
                m "Well, I'm done."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "...................................."
                hide screen h_head2  
                m "I said it's over, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Yes, I heard you [genie_name]..."
                hide screen h_head2  
                m "So... Aren't you going to clean up?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "In a moment..."
                her2 "I'm giving my skin time to soak in the anti-oxidants..." 
                hide screen h_head2  
                m "Hm... I find this quite hot..."
                m "Take your time, [hermione_name]..."
                show screen blkfade
                with d3
                stop music fadeout 1.0 
                ">A while later."
                $ uni_sperm = False
                $ aftersperm = True
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
                her "I take it you enjoyed yourself [genie_name]?"
                hide screen h_head2  
                play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
                m "Yes I did, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_123.png" # HERMIONE
                her "Good, so Can I get paid now?"
                if whoring >= 20:
                    hide screen h_head2  
                    m "What, even after I just gave you a salon treatment?"
                    m "Women pay a lot of money for a good facial."
                    show screen h_head2                                                             # HERMIONE
                    $ h_body = "01_hp/13_hermione_main/body_17.png" # HERMIONE
                    her "............." #Smile.
                    her "Fine, but my skin better look better tomorrow."
                hide screen h_head2  
                
                    
                
            
        
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
    
    $ badges = True # Turns the badges layer of hermione_main back on.
    if whoring <= 19:
        m "Yes, [hermione_name]. 55 points to \"Gryffindor\"." 
        $ gryffindor +=55
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 17:
        $ whoring +=1


    
    
    if request_22_points == 0:
        $ new_request_22_01 = True #  HEARTS
        $ new_request_22_heart = 1
    if request_22_points == 1:
        $ new_request_22_02 = True #  HEARTS
        $ new_request_22_heart = 2
    if request_22_points >= 2:
        $ new_request_22_03 = True #  HEARTS
        $ new_request_22_heart = 3

    $ request_22_points += 1

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    $ custom_outfit = temp_outfit
    $ stockings = temp_stockings
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    
    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
        
###################REQUEST_29 (Level 07) (65 pt.) (Sex). #################################################################
label new_request_29: #LV.7 (Whoring = 18 - 20)

    hide screen hermione_main 
    with d3
    m "{size=-4}(Should I ask her to have sex with me?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
  
    if request_29_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]?"
        call her_main("[genie_name]?","body_01")
        m "The favour I will be buying from you today..."
        call her_main(".......?","body_06")
        m "How should I put this delicately...?"
        call her_main("Is it sex, [genie_name]?","body_129")
        m "Well, yes. How did you...?"
        if whoring <=17:
            jump too_much
        call her_main("Not a terribly difficult deduction all things considered...","body_128")
        m "You don't mind then?"
        call her_main("Of course, I mind, [genie_name]!","body_120")
        her "I am not a prostitute!"
        m "But you'll do it anyway??"
        call her_main("\"Gryffindor\" is falling behind again...","body_127")
        her "What choice do I have...?"
        m "Great!"
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
       
        label your_ass:
            
        show screen blkfade 
        with d7
            
        stop music fadeout 1.0
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        call her_head(".............","body_120")
        call her_head("!!!!!!!!!!!!!!!","body_119")
        m "Relax, [hermione_name]. I'm Just gonna take off your panties."
        call her_head("..............","body_49")
        m "Are you ready?"
        call her_head("No...","body_50")
        m "Good girl."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","body_130")
        

        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3    
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
            
            
            
            
        
        
        #FUCKING
        
        g4 "Your pussy... It's so tight."
        call her_head("................","body_33")
        m "You alright?"
        call her_head("A-ha... It's too big...","body_21")
        call her_head("You will rip me apart, [genie_name]!")
        m "Nonsense! My cock is of a regular size."
        m "It's not my fault that you are so tiny."
        call her_head("......................","body_33")
        hide screen ctc
        menu:
            "\"You should be ashamed of yourself!\"":
                call her_head("I am not ashamed, [genie_name]!","body_33")
                call her_head("I am doing this for the sake my house!")
                call her_head("To help my--")
                call her_head("ah-ha-a...","body_131")
                call her_head("My classmates depend on me... ah-a...")
                m "Are you sure that's the only reason?"
                call her_head("I don't know--","body_33")
                call her_head("ah-a...","body_131")
                call her_head("I don't know what you mean, [genie_name].","body_118")
                m "It seems to me that you are enjoying this a little bit too much."
                call her_head("I'm not, [genie_name]!","body_118")
                m "Really?"
                call her_head("......................","body_33")
                m "Then why is your pussy so wet?"
                call her_head("....................a-ha.{image=textheart}","body_131")
                m "Admit it, you enjoy getting fucked by your [genie_name]!"
                call her_head("I do not!","body_33")
                m "Stubborn girl..."
                call her_head("Aha...{image=textheart}","body_131") 
                "\"So... What's new in your life?\"":
                call her_head("...[genie_name]?","body_31")
                m "Just trying to have a polite conversation."
                call her_head("Ah-ah... But... ah...","body_31")
                m "Any news from your folks?"
                call her_head("My parents?","body_34")
                call her_head("[genie_name], please, I cannot talk...","body_131")
                m "Why not? Enjoying this too much?"
                call her_head("I am not... ah...{image=textheart}","body_131")
                m "I think you are."
                call her_head("I am only doing this for the points, [genie_name]...","body_131")
                m "Oh, I see..."
                m "So you are like a prostitute then."
                call her_head("What?","body_117")
                m "Well I pay you to have sex with me. How would you call that?"
                call her_head("...........","body_118")
                call her_head("I am not a prostitute...","body_131")
                call her_head("Why are you being so mean to me, [genie_name]?","body_21")
                m "I think you like it when I'm mean."
                call her_head("I do not!","body_67")
                m "Really? Then why is your pussy so wet?"
                call her_head("Not because of that!","body_118")
                m "If you say so..."
                call her_head("A-ah...{image=textheart}","body_131")
                call her_head("I am... ah...{image=textheart} not a prostitute...","body_132")            
                "\"......................................................\"":
                call her_head("A-ha... ah...","body_131")
                m "*Panting!*"
                call her_head("Ah... ha-aha...","body_131")
                m "Oh..."
                call her_head("Ah-ah...","body_131")
                m "......................"
                call her_head("Ah... ah...","body_131")
                call her_head("Ah... [genie_name]?","body_31")
                m "What is it?"
                call her_head("Ah... Do you.... like it?","body_131")
                m "Do I like drilling your super-tight pussy?"
                m "Very much so, [hermione_name]. Why?"
                call her_head(".....................","body_33")
                call her_head("Ah... You just got so quiet...","body_131")
                m "Just enjoying the moment, [hermione_name]."
                m "What about you? You alright?"
                call her_head("Ah... yes...","body_131")
                call her_head("It hurts a little though, ah...","body_31")
                call her_head("Your penis is too big... ah...","body_131")
                m "Hm..."
                m "You need me to slow down or something?"
                call her_head("No, [genie_name]... You don't have to...","body_31")
                call her_head("Please, don't mind me... Enjoy your moment.","body_33")
                call her_head("I will... ah... Get used to it eventually... ah...")
                m "As you say, [hermione_name]."
                call her_head("Ah-a...{image=textheart}","body_131")
                m "Yes, this is great!"
        call her_head("Ah-ah...{image=textheart}","body_131")
        if daytime:
            m "Going to classes after this?"
        else:
            m "Going to bed after this?"
        call her_head("Yes, ah...{image=textheart}","body_131")
        call her_head("If I'll be able to walk...")
        g4 "Ght! {image=textheart} Yes, you always say the right things, [hermione_name]!"
        call her_head("Ah...{image=textheart} ah...{image=textheart}{image=textheart}","body_132")
        with hpunch
        call her_head("{size=+7}!!!!!!!!!!!!!!!{/size}{image=textheart}{image=textheart}{image=textheart}","body_130")
        m "Huh? You alright?"
        show screen blktone8
        with d3
        ">Hermione's legs are shaking..."
        m "[hermione_name]?"
        call her_head("{image=textheart}{image=textheart}{image=textheart}I think I'm cumming, [genie_name]!{image=textheart}{image=textheart}{image=textheart}","body_130")
        g9 "Tch... You nasty slut!"
        call her_head("AAH! I can't hold it!","body_133")
        g4 "You need to be punished for being such a slut!"
        ">You tighten your grip on Hermione's buttocks and start to fuck her fiercely!"
        $ g_c_u_pic = "sex2_ani"
        with hpunch
        call her_head("NO! STOP! PLEASE!","body_130")
        g4 "Who told you you could cum, slut? This is your punishment!"
        call her_head("[genie_name], no, ah-a!{image=textheart}","body_131")
        call her_head("Ah-a...{image=textheart}I will go insane!{image=textheart}{image=textheart}{image=textheart}","body_134")
        g4 "{size=+7}Grragh!{/size}"
        hide screen blktone8
        with d3
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        show screen bld1
        with d3
        call her_head("No...{image=textheart} ah...{image=textheart}","body_134")
        call her_head("I think I will...{image=textheart} pass out...{image=textheart}")
        g4 "ARGH! YOU WHORE!"
        menu:
            "-Cum all over Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","body_133")
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"

                m "Well, that was rather intense..."
                call her_head("*heavy panting*","body_135")
                m "You alright?"
                call her_head("Ah... yes...","body_133")
                call her_head("My legs are still shaking...")
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                if daytime:
                    call her_head("But I think I will be able to make it to my classes...","body_133")
                else:
                    call her_head("But I think I will be able to make it to the common room...","body_133")
                m "Good."
                m "Did you enjoy getting fucked by your [genie_name]?"
                call her_head("[genie_name], I am only doing this for my house.","body_136")
                m "Seriously? Still?"
                call her_head("Could I just get paid now... please?","body_131")
                "-Cum inside Hermione-":
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                
                
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","body_133")
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"
                call her_head("You came inside of me...","body_133")
                g9 "I sure did."
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                call her_head("But...","body_133")
                m "What?"
                call her_head("What if I get pregnant?","body_132")
                m "Nah, you will be alright..."
                call her_head("How do you know, [genie_name]?","body_132")
                m "We witchers are infertile."
                call her_head("Witchers?","body_131")
                m "Sure... You are a witch, that make me a witcher, right?"
                m "And everyone knows that witchers are infertile..."
                call her_head("[genie_name], you make no sense...","body_117")
                call her_head("Can I please just get paid now...?")
                elif request_29_points == 1: # SECOND EVENT <============================================================== EVENT 02
        m "[hermione_name], are you keeping your pussy wet and ready for me?"
        call her_main("[genie_name]!","body_30")
        m "Just say \"I do\" and come over here, [hermione_name]."
        call her_main("...........","body_31")
        call her_main("I do....","body_118")
        hide screen hermione_main    
        jump your_ass

    elif request_29_points >= 2: # THIRD EVENT <============================================================== EVENT 03
        m "[hermione_name]..."
        m "Last night I had a dream..."
        g9 "You were lying on my desk and I was fucking your tight pussy like a madman..."
        hide screen hermione_main
        with d3
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        if whoring >= 24:
            call her_main("In that dream, [genie_name]...","body_121")
        else:
            call her_main("In that dream, [genie_name]...","body_120")
        if whoring <= 23:
            call her_main("Did I happen to receive 65 house points afterwards?","body_47")
            g9 "Why yes, you did, [hermione_name]."
        else:
            call her_main("Did you cum inside me or not?","body_46")
            g9 "I'm not sure [hermione_name], care to find out?"
        call her_main("...............................","body_66")
        her "Let me just take my panties off..."
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        show screen blkfade
        with d3
        # SEX
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        call her_head("Ooooohhhhhhhhhhhh....{image=textheart}","body_130")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        show screen bld1
        with d3    


        call her_head("Ah...{image=textheart}","body_131")
        m "Your pussy feels a bit looser today..."
        call her_head("Does it...{image=textheart} ah...?{image=textheart}","body_131")
        call her_head("That's all because of you [genie_name]...{image=textheart}","body_132")
        call her_head("You are ruining my little pussy with your monstrous penis...{image=textheart}","body_134")
        g4 "Agh, you whore!"
        call her_head("Ah...{image=textheart}{image=textheart}","body_134")
        #        if not ask_me_once: #Turns true after Hermione asks you about your true identity, during sex.
#            $ ask_me_once = True #Turns true after Hermione asks you about your true identity, during sex.
#            her "[genie_name], can I ask you something?"
#            m "What is it, [hermione_name]?"
#            her "Ah... Oh, not so deep please..."
#            her "Ah... I... Ah..."
#            her "?!!"
#            her "[genie_name]? Why did you stop?"
#            m "What did you want to ask me, [hermione_name]?"
#            her "But I think I was about to cum..."
#            m "So soon? Good think I did stop then."
#            her "[genie_name], please..."
#            her "I want to ask you this question while..."
#            her "While you are fucking me..."
#            her "Ah..."
#            her "[genie_name], I just want to know..."
#            her "Are you really [genie_name]?"
#            g4 "WHAT!?"
#            menu:
#                m "!!!"
#                "\"Yes! Albus Dumbledore! That's me!\"":
#                    her "Oh..."
#                    her "You just been acting so unlike yourself lately..."
#                    g4 "You whore! Your little pussy is the best!"
#                    her "I suppose that was just my imagination then..."
#                    her "Ah-ah-a..."
#                "\"You got me... The truth is...\"":
        m "Yes! Do you like it when I fuck you like this?"
        call her_head("Yes, [genie_name]...","body_128")
        menu:
            g4 "..."
            "\"Be sweet but passionate.\"":
                m "Yes, you're liking this?"
                call her_head("I do, [genie_name]... ah...{image=textheart}","body_127")
                m "Good girl!"
                m "Just relax and take my cock!"
                call her_head("Yes... ah...{image=textheart}","body_127")
                m "All the way in... all the way..."
                call her_head("Ah...{image=textheart}{image=textheart}","body_131")
                m "Yes, my little princess..."
                call her_head("What?","body_119")
                call her_head("No, please don't call me that... ah...{image=textheart}","body_118")
                call her_head("My daddy used to call me his little princess when I was little...")
                m "Well, right now I am your daddy!"
                call her_head("Ah...{image=textheart} ah-ah...{image=textheart}{image=textheart}","body_121")
                m "And you are my little princess-slut!"
                call her_head("Ah...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","body_123")
            "\"Be mean to her!\"":
                m "Yes, you slut!"
                m "I bet you love every second of this!"
                show screen blktone
                hide screen ctc
                with d3
                ">You pick up the pace."
                hide screen blktone
                with d3
                call her_head("Ah...{image=textheart} [genie_name]...","body_131")
                m "You nasty slut!"
                call her_head("Ah...{image=textheart} ah-a...{image=textheart}","body_132")
                m "You are a disgrace, [hermione_name]!"
                call her_head("Ah-ah...{image=textheart}{image=textheart}{image=textheart}","body_132")
                m "Your parents sent you here to study, not to screw your teachers, you disgusting cunt!"
                call her_head("Ah-a...{image=textheart} But I am only doing this--","body_132")
                m "Nobody cares why you are doing this, cocksucker!"
                m "Look at what you've become!"
                m "Butt-naked, on your professor's old cock, like a cheap whore!"
                call her_head("Ah...{image=textheart} No...{image=textheart} stop saying...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","body_134")
                show screen blktone
                with d3
                ">You pick up the pace some more."
                $ g_c_u_pic = "sex2_ani"
                ">The room fills up with rhythmical sound of a flesh hitting flesh..."
                hide screen blktone
                with d3
                m "You let me molest you... You suck my cock..."
                m "What are you after that I ask you!?"
                call her_head("................","body_123")
                call her_head("Ah...{image=textheart} ah....{image=textheart}{image=textheart}{image=textheart}","body_132")
                call her_head(".......................","body_118")
                call her_head("{size=-5}I am a whore...{/size}")
                #her "{size=-5}I am a whore... ah...{\size}"
                m "Yes! That's exactly what you are!"
        call her_head("Ah... ah... ah...","body_118")
        call her_head("[genie_name], you think you could... ah...")
        m "What?"
        call her_head("Could you spank me a little... ah...?","body_138")
        g4 "Gladly!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        call her_head("Aa-a-ah!{image=textheart}{image=textheart}{image=textheart}","body_139")
        m "You liked that one, huh?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        call her_head("Ah..!{image=textheart} Yes!{image=textheart}{image=textheart}{image=textheart}","body_138")
        m "And some more!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        call her_head("Ahh! Yes!","body_138")
        show screen blktone
        with d3
        ">You notice that every time you slap the girl's butt, her pussy clutches your cock tightly for a second..."
        ">You love the sensation..."
        ">You unleash another series of slaps on Hermione's ass-cheeks."
        ">Every single one met with a gasp of excitement from the girl."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        call her_head("Aah!!!{image=textheart}{image=textheart}{image=textheart} IT HURTS!{image=textheart}{image=textheart}{image=textheart}","body_138")
        call her_head("It hurts...{image=textheart}{image=textheart}{image=textheart} It hurts...{image=textheart}{image=textheart}{image=textheart}","body_134")
        m "Hm?"
        m "Why your legs are shaking, [hermione_name]?"
        m "Are you cumming?"
        call her_head("Yes...{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}{image=textheart}","body_133")
        m "Well, I think I will follow your example then."
        call her_head("..............","body_133")
        show screen blktone 
        with d3
        ">You start fucking Hermione with renewed determination!"
        hide screen blktone 
        with d3
        call her_head("Ah! No! I can't...{image=textheart} I...{image=textheart} ah...{image=textheart}{image=textheart}{image=textheart}","body_139")
        m "Shut it whore!"
        g4 "Argh!"
        menu:
            "-Cum inside of Hermione-":
                with hpunch
                g4 "{size=+7}Argh, TAKE THIS!!!{/size}"
                
                
                
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                call her_head("!!!","body_133")
                call her_head("AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}")
                g4 "I'm Not done yet, bitch!"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                call her_head("AH! MY BELLY!","body_139")
                g4 "{size=+5}SLUT!{/size}"






                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"

                show screen blktone
                with d7
               

                
                
                
                
    
 
                
                m "Well, this was pretty great..."
                call her_head("Ah...{image=textheart}","body_133")
                m "You alright there, slut? Ehm, I mean, [hermione_name]."
                call her_head("Yes... I...","body_133")
                call her_head("I feel so full...","body_135")
                call her_head("!!!","body_130")
                call her_head("You came inside of me, [genie_name]!")
                m "I sure did."
                call her_head("You shouldn't have...","body_131")
                m "Didn't you enjoy it?"
                call her_head("....maybe.","body_123")
                call her_head("I think I came several times...","body_121")
                show screen blkfade
                with d3
                call her_head("Maybe you are right, [genie_name], and I shouldn't worry so much.","body_122")
                if whoring <= 23:
                    her "Can I get my payment now?"
                "-Cum all over Hermione-":
                
                with hpunch
                g4 "{size=+7}Argh!!!{/size}"
                

                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                call her_head("Ah...{image=textheart}{image=textheart}{image=textheart}","body_133")
                g4 "{size=+5}You whore! Take this!{/size}"
                call her_head("{size=+5}!!!{/size}","body_138")
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "sex_cum_out_blink_ani"
                
                


                
                m "Well, that was pretty great..."
                call her_head("Ah...{image=textheart}","body_138")
                m "You alright there, slut?"
                call her_head("Yes... I...","body_133")
                m "Didn't you enjoy this?"
                call her_head("....I think so...","body_123")
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d3
                call her_head("I think I came several times, [genie_name]...","body_121")
                if whoring <= 23:
                    call her_head("Can I get my payment now?","body_122")
                $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    hide screen blktone
    with d3
    
    stop music fadeout 4.0
    if whoring <= 23:
        m "Yes, [hermione_name]. 65 points to the \"Gryffindor\" house." 
        $ gryffindor +=65
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_13.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 20: # Level 07 <
        $ whoring +=1




    if request_29_points == 0:
        $ new_request_29_01 = True # HEARTS
        $ new_request_29_heart = 1
    if request_29_points == 1:
        $ new_request_29_02 = True # HEARTS
        $ new_request_29_heart = 2
    if request_29_points >= 2:
        $ new_request_29_03 = True # HEARTS
        $ new_request_29_heart = 3



    $ request_29_points += 1

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    #call music_block 
    
    if daytime:
        jump night_start
    else:
        jump day_start
        
###################REQUEST_31 (Level 08) (75 pt.) (Anal sex).  #####################################################
label new_request_31: #LV.8 (Whoring = 21 - 23)
    hide screen hermione_main 
    with d3
    m "{size=-4}(Should I ask her to have anal sex with me?){/size}"
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        "\"(Yes, let's do it!)\"":
            show screen blktone
            with d3
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
            
 
    if request_31_points == 0: # FIRST EVENT <============================================================== EVENT 01
        m "[hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "[genie_name]..?"
        m "How familiar you are with the term \"Anal Sex\"?"
        if whoring <=20:
            jump too_much
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                         
        her "90 house points..."
        m "What?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE          
        her "............................."
        m "Well alright then. 90 house points it is."
        hide screen hermione_main   
        
        
        label lucky_guess:
            
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
        her "..........."
        hide screen h_head2      
        m "Let's see..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
        her "................."
        hide screen h_head2      
        m "Hm..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
        her "!!!"
        hide screen h_head2      
        g4 "Oh, come on!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
        her "Ouch!"
        hide screen h_head2      
        m "Just try to loosen up a little, would you?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_21.png" # HERMIONE
        her "I'm trying!"
        hide screen h_head2      
        m "Ok, what if I do this..?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
        her "Ouch! What are you doing, [genie_name]?"
        hide screen h_head2      
        m "Yeah, this won't work either..."
        m "Hm..."
        m "Alright, I think I know what we should do."
        menu:
            m "..."
            "\"I think I'll spit on it and just force it in!\"":
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_18.png" # HERMIONE
                her "Force it in, [genie_name]?!"
                hide screen h_head2      
                $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
                g3 "*SPIT!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Eeeeeew!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "No, [genie_name], wait! Maybe if I just relax--"
                hide screen h_head2      
                m "No need, here I come!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_22.png" # HERMIONE
                her "ARGH!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Ouch! Ouch! Ouch!"
                hide screen h_head2      
                g4 "Almost in!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "No, you're hurting me! You are hurting me!"
                hide screen h_head2      
                g4 "Almost! Almost!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ah! It hurts!"
                hide screen h_head2      
                g4 "Shut it, [hermione_name]! I'm doing you a favour!"
                g4 "Your anus is so tight it's completely un-fuckable!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
                her "Then stop, please!"
                hide screen h_head2      
                m "No! We need to loosen up your asshole a little!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_20.png" # HERMIONE
                her "But I don't want you to!"
                hide screen h_head2      
                m "Really? How do you expect people to fuck you up your ass then?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "What people?"
                hide screen h_head2      
                g4 "You know... people."
                g4 "Argh, dammit... My dick is hurting too now."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "Stop then! Stop, [genie_name]!"
                her "I've changed my mind! I don't need 90 points!"
                hide screen h_head2      
                g4 "I think I'm almost..."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}AAAAAAAAhhhhh!!!{/size}"
                hide screen h_head2
                g4 "YES!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARGH!"
                hide screen h_head2
                g4 "Let us pump this little asshole full of semen then, shall we?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_137.png" # HERMIONE
                her "Yes... Please, I just want this to end..."
                hide screen h_head2




                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3    
                        
                        
                        
                
                
                
                
                #SCHUSH!
                
               
                g4 "Agh... You want this to end sooner?"
                g4 "Help me out then!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*sob!* How?"
                hide screen h_head2       
                g4 "You know..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Oh..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "I am a whore??"
                hide screen h_head2    
                g9 "Yes you are!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "*Sob!* I am a whore..."
                her "I love to suck cock..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her2 "And now my tiny asshole is getting ripped to pieces... *Sob!*"
                hide screen h_head2    
                g4 "Yes! Yes!"
                g4 "Agrh! Yes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "No! Is it getting bigger?! I'm scared!"
                hide screen h_head2    
                g4 "ARGH!"

                
            "\"Suck me off first. Lubricate my cock!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "Oh... Alright..."
                hide screen h_head2    
                play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
                #SUCKING
                
                hide screen blkfade
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3
                        
                
                
                
                
                
                
                
                her "*Slurp!* *Slurp!* *Slurp!*"
                hide screen h_head2    
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                hide screen h_head2    
                m "Alright, I think that's enough. Back on the desk now."
                show screen blkfade
                with d3

                
                #ON THE DESK
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "............."
                hide screen h_head2    
                g4 "Yes! Almost!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_32.png" # HERMIONE
                her "Ouch!"
                hide screen h_head2    
                m "Relax. Almost in."
                
                $ renpy.play('sounds/gltch.mp3')
                with hpunch
                with kissiris
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her2 "{size=+5}AAAAAAAAhhhhh!!!{/size}"
                hide screen h_head2
                g4 "YES!!!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "My... my..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_132.png" # HERMIONE
                her "It hurts!"
                hide screen h_head2
                g4 "Let's pump this little asshole full of semen then, shall we?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "....................."
                hide screen h_head2               
                
                # SEX
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_slow_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3    


                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "....................."
                hide screen h_head2    
                m "You alright there, slut?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her2 "Ah... You are... stretching me out from the inside... [genie_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "And it still hurts..."
                hide screen h_head2    
                m "Hm..."
                m "Maybe not enough lubrication...?"
                m "Come on down, [hermione_name]. Suck my dick some more."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "What? But..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "But it's dirty... It's been inside already."
                hide screen h_head2    
                m "Yes, it's been inside, but that doesn't mean it's dirty now."
                m "Come one, [hermione_name]. Suck my cock some more."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                hide screen h_head2   
                show screen blkfade
                with d3
                
                
                #SUCKING
                
                hide screen blkfade
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "blowjob_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3
                
                
                
                
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Yes... good..."
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Can you taste your ass on my dick?"
                her "*Slurp!* *Slurp!* *Slurp!*"
                m "Alright, Maybe that's enough."
                show screen blkfade
                with d3
               

                
                #ON DESK AGAIN.
                
                
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                hide screen genie
                $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
                $ genie_chibi_ypos = 10
                $ g_c_u_pic = "sex_ani"
                show screen chair_02
                show screen g_c_u
                
                hide screen hermione_02 #Hermione stands still.
                hide screen blkfade
                hide screen blktone
                hide screen bld1
                show screen ctc
                with fade
                pause
                show screen bld1
                with d3    
                
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Ah..."
                hide screen h_head2     
                m "Better now?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "It still hurts..."
                her "But I think I will be fine..."
                hide screen h_head2     
                m "I'll take it slow for now..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_141.png" # HERMIONE
                her "Ah... thank you, [genie_name]."
                hide screen h_head2     
                m "Oh... yes... this feels great..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "..........."
                hide screen h_head2     
                m "Oh... So tight..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_143.png" # HERMIONE
                her "................"
                hide screen h_head2     
                m "Why are you being so quiet [hermione_name]?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "Because this is painful..."
                her "And I just want you to cum sooner, [genie_name]..."
                hide screen h_head2     
                m "So you stifle your cries of pain?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "yes [genie_name]. *Sob!*"
                hide screen h_head2     
                m "Don't do that."
                m "Sob, scream and cry as much as you wish!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_140.png" # HERMIONE
                her "B-but--"
                hide screen h_head2     
                m "That will make me cum sooner."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Really? *Sob!*"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "*Sob!* It hurts! *Sob!* It hurts so much! *Sob!*"
                hide screen h_head2     
                m "Yes, yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*SOB!*"
                hide screen h_head2     
                m "You poor little kid..."
                m "A Big, evil man is raping your asshole!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_146.png" # HERMIONE
                her "*SOB!* Yeees! *SOB!*"
                hide screen h_head2     
                g4 "Argh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_147.png" # HERMIONE
                her "No, I'm scared! *SOB!*"
                hide screen h_head2   
        
        menu:
            "-Fill Hermione up with cum-":
                g4 "Argh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE  
                her "No! AH!"
                hide screen h_head2    
                
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                $ g_c_u_pic = "sex_cum_in_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "AH! IT'S FILLING ME UP!{image=textheart}{image=textheart}{image=textheart}"
                hide screen h_head2  
                
                
                g4 "Yes, you whore! Yes!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "It hurts, it hurts!"
                hide screen h_head2         
                g4 "Shut up!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_149.png" # HERMIONE
                her "No, I am already full! Stop cumming, you bastard!"
                hide screen h_head2      
                g4 "Shut the fuck up, slut! I am not done yet!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_146.png" # HERMIONE
                her "No! Please! My stomach! I will explode!"
                hide screen h_head2   
                g4 "ARGH!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "No, I think I will throw up..."
                hide screen h_head2    
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_150.png" # HERMIONE
                play sound "sounds/burp.mp3"
                her "{size=+7}*BURP!*!!!!!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_151.png" # HERMIONE
                her "......................."
                her "............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_126.png" # HERMIONE
                $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liquid.
                her "{size=+7}*GULP!*{/size}"  
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*SOB!* I HATE YOU..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_148.png" # HERMIONE
                her "{size=+5}I HATE YOU AND YOUR NASTY OLD COCK?{/size}"
                her "{size=+5}I HATE YOU! YOU HEAR ME?!{/size}"
                hide screen h_head2   
                g4 "Agh...Shut it, whore!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "*sob!* *Sob!*..."
                hide screen h_head2
                
                
                
                
                
                
                
                # AFTER CUM INSIDE
                
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3
                $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "*Sob!*..."
                hide screen h_head2
                m "Whew!... I think that was the last of it."
                m "You alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Yes... *Sob!*"
                hide screen h_head2 
                m "Are You crying?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "My butt hurts, but I am alright, [genie_name]..."
                hide screen h_head2 
                m "Well, you took my dick stoically, I must say..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Thank you [genie_name]..."
                hide screen h_head2 

                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen blkfade
                with d7
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_152.png" # HERMIONE
                her "I apologize for saying that I hate you, [genie_name]..."
                her "And your cock is not nasty..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_153.png" # HERMIONE
                her "I don't know what's gotten into me..."
                hide screen h_head2
                g9 "My dick!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_153.png" # HERMIONE
                her2 "I suppose it's as when you call me a \"whore\". I know you actually don't mean it..."
                hide screen h_head2    
                m "Yeah, sure..."
                m "Does it still hurt?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_154.png" # HERMIONE  
                her "A little..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_155.png" # HERMIONE
                her "I also feel full and warm inside..."
                hide screen h_head2      
                m "You plan to keep it in? My cum I mean."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_156.png" # HERMIONE     
                her "Yes..."
                if daytime:
                    her2 "I hope it won't start leaking during my classes..."
                else:
                    her2 "I hope it won't start leaking before I get to my room..."
                hide screen h_head2 
                m "Well, good luck on your journey."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_155.png" # HERMIONE  
                her "Can I get paid now please?"
                hide screen h_head2 
                
                    
                
                
                
                
            "-Pull out and cum on Hermione-":
                
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her2 "Ah...{image=textheart}{image=textheart}{image=textheart}"

                hide screen h_head2     
                g4 "Yes!!! Allover your ass!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ah... It's so hot!"
                hide screen h_head2          

                
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
                
                m "Well, I'm done... You can get off my desk now."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Yes, [genie_name]..."
                hide screen h_head2     
                m "You feeling alright?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_139.png" # HERMIONE
                her "Yes, [genie_name]. It still hurts a little, but..."
                hide screen h_head2     
                m "But what?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "But in a good way... [genie_name]."
                hide screen h_head2     
                m "In a good way, huh?"
                g9 "Heh... You cute, little mynx."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Can I get paid now, [genie_name]?"
                hide screen h_head2 

        
    elif request_31_points == 1: # FIRST EVENT <============================================================== EVENT 02
        m "[hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE                     
        her "[genie_name]?"
        m "I will be buying another favour from you today..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "............."
        m "Care to guess what the favour will be?"
        m "You have three attempts to find out."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "..........."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "Anal sex?"
        g4 "Wha..........?!"
        g4 "How did you...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE    
        her "Just a lucky guess, [genie_name]..."
        m "Sometimes you scare me, [hermione_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3 
        jump lucky_guess
        
        
        
        
        
    elif request_31_points >= 2: # FIRST EVENT <============================================================== EVENT 03
        m "How about another assfuck, [hermione_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE     
        her "Of course, [genie_name]."
        g9 "Come here, you little mynx!"
        hide screen hermione_main     
        with d3
        # SEX
        show screen blkfade
        with d3
        
        stop music fadeout 1.0
        
        $ her_head_xpos=390 #Defines position of the Hermione's full length sprite. (Default 370). 140 - center. Bottom right: 390
        $ her_head_ypos=340 #Defines position of the Hermione's full length sprite. (Default 0). Right bottom corner: 340 - head only. 235 - tits.
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" # HERMIONE
        her "........"
        hide screen h_head2               
        m "Hm..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
        her "..........."
        hide screen h_head2
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
        her2 "Ooooohhhhhhhhhhhh....{image=textheart}"
        hide screen h_head2
        g4 "Oh, ye-es!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_121.png" # HERMIONE
        her "Ah..."
        hide screen h_head2
        m "It seems like your butthole became a bit more welcoming, [hermione_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE
        her "Ah... It still hurts a little."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_129.png" # HERMIONE
        her "And please, just call me \"whore\", [genie_name]."
        hide screen h_head2
        g4 "Agh! You slut! You always get me with your words!"



        
        
        
        
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        hide screen genie
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        pause
        show screen bld1
        with d3    
        
        
        
        
        
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        # INSERTION
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ah... Ah..."
        her "Ah..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" # HERMIONE
        her "[genie_name]?"
        hide screen h_head2
        m "Yes, whore?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Em..."
        hide screen h_head2
        hide screen ctc
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her "Would you marry me, [genie_name]?"
        hide screen h_head2
        with hpunch
        g4 "{size=+9} WHAT?!{/size}"
        g4 "Don't tell me you're pregnant, [hermione_name]!"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" # HERMIONE
        her "I Couldn't get pregnant the way we are doing it, [genie_name]..."
        hide screen h_head2
        m "What is this talk of marriage then?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "You misunderstood me [genie_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her "I meant to say, would you marry a girl {size=+5}like{/size} me?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" # HERMIONE
        her2 "I would never propose to a man with his cock in my ass, [genie_name]..."
        hide screen h_head2
        m "Good. Because I don't think any man would be able to say \"no\" to then."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
        her "Ah{image=textheart}..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her2 "What I meant... ah{image=textheart} {w} ...to say was ah{image=textheart}... {w}...do you think someone would ever ah{image=textheart}... {w} ...want to marry a girl like me?"
        hide screen h_head2
        m "Huh?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" # HERMIONE
        her "I mean, with all that was happening lately... ah{image=textheart}..."
        her "I can't help but feel unclean... damaged even."
        her "And in a no way innocent..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" # HERMIONE
        her "Who would want a wife like that?"
        hide screen h_head2  
        menu:
            m "..."
            "\"I would marry you in a heartbeat!\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_31.png" # HERMIONE
                her "What?"
                hide screen h_head2  
                m "Well, hypothetically speaking of course..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_54.png" # HERMIONE
                her "...of course...{image=textheart}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_53.png" # HERMIONE
                her ".............."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_55.png" # HERMIONE
                her "But why do you say that, [genie_name]?"
                hide screen h_head2  
                m "Huh?"
                m "What do you mean \"why\", whore?"
                m "You are young and attractive..."
                m "Tight asshole, full tits and wet little pussy..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_127.png" # HERMIONE
                her "Ah...{image=textheart}"
                hide screen h_head2  
                m "You will make some lucky guy a very happy man one day, whore."
                m "Ehm, I mean, [hermione_name]."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "No, \"whore\" is good. Call me that, [genie_name]."
                hide screen h_head2  
                m "There, you see? You are a great catch, I'm telling you, whore."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Ah...{image=textheart} Thank you, [genie_name]."
                hide screen h_head2  
                m "Huh?"
                m "Are you crying?"
                label among_other_things:
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Among other things, [genie_name]...{image=textheart}{image=textheart}{image=textheart}"
                hide screen h_head2  
                m "Among other things?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_135.png" # HERMIONE
                her "I'm cumming [genie_name]...{image=textheart}{image=textheart}{image=textheart}"
                hide screen h_head2  
                g4 "Agh! My cock!" 
                g4 "Relax your muscles a little, would you?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_131.png" # HERMIONE
                her "BUT I'M CUMMING!{image=textheart}{image=textheart}{image=textheart}"
                hide screen h_head2  
                g4 "Fine! Have it your way whore!"
                with hpunch
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "{size=+7}Ah-ah-aha!!! I'm cumming!!!{/size}"
                hide screen h_head2  
                g4 "{size=+7}Argh!{/size}"
                
            "\"Marriage is out of the picture for you.\"":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_143.png" # HERMIONE
                her "That's what I thought..."
                hide screen h_head2  
                m "Oh... I just love that little asshole of yours!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "....................."
                her2 "Yes... After all the things I had to do for my house..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "...no one will ever want me..."
                hide screen h_head2  
                m "Oh, they will want you alright!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "What? But you said..."
                hide screen h_head2  
                m "Marriage, [hermione_name]. Marriage is impossible for you."
                m "But as a man-pleaser you are a great catch!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Really?"
                hide screen h_head2  
                m "Are you kidding me?!"
                m "Young, hot and slutty. You could have any man you want!"
                m "Or a wizard or whatever you are into..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_157.png" # HERMIONE
                her "I think you may be right, [genie_name]."
                hide screen h_head2  
                m "I know I am right, whore."
                m "Now wiggle that little ass of yours a little."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Like this?"
                hide screen h_head2  
                m  "Yes, that's a good whore."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "I am a whore, aren't I?"
                hide screen h_head2  
                m "You just sold me your asshole for 90 house points. How would you call that?"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_138.png" # HERMIONE
                her "Yes, yes...{image=textheart} I am a whore...{image=textheart}"
                hide screen h_head2  
                m "Are you crying?"
                jump among_other_things
                
        menu:
            g4 "!!!"
            "-Fill Hermione up with cum-":
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_130.png" # HERMIONE
                her "!!!"
                hide screen h_head2 
                m "Yes! Argh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ah!{image=textheart} It's filling me up!{image=textheart} I can feel it!{image=textheart}"
                hide screen h_head2 
                m "Shut up, whore!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_137.png" # HERMIONE
                her "Ah! I AM A WHORE!!!!{image=textheart}{image=textheart}{image=textheart}"
                hide screen h_head2 
                m "Agh!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_144.png" # HERMIONE
                her "Ah...{image=textheart} your cum, [genie_name]...{image=textheart}"
                hide screen h_head2 
                m "Yes, yes..."
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_145.png" # HERMIONE
                her "Ah...{image=textheart}"
                hide screen h_head2          
                m "......"
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7
            "-Cum allover Hermione-":
                
                $ g_c_u_pic = "sex_cum_out_ani"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                show screen ctc
                pause
                hide screen ctc
                $ uni_sperm = True
                $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_133.png" # HERMIONE
                her "Ah-aha! You're cumming! {image=textheart}{image=textheart}{image=textheart}"
                hide screen h_head2    
                g4 "{size=+7}Yes I do, whore!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_147.png" # HERMIONE
                her "Ah, me too! Me too!"
                hide screen h_head2    
                g4 "{size=+7}FUCKING SLUT!{/size}"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_142.png" # HERMIONE
                her "Ah...{image=textheart} your cum...{image=textheart}"
                her "I'm so full...{image=textheart}{image=textheart}{image=textheart}"


                hide screen h_head2     
                g4 "Yes!!! All over your ass!"
                show screen h_head2                                                             # HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_134.png" # HERMIONE
                her "Ah... It's so hot!"
                hide screen h_head2          

                
                hide screen h_head2     
                hide screen bld1
                with d3
                show screen ctc
                pause
                hide screen ctc
                show screen bld1
                with d3


                
                
                show screen blkfade
                with d7

                
                
                
                
                
                
                
                
                
                
                
               
              
        #Ending
        m "Well, this was intense..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Ah-ha...{image=textheart} ah...{image=textheart}"
        hide screen h_head2   
        m "Are You alright, [hermione_name]?"
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "I think so... I'm not sure..."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "I think I may still be cumming, [genie_name]."
        show screen h_head2                                                             # HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_158.png" # HERMIONE
        her "Or maybe not..."
        her "Everything is in a daze... and my legs feel so weak..."
        if whoring <= 23:
            her "Can I just get paid now, [genie_name]?"
        hide screen h_head2                                                             # HERMIONE

        
    
    stop music fadeout 1.0
    
    $ uni_sperm = False #Sperm layer is not displayed in hermione screen.
    $ gryffindor += current_payout #35
    hide screen h_c_u
    hide screen g_c_u
    hide screen g_c_c_u # Genie's sperm. Universal.
    hide screen ctc
    hide screen chair_02
    hide screen desk_02
    show screen genie
    show screen bld1
    $ hermione_chibi_xpos = 400 #Near the desk.
    $ hermione_chibi_ypos = 250 #Default: 250
    show screen hermione_02 #Hermione stands still.
    pause.1
    hide screen blkfade
    with d3
 
 
    if whoring <= 23:
        m "Yes, [hermione_name]. 90 points to \"Gryffindor\"." 
        $ gryffindor +=90
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    $ h_body = "01_hp/13_hermione_main/body_141.png" #Flashing panties
    show screen hermione_main
    hide screen hermione_01_f #Hermione stands still.
    with d3
    her "Thank you, [genie_name]..."

    if whoring <= 23: # Level 08 <
        $ whoring +=1

    if request_31_points == 0:
        $ new_request_31_01 = True # HEARTS.
        $ new_request_31_heart = 1
    if request_31_points == 1:
        $ new_request_31_02 = True # HEARTS.
        $ new_request_31_heart = 2
    if request_31_points >= 2:
        $ new_request_31_03 = True # HEARTS.
        $ new_request_31_heart = 3


    $ request_31_points += 1

    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen ctc
    with Dissolve(.3)
    
    # $ walk_xpos=400 #Animation of walking chibi. (From)
    # $ walk_xpos2=610 #Coordinates of it's movement. (To)
    # $ hermione_speed = 02.0 #The speed of moving the walking animation across the screen.
    # show screen hermione_walk_01_f 
    # pause 2
    # hide screen hermione_walk_01_f 
    
    call her_walk(400,610,2)
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    with Dissolve(.3)

    $ aftersperm = False #Show cum stains on Hermione's uniform.

    call music_block
    
    if daytime:
        $ hermione_takes_classes = True
        jump night_main_menu
    else:
        $ hermione_sleeping = True
        jump day_main_menu            
        
label per_quest_the_gamble:
    hide screen hermione_main
    with d3
    call display_order_hide
    m "{size=-4}(I'm bored...){/size}"
    g9 "{size=-4}(Should I try something completely different?){/size}"
    
    $ menu_x = 0.5 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
    menu:
        ">This may be {i}{size=+7}the end{/size}{/i} of her..."
        "\"(Yes, let's do it!)\"":
            pass
        "\"(Not right now.)\"":
            jump new_personal_request
    
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    show screen hermione_main
    with d3
    
    m "You know what? I've been doing too much of the work lately."
    call her_main("[genie_name]?","body_02")#247
    m "You heard me. Lately, all you've done is bend over the desk, while I slam your cunt and your ass to a sloppy, screaming orgasm."
    if whoring < 21:
        jump too_much
    #*Hermione looks shocked*hide screen hermione_main
    #call her_expression(248)#248
    #show screen ctc
    #pause
    call her_main("I... then... ahem. What would you like to do then?","body_10")#249
    m "I am going to sit back and you are going to sit and bounce on my cock."
    call her_main("What?! [genie_name], I don't-","body_18")#250
    m "So Gryffindor doesn't need any points then? Oh, well. I tried. Good day Miss Granger."
    #call her_expression(251)#251
    #show screen ctc
    #pause
    call her_main("Aright, alright. So... what's the pay?","body_09")#252
    m "The standard. I have been doing all the work lately. It's only fair."
    
    
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    hide screen hermione_02
    $ walk_xpos=400 #Animation of walking chibi. (From)
    $ walk_xpos2=325 #Coordinates of it's movement. (To)
    $ hermione_speed = 1.25 #The speed of moving the walking animation across the screen.
    show screen hermione_walk_01 
    pause 1.20
    
    show screen blkfade
    with fade
    
    hide screen blktone
    show screen bld1
    hide screen hermione_walk_01
    hide screen hermione_main
    
    call her_face("...fine. Just let me... there we...","body_04")#253

    #*Penetration transition*
    $ renpy.play('sounds/gltch.mp3')
    with hpunch
    with kissiris
    
    call her_face("OOOOOOOHH! {image=textheart}","body_235")#254
    call her_face("Yes...","body_236")#255
    
    hide screen hermione_main
    hide screen genie
    $ genie_chibi_xpos = -170 #-185 behind the desk. (Also 5 is something).
    $ genie_chibi_ypos = 35
    $ g_c_u_pic = "bounce_ani_s"
    show screen desk_03
    show screen g_c_u
    hide screen blkfade
    with d3
    
    ">Hermione begins to slowly slide up and down your dick."
    m "You can do better than this! Pick up the pace whore!"
    call her_face("Ah... ah...{image=textheart}","body_237")#256
    "She moves a little faster..."
    $ g_c_u_pic = "bounce_ani"
    show screen g_c_u
    m "Did you hear me, slut? I said go faster you little whore!"
    ">You feel a shiver pass through her with each insult."
    m "Go."
    call soft_slaps
    m "Faster."
    call soft_slaps
    #">You punctuate each word with a slap to her ass."
    call her_face("AAAH! {image=textheart} {image=textheart} {image=textheart}","body_219")#257
    "She starts to move much faster."
    $ g_c_u_pic = "bounce_ani_f"
    show screen g_c_u
    call her_face("Yes! Harder!","body_232")#258
    m "Honestly."
    ">You reach under her shirt with one hand and start to twist and pull on one of her nipples."
    ">You spank even harder with the other."
    call hard_slaps
    call her_face("IT HUUURTS! {image=textheart} {image=textheart}","body_220")#259
    m "Even now, I still have to take the initiative, you self-deluding whore!"
    call her_face("I- AH! {image=textheart} I'm n- Ah-a!","body_235")#260
    m "You're still claiming this is all just for the house points? Even while you're bouncing yourself up and down on my cock? "
    call her_face("I-i-it i-i-i-isss- Ah! {image=textheart}","body_236")#261
    m "All right, fine. Prove it. If you can go {i}ONE FULL MONTH{/i} without any form of sexual relief;" 
    m "I'll award \"Gryffindor\" {i}ONE THOUSAND{/i} points and double the points of any favours you choose to take thereafter."
    call her_face("!!!! REALLY?! (Oh god, I'm getting so close...)","body_202")#262
    m "Yes. BUT. If you can't, you belong to me. No more house points. You'll be my personal fucktoy from then on. Do we have a deal?"
    call her_face("Yessss...","body_236")#263
    m "Answer me clearly, whore! Do we have a deal?"
    call her_face("OH GOD! YES! YES WE HAVE A DEAL!","body_234")#264
    call her_face("I! I'M-","body_234")#265
    stop music fadeout 1 
    m "Good."
    
    show screen blkfade
    with fade
    hide screen desk_03
    hide screen g_c_u
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen genie
    
    ">You lift Hermione off of you."
    call her_face("!!! W-what are you-","body_211")#266
    m "We did just make an agreement. Of course if you wish to forfeit already..."
    
    
    hide screen bld1
    hide screen blkfade
    with d3
    
    #show full sprite and chibi in middle
    
    call her_main("I- N-no! I was just surprised.","body_208")#267
    m "Oh, and before I forget."
    call cast_spell
    ">You cast a spell on Hermione"
    m "There."
    call her_main("What did you just do?","body_206")
    m "I cast a spell to prevent you from feeling any relief."
    m "After all, it wouldn't due for you to lose by accident! This is a test of character, not chance. "
    call her_main("I suppose.","body_203")#*Looks at you cautiously*
    call her_main("...Thank you.","body_204")
    m "You'll need to stop by every morning so I can reapply it."
    call her_main("I-very well. Until then.","body_199")
    
    call hermione_exit
    $ hermione_takes_classes = True
    
    m "Well. My balls are going to be the right colour for a little while..."
    show screen blkfade
    with fade
    $ per_quest_30_points = 1
    $ per_q_the_gamble = True
    $ per_q_the_gamble_a = True
    jump night_start
label per_quest_the_gamble_complete:
    
    if per_q_the_gamble_a:
        jump tell_snape_gamble
    elif per_q_the_gamble_b:
        pass
    elif per_q_the_gamble_c:
        jump my_slave_n
            
        
    if per_quest_30_points < 3:
        if per_quest_30_points == 1:
            #*Scene transitions to morning. Hermione enters.*
            
            call hermione_enter
            
            call her_main("","body_33")
            call her_main("G-good morning, [genie_name].","body_44")
            ">Hermione can't stop twitching and fidgeting."
            m "Good morning, Miss Granger."
            m "Hm. You don't appear to have slept well. Is something the matter?"
            call her_main("I-no! I mean- its fine.","body_43")
            m "...If you say so."
            call cast_spell
            ">You cast a spell on Hermione"
            m "There you go. Until next time."
            call her_main("I-yes.","body_34")
            $ per_quest_30_points += 1
        elif per_quest_30_points == 2:
            #*Scene transitions to morning*
            
            m "Huh. What do you know? She's late."
            pause 1.0
            ">Hermione enters the room dazed and distracted"
            call hermione_enter
            
            m "Miss Granger?"
            m "Hello?"
            
            hide screen genie
            show screen chair_02
            hide screen desk       
            show screen desk
            show screen genie_stand
            with d3
            #"You stand and move out from behind the desk."
            
            
            m "{size=+7}WHORE!{/size}"
            with hpunch
            ">Hermione jumps"
            call her_main("I- Oh. Good morning [genie_name]...","body_123")
            ">As she trails off you notice her repeatedly glancing at your crotch."
            m "You don't seem to have improved from yesterday morning. Did you sleep at all?"
            call her_main("I-","body_124")
            ">her hands keep drifting towards her groin and chests before she jerks and moves them away"
            call her_main("I'm fine.","body_123")
            m "Are you certain?"
            call her_main("I, uh, I need to get to class.","body_121")
            m "Very well, then."
            call cast_spell
            ">you cast the spell."
            call her_main("","body_124")
            ">Hermione glances at your groin one last time before she leaves."
            $ per_quest_30_points += 1
        
        hide screen bld1
        hide screen hermione_main
        # hide screen desk
        # hide screen chair_02
        # show screen blkfade
        # with d3
        
        call hermione_exit
        $ hermione_takes_classes = True
        
        hide screen genie_stand
        
        jump day_main_menu
    else:
        jump my_slave
    return
    
    
    
    label tell_snape_gamble:
        #*Scene skips to Genie and Snape drinking wine by the fire.*
        show screen with_snape_animated
        play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
        show screen fireplace_fire
        hide screen genie
        hide screen chair
        hide screen desk
        show screen desk
        
        hide screen snape_02 #Snape stands still.
        hide screen bld1
        hide screen snape_main
        with d3
        
        $ fire_in_fireplace = True
        
        
        hide screen blkfade
        with fade
        "You tell Snape about what happened."
        sna_[5] "!!! You did what!? Are you completely MAD?!"
        m "Not completely, no. All is well in hand. Stop worrying so much."
        sna_[4] "But-"
        m "Think about it."
        m "I've spent how long getting her hooked on orgasms? And now I've forced her to go cold turkey."
        m "No matter how much she masturbates or how frantically she fucks she can't cum."
        m "She can still get excited, though."
        m "With her frustration constantly building, I wouldn't give her much before she snaps. A week, week and a half, tops."
        sna_[11] "Hmm... Well, we'll just have to hope for the best."
        m "It will all work out. Just trust me."
        $ per_q_the_gamble_a = False
        $ per_q_the_gamble_b = True
        jump day_start
    
    label my_slave:
        #*Scene transitions to morning*
        pause 0.25
        # $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        # $ walk_xpos=570 #Animation of walking chibi. (From)
        # $ walk_xpos2=400 #Coordinates of it's movement. (To)
        # $ hermione_speed = 2.1 #The speed of moving the walking animation across the screen.
        # $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        # show screen hermione_walk_01 
        # with d4
        # pause 2.1
        # $ hermione_chibi_xpos = 400 #Near the desk.
        # show screen hermione_02 #Hermione stands still.
        # with d3
        ">Hermione enters. She does not look happy"
        call hermione_enter
        m "Miss Granger?"
        hide screen hermione_02
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=325 #Coordinates of it's movement. (To)
        $ hermione_speed = 1.25 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1.20
        show screen blkfade
        with fade
        hide screen hermione_walk_01 
        "She says nothing as she walks around the desk."
        #show screen blktone
        m "Mi-"
        
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        hide screen hermione_main
        hide screen genie
        $ genie_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        
        hide screen hermione_02 #Hermione stands still.
        hide screen blkfade
        hide screen blktone
        hide screen bld1
        show screen ctc
        with fade
        show screen bld1
        with d3
        #"You're interrupted as she jerks your pants down and swallows your cock to the root."
        ">Hermione jerks your pants down and swallows your cock to the root."
        
        
        
        m "HOLY! I suppose this means you forfeit?"
        her "Gobble! Glurk! Gulp!"
        #"She says nothing, the only noise she makes are the desperate mewling and the sounds of gobbling your dick."
        ">Hermione says nothing, the only noise she makes is the desperate mewling and gobbling of your dick."
        m "Have it your way."
        ">You grab her head and start to fuck her throat."
        m "YES! TAKE IT ALL THE WAY DOWN!"
        her "!!! Gobble -- Gobble -- Gobble!!!!"
        m "USE YOUR TONGUE, YOU FILTHY BITCH!"
        her "Gobble! Lick! Lick! Lick! Gobble!"
        m "(Damn. The past couple days are getting to me. I was hoping to make this last.)"
        ">You force your pulsing cock all the way down her throat and start cumming."
        
        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u # SUCKING
        with d3 
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        
        
        her "GHT!!!!"
        m "ARGH!!!"
        her "GULP! GULP! GULP! GULP! GULP! GULP!"
        m "SUCK IT ALL OUT!"
        her "GULP! GULP! GULP! GULP!"
        m "Ah!"
        
        ">As you release her, Hermione falls to the ground shivering."
        ">She doesn't seem very coherent as she grasps at your leg."
        
        $ hermione_chibi_xpos = -150 #-185 behind the desk. (Also 5 is something).
        $ hermione_chibi_ypos = 10
        $ h_c_u_pic = "hand_ani"
        show screen h_c_u
        hide screen g_c_u
        with d3
        show screen blkfade
        with d3
        hide screen h_c_u # NOT SUCKING
        
        #her "Please- Give- Need- Please!"
        call her_face("Please- Give- Need- Please!","body_209")
        m "So much for a month! You couldn't even last a week!"
        #her "Need- Please-"
        call her_face("Need- Please-","body_210")
        #">She scrambles to stand as you lift her by her hair and half toss her onto the desk."
        ">Hermione scrambles to stand as you lift her by her hair and half toss her onto the desk."
        m "Well, since you asked so nicely."
        
        #*penetration transition*
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        $ genie_chibi_xpos = -210 #-185 behind the desk. (Also 5 is something).
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "sex_ani"
        show screen chair_02
        show screen g_c_u
            
        hide screen blkfade
        with d3
        
        
        #her "AAAAAAAAAAHHH! Biiiiiiig!!!!!"
        call her_face("AAAAAAAAAAHHH! Biiiiiiig!!!!!","body_219")
        m "Has your pussy actually gotten tighter?"
        #her "AAAAH! NO! NO! STILL NEEEEED!!!"
        call her_face("AAAAH! NO! NO! STILL NEEEEED!!!","body_206")
        m "Oh, right the spell. Well, you'll just have to wait till I'm ready to cum myself."
        #her "!!!"
        call her_face("!!!","body_207")
        ">Hermione starts slamming herself against you with abandon."
        $ g_c_u_pic = "sex2_ani"
        show screen g_c_u
        with hpunch
        #her "GIVE! GIVE! GIVE! GIVE! GIVE!"
        call her_face("GIVE! GIVE! GIVE! GIVE! GIVE!","body_213")
        ">With every thrust she seems to get tighter."
        m "FUCK! ALMOST. ALMOST! HERE WE GO!"
        ">You undo the spell as you flood Hermione's cunt with your cum."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen g_c_u
        pause .35
        with d3 
        pause .15
        show screen remove_spell
        pause 1.7
        hide screen remove_spell
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        
        $ g_c_u_pic = "pause_sex"
        
        #her "!!!!"
        call her_face("!!!!","body_234")
        ">Hermione tries to scream but can only manage to gasp and convulse as she finally gets her release."
        ">You watch her and wait for her spasms to die down."
        
        show screen blkfade
        with d3
        hide screen g_c_u
        
        m "Can you understand me?"
        ">Hermione's eyes are still glassy but she nods."
        m "Good. A deal is a deal. You belong to me now. Understand?"
        #her "Yesss."
        call her_face("Yesss.","body_199")
        m "Ready for more?"
        ">Still twitching on the ground, she speaks slowly, as though her thoughts are traveling through molasses."
        #her "I... but... class..."
        call her_face("I... but... class...","body_211")
        m "Oh, you're not going to class."
        m "I'm going to thoroughly enjoy my first day as your owner."
        ">You walk to the door and send for Snape."
        m "Now, what to do next... Ah! I know!"
        ">You walk over to Hermione and lift her. Keeping her back to your chest and your hands under her thighs, you hold her up with her legs spread."
        m "Now put your hands around the back of my neck and tell me what you are."
        #her "Your whore."
        call her_face("Your whore.","body_209")
        m "Wrong."
        #her "?"
        call her_face("?","body_210")
        m "You see, whores get paid. Whores are people."
        m "You don't get paid. You stopped being a person when you sold yourself to me for release."
        m "You are my slave now. My toy. My pretty little fucktoy."
        m "SAY IT."
        #her "I'm your fucktoy."
        call her_face("I'm your fucktoy.","body_199")
        m "Now, what does a fucktoy want?"
        ">You lower her, teasing her asshole with the tip of your cock."
        #her "N-Nothing. A toy w-wants nothing. It's just used by its owner."
        call her_face("N-Nothing. A toy w-wants nothing. It's just used by its owner.","body_215")
        m "VERY good."
        ">You drop her onto your dick."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #her "MY AAASS!!!"
        call her_face("MY AAASS!!!","body_219")
        m "Whose ass?"
        ">You lift her off your dick."
        #her "YOURS! YOUR FUCKTOY'S ASS!"
        call her_face("YOURS! YOUR FUCKTOY'S ASS!","body_225")
        ">Desperate tears form in her eyes."
        m "Since it is your first day, I'll be nice."
        m "I'll give you a few choices."
        m "Do you want me to fuck your ass?"
        #her "Yes."215
        call her_face("Yes.","body_215")
        m "How?"
        #her "Haaard. Pound me. Fill me with your cum!"
        call her_face("Haaard. Pound me. Fill me with your cum!","body_213")
        m "As you wish!"
        ">You drop her back onto your dick and start pounding her ass, your dick is harder than it's ever been."
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        #her "MY ASS!!! YOU'LL BREAK IT!!"
        call her_face("MY ASS!!! YOU'LL BREAK IT!!","body_219")
        ">You lift her up slowly, making the threat clear."
        #her "AHH!! BREAK IT!! BREAK ME!! HARDER!!"
        call her_face("AHH!! BREAK IT!! BREAK ME!! HARDER!!","body_236")
        call snape_enter
        sna_[1] "What did you-"
        sna_[8] "!!!"
        #her "CUMMING!! MY ASS IS CUMMING!!"
        call her_face("CUMMING!! MY ASS IS CUMMING!!","body_236")
        m "As you can see, Miss Granger will be indisposed."
        ">Hermione's grip slips and she catches herself on your desk. She quivers as you adapt and start pounding her from behind."
       
        $ g_c_u_pic = "sex2_ani"
        show screen g_c_u
        hide screen blkfade
        with d3
        
        m "Can you arrange an excuse for the next day? Or three?"
        #her "AAAAH! OH GOD!"
        call her_face("AAAAH! OH GOD!","body_238")
        sna_[18] "Ha! Of course!"
        #her "AGAIN!! CUMMING AGAIN!! {image=textheart} {image=textheart}"
        call her_face("AGAIN!! CUMMING AGAIN!! {image=textheart} {image=textheart}","body_237")
        sna_[21] "(This might be the happiest day of my life!)"
        call snape_leave
        ">Hermione kept screaming and shaking her ass on your dick. You're fairly certain she didn't notice the conversation."
        #her "I'm going insane! Your dick is driving your fucktoy insane!"
        call her_face("I'm going insane! Your dick is driving your fucktoy insane!","body_236")
        m "You and your way with words!"
        #her "CUMMING! STILL CUMMING!"
        call her_face("CUMMING! STILL CUMMING!","body_234")
        m "Here, let me JOIN YOU!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        
        
        #her "MY ASS! SO HOT!"
        call her_face("MY ASS! SO HOT!","body_235")
        #her "FILLING MY ASS!"
        call her_face("FILLING MY ASS!","body_236")
        m "YOU LIKE IT?"
        #her "YES!!!! {image=textheart} {image=textheart}"
        call her_face("YES!!!! {image=textheart} {image=textheart}","body_234")
        m "HAVE SOME MORE!"
        ">Hermione tries to scream as you flood her ass but once again can only manage gasps as she collapses to your desk, quivering."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
        $ g_c_u_pic = "sex_cum_in_ani"
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        hide screen bld1
        with d3
        show screen ctc
        pause
        hide screen ctc
        
        m "So, Toy, what should... Toy?"
        ">Hermoine lies there, unresponsive to your words and shakes."
        $ g_c_u_pic = "pause_sex"
        m "Huh. She passed out. I guess having the biggest orgasms of your life after being too horny to sleep for three days will do that."
        m "Now, how to pass the time..."
        $ per_q_the_gamble_b = False
        $ per_q_the_gamble_c = True
        jump night_start
        
    #transition to nighttime menu
    #after daytime menu
        
    label my_slave_n:
        #$ hermione_chibi_xpos = 400 #Near the desk.
        #$ hermione_chibi_ypos
        #show screen hermione_02 #Hermione stands still.
        #hide screen blkfade
        #with d3
        #$ h_c_u_pic = ""
        #show screen h_c_u
        
        her "Hn... Wha... Where..."
        m "Good evening, Toy. I was beginning to worry."
        her "Oh... Oh God... I - we - the bet-"
        m "You lost the bet, yes, and then you passed out. I had to entertain myself. I hope you don't mind."
        her "Mind?"
        m "You Haven't noticed?"
        her "...Noticed what?"
        m "This."
        "You rip the anal beads out in one motion."
        her "!!!!"
        "She had started to rise but promptly falls back to the desk as her legs give out."
        m "Now that you're more or less in your right mind, I will make myself perfectly clear. We had an agreement."
        her "I-"
        "You walk behind her, grasp her hips and forcefully shove her ass against you. Your rigid cock grinding against the lips of her pussy."
        m "You made your own choices. Took your chances. And you FAILED.So now you. Are. MINE."
        "You slip your hand to her cunt, and shove your fingers inside."
        m "THIS belongs to me."
        her "Ah-"
        "You remove your fingers, now sopping wet. You give her young, bountiful ass a slap and plunge your thumb into her tight asshole."
        m "THIS belongs to ME."
        her "HAH-AH-"
        "You start pumping her ass with your thumb as you slowly rub her pussy with your dick."
        m "Is that clear?"
        her "..."
        her "*sobs* yes."
        m "Good."
        "You open a desk drawer, remove a black leather collar, and toss it in front of her face."
        m "Put it on."
        "Crestfallen, she slowly puts it on."
        m "A few key points. That collar is enchanted. Only you could put it on and only if you were willing. If you were unwilling, it would refuse to close."
        m "Only I can remove it. If you refuse my orders it will activate an aphrodisiac charm as well as the same charm I cast on you for the last three days until you comply."
        m "I can, of course, activate it at will as well."
        m "Now, get on your knees."
        "Once she's done so, you rip her shirt open. You pay the flying buttons and her halfhearted sounds of protest no mind."
        "You grab her tits roughly in each hand; jerking her forward, and wrapping them around your cock."
        "You twist her nipples as you thrust between her breasts."
        her "...Ah... ha... ah..."
        m "Do you like this, Toy?"
        her "...Ah... n-no..."
        m "Tell me the truth, Toy. Do you enjoy this?"
        her "N-no- AH-AH-AH!!!"
        "Her panting becomes even heavier and her hands quickly move to her pussy."
        her "I -AH!- I-"
        "Her breath hitches as she frantically stirs her pussy with her fingers."
        her "N-AH!- -HAH!- YES! {image=textheart} {image=textheart} YES! I ENJOY IT!!"
        "Her hips start to rock, and you squeeze her tits with force."
        her "AH! {image=textheart}"
        m "Are you you going to cum?"
        her "YES!! {image=textheart}"
        m "Are you going to cum from having your tits manhandled?"
        her "*sobs* YES!!! {image=textheart}"
        m "No, you're not. You're not allowed to cum before I do."
        her "!! AH! NO! PLEASE!"
        m "Tell me what I am slave! Who are you begging?"
        her "MASTER! MY MASTER! PLEASE LET ME CUM, MASTER!"
        m "What? Did I not make myself clear before? You're my little toy. What does this little toy want?"
        her "CUM ON ME, MASTER! COVER ME IN JIZZ! DROWN ME WITH YOUR SPUNK!"
        m "You and your words! Everytime!"
        "As you soak her hair, face, and perky teen tits with your cum, Hermione's body starts to spasm."
        "You have trouble keeping your hold on her as she her back bows and her body jumps in place."
        "You couldn't say how many times the pain caused by her own thrashing makes her cum as you hold tight to her tits."
        "Eventually, she collapses against you. You can feel her breath on your cock."
        m "Look at yourself."
        m "All of that pride and self righteousness you had at the beginning, and now you're collapsed against me. drooling on my dick, and... you can't even hear me, can you?"
        "You grab her hair and slap her face."
        m "Can you!"
        her "AH!! {image=textheart} AH!! {image=textheart} AH!! {image=textheart}"
        "Your slap sends a short series of tremors through her body."
        "As you watch her hips buck, you feel your dick growing harder."
        m "...I am not waiting for morning."
        m "Come on. Up and at 'em."
        "You start slapping her face with your cock, careful not to hit hard enough to send her into another round of paingasms."
        her "..."
        "She moans blearily as you cockslap her back to some semblance of consciousness."
        m "Wakey, wakey. Now, what should you be doing?"
        "You let go of her hair. Her eyes are still dazed as she opens her mouth, tongue sticking out, and tries to catch your still swaying dick in her mouth."
        "She fumbles at first and you find yourself tempted to tease her. Before you can decide she manages to get her lips around your cockhead and holds on stubbornly, if weakly."
        "She slowly forces your cock deeper and deeper into to her throat."
        her "Glurk... Gobble... Lick..."
        m "Do I need to explain what will happen if you don't pick up the pace?"
        "The threat seems to rouse her some."
        her "GLURK! GOBBLE! GOBBLE! GULP!"
        "As her motions become more frantic, you can't stop your hips from thrusting."
        m "See? That wasn't so difficult. Now, take a deep-breath through your nose..."
        "You grab her by her soaked, matted hair and force you dick as far as it will go and keep it there."
        her "..............."
        m "Oh, yes. Your throat is the best."
        her ".............................."
        m "Actually, I can't think of any part of your body that isn't."
        her ".............................."
        m "It's as though you were made to be my personal plaything!"
        her "......"
        m "I suppose I'm really quite blessed."
        her "!!!"
        m "Hm? what's this?"
        "You watch as Hermione's hips start to roll."
        her "!!!!!!!"
        m "Oh, this is just precious!"
        "Hermione's hand has drifted toward her pussy."
        her "!!!!!!!!!!"
        m "Here I am, choking you with my cock, and not only are you getting off, you're actually masturbating!"
        "She wildly fingers herself with one hand as the other firmly rubs your balls with the other."
        her "!!!!!!!!!!!!!!"
        m "I don't know what I could have done to deserve a wonderful little toy like you! Now, TAKE IT ALL!"
        her "GHT!!!!!!!!"
        "Your fucktoy's eyes roll back as you flood her throat, her hand has stopped massaging your balls and is now twisting one of her nipples."
        her "GULP! GULP! GULP! GULP! GULP! GULP! GULP!"
        m "ALL OF IT! DOWN YOUR THROAT!"
        "As her body is once consumed by her climax, you hold tight to her hair."
        her "GULP! GULP! GULP! GULP! GULP! GULP!"
        m "COME ON! ALMOST DONE!"
        her "GULP! GULP! GULP! GULP!"
        "You pull her off your dick. It takes more effort than you expected, and are rewarded with an interesting popping sound, accompanied by a more interesting sensation."
        $ renpy.play('sounds/pop02.mp3')
        "Not having finished, you spatter her face with still more of your cum."
        m "There!"
        "You let go of your toy's hair and she falls to the ground, still jerking and twitching."
        m "Oooh, no. No, you don't. You're not passing out again."
        "You gently shake her, trying to keep her awake."
        m "I should have known better. Here."
        "After you're (mostly) certain she won't pass out again, you hand her a slip of paper."
        m "Take this hall pass and go take a bath at the prefect's bath. The password should be lemony fresh. Then go to bed."
        "She blinks blearily at the pass and then at you. You can almost see as she tries to form a coherent thought."
        m "Don't be mistaken. You're my new little fucktoy, and I intend to make frequent and hard use of you for as long as I am able."
        m "That means I need to keep you well maintained."
        m "Now go."
        "Hermione staggers out of the room."
        $ per_q_the_gamble = False
        $ per_quest_30c = False
        jump day_start
        
        
        
        
