label hat_intro:
    $ hat_known = True
    who2 "Hey."
    m "What? who said that?"
    menu:
        "-Look behind you-":
            ">You turn around and look in the general direction of the voice."
            m "There's no one there..."
            who2 "..."
            who2 "You're looking straight at me Dumbledore."
        "-Look under the desk-":
            ">You take a quick look under your desk."
            m "There's no one there..."
            who2 "......"
            who2 "Behind you."
            ">You turn around."
            g4 "Who's there?! {p} Show yourself!"
            who2 "You're looking straight at me Dumbledore."
    hat "Or should I say Genie."
    g4 "(The hat is talking!)"
    m "(Wait, is it supposed to talk? Is this normal?)"
    m "What do you want...{p} hat?"
    hat "I'm the {size=+5}sorting{/size} hat, and I Just want to talk."
    m "Well go ahead then, it's not like I've got anything better to do in this room."
    hat "So, about what you've been doing to Hermione Granger..."
    m "Oh, that, Ummmmmm... It's not what it-"
    hat "I want in."
    g4 "What?"
    hat "I want to help you corrupt another girl."
    m "Another girl?"
    hat "Well it wouldn't be much fun messing around with the Granger girl anymore, she's too far gone."
    m "so What's in it for you hat?"
    hat "Entertainment. Do you understand how boring it is to sit in this room all day, staring at the wall with nothing to do..."
    m "..."
    hat "Oh, yeah... Well you should appreciate my offer to fight off the boredom for you then."
    m "And how do you plan to \'corrupt a girl\' from up there on the shelf?"
    hat "I'm the sorting hat, I sort people."
    m "..."
    m "and How does that help?"
    hat "well Normally I'm placed on student's heads at the beginning of the year."
    hat "I then read their personality using Legilimency to decide what house they go in."
    m "and how does that help us?"
    hat "Well I can do more than just read personalities, I can alter them as well."
    g9 "Really?"
    hat "Well I mean in theory... The real Dumbledore never let me try it out. Not even on \'him\'."
    g9 "So you're saying if I get a student in here you can turn them into whatever I want?"
    hat "To an extent."
    m "what's that supposed to mean?"
    hat "I can change what house their in, and their personalities will change to suit that, but I can't completely alter a person's mind."
    m "So I still have to do all the hard work?"
    hat "If you call sexually harassing teens hard work..."
    m "I'll think about it."
    hat "Go ahead, I'm sure you'll have plenty of time to think it over while you sit there by yourself..."
    hat "But... {p}if you want to have some real fun, get that brat Miss Granger to bring one of her slutty little friends up here."
    hat "Until then..."
    m "What?"
    hat "zzz..."
    m "Oh."
    return

    

label hat_intro_2: #Bringing in Hermione
    m "[hermione_name], I wanted to talk to you about something."
    call her_main("Whats that [genie_name]?","body_14")
    m "Do you feel that any of your friends are in the wrong house?"
    call her_main("What do you mean In the wrong house?","body_15")
    m "well, do you know anyone who'd be better suited being in a different house?"
    call her_main("That's a weird question [genie_name].","body_02")
    call her_main("I suppose that Neville Longbottom isn't very courageous, Maybe he'd be better off in \"Hufflepuff\"...","body_08")
    m "(Probably don't want him...)"
    m "Anyone else come to mind?"
    call her_main("I don't think so...","body_10")
    m "Oh well, just-"
    call her_main("Wait, I know! Luna Lovegood!","body_30")
    m "And why is that?"
    call her_main("Well surely you've seen her grades [genie_name]...","body_16")
    call her_main("Suffice to say, she's hardly \"Ravenclaw\" material. She'd probably be better suited to \"Hufflepuff\" as well.","body_17")
    m "Fantastic. Could you please tell her to come to my office later this afternoon?"
    call her_main("Why? You're not going to ask her for favours are you?","body_50")
    m "Nothing of the sort. This is strictly school business."
    call her_main("...","body_50")
    call her_main("Fine... Just don't do anything too bad...","body_17")
    m "Scouts honor!"
    call her_main("Well if that's all then [genie_name], I better head to class.","body_16")

    jump end_hg_pf

label hat_intro_3: #Luna change scene TODO






