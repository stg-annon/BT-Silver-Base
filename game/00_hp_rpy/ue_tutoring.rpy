label l_tutoring_check:
    if v_tutoring == 0:
        jump l_tutoring
    elif v_tutoring == 1 and whoring >= 1:
        jump l_tutoring
    elif v_tutoring == 2 and whoring >= 2:
        jump l_tutoring
    elif v_tutoring == 3 and whoring >= 3:
        jump l_tutoring
    elif v_tutoring == 4 and whoring >= 5:
        jump l_tutoring
    elif v_tutoring == 5 and whoring >= 8:
        jump l_tutoring
    elif v_tutoring == 6 and whoring >= 11:
        jump l_tutoring
    elif v_tutoring == 7 and whoring >= 14:
        if gift_item_inv[7] >= 1:# Adult magazines
            jump l_tutoring
        else:
            m "I need to buy adult magazines for this lesson."
    elif v_tutoring == 8 and whoring >= 17:
        if gift_item_inv[7] >= 1:# Porn magazines
            jump l_tutoring
        else:
            m "I need to buy porn magazines for this lesson."
    elif v_tutoring == 9 and whoring >= 20:
        if gift_item_inv[11] >= 1:# Vibrator
            jump l_tutoring
        else:
            m "I need to buy a vibrator for this lesson."
    elif v_tutoring == 10 and whoring >= 23:
        if gift_item_inv[14] >= 1:# Anal plugs
            jump l_tutoring
        else:
            m "I need to buy anal plugs for this lesson."
    elif v_tutoring == 11 and whoring >= 23:
        jump l_tutoring
    elif v_tutoring == 12 and whoring >= 23:
        jump l_tutoring
    elif v_tutoring == 13 and whoring >= 23:
        jump l_tutoring
    else:
        m "Not the right time. Soon..."
    
    jump day_time_requests

