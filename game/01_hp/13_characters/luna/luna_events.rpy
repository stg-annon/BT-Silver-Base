label luna_reversion_event:
    m "{size=-4}(I'll just ask for a quick tug...){/size}"
    if luna_corruption <= 10: #FIRST TIME
        if luna_corruption <= 9:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        if luna_sub > luna_dom: #Sub intro
            m "[luna_name]..."
            call luna_main("yes [l_genie_name]...", 6, 3, 4, 2)
            m "Do you know what a handjob is?"
            call luna_main("What?", 1, 1, 3, 3)
            m "It's where you wrap your hand around-"
            call luna_main("I know what they are!", 4, 1, 2, 4)
            m "Fantastic!"
            call luna_main("...", 7, 2, 2, 3)

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
                call luna_main("Really? You expect me to {size=+5}touch{/size} that filthy cock of yours?", 4, 1, 5, 3)
                call luna_main("It's bad enough that I have to stand here while you touch yourself...", 8, 1, 2, 2)
                call luna_main("But that's where I draw the line, [l_genie_name]!", 9, 1, 3, 3)
                m "Hmmm...{p} well alright then, I'm not going to force you into anything."
                call luna_main("Thank you...", 6, 2, 4, 3)
                m "That will be all for today, [luna_name], you may leave now."
                call luna_main("Alright, [l_genie_name]...", 6, 1, 4, 2)
                call luna_main("(Good work finally standing up to him!)", 2, 2, 4, 1)
                ">Luna turns around to leave your office."
                m "Oh, one last thing..."
                call luna_main("...", 7, 1, 4, 2) 
                m "Could you send the first \'slytherin\' girl you see to my office?"
                call luna_main("What! Why?", 4, 1, 2, 4) 
                m "Well seeing as how you're not able to give me a little attention, I figure that one of those \'slytherin\' sluts will."
                m "They'll probably even do it for half the price..." 
                call luna_main("...", 7, 1, 2, 3) 
                call luna_main("......", 6, 3, 4, 2)
                $ luna_tears = 1 
                call luna_main(".........", 5, 1, 4, 3) 
                call luna_main("{size=-5}Fine{/size}...", 5, 3, 4, 2) 
                m "What was that, [luna_name]?"
                call luna_main("{size=+5}Fine!{/size} I'll jerk that disgusting, old, filthy, wrinkly old cock of yours!", 4, 1, 4, 6) 
                m "Fantastic! Let me just stand up."
                call luna_main("You're despicable...", 8, 1, 2, 3) 

            "-Ask for a handjob-" if luna_sub > luna_dom:
                $ current_payout = 120
                if luna_sub <= 8:
                    $ luna_sub += 1
                $ luna_choice = 2
                m "Well seeing as how you're familiar with the concept..."
                call luna_main("...", 7, 1, 3, 3) 
                call luna_main("Really? You expect me to {size=+5}touch{/size} that filthy cock of yours?", 4, 1, 5, 3) 
                call luna_main("It's bad enough that I have to stand here while you touch yourself...", 8, 8, 4, 2) 
                m "There'll be a hefty reward..."
                call luna_main("...", 6, 3, 4, 3) 
                call luna_main("......", 6, 2, 4, 1)
                call luna_main("I expect that my father's magazine will also sell a few more copies...", 7, 1, 4, 2) 
                m "Of course..."
                call luna_main("Fine...", 6, 3, 4, 3) 
                m "Fantastic! Let me just stand up."
                call luna_main("*Hmmmph* Don't expect that you'll be cumming anywhere near me though!", 8, 1, 3, 3) 
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
                call luna_main("Really? You want me to stroke that filthy cock of yours?", 8, 1, 2, 3) 
                call luna_main("Isn't it enough that I let you touch yourself...", 9, 2, 3, 3)
                m "There'll be a hefty reward..."
                call luna_main("...", 8, 2, 3, 3) 
                call luna_main("......", 8, 1, 2, 2)
                call luna_main("Well seeing as how you asked so nicely...", 8, 1, 1, 1) 
                m "..."
                call luna_main("Get over here...", 7, 1, 3, 1) 
                m "Fantastic! Let me just stand up."
                call luna_main("(This couldn't get any easier)", 8, 2, 2, 1) 
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
                call luna_main("Really? You want me to stroke that filthy cock of yours?", 8, 1, 2, 3) 
                m "If it's not too much trouble..."
                call luna_main("Well I suppose I probably should.", 5, 2, 1, 1)
                call luna_main("Who knows who you'll call up her if I don't...", 8, 1, 3, 1)
                m "Thank you..."
                call luna_main("...", 8, 2, 3, 3) 
                call luna_main("......", 8, 1, 2, 2)
                call luna_main("However I do expect to be fairly compensated...", 8, 1, 1, 1) 
                m "Of course."
                call luna_main("Good. Now Get over here...", 7, 1, 3, 1) 
                m "Fantastic! Let me just stand up."
                call luna_main("(This couldn't get any easier...)", 8, 2, 2, 1) 
                call luna_main("(I'll be the only person in his will by the end of the month at this rate...)", 9, 1, 3, 1) 

        if luna_choice <= 2: #Sub choices
            jump luna_revert_1
        else:
            jump luna_revert_2


