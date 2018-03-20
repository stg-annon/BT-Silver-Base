#LETTER FROM THE MINISTRY OF MAGIC
#Dear Albus Dubmbledore, as we are sure you are aware,
#an unforgivable curse has been detected within the grounds of Hogwarts.
#While the punishment for such a curse is usually lifetime incarceration in the
#prison, Azkaban, we are allowing you to address this matter at your own discretion.
#This is due to the possible nature of the spell being cast by a minor who has not
#fully grasped the serious nature of the curse. If this is the case we expect no further communication from 
#you regarding this unfortunate event. If, however, you believe the curse has been cast by someone other than a student,
#or if any other complications arise we expect direct communication. Lastly, the detection of any further curses will 
#result in the immediate dispatchment of an auror to Hogwarts.

#Cornelius Fudge, 
#Department Head: Improper Use of Magic Office

#m "That doesn't sound good..."
#m "Perhaps I should tell Snape about this."
#m "Or maybe miss granger?"


#TELL HERMIONE ABOUT THE LETTER
label letter_intro_hermione:
    m "I received a letter not too long ago."
    her "I assume you receive hundreds of letters each day. You're the headmaster of hogwarts after all..."
    m "this one was different."
    m "Apparently they've detected something called an \'unforgivable\' curse at the school."
    her "AN unforgivable CURSE!!!"
    her "SOMEONE COULD BE DEAD!"
    her "OR TORTURED!!"
    her "OR WORSE!!!"
    m "really?"
    her "Those are the only things that can happen with an unforgivable curse [genie_name]!"
    m "of course... I'm just making sure you were aware of them..."
    her "It's the first lesson we ever received in defense against the dark arts."
    m "Well, one's been cast somewhere on the school."
    m "and I need your help finding out who did it..."
    her "Why do you need my help?"
    her "Surely you're able to detect who did it?"
    m "Unfortunately not... I must have been... asleep... when the thing happened..."
    m "I missed my chance, so to speak..."
    her "So how do you expect me to find out who did it?"
    m "I'm certain that it's the work of another student..."
    m "(or snape finally snapped...)"
    m "so I'll need you to go undercover to find out who."
    her "really? You're depending on me to find a criminal student within our school?"
    m "If it's not too much troub-"
    her "I'd be honored [genie_name]!"
    her "It's no doubt the work of one of those despicable \'slytherins\'..."
    her "Nothing would give me greater pleasure than to see scum like that sent to \'Azkaban\'..."
    m "And what's Azkaban?"
    her "It's the prison of the damned... An impenetrable rocky outcrop surrounded by the harsh North Sea..."
    her "the guards are the deathly eaters of all happy thoughts and emotions known as dementors..."
    her "They endlessly patrol the prison, devouring all hope from the prisoners, driving them mad within a few days..."
    her "Tormenting them relentlessly for the rest of their miserable lives..."
    her "And the perfect place to house all those dirty \'slytherins\'!"
    m "ah..."
    menu:
        "-just tell her to find the student-":
            m "Whatever..."
            m "just find them so we can send them to Akabur..."
            her "Azkaban, sir..."
            m "Just go!"
        "-Tell her you're not going to send them to Azkaban-":
            m "By the gods [hermione_name], what's wrong with you?"
            her "What are you talking about [genie_name]?"
            her "Everyone knows that life in Azkaban is the punishment for casting an unforgivable curse..."
            m "I've been given special permission to punish them as I see fit."
            her "Oh..."
            her "So no Azkaban?"
            m "Not unless they've killed someone..."
            her "Really? So there's still a chance?"
            m "Only if you find a body..."
            her "yay!"
    ">hermione quickly exits your office."
    if astoria_intro_flag_1 == True:
        m "I wonder if she'll find them before Snape..."
    else:
        m "I should probably tell Snape as well..."

    jump day_main_menu

label letter_intro_snape:
    m "I got some letter from the ministry of magic..."
    sna "Really?"
    sna "Why are you telling me?"
    m "Apparently they've detected something called an \'unforgivable\' curse at the school, and if they detect another one they're going to send an \'auror\' or something."
    sna "oh shit... this isn't good..."
    sna "This really isn't good..."
    m "Why, are the curses that bad?"
    sna "Forget about the damn curses, if they send an auror here they might find out what we've been doing."
    m "What?"
    sna "THe favour trading! Fucking our students isn't something teachers are supposed to do genie!"
    sna "If an auror finds out what's going on here we're both going to Azkaban!"
    m "so what are we going to do?"
    sna "We'll just have to make sure that no more curses are cast..."
    m "How do we manage that?"
    sna "We have to find out who's been casting them."
    sna "Normally the real Dubmbledore would be able to detect who had cast them, but seeing as how you're here instead..."
    sna "We'll have to find them the old fashioned way."
    m "So you want me to launch a manhunt?"
    sna "Are you crazy? We can't let anyone know what's happened. All the students will panic thinking someone's been murdered..."
    sna "It's probably just an imperio or crucio that's been cast."
    sna "I'll start the search immediately. In the mean time you just stay here and keep yourself busy."
    m "You don't want my help?"
    sna "Not really... With how potent your magic is you'll probably just attract more attention from the ministry and then they'll definitely send an auror."
    sna "Don't worry Genie, I'll find that student in no time."
    ">Snape quickly exits your office, his cape billowing menacingly behind him as he leaves."
    m "Drama queen..."

    jump day_main_menu