label l_tutoring:
    $ d_flag_01 = False
    $ menu_x = 0.5

    hide screen hermione_main
    $ h_xpos = 140

    if v_tutoring == 0:   # Whoring lvl 0
        $ her_SC.setXPos("right")
        
        $ her_SC.say("Of course, sir.","body_14")
        $ her_SC.say("I'll go get my books then.")
        
        $ her_SC.hideScreen()
        show screen blkfade
        with d3
        play sound sd_door
        pause 2
        play sound sd_door
        pause.3
        $ her_SC.setXPos("center")
        $ her_SC.setAction("hold_book")
        $ her_SC.say("","body_45")
        
        hide screen blkfade
        with d3
        show screen ctc
        pause
        hide screen ctc
        
        $ her_SC.say("Again, thank you for doing this for me, sir...","body_14")
        m "..........."
        $ her_SC.say("Sir?","body_13")
        m "It's time to talk about your future, child."
        stop music fadeout 1.0
        $ her_SC.say("I'm not a child anymore professor!","body_07")
        m "In a way you're right but..."
        her "..........."
        m "Anyway I can tutor you but you need to understand certain things about magic."
        m "With proper training you can learn to increase your magic ability."
        play music ms_manatees fadein 1 fadeout 1
        $ her_SC.say("Yes?","body_13")
        m "Certain emotions like love and hate, pleasure and pain..."
        g9 "{size=-2}(If she falls for that, I'm a true genius){/size}"
        $ her_SC.say("I've been studying magic for years and I've never heard of such a thing.","body_03")
        g4 "{size=-2}(Shit){/size}"
        m "And that's exactly why you're still a child. You still have much to learn about magic."
        $ her_SC.say("Please stop that, professor. Nobody considers me a child anymore.","body_02")
        m "Yes, technically..."
        $ her_SC.say("Technically?!","body_02")
        g4 "Enough of this. You came to me to ask for my help and if it starts like that..."
        $ her_SC.say("Yes, I suppose you are right...","body_05")
        $ her_SC.say("Alright, I'm ready to study hard with you!","body_45")
        g9 "{size=-2}(Yes!){/size}"
        $ her_SC.say("What was that?","body_186")
        m "Uh, yes I'm glad you're beginning to understand, {w=0.3}child."
        her "..........."
        m "Alright, I want you to take some time and think about what I've said. Next time we'll start with your first lesson."
        $ her_SC.say("Can't we start now?","body_14")
        m "Miss Hermione, you're not the only student I must take care of."
        $ her_SC.say("You're tutoring someone else?","body_02")
        m "{size=-2}(If only...){/size}"
        m "I meant, I must take care of all the students of this school."
        m "But yes, there is another girl who needs..."
        $ her_SC.say("A Slytherin girl?!","body_130")
        g9 "That is none of your business, miss Granger."
        $ her_SC.say("Yes, professor, I'm sorry but with all the recent events I'm a little on edge.","body_05")
        m "Apology accepted and now goodnight!"
        $ her_SC.say("Good night professor and thanks again for taking some of your precious time to help me.","body_45")
        hide screen bld1
        $ her_SC.hideScreen()
        with d3
        "You dismiss Hermione."
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(I'm glad professor agreed to tutor me){/size}","head_exp/35")
        $ her_SC.sayHead("{size=-4}(But pleasure and pain? I don't understand where this is going...){/size}","head_exp/2")
        hide screen hermione_stand_f
        with d3
        
        $ her_SC.setAction(None)
        
        $ v_tutoring = 1
        jump l_tutoring_end

    if v_tutoring == 1:   # Whoring lvl 1
        $ her_SC.setAction("hold_book")
        $ her_SC.say("","body_45")
        m "Miss Granger, time for your first lesson."
        $ her_SC.say("Yes, professor.","body_13")
        m "You've brought your books again, I don't think we'll need them for the moment."
        $ her_SC.say("Too bad, I love books.","body_03")
        g9 "{size=-2}(And soon you'll love cock){/size}"
        $ her_SC.say("Yes?","body_13")
        m "It's nothing, I was just thinking about our next lesson."
        $ her_SC.say("{size=-2}(The elderly...){/size}","body_05")
        m "............."
        m "Anyway have you thought about what we discussed?"
        $ her_SC.say("Not really, I'm not sure what you mean by \"emotions\".","body_03")
        g9 "{size=-2}(Oh me I'm sure){/size}"
        m "For example, what was your state of mind when you heard those rumours about the Slytherin girls?"
        $ her_SC.say("Please don't bring it up, sir, it really makes me mad!","body_130")
        m "And what is this feeling?"
        $ her_SC.say("...{w=0.5}an emotion I suppose...","body_03")
        m "Yes and don't you have emotions you prefer over others?"
        $ her_SC.say("When I have the best score at a test.","body_75")
        m "{size=-2}(This girl is a monomaniac...){/size}"
        m "Don't you have other passions, things you like to do?"
        $ her_SC.say("Yes! Studing and reading books.","body_75")
        g4 "{size=-2}(By all the ancient gods and the new){/size}"
        m "Things are not going in the right direction..."
        $ her_SC.say("And what direction is that, sir?","body_03")
        g9 "{size=-2}(You impaled on my cock){/size}"
        m "Adulthood Miss Hermione, adulthood..."
        $ her_SC.say("I am by far the most mature of my peers, professor. What more can you ask?","body_16")
        m "......{w=0.5}Miss Granger, did we not discuss this already? You need to accept you still have much to learn."
        m "I'm tired of all this and I have work to do so goodnight, child."
        $ her_SC.say("Tutoring one of those filthy Slytherin girls maybe?","body_186")
        m "Maybe that's the right direction, think about what all those girls do with professors."
        $ her_SC.say("But...{w=0.5} that's so wrong...{w=0.5} I don't know if I want to think about that.","body_02")
        m "If you want to progress and to restore the Gryffindor pride, you must!"
        $ her_SC.say("Yes, you are right! It's my mission! I'll do my best professor.","body_195")
        g9 "{size=-2}(She is so naive, it's adorable){/size}"
        m "Good, now time to go to bed child."
        $ her_SC.say("{size=-2}(Tss like I'm going to bed at this time, I need to study more){/size}","body_07")
        hide screen bld1
        $ her_SC.hideScreen()
        with d3
        "You dismiss Hermione."
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Filthy whores...){/size}","head_exp/19")
        $ her_SC.sayHead("{size=-4}(Oh, I should not talk like that...{w=0.5} but it feels so good){/size}","head_exp/35")
        hide screen hermione_stand_f
        with d3
        
        $ her_SC.setAction(None)
        
        $ v_tutoring = 2
        jump l_tutoring_end

    elif v_tutoring == 2:   # Whoring lvl 2
        m "Good you didn't bring your books this time."
        $ her_SC.say("Not that I agree with it. All the knowledge I need is in those books.","body_12")
        m "You're forgetting something important, practice and experience!"
        $ her_SC.say("Maybe, after all you're not at the head of Hogwarts by chance.","body_17")
        m "Sometimes you seem to forget it Miss Granger."
        $ her_SC.say("That sounded like something professor Snape would say...","body_08")
        $ her_SC.say(".........","body_17")
        $ her_SC.say("Sorry about that, he thinks he's always right and it annoys me.","body_75")
        m "Not unlike you, miss Granger..."
        $ her_SC.say("I suppose you have a point...","body_203")
        m "From now on I hope it's clear."
        $ her_SC.say("Yes, professor Dumbledore.","body_199")
        m "So, have you thought about emotions and their usefulness in the practice of magic?"
        $ her_SC.say("Yes, first I tried to cast a spell while thinking of the behavior of those Slytherin girls.","body_16")
        $ her_SC.say("It made me angry and confused so I lost my focus and failed miserably.","body_82")
        $ her_SC.say("I don't think it helps at all.","body_17")
        m "That's your problem Miss Granger, you think you know the answer and don't follow my instructions."
        m "I don't care about the behavior of those girls."
        $ her_SC.say("What professor! You don't care?!","body_72")
        g9 "{size=-2}(Oh I do care, just not in the way you think){/size}"
        m "For this exercise, Miss Granger, for this exercise. Don't get on your high horse."
        $ her_SC.say(".........","body_70")
        $ her_SC.say("Sorry about that, {w=0.5}again.","body_08")
        m "I need you to focus on what those girls do with professors, not their behavior in general."
        $ her_SC.say("But...","body_183")
        m "Last time you were talking about your sacred duty and at the first hurdle you hesitate."
        $ her_SC.say("{size=-2}(\"Sacred\"? Don't exagerate old man){/size}","body_73")
        $ her_SC.say("{size=-2}(Or not! Maybe I'll be remembered later for being the savior of house Gryffindor){/size}","body_182")
        $ her_SC.say("Yes, you're right! It {b}is{/b} my sacred duty!","body_46")
        g9 "{size=-2}(And it works every time, it's too easy... She looks so proud of herself){/size}"
        $ her_SC.say("I'll do my best, professor!","body_183")
        g9 "I'm excited too... uh, I'm sure you will."
        $ her_SC.say("I'm glad you have such a high confidence in me.","body_57b")
        m "And I'm glad you're starting to believe in this. I think you have a very good potential to master this branch of magic."
        $ her_SC.say("You seem tired professor.","body_08")
        g11 "{size=-2}(Tired of waiting to annihilate your ass){/size}"
        $ her_SC.say("Yes, professor?","body_82")
        g9 "Yes we can!"
        m "Uh, I mean, I'm sure I'll tire you out soon enough, Miss Granger. How about you get some sleep?"
        $ her_SC.say("Sleep? I must study first.","body_16")
        m "I wasn't thinking about that but you're right, time to go to bed!"
        m "Just make sure to think about what you learned today."
        $ her_SC.hideScreen()
        with d3
        "You dismiss Hermione."
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Hmm, I wonder what he {b}was{/b} thinking about){/size}","head_exp/16")
        $ her_SC.sayHead("{size=-4}(Probably all the problems caused by those harlots){/size}","head_exp/18")
        $ her_SC.sayHead("{size=-4}(Well I will never be like them, so no need to worry){/size}","head_exp/34")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 3
        jump l_tutoring_end

    elif v_tutoring == 3:   # Whoring lvl 3
        $ her_SC.say("First sir, I want to apologize for doubting you.","body_14")
        m "Yes?"
        $ her_SC.say("Your \"atypical\" method works!","body_34")
        m "{size=-2}(Impossible){/size}"
        m "It works? I mean yes, naturally it works!"
        m "I'm glad you've succeeded. Now tell me more."
        $ her_SC.say("I managed to levitate a heavy rock while thinking about the behavior of two girls I saw earlier in the library.","body_127")
        $ her_SC.say("Usually I only manage to move small rocks. I don't know, I felt kind of warm inside thinking about that.","body_207")
        her "It felt weird but... {w=0.5}good at the same time."
        m "{size=-2}(She is so ignorant of life, unbelievable){/size}"
        m "You've never felt such a sensation before?"
        $ her_SC.say("Generally I get angry and rush to stop such behavior.","body_140")
        $ her_SC.say("But yesterday, I don't know, I just watched without interrupting them.","body_182")
        $ her_SC.say("And when I pictured it, as you told me to, it worked.","body_183")
        $ her_SC.say("I feel at the same level as those harlots, I'm so ashamed.","body_187")
        m "But you succeeded."
        g9 "{size=-2}(To my surprise){/size}"
        $ her_SC.say("Yes! With this method I'll have better grades in my tests and win the House Cup for Gryffindor!","body_208")
        g9 "{size=-2}(In your dreams){/size}"
        m "Good, good. Now I want to know more about those two girls."
        $ her_SC.say("It's not very relevant, professor. And I'm not sure this is appropriate.","body_203")
        m "How will you improve yourself if I can't guide you?"
        m "And for that, I must know more."
        $ her_SC.say("Alright, but it's embarassing.","body_203")
        g9 "{size=-2}(Ooh, I hope they were naked){/size}"
        $ her_SC.say("I went to the library to study interactions between plants...","body_16")
        g11 "{size=-2}(Yeah, yeah, come on){/size}"
        $ her_SC.say("... and I heard muffled sounds.","body_188")
        $ her_SC.say("I was hoping to catch a teacher doing bad things with one of those Slytherin whores.","body_203")
        $ her_SC.say("I slowly headed towards the sounds and I discovered two girls in an alcove.","body_183")
        $ her_SC.say("I remained hidden to observe them.","body_209")
        g11 "{size=-2}(Come on!){/size}"
        $ her_SC.say("Yes, professor?","body_205")
        m "Yes, no, please continue."
        $ her_SC.say("They were kissing passionately.","body_182")
        g9 "And? And?"
        $ her_SC.say("And a moment later they began to...","body_127")
        $ her_SC.say("They began to...","body_182")
        $ her_SC.say("They began to touch their breasts!","body_210")
        m "They were naked, I hope?"
        $ her_SC.say("What?","body_190")
        her "No, fortunately they were dressed."
        $ her_SC.say("How can such a thing happen in our beloved school!","body_191")
        m "But you kept watching, didn't you?"
        $ her_SC.say("Only for educational purposes.","body_203")
        g9 "{size=-2}(\"Educational purposes\", haha, never heard a worse excuse){/size}"
        m "And during all this time you didn't feel a certain need?"
        $ her_SC.say("To my shame, yes. Like I said before, I felt kind of warm inside.","body_203")
        $ her_SC.say("Like when I have to pee but... different. Better.","body_199")
        m "This good sensation, next time you experience it, let it come."
        $ her_SC.say("But...","body_183")
        m "It's the only way to get better, miss Hermione."
        m "If you suppress it, it won't work."
        $ her_SC.say("Ok...{w=0.3} I'll try my best.","body_203")
        her "But to be honest, sir, I thought you were going to punish those two sluts."
        m "Can you provide proof of their crime? No?"
        m "Even I can't punish students without proof of any wrongdoing."
        g11 "{size=-2}(With the possible exception of you!){/size}"
        m "Anyway, you've done well. I think it will be enought for this lesson."
        m "Remember well what I just told you and good night!"
        $ her_SC.say("Good night, professor.","body_06")
        $ her_SC.hideScreen()
        with d3
        "You dismiss Hermione."
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Well, I'll try to investigate those two girls again){/size}","head_exp/12")
        $ her_SC.sayHead("{size=-4}(Like a real anthropologist){/size}","head_exp/18")
        $ her_SC.sayHead("{size=-4}(Yes, that's right, Hermione the anthropologist!){/size}","head_exp/35")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 4
        jump l_tutoring_end

    elif v_tutoring == 4:   # Whoring lvl 5
        m "So, any luck with your \"studies\"?"
        $ her_SC.say("Yes! When you hear the results of my hunt, you'll be proud of me!","body_74")
        m "{size=-2}(\"Hunt\"?){/size}"
        m "Your \"hunt\" Miss Hermione?"
        $ her_SC.say("Yes professor!","body_75")
        $ her_SC.say("Like an explorer in the wild jungle, I tracked those two filthy animals.","body_157")
        $ her_SC.say("With success, sir!","body_80b")
        $ her_SC.say("Hogwarts has so many dark and discreet corners...","body_82")
        $ her_SC.say("Believe me, it wasn't easy, professor.","body_157")
        m "I'm sure you gave it your best."
        m "But right now I await your report."
        $ her_SC.say("Yes, but before that I want to clarify that my report is purely for scientific purposes.","body_205")
        m "{size=-2}(Sure...){/size}"
        $ her_SC.say("So I tracked down those two tarts to an area in the attic.","body_16")
        $ her_SC.say("Which, by the way, seems to be the meeting place for girls of this... sort.","body_17")
        m "And what is your opinion on them?"
        $ her_SC.say("At least they don't sleep with professors in exchange for house points.","body_08")
        $ her_SC.say("","body_17")
        m "And that's it? No \"this behavior must be severely punished\" ?"
        m "Do you find girls of this sort attractive, miss Hermione?"
        $ her_SC.say("What? Lesbians? I'm not... I... no way I...","body_183")
        m "Alright, alright, back to your report if you please."
        $ her_SC.say("{size=-2}(I'm not a lesbian...{w=0.3} I think...){/size}","body_199")
        $ her_SC.say("{size=-2}(Hermione, girl, pull yourself together! You're not a harlot!){/size}","body_206")
        $ her_SC.say("No, I'm not!","body_184b")
        m "Excuse me?"
        $ her_SC.say("Uh, yes, my report. My {b}scientific{/b} report.","body_183")
        m "{size=-2}(Yeah, we get it..){/size}"
        $ her_SC.say("So, like before, they started by kissing passionately.","body_182")
        $ her_SC.say("With the tongue and everything!","body_189")
        menu:
            "-Start to jerk off while she is talking-":
                $ d_flag_01 = True
                $ her_SC.hideScreen()
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
            "Do nothing.":
                pass
        $ her_SC.say("","body_183")
        g9 "And? And?"
        $ her_SC.say("They pulled up their shirts and caressed each others breasts.","body_182")
        $ her_SC.say("{size=-2}(Their beautiful and tempting breasts){/size}","body_196")
        $ her_SC.say("Later those nasty girls raised their skirts and started to touch each other \"there\" while kissing.","body_212")
        $ b_her_tears = True
        $ her_SC.say("{size=-2}(I can't believe I said that!){/size}","body_213","tears_03b")
        $ her_SC.say("They were very excited and I could see their panties become wet.","body_196")
        $ her_SC.say("Disgusting.","body_214")
        if d_flag_01:
            g9 "{size=-2}(Yes... yes...){/size}"
        $ b_her_tears = False
        $ her_SC.say("One of the girls went crazy and inserted her fingers into the other's \"thing\" and worked them furiously.","body_138")
        $ her_SC.say("Soon imitated by her girlfriend.","body_212")
        $ her_SC.say("Those whores came so hard they had to bite their lips not to scream.","body_215")
        if d_flag_01:
            her "{size=-2}(And me too){/size}"
            $ her_SC.hideScreen()
            with d3
            show screen white
            pause.1
            hide screen white
            pause.2
            show screen white
            pause .1
            hide screen white
            with hpunch
            g11 "Me too! YES!"
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            pause
            show screen bld1
            with d3
            $ her_SC.say("Professor!","body_187")
            show screen genie_jerking_sperm_02
            with d3
            m "You enjoyed it too so don't act innocent."
            hide screen genie_jerking_sperm_02
            show screen genie
            with d3
            $ mad = +7
            $ d_flag_01 = False
        else:
            m "You enjoyed it too."
        $ her_SC.say("Maybe...","body_203")
        m "Anyway, I hope it was revealing."
        $ her_SC.say("\"Revealing\"? I'm not sure what you mean by that.","body_08")
        $ her_SC.say("You're the headmaster, act as such!","body_02")
        $ her_SC.say("Do all you can to stop those acts of debauchery!")
        $ her_SC.say("","body_12")
        m "Yes, of course."
        m "{size=-2}(Hypocrite){/size}"
        her "{size=-2}(Old pervert){/size}"
        m "You said that those girls became wet."
        g9 "Weren't you a little too?"
        $ her_SC.say("When I went to bed I noticed it, yes.","body_199")
        $ her_SC.say("Apparently bad fluids are released from your body when you have faced such acts.","body_206")
        m "No, they aren't bad. It happens when you're excited."
        $ b_her_tears = True
        $ her_SC.say("No way! I can control myself!","body_216","tears_01b")
        $ b_her_tears = False
        $ her_SC.say("","body_187")
        m "No one can control their base desires."
        m "Consider this well and enjoy your night, Miss Hermione."
        $ her_SC.say("Good night, professor.","body_29")
        $ her_SC.hideScreen()
        with d3
        "You dismiss Hermione."
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(I enjoyed it too much. Maybe I'm becoming a pervert as well){/size}","head_exp/6")
        $ her_SC.sayHead("{size=-4}(I lost control, it won't happen again!){/size}","head_exp/13")
        $ her_SC.sayHead("{size=-4}(Good thing I'm not a degenerate like those filthy girls){/size}","head_exp/18")
        hide screen hermione_stand_f
        with d3

        $ v_tutoring = 5
        jump l_tutoring_end

    elif v_tutoring == 5:   # Whoring lvl 8
        m "Bravo, last time you experienced your first \"emotion\"."
        $ her_SC.say("Yes, I remember but I still don't see the link with magic.","body_08")
        m "{size=-2}(Me neither...){/size}"
        m "If you want to progress, you have to go a little further than a simple observation."
        m "You'll need to participate."
        $ her_SC.say("What! No way I'll participate in such debauchery!","body_217")
        $ her_SC.say("How can you even suggest such a thing!","body_05")
        m "Oh you don't have to go that far in one go."
        $ her_SC.say("I'm not sure I want to go there at all.","body_16")
        m "How many times do I have to remind you why you're doing this?"
        $ her_SC.say("Yes but...","body_02")
        m "But what?"
        $ her_SC.say("A girl like me shouldn't stoop to such practices.","body_17")
        m "A girl like you should use all means at their disposal in order to excel."
        her "..........."
        $ her_SC.say("Alright, but this must remain between us.","body_203")
        $ her_SC.say("You cannot disclose this to other professors, especially professor Snape!","body_71")
        m "Oh, I have no intention of shar.. speaking of you with professor Snape."
        g9 "{size=-2}(You're mine){/size}"
        $ her_SC.say("Well, what must I do now?","body_127")
        m "Come here."
        $ her_SC.hideScreen()
        with d3
        
        $ her_SC.chibi.walk(400,300,1)
        show screen blkfade
        with d1
        pause.5
        
        hide screen genie
        show screen ctc
        show screen no_groping_01
        with d1
        hide screen blkfade
        with d5
        pause
        m "Have you ever touched yourself?"
        hide screen ctc
        $ her_SC.say("Professor!","body_157")
        show screen groping_01
        with d7
        ">You touch her leg with your hands."
        m "Please answer the question, Miss Granger. Have you ever touched yourself?"
        $ her_SC.say("No, it's... it's wrong!","body_203")
        m "But when you looked at these girls, you felt certain emotions."
        $ her_SC.say("Yes and ?","body_209")
        m "You didn't feel the need to touch yourself?"
        $ her_SC.say("Yes... but I resisted.","body_205")
        ">You start to caress her thigh."
        $ her_SC.say("Professor...","body_182")
        m "And you felt those emotions without even touching yourself."
        $ her_SC.say("Yes...","body_183")
        g9 "{size=-2}(What a slut){/size}"
        if whoring <= 12 or custom_bra >0:
            ">You move forward to her panties."
        else:
            ">You move forward to her pussy."
        $ her_SC.say("","body_182")
        m "Good."
        hide screen groping_01
        show screen no_groping_01
        ">You stop caressing her."
        $ her_SC.say("Why... why did you stop?","body_206")
        m "Oh, because I need you to think about all this before we meet again."
        $ her_SC.say("But...","body_206")
        m "Good night, my dear."
        $ her_SC.say("Good night, professor.","body_29")
        $ her_SC.hideScreen()
        show screen blkfade
        with d3
        hide screen no_groping_01
        "You dismiss Hermione."
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(This is wrong...){/size}","head_exp/12")
        $ her_SC.sayHead("{size=-4}(I shouldn't listen to him){/size}","head_exp/15")
        $ her_SC.sayHead("{size=-4}(And yet...){/size}","head_exp/16")
        hide screen hermione_stand_f
        with d3

        $ v_tutoring = 6
        jump l_tutoring_end

    elif v_tutoring == 6:   # Whoring lvl 11
        m "Miss Hermione, I wanted to remind you that this is not a formal lesson."
        m "You need not wear your uniform for these lessons."
        m "At least take off that tie, I know it gets uncomfortable after all these hours."
        $ her_SC.say("The school rules are very strict about this, professor.","body_02")
        m "You have my permission, Miss Granger."
        $ her_SC.say("..........","body_199")
        $ her_SC.say("Right. But only when I come to see you in the evenings.","body_12")
        $ her_SC.say("{size=-2}(I have to be careful with my reputation.){/size}","body_203")
        m "It's a deal."
        show screen blkfade
        with d3
        ">Hermione takes off her tie."
        ##$ v_her_current_shirt = "shirt1_without_tie"
        ##$ v_her_shirt = v_her_current_shirt
        hide screen hermione_blink
        show screen hermione_blink
        $ her_SC.hideScreen()
        hide screen blkfade
        with d3
        $ her_SC.say("","body_188")
        m "There. Doesn't that feel better?"
        $ her_SC.say("Actually, it does, sir. Thank you.","body_208b")
        m "So, have you started practicing my teachings?"
        $ her_SC.say("I don't even know where to start.","body_08")
        m "You see, the secret is to stimulate appropriate areas."
        m "Areas which are more sensitive than others."
        $ her_SC.say("You mean my intimate areas, sir?!","body_203")
        m "Well, they're called intimate for a reason."
        m "You said you've never touched yourself because it was wrong."
        m "But it's never wrong to exercise ones body in order to reach a new level of consciousness."
        g4 "{size=-2}(The things I have to make up...){/size}"
        m "You can begin with your breasts, for example."
        m "But you shouldn't only caress your nipples but also grab your tits and squeeze them."
        m "And in the meanwhile, you can think of those two girls."
        g9 "Or what you want to do with those girls."
        $ her_SC.say("What makes you think... No, I don't want...","body_208")
        $ her_SC.say("I definitely don't want to have {b}anything{/b} to do with those harlots!","body_216")
        m "Don't lie to yourself. It's obvious that you feel a form of attraction to those two girls."
        $ her_SC.say("I...{w=0.3} I honestly don't know what to think anymore.","body_207")
        her "At the moment my feelings are so confusing..."
        g9 "{size=-2}(Exactly what I was hoping){/size}"
        $ her_SC.say("I'm happy to earn points for my house and at the same time I feel so ashamed.","body_145")
        her "And the same goes for your lessons."
        m "Yet you can't deny your progress in the practice of magic."
        $ her_SC.say("...{w=0.2} Yes...{w=0.2} perhaps you're right.","body_157","tears_03b")
        m "You have to let it go, Miss Hermione, follow your instincts!"
        g9 "{size=-2}(Grab my cock and wank it savagely!){/size}"
        $ b_her_tears = False
        $ her_SC.say("I'm not sure if...","body_154")
        m "Enough procrastination, time for practice!"
        m "Come here."
        show screen blkfade
        with d1
        pause.5
        ">Hermione walks towards your desk."
        hide screen hermione_blink
        hide screen genie
        ">You grab her tits and massage them softly."
        show screen ctc
        show screen groping_03
        with d1
        hide screen blkfade
        with d5
        $ her_SC.say("","body_182",xpos=160)
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "Like I said, it's important you learn how to properly stimulate your \"emotional\" body areas."
        m "It's not enough if I do it myself, you need to practice when you're alone."
        $ her_SC.say("","body_182b")
        m "Like in your bed or in the shower, for example."
        ">You keep massaging her tits..."
        $ her_SC.say("","body_182")
        ">You feel her nipples becoming hard."
        $ her_SC.say("Yes but...{w=0.3} Professor, it's inappropriate for a girl of good education!","body_183")
        m "Don't let old prejudices weigh you down. You're a girl with great potential."
        ">You gently squeeze her nipples through the fabric."
        $ her_SC.say("Ah, thank you professor.","body_196")
        m "A girl with a brilliant mind."
        ">You increase your grip on her nipples."
        m "A girl who will become a woman of exception."
        $ her_SC.say("Ahh yes... I'm already a woman of exception you fool.","body_195")
        m "Fool?"
        ">You firmly pinch her nipples."
        $ her_SC.say("Ahhh yesss, not that hard, yesss...","body_138")
        ">You abruptly stop."

        show screen blkfade
        with d5
        $ her_SC.hideScreen()
        hide screen groping_03
        show screen genie_and_hermione
        hide screen blkfade
        with d1
        
        $ her_SC.say("Don't stop, you idiot!","body_218")
        show screen blkfade
        ">She moves away from the desk."
        hide screen genie_and_hermione
        show screen genie
        show screen hermione_blink
        hide screen blkfade
        with d1
        
        $ her_SC.say("...........","body_206")
        $ her_SC.say("Sorry, professor.","body_187")
        m "Lesson is over. Time to practice by yourself."
        m "Good night my little witch."
        $ her_SC.say("Good night professor and thank you for this lesson.","body_74")
        $ her_SC.say("{size=-2}(This too short of a lesson){/size}","body_17")
        $ her_SC.hideScreen()
        with d3
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(\"My little witch?\"){/size}","head_exp/4")
        $ her_SC.sayHead("{size=-4}(Why not, after all...){/size}","head_exp/6")
        hide screen hermione_stand_f
        with d3

        $ lock_public_favors = True
        $ v_tutoring = 7
        jump l_tutoring_end

    elif v_tutoring == 7:   # Whoring lvl 14
        m "So, Miss Hermione, have you practiced my teachings?"
        $ her_SC.say("Yes...{w=0.2} a little.","body_203")
        m "And?"
        $ her_SC.say("It feels even better when I'm naked.","body_80b")
        $ her_SC.say("{size=-2}(Oh no, I should never have said that){/size}","body_206")
        m "Well come here and undress, we'll practice."
        $ her_SC.say("Completely?!","body_207")
        m "No, only the top will suffice."
        g9 "{size=-2}(For the moment...){/size}"
        $ her_SC.say("I'll be showing you my breasts without even earning any points?","body_08")
        m "You can't have both points and lessons."
        $ her_SC.say("Ok...","body_208")
        $ her_SC.hideScreen()
        hide screen hermione_blink
        show screen hermione_04
        ##call her_pose("shirt raised")
        $ lift_shirt = True
        $ her_SC.say("Like that?","body_203")
        if custom_bra >=1 and badges and custom_outfit_old <= 0:
            m "Without your bra Miss Hermione... and come here."
        else:
            m "Yes and now come here."
        $ badges = False
        $ her_SC.say("........","body_184b")
        $ her_SC.say("","body_198")
        m "Now."
        show screen blkfade
        with d1
        pause.5
        ">Hermione slowly walks towards your desk."
        ">She tries not to bounce her tits without much success..."
        hide screen hermione_04
        hide screen genie
        show screen ctc
        show screen genie_and_tits_01
        with d1
        ##$ v_her_bra = 0
        hide screen blkfade
        with d5
        $ her_SC.say("","body_198",xpos=160)
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "Now let's get serious if you want to."
        g9 "{size=-2}(Well, even if you don't...){/size}"

        $ her_SC.hideScreen()
        with d3
        show screen blkfade
        with d3
        ">You grab her tits and squeeze them gently."
        hide screen blkfade
        show screen chair_02
        hide screen bld1
        hide screen genie_and_tits_01
        show screen groping_naked_tits
        with fade
        pause

        $ her_SC.say("Professor, what are you doing?","body_199")
        g9 "Teaching you, dear, teaching you."
        m "Doesn't it feel good?"
        $ her_SC.say("A little...","body_198")
        m "Your hard nipples say the contrary."
        m "I can stop if you want."
        $ her_SC.say("Yeah sure!","body_195")
        $ her_SC.say("Suck them professor.","body_212")
        g9 "As you wish, princess."
        $ her_SC.say("","body_212")
        ">You suck her nipples with devotion."
        $ b_her_tears = True
        $ her_SC.say("Yes {image=textheart} like that.","body_212","tears_03c")
        ">You start to chew on her nipples."
        $ her_SC.say("Ah, noo, don't...","body_219")
        ">You chew on them even harder."
        $ her_SC.say("Not that hard, I will...","body_215")
        g9 "{size=-2}(Time for the grand finale){/size}"
        if whoring <= 12 or custom_bra >0:
            ">You quickly slip your hand into her panties and rub her pussy furiously."
        else:
            ">You quickly move your hand toward her pussy and rub it furiously."
        $ b_her_tears = False
        $ her_SC.say("Yes! {image=textheart}","body_142")
        her "I... I..."
        g9 "Came, my dear."
        show screen blkfade
        with d5
        pause
        ##call her_pose()
        $ lift_shirt = False
        $ badges = True
        $ her_SC.hideScreen()
        hide screen chair_02
        hide screen groping_naked_tits
        hide screen genie
        hide screen blkfade
        show screen genie_and_hermione
        with d1
        $ her_SC.say("Is the lesson over professor?","body_156")
        m "Not if you don't want it to be."
        her "Maybe it's enough for tonight."
        $ her_SC.say("After all, you have a lot of work to do.","body_153")
        m "Sure."
        m "But before that I have a little present for you."
        $ the_gift = "01_hp/18_store/gifts/7.png"
        show screen gift
        with d3
        ">You give an assortment of adult magazines to Hermione."
        hide screen gift
        m "I hope this will help you in your studies."
        $ her_SC.say("Yes, certainly.","body_155")
        her "Thank you and good night professor."
        m "Good night dear child."
        $ her_SC.hideScreen()
        show screen blkfade
        with d3
        hide screen genie_and_hermione
        "You dismiss Hermione."
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(I'm such a slut...){/size}","head_exp/6")
        $ her_SC.sayHead("{size=-4}(Coming in front of my professor){/size}","head_exp/16")
        $ her_SC.sayHead("{size=-4}(I definitely need to do that again){/size}","head_exp/18")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 8
        jump l_tutoring_end

    elif v_tutoring == 8:   # Whoring lvl 17
        m "Miss Hermione, is my office really that cold that you need to wear your vest?"
        m "I don't want you getting all hot and sweaty."
        m "{size=-2}(Oh wait...){/size}"
        $ her_SC.say("It's the vest or the tie but I must have a symbol of my house!","body_16")
        m "Alright, alright, you can wear your tie if you insist."
        $ her_SC.say("{size=-2}(I've never seen him give in so quickly...){/size}","body_206")
        $ her_SC.say("{size=-2}(I did well to exercise my authority!){/size}","body_220")
        show screen blkfade
        with d3
        ">Hermione takes off her vest and puts her tie back on."
        ##$ v_her_current_shirt = "shirt2"
        ##$ v_her_shirt = "shirt2_tucked"
        hide screen hermione_blink
        show screen hermione_blink
        $ her_SC.hideScreen()
        hide screen blkfade
        with d3
        $ her_SC.say("","body_188")
        m "So tell me, were your readings enlightening?"
        $ her_SC.say("I'm not sure if \"readings\" is the right term but yes. Very \"stimulating\" too.","body_208b")
        m "Maybe it's time to discover new areas to stimulate."
        $ her_SC.say("You mean my pussy, right?","body_08")
        $ her_SC.say("I'm not an idiot, professor.","body_12")
        m "If it doesn't suit you, we can stop here."
        $ her_SC.say("And if I said stop?","body_17")
        g4 ".........."
        $ her_SC.say("Haha, you should have seen your face!","body_220")
        $ her_SC.say("With all your recent lessons you can imagine that this area isn't a *no man's land* any more.","body_46")
        g4 "Have you slept..."
        $ her_SC.say("No I haven't! I'm not a harlot who offers her pussy to every boy around.","body_217")
        m "{size=-2}(Good, your pussy is mine alone){/size}"
        $ her_SC.say("","body_70")
        g9 "{size=-2}(Although I may agree to share it with other girls...){/size}"
        m "I'm happy you're behaving honorably, Miss Hermione."
        $ her_SC.say("Ha, who'd have guessed!","body_203")
        m "Yes, I'm glad that my favorite student is not wasting her precious time with boys."
        her "Sure...{w=0.3} {size=-4}old hypocrite{/size}."
        m "Enough of this! Now take off your shirt and come here."
        $ her_SC.say("Here we go for another \"lesson\".","body_08")
        $ her_SC.hideScreen()
        hide screen hermione_blink
        show screen hermione_04
        ##$ v_her_shirt = 0
        $ wear_shirts = False
        $ h_body = "01_hp/13_hermione_main/body_203.png"
        show screen hermione_main
        with fade
        if custom_bra >=1 and badges and custom_outfit_old <= 0:
            m "And your bra..."
            $ badges = False
        $ her_SC.say("........","body_184b")
        show screen ctc
        pause
        show screen blkfade
        $ her_SC.hideScreen()
        with d3
        
        hide screen blkfade
        $ her_SC.chibi.walk(400,300,1)
        show screen blkfade
        with d1
        pause.5
        hide screen genie
        show screen no_groping_06
        hide screen blkfade
        with d5
        pause
        hide screen ctc
        $ her_SC.say("","body_198",xpos = 160)
        hide screen blkfade
        with d5
        pause
        hide screen ctc
        $ her_SC.say("And free tits again, enjoy!","body_195")
        m "I definitely intend to."
        g9 "Lift your skirt."
        ##call her_pose("skirt raised")
        $ skirt_up = True
        $ her_SC.say("","body_188")
        show screen ctc
        pause
        hide screen ctc
        if whoring >= 13 and custom_bra == 0:
            $ her_SC.say("You love my pussy don't you?","body_205")
            g9 "Oh yes, I love your smell, especially when you're wet."
            $ her_SC.say("Professor...","body_208")
            hide screen no_groping_01
            show screen groping_06
            with d3
            ">You caress her clit."
            $ her_SC.say("Professor!","body_206")
        else:
            $ her_SC.say("You love my panties don't you?","body_205")
            g9 "Oh yes, I love their smell, especially when you're wet."
            $ her_SC.say("Professor...","body_208")
            hide screen no_groping_01
            show screen groping_06
            with d3
            ">You caress her clit through the fabric."
            $ her_SC.say("Professor!","body_206")
            m "Now take them off."
            show screen blkfade
            with d5
            ">She slowly lowers her panties."
            $ her_SC.hideScreen()
            hide screen groping_06
            show screen no_groping_06
            hide screen blkfade
            $ b_her_panties_off = True
            $ her_SC.say("","body_198")
            show screen ctc
            $ panties = False
            pause
            hide screen ctc
        m "What's great, you see, is that I have two hands."
        m "One can caress your clit while the other can play with your pussy."
        ">You move from words to deeds and penetrate her already wet pussy with ease."
        hide screen no_groping_06
        show screen groping_06
        with d5
        $ her_SC.say("Yes, you're probably right.","body_195")
        m "Probably?!"
        ">While you're moving your finger in her pussy, you take over her clit with your thumb."
        $ her_SC.say("Haa {image=textheart}, I'm only your humble student, I wouldn't know such naughty things.","body_212")
        m "One finger is rarely enough even with a tight pussy like yours."
        ">You insert a second finger in her tight and warm pussy..."
        $ her_SC.say("Yesss {image=textheart}, I'll try to remember your teachings.","body_212")
        ">You increase the pace and feel her pussy tighten on your fingers."
        m "Maybe a third finger?"
        $ b_her_tears = True
        $ her_SC.say("Don't be so bold.","body_195","tears_01")
        ">Her whole body starts shaking as you increase your ramming."
        hide screen groping_06
        show screen groping_06b
        with d1
        $ her_SC.say("Noo {image=textheart}{w=0.2} not so fast I will...","body_219")
        ">You increase your pace even more."
        $ her_SC.say("I will I will...","body_215")
        g9 "Time to get serious."
        ">You force your soaked thumb into her butthole."
        $ b_her_tears = False
        $ her_SC.say("Haaaaa {image=textheart} yesss {image=textheart}.","body_215")
        g9 "Lucky girl."
        show screen blkfade
        with d5
        pause
        ##call her_pose()
        $ her_SC.hideScreen()
        hide screen groping_06b
        hide screen genie
        hide screen blkfade
        show screen no_groping_01
        with d1
        $ her_SC.say("I'm sure this lesson will be of great help tonight.","body_156")
        $ her_SC.say("And the other nights {image=textheart}.","body_138")
        m "Always glad to help my little witch in her studies."
        $ her_SC.say("\"Studies\", yes, that's right.","body_156")
        m "And to aid your studies I have even more scientific materials."
        $ the_gift = "01_hp/18_store/gifts/8.png"
        show screen gift
        with d3
        ">You give an assortment of porn magazines to Hermione."
        hide screen gift
        $ her_SC.say("You can be certain that I'll study them profoundly.","body_155")
        $ her_SC.say("Thank you and good night professor.","body_156")
        m "Good night, my favorite little witch."
        $ her_SC.hideScreen()
        show screen blkfade
        with d3
        hide screen no_groping_01
        "You dismiss Hermione."
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Favorite...){/size}","head_exp/6")
        $ her_SC.sayHead("{size=-4}(There's another one?){/size}","head_exp/7")
        $ her_SC.sayHead("{size=-4}(I'll do my best to remain his favorite!){/size}","head_exp/35")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 9
        jump l_tutoring_end

    elif v_tutoring == 9:   # Whoring lvl 20
        m "So, Miss Hermione, have you had an enjoyable night?"
        $ her_SC.say("You shouldn't ask such things, Professor.","body_127")
        m "I have to make sure my students have a pleasant nights rest."
        $ her_SC.say("With your teachings and your \"scientific\" literature, indeed.","body_157")
        $ her_SC.say("I'll become proficient in human anatomy with all this documentation.","body_208b")
        m "Do you need some scientific instruments for your research?"
        $ her_SC.say("They could come in handy.","body_209")
        $ her_SC.say("As long as it's not your dick.","body_203")
        $ her_SC.say("{size=-2}(Not that I don't appreciate it but no points no cock!){/size}","body_220")
        m "Miss Hermione! This is a serious matter!"
        $ her_SC.say("Sure...","body_17")
        m ".........."
        $ her_SC.say("So what's my gift this time?","body_08")
        $ the_gift = "01_hp/18_store/gifts/12.png"
        show screen gift
        with d3
        ">You give the vibrator to Hermione"
        hide screen gift
        with d3
        $ her_SC.say("And I suppose you want me to test this in front of you?","body_16")
        g9 "Of course."
        $ her_SC.say("Where is the educational purpose in all of this?","body_17")
        m "Good question. Improving your skills?"
        $ her_SC.say("At what? Magic?","body_207")
        m "Certainly."
        her "........."
        $ her_SC.say("I have one request though.","body_204")
        $ her_SC.say("If I'm going to masturbate I don't want to be the only one. So enjoy the free show.","body_182")
        g9 "With pleasure!"
        ">You reach under the desk and grab your cock."
        $ her_SC.hideScreen()
        hide screen blktone
        with d3
        hide screen genie
        show screen genie_jerking_off
        with d3
        ##call her_pose("fingering")
        $ fingering = True
        $ h_body = "01_hp/13_hermione_main/body_219.png"
        show screen hermione_main
        with d3
        her "{size=-2}(Thinking of the headmaster masturbating makes me wet already {image=textheart}){/size}"
        $ her_SC.say("{size=-2}(I've become such a whore. Not that I enjoy it all that much though){/size}","body_220")
        $ her_SC.say("So... where do we start?","body_190")
        if custom_bra == 0:
            m "Take off your shirt and bra, I want to see your tits."
            ##$ v_her_bra = 0
        else:
            m "Take off your shirt, I want to see your tits."
        show screen blkfade
        with d5
        $ her_SC.hideScreen()
        hide screen hermione_blink
        hide screen blkfade
        with d1
        ##$ v_her_shirt = 0
        $ badges = False
        $ wear_shirts = False
        $ h_body = "01_hp/13_hermione_main/body_182.png"
        show screen hermione_main
        pause
        her "You love them don't you?"
        $ h_body = "01_hp/13_hermione_main/body_195.png"
        show screen hermione_main
        g9 "Oh yes..."
        her "Having watched the other girls I now know why."
        her "Those breasts are so tempting."
        $ her_SC.say("Big or small, I want to hold them in my hands and suck the nipples.","body_219")
        g9 "Me too, me too!"
        m "Now lift your skirt!"
        show screen blkfade
        with d5
        $ her_SC.hideScreen()
        hide screen blkfade
        with d1
        ##call her_pose("fingering skirt raised")
        $ skirt_up = True
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_01.png"
        $ b_her_tears = True
        $ h_body = "01_hp/13_hermione_main/body_205.png"
        show screen hermione_main
        pause
        her "Good idea."
        $ her_SC.say("Sometimes I wish I could do this with others girls.","body_190")
        $ her_SC.say("Masturbate naked in front of each other.","body_196")
        if whoring <= 12 or custom_bra >0 and panties:
            g9 "Yes go on, take off your panties!"
            show screen blkfade
            with d5
            $ her_SC.hideScreen()
            hide screen blkfade
            with d1
            $ panties = False
            $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_02b.png"
            $ h_body = "01_hp/13_hermione_main/body_195.png"
            show screen hermione_main
            pause
            her "Your wish is my command."
            $ her_SC.say("And mine is to touch another girl's pussy.","body_212")
        else:
            $ her_SC.say("Touch her pussy like I'm touching mine now.","body_212")
        $ her_SC.say("Caress it.","body_219")
        $ her_SC.say("Insert my fingers into her wet pussy.","body_219")
        g11 "Yes, yes! Now the vibrator!"
        show screen blkfade
        with d5
        $ her_SC.hideScreen()
        hide screen blkfade
        with d1
        ##call her_pose("vibrator")
        $ vibrator = True
        $ h_body = "01_hp/13_hermione_main/body_142.png"
        show screen hermione_main
        pause
        her "Oh I had forgotten about it already."
        $ her_SC.say("I want to hear her moan as I work my fingers.","body_215")
        her "Hear her cum!"
        $ her_SC.say("Like me! Aaah yesssss! {image=textheart} {image=textheart}","body_215")
        #$ b_her_squirt = True # the squirting needs some work. Graphically, I mean.
        pause
        g11 "Ahh! You little whore!!!"
        show screen genie_jerking_sperm
        her "The vibrator... aaah I'm still cumming!!"
        show screen genie_jerking_sperm_02
        g11 "Take this!"

        show screen blkfade
        ">Hermione catches her breath and puts her clothes back on."
        with d5
        $ her_SC.hideScreen()
        hide screen genie_jerking_sperm_02
        hide screen her_naked
        show screen genie
        show screen hermione_blink
        hide screen blkfade
        with d3
        ##call her_pose()
        $ panties = True
        $ wear_shirts = True
        $ badges = True
        $ skirt_up = False
        $ b_her_tears = False
        $ fingering = False
        #$ aftercum = True   # the aftercum skirt is a bit overkill IMO. Maybe reduce the height of the stains and add some dripping down the legs.
        $ her_SC.say("I hope you enjoyed it as much I did.","body_154")
        m "Oh fuck yes, you're doing great, my little witch!"
        g9 "Very good!"
        $ her_SC.say("Thank you, professor.","body_153")
        m "After all this, you need to rest."
        $ her_SC.say("Oh yes. Good night professor.","body_155")
        m "Good night, my dirty little slut."
        "You dismiss Hermione."
        $ her_SC.hideScreen()
        hide screen hermione_blink
        show screen blkfade
        with d3
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Rest...){/size}","head_exp/16")
        $ her_SC.sayHead("{size=-4}(Not before I've played with this marvelous toy again){/size}","head_exp/18")
        $ her_SC.sayHead("{size=-4}(And again){/size}","head_exp/34")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 10
        jump l_tutoring_end

    elif v_tutoring == 10:   # Whoring lvl 23
        m "Miss Hermione, I see you still insist on wearing that tie."
        m "Don't you get tired of wearing it constantly?"
        $ her_SC.say("I suppose I do... But I'm proud of being a Gryffindor and I'm willing to make such a small sacrifice for my house.","body_82")
        $ her_SC.say("{size=-2}(It does get stifling quite often){/size}","body_214")
        $ h_body = "01_hp/13_hermione_main/body_205.png"
        show screen hermione_main
        m "Miss Hermione, I know how strongly you feel towards your house. There's no need to keep up appearances in this office."
        her "Are you sure, professor?"
        m "Miss Hermione, I think you will feel much better without that tie."
        g9 "{size=-2}(And even better when covered in my cum){/size}"
        $ her_SC.say("If you insist, professor.","body_208b")
        show screen blkfade
        with d3
        ">Hermione takes off her tie."
        ##$ v_her_current_shirt = "shirt3"
        ##$ v_her_shirt = "shirt3_tucked"
        $ her_SC.hideScreen()
        hide screen blkfade
        with d3
        $ h_body = "01_hp/13_hermione_main/body_188.png"
        show screen hermione_main
        m "So... I hope my lessons are paying off."
        $ her_SC.say("You mean, by making me more \"open\" to the wonders of adulthood?","body_08")
        m "Among other things..."
        $ her_SC.say("That's what I thought.","body_17")
        $ her_SC.say("But to be honest, I was looking forward to this lesson.","body_16")
        $ her_SC.say("{size=-2}(Maybe, I shouldn't have said that){/size}","body_18")
        her "{size=-2}(This will drive him crazy and he'll rape me savagely on his desk){/size}"
        $ her_SC.say("{size=-2}(Not that I would mind...){/size}","body_208b")
        $ her_SC.say("{size=-2}(And I could ask him for points afterwards){/size}","body_46")
        m "Miss Hermione? Are you alright?"
        $ her_SC.say("Yes professor! Sorry, I was thinking of my next exam.","body_209")
        m "Oh, I'm sure it's an important one. Maybe next lesson I can help you revise."
        $ her_SC.say("I would love that!","body_182")
        m "So, anal stimulation..."
        $ her_SC.say("Ah! I knew you would say that.","body_220")
        her "{size=-2}(Once again, not that I mind...){/size}"
        $ her_SC.say("{size=-2}(I'm such a whore, even the Slytherin girls can't compete...){/size}","body_213")
        m "Come again, Miss Hermione?"
        $ her_SC.say("In this school nobody can compete with me, right professor?","body_80b")
        $ her_SC.say("In any field!","body_220")
        m "In any field? I'm not sure."
        m "You still have things to learn..."
        $ her_SC.say("What?! What are we waiting for then?","body_217")
        ">She rips off her shirt and rushes to your desk."
        show screen blkfade
        $ her_SC.hideScreen()
        with d3
        ##$ v_her_shirt = 0
        ##$ v_her_bra = 0
        ##$ badges = False
        ##$ wear_shirts = False
        hide screen blkfade
        $ her_SC.chibi.walk(400,300,1)
        show screen blkfade
        with d1
        pause.5
        hide screen genie
        show screen groping_05
        hide screen blkfade
        with d5
        pause
        m "We haven't even started yet and you're already wet, my adorable slut."
        $ her_SC.say("It's you and your dirty talk!","body_203")
        her "Talking about anal insertions, asshole licking and... and..."
        $ her_SC.say("Fisting!","body_196")
        m "I never mentioned any of that."
        $ her_SC.say("Oh. You didn't?","body_214")
        $ her_SC.say("Well maybe you didn't but you {b}were{/b} thinking about it!","body_205")
        g9 "Maybe."
        g9 "Your ass is so luscious I could eat it."
        $ her_SC.say("My point exactly!","body_208b")
        $ her_SC.say("Enough talking, old man. Get to work!","body_157")
        m "I haven't even given you your gift yet!"
        m "I'll just put it where you'll be sure to find it."
        m "So, can we start the lesson?"
        $ her_SC.say("Yes for Merlin's sake!","body_183")
        m "But before that..."
        $ her_SC.say("If you say another word I swear I will go back to my dorm right now!","body_218")
        ">You suddenly insert the anal plug."
        $ her_SC.say("Yesss {image=textheart} like that!","body_212")
        ">You remove it just as quickly while giving her butt a loud slap."
        play sound sd_boing1
        with flashbulb
        play sound sd_slap
        with hpunch
        $ her_SC.say("Yessss more {image=textheart}.","body_219")
        g9 "As you wish, princess."
        ">You promptly insert and remove it."
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03d.png"
        $ b_her_tears = True
        $ her_SC.say("More!!","body_219")
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03b.png"
        $ her_SC.say("Aaaah {image=textheart}.","body_215")
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        m "You can touch yourself too, you know."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03d.png"
        $ her_SC.say("I can't.","body_215")
        her "{size=-2}(If I do, I will lose what little dignity I have left){/size}"
        $ her_SC.say("{size=-2}(But tonight...){/size}","body_215")
        m "I'll handle it then."
        ">You finger both her butthole and her pussy."
        $ her_SC.say("Nooo it's too much {image=textheart}.","body_215")
        g9 "Faster? No problem!"
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        $ her_SC.say("Aaah, you're killing me {image=textheart}.","body_142")
        $ her_SC.say("{size=-2}(And I love it){/size}","body_138")
        m "More fingers?"
        $ her_SC.say("No more pleassse.","body_154")
        m "Actually, it wasn't a question."
        $ her_SC.say("If you keep this pace I will...","body_142")
        ">You feel her muscles tighten on your fingers."
        $ her_SC.say("Come!!","body_215")
        g9 "Good girl."
        her "Keep it up, I..."
        $ her_SC.say("Yessss {image=textheart}.","body_215")
        m "I can keep this up as long as you please."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_04.png"
        $ b_her_tears = True
        $ her_SC.say("Yesss {image=textheart}, nooo I will die!","body_215")
        g9 "In ecstasy."
        $ her_SC.say("Aahh not again {image=textheart}.","body_215")
        hide screen groping_05b
        show screen no_groping_05
        m "I think you've had enough for one night."
        $ her_SC.say("Yes I... I better go.","body_219")
        m "You forgot your gift."
        ">You promptly insert the butt plug."
        with hpunch
        $ her_SC.say("Aaaaaaah.","body_215")
        hide screen no_groping_05
        show screen no_groping_05_desk
        $ her_SC.hideScreen()
        with d5
        ">She collapses panting on the desk."
        g9 "Best view in the world."
        show screen blkfade
        with d5
        ">After a while, she puts her shirt back on."
        ##call her_pose()
        $ badges = True
        $ wear_shirts = True
        $ b_her_tears = False
        hide screen no_groping_05_desk
        show screen genie
        show screen hermione_blink
        hide screen blkfade
        with d3

        #$ aftercum = True
        $ h_body = "01_hp/13_hermione_main/body_156.png"
        show screen hermione_main
        pause
        her "Thank you for everything, professor."
        $ her_SC.say("It was very...{w=0.5} enlightening.","body_153")
        $ her_SC.say("But please, try to go easy on me next time.","body_155")
        g9 "I have absolutely no idea what you mean by that."
        $ her_SC.say("Good night professor.","body_156")
        m "Good night, my dear anal whore."
        $ her_SC.say("Professor...","body_154")
        "You dismiss Hermione."
        $ her_SC.hideScreen()
        hide screen hermione_blink
        show screen blkfade
        with d3
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Finally tonight I'll just go to bed){/size}","head_exp/35")
        $ her_SC.sayHead("{size=-4}(That was a little too intense){/size}","head_exp/15")
        $ her_SC.sayHead("{size=-4}(Not that I'm complaining...){/size}","head_exp/34")
        show screen hermione_stand_f
        with d3
        
        $ v_tutoring = 11
        jump l_tutoring_end

    elif v_tutoring == 11:
        m "So..."
        $ her_SC.say("Wait...","body_208b")
        show screen blkfade
        with d3
        ">Hermione unbuttons her collar."
        ##$ v_her_current_shirt = "shirt4"
        ##$ v_her_shirt = "shirt4_tucked"
        $ her_SC.hideScreen()
        hide screen blkfade
        with d3
        $ her_SC.say("You have another gift for me?","body_205")
        $ her_SC.say("Please, please.","body_182")
        m "I thought I had to go easier on you?"
        $ her_SC.say("Oh don't worry, it was just a moment of weakness.","body_220")
        her "I'm ready now!"
        $ her_SC.say("{size=-2}(My body perhaps not...){/size}","body_71")
        m "Did you have fun with your anal plug?"
        $ her_SC.say("Y-yes... I wear it sometimes...","body_213")
        $ her_SC.say("But I cut the tail!","body_203")
        her "{size=-2}(No way I could walk around like that...){/size}"
        m "And you like it?"
        $ her_SC.say("It's very...{w=0.5} stimulating. It helps me whenever I cast a spell.","body_157")
        m "Tell me the truth Miss Hermione, you wear it all the time, don't you?"
        $ her_SC.say("Nooo...","body_203")
        $ her_SC.say("Maybe...","body_219")
        her "........"
        m "Don't be ashamed, it's alright my little whore."
        $ her_SC.say("I wear it all the time and...{w=0.3} I love it!","body_80b")
        g9 "{size=-2}(Marvelous){/size}"
        m "I've taught you good."
        $ her_SC.say("To be a slut? Yes you have...","body_16")
        $ her_SC.say("And now I want more so where is my gift?!","body_17")
        m "There, there."
        $ the_gift = "01_hp/18_store/gift_anal_beads.png"
        show screen gift
        with d3
        ">You give the anal beads to Hermione"
        hide screen gift
        with d3
        $ her_SC.say("Oh! That's even better than a butt plug.","body_211")
        g9 "And they can be useful for your pussy too."
        $ her_SC.say("So many possibilities...","body_220")
        her "...so little time."
        $ her_SC.say("I suppose you want me to try them out?","body_75")
        her "Or would you rather try them out on me yourself?"
        g9 "Oh yes."
        $ her_SC.say("I don't even know why I'm asking...","body_70")
        her "{size=-2}(Old pervert...){/size}"
        $ her_SC.say("{size=-2}({b}My{/b} old pervert){/size}","body_182")
        show screen blkfade
        if custom_bra >=1 and badges and custom_outfit_old <= 0:
            ">She wantonly removes her shirt and bra."
            ##$ v_her_bra = 0
        else:
            ">She wantonly removes her shirt."
        $ her_SC.hideScreen()
        hide screen hermione_blink
        pause.5
        hide screen blkfade
        ##$ v_her_shirt = 0
        $ badges = False
        $ wear_shirts = False
        $ her_SC.say("My tits are the best in all of Hogwarts!","body_212")
        m "Have you been with many girls to say that?"
        $ her_SC.say("I wish...","body_194")
        g9 "I can tutor you on that too."
        $ her_SC.say("Maybe we should finish this lesson first.","body_205")
        m "Oh, we have time."
        $ her_SC.say("Speaking of that...","body_157")
        show screen blkfade
        $ her_SC.hideScreen()
        with d3
        hide screen blkfade
        $ her_SC.chibi.walk(400,300,1)
        show screen blkfade
        with d1
        pause.5
        hide screen genie
        show screen ctc
        show screen no_groping_05
        with d1
        hide screen blkfade
        with d5
        pause
        hide screen ctc
        g9 "As always, it's a delightful view."
        $ her_SC.say("I'm glad you love it.","body_208b")
        $ her_SC.say("Can we start now?","body_195")
        g9 "I suppose you want them in your ass?"
        $ her_SC.say("Naturally.","body_205")
        $ her_SC.say("{size=-2}(I'll try them in my pussy later tonight){/size}","body_198")
        hide screen no_groping_05
        show screen groping_05
        ">You push the first bead in with ease."
        her "Hmmm {image=textheart}"
        m "How many do you think you can take, my dear?"
        $ her_SC.say("How many have you got?","body_205")
        g9 "That's the spirit!"
        ">You push another one inside with little resistance."
        $ her_SC.say("Yess {image=textheart}, one more please.","body_196")
        ">You feel the beads sink deeper when you push the third one inside."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_01.png"
        $ b_her_tears = True
        $ her_SC.say("Ohhh, they're... they're moving {image=textheart}.","body_194")
        ">The fourth takes some work before it pops in."
        $ b_her_tears = False
        $ her_SC.say("Ah {image=textheart} ah {image=textheart}.","body_212")
        ">You push the last one forcefully inside."
        $ her_SC.say("Ahhhhh {image=textheart}, delightful.","body_219")
        her "They're so deep in my ass... almost like your cock."
        g9 "I can..."
        $ her_SC.say("No you can't! My butthole is too tight for both.","body_184b")
        $ her_SC.say("{size=-2}(But it's such a good idea){/size}","body_194")
        m "I'm sure there's still room for at least one finger."
        ">You finger her butthole gently."
        $ her_SC.say("Ahh... {image=textheart}{w=0.5} aah...{image=textheart}","body_212")
        $ her_SC.say("W-What did I say...","body_194")
        m ">You wiggle the finger inside."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03b.png"
        $ b_her_tears = True
        $ her_SC.say("You never listen, old pervert.","body_194")
        m "What can I say, I just know what's best for you, my little witch."
        ">You pick up the pace."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03d.png"
        $ b_her_tears = True
        $ her_SC.say("Yesss {image=textheart}.","body_194")
        m "I thought you didn't want the finger?"
        g9 "In that case, one more finger."
        ">She shivers when you insert a second finger."
        $ her_SC.say("Ahh noo... no more please.","body_195")
        $ her_SC.say("My butthole is stretched so wide!","body_196")
        g9 "Your butthole is doing great."
        ">You finger her butthole fiercely."
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        $ her_SC.say("Nooo... aahh {image=textheart}.","body_154")
        m "Your pussy is getting neglected. We need to fix that!"
        ">You start fingering her pussy with your other hand. She is panting heavily."
        $ her_SC.say("Ah... ah... like that yesss {image=textheart}.","body_215")
        ">You suddenly pull out all the beads."
        $ her_SC.say("Ahhhhhh!!","body_158")
        ">And insert four fingers in her ass."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_04.png"
        $ b_her_tears = True
        $ her_SC.say("I'm cumming old bastard, I cumming!","body_212")
        m "If you must..."
        ">You continue to work her ass while you finger her pussy."
        her "No don't I..."
        $ her_SC.say("Cummm {image=textheart}{image=textheart}.","body_138")
        $ her_SC.say("Agaaain aaah {image=textheart}.","body_215")
        g11 "Sorry my little anal whore but I'm starting to get tired."
        $ b_her_tears = False
        $ her_SC.say("Don't you dare stop now!","body_148")
        $ her_SC.say("Just a little more pleassse {image=textheart}.","body_158")
        $ her_SC.say("Because I will...","body_158")
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_04.png"
        $ b_her_tears = True
        $ her_SC.say("Come again!!","body_215")
        show screen blkfade
        with d7
        ">There's a small puddle on your desk from her juices. You slowly remove your fingers."
        hide screen groping_05b
        show screen no_groping_05_desk
        hide screen blkfade
        $ b_her_tears = False
        $ her_SC.say("*Pant* *pant*","body_154")
        $ her_SC.say("I feel completely ravaged but happy.","body_156")
        $ her_SC.say("Thank you professor, for letting me discover such great sensations.","body_156")
        $ her_SC.say("But I'm exhausted so good night.","body_155")
        show screen blkfade
        with d3
        ">She puts her shirt back on and rushes to the door."
        hide screen no_groping_05_desk
        $ her_SC.hideScreen()
        $ badges = True
        $ wear_shirts = True
        ##call her_pose()
        $ hermione_SC.chibi.xpos = 610
        ##show screen hermione_stand_f
        show screen genie
        hide screen blkfade
        m "Come back here, girl."
        g11 "I need your mouth, I can't hold it anymore."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03.png"
        $ b_her_tears = True
        $ her_SC.say("Professor!","body_190")
        $ her_SC.say(".........","body_205")
        $ her_SC.say("Can I have points for this?","body_206")
        g11 "Now!"
        show screen blkfade
        with d5
        ">She comes back and does not seem particularly upset."
        $ her_SC.hideScreen()
        ##hide screen hermione_stand_f
        hide screen genie
        $ genie_chibi_xpos = -150
        $ genie_chibi_ypos = 10
        $ g_c_u_pic = "blowjob_ani"
        show screen chair_02
        show screen g_c_u
        hide screen blkfade
        her "*Slurp!* *Slurp!* *Gulp!*"
        g9 "Yes, like that..."
        ">Hermione eagerly sucks your dick."
        m "You seem to be in a hurry. Is it because you're not getting points for this?"
        m "Consider it a payment for your private lessons."
        her "Mmmh..."
        m "Next time, come with your robe and your robe only."
        ">She briefly nods."
        her "*Slurp!* *Gulp!* *Slurp!*"
        g9 "You're doing great my little whore, I will..."
        g11 "Yes!"
        show screen blkfade
        with d3
        $ g_c_u_pic = "cum_in_mouth_ani"
        show screen g_c_u
        hide screen blkfade
        her "*Gobble!* *Gobble!* *Gobble!*"
        g9 "Good girl, you swallowed it all!"
        show screen blkfade
        with d7

        ">She wipes her mouth."
        hide screen g_c_u
        hide screen chair_02
        show screen genie
        $ hermione_SC.chibi.xpos = 300
        show screen hermione_blink
        hide screen blkfade

        $ her_SC.say("Sir, I still think I deserve some...","body_203")
        m "Good night, my dear child."
        $ her_SC.say(".........","body_214")
        $ her_SC.say("Good night, professor.","body_184b")
        "You dismiss Hermione."
        $ her_SC.hideScreen()
        $ b_her_tears = False
        hide screen hermione_blink
        show screen blkfade
        with d3
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Sucking his cock without getting any points!){/size}","head_exp/4")
        $ her_SC.sayHead("{size=-4}(If he hadn't made me come so hard...){/size}","head_exp/6")
        $ her_SC.sayHead("{size=-4}(*sigh* Although I guess it's not that high a price...){/size}","head_exp/16")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 12
        jump l_tutoring_end

    elif v_tutoring == 12:
        $ her_SC.say("Oh! I can't believe I forgot! Stay where you are, I'll be right back!","body_206")
        $ her_SC.hideScreen()
        show screen blkfade
        with d3
        play sound sd_door
        pause 2
        play sound sd_door
        pause.3
        ##call her_pose("naked")
        ##call her_pose("robe")
        ##$ v_her_robe = "robe1"
        $ robe = 1
        $ badges = False
        $ wear_shirts = False
        $ panties = False
        $ custom_outfit_old = 20
        hide screen blkfade
        $ walk_xpos = 600
        $ walk_xpos2 = 400
        $ hermione_speed = 01.0
        show screen hermione_walk_01
        pause 1
        show screen hermione_blink
        $ her_SC.say("{size=-4}*panting*{/size} Oh good, you're still here.","body_183")
        m "Is it safe to assume you have honored my request this time?"
        $ her_SC.say("I thought it was obvious.","body_190")
        $ her_SC.say("I even had to hide in an alcove to avoid getting noticed on my way here!","body_183")
        $ her_SC.say("It was so embarrassing!","body_182")
        $ her_SC.say("{size=-2}(And exciting!){/size}","body_182")
        m "Are you sure you're not wearing anything underneath?"
        $ her_SC.hideScreen()
        with d3
        ">Hermione opens up her cloak a little."
        ##$ v_her_robe = "robe1_gap"
        $ robe = 2
        $ h_body = "01_hp/13_hermione_main/body_205.png"
        show screen hermione_main
        pause
        $ her_SC.say("Does this answer your question?","body_190")
        m "Not really. It's hard to tell from this distance. I mean, it's so dark..."
        $ her_SC.hideScreen()
        with d3
        ">Hermione rolls her eyes and pulls the gap wider"
        ##$ v_her_robe = "robe1_gap_wide"
        $ robe = 3
        $ h_body = "01_hp/13_hermione_main/body_208b.png"
        show screen hermione_main
        pause
        her "Is that better?"
        g9 "Oh yes, definitely. Well done, my girl."
        $ her_SC.hideScreen()
        with d3
        ">Hermione makes to pull her cloak back together, then pauses and puts her hands back down."
        $ h_body = "01_hp/13_hermione_main/body_209.png"
        show screen hermione_main
        pause
        $ her_SC.say("Alright then, can we start the lesson now?","body_220")
        m "Maybe, I don't know... do you like butterbeer?"
        $ her_SC.say("You know I do. What's that got to do with...","body_200")
        g9 "......."
        $ her_SC.say("Do you mean...{w=0.3} no, no way professor!","body_210")
        m "Oh, rest assured, we won't start with the bottom end."
        $ her_SC.say("Still, professor, this is so dirty...","body_212")
        $ her_SC.say("{size=-2}(And exciting){/size}","body_212")
        $ her_SC.say("Moreover, my butthole isn't stretched enough.","body_184b")
        g4 "Are you kidding me, with all your training!"
        $ her_SC.say("And what a training!","body_214")
        $ her_SC.say("{size=-2}(Good thing I practiced by myself, otherwise...){/size}","body_208b")
        g4 "Now stop making up excuses!"
        m "I can see you rubbing your thighs from excitement!"
        $ her_SC.say("I thought it was so dark in here...","body_190")
        $ her_SC.say("Humm, okay, but you better start out easy on me.","body_17")
        g9 "I'm always gentle with you my dear child."
        $ her_SC.say("Yeah, obviously...","body_70")
        m "{size=-2}(It's not as if you don't like it rough){/size}"
        m "Alright, my desk, you, naked, now!"

        $ her_SC.hideScreen()
        with d3
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d5
        ">Hermione slowly slides down her robe."
        hide screen hermione_blink
        $ hermione_SC.chibi.xpos = 300
        show screen ctc
        with d1
        hide screen blkfade
        with d5
        ##$ v_her_robe = "robe1_off"
        $ robe = 4
        $ h_body = "01_hp/13_hermione_main/body_182.png"
        show screen hermione_main
        pause
        hide screen ctc
        her "You're crazy for my body, aren't you?"
        m "Why do you ask..."
        $ her_SC.say("Because a girl likes to be complimented, professor!","body_17")
        $ her_SC.say("Especially when she's about to do these kinds of things!","body_70")
        m "I meant, of course you have a amazing body! That's not up to question."
        $ her_SC.say("Best in the school?","body_205")
        m "......{w=0.3} Yeah, yeah, best in the school."
        $ her_SC.say("I can tell you're lying!","body_207")
        m "Miss Hermione, I've lived for a very long time and believe me, I have seen few women with a body like yours."
        m "And definitely none in this school."
        m "{size=-2}(Severus still hasn't sent those Slytherin whores up){/size}"
        m "{size=-2}(I wonder if I can fire him for that...){/size}"
        $ her_SC.say("Thank you, professor.","body_182")
        $ her_SC.say("Feel free to do use my body as you please.","body_208b")
        m "{size=-2}(*sigh* women...){/size}"
        m "Bend over the desk my dear little witch."
        $ her_SC.say("{size=-2}(It starts with my dear little witch and ends up with my dear anal whore){/size}","body_214")
        $ her_SC.say("{size=-2}(*sigh* men...){/size}","body_214")
        $ her_SC.say("As you wish my dear {b}old{/b} headmaster.","body_190")
        m "{size=-2}(If you knew how old I actually am...){/size}"
        show screen blkfade
        with d5
        ">Hermione languorously bends over the desk."
        hide screen her_naked
        $ her_SC.hideScreen()
        hide screen genie
        show screen no_groping_laying_02
        show screen ctc
        with d1
        hide screen blkfade
        with d5
        ##$ v_her_robe = 0
        $ robe = 0 
        $ h_body = "01_hp/13_hermione_main/body_182.png"
        show screen hermione_main
        pause
        hide screen ctc
        her "I'm ready my prince."
        ">You take an empty butterbeer bottle, spit on the neck and push it inside her butthole."
        hide screen no_groping_laying_02
        show screen scr_her_fingering_naked("slow")
        $ her_SC.say("Hmmm, yes like that.","body_213")
        $ her_SC.say("My pussy feels lonely without your care.","body_209")
        ">You start to finger her pussy too."
        $ h_body = "01_hp/13_hermione_main/body_196.png"
        show screen hermione_main
        m "Poor little thing."
        $ her_SC.say("What's better in life than this professor?","body_196")
        m "Oh, I don't know."
        $ her_SC.say("Thank you for letting me discover such pleasures.","body_182")
        g9 "{b}My{/b} pleasure."
        $ her_SC.say("It's even better when it's mutual, isn't it?","body_190")
        m "Hmm, yes you're right. I'm glad you feel that way."
        $ her_SC.say("Now a little deeper please.","body_200")
        ">You push the whole bottle neck up inside her asshole."
        $ her_SC.say("Ohhh, yesss! {image=textheart}","body_196")
        $ her_SC.say("More, faster!","body_196")
        show screen scr_her_fingering_naked()
        ">You rotate the bottle while going back and forth deeper and deeper."
        $ her_SC.say("Yessss, don't forget my pussy {image=textheart}.","body_194")
        g9 "Oh, your pussy better be ready for what's coming!"
        ">You insert all four fingers in her sopping wet pussy."
        $ her_SC.say("Sweet Circe, aah, aah, that's too much! {image=textheart}","body_154")
        m "Nothing is too much for my little whore."
        ">You increase the pace of both hands."
        $ her_SC.say("No, no, yes, yessss! {image=textheart}","body_158")
        ">Most of the bottle is inside her now, leaving just enough to get a good grip."
        m "Push the bottle, push it!"
        ">Whenever she pushes it back you do the same in the other direction."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_04.png"
        $ b_her_tears = True
        $ her_SC.say("This is, this is, aaaah!!! {image=textheart}{image=textheart}","body_215")
        ">Her whole body convulses as she comes hard."
        show screen blkfade
        with d5
        $ b_her_tears = False
        $ her_SC.hideScreen()
        hide screen scr_her_fingering_naked
        show screen no_groping_laying_02
        pause.3
        hide screen blkfade
        $ her_SC.say("*Panting* *panting*","body_158")
        $ her_SC.say("P-professor...{w=0.3} I'm so happy right now.","body_157")
        g9 "Glad to hear it."
        show screen blkfade
        ">After a while, she makes herself somewhat presentable."
        ##call her_pose()
        $ robe = 1
        hide screen no_groping_laying_02
        show screen genie
        show screen hermione_blink
        hide screen blkfade
        with d3
        m "Sweet dreams my little princess."
        $ her_SC.say("You too, professor.","body_183")
        g9 "They are always sweet with you around."
        $ her_SC.say("Thank you.","body_213")
        m "And next time bring your books, I'll help you with your revisions."
        "You dismiss Hermione."
        $ her_SC.hideScreen()
        hide screen hermione_blink
        show screen blkfade
        with d3
        $ b_her_tears = False
        hide screen blkfade
        show screen genie
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(Yes, sweet dreams...){/size}","head_exp/35")
        $ her_SC.sayHead("{size=-4}(Sweet and wet!){/size}","head_exp/34")
        hide screen hermione_stand_f
        with d3
        
        $ v_tutoring = 13
        jump l_tutoring_end

    elif v_tutoring == 13:
        $ her_SC.say("I'll go get my books right away, sir!","body_13")
        $ her_SC.hideScreen()
        show screen blkfade
        with d3
        play sound sd_door
        pause 2
        play sound sd_door
        pause.3
        $ book_hold = True
        $ h_body = "01_hp/13_hermione_main/body_45.png"
        show screen hermione_main
        show screen hermione_blink
        show screen ctc
        hide screen blkfade
        with d3
        pause
        hide screen ctc
        m "Your vest is back?"
        $ her_SC.say("Revisions are a serious matter!","body_11")
        m "{size=-2}(My cock in your ass is a serious matter...){/size}"
        m "In this regard, I kinda lied, it's more of a mock exam than revisions."
        $ her_SC.say("What a surprise!","body_214")
        m "I need to make sure you've been working out your butthole."
        $ her_SC.say("........","body_214")
        g9 "With my cock."
        $ her_SC.say("I see...","body_201")
        $ her_SC.say("I'm not against that but I bet I'll gain no points for this?","body_203")
        m "I'm helping you with your revisions, why should you be getting points for that?"
        $ her_SC.say("And what revisions...","body_184b")
        $ her_SC.say("Alright, since you have helped me a lot, I'm in.","body_188")
        $ her_SC.say("{size=-2}(I give myself away for free now, what a bad whore I make){/size}","body_157")
        m "Come here and strip."
        show screen blkfade
        hide screen hermione_04
        $ her_SC.hideScreen()
        with d3
        hide screen blkfade
        $ her_SC.chibi.walk(400,300,1)
        show screen blkfade
        with d3
        pause 1
        $ panties = False
        $ wear_shirts = False
        $ badges = False
        $ custom_outfit_old = 20
        $ h_body = "01_hp/13_hermione_main/body_198.png"
        show screen hermione_main
        show screen ctc
        hide screen blkfade
        with d3
        pause
        hide screen ctc
        m "Ok now, put your books down and bend over the desk, my little whore."
        show screen blkfade
        with d1
        pause.5
        $ her_SC.hideScreen()
        hide screen genie
        show screen no_groping_laying_02
        hide screen blkfade
        with d5
        g9 "You can open a book if you want."
        ##$ v_her_book = 0
        ##$ v_her_shirt = 0
        $ book_hold = False
        $ her_SC.say("I should read about this spell called \"the Clap\"!","body_184b")
        ">You take advantage of her moment of distraction to force you cock into her butthole."
        show screen blkfade
        pause 1
        hide screen no_groping_laying_02
        show screen chair_02
        show screen scr_her_sex("slow")
        hide screen blkfade
        with hpunch
        $ her_SC.say("Ah, you brute {image=textheart}.","body_194")
        m "Your butthole is the perfect fit, not too tight and not too stretched!"
        $ her_SC.say("You've trained me well...","body_212")
        ">You caress her clit while fucking her."
        $ her_SC.say("Mmmh, yes {image=textheart}.","body_196")
        g9 "You love it don't you?"
        $ her_SC.say("Your cock in my ass, oh yes.","body_205")
        m "Even without points?"
        $ her_SC.say("Don't make me regret agreeing to this.","body_182b")
        m "Say you love it even without points."
        show screen scr_her_sex()
        ">You increase the pace."
        $ her_SC.say("Ahh yesss {image=textheart}.","body_219")
        $ her_SC.say("I'm such a whore, I love sex even for free.","body_206")
        g9 "You know it!"
        $ her_SC.say("Don't make it a habit.","body_190")
        m "......"
        ">You pull out your cock and roughly shove it back inside."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_01.png"
        $ b_her_tears = True
        $ h_body = "01_hp/13_hermione_main/body_194.png"
        show screen hermione_main
        with hpunch
        her "Aaaaah {image=textheart}."
        $ her_SC.say("I love being sodomized savagely by my headmaster.","body_212")
        ">And again."
        $ h_body = "01_hp/13_hermione_main/body_215.png"
        show screen hermione_main
        with hpunch
        her "Yessss {image=textheart}."
        $ her_SC.say("I love his big cock in my ass.","body_138")
        ">You slap her buttcheek."
        play sound sd_slap
        with hpunch
        $ b_her_tears = False
        $ her_SC.say("And being punished for my sluttiness.","body_154")
        play sound sd_slap
        with hpunch
        $ her_SC.say("Aah, like this, punish me more master {image=textheart}.","body_138")
        play sound sd_slap 
        with hpunch
        $ her_SC.say("Yess!","body_215")
        play sound sd_slap 
        with hpunch
        $ her_SC.say("Mooore!","body_215")
        play sound sd_slap 
        with hpunch
        $ her_SC.say("I'm about to...","body_142")
        play sound sd_slap 
        with hpunch
        pause.1
        play sound sd_slap
        with hpunch
        pause.1
        $ her_SC.say("Cuuuum {image=textheart}{image=textheart}.","body_215")
        show screen scr_her_sex("fast")
        ">You fuck her butthole fiercely."
        $ her_SC.say("Yes, yes, again, aaaah {image=textheart}.","body_215")
        g11 "Yes, my little whore, yes!"
        hide screen scr_her_sex
        show screen scr_her_sex_cum_outside()
        $ her_SC.say("*Panting* *panting*","body_154")
        show screen scr_her_sex_cum_outside(1)
        g11 "*Panting* *panting*"
        show screen blkfade
        hide screen chair_02
        $ her_SC.hideScreen()
        hide screen scr_her_sex_cum_outside
        pause 1
        show screen no_groping_laying_02
        hide screen blkfade
        m "*sigh* that was, that was..."
        $ u_tears_pic = "01_hp/13_hermione_main/e_her_tears_03.png"
        $ b_her_tears = True
        $ her_SC.say("Marvellous {image=textheart}.","body_46")
        $ her_SC.say("I'm so glad you agreed to tutor me, professor...","body_212")
        $ her_SC.say("Your lessons have changed my life so much!","body_220")
        g9 "{size=-2}(Victory!){/size}"
        $ her_SC.say("But if you think you can fuck me all the time without giving me points...","body_203")
        $ her_SC.say("You're dreaming!","body_214")
        m "{size=-2}(Ohhh...){/size}"
        m "Even occasionally?"
        her "......."
        $ her_SC.say("Only if you are well-behaved...","body_200")
        g9 "I'm the most well-behaved professor in the whole school!"
        $ her_SC.say("Sure.","body_203")
        $ her_SC.say("{size=-2}(At least, you're not the worst...){/size}","body_214")
        m "Good night my beloved princess."
        $ her_SC.say("Good night my beloved prince.","body_188")
        ">You dismiss Hermione."
        ">She puts her clothes back on without haste."
        $ her_SC.hideScreen()
        hide screen no_groping_laying_02
        show screen blkfade
        with d3
        pause 1
        ##call her_pose()
        $ b_her_tears = False
        show screen genie
        hide screen blkfade
        with d3
        
        $ her_SC.chibi.walk(400,610,2)
        
        show screen hermione_stand_f
        $ her_SC.sayHead("{size=-4}(I called my headmaster \"my beloved prince\"){/size}","head_exp/16")
        $ her_SC.sayHead("{size=-4}(He's hardly Prince Charming but...){/size}","head_exp/18")
        $ her_SC.sayHead("{size=-4}(I doubt Prince Charming could fuck me half as well as he can!){/size}","head_exp/38")
        show screen hermione_stand_f
        with d3
        
        $ v_tutoring = 14
        jump l_tutoring_end