label luna_revert_1: #Reversion event
    hide screen bld1
    hide screen genie
    show screen chair_02
    show screen desk_02
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "jerking_off_02_ani"
    show screen g_c_u
    with fade
    hide screen blktone
    hide screen blkfade
    with d5
    pause
    ">You stand up and walk around your desk, standing in front of Luna."
    ">You open your cloak and pull out your cock."
    m "Well..."
    $ luna_tears = 0
    call luna_main("...", 5, 3, 1, 2) 
    ">Luna looks hesitantly at your cock."
    call luna_main("......", 3, 3, 4, 2)  
    ">She slowly takes a hold of it with her right hand."
    $ luna_r_arm = 3
    $ genie_sprite_xpos = 300
    $ luna_xpos = 390
    call gen_main("!!!", 4, 2)

    call luna_main("It's so big...", 5, 3, 4, 1) 
    call luna_main("(I can't even fit my hand around it.)", 5, 2, 4, 1) 
    m "Why don't you try grabbing it with both hands, [luna_name]..."
    call luna_main("Alright...", 6, 3, 4, 1) 
    ">Luna slowly wraps both hands around your cock."
    m "Mmmm, that's it. Now start moving your hands back and forth."
    call luna_main("......", 5, 3, 1, 2) 
    ">Luna starts moving her hands back and forth along the length of your cock."
    m "Yes, that's it..."
    call luna_main("...", 6, 3, 4, 1) 
    m "Mmmm, yes... not bad [luna_name], have you been practicing?"
    call luna_main("What? Of course not!", 4, 1, 2, 2) 
    m "well, I expect you to start practicing from now on!"
    call luna_main("on what?", 7, 1, 5, 2) 
    m "My cock, of course!"
    call luna_main("[l_genie_name]!", 8, 1, 2, 6) 
    m "I'm kidding, [luna_name]."
    call luna_main("oh...", 7, 2, 4, 14) 
    m "But I do expect you to improve..."
    call luna_main("Doesn't this feel good?...", 8, 1, 5, 4) 
    m "It's alright..."
    call luna_main("Well, what do I need to do differently?", 6, 2, 4, 2) 
    menu:
        "\"Take your shirt off\"":
            $ luna_choice = 1
            call luna_main("My shirt? Really?", 8, 1, 2, 14) 
            m "It'd make this go a lot faster."
            call luna_main("...", 6, 3, 4, 3) 
            call luna_main("Fine...", 8, 1, 4, 2) 
            call luna_main("But I expect to be paid extra!", 3, 3, 2, 3) 
            $ current_payout += 20
            m "It's a deal."
            call luna_main("...", 6, 3, 4, 3) 
            ">Luna slowly takes off her top, placing it on the floor."
            $ luna_wear_top = False
            call luna_main("There...", 5, 1, 4, 2) 
            call luna_main("Is that enough, [l_genie_name]?", 7, 2, 2, 3) 
            m "Almost... hands back on the cock, [luna_name]..."
            call luna_main("...", 5, 3, 4, 1) 
            ">Luna slowly wraps her hands back around your cock and starts pumping."
        "\"Faster\"":
            $ luna_choice = 2
            call luna_main("Like this?", 7, 8, 4, 1) 
            ">Luna starts moving her hands up and down your cock a little faster."
            m "mmmm..."
            call luna_main("Is this fast enough [l_genie_name]?", 5, 2, 4, 1) 
            m "Almost..."
            call luna_main("...", 6, 3, 4, 3) 
            ">She speeds up the pace."
            call gen_main("Ah!", 2)
            call luna_main("What?", 4, 1, 1, 2) 
            m "Well if you go that fast the friction's a little painful"
            call luna_main("Really? I'll slow down then...", 6, 3, 4, 3) 
            m "No need for that [luna_name], a little spit should solve the problem."
            call luna_main("...", 8, 1, 2, 2) 
            call luna_main("You want me to spit on your cock?", 9, 2, 4, 3) 
            m "Just a little bit."
            call luna_main("...", 8, 1, 4, 3) 
            call luna_main("......", 7, 2, 4, 3) 
            call luna_main("*Ptew*", 6, 3, 4, 16) 
            ">Luna spits into her hand before placing it back on your cock."
    call gen_main("Mmmm... yes that's it, [luna_name]...", 4)
    call luna_main("...", 5, 1, 1, 1) 
    g9 "Just keep pumping those hands up and down."
    call luna_main("......", 5, 2, 4, 1) 
    if luna_choice == 1:
        g9 "Why don't you give those milky tits of yours a nice shake?"
        call luna_main("[l_genie_name]...", 5, 2, 1, 1) 
        call luna_main("(A little shake won't hurt...)", 3, 3, 1, 1) 
        ">Luna gently starts shaking her boobs as she jerks you off."
    else:
        g9 "Mmmm, yes... how about a little more spit [luna_name]?"
        g9 "Just to make sure everything is nice and lubricated..."
        call luna_main("...", 5, 2, 1, 1) 
        call luna_main("Alright...", 5, 3, 1, 1) 
        call luna_main("*Ptew*", 6, 3, 4, 16)  
        ">Luna spits into her hand again and places it back on your cock."
    ">She starts pumping your cock even faster."
    g9 "Gods yes..."
    g9 "(This is it, where should I cum?)"
    menu:
        "-On her face-":
            ">You place your hand on the top of Luna's head and slowly force it down to be level with your crouch."
            ">Her slender hands don't stop sliding up and down your length."
            call luna_main("[l_genie_name]!!!", 4, 1, 4, 6)
            g9  "Shhh [luna_name], I'm just giving you a closer look."
            call luna_main("...", 8, 3, 4, 2)
            $ luna_tears = 2
            call luna_main("{size=-5}please sir...{/size}", 5, 2, 4, 3)
            g9  "what [luna_name]?"
            call luna_main("Please don't...", 6, 3, 4, 3) 
            g9  "mmmm..."
            call luna_main("cum on my-", 5, 3, 4, 3) 
            hide screen luna
            with d3
            $ luna_wear_cum = True
            $ luna_cum = 7
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            call luna_main("!!!!!!", 4, 1, 4, 8)
            g9  "Argh! by the gods {size=+10}YES!{/size}"
            g9  "{size=+10}TAKE IT ALL!{/size}"

        "-On her shirt-":
            ">You place your hand on Luna's shoulder."
            ">Her slender hands don't stop sliding up and down your length."
            call luna_main("[l_genie_name]...", 4, 1, 4, 6)
            g9  "Shhh [luna_name], just keep stroking."
            call luna_main("...", 8, 3, 4, 2)
            $ luna_tears = 2
            call luna_main("{size=-5}please sir...{/size}", 5, 2, 4, 3)
            g9  "what [luna_name]?"
            call luna_main("Please don't...", 6, 3, 4, 3) 
            g9  "mmmm"
            call luna_main("cum on me-", 5, 3, 4, 3) 
            hide screen luna
            with d3
            $ luna_wear_cum = True
            $ luna_cum = 3
            show screen white 
            pause.1
            hide screen white
            pause.2
            show screen white 
            pause .1
            hide screen white
            with hpunch
            call luna_main("!!!!!!", 4, 1, 4, 8)
            g9  "Argh! by the gods {size=+10}YES!{/size}"
            g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
    g9  "mmmm....."
    m "That hit the spot..."
    call luna_main("[l_genie_name]!", 8, 1, 2, 9)
    call luna_main("How could you!", 7, 1, 3, 6)
    m "Ahh... that was fantastic, slut..."
    $ g_c_u_pic = "01_hp/08_animation_02/06_groping_01.png"
    call luna_main("[l_genie_name]!!!", 8, 1, 3, 15)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 600 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    pause
    hide screen luna
    with d3
    $ luna_flip = -1
    $ luna_r_arm = 2
    hide screen genie_sprite
    with d3
    call her_main("[genie_name], I hope you don't mind me coming in unannounced...","body_122")
    $ changeLuna(4, 1, 4, 3, 400)
    call her_main("But I really need a good-.","body_118")
    call her_main("...","body_48")
    call luna_main("...", 4, 2, 4, 3)
    m "..."
    pause
    call her_main("{size=+5}WHAT{/size}","body_79")
    $ changeLuna(4, 3, 4, 3)
    call her_main("{size=+10}THE{/size}","body_77")
    $ changeLuna(4, 2, 4, 3)
    call her_main("{size=+15}FRICK!{/size}","body_86")
    call luna_main("It's not what it looks-", 5, 2, 4, 6)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call her_main("{size=+15}petrificus totalus!{/size}","body_86")
    ">Hermione pulls out her wand with surprising speed and paralyzes Luna."
    call luna_main("!!!", 4, 1, 4, 6)
    m "(Whoa...)"
    call her_main("Honestly, sir, what are you thinking!","body_81")
    call her_main("If you need your filthy old cock jerked so badly you should just call me!","body_69")
    call luna_main("???", 4, 2, 4, 3)
    call her_main("But to be doing this with Luna Lovegood...","body_79")
    call her_main("She's not even a {size=+5}\"Gryffindor\"!{/size}","body_77")
    m "I wasn't pay-"
    call her_main("Shut up!","body_86")
    call her_main("How did you even get Luna to agree to this, sir?","body_79") 
    call her_main("I don't even think she knows what house she's in half the time.","body_77")
    call her_main("I can't imagine her sense of house pride is large enough to warrant this...","body_81")
    $ changeLuna(4, 3, 4, 2)
    m "I can explain this..."
    call her_main("Really? {p}Go on...","body_05")
    m "Well I was sitting here alone in my office."
    m "(What else can I do...)"
    m "When all of a sudden this weird hat on the shelf behind me starts talking!"
    call her_main("...","body_17")
    call her_main("Are you serious, sir?","body_61")
    m "I knew you wouldn't believe-"
    call her_main("Of course I believe you! It's the sorting hat!","body_77")
    m "(I keep forgetting that this place is magic...)"
    m "Yes, well... the \"sorting\" hat mentioned that it may have made a mistake with the sorting of some students."
    hat "..."
    m "So it offered to use \"Legitimancy\" or something to fix-"
    call her_main("You performed Legilimency?","body_18")
    call her_main("On a {size=+5}student{/size}!?","body_86")
    m "It's not that bad, surely..."
    call her_main("Sir, it's bad enough to use Legilimency to read someone's mind...","body_79")
    call her_main("but to use it to change their mind...","body_79")
    call her_main("I didn't even think it was possible...","body_77")
    m "So it's ok then?"
    call her_main("It's pretty frickin' far from OK...","body_86")
    call her_main("You have to Change her back!","body_79")
    m "Really? But this has been pretty fun."
    call her_main("I can't even believe I have to tell you how wrong this is sir!","body_77")
    call her_main("Change her back now or I tell the ministry everything.","body_30")
    m "What about your house-"
    call her_main("{size=+10}NOW!{/size}","body_86")
    m "Alright, alright, sheesh..."
    m "{size=-5}(these bitches be crazy!){/size}"
    m "Let me just get the hat."
    ">You reach around and pull the old leathery hat down from the dusty cupboard."
    hat "Ughh... Gently does it now."
    call her_main("Put it on her head.","body_79")
    hat "Well if it isn't Miss Granger..."
    call her_main("...","body_69")
    ">You place the sorting hat gently on top of Luna's head."
    m "There."
    call her_main("Well, change her back!","body_79")
    hat "Are you sure? She seemed much more entertaining this way..."
    call her_main("Do. {size=+5}it. {size=+5}NOW!{/size}","body_77")
    hat "Alright, alright. Sheesh."
    hat "You don't seem this bossy when you're in here normally..."
    call luna_main("!!!", 4, 1, 4, 3)
    call her_main("{size=+5}Shut up!{/size}","body_30")
    hat "One boring old Lovegood, coming right up."
    call luna_main("???", 4, 2, 4, 3) 
    call luna_main("......", 4, 3, 4, 2) 
    call luna_main(".....", 4, 1, 4, 2) 
    call luna_main("....", 4, 6, 4, 3) 
    call luna_main("...", 4, 6, 4, 2) 
    $ luna_reverted = True
    call luna_main("...", 4, 6, 4, 2) 
    hat "There, she's back to normal... {size=-8}sadly{/size}"
    call her_main("Are you certain?","body_81")
    hat "Yes, I'm sure of it. Can I go back up on the shelf now?"
    call her_main("Fine...","body_81")
    call her_main("But if you every try anything else like this again...","body_69")
    call her_main("...","body_79")
    ">You decide to place the hat back on the top of the cupboard."
    m "There, all better. now we can forget this whole thing ever happened."
    call her_main("You're not serious, are you?","body_81")
    m "What? Miss Lovesgood is back to normal..."
    call her_main("You're not getting away with this, sir.","body_79")
    m "I'm not sure what you're referring to?"
    call her_main("What I'm referring to?","body_77")
    call her_main("Luna Lovegood is {size=+10}COVERED {/size}in your cum!","body_76")
    m "Oh..."
    call her_main("more importantly, How many points did you pay her?","body_81")
    menu:
        "\"None\"":
            call her_main("What?","body_66")
            call her_main("I'm supposed to believe that she came up to your office...","body_79")
            call her_main("And let you jerk your disgusting old cock in front of her...","body_77")
            call her_main("For free?","body_79")
            ">You raise your hand to the air."
            m "Scouts honor!"
            call her_main("...","body_66")
            m "Besides, surely you'd notice a jump in \"Ravenclaw's\" points?"
            call her_main("I suppose you're right...","body_69")
            call her_main("If the sorting hat had manipulated her then doing this isn't out of the question.","body_69")
            call her_main("{size=-5}(But for her to do it so willingly...){/size}","body_12")
        "\"I paid her in gold.\"":
            call her_main("Gold?","body_66")
            m "Gold."
            call her_main("So, no points?","body_79")
            m "Not one."
            call her_main("I suppose that's OK then...","body_69")
            call her_main("{size=-5}(Why don't I ever get paid in gold...){/size}","body_50")
            call her_main("{size=-5}(No, Hermione! If I did that I'd be a prostitute...){/size}","body_33")
            call her_main("{size=-5}{image=textheart}{image=textheart}{image=textheart}{/size}","body_106")

    call her_main("Well regardless, she has to be punished.","body_79")
    m "Wait, she's being punished?"
    call her_main("Of course!","body_69")
    call her_main("Seeing as how you didn't give \"Ravenclaw\" any points you haven't done anything wrong.","body_17")
    call her_main("But her...","body_09")
    ">Hermione glares at the still frozen Luna Lovegood."
    call her_main("...","body_09")
    call her_main("She needs a punishment.","body_111")
    m "What are you thinking?"
    call her_main("Hmmm...","body_103")
    call her_main("Sorting hat!","body_79")
    hat "W-w-what? I'm trying to go to sleep..."
    call her_main("How long until Luna's back to normal?","body_101")
    hat "I'm not exactly sure... Probably twenty minutes."
    hat "Until then she'll pretty much be in a fairly lucid and suggestible state."
    call her_main("Good...","body_111")
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call her_main("liquescimus corporis!","body_30")
    ">Another flash of light as Luna becomes un-petrified."
    call luna_main("Ugh... where am I?", 6, 2, 4, 2)
    call her_main("Shhh, it's alright.","body_58")
    call luna_main("Hermione? What's happening?", 6, 1, 4, 2)
    call her_main("Nothing... Professor Dumbledore and I just needed your help.","body_59")
    call luna_main("What with?", 7, 1, 4, 3)
    call luna_main("And what's this stuff on-", 8, 2, 4, 2)
    call her_main("Shhh, that doesn't matter right now.","body_105")
    call her_main("Just head back to your common room...","body_107")
    m "is that really-"
    ">Hermione glares at you."
    call her_main("...","body_81")
    call luna_main("Alright, I'll go back to my common room...", 6, 1, 4, 3)
    call her_main("That's right...","body_105")
    ">Luna quietly exits the room."
    hide screen luna_chibi
    hide screen luna 
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    call her_main("Well, now that that's over...","body_69")
    call her_main("I think I'll be leaving as well...","body_61")
    m "Don't you want to stay a little longer?"
    call her_main("I don't think so, sir...","body_66")

    ">Hermione turns to leave."
    $ hermione_busy = True
    if daytime:
        $ hermione_takes_classes = True
    else:
        $ hermione_sleeping = True
    hide screen hermione_main
    with d3
    show screen genie
    hide screen chair_02
    hide screen desk_02
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    hide screen g_c_u
    call luna_reset
    jump end_hg_pf

    #result of this event:
        #Ability to redo all luna's favours with the real luna


