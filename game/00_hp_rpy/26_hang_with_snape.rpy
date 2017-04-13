label __init_variables:
    
    if not hasattr(renpy.store,'first_snape_with_wine'): #important!
        $ first_snape_with_wine = True
    
    return
    
label hang_with_snape:  ### HANGING WITH SNAPE ###
    
    show screen with_snape_animated
    play bg_sounds "sounds/fire02.mp3" fadeout 1.0 fadein 1.0 #Quiet...
    $ fire_in_fireplace = True
    hide screen genie
    hide screen chair_right
    hide screen desk
    show screen desk
    
    hide screen snape_main
    hide screen snape_02 #Snape stands still.
    hide screen bld1
    with d3
    
    with fade
   
    if snape_against_hermione: #(event_08) Turns True after event_08 (Hermione shows up for the first time).
        jump special_date_with_snape
    if snape_against_hermione_02: #(event_09) Activates after second visit from Hermione.
        jump special_date_with_snape_02
    
    if wine >= 1:
        call wine_with_snape
    
    if snape_friendship <= 98 and snape_events < 15:
        call date_with_snape
    else:
        show screen bld1
        with d3
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">You spend the evening hanging out with Professor Snape.\n>Your relationship with him has improved."
        hide screen bld1
        with d3
    
    $ snape_friendship +=1
   
    jump day_start
    
    
label wine_with_snape:
    if first_snape_with_wine:
        m "Look what I've got!"
        $ snape_SC.sayHead("Hm..?","snape_05")
        $ snape_SC.sayHead("Let me see...")
        
        pause.1
        $ the_gift = "01_hp/18_store/27.png" # WINE.
        show screen gift
        with d3
        ">You hand over the bottle you found in the cupboard to professor Snape..." 
        hide screen gift
        with d3
        
        $ snape_SC.sayHead("This one has got to be from Albus' personal stash!","snape_24")
        $ snape_SC.sayHead("Some pricey and incredibly rare stuff.","snape_06")
        m "Shall we then?"
        $ snape_SC.sayHead("We most certainly shall!","snape_02")
        $ first_snape_with_wine = False
    else:
        m "Look what I've got!"
        
        pause.1
        $ the_gift = "01_hp/18_store/27.png" # WINE.
        show screen gift
        with d3
        ">You hand over the bottle you fond in the cupboard to professor Snape..." 
        hide screen gift
        with d3
        
        $ snape_SC.sayHead("Another one?","snape_05")
        if one_of_ten == 1:
            $ snape_SC.sayHead("Splendid!","snape_02")
        elif one_of_ten == 2:
            $ snape_SC.sayHead("Alright!","snape_02")
        elif one_of_ten == 3:
            $ snape_SC.sayHead("Awesome!","snape_02")
        elif one_of_ten == 4:
            $ snape_SC.sayHead("Well done, my friend!","snape_02")
        elif one_of_ten == 5:
            $ snape_SC.sayHead("Did you find Albus' secret stash or was it his personal wine cellar?","snape_05")
        elif one_of_ten == 6:
            $ snape_SC.sayHead("lately I am having hard time drinking anything but this!","snape_02")
        elif one_of_ten == 7:
            $ snape_SC.sayHead("Great! I feel less stressed out already!","snape_02")
        elif one_of_ten == 8:
            $ snape_SC.sayHead("This just keeps getting better and better!","snape_02")
        elif one_of_ten == 9:
            $ snape_SC.sayHead("Seriously, how big is that stash?","snape_05")
        elif one_of_ten == 2:
            $ snape_SC.sayHead("It's sure good to be us! let's uncork that bastard!","snape_02")
        
    $ wine -= 1
    show screen bld1
    with d3
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">Your relationships with Professor Snape have improved."
    $ snape_friendship +=1
    hide screen bld1
    with d3
    
    return
    
