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
    if luna_corruption <= 3: #FIRST TIME 
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
                        call luna_main("Sitting on your lap is one thing!", 9, 1, 2, 3)
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

    elif luna_corruption <= 4: #SECOND TIME 
        if luna_corruption <= 4:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "Can I offer you another seat [luna_name]?"
        if luna_sub > luna_dom:
            call luna_main("...", 1, 3, 4, 2) 
            call luna_main("Alright [l_genie_name]...", 1, 2, 4, 2) 
            m "Good girl."
            call luna_main("...", 1, 3, 4, 3) 
        else:
            call luna_main("Fine...", 1, 2, 2, 2) 
            call luna_main("But I expect to be fairly compensated [l_genie_name]...", 7, 1, 2, 2)
            m "yes, yes..."
            call luna_main("...", 7, 2, 2, 2) 
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
            "-Ask her to remove her skirt first-" if luna_sub >= 2:
                if luna_sub <= 3:
                    $ luna_sub += 1
                $ luna_grope = True
                m "How about you take off your skirt before we start?"
                call luna_main("!!!", 4, 2, 4, 2) 
                call luna_main("You're not serious are you?", 6, 2, 4, 2)
                m "I am [luna_name], or do you not want hogwarts to keep purchasing new copies of the quibbler?" 
                call luna_main("...", 6, 3, 4, 2)
                call luna_main("......", 6, 2, 4, 2)
                m "I'm waiting."
                call luna_main("Fine...", 6, 3, 4, 6)
                hide screen luna 
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly removes her skirt, revealing her black silk panties."
                show screen luna
                hide screen blkfade
                with d3
                m "I like your panties..."
                call luna_main("...", 6, 3, 4, 2) 
                call luna_main("(this is so degrading)", 6, 3, 4, 6) 
                m "Now take a seat..."
                call luna_main("yes [l_genie_name]...", 6, 2, 4, 2) 
                ">Luna softly takes a seat on your lap."
                call luna_main("...", 6, 3, 4, 3) 
                jump luna_lap_dance_2

            "-Tell her to sit down-" if luna_sub >= luna_dom:
                $ luna_grope = False
                m "come on now..."
                call luna_main("...", 8, 2, 4, 3) 
                call luna_main("......", 8, 2, 4, 3) 
                m "Sit down [luna_name]."
                call luna_main("...", 8, 2, 4, 3) 
                ">Luna softly takes a seat on your lap ."
                m "mmmmm..."
                call luna_main("...", 6, 2, 4, 2) 
                call luna_main("(ugh, he's so hard...)", 6, 3, 4, 6) 

                label luna_lap_dance_2:
                    m "That's it, now just start moving your ass."
                ">Luna gradually starts grinding her waist against you."
                m "ughh, that's it."
                call luna_main("...", 8, 3, 4, 3) 
                call luna_main("is this alright?", 5, 2, 4, 2) 
                m "yes, just keep going..."
                call luna_main("For how long?", 8, 1, 4, 3) 
                m "As long as it takes [luna_name]."
                call luna_main("fine...", 8, 2, 4, 3)
                call luna_main("...", 8, 3, 4, 3)
                call luna_main("..........", 9, 3, 4, 3)
                call luna_main("Is there anything I can do to speed this up?", 6, 2, 4, 2) 
                menu:
                    "-enjoy yourself-":
                        $ current_payout = 65
                        m "Just keep doing what you're doing..."
                        call luna_main("...", 6, 3, 4, 6)
                        call luna_main("How about this?", 5, 2, 4, 2)
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "Mmmm, yes!"
                        ">You start thrusting into her ever so slightly."
                        call luna_main("...", 6, 3, 4, 5)
                        m "That's it [luna_name], not much longer now."
                        call luna_main(".......", 5, 2, 4, 2)
                        m "mmmm, almost there..."
                        call luna_main("Already?", 4, 2, 4, 3)
                        m "Almost... this is really good..."
                        call luna_main("it is?", 5, 2, 4, 1)
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call luna_main("...", 5, 2, 4, 1)
                        call luna_main("How's this?", 5, 3, 4, 5)
                        ">She starts rocking back and forward on your lap"
                        m "mmmmm"
                        call luna_main("You're so hard [l_genie_name]...", 5, 3, 4, 1)
                        m "mmmm"
                        call luna_main("are you almost there?", 5, 2, 4, 2)
                        m "yes..."
                        call luna_main("well I expect to be-", 5, 2, 2, 3)
                        m "shhh, don't ruin it."
                        call luna_main("...", 8, 2, 4, 3)
                        ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                        m "ah..."
                        call luna_main("...", 5, 2, 4, 3)
                        m "keep going [luna_name]..."
                        call luna_main("........", 3, 2, 4, 1)
                        m "mmm, just a little more..."
                        call luna_main("...[l_genie_name]...", 7, 3, 4, 2)
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}(mmmm...){/size}"
                        call luna_main("......", 6, 1, 4, 1)
                        g4 "{size=+4}(agh... almost there...){/size}"
                        $ luna_tears = 1
                        call luna_main("............", 9, 1, 4, 1)
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
                        $ luna_tears = 0
                        call luna_main("ugh...", 5, 2, 4, 1)
                        call luna_main("...", 8, 2, 4, 3)
                        call luna_main("......", 8, 3, 4, 2)
                        call luna_main(".........", 5, 3, 4, 3)
                        call luna_main("Are you finished now [l_genie_name]?", 5, 2, 4, 1)
                        m "Almost... just stay there for a little longer..."
                        call luna_main("......", 5, 2, 4, 1)
                        ">Luna waits for a few seconds before standing up."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        $ luna_wear_skirt = True
                        hide screen blkfade
                        with d3 
                        call luna_main("will that be all [l_genie_name]?", 9, 1, 4, 2)
                        m "Yes, thank you [luna_name]."
                        call luna_main("You're welcome [l_genie_name].", 7, 2, 4, 3)
                        call luna_main("Well I better be off to class then.", 8, 1, 4, 3)
                        m "Don't you want your payment first?"
                        call luna_main("Oh right...", 5, 2, 4, 1)
                    "-Grope her-" if luna_grope:
                        $ current_payout = 35
                        ">You start running your hands along the outside of her thighs."
                        call luna_main("...", 4, 1, 4, 6)
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        call luna_main("....", 5, 2, 4, 6)
                        m "yes, just like that [luna_name]."
                        "You move your hands up to her waist"
                        call luna_main("......", 6, 3, 4, 6)
                        m "gods you've got such a nice ass."
                        $ luna_tears = 1
                        call luna_main("t-thank you [l_genie_name]...", 2, 2, 4, 3)
                        ">You Start moving your hands slowly up over her smooth stomach."
                        call luna_main(".........", 6, 2, 4, 3)
                        m "That's it [luna_name], just enjoy yourself..."
                        $ luna_tears = 0
                        call luna_main("..................", 6, 2, 4, 2)
                        ">your hands are about an inch below her breasts..."
                        m "mmmm, almost there..."
                        call luna_main("..........................", 4, 2, 4, 2)
                        ">You quickly move your hands up and grab a hold of her supple breasts over her vest."
                        call luna_main("!!!!", 4, 1, 3, 6)
                        "Luna quickly tries to pull away from you."
                        menu: 
                            "-let her up-":
                                $ current_payout = 55
                                ">Luna quickly stands up and moves around to the front of your desk."
                                $ luna_flip = 1
                                $ luna_xpos = 600
                                $ luna_chibi_xpos = 500
                                $ luna_wear_skirt = True
                                hide screen blkfade
                                with d3 
                                call luna_main("Professor!", 4, 1, 3, 7)
                                call luna_main("Grabbing me there wasn't part of the deal!", 8, 2, 3, 2)
                                m "I just couldn't resist..."
                                call luna_main("*hmph*", 8, 2, 2, 3)
                                m "My apologies, [luna_name]."
                                call luna_main("It's alright... just don't let it happen again!", 8, 1, 3, 9)
                                call luna_main("I think I'd like to be paid now...", 8, 2, 2, 3)
                            "-Hold her down-":
                                if luna_sub <= 4:
                                    $ luna_sub += 1
                                call luna_main("Professor!", 4, 1, 3, 7)
                                call luna_main("I'd like to leave now!", 8, 2, 3, 2)
                                m "just a bit longer [luna_name]..."
                                ">You start grinding your hard cock between her ample cheeks."
                                call luna_main("!!!", 4, 3, 4, 3)
                                call luna_main("I insist you let me go!", 4, 2, 3, 4)
                                m "If you leave now you can forget about hogwarts purchasing any more of your father's newspaper, [luna_name]."
                                call luna_main("...", 6, 3, 4, 3)
                                $ luna_tears = 1
                                call luna_main("you're despicable [l_genie_name]...", 8, 2, 2, 3)
                                ">You give her tits a couple of firm squeezes..."
                                call luna_main("ah{image=textheart}...", 7, 3, 4, 3)
                                call luna_main("this isn't right...", 7, 2, 4, 3)
                                m "I know, I know... But it's hard to resist..."
                                call luna_main(".................", 5, 3, 4, 2)
                                call luna_main("....................ah...{image=textheart}", 5, 3, 4, 14)
                                call luna_main("[l_genie_name], you need to stop now...", 7, 2, 4, 3)
                                m "Just a bit longer..."
                                $ luna_tears = 2
                                call luna_main("please...", 7, 3, 4, 3)
                                m "mmmm, I suppose this will have to do..."
                                ">You give her tits a final pinch..."
                                call luna_main("ah...", 7, 3, 4, 3)
                                ">Luna quickly stands up and moves around to the front of your desk."
                                $ luna_flip = 1
                                $ luna_tears = 1
                                $ luna_xpos = 600
                                $ luna_chibi_xpos = 500
                                $ luna_wear_skirt = True
                                hide screen blkfade
                                with d3 
                                call luna_main("Professor!", 4, 1, 3, 7)
                                call luna_main("Grabbing me there wasn't part of the deal!", 8, 2, 3, 2)
                                m "Sorry, [luna_name], I just couldn't help myself..."
                                call luna_main(".......just please try to control yourself next time...", 8, 1, 3, 9)
                                m "So you want there to be a next time?"
                                call luna_main("as long as I'm getting paid.", 8, 2, 2, 3)
                                call luna_main("speaking of which...", 8, 1, 2, 3)
                                call luna_main("can I please be paid now?", 8, 3, 4, 3)


            "-Do nothing-" if luna_sub <= luna_dom:
                call luna_main("...", 7, 1, 2, 2)
                call luna_main("......", 8, 2, 2, 3)
                call luna_main("I suppose I'll start then...", 6, 2, 2, 2)
                ">Luna lightly places herself on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("You're so pathetic...", 5, 2, 2, 3)
                call luna_main("THe worlds greatest wizard...", 5, 2, 1, 1)
                call luna_main("More like the worlds greatest pervert.", 9, 2, 2, 3)
                if luna_name == "Miss Lovegood":
                    $ luna_name = "Princess"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", 5, 2, 3, 14)
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", 8, 2, 2, 3)
                m "I don't recall begging."
                call luna_main("Hmmm...", 7, 2, 1, 2)
                ">Luna stands up slowly."
                call luna_main("Well then...", 8, 2, 2, 3)
                m "what?"
                call luna_main("beg...", 5, 2, 3, 3)
                m "Please..."
                call luna_main("Please what?", 5, 2, 1, 2)
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", 7, 2, 2, 1)
                ">She starts rocking back and forward on your lap"
                call luna_main("ugh, You're so hard...", 9, 3, 3, 3)
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", 5, 2, 2, 1)
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", 7, 2, 2, 2)
                m "of course..."
                call luna_main("...", 8, 2, 2, 3)
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", 5, 2, 3, 1)
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", 2, 2, 1, 1)
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", 5, 2, 2, 1)
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", 9, 1, 2, 1)
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your queen...", 9, 1, 4, 1)
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
                call luna_main("mmmm... pathetic...", 5, 2, 3, 1)
                call luna_main("...", 7, 2, 2, 3)
                call luna_main("......", 8, 3, 3, 2)
                call luna_main(".........", 9, 3, 3, 3)
                call luna_main("Alright, time's up!", 5, 2, 2, 1)
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3 
                call luna_main("*hmph* You naughty [l_genie_name]!", 9, 1, 2, 2)
                m "You can hardly blame me for this."
                call luna_main("What? You're the one who begged for it, of course it's your fault.", 7, 2, 3, 3)
                m "well you didn't have to be so good at it."
                call luna_main("I was just making sure that I earned my reward.", 8, 1, 2, 1)
                call luna_main("Speaking of which...", 5, 2, 1, 1)
                $ current_payout = 200


            "-Ask Nicely-" if luna_dom >= 2:
                if luna_dom <= 3:
                    $ luna_dom += 1
                m "can you please sit on my lap [luna_name]?"
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("well seeing as how you asked so nicely...", 6, 2, 1, 1)
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", 5, 3, 2, 1)
                call luna_main("You're pathetic...", 5, 2, 2, 1)
                call luna_main("THe worlds greatest wizard...", 5, 2, 1, 1)
                call luna_main("More like the worlds greatest pervert.", 9, 3, 2, 1)
                if l_genie_name == "Old man":
                    $ l_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", 5, 3, 2, 14)
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", 8, 2, 2, 1)
                m "I don't recall begging."
                call luna_main("Hmmm...", 5, 2, 2, 1)
                ">Luna stands up slowly."
                call luna_main("Well then...", 8, 2, 2, 3)
                m "what?"
                call luna_main("beg...", 5, 2, 3, 3)
                m "Please..."
                call luna_main("Please what?", 5, 1, 5, 1)
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", 7, 2, 2, 1)
                ">She starts rocking back and forward on your lap"
                call luna_main("You're so hard...", 5, 3, 3, 1)
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", 5, 2, 5, 1)
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", 7, 2, 2, 1)
                m "of course..."
                call luna_main("...", 8, 2, 2, 1)
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", 5, 3, 3, 1)
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", 2, 2, 2, 1)
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", 5, 2, 1, 1)
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", 9, 1, 2, 1)
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", 9, 1, 4, 14)
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
                call luna_main("...", 7, 2, 2, 3)
                call luna_main("......", 8, 3, 5, 1)
                call luna_main(".........", 9, 2, 3, 1)
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [luna_name]."
                call luna_main("Who says you get to decide when this ends?", 9, 2, 2, 3)
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call luna_main("really?", 8, 2, 5, 1)
                call luna_main("But you sounded so sincere earlier when you were begging for this.", 5, 2, 4, 14)
                call luna_main("Surely you don't want it to end already?", 5, 2, 2, 1)
                ">she pushes hard against your cock."
                g11 "ah..."
                call luna_main("That's it [l_genie_name], just keep enjoying yourself.", 8, 3, 2, 1)
                g11 "I can't, it's too sensitive..."
                call luna_main("I don't see how that's my problem.", 8, 2, 4, 1)
                ">She starts moving as fast as she can."
                g11 "{size=-2}ahhh...{/size}"
                call luna_main("come on [l_genie_name]...", 9, 2, 2, 1)
                g11 "{size=+4}aghhh!{/size}"
                call luna_main("shoot another filthy load...", 9, 2, 3, 1)
                g4 "{size=+4}*Argh!* It's too much!{/size}"
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", 9, 3, 3, 1)
                ">You start shooting another load against the inside of your sodden cloak."
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
                g4 "Argh!"
                call luna_main("good boy...", 5, 2, 3, 1)
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3 
                call luna_main("*hmph* You nasty old [l_genie_name]!", 9, 1, 2, 1)
                m "ah..."
                call luna_main("Enjoy yourself a little too much did we?", 7, 2, 3, 1)
                m "That was too much [luna_name]..."
                call luna_main("Stop complaining. I was just making sure that I earned my reward.", 8, 1, 2, 1)
                call luna_main("Speaking of which...", 5, 2, 1, 1)
                $ current_payout = 250


        if luna_dom >= luna_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [luna_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", 8, 2, 2, 3) 
            call luna_main("Thank you, [l_genie_name].", 6, 2, 2, 2)   
        else:
            call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
        ">Luna leaves your office."  

    elif luna_corruption >= 5: #THIRD TIME 
        if luna_corruption <= 5:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "Can I offer you another seat [luna_name]?"
        if luna_sub > luna_dom:
            call luna_main("...", 1, 3, 4, 2) 
            call luna_main("Alright [l_genie_name]...", 1, 2, 4, 2) 
            m "Good girl."
            call luna_main("...", 1, 3, 4, 3) 
        else:
            call luna_main("Fine...", 1, 2, 2, 2) 
            call luna_main("But I expect to be fairly compensated [l_genie_name]...", 7, 1, 2, 2)
            m "yes, yes..."
            call luna_main("...", 7, 2, 2, 2) 
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
            "-Pull her onto your lap-" if luna_sub >= 3:
                if luna_sub <= 4:
                    $ luna_sub += 1
                $ luna_grope = True
                ">You grab Luna by the waist and pull her hard onto your lap."
                call luna_main("!!!", 4, 2, 4, 2) 
                call luna_main("There's no need to be so forceful [l_genie_name]!", 7, 2, 4, 4)
                m "Sorry, it's hard to help myself when I've got such an eager slut in front of me. You don't mind do you?" 
                call luna_main("...", 6, 3, 4, 1)
                call luna_main("......", 5, 2, 4, 2)
                m "Do you?..."
                call luna_main("{size=-5}No...{/size}", 6, 3, 4, 2)
                call luna_main("...", 6, 2, 4, 2) 
                m "No what?"
                call luna_main("{size=-5}No... sir...{/size}", 6, 3, 4, 6) 
                m "Good girl..."
                ">You push your cock hard against her ass."
                call luna_main("ah... thank you [l_genie_name]...", 6, 3, 4, 1) 
                call luna_main("...", 6, 3, 4, 3) 
                jump luna_lap_dance_3

            "-Tell her to sit down-" if luna_sub >= luna_dom:
                $ luna_grope = False
                if luna_sub <= 3:
                    $ luna_sub += 1
                m "why don-"
                ">Luna quickly sits down on your lap, wriggling around slightly until your cock rests between her cheeks."
                call luna_main("(ah...{image=textheart})", 8, 3, 4, 1) 
                call luna_main("......", 4, 2, 4, 3) 
                m "Some one's eager today..."
                call luna_main("...", 8, 3, 4, 3) 
                ">Luna softly starts rocking her hips back and forth."
                m "mmmmm..."
                call luna_main("...", 6, 2, 4, 2) 
                call luna_main("(he's so hard...{image=textheart})", 6, 3, 4, 1) 

                label luna_lap_dance_3:
                    m "That's it, now just start moving your ass a little more."
                ">Luna starts forcefuly grinding her supple ass against you."
                m "mmmm, that's it."
                call luna_main("...", 8, 3, 4, 3) 
                call luna_main("is this good?", 5, 2, 4, 2) 
                m "yes, just keep going..."
                call luna_main("For how long?", 8, 1, 4, 3) 
                m "As long as it takes [luna_name]."
                call luna_main("fine...", 8, 2, 4, 3)
                call luna_main("...", 8, 3, 4, 3)
                call luna_main("..........", 9, 3, 4, 3)
                call luna_main("Is there anything I can do to speed this up?", 6, 2, 4, 1) 
                call luna_main("Not that I want it to end...", 6, 3, 4, 1) 
                call luna_main("It's just that people will start to ask questions if-", 5, 2, 4, 2) 
                menu:
                    "-enjoy yourself-":
                        $ current_payout = 75
                        m "shhh... Just keep doing what you're doing..."
                        call luna_main("...", 6, 3, 4, 6)
                        call luna_main("How about this?", 5, 3, 4, 2)
                        ">Luna starts jiggling her ass slightly as she rocks back and forth."
                        m "Mmmm, yes!"
                        ">You start thrusting into her ever so slightly."
                        call luna_main("...", 6, 3, 4, 4)
                        m "That's it [luna_name], not much longer now."
                        call luna_main(".......", 5, 2, 4, 2)
                        m "mmmm, almost there..."
                        call luna_main("Already?", 4, 2, 4, 3)
                        m "Almost... this is really good..."
                        call luna_main("it is?", 5, 2, 4, 1)
                        m "yeah, just keep moving that perfect little ass of yours..."
                        call luna_main("...", 5, 2, 4, 1)
                        call luna_main("How's this?", 5, 3, 4, 5)
                        ">She starts rocking back and forward on your lap"
                        m "mmmmm"
                        call luna_main("You're so hard [l_genie_name]...", 5, 3, 4, 1)
                        m "mmmm"
                        call luna_main("are you almost there?", 5, 2, 4, 1)
                        m "yes..."
                        call luna_main("well I expect to be-", 5, 2, 2, 3)
                        m "shhh, don't ruin it."
                        call luna_main("...", 8, 2, 4, 3)
                        ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                        m "ah..."
                        call luna_main("...", 5, 2, 4, 3)
                        m "keep going [luna_name]..."
                        call luna_main("........", 3, 2, 4, 1)
                        m "mmm, just a little more..."
                        call luna_main("...[l_genie_name]...", 7, 3, 4, 1)
                        ">Luna starts grinding hard against your lap."
                        m "{size=-2}(mmmm...){/size}"
                        call luna_main("......", 6, 1, 4, 1)
                        g4 "{size=+4}(agh... almost there...){/size}"
                        $ luna_tears = 1
                        call luna_main("............", 9, 1, 4, 1)
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
                        $ luna_tears = 0
                        call luna_main("ugh...", 5, 2, 4, 1)
                        call luna_main("...", 8, 2, 4, 3)
                        call luna_main("......", 8, 3, 4, 2)
                        call luna_main(".........", 5, 3, 4, 3)
                        call luna_main("Are you finished now [l_genie_name]?", 5, 2, 4, 1)
                        m "Almost... just stay there for a little longer..."
                        call luna_main("ok......", 5, 3, 4, 1)
                        ">Luna waits for a few seconds before standing up."
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        $ luna_wear_skirt = True
                        hide screen blkfade
                        with d3 
                        call luna_main("will that be all [l_genie_name]?", 9, 1, 4, 1)
                        m "Yes, thank you [luna_name]."
                        call luna_main("You're welcome [l_genie_name].", 7, 2, 4, 3)
                        call luna_main("Well I better be off to class then.", 8, 1, 4, 3)
                        m "Don't you want your payment first?"
                        call luna_main("Oh right...", 5, 2, 4, 1)
                    "-Grope her-" if luna_grope:
                        $ current_payout = 35
                        ">You start running your hands along the outside of her thighs."
                        call luna_main("ah...{image=textheart}", 4, 1, 4, 1)
                        m "mmmm, lovely."
                        ">You keep grinding your cock against her butt checks."
                        call luna_main("....", 5, 3, 4, 6)
                        m "yes, just like that [luna_name]..."
                        "You move your hands to her knees, just at the edge of her skirt."
                        call luna_main("......", 6, 3, 4, 1)
                        m "gods you've got such nice legs."
                        $ luna_tears = 1
                        call luna_main("t-thank you [l_genie_name]...", 2, 2, 4, 2)
                        ">You Start slowly moving your hands back towards her waist, pulling up her skirt slightly as you go."
                        call luna_main(".........", 6, 2, 4, 3)
                        m "That's it [luna_name], just enjoy yourself..."
                        $ luna_tears = 0
                        call luna_main("..................", 6, 2, 4, 2)
                        ">you move your hands to the inside of her thighs..."
                        m "mmmm, that's it..."
                        call luna_main("..........................", 4, 2, 4, 2)
                        ">You start stroking the insides of her thighs, moving closer towards her sex each time."
                        call luna_main("!!!!", 4, 1, 3, 6)
                        $ luna_tears = 1
                        if luna_sub <= 4:
                            $ luna_sub += 1
                        call luna_main("Professor...", 4, 1, 3, 7)
                        call luna_main("please...", 8, 2, 3, 2)
                        m "just a bit longer [luna_name]..."
                        ">You start grinding your hard cock between her ample cheeks."
                        call luna_main("...", 4, 3, 4, 3)
                        call luna_main("[l_genie_name]...", 8, 2, 2, 3)
                        ">You start lightly running your the tips of your fingers up and down her thighs..."
                        call luna_main("ah{image=textheart}...", 7, 3, 4, 3)
                        $ luna_tears = 2
                        call luna_main("[l_genie_name]... this isn't right...", 7, 2, 4, 3)
                        m "you don't seem to mind..."
                        call luna_main("(I'll let him keep going for a little bit more...)", 5, 3, 4, 2)
                        call luna_main("(Then I'll make him stop).......ah...{image=textheart}", 5, 3, 4, 14)
                        call luna_main("[l_genie_name], how much longer do you need?...", 7, 2, 4, 3)
                        m "Just a bit longer..."
                        ">Luna keeps rubbing her ass against your sensitive cock."
                        m "ugh, that's it [luna_name]."
                        call luna_main("p-please hurry [l_genie_name]...", 9, 2, 4, 3)
                        m "Well I think I might know a way to speed this up."
                        call luna_main("really?", 8, 2, 4, 1)
                        call luna_main("what are-", 5, 2, 4, 14)
                        ">You quickly move your hands up and grab a hold of her supple breasts through her vest."
                        call luna_main("!!!!", 4, 1, 3, 6)
                        ">Luna's body quivers as her hips roll against you."
                        m "mmm that's it [luna_name]..."
                        call luna_main("...", 8, 3, 4, 1)
                        m "I think someone's enjoying herself."
                        call luna_main("What?", 8, 2, 4, 1)
                        call luna_main("You think I enjoy this? Feeling your disgusting old cock grind against me?", 8, 3, 4, 1)
                        m "{size=-2}ahhh...{/size}"
                        call luna_main("while you paw at me like some filthy old pervert?", 9, 6, 4, 1)
                        m "{size=+4}aghhh!{/size}"
                        call luna_main("you really are a filthy old man aren't you...", 9, 2, 4, 1)
                        g4 "{size=+4}*Argh!* that's is [luna_name]! here it comes!{/size}"
                        call luna_main("!!!!", 4, 3, 4, 6)
                        ">You start shooting a massive load against Luna's ass"
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
                        g4 "Argh!"
                        call luna_main(".....", 8, 3, 4, 1)
                        ">Luna stands up from your lap"
                        $ luna_flip = 1
                        $ luna_xpos = 600
                        $ luna_chibi_xpos = 500
                        hide screen blkfade
                        with d3 
                        call luna_main("*hmph*", 9, 1, 2, 1)
                        m "ah... gods that was good"
                        $ luna_tears = 1 
                        call luna_main("I think I'd like to leave now [l_genie_name]...", 5, 2, 1, 1)

            "-Ask Nicely-" if luna_dom >= luna_sub:
                if luna_dom <= 3:
                    $ luna_dom += 1
                m "can you please sit on my lap [luna_name]?"
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("well seeing as how you asked so nicely...", 6, 2, 1, 1)
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", 5, 3, 2, 1)
                call luna_main("You're pathetic...", 5, 2, 2, 1)
                call luna_main("THe worlds greatest wizard...", 5, 2, 1, 1)
                call luna_main("More like the worlds greatest pervert.", 9, 3, 2, 1)
                if l_genie_name == "Old man":
                    $ l_genie_name = "Pervert"
                ">Luna stands bouncing slowly on your lap, lifting her weight on and off your crouch."
                m "yes... that's it."
                call luna_main("*hmph* You're not even ashamed are you?", 5, 3, 2, 14)
                m "of what?"
                call luna_main("What? begging your student for a lap dance.", 8, 2, 2, 1)
                m "I don't recall begging."
                call luna_main("Hmmm...", 5, 2, 2, 1)
                ">Luna stands up slowly."
                call luna_main("Well then...", 8, 2, 2, 3)
                m "what?"
                call luna_main("beg...", 5, 2, 3, 3)
                m "Please..."
                call luna_main("Please what?", 5, 1, 5, 1)
                m "Please keep going [luna_name]..."
                ">Luna slowly places herself back on your lap."
                call luna_main("That's better isn't it?", 7, 2, 2, 1)
                ">She starts rocking back and forward on your lap"
                call luna_main("You're so hard...", 5, 3, 3, 1)
                m "mmmm"
                call luna_main("I bet you'd cum if I kept going wouldn't you...", 5, 2, 5, 1)
                m "yes..."
                call luna_main("well you better be prepared to pay extra for the privilige...", 7, 2, 2, 1)
                m "of course..."
                call luna_main("...", 8, 2, 2, 1)
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah..."
                call luna_main("a {size=+5}lot{/size} extra...", 5, 3, 3, 1)
                m "of course [luna_name]..."
                call luna_main("Good. just enjoy yourself then...", 2, 2, 2, 1)
                m "mmm, just a little more..."
                call luna_main("...[l_genie_name]", 5, 2, 1, 1)
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", 9, 1, 2, 1)
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", 9, 1, 4, 14)
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
                call luna_main("...", 7, 2, 2, 3)
                call luna_main("......", 8, 3, 5, 1)
                call luna_main(".........", 9, 2, 3, 1)
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, that's enough now [luna_name]."
                call luna_main("Who says you get to decide when this ends?", 9, 2, 2, 3)
                ">Luna starts rolling her hips, focusing on the head of your cock."
                g11 "ah, please, not after I just came."
                call luna_main("really?", 8, 2, 5, 1)
                call luna_main("But you sounded so sincere earlier when you were begging for this.", 5, 2, 4, 14)
                call luna_main("Surely you don't want it to end already?", 5, 2, 2, 1)
                ">she pushes hard against your cock."
                g11 "ah..."
                call luna_main("That's it [l_genie_name], just keep enjoying yourself.", 8, 3, 2, 1)
                g11 "I can't, it's too sensitive..."
                call luna_main("I don't see how that's my problem.", 8, 2, 4, 1)
                ">She starts moving as fast as she can."
                g11 "{size=-2}ahhh...{/size}"
                call luna_main("come on [l_genie_name]...", 9, 2, 2, 1)
                g11 "{size=+4}aghhh!{/size}"
                call luna_main("shoot another filthy load...", 9, 2, 3, 1)
                g4 "{size=+4}*Argh!* It's too much!{/size}"
                call luna_main("{image=textheart}{image=textheart}{image=textheart}", 9, 3, 3, 1)
                ">You start shooting another load against the inside of your sodden cloak."
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
                g4 "Argh!"
                call luna_main("good boy...", 5, 2, 3, 1)
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3 
                call luna_main("*hmph* You nasty old [l_genie_name]!", 9, 1, 2, 1)
                m "ah..."
                call luna_main("Enjoy yourself a little too much did we?", 7, 2, 3, 1)
                m "That was too much [luna_name]..."
                call luna_main("Stop complaining. I was just making sure that I earned my reward.", 8, 1, 2, 1)
                call luna_main("Speaking of which...", 5, 2, 1, 1)
                $ current_payout = 250


            "-Beg-" if luna_dom >= 3:
                if luna_dom <= 3:
                    $ luna_dom += 1
                m "can you please sit on my lap [luna_name]?"
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("keep going...", 6, 2, 1, 1)
                m "please place your perfect little ass on my lap princess..."
                call luna_main("that's better...", 6, 2, 1, 1)
                ">Luna lightly sits on your lap."
                m "mmmm"
                ">You start to feel yourself get hard against her ass"
                call luna_main("...", 5, 3, 2, 1)
                call luna_main("that's it [l_genie_name]...", 5, 2, 1, 1)
                call luna_main("just sit back and enjoy yourself...", 5, 2, 1, 1)
                call luna_main("enjoy the feeling of your disgusting old cock rub against me...", 9, 3, 2, 1)
                ">Luna stands moving her hips backward and forwards..."
                m "ah..."
                call luna_main("*hmph* that's it... tell me how good it feels.", 5, 3, 2, 14)
                m "w-what?"
                call luna_main("tell me how good it feels to rub that filthy cock of your against me...", 8, 2, 2, 1)
                m "..."
                call luna_main("go on... or else.", 5, 2, 2, 1)
                ">Luna goes to stand up slowly."
                m "alright... I'll do it."
                ">Luna sits back down onto your lap"
                call luna_main("good boy...", 5, 2, 1, 1)
                m "it's like I'm rubbing up against a ...cloud..."
                call luna_main("a cloud?", 5, 2, 5, 3)
                m "I mean it's soft..."
                ">Luna slowly grinds against your shaft."
                call luna_main("I suppose that's better than nothing.", 7, 2, 5, 1)
                m "mmmm, keep going [luna_name]..."
                call luna_main("pervert...", 9, 2, 3, 1)
                m "yes..."
                call luna_main("do you even know old I am?", 7, 2, 2, 1)
                m "of course..."
                call luna_main("well...", 8, 2, 2, 1)
                ">luna starts rocking her hips forward and backwards, your cock pressed between her cheeks."
                m "ah... 18?"
                call luna_main("{size=-5}18?{/size} you don't sound so sure about that [l_genie_name]...", 5, 3, 3, 1)
                m "..."
                call luna_main("what if I'm 17?", 9, 2, 4, 1)
                m "mmm..."
                call luna_main("I bet that'd just make you harder wouldn't it?", 5, 2, 1, 2)
                ">Luna starts rubbing hard against your lap."
                m "{size=-2}(mmmm...){/size}"
                call luna_main("come on...", 9, 1, 2, 1)
                g4 "{size=+4}(agh... almost there...){/size}"
                call luna_main("come for your little girl...", 9, 1, 4, 14)
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
                g4 "Argh... YES!"
                call luna_main("ugh... pathetic...", 5, 2, 3, 1)
                call luna_main("...", 7, 2, 2, 3)
                call luna_main("......", 8, 3, 5, 1)
                call luna_main(".........", 9, 2, 3, 1)
                ">Luna keeps rubbing her ass against your sensitive cock."
                g11 "ugh, no more please [luna_name]."
                call luna_main("good boy...", 5, 2, 3, 1)
                ">Luna stands up from your lap"
                $ luna_flip = 1
                $ luna_xpos = 600
                $ luna_chibi_xpos = 500
                hide screen blkfade
                with d3 
                call luna_main("*hmph* You're such nasty old [l_genie_name]!", 9, 1, 2, 1)
                call luna_main("But I suppose I don't mind, as long as I get my reward.", 8, 1, 2, 1)
                call luna_main("Speaking of which...", 5, 2, 1, 1)
                $ current_payout = 250


        if luna_dom >= luna_sub:
            m "Alright, alright. Here's your gold."
        else:
            m "Here's your payment [luna_name]."
        $ gold -= current_payout
        $ luna_gold += current_payout
        ">You hand Luna [current_payout] gold."
        if current_payout <= 50:
            call luna_main("(only [current_payout]?) *hmph*", 8, 2, 2, 3) 
            call luna_main("Thank you, [l_genie_name].", 6, 2, 2, 2)   
        else:
            call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
        ">Luna leaves your office."  
    hide screen genie_jerking_sperm_02    
    jump luna_away



label luna_favour_3: #STRIP FOR ME - Have this as one favour with three options for each path. 
    if luna_corruption <= 8:
        $ luna_corruption += 1
    play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
    if luna_corruption < 8:
        if luna_sub > luna_dom and luna_corruption < 5:
            m "Have you ever been naked in front of another person [luna_name]?"
            call luna_main("What?", 1, 3, 4, 2) 
            call luna_main("Well... um... not really, I suppose.", 1, 2, 4, 2) 
            m "Well then there's a first time for everything!"
            call luna_main("...", 1, 3, 4, 3) 
        elif luna_sub > luna_dom :
            m "How would you like to step out of those restrictive clothes [luna_name]?"
            call luna_main("...", 1, 3, 4, 2) 
            call luna_main("Well... {size=-3}they're{/size} {size=-4}not{/size} {size=-5}really{/size} {size=-6}that{/size} {size=-7}restrictive.{/size}", 1, 2, 4, 2) 
            m "..."
            call luna_main("alright then [l_genie_name]...", 1, 3, 4, 3) 
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("...", 1, 2, 4, 3)  
        else:
            m "You don't mind taking some of your clothes of do you [luna_name]?"
            call luna_main("I suppose not...", 1, 2, 2, 2) 
            call luna_main("So long as your prepared to show some {i}appreciation...{/i}", 7, 1, 2, 2)
            m "yes, [luna_name]..."
            call luna_main("...pervert...", 7, 2, 2, 2) 
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("...", 7, 2, 2, 2) 
        menu:
            "\"Take off your skirt.\"" if luna_sub >= 5:
                $ luna_choice = 1
                call luna_main("you want me to take of my skirt!", 4, 1, 4, 4) 
                m "Yes... You think you could manage that?"
                call luna_main("of course I can manag-", 7, 2, 4, 2) 
                m "Fantastic! Why don't you pop it off then so we can take a look..."
                call luna_main("...", 3, 3, 4, 2) 
                call luna_main("Fine... (I hope he doesn't expect me to take off my panties as well)", 7, 3, 4, 4) 
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                ">Luna slowly steps out of her skirt and places it on your desk."
                show screen luna
                hide screen blkfade
                with d3
                call luna_main("There... are you happy now [l_genie_name]?", 8, 3, 4, 3) 
                m "Almost... take off your shirt next."
                call luna_main("...alright...", 6, 2, 4, 6)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">Luna starts to unbutton her shirt..."
                ">She slowly fumbles with the buttons until Finally the last button is undone..."
                ">Luna begrudgingly takes off her shirt and places it on top of her skirt."
                show screen luna
                hide screen blkfade
                with d3

            "\"Take off your shirt.\"" if luna_sub > luna_dom:
                $ luna_choice = 2
                call luna_main("my shirt?", 7, 1, 4, 2)
                m "Did I stutter [luna_name]?"
                call luna_main("no...", 8, 2, 4, 2)
                m "well Why don't you take it off then so we can take a look..."
                call luna_main("...", 9, 3, 4, 3)
                call luna_main("Fine... (I hope he doesn't expect me to take off my bra as well)", 7, 2, 4, 2)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">Luna starts to unbutton her shirt..."
                ">She slowly fumbles with the buttons until Finally the last button is undone..."
                ">Luna begrudgingly takes off her shirt and places it on top of your desk."
                show screen luna
                hide screen blkfade
                with d3
                pause
                call luna_main("There... are you happy now [l_genie_name]?", 9, 1, 4, 2)
                m "Almost... take off your skirt next."
                call luna_main("...fine...", 7, 2, 4, 2)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly starts to unzip her skirt..."
                ">She seems very hesitant and takes her time..."
                ">Finally the zipper is undone and she has no choice but to take the skirt off..."
                ">Luna slowly steps out of her skirt and places it on top of her shirt."
                show screen luna
                hide screen blkfade
                with d3

            "\"Please take off your shirt.\"" if luna_dom >= luna_sub:
                $ luna_choice = 3
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("well seeing as how you said the magic word I suppose it's only fair...", 6, 2, 1, 1)
                m "thank you [luna_name]."
                call luna_main("(Who'd have thought it'd be the easy...)", 7, 2, 1, 1) 
                call luna_main("close your eyes...", 8, 1, 2, 2) 
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">you can hear the soft ruffle of clothes being removed..."
                ">You hear her softly place her shirt and vest on the table..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "just a second..."
                lun "Alright, go ahead."
                show screen luna
                hide screen blkfade
                with d3 
                pause

            "\"Please take off your skirt [luna_name]...\"" if luna_dom >= 5:
                $ luna_choice = 4
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("well seeing as how you said the magic word I suppose it's only fair...", 6, 2, 1, 1)
                m "thank you [luna_name]."
                call luna_main("(Who'd have thought it'd be the easy...)", 7, 2, 1, 1) 
                call luna_main("well... close your eyes...",8, 1, 2, 2)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">you can hear the soft ruffle of clothes and zips..."
                ">You hear her softly place her skirt on the table..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "just a second..."
                lun "Alright, go ahead."
                show screen luna
                hide screen blkfade
                with d3 
                pause

        if luna_choice <= 2: #luna sub choices
            if luna_sub <= 5:
                $ luna_sub += 1
            m "Good... now your underwear..."
            call luna_main("!!!", 4, 1, 4, 2)
            call luna_main("You're not serious are you?", 7, 2, 4, 2)
            m "I am. And I expect you to do it now, [luna_name]."
            call luna_main("[l_genie_name]!", 8, 1, 3, 3)
            m "don't you raise your voice at me, [luna_name]!"
            call luna_main(".....!!?", 7, 2, 4, 2)
            m "Nobody is forcing you to do this."
            call luna_main("but-", 5, 2, 4, 2)
            m "I am doing you and your family a favour!"
            m "so If you don't think your father needs help with his failing magazine, please feel free to leave."
            call luna_main(".....................", 6, 2, 4, 3) 
            call luna_main(".......................................", 7, 3, 4, 2) 
            $ luna_tears = 1
            call luna_main("please [l_genie_name]...", 8, 1, 4, 2)
            call luna_main("isn't there anything else I can do...", 9, 2, 4, 2)
            menu:
                "-Make her strip-" if luna_choice == 1:
                    $ current_payout = 40
                    m "Take off your underwear now [luna_name]..."
                    call luna_main("{size=-5}(Should I really do this?){/size}", 9, 3, 4, 2)
                    call luna_main("[l_genie_name] I don't know about this... ", 8, 1, 4, 2)
                    if daytime:
                        m "Come on [luna_name], just a little peek and then you'll be off to class."
                    else:
                        m "Come on [luna_name], just a little peek and then you'll be off to bed."
                    call luna_main("Alright [l_genie_name]... ", 9, 3, 4, 2)
                    call luna_main("(Stripping for the headmaster...)", 9, 2, 4, 2)   
                    call luna_main("(imagine if daddy found out...)", 9, 3, 4, 2) 
                    call luna_main("......", 9, 1, 4, 2)
                    hide screen luna
                    show screen blkfade
                    with d3
                    $ luna_wear_bra = False
                    ">Luna slowly unlatches her bra and places it on your desk."  
                    show screen luna
                    hide screen blkfade
                    with d3
                    m "Mmmm, very nice [luna_name]."
                    m "Now for your panties..."
                    $ luna_tears = 2
                    call luna_main("yes [l_genie_name]... ", 8, 2, 4, 3)
                    hide screen luna
                    show screen blkfade
                    with d3
                    $ luna_wear_panties = False
                    ">Luna slightly turns to the side so you can't quite make out her crouch..."
                    ">She's very hesitant and takes her time pulling down her panties..."
                    ">Luna slowly steps out of her panties and places them on top of the pile of clothes on your desk." 
                    show screen luna
                    hide screen blkfade
                    with d3
                    pause
                    call luna_main("...", 9, 3, 4, 3)
                    m "Very nice..."
                    call luna_main("c-can I get dressed now... it's a bit cold in here.", 9, 2, 4, 2)
                    m "mmmm... so I can see."
                    call luna_main("!!!", 4, 1, 2, 3)
                    call luna_main("That's enough! I refuse to stand here any longer!", 9, 1, 3, 2)

                "-start touching yourself-":
                    $ current_payout = 65
                    m "anything..."
                    hide screen blktone
                    with d3
                    ">You reach under the desk and grab your cock..."
                    hide screen blktone8
                    with d3
                    hide screen genie
                    show screen genie_jerking_off
                    with d3
                    pause 
                    m "Is this better [luna_name]?"
                    call luna_main("{size=-3}I suppose so...{/size}", 6, 3, 4, 3)
                    m "Well if it makes you happy..."
                    ">You start stroking faster."
                    call luna_main("...", 6, 3, 4, 3)
                    m "Yes... Ah, yes, this is good..."
                    $ luna_tears = 3
                    call luna_main("Fine! Have it your way, [l_genie_name]!", 6, 3, 4, 3)
                    call luna_main("enjoy stroking your filthy old cock while you force me stand here...", 6, 1, 3, 3)
                    m "{size=-4}(mmmm... yes...){/size}"
                    m "well seeing as how you are standing there... why don't you give those nice little tits of yours a good shake?"
                    call luna_main("*hmph*...", 7, 1, 2, 2)
                    ">Luna sways her chest side to side ever so slightly."
                    call luna_main("well...", 7, 3, 3, 2)
                    ">You keep on wanking while you gaze at Luna's milky tits..."
                    m "just a little bit faster..."
                    call luna_main("*hmph*... just hurry up get it over with [l_genie_name]...", 6, 3, 4, 3)
                    ">Luna starts shaking her chest a little faster"
                    m "{size=-4}ah...{/size}"
                    m "that's it slut... keep going..."
                    call luna_main("........", 8, 1, 3, 2)
                    m "{size=-4}(argh... yes...){/size}"
                    call luna_main("(he's going to shoot it all out front of me...)", 7, 3, 4, 2)
                    m "{size=-4}yes...{/size}"
                    call luna_main("(Should I stop.)", 9, 2, 4, 3)
                    g4 "{size=+2}mmmm... thats it keep shaking those milky tits...{/size}"
                    call luna_main(".........", 5, 1, 4, 1)
                    g4 "{size=+4}(agh... almost there...){/size}"
                    call luna_main("(too late...)", 9, 3, 4, 1)
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
                    call luna_main("ugh... there's so much...", 8, 3, 4, 2)
                    call luna_main("{size=-5}(As usual...){/size}", 8, 2, 4, 1)
                    show screen genie_jerking_sperm_02
                    with d3
                    g4 "good work, slut... ah, shit, this feels so good..."
                    show screen genie
                    hide screen bld1
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("......", 7, 1, 4, 2)
                    m "Ah... you did good [luna_name]..."

            hide screen luna
            show screen blkfade
            with d3
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            ">Luna quickly picks her clothes up off your desk and gets dressed."
            show screen luna
            hide screen blkfade
            with d3
            call luna_main("I think I'd like to leave now [l_genie_name]...", 7, 3, 4, 2)
            m "You're free to leave whenever you like [luna_name]."
            call luna_main("Well I'm certainly not leaving until you pay me!", 9, 1, 2, 3)


        else:
            call luna_main("There... is this what you wanted to see [l_genie_name]?", 7, 1, 2, 2) 
            g4 "gods yes!"
            if luna_dom <= 5:
                $ luna_dom += 1
            call luna_main("well... seeing as how you seem to be enjoying yourself so much...", 5, 1, 2, 1)
            m "what?"
            call luna_main("why don't you start ...touching... yourself [l_genie_name]...", 5, 3, 2, 1)
            m "I'm not sure if-"
            call luna_main("that wasn't a question [l_genie_name]...", 8, 1, 2, 2)
            hide screen blktone
            with d3
            ">You reach under the desk and grab your cock..."
            hide screen blktone8
            with d3
            hide screen genie
            show screen genie_jerking_off
            with d3
            pause  
            call luna_main("there we are...", 8, 1, 4, 1)
            call luna_main("don't you feel better now?", 8, 2, 4, 1)
            m "mmmm... yes..."
            call luna_main("Hmmm, I'm not sure if I believe you.", 9, 1, 4, 3)
            call luna_main("maybe you need a little encouragement...", 9, 2, 4, 1)
            m "encouragement?"
            call luna_main("close your eyes [l_genie_name]...", 9, 1, 4, 1)
            hide screen luna
            show screen blkfade
            with d3
            $ luna_chibi("stand_naked")
            if luna_wear_top:
                $ luna_wear_panties = False
            else:
                $ luna_wear_bra = False
            ">you can hear the soft ruffle of clothes being taken off..."
            ">You feel something light get thrown against your chest..."
            m "???"
            m "Can I open my eyes yet [luna_name]?"
            lun "Go ahead [l_genie_name]..."
            show screen luna
            hide screen blkfade
            with d3 
            g9 "!!!"
            call luna_main("like what you see?", 9, 2, 4, 1)
            g9 "..."
            ">You start stroking your cock with renewed vigor."
            call luna_main("I'll take that as a yes...", 8, 1, 2, 1)
            g9 "Aha... Yeah... This feels great..."
            call luna_main("good... just work up a nice big load for me...", 9, 1, 2, 1)
            if luna_wear_panties:
                call luna_main("if you're a good boy I might even let you shoot it all over my bra...", 8, 2, 2, 1)
            else:
                call luna_main("if you're a good boy I might even let you shoot it all over my panties...", 8, 2, 2, 1)
            g9 "Yes, [luna_name]!"
            call luna_main("I bet you'd love that wouldn't you?", 7, 1, 2, 1)
            m "yes..."
            call luna_main("Shooting your filthy old cum all over my underwear...", 8, 3, 4, 1)
            m "..."
            call luna_main("well come on then [l_genie_name]...", 9, 1, 4, 1)
            call luna_main("keep stroking that disgusting cock of yours...", 9, 1, 2, 1)
            m "{size=-4}(argh... yes...){/size}"
            call luna_main("do you need a little more encouragement [l_genie_name]...", 8, 1, 3, 1)
            m "{size=-4}yes...{/size}"
            call luna_main("say it louder...", 8, 1, 3, 1)
            g9 "{size=+4}yes{/size}"
            call luna_main("well close your eyes...", 9, 1, 3, 1)
            hide screen luna
            show screen blkfade
            with d3
            if luna_wear_panties:
                $ luna_wear_skirt = False
            else:
                $ luna_wear_top = False
            ">you can once more hear the soft ruffle of clothes..."
            m "{size=-2}(mmmm...){/size}"
            lun "open wide [l_genie_name]..."
            show screen luna
            hide screen blkfade
            with d3 
            pause
            m "{size=+2}yes...{/size}"
            call luna_main("you love this don't you...", 9, 1, 2, 1)
            g4 "{size=+4}(agh...){/size}"
            ">you start stroking your cock even faster!"
            g4 "{size=+4}yes...{/size}"
            call luna_main("that's it [l_genie_name], cum for your princess...", 9, 1, 4, 1)
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            g4 "{size=+4}(agh... almost there...){/size}"
            call luna_main("cum...", 9, 1, 3, 14)
            if luna_wear_panties:
                call luna_main("{size=+4}cum all over my bra!{/size}", 9, 1, 3, 14)
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You grab Luna's bra and start stroking your cock into it."
            else:
                call luna_main("{size=+4}cum all over my panties!{/size}", 9, 1, 3, 14)
                g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                ">You grab Luna's panties and start stroking your cock into them."
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
            call luna_main("That's it, [l_genie_name], make sure you cover them...", 9, 1, 3, 1)
            show screen genie_jerking_sperm_02
            with d3
            g4 "ah, shit they're so soft, why does this feels so good..."
            show screen genie
            hide screen bld1
            #show screen genie_jerking_off
            with d3
            call luna_main("mmm...", 8, 1, 3, 1)
            m "ah..."
            call luna_main("keep going... make sure you get every last drop out.", 8, 3, 4, 1)
            m "ah... Thank you..."
            call luna_main("Thank you...?", 9, 1, 5, 3)
            m "Thank you princess..."
            $ luna_name = "Princess"
            call luna_main("*hmph*", 9, 2, 2, 2)
            call luna_main("Well seeing as how you've ...finished... I suppose I better get dressed.", 7, 2, 2, 2)

            hide screen luna
            with d3

            if luna_wear_panties:
                ">Luna quickly picks her clothes up off your desk and gets dressed except for her cum covered bra."
            else:
                ">Luna quickly picks her clothes up off your desk and gets dressed except for her cum covered panties."
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            show screen luna
            with d3
            m "aren't you going to put those on as well?"
            call luna_main("What? and risk contaminating the evidence?", 9, 1, 5, 3)
            m "Evidence..."
            call luna_main("Oh don't worry, I just needed some ...insurance...", 7, 2, 4, 1)
            m "insurance? Against what?"
            call luna_main("well if I tried to tell the ministry of magic what was going on here I'd get laughed out of the room.", 8, 1, 5, 1)
            call luna_main("but this?", 7, 1, 2, 1)
            ">She dangles the cum soaked underwear in front of you."
            call luna_main("This says otherwise.", 7, 3, 2, 1)
            m "How will they know it's mine? That could be anyone's cum!"
            call luna_main("Please... we're taught identification spells in second year. even neville longbottom would know it's yours.", 9, 1, 3, 1)
            m "(Shit, if she actually tries that she might work out I'm not really Dumblefore or whatever his name is...)"
            m "So you're going to tell them everything?"
            call luna_main("What? of course not.", 9, 2, 1, 1)
            call luna_main("As long as you behave yourself...", 9, 1, 1, 1)
            m "And what does that entail?"
            call luna_main("Well first things first we're going to talk about how much I'm going to be paid.", 9, 2, 1, 1)
            call luna_main("300 gold sounds fair to me... {p}how about you?", 9, 1, 2, 1)
            m "It sounds... fair..."
            call luna_main("I'm glad we could come to an agreement.", 8, 2, 4, 1)
            m "yes [luna_name]..."
            call luna_main("Good boy... now, speaking of payment...", 9, 1, 2, 2)
            $ current_payout = 300
    

    else: ###THIRD TIME EVENT IS RUN
        if luna_sub > luna_dom :
            m "You don't mind taking your clothes off again do you [luna_name]?"
            call luna_main("...", 1, 2, 4, 2) 
            call luna_main("Well... {size=-3}I {size=-4}mean {size=-2}I {size=-2}do {size=-2}mind.", 1, 3, 4, 2) 
            m "..."
            call luna_main("...", 1, 1, 4, 2) 
            call luna_main("alright then [l_genie_name]...", 1, 2, 4, 1) 
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("(Why can't I stand up for myself?)", 1, 2, 4, 3)  
            call luna_main("...", 1, 3, 4, 4)  
        else:
            m "If it's not too much trouble-"
            call luna_main("...", 1, 2, 2, 2) 
            m "Could you please take your clothes off?"
            call luna_main("*hmph* {p}Well seeing as how you seemed to have learned some manners.", 7, 1, 2, 2)
            m "yes, [luna_name]..."
            call luna_main("I suppose there's no harm in it...", 5, 2, 2, 1) 
            hide screen luna
            with d3
            $ luna_xpos = 270
            ">Luna positions herself directly in front of your desk."
            call luna_main("...", 9, 1, 2, 1) 
        menu:
            "\"Take off your skirt.\"" if luna_sub >= 5:
                $ luna_choice = 1
                call luna_main("My skirt?", 4, 1, 4, 4) 
                m "Yes..."
                call luna_main("...", 7, 2, 4, 2) 
                call luna_main(".......", 7, 2, 4, 2) 
                call luna_main("{size=-7}Alright...{/size}", 7, 2, 4, 1) 
                m "Mmmm, someone's eager today."
                call luna_main("[l_genie_name]...", 3, 3, 4, 2) 
                call luna_main("...", 1, 2, 4, 1) 
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_skirt = False
                ">Luna slowly starts to unzip her skirt..."
                ">She doesn't hesitate however, quickly placing the skirt on your desk..."
                show screen luna
                hide screen blkfade
                with d3
                call luna_main("There... Is that all [l_genie_name]?", 8, 2, 4, 3) 
                m "Not quite..."
                call luna_main("(Surely he doesn't want me to take off my panties?)", 6, 2, 2, 3)
                call luna_main("[l_genie_name] please...", 7, 1, 4, 2)
                m "Now now [luna_name], a deal's a deal..."
                call luna_main("...", 6, 2, 4, 3)
                $ luna_tears = 1
                call luna_main("At least close your eyes...", 7, 1, 4, 2)
                m "As you wi- {p}command..."
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_panties = False
                ">You hear the soft rustle of clothes..."
                ">Suddenly something is gently placed on your desk"
                show screen luna
                hide screen blkfade
                with d3
                call luna_main("There... are you happy now!", 5, 2, 2, 2)
                g9 "Of course!"
                g9 "I only expected you to take your shirt off!"
                call luna_main("What!", 4, 1, 2, 15)
                call luna_main("Please! let me put them back on!", 4, 1, 4, 2)
                ">Luna scrambles to pick her panties back up off your desk but you're too fast for her, quickly snatching them up."
                m "Ah ah ah miss lovegood."
                call luna_main("You're so... You're so mean!", 8, 2, 4, 2)
                m "Don't complain too much, I was hoping you'd take those off anyway."
                call luna_main("*hmph*", 6, 1, 1, 3)
                m "Well seeing as how we've already crossed this line, how about you take off your top anyway."
                call luna_main("You can't be serious! I think you've seen enough [l_genie_name]!", 7, 1, 2, 3)

            "\"Take off your shirt.\"" if luna_sub > luna_dom:
                $ luna_choice = 2
                call luna_main("my shirt?", 7, 1, 4, 2)
                m "That's not too much is it [luna_name]?"
                call luna_main("no...", 8, 2, 4, 2)
                m "..."
                call luna_main("...", 9, 3, 4, 3)
                call luna_main("ugh, Fine... (I hope he doesn't expect me to take off my bra as well)", 7, 2, 4, 2)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_top = False
                ">Luna starts to unbutton her shirt..."
                ">She gently undoes the buttons, letting it slide off her shoulders before placing it on your desk."
                show screen luna
                hide screen blkfade
                with d3
                pause
                call luna_main("There... is that all [l_genie_name]?", 9, 1, 4, 2)
                m "Almost... take off your bra next."
                call luna_main("[l_genie_name], I really don't-", 7, 2, 4, 2)
                m "[luna_name]..."
                call luna_main("...{p}fine...", 7, 2, 4, 1)
                call luna_main("But you have to close your eyes.", 7, 1, 4, 2)
                m "done."
                call luna_main("...", 9, 3, 4, 1)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_bra = False
                ">You hear the soft rustle of clothes..."
                ">You can hear something being placed softly onto your desk"
                show screen luna
                hide screen blkfade
                with d3
                m "Very nice..."
                m "Now you're skirt."
                call luna_main("You can't be serious! I think you've seen enough [l_genie_name]!", 7, 1, 2, 3)


            "\"Please take off your shirt.\"" if luna_dom >= luna_sub:
                $ luna_choice = 3
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("well seeing as how you asked so {i}nicely{/i}...", 6, 1, 1, 1)
                m "thank you [luna_name]."
                call luna_main("(I can't believe people think that this is the greatest wizard ever...)", 7, 2, 1, 1) 
                call luna_main("close your eyes...", 8, 1, 2, 1) 
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_panties = False
                $ luna_wear_bra = False
                $ luna_wear_skirt = False
                $ luna_wear_top = False
                ">you can hear the soft ruffle of clothes being removed..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "you can open then when I tell you..."
                ">You hear her softly place something on the table..."
                lun "..."
                m "..."
                lun "Alright, go ahead."
                show screen luna
                hide screen blkfade
                with d3 

            "\"Please take off your skirt [luna_name]...\"" if luna_dom >= 5:
                $ luna_choice = 4
                call luna_main("...", 5, 2, 1, 1)
                call luna_main("......", 8, 2, 2, 1)
                call luna_main("well seeing as how you said the magic word I suppose it's only fair...", 6, 1, 1, 1)
                m "thank you [luna_name]."
                call luna_main("(I've got him wrapped around my finger...)", 7, 2, 1, 1) 
                call luna_main("well... close your eyes...",8, 1, 2, 2)
                hide screen luna
                show screen blkfade
                with d3
                $ luna_wear_panties = False
                $ luna_wear_bra = False
                $ luna_wear_skirt = False
                $ luna_wear_top = False
                ">you can hear the soft ruffle of clothes and zips..."
                m "..."
                m "Can I open my eyes yet [luna_name]?"
                lun "wait..."
                m "..."
                ">You hear her softly place something on the table..."
                lun "Alright, you can open them now..."
                show screen luna
                hide screen blkfade
                with d3 

        if luna_choice <= 2: #luna sub choices
            if luna_sub <= 6:
                $ luna_sub += 1
            m "I am. And I expect you to do it now, [luna_name]."
            call luna_main("[l_genie_name]... please...", 5, 1, 4, 2)
            m "Hmmm, well seeing as how I'm in a generous mood how about we make another deal?"
            call luna_main("...", 7, 2, 4, 2)
            $ luna_tears = 0
            call luna_main("Really? What sort?", 7, 2, 4, 2)
            m "what's the closest school to Howgsmorts?"
            call luna_main("?...{p}Um, probably Beauxbatons Academy of Magic [l_genie_name]...", 5, 2, 4, 2)
            m "Well, how about I send a glowing letter of recommendation to them concerning your father's magazine?"
            m "I'm sure that will probably boost sales."
            call luna_main("Really sir? You'd do that?", 4, 1, 1, 1) 
            call luna_main("And all I have to do is stand here and...", 5, 2, 4, 2) 
            if luna_wear_skirt == False:
                call luna_main("take off my top...", 7, 3, 4, 2) 
                m "and your bra."
            else:
                call luna_main("take off my skirt...", 7, 3, 4, 2) 
                m "and your panties."
            call luna_main("......", 8, 1, 4, 2)
            call luna_main("..........", 9, 2, 4, 2)
            call luna_main("Alright... but you have to close your eyes...", 9, 1, 4, 2)
            m "Done."
            hide screen luna
            hide screen luna_chibi
            show screen blkfade
            with d3
            $ luna_wear_panties = False
            $ luna_wear_bra = False
            $ luna_wear_skirt = False
            $ luna_wear_top = False
            ">You hear the soft rustle of clothes..."
            ">Suddenly something is gently placed on your desk"
            $ luna_chibi("stand_naked")
            show screen luna
            show screen luna_chibi
            hide screen blkfade
            with d3
            call luna_main("......", 8, 3, 4, 2)
            g9 "looking good [luna_name]!"
            g9 "So good in fact I think I need a closer look!"
            ">You stand up and walk in front of luna, towering over her."
            hide screen bld1
            hide screen genie
            show screen chair_02
            show screen desk_02
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "groping_ass_ani"
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            pause
            m "mmmm"
            call luna_main("......", 8, 2, 4, 2)
            menu:
                "-Grab her tits!-":
                    $ current_payout = 40
                    show screen blkfade
                    hide screen genie
                    $ genie_chibi_xpos = 40
                    $ genie_chibi_ypos = 10
                    $ g_c_u_pic = "groping_ass_ani"
                    show screen g_c_u
                    with fade
                    ">You reach out swiftly and grab both of her creamy tits..."
                    hide screen blkfade
                    call luna_main("!!!", 4, 1, 3, 3)
                    ">YOu start gently kneading her breasts."
                    m "Mmmm that's it [luna_name]..."
                    call luna_main("{size=-5}(What is he doing?){/size}", 9, 2, 4, 2)
                    call luna_main("[l_genie_name] you really have to stop... ", 8, 1, 4, 3)
                    if daytime:
                        m "Come on [luna_name], just a little more then you'll be off to class."
                    else:
                        m "Come on [luna_name], just a little more then you'll be off to bed."
                    $ luna_tears = 2
                    call luna_main("[l_genie_name]... no...", 9, 3, 4, 2)
                    call luna_main("(I should stop him...)", 9, 2, 4, 2)   
                    call luna_main("(before he gets too excited...)", 9, 3, 4, 2) 
                    ">Luna pushes shoves you back."
                    call luna_main("......", 9, 1, 4, 2)
                    ">You let her go and tack a step back."
                    $ genie_chibi_xpos = 20
                    call luna_main("...", 9, 3, 4, 3)
                    m "Sorry..."
                    call luna_main("It-it's alright [l_genie_name]...", 9, 2, 4, 2)
                    call luna_main("You just got a little over excited...", 9, 3, 4, 2)
                    call luna_main("Just, please, try and control yourself next time...", 9, 2, 4, 1)
                    g9 "With tits like that I'm not so sure!"
                    call luna_main("...", 9, 2, 4, 2)


                "-start touching yourself-"if luna_choice == 1:
                    $ current_payout = 100
                    m "mmmm..."
                    call luna_main("......", 8, 1, 4, 2)
                    hide screen blktone
                    show screen blkfade
                    with d3
                    ">You reach into your robe and pull out your cock..."
                    ">You spit on your hand to lube it before you start stroking..."
                    hide screen genie
                    $ genie_chibi_xpos = -20
                    $ genie_chibi_ypos = 10
                    $ g_c_u_pic = "jerking_off_02_ani"
                    show screen g_c_u
                    hide screen blkfade
                    with fade
                    call luna_main("!!!", 4, 1, 3, 3)
                    call luna_main("(Am I just going to let him do this?)", 9, 2, 2, 3)
                    call luna_main("Sir I really thin-", 8, 1, 2, 3)
                    m "Shhhh..."
                    ">You start stroking faster."
                    call luna_main("...", 5, 2, 4, 3)
                    call luna_main("(I can't just let him...)", 6, 3, 4, 3)
                    m "Yes... Ah, yes, this is good..."
                    $ luna_tears = 2
                    call luna_main("sir... please... don't...", 6, 3, 4, 3)
                    m "I said shhhh [luna_name]..."
                    call luna_main("Sir... I-I'll leave if y-you don't stop...", 6, 2, 4, 3)
                    m "If you leave, you can say goodbye to the squibbler or whatever it's called."
                    call luna_main("(I can't do that to daddy...)", 7, 3, 4, 3)
                    call luna_main("Fine! I hope your happy!", 7, 1, 4, 3)
                    call luna_main("enjoy stroking that filthy old cock while you force me stand here...", 7, 3, 4, 3)
                    g9 "{size=-4}(mmmm... yes...){/size}"
                    g9 "Oh I am!"
                    call luna_main("*hmph*...", 7, 1, 2, 2)
                    ">Luna tosses her hair over her shoulder in frustration."
                    call luna_main("You're disgusting...", 7, 3, 3, 2)
                    ">You keep on wanking while you gaze at Luna's milky tits..."
                    m "mmmm that's it [luna_name]..."
                    $ luna_tears = 3
                    call luna_main("*hmph*... just hurry up get it over with [l_genie_name]...", 6, 3, 4, 3)
                    call luna_main("I'm sick of looking at that... thing...", 7, 2, 4, 2)
                    m "{size=-4}ah...{/size}"
                    m "that's it slut... keep looking..."
                    call luna_main("Professor!", 8, 3, 2, 2)
                    m "{size=-4}(argh... yes...){/size}"
                    call luna_main("I really don't-", 5, 3, 4, 2)
                    m "{size=-4}yes...{/size}"
                    call luna_main("-think that-", 9, 3, 4, 3)
                    g4 "{size=+2}mmmm... thats it keep going...{/size}"
                    call luna_main("-we should be-", 5, 3, 4, 1)
                    g4 "{size=+4}(agh... almost there...){/size}"
                    call luna_main("doing thi-", 9, 3, 4, 1)
                    g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
                    $ genie_cum_chibi_xpos = -20
                    $ genie_cum_chibi_ypos  = 10
                    $ g_c_c_u_pic = "genie_cum_03" 
                    show screen g_c_c_u
                    $ luna_wear_cum = True
                    $ luna_cum = 5
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
                    show screen bld1
                    with d3
                    $ g_c_u_pic = "jerking_off_02_ani"
                    hide screen g_c_c_u
                    call luna_main("ugh... there's so much...", 8, 3, 4, 2)
                    call luna_main("{size=-5}(I can't believe this...){/size}", 8, 2, 4, 2)
                    call luna_main("ugh... {size=-5}(it stinks as well...){/size}", 8, 3, 2, 2)
                    with d3
                    g4 "argh... good work, slut... ah, shit, this feels so good..."
                    show screen genie
                    hide screen bld1
                    hide screen g_c_u
                    #show screen genie_jerking_off
                    with d3
                    call luna_main("......", 7, 1, 4, 2)
                    m "Ah... you did good [luna_name]..."

            hide screen luna
            show screen blkfade
            with d3
            show screen genie
            hide screen g_c_u
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            $ luna_cum = 2
            hide screen chair_02
            hide screen desk_02
            ">Luna quickly picks her clothes up off your desk and gets dressed, putting on her shirt over the cum."
            show screen luna
            hide screen blkfade
            with d3
            call luna_main("I think I'd like to leave now [l_genie_name]...", 7, 3, 4, 2)
            m "You're free to leave whenever you like [luna_name]."
            call luna_main("Well I'm certainly not leaving until you pay me!", 9, 1, 2, 3)


        else:
            call luna_main("...", 7, 1, 1, 1) 
            $ luna_chibi("stand_naked")
            pause
            g9 "mmmm"
            if luna_dom <= 5:
                $ luna_dom += 1
            call luna_main("Like what you see [l_genie_name]?", 5, 2, 1, 1) 
            g9 "Yes... Yes..."
            call luna_main("well... why don't you come take a closer look?...", 5, 1, 2, 1)
            m "what?"
            call luna_main("why don't you stand up and take a good look [l_genie_name]...", 8, 1, 3, 1)
            m "I don't think that-"
            call luna_main("shhh...", 9, 1, 2, 14)
            call luna_main("just stand up sir.....", 7, 1, 2, 1)
            m "..."
            ">You stand up and walk in front of luna, feeling the pressure of her gaze."
            hide screen bld1
            hide screen genie
            show screen chair_02
            show screen desk_02
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "01_hp/08_animation_02/06_groping_01.png" 
            show screen g_c_u
            with fade
            hide screen blktone
            hide screen blkfade
            with d5
            pause
            call luna_main("there we are...", 8, 1, 4, 1)
            call luna_main("Isn't that better?", 8, 2, 4, 1)
            m "mmmm... yes..."
            call luna_main("Hmmm, that's it just keep looking...", 8, 2, 3, 1)
            ">Luna gives her tits a little shake."
            g9 "!!!"
            call luna_main("See something you like?...", 9, 2, 4, 1)
            m "ah, gods yes..."
            call luna_main("mmmmm... why don't you take it out [l_genie_name]...", 9, 1, 4, 1)
            m "..."
            call luna_main("be a good boy....", 5, 1, 4, 1)
            show screen blkfade
            ">You take your cock out and start stroking it..."
            hide screen genie
            $ genie_chibi_xpos = -20
            $ genie_chibi_ypos = 10
            $ g_c_u_pic = "jerking_off_02_ani"
            show screen g_c_u
            hide screen blkfade
            with fade
            call luna_main("that's it [l_genie_name]...", 9, 1, 4, 1)
            ">you stare at her soft milky tits..."
            m "Mmmm..."
            call luna_main("Mmmm, isn't that better?", 9, 2, 4, 1)
            g9 "yes..."
            ">You start stroking your cock with renewed vigor."
            call luna_main("Aren't you keen today?", 8, 1, 2, 1)
            g9 "Aha... Yeah... This really great..."
            call luna_main("good... make sure you work up a nice big load for me...", 9, 1, 2, 1)
            call luna_main("if you're a really good boy I might even let you shoot it... on me...", 5, 2, 4, 1)
            g9 "Yes!"
            call luna_main("I bet you'd love that wouldn't you?", 7, 1, 2, 1)
            g9 "gods yes..."
            call luna_main("Shooting your filthy old cum all over me...", 9, 3, 2, 1)
            g9 "!!!"
            call luna_main("come on then [l_genie_name]...", 9, 1, 2, 1)
            call luna_main("stroke it faster...", 5, 1, 4, 1)
            m "{size=-4}(argh... yes...){/size}"
            call luna_main("get that nasty cum ready for me...", 8, 1, 3, 1)
            m "{size=-4}yes...{/size}"
            call luna_main("mmm...", 8, 1, 3, 1)
            m "{size=+2}yes...{/size}"
            call luna_main("you really love this don't you...", 9, 1, 2, 1)
            g4 "{size=+4}(agh...){/size}"
            ">you start stroking your cock even faster!"
            g4 "{size=+4}yes...{/size}"
            call luna_main("Is this why you became a teacher...", 9, 1, 4, 1)
            call luna_main("Just to cover young students in your filthy cum...", 5, 1, 2, 1)
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            call luna_main("well?", 9, 1, 4, 1)
            g4 "{size=+4}(agh... almost there...){/size}"
            call luna_main("do it...", 7, 1, 2, 1)
            call luna_main("{size=+4}cum all over me!{/size}", 7, 1, 2, 11)
            g4 "{size=+4}(YES! YES! YES!) *Argh!*{/size}"
            $ genie_cum_chibi_xpos = -20
            $ genie_cum_chibi_ypos  = 10
            $ g_c_c_u_pic = "genie_cum_03" 
            show screen g_c_c_u
            $ luna_wear_cum = True
            $ luna_cum = 5
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
            call luna_main("...", 5, 3, 1, 1)
            g4 "Argh! YES!"
            hide screen luna
            with d3
            hide screen bld1
            with d3
            show screen bld1
            with d3
            $ g_c_u_pic = "jerking_off_02_ani"
            hide screen g_c_c_u
            hide screen bld1
            call luna_main("That's it, [l_genie_name], make sure you cover me...", 9, 1, 3, 1)
            show screen genie_jerking_sperm_02
            with d3
            g4 "ah, shit... ah... this is too good..."
            call luna_main("mmm...", 8, 1, 3, 1)
            m "ah..."
            call luna_main("keep going... make sure you get every last drop out.", 8, 3, 4, 1)
            m "ah... Thank you..."
            call luna_main("Good boy...", 5, 2, 2, 1)
            call luna_main("Well seeing as how you've ...finished... I suppose I better get dressed.", 7, 2, 2, 2)

            hide screen luna
            with d3
            ">Luna quickly picks her clothes up off your desk and gets dressed, putting her shirt on over her cum covered chest."
            $ luna_wear_skirt = True
            $ luna_wear_top = True
            $ luna_wear_bra = True
            $ luna_wear_panties = True
            $ luna_cum = 2
            show screen genie
            hide screen chair_02
            hide screen desk_02
            hide screen g_c_u
            show screen luna
            with d3
            m "That was... amazing"
            call luna_main("I'm glad you enjoyed yourself...", 1, 1, 1, 1)
            m "I have to ask though. why did you-"
            call luna_main("Do this?", 5, 2, 2, 2)
            m "yes."
            call luna_main("Don't worry about that...", 8, 1, 2, 1)
            call luna_main("THe only thing you have to worry about...", 7, 1, 2, 1)
            ">She runs her finger down the front of her shirt."
            call luna_main("Is keeping that cock of yours in check...", 7, 3, 2, 1)
            m "What?"
            call luna_main("I know you're probably leering after some other students sir...", 9, 1, 3, 1)
            call luna_main("But if I find out that you've buying favours from other students.", 9, 2, 1, 1)
            call luna_main("well...", 9, 1, 1, 1)
            m "..."
            call luna_main("let's just say I wouldn't let that happen if I were you...", 9, 2, 1, 1)
            call luna_main("Now forget about that, let's discuss payment. 100 gold sounds fair to me... {p}how about you?", 9, 1, 2, 1)
            m "It sounds... surprisingly fair..."
            call luna_main("I'm glad we could come to a happy agreement.", 8, 2, 4, 1)
            m "yes [luna_name]..."
            call luna_main("Good boy... now, speaking of payment...", 9, 1, 2, 2)
            $ current_payout = 100







    hide screen bld1
    if luna_dom >= luna_sub:
        m "Alright, alright. Here's your gold."
    else:
        m "well then, Here's your payment [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    if current_payout <= 40:
        call luna_main("(only [current_payout]?) *hmph*", 8, 2, 2, 3) 
        call luna_main("Thank you, [l_genie_name].", 6, 2, 2, 2)   
    else:
        call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
    ">Luna leaves your office."  
    $ luna_wear_cum = False
    hide screen genie_jerking_sperm_02    

    jump luna_away




label luna_favour_4: ###Luna handjob
    m "{size=-4}(I'll just ask for a quick tug...){/size}"
    if luna_corruption <= 10: #FIRST TIME - Change this to 10 when part 2 added
        if luna_corruption <= 10:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "[luna_name]?"
        call luna_main("yes [l_genie_name]...", 1, 2, 2, 2) 
        m "Would it be possible for me to buy another favour..."
        call luna_main("...", 7, 2, 2, 2) 
        call luna_main("Go on...", 7, 2, 2, 2) 
        menu:
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
                m "give me a handjob..."
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
        m "ugh... Yes, that's it..."
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
                m "Ah..."
                call luna_main("What's wrong?", 7, 1, 5, 2) 
                m "Well if you go that fast the friction's a little painful."
                call luna_main("Really?...", 8, 1, 2, 1) 
                ">Luna doesn't slow down. If anything she speeds up slightly."
                g9 "Ah!"
                call luna_main("...", 9, 1, 3, 1) 
                g9 "[luna_name]..."
                call luna_main("Hmmm, do You want me to spit on your cock then?", 5, 1, 5, 1) 
                g9 "Just a little bit..."
                call luna_main("...", 5, 1, 2, 1) 
                call luna_main("......", 5, 1, 3, 1) 
                g9 "Please..."
                call luna_main("Good boy.", 7, 1, 2, 1) 
                call luna_main("*Ptew*", 5, 8, 2, 16) 
                ">Luna spits into her hand before placing it back on your cock."
        g4 "Mmmm, yes that's it [luna_name]..."
        call luna_main("...", 7, 8, 2, 1) 
        g4 "Just keep pumping those hands up and down."
        call luna_main("......", 8, 1, 3, 1) 
        if luna_choice == 1:
            ">Luna gently starts shaking her boobs as she jerks you off."
        else:
            call luna_main("*Ptew*", 8, 8, 3, 16) 
            ">Luna spits into her hand again and places it back on your cock."
        ">She then starts pumping your cock even faster."
        g4 "Gods yes..."
        g4 "(This is it, where should I cum?)"
        menu:
            "-On her face-":
                ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

            "-On her tits-":
                ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

        call luna_main("[l_genie_name]!!!", 7, 1, 3, 6) 
        call luna_main("You're not trying to cum on me are you?", 8, 1, 3, 3) 
        g4 "Ah [luna_name], I'm almost there."
        call luna_main("Well...", 9, 8, 3, 3) 
        $ luna_wear_skirt = False
        ">Luna quickly pulls down her skirt."
        g4 "!!!"
        call luna_main("You cum...", 8, 1, 3, 3) 
        g4 "Ah..."
        ">Luna slowly pulls her panties forward, exposing her pussy to the air."
        ">Her right hand is still wrapped around your cock as she pumps it with blinding speed."
        call luna_main("Where I tell you...", 9, 1, 3, 3) 
        g4 "mmmm"
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
        g4 "Argh! by the gods {size=+10}YES!{/size}"
        call luna_main("...", 5, 3, 1, 1)
        call luna_main("(It's so warm...)", 5, 2, 4, 1)
        g4 "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
        g4 "mmmm....."
        hide screen g_c_c_u
        $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png"
        $ luna_r_arm = 2
        hide screen genie_sprite
        with d3
        m "That hit the spot..."
        call luna_main("({image=textheart}{image=textheart}{image=textheart})", 5, 8, 4, 1)
        call luna_main("[l_genie_name]!", 8, 1, 3, 1)
        call luna_main("How could you! Cumming on your students {size=-10}pussy{/size}...", 7, 8, 2, 1)
        m "Ahh... that was fantastic slut..."
        $ g_c_u_pic = "01_hp/08_animation_02/06_groping_01.png"
        call luna_main("[l_genie_name]...", 6, 2, 2, 1)

    else: #last time event is run before cum addict variant
        if luna_corruption <= 11:
            $ luna_corruption += 1
        play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1 
        m "[luna_name]?"
        call luna_main("yes [l_genie_name]...", 1, 2, 2, 2) 
        m "Would it be possible for me to buy another favour..."
        call luna_main("I think I know what you want...", 7, 2, 2, 1) 
        call luna_main("but why don't you ask me anyway...", 5, 1, 1, 1) 
        call luna_main("you know I like to hear you beg.", 8, 1, 3, 1) 
        menu:
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
                m "give me a handjob..."
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
        call luna_main("Hmph... you wish [l_genie_name]!", 8, 1, 2, 1) 
        m "..."
        ">Luna starts moving her hand back and forth along the length of your cock."
        m "ugh... Yes, that's it..."
        call luna_main("(He loves this...)", 6, 3, 3, 3) 
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
                call luna_main("well, seeing as how you're being such a good boy...", 8, 3, 2, 1) 
                $ luna_wear_bra = False
                $ luna_r_arm = 2
                $ luna_l_arm = 2
                ">Luna slowly removes her bra before placing her hand back on your cock."
                $ luna_r_arm = 3
                $ luna_l_arm = 1
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
                m "Ah..."
                call luna_main("mmmm, hurts doesn't it.", 7, 3, 2, 1) 
                m "yes..."
                call luna_main("Really?...", 8, 1, 2, 1) 
                ">Luna doesn't slow down. If anything she speeds up slightly."
                g9 "Ah! yes!"
                call luna_main("...", 9, 1, 3, 1) 
                g9 "[luna_name]..."
                call luna_main("Hmmm, do You want me to spit on your cock then?", 5, 1, 5, 1) 
                g9 "yes... please [luna_name]..."
                call luna_main("Good boy.", 7, 1, 2, 1) 
                call luna_main("*Ptew*", 5, 8, 2, 16) 
                ">Luna spits into her hand before placing it back on your cock."
        g4 "Mmmm, yes that's it [luna_name]..."
        call luna_main("...", 7, 8, 2, 1) 
        g4 "Just keep pumping those hands up and down."
        call luna_main("......", 8, 1, 3, 1) 
        if luna_choice == 1:
            ">Luna gently starts shaking her boobs as she jerks you off."
        else:
            call luna_main("*Ptew*", 8, 8, 3, 16) 
            ">Luna spits into her hand again and places it back on your cock."
        ">She then starts pumping your cock even faster."
        g4 "Gods yes..."
        g4 "(This is it, where should I cum?)"
        menu:
            "-On her face-":
                ">You place your hand on the top of Luna's head and slowly try to force it down to be level with your crouch."

            "-On her tits-":
                ">You place your hand on the top of Luna's should and slowly try to force her down to be level with your crouch."

        call luna_main("[l_genie_name]!!!", 7, 1, 3, 6) 
        call luna_main("You're not trying to cum on me are you?", 8, 1, 3, 3) 
        g4 "Ah [luna_name], I'm almost there!"
        call luna_main("Well...", 9, 8, 3, 3) 
        $ luna_wear_skirt = False
        $ luna_wear_bra = False
        $ luna_wear_skirt = False
        $ luna_wear_skirt = False
        ">Luna quickly strips, all while keeping a firm grip of your cock.."
        g4 "hurry up! You'll ruin the damn moment!"
        call luna_main("well, pick...", 8, 1, 3, 3) 
        g4 "you mean..."
        ">Leans forward slowly while ever so slithery jiggling her milky boobs."
        ">Her right hand is still wrapped around your cock as she pumps slowly, keeping you at the edge."
        call luna_main("pick where you want...", 9, 1, 3, 3) 
        g4 "Ah yes!"
        call luna_main("you can pick my boobs...", 8, 1, 3, 2) 
        ">She gives them another shake."
        call luna_main("or my thighs...", 5, 1, 2, 1) 
        ">She rubs them together as she rotates on the balls of her feet."
        call luna_main("boobs are an extra 100...", 5, 1, 2, 1) 
        call luna_main("thighs are 50...", 5, 1, 2, 1) 
        g4 "Ah{size+=2} here {size+=2}it {size+=2}is!{/size}"
        menu:
            "-boobs-":
                $ current_payout += 100 
                $ g_c_c_u_pic = "jerking_off_cum_ani"
                show screen g_c_c_u
                $ luna_cum = 5
                show screen white 
                pause.1
                hide screen white
                pause.2
                show screen white 
                pause .1
                hide screen white
                with hpunch
                ">You start shooting your load across her chest, coating her tits in cum."

            "-thighs-":
                $ current_payout += 50 
                $ g_c_c_u_pic = "jerking_off_cum_ani"
                show screen g_c_c_u
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

            "-{size=+10}FACE!{/size}-":
                jump luna_cum_addict_event
        g4 "Argh! by the gods {size=+10}YES!{/size}"
        call luna_main("...", 5, 3, 1, 1)
        call luna_main("(It's so warm...)", 5, 2, 4, 1)
        g4 "{size=+10}TAKE IT ALL YOU big titted sLUT!{/size}"
        g4 "mmmm....."
        hide screen g_c_c_u
        $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png"
        $ luna_r_arm = 2
        hide screen genie_sprite
        with d3
        m "That hit the spot..."
        call luna_main("({image=textheart}{image=textheart}{image=textheart})", 5, 8, 4, 1)
        call luna_main("[l_genie_name]!", 8, 1, 3, 1)
        call luna_main("How could you! Cumming on your students {size=-10}pussy{/size}...", 7, 8, 2, 1)
        m "Ahh... that was fantastic slut..."
        $ g_c_u_pic = "01_hp/08_animation_02/06_groping_01.png"
        call luna_main("[l_genie_name]...", 6, 2, 2, 1)

    hide screen bld1
    m "well then, Here's your payment [luna_name]."
    $ gold -= current_payout
    $ luna_gold += current_payout
    ">You hand Luna [current_payout] gold."
    call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)  
    ">Luna leaves your office."  
    $ luna_wear_cum = False
    $ luna_wear_cum_under = False

    hide screen g_c_u
    show screen genie
    hide screen chair_02
    hide screen desk_02

    jump luna_away