label luna_revert_2: #Non-Reversion event
    show screen blkfade
    ">You stand up and walk around your desk, standing in front of Luna."
    ">You open your cloak and pull out your cock."
    hide screen bld1
    hide screen genie
    show screen chair_02
    show screen desk_02
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "jerking_off_02_ani"
    show screen g_c_u
    with fade
    hide screen blktone
    hide screen blkfade
    with d5
    pause
    m "Well..."
    call luna_main("...", 7, 8, 2, 3) 
    ">Luna looks down at your cock."
    call luna_main("Disgusting...", 9, 8, 3, 1) 
    ">She takes a firm hold of it with her right hand"
    $ luna_r_arm = 3
    $ genie_sprite_xpos = 300
    $ luna_xpos = 390
    call gen_main("!!!", 4, 2)
    call luna_main("*Hmmph* At least it isn't small...", 5, 8, 2, 1) 
    call luna_main("(I can't even fit my hand around it.)", 5, 3, 3, 1) 
    ">Luna slowly starts stroking your cock with her hand, her movements are rough and inexperienced."
    m "Why don't you try grabbing it with both hands [luna_name]..."
    call luna_main("Hmph... you wish!", 8, 1, 2, 1) 
    m "..."
    ">Luna starts moving her hand back and forth along the length of your cock."
    m "Yes, that's it..."
    call luna_main("(Men really are the worst)", 6, 3, 3, 3) 
    m "Mmmm, yes... just like that [luna_name]..."
    call luna_main("Is this good [l_genie_name]?", 6, 1, 4, 14) 
    m "yes, yes, this is amazing..."
    call luna_main("good...", 6, 1, 4, 1) 
    call luna_main("but...", 6, 2, 4, 2) 
    call luna_main("Do you need a little more encouragement?", 8, 1, 4, 1) 
    m "What are you thinking?"
    call luna_main("......", 9, 8, 3, 1) 
    menu:
        "-Luna takes her top off-":
            ">Luna slowly removes her vest and starts to unbutton her top."
            m "Mmmm"
            $ luna_wear_top = False
            $ luna_choice = 1
            ">She takes her shirt off and places it onto the floor."
            call luna_main("There...", 8, 2, 4, 1) 
            m "Very nice [luna_name]!"
            call luna_main("...", 7, 8, 4, 2) 
            call luna_main("Thank you sir...", 7, 1, 4, 1) 
            ">She places her hands back around your cock."
            call luna_main("Mmm, much better...", 5, 8, 2, 1) 
            m "Gods yes."
            call luna_main("...", 5, 1, 2, 1) 
            call luna_main("I'd take my bra off as well...", 5, 2, 4, 2) 
            call luna_main("But I don't think you'd be able to stop yourself from cumming on the spot, would you?", 8, 1, 3, 1) 
            g4 "probably not!"
            call luna_main("...", 9, 8, 2, 1) 
            ">Luna starts pumping your cock a little faster."
        "-Luna teases you-":
            $ luna_choice = 2
            call luna_main("Come on Professor...", 8, 2, 4, 1) 
            ">Luna starts moving her hands up and down your cock a little faster."
            m "mmmm..."
            call luna_main("Get a nice big load ready for me...", 7, 8, 4, 2) 
            m "Ah yes..."
            call luna_main("get ready to cum all over your student.", 7, 1, 4, 1) 
            ">She speeds up the pace."
            call gen_main("Ah...", 2)
            call luna_main("What's wrong?", 7, 1, 5, 2) 
            m "Well if you go that fast the friction's a little painful."
            call luna_main("Really?...", 8, 1, 2, 1) 
            ">Luna doesn't slow down. If anything she speeds up slightly."
            g4 "Ah!"
            call luna_main("...", 9, 1, 3, 1) 
            g4 "[luna_name]..."
            call luna_main("Hmmm, do You want me to spit on your cock then?", 5, 1, 5, 1) 
            g4 "Just a little bit..."
            call luna_main("...", 5, 1, 2, 1) 
            call luna_main("......", 5, 1, 3, 1) 
            g4 "Please..."
            call luna_main("Good boy.", 7, 1, 2, 1) 
            call luna_main("*Ptew*", 5, 8, 2, 16) 
            ">Luna spits into her hand before placing it back on your cock."
    call gen_main("Mmmm, yes that's it [luna_name]...", 4)
    call luna_main("...", 7, 8, 2, 1) 
    g9  "Just keep pumping that hand up and down."
    call luna_main("......", 8, 1, 3, 1) 
    if luna_choice == 1:
        ">Luna gently starts shaking her boobs as she jerks you off."
    else:
        call luna_main("*Ptew*", 8, 8, 3, 16) 
        ">Luna spits into her hand again and places it back on your cock."
    ">She then starts pumping your cock even faster."
    g9  "Gods yes..."
    g9  "(This is it, where should I cum?)"
    menu:
        "-On her face-":
            ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

        "-On her tits-":
            ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

    call luna_main("[l_genie_name]!!!", 7, 1, 3, 6) 
    call luna_main("You're not trying to cum on me are you?", 8, 1, 3, 3) 
    g9  "Ah [luna_name], I'm almost there."
    call luna_main("Well...", 9, 8, 3, 3) 
    $ luna_wear_skirt = False
    ">Luna quickly pulls down her skirt."
    g9  "!!!"
    call luna_main("You cum...", 8, 1, 3, 3) 
    g9  "Ah..."
    ">Luna slowly pulls her panties forward, exposing her pussy to the air."
    ">Her right hand is still wrapped around your cock as she pumps it with blinding speed."
    call luna_main("Where I tell you...", 9, 1, 3, 3) 
    g9  "mmmm"
    call luna_main("Now...", 8, 1, 3, 2) 
    call luna_main("Cum.", 5, 1, 2, 1) 
    $ g_c_c_u_pic = "jerking_off_cum_ani"
    show screen g_c_c_u
    $ luna_wear_cum_under = True
    $ luna_cum = 10
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    ">You start shooting your load directly into Luna's panties, coating her pussy in cum."
    g9  "Argh! by the gods {size=+10}YES!{/size}"
    call luna_main("...", 5, 3, 1, 1)
    call luna_main("(It's so warm...)", 5, 2, 4, 1)
    g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
    g9  "mmmm....."
    hide screen g_c_c_u
    $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png"
    m "That hit the spot..."
    call luna_main("({image=textheart}{image=textheart}{image=textheart})", 5, 8, 4, 1)
    call luna_main("[l_genie_name]!", 8, 1, 3, 1)
    call luna_main("How could you! Cumming on your students {size=-10}pussy{/size}...", 7, 8, 2, 1)
    m "Ahh... that was fantastic slut..."
    $ g_c_u_pic = "01_hp/08_animation_02/06_groping_01.png"
    call luna_main("[l_genie_name]...", 6, 2, 2, 1)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 600 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    hide screen luna 
    with d3
    $ luna_flip = -1
    $ luna_r_arm = 2
    hide screen genie_sprite
    with d3
    call her_main("[genie_name], I hope you don't mind me coming in unannounced...","body_122")
    call her_main("But I really need a good-.","body_118")
    $ changeLuna(4, 1, 4, 3, 400)
    call luna_main("...", 7, 1, 3, 3)
    call her_main("...","body_72")
    m "..."
    pause
    call her_main("{size=+5}WHAT{/size}","body_79")
    $ changeLuna(8, 1, 3, 3)
    call her_main("{size=+10}THE{/size}","body_77")
    $ changeLuna(9, 1, 3, 3)
    call her_main("{size=+15}FRICK!{/size}","body_86")
    call her_main("What on earth is going on-","body_77")
    call luna_main("{size=+15}petrificus totalus!{/size}", 8, 1, 3, 15)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    ">Luna pulls out her wand with surprising speed and paralyzes Hermione."
    call her_main("!!!","body_89")
    m "(Whoa...)"
    hide screen luna
    with d3
    $ luna_flip = 1
    $ changeLuna(9, 1, 3, 7, 400)
    ">Luna turns back around to face you, leaving Hermione paralyzed in the middle of the room. "
    call luna_main("{size=+15}What is the meaning of this?{/size}", 7, 1, 3, 7)
    m "I don't know, Miss Granger must have come up here to ask for something."
    call luna_main("The door was locked!", 9, 1, 2, 6)
    call luna_main("And everyone knows your door is enchanted against every spell possible!", 8, 1, 3, 4)
    m "(It is?)"
    call luna_main("So she must have had a key...", 5, 3, 3, 4)
    m "..."
    call luna_main("Why does she have a key [l_genie_name]?", 9, 1, 3, 3)
    m "Ah... um..."
    menu:
        "\"To buy favours\"":
            pass

        "\"I don't know\"":
            call luna_main("...", 9, 1, 3, 4)
            call luna_main("Really? You don't know...", 8, 1, 3, 6)
            m "No idea..."
            call luna_main("Well then, we'll just have to ask hermione...", 7, 2, 3, 4)
            call her_main("...","body_94")
            call luna_main("I'm sure that some Veritaserum will clear things up...", 7, 1, 3, 6)
            call her_main("!!!","body_95")
            m "(Is that bad?)"
            ">Hermione gives you a pleading look with her eyes."
            call her_main("...","body_97", "tears_02")
            m "(Probably...)"
            m "Um..."
            call luna_main("Go on old man...", 9, 1, 3, 2)
            m "She's here to buy favours..."



    call luna_main("{size=+5}WHAT{/size}", 4, 1, 3, 7)
    call luna_main("To think that I came here and let you leer at my body...", 9, 1, 3, 6)
    call luna_main("While you stroked that filthy cock of yours...", 8, 8, 3, 6)
    call luna_main("and all the while you've been throwing your gold away to some \"Gryffin-{size=+5}WHORE{/size}\"!", 7, 1, 3, 3)
    call luna_main("well then, How much have you paid her?", 9, 1, 2, 2)
    hide screen luna
    with d3
    $ luna_flip = -1
    call luna_main("How much have you wasted on this fat assed tart?", 8, 1, 3, 3)

    $ point_estimate = (gryffindor-200)
    m "All up? probably about [point_estimate] points..."
    hide screen luna
    with d3
    $ luna_flip = 1
    call luna_main("[point_estimate]... {p}points?", 7, 1, 5, 2)
    m "you know. For \"gryffiedoore\"..."
    call luna_main("...", 5, 1, 5, 2)
    call luna_main("hahahaha!", 2, 1, 1, 11)
    call her_main("...","body_103")
    m "..."
    hide screen luna
    with d3
    $ luna_flip = -1
    ">Luna turns back around to face hermione."
    call luna_main("really? you sell your body for points?", 5, 2, 1, 5)
    call her_main("...","body_81")
    call luna_main("Oh right, I suppose I should probably undo that.", 7, 1, 2, 4)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("liquescimus corporis!", 5, 1, 2, 15)
    ">Another flash of light as Hermione becomes un-petrified."
    $ changeLuna(5, 2, 1, 1, 400)
    call her_main("Professor! What is the meaning of this!","body_30")
    call her_main("And what were the two of you doing before I got here?","body_77")
    call luna_main("oh... I was just helping out Professor Dumbledore...", 5, 3, 1, 2)
    call her_main("helping out how?","body_79")
    call luna_main("just to relieve some... tension. {p}Don't worry he isn't going to pay me in points... *tssk*", 7, 2, 1, 1)
    call her_main("what?","body_76")
    call her_main("[genie_name]! What are you doing!","body_30")
    m "Ah...."
    call luna_main("don't blame him. It's not his fault you fail to satisfy...", 8, 1, 2, 1)
    call her_main("You... you...","body_79")
    call her_main("{size=+10}You Stupid whore!{/size}","body_77")
    call her_main("{size=+15}You're nothing more than a prostit-{/size}","body_76")
    call luna_main("{size=+15}petrificus totalus!{/size}", 9, 1, 3, 15)
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    ">Luna paralyzes Hermione for the second time."
    $ changeLuna(9, 1, 3, 2, 400)
    call her_main("!!!","body_95")
    call her_main("...","body_77")
    ">Hermione stares at Luna with a blind rage."
    m "Should you really be doing that?"
    hide screen luna
    with d3
    $ luna_flip = 1
    call luna_main("*Hmmmph*", 5, 2, 2, 3)
    ">Luna huffs, ignoring the question."
    call luna_main("Honestly [l_genie_name], I don't know what you see in her...", 7, 1, 2, 2)
    pause
    call luna_main("So, how should we punish her?", 5, 2, 1, 5)
    call her_main("!!!","body_95")
    m "Punish her?"
    call luna_main("Of course! For what she said.", 5, 1, 2, 11)
    call her_main("...","body_88")
    call luna_main("You're not going to let her get away with that are you?", 7, 1, 3, 3)
    menu:
        "-Tell her to let hermione go-" if False:
            m "Unfreeze miss granger."
            call luna_main("What? You're taking her side?", 5, 3, 1, 1)
            m "(Ugh... bitches...)"
            m "I'm not taking anyone's side. I'll punish Miss granger appropriately later."
            call luna_main("...", 5, 3, 1, 1)
            call luna_main("Whatever...", 5, 3, 1, 1)
            show screen white 
            pause .1
            hide screen white
            $ renpy.play('sounds/magic4.ogg')   #Not loud.
            call luna_main("liquescimus corporis!", 5, 3, 1, 1)
            call her_main("...","body_122")
            m "That will be all for now miss lovegood."
            call luna_main("...", 5, 3, 1, 1)
            call luna_main("You better punish her...", 5, 3, 1, 1)
            jump luna_away
            call her_main("...","body_122")

        "-Let Luna decide-":
            pass
    m "I'll leave the punishment to you."
    call luna_main("Yes, you're probably right.", 5, 3, 1, 1)
    hide screen luna
    with d3
    $ luna_flip = -1
    ">Luna turns to face hermione."
    call luna_main("Hmmm, what should I do...", 8, 1, 3, 1)
    call luna_main("...", 5, 1, 2, 1)
    call her_main("...","body_94")
    call luna_main("I've got it!", 4, 1, 2, 5)
    hide screen hermione_main 
    with d3
    ">Luna places her hands on Hermione's shoulders and gently forces her paralyzed body to her knees."
    $ hermione_SC.chibi.xpos = 40 #40 = Near Luna
    $ hermione_SC.chibi.ypos = 60
    $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/08_sits.png"
    call luna_main("That should be about right...", 5, 8, 2, 1)
    call luna_main("wait...", 5, 8, 1, 2)
    if luna_wear_top:
        $ luna_wear_top = False
        ">Luna quickly removes her top."
    ">Luna places her hand on hermione's chin and gently turns her head upwards."
    call luna_main("Perfect...", 5, 8, 1, 5)
    call her_kneel("...","body_29")
    call luna_main("Now, before you so rudely decided to interrupt us, Professor Dumbledore made a nasty mess...", 5, 3, 1, 1)
    call her_kneel("...","body_28")
    call luna_main("I was going to go back to my room and tidy up before class but seeing as how your interruption has taken so long, you'll have to tidy me up instead.", 5, 2, 2, 1)
    call her_kneel("...","body_33")
    hide screen luna 
    with d3
    $ luna_wear_panties = False 
    show screen luna
    with d3
    ">Luna slowly pulls down her panties, revealing her cum-soaked pussy."
    call her_kneel("!!!","body_43")
    call luna_main("Well... {p}get to work!", 8, 8, 1, 5)
    ">Hermione glares at luna."
    call her_kneel("...","body_81")
    call luna_main("*Sigh* I guess I have to do everything then!", 7, 8, 2, 1)
    show screen blkfade
    hide screen hermione_kneel
    $ luna_l_arm = 3
    $ luna_xpos=635
    $ hermione_head_ypos=390
    $ hermione_kneel_leg = True
    ">Luna thrusts her mound forward, griding it under Hermione's nose and against her closed mouth."
    hide screen blkfade
    call her_kneel("!!!","body_97")
    m "!!!"
    call luna_main("Mmmm, that's it...", 5, 3, 1, 1)
    call luna_main("who's a good girl...", 5, 8, 1, 5)
    call her_kneel("!!!","body_33")
    call luna_main("mmmm... smells good doesn't it, slut?", 5, 3, 1, 1)
    call luna_main("mmmm... you look like you want more though...", 5, 3, 2, 5)
    $ luna_xpos = 550
    $ luna_l_arm = 1
    $ hermione_kneel_leg = False
    ">Luna takes a step back from hermione's face."
    call luna_main("Such a pretty face...", 5, 8, 4, 1)
    ">Luna places her thumb into hermione's paralyzed mouth, slowly opening it."
    call her_kneel("...","body_36")
    ">She grabs a hold of her tongue and slowly pulls it out until it hangs from her mouth."
    call her_kneel("oahhh hiiieerr!!!","body_40")
    m "(...)"
    call luna_main("Shhh....", 5, 3, 4, 2)
    $ luna_xpos=635
    $ luna_l_arm = 3
    $ hermione_kneel_leg = True
    ">Luna steps forward, placing her cum coated pussy on top of hermione's open mouth."
    call her_kneel("!!!","body_116")
    call luna_main("Shhh.... mmmm, that's not bad...", 5, 8, 1, 5)
    call her_kneel("...","body_115")
    call her_kneel("...","body_38")
    call her_kneel("......","body_39", "blush")
    call her_kneel(".........","body_215")
    call luna_main("Good girl...", 5, 8, 2, 5)
    call luna_main("Just enjoy yourself...", 5, 8, 2, 1)
    call luna_main("We both know who's the real slut now don't we?...", 7, 8, 3, 3)
    call her_kneel("...","body_215", "blush")
    call luna_main("Don't we?", 9, 8, 3, 5)
    call her_kneel("hheessss...","body_135", "blush")
    ">Hermione barely manages a muffled response."
    g9  "(This is too much!)"
    menu:
        "-Join in-" if False: #Have sex with hermione while luna grinds on her face. Needs chibi work
            show screen blkfade
            ">You walk over to hermione's kneeling form and pick up her limber body."
            call luna_main("Hey! I wasn't finished with her!", 5, 3, 1, 1)
            m "Don't worry, I'm just repositioning her. You can still have your fun."
            ">You carry hermione's stiff, paralyzed form over to your desk, placing her gently on top of it."
            hide screen blkfade
            call luna_main("...", 5, 3, 1, 1)
            m "Hmmm... I wonder if..."
            ">You start bending hermione's limbs, finding that they move easily but lock into place when you stop pushing."
            m "Huh, she's just like a barbie doll!"
            call her_kneel("hrohessor!","body_122")
            ">You bend her over your desk with her face pointing towards Luna."
            m "There, I trust you're still able to administer your punishment [luna_name]?"
            call luna_main("Mmmm, I think so...", 5, 3, 1, 1)
            ">Luna walks over to hermione and presses her sex back onto the girls open tongue."
            call luna_main("Ah... {image=textheart}", 5, 3, 1, 1)
            call her_kneel("...","body_122")
            ">You slowly lift hermione's skirt."
            call her_kneel("!!!","body_122")
            ">Revealing her sopping pussy."
            m "Mmmm..."
            m "Come on barbie..."
            ">You thrust your full length into hermione's cunt!"
            g9  "Let's go party!"
            call her_kneel("{image=textheart}{image=textheart}{image=textheart}","body_122")
            g9  "Gods yes!"
            call luna_main("mmmm {image=textheart}", 5, 3, 1, 1)
            ">You start fucking hermione in earnest."
            call luna_main("so [l_genie_name]...", 5, 3, 1, 1)
            call luna_main("How long has this been going on?", 5, 3, 1, 1)
            m "With miss granger? A while..."
            call luna_main("figures...", 5, 3, 1, 1)
            call luna_main("You always were a teacher's pet weren't you...", 5, 3, 1, 1)
            call her_kneel("{image=textheart}{image=textheart}{image=textheart}","body_122")
            call luna_main("I bet you even came here on your own didn't you...", 5, 3, 1, 1)
            call luna_main("Eager to sell your body for a few lousy points...", 5, 3, 1, 1)
            g9  "Yes..."
            call her_kneel("...","body_122")
            call luna_main("just so your house can win the cup this year...", 5, 3, 1, 1)
            call luna_main("you know no one cares about the house cup don't you?", 5, 3, 1, 1)
            ">You start thrusting even harder into hermione's dripping pussy."
            call her_kneel("hess heeyyy hoooo!!!","body_122")
            call luna_main("Let's see the shall we...", 5, 3, 1, 1)
            call luna_main("Professor...", 5, 3, 1, 1)
            m "Ah... yes?"
            call luna_main("Who won the house cup when you were in school...", 5, 3, 1, 1)
            m "(Shit! I have no idea who won the lousy cup when dumbiedoor was a kid.)"
            m "Um... ah..."
            ">Hermione's pussy squeezes around your cock."
            m "It seems to have... ah... slipped my mind."
            call luna_main("see...", 5, 3, 1, 1)
            call luna_main("Even dumbledore doesn't remember who won when he was a student...", 5, 3, 1, 1)
            call her_kneel("...","body_122")
            #hermione tears
            call luna_main("so that means you've done all this for nothing...", 5, 3, 1, 1)
            call luna_main("all the times you've sold your body...", 5, 3, 1, 1)
            call luna_main("all the times you've humiliated yourself...", 5, 3, 1, 1)
            call luna_main("even lying here eating me out while your precious dumbledore fucks you...", 5, 3, 1, 1)
            g9  "Yes..."
            call her_kneel("...","body_122")
            g9  "Argh!"
            call luna_main("you did it all just because you wanted to...", 5, 3, 1, 1)
            call her_kneel("...","body_122")
            g9  "{size=+5}yes!!!!{/size}"
            call luna_main("you...", 5, 3, 1, 1)
            call luna_main("filthy...", 5, 3, 1, 1)
            call luna_main("slut...", 5, 3, 1, 1)
            with hpunch
            g9  "{size=+7}Argh, TAKE THIS!!!{/size}"
            call cum_block
            g9  "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            $ g_c_u_pic = "sex_cum_in_ani"
            call cum_block
            show screen ctc
            pause
            hide screen ctc
            $ uni_sperm = True
            $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
            hide screen bld1
            with d3
            show screen ctc
            pause
            hide screen ctc
            show screen bld1
            with d3
            $ g_c_u_pic = "01_hp/08_animation_02/23_cum_19.png"


        "-Start jerking off-": #Jerk off and cum on hermione
            show screen blkfade
            hide screen hermione_kneel
            ">You walk over to hermione's kneeling form and pull your hardening cock out of your robe."
            lun "Mmmm, it's about time you started disciplining your students properly."
            $ genie_sprite_xpos = 450
            hide screen blkfade
            show screen hermione_kneel
            call gen_main("Maybe you're right.", 4, 3)
            $ genie_chibi_xpos = 50
            $ genie_cum_chibi_xpos = 50
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            ">You start stroking your cock, aiming it directly at hermione's face"
            call luna_main("I'm always right...", 8, 2, 1, 5)
            hide screen genie_sprite 
            with d3
            call her_kneel("...","body_39", "blush")
            m "Yes... that's it slut."
            call luna_main("Mmmm, I can see what you like about her...", 5, 8, 1, 1)
            ">Luna grinds herself hard against hermione's mouth."
            call her_kneel("...","body_135", "blush")
            call luna_main("She's much more tenable with her mouth full...", 8, 8, 1, 5)
            g9  "You're telling me!"
            call luna_main("so how long has this been going on [l_genie_name]?", 8, 2, 2, 1)
            m "A while now..."
            call luna_main("That doesn't surprise me...", 5, 8, 1, 3)
            call luna_main("I always figured Hermione was a repressed slut...", 5, 8, 2, 1)
            call luna_main("I bet she even came to you didn't she?", 5, 2, 2, 1)
            call her_kneel("...","body_215")
            m "Ah... yes, she did."
            call luna_main("Typical...", 7, 8, 2, 3)
            call luna_main("It figures that the head of the \"MRM\" would be a slut...", 8, 8, 3, 1)
            call her_kneel("...","body_135", "blush")
            call luna_main("desperate to sell her body...", 9, 8, 2, 5)
            call luna_main("all for a few points...", 5, 8, 1, 1)
            m "Yes... keep going..."
            call luna_main("Aww, Do you enjoy it when I degrade her [l_genie_name]?", 7, 2, 4, 1)
            g9  "Gods yes!"
            call luna_main("good...", 5, 2, 2, 1)
            call luna_main("because I expect you to coat this slut in your \"enjoyment\"...", 7, 8, 2, 5)
            g9  "Don't you worry!"
            g9  "One fresh load cumming right up!"
            call luna_main("hear that hermione?", 8, 8, 3, 5)
            call her_kneel("...","body_39", "blush")
            call luna_main("you're headmaster has a nice load of cum ready for you...", 9, 8, 2, 1)
            call luna_main("if you're lucky he might even give \"gryffindor\" some points...", 5, 3, 1, 11)
            g9  "Yes..."
            call her_kneel("...","body_40", "blush")
            call luna_main("Aww, you look so upset...", 5, 3, 4, 2)
            call luna_main("don't be sad... this is what you were born for...", 5, 8, 4, 5)
            call her_kneel("...","body_135", "blush")
            ">You start beating your meat with renewed determination!"
            call luna_main("you should be proud to take a thick load of cum from one of your teachers...", 7, 3, 4, 1)
            call luna_main("speaking of which... are you ready [l_genie_name]?", 5, 2, 2, 1)
            g9  "Argh! by the nine gods yes!"
            call luna_main("then cum!", 9, 2, 2, 5)
            $ g_c_c_u_pic = "jerking_off_cum_ani"
            show screen g_c_c_u
            g9  "{size=+7}Argh, TAKE THIS!!!{/size}"
            call luna_main("Cover this slut!", 8, 3, 2, 1)
            g9  "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            $ uni_sperm = True
            $ u_sperm = "01_hp/13_hermione_main/auto_15.png"
            $ luna_xpos = 550
            $ luna_l_arm = 1
            $ hermione_kneel_leg = False
            call her_kneel("!!!","body_136", "blush")

            ">Luna takes a step back as you simply erupt over Hermione's petrified expression."
            g9  "take it all, bitch!"
            g9  "{size=+15}ARGH!!!!!!!!!!!!!!!!{/size}"
            call her_kneel("!!!","body_133", "blush")
            ">You feel like your cumming more then you've ever cum in your life"
            g9  "take it all!"
            hide screen g_c_c_u
            $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png"
            $ u_sperm = "01_hp/13_hermione_main/auto_16.png"
            pause 
            call her_kneel("...","body_135", "blush")
            ">Hermione kneels before you, unable to move as her face is plastered with more cum than you've ever seen."
            ">You can barely make out her features through a wall of whiteness."

    m "Gods yes... that was amazing..."
    hide screen luna
    with d3
    $ luna_flip = 1
    $ luna_xpos = 400
    $ hermione_kneel_leg = False
    call luna_main("I'm glad you enjoyed yourself [l_genie_name]...", 5, 2, 1, 1)
    $ luna_wear_skirt = True 
    $ luna_wear_panties = True 
    $ luna_wear_cum_under = False 
    $ luna_wear_top = True
    show screen genie
    hide screen chair_02
    hide screen desk_02
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    hide screen g_c_u
    $ luna_chibi("stand")
    ">Luna quickly puts her panties and clothes back on."
    call her_kneel("...","body_133", "blush")
    call luna_main("but How much would you say you enjoyed yourself?", 7, 1, 2, 1)
    m "A lot..."
    call luna_main("And if you had to put a number on your enjoyment?", 8, 1, 2, 3)
    m "Oh... um I'd say about 250?"
    call luna_main("Fantastic!", 2, 1, 1, 1)
    m "..."
    m "Here's your payment [luna_name]."
    $ gold -= 250
    $ luna_gold += 250
    call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
    call luna_main("Well, I best be off then. I'm late for class.", 5, 2, 2, 2)  
    m "Aren't you going to fix up Hermione first?"
    call her_kneel("...","body_134", "blush")
    call luna_main("Really? You're too lazy to cast a few simple spells?", 7, 1, 2, 2)  
    m "Ah... I'm a little tired after all that..."
    m "I think it's for the best if you did it."
    call luna_main("Fine... I suppose you'll want me to wipe her memories too?", 5, 2, 1, 2)  
    m "Wipe her memories?"
    call her_kneel("???","body_97")
    call luna_main("Of course. I mean what we just did to her was a little questionable...", 7, 1, 2, 2)  
    call luna_main("A memory charm would proably be for the best.", 8, 2, 1, 1)  
    call her_kneel("!!!","body_185")
    m "(I think I've underestimated the magic at this school...)"
    m "Ah sure... why not..."
    hide screen luna
    with d3
    $ luna_flip = -1
    call luna_main("I guess I'll clean her up as well...", 6, 8, 2, 2)  
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("scourgify!", 7, 1, 2, 15)
    $ uni_sperm = False
    ">All the cum vanishes from hermione's body."
    call her_kneel("...","body_82")
    m "Woah..."
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("obliviate!", 8, 1, 2, 15)
    ">Another flash of light as hermione's eye's glaze over."
    call her_kneel("...","body_225")
    m "..."
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("liquescimus corporis!", 7, 1, 3, 15)
    ">Hermione collapses to the floor in a limp heap."
    call her_kneel("agh...","body_226")
    hide screen hermione_kneel
    with d3
    m "(Is it over?)"
    show screen white 
    pause .1
    hide screen white
    $ renpy.play('sounds/magic4.ogg')   #Not loud.
    call luna_main("vestimenta lacus!", 9, 1, 2, 15)
    ">All of Hermione's clothes wriggle like worms back onto her body."
    hide screen luna
    with d3
    $ luna_flip = 1
    call luna_main("There...", 7, 2, 2, 2)    
    call luna_main("Will that be all [l_genie_name]?", 6, 1, 2, 1)
    m "That will do for now [luna_name]."
    ">Luna turns to leave your office with Hermione still in a heap on the floor."
    call luna_main("See you next time...", 9, 1, 3, 1)    

    hide screen luna_chibi
    hide screen luna
    with d3

    ">You turn towards Hermione."
    m "[hermione_name]? Are you OK?"
    call her_main("agh... what happened?","body_87")
    call her_main("Was Luna lovegood here?","body_44")
    m "Who?"
    call her_main("never mind...","body_33")
    call her_main("I think I'm going go now [genie_name]...","body_34")
    m "Alright, well have a nice day."
    call her_main("ugh...","body_85")
    call her_main("(I could have sworn Luna was here...)","body_29")
    call her_main("(Wait, what was I doing here...)","body_17")
    call luna_reset
    jump end_hg_pf
    #result of this event:
        #Ability to get Luna to summon hermione for threesome (Planned future event)



