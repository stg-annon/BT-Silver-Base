label your_whore:
    show screen end_u_1
    $ end_u_1_pic =  "01_hp/17_ending/02.png"
    
    # $ badges = False
    # $ hair_color = 10 
    # $ collar = 0 
    
    hide screen hermione_main
    hide screen room # MAIN BG (DAY).
    
    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 #CANDLE FIRE.
    hide screen candlefire_02 #CANDLE FIRE.
    hide screen lightening #Hide lighting so it woudn't get stuck during clear sky weather and such.
    hide screen cloud_night_01 #NIGHT CLOUDS.
    hide screen cloud_night_02 #NIGHT CLOUDS.
    hide screen cloud_night_03 #NIGHT CLOUDS.
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
     
    hide screen main_menu_01  

    with fade
    #hide screen end_u_1                                           #<---- SCREEN
    #hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    #hide screen end_u_4                                           #<---- SCREEN
    pause.1
    hide screen blkfade
    with d5
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d7
        
        
        
    
    
    
    
    
  
    m "I'd better make sure to avoid being noticed..."
    m "......................"
    m "That's a whole lot of people out there..."
    m "How big exactly is this school?"
    m ".................."
    m ".................................."
    m "I don't see the girl anywhere..."
    m ".............."
    m "......................"
    m "Well, she has got to be here somewhere..."
    m "................"
    m "................................."
    # FADE
    show screen blktone
    with d7
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        mal "Have you heard that rumour about Hermione Granger?"
        mal2 "That she is a major slut?"
        mal "Huh? No, that's not a rumour, that's a fact."
        mal "The rumour was that she is being paid in house points to whore herself out."
        mal2 "Hm... I don't believe that. I think she is just a slut."
        fem "Who's a slut?"
        mal "Oh, hey you..."
        fem "So, who's a slut?"
        mal2 "Hermione Granger..."
        fem "Tsk! You, guys are talking about that whore again?"
        fem "That girl jerks off a couple of dicks, gives a few blowjobs and suddenly she is the school's new sensation."
        fem "Pathetic little muggle-born..."
        mal "You should not be jealous of her--"
        fem "Jealous? Of her? Puh-lease!"
        fem "I have no use for popularity that comes from putting cocks in my mouth!"
        mal "Well, if you ever change your mind..."
        fem "Huh?"
        mal "Feel free to use me as a stepping stone on your road to fame!"
        fem "You wish!"
        mal2 "Hey, guys, I think that's Hermione over there!"
        mal "You're right!"
        mal2 "You think if I ask her to the dance I might get lucky later?"
        mal "Not if I ask her first!"
        $ renpy.play('sounds/run_04.mp3')    #<--------------------Sound of running off.
        pause 2
        mal2 "Hey, wait up! That was my idea!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 2
        fem "Guys...?"
        fem "........................."
        fem "Tsk... Men........"
        
        
        
        
        
        
        
        
        
    else: #Students talking. Ending "Your whore".
        mal "(Have you heard the rumours?)"
        mal2 "(Yeah. They say Hermione took one for the team.)"
        fem "(Whoring herself out for house points!)"
        fem "(How disgraceful!)"
        mal "(Those are just rumours!)"
        fem "(I think it's more than just that...)"
        mal "(Oh, shut up. You are just jealous.)"
        mal2 "(Yeah, you wish you had Hermione's courage!)"
        mal "(Exactly! She is as loyal to \"Gryffindor\" as no one else!)"
        mal "(Even if that's true, what about it?)"
        mal "(Thanks to her sacrifice our house will be getting the cup this year!)"
        mal2 "(Yeah, and what did you ever do for our house?)"
        fem "(I..... But....)"
        mal "(Exactly! So don't you bad-mouth Hermione then!)"
        mal2 "(You said it, man.)"
        fem "(*Pouting*)"
    
    
    
    
    
    
    
    hide screen blktone
    with d3
    hide screen bld1
    with d3
    show screen ctc
    pause
    hide screen ctc
    
    
    $ end_u_2_pic =  "01_hp/17_ending/01.png"
    show screen end_u_2
    with d7
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d5
    m "(There she is!)"
    
    mal "Hermione, hey..."
    call set_hermione_outfit(hg_ballDress_OBJ)
    $ hermione_hair_a = "01_hp/13_characters/hermione/body/head/B_1.png"
    $ hermione_hair_b = "01_hp/13_characters/hermione/body/head/B_1_2.png"
    $ her_head_ypos = her_head_tits
    call her_head("Oh, hello.","body_159")     
    mal "You look... so beautiful tonight, Hermione."
    call her_head("Thank you, you are too sweet.","body_160") 
    mal2 "Can I have the next dance?"
    mal "What? Back off buddy, I was here first!"
    mal2 "Like hell you were!"
    mal "Alright, pal! That does it!"
    mal2 "I'm not your \"pal\", buddy!"
    call her_head("..............","body_161") 
    
    show screen blktone8
    with d3
    stop music fadeout 3.0
    m "Here is my chance!"
    m "(Pst! Girl!)"
    call her_head("???","body_162")     
    m "(Girl, it's me! Over here!)"
    call her_head("[genie_name]?","body_163")     
    #her "Professor Dumbledore?"
    m "(Shush! Keep your voice down and follow me.)"
    call her_head("Oh?","body_163")     
    pause.1
    $ end_u_1_pic =  "01_hp/17_ending/02.png"
    hide screen blktone8
    hide screen blktone
    hide screen bld1
    show screen end_u_1 #<---- SCREEN
    with fade
    show screen ctc
    pause
    hide screen ctc
    show screen bld1
    with d3


    
    
    # ALCOVE 
    
    call her_head("Sir, what is going on? Why are you... lurking in the shadows?","body_162")
    m "Just be quiet and listen for a second! Can you do that for me?"
    play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
    call her_head("Yes, sir...","body_162")
    m "Well, here is the thing then..."
    m "There is something you need to kn--"
    call her_head("Of course sir!","body_166")
    m "What?"
    call her_head("Let's just make this quick, alright?","body_165")
    g4 "Let's make what quick?"
    call her_head("You want me to thank you for the dress now, don't you, sir?","body_164")
    m "The dress? No, no that's not why I am here."
    call her_head("It is fine, sir. I do not mind.","body_165")
    m "Listen to me, girl! I am not who you think--"
    call her_head("Please, sir, let me suck on your cock a little.","body_167")
    g4 "Gh--!!!"
    call her_head("Just a little will do. Please. I'm begging you...","body_167")
    g4 "Damn you, you damn witch!"
    g4 "Stop this! I really need to talk to you!"
    call her_head("Well of course, sir.","body_164")
    call her_head("Put your dick in my mouth and talk to me.","body_167")
    call her_head("Talk dirty to me...")
    g4 "*growl!*"
    m "*Sigh....*"
    m "Fine, let's have it your way..."
    m "But you are abusing your power, girl!"
    call her_head("*Giggle!*","body_168")
    m "And after we're done, we'll have that talk!"
    
    # SUCKING
    
    show screen blkfade
    with d7
    her "*Slurp!* *Slurp!* *Slurp!*"
    m "................."
    
    $ end_u_1_pic =  "01_hp/17_ending/03.png" #<---- SCREEN
    hide screen blkfade
    hide screen bld1
    with d7
    show screen ctc
    pause
    hide screen ctc
    her "*Slurp!* *Gulp!* *Slurp!*"
    her "*Slurp--"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    # LOOKING BACK
    her "Huh?.........."
    her "...................."
    $ end_u_1_pic =  "01_hp/17_ending/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "Yes... Like that.... oh... yes..."
    her "*Gulp!* *Slurp!* *Slurp!*"
    her "*Gulp--"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "...................." #LOOKING BACK
    m "Just keep going girl."
    m "I will let you know if I see someone coming..."
    her "Oh... That's not that, sir..."
    m "Hm?"
    her "They are supposed to make the announcement soon..."
    $ end_u_1_pic =  "01_hp/17_ending/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Slurp!* *Gulp!* *Slurp!*"
    m "The announcement?"
    her "*Slurp!* *Slurp!* *Slurp!*"
    her "*Slurp--"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Yes. About the coronation..."
    $ end_u_1_pic =  "01_hp/17_ending/03.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Gulp!* *Slurp!* *Gulp!*"
    m "What...?"
    her "*Slurp--"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "The Hogwarts autumn ball's queen coronation, sir."
    m "Oh... Is that's a thing?"
    m "Any chance you may be chosen?"
    her "A chance?"
    her "It's already been decided, sir."
    m "What?"
    her "Oh, I mean I hope I will win..."
    her "Since I am the one who organized the whole thing it is only fair..."
    her "Wouldn't you agree sir?"
    m "Well... Sounds like cheat--"
    $ end_u_1_pic =  "01_hp/17_ending/07.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7
    her "*Slurp!* *Slurp!* *Slurp!*"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Wouldn't you agree sir?"
    m "Ehm..."
    her "Wouldn't you agree sir?"
    $ end_u_1_pic =  "01_hp/17_ending/06.png" #<---- SCREEN
    show screen end_u_1                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    with hpunch
    her "{size=+7}*gobble!*{/size}" #DEEPTHROATING
    g4 "{size=+7}Oh, yes!!!{/size}"
    her "*gobble!* *gobble!* *gobble!*"
    her "*gobble---"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    with d7                                                                        #<---- SCREEN
    her "Good. I knew you would approve."
    $ end_u_1_pic =  "01_hp/17_ending/07.png" #<---- SCREEN
    show screen end_u_1                                            #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "*Slurp!* *Slurp!* *Gulp!*"
    m "Oh... This is magnificent..."
    her "*Slurp!* *Slurp!* *Gulp!*"
    
    show screen bld1
    with d5
    sna "*Khem!*"
    sna "Attention, maggots!" 
    m "(Snape?)"
    sna "I said, quiet down everyone!"
    sna "It is time to announce who will be this year's queen of the annual \"Hogwarts autumn ball\"."
    
    
