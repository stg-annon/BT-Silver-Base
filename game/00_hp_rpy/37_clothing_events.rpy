###Jeans ###
label equip_jeans:

    if whoring >= 0 and whoring <= 2: # Lv 0
        call her_main("Muggle pants?","body_11")
        m "Yup"
        call her_main(".....?","body_11")
        call her_main("Wait you want me to WEAR them!?","body_31")
        m "Yup"
        call her_main("At school!?")
        m "How does 10 points sound?"
        call her_main("Those are not part of the school uniform! I'd be suspended or *shudder* worse!","body_18")
        m "Who cares. 15 points?"
        call her_main("NO amount of points is worth being suspended!","body_07")
        m "30?"
        jump very_no
    elif whoring >= 3 and whoring < 6: #Lv 1  - 2
       call her_main("Muggle pants?","body_11")
       m "Yup"
       call her_main(".....","body_11")
       call her_main("You... want me to wear them...","body_31")
       m "Yup"
       call her_main("At school?")
       m "How does 10 points sound?"
       call her_main("But they're not part of the school uniform... I'd get suspended... I don't have permission!","body_18")
       m "I'm the head master, [hermione_name]. I'm giving you permission"
       m "15 points?"
       call her_main("............")   
       call her_main("... How on earth am I going to explain this to my classmates?","body_21")
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_skirt("jeans_long")
       call her_main("","body_21",xpos=120,ypos=0)
       show screen ctc
       with d3
       pause
       $ request_jeans = True
       m "15 points for Gryffindor!"
       $ gryffindor +=15
       call her_main("Thank you, [genie_name]","body_29",xpos=410)
    elif whoring >= 6 and whoring < 9:
       call her_main("Jeans?","body_02")
       m "Yup"
       call her_main("You want me to wear them at school?","body_17")
       m "Yup"
       call her_main("*sigh* as long as I don't get into any trouble...","body_16")
       call her_main("and I get some points for Gryffindor","body_14")
       m "I'm the head master, [hermione_name], there won't be any trouble."
       m "And 15 points for Gryffindor!"
       $ gryffindor +=15
       call her_main("Thank you, [genie_name]! (These might.. get me some extra attention)","body_59")
       call her_main("(Not that I want the attention!) I'm only in it for the points!","body_58")
       g9 ""
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_skirt("jeans_long")
       call her_main("","body_58",xpos=120,ypos=0)
       $ request_jeans = True
       show screen ctc
       with d3
       pause
       call her_main("","body_01",xpos=410)
    elif whoring >= 9 and whoring <= 15: 
       call her_main("Jeans?","body_02")
       m "Yup"
       call her_main("Aren't they a little... plain?","body_66")
       m "How do you mean?"
       call her_main("How am I going to save Gryffindor if I look like just another boring girl?","body_16")
       call her_main("How am I going to get my points?","body_16")
       call her_main("At least make this worth while... Please, [genie_name]","body_17")
       m "15 points for Gryffindor, I guess?"
       call her_main("You're the best, [genie_name]!","body_129")
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_skirt("jeans_long")
       $ request_jeans = True
       show screen ctc
       with d3
       call her_main("*humph* ... (These are so stuffy... How am i supposed to get my hands into...)","body_12",xpos=120)
       call her_main("(What if [genie_name] needs me to...)","body_12",xpos=120)
       call her_main("(No... i shouldn't think about things like that! Keep your head in the game, [hermione_name]","body_141")
       call her_main("...","body_141")
       call her_main("(ahh... i thought about it again... naughty [hermione_name]!)","body_188")
       g9 "....."
       call her_main("","body_188",xpos=410)
    elif whoring > 15: 
        call her_main("...Jeans?","body_02")
        m "Yup"
        call her_main("*sigh*...are you serious?","body_04")
        m "...? You're going to draw the line at... a pair of jeans, [hermione_name]?"
        call her_main("Of course not, [genie_name]!","body_87")
        call her_main("It's just that... they take... time to get off","body_204")
        g4 "..."
        call her_main("I have needs and...","body_204")
        call her_main("There's a lot of fabric, [genie_name]")
        call her_main("between [genie_name] and his... [hermione_name]'s ...")
        m "And [hermione_name]'s what?"
        call her_main("...and [hermione_name]'s cunt, [genie_name]","body_208b")
        g4 "(This needy little slut was once the feared Hermione Granger?)"
        g9 ""
        call her_main("...")
        call her_main("I'll go change immediately, [genie_name]","body_209")
        show screen bld1
        with d3
        show screen blktone
        with d3
        call set_h_skirt("jeans_long")
        call her_main("","body_209",xpos=120,ypos=0)
        $ request_jeans = True
        show screen ctc
        with d3
        pause
        call her_main("If you still have time, [genie_name], we could test how long it takes to get out of these things?","body_205")
        g9 "(I love my job)"
        call her_main("","body_209",xpos=410)
    
    jump day_request_clothing
    