label date_with_snape:
    
    show screen bld1
    with d3
    
    if snape_events == 0:
        m "Alright. Teach me your wand-based magic now."
        $ snape_SC.sayHead("Sure, I could do that...","snape_23")
        $ snape_SC.sayHead("Or I could tell you some more about those teenage \"slytherin\" sluts...","snape_02")
        g9 "The latter, please."
        $ snape_SC.sayHead("Great... Get a load of this then...","snape_13")
        
        pause.1
        show screen blktone
        with d3
        ">You spend the evening by discussing all sorts of inappropriate things with Porfessor Snape."
        $ renpy.play('sounds/win_04.mp3')   #Not loud.
        show screen notes
        ">You feel a faint bond forming between you two..."
    if snape_events == 1:
        m "For our little enterprise to succeed..."
        m "You need to be more generous with these house point things..."
        $ snape_SC.sayHead("Right, of course...","snape_09")
        $ snape_SC.sayHead("Miss Granger will require a strong incentive...")
        $ snape_SC.sayHead("So putting my house in the lead is essential...")
        $ snape_SC.sayHead("Could take time though...","snape_06")
        m "Take time?"
        m "Why not just award a couple of hundred points to \"Slytherin\" and be done with it?"
        $ snape_SC.sayHead("No, we need to be discreet with this...","snape_24")
        $ snape_SC.sayHead("Awarding a whole bunch of points to my house without any reason could draw in unnecessary attention...","snape_05")
        m "Hm... I see your point..."
        
        show screen blktone
        with d3
        ">You spend the evening by conspiring against Hermone with professor Snape..."
        ">The faint bond of friendship between you two strengthens."
    if snape_events == 2:
        $ snape_SC.sayHead("Have you heard of that \"men's rights movement\" nonsense?","snape_01")
        $ snape_SC.sayHead("What a nuisance that girl is...","snape_03")
        $ snape_SC.sayHead("She is smart, popular and has a will of iron...")
        $ snape_SC.sayHead("Lately I am starting to feel very doubtful about our whole plan...","snape_06")
        m "You shouldn't though..."
        $ snape_SC.sayHead("Is that so...","snape_26")
        m "It may take some time, but I {size=+5}will{/size} break her."
        m "Just trust me."
        $ snape_SC.sayHead("Alright...","snape_26")
        $ snape_SC.sayHead("What choice do I have but to hope for the best...?","snape_06")
        show screen blktone
        with d3
        ">You spend the evening by dreading the uncertain future with professor Snape."
        ">A faint bond of trust is forming between you two."
    if snape_events == 3:
        $ snape_SC.sayHead("Tell me something, Genie...","snape_24")
        m "Yes?"
        $ snape_SC.sayHead("Do you believe in the theory of parallel worlds?","snape_25")
        m "Well, it is hard not to. All things considered."
        $ snape_SC.sayHead("True...","snape_23")
        $ snape_SC.sayHead("So you think somewhere out there is another version of me?","snape_05")
        m "Probably..."
        $ snape_SC.sayHead("Hm...","snape_23")
        $ snape_SC.sayHead("Severus Snape - the ever cheerful white mage...")
        m "Sure, why not?"
        $ snape_SC.sayHead("What unsettling imagery you put into my mind...","snape_03")
        m "How about another version of that Granger girl?"
        $ snape_SC.sayHead("Yes! Hermione Granger - the repulsive slut without any dignity! Yes, I like it!","snape_02")
        m "And what if in that other world the cheerful Severus teams up with some bizarre version of me?"
        m "And maybe together we train the slut Hermione to be a proper girl and a good student?"
        $ snape_SC.sayHead("Ha-ha-ha! That's hilarious!","snape_28")
        pause.1
        show screen blktone
        with d3
        ">You spend the evening by discussing science, metaphysics, philosophy and sluts."
        ">the bond of friendship between you and Professor Snape strengthens."
    if snape_events == 4:
        $ snape_SC.sayHead("So... How is our little plan coming along?","snape_05")
        $ snape_SC.sayHead("Is that wretched girl giving you trouble?")
        menu:
            "\"Yeah. She's stubborn.\"":
                $ snape_SC.sayHead("No surprise there...","snape_06")
            "\"No, not really...\"":
                $ snape_SC.sayHead("Seriously?","snape_05")
                $ snape_SC.sayHead("Interesting...")
        $ snape_SC.sayHead("But you are positive you will be able to break her?","snape_01")
        m "Oh, absolutely."
        m "It may take some time though..."
        $ snape_SC.sayHead("Well, we do have time...","snape_06")
        $ snape_SC.sayHead("I mean you are still pretty much powerless, right?","snape_05")
        m "Yeah, pretty much..."
        $ snape_SC.sayHead("Splendid!","snape_02")
        m "......................."
        $ snape_SC.sayHead("I mean it is bad for {size=+5}you{/size}, but good for {size=+5}us{/size}, right?","snape_29")
        m "Right..."
        show screen blktone
        with d3
        ">Professor Snape seems to feel awkward about benefitting from your misery..."
        ">The bond of friendship between you two strengthens slightly..."
    if snape_events == 5:
        m "So, tell me about those \"slytherin\" sluts some more!"
        $ snape_SC.sayHead("What can I say? Life's been good to me lately, my friend.","snape_23")
        $ snape_SC.sayHead("These days I have a whole harem of skimpy students to choose from.","snape_22")
        g9 "Nice!"
        $ snape_SC.sayHead("Yes. Thanks to you, my friend I can do whatever the bloody hell I want!","snape_02")
        $ snape_SC.sayHead("And more importantly...")
        $ snape_SC.sayHead("Whoever the hell I want!","snape_13")
        m "Seriously?"
        $ snape_SC.sayHead("Well, sort of...","snape_09")
        $ snape_SC.sayHead("Obviously I don't actually walk around and \"do whoever I want\"...")
        $ snape_SC.sayHead("But you wouldn't believe what some of those girls are willing to do in exchange for house points!","snape_13")
        $ snape_SC.sayHead("Or even for the mere promise of good grades...","snape_22")
        pause.1
        show screen blktone
        with d3
        ">Professor Snape's usual cold exterior disintegrates before your eyes..."
        ">The bond of your friendship strengthens yet again..."
    if snape_events == 6:
        $ snape_SC.sayHead("So, back in your world you are some kind of all-powerful being?","snape_05")
        m "Yeah, sort of..."
        $ snape_SC.sayHead("Then how come you do the bidding of that Jasmine woman?","snape_05")
        m "Oh... Well..."
        m "...she is a princess."
        $ snape_SC.sayHead("So?","snape_05")
        $ snape_SC.sayHead("Is she your princess? You are not even human.")
        $ snape_SC.sayHead("Did you swear your loyalty to her?")
        m "Not really..."
        $ snape_SC.sayHead("Why do you even bother then?","snape_06")
        $ snape_SC.sayHead("The way I see it, you are an all-powerful being and she is just some muggle...","snape_09")
        m "She's a what?"
        $ snape_SC.sayHead("A human... She's just a human...","snape_25")
        $ snape_SC.sayHead("So why bother trying to please her?","snape_05")
        m "Well it's complicated..."
        $ snape_SC.sayHead("..............","snape_05")
        m ".................."
        $ snape_SC.sayHead("She's hot, isn't she?","snape_02")
        m "Smoking..."
        $ snape_SC.sayHead("Gotcha.","snape_23")
        pause.1
        show screen blktone
        with d3
        ">You and professor Snape share a bitter-sweet moment of complete male solidarity."
        ">The bond of your friendship strengthens."
    if snape_events == 7:
        $ snape_SC.sayHead("do you think if we wanted to...","snape_05")
        $ snape_SC.sayHead("We could bring the public flogging back?")
        m "What do you mean?"
        $ snape_SC.sayHead("Well, years ago flogging was a completely acceptable measure of punishment for the students.","snape_06")
        $ snape_SC.sayHead("*Sigh* Simpler times...")
        $ snape_SC.sayHead("These days students just completely lack discipline...","snape_16")
        $ snape_SC.sayHead("I would like nothing more than to publicly flog every single one of them...")
        $ snape_SC.sayHead("Especially the girls...","snape_22")
        m "Hm... Fine by me..."
        m "But won't a reform like that attract unnecessary attention towards us?"
        $ snape_SC.sayHead("Yes. You are right of course.","snape_29")
        $ snape_SC.sayHead("I am getting greedy...")
        $ snape_SC.sayHead("I'm getting drunk with power, my friend!","snape_28")
        $ snape_SC.sayHead("And this exquisite wine does not improve my judgment in the slightest either!")
        pause.1
        show screen blktone
        with d3
        ">Professor Snape seems to be completely at ease around you now."
        ">The bond of male friendship between you twe strengthens even more.\n>\"Slytherin\" house point payouts have increased formidably..."
    if snape_events == 8:
        $ snape_SC.sayHead("...so, after that I return back to Russia, right?","snape_24")
        g4 "Back to Russia?"
        $ snape_SC.sayHead("But wait, it gets worse.","snape_01")
        $ snape_SC.sayHead("Apparently I am fluent in Russian now.","snape_05")
        g4 "Wait, what?"
        $ snape_SC.sayHead("And I am this miserable muggle guy who lives in this shithole of a town full of rundown buildings.","snape_06")
        $ snape_SC.sayHead("I try to make a living by drawing comics and creating games with \"Ren'Py\"...")
        $ snape_SC.sayHead("And that is so bizarre because I don't even know what a \"Ren'Py\" is!","snape_24")
        m "Hm... Then what happened?"
        $ snape_SC.sayHead("Not much... Mostly worked my ass off for months...","snape_05")
        $ snape_SC.sayHead("Then managed to create a relatively successful game somehow...")
        $ snape_SC.sayHead("Eventually began to make decent money with my craft...","snape_24")
        $ snape_SC.sayHead("And then, just when I was about to allow myself to feel hopeful about the future...","snape_06")
        $ snape_SC.sayHead("I woke up...","snape_04")
        $ snape_SC.sayHead("....................","snape_09")
        m "......................"
        $ snape_SC.sayHead("What do you think all of that means?","snape_05")
        m "Sounds like another one of Akabur's self-inserts."
        $ snape_SC.sayHead("What?","snape_05")
        m "Just ignore the whole thing."
        m "A silly dream, nothing more."
        $ snape_SC.sayHead("Felt more like a nightmare...","snape_29")
        pause.1
        show screen blktone
        with d3
        ">Professor Snape trusts you more than he used to..."
        ">(To the point where he doesn't think twice about sharing his weird-ass dreams with you)."
    if snape_events == 9:
        $ snape_SC.sayHead("What is the meaning of life, Genie?","snape_29")
        g4 "What?"
        $ snape_SC.sayHead("Since you are an all-powerful being, you've got to know things like that, right?","snape_05")
        m "Maybe..."
        $ snape_SC.sayHead("Great. Tell me then.","snape_06")
        m "Hm... You sure you're ready for this?"
        $ snape_SC.sayHead("Yes. Lay it on me, friend.","snape_05")
        m "Alright then..."
        $ snape_SC.sayHead("................!","snape_01")
        m "It's plastic..."
        $ snape_SC.sayHead("I beg your pardon?","snape_05")
        m "it's plastic..."
        $ snape_SC.sayHead("I don't get it...","snape_25")
        m "This planet plans to evolve into something else in a million years or so..."
        m "In order to do that it needs a special kind of material that it can't produce on it's own."
        m "So it spawns a new form of life - humans."
        $ snape_SC.sayHead("..............","snape_11")
        m "You wanted to know the purpose of your existence?"
        m "It's to produce plastic. Simple as that."
        $ snape_SC.sayHead("Are you fucking kidding me?!","snape_30")
        $ snape_SC.sayHead("No, no... That can't be it...","snape_26")
        g9 "He-he..."
        $ snape_SC.sayHead("Are you pulling my leg?","snape_25")
        g9 "You should've seen your face."
        $ snape_SC.sayHead("You really got me worried there, you bloody non-human bastard!","snape_15")
        g9 "I know! It was hard to resist..."
        show screen blktone
        with d3
        ">You spend the evening by skillfully avoiding a whole variety of similar questions."
        ">Despite your refusal to cooperate the bond of friendship between you two strengthens yet again."
    if snape_events == 10:
        $ snape_SC.sayHead("So... Back in your world, do you people have a country named England?","snape_05")
        m "We used to..."
        $ snape_SC.sayHead("What happened?","snape_26")
        m "\"The great catastrophe\"..."
        m "It incinerated most of the worlds population in a matter of hours..."
        $ snape_SC.sayHead("................","snape_26")
        m "Turning about eighty percent of the planet's surface into a scorching desert..."
        m "And the remaining twenty percent into an icy wasteland..."
        m "............."
        $ snape_SC.sayHead("That is...","snape_26")
        $ snape_SC.sayHead("Horrible...","snape_06")
        $ snape_SC.sayHead("Are you sure that you want to return to that place?","snape_25")
        m "Of course."
        m "It may be a bit barbaric, but hey... it's home."
        show screen blktone 
        with d3
        ">Professor Snape finds a new level of respect for you..."
        ">The bond of friendship between you two solidifies."
    if snape_events == 11:
        $ snape_SC.sayHead("I've been thinking about what you've said the other day...","snape_09")
        $ snape_SC.sayHead("About your home world being nothing but a scorched desert and all...")
        m "Yes?"
        $ snape_SC.sayHead("do You think Albus will be alright there?","snape_06")
        m "Oh, absolutely!"
        m "Since I quite literally replaced him in his chair..."
        m "He probably replaced me in exactly the same place back in Agrabah."
        $ snape_SC.sayHead("Agrabah?","snape_05")
        m "Yes... A very big city."
        m "One of the few that rose after the great catastrophe."
        m "Probably the biggest of them all as well..."
        m "the heart of the human civilization if you will."
        $ snape_SC.sayHead("I am relieved to hear that...","snape_23")
        m "Sure..."
        m "Although if your Albus friend really materialized in exactly the same spot I occupied before I casted the spell..."
        m "I suppose the princess could have him beheaded..."
        $ snape_SC.sayHead("WHAT?!","snape_01")
        m "But the probabilty of that happening is very slim..."
        m "About five percent... Maybe ten... Twenty percent tops."
        $ snape_SC.sayHead(".......................................................","snape_03")
        pause.1
        show screen blktone
        with d3
        ">Professor Snape seems grateful to you for (sort of) putting his concerns about Albus Dumbledore's well-being to rest..."
        ">The bond of your friendship strengthens yet again..."
    if snape_events == 12:
        $ snape_SC.sayHead("You know what?","snape_01")
        m "What?"
        $ snape_SC.sayHead("For the first time in a very long time...","snape_01")
        $ snape_SC.sayHead("I think...","snape_03")
        $ snape_SC.sayHead("I am actually content with the way my life is going.","snape_25") # 0_0
        $ snape_SC.sayHead("What an unsettling feeling...","snape_26")
        m "Are you sure that this is not some euphoric trance state caused by all the sex you've been having lately?"
        $ snape_SC.sayHead("Could be.","snape_22")
        $ snape_SC.sayHead("Nonetheless, you may only be training just one girl...","snape_09")
        $ snape_SC.sayHead("But it has a great impact on my life...","snape_24")
        $ snape_SC.sayHead("And even the school itself...")
        m "In other words you are getting less broody and you blame me."
        $ snape_SC.sayHead("Something like that...","snape_23")
        $ snape_SC.sayHead("I'm losing my dark presence, man.","snape_28") # :)
        pause.1
        show screen blktone
        with d3
        ">Professor Snape really did become a little more cheerful lately..."
        ">He even looks younger now than back when you first met him..."
        ">Professor Snape's feeling of gratitude fortifies the bond of your friendship."
    if snape_events == 13:
        $ snape_SC.sayHead("...so she says: \"Sir, could you choke me a little, please!\".","snape_02")
        $ snape_SC.sayHead("And I am happy to oblige of course!","snape_13")
        $ snape_SC.sayHead("So, I choke that little bitch while I'm fucking her, right?","snape_19")
        $ snape_SC.sayHead("And she rolls her eyes up to the point where I can't even see her pupils anymore!")
        $ snape_SC.sayHead("Her face turns to a cute tint of purple and she's barely breathing.")
        $ snape_SC.sayHead("So I think that maybe I should loosen up my grip a little...","snape_14")
        $ snape_SC.sayHead("And that's when the bitch starts to cum!","snape_21")
        m "Sweet! And then you woke up?"
        $ snape_SC.sayHead("What? No, it actually happened.","snape_05")
        $ snape_SC.sayHead("I finally nailed that blond witch from \"Slytherin\".","snape_13")
        g9 "Nice!"
        $ snape_SC.sayHead("I know.","snape_13")
        $ snape_SC.sayHead("She is pretty twisted though...","snape_25")
        $ snape_SC.sayHead("And I mean really fucking messed up.","snape_26")
        g9 "Our type of girl!"
        $ snape_SC.sayHead("Exactly!","snape_22")
        pause.1
        show screen blktone
        with d3
        ">You and professor Snape bond over the similarities of your taste in women."
        ">The bond of your friendship has never been stronger."    
    if snape_events == 14:
        $ snape_SC.sayHead("It's been a while now...","snape_05")
        m "What do you mean?"
        $ snape_SC.sayHead("The spell that brought you here...","snape_24")
        $ snape_SC.sayHead("You said it would wear off in time...")
        $ snape_SC.sayHead("Do you feel any different?","snape_05")
        m "No... Not really..."
        m "Maybe it needs more time?"
        $ snape_SC.sayHead("Could be...","snape_01")
        $ snape_SC.sayHead("Or there could be something else...")
        m "Like what?"
        $ snape_SC.sayHead("No idea...","snape_09")
        $ snape_SC.sayHead("But I shall give this some more thought...")
        $ snape_SC.sayHead("Oh, and one more thing...","snape_24")
        m "Hm...?"
        $ snape_SC.sayHead("This time of the year is usually pretty busy...","snape_24")
        $ snape_SC.sayHead("Even more so now when I need to constantly cover up for Albus' absence.")
        m "..................."
        $ snape_SC.sayHead("I'm not sure if I will be able to spend my evenings with leisurely drinking wine anymore...","snape_06")
        m "Really?"
        $ snape_SC.sayHead("Yes...","snape_06")
        $ snape_SC.sayHead("I'll  still be around for a quick chat from time to time, but that's about it.")
        m "I see..."
        m "I will have to find another way of spending my evenings from now on then..."
        $ snape_SC.sayHead("I'm sure miss granger will be happy to help.","snape_02")
        m "Yes, for as long as \"slytherin\" is in the lead."
        $ snape_SC.sayHead("Seriously? She still cares about that?","snape_05")
        m "Very much so."
        $ snape_SC.sayHead("Well in that case I shall personally ensure that \"slytherin\" house gets as many house points as possible.","snape_23")
        pause.1
        show screen blktone
        with d3
        ">Your friendship level with professor Snape reached itss maximum value."
        ">Congratulations. If this were a \"dating-sim\" you would be getting the ending with Severus Snape."
        ">The \"Slytherin\" house point payout has increased greatly and reached it's maximum level as well."
        $ sfmax = True # Turns TRUE when friendship with Snape been maxed out.
    
    
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    ">The \"Slytherin\" house point payout has increased..."
    
    hide screen blktone
    hide screen bld1
    with d3
    
    $ snapes_support += 1 #Controls how much points is awarded to SLYTHERIN daily.
    $ snape_events += 1 #Makes sure this event will happen only once. Also triggers next event with Snape.
    
    return
    