label luna_reverted_greeting_1: #reverted Luna explains the wrackspurt problem
    $ luna_corruption += 1
    $ luna_wear_glasses = True
    $ luna_wear_acc = True
    $ luna_l_arm = 1
    $ luna_r_arm = 2
    $ luna_hair = 2
    $ l_genie_name = "sir" #reset genie's name with Luna
    $ luna_name = "Miss Lovegood" #reset luna's name with genie
    "*Knock* *Knock* *Knock*"
    lun "Hello?"
    m "(Sounds like Luna...)"
    menu:
        "-Let her in-":
            m "Come in!"
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ luna_chibi("stand")
            ">Luna stands in front of your desk."
            call luna_main("Hello Professor...", 1, 1, 4, 1) 
            m "Miss Lovegood."
            pass


        "-Tell her to go away-":
            m "(SHe's probably here because of that thing with the hat!)"
            m "Ugh... I'm not here!"
            lun "..." 
            ">Your door opens as Luna walks in."
            $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            $ luna_chibi("stand")
            ">Luna stands in front of your desk."
            call luna_main("Hello Professor...", 1, 1, 4, 1) 
            m "Oh, um... Hello miss lovegood."

    $ luna_l_arm = 1
    $ luna_r_arm = 1
    call luna_main("...", 1, 2, 4, 1) 
    call luna_main("......", 1, 3, 4, 2) 
    ">Luna starts looking around your room."
    call luna_main("There's such a strange aura in here...", 6, 2, 2, 2) 
    call luna_main("it's like a big hollow tree...", 1, 2, 4, 2)
    m "..."
    m "(What?)"
    m "Can I help you with something?"
    call luna_main("oh... there was something I came here for, wasn't there...", 1, 3, 4, 3) 
    m "(What's going on here? I thought the hat wiped her mind!)"
    call luna_main("I remember! The wrackspurt infestation!", 2, 2, 4, 1) 
    menu: 
        "\"Wrackspurts?... Is that some sort of wizard STD?\"":
            call luna_main("Hahaha, I guess you could say that, Professor! ", 1, 2, 4, 1)
            call luna_main("Wrackspurts are invisible creatures which float into a person’s ear and make their brain go all fuzzy.", 1, 1, 4, 2)
            $ luna_l_arm = 2
            call luna_main("You can only view them wearing these spectrespecs!", 1, 4, 1, 1)
            $ luna_l_arm = 1
            m "I see... (This bitch really is crazy!)"
            m "(Maybe the hat was good for her...)"
            m "Well, Miss Lovegood, what can we do about it?"
            call luna_main("I am not sure, professor... normally thinking positive thoughts is enough to remove them, but I am having trouble with these. If my father, Xenophilius-", 7, 2, 4, 2)
            "*Genie jumps from the table*"
            g4 "DID YOU JUST CAST A SPELL ON ME?!"
            $ luna_l_arm = 2
            $ luna_r_arm = 2
            call luna_main("Professor?", 4, 1, 4, 3)
            g4 "EXPLAIN YOURSELF!"
            $ luna_l_arm = 1
            $ luna_r_arm = 1
            call luna_main("I am sorry Professor, I am not sure what-", 4, 2, 4, 2)
            g4 "XENOFIUS! What does it do?"
            call luna_main("Xenofius? I’ve not heard of that spell before, Professor.", 7, 1, 4, 2)
            m "The spell... That you just... Never mind."
            call luna_main("(A Secret spell?) Professor, your magic is the strongest in Hogwarts and these wrackspurts are really getting to me.", 8, 2, 4, 3)
            m "I see... do go on."
        "\"I am afraid I can’t help you Miss Lovegood.\"":
            call luna_main("Oh please, Professor! You’re the only one powerful enough to help.", 4, 1, 4, 15)
            "*You can see Luna is rocking her pelvis as though she were grinding the air*"
            m "Miss Lovegood, I am afraid I don’t know what a wrackspurt is, let alone how to cure it."
            call luna_main("Well, professor; wrackspurts are detailed on page 6 of The Quibbler! Here!", 1, 1, 4, 2)
            "*Luna hands you a Quibbler*"
            m "*Reading* “Rotfang conspiracy... 300 ways to tie up a ghost... “ Ah! Wrackspurts..."
            "\"Invisible creatures which float into a person’s ears, making his/her brain go fuzzy\""
            "*Luna points to her spectrespecs* "
            call luna_main("I can see them, Professor.", 2, 1, 1, 1)
            m "I see...(No wonder Hermione called her Loony Lovegood)."
        "\"What in Agrabah are you wearing?\"":
            call luna_main("Oh! These are my spectrespecs, professor!", 1, 5, 4, 1)
            m "(Please don’t be mind-reading, please don’t be mind-reading-)"
            call luna_main("They help me see the wrackspurts.", 1, 1, 4, 2)
            m "(Thank the great desert sands!)"
            call luna_main("And these are my plum earrings.", 1, 4, 4, 1)
            m "Ah yes, very nice..."
            m "So about these wrecksputs..."

    call luna_main("Yes, Professor, they’re proving to be quite a pain.", 3, 1, 4, 2)

    "*Luna is visibly grinding her pelvis against her thighs.*"
    m "(Is she really?... Ohhh). Miss Lovegood, how exactly do these wickspurts make you feel?"
    call luna_main("they're Just like the quibbler says sir, except...", 5, 2, 4, 2)
    m "Go on..."
    call luna_main("Well, it's not my brain they're making fuzzy.", 5, 3, 4, 14)
    m "Where exactly is fuzzy, miss lovegood?"
    call luna_main("Umm... I'm not sure if I can say...", 5, 2, 4, 2)
    m "(YES!)"
    m "Now now, miss lovegood. as your headmaster there shouldn't be anything that you can't say to me."
    call luna_main("Well, alright...", 5, 3, 4, 1)
    call luna_main("the fuzziness is in between my legs, sir...", 5, 1, 4, 1)
    m "Really? That seems quite strange..."
    call luna_main("It is sir! I've only ever heard of people's brains going fuzzy...", 1, 1, 4, 2)
    call luna_main("but this...", 7, 1, 4, 2)
    call luna_main("it's like this unbearable itch I can't scratch...", 5, 3, 4, 3)
    m "(I know that feeling.)"
    call luna_main("and I feel like I can't quite remember what I've been up to over the last few days...", 6, 2, 4, 2)
    m "Oh um... I wouldn't worry about that at all..."
    m "Let's just focus on this fuzziness of yours."
    call luna_main("Alright, professor...", 5, 3, 4, 2)
    call luna_main("As I was saying, this fuzziness has really been bothering me the last few days...", 5, 1, 4, 2)
    m "Hmmm, has it been affecting your studies at all?"
    call luna_main("yes, it has, sir...", 5, 3, 4, 3)
    m "Well, we can't have that now, can we?"
    call luna_main("no, sir...", 5, 1, 4, 1)
    m "Are you free at the moment?"
    call luna_main("Umm... I'm about to go to divination class, sir...", 5, 3, 4, 2)
    m "Well, in that case, we'll address that nasty itch of yours later on."
    m "Come to my office later tonight, and we'll see what we can do."
    call luna_main("Oh, thank you, sir!", 4, 1, 4, 1)
    call luna_main("I can't wait!", 5, 1, 4, 1)
    call luna_main("Do you think you could possibly stop the nargles stealing my shoes as well?", 1, 3, 4, 1)
    m "(What the hell is a nargle?)"
    m "One step at a time, miss lovegood."
    call luna_main("yes, you're right... the nargles wouldn't like it if we were multitasking...", 3, 1, 4, 2)
    m "..."
    call luna_main("well, I'd best be off... goodbye professor!", 2, 1, 1, 1)
    "*Luna skips out of the room, squeezing her legs together as she prances.*"
    m "(This is going to be fun!)"
    $ luna_wear_glasses = True
    jump luna_away


