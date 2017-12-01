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
    hat "then you Put me on their head and we'll have some fun."
    hat "Until then..."
    m "What?"
    hat "{size=+5}z{/size}{size=+4}z{/size}{size=+3}z{/size}{size=+2}z{/size}{size=+1}z{/size}"
    m "Oh..."
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

label hat_intro_3: #Luna change scene 
    $ renpy.play('sounds/knocking.mp3')
    "*knock* *knock* *knock*"
    lun "It's Luna Lovegood sir..."
    m "come in, come in..."
    $ renpy.play('sounds/door.mp3')
    ">Luna stands in front of you."
    $ luna_chibi("stand")
    call luna_main("Hermione said you wanted to see me?", 1, 2, 1, 2)
    m "Yes. It's about your school house."
    call luna_main("Ravenclaw?", 1, 1, 5, 2)
    m "Yes. I've been speaking with the sorting hat recently and I've been worried that he may have gotten a few student's houses wrong over the years."
    call luna_main("Really? So am I going to have to change house?", 1, 1, 4, 3)
    m "Of course not!"
    call luna_main("*Phew*!", 2, 1, 1, 1)
    m "I just wanted to put the hat on your head to see if he made the right choice."
    call luna_main("oh, alright then!", 1, 2, 1, 1)
    ">You turn around and reach for the hat."
    m "Almost there... Just grab the edge of it..."
    hat "Careful!"
    ">You pull the heavy hat down of the cupboard."
    hat "*Psst*{size=-5}Nice work! Now just put me on her head.{/size}"
    m "Here we are Miss Lovegood..."
    ">You place the hat gingerly on her head."
    call luna_main("...", 1, 2, 1, 3)
    call luna_main("Is it-", 1, 2, 5, 3)
    hat "{size=+5}HMMMM{/size}yes... {size=-5}yes...{/size} I see. Very interesting... {size=+5}Very{/size}{p} {size=+5}interesting...{/size}"
    call luna_main("What's interesting?", 1, 1, 5, 2)
    hat "What? Oh nothing, nothing. Just close your eyes, try and get a bit of sleep..."
    call luna_main("Sleep?", 6, 2, 5, 2)
    call luna_main("Why would I... want{p} to...", 3, 1, 4, 2)
    call luna_main("...", 1, 6, 4, 2) #hypno eyes
    m "is she alright?"
    hat "She's fine. Just having a bit of a rest. Now about that personality..."
    hat "Oh yes... Hmmmm, {p}well I suppose that could work..."
    hat "{size=-5}yes... I'm sure salazar would be proud...{/size}"
    hat "Just a little longer..."
    call luna_main("...", 1, 6, 4, 2) #hypno eyes
    call luna_main("...", 1, 6, 1, 2) #hypno eyes
    $ luna_unlocked = True
    call luna_main("...", 1, 6, 1, 2) #hypno eyes
    m "Wait what happened?! Her eyes just changed color!"
    hat "Really? Hmmm... didn't expect that... what color are they?"
    m "Green."
    hat "Well that seems rather fitting."
    m "Why, what did you do to her personality?"
    hat "Not much, just made it a bit more Snake like..."
    m "What now."
    hat "Well she's going to be a little... out of sorts..."
    hat "It would probably be in your best interests to send her to her room and let her sleep it off."
    m "Will she be able to hear me?"
    hat "Yes, she's in a fairly... lucid state..."
    ">You take the hat off of Luna's head."
    m "Thank you very much Miss Lovegood. I think you better be off to bed now "
    call luna_main("yes... bed...", 1, 6, 1, 2) #hypno eyes
    call luna_away

    ">You place the hat back on the cupboard"
    m "So what did you do to her personality?"
    hat "Now now... no sense ruining the fun. You'll just have to wait..."
    m "Hmmph"
    $ luna_busy = True
    ">Luna can now be summoned from the door!"
    return




###Need another intro event here, introducing Luna and setting up the favour selling stuff.

