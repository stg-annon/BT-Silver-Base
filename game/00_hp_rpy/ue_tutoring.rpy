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
        if mag3 >= 1:
            jump l_tutoring
        else:
            m "I need to buy adult magazines for this lesson."
    elif v_tutoring == 8 and whoring >= 17:
        if mag4 >= 1:
            jump l_tutoring
        else:
            m "I need to buy porn magazines for this lesson."
    elif v_tutoring == 9 and whoring >= 20:
        if vibrator >= 1:
            jump l_tutoring
        else:
            m "I need to buy a vibrator for this lesson."
    elif v_tutoring == 10 and whoring >= 23:
        if plug >= 1:
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
    $ hair_temp = hair_color
    $ hair_color = 0

    hide screen hermione_main
    with d3

    $ h_xpos = 140

    if v_tutoring == 0:   # Whoring lvl 0
        $ h_xpos = 370
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051_norm.png"
        show screen hermione_main
        with d3
        her "Of course, sir."
        her "I'll go get my books then."
        hide screen hermione_main
        show screen blkfade
        with d3
        play sound sd_door
        pause 2
        play sound sd_door
        pause.3
        $ h_xpos = 140
        $ book_hold = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_norm.png"
        show screen hermione_main
        with d3
        hide screen blkfade
        with d3
        show screen ctc
        pause
        hide screen ctc
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052_norm.png"
        show screen hermione_main
        with d3
        her "Again, thank you for doing this for me, sir..."
        m "..........."
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n042_norm.png"
        show screen hermione_main
        with d3
        her "Sir?"
        m "It's time to talk about your future, child."
        stop music fadeout 1.0
        hide screen hermione_main
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_a002b_norm.png"
        show screen hermione_main
        with d3
        her "I'm not a child anymore professor!"
        m "In a way you're right but..."
        her "..........."
        m "Anyway I can tutor you but you need to understand certain things about magic."
        m "With proper training you can learn to increase your magic ability."
        play music ms_manatees fadein 1 fadeout 1
        $ h_body = "01_hp/27_ue/hermione/bd_her_n042_norm.png"
        show screen hermione_main
        her "Yes?"
        m "Certain emotions like love and hate, pleasure and pain..."
        g9 "{size=-2}(If she falls for that, I'm a true genius){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n001_norm.png"
        show screen hermione_main
        her "I've been studying magic for years and I've never heard of such a thing."
        g4 "{size=-2}(Shit){/size}"
        m "And that's exactly why you're still a child. You still have much to learn about magic."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "Please stop that, professor. Nobody considers me a child anymore."
        hide screen hermione_main
        m "Yes, technically..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "Technically?!"
        hide screen hermione_main
        g4 "Enough of this. You came to me to ask for my help and if it starts like that..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n072_norm.png"
        show screen hermione_main
        her "Yes, I suppose you are right..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_norm.png"
        show screen hermione_main
        her "Alright, I'm ready to study hard with you!"
        hide screen hermione_main
        g9 "{size=-2}(Yes!){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a053_blush.png"
        show screen hermione_main
        her "What was that?"
        m "Uh, yes I'm glad you're beginning to understand, {w=0.3}child."
        her "..........."
        hide screen hermione_main
        m "Alright, I want you to take some time and think about what I've said. Next time we'll start with your first lesson."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052_norm.png"
        show screen hermione_main
        her "Can't we start now?"
        hide screen hermione_main
        m "Miss Hermione, you're not the only student I must take care of."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "You're tutoring someone else?"
        hide screen hermione_main
        m "{size=-2}(If only...){/size}"
        m "I meant, I must take care of all the students of this school."
        m "But yes, there is another girl who needs..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n167_norm.png"
        show screen hermione_main
        her "A Slytherin girl?!"
        g9 "That is none of your business, miss Granger."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n072_norm.png"
        show screen hermione_main
        her "Yes, professor, I'm sorry but with all the recent events I'm a little on edge."
        m "Apology accepted and now goodnight!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_norm.png"
        show screen hermione_main
        her "Good night professor and thanks again for taking some of your precious time to help me."
        hide screen bld1
        hide screen hermione_main
        with d3
        "You dismiss Hermione."

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[35] "{size=-4}(I'm glad professor agreed to tutor me){/size}"
        her_[2] "{size=-4}(But pleasure and pain? I don't understand where this is going...){/size}"

        $ v_tutoring = 1
        jump l_tutoring_end

    if v_tutoring == 1:   # Whoring lvl 1
        ##call her_pose("book")
        ##$ v_her_book = 1
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_norm.png"
        show screen hermione_main
        with d3
        m "Miss Granger, time for your first lesson."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n042_norm.png"
        show screen hermione_main
        her "Yes, professor."
        m "You've brought your books again, I don't think we'll need them for the moment."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n001_norm.png"
        show screen hermione_main
        her "Too bad, I love books."
        g9 "{size=-2}(And soon you'll love cock){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n042_norm.png"
        show screen hermione_main
        her "Yes?"
        hide screen hermione_main
        m "It's nothing, I was just thinking about our next lesson."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n072_norm.png"
        show screen hermione_main
        her "{size=-2}(The elderly...){/size}"
        m "............."
        hide screen hermione_main
        m "Anyway have you thought about what we discussed?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n001_norm.png"
        show screen hermione_main
        her "Not really, I'm not sure what you mean by \"emotions\"."
        g9 "{size=-2}(Oh me I'm sure){/size}"
        m "For example, what was your state of mind when you heard those rumours about the Slytherin girls?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n167_norm.png"
        show screen hermione_main
        her "Please don't bring it up, sir, it really makes me mad!"
        hide screen hermione_main
        m "And what is this feeling?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n001_norm.png"
        show screen hermione_main
        her "...{w=0.5}an emotion I suppose..."
        m "Yes and don't you have emotions you prefer over others?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_norm.png"
        show screen hermione_main
        her "When I have the best score at a test."
        hide screen hermione_main
        m "{size=-2}(This girl is a monomaniac...){/size}"
        m "Don't you have other passions, things you like to do?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_norm.png"
        show screen hermione_main
        her "Yes! Studing and reading books."
        hide screen hermione_main
        g4 "{size=-2}(By all the ancient gods and the new){/size}"
        m "Things are not going in the right direction..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n001_norm.png"
        show screen hermione_main
        her "And what direction is that, sir?"
        hide screen hermione_main
        g9 "{size=-2}(You impaled on my cock){/size}"
        m "Adulthood Miss Hermione, adulthood..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a059b_norm.png"
        show screen hermione_main
        her "I am by far the most mature of my peers, professor. What more can you ask?"
        hide screen hermione_main
        m "......{w=0.5}Miss Granger, did we not discuss this already? You need to accept you still have much to learn."
        m "I'm tired of all this and I have work to do so goodnight, child."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a053_blush.png"
        show screen hermione_main
        her "Tutoring one of those filthy Slytherin girls maybe?"
        hide screen hermione_main
        m "Maybe that's the right direction, think about what all those girls do with professors."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "But...{w=0.5} that's so wrong...{w=0.5} I don't know if I want to think about that."
        m "If you want to progress and to restore the Gryffindor pride, you must!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        her "Yes, you are right! It's my mission! I'll do my best professor."
        hide screen hermione_main
        g9 "{size=-2}(She is so naive, it's adorable){/size}"
        m "Good, now time to go to bed child."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a002b_norm.png"
        show screen hermione_main
        her "{size=-2}(Tss like I'm going to bed at this time, I need to study more){/size}"
        hide screen bld1
        hide screen hermione_main
        with d3
        "You dismiss Hermione."

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[19] "{size=-4}(Filthy whores...){/size}"
        her_[35] "{size=-4}(Oh, I should not talk like that...{w=0.5} but it feels so good){/size}"

        $ v_tutoring = 2
        jump l_tutoring_end

    elif v_tutoring == 2:   # Whoring lvl 2
        m "Good you didn't bring your books this time."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a036_norm.png"
        show screen hermione_main
        with d3
        her "Not that I agree with it. All the knowledge I need is in those books."
        m "You're forgetting something important, practice and experience!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "Maybe, after all you're not at the head of Hogwarts by chance."
        m "Sometimes you seem to forget it Miss Granger."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "That sounded like something professor Snape would say..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_norm.png"
        show screen hermione_main
        her "Sorry about that, he thinks he's always right and it annoys me."
        m "Not unlike you, miss Granger..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "I suppose you have a point..."
        m "From now on I hope it's clear."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n127_blush.png"
        show screen hermione_main
        her "Yes, professor Dumbledore."
        hide screen hermione_main
        m "So, have you thought about emotions and their usefulness in the practice of magic?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "Yes, first I tried to cast a spell while thinking of the behavior of those Slytherin girls."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_norm.png"
        show screen hermione_main
        her "It made me angry and confused so I lost my focus and failed miserably."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "I don't think it helps at all."
        hide screen hermione_main
        m "That's your problem Miss Granger, you think you know the answer and don't follow my instructions."
        m "I don't care about the behavior of those girls."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n168_norm.png"
        show screen hermione_main
        her "What professor! You don't care?!"
        hide screen hermione_main
        g9 "{size=-2}(Oh I do care, just not in the way you think){/size}"
        m "For this exercise, Miss Granger, for this exercise. Don't get on your high horse."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_norm.png"
        show screen hermione_main
        her "........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "Sorry about that, {w=0.5}again."
        m "I need you to focus on what those girls do with professors, not their behavior in general."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "But..."
        m "Last time you were talking about your sacred duty and at the first hurdle you hesitate."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n023_norm.png"
        show screen hermione_main
        her "{size=-2}(\"Sacred\"? Don't exagerate old man){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "{size=-2}(Or not! Maybe I'll be remembered later for being the savior of house Gryffindor){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n156_blush.png"
        show screen hermione_main
        her "Yes, you're right! It {b}is{/b} my sacred duty!"
        g9 "{size=-2}(And it works every time, it's too easy... She looks so proud of herself){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052_blush.png"
        show screen hermione_main
        her "I'll do my best, professor!"
        g9 "I'm excited too... uh, I'm sure you will."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_norm_e.png"
        show screen hermione_main
        her "I'm glad you have such a high confidence in me."
        m "And I'm glad you're starting to believe in this. I think you have a very good potential to master this branch of magic."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "You seem tired professor."
        hide screen hermione_main
        g11 "{size=-2}(Tired of waiting to annihilate your ass){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_norm.png"
        show screen hermione_main
        her "Yes, professor?"
        g9 "Yes we can!"
        m "Uh, I mean, I'm sure I'll tire you out soon enough, Miss Granger. How about you get some sleep?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "Sleep? I must study first."
        hide screen hermione_main
        m "I wasn't thinking about that but you're right, time to go to bed!"
        m "Just make sure to think about what you learned today."
        "You dismiss Hermione."

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[16] "{size=-4}(Hmm, I wonder what he {b}was{/b} thinking about){/size}"
        her_[18] "{size=-4}(Probably all the problems caused by those harlots){/size}"
        her_[34] "{size=-4}(Well I will never be like them, so no need to worry){/size}"

        $ v_tutoring = 3
        jump l_tutoring_end

    elif v_tutoring == 3:   # Whoring lvl 3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051_norm.png"
        show screen hermione_main
        her "First sir, I want to apologize for doubting you."
        hide screen hermione_main
        m "Yes?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_norm_e.png"
        show screen hermione_main
        her "Your \"atypical\" method works!"
        hide screen hermione_main
        m "{size=-2}(Impossible){/size}"
        m "It works? I mean yes, naturally it works!"
        m "I'm glad you've succeeded. Now tell me more."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_blush.png"
        show screen hermione_main
        her "I managed to levitate a heavy rock while thinking about the behavior of two girls I saw earlier in the library."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n113_blush.png"
        show screen hermione_main
        her "Usually I only manage to move small rocks. I don't know, I felt kind of warm inside thinking about that."
        her "It felt weird but... {w=0.5}good at the same time."
        hide screen hermione_main
        m "{size=-2}(She is so ignorant of life, unbelievable){/size}"
        m "You've never felt such a sensation before?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a137_blush.png"
        show screen hermione_main
        her "Generally I get angry and rush to stop such behavior."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059_blush.png"
        show screen hermione_main
        her "But yesterday, I don't know, I just watched without interrupting them."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052b_blush.png"
        show screen hermione_main
        her "And when I pictured it, as you told me to, it worked."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n072_blush_t.png"
        show screen hermione_main
        her "I feel at the same level as those harlots, I'm so ashamed."
        m "But you succeeded."
        g9 "{size=-2}(To my surprise){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a079_blush_e.png"
        show screen hermione_main
        her "Yes! With this method I'll have better grades in my tests and win the House Cup for Gryffindor!"
        g9 "{size=-2}(In your dreams){/size}"
        m "Good, good. Now I want to know more about those two girls."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "It's not very relevant, professor. And I'm not sure this is appropriate."
        m "How will you improve yourself if I can't guide you?"
        m "And for that, I must know more."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a036_blush.png"
        show screen hermione_main
        her "Alright, but it's embarassing."
        g9 "{size=-2}(Ooh, I hope they were naked){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "I went to the library to study interactions between plants..."
        g11 "{size=-2}(Yeah, yeah, come on){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n013_blush.png"
        show screen hermione_main
        her "... and I heard muffled sounds."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a035_blush.png"
        show screen hermione_main
        her "I was hoping to catch a teacher doing bad things with one of those Slytherin whores."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "I slowly headed towards the sounds and I discovered two girls in an alcove."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n067_blush.png"
        show screen hermione_main
        her "I remained hidden to observe them."
        hide screen hermione_main
        g11 "{size=-2}(Come on!){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Yes, professor?"
        m "Yes, no, please continue."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "They were kissing passionately."
        g9 "And? And?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_blush.png"
        show screen hermione_main
        her "And a moment later they began to..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059b_blush.png"
        show screen hermione_main
        her "They began to..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n167b_blush2_t.png"
        show screen hermione_main
        her "They began to touch their breasts!"
        m "They were naked, I hope?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n054_blush.png"
        show screen hermione_main
        her "What?"
        her "No, fortunately they were dressed."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a073_blush.png"
        show screen hermione_main
        her "How can such a thing happen in our beloved school!"
        m "But you kept watching, didn't you?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a035_blush.png"
        show screen hermione_main
        her "Only for educational purposes."
        g9 "{size=-2}(\"Educational purposes\", haha, never heard a worse excuse){/size}"
        m "And during all this time you didn't feel a certain need?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "To my shame, yes. Like I said before, I felt kind of warm inside."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a026_blush.png"
        show screen hermione_main
        her "Like when I have to pee but... different. Better."
        m "This good sensation, next time you experience it, let it come."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "But..."
        m "It's the only way to get better, miss Hermione."
        m "If you suppress it, it won't work."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "Ok...{w=0.3} I'll try my best."
        her "But to be honest, sir, I thought you were going to punish those two sluts."
        hide screen hermione_main
        m "Can you provide proof of their crime? No?"
        m "Even I can't punish students without proof of any wrongdoing."
        g11 "{size=-2}(With the possible exception of you!){/size}"
        m "Anyway, you've done well. I think it will be enought for this lesson."
        m "Remember well what I just told you and good night!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n011_norm.png"
        show screen hermione_main
        her "Good night, professor."
        hide screen hermione_main
        "You dismiss Hermione."

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[12] "{size=-4}(Well, I'll try to investigate those two girls again){/size}"
        her_[18] "{size=-4}(Like a real anthropologist){/size}"
        her_[35] "{size=-4}(Yes, that's right, Hermione the anthropologist!){/size}"

        $ v_tutoring = 4
        jump l_tutoring_end

    elif v_tutoring == 4:   # Whoring lvl 5
        m "So, any luck with your \"studies\"?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_norm.png"
        show screen hermione_main
        her "Yes! When you hear the results of my hunt, you'll be proud of me!"
        m "{size=-2}(\"Hunt\"?){/size}"
        m "Your \"hunt\" Miss Hermione?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_norm.png"
        show screen hermione_main
        her "Yes professor!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "Like an explorer in the wild jungle, I tracked those two filthy animals."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_blush_e.png"
        show screen hermione_main
        her "With success, sir!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_norm.png"
        show screen hermione_main
        her "Hogwarts has so many dark and discreet corners..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "Believe me, it wasn't easy, professor."
        m "I'm sure you gave it your best."
        m "But right now I await your report."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Yes, but before that I want to clarify that my report is purely for scientific purposes."
        m "{size=-2}(Sure...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "So I tracked down those two tarts to an area in the attic."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "Which, by the way, seems to be the meeting place for girls of this... sort."
        m "And what is your opinion on them?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "At least they don't sleep with professors in exchange for house points."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        m "And that's it? No \"this behavior must be severely punished\" ?"
        m "Do you find girls of this sort attractive, miss Hermione?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "What? Lesbians? I'm not... I... no way I..."
        m "Alright, alright, back to your report if you please."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n077_blush.png"
        show screen hermione_main
        her "{size=-2}(I'm not a lesbian...{w=0.3} I think...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush.png"
        show screen hermione_main
        her "{size=-2}(Hermione, girl, pull yourself together! You're not a harlot!){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a029_blush.png"
        show screen hermione_main
        her "No, I'm not!"
        m "Excuse me?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052_blush.png"
        show screen hermione_main
        her "Uh, yes, my report. My {b}scientific{/b} report."
        m "{size=-2}(Yeah, we get it..){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "So, like before, they started by kissing passionately."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n053_blush.png"
        show screen hermione_main
        her "With the tongue and everything!"
        menu:
            "-Start to jerk off while she is talking-":
                $ d_flag_01 = True
                hide screen hermione_main
                hide screen blktone
                with d3
                ">You reach under the desk and grab your cock..."
                hide screen blktone8
                with d3
                hide screen genie
                show screen genie_jerking_off
                with d3
                pause
                $ h_body = "01_hp/27_ue/hermione/bd_her_n052_blush.png"
                show screen hermione_main
            "Do nothing.":
                $ h_body = "01_hp/27_ue/hermione/bd_her_n052_blush.png"
                show screen hermione_main
        g9 "And? And?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059_blush.png"
        show screen hermione_main
        her "They pulled up their shirts and caressed each others breasts."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "{size=-2}(Their beautiful and tempting breasts){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t1.png"
        show screen hermione_main
        her "Later those nasty girls raised their skirts and started to touch each other \"there\" while kissing."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c017_blush.png"
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03b.png"
        $ b_her_tears = True
        show screen hermione_main
        her "{size=-2}(I can't believe I said that!){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "They were very excited and I could see their panties become wet."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "Disgusting."
        if d_flag_01:
            g9 "{size=-2}(Yes... yes...){/size}"
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c098_blush_t.png"
        show screen hermione_main
        her "One of the girls went crazy and inserted her fingers into the other's \"thing\" and worked them furiously."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t1.png"
        show screen hermione_main
        her "Soon imitated by her girlfriend."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t1.png"
        show screen hermione_main
        her "Those whores came so hard they had to bite their lips not to scream."
        if d_flag_01:
            her "{size=-2}(And me too){/size}"
            hide screen hermione_main
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
            hide screen hermione_main
            with d3
            hide screen bld1
            with d3
            show screen genie_jerking_sperm
            with d3
            pause
            show screen bld1
            with d3
            $ h_body = "01_hp/27_ue/hermione/bd_her_a071_blush.png"
            show screen hermione_main
            with d3
            her "Professor!"
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
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "Maybe..."
        m "Anyway, I hope it was revealing."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "\"Revealing\"? I'm not sure what you mean by that."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "You're the headmaster, act as such!"
        her "Do all you can to stop those acts of debauchery!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a025_norm.png"
        show screen hermione_main
        m "Yes, of course."
        m "{size=-2}(Hypocrite){/size}"
        her "{size=-2}(Old pervert){/size}"
        m "You said that those girls became wet."
        g9 "Weren't you a little too?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n077_blush.png"
        show screen hermione_main
        her "When I went to bed I noticed it, yes."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush.png"
        show screen hermione_main
        her "Apparently bad fluids are released from your body when you have faced such acts."
        m "No, they aren't bad. It happens when you're excited."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a169_blush.png"
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_01b.png"
        $ b_her_tears = True
        show screen hermione_main
        her "No way! I can control myself!"
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n072_blush_t.png"
        show screen hermione_main
        m "No one can control their base desires."
        m "Consider this well and enjoy your night, Miss Hermione."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n025_norm_t.png"
        show screen hermione_main
        her "Good night, professor."
        hide screen hermione_main
        "You dismiss Hermione."

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[6] "{size=-4}(I enjoyed it too much. Maybe I'm becoming a pervert as well){/size}"
        her_[13] "{size=-4}(I lost control, it won't happen again!){/size}"
        her_[18] "{size=-4}(Good thing I'm not a degenerate like those filthy girls){/size}"

        $ v_tutoring = 5
        jump l_tutoring_end

    elif v_tutoring == 5:   # Whoring lvl 8
        m "Bravo, last time you experienced your first \"emotion\"."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "Yes, I remember but I still don't see the link with magic."
        hide screen hermione_main
        m "{size=-2}(Me neither...){/size}"
        m "If you want to progress, you have to go a little further than a simple observation."
        m "You'll need to participate."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a168_blush.png"
        show screen hermione_main
        her "What! No way I'll participate in such debauchery!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a071_norm.png"
        show screen hermione_main
        her "How can you even suggest such a thing!"
        m "Oh you don't have to go that far in one go."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a059b_norm.png"
        show screen hermione_main
        her "I'm not sure I want to go there at all."
        m "How many times do I have to remind you why you're doing this?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "Yes but..."
        m "But what?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "A girl like me shouldn't stoop to such practices."
        m "A girl like you should use all means at their disposal in order to excel."
        her "..........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "Alright, but this must remain between us."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n037_norm.png"
        show screen hermione_main
        her "You cannot disclose this to other professors, especially professor Snape!"
        m "Oh, I have no intention of shar.. speaking of you with professor Snape."
        g9 "{size=-2}(You're mine){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_blush.png"
        show screen hermione_main
        her "Well, what must I do now?"
        m "Come here."
        hide screen hermione_main
        with d3
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d1
        pause.5
        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen no_groping_01
        with d1
        hide screen blkfade
        with d5
        pause
        m "Have you ever touched yourself?"
        hide screen ctc
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "Professor!"
        show screen groping_01
        with d7
        ">You touch her leg with your hands."
        m "Please answer the question, Miss Granger. Have you ever touched yourself?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "No, it's... it's wrong!"
        m "But when you looked at these girls, you felt certain emotions."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n067_blush.png"
        show screen hermione_main
        her "Yes and ?"
        m "You didn't feel the need to touch yourself?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Yes... but I resisted."
        ">You start to caress her thigh."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059_blush.png"
        show screen hermione_main
        her "Professor..."
        m "And you felt those emotions without even touching yourself."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052b_blush.png"
        show screen hermione_main
        her "Yes..."
        g9 "{size=-2}(What a slut){/size}"
        if whoring <= 12 or custom_bra >0:
            ">You move forward to her panties."
        else:
            ">You move forward to her pussy."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059b_blush.png"
        show screen hermione_main
        m "Good."
        hide screen groping_01
        show screen no_groping_01
        ">You stop caressing her."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush.png"
        show screen hermione_main
        her "Why... why did you stop?"
        m "Oh, because I need you to think about all this before we meet again."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush_t.png"
        show screen hermione_main
        her "But..."
        m "Good night, my dear."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n025_norm_t.png"
        show screen hermione_main
        her "Good night, professor."
        hide screen hermione_main
        show screen blkfade
        with d3
        hide screen no_groping_01
        "You dismiss Hermione."
        hide screen blkfade
        show screen genie

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[12] "{size=-4}(This is wrong...){/size}"
        her_[15] "{size=-4}(I shouldn't listen to him){/size}"
        her_[16] "{size=-4}(And yet...){/size}"

        $ v_tutoring = 6
        jump l_tutoring_end

    elif v_tutoring == 6:   # Whoring lvl 11
        m "Miss Hermione, I wanted to remind you that this is not a formal lesson."
        m "You need not wear your uniform for these lessons."
        m "At least take off that tie, I know it gets uncomfortable after all these hours."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a051_norm.png"
        show screen hermione_main
        her "The school rules are very strict about this, professor."
        m "You have my permission, Miss Granger."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a026_blush.png"
        show screen hermione_main
        her ".........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a025_norm.png"
        show screen hermione_main
        her "Right. But only when I come to see you in the evenings."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "{size=-2}(I have to be careful with my reputation.){/size}"
        m "It's a deal."
        show screen blkfade
        with d3
        ">Hermione takes off her tie."
        ##$ v_her_current_shirt = "shirt1_without_tie"
        ##$ v_her_shirt = v_her_current_shirt
        hide screen hermione_02
        show screen hermione_02
        hide screen hermione_main
        hide screen blkfade
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_blush.png"
        show screen hermione_main
        m "There. Doesn't that feel better?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "Actually, it does, sir. Thank you."
        m "So, have you started practicing my teachings?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "I don't even know where to start."
        m "You see, the secret is to stimulate appropriate areas."
        m "Areas which are more sensitive than others."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "You mean my intimate areas, sir?!"
        hide screen hermione_main
        m "Well, they're called intimate for a reason."
        m "You said you've never touched yourself because it was wrong."
        m "But it's never wrong to exercise ones body in order to reach a new level of consciousness."
        g4 "{size=-2}(The things I have to make up...){/size}"
        m "You can begin with your breasts, for example."
        m "But you shouldn't only caress your nipples but also grab your tits and squeeze them."
        m "And in the meanwhile, you can think of those two girls."
        g9 "Or what you want to do with those girls."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a079_blush_e.png"
        show screen hermione_main
        her "What makes you think... No, I don't want..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a169_blush.png"
        show screen hermione_main
        her "I definitely don't want to have {b}anything{/b} to do with those harlots!"
        m "Don't lie to yourself. It's obvious that you feel a form of attraction to those two girls."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n113_blush_t.png"
        show screen hermione_main
        her "I...{w=0.3} I honestly don't know what to think anymore."
        her "At the moment my feelings are so confusing..."
        g9 "{size=-2}(Exactly what I was hoping){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n075_blush_t.png"
        show screen hermione_main
        her "I'm happy to earn points for my house and at the same time I feel so ashamed."
        her "And the same goes for your lessons."
        m "Yet you can't deny your progress in the practice of magic."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03b.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "...{w=0.2} Yes...{w=0.2} perhaps you're right."
        m "You have to let it go, Miss Hermione, follow your instincts!"
        g9 "{size=-2}(Grab my cock and wank it savagely!){/size}"
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055b_blush_t.png"
        show screen hermione_main
        her "I'm not sure if..."
        m "Enough procrastination, time for practice!"
        m "Come here."
        show screen blkfade
        with d1
        pause.5
        ">Hermione walks towards your desk."
        hide screen hermione_02
        hide screen genie
        ">You grab her tits and massage them softly."
        show screen ctc
        show screen groping_03
        with d1
        $ h_xpos = 160
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059_blush.png"
        show screen hermione_main
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "Like I said, it's important you learn how to properly stimulate your \"emotional\" body areas."
        m "It's not enough if I do it myself, you need to practice when you're alone."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n008_blush.png"
        show screen hermione_main
        m "Like in your bed or in the shower, for example."
        ">You keep massaging her tits..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        ">You feel her nipples becoming hard."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "Yes but...{w=0.3} Professor, it's inappropriate for a girl of good education!"
        m "Don't let old prejudices weigh you down. You're a girl with great potential."
        ">You gently squeeze her nipples through the fabric."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "Ah, thank you professor."
        m "A girl with a brilliant mind."
        ">You increase your grip on her nipples."
        m "A girl who will become a woman of exception."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c068_blush.png"
        show screen hermione_main
        her "Ahh yes... I'm already a woman of exception you fool."
        m "Fool?"
        ">You firmly pinch her nipples."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c098_blush_t.png"
        show screen hermione_main
        her "Ahhh yesss, not that hard, yesss..."
        ">You abruptly stop."

        show screen blkfade
        with d5
        hide screen hermione_main
        hide screen groping_03
        show screen genie_and_hermione
        hide screen blkfade
        with d1
        $ h_body = "01_hp/27_ue/hermione/bd_her_a162_blush_e.png"
        show screen hermione_main
        her "Don't stop, you idiot!"
        show screen blkfade
        ">She moves away from the desk."
        hide screen genie_and_hermione
        show screen genie
        show screen hermione_02
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush_t.png"
        show screen hermione_main
        hide screen blkfade
        with d1

        her "..........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n072_blush_t.png"
        show screen hermione_main
        her "Sorry, professor."
        m "Lesson is over. Time to practice by yourself."
        m "Good night my little witch."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_norm.png"
        show screen hermione_main
        her "Good night professor and thank you for this lesson."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "{size=-2}(This too short of a lesson){/size}"
        hide screen hermione_main

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[4] "{size=-4}(\"My little witch?\"){/size}"
        her_[6] "{size=-4}(Why not, after all...){/size}"

        $ lock_public_favors = True
        $ v_tutoring = 7
        jump l_tutoring_end

    elif v_tutoring == 7:   # Whoring lvl 14
        m "So, Miss Hermione, have you practiced my teachings?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "Yes...{w=0.2} a little."
        m "And?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_blush_e.png"
        show screen hermione_main
        her "It feels even better when I'm naked."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush.png"
        show screen hermione_main
        her "{size=-2}(Oh no, I should never have said that){/size}"
        m "Well come here and undress, we'll practice."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n113_blush.png"
        show screen hermione_main
        her "Completely?!"
        m "No, only the top will suffice."
        g9 "{size=-2}(For the moment...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "I'll be showing you my breasts without even earning any points?"
        m "You can't have both points and lessons."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a079_blush_e.png"
        show screen hermione_main
        her "Ok..."
        hide screen hermione_main
        hide screen hermione_02
        show screen hermione_04
        ##call her_pose("shirt raised")
        $ lift_shirt = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_a035_blush.png"
        show screen hermione_main
        with fade
        her "Like that?"
        if custom_bra >=1 and badges and custom_outfit <= 0:
            m "Without your bra Miss Hermione... and come here."
        else:
            m "Yes and now come here."
        $ badges = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n039_blush.png"
        show screen hermione_main
        her "........"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
        show screen hermione_main
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
        $ h_xpos = 160
        $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
        show screen hermione_main
        hide screen blkfade
        with d5
        pause
        show screen bld1
        with d3
        hide screen ctc
        m "Now let's get serious if you want to."
        g9 "{size=-2}(Well, even if you don't...){/size}"

        hide screen hermione_main
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

        $ h_body = "01_hp/27_ue/hermione/bd_her_n127_blush.png"
        show screen hermione_main
        her "Professor, what are you doing?"
        g9 "Teaching you, dear, teaching you."
        m "Doesn't it feel good?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
        show screen hermione_main
        her "A little..."
        m "Your hard nipples say the contrary."
        m "I can stop if you want."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        her "Yeah sure!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n097_blush.png"
        show screen hermione_main
        her "Suck them professor."
        g9 "As you wish, princess."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n095b_blush_t.png"
        show screen hermione_main
        ">You suck her nipples with devotion."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03c.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t2.png"
        show screen hermione_main
        her "Yes {image=textheart.png} like that."
        ">You start to chew on her nipples."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177b_blush_t.png"
        show screen hermione_main
        her "Ah, noo, don't..."
        ">You chew on them even harder."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t2.png"
        show screen hermione_main
        her "Not that hard, I will..."
        g9 "{size=-2}(Time for the grand finale){/size}"
        if whoring <= 12 or custom_bra >0:
            ">You quickly slip your hand into her panties and rub her pussy furiously."
        else:
            ">You quickly move your hand toward her pussy and rub it furiously."
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c078_blush_t.png"
        show screen hermione_main
        her "Yes! {image=textheart.png}"
        her "I... I..."
        g9 "Came, my dear."
        show screen blkfade
        with d5
        pause
        ##call her_pose()
        $ lift_shirt = False
        $ badges = True
        hide screen hermione_main
        hide screen chair_02
        hide screen groping_naked_tits
        hide screen genie
        hide screen blkfade
        show screen genie_and_hermione
        with d1
        $ h_body = "01_hp/27_ue/hermione/bd_her_n016_blush_m.png"
        show screen hermione_main
        her "Is the lesson over professor?"
        m "Not if you don't want it to be."
        her "Maybe it's enough for tonight."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n062_blush_m.png"
        show screen hermione_main
        her "After all, you have a lot of work to do."
        m "Sure."
        m "But before that I have a little present for you."
        $ the_gift = "01_hp/18_store/19.png"
        show screen gift
        with d3
        ">You give an assortment of adult magazines to Hermione."
        hide screen gift
        m "I hope this will help you in your studies."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n069_blush_m.png"
        show screen hermione_main
        her "Yes, certainly."
        her "Thank you and good night professor."
        m "Good night dear child."
        hide screen hermione_main
        show screen blkfade
        with d3
        hide screen genie_and_hermione
        "You dismiss Hermione."
        hide screen blkfade
        show screen genie

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[6] "{size=-4}(I'm such a slut...){/size}"
        her_[16] "{size=-4}(Coming in front of my professor){/size}"
        her_[18] "{size=-4}(I definitely need to do that again){/size}"

        $ v_tutoring = 8
        jump l_tutoring_end

    elif v_tutoring == 8:   # Whoring lvl 17
        m "Miss Hermione, is my office really that cold that you need to wear your vest?"
        m "I don't want you getting all hot and sweaty."
        m "{size=-2}(Oh wait...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a059b_norm.png"
        show screen hermione_main
        her "It's the vest or the tie but I must have a symbol of my house!"
        m "Alright, alright, you can wear your tie if you insist."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n020_blush.png"
        show screen hermione_main
        her "{size=-2}(I've never seen him give in so quickly...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "{size=-2}(I did well to exercise my authority!){/size}"
        show screen blkfade
        with d3
        ">Hermione takes off her vest and puts her tie back on."
        ##$ v_her_current_shirt = "shirt2"
        ##$ v_her_shirt = "shirt2_tucked"
        hide screen hermione_02
        show screen hermione_02
        hide screen hermione_main
        hide screen blkfade
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_blush.png"
        show screen hermione_main
        m "So tell me, were your readings enlightening?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "I'm not sure if \"readings\" is the right term but yes. Very \"stimulating\" too."
        m "Maybe it's time to discover new areas to stimulate."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "You mean my pussy, right?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a036_norm.png"
        show screen hermione_main
        her "I'm not an idiot, professor."
        m "If it doesn't suit you, we can stop here."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "And if I said stop?"
        g4 ".........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "Haha, you should have seen your face!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n156_blush.png"
        show screen hermione_main
        her "With all your recent lessons you can imagine that this area isn't a *no man's land* any more."
        g4 "Have you slept..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a168_blush.png"
        show screen hermione_main
        her "No I haven't! I'm not a harlot who offers her pussy to every boy around."
        m "{size=-2}(Good, your pussy is mine alone){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_norm.png"
        show screen hermione_main
        g9 "{size=-2}(Although I may agree to share it with other girls...){/size}"
        m "I'm happy you're behaving honorably, Miss Hermione."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_norm.png"
        show screen hermione_main
        her "Ha, who'd have guessed!"
        m "Yes, I'm glad that my favorite student is not wasting her precious time with boys."
        her "Sure...{w=0.3} {size=-4}old hypocrite{/size}."
        m "Enough of this! Now take off your shirt and come here."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "Here we go for another \"lesson\"."
        hide screen hermione_main
        hide screen hermione_02
        show screen hermione_04
        ##$ v_her_shirt = 0
        $ wear_shirts = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_a035_blush.png"
        show screen hermione_main
        with fade
        if custom_bra >=1 and badges and custom_outfit <= 0:
            m "And your bra..."
            $ badges = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n039_blush.png"
        show screen hermione_main
        her "........"
        show screen ctc
        pause
        show screen blkfade
        hide screen hermione_main
        with d3
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        hide screen blkfade
        hide screen hermione_04
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d1
        pause.5
        hide screen hermione_walk_01
        hide screen genie
        show screen no_groping_06
        hide screen blkfade
        with d5
        pause
        hide screen ctc
        $ h_xpos = 160
        $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
        show screen hermione_main
        hide screen blkfade
        with d5
        pause
        hide screen ctc
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        her "And free tits again, enjoy!"
        m "I definitely intend to."
        g9 "Lift your skirt."
        ##call her_pose("skirt raised")
        $ skirt_up = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n011_blush2.png"
        show screen hermione_main
        with d3
        show screen ctc
        pause
        hide screen ctc
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        if whoring >= 13 and custom_bra == 0:
            her "You love my pussy don't you?"
            g9 "Oh yes, I love your smell, especially when you're wet."
            $ h_body = "01_hp/27_ue/hermione/bd_her_n068b_blush_e.png"
            show screen hermione_main
            her "Professor..."
            hide screen no_groping_01
            show screen groping_06
            with d3
            ">You caress her clit."
            $ h_body = "01_hp/27_ue/hermione/bd_her_n020_blush.png"
            show screen hermione_main
            her "Professor!"
        else:
            her "You love my panties don't you?"
            g9 "Oh yes, I love their smell, especially when you're wet."
            $ h_body = "01_hp/27_ue/hermione/bd_her_n068b_blush_e.png"
            show screen hermione_main
            her "Professor..."
            hide screen no_groping_01
            show screen groping_06
            with d3
            ">You caress her clit through the fabric."
            $ h_body = "01_hp/27_ue/hermione/bd_her_n020_blush.png"
            show screen hermione_main
            her "Professor!"
            m "Now take them off."
            show screen blkfade
            with d5
            ">She slowly lowers her panties."
            hide screen hermione_main
            hide screen groping_06
            show screen no_groping_06
            hide screen blkfade
            $ b_her_panties_off = True
            $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
            show screen hermione_main
            with d3
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
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        her "Yes, you're probably right."
        m "Probably?!"
        ">While you're moving your finger in her pussy, you take over her clit with your thumb."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n097_blush.png"
        show screen hermione_main
        her "Haa {image=textheart.png}, I'm only your humble student, I wouldn't know such naughty things."
        m "One finger is rarely enough even with a tight pussy like yours."
        ">You insert a second finger in her tight and warm pussy..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t2.png"
        show screen hermione_main
        her "Yesss {image=textheart.png}, I'll try to remember your teachings."
        ">You increase the pace and feel her pussy tighten on your fingers."
        m "Maybe a third finger?"
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_01.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        her "Don't be so bold."
        ">Her whole body starts shaking as you increase your ramming."
        hide screen groping_06
        show screen groping_06b
        with d1
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177b_blush.png"
        show screen hermione_main
        her "Noo {image=textheart.png}{w=0.2} not so fast I will..."
        ">You increase your pace even more."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush.png"
        show screen hermione_main
        her "I will I will..."
        g9 "Time to get serious."
        ">You force your soaked thumb into her butthole."
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c189_blush_t.png"
        show screen hermione_main
        her "Haaaaa {image=textheart.png} yesss {image=textheart.png}."
        g9 "Lucky girl."
        show screen blkfade
        with d5
        pause
        ##call her_pose()
        hide screen hermione_main
        hide screen groping_06b
        hide screen genie
        hide screen blkfade
        show screen no_groping_01
        with d1
        $ h_body = "01_hp/27_ue/hermione/bd_her_n016_blush_m.png"
        show screen hermione_main
        her "I'm sure this lesson will be of great help tonight."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n096_blush_m.png"
        show screen hermione_main
        her "And the other nights {image=textheart.png}."
        m "Always glad to help my little witch in her studies."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n063_blush_m.png"
        show screen hermione_main
        her "\"Studies\", yes, that's right."
        m "And to aid your studies I have even more scientific materials."
        $ the_gift = "01_hp/18_store/20.png"
        show screen gift
        with d3
        ">You give an assortment of porn magazines to Hermione."
        hide screen gift
        $ h_body = "01_hp/27_ue/hermione/bd_her_n069_blush_m.png"
        show screen hermione_main
        her "You can be certain that I'll study them profoundly."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n016_blush_m.png"
        show screen hermione_main
        her "Thank you and good night professor."
        m "Good night, my favorite little witch."
        hide screen hermione_main
        show screen blkfade
        with d3
        hide screen no_groping_01
        "You dismiss Hermione."
        hide screen blkfade
        show screen genie

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[6] "{size=-4}(Favorite...){/size}"
        her_[7] "{size=-4}(There's another one?){/size}"
        her_[35] "{size=-4}(I'll do my best to remain his favorite!){/size}"

        $ v_tutoring = 9
        jump l_tutoring_end

    elif v_tutoring == 9:   # Whoring lvl 20
        m "So, Miss Hermione, have you had an enjoyable night?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_blush.png"
        show screen hermione_main
        her "You shouldn't ask such things, Professor."
        m "I have to make sure my students have a pleasant nights rest."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "With your teachings and your \"scientific\" literature, indeed."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "I'll become proficient in human anatomy with all this documentation."
        m "Do you need some scientific instruments for your research?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n067_blush.png"
        show screen hermione_main
        her "They could come in handy."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a035_blush.png"
        show screen hermione_main
        her "As long as it's not your dick."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "{size=-2}(Not that I don't appreciate it but no points no cock!){/size}"
        m "Miss Hermione! This is a serious matter!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "Sure..."
        m ".........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "So what's my gift this time?"
        $ the_gift = "01_hp/18_store/13.png"
        show screen gift
        with d3
        ">You give the vibrator to Hermione"
        hide screen gift
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "And I suppose you want me to test this in front of you?"
        g9 "Of course."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "Where is the educational purpose in all of this?"
        m "Good question. Improving your skills?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a124_blush.png"
        show screen hermione_main
        her "At what? Magic?"
        m "Certainly."
        her "........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n065_blush.png"
        show screen hermione_main
        her "I have one request though."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "If I'm going to masturbate I don't want to be the only one. So enjoy the free show."
        g9 "With pleasure!"
        ">You reach under the desk and grab your cock."
        hide screen hermione_main
        hide screen blktone
        with d3
        hide screen genie
        show screen genie_jerking_off
        with d3
        ##call her_pose("fingering")
        $ fingering = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n175_blush.png"
        show screen hermione_main
        with d3
        her "{size=-2}(Thinking of the headmaster masturbating makes me wet already {image=textheart.png}){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144b_blush.png"
        show screen hermione_main
        her "{size=-2}(I've become such a whore. Not that I enjoy it all that much though){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n056_blush.png"
        show screen hermione_main
        her "So... where do we start?"
        if custom_bra == 0:
            m "Take off your shirt and bra, I want to see your tits."
            ##$ v_her_bra = 0
        else:
            m "Take off your shirt, I want to see your tits."
        show screen blkfade
        with d5
        hide screen hermione_main
        hide screen hermione_02
        hide screen blkfade
        with d1
        ##$ v_her_shirt = 0
        $ badges = False
        $ wear_shirts = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        pause
        her "You love them don't you?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        g9 "Oh yes..."
        her "Having watched the other girls I now know why."
        her "Those breasts are so tempting."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177b_blush_t.png"
        show screen hermione_main
        her "Big or small, I want to hold them in my hands and suck the nipples."
        g9 "Me too, me too!"
        m "Now lift your skirt!"
        show screen blkfade
        with d5
        hide screen hermione_main
        hide screen blkfade
        with d1
        ##call her_pose("fingering skirt raised")
        $ skirt_up = True
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_01.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        pause
        her "Good idea."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n056_blush.png"
        show screen hermione_main
        her "Sometimes I wish I could do this with others girls."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "Masturbate naked in front of each other."
        if whoring <= 12 or custom_bra >0 and panties:
            g9 "Yes go on, take off your panties!"
            show screen blkfade
            with d5
            hide screen hermione_main
            hide screen blkfade
            with d1
            $ panties = False
            $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_02b.png"
            $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
            show screen hermione_main
            pause
            her "Your wish is my command."
            $ h_body = "01_hp/27_ue/hermione/bd_her_n095_blush.png"
            show screen hermione_main
            her "And mine is to touch another girl's pussy."
        else:
            $ h_body = "01_hp/27_ue/hermione/bd_her_n095_blush.png"
            show screen hermione_main
            her "Touch her pussy like I'm touching mine now."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n174_blush.png"
        show screen hermione_main
        her "Caress it."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177_blush.png"
        show screen hermione_main
        her "Insert my fingers into her wet pussy."
        g11 "Yes, yes! Now the vibrator!"
        show screen blkfade
        with d5
        hide screen hermione_main
        hide screen blkfade
        with d1
        ##call her_pose("vibrator")
        $ vibrator = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c078_blush_t.png"
        show screen hermione_main
        pause
        her "Oh I had forgotten about it already."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c179_blush_t.png"
        show screen hermione_main
        her "I want to hear her moan as I work my fingers."
        her "Hear her cum!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c189_blush_t.png"
        show screen hermione_main
        her "Like me! Aaah yesssss! {image=textheart.png} {image=textheart.png}"
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
        hide screen hermione_main
        hide screen genie_jerking_sperm_02
        hide screen her_naked
        show screen genie
        show screen hermione_02
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
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055b_blush_m.png"
        show screen hermione_main
        her "I hope you enjoyed it as much I did."
        m "Oh fuck yes, you're doing great, my little witch!"
        g9 "Very good!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n062_blush_m.png"
        show screen hermione_main
        her "Thank you, professor."
        m "After all this, you need to rest."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n069_blush_m.png"
        show screen hermione_main
        her "Oh yes. Good night professor."
        m "Good night, my dirty little slut."
        "You dismiss Hermione."
        hide screen hermione_main
        hide screen hermione_02
        show screen blkfade
        with d3
        hide screen blkfade
        show screen genie

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[16] "{size=-4}(Rest...){/size}"
        her_[18] "{size=-4}(Not before I've played with this marvelous toy again){/size}"
        her_[34] "{size=-4}(And again){/size}"

        $ v_tutoring = 10
        jump l_tutoring_end

    elif v_tutoring == 10:   # Whoring lvl 23
        m "Miss Hermione, I see you still insist on wearing that tie."
        m "Don't you get tired of wearing it constantly?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_norm.png"
        show screen hermione_main
        her "I suppose I do... But I'm proud of being a Gryffindor and I'm willing to make such a small sacrifice for my house."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "{size=-2}(It does get stifling quite often){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        m "Miss Hermione, I know how strongly you feel towards your house. There's no need to keep up appearances in this office."
        her "Are you sure, professor?"
        m "Miss Hermione, I think you will feel much better without that tie."
        g9 "{size=-2}(And even better when covered in my cum){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "If you insist, professor."
        show screen blkfade
        with d3
        ">Hermione takes off her tie."
        ##$ v_her_current_shirt = "shirt3"
        ##$ v_her_shirt = "shirt3_tucked"
        hide screen hermione_main
        hide screen blkfade
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_blush.png"
        show screen hermione_main
        m "So... I hope my lessons are paying off."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_norm.png"
        show screen hermione_main
        her "You mean, by making me more \"open\" to the wonders of adulthood?"
        m "Among other things..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "That's what I thought."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "But to be honest, I was looking forward to this lesson."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078_norm.png"
        show screen hermione_main
        her "{size=-2}(Maybe, I shouldn't have said that){/size}"
        her "{size=-2}(This will drive him crazy and he'll rape me savagely on his desk){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "{size=-2}(Not that I would mind...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n156_blush.png"
        show screen hermione_main
        her "{size=-2}(And I could ask him for points afterwards){/size}"
        m "Miss Hermione? Are you alright?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n074_blush.png"
        show screen hermione_main
        her "Yes professor! Sorry, I was thinking of my next exam."
        m "Oh, I'm sure it's an important one. Maybe next lesson I can help you revise."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "I would love that!"
        m "So, anal stimulation..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "Ah! I knew you would say that."
        her "{size=-2}(Once again, not that I mind...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c017_blush.png"
        show screen hermione_main
        her "{size=-2}(I'm such a whore, even the Slytherin girls can't compete...){/size}"
        m "Come again, Miss Hermione?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_blush_e.png"
        show screen hermione_main
        her "In this school nobody can compete with me, right professor?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "In any field!"
        m "In any field? I'm not sure."
        m "You still have things to learn..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a168_blush.png"
        show screen hermione_main
        her "What?! What are we waiting for then?"
        ">She rips off her shirt and rushes to your desk."
        show screen blkfade
        hide screen hermione_main
        with d3
        ##$ v_her_shirt = 0
        ##$ v_her_bra = 0
        $ badges = False
        $ wear_shirts = False
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        hide screen blkfade
        hide screen hermione_02
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d1
        pause.5
        hide screen hermione_walk_01
        hide screen genie
        show screen groping_05
        hide screen blkfade
        with d5
        pause
        m "We haven't even started yet and you're already wet, my adorable slut."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a036_blush.png"
        show screen hermione_main
        her "It's you and your dirty talk!"
        her "Talking about anal insertions, asshole licking and... and..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "Fisting!"
        m "I never mentioned any of that."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n023_blush.png"
        show screen hermione_main
        her "Oh. You didn't?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Well maybe you didn't but you {b}were{/b} thinking about it!"
        g9 "Maybe."
        g9 "Your ass is so luscious I could eat it."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "My point exactly!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "Enough talking, old man. Get to work!"
        m "I haven't even given you your gift yet!"
        m "I'll just put it where you'll be sure to find it."
        m "So, can we start the lesson?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a058_blush.png"
        show screen hermione_main
        her "Yes for Merlin's sake!"
        m "But before that..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a162_blush.png"
        show screen hermione_main
        her "If you say another word I swear I will go back to my dorm right now!"
        ">You suddenly insert the anal plug."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t2.png"
        show screen hermione_main
        her "Yesss {image=textheart.png} like that!"
        ">You remove it just as quickly while giving her butt a loud slap."
        play sound sd_boing1
        with flashbulb
        play sound sd_slap
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177b_blush_t.png"
        show screen hermione_main
        her "Yessss more {image=textheart.png}."
        g9 "As you wish, princess."
        ">You promptly insert and remove it."
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03d.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c178_blush.png"
        show screen hermione_main
        her "More!!"
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03b.png"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t2.png"
        show screen hermione_main
        her "Aaaah {image=textheart.png}."
        play sound sd_boing1
        pause.1
        play sound sd_slap
        with hpunch
        m "You can touch yourself too, you know."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03d.png"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n186_blush.png"
        show screen hermione_main
        her "I can't."
        her "{size=-2}(If I do, I will lose what little dignity I have left){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush.png"
        show screen hermione_main
        her "{size=-2}(But tonight...){/size}"
        m "I'll handle it then."
        ">You finger both her butthole and her pussy."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c188_blush.png"
        show screen hermione_main
        her "Nooo it's too much {image=textheart.png}."
        g9 "Faster? No problem!"
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c078_blush_t.png"
        show screen hermione_main
        her "Aaah, you're killing me {image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c099_blush_t.png"
        show screen hermione_main
        her "{size=-2}(And I love it){/size}"
        m "More fingers?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c058_blush_t.png"
        show screen hermione_main
        her "No more pleassse."
        m "Actually, it wasn't a question."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c078_blush_t.png"
        show screen hermione_main
        her "If you keep this pace I will..."
        ">You feel her muscles tighten on your fingers."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c189_blush_t.png"
        show screen hermione_main
        her "Come!!"
        g9 "Good girl."
        her "Keep it up, I..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t3.png"
        show screen hermione_main
        her "Yessss {image=textheart.png}."
        m "I can keep this up as long as you please."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_04.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush.png"
        show screen hermione_main
        her "Yesss {image=textheart.png}, nooo I will die!"
        g9 "In ecstasy."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c188_blush.png"
        show screen hermione_main
        her "Aahh not again {image=textheart.png}."
        hide screen groping_05b
        show screen no_groping_05
        m "I think you've had enough for one night."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c178_blush.png"
        show screen hermione_main
        her "Yes I... I better go."
        m "You forgot your gift."
        ">You promptly insert the butt plug."
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush.png"
        show screen hermione_main
        her "Aaaaaaah."
        hide screen no_groping_05
        show screen no_groping_05_desk
        hide screen hermione_main
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
        show screen hermione_02
        hide screen blkfade
        with d3

        #$ aftercum = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n016_blush_m.png"
        show screen hermione_main
        pause
        her "Thank you for everything, professor."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n062_blush_m.png"
        show screen hermione_main
        her "It was very...{w=0.5} enlightening."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n069_blush_m.png"
        show screen hermione_main
        her "But please, try to go easy on me next time."
        g9 "I have absolutely no idea what you mean by that."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n016_blush_m.png"
        show screen hermione_main
        her "Good night professor."
        m "Good night, my dear anal whore."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055b_blush_m.png"
        show screen hermione_main
        her "Professor..."
        "You dismiss Hermione."
        hide screen hermione_main
        hide screen hermione_02
        show screen blkfade
        with d3
        hide screen blkfade
        show screen genie

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[35] "{size=-4}(Finally tonight I'll just go to bed){/size}"
        her_[15] "{size=-4}(That was a little too intense){/size}"
        her_[34] "{size=-4}(Not that I'm complaining...){/size}"

        $ v_tutoring = 11
        jump l_tutoring_end

    elif v_tutoring == 11:
        m "So..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "Wait..."
        show screen blkfade
        with d3
        ">Hermione unbuttons her collar."
        ##$ v_her_current_shirt = "shirt4"
        ##$ v_her_shirt = "shirt4_tucked"
        hide screen hermione_main
        hide screen blkfade
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        her "You have another gift for me?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059_blush.png"
        show screen hermione_main
        her "Please, please."
        m "I thought I had to go easier on you?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "Oh don't worry, it was just a moment of weakness."
        her "I'm ready now!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n037_norm.png"
        show screen hermione_main
        her "{size=-2}(My body perhaps not...){/size}"
        m "Did you have fun with your anal plug?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c017_blush.png"
        show screen hermione_main
        her "Y-yes... I wear it sometimes..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a035_blush.png"
        show screen hermione_main
        her "But I cut the tail!"
        her "{size=-2}(No way I could walk around like that...){/size}"
        m "And you like it?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "It's very...{w=0.5} stimulating. It helps me whenever I cast a spell."
        m "Tell me the truth Miss Hermione, you wear it all the time, don't you?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "Nooo..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n027_blush.png"
        show screen hermione_main
        her "Maybe..."
        her "........"
        m "Don't be ashamed, it's alright my little whore."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_blush_e.png"
        show screen hermione_main
        her "I wear it all the time and...{w=0.3} I love it!"
        g9 "{size=-2}(Marvelous){/size}"
        m "I've taught you good."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n058_norm.png"
        show screen hermione_main
        her "To be a slut? Yes you have..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "And now I want more so where is my gift?!"
        m "There, there."
        $ the_gift = "01_hp/18_store/gift_anal_beads.png"
        show screen gift
        with d3
        ">You give the anal beads to Hermione"
        hide screen gift
        with d3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n108_blush.png"
        show screen hermione_main
        her "Oh! That's even better than a butt plug."
        g9 "And they can be useful for your pussy too."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "So many possibilities..."
        her "...so little time."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n159_norm.png"
        show screen hermione_main
        her "I suppose you want me to try them out?"
        her "Or would you rather try them out on me yourself?"
        g9 "Oh yes."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_norm.png"
        show screen hermione_main
        her "I don't even know why I'm asking..."
        her "{size=-2}(Old pervert...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "{size=-2}({b}My{/b} old pervert){/size}"
        show screen blkfade
        if custom_bra >=1 and badges and custom_outfit <= 0:
            ">She wantonly removes her shirt and bra."
            ##$ v_her_bra = 0
        else:
            ">She wantonly removes her shirt."
        hide screen hermione_main
        hide screen hermione_02
        pause.5
        hide screen blkfade
        ##$ v_her_shirt = 0
        $ badges = False
        $ wear_shirts = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n097_blush.png"
        show screen hermione_main
        her "My tits are the best in all of Hogwarts!"
        m "Have you been with many girls to say that?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush.png"
        show screen hermione_main
        her "I wish..."
        g9 "I can tutor you on that too."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Maybe we should finish this lesson first."
        m "Oh, we have time."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "Speaking of that..."
        show screen blkfade
        hide screen hermione_main
        with d3
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        hide screen blkfade
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d1
        pause.5
        hide screen hermione_walk_01
        hide screen genie
        show screen ctc
        show screen no_groping_05
        with d1
        hide screen blkfade
        with d5
        pause
        hide screen ctc
        g9 "As always, it's a delightful view."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "I'm glad you love it."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n061_blush.png"
        show screen hermione_main
        her "Can we start now?"
        g9 "I suppose you want them in your ass?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Naturally."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
        show screen hermione_main
        her "{size=-2}(I'll try them in my pussy later tonight){/size}"
        hide screen no_groping_05
        show screen groping_05
        ">You push the first bead in with ease."
        her "Hmmm {image=textheart.png}"
        m "How many do you think you can take, my dear?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "How many have you got?"
        g9 "That's the spirit!"
        ">You push another one inside with little resistance."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "Yess {image=textheart.png}, one more please."
        ">You feel the beads sink deeper when you push the third one inside."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_01.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush.png"
        show screen hermione_main
        her "Ohhh, they're... they're moving {image=textheart.png}."
        ">The fourth takes some work before it pops in."
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t2.png"
        show screen hermione_main
        her "Ah {image=textheart.png} ah {image=textheart.png}."
        ">You push the last one forcefully inside."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177b_blush_t.png"
        show screen hermione_main
        her "Ahhhhh {image=textheart.png}, delightful."
        her "They're so deep in my ass... almost like your cock."
        g9 "I can..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n039_blush.png"
        show screen hermione_main
        her "No you can't! My butthole is too tight for both."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush.png"
        show screen hermione_main
        her "{size=-2}(But it's such a good idea){/size}"
        m "I'm sure there's still room for at least one finger."
        ">You finger her butthole gently."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t1.png"
        show screen hermione_main
        her "Ahh... {image=textheart.png}{w=0.5} aah...{image=textheart.png}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_a066_blush_t.png"
        show screen hermione_main
        her "W-What did I say..."
        m ">You wiggle the finger inside."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03b.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_a067_blush.png"
        show screen hermione_main
        her "You never listen, old pervert."
        m "What can I say, I just know what's best for you, my little witch."
        ">You pick up the pace."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03d.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush.png"
        show screen hermione_main
        her "Yesss {image=textheart.png}."
        m "I thought you didn't want the finger?"
        g9 "In that case, one more finger."
        ">She shivers when you insert a second finger."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c068_blush.png"
        show screen hermione_main
        her "Ahh noo... no more please."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c057_blush.png"
        show screen hermione_main
        her "My butthole is stretched so wide!"
        g9 "Your butthole is doing great."
        ">You finger her butthole fiercely."
        hide screen groping_05
        show screen groping_05b
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c058_blush_t.png"
        show screen hermione_main
        her "Nooo... aahh {image=textheart.png}."
        m "Your pussy is getting neglected. We need to fix that!"
        ">You start fingering her pussy with your other hand. She is panting heavily."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t3.png"
        show screen hermione_main
        her "Ah... ah... like that yesss {image=textheart.png}."
        ">You suddenly pull out all the beads."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c068_blush_t.png"
        show screen hermione_main
        her "Ahhhhhh!!"
        ">And insert four fingers in her ass."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_04.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t1.png"
        show screen hermione_main
        her "I'm cumming old bastard, I cumming!"
        m "If you must..."
        ">You continue to work her ass while you finger her pussy."
        her "No don't I..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c098_blush_t.png"
        show screen hermione_main
        her "Cummm {image=textheart.png}{image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c188_blush_t.png"
        show screen hermione_main
        her "Agaaain aaah {image=textheart.png}."
        g11 "Sorry my little anal whore but I'm starting to get tired."
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_a162b_blush_t2.png"
        show screen hermione_main
        her "Don't you dare stop now!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c068_blush_t.png"
        show screen hermione_main
        her "Just a little more pleassse {image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c068_blush_t.png"
        show screen hermione_main
        her "Because I will..."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_04.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t1.png"
        show screen hermione_main
        her "Come again!!"
        show screen blkfade
        with d7
        ">There's a small puddle on your desk from her juices. You slowly remove your fingers."
        hide screen groping_05b
        show screen no_groping_05_desk
        hide screen blkfade
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055b_blush_m.png"
        show screen hermione_main
        her "*Pant* *pant*"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n063_blush_m.png"
        show screen hermione_main
        her "I feel completely ravaged but happy."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n064_blush_m.png"
        show screen hermione_main
        her "Thank you professor, for letting me discover such great sensations."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n069_blush_m.png"
        show screen hermione_main
        her "But I'm exhausted so good night."
        show screen blkfade
        with d3
        ">She puts her shirt back on and rushes to the door."
        hide screen no_groping_05_desk
        hide screen hermione_main
        $ badges = True
        $ wear_shirts = True
        ##call her_pose()
        $ hermione_chibi_xpos = 610
        ##show screen hermione_02_f
        show screen genie
        hide screen blkfade
        m "Come back here, girl."
        g11 "I need your mouth, I can't hold it anymore."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n054_blush.png"
        show screen hermione_main
        her "Professor!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        her "........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n020_blush.png"
        show screen hermione_main
        her "Can I have points for this?"
        g11 "Now!"
        show screen blkfade
        with d5
        ">She comes back and does not seem particularly upset."
        hide screen hermione_main
        ##hide screen hermione_02_f
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
        $ hermione_chibi_xpos = 300
        show screen hermione_02
        hide screen blkfade

        $ h_body = "01_hp/27_ue/hermione/bd_her_n033_blush.png"
        show screen hermione_main
        her "Sir, I still think I deserve some..."
        m "Good night, my dear child."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "........."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n039_blush.png"
        show screen hermione_main
        her "Good night, professor."
        "You dismiss Hermione."
        hide screen hermione_main
        $ b_her_tears = False
        hide screen hermione_02
        show screen blkfade
        with d3
        hide screen blkfade
        show screen genie
        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[4] "{size=-4}(Sucking his cock without getting any points!){/size}"
        her_[6] "{size=-4}(If he hadn't made me come so hard...){/size}"
        her_[16] "{size=-4}(*sigh* Although I guess it's not that high a price...){/size}"

        $ v_tutoring = 12
        jump l_tutoring_end

    elif v_tutoring == 12:
        $ h_body = "01_hp/27_ue/hermione/bd_her_n020_blush.png"
        show screen hermione_main
        her "Oh! I can't believe I forgot! Stay where you are, I'll be right back!"
        hide screen hermione_main
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
        $ custom_outfit = 20
        hide screen blkfade
        $ walk_xpos = 600
        $ walk_xpos2 = 400
        $ hermione_speed = 01.0
        show screen hermione_walk_01
        pause 1
        show screen hermione_02
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "{size=-4}*panting*{/size} Oh good, you're still here."
        m "Is it safe to assume you have honored my request this time?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n054_blush.png"
        show screen hermione_main
        her "I thought it was obvious."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b1_blush.png"
        show screen hermione_main
        her "I even had to hide in an alcove to avoid getting noticed on my way here!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059b_blush.png"
        show screen hermione_main
        her "It was so embarrassing!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "{size=-2}(And exciting!){/size}"
        m "Are you sure you're not wearing anything underneath?"
        hide screen hermione_main
        with d3
        ">Hermione opens up her cloak a little."
        ##$ v_her_robe = "robe1_gap"
        $ robe = 2
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        pause
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_blush.png"
        show screen hermione_main
        her "Does this answer your question?"
        m "Not really. It's hard to tell from this distance. I mean, it's so dark..."
        hide screen hermione_main
        with d3
        ">Hermione rolls her eyes and pulls the gap wider"
        ##$ v_her_robe = "robe1_gap_wide"
        $ robe = 3
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        pause
        her "Is that better?"
        g9 "Oh yes, definitely. Well done, my girl."
        hide screen hermione_main
        with d3
        ">Hermione makes to pull her cloak back together, then pauses and puts her hands back down."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n067_blush.png"
        show screen hermione_main
        pause
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144_blush.png"
        show screen hermione_main
        her "Alright then, can we start the lesson now?"
        m "Maybe, I don't know... do you like butterbeer?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n041_blush.png"
        show screen hermione_main
        her "You know I do. What's that got to do with..."
        g9 "......."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n167_blush.png"
        show screen hermione_main
        her "Do you mean...{w=0.3} no, no way professor!"
        m "Oh, rest assured, we won't start with the bottom end."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n099_blush_e.png"
        show screen hermione_main
        her "Still, professor, this is so dirty..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n097_blush.png"
        show screen hermione_main
        her "{size=-2}(And exciting){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n039_blush.png"
        show screen hermione_main
        her "Moreover, my butthole isn't stretched enough."
        g4 "Are you kidding me, with all your training!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "And what a training!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "{size=-2}(Good thing I practiced by myself, otherwise...){/size}"
        g4 "Now stop making up excuses!"
        m "I can see you rubbing your thighs from excitement!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n056_blush.png"
        show screen hermione_main
        her "I thought it was so dark in here..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "Humm, okay, but you better start out easy on me."
        g9 "I'm always gentle with you my dear child."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_norm.png"
        show screen hermione_main
        her "Yeah, obviously..."
        m "{size=-2}(It's not as if you don't like it rough){/size}"
        m "Alright, my desk, you, naked, now!"

        hide screen hermione_main
        with d3
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d5
        ">Hermione slowly slides down her robe."
        hide screen hermione_02
        $ hermione_chibi_xpos = 300
        show screen ctc
        with d1
        hide screen blkfade
        with d5
        ##$ v_her_robe = "robe1_off"
        $ robe = 4
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        pause
        hide screen ctc
        her "You're crazy for my body, aren't you?"
        m "Why do you ask..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_norm.png"
        show screen hermione_main
        her "Because a girl likes to be complimented, professor!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_norm.png"
        show screen hermione_main
        her "Especially when she's about to do these kinds of things!"
        m "I meant, of course you have a amazing body! That's not up to question."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n015_blush.png"
        show screen hermione_main
        her "Best in the school?"
        m "......{w=0.3} Yeah, yeah, best in the school."
        $ h_body = "01_hp/27_ue/hermione/bd_her_a124_blush.png"
        show screen hermione_main
        her "I can tell you're lying!"
        m "Miss Hermione, I've lived for a very long time and believe me, I have seen few women with a body like yours."
        m "And definitely none in this school."
        m "{size=-2}(Severus still hasn't sent those Slytherin whores up){/size}"
        m "{size=-2}(I wonder if I can fire him for that...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        her "Thank you, professor."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n068_blush.png"
        show screen hermione_main
        her "Feel free to do use my body as you please."
        m "{size=-2}(*sigh* women...){/size}"
        m "Bend over the desk my dear little witch."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "{size=-2}(It starts with my dear little witch and ends up with my dear anal whore){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n023_blush.png"
        show screen hermione_main
        her "{size=-2}(*sigh* men...){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n055_blush.png"
        show screen hermione_main
        her "As you wish my dear {b}old{/b} headmaster."
        m "{size=-2}(If you knew how old I actually am...){/size}"
        show screen blkfade
        with d5
        ">Hermione languorously bends over the desk."
        hide screen hermione_walk_01
        hide screen her_naked
        hide screen hermione_main
        hide screen genie
        show screen no_groping_laying_02
        show screen ctc
        with d1
        hide screen blkfade
        with d5
        ##$ v_her_robe = 0
        $ robe = 0 
        $ h_body = "01_hp/27_ue/hermione/bd_her_n019_blush.png"
        show screen hermione_main
        pause
        hide screen ctc
        her "I'm ready my prince."
        ">You take an empty butterbeer bottle, spit on the neck and push it inside her butthole."
        hide screen no_groping_laying_02
        show screen scr_her_fingering_naked("slow")
        $ h_body = "01_hp/27_ue/hermione/bd_her_c017_blush.png"
        show screen hermione_main
        her "Hmmm, yes like that."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n067_blush.png"
        show screen hermione_main
        her "My pussy feels lonely without your care."
        ">You start to finger her pussy too."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        m "Poor little thing."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c057_blush.png"
        show screen hermione_main
        her "What's better in life than this professor?"
        m "Oh, I don't know."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n059b_blush.png"
        show screen hermione_main
        her "Thank you for letting me discover such pleasures."
        g9 "{b}My{/b} pleasure."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n056_blush.png"
        show screen hermione_main
        her "It's even better when it's mutual, isn't it?"
        m "Hmm, yes you're right. I'm glad you feel that way."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n044_blush.png"
        show screen hermione_main
        her "Now a little deeper please."
        ">You push the whole bottle neck up inside her asshole."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c057_blush.png"
        show screen hermione_main
        her "Ohhh, yesss! {image=textheart.png}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "More, faster!"
        show screen scr_her_fingering_naked()
        ">You rotate the bottle while going back and forth deeper and deeper."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush_t.png"
        show screen hermione_main
        her "Yessss, don't forget my pussy {image=textheart.png}."
        g9 "Oh, your pussy better be ready for what's coming!"
        ">You insert all four fingers in her sopping wet pussy."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c059_blush_t.png"
        show screen hermione_main
        her "Sweet Circe, aah, aah, that's too much! {image=textheart.png}"
        m "Nothing is too much for my little whore."
        ">You increase the pace of both hands."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c068_blush_t.png"
        show screen hermione_main
        her "No, no, yes, yessss! {image=textheart.png}"
        ">Most of the bottle is inside her now, leaving just enough to get a good grip."
        m "Push the bottle, push it!"
        ">Whenever she pushes it back you do the same in the other direction."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_04.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t1.png"
        show screen hermione_main
        her "This is, this is, aaaah!!! {image=textheart.png}{image=textheart.png}"
        ">Her whole body convulses as she comes hard."
        show screen blkfade
        with d5
        $ b_her_tears = False
        hide screen hermione_main
        hide screen scr_her_fingering_naked
        show screen no_groping_laying_02
        pause.3
        hide screen blkfade
        $ h_body = "01_hp/27_ue/hermione/bd_her_n049_blush_m.png"
        show screen hermione_main
        her "*Panting* *panting*"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush_m.png"
        show screen hermione_main
        her "P-professor...{w=0.3} I'm so happy right now."
        g9 "Glad to hear it."
        show screen blkfade
        ">After a while, she makes herself somewhat presentable."
        ##call her_pose()
        $ robe = 1
        hide screen no_groping_laying_02
        show screen genie
        show screen hermione_02
        hide screen blkfade
        with d3
        m "Sweet dreams my little princess."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n052_blush.png"
        show screen hermione_main
        her "You too, professor."
        g9 "They are always sweet with you around."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n017_blush.png"
        show screen hermione_main
        her "Thank you."
        m "And next time bring your books, I'll help you with your revisions."
        "You dismiss Hermione."
        hide screen hermione_main
        hide screen hermione_02
        show screen blkfade
        with d3
        $ b_her_tears = False
        hide screen blkfade
        show screen genie

        $ walk_xpos = 400
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[35] "{size=-4}(Yes, sweet dreams...){/size}"
        her_[34] "{size=-4}(Sweet and wet!){/size}"

        $ v_tutoring = 13
        jump l_tutoring_end

    elif v_tutoring == 13:
        $ h_body = "01_hp/27_ue/hermione/bd_her_n041_norm.png"
        show screen hermione_main
        her "I'll go get my books right away, sir!"
        hide screen hermione_main
        show screen blkfade
        with d3
        play sound sd_door
        pause 2
        play sound sd_door
        pause.3
        $ book_hold = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_norm.png"
        show screen hermione_main
        show screen hermione_02
        show screen ctc
        hide screen blkfade
        with d3
        pause
        hide screen ctc
        m "Your vest is back?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n051b_norm.png"
        show screen hermione_main
        her "Revisions are a serious matter!"
        m "{size=-2}(My cock in your ass is a serious matter...){/size}"
        m "In this regard, I kinda lied, it's more of a mock exam than revisions."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "What a surprise!"
        m "I need to make sure you've been working out your butthole."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n023_blush.png"
        show screen hermione_main
        her "........"
        g9 "With my cock."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n031_blush.png"
        show screen hermione_main
        her "I see..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_blush.png"
        show screen hermione_main
        her "I'm not against that but I bet I'll gain no points for this?"
        m "I'm helping you with your revisions, why should you be getting points for that?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n029b_blush.png"
        show screen hermione_main
        her "And what revisions..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n011_blush2.png"
        show screen hermione_main
        her "Alright, since you have helped me a lot, I'm in."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014b_blush.png"
        show screen hermione_main
        her "{size=-2}(I give myself away for free now, what a bad whore I make){/size}"
        m "Come here and strip."
        show screen blkfade
        hide screen hermione_main
        with d3
        $ walk_xpos = 400
        $ walk_xpos2 = 300
        $ hermione_speed = 01.0
        hide screen blkfade
        hide screen hermione_04
        show screen hermione_walk_01
        pause 1
        show screen blkfade
        with d3
        hide screen hermione_walk_01
        pause 1
        $ panties = False
        $ wear_shirts = False
        $ badges = False
        $ custom_outfit = 20
        $ h_body = "01_hp/27_ue/hermione/bd_her_n018_blush.png"
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
        hide screen hermione_main
        hide screen genie
        show screen no_groping_laying_02
        hide screen blkfade
        with d5
        g9 "You can open a book if you want."
        ##$ v_her_book = 0
        ##$ v_her_shirt = 0
        $ book_hold = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_a029_blush.png"
        show screen hermione_main
        her "I should read about this spell called \"the Clap\"!"
        ">You take advantage of her moment of distraction to force you cock into her butthole."
        show screen blkfade
        pause 1
        hide screen no_groping_laying_02
        show screen chair_02
        show screen scr_her_sex("slow")
        hide screen blkfade
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush.png"
        show screen hermione_main
        her "Ah, you brute {image=textheart.png}."
        m "Your butthole is the perfect fit, not too tight and not too stretched!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n095_blush.png"
        show screen hermione_main
        her "You've trained me well..."
        ">You caress her clit while fucking her."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c047_blush.png"
        show screen hermione_main
        her "Mmmh, yes {image=textheart.png}."
        g9 "You love it don't you?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n014_blush.png"
        show screen hermione_main
        her "Your cock in my ass, oh yes."
        m "Even without points?"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n008_blush.png"
        show screen hermione_main
        her "Don't make me regret agreeing to this."
        m "Say you love it even without points."
        show screen scr_her_sex()
        ">You increase the pace."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c177b_blush.png"
        show screen hermione_main
        her "Ahh yesss {image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n078b_blush.png"
        show screen hermione_main
        her "I'm such a whore, I love sex even for free."
        g9 "You know it!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n056_blush.png"
        show screen hermione_main
        her "Don't make it a habit."
        m "......"
        ">You pull out your cock and roughly shove it back inside."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_01.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_c067_blush.png"
        show screen hermione_main
        with hpunch
        her "Aaaaah {image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c097_blush_t1.png"
        show screen hermione_main
        her "I love being sodomized savagely by my headmaster."
        ">And again."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t1.png"
        show screen hermione_main
        with hpunch
        her "Yessss {image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c098_blush_t.png"
        show screen hermione_main
        her "I love his big cock in my ass."
        ">You slap her buttcheek."
        play sound sd_slap
        with hpunch
        $ b_her_tears = False
        $ h_body = "01_hp/27_ue/hermione/bd_her_c058_blush_t.png"
        show screen hermione_main
        her "And being punished for my sluttiness."
        play sound sd_slap
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c099_blush_t.png"
        show screen hermione_main
        her "Aah, like this, punish me more master {image=textheart.png}."
        play sound sd_slap
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c179_blush_t.png"
        show screen hermione_main
        her "Yess!"
        play sound sd_slap
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t3.png"
        show screen hermione_main
        her "Mooore!"
        play sound sd_slap
        with hpunch
        $ h_body = "01_hp/27_ue/hermione/bd_her_c078_blush_t.png"
        show screen hermione_main
        her "I'm about to..."
        play sound sd_slap
        with hpunch
        pause.1
        play sound sd_slap
        with hpunch
        pause.1
        $ h_body = "01_hp/27_ue/hermione/bd_her_c189_blush_t.png"
        show screen hermione_main
        her "Cuuuum {image=textheart.png}{image=textheart.png}."
        show screen scr_her_sex("fast")
        ">You fuck her butthole fiercely."
        $ h_body = "01_hp/27_ue/hermione/bd_her_c187_blush_t3.png"
        show screen hermione_main
        her "Yes, yes, again, aaaah {image=textheart.png}."
        g11 "Yes, my little whore, yes!"
        hide screen scr_her_sex
        show screen scr_her_sex_cum_outside()
        $ h_body = "01_hp/27_ue/hermione/bd_her_c058_blush_t.png"
        show screen hermione_main
        her "*Panting* *panting*"
        show screen scr_her_sex_cum_outside(1)
        g11 "*Panting* *panting*"
        show screen blkfade
        hide screen chair_02
        hide screen hermione_main
        hide screen scr_her_sex_cum_outside
        pause 1
        show screen no_groping_laying_02
        hide screen blkfade
        m "*sigh* that was, that was..."
        $ u_tears_pic = "01_hp/27_ue/hermione/e_her_tears_03.png"
        $ b_her_tears = True
        $ h_body = "01_hp/27_ue/hermione/bd_her_n156_blush.png"
        show screen hermione_main
        her "Marvellous {image=textheart.png}."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n095_blush.png"
        show screen hermione_main
        her "I'm so glad you agreed to tutor me, professor..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n144b_blush.png"
        show screen hermione_main
        her "Your lessons have changed my life so much!"
        g9 "{size=-2}(Victory!){/size}"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n032_blush.png"
        show screen hermione_main
        her "But if you think you can fuck me all the time without giving me points..."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n036_blush.png"
        show screen hermione_main
        her "You're dreaming!"
        m "{size=-2}(Ohhh...){/size}"
        m "Even occasionally?"
        her "......."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n044_blush.png"
        show screen hermione_main
        her "Only if you are well-behaved..."
        g9 "I'm the most well-behaved professor in the whole school!"
        $ h_body = "01_hp/27_ue/hermione/bd_her_n037_blush.png"
        show screen hermione_main
        her "Sure."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n022_blush.png"
        show screen hermione_main
        her "{size=-2}(At least, you're not the worst...){/size}"
        m "Good night my beloved princess."
        $ h_body = "01_hp/27_ue/hermione/bd_her_n012_blush.png"
        show screen hermione_main
        her "Good night my beloved prince."
        ">You dismiss Hermione."
        ">She puts her clothes back on without haste."
        hide screen hermione_main
        hide screen no_groping_laying_02
        show screen blkfade
        with d3
        pause 1
        ##call her_pose()
        $ b_her_tears = False
        show screen genie
        hide screen blkfade
        with d3

        $ walk_xpos = 300
        $ walk_xpos2 = 610
        $ hermione_speed = 02.0
        show screen hermione_walk_01_f
        pause 2
        $ hermione_chibi_xpos = 610
        hide screen hermione_walk_01_f
        ##show screen hermione_02_f
        with d3

        her_[16] "{size=-4}(I called my headmaster \"my beloved prince\"){/size}"
        her_[18] "{size=-4}(He's hardly Prince Charming but...){/size}"
        her_[38] "{size=-4}(I doubt Prince Charming could fuck me half as well as he can!){/size}"

        $ v_tutoring = 14
        jump l_tutoring_end

label l_tutoring_end:
    play sound sd_door
    ##hide screen hermione_02_f
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
    $ custom_outfit = 0
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
    add "01_hp/05_props/genie_and_hermione_01.png" at Position(xpos=-200, ypos=10)

screen groping_05:
    tag favor
    add "groping_05" at Position(xpos=-200, ypos=10)
    add "groping_05_blinking" at Position(xpos=-200, ypos=10)

screen groping_05b:
    tag favor
    add "groping_05b" at Position(xpos=-200, ypos=10)
    add "groping_05_blinking" at Position(xpos=-200, ypos=10)

screen no_groping_05:
    tag favor
    add "01_hp/animation/grope_d_05.png" at Position(xpos=-200, ypos=10)
    add "groping_05_blinking" at Position(xpos=-200, ypos=10)

screen no_groping_05_desk:
    tag favor
    add "01_hp/animation/grope_d_06.png" at Position(xpos=-200, ypos=10)

screen no_groping_06: #Facing Genie.
    tag favor
    add "01_hp/animation/grope_e_05.png" at Position(xpos=-200, ypos=10)
    add "groping_06_blinking" at Position(xpos=-200, ypos=10)

screen groping_06:
    tag favor
    add "groping_06" at Position(xpos=-200, ypos=10)
    add "groping_06_blinking" at Position(xpos=-200, ypos=10)

screen groping_06b:
    tag favor
    add "groping_06b" at Position(xpos=-200, ypos=10)
    add "groping_06_blinking" at Position(xpos=-200, ypos=10)

screen no_groping_laying_01:
    tag favor
    add "01_hp/animation/grope_laying_01.png" at Position(xpos=-200, ypos=10)

screen no_groping_laying_02:
    tag favor
    add "01_hp/animation/grope_laying_b_01.png" at Position(xpos=-200, ypos=10)

screen scr_her_fingering_naked(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_fingering_slow_naked" at Position(xpos=-200, ypos=10)
    else:
        add "ani_her_fingering_naked" at Position(xpos=-200, ypos=10)
    add "ani_her_fingering_blinking" at Position(xpos=-200, ypos=10)

screen scr_her_sex(speed="normal"):
    tag favor
    if speed == "slow":
        add "ani_her_sex_slow_naked" at Position(xpos=-200, ypos=10)
    elif speed == "normal":
        add "ani_her_sex_naked" at Position(xpos=-200, ypos=10)
    elif speed == "fast":
        add "ani_her_sex_fast_naked" at Position(xpos=-200, ypos=10)

screen scr_her_sex_cum_outside(blink=0):
    tag favor
    add "ani_her_sex_cum_outside_naked" at Position(xpos=-200, ypos=10)

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