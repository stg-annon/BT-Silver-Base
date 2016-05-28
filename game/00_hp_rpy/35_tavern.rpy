label inn_menu:
    show bld1
    if inn_first:
        jump inn_intro
    abe "Welcome to the Hog's Head Inn"
    menu:
        "-Present Hermione to Aberforth-":
            m "I present you you're new barmaid."
            $ robeon = True
            $ stockings = 5
            $ custom_outfit_old = 5
            $ her_main("","body_07")
            pause
            abe "Well go on then girl, take the robe off."
            her "Fine..."
            $ robeon = False
            $ her_main("","body_33")
            pause
            hide screen hermione_main
            jump inn_menu
        "-Talk to Aberforth-":
            jump inn_talk
        "-Play Dice with Aberforth-":
            "Not added yet (will be soon)."
            jump inn_menu
        "-Leave-":
            jump return_office


label inn_intro: 
    m "Hello."
    abe "Hello Professor..."
    ">There is a sour tone in the mans voice."
    m "So what do you sell here?"
    abe "What do you want Albus?"
    m "(Albus? He must know the Professor.)"
    m "Just a drink."
    abe "You, drinking? I never thought that I'd see the day."
    m "Why's that?"
    abe "I never expected my little brother to lift his head out of the books long enough to come have a drink."
    m "(Brother?)"
    m "Well there's a first time for everything."
    abe "Hmmmph. Well we'll start you with a Butterbeer then. Anything stronger and you'll probably pass out."
    ">Aberforth pours you a large stein of a golden, frothy beer."
    ">You take a sip. It has a sweet almost sugary taste and a creamy consistency."
    m "That's not half bad, so how much do I owe you?"
    abe "Just tell me who you are."
    m "(Shit)"
    m "What do you mean."
    abe "I've never seen my brother drink Butterbeer in his life. Either you're not Albus or I'm a bowtruckle."
    m "Fine, you got me, I'm not Albus."
    abe "Then what are you doing in his skin?"
    m "I'm an all powerful genie from a magical world that accidentally made a potion that swapped the minds of me and your brother."
    abe "...."
    abe "That sounds convoluted."
    m "You're telling me."
    abe "So how long will it last?"
    m "No idea."
    abe "Well as far as I'm concerned this is nothing but an improvement."
    m "You don't like your brother that much?"
    abe "It's a long story."
    abe "Now how about a proper drink instead of that buttery crap."
    m "Sure."
    ">You drink well into the night, eventually staggering back to the castle"
    $ inn_first = False
    jump day_start
    
label inn_talk: #Responses to Genie asking Aberforth how he's doing
if day_random <= 2:
    "bla bla bla"
    jump inn_menu
elif day_random >= 3 and day_random <= 5:
    "bla bla bla"
    jump inn_menu
elif day_random >= 6 and day_random <= 8:
    "bla bla bla"
    jump inn_menu
elif day_random >=9:
    "bla bla bla"
    jump inn_menu