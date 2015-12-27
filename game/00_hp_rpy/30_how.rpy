label howtoplay_ht:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/silly_fun_loop.mp3" fadein 1 fadeout 1 # LOLA'S THEME.
    if not persistent.tut: #Turns TRUE after tutorial happened once already. EVENT_01
        
        
        
        
        $ lola_face = "01_hp/22_lola/01.png"
        $ lola_body = "01_hp/22_lola/body_01.png"
        
        $ l_things = True
        #$ l_blush = True
        $ lx = 490
        $ ly = 190
        show screen l_head
        l "Hello, pervs of the internet!"
        hide screen l_head
        a5 "Whach it, brat!"
        $ l_things = False
        $ lola_face = "01_hp/22_lola/02.png"
        show screen l_head
        l "Huh...?"
        hide screen l_head
        a6 "What did I tell you about using the \"p\" word?"
        $ l_question = True
        $ lola_face = "01_hp/22_lola/03.png"
        show screen l_head
        l "Em... Use it as often as possible?"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}Wrong!{/size}"
        $ l_question = False
        $ l_drop = True
        $ lola_face = "01_hp/22_lola/04.png"
        show screen l_head
        l "ght!"
        hide screen l_head
        pause.01
        with hpunch
        a7 "{size=+7}We don't use it! Ever!{/size}"
        $ lola_face = "01_hp/22_lola/01.png"
        $ l_drop = False
        show screen l_head
        l "Because daddy is the biggest perv there is?"
        hide screen l_head
        a6 "Ght!"
        a6 "Did you enjoy starring in \"Princess Trainer\"?"
        $ l_hearts = True
        $ lola_face = "01_hp/22_lola/01.png"
        show screen l_head
        l "It was the best!"
        hide screen l_head
        a1 "Want to be in the \"gold edition\" as well?"
        $ l_hearts = False
        $ lola_face = "01_hp/22_lola/05.png"
        show screen l_head
        l "!!!"
        $ lola_face = "01_hp/22_lola/06.png"
        show screen l_head
        l "Ladies and gentlemen, welcome to the \"Hermione Trainer\" tutorial."
        hide screen l_head
        a1 "Attagirl."
        $ l_drop = True
    else: # EVENT_02
        $ lx = 490
        $ ly = 190
        $ lola_body = "01_hp/22_lola/body_01.png"
        $ lola_face = "01_hp/22_lola/05.png"
        show screen l_head
        l "Hm...?"
        l "You want to hear the tutorial again?"
        $ lola_face = "01_hp/22_lola/09.png"
        l "Hm...."
        $ lola_face = "01_hp/22_lola/11.png"
        l "You are not very bright, are you?"
        $ lola_face = "01_hp/22_lola/10.png"
        l "Hm..."
        $ l_things = True
        $ lola_face = "01_hp/22_lola/08.png"
        l "*Giggle!*"
        $ l_things = False
        $ lola_face = "01_hp/22_lola/01.png"
        l "You want me to give you the tutorial topless?"
        hide screen l_head
        $ d_flag_01 = False
        menu:
            "\"You bet!\"":
                $ lola_face = "01_hp/22_lola/01.png"
                show screen l_head
                
                $ d_flag_01 = True
                l "Alrighty!"
                hide screen l_head
                pause.1
                show screen blkfade 
                with d3
                $ lola_body = "01_hp/22_lola/body_02.png"
                $ l_blush = True
                pause.5
                hide screen blkfade
                with d7
                
                
            "\"Not interested.\"":
                $ lola_face = "01_hp/22_lola/12.png"
                show screen l_head
                l "You're boring..."
                $ lola_face = "01_hp/22_lola/09.png"
                l "Well, whatever..."

                   
    ### THE TUTORIAL ###
    play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
    $ lola_face = "01_hp/22_lola/06.png"
    show screen l_head
    l "Here is a short list of things to keep in mind..."
    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_02.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   

    l "Hermione will only be willing to sell sexual favors in exchange for house points when house of gryffindor is falling behind."
    
    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_01.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3')   
    l "Making friends with professor Snape will make him trust you more, and will increase the rate at which slytherin house get's the points."
    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_03.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    if d_flag_01: # TOPLESS.
        $ lola_face = "01_hp/22_lola/07.png"
    l "Reading educational books makes earning money easier, but is not mandatory."

    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_04.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "Buying the same sexual favor again could lead to a different outcome depending on how far along Hermione is in her training."
    $ lola_face = "01_hp/22_lola/06.png"

    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_07.png" #<---- SCREEN
    l "All favors are organized into two groups: \"personal favors\" and \"public favors\"."
    l "Personal favors take place in the office and don't affect Hermione's reputation much."
    l "Public favors take place off-screen during classes."
    l "Every public favor, except for the last one, has nine different outcomes."
    l "Also buying personal favors is esential for Hermione's training, but public favors are optional."

    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_05.png" #<---- SCREEN

    $ renpy.play('sounds/boing02.mp3') 
    l "Treating Hermione poorly will worsen her mood and could make her very uncooperative..."
    l "She will cool off with time, but you can speed up the process by buying her something nice..."
    
    with hpunch
    $ end_u_1_pic =  "01_hp/22_lola/tut_06.png" #<---- SCREEN
    $ renpy.play('sounds/boing02.mp3') 
    l "And there is no timelimit. So feel free to take as many days to comlete the game as you want."
 
    
    
    
    $ end_u_1_pic =  "01_hp/22_lola/tut_00.png" #<---- SCREEN
    $ l_drop = False
    
    if not persistent.tut: # FIRST TIME TUTORIAL. Turns TRUE after tutorial happened once already. EVENT_01
        $ persistent.tut = True #Turns TRUE after tutorial happened once already.
        hide screen l_head
        a1 "Alright, that's enough..."
        $ l_question = True
        $ lola_face = "01_hp/22_lola/05.png"
        show screen l_head
        l "How did I do?"
        hide screen l_head
        a1 "You did well. Good girl."
        $ l_question = False
        $ l_things = True
        $ lola_face = "01_hp/22_lola/08.png"
        show screen l_head
        l "Me-he-he. Lola is a good girl!"
        $ l_things = False
        $ lola_face = "01_hp/22_lola/01.png"
        show screen l_head
        l "What do I get?"
        hide screen l_head
        a1 "What you want?"
        $ lola_face = "01_hp/22_lola/10.png"
        show screen l_head
        l "Hm..."
        $ l_exclamation = True
        $ lola_face = "01_hp/22_lola/01.png"
        l "Can we have a rape scene with me in the \"Gold Edition\"?"
        hide screen l_head
        a6 "Don't taste my patience, girl."
        $ l_exclamation = False
        $ l_drop = True
        $ lola_face = "01_hp/22_lola/04.png"
        show screen l_head
        l "Sorry, daddy."
        $ l_drop = False
        hide screen l_head
        a5 "............"

    else: ### NOT FIRST TUTORIAL. EVENT_02
        if d_flag_01: #TOPLESS.
            hide screen l_head
            stop music fadeout 1.0
            a1 "What is going on here?"
            $ lola_face = "01_hp/22_lola/14.png"
            $ l_drop = True
            show screen l_head
            l "Yikes!"
            hide screen l_head
            a1 "What did I tell you about exposing yourself to complete strangers?"
            $ lola_face = "01_hp/22_lola/04.png"
            show screen l_head
            l "It's an important part of growing up?"
            hide screen l_head
            a6 "Wrong!"
            $ l_drop = False
            $ l_tears = True
            $ lola_body = "01_hp/22_lola/body_01.png"
            $ lola_face = "01_hp/22_lola/04.png"
            show screen l_head
            l "Daddy, I'm so sorry!"
            l "That mean random Internet person forced me, I swear!"
            hide screen l_head
            a1 "This tutorial is over."
            $ l_blush = False
            $ l_tears = False
            $ lola_face = "01_hp/22_lola/15.png"
            show screen l_head
            l "He-he! You got busted!"
        else:
            $ lola_face = "01_hp/22_lola/09.png"
            l "And that's that..."
            $ lola_face = "01_hp/22_lola/13.png"
            l "Did you get it this time?"
            
        