### SPECIAL DATE 01 ###
label special_date_with_snape: #TAKES PLACE AFTER FIRST VISIT FROM HERMIONE.
    show screen with_snape
    $ snape_against_hermione = False #Turns True after event_08. Activates special event (THIS EVENT) when hanging out with Snape next time.
    $ snape_SC.say_H("...........................","head_2")
    m "...............................?"
    $ snape_SC.say_H("I hate her so much...","head_3")
    menu:
        "\"Yeah! That bitch!\"":
            $ snape_SC.say_H("Good to know that we are on the same page...","head_1")
            $ snape_SC.say_H("That girl...","head_2")
        "\"You hate who?\"":
            $ snape_SC.say_H("Why would you ask that?","head_1")
            $ snape_SC.say_H("That Hermione girl of course!","head_1")
        "\"Is she that bad?\"":
            $ snape_SC.say_H("She is the worst!","head_1")

    $ snape_SC.say_H("A top student...","head_2")
    $ snape_SC.say_H("Leads all sorts of extracurricular activities and clubs...","head_3")
    $ snape_SC.say_H("the president of the school's Student Representative Body...","head_3")
    $ snape_SC.say_H("Likely to become the head girl soon...","head_3")
    $ snape_SC.say_H("................","head_2")
    $ snape_SC.say_H("............","head_3")
    with hpunch
    $ snape_SC.say_H("{size=+7}I hate that fucking witch!!!{/size}","head_5")
    g4 "{size=-4}(What the...?){/size}"
    $ snape_SC.say_H("..............","head_2")
    $ snape_SC.say_H("She used to be just an annoyance, but these days...","head_2")
    $ snape_SC.say_H("She became a fully fledged menace...","head_1")
    $ snape_SC.say_H("That witch is officially my least favorite student in the entire school now...","head_1")
    m "What about that Potter boy?"
    $ snape_SC.say_H("The Potter boy? Ha! Who's that!?","head_6")
    $ snape_SC.say_H("No I'm serious...","head_1")
    $ snape_SC.say_H("I will go as far as to say that Potter jr. and his wretched father combined...","head_1")
    $ snape_SC.say_H("Didn't cause me nearly as much grief as this little witch does lately...","head_1")
    m "Now, now, we both know that's not true..."
    $ snape_SC.say_H("Yeah... You're probably right...","head_2")
    $ snape_SC.say_H("That bastard James Potter really did a number on me--","head_7")
    $ snape_SC.say_H("Wait, how do you know this?","head_6")
    m "Well... I've read the books..."
    $ snape_SC.say_H("What? What books?","head_6")
    m "Nah, never-mind. I'm a genie, remember? I know things..."
    $ snape_SC.say_H("Hm... And yet you need me to teach you stuff...","head_9")
    m "Well, I told you, my magic is acting up in your world..."
    $ snape_SC.say_H("Sure, sure...","head_9")
    m "......"
    m "She came by the other day..."
    $ snape_SC.say_H("Who did?","head_10")
    m "The Hermione girl..."
    $ snape_SC.say_H("What?!","head_1")
    $ snape_SC.say_H("I thought we agreed on the \"no human contact\" rule.","head_2")
    $ snape_SC.say_H("(Even though lately I've been wondering whether or not she is human at all...)","head_7")
    m "I know... She kinda forced her way in..."
    $ snape_SC.say_H("I imagine she did...","head_1")
    $ snape_SC.say_H("What did she want?","head_1")
    
    if jerk_off_session:
        m "I'm not sure..."
        $ snape_SC.say_H("??","head_11")
        m "I've been jerking off during the entire time she was talking..."
        $ snape_SC.say_H("You've been...","head_2")
        $ snape_SC.say_H("... doing what?","head_2")
        m "Hey, don't judge me!"
        m "You don't know what it's like to be cooped up in this tower like a prisoner!"
        $ snape_SC.say_H("You... y-you....","head_2")
        $ snape_SC.say_H("......","head_12")
        $ snape_SC.say_H("Ha.... ha-ha... HA-HA-HA!!!","head_15")
        m "Wha..? What did I say?"
        $ snape_SC.say_H("Ha-ha-ha! You are amazing!","head_14")
        $ snape_SC.say_H("Are all genies so... wonderfully nihilistic?","head_9")
        m "Yeah... We immortals tend to not give a fuck."
        $ snape_SC.say_H("Understandable...","head_9")
        $ snape_SC.say_H("Unfortunately, us mere mortal cannot afford such luxury...","head_10")
        
    else:
        m "Not sure... She's been talking a lot..."
        m "Something about some \"greefeendo\" points... and..."
        m "Er... I wasn't paying attention to be honest..."
        $ snape_SC.say_H("Nah... Probably another load of self righteous crap...","head_1")
        $ snape_SC.say_H("She is famous for that...","head_7")
    

    $ snape_SC.say_H("I have a class early tomorrow, so let us call it a night.","head_7")
    m "What about you teaching me magic and stuff?"
    $ snape_SC.say_H("Yeah, absolutely...","head_10")
    $ snape_SC.say_H("Next time...","head_10")
    m "Alright..."
    
    

    
    $ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    
    jump day_start
    