#    ann "Quiet down everyone, quiet down..."
#    ann "It is time to choose this year's queen of the annual \"Hogwarts autumn ball\"."
    hide screen bld1
    with d5
    
    
    her "Slurp--"
    $ end_u_2_pic =  "01_hp/17_ending/04.png" #<---- SCREEN
    show screen end_u_2                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    her "Oh no! I think they are about to start..."
    her "But I can't just leave you in this..."
    her "...condition, sir."
    
    
    her "What should I do?"
    m "Just go, girl. We can finish this up later."
    her "But... But you got me this dress, sir. And..."
    her ".........."
    her "No, I can't just leave you like this, sir."
    m "Fine! Finish the job then."
    m "If you put some effort into this we'll be done in no time."
    m "I believe in you, girl."
    her "Hm..."
    her "Then you must promise me something, sir."
    m "Yes, what is it?"
    her "Please, do not restrain yourself."
    g9 "Heh... I rarely do, girl."
    show screen bld1
    with d5
    sna "This year's \"Hogwarts Autumn Ball\" queen is..."
    sna "Let's see... Can't open the damn envelope..."
    hide screen bld1
    with d5
    her "Alright. There is no time lose then."
    m "Yes! That's the spirit!"
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        $ end_u_1_pic =  "01_hp/17_ending/03.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Slurp!*"
        m "Yes..."
        $ end_u_2_pic =  "01_hp/17_ending/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Gulp!* *Slurp!* *Gulp!*"
        her "*Slurp--"
        $ end_u_1_pic =  "01_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Sir, is this really the proper way to treat one of your students?"
        m "Huh?"
        $ end_u_2_pic =  "01_hp/17_ending/08.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Gulp!*"
        her "*Slurp--"
        $ end_u_1_pic =  "01_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "I am like a fragile and impressionable little dove..."
        her "Entrusted to your care by my parents..."
        $ end_u_2_pic =  "01_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "You were supposed to treat me \"right\", sir..."
        her "And what did you do instead?"
        m "*Khem!* Let me repeat my previous statement:..."
        m "{size=+7}\"huh?\"{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/94.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "You put your penis in my innocent mouth, sir!"
        $ end_u_2_pic =  "01_hp/17_ending/95.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        g9 "Oh, I see! Yes, I like this innocent girl act!"
        her "*Slurp--"
        $ end_u_1_pic =  "01_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "You pretended to be kind to me..."
        her "You bought me this dress..."
        $ end_u_2_pic =  "01_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "And then....................."
        $ end_u_1_pic =  "01_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Gulp!*"
        her "*Slurp--"
        $ end_u_2_pic =  "01_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "You took advantage of me, sir!"
        her "Tricked me into sucking your big cock!"
        g4 "Oh... Yes! You're good!"
        $ end_u_1_pic =  "01_hp/17_ending/96.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "I'm supposed to be enjoying the ball with my classmates right now..."
        $ end_u_2_pic =  "01_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "But what am I doing instead?"
        $ end_u_1_pic =  "01_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        m "Oh..."
        $ end_u_2_pic =  "01_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Gulp!* *Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp--"
        $ end_u_1_pic =  "01_hp/17_ending/98.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "I'm on my knees, sucking my headmaster off!"
        $ end_u_2_pic =  "01_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Oh, yes you are, you little slut!"
        her "*Slurp!* *Slurp!* *Slurp!*"
        her "*Slurp!* *Slurp!* *Gulp!*"
        g4 "You are really good at this dirty talk stuff..."
        g9 "You should try writing children's books, or something..."
        $ end_u_1_pic =  "01_hp/17_ending/07.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp--"
        $ end_u_2_pic =  "01_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Oh, but I would not know how, sir..."
        $ end_u_1_pic =  "01_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "because I am but a child myself..."
        g4 "You nasty little thing!"
        $ end_u_2_pic =  "01_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Gulp!* *Slurp!* *Slurp!*"
        
        show screen bld1
        with d5
        sna "Miss Granger?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">A murmur is running though the crowd of students..."
        hide screen bld1
        with d5
        
        her "*Slurp!* *Slurp!* *Gulp!*"
        her "*Gulp--"
        $ end_u_1_pic =  "01_hp/17_ending/91.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Sir, am I being an obedient little slut?"
        g4 "Yes you are, girl!"
        $ end_u_2_pic =  "01_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Would you say I am a good student?"
        g9 "I would say that you are an excellent student, girl!"
        $ end_u_1_pic =  "01_hp/17_ending/92.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Good..."
        $ end_u_2_pic =  "01_hp/17_ending/99.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "I am making my mommy and my daddy proud!"
        $ end_u_1_pic =  "01_hp/17_ending/95.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Gulp!*"
        g4 "Oh, girl, you are killing me!"
        her "*Slurp-slurp-slurp-slurp!!!*"
        g4 "Oh, yes! Like that!"
        her "*Slurp--"
        $ end_u_2_pic =  "01_hp/17_ending/93.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Do I deserve a reward, sir?"
        $ end_u_1_pic =  "01_hp/17_ending/100.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "I would like you to reward me with your cum, please."
        g4 "Grh!"
        $ end_u_2_pic =  "01_hp/17_ending/97.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Geh! Almost...!"
        her "{size=+5}*Slurp-gulp-slurp-slurp!!!*{/size}"
        g4 "{size=+5}Here it com--{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/101.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "*Slurp--.........................."
        her "!!!"
        show screen ctc
        pause
        hide ctc
        show screen blkfade 
        with d7
        $ end_u_2_pic =  "01_hp/17_ending/102.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        g4 "{size=+5}What the...!? Why did you stop?!{/size}"
        g4 "{size=+5}What the hell are you doing--{/size}"
        hide screen blkfade 
        with d7
        show screen ctc
        pause
        hide screen ctc
        her "{size=+5}Cum for me. sir! Cum for me!{/size}"
        with hpunch
        g4 "{size=+5}What the hell is this?!{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/103.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Cum for me. sir! I want your hot cum on me!{/size}"
        g4 "Argh! You whore!"
        $ end_u_2_pic =  "01_hp/17_ending/104.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Yes I am!{/size}"
        her "{size=+5}Nothing but a cum hungry whore, sir!{/size}"
        with hpunch
        g4 "{size=+7}Argh!!!{/size}"
        g4 "{size=+7}Take this, then!!!{/size}"
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+7}ARGH!{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/105.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "{size=+5}Ah! Yes, sir! Yes! cum for me!{/size}"
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        with hpunch
        g4 "{size=+7}ARGH!{/size}"
        g4 "{size=+7}Argh!!! YES!!!{/size}"
        $ end_u_2_pic =  "01_hp/17_ending/106.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Ah... yes... ah..."
        g4 "Oh... ght... *panting*"
        $ end_u_1_pic =  "01_hp/17_ending/105.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "Thank you sir..."
        $ end_u_2_pic =  "01_hp/17_ending/107.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                       #<---- SCREEN
        her "..........................................."
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        
        # CUMMING
        pause.5
        m "What on earth just happened, girl?!"
        $ her_head_ypos = her_head_tits
        call her_head("What do you mean, sir?","body_165")  
        $ end_u_1_pic =  "01_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        hide screen blkfade
        with d7
        m "Do I really need to point this out to you, girl?"
        g4 "{size=+5}Do I really?{/size}"
        call her_head("Oh... You mean the hair thing...?","body_165")
        m "Yes...\"the hair thing\"..."
        call her_head("Well, what did you expect me to do, sir?","body_168")
        m "Literally anything..."
        g4 "...but {size=+7}THAT!{/size}"
        call her_head("But... I need to look my best for the coronation...","body_163")
        m "And a hairdo full of cum is supposed to ensure that?"
        call her_head("Well... yes...","body_165")
        call her_head("You see, cum is a great hair fixative and--","body_163")
        
        show screen bld1
        with d5
        stop music fadeout 1.0
        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"
        sna "(Not that I care...)"
        hide screen bld1
        with d5
        
        call her_head("The coronation! I must go now!","body_161")
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        
        m ".............................."
        m "................"
        m "..."
        with hpunch
        g4 "{size=+9}WHAT THE HELL...?!!{/size}"
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        

        ">..............{w}..................{w}...................."
        
        
        
        
    else:
        $ end_u_1_pic =  "01_hp/17_ending/06.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "{size=+5}*GOBBLE!*{/size}"
        g4 "{size=+5}Yeeeeeeeeeees!{/size}"
        show screen bld1
        with d5
        sna "There! Hm...?"
        sna "(Well of course... Why am I not surprised?)"
        sna "Miss Hermione Granger of the \"Gryffindor\" house..."
        ">Loud applause and cheering."
        sna "Miss Granger, if you would be so kind to grace us with your presence..."
        hide screen bld1
        with d5
        her "*GOBBLE--GOBBLE--GOBBLE!*"
        m "Yes! That's a good slut!"
        her "{size=+5}*gobble--gobble--gobble!!!*{/size}"
        m "Yes. Now, move your tongue..."
        m "Lick my balls, girl. Come on!"
        $ end_u_2_pic =  "01_hp/17_ending/10.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *Lick!* *Lick!* *gobble!*"
        m "Yes... Like that."
        m "What a good whore you are..."
        her "*Lick!* *Lick!* *gobble!* *Lick!*"
        m "Now look up at me whore."
        $ end_u_1_pic =  "01_hp/17_ending/11.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "???................"
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        pause.3
        $ end_u_1_pic =  "01_hp/17_ending/12.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        hide screen white
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        her "*gobble??!*"
        m "No, don't you stop now!"
        $ end_u_2_pic =  "01_hp/17_ending/13.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble--gobble--gobble!*"
        m "Yes, whore! Yes!"
        show screen bld1
        with d5
        sna "MIss Granger?"
        sna "If you would, please..."
        sna "Miss Granger?"
        hide screen bld1
        with d5
        $ renpy.play('sounds/spit.mp3')    #<--------------------Sound of spiting. 
        show screen white
        pause.3
        $ end_u_2_pic =  "01_hp/17_ending/14.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        hide screen white
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        her "!!!!!!!!!!!"
        her "......................................?"
        m "What's the matter, my little spit bucket?"
        m "Keep sucking my cock!"
        $ end_u_1_pic =  "01_hp/17_ending/15.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble--gobble--gobble!*"
        m "Yes. Good whore."
        her "*gobble--gobble--gobble!*"
        m "Keep deepthroating me like that, yes!"
        her "*gobble!* *gobble!* *gobble!*"
        m "The balls! Don't forget to work your tongue!"
        $ end_u_2_pic =  "01_hp/17_ending/16.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *Lick!...* *Lick!...*"
        m "Yes! Keep at it and we will be done here in no time!"
        m "Oh, I almost forgot..."
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        pause.3
        $ end_u_2_pic =  "01_hp/17_ending/17.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        her "..........................."
        her ".................."
        $ end_u_2_pic =  "01_hp/17_ending/18.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "you just look so pretty with your face all covered in my spit!"
        $ end_u_1_pic =  "01_hp/17_ending/19.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Hm..."
        her "*gobble!* *gobble!* *Lick...* *gobble!*"
        m "Maybe we should show your pretty face to everyone?"
        m "Should I call some of your classmates over?"
        $ end_u_2_pic =  "01_hp/17_ending/17.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "!!!!!!!!!!!!!!!"
        m "Relax..."
        m "I want to get caught as much as you do."
        $ end_u_1_pic =  "01_hp/17_ending/19.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        
        
        

        show screen bld1
        with d5
        sna "Miss Granger?"
        sna "{size=-4}(Where is that girl?){/size}"
        ">A murmur is running though the crowd of students..."
        hide screen bld1
        with d5
        
        m "Alright, listen up, whore."
        $ end_u_2_pic =  "01_hp/17_ending/20.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "*gobble??*"
        m "I need you to stay still now."
        her "???"
        $ end_u_1_pic =  "01_hp/17_ending/21.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "Yes, just like that."
        her "................"
        
        $ end_u_2_pic =  "01_hp/17_ending/22.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "....................................."
        m "I plan to choke you with my cock a little..."
        m "It'll be fun... just relax..."
        her "......................................"
        m "Your throat is the best, girl."
        her "..........."
        $ end_u_1_pic =  "01_hp/17_ending/23.png" #<---- SCREEN
        show screen end_u_1                                           #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        m "So warm and tight..."
        her "............................................."
        her "...................."
        her "......."
        $ end_u_2_pic =  "01_hp/17_ending/24.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "!!!"
        m "I know, I know, you can't really breathe..."
        g9 "But that's what makes this so much fun!"
        
        with hpunch
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Stop struggling, slut. You are not going anywhere!"
        with hpunch
        her "{size=+9}!!!!!!!!!!!!!!!!{/size}"
        
        show screen bld1
        with d5
        sna "Miss Granger..................?"
        sna "You are about to miss your own coronation, girl!"
        hide screen bld1
        with d5
        
        g9 "Heh..."
        g9 "Your queen is right here..."
        g4 "Chocking on my engorged cock!"
        $ end_u_1_pic =  "01_hp/17_ending/26.png" #<---- SCREEN
        show screen end_u_1                                         #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+7}!!!!!!!!!!!!!!!!{/size}"
        m "Oh. You are turning blue, love."
        m "Will you be alright?"
        $ end_u_1_pic =  "01_hp/17_ending/27.png" #<---- SCREEN
        show screen end_u_1                                         #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}!!!!!!!!!!!!!!!!........................{/size}"
        m "Look up whore!"
        her "{size=+3}........................{/size}"
        g4 "I said, look at me!"
        $ end_u_2_pic =  "01_hp/17_ending/28.png" #<---- SCREEN
        show screen end_u_2                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}??!.....................{/size}"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        pause.5
        
        $ end_u_1_pic =  "01_hp/17_ending/29.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
       # with d7                                                                        #<---- SCREEN
        with vpunch
        her "{size=+9}*!!!!!!!!!!!!!!!!!!*{/size}" # 4 (EYE)
        
        $ end_u_2_pic =  "01_hp/17_ending/30.png" #<---- SCREEN
        show screen end_u_2                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................................................."
        g4 "There you go! You wear it well!"
        $ end_u_1_pic =  "01_hp/17_ending/31.png" #<---- SCREEN
        show screen end_u_1                                        #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...........................................................*SOB!*"
        with hpunch
        g4 "Gght!"
        g4 "Here it comes!"
        g4 "I know you are fighting for air down there..."
        $ end_u_2_pic =  "01_hp/17_ending/32.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        g4 "But all you will get from me is a load of hot cum!"
        $ end_u_1_pic =  "01_hp/17_ending/33.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        with hpunch
        her "{size=+9}GHT!!!!!!!!!!!!!!!!{/size}"
        with hpunch
        g4 "{size=+9}ARGH!{/size}"
        with hpunch
        $ end_u_2_pic =  "01_hp/17_ending/34.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+9}*GULP!-GULP!-GULP!-GULP!-GULP!*{/size}"
        g4 "{size=+5}Yes, whore! Drink my cum!{/size}"
        her "*GULP!-GULP!-GULP!-GULP......*"
        with hpunch
        g4 "Not done, yet. Not done! Argh!"
        $ end_u_1_pic =  "01_hp/17_ending/35.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-4}*GULP!* *Gulp!* *Gulp...*{/size}"
        m "Oh, yes..."
        $ end_u_2_pic =  "01_hp/17_ending/36.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "...................................................."
        m "Well, I think that was the last of it--"
        with hpunch
        g4 "{size=+5}Huh?!!{/size}"
        show screen blkfade
        with d3
        stop music fadeout 1.0
        g4 "Hey, what are you--"
        ">Hermione gets up abruptly and runs off without saying a word..."
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "Hm...?"
        m "Oh, that's right... The coronation thing..."
        m "............."
        #m "Still need to talk to her though..."
        ">..............{w}..................{w}...................."
    
    pause 1
    
    
    if public_whore_ending: #Students talking. Ending "Public whore".
        $ s_head_xpos = 330 # x = 330,
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        call sna_head("Miss Granger...?","snape_03")
        call sna_head("You decided to show up after all?","snape_04")
        $ s_sprite = "01_hp/13_characters/snape/main/.png"
        call sna_head("What an unpleasant surprise...","snape_03")
        #her "Professor..."
        call her_head("Professor...","body_162")
        call sna_head("Well, go ahead then...","snape_10")
        call sna_head("Here is the tiara...")
        call sna_head("And the stage is yours...")
        $ tiara = True #Tiara is displayed.
        #her "Thank you, professor."
        call her_head("Thank you, professor.","body_160")
        pause.7
        
        $ end_u_1_pic =  "01_hp/17_ending/108.png" #<---- SCREEN
        hide screen blkfade
        with d7
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        show screen ctc
        pause
        hide screen ctc
        
        her "..............."
        her ".................................."
        $ end_u_2_pic =  "01_hp/17_ending/109.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        her "Hello, everyone!"
        her "Thank you for making me your ball queen for two years in a row!"
        
        show screen blktone
        show screen bld1
        with d3
        m "!!!"
        m "Her hairdo looks perfect!"
        m "I suppose I was wrong and--"
        g4 "Nope, there it is!"
        g4 "Dripping down behind her ear!"
        hide screen blktone
        hide screen bld1
        with d3
        
        $ end_u_1_pic =  "01_hp/17_ending/110.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I would like to dedicate my speech to every girl in this room..."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "What was she thinking pulling a stunt like that?"
        hide screen blktone
        hide screen bld1
        with d3
        
        $ end_u_2_pic =  "01_hp/17_ending/111.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I shall not go as far as to say that I do not deserve this honor..."
        her "Because I think I do..."
        $ end_u_1_pic =  "01_hp/17_ending/112.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "But I am still very grateful to stand here before all of you tonight..."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(huh?)"
        mal "(What's that stuff on her forehead you wager?)"
        mal2 "(Sweat...?)"
        mal "(Hm... Probably..)"
        hide screen blktone
        hide screen bld1
        with d3
        $ end_u_2_pic =  "01_hp/17_ending/113.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I would especially like to thank our esteemed teachers for their hard work."
        
        show screen blktone
        show screen bld1
        with d3
        g4 "Doesn't she feel it by now?!"
        g4 "She'd better cut her speech short!"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Hogwarts truly did become a second home for all of us..."
        $ end_u_1_pic =  "01_hp/17_ending/114.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I know that I speak for every student in this building when I say this."
        
        show screen blktone
        show screen bld1
        with d3
        mal "(That doesn't look like sweat though...)"
        mal2 "(Yeah...)"
        mal2 "(Some weird goo seeping out of her hair...)"
        fem "(Are you guys really {size=+5}that{/size} dim?)"
        mal "(What?)"
        fem "(That's cum... obviously.)"
        mal2 "(What? Bullshit, girl!)"
        fem "(I think I know cum when I see it.)"
        mal "(I bet you do. *Chuckle*)"
        fem "(Whatever. Just take a better look...)"
        fem "(She must've let some guy bury his cock in her hairdo and pump it full of semen.)"
        mal "(Hm... Hair fucking then? Is it a thing now?)"
        mal2 "(You girls do the craziest things.)"
        fem "(*Humph!* Not all of us are sluts, you know.)"
        mal "(Unfortunately not...)"
        fem "(\"Unfortunately\"?!)"
        fem "(Tsk! You, men are so clueless about everything!)"
        fem "(You could never build a meaningful relationship with a slut!)"
        mal "(What's a \"meaningful relationship\"?)"
        fem "(It's when your girl is also your best friend.)"
        mal "(Oh, I don't need {size=+5}that{/size}!)"
        mal "(I already have a best friend, this ugly bugger right here.)"
        mal2 "(Dito, mate!)"
        mal "(But I sure could use a slut in my life!)"
        mal2 "(Dito, mate!)"
        fem "(...you guys are...)"
        fem "Such Idiots!!!"
        hide screen blktone
        hide screen bld1
        with d3
        $ end_u_2_pic =  "01_hp/17_ending/115.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I remember when I was just a little girl..."
        
        show screen blktone
        show screen bld1
        with d3
        m "Huh?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Frightened of my power... confused..."
        
        show screen blktone
        show screen bld1
        with d3
        m "Hm..."
        m "There... She did it again..."
        hide screen blktone
        hide screen bld1
        with d3
        
        her "Who knows what would have become of me if not for Hogwarts!"
        show screen blktone
        show screen bld1
        with d3
        m "And again..."
        m "Why does she keep on jerking her shoulder in that awkward manner...?"
        hide screen blktone
        hide screen bld1
        with d3
        
        her "I am so lucky to be a student here..."
        show screen ctc
        pause
        stop music
        #$ renpy.play('sounds/scratch.wav')
        hide screen ctc
        $ end_u_1_pic =  "01_hp/17_ending/116.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        
        hide screen ctc
        # TIT BARES
        # MUSIC STOPS
        
        show screen blktone
        show screen bld1
        with hpunch
        g4 "!!!"
        #play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        call sna_head("!!!","snape_11")
        hide screen blktone
        hide screen bld1
        show screen ctc
        pause
        hide screen ctc
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        her "Thank you, everyone..."
        $ end_u_2_pic =  "01_hp/17_ending/117.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Let me say this again..."
        $ end_u_1_pic =  "01_hp/17_ending/118.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Thank you for making me your ball queen this year..."
        show screen ctc
        pause
        hide screen ctc
        # SEX MUSIC STARTS TO PLAY
        
        show screen blktone
        with d7
        #play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        mal "(Am I hallucinating?)"
        mal2 "(No, it's really happening... I see it too...)"
        mal "(Hermione... Granger's... tit...)"
        mal "(Major wardrobe malfunction, mate!)"
        fem "(Oh no! Poor thing! We must let her know!)"
        mal "(Don't you dare to take this away from us, girl!)"
        fem "(But...!!)"
        hide screen blktone
        with d7
        
        show screen ctc
        pause
        hide screen ctc
        her "And most of all I am thankful to my parents..."
        her "The people who raised me..."
        her "Mommy... Daddy..."
        $ end_u_2_pic =  "01_hp/17_ending/119.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I wish you could see how much Hogwarts changed me..."
        her "I wish you could see your little girl right now..."
        her "{size=-5}Ah...{/size}{image=textheart}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen blktone
        with d7
        g4 "The whore is blushing! She is well aware of what's going on!"
        g4 "Nasty slut!"
        g4 "(She planned the whole thing??!)"
        m "(By the great desert sands... What have I unleashed!?)"
        hide screen blktone
        with d7
        
        $ end_u_1_pic =  "01_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "..............................."
        her ".................."
        show screen ctc
        pause
        hide screen ctc
        
        show screen blktone
        with d7
        mal "(Now she just sorta stands there...)"
        mal2 "(Giving us a better look...?)"
        mal "(Do You think she is aware of her tit being visible at all?)"
        fem "(What a shameless display...)"
        fem "(And to think that I almost felt sorry for the slut...)"
        fem "........................"
        with hpunch
        fem "{size=+7}Cover up, you shameless slut!!!{/size}"
        mal "(!!!)"
        mal2 "(Have you lost your mind, yelling like that?!)"
        with hpunch
        fem "{size=+7}Gryffindor whore!!!{/size}"
        hide screen blktone
        with d7
        
        $ end_u_2_pic =  "01_hp/17_ending/121.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=-3}Ah...{/size}{image=textheart}"
        her "...............................a-ha...{image=textheart}{image=textheart}{image=textheart}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        cr1 "Show us both of them, Hermione!"
        cr2 "Look! Her face is all covered in cum!"
        cr1 "Have you no shame anymore, Hermione?!"
        cr2 "Cover up, you slut!"
        hide screen bld1
        with d7
        
        $ end_u_1_pic =  "01_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Oh... That's right..."
        her "I almost forgot..."
        $ end_u_2_pic =  "01_hp/17_ending/123.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "{size=+5}Go Gryffindor!{/size}"
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        "*Wild whisting and cheering!*"
        $ end_u_1_pic =  "01_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "......................................"
        her ".........................................................."
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        $ s_sprite = "01_hp/13_characters/snape/main/snape_12.png"
        show screen s_head2
        sna "Quiet down everyone!"
        sna "As for you, miss Granger..."
        sna "I think that's enough."
        sna "Cover up and get off the stage... Go..."
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        
        $ end_u_2_pic =  "01_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "\"Cover up\", sir?"
        $ end_u_1_pic =  "01_hp/17_ending/119.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Oh? What is this? One of my breasts is completely naked..."
        $ end_u_2_pic =  "01_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "How embarrassing..."
        $ end_u_1_pic =  "01_hp/17_ending/121.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ah...{image=textheart}{image=textheart}{image=textheart}"
        show screen ctc
        pause
        hide screen ctc
        
        show screen bld1
        with d7
        cr1 "Whore!"
        cr2 "Gryffindor slut!"
        cr1 "I love you, Hermione!"
        cr2 "Gryffindor rules!!!"
        
        $ s_sprite = "01_hp/13_characters/snape/main/snape_18.png"
        show screen s_head2
        sna "Miss Granger, I said that's enough!"
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        #her "As you say, professor..."
        her "As you say, [genie_name]..."
        show screen bld1
        with d7
        $ s_sprite = "01_hp/13_characters/snape/main/snape_12.png"
        show screen s_head2
        sna "And wipe your face, girl. You look repulsive."
        hide screen s_head2
        pause.1
        hide screen bld1
        $ end_u_2_pic =  "01_hp/17_ending/122.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Oh, this? This is just my--"
        show screen bld1
        with d7
        $ s_sprite = "01_hp/13_characters/snape/main/snape_18.png"
        show screen s_head2
        sna "Don't care! Get off the stage already!"
        sna "Now!"
        hide screen s_head2
        pause.1
        hide screen bld1
        with d7
        $ end_u_1_pic =  "01_hp/17_ending/120.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Wild whisting and cheering persists as Hermione descends off the stage..."
        pause 1
        stop music fadeout 3.0
        ">.......................{w}....................{w}......................."
        
        # BACK AT THE ALCOVE (BLACK SCREEN STILL).
        $ end_u_2_pic =  "01_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        hide screen blkfade
        with d7
        show screen bld1
        with d5
        show screen ctc
        pause
        hide screen ctc
        
        $ her_head_ypos = her_head_tits
        call her_head("[genie_name]...","body_165")
        #her "Professor Dumbledore..."
        call her_head("There was something you wanted to discuss with me?")
        g4 "Not right now, whore!"
        show screen blkfade
        with d5
        call her_head("Sir?!","body_164")
        g4 "I want to fuck you so badly! Come over here!"
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        call her_head("Of course, sir...","body_181")
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        pause.5
        g4 "{size=+7}OH YEEEES!{/size}"
        
        
        $ end_u_1_pic =  "01_hp/17_ending/46.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        hide screen blkfade
        hide screen bld1
        with d7
        
        show screen ctc
        pause
        hide screen ctc
        
        
        her "Aaah!!!"
        g4 "Your acceptance speech was a disgrace, girl!"
        $ end_u_2_pic =  "01_hp/17_ending/50.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "I thought it went rather well..."
        g4 "Showing off your tits like that?!"
        $ end_u_1_pic =  "01_hp/17_ending/56.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "Only one... ah..."
        g4 "What?"
        her "Only one tit, sir..."
        g4 "Whatever happened to that idealistic and self righteous girl you once were?!"
        $ end_u_2_pic =  "01_hp/17_ending/59.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "You fucked her out of me, sir!"
        g4 "You're damn right I did!"
        $ end_u_1_pic =  "01_hp/17_ending/124.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d2                                                                        #<---- SCREEN
        her "You fucked her out of me with your enormous cock, sir!"
        g4 "Argh! You whore!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        $ end_u_2_pic =  "01_hp/17_ending/58.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Ah!!!"
        g4 "Quiet, whore! Someone will hear you!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        
        #her "Ah! Professor!"
        her "Ah! [genie_name]!"
        g4 "I said, be quiet!"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        # SLAP!
        $ end_u_1_pic =  "01_hp/17_ending/55.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                       #<---- SCREEN
        #her "Ah! Professor!"
        her "Ah! [genie_name]!"
        $ end_u_2_pic =  "01_hp/17_ending/124.png" #<---- SCREEN
        show screen end_u_2                                               #<---- SCREEN
        with d5                                                                         #<---- SCREEN
        her "Yes! Fuck me harder!"
        m "Are you raising your voice on purpose, whore?"
        g4 "Do you want to get caught like this?"
        g4 "On your professor's cock?"
        $ end_u_1_pic =  "01_hp/17_ending/125.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah! Maybe..."
        $ end_u_2_pic =  "01_hp/17_ending/124.png" #<---- SCREEN
        show screen end_u_2                                               #<---- SCREEN
        with d5                                                                         #<---- SCREEN
        her "Call me a \"mudblood\", sir!"
        m "What?"
        $ end_u_1_pic =  "01_hp/17_ending/51.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Call me a \"mudblood\", please!"
        m "A \"mudblood\"?"
        $ end_u_2_pic =  "01_hp/17_ending/58.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah! Yes! Yes! I am a mudblood whore!"
        g4 "Whatever!"
        
        #SLAP
        #SLAP
        #SLAP
        #SLAP
        
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.5
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.4
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.2
        hide screen white
        with hpunch
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch

        
        $ end_u_1_pic =  "01_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        her "AAAAAAAAAAAAAAAAH!"
        her "Yes!!! Yeeees! Ah!"
        $ end_u_2_pic =  "01_hp/17_ending/63.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        #her "Fuck me professor! Fuck me harder!!!"
        her "Fuck me [genie_name]! Fuck me harder!!!"
        g4 "Grht! Harder than this, whore?!"
        g4 "!!!"
        g4 "Crap!  Someone's coming!"
        $ end_u_1_pic =  "01_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "No, sir, not yet. But if you keep spanking me--"
        g4 "No, whore! A bunch of students are coming this way!"
        $ end_u_2_pic =  "01_hp/17_ending/127.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "What?!"
        
        # STUDENTS
        
        sly1 "Well, well, well... What have we here?"
        $ end_u_1_pic =  "01_hp/17_ending/126.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        show screen ctc
        pause
        hide screen ctc
        her "!!!"
        sly1 "I thought it could be you, \"gryffindor\" filth..."
        sly1 "Moaning like a whore..."
        sly1 "Getting fucked by... Oh..."
        with hpunch
        sly1 "Professor Dumbledore!?"
        m "Hello, boys..."
        her ".........................."
        sly1 "Oh... Em... We didn't know..."
        sly1 "We'll be leaving now..."
        m "What? Don't be silly, boys."
        m "You are more than welcome to stay."
        sly1 "We are?"
        $ end_u_2_pic =  "01_hp/17_ending/128.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "What?!"
        m "Of course."
        $ end_u_1_pic =  "01_hp/17_ending/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        #her "Professor!!!?"
        her "[genie_name]!!!?"
        m "The girl's frontal area is completely at your disposal."
        $ end_u_2_pic =  "01_hp/17_ending/130.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        #her "Professor! No!"
        her "[genie_name]! No!"
        m "What's wrong, slut?"
        $ end_u_1_pic =  "01_hp/17_ending/129.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Sir, don't call me that in front of them, please..."
        m "What's the matter? Why are you Acting shy all a of sudden?"
        her "Can't you see that they are from \"Slytherin\"?!"
        m "So what?"
        her "Our two houses... we have a history."
        m "Oh..."
        m "Well, then you shall become the bridge between \"slytherin\" and \"gryffindor\"."
        m "Hermione Granger, the ambassador of peace!"
        $ end_u_2_pic =  "01_hp/17_ending/130.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "No, sir! I refuse!"
        her "And stop moving your hips while we're talking, sir!"
        m "Boys, what is taking you so long?"
        m "I said, the whore is yours!"
        #her "Professor Dumbled--"
        her "[genie_name]--"
        sly1 "Shut up, filth!"
        
        # FACE SPIT
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "01_hp/17_ending/132.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_1_pic =  "01_hp/17_ending/133.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!"
        m "There you go!"
        
        sly2 "Ha-ha-ha! Nice one! Look at her stupid face!"
        $ end_u_2_pic =  "01_hp/17_ending/134.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "You... You...!"
        sly1 "We really enjoyed your speech, \"gryffindor slut\"."
        sly2 "Yeah... Sure did..."
        her "That wasn't meant for you, you slytherin scum!"
        sly1 "Wasn't meant for us? What are you, stupid?"
        sly1 "You bared your filthy, muggle-born flesh on stage! In front of the entire school!"
        sly1 "{size=+7}Of course it was for everyone, you dumb cunt!{/size}"
        
        $ end_u_1_pic =  "01_hp/17_ending/135.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN

        her "Sir! Stop fucking me!"
        m "Huh? You mean, like this?"
        with hpunch
        pause.3
        #her "Ah-aha! No, professor, stop it!"
        her "Ah-aha! No, [genie_name], stop it!"
        m "Stop? I think I will fuck you harder instead!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        $ end_u_2_pic =  "01_hp/17_ending/133.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Aahah!!!"
        sly1 "Yes... You are ours now, slut!"
        
        show screen ctc
        pause
        hide screen ctc
        
        # DICKS OUT
        $ end_u_1_pic =  "01_hp/17_ending/136.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "What?! What are you doing?!"
        $ end_u_2_pic =  "01_hp/17_ending/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Put your filthy dicks away immediately!"
        with hpunch
        pause.3
        $ end_u_1_pic =  "01_hp/17_ending/138.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah... Aha..."
        sly1 "Yes... I wanted to do this for quite some time now..."
        #her "Professor!"
        her "[genie_name]!"
        m "Huh? Oh, don't you mind me girl."
        m "Imagine that I'm not even here..."
        
        # SPIT!
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_1_pic =  "01_hp/17_ending/139.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_2_pic =  "01_hp/17_ending/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Stop it! Stop spitting in my face, you bastards!"
        sly1 "Make us, whore!"
        her "I am warning--"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "01_hp/17_ending/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc
        
        # SPIT!
        $ end_u_1_pic =  "01_hp/17_ending/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Gulp!*{/size}"
        sly2 "Ha-ha-ha! Right in the mouth! Good one, mate!"
        sly1 "And she swallowed it too!"
        $ end_u_2_pic =  "01_hp/17_ending/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "That's was an accident!"
        sly1 "Was it? Let's see."
        her "Huh?"
        
        # SPIT!
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "01_hp/17_ending/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc

        
        # SPIT!
        $ end_u_1_pic =  "01_hp/17_ending/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*GULP!*{/size}"
        
        

        sly2 "She did it agagin!"
        $ end_u_2_pic =  "01_hp/17_ending/140.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "That's because I didn't expect it... That's just a reflex!"
        sly1 "That's one hot reflex!"
        g4 "Oh... yes..."
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "Ah... Ah-aha..."
        her "You will pay for this, you spineless slytheri--"
        sly1 "Shut it, mudblood!"
        $ end_u_1_pic =  "01_hp/17_ending/143.png" #<---- SCREEN
        show screen end_u_1                                                #<---- SCREEN
        with hpunch                                                                        #<---- SCREEN
        
        # DICK IN MOUTH
        
        show screen ctc
        pause
        hide screen ctc
        
        her "!!!........................................................."
        sly2 "Cool! I'm next!"
        her "*Gulp!*"
        sly1 "Suck my cock, bitch! Suck it I said!"
        m "Do what the boy tells you, girl."
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        
        # SLAP!
        
        m "Come on!"
        $ end_u_2_pic =  "01_hp/17_ending/144.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp...*"
        sly1 "She's doing it! Hermione Granger sucking me off, lads!"
        sly2 "Awesome! Can't wait to give it a go myself!"
        sly1 "Oh... wow... she's good..."
        her "*Slurp!* *Slurp!* *Gulp!*"
        sly1 "Oh yes... Yes..."
        sly1 "Oh... You are so good at this, whore!"
        sly1 "It's... I..."
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/145.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*gobble?!?*{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"
        

        $ end_u_2_pic =  "01_hp/17_ending/146.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        # CUMMING
        
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        her "*{size=+3}Gulp-gulp-gulp...*{/size}"
        her "*Gulp-gulp-gulp...*"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        $ end_u_1_pic =  "01_hp/17_ending/147.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Gu-aha..."
        her "Is this all you got? Pathetic!"
        sly2 "Oh... Shut up whore... You sucked me dry..."
        $ end_u_2_pic =  "01_hp/17_ending/137.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Come on! Who's next?!"
        sly2 "Me! I'm next!"
        $ end_u_1_pic =  "01_hp/17_ending/148.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch                                                                       #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_2_pic =  "01_hp/17_ending/149.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Oh... Yes... Yes!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly2 "Oh! Her mouth is so slippery and warm!"
        her "*Slurp!* *Slurp!* *Slurp!*"
        g4 "Yes! Suck that cock, you whore!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "*Gulp!* Gulp!* *Slurp!*"
        sly2 "I don't know... gh... How much longer..."
        sly2 "...I could keep up like that."
        her "*Slurp--Slurp-Slurp-slurp!*"
        her "*Slurp-Gulp-Slurp-Slurp-gulp!!!*"
        sly2 "Oh, man... Oh man..."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp!!*"
        sly2 "I... I..."
        sly2 "..................."
        her "*Slurp-Slurp-Slurp-Slurp-Slurp!!*"
        with hpunch
        sly2 "{size=+7}I'm cummiiiiiiiiing!{/size}"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_2_pic =  "01_hp/17_ending/150.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*gobble?!?*{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/149.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        her "{size=+3}*Gulp-gulp...*{/size}"
        her "*Gulp....."
        sly2 "Ah... my cock..."
        $ end_u_2_pic =  "01_hp/17_ending/152.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Gu-aha..."
        $ end_u_1_pic =  "01_hp/17_ending/151.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Next! Come on! Is this all you got?"
        sly1 "I'm next, mudblood!"
        $ end_u_2_pic =  "01_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=-5}Ah... Don't call me that, you bastard...{/size}{image=textheart}"
        sly1 "Gonna fuck your face real good, whore!"
        sly1 "And after I fill your mouth with my cum, you're gonna thank me!"
        sly1 "Aren't you, mudblood whore?"
        $ end_u_1_pic =  "01_hp/17_ending/153.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Fuck you!"
        
        # Spit!
        
                
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        $ end_u_2_pic =  "01_hp/17_ending/141.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        pause.2
        hide screen white
        with hpunch
        

        
        show screen ctc
        pause
        hide screen ctc

        
        # SPIT!
        $ end_u_1_pic =  "01_hp/17_ending/142.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}*GULP!*{/size}"
        
        
        
        

        sly1 "That's what I thought!"
        $ end_u_2_pic =  "01_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "You worthless...\"slythe-"
        $ end_u_1_pic =  "01_hp/17_ending/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "!!?"
        $ end_u_2_pic =  "01_hp/17_ending/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly1 "Yes! Yes, you mudblood filth! Suck my cock! Suck it!"
        m "This is quite extraordinary..."
        sly1 "Sir?"
        m "It's just..."
        m "Her pussy..."
        $ end_u_1_pic =  "01_hp/17_ending/155.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "*Slurp?*"
        m "It's tightens every time you call the girl a \"mudblood\"..."
        m "Try calling her that again, boy."
        sly1 "Gladly, sir."
        $ end_u_2_pic =  "01_hp/17_ending/156.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "*Slurp!* *Slurp!* *Slurp!*"
        sly1 "Yes, whore! I love fucking your \"mudblood\" face!"
        sly1 "And you're loving every moment of this, aren't you?"
        sly1 "Aren't you, mudblood?"
        her "*Slurp!* *Slurp!* *Gulp!*"
        m "Yup... Every time you say that..."
        m "Huh?"
        m "What is this? Her legs are shaking!"
        m "Are you cumming, girl?"
        $ end_u_1_pic =  "01_hp/17_ending/157.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                   #<---- SCREEN
        her "..............................................."
        m "I think you are!"
        m "Come on, boy let's speed this thing up a little!"
        m "Let's fuck her from the both ends while she is orgasming like a dirty slut!"
        sly1 "Of course, sir."
        sly1 "Take, this, \"mudblood\" whore!"
        with vpunch
        pause.3
        with vpunch
        pause.3
        with vpunch
        pause.3
        g4 "And this!!!"
        with hpunch
        pause.3
        with hpunch
        pause.3
        with hpunch
        pause.3
        her "{size=+7}!!!!!!!!{/size}"
        g4 "Yes! Her pussy is flooded with juice!"
        sly1 "Agh! Her mouth as well, sir."
        sly1 "I don't know how much longer I... oh..."
        sly1 "Argh!"
        sly1 "{size=+3}Take this, whore!{/size}"
        
        
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/159.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        her "{size=+7}*gobble?!?*{/size}"
        sly1 "{size=+5}Yes, yes! Swallow it all!!!{/size}"
        

        $ end_u_2_pic =  "01_hp/17_ending/160.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        # CUMMING
        
        her "{size=+5}*Gulp-gulp-gulp-gulp!*{/size}"
        her "*{size=+3}Gulp-gulp-gulp...*{/size}"
        her "*Gulp-gulp-gulp...*"
        her "{size=-3}*Gulp* *Gulp*{/size}"
        her "{size=-5}*Gulp*..................{/size}"
        her "........................................"
        her "....................."
        $ end_u_1_pic =  "01_hp/17_ending/154.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        her "Gu-aha..."
        sly2 "You drained my balls, bitch..."
        m "Alright, boys! Let's bring this little party to a worthy conclusion."
        her "{size=+7}I'm cumming!{/size}"
        m "Yeah, whatever, whore."
        m "So, rest of you boys, you just jerk off in her face now, alright?"
        sly1 "Of course, sir."
        sly2 "Yes, sir!"
        m "Yes, just plaster her face with cum. She loves that shit!"
        $ end_u_2_pic =  "01_hp/17_ending/161.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+3}No! I am already cumming... Stop!{/size}"
        sly1 "Heh... Hermione Granger... What a whore!"
        sly2 "Yeah! Nothing but a mudblood cunt!"
        her "{size=+9}AAAAAH!!!!!{/size}"
        her "{size=+3}Yes! I'm a whore! I'm a whore!{/size}"
        sly1 "She even admits it!"
        sly2 "I don't think I can last much longer!"
        sly1 "Me neither!"
        sly2 "ARGH!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/162.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc

        
        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        her "{size=+3}My face!!{/size}"
        sly1 "Take this, whore!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/163.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc
        
        her "{size=+5}AAAAAAAAAAAAH!{/size}"
        sly2 "Argh! Here! Me too!"
        
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/164.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc
        
        $ end_u_2_pic =  "01_hp/17_ending/165.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d7                                                                        #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        her "{size=+4}I'm cumming!{/size}"
        m "Well, don't mind if I do!"
        $ end_u_1_pic =  "01_hp/17_ending/166.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        #her "{size=+3}No professor, I............!{/size}"
        her "{size=+3}No [genie_name], I............!{/size}"
        g4 "Argh!"
        
        show screen white 
        pause.1
        hide screen white
        pause.2
        show screen white 
        pause .1
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/167.png" #<---- SCREEN
        show screen end_u_1                                             #<---- SCREEN
        with hpunch
        
        show screen ctc
        pause
        hide screen ctc
        
        
        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        $ end_u_2_pic =  "01_hp/17_ending/168.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}No! My face! My pussy! Ah! I can't stop cumming!!!{/size}"
        sly1 "What a slut!"
        sly2 "Whore!"
        sly1 "Mudblood!"
        her "{size=+8}AAAAAAAAAAAAH!{/size}"
        
        $ renpy.play('sounds/spit.mp3') #Sound of spiting. 
        show screen white
        pause.3
        $ end_u_1_pic =  "01_hp/17_ending/169.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        hide screen white
        with vpunch
        show screen ctc
        pause
        hide screen ctc
        $ end_u_2_pic =  "01_hp/17_ending/170.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+8}*Gulp!*{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/168.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        #with d3                                                                        #<---- SCREEN
        her "{size=+8}I'll go insane!{/size}"
        
        # SPIT!
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen white
        with d9
        pause 1
        
        
        # WHITE FADE
        
        ">.............{w}......................{w}....................."
        
        # Character sprites.
        
        m "Well, thank you for your cooperation, boys."
        sly1 "Of course, sir, professor Dumbledore."
        sly2 "Glad to be of help, sir."
        sly1 "Thank you, professor."
        sly2 "Alright, let's go back to the ball?"
        sly1 "Yeah, let's go!"
        sly2 "Bye, mudblood whore!"
        sly1 "Yeah, thank you for being such a slut!"
        call her_head("..........................","body_176")
        $ renpy.play('sounds/footsteps.mp3') #Walking away sound
        # Walking away sound...."
        
        $ end_u_1_pic =  "01_hp/17_ending/02.png" #<---- SCREEN
        
        pause 2
        
        hide screen white
        with d9
        
        sly1 "{size=-4}(Man, professor Dumbledore sure is one cool dude.){/size}"
        sly2 "{size=-4}(Yeah... Who would have thought.){/size}"
        sly1 "{size=-4}(True. I can't help but respect the man...){/size}"
        m "Aw... What nice boys..."
        sly2 "{size=-4}(Yeah... I hope I will be as agile as he is when I am that ancient.){/size}"
        g4 "I'm not ancient, you young punks!"
        m "Although I suppose in a way I am..."
        
        call her_head("..........................","body_176")
        m "Whore! Why so quiet?"
        call her_head("I...","body_177")
        call her_head("I am... not sure...")
        call her_head("What...? What is.......","body_176")
        m "Come on, girl. Pull yourself together!"
        call her_head("I... I... What?","body_178")
        call her_head("I don't understand... I...")
        m "Hm..."
#        m "Doesn't look like you are in any condition for serious talks..."
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "01_hp/13_hermione_main/body_178.png" # HERMIONE
#        her "Serious talks?"
#        hide screen h_head2
#        m "Well, so be it, then."
#        m "I wrote you a letter."
#        show screen h_head2                                                             # HERMIONE
#        $ h_body = "01_hp/13_hermione_main/body_177.png" # HERMIONE
#        her "A letter...? What...? I...."
#        hide screen h_head2
#        m "Yes! Concentrate for a second, would you?"
#        m "I wrote you a letter. It should explain a couple of things."
        m "I will be leaving now."
        call her_head("Leaving...?","body_176")
        m "Yes. Maybe you should too..."
        m "Go clean yourself up and rest or something."
        call her_head("But I can't leave... No... I must...","body_178")
        call her_head("The formal dance... I must...")
        m "A dance? You can't dance in this condition."
        call her_head("No! I am the ball queen! I must....","body_176")
        m "Well, suit yourself."
        m "I'm leaving..."
        call her_head("Good bye... sir...","body_176")
        m "............."
        m "Farewell, girl."
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        $ end_u_2_pic =  "01_hp/17_ending/90.png" #<---- SCREEN
        show screen end_u_2                                             #<---- SCREEN
        with d9                                                                        #<---- SCREEN
        pause.5
        hide screen blkfade
        with d5
        
        show screen ctc
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 # BALL THEME 02.
        pause
        hide screen ctc
        
        m "Hm..."
        m "Maybe I should stay and watch Hermione's post-multiple-orgasm dancing?"
        m "No... This ball is almost over. This is my only chance to sneak out unnoticed."
        
        show screen ctc
        pause
        hide screen ctc
        
        show screen blkfade 
        with d7
        pause.5
    
    else: # Ending "Your whore".
        $ s_head_xpos = 330 # x = 330,
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.
        $ s_sprite = "01_hp/13_characters/snape/main/snape_03.png"
        show screen s_head2
        sna "Miss Granger...?"
        $ s_sprite = "01_hp/13_characters/snape/main/snape_04.png"
        sna2 "You decided to show up after all? What an unpleasant surprise..."
        call her_head("...............................","body_169")
        $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"
        show screen s_head2
        sna "What happened to your face, girl?"
        call her_head(".......................................","body_170")
        $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"
        show screen s_head2
        sna "Hm... Well, go ahead then..."
        sna "Here is the tiara..."
        sna "And the stage is yours..."
        hide screen s_head2
        pause.7
        
        
        
        $ end_u_2_pic =  "01_hp/17_ending/37.png" #<---- SCREEN
        hide screen blkfade
        with d7
        
        $ renpy.play('sounds/applause01.ogg')
        show screen ctc
        pause
        hide screen ctc
        
        her "..............."
        her ".................................."
        her ".........................................................................."
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        $ end_u_1_pic =  "01_hp/17_ending/38.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Ah-a.........................................."
        show screen bld1
        with d5
        m "Is that...?"
        m "are Leftovers of my cum still in her mouth?"
        g4 "What the hell is she doing?"
        hide screen bld1
        with d5
        
        $ end_u_2_pic =  "01_hp/17_ending/39.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "...................................."
        her "Helwo eweruone..." #Misspelled on purpose.
        $ end_u_1_pic =  "01_hp/17_ending/40.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Fenk you for being heah today..." #Misspelled on purpose.
        show screen bld1
        with d5
        m "I can barely understand a word she is saying..."
        hide screen bld1
        with d5
        her "Fifst of all I would like foo fenk Profeffor Dumblefore..." #Misspelled on purpose.
        show screen bld1
        with d3
        m "Me?"
        hide screen bld1
        with d3
        her "................"
        $ end_u_2_pic =  "01_hp/17_ending/37.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        stop music fadeout 1.0
        her ".................................................."
        show screen ctc
        pause
        hide screen ctc
        $ end_u_1_pic =  "01_hp/17_ending/41.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        $ renpy.play('sounds/gulp.mp3') #Sound of gulping down a liqui
        her "{size=+5}*GULP!!!*{/size}"
        $ end_u_2_pic =  "01_hp/17_ending/42.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Gua-ha..."
        #her "Thank you, professor."
        her "Thank you, [genie_name]."
        show screen bld1
        with d3
        with hpunch
        g4 "YOU WHORE!!!"
        g4 "When did you get this nasty!"
        #m "Now I want to fuck you... Dammit."
        hide screen bld1
        with d3
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        $ end_u_1_pic =  "01_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "I would also like to thank my parents..."
        her "Then I would like to thank my fellow students!"
        show screen bld1
        with d3
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">Loud cheering and whistling..."
        hide screen bld1
        with d3
        her "And the teachers of course..."
        $ end_u_2_pic =  "01_hp/17_ending/44.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        show screen bld1
        with d3
        ">A few rather feeble applauses..."
        hide screen bld1
        with d3
        
        show screen ctc
        pause
        hide screen ctc
        show screen blktone
        with d5
        
        mal "(So it's Hermione Granger again this year...)"
        fem "(Tsk... Why am I not surprised?)"
        mal2 "(Maybe because she deserves it?)"
        mal "(Yeah! Stop hating on Hermione!)"
        fem "(Tch... Whatever.)"
        mal "(By the way, when Hermione came upstage...)"
        mal2 "(Yeah, there was something in her mouth. I noticed it too.)"
        fem "(I bet it was someone's cum!)"
        mal "(WHAT!!?)"
        mal2 "(Get your head out of the gutter, girl!)"
        fem "(Why not?)"
        fem "(Everyone knows she is sleeping with Professor Dumbledore!)"
        mal "(No, not your gossips again.)"
        mal2 "(Wait, I want to hear this one. Tell us more.)"
        fem "(What is there to tell?)"
        fem "(Hermione Granger is a whore. She enjoys sucking cocks....)"
        fem "(Yes, she loves to suck cocks but she loves sperm even more!)"
        mal "(....)"
        fem "(She is a sperm addict! She must swallow half a cup of sperm every day...)"
        fem "(Because if she doesn't she goes into a sex-craze...)"
        mal2 "(.....)"
        fem "(And when that happenes she cannot control herself and will gladly sleep with the first man she sees.)"
        mal "(.............)"
        mal2 "(.....................)"
        fem "(Hm? Why are you staring at me like that?)"
        mal "(What? We are not staring.)"
        mal2 "(Yes, keep talking. You are good at this!)"
        fem "(Good at what?!)"
        fem "(Wait a second, are you guys getting off on this?)"
        mal "(Heh... Look at the crow calling the raven black!)"
        fem "(What do you mean?)"
        mal2 "(You are blushing like crazy, girl! And your eyes are all misty!)"
        mal "(Yeah! You enjoy this as much as we do!)"
        fem "(!!!?)"
        fem "You guys are idiots!"
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        mal "(What? What did I say?)"
        mal2 "(Who knows, bro? Bitches be crazy...)"
        mal "(They do be crazy...)"


        
        hide screen blktone
        with d5
        $ end_u_1_pic =  "01_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "Thank you, everyone for being such a big help in organizing today's event."
        her "And thank you for choosing me as your queen again this year..."
        $ end_u_1_pic =  "01_hp/17_ending/45.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "What a pleasant but completely unexpected surprise...!"
        her "And one more thing..."
        $ end_u_2_pic =  "01_hp/17_ending/43.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        her "{size=+5}Go gryffindor!{/size}"
        show screen bld1
        with d5
        $ renpy.play('sounds/applause01.ogg') # APPLAUSE
        ">The crowd explodes with loud cheers and whistles interspersed by occasional booing..."
        hide screen bld1
        with d5
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d7
        pause.7
        stop music fadeout 1.0
        m "Great speech..."
        m "Very arousing... Ehm, I mean inspiring."
        $ tiara = True #Tiara is displayed.
        call her_head("Thank you, sir.","body_165")   
        m "Swallowing my load in front of the entire school?"
        g9 "Very nice touch."
        call her_head("........................................................","body_168")                     
        
        play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        $ end_u_2_pic =  "01_hp/17_ending/02.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        with d3
        show screen bld1 
        with d3
        m "Alright, girl. Let's have that talk now..." 
        call her_head("....................","body_162")
        m "There is something I need to tell you..."
        m "Not sure where to start though..."
        m "........................................"
        m "Well, first of all I am--"
        call her_head("Sir, I think I know exactly what you are about to say.","body_163")
        m "You do?"
        call her_head("Of course.","body_163")
        call her_head("One hasty blowjob is not nearly enough to repay my debt to you, am I right?","body_164")
        m "What? No, that's not what I--"
        call her_head("It's fine, sir. Really.","body_164")
        call her_head("Let me just pull my panties down a little...","body_165")
        g4 "Damn you girl! Will you let me finish!?"
        call her_head("Of course sir...","body_164")
        m "Huh?"
        call her_head("Just make sure you don't hit my dress, alright?","body_167")
        g4 "*Low growl!*"
        g4 "Come here, whore!"
        g4 "Suppose I might as well fuck you one last time!"
        call her_head("(One last time?)","body_162")
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade 
        with d7
        
        # INSERTION
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        $ her_head_ypos = her_head_only
        call her_head("{size=+5}Ahh!!!{/size}","body_172")            
        g4 "Oh, yes!"
        
        $ end_u_2_pic =  "01_hp/17_ending/46.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d3                                                                        #<---- SCREEN
        hide screen blkfade 
        hide screen bld1
        with d7
        show screen ctc
        pause
        hide screen ctc
        her "Ah-ah..."
        m "Hm? Your pussy..."
        m "It's dripping wet, girl."
        $ end_u_1_pic =  "01_hp/17_ending/47.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah...{image=textheart} It is, sir?"
        her "That's probably from before..."
        m "From before?"
        m "You mean from when you were choking on my cock?"
        her "Ah...{image=textheart} Yes, sir..."
        m "Did it make you cum?"
        $ end_u_2_pic =  "01_hp/17_ending/48.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "A little..."
        m "Well, you are just precious then, aren't you?"
        her "ah......"
        m "Arent't you, whore?!"
        her "Ah... Whatever you say, sir."
        m "Yes, you are precious, you slut!"
        $ end_u_1_pic =  "01_hp/17_ending/49.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "............."
        m "Squeezing my cock with your little pussy!"
        her "......................"
        m "Hm...?"
        m "Why are you being so quiet?"
        $ end_u_2_pic =  "01_hp/17_ending/51.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Oh... I'm just afraid that someone would--"
        m "I think that's because you want to get spanked!"
        her "What!?"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.1
        hide screen white
        with hpunch
        
        $ end_u_2_pic =  "01_hp/17_ending/52.png" #<---- SCREEN
        #show screen end_u_2                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN
        her "EEeeeeeeeegh!"
        m "Quiet, whore! Someone would hear!"
        $ end_u_1_pic =  "01_hp/17_ending/53.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Sir, I--"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/54.png" #<---- SCREEN
        #show screen end_u_1                                            #<---- SCREEN
        #with d5                                                                        #<---- SCREEN

        her "{size=+7}EEghh!!!{/size}"
        m "Be quiet, I said!"
        m "Or do you want to get caught like this? On your headmaster's cock?"
        m "Do you, Miss queen of the autumn ball?"
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/55.png" #<---- SCREEN
        her "Ah..."
        m "Yes, you're liking this aren't you?!"
        $ end_u_2_pic =  "01_hp/17_ending/56.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her ".............."
        g4 "Answer me, slut!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "01_hp/17_ending/55.png" #<---- SCREEN
        her "Yes, sir! I love it!!!"
        $ end_u_1_pic =  "01_hp/17_ending/53.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Spank me harder, sir! I deserve it!"
        m "That's the spirit!"
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/55.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/55.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/58.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/58.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_1_pic =  "01_hp/17_ending/59.png" #<---- SCREEN
        
        
        show screen ctc
        pause
        hide screen ctc
        
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "01_hp/17_ending/59.png" #<---- SCREEN
        
        show screen ctc
        pause
        hide screen ctc
        
        her "{size=+7}Aaaaaah............................{/size}"


        show screen blktone
        with d3
        sna "Attention, maggots!"
        sna "The \"Hogwarts Autumn Ball\" formal dance is about to begin..."
        hide screen blktone 
        with d3
        
        $ end_u_2_pic =  "01_hp/17_ending/60.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!"
        her "The dance! I completely forgot!!?"
        $ end_u_2_pic =  "01_hp/17_ending/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Sir, excuse me, but you will have to let me go..."
        g4 "Ah... Your pussy is something else!"
        her "Sir... Ah... I am serious."
        her "As the queen I am expected to lead the dance."
        g4 "Yes... Like that, just like that... Oh, yes."
        $ end_u_1_pic =  "01_hp/17_ending/62.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Sir, are you even listening?"
        m "Oh, I hear you alright. And let me make you a counteroffer."
        $ end_u_2_pic =  "01_hp/17_ending/61.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Sir?"
        m "Instead of letting you go..."
        m "I will stick my cock up your ass."
        m "Huh? How about that?"
        her "What? B-but..."
        m "I think that is a great plan!"
        her "Sir, no! I--"
        m "One sec, one sec..."
        show screen blkfade
        with d7
        m "Let me take my dick out of your pussy first..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        call her_head("Ah...","body_172")
        call her_head("Sir, no. You must listen to me--","body_167")     
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        
        # INSERTION
        call her_head("{size=+7}!!!!!!!!!!!!!!!!!{/size}","body_173")
        call her_head("My...{w} My...{w} My...")
        m "Shut it, girl! You are being loud."
        with hpunch
        call her_head("{size=+7}My anus!!!!!!!!!!!!!{/size}","body_173")  
        g4 "Dammit, girl. I said, be quiet."
        
        $ end_u_2_pic =  "01_hp/17_ending/63.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        
        hide screen blkfade 
        with d9
        her "{size=+7}I can't! I don't care! It hurts!!!{/size}"
        g4 "Maybe you don't care, but I do, you whore!"
        $ end_u_1_pic =  "01_hp/17_ending/64.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Your cock is so huge!{/size}"
        g4 "We'll get caught because of you, you stupid slut!"
        m "Maybe this will help you shut up..." 
        
        # Fishhooking.
        $ end_u_2_pic =  "01_hp/17_ending/65.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "!!!............"
        g4 "That's right, you slut. Keep quiet!"
        $ end_u_1_pic =  "01_hp/17_ending/66.png" #<---- SCREEN
        show screen end_u_1                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah... Blah..."
        g4 "Your butthole... It's so damn tight..."
        $ end_u_2_pic =  "01_hp/17_ending/67.png" #<---- SCREEN
        show screen end_u_2                                          #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah... blah... ah..."
        g4 "You are drooling allover my hand, you nasty slut!"
        her "Ah... Blah-blhah... ah... bla-ah..."
        
        show screen blktone
        with d5
        stop music fadeout 1.0
        sna "Well, we are about to start..."
        sna "Get into pairs now..."
        sna "No! Male - female pairs, you dull creatures. What do you think this is? A laboratory assignment?"

        hide screen blktone
        with d5
        $ end_u_1_pic =  "01_hp/17_ending/69.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with fade                                                                    #<---- SCREEN
        play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 # BALL THEME 02.
        m "Don't you worry about missing out on your dance, whore."
        m "We will do a little bit of dancing of our own..."
        her "Ah..."
        m "Yes. This year's ball queen is performing a complicated pirouette with a dick buried deep in her tiny asshole!"
        $ end_u_2_pic =  "01_hp/17_ending/69.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Ah... I am ahh..."
        m "Did you say something, your majesty?"
        her "Ah... I am the autumn ball queen... ah..."
        m "Well of course you are!"
        m "But you're also a whore!"
        $ end_u_1_pic =  "01_hp/17_ending/68.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "I'm a whore..."
        $ end_u_2_pic =  "01_hp/17_ending/70.png" #<---- SCREEN
        show screen end_u_2                                           #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+7}I'm a whore!!!{/size}"
        $ end_u_1_pic =  "01_hp/17_ending/71.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+10}I'm a whoooooooore!!!{/size}"
        g4 "Yes you are!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        $ end_u_1_pic =  "01_hp/17_ending/72.png" #<---- SCREEN
        with hpunch
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"
        $ renpy.play('sounds/slap.mp3')
        show screen white 
        pause.3
        hide screen white
        with hpunch
        $ end_u_2_pic =  "01_hp/17_ending/73.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5} I'm cumming!!!{/size}"
        
        with hpunch
        g4 "Argh! My cock!"
        $ end_u_1_pic =  "01_hp/17_ending/74.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+10}I'M CUMMING! I'm a whore!{/size}"
        g4 "I can't fucking move it anymore!"
        her "{size=+10}I'm CUMMING!{/size}"
        
        
        g4 "My cock is stuck in your asshole, slut!"
        her "{size=+10}I'm a whooore!!!{/size}"
        g4 "I said relax your muscles a little, dammit!"
        $ end_u_2_pic =  "01_hp/17_ending/73.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+7}I can't! I'm cumming!!!{/size}"
        g4 "Fine! Have it your way. I am switching back to your pussy then."
        $ end_u_1_pic =  "01_hp/17_ending/75.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "Huh?"
        # POP
        
        show screen blkfade
        with d7
        g4 "Can't pull out!"
        g4 "Relax your damn anus, girl!..."
        
        $ renpy.play('sounds/boing.mp3') #Sound of # POP!
        with hpunch
        pause.3
        call her_head("...........","body_175")                       
        m "There..."
        
     
    #    $ renpy.play('sounds/gltch.mp3')
    #    with hpunch
    #    with kissiris
        
    #    # INSERTION
    #    show screen h_head2                                                             # HERMIONE
    #    $ h_body = "01_hp/13_hermione_main/body_175.png" # HERMIONE
    #    her "{size=+7}!!!!!!!!!!!!!!!!!{/size}"

        
        
        
        $ renpy.play('sounds/gltch.mp3')
        with hpunch
        with kissiris
        $ end_u_1_pic =  "01_hp/17_ending/77.png" #<---- SCREEN
        hide screen blkfade
        with d5
        # INSERTION
        her "{size=+10}AAAAAAAAAAAH!!{/size}"
        her "It's in my pussy again..."
        g4 "Yes it is, slut!"
        $ end_u_2_pic =  "01_hp/17_ending/79.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "But I'm still cumming!"
        her "What is happening to me, sir!?"

        m "Relax girl, I know what I'm doing!"
        m "This is normal for a slut."
        $ end_u_1_pic =  "01_hp/17_ending/78.png" #<---- SCREEN
        show screen end_u_1                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}No! I will go insane!!!{/size}"
        g4 "You will not. Just ride the wave."
        g4 "Enjoy the sensation while I keep on pounding your pussy!"
        her "{size=+5}Ah!!!{/size}"
        
        $ end_u_2_pic =  "01_hp/17_ending/81.png" #<---- SCREEN
        show screen end_u_2                                            #<---- SCREEN
        with d5                                                                        #<---- SCREEN
        her "{size=+5}Oh!!!{/size}"
        her "{size=+5}I'm a whore!!!{/size}"
        g4 "Yes you are!"
        her "{size=+5}I'm a slut!!!{/size}"
        g4 "Yes you are!"
        g4 "Oh... I think I am getting close myself..."
        g4 "Argh!"
        $ d_flag_01 = False #Came into pussy
        $ d_flag_02 = False #Came into asshole
        
        $ menu_x = 0.5 #Menu is moved to the left side.

                    
        menu:
            "-Cum inside Hermione's pussy-":
                $ d_flag_01 = True #Came into pussy
                g4 "You think your pussy is ready for this, whore!?"
                her "Sir?!"
                g4 "Take this, then!"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                $ end_u_2_pic =  "01_hp/17_ending/86.png" #<---- SCREEN
                with hpunch
                her "{size=+5}Ah! AAaaah!!{/size}"
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                
               
                her "{size=+5}Ah! I can feel it! It's so hot!{/size}"
                g4 "Argh! Yes!"
                $ end_u_1_pic =  "01_hp/17_ending/87.png" #<---- SCREEN
                show screen end_u_1                                         #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                
                
                
                
                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                g4 "Yes! You whore! I'll pump your british cunt full of my cum!"
                
              
                
                $ end_u_2_pic =  "01_hp/17_ending/88.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                #her "Professor! My dress!"
                her "[genie_name]! My dress!"
                g4 "What?"
                her "Make sure you don't get any on my dress!"
                g4 "Shut up about your dress, whore! You are ruining the momment!"
                $ end_u_1_pic =  "01_hp/17_ending/87.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                g4 "Yes! Much better!"
                g4 "Oh......."
        
            "-Cum inside Hermione's butt-":
                $ d_flag_02 = True #Came into asshole.
                g4 "Your butthole should better be ready for this, whore!"
                her "What?!"
                $ renpy.play('sounds/gltch.mp3')
                
                pause.5
                her "Ah..."
                
                #Pop
                
                #INSERTION
                $ renpy.play('sounds/boing.mp3') #Sound of # POP!
                with hpunch
                with kissiris
                $ end_u_1_pic =  "01_hp/17_ending/82.png" #<---- SCREEN
                show screen end_u_1                                          #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+10}AAaaaahhhhh!!!{/size}"
                her "{size=+5}It's in my butthole again!{/size}"
                $ end_u_2_pic =  "01_hp/17_ending/81.png" #<---- SCREEN
                show screen end_u_2                                          #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}No, sir, please! Don't cum inside of my anus!{/size}"
                her "{size=+5}No, I will die!!!{/size}"
                g4 "You will not die, you silly girl."
                g4 "You will orgasm like crazy. Maybe even pass out for a while, but that's all..."
                her "No, sir, please... I'm scared..."
                g4 "Take this, whore!"
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                g4 "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
                
                $ end_u_1_pic =  "01_hp/17_ending/82.png" #<---- SCREEN
                show screen end_u_1                                         #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}Ah! I can feel it!!!{/size}"
                g4 "Argh! Yes!"
                $ end_u_2_pic =  "01_hp/17_ending/83.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}It's filling me up! It's filling me up!!!{/size}"
                g4 "Yes! You whore! I'll pump you full of my cum!"
                $ end_u_1_pic =  "01_hp/17_ending/84.png" #<---- SCREEN
                show screen end_u_1                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                #her "Professor! My dress!"
                her "[genie_name]! My dress!"
                g4 "What?"
                her "Make sure you don't get any on my dress!"
                g4 "Shut up about your dress, whore! You are ruining the momment!"
                $ end_u_2_pic =  "01_hp/17_ending/85.png" #<---- SCREEN
                show screen end_u_2                                             #<---- SCREEN
                with d5                                                                        #<---- SCREEN
                her "{size=+5}I'm sorry! Your whore is sorry!!!!{/size}"
                g4 "Yes! Much better!"
        
                
        $ her_head_ypos = her_head_tits
                
        show screen ctc
        pause
        hide screen ctc
        show screen blkfade
        with d9
        stop music fadeout 1.0
        call her_head("Ah...","body_177")
        call her_head("I can... barely... stand...")
        g4 "I know what you mean, girl."
        g4 "This was our most intense fuck session yet!"
        call her_head("Yes... I never knew I could...","body_177")
        call her_head("...orgasm so hard...")
    #    her "But I must, go... The dance..."
    #    m "Go then..."
        call her_head("Sir... That thing you wanted to discuss with me...","body_176")     
        m "Yeah... You know what? I actually wrote you a little letter on the matter..."
        call her_head("A letter?","body_178")     
        m "Yeah... It should explain a couple of things..."
        call her_head("Oh... Alright...","body_177")     
        m "Just read it tomorrow morning..."
        m "Or whenever..."
        m "Or don't read it at all, I don't care..."
        g4 "............."
        call her_head("Sir...?","body_179")     
        m "Stop it with the eyes! You're making me feel uncomfortable..."
        m "I wrote you a letter, so what?"
        call her_head("I think it's sweet.............","body_179") 
        g4 "I said, stop gawking at me girl. I thought you were late for your dance or something!"
        call her_head("THE DANCE!","body_180")
        call her_head("I'm sorry, I have to go!")
        call her_head("I will see you later, sir!")
        
        $ renpy.play('sounds/run_03.mp3')    #<--------------------Sound of running off.
        pause 3
        m "......................"
        m "No you won't......."
        m "Farewell... Hermione..."
        pause.7
        ">..................................{w}.....................................{w}................................"
    
        play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 # BALL THEME.
        
        if d_flag_01: #Came into pussy
            show screen end_u_1                                             #<---- SCREEN
            $ end_u_1_pic =  "01_hp/17_ending/89.png" #<---- SCREEN
        else:
            show screen end_u_1                                             #<---- SCREEN
            $ end_u_1_pic =  "01_hp/17_ending/90.png" #<---- SCREEN
            
        ">You linger at the alcove for a short while longer..."
        ">You watch Hermione participate in the formal dance..."
        hide screen blkfade
        with d7
        show screen ctc
        pause
        hide screen ctc
        ">She is tired and exhausted no doubt, but she hides it well..."
        show screen bld1
        with d5
        m "(Hm... The girl really is strong...)"
        m "(In all sorts of ways...)"
        hide screen bld1
        with d5
        if d_flag_01: #Came into pussy
            ">You notice a tiny stream of glistening liquid dripping down the inner sides of her legs unnoticed by the crowd..."
        elif d_flag_02: #Came into asshole.
            ">You notice that she sort of clenches her buttocks together every now and then."
            ">Probably doing her best to keep the enormous load you deposited up her butthole just a moment ago inside..."
        show screen bld1
        with d5
        m "................................................."
        m "..............."
        m "(I'd better go now...)"
        hide screen bld1
        with d5
        show screen ctc
        pause
        hide screen ctc
    
    
    #FINAL SCENE. GENIE IS LEAVING.
    
    
    
    show screen blkfade
    with d7
    pause 1
    stop music fadeout 1.0
    
    centered "{size=+7}{color=#cbcbcb}Outskirts of hogwarts{/color}{/size}"

    
    $ end_u_1_pic =  "01_hp/17_ending/171.png" #<---- SCREEN
    show screen end_u_1                                           #<---- SCREEN
    pause.3
    hide screen blkfade 
    with d7
    
    play music "sounds/night.mp3" fadein 1 fadeout 1 #NIGHT SOUNDS.
    
    show screen ctc
    pause
    hide screen ctc
    
    $ renpy.play('sounds/steps_grass.mp3') # SOUNDS OF STEPS IN THE GRESS.
    m "......."
    pause.5
    
    $ end_u_3_pic =  "01_hp/17_ending/172.png" #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    
    
    m "Well, now it is really time for me to go..."
    
    $ end_u_4_pic =  "01_hp/17_ending/173.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    pause.5
    
    
    m "Good bye world of bizzare magic..."
    m "Good bye my who--......"
    m "Good bye, Hermione..."
    m "............"
    m "......"
    
    $ renpy.play('sounds/magic4.ogg')
    with hpunch
    $ end_u_3_pic =  "01_hp/17_ending/174.png" #<---- SCREEN
    hide screen end_u_4                                           #<---- SCREEN
    show screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    $ end_u_4_pic =  "01_hp/17_ending/175.png" #<---- SCREEN
    show screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    hide screen end_u_3                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    
    pause.2
    
    hide screen end_u_4                                           #<---- SCREEN
    with d7                                                                       #<---- SCREEN
    

    show screen ctc
    pause
    hide screen ctc
    
    show screen blktone
    with d7
    
    show screen blktone8
    with d7
