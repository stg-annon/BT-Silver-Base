label date_with_snape_01:
    show screen bld1
    with d3
    m "Alright. Teach me your wand-based magic now."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Sure, I could do that..."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Or I could tell you some more about those teenage \"slytherin\" sluts..."
    hide screen s_head2              
    g9 "The latter, please."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Great... Get a load of this then..."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">You spend the evening by discussing all sorts of inappropriate things with Porfessor Snape."
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">You feel a faint bond forming between you two..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
    
label date_with_snape_02:
    show screen bld1
    with d3
    m "For our little enterprise to succeed..."
    m "You need to be more generous with these house point things..."
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                                      # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Right, of course..."
    sna "Miss Granger will require a strong incentive..."
    sna "So putting my house in the lead is essential..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Could take time though..."
    hide screen s_head2 
    m "Take time?"
    m "Why not just award a couple of hundred points to \"Slytherin\" and be done with it?"
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "No, we need to be discreet with this..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                        # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Awarding a whole bunch of points to my house without any reason could draw in unnecessary attention..."
    hide screen s_head2 
    m "Hm... I see your point..."
    show screen blktone
    with d3
    ">You spend the evening by conspiring against Hermone with professor Snape..."
    ">The faint bond of friendship between you two strengthens."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
label date_with_snape_03:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Have you heard of that \"men's rights movement\" nonsense?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "What a nuisance that girl is..."
    sna2 "She is smart, popular and has a will of iron..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Lately I am starting to feel very doubtful about our whole plan..."
    hide screen s_head2 
    m "You shouldn't though..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Is that so..."
    hide screen s_head2 
    m "It may take some time, but I {size=+5}will{/size} break her."
    m "Just trust me."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Alright..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "What choice do I have but to hope for the best...?"
    hide screen s_head2 
    show screen blktone
    with d3
    ">You spend the evening by dreading the uncertain future with professor Snape."
    ">A faint bond of trust is forming between you two."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    

    $ snapes_support += 1 #Controls how many points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
  
    return
    
label date_with_snape_04:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Tell me something, Genie..."
    hide screen s_head2            
    m "Yes?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Do you believe in the theory of parallel worlds?"
    hide screen s_head2    
    m "Well, it is hard not to. All things considered."
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "True..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "So you think somewhere out there is another version of me?"
    hide screen s_head2    
    m "Probably..."
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Hm..."
    sna "Severus Snape - the ever cheerful white mage..."
    hide screen s_head2    
    m "Sure, why not?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What unsettling imagery you put into my mind..."
    hide screen s_head2    
    m "How about another version of that Granger girl?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Yes! Hermione Granger - the repulsive slut without any dignity! Yes, I like it!"
    hide screen s_head2    
    m "And what if in that other world the cheerful Severus teams up with some bizarre version of me?"
    m "And maybe together we train the slut Hermione to be a proper girl and a good student?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Ha-ha-ha! That's hilarious!"
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">You spend the evening by discussing science, metaphysics, philosophy and sluts."
    ">the bond of friendship between you and Professor Snape strengthens."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return

    
    
label date_with_snape_05:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "So... How is our little plan coming along?"
    sna2 "Is that wretched girl giving you trouble?"
    hide screen s_head2    
    menu:
        "\"Yeah. She's stubborn.\"":
            $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
            show screen s_head2                                                                                                 # SNAPE
            sna "No surprise there..."
        "\"No, not really...\"":
            $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
            show screen s_head2                                                                                                 # SNAPE
            sna "Seriously?"
            sna "Interesting..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "But you are positive you will be able to break her?"
    hide screen s_head2    
    m "Oh, absolutely."
    m "It may take some time though..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Well, we do have time..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "I mean you are still pretty much powerless, right?"
    hide screen s_head2    
    m "Yeah, pretty much..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Splendid!"
    hide screen s_head2    
    m "......................."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "I mean it is bad for {size=+5}you{/size}, but good for {size=+5}us{/size}, right?"
    hide screen s_head2    
    m "Right..."
    show screen blktone
    with d3
    ">Professor Snape seems to feel awkward about benefitting from your misery..."
    ">The bond of friendship between you two strengthens slightly..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_06:
    show screen bld1
    with d3
    m "So, tell me about those \"slytherin\" sluts some more!"
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "What can I say? Life's been good to me lately, my friend."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "These days I have a whole harem of skimpy students to choose from."
    hide screen s_head2  
    g9 "Nice!"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Yes. Thanks to you, my friend I can do whatever the bloody hell I want!"
    sna2 "And more importantly..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Whoever the hell I want!"
    hide screen s_head2  
    m "Seriously?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Well, sort of..."
    sna2 "Obviously I don't actually walk around and \"do whoever I want\"..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "But you wouldn't believe what some of those girls are willing to do in exchange for house points!"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Or even for the mere promise of good grades..."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Professor Snape's usual cold exterior disintegrates before your eyes..."
    ">The bond of your friendship strengthens yet again..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
    