label l_tutoring_end:
    play sound sd_door
    ##hide screen hermione_stand_f
    with d3

    $ aftercum = False
    $ hair_color = hair_temp
    $ book_hold = False
    $ panties = True
    $ skirt_up = False
    $ wear_shirts = True
    $ badges = True
    $ fingering = False
    $ robe = 0
    $ custom_outfit_old = 0
    ##call her_pose()
    jump day_start





###UE CUSTOM THINGS
# Music
define ms_arabian_nights = "music/Arabian_Nights.mp3"
define ms_bushwick = "music/Bushwick_Tarantella_Loop.mp3"
define ms_croft_manor = "music/Croft_Manor.mp3"
define ms_dice_game = "music/Dice_Game.mp3"
define ms_gtkm = "music/Going_to_Kill_Me.mp3"
define ms_gorilla = "music/Gorilla_Theme.mp3"
define ms_india = "music/India's_Different.mp3"
define ms_jafar = "music/Jafar's_Hour.mp3"
define ms_kabul = "music/Kabul_Flight_Jumpstart.mp3"
define ms_manatees = "music/Music for Manatees.mp3"
define ms_marketplace = "music/Marketplace.mp3"
define ms_outlaw_star = "music/Outlaw_Star_Freedom.mp3"
define ms_ozone = "music/Ozone.ogg"
define ms_sleep_walking = "music/Sleep_Walking.mp3"
define ms_tension = "music/Tension.mp3"
define ms_the_calm_before = "music/The_Calm_Before.mp3"
define ms_the_eastern_wind = "music/The_Eastern_Wind.mp3"
define ms_the_kiss = "music/The_Kiss.mp3"
define ms_the_xfiles = "music/The_X-Files.mp3"
define ms_vision = "music/Vision.mp3"
# Sounds
define sd_boing1 = "sounds/boing.mp3"
define sd_boing2 = "sounds/boing02.mp3"
define sd_boing3 = "sounds/boing03.mp3"
define sd_burp = "sounds/burp.mp3"
define sd_door = "sounds/door.mp3"
define sd_door2 = "sounds/door2.mp3"
define sd_door3 = "sounds/door3.mp3"
define sd_fall = "sounds/fall.wav"
define sd_glitch = "sounds/gltch.mp3"
define sd_iris_run = "sounds/iris_run.mp3"
define sd_kungfupunch = "sounds/kung-fu-punch.mp3"
define sd_magic4 = "sounds/magic4.ogg"
define sd_monster = "sounds/mon.wav"
define sd_monster_dead = "sounds/mondead.wav"
define sd_pistol2 = "sounds/pistol2.mp3"
define sd_pop1 = "sounds/pop01.mp3"
define sd_pop2 = "sounds/pop02.mp3"
define sd_pop3 = "sounds/pop03.mp3"
define sd_punch1 = "sounds/punch01.mp3"
define sd_punch2 = "sounds/punch02.mp3"
define sd_rustling = "sounds/rustling.mp3"
define sd_scratch = "sounds/scratch.wav"
define sd_slap = "sounds/slap.mp3"
define sd_spit = "sounds/spit.mp3"
define sd_win2 = "sounds/win2.mp3"
# Screens
screen genie_and_hermione: #Genie sitting, Hermione stands right in front of him (behind the desk even).
    tag favor
    add "01_hp/05_props/genie_and_hermione_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_05:
    tag favor
    add "groping_05" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_05b:
    tag favor
    add "groping_05b" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_05:
    tag favor
    add "01_hp/animation/grope_d_05.png" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_05_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_05_desk:
    tag favor
    add "01_hp/animation/grope_d_06.png" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_06: #Facing Genie.
    tag favor
    add "01_hp/animation/grope_e_05.png" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_06:
    tag favor
    add "groping_06" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen groping_06b:
    tag favor
    add "groping_06b" at Position(xpos = table_position_x -84, ypos = 10)
    add "groping_06_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_laying_01:
    tag favor
    add "01_hp/animation/grope_laying_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen no_groping_laying_02:
    tag favor
    add "01_hp/animation/grope_laying_b_01.png" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_fingering_naked(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_fingering_slow_naked" at Position(xpos = table_position_x -84, ypos = 10)
    else:
        add "ani_her_fingering_naked" at Position(xpos = table_position_x -84, ypos = 10)
    add "ani_her_fingering_blinking" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_sex(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_sex_slow_naked" at Position(xpos = table_position_x -84, ypos = 10)
    elif speed == "normal":
        add "ani_her_sex_naked" at Position(xpos = table_position_x -84, ypos = 10)
    elif speed == "fast":
        add "ani_her_sex_fast_naked" at Position(xpos = table_position_x -84, ypos = 10)

screen scr_her_sex_cum_outside(blink=0):
    tag favor
    add "ani_her_sex_cum_outside_naked" at Position(xpos = table_position_x -84, ypos = 10)

image groping_06: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "01_hp/animation/grope_e_01.png"
    pause.2
    "01_hp/animation/grope_e_02.png"
    pause.2
    "01_hp/animation/grope_e_03.png"
    pause.5
    "01_hp/animation/grope_e_02.png"
    pause.2
    "01_hp/animation/grope_e_01.png"
    pause.2
    repeat

image groping_06b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "01_hp/animation/grope_e_01.png"
    pause.1
    "01_hp/animation/grope_e_02.png"
    pause.1
    "01_hp/animation/grope_e_03.png"
    pause.2
    "01_hp/animation/grope_e_02.png"
    pause.1
    "01_hp/animation/grope_e_01.png"
    pause.1
    repeat

image groping_06_blinking: #Animation of Hermione blinking her eyes.
    "01_hp/animation/00.png"
    pause.1
    "01_hp/animation/grope_e_04.png"
    pause.1
    "01_hp/animation/00.png"
    pause 3
    "01_hp/animation/grope_e_04.png"
    pause.1
    "01_hp/animation/00.png"
    pause.1
    "01_hp/animation/grope_e_04.png"
    pause.1
    "01_hp/animation/00.png"
    pause 3
    repeat

image groping_05: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "01_hp/animation/grope_d_01.png"
    pause.2
    "01_hp/animation/grope_d_02.png"
    pause.2
    "01_hp/animation/grope_d_03.png"
    pause.5
    "01_hp/animation/grope_d_02.png"
    pause.2
    "01_hp/animation/grope_d_01.png"
    pause.2
    repeat

image groping_05b: #Genie groping Hermione under her skirt. Hermione is facing Genie.
    "01_hp/animation/grope_d_01.png"
    pause.1
    "01_hp/animation/grope_d_02.png"
    pause.1
    "01_hp/animation/grope_d_03.png"
    pause.2
    "01_hp/animation/grope_d_02.png"
    pause.1
    "01_hp/animation/grope_d_01.png"
    pause.1
    repeat

image groping_05_blinking: #Animation of Hermione blinking her eyes.
    "01_hp/animation/00.png"
    pause.1
    "01_hp/animation/grope_d_04.png"
    pause.1
    "01_hp/animation/00.png"
    pause 3
    "01_hp/animation/grope_d_04.png"
    pause.1
    "01_hp/animation/00.png"
    pause.1
    "01_hp/animation/grope_d_04.png"
    pause.1
    "01_hp/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_blinking: #Animation of Hermione blinking her eyes.
    "01_hp/animation/00.png"
    pause.1
    "01_hp/animation/grope_fingering_blink.png"
    pause.1
    "01_hp/animation/00.png"
    pause 3
    "01_hp/animation/grope_fingering_blink.png"
    pause.1
    "01_hp/animation/00.png"
    pause.1
    "01_hp/animation/grope_fingering_blink.png"
    pause.1
    "01_hp/animation/00.png"
    pause 3
    repeat

image ani_her_fingering_slow_naked:
    "01_hp/animation/grope_fingering_n_01.png"
    pause.3
    "01_hp/animation/grope_fingering_n_02.png"
    pause.3
    "01_hp/animation/grope_fingering_n_03.png"
    pause.3
    "01_hp/animation/grope_fingering_n_04.png"
    pause.3
    repeat

image ani_her_fingering_naked:
    "01_hp/animation/grope_fingering_n_01.png"
    pause.2
    "01_hp/animation/grope_fingering_n_02.png"
    pause.2
    "01_hp/animation/grope_fingering_n_03.png"
    pause.2
    "01_hp/animation/grope_fingering_n_04.png"
    pause.2
    repeat

image ani_her_sex_slow_naked:
    "01_hp/08_animation_02/21_sex_n_01.png"
    pause.15
    "01_hp/08_animation_02/21_sex_n_02.png"
    pause.15
    "01_hp/08_animation_02/21_sex_n_03.png"
    pause.15
    "01_hp/08_animation_02/21_sex_n_04.png"
    pause.15
    "01_hp/08_animation_02/21_sex_n_05.png"
    pause.15
    "01_hp/08_animation_02/21_sex_n_06.png"
    pause.15
    "01_hp/08_animation_02/21_sex_n_07.png"
    pause.15
    repeat

image ani_her_sex_naked:
    "01_hp/08_animation_02/21_sex_n_01.png"
    pause.1
    "01_hp/08_animation_02/21_sex_n_02.png"
    pause.1
    "01_hp/08_animation_02/21_sex_n_03.png"
    pause.1
    "01_hp/08_animation_02/21_sex_n_04.png"
    pause.1
    "01_hp/08_animation_02/21_sex_n_05.png"
    pause.1
    "01_hp/08_animation_02/21_sex_n_06.png"
    pause.1
    "01_hp/08_animation_02/21_sex_n_07.png"
    pause.1
    repeat

image ani_her_sex_fast_naked:
    "01_hp/08_animation_02/21_sex_n_01.png"
    pause.05
    "01_hp/08_animation_02/21_sex_n_02.png"
    pause.05
    "01_hp/08_animation_02/21_sex_n_03.png"
    pause.05
    "01_hp/08_animation_02/21_sex_n_04.png"
    pause.05
    "01_hp/08_animation_02/21_sex_n_05.png"
    pause.05
    "01_hp/08_animation_02/21_sex_n_06.png"
    pause.05
    "01_hp/08_animation_02/21_sex_n_07.png"
    pause.05
    repeat

image ani_her_sex_cum_outside_naked:
    "01_hp/08_animation_02/22_cum_n_01.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_02.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_03.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_04.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_05.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_06.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_07.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_08.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_09.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_10.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_11.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_12.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_13.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_14.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_15.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_16.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_17.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_18.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_19.png"
    pause 2
    "01_hp/08_animation_02/22_cum_n_20.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_21.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_22.png"
    pause.1
    "01_hp/08_animation_02/22_cum_n_23.png"
    pause.1
    repeat
