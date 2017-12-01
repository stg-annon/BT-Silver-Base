label luna_reversion_event:
    m "{size=-4}(I'll just ask for a quick tug...){/size}"
    if luna_corruption <= 10: #FIRST TIME
        if luna_corruption <= 9:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        if luna_sub > luna_dom: #Sub intro
            m "[luna_name]..."
            call luna_main("yes [l_genie_name]...", 6, 1, 2, 3)
            m "Do you know what a handjob is?"
            call luna_main("What?", 6, 1, 2, 3)
            m "It's where you wrap your hand around-"
            call luna_main("I know what they are!", 6, 1, 2, 3)
            m "Fantastic!"
            call luna_main("...", 6, 1, 2, 3)

        else: #Dom intro
            m "[luna_name]?"
            call luna_main("yes [l_genie_name]...", 1, 2, 2, 2) 
            m "Do you happen to know what a handjob is?"
            call luna_main("...", 7, 1, 2, 2)
            m "..."
            m "Well if it's not too much trouble..."
            call luna_main("...", 7, 2, 2, 2) 
            call luna_main("Go on...", 7, 2, 2, 2) 
        menu:
            "-Tell her to give you a handjob-" if luna_sub >= 7:
                $ current_payout = 80
                if luna_sub <= 8:
                    $ luna_sub += 1
                $ luna_choice = 1
                m "Well seeing as how you're familiar with the concept, how about a practical demonstration."
                call luna_main("...", 6, 2, 2, 3) 
                call luna_main("Really? You expect me to {size=+5}touch{/size} that filthy cock of yours?", 8, 2, 1, 2) 
                call luna_main("It's bad enough that I have to stand here while you touch yourself...", 4, 2, 5, 3)
                call luna_main("But that's where I draw the line [l_genie_name]!", 4, 2, 5, 3)
                m "Hmmm{p}, well alright then, I'm not going to force you into anything."
                call luna_main("Thank you...", 4, 2, 5, 3)
                m "Well that will be all for today Ms Lovegood, you may leave now."
                call luna_main("Alright [l_genie_name]...", 4, 2, 5, 3)
                call luna_main("(Good work finally standing up to him!)", 4, 2, 5, 3)
                ">Luna turns around to leave your office."
                m "Oh, one last thing..."
                call luna_main("...", 6, 3, 4, 2) 
                m "Could you send the first \'slytherin\' girl you see to my office?"
                call luna_main("What! Why?", 6, 3, 4, 3) 
                m "Well seeing as how you're not able to give me a little attention, I figure that one of those \'slytherin\' sluts will."
                m "They'll probably even do it for half the price..." 
                call luna_main("...", 6, 3, 4, 3) 
                call luna_main("......", 6, 3, 4, 3)
                $ luna_tears = 1 
                call luna_main(".........", 6, 3, 4, 3) 
                call luna_main("{size=-5}Fine{/size}...", 6, 3, 4, 3) 
                m "What was that [luna_name]?"
                call luna_main("{size=+5}Fine!{/size} I'll jerk that disgusting, old, filthy, wrinkly old cock of yours!", 6, 3, 4, 3) 
                m "Fantastic! Let me just stand up."
                call luna_main("You're despicable...", 6, 3, 4, 3) 

            "-Ask for a handjob-" if luna_sub > luna_dom:
                $ current_payout = 120
                if luna_sub <= 8:
                    $ luna_sub += 1
                $ luna_choice = 2
                m "Well seeing as how you're familiar with the concept..."
                call luna_main("...", 6, 2, 2, 3) 
                call luna_main("Really? You expect me to {size=+5}touch{/size} that filthy cock of yours?", 8, 2, 1, 2) 
                call luna_main("It's bad enough that I have to stand here while you touch yourself...", 4, 2, 5, 3)
                m "There'll be a hefty reward..."
                call luna_main("...", 6, 3, 4, 3) 
                call luna_main("......", 6, 3, 4, 3)
                call luna_main("I expect that my father's magazine will also sell a few more copies...", 6, 3, 4, 3) 
                m "Of course..."
                call luna_main("Fine...", 6, 3, 4, 3) 
                m "Fantastic! Let me just stand up."
                call luna_main("*Hmmmph* Don't expect that you'll be cumming anywhere near me though!", 6, 3, 4, 3) 
            "-Ask for a handjob politely-" if luna_sub < luna_dom:
                $ current_payout = 160
                if luna_dom <= 8:
                    $ luna_dom += 1
                $ luna_choice = 3
                m "Well seeing as how you're so skilled at everything you turn your hand towards..."
                call luna_main("Mhmmm...", 6, 2, 2, 3) 
                m "I was hoping you could turn your hand towards my cock."
                call luna_main("...", 8, 2, 1, 2) 
                m "please..."
                call luna_main("Really? You want me to stroke that filthy cock of yours?", 8, 2, 1, 2) 
                call luna_main("Isn't it enough that I let you touch yourself...", 4, 2, 5, 3)
                m "There'll be a hefty reward..."
                call luna_main("...", 6, 3, 4, 3) 
                call luna_main("......", 6, 3, 4, 3)
                call luna_main("Well seeing as how you asked so nicely...", 6, 3, 4, 3) 
                m "..."
                call luna_main("Get over here...", 6, 3, 4, 3) 
                m "Fantastic! Let me just stand up."
                call luna_main("(This couldn't get any easier)", 6, 3, 4, 3) 
            "-Beg for a handjob-" if luna_dom >= 7:
                $ current_payout = 200
                if luna_dom <= 8:
                    $ luna_dom += 1
                $ luna_choice = 4
                m "Well if it's not too much trouble..."
                call luna_main("Mhmmm...", 6, 2, 2, 3) 
                m "I was hoping you could..."
                call luna_main("...", 8, 2, 1, 2) 
                m "give me one..."
                call luna_main("Really? You want me to stroke that filthy cock of yours?", 8, 2, 1, 2) 
                m "If it's not too much trouble..."
                call luna_main("Well I suppose I probably should.", 4, 2, 5, 3)
                call luna_main("Who knows who you'll call up her if I don't...", 4, 2, 5, 3)
                m "Thank you..."
                call luna_main("...", 6, 3, 4, 3) 
                call luna_main("......", 6, 3, 4, 3)
                call luna_main("However I do expect to be fairly compensated...", 6, 3, 4, 3) 
                m "Of course."
                call luna_main("Good. Now Get over here...", 6, 3, 4, 3) 
                m "Fantastic! Let me just stand up."
                call luna_main("(This couldn't get any easier...)", 6, 3, 4, 3) 
                call luna_main("(I'll be the only person in his will by the end of the month at this rate...)", 6, 3, 4, 3) 

        if luna_choice <= 2: #Sub choices
            jump luna_revert_1
        else:
            jump luna_revert_2