label luna_reverted_greeting_2: #Explaining to Luna what will happen or something
    $ luna_corruption += 1
    "*knock* *knock* *knock*"
    m "Come in..."
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ luna_chibi("stand")
    ">Luna stands in front of your desk."
    call luna_main("Hello, Professor...", 2, 1, 1, 1) 
    m "Miss Lovegood. So, Did the wickerspats leave you alone today?"
    call luna_main("Not at all! They were worse than ever!", 1, 2, 2, 3)
    m "Really?"
    call luna_main("Really, sir. And I don't think it's just me they're affecting either.", 1, 1, 4, 2)
    call luna_main("I fear the whole school is becoming overrun!", 4, 1, 4, 2)
    m "What makes you say that?"
    call luna_main("The way people are acting...", 7, 2, 4, 2)
    call luna_main("It's very strange, don't you think, sir?", 7, 1, 4, 3)
    m "(Like this crazy bitch can call anyone strange!)"
    m "Strange how?"
    call luna_main("it's Their auras sir!", 3, 2, 4, 2)
    m "Oh..."
    call luna_main("They're far too red!", 7, 1, 4, 2)
    m "Too red?"
    call luna_main("I'm afraid so...", 7, 2, 4, 3)
    m "And you think these wackspots are to blame?"
    call luna_main("I'm not sure...", 5, 3, 4, 2)
    call luna_main("According to my father's beastiaries, they should only ever produce a grey tinge to an aura...", 5, 2, 4, 2)
    call luna_main("For them to be making auras red...", 4, 3, 4, 3)
    call luna_main("It could be very dangerous!", 4, 1, 4, 2)
    m "(Pffft... auras...)"
    m "yes, I see how that could be dangerous..."
    "*Luna starts grinding her thighs together.*"
    call luna_main("yes...", 5, 3, 4, 1)
    call luna_main("So, about this itch, sir...", 5, 1, 4, 1)
    m "Yes."
    call luna_main("Did you say you had some way to get rid of it?", 5, 1, 4, 2)
    m "I did."
    call luna_main("well...", 5, 2, 4, 3)
    m "well, the first thing's first I need something from you, miss lovegood."
    call luna_main("Something from me?", 4, 1, 4, 4)
    m "Yes, I need a promise."
    call luna_main("oh...", 1, 2, 4, 2)
    call luna_main("alright then!", 2, 1, 4, 1)
    m "I haven't even told you what it is yet."
    call luna_main("Don't worry sir, I trust you!", 4, 1, 1, 1)
    m "(this might be too easy!)"
    m "Yes well, the techniques I'm going to be showing you are proprietary so I'm going to have to make you promise not to talk to anyone about what goes on in this room."
    call luna_main("techniques...", 5, 2, 4, 2)
    call luna_main("proprietary...", 5, 3, 4, 3)
    call luna_main("I'm not sure I understand, sir.", 5, 1, 4, 2)
    m "Well, if what you're saying is correct, even if I use some powerful magic to remove them..."
    m "(I hope she buys this...)"
    m "They'll soon be back, and in greater numbers."
    call luna_main("...", 5, 2, 4, 2)
    m "(Did she buy it?)"
    call luna_main("yes, You're right, sir.", 3, 2, 4, 2)
    m "(YES!)"
    call luna_main("But are there really techniques to dispell them?", 5, 1, 5, 2)
    m "There are, but as I said, if you want to learn them you have to promise not to tell anyone what happens here."
    call luna_main("I suppose that's only fair, This information would be worth more than a snorkack sighting!", 1, 1, 4, 1)
    m "..."
    m "well, it's Not just the techniques miss lovegood."
    m "You must promise to tell anyone anything that happens in this room, no matter what."
    call luna_main("well...", 5, 2, 4, 2)
    "*You can see Luna is awkwardly rocking her pelvis*"
    call luna_main("alright then...", 5, 1, 4, 1)
    call luna_main("I solemnly swear that I will tell no one what happens within these hallowed walls...", 3, 2, 1, 2)
    m "Fantastic!"
    call luna_main("so, can you please teach me the techniques, sir?", 4, 1, 4, 1)
    ">There's a desperate need in Luna's eyes that excites you to no end."
    m "yes, yes. I think I've made you wait long enough."
    call luna_main("Thank you so much!", 2, 2, 1, 1)
    m "No need to thank me, miss lovegood, I'm simply doing what any good teacher should."
    m "Now, stand in the middle of the room for me."
    hide screen luna 
    with d3
    $ luna_xpos = 400
    call luna_main("is Here ok?", 1, 1, 4, 4)
    m "Perfect."
    m "Before we begin I have to explain a few things."
    ">Luna stares at you intently."
    call luna_main("...", 7, 1, 4, 2)
    m "From what I can tell these rockspits seem to have infected an unusual part of your body."
    call luna_main("Yes... Normally they only make your head fuzzy.", 7, 2, 4, 4)
    m "And how do you get rid of them in that situation?"
    call luna_main("By thinking positive thoughts, sir...", 2, 2, 4, 1)
    m "Correct."
    m "So, in your current situation, you simply need to focus positive thoughts on the affected area."
    call luna_main("...", 1, 2, 5, 2)
    call luna_main("How do I do that?", 1, 1, 4, 3)
    m "We'll try some self-applied massage to the area to start with."
    call luna_main("So I just start massaging the area that they're making fuzzy?", 1, 1, 4, 14)
    m "That's correct, I'll be here to give you some guidance."
    call luna_main("thank you, professor!", 2, 2, 4, 1)
    m "You're quite welcome."
    call luna_main("...", 1, 3, 4, 1)
    $ luna_l_arm = 4
    ">Luna quickly puts her hand down her skirt, barely acknowledging the nature of her actions."
    call luna_main("ah...", 5, 3, 4, 2)
    m "Is everything alright, miss lovegood?"
    call luna_main("ah... of course!", 4, 1, 4, 1)
    call luna_main("It's just a little sensitive...", 5, 3, 4, 1)
    m "That's to be expected. Keep going."
    call luna_main("ah... yes sir...", 2, 2, 4, 2)
    g4 "..."
    call luna_main("ah... is this how it should be done?", 1, 8, 4, 4)
    m "As long as it's feeling good I'm sure it's working. If you keep this up I'm sure you'll be rid of those nasty wickerspoons."
    call luna_main("that's nice...", 3, 2, 4, 1)
    call luna_main("...", 1, 8, 4, 2)
    call luna_main("are you sure this will work, sir?", 5, 1, 4, 14)
    m "Of course I am! Do you dare doubt the powerful Dumbelldoor?"
    call luna_main("certainly not, sir...", 4, 2, 4, 2)
    call luna_main("it's just...", 5, 3, 4, 2)
    call luna_main("I'm not sure this is going to get rid of them...", 5, 1, 4, 4)
    m "What makes you say that?"
    call luna_main("do you remember how I said the wickerspats were like a nasty itch, sir?", 5, 2, 4, 2)
    m "I do."
    call luna_main("well... as nice as this massage feels...", 5, 3, 4, 2)
    call luna_main("it's not really scratching that itch sir...", 7, 8, 4, 4)
    call luna_main("... {p}am I doing it wrong, sir?", 5, 1, 4, 2)
    m "Certainly not, but this is worse than I feared."
    call luna_main("really?", 4, 1, 4, 2)
    m "Yes. It would seem that those nasty critters are trying to hide."
    call luna_main("Hide? Where?", 4, 3, 4, 2)
    m "Well, as long as you're still feeling that itch they can't have gone far."
    m "But this means you'll have to chase them down."
    call luna_main("chase them down?", 5, 1, 5, 2)
    m "Don't worry, I'll be here to guide you through it."
    call luna_main("thank you, sir.", 1, 2, 4, 1)
    m "First things first, close your eyes."
    call luna_main("...", 2, 2, 4, 2) #eyes closed
    m "Very good. Now I want you to block everything else out."
    call luna_main("alright, sir...", 2, 2, 4, 3)
    m "Imagine it's just you alone in your room."
    call luna_main("yes...", 2, 2, 4, 2)
    m "Nice and cozy. Not a care in the world."
    call luna_main("...", 2, 2, 4, 1) #smile
    m "Now, focus on where the itch is strongest."
    call luna_main("Ah... alright...", 2, 2, 1, 1)
    m "I want you to chase that feeling with your fingers."
    call luna_main("...", 2, 2, 1, 2)
    m "Focus on catching it."
    call luna_main("I can't...", 2, 2, 4, 4)
    call luna_main("It's like trying to grab rays of sunlight...", 2, 2, 4, 2)
    m "Don't try and grab a hold of it, just brush against it with the tips of your fingers."
    call luna_main("...", 2, 2, 4, 1)
    call luna_main("...", 2, 2, 1, 1)
    ">Luna starts dancing her fingers along under her skirt."
    call luna_main("ah...", 2, 2, 4, 1)
    call luna_main("mmm...", 2, 2, 4, 5)
    ">Luna starts to softly moan under her breath."
    call luna_main("I'm close sir...", 2, 2, 4, 1)
    m "Good. Just keep your eyes closed and focus on your fingers."
    call luna_main("{image=textheart}", 2, 2, 1, 5)
    call luna_main("ah... I think it's working, sir!", 2, 2, 4, 1)
    call luna_main("I think I'm about to catch it!", 2, 2, 1, 1)
    m "Shhh, don't speak, just focus..."
    call luna_main("ok...", 2, 2, 4, 2)
    call luna_main("...", 2, 2, 4, 1)
    call luna_main("ah...", 2, 2, 4, 5)
    call luna_main("{image=textheart}", 2, 2, 4, 1)
    call luna_main("...", 2, 2, 4, 3)
    call luna_main("ah... sir...", 5, 1, 4, 2)
    call luna_main("I think...", 5, 3, 4, 5)
    call luna_main("ah...", 5, 2, 4, 5)
    call luna_main("I think I've almost got it...", 2, 2, 4, 5)
    m "Shhh..."
    call luna_main("ah...", 2, 1, 2, 5)
    ">Luna's fingers start furiously dancing underneath her skirt."
    call luna_main("mmmm...", 2, 1, 2, 1)
    call luna_main("ah...", 2, 1, 2, 5)
    call luna_main("a-ah...", 5, 3, 4, 1)
    call luna_main("yes...", 5, 8, 2, 1)
    m "(I think this is it!)"
    call luna_main("Ah... ah...{image=textheart}", 5, 2, 4, 5)
    call luna_main("{size=+4}mmm... yes...{image=textheart}{/size}", 5, 3, 4, 1)
    call luna_main("{size=+8}ah... ah...{/size}", 5, 8, 4, 5)
    call luna_main("!!!", 4, 9, 1, 5) #orgasm face
    ">THere's a blur of movement under Luna's skirt."
    call luna_main("ah! I think they're attacking me, sir!", 4, 8, 4, 1)
    call luna_main("!!!", 1, 9, 4, 1) #orgasm face
    m "Is everything OK?"
    call luna_main("Ah... yes sir...{image=textheart}", 5, 2, 4, 2)
    call luna_main("it's just...", 5, 2, 4, 1)
    m "..."
    call luna_main("I-I've never...", 5, 2, 4, 2)
    call luna_main("...", 5, 3, 4, 1)
    call luna_main("{size=-5}Ah...{/size}", 5, 2, 4, 1)
    m "Have the wickspots left you alone?"
    call luna_main("I think so, sir...", 5, 1, 4, 2)
    $ luna_l_arm = 1
    ">Luna slowly pulls her hand out from under her skirt."
    call luna_main("at least That nasty itch seems to have gone away.", 1, 1, 4, 1)
    m "Fantastic! will that be all then, miss lovegood."
    call luna_main("OH... did you want me to leave already, sir?", 5, 3, 4, 2)
    m "If there's nothing else I can help you with."
    call luna_main("I suppose not... but what if the feeling comes back, sir?", 5, 2, 4, 3)
    call luna_main("Should I try and get rid of them myself?", 5, 3, 4, 2)
    m "Certainly not!"
    call luna_main("Really? Why not?", 4, 1, 4, 2)
    m "as I said earlier miss lovegood, These techniques are to be kept secret."
    m "Not to mention dispelling them in your common room could lead to a school wide outbreak."
    call luna_main("So what can I do if they come back?", 1, 1, 4, 2)
    m "If you ever feel like you need to relieve yourself of those pesky little things again, my door is always open."
    call luna_main("Are you sure, sir?", 5, 1, 4, 2)
    call luna_main("I wouldn't want to bother you...", 5, 2, 4, 2)
    m "You'd be doing no such thing! besides, I've been meaning to test these sort of techniques for a while now."
    m "If anything you'll be helping me with important research."
    call luna_main("Really? thank you very much, sir.", 4, 1, 1, 1)
    call luna_main("Hopefully they leave me alone, but if not I'll come and visit you again.", 1, 2, 4, 1)
    m "I look forward to it."
    call luna_main("...", 5, 1, 4, 1)
    ">Luna gives you one last smile before leaving your office."
    jump luna_away