label date_with_snape_07:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "So, back in your world you are some kind of all-powerful being?"
    hide screen s_head2  
    m "Yeah, sort of..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Then how come you do the bidding of that Jasmine woman?"
    hide screen s_head2  
    m "Oh... Well..."
    m "...she is a princess."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "So?"
    sna "Is she your princess? You are not even human."
    sna "Did you swear your loyalty to her?"
    hide screen s_head2  
    m "Not really..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Why do you even bother then?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "The way I see it, you are an all-powerful being and she is just some muggle..."
    hide screen s_head2  
    m "She's a what?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "A human... She's just a human..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "So why bother trying to please her?"
    hide screen s_head2  
    m "Well it's complicated..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna ".............."
    hide screen s_head2  
    m ".................."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "She's hot, isn't she?"
    hide screen s_head2  
    m "Smoking..."
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Gotcha."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">You and professor Snape share a bitter-sweet moment of complete male solidarity."
    ">The bond of your friendship strengthens."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
    
label date_with_snape_08:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "do you think if we wanted to..."
    sna "We could bring the public flogging back?"
    hide screen s_head2  
    m "What do you mean?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Well, years ago flogging was a completely acceptable measure of punishment for the students."
    sna "*Sigh* Simpler times..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_16.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "These days students just completely lack discipline..."
    sna2 "I would like nothing more than to publicly flog every single one of them..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Especially the girls..."
    hide screen s_head2  
    m "Hm... Fine by me..."
    m "But won't a reform like that attract unnecessary attention towards us?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Yes. You are right of course."
    sna "I am getting greedy..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I'm getting drunk with power, my friend!"
    sna2 "And this exquisite wine does not improve my judgment in the slightest either!"
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Professor Snape seems to be completely at ease around you now."
    ">The bond of male friendship between you twe strengthens even more.\n>\"Slytherin\" house point payouts have increased formidably..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return


label date_with_snape_09:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                                     # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "...so, after that I return back to Russia, right?"
    hide screen s_head2  
    g4 "Back to Russia?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "But wait, it gets worse."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Apparently I am fluent in Russian now."
    hide screen s_head2 
    g4 "Wait, what?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "And I am this miserable muggle guy who lives in this shithole of a town full of rundown buildings."
    sna2 "I try to make a living by drawing comics and creating games with \"Ren'Py\"..."
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "And that is so bizarre because I don't even know what a \"Ren'Py\" is!"
    hide screen s_head2  
    m "Hm... Then what happened?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Not much... Mostly worked my ass off for months..."
    sna2 "Then managed to create a relatively successful game somehow..."
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Eventually began to make decent money with my craft..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "And then, just when I was about to allow myself to feel hopeful about the future..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_04.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I woke up..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "...................."
    hide screen s_head2  
    m "......................"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What do you think all of that means?"
    hide screen s_head2  
    m "Sounds like another one of Akabur's self-inserts."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What?"
    hide screen s_head2  
    m "Just ignore the whole thing."
    m "A silly dream, nothing more."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Felt more like a nightmare..."
    hide screen s_head2  
    pause.1
    show screen blktone
    with d3
    ">Professor Snape trusts you more than he used to..."
    ">(To the point where he doesn't think twice about sharing his weird-ass dreams with you)."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
    