### SPECIAL DATE 02 ###    
label special_date_with_snape_02: #TAKES PLACE AFTER SECOND VISIT FROM HERMIONE. (Where she says that she sent letter to the ministry.)
    show screen with_snape
    show screen bld1
    with d5
    #$ snape_against_hermione = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.
    m "......................."
    m "Hermione Granger came by again..."
    $ snape_SC.say_H("Don't mention the witch's name when I'm off duty...","head_1")
    $ snape_SC.say_H("...............","head_2")
    $ snape_SC.say_H("Dammit! I am a grown man, Albus!","head_3")
    m "My name is not--"
    $ snape_SC.say_H("An esteemed wizard...","head_3")
    m "Well, alright, let it out..."
    $ snape_SC.say_H("How come one tiny....cunt, is able to cause me so much grief?!","head_2")
    $ snape_SC.say_H("I thought with you as my ally I will have a chance to--","head_4")
    m "To unclench?" 
    $ snape_SC.say_H("Yeah, that could be the word...","head_2")
    $ snape_SC.say_H("But all I did was give her more leverage to harass me with...","head_16")
    $ snape_SC.say_H("She's even turning the teachers against me now...","head_16")
    $ snape_SC.say_H(".................","head_3")
    $ snape_SC.say_H("She must go...","head_7")
    m "What do you mean?"
    with hpunch
    $ snape_SC.say_H("{size=+6}I will have to kill her!{/size}","head_5")
    g4 "Like literally kill her?"
    $ snape_SC.say_H("Do I have any other choice?","head_6")
    m "You're joking, right?"
    $ snape_SC.say_H("Am i?!","head_6")
    $ snape_SC.say_H("Can you do this for me?","head_11")
    m "Em..."
    m "As much I would \"enjoy\" murdering a teenage girl..."
    m "Genies can't kill..."
    $ snape_SC.say_H("Rats!","head_7")
    m "And we frown upon murderers..."
    if jerk_off_session:
        $ snape_SC.say_H("Really? I thought you didn't give a fuck...","head_17")
        m "to a certain degree..."
        $ snape_SC.say_H(".............","head_7")
    $ snape_SC.say_H("Well... don't mind me then...","head_2")
    $ snape_SC.say_H("I'm all talk...","head_2")
    $ snape_SC.say_H("I would never actually harm a student...","head_2")
    $ snape_SC.say_H("(...permanently that is.)","head_3")
    m "Listen, if she bugs you so much, why not just find a less radical way to deal with her?"
    $ snape_SC.say_H("Nah... Flogging has been outlawed years ago...","head_7")
    m "That's not what I mean..."
    $ snape_SC.say_H("Huh?","head_1")
    m "She is a top student, right?"
    $ snape_SC.say_H("Yes, damn her. The girl is a hard-worker, I give her that.","head_2")
    m "She also has a reputation for being self righteous."
    $ snape_SC.say_H("Oh, yes!","head_6")
    m "And she thinks that she is better than everyone else..."
    $ snape_SC.say_H("Where are you going with this?","head_17")
    m "Well it seems like all of her power comes from her reputation..."
    $ snape_SC.say_H("......................?","head_11")
    m "What if we take that away from her?"
    $ snape_SC.say_H("That would shut her up I suppose...","head_10")
    $ snape_SC.say_H("But how? She's practically a saint.","head_2")
    $ snape_SC.say_H("Even students who hate her secretly admire her.","head_7")
    $ snape_SC.say_H("She didn't fail a single test in her entire time here...","head_2")
    $ snape_SC.say_H("She is always ahead of the schedule...","head_2")
    $ snape_SC.say_H("Damn, how I hate it when she corrects me during my classes...","head_3")
    $ snape_SC.say_H("And thanks to her the \"Gryffindor\" house is way ahead of everybody else now...","head_6")
    $ snape_SC.say_H("Even \"Slytherin\" is no match for them this year...","head_7")
    $ snape_SC.say_H("........................","head_16")
    $ snape_SC.say_H("Dammit... I need more wine...","head_6")
    m "The wine could wait. Hear me out first!"
    $ snape_SC.say_H("Huh...?","head_1")
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    label fuck_off:
    m "Hm... Let us..."
    menu:
        m "..."
        "{size=-3}\"Make sure she is not a top student any longer!\"{/size}" if not d_flag_01:
            $ d_flag_01 = True
            $ snape_SC.say_H("What? You mean grade her unfairly?","head_1")
            $ snape_SC.say_H("Nah... Dumbledore would never allow--","head_2")
            $ snape_SC.say_H("Wait a second!","head_9")
            m "Exactly!"
            $ snape_SC.say_H("You're right! I grade her tests unfairly! I could even make other teachers do the same!","head_18")
            $ snape_SC.say_H("I could say that the order comes from you...","head_18")
            $ snape_SC.say_H("And when the real Dumbledore shows up I will pretend that I had no idea that he was away...","head_19")
            m "Works for me."
            $ snape_SC.say_H("Er...","head_10")
            $ snape_SC.say_H("This is still you, genie, right?","head_10")
            m "Yeah, yeah, still here..."
            $ snape_SC.say_H("OK, good.","head_18")
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off
        "{size=-3}\"Make sure \"Gryffindor\" loses the cup this year!\"{/size}" if not d_flag_02:
            $ d_flag_02 = True
            $ snape_SC.say_H("You mean to just start subtracting points from them for no good reason?","head_1")
            $ snape_SC.say_H("Oh, I like that!","head_18")
            $ snape_SC.say_H("There are a couple of \"Slytherin\" girls who are long overdue for receiving some extra house points as well.","head_20")
            $ snape_SC.say_H("Oh, this will work out magnificently!","head_19")
            $ snape_SC.say_H("You are a Genius!","head_18")
            m "Yes, I am a genius genie. What are the odds of that..."
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

        "{size=-3}\"Ruin her reputation!\"{/size}" if not d_flag_03:
            $ d_flag_03 = True
            $ snape_SC.say_H("Tarnish her reputation?","head_1")
            $ snape_SC.say_H("But the girl is incorruptible...","head_1")
            m "Nonsense!"
            m " All we need to do is convince her that she needs to make some sacrifices \"for the greater good\"."
            $ snape_SC.say_H("Oh, but of course...","head_9")
            $ snape_SC.say_H("She would gladly \"Get her hands dirty\" to save the honour of her precious \"Gryffindor\" house!","head_21")
            $ snape_SC.say_H("And when she does, we will have the leverage we need...","head_9")
            if d_flag_01 and d_flag_02 and d_flag_03:
                pass
            else:
                jump fuck_off

    $ snape_SC.say_H("This could actually work!","head_9")
    m "I think so too."
    $ snape_SC.say_H("Oh, I feel so alive tonight!","head_19")
    $ snape_SC.say_H("Pour me another goblet!","head_15")
    $ snape_SC.say_H("The \"Defence Against the Dark Arts\" class will start late tomorrow!","head_19")
    m "....."
    m "Don't you think this is a bit too brutal though?"
    m "I mean, she's just a girl..."
    $ snape_SC.say_H("Just a girl?","head_8")
    $ snape_SC.say_H("Oh no, no, no...","head_8")
    $ snape_SC.say_H("She is the embodiment of pure evil!","head_4")
    $ snape_SC.say_H("If we don't do this now...","head_2")
    $ snape_SC.say_H("One of those days I may just snap and \"Avada Kedavra\" her!","head_3")
    m "You'll do what?"
    $ snape_SC.say_H("Murder her for real!","head_4")
    m "Alright, alright... got it."
    m "Let's choose the lesser of the two evils then."
    $ snape_SC.say_H("Yes...","head_7")
    $ snape_SC.say_H("Now, pour me some more wine.","head_6")

    ">You spend rest of the evening in Snape's company drinking your worries away."
    
    $ snape_against_hermione_02 = False #Turns True after event_10. Activates special event (THIS EVENT) when hanging out with Snape next time.   
    $ hermione_is_waiting_02 = True #Triggers another visit from Hermione. (Event_11)
   

    #$ hermione_is_waiting_01 = True #Triggers another visit from Hermione. (Event_09)
    hide screen bld1
    with d3
    $ days_without_an_event = 0 #Making sure next even will not start right away.
    jump day_start
    
    
    
    