### Gryffindor Stockings ###
label equip_gryyf_stockings:
    if whoring < 3:
       call her_main("Is that!?","body_11")
       call her_main("A pair of Gryffindor stockings!?","body_48")
       m "Yep?"
       call her_main("They're sold out from the uniform shop on the very first day, of EVERY SINGLE YEAR!","body_48")
       m "Probably?"
       call her_main("I NEED THEM! What'll it cost me!?","body_34")
       m "No cost"
       call her_main("!","body_48")
       m "It's a gift, [hermione_name], to show you what a great guy ME, Proffesor DeltaDwarf, really is!"
       call her_main("...")
       call her_main("hhmppphhh", "body_42")
       call her_main("hahahahahahaha!","body_80b")
       call her_main("ahhh....","body_157")
       call her_main("You're too funny! Thanks for the gift! I'll put them on right away","body_01")
       g6 "(...What did I say?)"
       call her_main("I've always wanted a pair of these! They're warm, and they reduce unwanted attention from the boys","body_45")
       call her_main("I will be the next best thing to having a skirt that's twice as long!","body_46")
       m "Just glad to help, [hermione_name]!"
       g4 "(hehehe... hope you remember those words after I've made you so needy and desperate you'll suck off a hundred boys just to get off once)"
       call her_main("They feel great!","body_01",xpos=120,ypos=0)
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_stockings("gryff")
       show screen ctc
       with d3
       pause
       call her_main("Thanks again, [genie_name]! You're too kind","body_01",xpos=410)
       g9 "(We'll see)"
       $ request_gryyf_stockings = True
    
    elif whoring >= 3 and whoring <= 6:
    
       $ hermione_wear_skirt = True
       $ hermione_wear_top = True
       
       call her_main("Is that...","body_11")
       $ hermione_emote_exclam = True
       call her_main("A pair of Gryffindor stockings!?","body_48")
       m "Yep?"
       call her_main("They're sold out from the uniform shop on the very first day, of EVERY SINGLE YEAR!","body_48")
       m "K?"
       call her_main("....")
       $ hermione_emote_exclam = False
       $ hermione_emote_hearts = True
       call her_main("I NEED THEM!", "body_34")
       call her_main("What'll it cost me!?", "body_34")
       call her_main("WHAT DO I HAVE TO DO!?","body_32")
       $ hermione_emote_hearts = False
       m "Just a small favour"
       call her_main("(!)","body_48")
       m "All I want, [hermione_name], is to see how great they look on you."
       m "Easy, right?"
       call her_main("...")
       call her_main("You just want to see me in stockings? That should be no problem...", "body_14")
       call her_main("(Is he up to something?)","body_07")
       call her_main(".....")
       call her_main("","body_01",xpos=120,ypos=0)
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_stockings("gryff")
       show screen ctc
       with d3
       pause
       call her_main("What do you think, [genie_name]?")
       m "Impressive..."
       m "They look great, [hermione_name]!"
       call her_main("[genie_name]! My appearance has no bearing on my academic ability.","body_217") #Embarrassed mouth wide eyes closed angry
       call her_main("......","body_186")
       call her_main("(That does make me feel kinda nice, though...)","body_186") #Embarrassed mouth open angry
       g9 "But, I'm having a hard time seeing all the details with that skirt in the way"
       call her_main("(Oh no...)","body_28") #Worried, teeth showing
       call her_main("(I knew it! That pervert!)","body_47") #Angry, teeth showing
       call her_main("(sigh...)","body_47")
       call her_main("(alright, [hermione_name], we've done this before, it's as easy as Arithmancy)","body_47")
       call her_main("(there's nothing embarrassing about this!)","body_140") #Worried, embarrassing, small tears
       call her_main("I'm just showing that bastard a little square of fabric", "body_186")
       call her_main("That's all!")
       call her_main("And think of how much more I'll get done without boys staring at my legs all day...","body_141") #Worried, angry, embarrassed
       m "I'm waiting, [hermione_name]. Don't tell me you don't want your gift?"
       call her_main("No, [genie_name], I want it.")
       g9 "Then earn it, [hermione_name]"
       call her_main("....","body_182b",xpos=120) #embarrassed, eyes closed, mouth closed
       call set_hermione_action("lift_skirt")
       $ skirt_up = True
       show screen hermione_03 #Hermione lifts her skirt
       with d3
       pause
       show screen bld1
       with d3
       show screen blktone
       with d3
       call her_main("","body_141",xpos=120)
       show screen ctc
       with d3
       pause
       $ skirt_up = False
       #call reset_hermione_main
       show screen hermione_blink #Hermione stands still.
       with fade
       m "They suit you, [hermione_name]"
       call her_main("Again with the sweet talk?")
       call her_main("(it won't work on someone like me...)", "body_182")
       m "Your panties, your stockings... they make you look so pretty"
       call her_main("(ahh! he called me pretty)", "body_188")
       call her_main("You saw what you wanted... now I can go, right [genie_name]?","body_141",xpos=120)
       #call her_main("Please?","body_141")
       m "(True, I did get a great panty shot)"
       g9 "(But I could try to get more out of her...)"
       m "What should I do?"
       menu:
            "What a cutie! Let her go":
                m "Of course, [hermione_name]. Enjoy your stockings"
                $ hermione_emote_hearts = True
                call set_hermione_action("")
                call update_her_uniform
                call her_main("Thanks, [genie_name]! I'll wear them whenever you want.","body_209")
                call her_main("(phew. why does it feel like a dodged a bullet, though?)","body_209")
                $ hermione_emote_hearts = False
                $mad = 0
            
            "Cute is boring. Break her.":
               m "That was certainly adequate, [hermione_name]..."
               call her_main("(Adequate...?)","body_81",xpos=120)
               m "But..."
               call her_main("oh no...","body_48",xpos=120)
               m "You're one of our top students..."
               m "And there were still areas I couldn't see..."
               m "You're not giving it 100\%, here!"
               call her_main("(No way...)","body_48",xpos=120)
               g4 "You're going to remove your skirt"
               g4 "Then you're going to remove your panties."
               g9 "And then I'm going to get a proper look. Just as we agreed."
               call set_hermione_action("")
               $ hermione_emote_anger = True
               call her_main("NO", "body_218")
               g4 "(?)"
               call her_main("NO WAY!")
               call her_main("THERE IS ABSOLUTELY NO WAY AM I GOING TO DO THAT!!!")
               call her_main("I'm not some cheap slytherin slut that you can just play with!","body_148")
               g4 "..."
               m "Would you like to have your gift taken back from you?"
               $ hermione_emote_anger = False
               $ hermione_emote_exclam = True
               call her_main("....","body_140")
               m "Forfeit your points?"
               $ hermione_emote_exclam = False
               call her_main("...........","body_140")
               m "How about I remove some points for disobeying the head master?"
               call her_main("...............","body_48",xpos=145)
               m "And end our tutoring arrangement all together..."
               m "I wonder what will happen to your report card?"
               m "I wonder what your parents will think..."
               g9 "When they realize they've raised a failure"
               call her_main("Stop it...","body_143")
               g9 "(Hmm?)"
               call her_main("I get it already...","body_143",xpos=120)
               call her_main(".......","body_143")
               $mad += 55
               ">With tears rolling down her soft cheeks, Hermione begins to unzip her skirt"
               ">Her trembling hands make it difficult just to keep hold of the zipper"
               ">Eventually she gets it, and after hooking her thumb over her panties, she lowers the rest of her dignity to the floor"    
               $ hermione_wear_skirt = False
               #$ h_request_wear_panties = False
               call update_her_uniform
               hide screen ctc
               with d3
               pause
               $ hermione_wear_panties = False
               call update_her_uniform
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_147")
               pause
               show screen ctc
               with d3
               m "Hands behind your back, [hermione_name]. I want to see everything."
               call her_main(".....","body_145")
               call set_hermione_action("hands_behind")
               call set_hermione_action("")
               ">Too weak to fight back, Hermione does as she's told"
               hide screen ctc
               with d3
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_145")
               pause
               show screen ctc
               with d3
               m "Good girl."
               g9 "(What a spectacular body...)"
               call her_main(".......","body_145")
               call her_main("(After all he's done to me... why do i feel...)","body_145")
               call her_main("(like i'm still on fire...)","body_145")
               call her_main("this doesn't make any sense","body_145")
               call her_main("Ahh... hehehehehehehe","body_142")
               m "(...has she lost it already?)"
               call her_main("(whatever... it doesn't need to make sense)")
               call her_main("(You're headed straight to Azkaban once this is over, anyway)","body_142")
               call her_main("(so at least for now, keep looking at my body!)","body_142")
               call her_main("(my whole body needs to melt)","body_142")
               g9 "(hehehehe, i hope [hermione_name] can feel it)"
               g9 "(how a bitch feels when she's in heat)"
               ">Slowly but surely, you see a trickle of nectar begin to leak out of Hermione."
               $ hermione_dribble = True
               call h_update_body
               hide screen ctc
               with d3
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_158")
               pause
               show screen ctc
               with d3
               call her_main("(This is....)")
               call her_main("(too good)")
               g9 "(heh. once i'm done with you, you'll be dripping like this every day)"
               call her_main("(more....)")
               call her_main("(i want to be tutored more by [genie_name]!)")
               m "..."
               g9 "....."
               call her_main (".....")
               m "We're done here, [hermione_name]"
               call her_main(".....","body_158")
               m "You can keep the stockings."
               call her_main(".......","body_158")
               m "And 50 points to Gryffindor for your outstanding preformance."
               $ gryffindor += 50
               call her_main("..........","body_158")
               g4 "What do you say when you've been given a gift?"
               call her_main("..........","body_158")
               call her_main("Thank you, [genie_name]","body_158")
               g9 "That's right, [hermione_name]."
               m "Don't forget your clothes on the way out."
               call her_main("(my... p..)","body_158")
               call her_main("(..pussy is throbbing)","body_158")
               call her_main("(i might become an addict if i'm not careful)","body_158")
               ">Hermione retrieves her clothes and starts putting them back on"
               call her_main("(just the panties touching...)","body_142")
               call her_main("(feels incredible!)","body_142")
               "You can't help but notice stains on the pure white fabric that's hugging her leaking cunt "
               call set_hermione_action("hands_free")
               call set_hermione_action("")
               $ hermione_wetpanties = True
               $ hermione_wear_panties = True
               call update_her_uniform
               hide screen ctc
               with d3
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_142")
               pause
               call her_main("(ahh, i've made them all sloppy)","body_142")
               g9 "We're going to have a lot of fun in future, [hermione_name]"
               call her_main("","body_142")
               $ hermione_wear_skirt = True
               $ hermione_dribble = False
               call update_her_uniform
               with d3
               call her_main("","body_158")
               ">'Leaking' overlay now equip-able!"
               ">'Wet panties' overlay now equip-able!"
               $ hermione_wetpanties = True
               $ dribble_equippable = True
               $ wetpanties_equippable = True
       
       hide screen blktone
       hide screen bld1
       hide screen hermione_main
       hide screen hermione_stand_f #Hermione stands still.
       with d3
       call her_walk(400,610,2)
       $ request_gryyf_stockings = True
       ">Gryffindor stockings now equip-able!"
       #call reset_hermione_main
       
       jump end_hg_pf
    
    jump day_request_clothing