label date_with_snape_10:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_29.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What is the meaning of life, Genie?"
    hide screen s_head2  
    g4 "What?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Since you are an all-powerful being, you've got to know things like that, right?"
    hide screen s_head2  
    m "Maybe..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Great. Tell me then."
    hide screen s_head2  
    m "Hm... You sure you're ready for this?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Yes. Lay it on me, friend."
    hide screen s_head2  
    m "Alright then..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................!"
    hide screen s_head2  
    m "It's plastic..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I beg your pardon?"
    hide screen s_head2  
    m "it's plastic..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I don't get it..."
    hide screen s_head2  
    m "This planet plans to evolve into something else in a million years or so..."
    m "In order to do that it needs a special kind of material that it can't produce on it's own."
    m "So it spawns a new form of life - humans."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_11.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna ".............."
    hide screen s_head2 
    m "You wanted to know the purpose of your existence?"
    m "It's to produce plastic. Simple as that."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_30.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Are you fucking kidding me?!"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "No, no... That can't be it..."
    hide screen s_head2  
    g9 "He-he..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Are you pulling my leg?"
    hide screen s_head2  
    g9 "You should've seen your face."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_15.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "You really got me worried there, you bloody non-human bastard!"
    hide screen s_head2  
    g9 "I know! It was hard to resist..."
    show screen blktone
    with d3
    ">You spend the evening by skillfully avoiding a whole variety of similar questions."
    ">Despite your refusal to cooperate the bond of friendship between you two strengthens yet again."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return

label date_with_snape_11:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "So... Back in your world, do you people have a country named England?"
    hide screen s_head2  
    m "We used to..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What happened?"
    hide screen s_head2  
    m "\"The great catastrophe\"..."
    m "It incinerated most of the worlds population in a matter of hours..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "................"
    hide screen s_head2  
    m "Turning about eighty percent of the planet's surface into a scorching desert..."
    m "And the remaining twenty percent into an icy wasteland..."
    m "............."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "That is..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Horrible..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Are you sure that you want to return to that place?"
    hide screen s_head2  
    m "Of course."
    m "It may be a bit barbaric, but hey... it's home."
    show screen blktone 
    with d3
    ">Professor Snape finds a new level of respect for you..."
    ">The bond of friendship between you two solidifies."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_12:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "I've been thinking about what you've said the other day..."
    sna2 "About your home world being nothing but a scorched desert and all..."
    hide screen s_head2
    m "Yes?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "do You think Albus will be alright there?"
    hide screen s_head2
    m "Oh, absolutely!"
    m "Since I quite literally replaced him in his chair..."
    m "He probably replaced me in exactly the same place back in Agrabah."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Agrabah?"
    hide screen s_head2
    m "Yes... A very big city."
    m "One of the few that rose after the great catastrophe."
    m "Probably the biggest of them all as well..."
    m "the heart of the human civilization if you will."
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I am relieved to hear that..."
    hide screen s_head2
    m "Sure..."
    m "Although if your Albus friend really materialized in exactly the same spot I occupied before I casted the spell..."
    m "I suppose the princess could have him beheaded..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "WHAT?!"
    hide screen s_head2
    m "But the probabilty of that happening is very slim..."
    m "About five percent... Maybe ten... Twenty percent tops."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "......................................................."
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Professor Snape seems grateful to you for (sort of) putting his concerns about Albus Dumbledore's well-being to rest..."
    ">The bond of your friendship strengthens yet again..."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_13:
    show screen bld1
    with d3
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "You know what?"
    hide screen s_head2
    m "What?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "For the first time in a very long time..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_03.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I think..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "I am actually content with the way my life is going." # 0_0
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What an unsettling feeling..."
    hide screen s_head2
    m "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Could be."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Nonetheless, you may only be training just one girl..."
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "But it has a great impact on my life..."
    sna "And even the school itself..."
    hide screen s_head2
    m "In other words you are getting less broody and you blame me."
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Something like that..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_28.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I'm losing my dark presence, man." # :)
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Professor Snape really did become a little more cheerful lately..."
    ">He even looks younger now than back when you first met him..."
    ">Professor Snape's feeling of gratitude fortifies the bond of your friendship."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_14:
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "...so she says: \"Sir, could you choke me a little, please!\"."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "And I am happy to oblige of course!"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_19.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "So, I choke that little bitch while I'm fucking her, right?"
    sna2 "And she rolls her eyes up to the point where I can't even see her pupils anymore!"
    sna2 "Her face turns to a cute tint of purple and she's barely breathing."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_14.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "So I think that maybe I should loosen up my grip a little..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_21.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "And that's when the bitch starts to cum!"
    hide screen s_head2
    m "Sweet! And then you woke up?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "What? No, it actually happened."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I finally nailed that blond witch from \"Slytherin\"."
    hide screen s_head2
    g9 "Nice!"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_13.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I know."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_25.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "She is pretty twisted though..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_26.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "And I mean really fucking messed up."
    hide screen s_head2
    g9 "Our type of girl!"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_22.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Exactly!"
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">You and professor Snape bond over the similarities of your taste in women."
    ">The bond of your friendship has never been stronger."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    return
    
