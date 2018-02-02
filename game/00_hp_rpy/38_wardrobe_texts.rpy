

label equipping_failed:

    if mad >= 1 and mad <=5:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0 #activates dissolve in her_main
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "Would you wear this--"
            call her_main("I'm sorry [genie_name],...",xpos=525,"body_16") #525=default Hermione xpos #open, confident closed
            call her_main("But I don't feel like dressing up for you today.","body_10") #open mouth, concerned look left
            m "Any chance I could convince you otherwise?"
            call her_main("Hmm...","body_82") #very upset, default
            call her_main("I want 5 house points! And that's no guarantee that I'm actually going to wear...","body_127") #open, confident closed
            call her_main("Whatever it is you want me to put on.","body_50") #disgust, 

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Give her the points-":
                    m "alright, [hermione_name],... here are your points..."
                    m "ahe--hem..."
                    m "Five points for Gryffindor!"
                    m "Was that good enough for you?"
                    call her_main("...","body_03") #default, default
                    call her_main("Thank you, [genie_name].","body_13") #soft, default left
                    m "Great, now I forgot what I wanted you to wear..."
                    $ gryffindor += 5
                    $ mad = 0
                    $ her_main_smooth_transition = True
                    call her_main("", xpos=400)
                "-Don't give her the points-":
                    m "I don't think so, missy!"
                    call her_main("...","body_09") #very upset, very angry
                    call her_main("Fine!","body_49") #mad, angry
                    call her_main("I don't want them anyway!","body_71") #very upset, down
                    m "You sure?"
                    call her_main("Tzzz--","body_05") #mad, angry
                    $ her_main_smooth_transition = True
                    call her_main("", xpos=400)
        else:
            hide screen hermione_main
            with d3
            ">Hermione is mad at you! She won't wear it!"
            menu:
                ">You can give Gryffindor points to better her mood."
                "-5 points for Gryffindor!-":
                    $ gryffindor += 5
                    $ mad = 0
                    ">Hermione is no longer mad at you!"
                    $ hermione_xpos = 400
                    call her_main_rndm_happy
                "-Don't bother-":
                    $ her_main_smooth_transition = True
                    $ hermione_xpos = 400
                    call her_main_rndm_angry

        $ wardrobe_active = 1
        call her_main("",xpos=400)
        call screen wardrobe
        

    if mad >= 6 and mad <=10:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0 #activates dissolve in her_main
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "I'd like you to wear--"
            call her_main("No, [genie_name]...",xpos=525,"body_16") #525=default Hermione xpos #open, confident closed
            call her_main("I'm still mad at you for what you did!","body_10") #open, concerned left
            m "Will you wear it if I give Gryffindor some points?"
            call her_main("...","body_17") #very upset, suspicious
            call her_main("Fifteen house points!","body_14") #open, default
            call her_main("And maybe I will wear it.-- Only maybe!","body_107") #open, default left

            $ menu_x = 0.2 #Default position of the menu (0.5). Version B is $ menu_x = 0.2
            menu:
                "-Give her the points-":
                    m "alright, [hermione_name],... here are your points..."
                    m "Fifteen points..."
                    g4 "for Gryffindor!"
                    m "Was that good enough for you?"
                    call her_main("(It's so easy to get points out of him!)","body_13") #soft, baseL
                    call her_main("Thank you,[genie_name].","body_127") #open, closed
                    m "No poblem. Now put on... {w=0.9}what was it again?"
                    $ gryffindor += 15
                    $ mad = 0
                    $ her_main_smooth_transition = True
                    call her_main("", xpos=400)
                "-Don't give her the points-":
                    m "I'm already giving you new clothing! Isn't that enough?"
                    call her_main("No it's not enough, [genie_name]!","body_127") #open, closed
                    call her_main("I want those points!","body_49") #mad, angry
                    call her_main("(You can shove those clothes up your ass...)","body_12") #very upset, angryL
                    m "I'm not giving you the points, [hermione_name]."
                    call her_main("Tzzz--","body_05") #mad, angry
                    call her_main("Well then wear your... {w=0.5}-stuff yourself!","body_30") #screaming, angry closed
                    m "Wouldn't look good on me..."
                    call her_main("I don't care.","body_50") #very upset, annoyed
                    $ her_main_smooth_transition = True
                    call her_main("", xpos=400)
        else:
            hide screen hermione_main
            with d3
            ">Hermione is really mad at you! She won't wear it!"
            menu:
                ">You can give Gryffindor points to better her mood."
                "-15 points for Gryffindor!-":
                    $ gryffindor += 15
                    $ mad = 0
                    ">Hermione is no longer mad at you!"
                    $ hermione_xpos = 400
                    call her_main_rndm_happy
                "-Don't bother-":
                    $ her_main_smooth_transition = True
                    $ hermione_xpos = 400
                    call her_main_rndm_angry

        $ wardrobe_active = 1
        call her_main("",xpos=400)
        call screen wardrobe


    if mad >= 11:
        if wardrobe_chitchat_active:
            $ wardrobe_active = 0 #activates dissolve in her_main
            hide screen hermione_main
            with d3
            m "[hermione_name]..."
            m "Would you please--"
            call her_main("No--",xpos=525,"body_16") #525=default Hermione xpos #open, closed
            call her_main("...","body_50") #very upset, annoyed
            m "I just want you to wear--"
            call her_main("I SAID NO, [genie_name]!","body_30") #scream, angry closed
            call her_main("tzzzz...","body_69") #very upset, annoyedL
            g4 "Fine! {w=0.9}Forget it."
            call her_main("",xpos=400)
        else:
            hide screen hermione_main
            with d3
            ">Hermione is really mad at you! There is no point in trying to make her wear it!"
            call her_main_rndm_angry


        $ wardrobe_active = 1
        call her_main("",xpos=400)
        call screen wardrobe