label luna_favour_5: #Luna jerks Genie off onto Hermione's face
    m "[luna_name], how would you feel about selling another favour?"
    call luna_main("...", 6, 2, 2, 1)
    call luna_main("What is it this time [l_genie_name]?", 6, 2, 2, 1)
    m "Well, do you remember how we had a little fun with miss granger the other day?"
    call luna_main("...", 6, 2, 2, 1)
    call luna_main("go on...", 6, 2, 2, 1)
    m "how would you feel about bringing her up her for a little more fun?"
    call luna_main("You really are a disgusting pervert aren't you?", 6, 2, 2, 1)
    m "..."
    call luna_main("Aren't you...", 6, 2, 2, 1)
    m "Yes..."
    call luna_main("at least you're honest about it...", 6, 2, 2, 1)
    call luna_main("Which is more than I can say for that two-faced slut hermione...", 6, 2, 2, 1)
    m "So you're OK with having a little fun with her?"
    call luna_main("on one condition.", 6, 2, 2, 1)
    m "Name it."
    call luna_main("I'm in control. No matter what.", 6, 2, 2, 1)
    call luna_main("Even if you think what's happening is too mean...", 6, 2, 2, 1)
    call luna_main("I am in control... got it?", 6, 2, 2, 1)
    m "Done."
    call luna_main("alright then...", 6, 2, 2, 1)
    call luna_main("I also expect to be paid 150 gold for my troubles...", 6, 2, 2, 1)
    m "Certainly."
    call luna_main("...", 6, 2, 2, 1)
    call luna_main("Now [l_genie_name]...", 6, 2, 2, 1)
    m "Alright then..."
    ">You pay Luna 150 gold."
    $ gold -=150 
    $ luna_gold += 150
    call luna_main("thank you [l_genie_name]...", 6, 2, 2, 1)
    call luna_main("...", 6, 2, 2, 1)
    call luna_main("Well come on then, summon her...", 6, 2, 2, 1)
    ">You summon Hermione. Somehow..."
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 600 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    $ luna_flip = -1
    $ luna_r_arm = 2
    $ luna_xpos = 300
    call update_her_uniform
    pause
    call her_main("hello Prof-","body_122")
    call her_main("Luna! what are you doing here?","body_122")
    call luna_main("same thing as you...", 6, 2, 2, 1)
    call her_main("Oh, um... you must be here to... help Professor dumbledore then...","body_122")
    call luna_main("Mhmmm...", 6, 2, 2, 1)
    call her_main("So, ugh... what does dumbledore need our help with?","body_122")
    call luna_main("Probably emptying those nasty balls of his...", 6, 2, 2, 1)
    call her_main("!!!","body_122")
    call her_main("Luna! what are you talking about?","body_122")
    call her_main("are you feeling ok?","body_122")
    call luna_main("come on now hermione... it wouldn't be the first time you've helped old dumbledore like this?", 6, 2, 2, 1)
    call luna_main("would it...?", 6, 2, 2, 1)
    call her_main("I have no idea what you're talking about!","body_122")
    call her_main("Professor dumbledore must be mistaken...","body_122")
    call her_main("M-Maybe he needs to go to the nurses and have his mind checked...","body_122")
    call luna_main("So you're not selling favours to dumbledore in exchange for points?", 6, 2, 2, 1)
    call her_main("certainly not! I'd never do something so underhanded!","body_122")
    call luna_main("Really?", 6, 2, 2, 1)
    call her_main("Of course not! I'm shocked you even have to ask!","body_122")
    call luna_main("So you're comfortable saying that after you've had a sip of some veritaserum?", 6, 2, 2, 1)
    call her_main("!!!","body_122")
    call her_main("O-O-Of course... but as you know, that potion's banned...","body_122")
    call luna_main("Not for the illustrious Professor dumbledore!", 6, 2, 2, 1)
    call luna_main("Isn't that right sir?", 6, 2, 2, 1)
    m "Oh, um yes of course I can get that easily..."
    m "(What the hell is veribatium?)"
    call her_main("!!!","body_122") #angry face
    call her_main("surely you know there's no need for that sir!","body_122") #angry face
    m "..."
    call her_main("...","body_122") 
    call luna_main("...", 6, 2, 2, 1)
    call her_main("Fine! I admit it!","body_122") 
    call luna_main("See... Isn't it better to tell the truth?", 6, 2, 2, 1)
    call her_main("...","body_122")
    call her_main("So is that why I've been brought here? To be ridiculed!?","body_122") 
    call her_main("I'm not ashamed of what I've done for my house!","body_122")
    call luna_main("No, you've been brought here to sell dumbledore a favour.", 6, 2, 2, 1)
    call her_main("What?","body_122")
    call her_main("Why are you here then?","body_122")
    call luna_main("To help you.", 6, 2, 2, 1)
    call her_main("...","body_122")
    call her_main("Help how?","body_122")
    call luna_main("Why don't you take your clothes off and I'll show you...", 6, 2, 2, 1)
    call her_main("[genie_name]... please...","body_122")
    m "I'm sorry [hermione_name], my hands are tied..."
    call her_main("...","body_122")
    call her_main("Do I have to?","body_122")
    call luna_main("Of course not... So long as you don't mind me telling your precious \"MRM\" what's been going on.", 6, 2, 2, 1)
    call her_main("...","body_122")
    call her_main("FINE!","body_122", "tears_02")
    call her_main("I see how it is!","body_122", "tears_02")
    ">Hermione pulls off her top in a huff."
    $ hermione_wear_top = False
    $ hermione_wear_bra = False
    call her_main("Feel free to humiliate me!","body_122", "tears_02")
    ">Hermione angrly removes her skirt."
    $ hermione_wear_skirt = False
    $ hermione_wear_panties = False
    call her_main("for trying to do what's right!","body_122", "tears_02")
    ">Hermione stands naked before you and Luna. Her face is contorted in what seems like an equal mix of rage and embarrassment."
    call her_main("there! are you happy now you two?","body_122", "tears_02")
    m "Ye-"
    call luna_main("almost...", 6, 2, 2, 1)
    call luna_main("now why don't you get on your knees...", 6, 2, 2, 1)
    call her_main("!!!","body_122", "tears_02")
    call her_main("please, luna... I'm {size=-2}sorry {size=-2}about {size=-2}what I said...{/size}","body_122", "tears_02")
    call luna_main("then kneel...", 6, 2, 2, 1)
    hide screen hermione_main 
    $ hermione_SC.chibi.xpos = 40 #40 = Near Luna
    $ hermione_SC.chibi.ypos = 60
    $ h_c_u_pic = "01_hp/16_hermione_chibi/dance/08_sits.png"
    $ hermione_head_xpos=390
    show screen h_c_u 
    with d3
    call her_kneel("...","body_122")
    call luna_main("there... isn't this simpler?", 6, 2, 2, 1)
    call her_kneel("...","body_122", "blush")
    call luna_main("now... I'll need your help for this next bit Professor.", 6, 2, 2, 1)
    m "What do I need to do?"
    call luna_main("come and stand before your star student.", 6, 2, 2, 1)
    ">You get up out of your chair and walk over to the two girls."
    hide screen bld1
    hide screen genie
    show screen chair_02
    show screen desk_02
    $ genie_chibi_xpos = -20
    $ genie_chibi_ypos = 10
    $ g_c_u_pic = "01_hp/08_animation_02/06_jerking_01.png"
    show screen g_c_u
    with fade
    hide screen blktone
    hide screen blkfade
    with d5
    pause
    ">Hermione looks up at you with a pleading expression."
    call her_kneel("[genie_name]... please... what's going on?","body_122", "blush")
    call luna_main("I said that you're here to sell a favour.", 6, 2, 2, 1)
    call luna_main("Isn't that you want? To sell favours to dumbledore?", 6, 2, 2, 1)
    call her_kneel("I want... I want \"gryffindor\" to win the house cup...","body_122", "blush")
    if gryffindor > slytherin:
        call luna_main("But \"gryffindor\" is already ahead by [gryffindor-slytherin] points...", 6, 2, 2, 1)
        call luna_main("do you really think that they need any more points to win?", 6, 2, 2, 1)
        call her_kneel("they wouldn't understand...","body_122", "blush")
    else:
        call luna_main("do you really think it's fair for you to win by selling your body?", 6, 2, 2, 1)
        call luna_main("*tch* *tch* *tch* what would your parents think?", 6, 2, 2, 1)
        call her_kneel("they wouldn't understand...","body_122", "blush")
    ">Luna puts her hand in your robes and quickly pulls out your hardening cock."
    $ luna_r_arm = 3
    $ luna_flip = 1
    $ luna_xpos = 640
    $ hermione_head_xpos = 390
    $ hermione_head_ypos = 390
    $ genie_sprite_xpos = 550
    call gen_main("!!!", 4, 2)
    call luna_main("Just admit it...", 6, 2, 2, 1)
    call luna_main("you're a slut...", 6, 2, 2, 1)
    call her_kneel("{size=-5}no... I'm... a good student...{/size}","body_122", "blush")
    ">Luna starts sliding her smooth hand up and down your cock."
    call luna_main("hmmmm... I'm not so sure a good student would do this...", 6, 2, 2, 1)
    call her_kneel("...","body_122", "blush")
    call luna_main("kneel willingly in front of their headmaster..", 6, 2, 2, 1)
    call her_kneel("...","body_122", "blush")
    call luna_main("naked...", 6, 2, 2, 1)
    call her_kneel("...","body_122", "blush")
    call luna_main("While another student jerks him off...", 6, 2, 2, 1)
    call her_kneel("...","body_122")
    call luna_main("Waiting patiently to be covered in cum...", 6, 2, 2, 1)
    call her_kneel("{image=textheart}{image=textheart}{image=textheart}","body_122")
    call luna_main("in fact, I can think of only one sort of student who'd do that...", 6, 2, 2, 1)
    call luna_main("do you know what sort of student that is hermione?", 6, 2, 2, 1)
    call her_kneel("ah...{image=textheart} a...","body_122")
    call luna_main("Mhmmm, go on...", 6, 2, 2, 1)
    call her_kneel("ah... {p}a slut...{image=textheart}","body_122")
    call luna_main("good girl...", 6, 2, 2, 1)
    call her_kneel("{image=textheart}{image=textheart}{image=textheart}","body_122")
    m "Ah... almost there [luna_name]..."
    ">Luna gives your cock a hard squeeze."
    g9 "Ah!"
    call luna_main("not yet old man!", 6, 2, 2, 1)
    call luna_main("she hasn't learnt her lesson yet!", 6, 2, 2, 1)
    m "What else does she need to do?"
    call luna_main("...", 6, 2, 2, 1)
    call luna_main("Lick it...", 6, 2, 2, 1)
    call her_kneel("...","body_122")
    call her_kneel("OK...","body_122", "blush")
    ">Hermione opens her mouth and puts out her tongue, closing her eyes."
    call her_kneel("ah...","body_135", "blush")
    call luna_main("...", 6, 2, 2, 1)
    call luna_main("seems like I have to do everything then...", 6, 2, 2, 1)
    ">Luna pulls you forward, harshly, by your cock into Hermione's open mouth."
    g4 "!!!"
    $ luna_xpos += 45
    $ genie_sprite_xpos += 45
    $ luna_xpos += 10
    $ genie_sprite_xpos += 10
    $ hermione_kneel_cock = True
    call her_kneel("...","body_135")
    ">Hermione starts running her tongue along the length of your cock, lubricating it while Luna continues to stroke."
    g4 "Ah!!!"
    g4 "This is it sluts!"
    call luna_main("do it...", 6, 2, 2, 1)
    call her_kneel("mmmm...{image=textheart}{image=textheart}{image=textheart}","body_135")
    call luna_main("cover the slut...", 6, 2, 2, 1)
    g9  "Argh! by the gods {size=+10}YES!{/size}"
    $ luna_xpos -= 45
    $ genie_sprite_xpos -= 45
    $ luna_xpos -= 10
    $ genie_sprite_xpos -= 10
    $ hermione_kneel_cock = False
    g9  "{size=+10}TAKE IT ALL YOU sLUT!{/size}"
    show screen white 
    pause.1
    $ luna_r_arm = 4
    hide screen white
    pause.2
    $ uni_sperm = True
    $ u_sperm = "01_hp/13_hermione_main/auto_07.png"
    show screen white 
    pause .1
    hide screen white
    with hpunch
    $ luna_r_arm = 3
    ">You erupt over Hermione's face, coating her in a thick layer of spunk."
    call her_kneel("!!!!","body_122")
    g9 "{size=+10}YES!{/size}"
    call luna_main("mmmm, good girl...", 4, 1, 4, 8)
    ">Luna's hand slowly continues to stroke your cock, jerking out the last couple of drops of sperm onto Hermione's nose."
    call luna_main("perfect...", 4, 1, 4, 8)
    call her_kneel("...","body_122")
    m "that was fantastic!"
    hide screen genie_sprite
    with d3
    hide screen bld1
    show screen genie
    hide screen chair_02
    hide screen desk_02
    hide screen g_c_u
    call luna_main("...", 4, 1, 4, 8)
    $ luna_flip = -1
    $ luna_r_arm = 1
    $ luna_xpos = 300
    call luna_main("well it's not over yet...", 4, 1, 4, 8)
    call her_kneel("...what?","body_122")
    call her_kneel("why?","body_122")
    call luna_main("Just look at the mess you made!", 4, 1, 4, 8)
    call luna_main("You'll have to clean that up before you can go to class!", 4, 1, 4, 8)
    call her_kneel("well normally I just go the prefect bathroom...","body_122")
    call her_kneel("or I use a towel...","body_122")
    call her_kneel("{size=-5}but never scourgify for some reason...{/size}","body_122")
    call luna_main("And waste all that perfectly good cum the Professor gave you?!", 4, 1, 4, 8)
    call luna_main("No, I think I'll have to stay here and make sure you dispose of it properly...", 4, 1, 4, 8)
    call her_kneel("does that mean...","body_122")
    call luna_main("come on hermione, we don't have all day...", 4, 1, 4, 8)
    call luna_main("tranfiguration starts in 5 minutes...", 4, 1, 4, 8)
    call her_kneel("(I can't be late to mcgonagall's class...)","body_122")
    call luna_main("now dispose of that cum like a good little slut...", 4, 1, 4, 8)
    call her_kneel("...","body_122")
    ">Hermione slowly starts using her fingers to push your cum into her mouth."
    $ luna_l_arm = 4
    $ luna_cheeks = "01_hp/13_characters/luna/body/face/cheeks/cheeks_2.png"
    call luna_main("mmmmm... that's it... make sure you get it all slut...", 4, 1, 4, 8)
    m "(woah...)"
    ">Hermione slowly continues to clear her face of cum."
    $ u_sperm = "01_hp/13_hermione_main/auto_08.png"
    call her_kneel("...","body_125", "blush") #Cheek full
    ">She fills her mouth with cum before eventually swallowing."
    call her_kneel("*gulp*","body_126", "blush")
    ">Eventually she finally gets the last strand into her mouth."
    $ uni_sperm = False
    call her_kneel("...","body_125", "blush") #Cheek full
    call luna_main("see, good sluts don't waste anyting do they?", 4, 1, 4, 8)
    call her_kneel("...","body_125", "blush") #Cheek full
    $ luna_l_arm = 2
    call luna_main("Well, I better be off to... class...", 4, 1, 4, 8)
    call luna_main("Good bye [l_genie_name]...", 4, 1, 4, 8)
    call luna_main("Good bye slut...", 4, 1, 4, 8)
    ">Luna quietly exits the room."
    hide screen luna_chibi
    hide screen luna 
    with d3
    ">Hermione swallows the last mouthful of your cum."
    call her_kneel("*gulp*","body_126", "blush")
    call her_kneel("mmmm...{image=textheart}{image=textheart}{image=textheart}","body_123", "blush")
    ">She picks herself up from the floor gracefully. Getting dressed before turning to address you."
    $ hermione_wear_panties = True
    $ hermione_wear_skirt = True
    $ hermione_wear_top = True
    $ hermione_wear_bra = True
    $ hermione_SC.chibi.xpos = 500 #Near the desk: 400. (210 - standing on desk.)
    $ hermione_SC.chibi.ypos = 260#Default: 250. (180- standing on desk.)
    show screen hermione_blink #Hermione stands still.
    call update_her_uniform
    hide screen hermione_kneel 
    with d3
    call her_main("[genie_name], what on earth was that all about?!","body_122")
    call her_main("Why on earth was Luna in here?","body_122")
    call her_main("And how on earth does she know about me selling favours?","body_122")
    m "I can explain everything..."
    call her_main("Please do!","body_122")
    m "do you remember how you yourself described Luna lovegood as crazy?"
    call her_main("Of course. Everyone knows she's Loony Luna.","body_122")
    m "Well I was testing out some new magic..."
    m "And I'm attempting to cure her of her previous condition..."
    m "(I hope she believes this schlock...)"
    call her_main("Really?","body_122")
    call her_main("But isn't messing around with her mind a little...","body_122")
    call her_main("unethical?","body_122")
    m "Yes, well normally you'd be right, but this is more of a curing of an existing mental condition."
    m "Think about it like I'm trying to cure her of Aspergers disease."
    call her_main("Actually sir, Aspergers has been reclassified as part of the autism spectrum and is no longer it's own disease.","body_122")
    m "..."
    m "(Of course she'd know that...)"
    m "Well anyway, my point is there's nothing untoward happening."
    call her_main("...","body_122")
    call her_main("Alright then...","body_122")
    call her_main("But why is she so mean?","body_122")
    m "I'm not sure. Maybe that's the true her."
    call her_main("I guess...","body_122")
    call her_main("But why was she jerking you off?","body_122")
    m "Oh um..."
    m "Well that sort of just happened during my evaluation..."
    m "She wanted to help her fathers magazine anyway possible, and one thing led to another..."
    call her_main("...","body_122")
    call her_main("ugh, fine...","body_122")
    call her_main("I guess...","body_122")
    m "So you don't mind helping out with her in the future?"
    call her_main("What? I have to spend more time with her?","body_122")
    call her_main("But she's weird...","body_122")
    m "We can work on that. Besides, don't you want to help out one of your friends?"
    call her_main("Hmmm, I suppose that you're right [genie_name].","body_122")
    call her_main("I can't imagine that the daydreaming Luna would make it too well in the real world.","body_122")
    call her_main("and as her friend It's my responsibility to try and save her from that.","body_122")
    call her_main("!!!","body_122")
    call her_main("Maybe we could even have study sessions together!","body_122")
    call her_main("I've always wanted someone to study with! Normally it's only ever Harry and I'm pretty sure he's just there to stare at my boobs.","body_122")
    menu:
        "-Encourage friendship-":
            $ luna_friendship = 1
            $ luna_hatred = 0
            m "I'm sure she'd be happy to spend some more time with you."
            call her_main("Do you think so sir? She seemed pretty mean today.","body_122")
            m "She'll come around, just give it time."
            call her_main("I hope so sir! A ravenclaw study buddy would be great!","body_122")
            m "(more like fuck buddy...)"
            call her_main("...","body_08")
        "-discourage friendship-":
            $ luna_friendship = 0
            $ luna_hatred = 1
            m "I'm not so sure about that. She seemed pretty harsh today."
            call her_main("hmmm, you're probably right.","body_122")
            m "Maybe you should fight fire with fire?"
            call her_main("And be mean in return?","body_122")
            call her_main("I don't know [genie_name]... She is my friend...","body_08")
    m "Anyway, thanks for your help today."
    call her_main("anything for my friends [genie_name]...","body_08")
    m "(Does that mean me?)"
    m "Yes, well, 60 points to \"gryffindor\"!"
    $ gryffindor += 60
    call her_main("Thank you [genie_name]...","body_08")

    jump end_hg_pf


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