#    $ end_u_4_pic =  "title2.jpg" #<---- SCREEN
#    show screen end_u_3                                           #<---- SCREEN
#    with fade                                                                     #<---- SCREEN
    
    
#    show screen blkfade 
#    with d9
    pause .5
    
    
    ## FINAL CREDITS ###
    stop music fadeout 1.0
    if public_whore_ending: # PUBLIC WHORE ENDING
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
              {size=+5}{color=#cbcbcb}This is ending \"02\" of \"02\".{/color}{/size}"
    else: # YOUR PERSONAL WHORE
        centered "{size=+7}{color=#cbcbcb}Congratulations on completing the game!{/color}{/size}\n\n
              {size=+5}{color=#cbcbcb}This is ending \"01\" of \"02\".{/color}{/size}"
        
    hide screen blktone8
    with d7
    
    play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 # ORANGE RANGE THEME.
    
    
    #play music "music/Real Talk by Brix.MP3" fadein 1 fadeout 1 
    #play music "music/03_2_Voicemail Freestyle Mike Wiebe.mp3" fadein 3 fadeout 1  
    #scene image "08_ending/e05.png" with Dissolve(2)
    # show akaani with d5
    #$ dermo = "genie_attack"
    #$ dermo = "snape_attack_guard"
    $ dermo = "ch_sna defend"
    
    show screen credits_chibi
    centered "{cps=20}{size=+5}{color=#ea91b0}-Witch Trainer-{/color}{/size}\n\n
    {color=#e5e297}-\{Written and directed by\}-{/color}\n{size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Head programmer\}-{/color}\n {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Artwork by\}-{/color}\n   {size=+5}{color=#cbcbcb}AKABUR{/color}{/size}\n\n
    {color=#e5e297}-\{Additional Artwork\}-{/color}\n   {size=+5}{color=#cbcbcb}DAHR{/color}{/size}\n\n
    {color=#e5e297}-\{Texts proofread and edited by\}-{/color}\n   {size=+5}{color=#cbcbcb}LYK.D9{/color}{/size}\n\n
    {color=#e5e297}-\{Technical advisor\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO{/color}{/size}\n\n
    {color=#e5e297}-\{Game testers\}-{/color}\n   {size=+5}{color=#cbcbcb}XALJIO\nLYK.D9\nDAHR\nAKABUR{/color}{/size}\n\n{/cps}"
    

    
    
    #nvl clear


    #$ dermo = "ch_hem run_f"
#    $ dermo = "jerking_off_03_ani"
#    show screen credits_chibi
   
  
    $ xder = 160
    $ yder = 160
    $ dermo = "jerking_off_03_ani"
    show screen uni_cr
    hide screen credits_chibi
   
    
    
    
    centered "{cps=40}{size=+5}{color=#e5e297}-\{Sound Effects\}-{/color}{/size}\n    {color=#cbcbcb}http://www.freesound.org/{/color}\n\n
              
    {size=+5}{color=#e5e297}-\{Music provided by\}-{/color}{/size}\n    {color=#cbcbcb}http://incompetech.com/{/color}\n\n
    
    
    
    
    {size=+5}{color=#e5e297}-\{MUSIC\}-{/color}{/size}\n

              

    {color=#e5e297}\"(Orchestral) Playful Tension\" {/color}{color=#cbcbcb}by Shadow16nh.{/color}\n
    {color=#e5e297}\"Prologue\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Shanghai Honey\"{/color} {color=#cbcbcb}by orange range.{/color}\n
    {color=#e5e297}\"Introducing Colin\"{/color} {color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Neville's Waltz\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"The Quidditch Match\" {/color}{color=#cbcbcb}Harry Potter OST.{/color}\n
    {color=#e5e297}\"Anguish\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Awkward Meeting\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Brittle Rille\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Chipper Doodle v2\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Dark Fog\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Despair\" {/color}{color=#cbcbcb}by erenik.{/color}\n
    {color=#e5e297}\"Game Over Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n
    {color=#e5e297}\"Boss Theme\" {/color}{color=#cbcbcb}Final Fantasy VII OST.{/color}\n
    {color=#e5e297}\"Hitman\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Music for Manatees\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Plaint\" {/color}{color=#cbcbcb}by  Kevin MacLeod.{/color}\n
    {color=#e5e297}\"Under-the-Radar\" {/color}{color=#cbcbcb}by  PhobyAk.{/color}{/cps}"
 
    
    $ xder = 670
    $ yder = 410
    $ dermo = "ch_hem run_f"
    #$ dermo = "no_shirt_dance_ani"
    #nvl clear

    centered "{cps=40}{size=+2}{color=#e5e297}-\{CREATOR OF THIS GAME WOULD ALSO LIKE TO PERSONALLY THANK\}-{/color}{/size}\n\n{color=#cbcbcb}
    {size=+5}Dahr{/size}{/color}\n{color=#e5e297}for still working for me pretty much free of charge, for inspiring me to keep on going and simply for being a good friend and colleague. {/color}\n\n
    {color=#cbcbcb}{size=+5}Xaljio{/size}{/color}\n{color=#e5e297} for not only being my personal \"Ren'Py\" consultant but also an extremely thorough game-tester.\n\n
    {color=#cbcbcb}{size=+5}Lyk.D9 (a.k.a. Silentchill){/size}{/color}\n {color=#e5e297}for toiling tirelessly over my texts full of typos and broken grammar. {/color}\n\n
    {color=#cbcbcb}{size=+5}Bookfisher{/size}{/color}\n{color=#e5e297}For everything.\n\n
    {color=#cbcbcb}{size=+5}The fate (universe or higher power){/size}{/color}\n{color=#e5e297}For giving me an opportunity to release another game while retaining complete creative freedom.\n\n\n
              
    {color=#cbcbcb}{size=-1}A whole bunch of other people who helped me with development of this game in one way or another,\n but whom I forgot to mention.{/color}\n
    {color=#cbcbcb}And of course to everyone else who supports\nme and my work.\n\n\n
              
    {/color}{/size}{/cps}"

    hide screen uni_cr
    
    #nvl clear

    centered "{cps=70}{color=#cbcbcb}This is not a commercial video game. The entire project was independently founded solely through\nhttp://www.patreon.com/ and\nby \"Hentai United\" subscribers.{/color}\n\n\n
    
    {size=-1}{color=#e5e297}-People who supported development of this game with extraordinary amount of money-{/size}\n
    {color=#cbcbcb}Lawrence Dash, Wirefull, Dorago, Benoit Yan Larose, Talisca{/color}\n\n
              
    {size=-1}{color=#e5e297}-\"INVESTOR\" pledges-{/size}\n
    {color=#cbcbcb}Ace, Linus Furtenbach (Bluue), Eduardo Pereira Carneiro, Vicente Sampedro Burgos, Morning Dawnstar, Wolo, John Layon, stefan mitrano, Gavin Spears, sergio.{/color}\n\n
    
                        
    {size=-1}{color=#e5e297}-\"AGENT\" pledges-{/size}\n
    {color=#cbcbcb}Cameron MacDowell, Zarsher, Guynonymous, Nerzha, Silvanus2004, Xipomus, Carpy Rex, Adler, Deitan-Baruch St-Amand, Martin Neal, wetrx, mark howard, 
Kenneth Aguilar, alt, David McClellan, Leo H Wilkin, Thorn, TheDudeAbides, Alexandre Rouleau, thomas taylor, Alexander, Redmoonx22, Valdee, Alexander Lykke Landkildehus, Lucas Ferrari, Dom, derek zhang,Charlatan, Preston C T, waylan, Forrest, Loopy, JohnnyBB, Phantom Void, Kyaa, Stephen Richardson, mark herzog, will newton, Sascha Klug, Joshua McDonald, Undying S, John Cawley III, KitsuneEyes, Slingthatcat, Kieran James, Homod saleh al-shammri, randomuser89, Paul Keating, Antonio B, Marko, Tobias, Akhil Chokshi, Smiling_Jack, Clif Morgan, Derek Heynsbergen, Jack Cartwright, Damien Zaid, callmemusashi Mozambiqued, Nemesis Valentine Vanyar, Stalker, Jason, 4nubis, Curtis, Michael Simon, AB, The Wanderer (Mark Hawker), paul, JEB, Voe, Aselobar, Elgrangato82, froste, YllegaL, Bisongun, Skye Tomlinson, Parad0x, Eric Chen, Destiny, Podchamawa Petrovitch, Will, lc, Sathyan Mathai, Lisandro Gil, bill tedd, Tommy Turner, Marcel Kral, Oric13, Ren Ashjiro, anthony donihee, Honey Withers, Christopher, TofuCats, Drake King, Bookfisher Herring, Dustpan, dusty parrott, Bjorn, Robert Jolly, wilson yang, Tudor G, Arzaz, Etienne Ngo, xazathothx, Robert L Schliff, RO, DavidB, Daedilus, david green, Matt, Ketil, ALEXANDER KOVALEV, Oa, John, PG, largo_leet, David, Artemsgvozdem, heyPert.{/color}{/size}\n\n{/cps}"
         
         
    #nvl clear
    centered "{cps=70}{size=-1}{color=#e5e297}-\"REBEL\" pledges-{/size}\n
    {size=-4}{color=#cbcbcb}1234ghumm, A. R., AJ Ferolie, Catalyst Greenhorn, Abraham Benitio, Actafool812, Adam, Casax5, Adam, FearTheDee, Akasection, Alejandro Luna, Aleksandr, Alex Odoul, Alex P., Alexander Randolph, Maidaniuk Yurii, Alexander, Alexei, Alkosh, Allan Pineda, Altagar, Andreas Janning, Andrei Kuz, Andrey Nikolaev, Anton Belyankin, Anton Tropicflames, Antonio Jos Mucoz Gonzalez, Antonio Rivera, Artur Kevorkov, Baran, BearPerson, BeepBep, Benjamin Drew, Bernard Winters, Bob Mannaro, Boyko, Brad, Brandon Gauthier, Brandon Mirr, Brent, Brett Williams, Bruce Gates, Byakuya36, Cirrus, Calmea, Carez, Carnosaur, Chad Dunkerley, Charles Able, Chemmy, Chris, Christopher Coulter, Christopher Woo, Christopher, Conner Owen, Conrad Boucher, Cruise Russo, Cyanide Sam, DMetal, Dakota Rude, Damian Boggs, Daniel Beard, Daniel Nathans, Daniel Smith, Daniel Szczuka, Daniel Torres, Danno, Danny Johansson, Danny Nguyen, Darkflame256, David Lestina, David Ruskin, David, Dean, Devin Barr, Dirk Delva, Donaj88, Donoth Aveano, DoornailsAreJealous, Demodraken, Double A, Drity, Edward le coyte, Eldar Scum, Eric Hsu, Evan waleske, Fabian, Faux, Fetsch Sebastian, Finrock, Fix, Formless, FoxPrince623, Frank Pietsch, Fraziel, Frederic Chen, Garrett Smith, Geoff Levario, Georgika, Gregc, Greg Hartley, Gregory G, Gunderson, Harm Harm, Harry Tizard, Hooverspleen, Ian W, Innes French, Jacob Thompson, Jacob, Jake Smith, Janis Feldbergs, Janus, Jared Whisenand, Jarred Leverton, Jason Buisman, Jason Chong, Jeff Abrams, Jeff, Jeremiah, John F, John S, John doe, John, Jonathan Backer, Jonathan, Joseph Balbuena, Joseph Oliveira, Josh Stegmaier, Juan Gomez, Jurdia, Justin Golden, Karl Stevenson, Karolis, Kenneth Guevarra, Kenneth Jackson, Kenny Huang, Kimo Linder-Fattah, Kolkina, Kristian Lund Jensen, Kryssler, Kurrel, Kyle Sarty, Kyuubi43, LIndy, Levone W., Jonathan Liu, Lockkaliber, Lord G, Lord Rayek, Lothvarthian Malik, Lukas Vystup, Luke Arrowsmith, Magmanox, Majushi, Mario Mueller, Mark Walrusburg, Martino Livio Martinello, Mason Davis, Matt Sullivan, Matthew Young, Michael Klepper, Michael McPherson, Michael O'Hara, Michael, Mike M., Mike Orlando, MinoCrossing, Miran, Mitchell Goodwin, Monky of Space, Morten Brunebjerg Hansen, Myers, N Metso, Naintoxe, Nairolf, Nathan S, Neo Savoric, Niels T, NugLord, Number37, Nym Nemo, Oliver Pirie, Oscar Lan, PS, Passionately Odd Syntax, Patrick Fochler, Patrick, Paul Allen, Peter Grnlykke, Professor Snape, PuddingPowder, Pel-Tore, Rabe, Raglan Strom, Randolph Carter, Random, Reaver78, Rekoar, Reny Frederiksen, Richard Buettner, RickRub, Rightmind, Rob, Robert Doughty, Robert Simmons, Rodrigo Das Flores, Rune Daugaard Lundsteen, Runkle, Russell, SJ M, SYukito, Sane 300, Sayting, Sinedd, Scorch289, Sean Carstensen, Sebastian Tauch, Sehad, Shane Fitzsimons, Shawn Aiken, Skellman, Skull616, SlaveToTheSound, Smaug, Some Guy, Steffen Nissen, Stephen Krieger, Steve Jones, Steven Cunningham, Syr, TGriz, Talon Grant, Teemu, Thae, The Masked Masturbator, This Isntmahname, Thomas Frobish, Thomas Grimes, Thomas Vazquez, Timmothy Firewood, Tom Arne Vestby2, Tony Taylor, Tony Veliz, Truvor, Tuki, Tyler, Venron, Vervalsen, Vi9, Visp, Wanderer, Weenie Beenie, Wesley Gamble, XDrakeX, Xev, YummyTiger, Yuu Yi, Zach Rzepiela, Zakmonster, Zeath, Zenzard, Zim outside, Zoggy, alvin suryaputra, am1tg3, andrew gardiner, artisticMink, barry r king, bloodangel99, butts, caleb4532, charles turnbull, cvonsuela28, dingo egret, dingo1489, eXotic, fernando frias, gliph13, ippherita, izys, jabix, jassem dashti, john smith, josiah richter, karkazin, kyle mock, lia sven, lucas2684, n1ghtfox, nobody, potatohead, progste, randellspec, retchedegg, robster, silvarius2000, srt20022003, strider19, tehcalipwnt, terribleplan, thegreatbambe, timmy turner, varoksa, xenus, ziric.{/color}{/size}\n\n{/cps}"
    
    #nvl clear
    centered "{cps=70}{size=-1}{color=#e5e297}-\"ACTIVIST\" pledges-{/size}\n
    {size=-4}{color=#cbcbcb}Adam, Alvin, AmateurArtist98, Anders Sandahl, Naqqash Chaudhry, Andre, Andrew E., Bayushi, Ben Belcastro, Brandon Louie, Brandon Robinet, Brian Wilson, Carmen Williams, Chad Bennett, Dan George, Darklogic, Darknezzz, Dave Shevlin, David Crosby, David Sparkes, Douglas Jones, Draconic Paragon, DragonTamer, Ervin, Francis Dixson, Fredinator, Gene Boglin, George Craig, Greg, Guillaume Mroz, Gustaf Johansson, Hirin, Ian Lindop, IanDasein, Inge, Izzy Sabur, JBTClown, JP, Jack, Jacob Kain, Jan Hanenkamp, Jan M., Jan, Johannes Uwer, John Turner, Joshua Baadsgaard, KiSwordsman, Krux2022, L, Legio 20th, Marconi Ribeiro, Mike, Marius L, Mathias Frandsen, Matthew Marqueta, Max, Michael Webb, Miha Antauer, Mikhail V. Platonov, Mitch, Mountainj6, MrDurper, Sean Hill, Sam, Muirewedd, Neogeta, Nick Foronda, Nick, Noah Gerhards, Oren Barzilai, Pashike, Peeves, Phil Fairbanks, Philip G Honore, Riu Bas, Robert, Reinis Aleksejevs, Rougespartan181, Robert Lesundak, SO, SYH, Sacs, Sapherin, Sayyid, Sean, Shawn MacInnis, Simanith, Soda Zero, Speculations, Stephen Evans, Stonedrake, TRONboy, Tamenund Jones, Tintron, Victor Jd, Vincent McCool, Vitaliy Kasianenko, Vorcai0, Wolfcub, X.p., X39, Yan Luong, Zaker, chippy, joesco726, kurorol2, lambroll, ljennia, matthew lampell, moonwalkin, nh, raaq, six2make4, zack, Andry Sidorov.{/color}{/size}\n\n
              
              
              
    
    {size=-1}{color=#e5e297}-\"SUPPORTER\" pledges-{/size}\n
    {size=-4}{color=#cbcbcb}AS84, Aaron Gregory, Gianfranco Calzoni, Aarvil Kemph, Aestus, Alex Martin, Andrea, Andreas, Andrew, Antilles, Antonboeg, Aran, Armando Soto, Azuliar, Batman, Balint Sule, Ben Rog-Wilhelm, Benjamin Cathey, Beth, Brad Hingston, Brandon Grant, Brendan, Brian Borden, Bru, Canyon, Capperroff, Chaintan, Christian Wong, Colton Clayton, Corey S., D, Damian Paradis, Daniel Chai, Daniel Geach, Daniel, Danny Mullay, Darpy, Dave doedry, David Leitner, Dax, Doctor Worm, Dragonman, Edd Holmes, Erebe, Eric Speaker, Fattycakes, FearTheDee, FeyOne, Filip Jaromin, Florian Eberle, FooldiverDX, Fortifel, Frank Bull, G V, Gaetano, Gary Tinsley, Gerald, Gerald, Gerhalt, Gregoire Fauconnier, Gregory, Happy Days, Hellomellowyellow, Hurf durf, Ian Sayer, Ilya, Ivan Nadasaki, J Solomon, Jack Simons, Jack Trebles, James Brown, James Do, Jan-Kristoffer Brekke, Jayro Zipzapili, Jesse Doerksen, Jim, John Jon'zz, John Smith, Jonas Högman, Jose Gonzalez, Joshua West, Julian Silva, KC maps, Kabuto, Kasper Nohr, Kenny Bailey, Kevin McKie, Kuroguma, Lanthanio, Louie Castro, MaiconMM, Majinken, Malcom Reynolds, Marc Voigt, Marcel Muller, Marius Thomassen, MarkAurel, Martin Ax, Matri, Matt, Matthew Lam, Max Robitzsch, MehMonkeys, MercuryTwins, Messor Marra, Michael Troseth, Michael, Michael, Michael, Mike Bow, Mike Jones, Mike Moperz, Mikhail, N0body, NalfeinDoUrden, Nate A, Nicholas Alan McGuire, Nikuss, Nils Harder, Nitrat, Nordicberserk, Notsutos, Oberon, Onyxdime, Oxion1988, Ozzy, Paradosi, Pasi Huttunen, Patrick Gill, Paul Coad, patrick welsh, Paul, Pshenitsyn, PeeM, Peter Nikolas, Peter Ryskin, Pitt85, Preator, Pulimanne, Randall Lively, Richard Dumont, Richard Heying, Richard Soderberg, Riley Heffernan, Robert Bodo, Robert Davis, Rodrigo Rosado, Ronald, Roy Zimmermann, Ryan Bossard, Ryan Calhoun, Salvadore Broadfoot, Scott Barrie, Sebastien Elie, Sebastien Jalbert, SgtAfro, Shadefalcon, Stefano Sottocorna, SilverAxe, Sixxiie, Sky Valverde, Sodajuice, Steffen Sloth, TK, TP Samblanet, Taylor Patton, Taylor, Tenebrys Hentai Flash Games, Matthew Pruter, John Stanko, craig chadwick, TheOriginalJ, Thomas, Timeyy, Tony Li, TonyNinja, Tracy Scops, Travis Haapala, TrikJoker, Tyler Jones, Tyson, Urza Viderico, VC, Vasder, Vay Jay, Victor Sarosi, Warren P Nelson, Wayne Chattillon, William Farris, William Golding, Wlodzimierz Donatowicz, Xaljio, Xisis, brett, bronzeRanger, clerk4470, ghosti1, gillen, ismael torres, jaron uecker, levi tibbals, oakland, otakuguy01, rip_cpu, severin, sirpoffalot, teh_cabbage, tenko, trajor white, wilhelm, winsloven, Arkadii Terentiev, xxx, DAHR.{/color}{/size}\n\n
              
    {color=#e5e297}{size=-4}-\{Thank you, Joseph Antoni, for organizing all these 750+ names for me.\}-{/size}{/color}{/cps}"
              
              
              
              
              
              
    pause 1
    
    show screen ctc
    pause 
    hide screen ctc
    show screen blkfade
    with d9
    stop music fadeout 3.0
    ">................................{w}...........................{w}................................."
    pause.5
    centered "{size=+7}{color=#cbcbcb}The morning after...{/color}{/size}"
    
    hide screen end_u_1                                           #<---- SCREEN
    hide screen end_u_2                                           #<---- SCREEN
    hide screen end_u_3                                           #<---- SCREEN
    hide screen end_u_4                                           #<---- SCREEN
    hide screen blktone
    hide screen blktone8
    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.
    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 #CANDLE FIRE.
    hide screen candlefire_02 #CANDLE FIRE.
    hide screen lightening #Hide lighting so it woudn't get stuck during clear sky weather and such.
    hide screen cloud_night_01 #NIGHT CLOUDS.
    hide screen cloud_night_02 #NIGHT CLOUDS.
    hide screen cloud_night_03 #NIGHT CLOUDS.
    hide screen bld1 #You know what this is. Just making sure it doesn't get stuck.
     
    show screen new_window # CLEAR WEATHER.
    
    hide screen room_night #Hiding NIGHT BG from last night.
    show screen room #Showing main room BG. 

    hide screen door   
    hide screen cupboard
    hide screen chair
    hide screen fireplace
    hide screen phoenix
    hide screen candle_01    
    hide screen candle_02
    hide screen genie
    hide screen owl
    hide screen owl_02
    hide screen with_snape #Genie hangs out with Snape in front of the fireplace.
    hide screen with_snape_animated #Genie hangs out with Snape in front of the fireplace.

        
    show screen door   
    show screen cupboard
    show screen chair
    show screen fireplace
    show screen phoenix
    show screen candle_01    
    show screen candle_02
    show screen dumbledore

    hide screen blkfade
    with d9
    
    show screen ctc
    pause
    hide screen ctc
    
    show screen bld1
    with d3
    dum "................................"
    hide screen bld1
    with d3
    
    
    if public_whore_ending: # PUBLIC WHORE ENDING
        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        $ snape_speed = 02.0 #The speed of moving the walking animation across the screen.
        $ walk_xpos=470 #Animation of walking chibi. (From)
        $ walk_xpos2=360 #Coordinates of it's movement. (To)
        show screen snape_walk_01 
        with d3
        pause 1.5
        show screen snape_02 #Snape stands still.
        pause.1
        show screen bld1
        with Dissolve(.3)
        
        play music "music/Dark Fog.mp3" fadein 1 fadeout 1 # SNAPE'S THEME
        dum "Good morning, Severus."
        $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
        $ s_head_ypos = 340 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
        $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "......................................."
        hide screen s_head2              
        dum "I have the most extraordinary tale to share with you, old friend."
        $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "......................................"
        hide screen s_head2     
        dum "But before I do..."
        $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "........................................"
        hide screen s_head2     
        dum2 "Ehm... Severus?"
        $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "........................................."
        $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Who rules?"
        hide screen s_head2     
        dum2 "I beg your pardon?"
        $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Who rules?" # T_T
        hide screen s_head2     
        dum2 "...who rules what?"
        $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "A...?"
        hide screen s_head2     
        dum2 "A?"
        $ s_sprite = "01_hp/13_characters/snape/main/snape_27.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Aka-a....?"
        hide screen s_head2     
        dum2 "You don't make any sense, Severus."
        $ s_sprite = "01_hp/13_characters/snape/main/snape_29.png"                                         # SNAPE
        show screen s_head2                                                                                                 # SNAPE
        sna "Ah, bloody hell..................."
        hide screen s_head2     
        pause.5
        show screen ctc
        pause
        hide screen ctc
        stop music fadeout 1.0
        
        show screen blkfade
        with d7
        pause 2
        
        
        
        
        

        
        
    
    else: # PERSONAL WHORE ENDING 

        $ renpy.play('sounds/door.mp3') #Sound of a door opening.
        call her_walk(610,400,3)
        show screen hermione_blink #Hermione stands still.
        with d3
        pause.5
        show screen bld1
        with d3
        
        show screen ctc
        pause
        hide screen ctc
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        $ tiara = False #Turns off displaying of the tiara in h_head2 screen.
        $ her_head_ypos = her_head_tits
        call her_head("Sir, if this is about yesterday...","body_120")
        #her "You wanted to see me, sir?"
        dum "Good morning, miss Granger."
        call her_head("It's not like I actually enjoyed it or anything, you know...","body_79")  
        dum "Miss Granger, I found this letter on my desk..."
        dum "It's addressed to you..."
        call her_head("A letter, sir?","body_15")
        call her_head("Oh, of course! The one you wrote for me, sir.","body_24")  
        dum "This letter is not from me, miss Granger."
        call her_head("It is not?","body_17")
        call her_head("Oh, I see...","body_24")
        call her_head("There is no need to be so shy about this, sir. It's alright.")
        dum "*ahem*... here it is."
        call her_head("Thank you, sir.","body_06")
        call her_head("Let's see....","body_73")
        stop music fadeout 7.0
        pause.1
        
        $ letter_text = "{size=-7}To: Hermione Granger\n\n{/size}{size=-4}Dear [word_01]. \nI am not who you think I am... Not even human so to speak. For months now I have been posing as a person known to you as Professor Dumbledore. But it is time for me to go back [word_02]. By the time you will receive this letter I shall be long gone. We shall never cross paths again, but I promise you that I will cherish the memories of my brief time in your strange world. \n\nFarewell, my little [word_03]. {size=-3}\n\n-[word_04]-{/size}"
        
        label last_letter:
        show screen letter
        show screen ctc
        show screen bld1
        with Dissolve(.3)
        pause
        menu:
            "-Done reading-":
                pass    
            "-Not yet-":
                jump last_letter
        hide screen letter
        hide screen ctc
        hide screen bld1
        with Dissolve(.3)
        
        
     
        show screen bld1
        with d3
        call her_head(".............................................................................................................................................................","body_197")  
        dum "I assume the sender of this letter is that Genie fellow?"
        dum "The one who has been impersonating me for the past several months?"
        call her_head(".............................................................................................................................................................","body_197")  
        dum "Well, now that I am back..."
        dum "I will be putting an end to all that \"favour-selling-business\" of course."
        call her_main("","body_86",xpos=370)
        pause.1
        with hpunch
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 # HERMIONE'S THEME.
        her "{size=+7}What?!!{/size}"
        call her_main("How am I supposed to win any points then?","body_66")
        dum "The same way you always did, miss Granger."
        call her_main("Huh...?","body_186")
        dum "With hard work."
        call her_main("That's just stupid!","body_187")
        dum2 "Miss Granger, would you mind to guard your tongue when--"
        ### TITS ###
        #$ only_upper = True
        call set_hermione_action("lift_top")
        call her_main("","body_81",xpos=140)
        show screen ctc
        stop music
        pause
        hide screen ctc
        #her "..."
        dum3 "{size=+4}!!!{/size}"
        call her_main("Or would you rather see my pussy, sir?","body_86")
        call set_hermione_action("lift_skirt")
        call her_main("","body_61")
        show screen ctc
        pause
        hide screen ctc
        with hpunch
        dum5 "{size=+7}GHT!!!{/size}"
        her "I am willing to do anything to get those points, sir!"
        call set_hermione_action("")
        with hpunch
        call her_main("And I mean {size=+9}ANYTHING!!!{/size}","body_86")
        hide screen hermione_main
        with d3
        
        hide screen bld1
        with d3
        $ walk_xpos=400 #Animation of walking chibi. (From)
        $ walk_xpos2=280 #Coordinates of it's movement. (To)
        $ hermione_speed = 03.0 #The speed of moving the walking animation across the screen.
        show screen hermione_walk_01 
        pause 1
        show screen blkfade
        with Dissolve(0.3)
        $ renpy.play('sounds/08_hop_on_desk.mp3') #Sound of the desk squeaking. 
        pause.7
        
        dum4 "Oh, dear... {image=textheart} "
        pause 1
        
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    centered "{size=+7}{color=#cbcbcb}-\{Thank you for playing!\}-{/color}{/size}\n\n
              {size=+1}{color=#cbcbcb}-AKABUR 2014-{/color}{/size}"
    
    pause 2
    
    $ persistent.game_complete = True # Turns TRUE after you beat the game. Unlocks the gallery.
    
    # SILVER Items
    
    # gift item invintory
    $ persistent.gift_item_inv = []
    $ persistent.gift_item_inv = gift_item_inv
    
    # scroll invintory
    $ persistent.sscroll_ = []
    $ persistent.sscroll_ = sscroll_
    
    # outfit invintory 
    #$ persistent.outfit_inventory = []
    #$ persistent.outfit_inventory = outfit_inventory
    
    # books
    $ persistent.book_progress = []
    $ persistent.book_progress = book_progress
    $ persistent.book_done = []
    $ persistent.book_done = book_done
    $ persistent.books = []
    $ persistent.books = books
    
    
    if public_whore_ending:
        $ persistent.ending_02 = True # Unlocked ending 01.
    else:
        $ persistent.ending_01 = True # Unlocked ending 01.
        
    $ persistent.gold = 0
    $ persistent.gold = persistent.gold + gold
        
    ### THE SKIRT ###
    if gave_miniskirt: #Turns True when Hermione has the miniskirt.
        $ persistent.haveskirt = True # Makes sure you only need to buy the skirt once. Checked at the +new game screen.
   
    
    ### POSSESSIONS ###
    
    $ persistent.lolipop = 0
    $ persistent.lolipop = persistent.lolipop + candy # LOLIPOP.
    
    $ persistent.choco = 0
    $ persistent.choco = persistent.choco + chocolate # CHOCOLATE.
                    
    $ persistent.owl = 0
    $ persistent.owl = persistent.owl + owl # PLUSH OWL.
                
    $ persistent.beer = 0
    $ persistent.beer = persistent.beer + beer # BUTTERBEER
                
    $ persistent.mag1 = 0
    $ persistent.mag1 = persistent.mag1 + mag1 #MAGAZINE # 1
    
    $ persistent.mag2 = 0
    $ persistent.mag2 = persistent.mag2 + mag2 #MAGAZINE #  2
    
    $ persistent.mag3 = 0
    $ persistent.mag3 = persistent.mag3 + mag3 #MAGAZINE # 3
    
    $ persistent.mag4 = 0
    $ persistent.mag4 = persistent.mag4 + mag4 #MAGAZINE # 1

    $ persistent.krum = 0
    $ persistent.krum = persistent.krum + krum # KRUM POSTER.

    $ persistent.lin = 0
    $ persistent.lin = persistent.lin + lingerie # LENGERIE.

    $ persistent.con = 0 
    $ persistent.con = persistent.con + condoms # CONDOMS.
       
    $ persistent.vib = 0
    $ persistent.vib = persistent.vib + vibrator # VIBRATOR.
        
    $ persistent.lube = 0
    $ persistent.lube = persistent.lube + anal_lube # Anal lubricant.

    $ persistent.gag = 0
    $ persistent.gag = persistent.gag + ballgag # BALL GAG.
          
    $ persistent.plug = 0
    $ persistent.plug = persistent.plug + plug # ANAL PLUG.
          
    $ persistent.strap = 0
    $ persistent.strap = persistent.strap + strapon # STRAP-ON.
           
    $ persistent.broom = 0
    $ persistent.broom = persistent.broom + broom # BROOM.
              
    $ persistent.doll = 0
    $ persistent.doll = persistent.doll + sexdoll  # SEX DOLL.

    $ persistent.wine = 0
    $ persistent.wine = persistent.wine + wine # WINE.

            
           
    ### SACRED SCROLLS ###
    
    if sscroll_[1]:
        $ persistent.ss_01 = True # Sacred Scroll 01 will be unlocked in the gallery.
    if sscroll_[2]:
        $ persistent.ss_02 = True # Sacred Scroll 02 will be unlocked in the gallery.
    if sscroll_[3]:
        $ persistent.ss_03 = True # Sacred Scroll 03 will be unlocked in the gallery.
    if sscroll_[4]:
        $ persistent.ss_04 = True # Sacred Scroll 04 will be unlocked in the gallery.
    if sscroll_[5]:
        $ persistent.ss_05 = True # Sacred Scroll 05 will be unlocked in the gallery.
    if sscroll_[6]:
        $ persistent.ss_06 = True # Sacred Scroll 06 will be unlocked in the gallery.
    if sscroll_[7]:
        $ persistent.ss_07 = True # Sacred Scroll 07 will be unlocked in the gallery.
    if sscroll_[8]:
        $ persistent.ss_08 = True # Sacred Scroll 08 will be unlocked in the gallery.
    if sscroll_[9]:
        $ persistent.ss_09 = True # Sacred Scroll 09 will be unlocked in the gallery.
    if sscroll_[10]:
        $ persistent.ss_10 = True # Sacred Scroll 10 will be unlocked in the gallery.
        
    if sscroll_[11]:
        $ persistent.ss_11 = True # Sacred Scroll 11 will be unlocked in the gallery.
    if sscroll_[12]:
        $ persistent.ss_12 = True # Sacred Scroll 12 will be unlocked in the gallery.
    if sscroll_[13]:
        $ persistent.ss_13 = True # Sacred Scroll 13 will be unlocked in the gallery.
    if sscroll_[14]:
        $ persistent.ss_14 = True # Sacred Scroll 14 will be unlocked in the gallery.
    if sscroll_[15]:
        $ persistent.ss_15 = True # Sacred Scroll 15 will be unlocked in the gallery.
    if sscroll_[16]:
        $ persistent.ss_16 = True # Sacred Scroll 16 will be unlocked in the gallery.
    if sscroll_[17]:
        $ persistent.ss_17 = True # Sacred Scroll 17 will be unlocked in the gallery.
    if sscroll_[18]:
        $ persistent.ss_18 = True # Sacred Scroll 18 will be unlocked in the gallery.
    if sscroll_[19]:
        $ persistent.ss_19 = True # Sacred Scroll 19 will be unlocked in the gallery.
    if sscroll_[20]:
        $ persistent.ss_20 = True # Sacred Scroll 11 will be unlocked in the gallery.
            
             
    if sscroll_[21]:
        $ persistent.ss_21 = True # Sacred Scroll 21 will be unlocked in the gallery.
    if sscroll_[22]:
        $ persistent.ss_22 = True # Sacred Scroll 22 will be unlocked in the gallery.
    if sscroll_[23]:
        $ persistent.ss_23 = True # Sacred Scroll 23 will be unlocked in the gallery.
    if sscroll_[24]:
        $ persistent.ss_24 = True # Sacred Scroll 24 will be unlocked in the gallery.
    if sscroll_[25]:
        $ persistent.ss_25 = True # Sacred Scroll 25 will be unlocked in the gallery.
    if sscroll_[26]:
        $ persistent.ss_26 = True # Sacred Scroll 26 will be unlocked in the gallery.
    if sscroll_[27]:
        $ persistent.ss_27 = True # Sacred Scroll 27 will be unlocked in the gallery.
    if sscroll_[28]:
        $ persistent.ss_28 = True # Sacred Scroll 28 will be unlocked in the gallery.
    if sscroll_[29]:
        $ persistent.ss_29 = True # Sacred Scroll 29 will be unlocked in the gallery.
    if sscroll_[30]:
        $ persistent.ss_30 = True # Sacred Scroll 12 will be unlocked in the gallery.
        
        
        
        
        
        
        

        
        