### Change Hair-Style ###
       
label change_her_hair_style: 

    if wardrobe_hair_style == h_hair_style:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    if mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:
            hide screen hermione_main 
            with d3
            $ wardrobe_active = 0 #activates dissolve in her_main 

            $ hermione_xpos = 525

            if h_hair_style == "B" and wardrobe_hair_style == "A":
                m "[hermione_name]..."
                m "Could you wear your hair normal for me?"

            if h_hair_style == "A" and wardrobe_hair_style == "B":
                m "[hermione_name]..."
                m "Could you tie your hair up for me?"

            call her_main("Of course, [genie_name].","body_15") #525=default Hermione xpos #soft, base
            call her_main("Let me just change it.","body_01") #base, base


            hide screen hermione_main
            with d3

            pause.5

            $ her_main_smooth_transition = True
            call set_her_hair_style(wardrobe_hair_style)
            call compliment_her_hair_style

            $ her_main_smooth_transition = True
            call her_main("",xpos=400)
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            $ wardrobe_active = 1
            call set_her_hair_style(wardrobe_hair_style)
            call her_main("",xpos=400)
            call screen wardrobe


label compliment_her_hair_style:
    if whoring < 5:
        call her_main("Like this, [genie_name]?","body_15") #soft, base
        m "This look really suits you, [hermione_name]."
        call her_main("Thank you, [genie_name].","body_188") #smile, baseL, blush
    elif whoring < 11:
        call her_main("...","body_74") #smile, happy closed
        call her_main("Do you like it, [genie_name]?","body_209") #grin, wink, blush
        m "Indeed I do, [hermione_name]."
        call her_main("Thank you.","body_01") #smile, base
    elif whoring < 20:
        call her_main("How do I look?","body_127") #open, closed
        m "You look very lovely, [hermione_name]!"
        call her_main("Glad to hear that, [genie_name].","body_58") #smile, glance
    else: #20+
        if h_hair_style == "A":
            call her_main("Do you like my long hair, [genie_name]?","body_58") #smile, glance
            m "I do, [hermione_name]"
            call her_main("I prefer wearing my hair open like this.","body_127") #open, closed
            call her_main("Makes it easier to grab and pull...","body_58") #smile, glance
            call her_main("Like a leash!","body_111") #big smile, angry
            g4 "You dirty slut!"
        else: 
            call her_main("Do you like it, [genie_name]?","body_58") #smile, glance
            call her_main("Does this hair make me look...","body_01")
            call her_main("Slutty?","body_58") #smile, glance
            g4 "Ugh!--You can bet your perfect ass on it!" 
            g9 "Why don't you come over here and I give your hair some lotion!" 
            call her_main("[genie_name] you should know that I already used some rather expensive lotion this morning and--","body_127") #open, closed
            m "I just want to shower them in my cum, girl..."  
            call her_main("Oh-","body_15") #soft, base
            call her_main("...","body_200") #soft, baseL, blush  
            call her_main("(What a great idea.)","body_74") #smile, happy closed
            call her_main("Maybe next time, [genie_name].","body_46") #big smile, baseL
    return


### Change Hair-Color ###

