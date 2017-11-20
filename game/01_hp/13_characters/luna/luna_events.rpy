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
                call luna_main("(Hmmmph* Don't expect that you'll be cumming anywhere near me though!", 6, 3, 4, 3) 
            "-Ask for a handjob politely-" if luna_sub < luna_dom:
                "asd  s"
            "-Beg for a handjob-" if luna_dom >= 7:
                "asd"

        if luna_choice <= 2: #Sub choices
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
            m "But I do expect you to improve."
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
                    g4 "{size=+10}TAKE IT ALL you slut!{/size}"
            m "mmmm....."
            call luna_main("[l_genie_name]!", 5, 3, 1, 1)
            call luna_main("How could you!", 5, 3, 1, 1)
            m "Ahh..."
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
            call her_main("{size=+15}FUCK!{/size}","body_122")
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
            m "I wasn't paying her in points"
            call her_main("Oh...","body_122")
            call her_main("Well I suppose that's alright then...","body_122")
            call her_main("But you should have at least told me this was going on!","body_122")
            m "Sorry."
            call her_main("It's alright, as long as you didn't jeopordise our chances of winning the ","body_122")













