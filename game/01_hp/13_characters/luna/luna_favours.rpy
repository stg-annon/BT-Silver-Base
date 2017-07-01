###FAVOURS###------------------------------------------------------

label luna_favour_1: ###TALK TO ME
    m "{size=-4}(All I'll do is have a nice little conversation with her...){/size}"
    if luna_corruption <= 1:
        $ luna_corruption += 1
    if luna_corruption == 0: #FIRST TIME
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
            ">You hand Luna [current_payout] gold."
            call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)     
            ">Luna leaves your office."  



    elif luna_corruption >= 1: #SECOND TIME 
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
                            $ luna_dom = 1
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
                            $ luna_dom = 0
                            m "well now that you mention it I'm sure those tarts would probably charge a lot less for a conversation..."
                            call luna_main("*Hmph* You get what you pay for...", 7, 2, 3, 3)
                            m "And what exactly am I getting from you for my payment?"
                            call luna_main("Getting to Look at me while you stroke your filthy old cock should be payment enough.", 7, 1, 3, 2)
                            m "Well you'll have to excuse my old eyes because I can barely see you..."
                            menu: 
                                "-Ask her to open her top-":
                                    m "Perhaps you should undo a button or two so I can get a better look."
                                    call luna_main("Are you serious? You expect me to flaunt myself like some cheap tart?", 8, 1, 2, 2)
                                    m "No, I expect you to flaunt yourself like the princess you claim to be..."
                                    call luna_main("...", 7, 2, 2, 2)
                                    m "I'm waiting..."
                                    call luna_main("... {size=-8}(fine...){/size}", 6, 3, 4, 3)
                                    ">Luna removes her tie and opens her top slightly..."
                                    hide screen luna 
                                    with d3
                                    $ luna_top = "01_hp/13_characters/luna/clothes/uniform/top_2.png"
                                    show screen luna 
                                    with d3 
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
    ">You hand Luna [current_payout] gold."
    call luna_main("Thank you, [l_genie_name].", 5, 2, 1, 1)     
    ">Luna leaves your office."  
    hide screen genie_jerking_sperm_02     
    jump luna_away
label luna_favour_2: ###STRIP FOR ME
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