###FAVOURS###------------------------------------------------------

label luna_favour_1: ###TALK TO ME
    m "{size=-4}(All I'll do is have a nice little conversation with her...){/size}"
    if luna_corruption == 0: #FIRST TIME
            $ luna_corruption += 1
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
            m "Ok then..."
            m "Tell me a little about yourself, [luna_name]."
            call luna_main("*hmph* I assume you'll be paying me for this [l_genie_name].", 7, 1, 2, 2)
            menu:
                "-5 gold-":
                    m "How does five gold sound [luna_name]?"
                    call luna_main("five gold! Who do you think I am!", 8, 1, 2, 4)
                    m "A student with no source of income."
                    call luna_main("I am luna lovegood! You should be paying a hundred gold just to look at me!", 9, 2, 3, 3)
                    m "How does ten gold sound then?"
                    call luna_main("Perhaps if you'd offered that to being with...", 7, 1, 2, 2)
                    call luna_main("But now I'm far too upset to hold a conversation for such a low amount.", 7, 2, 2, 4)
                    m "would twenty gold calm you down?"
                    call luna_main("well, I suppose it would.", 3, 3, 1, 1)
                    $ current_payout = 20
                    m "Good, well now that we've got that sorted out..."
                "-10 gold-":
                    m "Will ten gold be enough for a conversation with your headmaster?"
                    call luna_main("I suppose so...", 6, 1, 1, 2)
                    call luna_main("Just don't try anything funny.", 7, 2, 2, 3)
                    $ current_payout = 10
                    m "Scouts honor. Now..."
                "-50 gold-":
                    $ current_payout = 50
                    m "How does fifty gold sound [luna_name]?"
                    call luna_main("{size=+10}(FIFTY GOLD!){/size}", 4, 1, 1, 17)
                    call luna_main("*Hmph* I suppose that's a fair amount.", 2, 3, 1, 1)
                    call luna_main("Just don't think it buys you anything other than a conversation.", 7, 1, 2, 2)
                    m "Of course not. Speaking of which..."
            call luna_main("Fine, fine, I'll start...", 3, 3, 1, 2)
            call luna_main("My school life so far has been painfully dull.", 1, 1, 2, 3)
            call luna_main("I've been under appreciated by everyone in this damn place.", 1, 2, 2, 2)
            call luna_main("No one seems to take me seriously...", 7, 3, 2, 2)
            menu: 
                "-Jerk off while she is talking-": # offended and stops unless you paid her 50 or offer to pay her more
                    hide screen luna
                    hide screen blktone
                    with d3
                    ">You reach under the desk and grab your cock..."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    pause                    
                    call luna_main("what are you doing [l_genie_name]!?", 9, 1, 5, 3)
                    m "What, oh it's nothing. Simply adjusting my robe, that's all."
                    if current_payout < 50:
                        call luna_main("This is exactly what I mean!", 8, 1, 3, 3)
                        call luna_main("Even the headmaster of this damn school thinks he can get away with touching himself in front of me for only [current_payout] gold!", 8, 2, 3, 3)
                        show screen genie
                        with d3
                        "You quickly tuck your cock back into your robe."
                        m "i can assure you I was doing no such thing!"
                        call luna_main("whatever... I'm leaving", 8, 2, 3, 3)
                        m "What! Already?"
                        call luna_main("Would you rather I stay and call the ministry of magic [l_genie_name]?", 8, 1, 3, 3)
                        m "Fair enough."
                        call luna_main("I mean if you're going to try this on you could at least offer a little more than [current_payout] gold...", 9, 1, 2, 4)
                        jump luna_away
                    call luna_main("...", 6, 2, 1, 2)
                    call luna_main("{size=-5}(Well I suppose he did offer fifty gold...){/size}", 6, 2, 1, 1)
                    call luna_main("As I was saying, no one seems to even notice me.", 7, 1, 2, 2)
                    call luna_main("The teachers are too busy playing favourites with the \"gryffindor\" and \"slytherin\" students.", 7, 2, 2, 4)
                    call luna_main("The girls are all self obsessesed.", 7, 3, 2, 3)
                    m "You don't say."
                    call luna_main("and The boys are off chasing anything that shows a little skin...", 8, 2, 2, 3)
                    m "well, maybe you should fight fire with fire."
                    call luna_main("what!? and parade myself around like some tart?", 4, 2, 2, 6)
                    m "{size=-4}(Yes... a nasty, little tart!){/size}"
                    call luna_main("I bet you'd enjoy that wouldn't you [l_genie_name]...", 5, 1, 2, 1)
                    m "{size=-4}(Yes...){/size}"
                    call luna_main("another one of your precious students, dressing like a slut.", 5, 2, 1, 1)
                    m "{size=-2}(Yes......){/size}"
                    call luna_main("showing off her body for anyone that will look.", 6, 2, 2, 11)
                    m "{size=+2}(Yes.........){/size}"
                    call luna_main("You probably want me to act like those \"slytherin\" sluts too...", 6, 1, 2, 1)
                    m "{size=+4}(Yes! Yes!){/size}"
                    call luna_main("willing to show it all for a few points...", 6, 1, 2, 5)
                    g4 "{size=+4}(almost there...){/size}"
                    call luna_main("is that what you want [l_genie_name]? a nice little slytherin slut?", 6, 1, 2, 1)
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
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
                    g4 "Argh! YES!"
                    hide screen luna
                    with d3
                    hide screen bld1
                    with d3
                    show screen genie_jerking_sperm
                    with d3
                    show screen bld1
                    with d3
                    call luna_main("That's it, [l_genie_name], just let it all out...", 5, 1, 1, 1)
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "What? No, I was just... ah, shit, this feels good..."
                    show screen genie
                    hide screen bld1
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("You couldn't help yourself could you?", 5, 2, 5, 1)
                    m "ah... I guess not."
                    call luna_main("Well, I expect a bonus.", 2, 2, 5, 2)
                    m "I'm already paying you fifty gold!"
                    call luna_main("That was just for the conversation. If you expect me to stand here and watch you cum all over yourself, that costs extra.", 8, 2, 3, 3)
                    m "Fine, I'll make it 70 gold."
                    $ current_payout = 70
                    call luna_main("Well I'm glad someone appreciates me.", 5, 2, 5, 1)
                    call luna_main("(Even if it is a filthy old pervert...)", 3, 2, 5, 2)
                "-Participate in the conversation-":
                    m "I can't see why..."
                    call luna_main("Even my father doesn't treat me like he should.", 7, 2, 2, 2)
                    m "And how is that?"
                    call luna_main("Like the princess I am!", 5, 1, 1, 4)
                    m "(Not this again...)"
                    call luna_main("As it is he's barely selling any copies of his newspaper.", 8, 2, 3, 3)
                    call luna_main("It's ridiculous! I should be showered in gifts and gold...", 9, 2, 3, 2)
            call luna_main("Speaking of which...", 5, 1, 2, 2)    
            m "Alright, alright. Here's your gold."
            $ gold -= current_payout
            $ luna_gold += current_payout
            ">You hand Luna [current_payout] gold."
            call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)     
            ">Luna leaves your office."  



    elif luna_corruption == 1: #SECOND TIME 
        if luna_corruption <= 1:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "Alright then..."
        m "How's school going, [luna_name]."
        call luna_main("aren't we going to discuss how much you'll be paying me first, [l_genie_name].", 7, 1, 2, 2)
        menu:
            "-10 gold-": #just conversation (very short)
                $ current_payout = 10
                m "How does 10 gold sound?"
                call luna_main("*Hmph* Fine...", 3, 3, 1, 2)
                m "so about your school life..."
                call luna_main("School is boring. All I do is go to classes.", 1, 1, 2, 3)
                call luna_main("Can I leave now?", 1, 2, 2, 2)
                g9 "What? That was barely a sentence!"
                call luna_main("And ten gold is barely a payment!", 1, 2, 2, 2)
                m "I'd say it's a fair payment for a little bit of idle chit chat."
                call luna_main("That's what you got. If you want more, pay more...", 1, 1, 3, 2)
            "-20 gold-": #Slightly flirty, still short
                $ current_payout = 20
                m "Will twenty gold be enough for you, [luna_name]?"
                call luna_main("I suppose so...", 6, 1, 1, 2)
                call luna_main("Just don't expect to get to touch yourself...", 7, 2, 2, 3)
                m "How much would that cost?"
                call luna_main("...{p}More than twenty gold...", 7, 2, 2, 3)
                m "Well I might take you up on that at a later date, For now tell me about school."
                call luna_main("School is boring...", 1, 1, 2, 3)
                m "..."
                call luna_main("but there are a few interesting things happening... ", 5, 1, 5, 1)
                m "go on..."
                call luna_main("Well there are some rumours about Peeves the ghost...", 5, 2, 5, 1)
                m "What sort?"
                call luna_main("Well I've heard that he's been touching some of the girls...", 5, 1, 4, 2)
                m "How haven't I heard a complaint?"
                call luna_main("Well from what I hear... the girls don't have any complaints afterwards...", 5, 1, 5, 1)
                m "Ah... Anything else?"
                call luna_main("Hmmm... nothing comes to mind.", 6, 3, 2, 2)
                m "fair enough, well I think that was worth your twenty gold."
            "-100 gold-": #JOI
                $ current_payout = 100
                m "How about one hundred gold?"
                call luna_main("Fine...", 5, 2, 2, 2)
                call luna_main("...", 6, 1, 2, 2)
                call luna_main("......", 6, 1, 5, 3)
                call luna_main("Well are you going to start?", 8, 2, 3, 3)
                m "Start what? You're the one who's supposed to be talking."
                call luna_main("Oh please... You expect me to believe you're willing to pay your students 100 gold just to talk?", 7, 1, 5, 3)
                m "Well I suppose that-"
                call luna_main("Just start stroking your cock already [l_genie_name].", 5, 1, 1, 2)
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause  
                call luna_main("Isn't that better?", 5, 1, 5, 1)
                m "..."
                call luna_main("So do you pay anyone else to watch you sit there and jerk your filthy old cock?", 5, 1, 2, 3)
                m "{size=-4}(I guess I don't really pay hermione...){/size}"
                m "ah... no..."
                call luna_main("good...", 5, 2, 1, 1)
                m "Good?"
                call luna_main("Well... we can't have you wasting your money on any of those other little tarts can we?", 8, 1, 3, 3)
                menu:
                    "-Play along-": #act submissive
                        $ luna_dom += 1
                        $ current_payout = 150
                        m "ah... of course not..."
                        call luna_main("That's right... why bother with them when I'm here to talk with you...", 8, 1, 3, 1)
                        m "{size=-4}(Yes...){/size}"
                        call luna_main("That's it, keep stroking it for me [l_genie_name].", 6, 1, 2, 2)
                        m "{size=-4}(Yes... yes...){/size}"
                        call luna_main("It's probably I good thing that I watch you drain your balls.", 6, 2, 2, 2)
                        call luna_main("Otherwise, who knows who you might call up here to watch you do it...", 7, 1, 2, 4)
                        m "{size=-4}(mmmm... yes...){/size}"
                        call luna_main("You'd probably even do it in front of a first year, wouldn't you?", 9, 1, 2, 1)
                        ">You stop stroking your cock."
                        m "I'd never do any-"
                        call luna_main("Do you even know how old I am?", 9, 1, 5, 1)
                        m "of course..."
                        call luna_main("*Hmph* Are you sure about that?", 9, 1, 5, 14)
                        m "..."
                        call luna_main("Back to stroking it [l_genie_name]...", 9, 1, 3, 1)
                        ">You start stroking your cock again."
                        call luna_main("Doesn't that feel better?", 9, 2, 3, 1)
                        m "{size=-4}(argh... yes...){/size}"
                        call luna_main("Say it outloud.", 8, 1, 3, 1)
                        m "{size=-4}yes...{/size}"
                        call luna_main("Good. Now cum for me.", 9, 1, 2, 1)
                        m "{size=-2}(What?){/size}"
                        call luna_main("come on...", 9, 1, 4, 1)
                        g4 "{size=+4}(agh... almost there...){/size}"
                        call luna_main("come for your little girl...", 9, 1, 3, 14)
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
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
                        g4 "Argh! YES!"
                        hide screen luna
                        with d3
                        hide screen bld1
                        with d3
                        show screen genie_jerking_sperm
                        with d3
                        show screen bld1
                        with d3
                        call luna_main("That's it, [l_genie_name] just like that...", 5, 1, 1, 1)
                        show screen genie_jerking_sperm_02
                        with d3
                        g4 "What? No, I was thinking about... ah, shit, this feels too good..."
                        show screen genie
                        hide screen bld1
                        #show screen genie_jerking_off
                        with d3
                        call luna_main("Your a nasty old man, aren't you.", 5, 2, 5, 1)
                        m "ah..."
                        call luna_main("Don't worry, I won't tell anyone...", 5, 1, 5, 1)
                        m "Thank you..."
                        call luna_main("I expect to be fairly compensated however...", 7, 2, 2, 1)
                        m "Don't worry, I'll add an extra 50 gold to your payment."
                        call luna_main("That's the least you could do [l_genie_name]...", 9, 2, 5, 1)



                    "-Let her know her place-": #note that he could get more for less from those tarts
                        $ luna_sub += 1
                        m "well now that you mention it I'm sure those tarts would probably charge a lot less for a conversation..."
                        call luna_main("*Hmph* You get what you pay for...", 7, 2, 3, 3)
                        m "And what exactly am I getting from you for my payment?"
                        call luna_main("Getting to Look at me while you stroke your filthy old cock should be payment enough.", 7, 1, 3, 2)
                        m "Well you'll have to excuse my old eyes because I can barely see you..."
                        menu: 
                            "-Ask her to open her top-":
                                $ luna_sub += 1
                                m "Perhaps you should undo a button or two so I can get a better look."
                                call luna_main("Are you serious? You expect me to flaunt myself like some cheap tart?", 8, 1, 2, 2)
                                m "No, I expect you to flaunt yourself like the princess you claim to be..."
                                call luna_main("...", 7, 2, 2, 2)
                                m "I'm waiting..."
                                call luna_main("... {size=-8}(fine...){/size}", 6, 3, 4, 3)
                                ">Luna removes her tie and opens her top slightly..."
                                hide screen luna 
                                with d3
                                $ luna_top_level = 2
                                call luna_main("...", 6, 3, 4, 2)
                                m "Why don't you keep you're shirt like that from now on..."
                                call luna_main("...", 6, 2, 4, 3)
                            "-Ask her to come closer-":
                                m "Perhaps you should come stand a little closer."
                                call luna_main("Really? You want me to come closer while you...?", 6, 1, 3, 2)
                                m "Well I am so \"old\"..."
                                call luna_main("...", 7, 2, 2, 2)
                                m "I'm waiting..."
                                call luna_main("... {size=-8}(fine...){/size}", 6, 3, 4, 3)
                                hide screen luna_chibi
                                with d3
                                ">Luna walks towards you, standing in front of the table..."
                                $ luna_chibi_xpos = 450
                                show screen luna_chibi 
                                with d3 
                                m "Very good... Maybe you should stand this close from now on..."
                                call luna_main("...", 6, 2, 4, 3)


                        call luna_main("Is this what you want?", 6, 3, 4, 3)
                        call luna_main("To humiliate me...", 6, 1, 3, 3)
                        m "{size=-4}(mmmm... yes...){/size}"
                        call luna_main("You love this, don't you...", 7, 1, 2, 2)
                        ">You start stroking faster."
                        call luna_main("What I'm forced to do...", 7, 3, 3, 2)
                        call luna_main("Just to survive...", 6, 3, 4, 3)
                        m "..."
                        call luna_main("Well don't worry about that...", 8, 1, 3, 2)
                        call luna_main("Just keep stroking it.", 8, 2, 3, 1)
                        m "{size=-4}(argh... yes...){/size}"
                        call luna_main("You nasty old man", 8, 1, 3, 1)
                        m "{size=-4}yes...{/size}"
                        call luna_main("Get your moneys worth...", 9, 1, 3, 3)
                        m "{size=-2}(mmmm...){/size}"
                        call luna_main("come on...", 9, 1, 2, 1)
                        g4 "{size=+4}(agh... almost there...){/size}"
                        call luna_main("come for your poor student...", 9, 1, 4, 1)
                        g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
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
                        g4 "Argh! YES!"
                        hide screen luna
                        with d3
                        hide screen bld1
                        with d3
                        show screen genie_jerking_sperm
                        with d3
                        show screen bld1
                        with d3
                        call luna_main("That's it, just let it out...", 8, 1, 3, 3)
                        show screen genie_jerking_sperm_02
                        with d3
                        g4 "good work, slut... ah, shit, this feels so good..."
                        show screen genie
                        hide screen bld1
                        #show screen genie_jerking_off
                        with d3
                        call luna_main("Your a nasty old man, aren't you.", 9, 1, 5, 1)
                        m "ah..."
                        call luna_main("Forcing me to watch you do this...", 9, 2, 3, 1)
                        m "Ah... I'm not forcing you to do anything..."
                        call luna_main("Hmph well I expect to be paid now...", 8, 1, 2, 2)
                        m "Don't worry, I'll give you your hundred gold."
                        call luna_main("*Hmph* Fine...{p}(Nothing extra...?)", 8, 2, 2, 3)


        call luna_main("Speaking of which...", 5, 1, 2, 2)    
        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)     
        ">Luna leaves your office."  

    elif luna_corruption >= 2: #THIRD TIME 
        if luna_corruption <= 2:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "Tell me [luna_name]..."
        m "How's you're home life going?"
        call luna_main("My home life?", 7, 2, 5, 2)
        call luna_main("In one word, [l_genie_name], inadequate.", 7, 1, 2, 4)
        m "inadequate?"
        call luna_main("Yes! Someone such as myself should be showered with gifts and gold.", 8, 2, 2, 4)
        call luna_main("Instead I live in a chess piece while my stupid, worthless father struggles to sell 10 copies of his dumb paper!", 8, 3, 3, 3)
        m "Surely he sells more than 10 copies?"
        call luna_main("Barely...", 7, 2, 2, 2)
        call luna_main("He's struggling to get any institutions to stock it these days... ever since the ministry stopped buying it.", 6, 2, 2, 2)
        menu:
            "-Say nothing-": #act submissive
                if luna_dom <= 1:
                    $ luna_dom += 1
                $ current_payout = 150
                call luna_main("Wait... that's it!", 5, 1, 2, 1)
                m "what's it?"
                call luna_main("Why don't you start buying the quibbler [l_genie_name]?.", 5, 1, 1, 1)
                m "I hardly think one more person is going to turn things around."
                call luna_main("Not you personally [l_genie_name], hogwarts!", 8, 1, 2, 2)
                call luna_main("Just imagine how many copies the entire school would buy!", 1, 2, 2, 11)
                m "Hmmm, I'll think about it..."
                call luna_main("You'll {size=+4}think{/size} about it?", 9, 1, 3, 3)
                call luna_main("*Hmph* Maybe I'll just have to {size=+4}think{/size} about getting my father to write a story...", 9, 2, 3, 3)
                call luna_main("involving a perverted old headmaster who likes to lure young girls into his office...", 9, 2, 5, 3)
                call luna_main("Just to leer at them while he strokes his filthy old cock...", 9, 1, 2, 3)
                m "..."
                call luna_main("I'm sure that would sell some extra copies...", 8, 2, 5, 3)
                call luna_main("Well?", 9, 1, 3, 2)
                m "Fine, fine. I'll get someone to start ordering some extra copies for the library."
                call luna_main("There, isn't that easy?", 5, 2, 2, 1)
                m "yes..."
                call luna_main("Good. Now as a reward, I'll let you touch that filthy old cock of yours.", 7, 1, 2, 1)
                m "..."
                call luna_main("come on [l_genie_name]...", 9, 1, 4, 1)
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause  
                call luna_main("That's better isn't it?", 9, 1, 2, 1)
                call luna_main("Just listen to my voice while you stroke yourself...", 9, 2, 2, 1)
                m "..."
                call luna_main("Just think about how happy I'll be once father becomes a respectable member of society.", 8, 1, 3, 1)
                call luna_main("Think about how much you enjoy making me happy...", 8, 2, 3, 1)
                m "{size=-4}(argh... yes...){/size}"
                call luna_main("You love making me happy don't you [l_genie_name]...", 8, 1, 3, 1)
                m "{size=-4}yes...{/size}"
                call luna_main("say it louder...", 8, 1, 3, 1)
                m "yes..."
                call luna_main("It makes you feel so good doesn't it...", 9, 1, 3, 1)
                m "{size=-2}(mmmm...){/size}"
                m "{size=+2}yes...{/size}"
                call luna_main("maybe i'll even make you kiss my feet... that would make me very happy", 9, 1, 2, 1)
                g4 "{size=+4}(agh...){/size}"
                g4 "{size=+4}yes...{/size}"
                call luna_main("that's it [l_genie_name], cum for your princess...", 9, 1, 4, 1)
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("cum...", 9, 1, 3, 14)
                call luna_main("{size=+4}cum!{/size}", 9, 1, 3, 14)
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
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
                g4 "Argh! YES!"
                hide screen luna
                with d3
                hide screen bld1
                with d3
                show screen genie_jerking_sperm
                with d3
                show screen bld1
                with d3
                call luna_main("That's it, [l_genie_name] just like that...", 8, 1, 2, 2)
                show screen genie_jerking_sperm_02
                with d3
                g4 "ah, shit, why does this feels so good..."
                show screen genie
                hide screen bld1
                #show screen genie_jerking_off
                with d3
                call luna_main("Disgusting...", 5, 2, 1, 6)
                m "ah..."
                call luna_main("...", 8, 1, 2, 2)
                m "Thank you..."
                call luna_main("Thank you...?", 9, 1, 3, 3)
                m "Thank you princess..."
                if luna_name == "Miss Lovegood":
                    $ luna_name = "Princess"
                call luna_main("That's better [l_genie_name]...", 7, 1, 2, 1)
                call luna_main("Now as a princess I expect a present for having to look at such a filthy act...", 7, 2, 2, 1)

            "-Make an offer-": #exchange quibbler purchase
                if luna_sub <= 1:
                    $ luna_sub += 1
                $ current_payout = 50
                m "well I'm sure that I could have a few words with the library staff about stocking it..."
                call luna_main("Really? You'd do that?", 4, 1, 1, 1)
                m "Of course."
                if l_genie_name == "Old man":
                    $ l_genie_name = "Professor"
                call luna_main("Thank you so much [l_genie_name]!", 2, 1, 1, 1)
                m "I was thinking you could thank me for my generous offer another way..."
                call luna_main("Oh...{p}", 7, 2, 3, 3)
                m "That's not a problem is it [luna_name]?"
                call luna_main("Of course not... What did you have in mind?", 6, 3, 4, 2)
                m "well for starters..."
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause  
                menu: 
                    "-Ask her to shorten her skirt-":
                        if luna_sub <= 2:
                            $ luna_sub += 1
                        m "lets talk about that skirt of yours..."
                        call luna_main("What about it?", 8, 1, 2, 2)
                        m "have you ever considered wearing it a little... shorter?"
                        call luna_main("...", 7, 2, 2, 2)
                        m "I'm waiting..."
                        call luna_main("...how short?", 6, 3, 4, 3)
                        m "Just an inch or so higher."
                        call luna_main("...", 6, 3, 4, 3)
                        call luna_main("(my father better appreciate this...)", 6, 3, 4, 3)
                        ">Luna pulls up her skirt slightly and then folds it over at the top..."
                        hide screen luna 
                        with d3
                        $ luna_skirt_level = 2
                        call luna_main("...", 6, 3, 4, 3)
                        m "{size=-4}(mmmm... yes...){/size}"
                        m "Why don't you wear it like that from now on..."
                        call luna_main("yes, [l_genie_name].", 6, 2, 4, 3)

                    "-Make her call you sir-":
                        $ l_genie_name = "Sir"
                        m "How about you start giving me the respect I deserve."
                        call luna_main("...", 6, 1, 3, 2)
                        m "I want you to refer to me as sir from now on."
                        call luna_main("...", 7, 2, 2, 2)
                        m "Is that clear?"
                        call luna_main("...Yes...{size=-8}sir{/size}", 6, 3, 4, 3)
                        m "Speak up [luna_name]..."
                        call luna_main("Yes sir...", 6, 2, 4, 3)
                        m "{size=-4}(yes...){/size}"


                call luna_main("You know this is wrong don't you?", 6, 3, 4, 3)
                call luna_main("What you're forcing me to do...", 6, 1, 3, 3)
                m "{size=-4}(mmmm... yes...){/size}"
                m "I don't recall forcing you into anything [luna_name]..."
                call luna_main("*hmph*...", 7, 1, 2, 2)
                ">You start stroking faster."
                call luna_main("well...", 7, 3, 3, 2)
                call luna_main("just get it over with...", 6, 3, 4, 3)
                m "{size=-4}ah...{/size}"
                call luna_main("Just keep touching yourself in front of me...", 8, 1, 3, 2)
                m "{size=-4}(argh... yes...){/size}"
                call luna_main("let it all out front of me...", 8, 1, 3, 5)
                m "{size=-4}yes...{/size}"
                call luna_main("Your student...", 9, 1, 3, 3)
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", 9, 1, 2, 1)
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little princess...", 9, 1, 4, 1)
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
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
                g4 "Argh! YES!"
                hide screen luna
                with d3
                hide screen bld1
                with d3
                show screen genie_jerking_sperm
                with d3
                show screen bld1
                with d3
                call luna_main("ugh... there's so much...", 8, 1, 3, 3)
                show screen genie_jerking_sperm_02
                with d3
                g4 "good work, slut... ah, shit, this feels so good..."
                show screen genie
                hide screen bld1
                #show screen genie_jerking_off
                with d3
                call luna_main("The floor...", 7, 3, 2, 2)
                call luna_main("it's covered...", 7, 2, 2, 2)
                m "Ah... you did good [luna_name]..."
                call luna_main("Hmph well I expect to be paid now...", 8, 1, 2, 2)


        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 2) 
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", 8, 2, 2, 3) 
        ">Luna leaves your office."  
    hide screen genie_jerking_sperm_02     
    jump luna_away