label date_with_snape_15:
    $ s_head_xpos = 330 # x = 330,                                                                              # SNAPE
    $ s_head_ypos = 380 #Right bottom corner: y = 340. y = 380 - no hand.       # SNAPE
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "It's been a while now..."
    hide screen s_head2
    m "What do you mean?"
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "The spell that brought you here..."
    sna "You said it would wear off in time..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Do you feel any different?"
    hide screen s_head2
    m "No... Not really..."
    m "Maybe it needs more time?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_01.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Could be..."
    sna "Or there could be something else..."
    hide screen s_head2
    m "Like what?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_09.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "No idea..."
    sna "But I shall give this some more thought..."
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Oh, and one more thing..."
    hide screen s_head2
    m "Hm...?"
    $ s_sprite = "01_hp/13_characters/snape/main/24.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "This time of the year is usually pretty busy..."
    sna2 "Even more so now when I need to constantly cover up for Albus' absence."
    hide screen s_head2
    m "..................."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "I'm not sure if I will be able to spend my evenings with leisurely drinking wine anymore..."
    hide screen s_head2
    m "Really?"
    $ s_sprite = "01_hp/13_characters/snape/main/snape_06.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Yes..."
    sna2 "I'll  still be around for a quick chat from time to time, but that's about it."
    hide screen s_head2
    m "I see..."
    m "I will have to find another way of spending my evenings from now on then..."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_02.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "I'm sure miss granger will be happy to help."
    hide screen s_head2
    m "Yes, for as long as \"slytherin\" is in the lead."
    $ s_sprite = "01_hp/13_characters/snape/main/snape_05.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna "Seriously? She still cares about that?"
    hide screen s_head2
    m "Very much so."
    $ s_sprite = "01_hp/13_characters/snape/main/23.png"                                         # SNAPE
    show screen s_head2                                                                                                 # SNAPE
    sna2 "Well in that case I shall personally ensure that \"slytherin\" house gets as many house points as possible."
    hide screen s_head2
    pause.1
    show screen blktone
    with d3
    ">Your friendship level with professor Snape reached itss maximum value."
    ">Congratulations. If this were a \"dating-sim\" you would be getting the ending with Severus Snape."
    ">The \"Slytherin\" house point payout has increased greatly and reached it's maximum level as well."
    call sly_plus
    hide screen blktone
    hide screen bld1
    with d3

    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    $ sfmax = True # Turns TRUE when friendship with Snape been maxed out.
    return


    
    
    
    
    
    
    
    
    
    
    
    
#    show screen bld1
#    with d3
#    $ renpy.play('sounds/win_04.mp3')   #Not loud.
#    hide screen notes
#    show screen notes
#    ">You spend the evening by hanging out with Professor Snape.\n>Your relationship with him has improved."
#    $ snape_friendship +=1
#    hide screen bld1
#    with d3

#    return
    
    
    
    
    
    
    
label sly_plus:
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    hide screen notes
    show screen notes
    ">The \"Slytherin\" house point payout has increased..."
    return