####Snape bonus###
#label snape_bonus:
#    if snape_events == 1:
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=3
#            "Slytherin got +3 points as a Snape-Bonus."
    
#    if snape_events == 2:#WEEK No.2
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=7
#            "Slytherin got +7 points as a Snape-Bonus."
    
#    if snape_events == 3:#WEEK No.3
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=10
#            "Slytherin got +10 points as a Snape-Bonus."
            
#    if snape_events == 4:#WEEK No.4
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=12
#            "Slytherin got +12 points as a Snape-Bonus."
            
#    if snape_events == 5:#WEEK No.5
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=16
#            "Slytherin got +16 points as a Snape-Bonus."
            
#    if snape_events == 6:#WEEK No.6
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=22
#            "Slytherin got +22 points as a Snape-Bonus."
            
#    if snape_events == 7:#WEEK No.7
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=26
#            "Slytherin got +26 points as a Snape-Bonus."
            
#    if snape_events == 8:#WEEK No.8
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=32
#            "Slytherin got +32 points as a Snape-Bonus."
            
#    if snape_events == 9:#WEEK No.9
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=36
#            "Slytherin got +36 points as a Snape-Bonus."
            
#    if snape_events == 10:#WEEK No.10
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=43
#            "Slytherin got +43 points as a Snape-Bonus."
            
#    if snape_events == 11:#WEEK No.11
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=46
#            "Slytherin got +46 points as a Snape-Bonus."
            
#    if snape_events == 12:#WEEK No.12
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=50
#            "Slytherin got +50 points as a Snape-Bonus."
            
#    if snape_events == 13:#WEEK No.13
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=56
#            "Slytherin got +56 points as a Snape-Bonus."
            
#    if snape_events == 14:#WEEK No.14
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=61
#            "Slytherin got +61 points as a Snape-Bonus."
            
#    if snape_events == 15:#WEEK No.15
#        if generating_snape_bonus == 1:
#            pass
#        elif generating_snape_bonus == 2:
#            $ slytherin +=66
#            "Slytherin got +66 points as a Snape-Bonus."

#return