label luna_cum_addict_event:
    $ luna_addicted = True #luna is now a cum addict. I'm a bit undecided about the whole thing tbh, might ruin the dom path but idk, we can work it in, make her a dommy cumslut or whatever........
    ">You put your arms on Luna's shoulders forcing her to her knees."
    $ luna_l_arm = 2
    $ luna_r_arm = 2
    call gen_main("Down we go!", 4, 4)
    $ luna_ypos = 225
    $ luna_xpos = 350
    call luna_main("Stop right now! This wasn't an option [l_genie_name]!", 4, 1, 3, 15)
    g4 "Argh, too late slut!"
    call luna_main("!!!", 3, 1, 3, 3)
    $ luna_cum = 11
    show screen white 
    pause.1
    hide screen white
    pause.2
    show screen white 
    pause .1
    hide screen white
    with hpunch
    $ luna_wear_cum = True
    ">You coat Luna's furious expression in a wave of hot cum!"
    pause
    g4 "Argh! by the gods {size=+10}YES!{/size}"
    call luna_main("...", 5, 5, 1, 2)
    call luna_main("(What's this smell?)", 5, 7, 4, 4)
    g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
    g4 "mmmm....."
    hide screen g_c_c_u
    $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png"
    $ luna_r_arm = 2
    hide screen genie_sprite
    $ genie_sprite_base = "01_hp/13_characters/genie/base_2.png"
    with d3
    m "That hit the spot..."
    call luna_main("...", 8, 4, 3, 4)
    call luna_main("......", 7, 7, 2, 2)
    call luna_main(".........", 5, 6, 4, 1)
    m "Ahh... that was fantastic slut..."
    $ g_c_u_pic = "01_hp/08_animation_02/06_groping_01.png"
    call luna_main("What {size=+4}is {size=+4}this {size=+4}smell?{/size}", 4, 1, 4, 1)
    m "Cum?"
    ">Luna gets up from her knees"
    $ luna_ypos = 0
    call luna_main("{size=+4}it{/size}", 9, 4, 3, 3)
    call luna_main("{size=+8}smells{/size}", 8, 7, 2, 2)
    call luna_main("{size=+12}incredible!!!{/size}", 4, 6, 4, 1)
    m "..."
    m "What?"
    call luna_main("my god!!! there's so much magical energy in it!", 4, 8, 4, 1)
    call luna_main("I've never sensed anything this powerful before!", 4, 3, 4, 1)
    m "Ah yes, well I am the great fumblemore!"
    call luna_main("even so sir...", 7, 1, 2, 4)
    call luna_main("This smell... it's too much for a mortal to make...", 7, 1, 1, 1)
    m "(Shit...)"
    call luna_main("can I...", 1, 1, 4, 2)
    call luna_main("taste it?", 5, 2, 4, 2)
    m "What sort of question is that?"
    call luna_main("If it's too much...", 4, 1, 4, 2)
    g9 "Of course you can taste my cum girl!"
    call luna_main("thank you sir...", 4, 1, 4, 1)
    m "(She seems different...)"
    $ luna_cum = 12
    ">Luna collects a stand of cum on the end of her finger starting at it intently before putting it into her mouth."
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 5, 6, 4, 13)
    call luna_main("{size=+4}It's {size=+4}amazing!!!!!{image=textheart}{image=textheart}{/size}", 2, 8, 4, 1)
    call luna_main("can I have the rest? Please sir?", 4, 1, 4, 1)
    m "Sure..."
    ">You watch in awe as Luna slowly heaps your cum in her mouth and swallows it."
    $ luna_cum = 13
    call luna_main("...", 5, 6, 4, 13)
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 2, 8, 4, 1)
    pause
    $ luna_cum = 14
    call luna_main("...", 5, 6, 4, 13)
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 2, 8, 4, 1)
    $ luna_cum = 15
    call luna_main("...", 5, 6, 4, 13)
    call luna_main("{image=textheart}{image=textheart}{image=textheart}", 2, 8, 4, 1)
    $ luna_wear_cum = False
    call luna_main("ah...", 2, 8, 4, 1)
    call luna_main("amazing...", 5, 8, 4, 1)
    m "Enjoy yourself did we?"
    call luna_main("How could I not?", 7, 2, 2, 4)
    m "(What is going on here? SHe seems all bitchy again...)"
    call luna_main("You have to tell me how you did that!", 8, 1, 2, 2)
    m "Cum? I'm pretty sure you've got that all worked out..."
    call luna_main("Not that, idiot!", 9, 1, 3, 2)
    call luna_main("why did it contain so much magical energy?", 7, 1, 2, 2)
    call luna_main("we lovegoods are sensitive to magic, but The only thing I've ever experienced like this was when I was allowed in the same room as some essence of Djinn...", 7, 2, 3, 4)
    call luna_main("But everyone knows the Djinn were hunted to extinction millenia ago...", 8, 1, 2, 2)
    g4 "(!!!)"
    m "oh, um..."
    m "Trade secret..."
    call luna_main("Fine! Be that way then [l_genie_name]...", 6, 2, 2, 4)
    ">Luna gets dressed in front of you in a huff."
    $ luna_wear_skirt = True
    $ luna_wear_bra = True
    $ luna_wear_panties = True
    $ luna_wear_top = True
    call luna_main("Just don't expect me to let you get away with wasting that spunk anymore [l_genie_name]!", 8, 1, 2, 2)

    hide screen bld1
    m "well... anyway, Here's your payment [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
    ">Luna leaves your office."  

    hide screen g_c_u
    show screen genie
    hide screen chair_02
    hide screen desk_02

    jump luna_away