label luna_revert_1: #Reversion event
    ">You stand up and walk around your desk, standing in front of Luna."
    ">You open your cloak and pull out your cock."
    m "Well..."
    $ luna_tears = 0
    call luna_main("...", 6, 3, 4, 3) 
    ">Luna looks hesitantly at your cock."
    call luna_main("......", 6, 3, 4, 3) 
    ">She slowly takes a hold of it with her right hand."
    call luna_main("It's so big...", 6, 3, 4, 3) 
    call luna_main("(I can't even fit my hand around it.)", 6, 3, 4, 3) 
    m "Why don't you try grabbing it with both hands [luna_name]..."
    call luna_main("Alright...", 6, 3, 4, 3) 
    ">Luna slowly wraps both hands around your cock."
    m "Mmmm, that's it. Now start moving your hands back and forth."
    call luna_main("......", 6, 3, 4, 3) 
    ">Luna starts moving her hands back and forth along the length of your cock."
    m "Yes, that's it..."
    call luna_main("...", 6, 3, 4, 3) 
    m "Mmmm, yes... not bad [luna_name], have you been practicing?"
    call luna_main("What? Of course not!", 6, 3, 4, 3) 
    m "well, I expect you to start practicing from now on!"
    call luna_main("on what?", 6, 3, 4, 3) 
    m "My cock of course!"
    call luna_main("[l_genie_name]!", 6, 3, 4, 3) 
    m "I'm kidding [luna_name]."
    call luna_main("oh...", 6, 3, 4, 3) 
    m "But I do expect you to improve..."
    call luna_main("Doesn't this feel good?...", 6, 3, 4, 3) 
    m "It's alright..."
    call luna_main("Well what do I need to do differently?", 6, 3, 4, 3) 
    menu:
        "\"Take your shirt off\"":
            $ luna_choice = 1
            call luna_main("My shirt? Really?", 6, 3, 4, 3) 
            m "It'd make this go a lot faster."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("Fine...", 6, 3, 4, 3) 
            call luna_main("But I expect to be paid extra!", 6, 3, 4, 3) 
            $ current_payout += 20
            m "Fair's fair."
            call luna_main("...", 6, 3, 4, 3) 
            ">Luna slowly takes off her top, placing it on the floor."
            $ luna_wear_top = False
            call luna_main("There...", 6, 3, 4, 3) 
            call luna_main("Is that enough [l_genie_name]?", 6, 3, 4, 3) 
            m "Almost... hands back on the cock [luna_name]..."
            call luna_main("...", 6, 3, 4, 3) 
            ">Luna slowly wraps her hands back around your cock and starts pumping."
        "\"Faster\"":
            $ luna_choice = 2
            call luna_main("Like this?", 6, 3, 4, 3) 
            ">Luna starts moving her hands up and down your cock a little faster."
            m "mmmm..."
            call luna_main("Is this fast enough [l_genie_name]?", 6, 3, 4, 3) 
            m "Almost..."
            call luna_main("...", 6, 3, 4, 3) 
            ">She speeds up the pace."
            m "Ah!"
            call luna_main("What?", 6, 3, 4, 3) 
            m "Well if you go that fast the friction's a little painful"
            call luna_main("Really? I'll slow down then...", 6, 3, 4, 3) 
            m "No need for that [luna_name], a little spit should solve the problem."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("You want me to spit on your cock?", 6, 3, 4, 3) 
            m "Just a little bit."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("......", 6, 3, 4, 3)
            call luna_main("*Ptew*", 6, 3, 4, 3) 
            ">Luna spits into her hand before placing it back on your cock."
    g9 "Mmmm, yes that's it [luna_name]..."
    call luna_main("...", 6, 3, 4, 3) 
    g9 "Just keep pumping those hands up and down."
    call luna_main("......", 6, 3, 4, 3) 
    if luna_choice == 1:
        g9 "Why don't you give those milky tits of yours a nice shake?"
        call luna_main("[l_genie_name]...", 6, 3, 4, 3) 
        call luna_main("(A little shake won't hurt...)", 6, 3, 4, 3) 
        ">Luna gently starts shaking her boobs as she jerks you off."
    else:
        g9 "Mmmm, yes... how about a little more spit [luna_name]?"
        g9 "Just to make sure everything is nice and lubricated..."
        call luna_main("...", 6, 3, 4, 3) 
        call luna_main("Alright...", 6, 3, 4, 3) 
        call luna_main("*Ptew*", 6, 3, 4, 3) 
        ">Luna spits into her hand again and places it back on your cock."
    ">She starts pumping your cock even faster."
    g9 "Gods yes..."
    g9 "(This is it, where should I cum?)"
    menu:
        "-On her face-":
            ">You place your hand on the top of Luna's head and slowly force it down to be level with your crouch."
            ">Her slender hands don't stop sliding up and down your length."
            call luna_main("[l_genie_name]!!!", 6, 3, 4, 3) 
            g9 "Shhh [luna_name], I'm just giving you a closer look."
            call luna_main("...", 6, 3, 4, 3) 
            $ luna_tears = 2
            call luna_main("{size=-5}please sir...{/size}", 6, 3, 4, 3) 
            g9 "what [luna_name]?"
            call luna_main("Please don't...", 6, 3, 4, 3) 
            g9 "mmmm"
            call luna_main("cum on my-", 6, 3, 4, 3) 
            $ luna_wear_cum = True
            $ luna_cum = 7
            hide screen luna
            with d3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            call luna_main("!!!!!!", 5, 3, 1, 1)
            g4 "Argh! by the gods {size=+10}YES!{/size}"
            g4 "{size=+10}TAKE IT ALL!{/size}"

        "-On her shirt-":
            ">You place your hand on Luna's shoulder."
            ">Her slender hands don't stop sliding up and down your length."
            call luna_main("[l_genie_name]...", 6, 3, 4, 3) 
            g9 "Shhh [luna_name], just keep stroking."
            call luna_main("...", 6, 3, 4, 3) 
            $ luna_tears = 2
            call luna_main("{size=-5}please sir...{/size}", 6, 3, 4, 3) 
            g9 "what [luna_name]?"
            call luna_main("Please don't...", 6, 3, 4, 3) 
            g9 "mmmm"
            call luna_main("cum on me-", 6, 3, 4, 3) 
            $ luna_wear_cum = True
            $ luna_cum = 3
            hide screen luna
            with d3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            call luna_main("!!!!!!", 5, 3, 1, 1)
            g4 "Argh! by the gods {size=+10}YES!{/size}"
            g4 "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
    g4 "mmmm....."
    m "That hit the spot..."
    call luna_main("[l_genie_name]!", 5, 3, 1, 1)
    call luna_main("How could you!", 5, 3, 1, 1)
    m "Ahh... that was fantastic slut..."
    call luna_main("[l_genie_name]!!!", 5, 3, 1, 1)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_main("[genie_name], I hope you don't mind me coming in unannounced...","body_122")
    call her_main("But I really need a good-.","body_122")
    call her_main("...","body_122")
    $ luna_flip = 1
    call luna_main("...", 5, 3, 1, 1)
    m "..."
    pause
    call her_main("{size=+5}WHAT{/size}","body_122")
    call her_main("{size=+10}THE{/size}","body_122")
    call her_main("{size=+15}FRICK!{/size}","body_122")
    call luna_main("It's not what it looks-", 5, 3, 1, 1)
    call her_main("{size=+15}petrificus totalus!{/size}","body_122")
    ">Hermione pulls out her wand with surprising speed and paralyzes Luna."
    call luna_main("!!!", 5, 3, 1, 1)
    m "(Whoa...)"
    call her_main("Honestly sir what are you thinking!","body_122")
    call her_main("If you need you're filthy old cock jerked so badly you should just call me!","body_122")
    call luna_main("???", 5, 3, 1, 1)
    call her_main("But to be doing this with Luna Lovegood...","body_122")
    call her_main("She's not even a {size=+5}\"Gryffindor!{/size}","body_122")
    m "I wasn't pay-"
    call her_main("Shut up!","body_122")
    call her_main("How did you even get Luna to agree to this sir?","body_122") 
    call her_main("I don't even think she knows what house she's in half the time.","body_122")
    call her_main("I can't imagine her sense of house pride is large enough to warrant this...","body_122")
    m "I can explain this..."
    call her_main("Really? {p}Go on...","body_122")
    m "Well I was sitting here alone in my office."
    m "(What else can I do...)"
    m "When all of a sudden this weird hat on the shelf behind me starts talking!"
    call her_main("...","body_122")
    call her_main("Are you serious sir?","body_122")
    m "I knew you wouldn't beli-"
    call her_main("Of course I believe you! It's the sorting hat!","body_122")
    m "(I keep forgetting that this place is magic...)"
    m "Yes, well... the \"sorting\" hat mentioned that it may have made a mistake with the sorting of some students."
    hat "..."
    m "So it offered to use \"Legitimancy\" or something to fix-"
    call her_main("You performed Legilimency?","body_122")
    call her_main("On a {size=+5}student{/size}!?","body_122")
    m "It's not that bad, surely..."
    call her_main("Sir, it's bad enough to use Legilimency to read someone's mind...","body_122")
    call her_main("but to use it to change their mind...","body_122")
    call her_main("I didn't even think it was possible...","body_122")
    m "So it's ok then?"
    call her_main("It's pretty frickin' far from OK...","body_122")
    call her_main("You have to Change her back!","body_122")
    m "Really? But this has been pretty fun."
    call her_main("I can't believe I have to tell you how wrong this is sir!","body_122")
    call her_main("Change her back now or I tell the ministry everything.","body_122")
    m "What about your house-"
    call her_main("{size=+10}NOW!{/size}","body_122")
    m "Alright, alright, sheesh..."
    m "{size=-5}(these bitches be crazy){/size}"
    m "Let me just get the hat."
    ">You reach around and pull the old leathery hat down from the dusty cupboard."
    hat "Ughh... Gently does it now."
    call her_main("Put it on her head.","body_122")
    hat "Well if it isn't Miss Granger..."
    call her_main("...","body_122")
    ">You place the sorting hat gently on top of Luna's head."
    m "There."
    call her_main("Well, change her back!","body_122")
    hat "Are you sure? She seemed much more entertaining this way..."
    call her_main("Do. {size=+5}it. {size=+5}NOW!{/size}","body_122")
    hat "Alright, alright. Sheesh."
    hat "You don't seem this bossy when you're in here normally..."
    call luna_main("!!!", 6, 3, 4, 3) 
    call her_main("{size=+5}Shut up!{/size}","body_122")
    hat "One boring old Lovegood, coming right up."
    call luna_main("???", 6, 3, 4, 3) 
    call luna_main("......", 6, 3, 4, 3) 
    call luna_main(".....", 6, 3, 4, 3) 
    call luna_main("....", 6, 3, 4, 3) 
    call luna_main("...", 6, 3, 4, 3) 
    $ luna_reverted = True
    call luna_main("...", 6, 3, 4, 3) 
    hat "There, she's back to normal... {size=-8}sadly{/size}"
    call her_main("Are you certain?","body_122")
    hat "Yes, I'm sure of it. Can I go back up on the shelf now?"
    call her_main("Fine...","body_122")
    call her_main("But if you every try anything else like this again...","body_122")
    call her_main("...","body_122")
    ">You decide to place the hat back on the top of the cupboard."
    m "There, all better. now we can forget this whole thing ever happened."
    call her_main("You're not serious are you?","body_122")
    m "What? Miss Lovesgood is back to normal..."
    call her_main("You don't think you're getting away with this do you?","body_122")
    m "I'm not sure what you're referring to?"
    call her_main("What I'm referring to?","body_122")
    call her_main("Luna Lovegood is {size+=10}COVERED {/size}in your cum!","body_122")
    m "Oh..."
    call her_main("more importantly, How many points did you pay her?","body_122")
    menu:
        "\"None\"":
            call her_main("What?","body_122")
            call her_main("I'm supposed to believe that she came up to your office...","body_122")
            call her_main("And let you jerk your disgusting old cock in front of her...","body_122")
            call her_main("For free?","body_122")
            ">You raise your hand to the air."
            m "Scouts honor!"
            call her_main("...","body_122")
            m "Besides, surely you'd notice a jump in \"Ravenclaw's\" points?"
            call her_main("I suppose you're right...","body_122")
            call her_main("If the sorting hat had manipulated her then doing this isn't out of the question.","body_122")
            call her_main("{size-=5}(But for her to do it so willingly...){/size}","body_122")
        "\"I paid her in gold\"":
            call her_main("Gold?","body_122")
            m "Gold."
            call her_main("So no points?","body_122")
            m "Not one."
            call her_main("I suppose that's OK then...","body_122")
            call her_main("{size-=5}(Why don't I ever get paid in gold...){/size}","body_122")
            call her_main("{size-=5}(well Then I'd be a prostitute...){/size}","body_122")
            call her_main("{size-=5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_122")

    call her_main("Well regardless, she has to be punished.","body_122")
    m "Wait, she's being punished?"
    call her_main("Of course!","body_122")
    call her_main("Seeing as how you didn't give \"Ravenclaw\" any points you haven't done anything wrong.","body_122")
    call her_main("But her...","body_122")
    ">Hermione glares at the still frozen Luna Lovegood."
    call her_main("...","body_122")
    call her_main("She needs a punishment.","body_122")
    m "What are you thinking?"
    call her_main("Hmmm...","body_122")
    call her_main("Sorting hat!","body_122")
    hat "W-w-what? I'm trying to go to sleep..."
    call her_main("How long until Luna's back to normal?","body_122")
    hat "I'm not exactly sure... Probably twenty minutes."
    hat "Until then she'll pretty much be in a fairly lucid and suggestible state."
    call her_main("Good...","body_122")
    call her_main("liquescimus corporis!","body_122")
    ">Another flash of light as Luna becomes un-petrified."
    call luna_main("Ugh... where am I?", 5, 3, 1, 1)
    call her_main("Shhh, it's alright.","body_122")
    call luna_main("Hermione? What's happening?", 5, 3, 1, 1)
    call her_main("Nothing. Professor Dumbledore and I just needed your help.","body_122")
    call luna_main("What with?", 5, 3, 1, 1)
    call luna_main("And what's this stuff on-", 5, 3, 1, 1)
    call her_main("Shhh, that doesn't matter right now.","body_122")
    call her_main("Just head back to your common room...","body_122")
    m "is that really-"
    ">Hermione glares at you."
    call her_main("...","body_122")
    call luna_main("Alright, I'll go back to my common room...", 5, 3, 1, 1)
    call her_main("That's right...","body_122")
    ">Luna quietly exits the room."
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_main("Well, now that that's over...","body_122")
    call her_main("I think I'll be leaving as well...","body_122")
    m "Don't you want to stay a little longer?"
    call her_main("I don't think so sir...","body_122")

    ">Hermione turns to leave."