label astoria_captured_intro:
    #play knock sound effect
    "*knock* *knock* *knock*"
    m "Who is it?"
    her "It's hermione granger, sir, although I'm not alone."
    m "Come in."
    ">hermione enters your office."
    m "I thought you said you weren't alone?"
    her "I'm not."
    her "Get in here Astoria!"
    ast "No!"
    her "Do you want to make this worse?"
    ast "..."
    ">Slowly, a small girl enters your office."
    m "..."
    m "Who's this?"
    ast "My name is Astoria Greengrass."
    m "And why are you here?"
    her "You asked me to bring you the person who cast the unforgivable curse sir."
    her "Here she is."
    m "I thought it would be some angsty teen who listens to death metal or something..."
    m "not some little girl..."
    ast "I am not a little girl!"
    m "What are you then, a 6000 year old vampire?"
    ast "Vampires aren't real!"
    m "..."
    m "So how are you not a little girl then?"
    ast "I'm older than I look!"
    m "I've heard that one before..."
    her "It's true sir. She was a cursed child, born with a frailty that affects her growth."
    ast "Told you!"
    m "Whatever... that still doesn't get you out of punishment."
    ast "punishment? for what?"
    her "You know what you did!"
    ast "I never cast Imperio on anyone! I swear sir! Hermione's just being a know-it-all tattle-tail!"
    m "Miss Granger..."
    her "I overheard her boasting about it to a group of slytherins in the library."
    her "By the sounds of it she used Imperio to control another student."
    ast "Did not!"
    m "Well, given the severity of the situation, I'm sure there's something we can use to get a clear answer out of you..."
    her "Shall I go fetch a vial of veritaserum from professor snape sir?"
    ast "v-veritaserum? Isn't that against the rules?"
    her "Not when you've been casting unforgivable curses you evil little witch!"
    ast "OK... I'll tell you what happened sir..."
    ast "But only if Hermione leaves!"
    her "Not a chance!"
    m "Miss granger..."
    her "professor! I think it's only fair, given that I was the one to catch her!"
    m "We'll talk about your reward later..."
    her "*hmph*"
    her "Fine..."
    her "I'll go back to my room then..."
    her "Goodbye sir..."
    her "Goodbye Astoria..."
    ">Hermione quietly leaves your office."
    m "Right, well now that Hermione's gone, why don't you tell me exactly what-"
    #magic sound effect and screen shake
    ast "IMPERIO!"
    m "..."
    m "What was that?"
    ast "I just cast Imperio on you professor! Now you have to do everything I say!"
    m "Did you just cast another unforgivable curse?"
    ast "yes... but it should have... why aren't you..."
    m "Ugh..."
    m "I better get Snape up here."
    ast "professor snape? I command you not to!"
    m "yeah, no. I'm bringing him up here because now we're probably going to have to deal with something called an auror coming to the school."
    ast "An auror?!"
    ast "But they'll send me to Azkaban!"
    m "I'm sure they'll be lenient, you're only a child after all."
    m "Anyway, I better get Snape."
    ">you summon snape to your office."
    sna "gen- oh, you've I see you already have a visitor."
    sna "Little young isn't she, even for you..."
    m "It's not that sort of visit."
    sna "Really? Then what's she doing here."
    m "She's the one who's been casting those curses."
    sna "Truthfully? A slytherin?"
    sna "I expect better than this from my students miss Greengrass..."
    sna "The very first lesson I give you is to not. get. caught!"
    sna "Do you have anything to say for yourself?"
    ast "I-I'm sorry sir... It won't happen again."
    sna "Well as long as you only cast it once..."
    ast "Twice..."
    sna "TWICE!?!"
    sna "But that means..."
    sna "There's probably an auror on the way right now!"
    sna "Who did you cast them on you little idiot?"
    sna "Who did you curse?"
    ast "Well the first time I was just testing it out on Susan Bones..."
    ast "She was being so mean to me so I might have used imperio to embarrass her a little..."
    sna "And the second time?"
    ast "I just tried to use imperio on professor Dumbledore then, so he wouldn't get me in trouble..."
    ast "But it didn't work!"
    sna "Really? It must be because he's a geni-"
    sna "Genius wizard!"
    sna "But this is no good... If they're sending an auror here then they'll want to talk to you... Dumbledore..."
    m "me?"
    sna "I'm afraid so..."
    m "How long until they get here?"
    sna "I'm not sure, but I don't intend to find out!"
    ">Snape quickly turns to leave your office, sprinting out the door."
    m "COWARD!"
    ast "So there really is an auror coming?"
    ast "I've heard that they're all trained by madeye moody..."
    ast "PLEASE SIR!"
    ast "YOU CAN'T LET THEM SEND ME TO Azkaban!"
    ast "I promise I'll be good! I won't cast anymore curses!"
    ast "I'll do Whatever you want!"
    m "Calm down..."
    ast "b-b-but... I don't want to... go to Azkaban..."
    m "I'm not going to let them take you to Azkaban."
    ast "r-r-r-really? even after I tried to control you?"
    m "we'll talk about your punishment later. For now, I think it's better for you to go back to your room."
    ast "A-a-alright... but what about the auror?"
    m "I'll just explain to them that this was all a simple misunderstanding."
    ast "T-thank you sir..."
    m "However I do expect you to come to my office whenever I summon you from now on."
    ast "Why?"
    m "I might have to call you up here to see the auror. Not to mention we still have the matter of your punishment."
    ast "But I thought it was all just a misunderstanding?"
    m "You've committed a very serious offense here young girl. Just because you're not going to Azkaban, doesn't mean you're getting out of punishment."
    ast "Alright sir..."
    m "Good. Now go back to your room until I summon you."
    m "And by the gods stop cursing people!"
    ast "yes sir..."
    ">Astoria turns to leave your office, looking slightly dejected at the prospect of future punishment."
    m "(Gods, I feel like I'm actually starting to run this damn school.)"
    m "(This isn't what I signed on for...)"

    jump day_main_menu

label tonks_intro_event:




































