label luna_favour_2: ###SIT ON MY LAP
    m "{size=-4}(I'll just ask her to sit on my lap...){/size}"
    if luna_corruption <= 4: #FIRST TIME 
        if luna_corruption <= 3:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "Before we get started, Would you like a seat [luna_name]?"
        call luna_main("I would, but there's no chair [l_genie_name]...", 7, 1, 5, 2) 
        m "Well how about you come sit on my lap then?"
        call luna_main("...", 9, 1, 2, 3)
        m "Come on, it'll be just like santa claus."
        call luna_main("...", 9, 2, 2, 3)
        call luna_main("You better make this worth it [l_genie_name]...", 8, 2, 2, 3) 
        m "Don't worry, I'm sure you'll be very happy with your \'reward\'."
        call luna_main("...", 6, 1, 2, 3)
        show screen blkfade
        with d3 
        ">Luna walks around the desk and stands in front of you."
        #chibi stuff
        $ luna_flip = -1
        $ luna_xpos = 120
        $ luna_chibi_xpos = 300
        hide screen blkfade
        with d3 
        menu:
            "-Pull her onto your lap-" if luna_sub >= 2:
                if luna_sub <= 3:
                    $ luna_sub += 1
                $ luna_grope = True
                call luna_main("...", 6, 2, 2, 3) 
                call luna_main("Actually, I'm not sure if...", 8, 2, 1, 2) 
                ">You grab Luna around the waist and pull her onto your lap."
                call luna_main("Professor! What are you doing?", 4, 2, 5, 3) 
                m "just giving you a helping hand..."
                ">you start slowly rubbing your crouch against her soft ass."
                m "mmm that's it..."
                call luna_main("...", 6, 3, 4, 2) 
                call luna_main("(this is so humiliating...)", 6, 3, 4, 3) 

                jump luna_lap_dance

            "-Tell her to sit down-":
                $ luna_grope = False
                m "go on [luna_name]..."
                call luna_main("...", 8, 2, 2, 3) 
                call luna_main("Do I really have to do this?", 8, 2, 2, 3) 
                m "just Sit down [luna_name]..."
                call luna_main("...", 8, 2, 2, 3) 
                ">Luna softly takes a seat on your lap ."
                m "mmmmm..."
                call luna_main("...", 6, 2, 4, 2) 
                call luna_main("(ugh, he's so hard...)", 6, 3, 4, 6) 

                label luna_lap_dance:
                    m "That's it, now just start moving your waist."
                ">Luna gradually starts grinding her ass against you."
                m "ughh, that's it."
                call luna_main("...", 8, 3, 2, 3) 
                call luna_main("are you happy now?", 8, 2, 3, 3) 
                m "Very..."
                call luna_main("Can I leave yet?", 8, 1, 2, 3) 
                m "What? We just started!"
                call luna_main("Well I don't have all day.", 8, 2, 2, 3)
                m "Hmmm, well I'll see what I can do to speed this up..." 
                menu:
                    "-Grab her waist-":
                        ">You take a hold of her waist."
                        call luna_main("!!!", 4, 1, 1, 6)
                        call luna_main("I don't think touching was part of the arrangement [l_genie_name]...", 7, 2, 3, 7)
                        $ current_payout = 75
                        m "Don't worry [luna_name], you'll be compensated fairly."
                        ">You pull her hard against your crouch, rubbing your cock between her cheeks."
                        call luna_main("...", 6, 3, 4, 5)
                        m "That's it [luna_name], not much longer now."
                        call luna_main(".......", 8, 2, 2, 3)
                        m "mmmm, almost there..."
                        call luna_main("What?!!!", 4, 2, 3, 3)
                        show screen blkfade
                        with d3 
                        "Luna quickly pulls away from you and stands up."
                        #chibi stuff
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3 
                        call luna_main("Professor!", 9, 1, 3, 14)
                        m "What on earth did you stop for?"
                        call luna_main("Sitting on your lap is one thing.", 8, 2, 2, 3)
                        call luna_main("But letting you do that...", 9, 1, 3, 2)
                        call luna_main("I simply refuse!", 8, 2, 3, 6)
                        m "fine fine."
                        call luna_main("Honestly [l_genie_name], who do you think I am?", 7, 1, 2, 2)
                        call luna_main("I think I'd like to be paid now...", 7, 2, 2, 2)
                    "-Grope her-" if luna_grope:
                        ">You start running your hands along the outside of her thighs, up to her waist and then over her belly."
                        call luna_main("!!!", 4, 1, 1, 6)
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        m "yes, just like that [luna_name]."
                        $ current_payout = 40
                        call luna_main("......", 6, 3, 4, 6)
                        m "gods you've got such a nice ass."
                        ">You Start moving your hands slowly up towards her breasts"
                        call luna_main(".........", 6, 2, 4, 3)
                        m "That's it [luna_name], just enjoy it."
                        call luna_main("..................", 6, 2, 4, 2)
                        ">your hands are about an inch below her breasts..."
                        m "mmmm, almost there..."
                        call luna_main("..........................", 4, 2, 4, 2)
                        ">Your about to reach her ample tits......"
                        call luna_main("!!!!", 4, 1, 3, 6)
                        show screen blkfade
                        with d3 
                        "Luna quickly pulls away from you and stands up."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3 
                        call luna_main("Professor!", 4, 1, 3, 7)
                        m "What on earth did you stop for?"
                        call luna_main("Sitting on your lap is one thing?", 9, 1, 2, 3)
                        call luna_main("But letting you touch me there...", 8, 2, 3, 2)
                        call luna_main("I won't do it!", 8, 2, 2, 3)
                        m "alright fine."
                        call luna_main("Honestly [l_genie_name], you really need to learn some self control.", 8, 1, 3, 9)
                        call luna_main("I think I'd like to be paid now...", 8, 2, 2, 3)



            "-Do nothing-" if luna_dom < 2:
                call luna_main("...", 7, 2, 2, 2)
                call luna_main("......", 8, 2, 2, 3)
                call luna_main("I guess I'll start then...", 6, 2, 2, 2)
                ">Luna lightly sits on your lap."
                m "mmmm"
                call luna_main("...", 7, 1, 2, 2)
                call luna_main("......", 8, 2, 2, 3)
                call luna_main(".........", 8, 2, 3, 3)
                call luna_main("Alright, time's up!", 1, 2, 1, 2)
                ">Luna stands up from your lap"
                m "What, you barely even sat down!"
                call luna_main("*hmph* You should consider yourself lucky you got what you did [l_genie_name]!", 8, 2, 2, 3)
                m "You could have at least moved around a little."
                call luna_main("What? Who do you think I am? Some sort of harlot who'll let you grind yourself against them for as long as you want?", 9, 2, 2, 6)
                m "well I expected at least a few minutes."
                call luna_main("Well if your that desperate...", 5, 2, 1, 1)
                ">Luna slams her ass into your crouch"
                m "ah..."
                call luna_main("pathetic...", 5, 2, 2, 3)
                ">She starts rocking back and forward on your lap"
                call luna_main("You really are disgusting [l_genie_name]...", 5, 2, 1, 14)
                m "mmmm"
                call luna_main("begging your students for a lap dance...", 8, 2, 3, 3)
                m "yes, yes..."
                call luna_main("well you better pay extra for this...", 7, 2, 1, 2)
                m "of course..."
                call luna_main("...", 5, 3, 1, 2)
                ">luna starts rolling her hips a little faster."
                call luna_main("a lot extra...", 9, 2, 3, 3)
                m "of course [luna_name]..."
                call luna_main("that's it [l_genie_name]. just enjoy it...", 5, 2, 1, 1)
                m "mmm, just a little more..."
                call luna_main("...", 8, 3, 5, 3)
                m "yes... almost..."
                call luna_main("Times up!", 5, 2, 2, 1)
                show screen blkfade
                with d3 
                ">Luna quickly stands up."
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3 
                m "What!"
                call luna_main("Times{p}up...", 8, 1, 2, 2)
                m "Ugh, fine."
                call luna_main("Glad you understand,{p} now about my payment...", 8, 2, 2, 3)
                $ current_payout = 120


            "-Do nothing-" if luna_dom >= 2:
                if luna_dom <= 3:
                    $ luna_dom += 1
                call luna_main("...", 7, 1, 2, 2)
                call luna_main("......", 8, 2, 2, 3)
                call luna_main("I guess I'll start then...", 6, 2, 2, 2)
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("You're pathetic...", 5, 2, 2, 3)
                call luna_main("THe worlds greatest wizard...", 5, 2, 1, 1)
                call luna_main("More like the worlds greatest pervert.", 9, 2, 2, 3)
                if l_genie_name == "Old man":
                    $ l_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", 5, 2, 1, 14)
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", 8, 2, 2, 3)
                m "I don't recall begging."
                call luna_main("Hmmm...", 7, 2, 1, 2)
                ">Luna stands up slowly."
                call luna_main("Well then...", 8, 2, 2, 3)
                m "what?"
                call luna_main("beg...", 5, 2, 3, 3)
                menu:
                    "-Beg-":
                        pass
                    "-Refuse-":
                        m "I don't think so [luna_name]."
                        call luna_main("*hmph* Fine...", 9, 2, 2, 4)
                        show screen blkfade
                        with d3
                        ">Luna walks around to the front of the desk."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3 
                        call luna_main("I'd like to be paid now [l_genie_name]...", 8, 1, 3, 3)
                        $ current_payout = 100
                        m "Alright, alright. Here's your gold."
                        $ gold -= current_payout
                        $ luna_gold += current_payout
                        ">You hand Luna [current_payout] gold."
                        call luna_main("Thank you, [l_genie_name].", 7, 2, 2, 2)     
                        ">Luna leaves your office."
                m "Please..."
                call luna_main("Please what?", 5, 2, 1, 2)
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", 7, 2, 2, 1)
                ">She starts rocking back and forward on your lap"
                call luna_main("You're so hard...", 5, 3, 1, 2)
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", 5, 2, 5, 2)
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", 7, 2, 2, 2)
                m "of course..."
                call luna_main("...", 8, 2, 2, 3)
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", 5, 2, 3, 3)
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", 2, 2, 1, 1)
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", 5, 2, 2, 2)
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", 9, 1, 2, 1)
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", 9, 1, 4, 1)
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You start shooting your load against the inside of your cloak."
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
                g4 "Argh! YES!"
                call luna_main("ugh... pathetic...", 5, 2, 3, 1)
                call luna_main("...", 8, 2, 2, 3)
                call luna_main("......", 8, 3, 5, 2)
                call luna_main(".........", 8, 3, 3, 3)
                call luna_main("Alright, time's up!", 5, 2, 2, 1)
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3 
                call luna_main("*hmph* You [l_genie_name]!", 9, 1, 2, 2)
                m "You can hardly blame me for this."
                call luna_main("What? You're the one who begged for it, of course it's your fault.", 7, 2, 3, 3)
                m "well you didn't have to be so good at it."
                call luna_main("I was just making sure that I earned my reward.", 8, 1, 2, 3)
                call luna_main("Speaking of which...", 5, 2, 1, 1)
                $ current_payout = 200


  
        m "Alright, alright. Here's your gold."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", 8, 2, 2, 3) 
            call luna_main("Thank you, [l_genie_name].", 6, 2, 2, 2)   
        else:
            call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
        ">Luna leaves your office."  


    jump luna_away



label luna_favour_3: 
    jump luna_away
label luna_favour_4:
    jump luna_away
label luna_favour_5:
    jump luna_away
label luna_favour_6:
    jump luna_away
label luna_favour_7:
    jump luna_away
label luna_favour_8:
    jump luna_away
label luna_favour_9:
    jump luna_away
label luna_favour_10:
    jump luna_away
label luna_favour_11:
    jump luna_away
label luna_favour_12:
    jump luna_away
label luna_favour_13:
    jump luna_away