label luna_revert_2: #Non-Reversion event
    ">You stand up and walk around your desk, standing in front of Luna."
    ">You open your cloak and pull out your cock."
    m "Well..."
    call luna_main("...", 6, 3, 4, 3) 
    ">Luna looks hesitantly at your cock."
    call luna_main("Disgusting...", 6, 3, 4, 3) 
    ">She take a firm hold of it with her right hand"
    call luna_main("*Hmmph* At least it isn't small...", 6, 3, 4, 3) 
    call luna_main("(I can't even fit my hand around it.)", 6, 3, 4, 3) 
    ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
    m "Why don't you try grabbing it with both hands [luna_name]..."
    call luna_main("Alright... But I expect to be paid extra!", 6, 3, 4, 3) 
    ">Luna slowly wraps both hands around your cock."
    m "Mmmm, that's it. Now start moving your hands back and forth."
    call luna_main("......", 6, 3, 4, 3) 
    ">Luna starts moving her hands back and forth along the length of your cock."
    m "Yes, that's it..."
    call luna_main("(Men really are the worst)", 6, 3, 4, 3) 
    m "Mmmm, yes... just like that [luna_name]..."
    call luna_main("Is this good [l_genie_name]?", 6, 3, 4, 3) 
    m "yes, yes, this is amazing..."
    call luna_main("good...", 6, 3, 4, 3) 
    call luna_main("but...", 6, 3, 4, 3) 
    call luna_main("Do you need a little more encouragement?", 6, 3, 4, 3) 
    m "What are you thinking?"
    call luna_main("......", 6, 3, 4, 3) 
    menu:
        "-Luna takes her top off-":
            ">Luna slowly removes her vest and starts to unbutton her top."
            $ luna_wear_top = False
            $ luna_choice = 1
            m "Mmmm"
            ">She takes her shirt off and places it onto the floor."
            call luna_main("There...", 6, 3, 4, 3) 
            m "Very nice [luna_name]!"
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("Thank you sir...", 6, 3, 4, 3) 
            ">She places her hands back around your cock."
            call luna_main("Mmm, much better...", 6, 3, 4, 3) 
            m "Gods yes."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("I'd take my bra off as well...", 6, 3, 4, 3) 
            call luna_main("But I don't think you'd be able to stop yourself from cumming on the spot, would you?", 6, 3, 4, 3) 
            m "Ah... probably not..."
            call luna_main("...", 6, 3, 4, 3) 
            ">Luna starts pumping your cock a little faster."
        "-Luna teases you-":
            $ luna_choice = 2
            call luna_main("Come on Professor...", 6, 3, 4, 3) 
            ">Luna starts moving her hands up and down your cock a little faster."
            m "mmmm..."
            call luna_main("Get a nice big load ready for me...", 6, 3, 4, 3) 
            m "Ah yes..."
            call luna_main("get ready to cum all over your student.", 6, 3, 4, 3) 
            ">She speeds up the pace."
            m "Ah..."
            call luna_main("What's wrong?", 6, 3, 4, 3) 
            m "Well if you go that fast the friction's a little painful."
            call luna_main("Really?...", 6, 3, 4, 3) 
            ">Luna doesn't slow down. If anything she speeds up slightly."
            g9 "Ah!"
            call luna_main("...", 6, 3, 4, 3) 
            g9 "[luna_name]..."
            call luna_main("Hmmm, do You want me to spit on your cock then?", 6, 3, 4, 3) 
            g9 "Just a little bit..."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("......", 6, 3, 4, 3)
            g9 "Please..."
            call luna_main("Good boy.", 6, 3, 4, 3) 
            call luna_main("*Ptew*", 6, 3, 4, 3) 
            ">Luna spits into her hand before placing it back on your cock."
    g4 "Mmmm, yes that's it [luna_name]..."
    call luna_main("...", 6, 3, 4, 3) 
    g4 "Just keep pumping those hands up and down."
    call luna_main("......", 6, 3, 4, 3) 
    if luna_choice == 1:
        ">Luna gently starts shaking her boobs as she jerks you off."
    else:
        call luna_main("*Ptew*", 6, 3, 4, 3) 
        ">Luna spits into her hand again and places it back on your cock."
    ">She starts pumping your cock even faster."
    g4 "Gods yes..."
    g4 "(This is it, where should I cum?)"
    menu:
        "-On her face-":
            ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

        "-On her tits-":
            ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

    call luna_main("[l_genie_name]!!!", 6, 3, 4, 3) 
    call luna_main("You're not trying to cum on me are you?", 6, 3, 4, 3) 
    g4 "Ah [luna_name], I'm almost there."
    call luna_main("Well...", 6, 3, 4, 3) 
    $ luna_wear_skirt = False
    ">Luna slowly pulls down her skirt."
    g4 "!!!"
    call luna_main("You cum...", 6, 3, 4, 3) 
    g4 "Ah..."
    ">Luna slowly pulls her panties forward, exposing her pussy to the air."
    ">Her right hand is still wrapped around your cock as she pumps it with blinding speed."
    call luna_main("Where I tell you...", 6, 3, 4, 3) 
    g4 "mmmm"
    call luna_main("Now...", 6, 3, 4, 3) 
    call luna_main("Cum.", 6, 3, 4, 3) 
    hide screen luna
    with d3
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    ">You start shooting your load directly into Luna's panties, coating her pussy in cum."
    g4 "Argh! by the gods {size=+10}YES!{/size}"
    call luna_main("...", 5, 3, 1, 1)
    call luna_main("(It's so warm...)", 5, 3, 1, 1)
    g4 "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
    g4 "mmmm....."
    m "That hit the spot..."
    call luna_main("({image=textheart}{image=textheart}{image=textheart})", 5, 3, 1, 1)
    call luna_main("[l_genie_name]!", 5, 3, 1, 1)
    call luna_main("How could you! Cumming on your students {size=-10}pussy{/size}...", 5, 3, 1, 1)
    m "Ahh... that was fantastic slut..."
    call luna_main("[l_genie_name]...", 5, 3, 1, 1)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_main("[genie_name], I hope you don't mind me coming in unannounced...","body_122")
    call her_main("But I really need a good-.","body_122")
    $ luna_flip = 1
    call luna_main("...", 5, 3, 1, 1)
    call her_main("...","body_122")
    m "..."
    pause
    call her_main("{size=+5}WHAT{/size}","body_122")
    call her_main("{size=+10}THE{/size}","body_122")
    call her_main("{size=+15}FRICK!{/size}","body_122")
    call her_main("What on earth is going on-","body_122")
    call luna_main("{size=+15}petrificus totalus!{/size}", 5, 3, 1, 1)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic1.ogg')   #Not loud.
    ">Luna pulls out her wand with surprising speed and paralyzes Hermione."
    call her_main("!!!","body_122")
    m "(Whoa...)"
    ">Luna turns back around to face you, leaving Hermione paralyzed in the middle of the room. "
    call luna_main("{size=+15}What is the meaning of this?{/size}", 5, 3, 1, 1)
    m "I don't know, Miss Granger must have come up here to ask for something."
    call luna_main("The door was locked!", 5, 3, 1, 1)
    call luna_main("And everyone knows your door is enchanted against every spell possible!", 5, 3, 1, 1)
    m "(It is?)"
    call luna_main("So she must have had a key...", 5, 3, 1, 1)
    m "..."
    call luna_main("Why does she have a key [l_genie_name]?", 5, 3, 1, 1)
    m "Ah... um..."
    menu:
        "\"To buy favours\"":
            pass

        "-I don't know-":
            call luna_main("...", 5, 3, 1, 1)
            call luna_main("Really? You don't know...", 5, 3, 1, 1)
            m "No idea..."
            call luna_main("Well then, we'll just have to ask hermione...", 5, 3, 1, 1)
            call her_main("...","body_122")
            call luna_main("I'm sure that some Veritaserum will clear things up...", 5, 3, 1, 1)
            call her_main("!!!","body_122")
            m "(Is that bad?)"
            ">Hermione gives you a pleading look with her eyes."
            call her_main("...","body_122", "tears_01")
            m "(Probably...)"
            m "Um..."
            call luna_main("Go on old man...", 5, 3, 1, 1)
            m "She's hear to buy favours..."



    call luna_main("...", 5, 3, 1, 1)
    call luna_main("...", 5, 3, 1, 1)
    call luna_main("{size=+5}WHAT{/size}", 5, 3, 1, 1)
    call luna_main("To think that I came here and let you leer at my body...", 5, 3, 1, 1)
    call luna_main("While you stroked that filthy cock of yours...", 5, 3, 1, 1)
    call luna_main("and all the while you've been throwing your gold away to some \"Gryffindor\" skank!", 5, 3, 1, 1)
    call luna_main("well then, How much have you paid her?", 5, 3, 1, 1)
    call luna_main("How much have you wasted on this fat assed tart?", 5, 3, 1, 1)

    $ point_estimate = gryffindor*0.80
    m "All up? probably about [point_estimate] points..."
    call luna_main("[point_estimate]... {p}points?", 5, 3, 1, 1)
    m "you know. For \"gryffinwhore\"..."
    call luna_main("...", 5, 3, 1, 1)
    call luna_main("hahahaha!", 5, 3, 1, 1)
    call her_main("...","body_122")
    m "..."
    ">Luna turns back around to face hermione/"
    call luna_main("really? you sell your body for points?", 5, 3, 1, 1)
    call her_main("...","body_122")
    call luna_main("Oh right, I suppose I should probably undo that.", 5, 3, 1, 1)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic1.ogg')   #Not loud.
    call luna_main("liquescimus corporis!", 5, 3, 1, 1)
    ">Another flash of light as Hermione becomes un-petrified."
    call her_main("Professor! What is the meaning of this!","body_122")
    call her_main("And what were the two of you doing before I got here?","body_122")
    call luna_main("oh... I was just helping out Professor Dumbledore...", 5, 3, 1, 1)
    call her_main("helping out how?","body_122")
    call luna_main("just to relieve some... tension. Don't worry he isn't going to pay me in points... *tssk*", 5, 3, 1, 1)
    call her_main("what?","body_122")
    call her_main("[genie_name]! What are you doing!","body_122")
    m "Ah...."
    call luna_main("don't blame him. It's not his fault you fail to satisfy...", 5, 3, 1, 1)
    call her_main("You... you...","body_122")
    call her_main("{size=+10}You Stupid whore!{/size}","body_122")
    call her_main("{size=+15}You're nothing more than a prostit-{/size}","body_122")
    call luna_main("{size=+15}petrificus totalus!{/size}", 5, 3, 1, 1)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic1.ogg')   #Not loud.
    ">Luna paralyzes Hermione for the second time."
    call her_main("!!!","body_122")
    ">Hermione stares at Luna with a blind rage."
    m "Should you really be doing that?"
    call luna_main("*Hmmmph*", 5, 3, 1, 1)
    ">Luna huffs, ignoring the question."
    call luna_main("Honestly [l_genie_name], I don't know what you see in her...", 5, 3, 1, 1)
    call luna_main("So, how should we punish her?", 5, 3, 1, 1)
    m "Punish her?"
    call luna_main("Of course! For what she said.", 5, 3, 1, 1)
    call luna_main("You're not going to let her get away with that are you?", 5, 3, 1, 1)
    menu:
        "-Tell her to let hermione go-":
            m "Unfreeze miss granger."
            call luna_main("What? You're taking her side?", 5, 3, 1, 1)
            m "(Ugh... bitches...)"
            m "I'm not taking anyone's side. I'll punish Miss granger appropriately later."
            call luna_main("...", 5, 3, 1, 1)
            call luna_main("Whatever...", 5, 3, 1, 1)
            show screen white 
            pause .1
            hide screen white
            $ renpy.play('sounds/magic1.ogg')   #Not loud.
            call luna_main("liquescimus corporis!", 5, 3, 1, 1)
            call her_main("...","body_122")
            m "That will be all for now miss lovegood."
            call luna_main("...", 5, 3, 1, 1)
            call luna_main("You better punish her...", 5, 3, 1, 1)
            jump luna_away
            call her_main("...","body_122")


        "-Let her decide-":
            m "I'll leave the punishment to you."
            call luna_main("Yes, you're probably right.", 5, 3, 1, 1)
            ">Luna turns to face hermione."
            call luna_main("Hmmm, what should I do...", 5, 3, 1, 1)
            call luna_main("...", 5, 3, 1, 1)
            call her_main("...","body_122")
            call luna_main("I've got it!", 5, 3, 1, 1)
            ">Luna places her hands on Hermione's shoulders and gently forces her paralyzed body to her knees."
            call luna_main("That should be about right...", 5, 3, 1, 1)
            call luna_main("wait...", 5, 3, 1, 1)
            ">Luna places her hand on hermione's chin and gently turns her head upwards."
            call luna_main("Perfect...", 5, 3, 1, 1)
            call her_main("...","body_122")
            call luna_main("Now, before you so rudely decided to interrupt us, Professor Dumbledore made a nasty mess...", 5, 3, 1, 1)
            call her_main("...","body_122")
            call luna_main("I was going to go back to my room and tidy up before class but seeing as how your interruption has taken so long, you'll have to tidy me up instead.", 5, 3, 1, 1)
            call her_main("...","body_122")
            ">Luna slowly pulls down her panties, revealing her cum-soaked pussy."
            call her_main("!!!","body_122")
            call luna_main("Well... get to work!", 5, 3, 1, 1)
            ">Hermione glares at luna."
            call her_main("...","body_122")
            call luna_main("*Sigh* I guess I have to do everything then!", 5, 3, 1, 1)
            ">Luna thrusts her mound forward, griding it under Hermione's nose and against her closed mouth."
            call her_main("!!!","body_122")
            call luna_main("Mmmm, that's it...", 5, 3, 1, 1)
            call luna_main("who's a good girl...", 5, 3, 1, 1)
            call her_main("!!!","body_122")