return

### ABOUT GAME ####
label abouttrainer_ht:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    play music "music/GrapeSodaIsFuckingRawbyjrayteam6.mp3" fadein 1 fadeout 1 
    
    a1 "Hm... Let's see..."
    a1 "I started to work on \"Hermione Trainer\" right after the release of \"Princess Trainer\"."
    a1 "In my mind I had an idea for a cute little game the development of which should not have taken me longer the a couple of month."
    a1 "As we all know now it actually took me longer then half a year..." 
    a1 "And that it despite countless compromises I had to make simply to prevent the damn thing taking even longer to develop."
    a1 "Working on this game was quite fun at times..."
    a1 "But it was also challenging..."
    a1 "Sometimes I had to wrestle with some ideas and gameplay mechanics that didn't want to work properly..."
    a1 "Also working on this game taught me a lot about my abilities as a game developer and of my limitations."
    a2 "I almost feel like I should be getting an achievement diploma or something."
    a1 "Well, I am off to my next project now. {size=-4}(\"Princess Trainer Gold Edition\"){/size}"
    a1 "Thank you for supporting me, guys. And I hope this game will brighten up your day a bit."
    a2 "Until next time..."

    return

### F.A.Q. ###
label faq_ht:
    $ end_u_1_pic =  "title3.jpg" #<---- SCREEN
    show screen end_u_1 
    with flashbb#<---- SCREEN
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 
    
    a1 "Hello. My name is Akabur. I am the creator of this game and I'm here to answer your questions." 