label change_her_hair_color:

    if wardrobe_hair_color == h_hair_color:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    elif mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:

            hide screen hermione_main 
            with d3
            $ wardrobe_active = 0 #activates dissolve in her_main 

            $ hermione_xpos = 525
            m "[hermione_name]..."

            #Brown
            if wardrobe_hair_color == "1":
                m "I want you to change your hair back to brown." 
                if whoring < 5:
                    call her_main("Gladly, [genie_name].","body_127") #open, closed
                    call her_main("(I hope this get people to stop staring at me...)","body_70") #very upset, ahegao
                    call her_main("I will go and change it.","body_54") #smile, baseL
                if whoring < 11:
                    call her_main("Of course, [genie_name].","body_14") #open, base
                    call her_main("Let me go change it.","body_01") #smile, base
                elif whoring < 20:
                    call her_main("Sure, [genie_name].","body_13") #soft, baseL
                    call her_main("Let me just change it.","body_58") #smile, glance
                else: #20+
                    call her_main("Brown, [genie_name]?","body_44") #upset, wink
                    call her_main("(But I liked having my hair stand out...)","body_71") #very upset, down
                    call her_main("Fine, [genie_name]... {w=0.9}let me go change it.","body_54") #smile, baseL
                    
            #Blonde
            elif wardrobe_hair_color == "2":
                m "Would you dye your hair blonde for me?" 
                if whoring >= 5:
                    if whoring < 5:
                        call her_main("Blonde?...","body_44") #upset, wink
                        call her_main("(It looks decent enough... {w=0.9}maybe I should try something new once in a while...)","body_71") #very upset, down 
                        call her_main("Ok, [genie_name]... {w=0.9}Let me go change it.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Blonde?","body_01") #smile, base
                        call her_main("Alright, [genie_name].","body_13") #soft, openL
                        call her_main("Let me just change it real quick.","body_58") #smile, glance
                    else: #20+
                        call her_main("That barely even looks like blonde!","body_71") #very upset, down
                        call her_main("Don't you have anything brighter?","body_122") #mad, wink 
                        m "You going to wear it or not?"
                        call her_main("Fine,... Let me go change it.","body_50") #upset, annoyed
                else:
                    call her_main("No thank you, [genie_name].","body_127") #open, closed
                    call her_main("I like my hair how it is.","body_10") #open, concernedL
                    call her_main("I have to refuse!","body_03") #normal, base
                    if cheats_active:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Red
            elif wardrobe_hair_color == "3":
                m "Would you dye your hair red for me?" 
                if whoring >= 5:
                    if whoring < 5:
                        call her_main("Red, [genie_name]?","body_14") #open, base
                        call her_main("It looks a lot like Ginny's hair-colour...","body_59") #smile, down
                        m "Genie?"
                        call her_main("Ginny Weasley, [genie_name].","body_127") #open, closed
                        m "..."
                        call her_main("(...?)","body_122") #mad, wink
                        m "Of course! That Weasely... uhh--sister...?"
                        call her_main("Yes, [genie_name].","body_08") #open, suspicious
                        m "(I wonder if she is hot...)"
                        m "(The girl says she is a redhead...)"
                        g9 "(She has to be!)"
                        call her_main("I will go and change my hair, [genie_name].","body_107") #open, baseL
                    elif whoring < 11:                                                                                          #Continue here
                        call her_main("Oh wow I like it!","body_01")
                        call her_main("It will make me look just like Ginny!","body_75") #big smile, happy closed
                        call her_main("(although she's a bit shorter than me,... and her hair isn't as curly.)","body_01")
                        call her_main("(I wonder if the teachers will notice should we switch places in class...)","body_01")
                        call her_main("(Only one way to find out!)","body_01")
                        call her_main("Let me go change it!","body_01")
                    else: #20+
                        call her_main("You want me to be a redhead, hmm...?","body_01")
                        call her_main("You know what they say about redheads, [genie_name].","body_01")
                        call her_main("Let me go change it for you.","body_01")
                else:
                    call her_main("No thank you, [genie_name].","body_127") #open, closed
                    call her_main("I like my hair how it is.","body_10") #open, concernedL
                    call her_main("I have to refuse!","body_03") #normal, base
                    if cheats_active:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Crimson
            elif wardrobe_hair_color == "4":
                m "Would you dye your hair crimson for me?" 
                if whoring >= 8:
                    call her_main("It's a really nice colour, [genie_name].","body_01")
                    call her_main("I will go and change it real quick.","body_01")
                else:
                    call her_main("That's a bit much don't you think?","body_01")
                    call her_main("(My hair would look like the hair of some street-whore...)","body_01")
                    call her_main("I have to refuse, [genie_name]!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Black
            elif wardrobe_hair_color == "5":
                m "Would you dye your hair black for me?" 
                if whoring >= 8:
                    call her_main("Black, [genie_name]?","body_01")
                    call her_main("(It does look nice.)","body_01")
                    call her_main("I will try it! Let me go and change it.","body_01")
                else:
                    call her_main("Black, [genie_name]?","body_01")
                    call her_main("Black isn't really my colour.","body_01")
                    call her_main("I don't think it will suit me, [genie_name].","body_01")
                    call her_main("I have to refuse.","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Green
            elif wardrobe_hair_color == "6":
                m "Would you dye your hair for me again?"
                call her_main("Sure, [genie_name]. In which colour?","body_01") 
                g9 "Slytherin Green!"
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","body_01")
                    if whoring >= 11 and whoring <= 17:
                        call her_main("Just because Slytherin choose that color for their house doesn't mean that I can't wear it!","body_01")
                        call her_main("(It will look awfully suspicious for a Gryffindor though)","body_01")
                    else: #18+
                        call her_main("Would you like me to tell you a secret, [genie_name]?","body_01")
                        call her_main("Green is my favourite colour!","body_01")
                        m "Really? not red?"
                        call her_main("Hmm... no, [genie_name]. Not anymore.","body_01")
                    call her_main("Just let me go change it.","body_01")
                else:
                    call her_main("What?!","body_01")
                    call her_main("I'm not going to walk around school parading as some Slytherin joke-mascot!","body_01")
                    call her_main("I definitely refuse!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Blue
            elif wardrobe_hair_color == "7":
                m "Would you dye your hair blue for me?" 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","body_01")
                    call her_main("Let me go change.","body_01")
                else:
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Really?","body_01")
                        call her_main("You want me to look like a lesbian that bad?","body_01")
                        call her_main("I'm going to refuse!","body_01")
                        if cheats_active:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                    else: #14+
                        call her_main("I'm not going to dye my hair blue, [genie_name]!","body_01")
                        call her_main("If you want a parrot that bad you should just buy one!","body_01")
                        if cheats_active:
                            ">Try again at whoring level 8."
                        jump return_to_wardrobe
                    
            #Purple
            elif wardrobe_hair_color == "8":
                m "Would you dye your hair purple for me?" 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","body_01")
                    call her_main("Let me go change.","body_01")
                else:
                    call her_main("Purple?","body_01")
                    call her_main("I do like the colour, but...","body_01")
                    call her_main("I don't think I want to wear it on my head","body_01")
                    call her_main("I have to refuse, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Pink
            elif wardrobe_hair_color == "9":
                m "Would you dye your hair pink for me?" 
                if whoring >= 14:
                    call her_main("Of course, [genie_name]!","body_01")
                    call her_main("I love pink!!!","body_01")
                    call her_main("Hi-hi--","body_01")
                    call her_main("Let me go change.","body_01")
                else:
                    call her_main("Pink?","body_01")
                    call her_main("I can't dye my hair pink, [genie_name]!","body_01")
                    call her_main("(What does he think I am? His cheap looking dressup-doll?)","body_01")
                    call her_main("It's an ugly colour anyway.","body_01")
                    call her_main("I definitely refuse!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe
                    
            #White
            elif wardrobe_hair_color == "10":
                m "Dye your hair white for me." 
                if whoring >= 17:
                    call her_main("Sure, [genie_name].","body_01")
                    call her_main("Let me go change.","body_01")
                else:
                    call her_main("No, [genie_name].","body_01")
                    call her_main("I'm not going to run around school looking like some grandma!","body_01")
                    call her_main("I refuse!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_her_hair_color(wardrobe_hair_color)

            $ her_main_smooth_transition = True
            call her_main("",xpos=400)
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            if wardrobe_hair_color == "2" and whoring <= 5:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if wardrobe_hair_color == "3" and whoring <= 5:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if wardrobe_hair_color == "4" and whoring <= 8:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if wardrobe_hair_color == "5" and whoring <= 8:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if wardrobe_hair_color == "6" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if wardrobe_hair_color == "7" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if wardrobe_hair_color == "8" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if wardrobe_hair_color == "9" and whoring <= 14:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 14."
                jump return_to_wardrobe
            if wardrobe_hair_color == "10" and whoring <= 17:
                ">She won't wear that colour just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_her_hair_color(wardrobe_hair_color)
            call her_main("",xpos=400)
            call screen wardrobe


### Equip Top ###

label equip_top:    #useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

    if top_choice == h_top:
        $ wardrobe_active = 1
        #">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    elif mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:

            hide screen hermione_main 
            with d3
            $ wardrobe_active = 0 #activates dissolve in her_main 

            $ hermione_xpos = 525
            m "[hermione_name]..."

            ### Uniform ###

            #Uniform Top Vest and Tie
            if top_choice == "uni_top_1":
                m "Would you wear your uniform top for me? The one with the vest and tie." 
                if whoring >= 0 and whoring <= 7:
                    call her_main("Of course, [genie_name].","body_01")
                    call her_main("Let me go and change real quick.","body_01")
                elif whoring >= 8 and whoring <= 13:
                    call her_main("Alright, [genie_name].","body_01")
                    call her_main("Let me go and change real quick.","body_01")
                elif whoring >= 14 and whoring <= 19:
                    call her_main("Are you sure, [genie_name]?","body_01")
                    call her_main("My old school top?","body_01")
                    call her_main("You don't even want me to remove my tie or show off my cleavage??","body_01")
                    m "No, [hermione_name]. No cleavage today."
                    call her_main("(Is he up to something?)","body_01")
                    call her_main("(Maybe this is a test...)","body_01")
                    call her_main("OK, let me go change real quick","body_01")
                else: #20+
                    call her_main("That old thing?","body_01")
                    call her_main("Is this some silly joke, [genie_name]?","body_01")
                    m "..."
                    m "(I don't know. Is it?)"
                    call her_main("This is unacceptable!","body_01")
                    call her_main("It doesn't even show any skin!","body_01")
                    m "(...)"
                    call her_main("You are insulting my tits, [genie_name]!!!","body_01")
                    g4 "No! I would never do that, [hermione_name]."
                    if one_of_ten == 1:
                        g4 "Your tits are marvelous!"
                    if one_of_ten == 2:
                        g4 "Your tits are magnificent!"
                    if one_of_ten == 3:
                        g4 "Your tits are breathtaking!"
                    if one_of_ten == 4:
                        g4 "Your tits are wonderful!"
                    if one_of_ten == 5:
                        g4 "Your tits are spectacular!"
                    if one_of_ten == 6:
                        g4 "Your tits are sensational!"
                    if one_of_ten == 7:
                        g4 "Your tits are glorious!"
                    if one_of_ten == 8:
                        g4 "Your tits are beautiful!"
                    if one_of_ten == 9:
                        g4 "Your tits are lovely!"
                    if one_of_ten == 10:
                        g4 "Your tits are bananas!"
                    call her_main("And yet you want me to wear those... rags!","body_01")
                    call her_main("(I hope the boys won't laugh at me for wearing this.)","body_01")
                    m "You going to wear it or not?"
                    call her_main("Ugh--Fine, let me change it real quick.","body_01")
                    
            #Uniform Top Tie only
            elif top_choice == "uni_top_2":
                m "Would you wear your uniform top for me? But leave the vest off." 
                if whoring >= 2:
                    if whoring >= 2 and whoring <= 4:
                        call her_main("OK, [genie_name].","body_01")
                        call her_main("While I find it inappropriate for a Hogwagwarts student to not wear their proper school attire at all times,...","body_01")
                        call her_main("(And of course half of house Slytherin doesn't even bother to tie their shoes...)","body_01")
                        call her_main("You are the headmaster, after all. If it's you request to remove my vest then I shall remove it.","body_01")
                        call her_main("Let me go and change, [genie_name].","body_01")
                    elif whoring >= 5 and whoring <= 10:
                        call her_main("Alright, [genie_name].","body_01")
                        call her_main("Let me go and change it real quick.","body_01")
                    elif whoring >= 11 and whoring <= 16:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("I will just change it right here if you don't mind.","body_01")
                        g4 "(Baby I don't mind at all!)"
                        g9 "(Show me those titties!)"
                    else: #17+
                        call her_main("Just my school shirt and my tie?","body_01")
                        m "Yes, [hermione_name]."
                        call her_main("Do you want me to tie the shirt around my breasts?","body_01")
                        m "No, put it on properly."
                        call her_main("Properly, [genie_name]? What do you mean?","body_01")
                        m "You know, buttons and everything."
                        call her_main("(I completely forgot this shirt had buttons...)","body_01")
                        call her_main("Can't I leave those buttons open, [genie_name]?","body_01")
                        m "I'm afraid not, [hermione_name]."
                        call her_main("(I'm gonna get laughed at for wearing my shirt like this.)","body_01")
                        call her_main("Fine, let me just change it real quick.","body_01")
                else:
                    call her_main("I'm sorry, [genie_name].","body_01")
                    call her_main("But that would be against the Hogwarts rule for proper school attire.","body_01")
                    call her_main("I have to refuse, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Uniform Top No Tie
            elif top_choice == "uni_top_3":
                m "Would you wear your uniform top for me? But remove the tie and the vest." 
                if whoring >= 5:
                    call her_main("You better appreciate this, [genie_name].","body_01")
                    m "It's only a tie, girl!"
                    call her_main("No it is not...","body_01")
                    call her_main("Let me go and change...","body_01")
                else:
                    call her_main("No thank you, [genie_name].","body_01")
                    call her_main("The golden and red tie around my neck represents my affiliation and commitment to Gryffindor, and while...","body_01")
                    m "(There she goes again, rambling on about her stupid school-house...)"
                    call her_main("...when the greatest of the four Hogwarts founders, Godric Gryffindor, choose those colours...","body_01")
                    m "(I don't understand a word she's is saying, {w=0.9}but she has a lovely accent!)"
                    call her_main("...the golden mane of a lion, which is also our houses emblematic animal, symbolizing...","body_01")
                    m "(Should I just jerk off again while she's talking? It's probably too late now. Please tell me she's almost done...)"
                    call her_main("...as can be read about in the book \"A history of Hogwarts\", which you [genie_name] have of course read many times...","body_01")
                    m "..."
                    call her_main("...it is important for a student of Hogwarts to--","body_01")
                    g4 "Enough, girl!"
                    m "Leave your tie on."
                    g4 "(And stop talking!)"
                    call her_main("Very well, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Cleavage
            elif top_choice == "uni_top_4":
                m "Would you wear your uniform top for me? Just the shirt..." 
                g9 "And unbutton some of those buttons! I want you to show some cleavage!" 
                if whoring >= 8:
                    if whoring >= 8 and whoring <= 10:
                        call her_main("(I hope nobody is going to look funny at me.)","body_01")
                        call her_main("Fine, [genie_name]. {w=0.9}Let me go change.","body_01")
                    if whoring >= 11 and whoring <= 19:
                        call her_main("Of course, [genie_name].","body_01")
                        call her_main("I will just change it here.","body_01")
                        m "Yes, do that, [hermione_name]."
                        g4 "(And show me those tits!)"
                    if whoring >= 20:
                        call her_main("(Buttons?... {w=0.9}Oh, he means those.)","body_01")
                        call her_main("Can't I just tie the shirt around my breasts so I can remove it more easily?","body_01")
                        m "Is that really a concern of yours, [hermione_name]"
                        call her_main("Well, yes.","body_01")
                        call her_main("I like showing them to people!","body_01")
                        g4 "You hopeless slut!"
                        call her_main("...","body_01")
                        m "Wear your shirt properly, for now."
                        m "If you are in luck, and I change my mind, I will let you know."
                        call her_main("Yes, [genie_name]. {w=0.9}Let me just change it!","body_01")
                else:
                    if whoring >=2:
                        call her_main("Show some... {w=0.9}Cleavage?","body_01")
                        call her_main("[genie_name], with all due respect,...","body_01")
                        call her_main("I'm not going to walk around school looking like some... harlot!","body_01")
                        call her_main("(What does he think I am? A Slytherin?)","body_01")
                        m "But, don't you realize..."
                        m "It can greatly boost a women's self-confidence showing some--"
                        call her_main("I feel very self-confident just the way am, [genie_name].","body_01")
                        call her_main("I definitely refuse.","body_01")
                    else:
                        ">You are walking on very thin ice here!"
                        call her_main("Whoops, I dropped my wand.","body_01")
                        call her_main("What was it you wanted from me, [genie_name]?","body_01")
                        m "Never mind girl!"
                        call her_main("OK, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Crop-Top
            elif top_choice == "uni_top_5":
                m "I want you to pull up the two ends of your school top and tie them together around your chest." 
                if whoring >= 11:
                    if whoring >= 11 and whoring <= 13:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","body_01")
                        call her_main("Everybody is going to look at my breasts.","body_01")
                        m "I would be surprised if they are not!"
                        call her_main("Ugh--Fine. Let me just change it real quick.","body_01")
                    if whoring >= 14 and whoring <= 19:
                        call her_main("Tie my shirt around my breasts?.","body_01")
                        m "Yes, if you could do that."
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("I will just change it right here.","body_01")
                    if whoring >= 20:
                        call her_main("Of course, [genie_name].","body_01")
                        call her_main("I love wearing my top like this! It's so handy!","body_01")
                        call her_main("I can just untie it whenever a Slytherin boy walks past me!","body_01")
                        call her_main("Or a Slytherin girl of course! I'm not saying that I'm leaving them out!","body_01")
                        m "And what about students of other houses?"
                        call her_main("They too of course!","body_01")
                        call her_main("(But not as much, now that I think about it.)","body_01")
                        call her_main("Let me change my top for you real quick!","body_01")
                else:
                    if whoring <= 2:
                        call her_main("[genie_name]?","body_01")
                        call her_main("Tie my school top... how am I supposed to tie it exactly?","body_01")
                        call her_main("There aren't even any cords or anything on it.","body_01")
                        m "Forget it girl."
                        call her_main("Whatever you say, [genie_name].","body_01")
                    elif whoring <= 8:
                        call her_main("I'm sorry, [genie_name]","body_01")
                        call her_main("But you can't possibly want me to run around like that!","body_01")
                        call her_main("(What a pervert!)","body_01")
                        call her_main("I refuse, [genie_name]!","body_01")
                    else:
                        call her_main("This is really a bit much to ask for, [genie_name].","body_01")
                        call her_main("I can't wear something like that around school!","body_01")
                        call her_main("I'm going to have to refuse!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Top Vest with Cleavage
            elif top_choice == "uni_top_6":
                m "Would you wear your vest for me? Just the vest. Maybe your shirt beneath it. But don't think about closing any of those buttons!"
                if whoring >= 8:
                    if whoring >= 8 and whoring <= 19:
                        call her_main("Just my vest?","body_01")
                        call her_main("(At least I get to show off my cleavage.)","body_01")
                        call her_main("Alright, [genie_name]. I will change it.","body_01")
                    else: #20+
                        call her_main("My vest, [genie_name]?","body_01")
                        call her_main("Don't you have anything more fashionable?","body_01")
                        call her_main("Besides, red and yellow doesn't really suit me.","body_01")
                        m "Wear it, or I will have you cover up your tits too!"
                        call her_main("(That would be horrible!)","body_01")
                        call her_main("Yes, [genie_name]. Let me change it for you.","body_01")
                else:
                    call her_main("Just my vest?","body_01")
                    call her_main("I don't even get to wear my Gryffindor tie?","body_01")
                    call her_main("(How am I supposed to cover my cleavage?)","body_01")
                    call her_main("I have to refuse, [genie_name]!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Top Gryff Cheer
            elif top_choice == "uni_top_cheer_gryff":
                m "Could you wear your cheerleader attire for me? Just the top."
                if whoring >= 5:
                    if whoring >= 5 and whoring <= 19:
                        call her_main("Of course, [genie_name]!","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("What is this? Is this for boys?","body_01")
                        call her_main("Did you steal this from the Gryffindor mascot, [genie_name]?","body_01")
                        call her_main("You want me to put on that giant lion-head too?","body_01")
                        m "(A lion-head? Do they have stuff like that here?)"
                        call her_main("You can't be serious, [genie_name]!","body_01")
                        m "Wear it, or I will have you go naked!"
                        call her_main("...","body_01")
                        call her_main("(Does he really think of making me do that?)","body_01")
                        call her_main("{size=-5}(How exciting...){/size}","body_01")
                        call her_main("I will wear it if I absolutely have to,...","body_01")
                        call her_main("{size=-5}Do I?{/size}","body_01")
                        m "Yes."
                        call her_main("Tzzz--Your loss...","body_01")
                else:
                    call her_main("I don't know, [genie_name].","body_01")
                    call her_main("I'm not the cheerleader type!","body_01")
                    call her_main("While I like the idea of supporting my house in Quidditch,","body_01")
                    call her_main("It is more important to me to secure this years win of the house-cup!","body_01")
                    call her_main("I have to refuse, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Gryff Cheer Skimpy
            elif top_choice == "uni_top_cheer_gryff_skimpy":
                m "Could you wear the top from your cheerleader attire for me?"
                if whoring >= 8: 
                    g9 "The skimpy one!" 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                        call her_main("But Gryffindor isn't even the winning team!","body_01")
                        call her_main("(I don't want to root for those losers...)","body_01")
                        call her_main("(well not all of them are losers, but...)","body_01")
                        call her_main("(They aren't even trying to win. They are so embarrassing.)","body_01")
                        call her_main("Fine. I will change it if I have to.","body_01")
                else:
                    if whoring <= 3: 
                        g9 "The skimp--" 
                        m "Girl? What are you doing?" 
                        ">You see Hermione eying the piece of cloth." 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                        call her_main("(Could it be...)","body_01")
                        call her_main("Do you have a rat problem, [genie_name]?","body_01")
                        m "A rat problem?"
                        call her_main("Yes, rats! They are everywhere in Hogwarts.","body_01")
                        call her_main("And I'm not talking about pet-rats.","body_01")
                        m "(People here keep rats as their pet?)"
                        call her_main("You should talk with Mr. Filch. He will surely know what to do about it!","body_01")
                        call her_main("And throw this away while you're at it. It has holes everywhere!","body_01")
                    else: 
                        g9 "The skimpy one!" 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                        call her_main("Are you out of your mind?","body_01")
                        call her_main("I'm not going to walk around looking like those... Slytherins!","body_01")
                        call her_main("(stupid sluts always distracting our team with their stupid... squeezing--bursting-out-breasts!)","body_01")
                        call her_main("(I hate those skunks! I've lost count how often they flashed their tits at our players during the last game.)","body_01")
                        call her_main("(I won't fall that low.)","body_01")
                        call her_main("I refuse, [genie_name]!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Top Slyth Cheer
            elif top_choice == "uni_top_cheer_slyth" or top_choice == "uni_top_cheer_slyth_skimpy":
                m "Would you wear this cheerleader top for me?" 
                if whoring >= 11:
                    if whoring >= 11 and whoring <= 13:
                        call her_main("But [genie_name], that's for Slytherins.","body_01")
                        m "And?"
                        call her_main("I'm a Gryffindor!","body_01")
                        call her_main("(A muggle-born on top of that.)","body_01")
                        call her_main("I can't wear this!","body_01")
                        m "You got it all wrong, [hermione_name]."
                        m "We have an... uh-student... uhh--exchange! going on right now!"
                        m "The best students of each of the three houses will change places with student."
                        m "And your task is to take the position of a fellow Slytherdings cheerleader!"
                        call her_main("(Three houses? Slyther-what? Did I not hear him right?)","body_01")
                        call her_main("When you say it like that, [genie_name].","body_01")
                        call her_main("I will gladly join your cause, and I won't disappoint!","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Fine, [genie_name].","body_01")
                        call her_main("(How humiliating to wear this...)","body_01")
                        call her_main("Let me just change it.","body_01")
                    else: #20+
                        call her_main("Of course I will wear it!","body_01")
                        call her_main("Gimme-Gimme--Gimme!!!","body_01")
                        call her_main("(I can't wait to root for them on the next game!)","body_01")
                        call her_main("(If they are winning I won't have to wear this long anyway!)","body_01")
                        call her_main("Whoooo, go Slytherin!","body_01")
                else:
                    call her_main("In green?","body_01")
                    call her_main("Are you serious, [genie_name]?","body_01")
                    call her_main("Are you sure you didn't just pick the wrong colour for me?","body_01")
                    m "(Something tells me she doesn't want to wear green stuff.)"
                    m "(Is she allergic to grasshoppers or something?)"
                    m "Forget about it, girl."
                    call her_main("I will!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
                    
            ### Fancy ###

            #Fancy Waitress Beige
            elif top_choice == "fancy_waitress_beige":
                m "Dye your hair white for me." 
                if whoring >= 8:
                    call her_main("Sure, [genie_name].","body_01")
                    call her_main("Let me go change.","body_01")
                else:
                    call her_main("No, [genie_name].","body_01")
                    call her_main("I'm not going to run around school looking like some grandma!","body_01")
                    call her_main("I refuse!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Fancy Waitress Green
            elif top_choice == "fancy_waitress_green":
                m "Dye your hair white for me." 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","body_01")
                    call her_main("Let me go change.","body_01")
                else:
                    call her_main("No, [genie_name].","body_01")
                    call her_main("I'm not going to run around school looking like some grandma!","body_01")
                    call her_main("I refuse!","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe

            hide screen hermione_main
            with d3

            pause.5

            call set_h_top(top_choice)

            $ her_main_smooth_transition = True
            call her_main("",xpos=400)
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if top_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that top just yet."
            #    if cheats_active:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if top_choice == "uni_top_2" and whoring < 2: #no vest
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "uni_top_3" and whoring < 5: #no tie
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_4" and whoring < 8: #cleavage
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_5" and whoring < 11: #crop top
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_6" and whoring < 8: #vest w/cleavage
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if top_choice == "uni_top_cheer_gryff" and whoring < 5:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_cheer_gryff_skimpy" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_cheer_slyth" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_cheer_slyth_skimpy" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Fancy
            if top_choice == "fancy_waitress_beige" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "fancy_waitress_green" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Wicked
            if top_choice == "wicked_leather_jacket_short_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_short_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_rocker_top" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe

            #Muggle
            if top_choice == "normal_pullover" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_pullover_sexy" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_purple_sweater" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe

            #Misc
            if top_choice == "top_banner_gryff" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_shirt_gryff_ripped_long_tie" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_tie_gryff" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_banner_slyth" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "top_fishnets" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe
            else:
                pass

            $ wardrobe_active = 1
            call set_h_top(top_choice)
            call her_main("",xpos=400)
            call screen wardrobe


### Equip Bottom ###

label equip_bottom:    #useful stuff: {w=0.9} {size=-2}text{/size} {b}text{/b} \"text\" 

    if skirt_choice == h_skirt:
        $ wardrobe_active = 1
        ">She's already wearing that!" #Remove line. Just for testing.
        jump return_to_wardrobe

    elif mad >= 1:
        jump equipping_failed

    else:
        if wardrobe_chitchat_active:

            hide screen hermione_main 
            with d3
            $ wardrobe_active = 0 #activates dissolve in her_main 

            $ hermione_xpos = 525
            m "[hermione_name]..."

            ### Uniform Skirts ###

            #Uniform Skirt Very Long
            if skirt_choice == "uni_skirt_1":
                m "Would you wear your school skirt for me? The very long one." 
                if whoring >= 0 and whoring <= 7:
                    call her_main("Of course, [genie_name].","body_01")
                    call her_main("Let me go and change real quick.","body_01")
                elif whoring >= 8 and whoring <= 13:
                    call her_main("Alright, [genie_name].","body_01")
                    call her_main("Let me go and change real quick.","body_01")
                elif whoring >= 14 and whoring <= 19:
                    call her_main("Are you sure, [genie_name]?","body_01")
                else: #20+
                    call her_main("That old thing?","body_01")
                    
            #Uniform Skirt Long
            elif skirt_choice == "uni_skirt_2":
                m "Would you wear your school skirt for me? The other long one." 
                if whoring >= 2:
                    if whoring >= 2 and whoring <= 4:
                        call her_main("OK, [genie_name].","body_01")
                    elif whoring >= 5 and whoring <= 10:
                        call her_main("Alright, [genie_name].","body_01")
                        call her_main("Let me go and change it real quick.","body_01")
                    elif whoring >= 11 and whoring <= 16:
                        call her_main("Sure, [genie_name].","body_01")
                    else: #17+
                        call her_main("Just my school shirt and my tie?","body_01")
                else:
                    call her_main("I'm sorry, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Medium Length
            elif skirt_choice == "uni_skirt_3":
                m "Would you wear your school skirt for me? The shorter one."  
                if whoring >= 5:
                    call her_main("You better appreciate this, [genie_name].","body_01")
                    m "It's only a tie, girl!"
                    call her_main("No it is not...","body_01")
                    call her_main("Let me go and change...","body_01")
                else:
                    call her_main("No thank you, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Short
            elif skirt_choice == "uni_skirt_4":
                m "Would you wear your school skirt for me? The short one." 
                g9 "And unbutton some of those buttons! I want you to show some cleavage!" 
                if whoring >= 8:
                    if whoring >= 8 and whoring <= 10:
                        call her_main("(I hope nobody is going to look funny at me.)","body_01")
                    if whoring >= 11 and whoring <= 19:
                        call her_main("Of course, [genie_name].","body_01")
                    if whoring >= 20:
                        call her_main("(Buttons?... {w=0.9}Oh, he means those.)","body_01")
                else:
                    if whoring >=2:
                        call her_main("Show some... {w=0.9}Cleavage?","body_01")
                    else:
                        call her_main("Whoops, I dropped my wand.","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Shortest
            elif skirt_choice == "uni_skirt_5":
                m "Would you wear your school skirt for me? The really short one."  
                if whoring >= 11:
                    if whoring >= 11 and whoring <= 13:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","body_01")
                    if whoring >= 14 and whoring <= 19:
                        call her_main("Tie my shirt around my breasts?.","body_01")
                    if whoring >= 20:
                        call her_main("Of course, [genie_name].","body_01")
                else:
                    if whoring <= 2:
                        call her_main("[genie_name]?","body_01")
                    elif whoring <= 8:
                        call her_main("I'm sorry, [genie_name]","body_01")
                    else:
                        call her_main("This is really a bit much to ask for, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Gryffindor
            elif skirt_choice == "uni_skirt_cheer_gryff":
                m "Would you wear this cheerleader skirt for me?" 
                g9 "And unbutton some of those buttons! I want you to show some cleavage!" 
                if whoring >= 8:
                    if whoring >= 8 and whoring <= 10:
                        call her_main("(I hope nobody is going to look funny at me.)","body_01")
                    if whoring >= 11 and whoring <= 19:
                        call her_main("Of course, [genie_name].","body_01")
                    if whoring >= 20:
                        call her_main("(Buttons?... {w=0.9}Oh, he means those.)","body_01")
                else:
                    if whoring >=2:
                        call her_main("Show some... {w=0.9}Cleavage?","body_01")
                    else:
                        call her_main("Whoops, I dropped my wand.","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Slytherin
            elif skirt_choice == "uni_skirt_cheer_slyth":
                m "Would you wear this cheerleader skirt for me?"  
                if whoring >= 11:
                    if whoring >= 11 and whoring <= 13:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","body_01")
                    if whoring >= 14 and whoring <= 19:
                        call her_main("Tie my shirt around my breasts?.","body_01")
                    if whoring >= 20:
                        call her_main("Of course, [genie_name].","body_01")
                else:
                    if whoring <= 2:
                        call her_main("[genie_name]?","body_01")
                    elif whoring <= 8:
                        call her_main("I'm sorry, [genie_name]","body_01")
                    else:
                        call her_main("This is really a bit much to ask for, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
                    
            ### Uniform Skirts Low ###

            #Uniform Skirt Low Very Long
            elif skirt_choice == "uni_skirt_1_low":
                m "Would you wear your school skirt for me? The very long one. But pull it down a bit." 
                if whoring >= 8:
                    if whoring >= 8 and whoring <= 19:
                        call her_main("Just my vest?","body_01")
                    else: #20+
                        call her_main("My vest, [genie_name]?","body_01")
                else:
                    call her_main("Just my vest?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Medium Length
            elif skirt_choice == "uni_skirt_2_low":
                m "Would you wear your school skirt for me? The long one. But pull it down a bit." 
                if whoring >= 5:
                    if whoring >= 5 and whoring <= 19:
                        call her_main("Of course, [genie_name]!","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("What is this? Is this for boys?","body_01")
                else:
                    call her_main("I don't know, [genie_name].","body_01")
                    if cheats_active:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Short
            elif skirt_choice == "uni_skirt_3_low":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Shortest (Micro Skirt)
            #elif skirt_choice == "uni_skirt_4_low":
            #    m "Would you wear this school skirt for me?" 
            #    ">You hand her the micro skirt." 
            #    if whoring >= 11:
            #       call her_main("Sure, [genie_name].","body_01")
            #       call her_main("Let me go change.","body_01")
            #    else:
            #        call her_main("No, [genie_name].","body_01")
            #        call her_main("I'm not going to run around school looking like some grandma!","body_01")
            #        call her_main("I refuse!","body_01")
            #        if cheats_active:
            #            ">Try again at whoring level 11."
            #        jump return_to_wardrobe


            ### Skirts ###
                    
            #Belted Mini Skirt
            elif skirt_choice == "skirt_belted_mini":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Belted Micro Skirt
            elif skirt_choice == "skirt_belted_micro":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe


            ### Pants ###
                    
            #Pants Jeans Long
            elif skirt_choice == "pants_jeans_long":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Pants Jeans Short
            elif skirt_choice == "pants_jeans_short":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Pants Retro Shorts
            elif skirt_choice == "pants_retro_shorts":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Pants Rocker Shorts
            elif skirt_choice == "pants_rocker":
                m "Would you wear your school skirt for me? The short one. But pull it down a bit." 
                if whoring >= 8: 
                    if whoring >= 8 and whoring <= 13:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    elif whoring >= 14 and whoring <= 19:
                        call her_main("Sure, [genie_name].","body_01")
                        call her_main("Let me go change.","body_01")
                    else: #20+
                        call her_main("The Gryffindor one?","body_01")
                else:
                    if whoring <= 3: 
                        call her_main("(Thats the schools Quidditch uniform, but... there are so many holes in it.)","body_01")
                    else: 
                        call her_main("The skimpy one, [genie_name]?","body_01")
                    if cheats_active:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
            else:
                pass

            hide screen hermione_main
            with d3

            pause.5

            call set_h_bottom(skirt_choice)

            $ her_main_smooth_transition = True
            call her_main("",xpos=400)
            $ wardrobe_active = 1
            call screen wardrobe

        else:
            #Change this to:
            #if skirt_choice == wardrobe_item and whoring < wardrobe_item.whoring_requirement:
            #    ">She won't wear that skirt just yet."
            #    if cheats_active:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if skirt_choice == "uni_skirt_2" and whoring < 2: #no vest
                ">She won't wear that skirt just yet."
                if cheats_active:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3" and whoring < 5: #no tie
                ">She won't wear that skirt just yet."
                if cheats_active:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_4" and whoring < 8: #cleavage
                ">She won't wear that skirt just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_5" and whoring < 11: #crop top
                ">She won't wear that skirt just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_cheer_gryff" and whoring < 8: #vest w/cleavage
                ">She won't wear that skirt just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_cheer_slyth" and whoring < 5:
                ">She won't wear that skirt just yet."
                if cheats_active:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe

            #Uniform Low
            if skirt_choice == "uni_skirt_1_low" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_2_low" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3_low" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            #if skirt_choice == "uni_skirt_4_low" and whoring < 8:
            #    ">She won't wear that top just yet."
            #    if cheats_active:
            #        ">Try again at whoring level 8."
            #    jump return_to_wardrobe

            #Skirts
            if skirt_choice == "skirt_belted_mini" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "skirt_belted_micro" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Pants
            if skirt_choice == "pants_jeans_long" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_jeans_short" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_retro_shorts" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_rocker" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe



            else:
                pass

            $ wardrobe_active = 1
            call set_h_bottom(skirt_choice)
            call her_main("",xpos=400)
            call screen wardrobe




#



