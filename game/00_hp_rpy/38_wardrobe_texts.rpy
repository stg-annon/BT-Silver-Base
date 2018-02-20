

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
            $ her_main_smooth_transition = True
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

            #Brown #Done
            if wardrobe_hair_color == "1":
                m "I want you to change your hair back to brown." 
                if whoring < 5:
                    call her_main("Gladly, [genie_name].","body_127") #open, closed
                    call her_main("(I hate having people stare at me...)","body_70") #very upset, ahegao
                    call her_main("I will go and change it.","body_54") #smile, baseL
                elif whoring < 11:
                    call her_main("Of course, [genie_name].","body_14") #open, base
                    call her_main("Let me go change it.","body_01") #smile, base
                elif whoring < 20:
                    call her_main("Sure, [genie_name].","body_13") #soft, baseL
                    call her_main("Let me just change it.","body_58") #smile, glance
                else: #20+
                    call her_main("Brown, [genie_name]?","body_44") #upset, wink
                    call her_main("(But I liked having my hair stand out...)","body_71") #very upset, down
                    call her_main("Fine, [genie_name]... {w=0.9}let me go change it.","body_54") #smile, baseL
                    
            #Blonde #Done
            elif wardrobe_hair_color == "2":
                m "Would you dye your hair blonde for me?" 
                if whoring >= 5:
                    if whoring < 11:
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
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Red #Done
            elif wardrobe_hair_color == "3":
                m "Would you dye your hair red for me?" 
                if whoring >= 5:
                    if whoring < 11:
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
                    elif whoring < 20:                                                                                          #Continue here
                        call her_main("Oh wow, it looks pretty. I really like it!","body_15") #soft, base
                        call her_main("It will make me look just like Ginny!","body_75") #big smile, happy closed
                        call her_main("(although she's a bit shorter than me,... and her hair isn't as curly.)","body_82") #very upset, base
                        call her_main("(I wonder if the teachers will notice should we switch places in class...)","body_136") #grin, ahegao
                        call her_main("(Only one way to find out!)","body_64") #big smile, glance
                        call her_main("Let me go change it!","body_58") #smile, glance
                    else: #20+
                        call her_main("You want me to be a redhead, hmm...?","body_58") #smile, glance
                        call her_main("You know what they say about redheads, [genie_name].","body_64") #big smile, glance
                        call her_main("Let me go change it for you.","body_15") #soft, base
                else:
                    call her_main("No thank you, [genie_name].","body_127") #open, closed
                    call her_main("I like my hair how it is.","body_10") #open, concernedL
                    call her_main("I have to refuse!","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Crimson #Done
            elif wardrobe_hair_color == "4":
                m "Would you dye your hair crimson for me?" 
                if whoring >= 8:
                    call her_main("It is a really nice colour, [genie_name].","body_15") #soft, base
                    call her_main("Let me go change it real quick.","body_01") #smile, base
                else:
                    call her_main("That's a bit much don't you think?","body_97") #mads, worried closed
                    call her_main("(I'm not dying my hair red to look like some harlot.)","body_201") #very upset, baseL
                    call her_main("I have to refuse, [genie_name]!","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Black #Done
            elif wardrobe_hair_color == "5":
                m "Would you dye your hair black for me?" 
                if whoring >= 8:
                    if whoring < 17:
                        call her_main("Black, [genie_name]?","body_71") #very upset, down
                        call her_main("(It does look nice.)","body_201") #very upset, baseL
                        call her_main("I will try it! Let me go and change it.","body_13") #soft, baseL
                    else: #17+
                        call her_main("Sure, [genie_name]!","body_58") #smile, glance
                        call her_main("I really like that colour!","body_75") #big smile,happy closed
                        call her_main("Let me just change it.","body_58") #smile, glance
                else:
                    call her_main("Black, [genie_name]?","body_08") #open, suspicious
                    call her_main("Black isn't really my colour.","body_13") #soft, baseL
                    call her_main("I don't think it will suit me, [genie_name].","body_127") #open, closed
                    call her_main("I have to refuse.","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Green #Done
            elif wardrobe_hair_color == "6":
                m "Would you dye your hair for me again?"
                call her_main("Of course, [genie_name]. In which colour?","body_14") #open, base
                g9 "Slytherin Green!"
                if whoring >= 11:
                    if whoring < 17:
                        call her_main("Sure, why not.","body_13") #soft, baseL
                        call her_main("Green is just a colour, [genie_name]!","body_14") #open, base
                        call her_main("Wear it on my head doesn't mean I support Slytherin!","body_127") #open, closed
                        call her_main("(It will look awfully suspicious for a Gryffindor though...)","body_29") #very upset, concernedL
                        call her_main("Just let me go change it.","body_01") #smile, base
                    else: #17+
                        call her_main("Yes, [genie_name].","body_01") #smile, base
                        call her_main("To tell you a secret...","body_13") #soft,  baseL
                        call her_main("Green is my favourite colour.","body_58") #smile, glance
                        m "Really? what about red?"
                        call her_main("Hmm... no, [genie_name].","body_201") #very upset, baseL
                        call her_main("Red is such an aggressive colour.","body_87") #open, down
                        call her_main("Green one the other hand is soft and sweet...","body_13") #soft, baseL
                        call her_main("It always reminds me of nature, grassy fields in the summer, the smell of flowers everywhere...","body_107") #open, baseL
                        call her_main("I really love it!","body_75") #big smile, happy closed
                        call her_main("Let me go change it for you.","body_58") #smile, glance
                else:
                    call her_main("What?!","body_49") #mad, angry
                    call her_main("I'm not going to walk around school parading as some Slytherin joke-mascot!","body_30") #scream, angry, closed
                    call her_main("I definitely refuse!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Blue #Done
            elif wardrobe_hair_color == "7":
                m "Would you dye your hair blue for me?" 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","body_13") #soft, baseL
                    call her_main("Let me go change.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("I'm not going to dye my hair blue for you, [genie_name]!","body_04") #open, angry closed
                        call her_main("If you want your own parrot, then you should just buy one!","body_49") #mad, angry
                        if cheats_active or game_difficulty <= 1:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                    else: #5-10
                        call her_main("Really, [genie_name]?","body_17") #very upset, suspicious
                        call her_main("You want me to look like a lesbian that bad?","body_186") #open, annoyed, blush
                        call her_main("I'm going to refuse!","body_201") #very upset, baseL
                        if cheats_active or game_difficulty <= 1:
                            ">Try again at whoring level 11."
                        jump return_to_wardrobe
                    
            #Purple #Done
            elif wardrobe_hair_color == "8":
                m "Would you dye your hair purple for me?" 
                if whoring >= 11:
                    call her_main("Sure, [genie_name].","body_13") #soft, baseL
                    call her_main("Let me go change.","body_58") #smile, glance
                else:
                    call her_main("Purple?","body_122") #mad, wink
                    call her_main("I do like the colour, but...","body_13") #soft, baseL
                    call her_main("I don't think I want to wear it on my head...","body_70") #very upset, ahegao
                    call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Pink #Done
            elif wardrobe_hair_color == "9":
                m "Would you dye your hair pink for me?" 
                if whoring >= 14:
                    call her_main("Of course, [genie_name]!","body_64") #big smile, glance
                    call her_main("I love pink!!!","body_13") #soft, baseL
                    call her_main("Hi-hi--","body_75") #big smile, happy closed
                    call her_main("Let me go change.","body_58") #smile, glance
                else:
                    call her_main("Dye my hair...","body_05") #mad, angry
                    call her_main("Dye my hair Pink?... {w=0.9}Pink?!","body_76") #mad, angry, emote red plus
                    call her_main("I can't dye my hair pink, [genie_name]!","body_32") #scream, worried closed
                    call her_main("(What does he think I am? Some cheap dressup-doll?)","body_69") #very upset, angryL
                    call her_main("It's an ugly colour anyway.","body_127") #open, closed
                    call her_main("I definitely refuse!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe
                    
            #White #Done
            elif wardrobe_hair_color == "10":
                m "Dye your hair white for me." 
                if whoring >= 17:
                    call her_main("Alright, [genie_name].","body_46") #big smile, baseL
                    call her_main("Let me go change.","body_58") #smile, glance
                else:
                    call her_main("No, [genie_name].","body_127") #open, closed
                    call her_main("I'm not going to run around school looking like some grandma!","body_50") #very upset, annoyed
                    call her_main("I refuse!","body_201") #very upset, baseL
                    if cheats_active or game_difficulty <= 1:
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
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if wardrobe_hair_color == "3" and whoring <= 5:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if wardrobe_hair_color == "4" and whoring <= 8:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if wardrobe_hair_color == "5" and whoring <= 8:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if wardrobe_hair_color == "6" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if wardrobe_hair_color == "7" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if wardrobe_hair_color == "8" and whoring <= 11:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if wardrobe_hair_color == "9" and whoring <= 14:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 14."
                jump return_to_wardrobe
            if wardrobe_hair_color == "10" and whoring <= 17:
                ">She won't wear that colour just yet."
                if cheats_active or game_difficulty <= 1:
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

            #Uniform Top Vest and Tie #Done
            if top_choice == "uni_top_1":
                m "Would you wear your uniform top for me? All of it, vest and tie!" 
                if whoring < 8:
                    call her_main("Of course, [genie_name].","body_13") #soft, baseL
                    call her_main("Let me go and change real quick.","body_01") #smile, base
                elif whoring < 14:
                    call her_main("Alright, [genie_name].","body_75") #big smile, happy closed
                    call her_main("Let me go and change real quick.","body_58") #smile, glance
                elif whoring < 20:
                    call her_main("Are you sure, [genie_name]?","body_122") #mad, wink
                    call her_main("My old school top?","body_117") #mad, base
                    call her_main("You don't even want me to remove my tie or show off my cleavage??","body_66") #disgust, annoyed
                    m "No, [hermione_name]. No cleavage today."
                    call her_main("(Is he up to something?)","body_17") #very upset, suspicious
                    call her_main("(Maybe this is a test of some sort...)","body_85") #disgust, down
                    call her_main("OK, let me change it real quick","body_50") #very upset, annoyed
                else: #20+
                    call her_main("That old thing?","body_18") #mad, wide
                    call her_main("Is this some silly joke, [genie_name]?","body_05") #mad, angry
                    m "..."
                    m "(I don't know. Is it?)"
                    call her_main("This is unacceptable!","body_32") #scream, worried closed
                    call her_main("It doesn't even show any skin!","body_118") #mad, down raised
                    m "(...)"
                    call her_main("You are insulting my tits, [genie_name]!!!","body_19") #soft, base, tears
                    g4 "*Gasps* {w=0.9}I would never do that, [hermione_name]!"
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
                    call her_main("And yet you want me to wear those... rags!","body_50") #very upset, annoyed
                    m "You going to wear it or not?"
                    call her_main("Ugh--Fine, let me change it real quick.","body_201") #very upset, baseL
                    
            #Uniform Top Tie only #Done
            elif top_choice == "uni_top_2":
                m "Would you wear your uniform top for me? But leave the vest off." 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("OK, [genie_name].","body_58") #smile, down
                        call her_main("While I find it inappropriate for a Hogwarts student to not wear their proper school attire at all times,...","body_127") #open, closed
                        call her_main("(And of course half of house Slytherin doesn't even bother to tie their shoes...)","body_69") #very upset, angryL
                        call her_main("You are the headmaster, after all. You make the rules.","body_127") #open, closed
                        call her_main("Let me just go and change, [genie_name].","body_01") #smile, base
                    elif whoring < 11:
                        call her_main("Alright, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me go and change it real quick.","body_01") #smile, base
                    elif whoring < 17:
                        call her_main("Sure, [genie_name].","body_56") #grin, baseL
                        call her_main("I will just change it right here if you don't mind.","body_58") #smile, glance
                        #g4 "(Baby I don't mind at all!)"
                        #g9 "(Show me those titties!)"
                        # $ wardrobe_strip = True 
                    else: #17+
                        call her_main("Just my school shirt and my tie?","body_15") #soft, base
                        m "Yes, [hermione_name]."
                        call her_main("Do you want me to tie the shirt around my breasts?","body_107") #open, baseL
                        m "No, put it on properly."
                        call her_main("Properly, [genie_name]?","body_122") #mad, wink
                        m "You know, buttons and everything."
                        call her_main("(I completely forgot this shirt even had buttons...)","body_71") #very upset, down
                        call her_main("Can't I leave these buttons open, [genie_name]?","body_13") #soft, baseL
                        m "I'm afraid not, [hermione_name]."
                        call her_main("(I'm gonna get laughed at for wearing my shirt like this.)","body_70") #very upset, ahegao
                        call her_main("Fine, let me just change it real quick.","body_54") #smile, baseL
                else:
                    call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                    call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Uniform Top No Tie #Done
            elif top_choice == "uni_top_3":
                m "Would you wear your uniform top for me? But remove the tie and the vest." 
                if whoring >= 5: #Gets removed at level 11.
                    call her_main("You better appreciate this, [genie_name].","body_50") #very upset, annoyed
                    call her_main("Can't believe I'm willing to remove my precious Grffindor tie for you...","body_05") #mad, angry
                    m "It's only a tie, girl!"
                    call her_main("No it is not...","body_32") #scream, worried closed
                    call her_main("...","body_29") #very upset, concernedL
                    call her_main("Just let me go and change...","body_82") #very upset, base
                else:
                    call her_main("No thank you, [genie_name].","body_10") #open, concernedL
                    call her_main("No amount of points will ever convince me to remove my precious Gryffindor tie!","body_127") #open, closed
                    call her_main("It's the single most valuable piece of clothing I possess!","body_13") #soft, baseL
                    m "(Maybe for you girl...)"
                    g9 "(But for me it's your panties!)"
                    call her_main("My tie represents my affiliation and commitment to the house Gryffindor, after all...","body_15") #soft, base
                    m "..."
                    call her_main("Every Gryffindor student knows that--","body_87") #open, down
                    m "(There she goes again, rambling on about her school-house...)"
                    call her_main("...when Godric Gryffindor, the greatest of the four founders of Hogwarts, choose the colours red and gold for his house he...","body_127") #open, closed
                    m "(I don't understand a word she's is saying,... {w=0.9}but she has a lovely accent!)"
                    call her_main("...the golden mane of a lion, which is also our houses emblematic animal,...","body_75") #big smile, happy closed
                    m "(Should I just jerk off again while she's talking?)"
                    m "(Probably too late now... {w=0.9}Please tell me she's almost done...)"
                    call her_main("...as can be read about in \"Hogwarts: A History\", which you [genie_name], of course have read a great many times...","body_127") #open, closed
                    m "(...)"
                    call her_main("...it is also important for a student of Hogwarts to--","body_13") #soft, baseL
                    g4 "Enough, girl!"
                    m "Leave your tie on."
                    g4 "(And stop talking!)"
                    call her_main("Very well, [genie_name].","body_15") #soft, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Cleavage #Done
            elif top_choice == "uni_top_4":
                m "Would you wear your uniform top for me? Just the shirt..." 
                g9 "And unbutton some of those buttons! I want you to show some cleavage!" 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("(Lets just hope nobody stares at them too much.)","body_71") #very upset, down
                        call her_main("Fine, [genie_name]. {w=0.9}Let me go change.","body_08") #open, suspicious
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("I will just change it here.","body_58") #smile, glance
                        m "Yes, do that, [hermione_name]."
                        g4 "(And show me those tits!)"
                    else: #20+
                        call her_main("(Buttons?...)","body_129") #smile, suspicious
                        call her_main("(Oh, he means those.)","body_59") #smile, down
                        call her_main("Can't I just tie the shirt around my breasts so I can remove it more easily?","body_127") #open, closed
                        m "Is that really a concern of yours, [hermione_name]"
                        call her_main("Well, yes.","body_13") #soft, baseL
                        call her_main("I like showing them to people!","body_209") #grin, wink, blush
                        g4 "You hopeless slut!"
                        call her_main("...","body_58") #smile, glance
                        m "Wear your shirt properly, for now."
                        m "If you are in luck, and I change my mind, I will let you know."
                        call her_main("Yes, [genie_name]. {w=0.9}Let me just change it!","body_13") #soft, baseL
                else:
                    if whoring >=2:
                        call her_main("Show some...","body_08") #open, suspicious
                        call her_main("Cleavage?","body_05") #mad, angry
                        call her_main("[genie_name], with all due respect,...","body_127") #open, closed
                        call her_main("I'm not going to walk around school looking like some... {w=0.9}harlot!","body_76") #mad, angry, emote red plus
                        call her_main("(What does he think I am? A Slytherin?)","body_12") #very upset, angryL
                        m "It can greatly boost a women's self-confidence if she's willing to show some--"
                        call her_main("I feel very self-confident just the way am, [genie_name].","body_127") #open, closed
                        call her_main("I definitely refuse.","body_17") #very upset, suspicious
                    else:
                        call her_main("Whoops.","body_118") #mad, worried closed down
                        call her_main("I dropped my wand.","body_87") #open, down
                        call her_main("I'm sorry, [genie_name]. {w=0.9}Let me just pick it up real quick.","body_204") #open, baseL, blush
                        hide screen hermione_main
                        with d3
                        ">You are walking on very thin ice here!"
                        $ her_main_smooth_transition = True
                        call her_main("What was it you wanted from me, [genie_name]?","body_13") #soft, baseL
                        m "(Maybe it's not a good idea to ask her that now.)"
                        m "Never mind, girl."
                        call her_main("OK, [genie_name].","body_01") #smile, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Crop-Top #Done
            elif top_choice == "uni_top_5":
                m "I want you to pull up the two ends of your school top and tie them together around your chest." 
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("I really don't know if that's such a good idea, [genie_name]...","body_127") #open, closed
                        call her_main("Everybody is going to look at my breasts...","body_71") #very upset, down
                        g9 "I would be concerned if they didn't!"
                        call her_main("Ugh--Fine. {w=0.9}Let me just change it real quick.","body_101") #soft, angry
                    elif whoring < 20:
                        call her_main("Tie my shirt around my breasts?.","body_08") #open, suspicious
                        m "Yes, if you could do that."
                        call her_main("Of course, [genie_name].","body_195") #grin, glance, blush
                        call her_main("I will just change right here, if you don't mind.","body_58") #smile, glance
                        #m "{w=0.5}.{w=0.5}.{w=0.5}.{w=1.0}!"
                        # $ wardrobe_strip = True 
                    else: #20+
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("I love wearing my top like this! It's so handy!","body_80") #big smile, happy closed, emote yellow
                        call her_main("I can just untie it whenever a Slytherin boy walks past me!","body_121") #soft, ahegao
                        call her_main("Or a Slytherin girl of course! I'm not saying that I'm leaving them out!","body_75") #big smile, happy closed
                        m "And what about students of other houses?"
                        call her_main("They too of course!","body_189") #soft, squintL, blush
                        call her_main("(But not as much, now that I think about it.)","body_70") #very upset, ahegao
                        call her_main("Let me change my top for you real quick!","body_56") #grin, baseL
                        # $ wardrobe_strip = True 
                else:
                    call her_main("This is just ridiculous!","body_05") #mad, angry
                    call her_main("I'm not walking around school wearing my shirt like that!","body_17") #mad, suspicious
                    call her_main("I refuse!","body_10") #open, concernedL
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Top Vest with Cleavage #Done
            elif top_choice == "uni_top_6":
                m "Would you wear your vest for me? Just the vest. Maybe your shirt beneath it. But don't think about closing any of those buttons!"
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Sure, why not.","body_13") #soft, baseL
                        call her_main("Let me just change it.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Just my vest?","body_71") #very upset, down
                        call her_main("(At least I get to show off my cleavage.)","body_70") #very upset, ahegao
                        call her_main("Alright, [genie_name]. I will change it.","body_58") #smile, glance
                    else: #20+
                        call her_main("My vest, [genie_name]?","body_122") #mad, wink
                        call her_main("Don't you have anything more fashionable?","body_70") #very upset, ahegao
                        call her_main("Besides, red and yellow doesn't really suit me.","body_127") #open, closed
                        m "Wear it, or I will have you cover up your tits too!"
                        call her_main("(That would be horrible!)","body_48") #shock, wide
                        call her_main("Yes, [genie_name]. Let me change it for you.","body_13") #soft, baseL
                else:
                    if whoring < 5:
                        call her_main("Just my vest?","body_01") #
                        call her_main("Without my Gryffindor tie?!","body_48") #shock, wide
                        call her_main("Why would I want to do that? I refuse, [genie_name]!","body_117") #mad, base
                    else:
                        call her_main("I'm sorry, [genie_name].","body_127") #open, closed
                        call her_main("But there is no way I will walk around school with...","body_49") #mad, angry
                        call her_main("I will not show off my cleavage, [genie_name]!","body_127") #open, closed
                        call her_main("I have to refuse!","body_201") #very upset, look left
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Top Gryff Cheer #Done
            elif top_choice == "uni_top_cheer_gryff":
                m "Could you wear your cheerleader attire for me? Just the top."
                if whoring >= 5:
                    if whoring < 11:
                        call her_main("Of course, [genie_name]!","body_200") #soft, baseL, blush 
                        call her_main("Let me go change.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Alright, [genie_name]!","body_15") #soft, base
                        call her_main("Let me just change it.","body_58") #smile, glance
                    else: #20+
                        call her_main("What is this? Is this for boys?","body_18") #mad, wide
                        call her_main("Did you steal this from the Gryffindor mascot, [genie_name]?","body_05") #mad, angry
                        call her_main("Want me to put on that giant lion-head too?","body_10") #open, concernedL
                        m "(A lion-head? Do they have stuff like that here?)"
                        call her_main("You can't be serious, [genie_name]!","body_131") #open, worried closed
                        m "Wear it, or I will have you go naked!"
                        call her_main("...","body_48") #shock, wide
                        call her_main("(Does he really think of making me do that?)","body_122") #mad, wink
                        call her_main("{size=-5}(How exciting!){/size}","body_75") #big smile, happy closed
                        call her_main("I will wear it if I absolutely have to,...","body_127") #open, closed
                        call her_main("{size=-5}Do I?{/size}","body_122") #mad, wink
                        m "Yes."
                        call her_main("Tzzz--Your loss...","body_05") #mad, angry
                else:
                    call her_main("I don't know, [genie_name].","body_71") #very upset, down
                    call her_main("I'm not the cheerleader type!","body_122") #mad, wink
                    call her_main("While I like the idea of supporting my house in Quidditch...","body_127") #open, closed
                    call her_main("My priority is to secure this years house-cup instead!","body_107") #open, baseL
                    call her_main("I have to refuse, [genie_name].","body_15") #soft, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Top Gryff Cheer Skimpy #Done
            elif top_choice == "uni_top_cheer_gryff_skimpy":
                m "Could you wear the top from your cheerleader attire for me?"
                if whoring >= 8: 
                    g9 "The skimpy one!" 
                    if whoring < 14:
                        call her_main("Sure, [genie_name]!","body_200") #soft, baseL, blush 
                        call her_main("Let me go change.","body_01") #smile, base
                    elif whoring < 23:
                        call her_main("Alright, [genie_name]!","body_15") #soft, base
                        call her_main("Let me just change it.","body_58") #smile, glance
                    else: #23+
                        call her_main("The Gryffindor one?","body_17") #very upset, suspicious
                        call her_main("But Gryffindor isn't even the winning team!","body_122") #mad, wink
                        call her_main("Gryffindor isn't even trying to win!","body_10") #open, concernedL
                        call her_main("(They are so embarrassing...)","body_70") #very upset, ahegao
                        call her_main("Do I really have to?","body_122") #mad, wink
                        m "Yes, [hermione_name]. Wear the Gryffindor one!"
                        call her_main("Fine, if I have to... Let me just change it.","body_50") #very upset, annoyed
                else:
                    if whoring < 3: 
                        g9 "The skimp--" 
                        m "Girl? What are you doing?" 
                        ">You see Hermione eying the piece of cloth." 
                        call her_main("(Thats the schools Quidditch uniform alright, but...)","body_71") #very upset, down
                        call her_main("(There are so many holes in it...)","body_85") #disgust, down
                        call her_main("(Could it be...!)","body_202") #soft, wide
                        call her_main("[genie_name], do you have a rat problem?","body_127") #open, closed
                        m "A rat problem?"
                        call her_main("Yes, rats! They are everywhere in Hogwarts.","body_11") #open, concerned
                        call her_main("And I'm not talking about pet-rats.","body_66") #disgust, annoyed raised
                        m "(People here keep rats as their pet?)"
                        call her_main("You should talk with Mr. Filch. He will surely know what to do about it!","body_127") #open, closed
                        call her_main("And throw this away while you're at it. It has holes everywhere!","body_50") #very upset, annoyed
                    else: 
                        g9 "The skimpy one!" 
                        call her_main("The skimpy one?","body_48") #shock, wide
                        call her_main("Are you out of your mind, [genie_name]?","body_32") #scream, worried closed
                        call her_main("I'm not going to walk around looking like those... Slytherins!","body_28") #mad, concerned
                        m "But it's a Gryffindor uniform!"
                        call her_main("That has nothing to do with it!","body_05") #mad, angry
                        call her_main("(stupid sluts... always distracting our team with their breasts...)","body_50") #very upset, annoyed
                        call her_main("(Always flashed their tits at our players...)","body_12") #very upset, angryL
                        call her_main("(I hate those skunks! I will never fall that low.)","body_05") #mad, angry
                        call her_main("I'm not going to wear that, [genie_name]!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Top Slyth Cheer #Done
            elif top_choice == "uni_top_cheer_slyth" or top_choice == "uni_top_cheer_slyth_skimpy":
                m "Would you wear this cheerleader top for me?" 
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("But [genie_name], that's for Slytherins.","body_122") #mad, wink
                        m "And?"
                        call her_main("I'm a Gryffindor!","body_50") #very upset, annoyed
                        call her_main("(A muggle-born on top of that.)","body_85") #disgust, down
                        call her_main("I can't wear this!","body_131") #open, worried closed
                        m "Why not?"
                        call her_main("I've already told you, I'm a Gryffindor!","body_70") #very upset, ahegao
                        m "(...)"
                        g9 "(I've got an idea!)"
                        g4 "[hermione_name], I completely forgot to mention!"
                        m "As the top student of Gryffingdoor, you were selected to switch places with a Slytherin student!"
                        m "As a form of bonding method... To bring the four houses closer together!"
                        call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!","body_66") #disgust, worried raised
                        g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students! Especially Gryffindor and Slytherin!"
                        m "I mean, do you like being called a mudblood every day by them?"
                        call her_main("No, [genie_name].","body_122") #mad, wink
                        m "Or when they call you a slut..."
                        g4 "Or a whore!"
                        g9 "Or bitch!"
                        g4 "Or... a whore!"
                        g4 "Or--"
                        call her_main("I get your point, [genie_name]!!!","body_216") #scream, worried closed, blush
                        m "See! I'm giving you an opportunity to better your relationship with Slytherin!"
                        m "Now are you going to wear this for me or not?..."
                        call her_main("(...)","body_69") #very upset, angryL
                        call her_main("Fine, [genie_name]... Let me just put it on.","body_50") #very upset, annoyed
                    elif whoring < 20:
                        call her_main("Fine, [genie_name].","body_121") #soft, ahegao
                        call her_main("(How humiliating to wear this as a Gryffindor...)","body_43") #disgust, very narrow
                        call her_main("Let me just change it.","body_13") #soft, baseL
                    else: #20+
                        call her_main("Of course I will wear it!","body_111") #big smile, angry
                        call her_main("Gimme-Gimme--Gimme!!!","body_75") #big smile, happy closed
                        call her_main("(I'm definitely going to root for them on the next game!)","body_200") #soft, baseL, blush
                        call her_main("(If they are winning I won't have to wear this thing long anyway!)","body_58") #smile, glance
                        call her_main("Whoooo, go Slytherin!","body_75") #big smile, happy closed
                else:
                    call her_main("In green?","body_48") #shock, wide
                    call her_main("Are you serious, [genie_name]?","body_49") #mad, angry
                    call her_main("Are you sure you didn't just pick the wrong colour for me?","body_17") #very upset, suspicious
                    m "(Something tells me she doesn't want to wear green stuff.)"
                    m "(Is she allergic to grasshoppers or something?)"
                    m "Forget about it, girl."
                    call her_main("I will!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
                    
            ### Fancy ###

            #Fancy Waitress Beige #Kinda done
            elif top_choice == "fancy_waitress_beige":
                m "Would you wear this top I bought you." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Fine, [genie_name].","body_127") #open, closed
                        call her_main("Let me put it on before I change my mind...","body_50") #very upset, annoyed
                    else: #11+
                        call her_main("Alright, [genie_name].","body_121") #soft, ahegao
                        call her_main("Let me just change it.","body_58") #smile, glance
                else:
                    if whoring < 2:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else: #2-7
                        call her_main("I'm sorry, [genie_name].","body_127") #open, closed
                        call her_main("But don't even think I would wear a top like this in school!","body_05") #mad, angry
                        call her_main("No thanks.","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Fancy Waitress Green #Kinda done
            elif top_choice == "fancy_waitress_green":
                m "Would you wear this top I bought you." 
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("Fine, [genie_name].","body_127") #open, closed
                        call her_main("Let me put it on before I change my mind...","body_50") #very upset, annoyed
                    else: #14+
                        call her_main("Alright, [genie_name].","body_121") #soft, ahegao
                        call her_main("Let me just change it.","body_58") #smile, glance
                else:
                    if whoring < 2:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else: #2-10
                        call her_main("I'm sorry, [genie_name].","body_127") #open, closed
                        call her_main("I refuse to walk around in a green top that's green!","body_05") #mad, angry
                        call her_main("People might mistake me for a Slytherin!","body_12") #very upset, angryL
                        call her_main("No thanks.","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
                    
            ### Wicked ###

            #Leather Jacket #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves" or top_choice == "wicked_leather_jacket_sleeveless" or top_choice == "wicked_leather_jacket_sleeves":
                m "Could you wear this leather Jacket for me?"

                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("You should know, [genie_name].","body_127") #open, closed
                        call her_main("I don't mind wearing this in your office.","body_10") #open, concernedL
                        call her_main("(Or wearing nothing at all most of the time.)","body_50") #very upset, annoyed
                        call her_main("But wearing something like this in class...","body_49") #mad, angry
                        call her_main("You better appreciate this, [genie_name]!","body_61") #very upset, angry
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","body_127") #open,closed
                        call her_main("It is a really nice looking jacked, after all...","body_71") #very upset, down
                        call her_main("Let me just change it.","body_01") #smile, base
                    else: #23+
                        call her_main("Of course, [genie_name]!","body_75") #big smile, happy closed
                        call her_main("I really love this jacket!","body_64") #big smile, glance
                        call her_main("(Maybe I will wear it open a couple of times...)","body_121") #open, ahegao
                        call her_main("(I want to show the boys my new bra...)","body_56") #grin, baseL
                        call her_main("Let me just put it on real quick.","body_58") #smile, glance
                else:
                    if whoring < 5: 
                        call her_main("[genie_name]?!","body_48") #shock, wide
                        call her_main("How can you even suggest something like that to one of your student!","body_122") #mad, wink
                        call her_main("What kind of silly joke is this?","body_132") #shock, worried closed
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","body_17") #very upset, suspicious
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif whoring < 11: 
                        call her_main("I can't believe you are asking me this, [genie_name]","body_49") #mad, angry
                        call her_main("A leather jacket?... On me?","body_28") #mad, concerned
                        call her_main("Not even a Slytherin would wear something like that!","body_127") #open, closed
                        call her_main("I definitely refuse!","body_50") #very upset, annoyed
                    else:
                        call her_main("No, [genie_name].","body_127") #open, closed
                        call her_main("Even with all the favours I'm willing to do for you...","body_10") #open, concernedL
                        call her_main("I am not going to wear a jacket like this on school grounds.","body_50") #very upset, annoyed
                        call her_main("I refuse!","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            #Leather Jacket Open #Done
            elif top_choice == "wicked_leather_jacket_short_sleeves_open" or top_choice == "wicked_leather_jacket_sleeveless_open" or top_choice == "wicked_leather_jacket_sleeves_open": 
                m "Could you wear this leather Jacket for me?"
                g9 "But leave the front open!"
                if whoring >= 11: 
                    g9 "Those puppies need to breath!"

                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("You should know, [genie_name].","body_127") #open, closed
                        call her_main("I don't mind wearing this in your office.","body_10") #open, concernedL
                        call her_main("(Or wearing nothing at all most of the time.)","body_50") #very upset, annoyed
                        call her_main("But wearing something like this in class...","body_49") #mad, angry
                        call her_main("(no way in hell am I going to leave it open once I step out of his office...)","body_70") #mad, ahegao 
                        call her_main("You better appreciate this, [genie_name]!","body_05") #mad, angry
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","body_127") #open,closed
                        call her_main("It is a really nice looking jacked, after all...","body_71") #very upset, down
                        call her_main("Just... do you expect me to leave it open the whole time?","body_122") #mad ,wink
                        m "Naturally, [hermione_name]."
                        call her_main("With just my bra beneath it?","body_43") #disgust, narrow
                        g9 "You betcha!"
                        call her_main("(Can't believe I'm agreeing to this...)","body_05") #mad, angry
                        call her_main("Fine, [genie_name]. I will wear it open.","body_50") #very upset, annoyed
                    else: #23+
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("Should I wear a bra beneath it, or would you like me to really show them off!?","body_64") #big smile, glance
                        m "Uhm..."
                        call her_main("I'm kidding!","body_75") #big smile, happy closed
                        call her_main("The other teachers wouldn't allow that sadly.","body_71") #very upset, down
                        call her_main("(Except for maybe Professor Snape...)","body_70") #very upset, ahegao
                        call her_main("Let me just put it on real quick.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("[genie_name]?!","body_48") #shock, wide
                        call her_main("How can you even suggest something like that to one of your student!","body_122") #mad, wink
                        call her_main("What kind of silly joke is this?","body_132") #shock, worried closed
                        m "Yes, I'm sorry [hermione_name]. It was indeed just a joke."
                        call her_main("Not a particularly funny one, [genie_name].","body_17") #very upset, suspicious
                        g4 "(What a prude,... I've spent a fortune on this jacket!)"
                        m "(Wonder if I can still get my money back...)"
                    elif whoring < 11: 
                        call her_main("I can't believe you are asking me this, [genie_name]","body_49") #mad, angry
                        call her_main("A leather jacket?... On me?","body_28") #mad, concerned
                        call her_main("Not even a Slytherin would wear something like that!","body_127") #open, closed
                        call her_main("I definitely refuse!","body_50") #very upset, annoyed
                    else:
                        call her_main("No, [genie_name].","body_127") #open, closed
                        call her_main("Even with all the favours I'm willing to do for you...","body_10") #open, concernedL
                        call her_main("I am not going to wear a jacket like this on school grounds.","body_50") #very upset, annoyed
                        call her_main("I refuse!","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe

            #Rocker Top #Done
            elif top_choice == "wicked_rocker_top":
                if whoring < 5: 
                    m "Could you wear this top--"
                else: 
                    m "Could you wear this top for me?"

                if whoring >= 20: 
                    if whoring < 23: 
                        call her_main("Sure, why not.","body_127") #open, closed
                        m "really?"
                        call her_main("Yes,... It's just a normal top after all...","body_13") #soft, baseL
                        m "(...)"
                        m "(Am I going crazy?)"
                        call her_main("Just let me change it real quick.","body_58") #smile, glance
                    else: #23+
                        call her_main("Of course, [genie_name].","body_121") #soft, ahegao
                        call her_main("I like how much it emphasizes my breasts!","body_64") #big smile, glance
                        call her_main("I really do love it!","body_75") #big smile, happy closed
                        call her_main("Let me just put it on real quick.","body_58") #smile, glance
                else:
                    if whoring < 5: 
                        call her_main("A--...","body_132") #shock, worried closed #Add screen shake and sneeze sound.
                        call her_main("A--Achou!!","body_208") #mad, worried closed, blush, emote drop #Add screen shake and sneeze sound.
                        ">Hermione sneezed."
                        call her_main("Ahh,...","body_134") #silly, ahegao
                        call her_main("I'm terribly sorry [genie_name]...","body_122") #mad, wink
                        call her_main("Thank you...","body_74") #smile, happy closed
                        ">Hermione grabs the tissue."
                        g4 "(Wait! what tissue?! Not my...)"
                        ">Hermione sneezes into the top."
                        m "(Oh that's just perfect...)"
                        call her_main("I'm sorry sir. What was it you asked me?","body_13") #soft, baseL
                        m "Nothing, girl..."
                    elif whoring < 11: 
                        call her_main("What?... What is this?!","body_48") #shock, wide
                        call her_main("Wizard... Sex?!","body_86") #scream, angry, emote red plus
                        call her_main("What is this even supposed to mean?","body_49") #mad, angry
                        m "It's just something the kids say nowadays!"
                        call her_main("It most certainly is not!","body_50") #very upset, annoyed
                        m "If you say so..."
                        call her_main("Keep this offensive... thing for yourself, [genie_name].","body_30") #scream, angry closed
                        call her_main("I'm not going to wear it!","body_28") #mad, concerned
                    else: #11-19
                        call her_main("No, [genie_name]!","body_127") #open, closed
                        call her_main("I'm not going to wear a shirt like this on school grounds!","body_10") #open, concernedL
                        call her_main("What are you even thinking!","body_05") #mad, angry
                        call her_main("I refuse!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe
                    
                    
            ### Muggle ###

            #Pink Pullover #Done
            elif top_choice == "normal_pullover":
                m "Could you wear this top I bought you?" 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("[genie_name], that's a pullover!","body_122") #mad, wink
                        m "... So what?"
                        call her_main("Muggle clothing!","body_199") #disgust, down, blush
                        call her_main("Muggle clothes are against the Hogwarts rules for--","body_127") #open, closed
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","body_50") #very upset, annoyed
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","body_12") #very upset, angryL
                    elif whoring < 11:
                        call her_main("Alright, [genie_name].","body_13") #soft, baseL
                        call her_main("(I really like the colour...)","body_59") #smile, down
                        call her_main("(I probably look really cute in it!)","body_74") #smile, happy closed
                        call her_main("Let me put it on, [genie_name].","body_01") #smile, base
                    else: #11+
                        call her_main("Sure, [genie_name].","body_64") #big smile, glance
                        call her_main("Let me put it on real quick.","body_58") #smile, glance
                else:
                    call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                    call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Pink Pullover #Done
            elif top_choice == "normal_pullover_sexy":
                m "Could you wear this pullover I bought you?" 
                if whoring >= 2:
                    if whoring < 11:
                        call her_main("Very well, [genie_name]. Just let me---","body_13") #soft, baseL
                        m "One second,... I'm almost done..."
                        call her_main("Done, [genie_name]? What are you doing with the--","body_08") #open, suspicious
                        m "Shhh! Be quiet, girl... I have to read the manual."
                        g4 "(Right,... I just have to push here, and pull on this...)"
                        ">A heart shaped hole magically appeared in the fabric!"
                        g9 "(Ah, there is is!)"
                        m "Ok girl, now put it on."
                        call her_main("(What did he just do to that pullover?)","body_17") #very upset, suspicious
                        call her_main("(Doesn't look any different to me...)","body_71") #very upset, down
                        call her_main("OK, [genie_name]. Let me put it on.","body_13") #soft, baseL
                    elif whoring < 20:
                        call her_main("You never mentioned that there's a hole in it.","body_87") #open, down
                        call her_main("(Right over my enormous cleavage...)","body_85") #disgust, down
                        m "It's not my fault you never noticed..."
                        call her_main("I can really feel that it's brimming with magic!","body_58") #smile, glance
                        call her_main("Maybe to see it you need a certain degree of... sexual awareness, for it to appear...","body_200") #soft, baseL, blush
                        m "Oh yes! I think something like that was mentioned in the manual!"
                        call her_main("(...)","body_66") #disgust, annoyed
                        call her_main("Fine... Let me just put it on.","body_121") #soft, ahegao
                    else: #20+
                        call her_main("Alright, [genie_name].","body_75") #big smile, happy closed
                        call her_main("Let me put it on real quick.","body_58") #smile, glance
                else:
                    call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                    call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Purple Sweater #Done
            elif top_choice == "normal_purple_sweater":
                m "Could you wear this top I bought you?" 
                if whoring >= 2:
                    if whoring < 5:
                        call her_main("[genie_name], that's a sweater!","body_122") #mad, wink
                        m "... So what?"
                        call her_main("Muggle clothing!","body_199") #disgust, down, blush
                        call her_main("Muggle clothes are against the Hogwarts rules for--","body_127") #open, closed
                        m "Proper school attire... Yeah yeah, heard that one a hundred times already..."
                        call her_main("(...)","body_50") #very upset, annoyed
                        m "I'm telling you to wear it. I'm the headmaster, after all."
                        g9 "(I can do shit like that!)"
                        call her_main("Fine... Let me go and put it on...","body_12") #very upset, angryL
                    elif whoring < 20:
                        call her_main("OK, [genie_name].","body_13") #soft, baseL
                        call her_main("(It does look a lot like one of my old sweaters...)","body_71") #very upset, down
                        call her_main("Let me put it on.","body_01") #smile, base
                    else: #20+
                        call her_main("Sure, [genie_name].","body_64") #big smile, glance
                        call her_main("Let me put it on real quick.","body_58") #smile, glance
                else:
                    call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                    call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe

            #Misc #Doesn't have texts yet.
            elif top_choice == "top_banner_gryff":
                if whoring >= 11:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_shirt_gryff_ripped_long_tie":
                if whoring >= 11:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_tie_gryff":
                if whoring >= 11:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
            elif top_choice == "top_banner_slyth":
                if whoring >= 17:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
            elif top_choice == "top_fishnets":
                if whoring >= 20:
                    pass
                else:
                    ">She won't wear that top just yet."
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 20."
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
            #    if cheats_active or game_difficulty <= 1:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if top_choice == "uni_top_2" and whoring < 2: #no vest
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "uni_top_3" and whoring < 5: #no tie
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_4" and whoring < 8: #cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_5" and whoring < 11: #crop top
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_6" and whoring < 8: #vest w/cleavage
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe

            if top_choice == "uni_top_cheer_gryff" and whoring < 5:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if top_choice == "uni_top_cheer_gryff_skimpy" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "uni_top_cheer_slyth" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "uni_top_cheer_slyth_skimpy" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Fancy
            if top_choice == "fancy_waitress_beige" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if top_choice == "fancy_waitress_green" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Wicked
            if top_choice == "wicked_leather_jacket_short_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_short_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeveless_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_leather_jacket_sleeves_open" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "wicked_rocker_top" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe

            #Muggle
            if top_choice == "normal_pullover" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_pullover_sexy" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if top_choice == "normal_purple_sweater" and whoring < 2:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe

            #Misc
            if top_choice == "top_banner_gryff" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_shirt_gryff_ripped_long_tie" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_tie_gryff" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if top_choice == "top_banner_slyth" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if top_choice == "top_fishnets" and whoring < 20:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
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

            ### Uniform Skirts ###

            #Uniform Skirt Very Long #Done
            if skirt_choice == "uni_skirt_1":
                m "Would you wear your school skirt for me? The very long one." 
                if whoring < 8:
                    call her_main("Of course, [genie_name].","body_13") #soft, baseL
                    call her_main("Let me go and change real quick.","body_01") #smile, base
                elif whoring < 11:
                    call her_main("Alright... sure, why not.","body_59") #smile, down
                    call her_main("Let me go and change real quick.","body_01") #smile, base
                elif whoring < 20:
                    call her_main("Are you sure, [genie_name]?","body_85") #disgust, down
                    call her_main("That thing looks rather plain...","body_127") #open, closed
                    call her_main("I would much rather wear one a bit shorter!","body_122") #mad, wink
                    m "No, [hermione_name]. Wear the long one..."
                    call her_main("Ugh... Fine.","body_85") #disgust, down
                    call her_main("Let me just change it.","body_50") #very upset, annoyed
                else: #20+
                    call her_main("Are you serious?","body_122") #mad, wink
                    call her_main("That thing is soooooo ugly!","body_70") #mad, ahegao
                    call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!","body_43") #disgust, ??? 
                    m "No, [hermione_name]. Wear the long one..."
                    call her_main("Fine... Just let me change it...","body_66") #disgust, annoyed
                    
            #Uniform Skirt Long #Done
            elif skirt_choice == "uni_skirt_2":
                m "Would you wear your school skirt for me? But make it a bit shorter would you." 
                if whoring >= 5:
                    if whoring < 8:
                        call her_main("...","body_50") #very upset, annoyed
                        call her_main("Fine.","body_127") #open, closed
                        call her_main("Let me go and change real quick.","body_01") #smile, base
                    elif whoring < 11:
                        call her_main("Sure, why not.","body_59") #smile, down
                        call her_main("Let me go and change real quick.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just change real quick.","body_58") #smile, glance
                    else: #20+
                        call her_main("...that old thing?","body_69")
                        m "Sure, is that a problem?"
                        call her_main("...","body_70")
                        call her_main("I suppose not...","body_71")
                        call her_main("It's just so plain!","body_69")
                else:
                    call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                    call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                    call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Medium Length #Done
            elif skirt_choice == "uni_skirt_3":
                m "Would you wear your school skirt for me? But make it a bit shorter would you." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Alright... sure, why not.","body_59") #smile, down
                        call her_main("Let me go and change real quick.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me go and change real quick.","body_58") #smile, glance
                    else: #20+
                        call her_main("(...)","body_50") #very upset, annoyed
                        call her_main("(At least it is short enough...)","body_70") #very upset, ahegao
                        call her_main("OK, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just change real quick.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else:
                        call her_main("That's way too short, [genie_name]!","body_127") #open, closed
                        call her_main("I have to refuse!","body_17") #very upset, suspicious
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Short #Done
            elif skirt_choice == "uni_skirt_4":
                m "Would you wear your school skirt for me? But make it a bit shorter would you."
                if whoring >= 14:
                    if whoring < 20:
                        call her_main("Sure, why not.","body_13") #soft, baseL
                        call her_main("Let me change it real quick.","body_58") #smile, glance
                    else: #20+
                        call her_main("(...)","body_50") #very upset, annoyed
                        call her_main("(At least it is short enough...)","body_70") #very upset, ahegao
                        call her_main("OK, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just change real quick.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else:
                        call her_main("That's way too short, [genie_name]!","body_127") #open, closed
                        call her_main("I have to refuse!","body_17") #very upset, suspicious
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 14."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Shortest #Done
            elif skirt_choice == "uni_skirt_5":
                m "Would you wear your school skirt for me? The shortest one you have."  
                if whoring >= 17:
                    if whoring < 23:
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just change real quick.","body_58") #smile, glance
                    else: #23+
                        call her_main("(That old thing?)","body_71") #very upset, down
                        call her_main("Can't I wear something a little shorter?","body_189")
                        m "I don't think they make anything shorter."
                        call her_main("I guess This will just have to do then...","body_196")
                        call her_main("Let me go change...","body_205")
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else:
                        call her_main("How... How short?!","body_48") #shock, wide
                        call her_main("Is that another one of your silly jokes, [genie_name]?","body_28") #mad, concerned
                        call her_main("No, please, don't tell me.","body_127") #open, closed
                        call her_main("I don't even want to know...","body_29") #very upset, concernedL
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Gryffindor #Done
            elif skirt_choice == "uni_skirt_cheer_gryff":
                m "Could you wear your cheerleader skirt for me?"
                if whoring >= 5:
                    if whoring < 11:
                        call her_main("Of course, [genie_name]!","body_200") #soft, baseL, blush 
                        call her_main("Let me go change.","body_01") #smile, base
                    else:
                        call her_main("Alright, [genie_name]!","body_15") #soft, base
                        call her_main("Let me just change it.","body_58") #smile, glance
                else:
                    call her_main("I don't know, [genie_name].","body_71") #very upset, down
                    call her_main("I'm not the cheerleader type!","body_122") #mad, wink
                    call her_main("While I like the idea of supporting my house in Quidditch...","body_127") #open, closed
                    call her_main("My priority is to secure this years house-cup instead!","body_107") #open, baseL
                    call her_main("I have to refuse, [genie_name].","body_15") #soft, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 5."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Cheerleader Slytherin #Done
            elif skirt_choice == "uni_skirt_cheer_slyth":
                m "Would you wear this cheerleader skirt for me?" 
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("But [genie_name], that's for Slytherins!","body_122") #mad, wink
                        m "And?"
                        call her_main("I'm a Gryffindor!","body_50") #very upset, annoyed
                        call her_main("(A muggle-born on top of that.)","body_85") #disgust, down
                        call her_main("I can't wear this!","body_131") #open, worried closed
                        m "Why not?"
                        call her_main("I've already told you, I'm a Gryffindor!","body_70") #very upset, ahegao
                        m "(...)"
                        g9 "(I've got an idea!)"
                        g4 "[hermione_name], I completely forgot to mention!"
                        m "As the top student of Gryffingdoor, you were selected to switch places with a Slytherin student!"
                        m "As a form of bonding method... To bring the four houses closer together!"
                        call her_main("But... the Hogwarts houses are supposed to compete with each other! Especially in a sport activity such as Quidditch!","body_66") #disgust, worried raised
                        g4 "Nonsense! All it does is cause a hateful and unhealthy relationship between students! Especially Gryffindor and Slytherin!"
                        m "I mean, do you like being called a mudblood every day by them?"
                        call her_main("No, [genie_name].","body_122") #mad, wink
                        m "Or when they call you a slut..."
                        g4 "Or a whore!"
                        g9 "Or bitch!"
                        g4 "Or... a whore!"
                        g4 "Or--"
                        call her_main("I get your point, [genie_name]!!!","body_216") #scream, worried closed, blush
                        m "See! I'm giving you an opportunity to better your relationship with Slytherin!"
                        m "Now are you going to wear this for me or not?..."
                        call her_main("(...)","body_69") #very upset, angryL
                        call her_main("Fine, [genie_name]... Let me just put it on.","body_50") #very upset, annoyed
                    elif whoring < 20:
                        call her_main("Fine, [genie_name].","body_121") #soft, ahegao
                        call her_main("(How humiliating to wear this as a Gryffindor...)","body_43") #disgust, very narrow
                        call her_main("Let me just change it.","body_13") #soft, baseL
                    else: #20+
                        call her_main("Of course I will wear it!","body_111") #big smile, angry
                        call her_main("Gimme-Gimme--Gimme!!!","body_75") #big smile, happy closed
                        call her_main("(I'm definitely going to root for them on the next game!)","body_200") #soft, baseL, blush
                        call her_main("(If they are winning I won't have to wear this thing long anyway!)","body_58") #smile, glance
                        call her_main("Whoooo, go Slytherin!","body_75") #big smile, happy closed
                else:
                    call her_main("In green?","body_48") #shock, wide
                    call her_main("Are you serious, [genie_name]?","body_49") #mad, angry
                    call her_main("Are you sure you didn't just pick the wrong colour for me?","body_17") #very upset, suspicious
                    m "(Something tells me she doesn't want to wear green stuff.)"
                    m "(Is she allergic to grasshoppers or something?)"
                    m "Forget about it, girl."
                    call her_main("I will!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
                    
            ### Uniform Skirts Low ###

            #Uniform Skirt Low Very Long #Done
            elif skirt_choice == "uni_skirt_1_low":
                m "Would you wear your school skirt for me? The very long one. But pull it down a bit." 
                if whoring >= 8:
                    if whoring < 11:
                        call her_main("Alright... sure, why not.","body_59") #smile, down
                        call her_main("Let me go and change real quick.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Are you sure, [genie_name]?","body_85") #disgust, down
                        call her_main("That thing looks rather plain...","body_127") #open, closed
                        call her_main("I would much rather wear one a bit shorter!","body_122") #mad, wink
                        m "No, [hermione_name]. Wear the long one..."
                        call her_main("Ugh... Fine.","body_85") #disgust, down
                        call her_main("Let me just change it.","body_50") #very upset, annoyed
                    else: #20+
                        call her_main("Are you serious?","body_122") #mad, wink
                        call her_main("That thing is soooooo ugly!","body_70") #mad, ahegao
                        call her_main("I'm gonna get laughed at! No one wears skirts that long in Hogwarts!","body_43") #disgust, ??? 
                        m "No, [hermione_name]. Wear the long one..."
                        call her_main("Fine... Just let me change it...","body_66") #disgust, annoyed
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","body_48") #shock, wide
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","body_49") #mad, angry
                        call her_main("How can you even suggest such a thing!","body_97") #mad, worried closed
                        call her_main("(disgusting old fool...)","body_50") #very upset, annoyed
                    else:
                        call her_main("No, [genie_name].","body_127") #open, closed
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","body_50") #very upset, annoyed
                        call her_main("My panties would be visible...","body_85") #disgust, down
                        m "That's kind of the point, [hermione_name]."
                        call her_main("I refuse!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Medium Length #Done
            elif skirt_choice == "uni_skirt_2_low":
                m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                if whoring >= 11:
                    if whoring < 14:
                        call her_main("Alright... sure, why not.","body_59") #smile, down
                        call her_main("Let me go and change real quick.","body_01") #smile, base
                    elif whoring < 20:
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me go and change real quick.","body_58") #smile, glance
                    else: #20+
                        call her_main("(...)","body_50") #very upset, annoyed
                        call her_main("(At least it is short enough...)","body_70") #very upset, ahegao
                        call her_main("OK, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just change real quick.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","body_48") #shock, wide
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","body_49") #mad, angry
                        call her_main("How can you even suggest such a thing!","body_97") #mad, worried closed
                        call her_main("(disgusting old fool...)","body_50") #very upset, annoyed
                    else:
                        call her_main("No, [genie_name].","body_127") #open, closed
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","body_50") #very upset, annoyed
                        call her_main("My panties would be visible...","body_85") #disgust, down
                        m "That's kind of the point, [hermione_name]."
                        call her_main("Besides, the length you suggested is way too short!","body_127") #open, closed
                        call her_main("I refuse!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Short #Done
            elif skirt_choice == "uni_skirt_3_low":
                m "Would you wear your school skirt for me? But make it a bit shorter would you. And pull it down a bit."
                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("Of course, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me go and change real quick.","body_58") #smile, glance
                    else: #20+
                        call her_main("(...)","body_50") #very upset, annoyed
                        call her_main("(At least it is short enough...)","body_70") #very upset, ahegao
                        call her_main("OK, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just change real quick.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("Pull my skirt down?!","body_48") #shock, wide
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","body_49") #mad, angry
                        call her_main("How can you even suggest such a thing!","body_97") #mad, worried closed
                        call her_main("(disgusting old fool...)","body_50") #very upset, annoyed
                    else:
                        call her_main("No, [genie_name].","body_127") #open, closed
                        call her_main("I'm not pulling my skirt down for you, [genie_name].","body_50") #very upset, annoyed
                        call her_main("My panties would be visible...","body_85") #disgust, down
                        m "That's kind of the point, [hermione_name]."
                        call her_main("Besides, the length you suggested is way too short!","body_127") #open, closed
                        call her_main("I refuse!","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Uniform Skirt Low Shortest (Micro Skirt) #Not implemented.
            elif skirt_choice == "uni_skirt_4_low":
                m "Could you wear this school skirt for me?" 
                ">You hand her the micro skirt." 
                if whoring >= 20:
                   call her_main("","body_01")
                else:
                    call her_main("","body_01")
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 20."
                    jump return_to_wardrobe


            ### Skirts ###
                    
            #Belted Mini Skirt #Done
            elif skirt_choice == "skirt_belted_mini":
                m "Could you wear this skirt I bought you?" 
                if whoring >= 8: 
                    if whoring < 14:
                        call her_main("(It's so short!)","body_85") #disgust, down raised
                        call her_main("(...)","body_69") #very upset, angry left
                        call her_main("Ok, [genie_name]... I will wear it.","body_127") #open, closed
                        m "Really?"
                        call her_main("Give me the skirt before I change my mind!","body_50") #very upset, annoyed
                    elif whoring < 23:
                        call her_main("Alright, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me just put it on.","body_58") #smile, glance
                    else: #23+
                        call her_main("Alright, [genie_name].","body_75") #big smile, happy closed
                        call her_main("Give it to me!","body_219") #tongue, ahegao, blush
                        g4 "(!!!)"
                        call her_main("The skirt I mean.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else: 
                        call her_main("Absolutely not, [genie_name]!","body_32") #scream, worried closed
                        call her_main("I'm not going to wear a skirt that short!","body_49") #mad, angry
                        call her_main("(What is he thinking?...)","body_28") #mad, concerned
                        call her_main("I refuse","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 8."
                    jump return_to_wardrobe
                    
            #Belted Micro Skirt #Done
            elif skirt_choice == "skirt_belted_micro":
                m "Could you wear this skirt I bought you?"
                if whoring >= 17: 
                    if whoring < 23: 
                        call her_main("(Oh wow, it's so short!)","body_85") #disgust, down raised
                        call her_main("(Everyone will be able to see my ass in this...)","body_121") #soft, ahegao
                        call her_main("(...)","body_69") #very upset, angry left
                        call her_main("I will wear it!.","body_127") #open, closed
                        m "Really?"
                        call her_main("Sure... It's short enough","body_13") #soft, baseL
                        call her_main("Or would you say this is too inappropriate to wear in this school?","body_58") #smile, glance
                        g4 "Grrrrr--... You have my approval!"
                        call her_main("Thank you, [genie_name].","body_13") #soft, baseL
                    else: #23+
                        call her_main("Alright, [genie_name].","body_75") #big smile, happy closed
                        call her_main("Give it to me!","body_219") #tongue, ahegao, blush
                        g4 "(!!!)"
                        call her_main("The skirt I mean.","body_58") #smile, glance
                else:
                    if whoring < 5:
                        call her_main("I'm sorry, [genie_name].","body_01") #smile, base
                        call her_main("But that would be against the Hogwarts rules for proper school attire!","body_127") #open, closed
                        call her_main("I have to refuse, [genie_name].","body_03") #normal, base
                    else: 
                        call her_main("Absolutely not, [genie_name]!","body_32") #scream, worried closed
                        call her_main("I'm not going to wear a skirt that short!","body_49") #mad, angry
                        call her_main("(What is he thinking?...)","body_28") #mad, concerned
                        call her_main("I refuse","body_50") #very upset, annoyed
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe


            ### Pants ###
                    
            #Pants Jeans Long #Done
            elif skirt_choice == "pants_jeans_long":
                m "Could you wear these pants for me?" 
                if whoring >= 2: 
                    if whoring < 5:
                        call her_main("[genie_name], those are jeans!","body_122") #mad, wink
                        m "... yes?"
                        call her_main("Muggle pants!","body_199") #disgust, down, blush
                        call her_main("Girls are supposed to wear skirts here at Hogwarts!","127") #open, closed
                        call her_main("At all times! No exceptions!","body_29") #very upset, concernedL
                        m "That's a very sexist thing to say, don't you think?"
                        call her_main("I-- uhm...","body_122") #mad, wink
                        call her_main("(Crap,... he is right...)","body_85") #disgust, down
                        call her_main("(Hmm... might as well wear them... They don't look too bad...)","body_88") #, down
                        m "(...)"
                        g4 "(How ridiculous!... How can she call those blankets around her hips skirts...)"
                        g9 "(At least I get a nice view of her ass in those pants!)"
                        call her_main("Fine, [genie_name].","body_70") #very upset, ahegao
                        call her_main("I will wear them.","body_15") #soft, base
                    elif whoring < 8:
                        call her_main("Sure, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me go change.","body_01") #smile, base
                    else:
                        call her_main("But they are so long, [genie_name]!","body_70") #very upset, ahegao
                        call her_main("I can't even show off my legs in those!","body_61") #very upset, angry
                        call her_main("(They make my ass look amazing though...)","body_85") #disgust, down
                        call her_main("(Now that I think about it...)","body_70") #very upset, ahegao
                        call her_main("Fine, I will wear them.","body_58") #smile, glance
                else:
                    call her_main("I'm sorry, [genie_name].","body_13") #open, baseL
                    call her_main("But pants are not part of Hogwarts' school attire.","body_127") #open, closed
                    call her_main("Besides, I feel more comfortable in my school skirt.","body_08") #open, suspicious
                    call her_main("I have to refuse!","body_03") #normal, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 2."
                    jump return_to_wardrobe
                    
            #Pants Jeans Short #Done
            elif skirt_choice == "pants_jeans_short":
                m "Could you wear those pants for me?" 
                if whoring >= 11:
                    if whoring < 20:
                        call her_main("Sure, [genie_name].","body_13") #soft, baseL
                        call her_main("Let me go change.","body_01") #smile, base
                    else: #20+
                        call her_main("Alright, [genie_name].","body_13") #soft, baseL
                        call her_main("(They are sooo tight,... I can barely even fit my ass into them...)","body_121") #soft, ahegao
                        call her_main("Let me put them on for you.","body_58") #smile, glance
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","body_13") #open, baseL
                        call her_main("But pants are not part of Hogwarts' school attire.","body_127") #open, closed
                        call her_main("Besides, I feel more comfortable in my school skirt.","body_08") #open, suspicious
                        call her_main("I have to refuse!","body_03") #normal, base
                    elif whoring < 5: 
                        call her_main("... What are these?","body_17") #very upset, suspicious
                        m "Pants..?"
                        call her_main("...","body_50") #very upset, annoyed
                        call her_main("These aren't pants!","body_97") #mad, worried closed
                        m "What are they then?"
                        call her_main("Underwear!","body_48") #shock, wide
                        m "So you're not going to wear them?"
                        call her_main("NO!","body_32") #scream, worried closed
                        call her_main("...","body_49") #mad, angry
                    else: 
                        call her_main("I'm sorry, [genie_name].","body_13") #soft, baseL
                        call her_main("But I don't think I should wear pants like those on school grounds...","body_127") #open, closed
                        call her_main("(They look really nice though...)","body_59") #smile, down
                        call her_main("(Maybe next time...)","body_54") #smile, baseL
                        call her_main("I have to refuse.","body_15") #soft, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 11."
                    jump return_to_wardrobe
                    
            #Pants Retro Shorts #Done
            elif skirt_choice == "pants_retro_shorts":
                m "I want you to wear these pants for me." 
                if whoring >= 17: 
                    if whoring < 20:
                        call her_main("(These pants look so short...)","body_85") #disgust, down raised
                        call her_main("(My ass is gonna be on display the whole time in those...)","body_219") #tongue, ahegao, blush
                        call her_main("Alright, [genie_name].","body_75") #big smile, happy closed
                        call her_main("Let me just change it.","body_58") #smile, glance
                    else: #20+
                        call her_main("Alright, [genie_name].","body_13") #soft, baseL
                        call her_main("I bet you love how my ass looks in those.","body_64") #big smile, glance
                        g9 "You bet I do!"
                        call her_main("Glad to hear that, [genie_name].","body_58") #smile, glance
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","body_13") #open, baseL
                        call her_main("But pants are not part of Hogwarts' school attire.","body_127") #open, closed
                        call her_main("Besides, I feel more comfortable in my school skirt.","body_08") #open, suspicious
                        call her_main("I have to refuse!","body_03") #normal, base
                    elif whoring < 11: 
                        call her_main("No, [genie_name].","body_131") #open, worried closed
                        call her_main("I will not wear pants that short here in school!","body_28") #mad, concerned
                        call her_main("(What is he thinking?!...)","body_69") #very upset, angryL
                    else: 
                        call her_main("I'm sorry, [genie_name].","body_13") #soft, baseL
                        call her_main("But I don't think I should wear pants like those on school grounds...","body_127") #open, closed
                        call her_main("(They look really nice though...)","body_59") #smile, down
                        call her_main("(Maybe next time...)","body_54") #smile, baseL
                        call her_main("I have to refuse.","body_15") #soft, base
                    if cheats_active or game_difficulty <= 1:
                        ">Try again at whoring level 17."
                    jump return_to_wardrobe
                    
            #Pants Rocker Shorts #Done
            elif skirt_choice == "pants_rocker":
                m "I want you to wear these pants for me." 
                if whoring >= 20: 
                    if whoring < 23:
                        call her_main("(These pants are so short...)","body_85") #disgust, down raised
                        call her_main("(I'm such a pervert!)","body_219") #tongue, ahegao, blush
                        call her_main("Alright, [genie_name].","body_75") #big smile, happy closed
                        call her_main("Let me just change it.","body_58") #smile, glance
                    else:
                        call her_main("Alright, [genie_name].","body_13") #soft, baseL
                        call her_main("I bet you love how my ass looks in those.","body_64") #big smile, glance
                        g9 "You bet I do!"
                        call her_main("Glad to hear that, [genie_name].","body_58") #smile, glance
                else:
                    if whoring < 2: 
                        call her_main("I'm sorry, [genie_name].","body_13") #open, baseL
                        call her_main("But pants are not part of Hogwarts' school attire.","body_127") #open, closed
                        call her_main("Besides, I feel more comfortable in my school skirt.","body_08") #open, suspicious
                        call her_main("I have to refuse!","body_03") #normal, base
                    elif whoring < 5: 
                        call her_main("What?!...","body_49") #mad, angry
                        call her_main("What?!... What is this?","body_76") #mad, angry, emote red plus
                        m "I just said those are--"
                        call her_main("[genie_name]!","body_48") #shock, wide
                        call her_main("You can't just hand underwear to your students!","body_28") #mad, concerned
                        m "Underwear?"
                        call her_main("Yes, underwear! Panties!","body_131") #open, worried closed
                        call her_main("What else can you possibly call this?","body_50") #very upset, angry
                        m "That's a perfectly fine pair of jeans!"
                        m "No need to make such a fuss about them!... Just put them on!"
                        call her_main("No I will not!","body_32") #scream, worried closed
                        call her_main("(Not in a million years...)","body_49") #mad, angry
                    elif whoring < 11: 
                        call her_main("I'm sorry, [genie_name].","body_131") #open, worried closed
                        call her_main("But I will not wear pants that short on school grounds!","body_28") #mad, concerned
                        call her_main("(What is he thinking?!...)","body_69") #very upset, angryL
                    else: 
                        call her_main("I'm sorry, [genie_name].","body_13") #soft, baseL
                        call her_main("But I don't think I should wear pants like those on school grounds...","body_127") #open, closed
                        call her_main("(They look really nice though...)","body_59") #smile, down
                        call her_main("(Maybe next time...)","body_54") #smile, baseL
                        call her_main("I have to refuse.","body_15") #soft, base
                    if cheats_active or game_difficulty <= 1:
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
            #    if cheats_active or game_difficulty <= 1:
            #        ">Try again at whoring level "+ ""wardrobe_item.whoring_requirement +"."
            #    jump return_to_wardrobe

            #Uniform
            if skirt_choice == "uni_skirt_2" and whoring < 5: #no vest
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3" and whoring < 8: #no tie
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_4" and whoring < 14: #cleavage
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 14."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_5" and whoring < 17: #crop top
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_cheer_gryff" and whoring < 5: #vest w/cleavage
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 5."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_cheer_slyth" and whoring < 11:
                ">She won't wear that skirt just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe

            #Uniform Low
            if skirt_choice == "uni_skirt_1_low" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_2_low" and whoring < 11:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "uni_skirt_3_low" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            #if skirt_choice == "uni_skirt_4_low" and whoring < 20:
            #    ">She won't wear that top just yet."
            #    if cheats_active or game_difficulty <= 1:
            #        ">Try again at whoring level 20."
            #    jump return_to_wardrobe

            #Skirts
            if skirt_choice == "skirt_belted_mini" and whoring < 8:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 8."
                jump return_to_wardrobe
            if skirt_choice == "skirt_belted_micro" and whoring < 17:
                ">She won't wear that top just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe

            #Pants
            if skirt_choice == "pants_jeans_long" and whoring < 2:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 2."
                jump return_to_wardrobe
            if skirt_choice == "pants_jeans_short" and whoring < 11:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 11."
                jump return_to_wardrobe
            if skirt_choice == "pants_retro_shorts" and whoring < 17:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 17."
                jump return_to_wardrobe
            if skirt_choice == "pants_rocker" and whoring < 20:
                ">She won't wear those pants just yet."
                if cheats_active or game_difficulty <= 1:
                    ">Try again at whoring level 20."
                jump return_to_wardrobe



            else:
                pass

            $ wardrobe_active = 1
            call set_h_bottom(skirt_choice)
            call her_main("",xpos=400)
            call screen wardrobe




#