label faq_ht2:    
    menu:
        "How can I show my support?":
            a1 "Well, there are few ways to do that..."  
            a1 "The easiest way would be to contact me (akaburfake2@yahoo.com) and let me know that you enjoyed the game."
            a1 "You could also support me personally at {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}"
            a1 "Another way to support me though would be to follow this link: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a}."
            a1 "For an independent artist like myself every buck counts..."
            a6 "I'm serious. Because of the way I make living the damn bank won't even issue me a creditcard still..."
#            label payments:
#            menu:
#                "-WebMoney info-":
#                    a1 "My RUBLES WebMoney purse: R133931000745"
#                    a1 "My USD WebMoney purse: Z319925489258"
#                    a1 "My EURO WebMoney purse: E800599783938"
#                    jump payments
#                "-YandexMoney Info-":
#                    a1 "My Yandex Purse Number: 41001849167270"
#                    jump payments
#                "-PayPal Info-":
#                    a1 "Contact me via email and i will give you my PayPal."
#                    jump payments
#                "-Credit Card-":
#                    a1 "Here: {a=http://www.test.akabur.com/donate}how to donate with Credit Card.{/a}"
#                    jump payments
#                "-Cancel-":
#                    jump faq_ht2
            jump faq_ht2
            
        "How to stay tuned?":
            a1 "Well, follow this link: {a=http://akabur.hentaiunited.com}akabur.hentaiunited.com{/a} and subscribe. Or visit my site: {a=http://akabur.com}akabur.com{/a}."
            a1 "There is also Patreon of course {a=http://www.patreon.com/akabur}www.patreon.com/akabur{/a}.\nAnd {a=https://twitter.com/AKABUR}my twitter{/a}." 
            jump faq_ht2
        "I have another question.":
            a1 "If you have a question that is not covered in this \"F.A.Q.\", feel free to email it to me: akaburfake2@yahoo.com"
            a1 "Or leave your question here: {a=http://ask.fm/AKABUR}ask.fm/AKABUR{/a}"
            jump faq_ht2
        "I want to report a bug/error.":
            a1 "This game has been tested many many many times, but the best testers are always the players."
            a1 "So if you did encounter a bug, typo or even a grammatical error - feel free to contact me (akaburfake2@yahoo.com) and I will fix the problem in the next version of the game."
            jump faq_ht2
        "Who helped you create this game?":
            a1 "Nobody helped me! I did everything myself!"
            a1 "I wrote all the scripts, created all the art, and composed all the music!"
            a7 "Me! {size=+3}Me! {size=+3}I cerated everything! {size=+3}me!{/size}"
            a2 "Heh..."
            a1 "Well, in truth I did most of the work. But I had a lot of help also."
            a1 "My friend and colleague Dahr provided me graciously (and free of charge) with a lot sorts of additional art (among other things)."
            a1 "Feel free to throw a coin or two the man's way at {a=http://www.patreon.com/DAHR}www.patreon.com/DAHR{/a}"
            a1 "Xaljio was always there for me whenever I needed help with coding. (quite often). Fell free to visit his page at {a=http://www.patreon.com/xaljio}www.patreon.com/xaljio{/a}"
            a1 "And of course patreon and hentaiunited community. You guys are awesome."
            a1 "Thank you for being so supportive and for financing the development of this game. You guys made this world a bit better place."
            jump faq_ht2
        "Is it OK to hack and translate this game?":
            a1 "..."
            a1 "..."
            a1 "no."
            jump faq_ht2

        "Nevermind. Let me out of here!":
            return

    
    return