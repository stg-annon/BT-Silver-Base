label snape_chitchat:
    if not chitchat_event_01_happened and tutoring_hermione_unlocked and days_without_an_event >=2:
        jump chitchat_event_01
    
    

    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    ### CHIT CHATS WITH SNAPE ###
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            call sna_main("Do You really think you can do this?","24")
            call sna_main("Do You think you can break the girl?","snape_25")
        
        elif one_of_ten == 2:
            call sna_main("Don't you just hate this wretched sunny weather?","snape_01")
            call sna_main("I wish it would rain every day.","snape_06") 
            
        elif one_of_ten == 3:
            call sna_main("I am feeling rather doubtful about our whole plan again...","snape_06")
            
        elif one_of_ten == 4:
            call sna_main("Are you sure that you are not Albus Dumbledore?","snape_05")
            sna "I'm still having a hard time believing this whole thing sometimes..."
  
        elif one_of_ten == 5:
            call sna_main("I killed a pupil once.","snape_01")
            call sna_main("Yes... I strangled the maggot with my bare hands.","snape_02")
            call sna_main("........*low growl*.","snape_03")
            call sna_main("Did that sound believable?","snape_05")
            call sna_main("The moment those animals stop fearing me, I'm done for.","snape_06")
            call sna_main("Cultivating fear in the hearts of your students is the most important task for every teacher.","snape_26")

        elif one_of_ten == 6:
            call sna_main("Those Weasley maggots...","snape_04")
            call sna_main("One of these days I'll just snap, I swear.","snape_07")

        elif one_of_ten == 7:
            call sna_main("Don't you think that owl post is a bit ridiculous?","snape_05")
            sna "I'd much rather use ravens."
            
        elif one_of_ten == 8:
            call sna_main("I'm having the worst day of my life...","snape_06")
            sna "So I'm really Not in the mood for chit-chats..."
            
        elif one_of_ten == 9:
            call sna_main("Being a wizard is a 24 hours a day...","snape_04")
            call sna_main("7 days a week...","snape_03")
            call sna_main("365 days a year job.","snape_04")
            sna "We get no vacation days..."
            
        elif one_of_ten == 10:
            call sna_main("Quidditch...","snape_04")
            call sna_main("What a waste of time and ressources!","snape_10")
            call sna_main("","snape_04")
            
            
        
        
    
    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02.
        if one_of_ten == 1:
            call sna_main("I have yet to notice any changes in miss Granger's behavior...","24")
            call sna_main("Are you sure that you know what you're doing?","snape_05")
            call sna_main("","snape_09")
        
        elif one_of_ten == 2:
            call sna_main("It sure feels good to be able to grant house points or take them away whenever I feel like it.","24")
            sna "My authority among the students is growing every day..."
            call sna_main("And when I say \"authority\" I mean \"fear\".","snape_02")

        elif one_of_ten == 3:
            call sna_main("Did you know that the full moon is known to boost male potency?","24")
            sna "It also makes it easier to focus at a task at hand, making you more proactive."
            call sna_main("But who gives a damn about that, am I right?","snape_28")
            call sna_main("","snape_29")

        elif one_of_ten == 4:
            call sna_main("My precious Slytherins make all of this torment worth while...","snape_06")
            call sna_main("Their skirts are getting shorter every week, I swear.","snape_19")
  
        elif one_of_ten == 5:
            call sna_main("There was a time when I was young and full of hope...","snape_06")
            call sna_main("Ha-ha... I'm pulling your leg, mate","snape_28")
            call sna_main("I was never full of hope...","snape_29")

        elif one_of_ten == 6:
            call sna_main("Duelling is one of my fortes, you know...","snape_09")

        elif one_of_ten == 7:
            call sna_main("A \"Men's rights movement\"...?","snape_05")
            call sna_main("What's next? A house elves' rights movement?","snape_04")
            call sna_main("How could a top student could be that dumb?","snape_06")
            
        elif one_of_ten == 8:
            call sna_main("I don't play favourites with my students.","snape_05")
            call sna_main("I merely tolerate some of them and hate the rest.","snape_04")
  
        elif one_of_ten == 9:
            call sna_main("There are four student houses at Hogwarts...","24")
            sna "Slytherin, Ravenclaw, Gryffindor and..."
            call sna_main("...and Huff-something...","snape_05")
            call sna_main("No one really cares.","snape_29")
            call sna_main("","snape_09")
 
        elif one_of_ten == 10:
            call sna_main("Brooms are for kids and witches.","24")
            call sna_main("You'll never see a self-respecting wizard prancing around on a broomstick.","snape_05")
            call sna_main("","snape_09")
        
        
        
        
        
        
        
        
        
    
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            call sna_main("Any progress on breaking our little ms. know-it-all?","24")
            call sna_main("","snape_09")
        
        elif one_of_ten == 2:
            call sna_main("The other day this one girl sold me her panties for five house points.","24")
            call sna_main("And man, was she excited about that...","snape_14")
            call sna_main("I think she would've given them away for free just to please me.","snape_19")
            call sna_main("","snape_09")

        elif one_of_ten == 3:
            call sna_main("I'm having a rather pleasant day so far...","23")
            call sna_main("Bet you didn't expect to hear me saying that?","snape_02")

        elif one_of_ten == 4:
            call sna_main("Quidditch seems to steadily gain more and more popularity over the years...","24")
            call sna_main("How disappointing...","snape_04")

        elif one_of_ten == 5:
            call sna_main("My life was incredibly dull before your arrival...","24")
            call sna_main("Nowadays it's...","snape_05")
            call sna_main("...less dull.","snape_02")

        elif one_of_ten == 6:
            call sna_main("Regrets? I don't know the meaning of the word!","snape_05")
            call sna_main("I live a very fulfilling life.","snape_06")
            call sna_main("Ha-ha-ha! I'm sorry, I just can't say such nonsense with a straight face.","snape_28")
            call sna_main("","snape_26")

        elif one_of_ten == 7:
            call sna_main("There is no room for mistakes during class.","24")
            call sna_main("One slip-up and the bloody bastards will tear you to shreds.","snape_04")

        elif one_of_ten == 8:
            call sna_main("You are the only person I have to answer to...","snape_04")
            call sna_main("So I can almost literally do whatever the bloody hell I want these days...","snape_05")
            call sna_main("...............","snape_09")
            call sna_main("So that's what freedom feels like, huh?","snape_06")

        elif one_of_ten == 9:
            call sna_main("Autumn... the most depressing time of the year...","snape_06")
            call sna_main("I Love it!","snape_02")
            call sna_main("","23")

        elif one_of_ten == 10:
            call sna_main("I have a magical portrait of a stripper hanging in my room.","24")
            call sna_main("One of my most precious possessions.","snape_22")
            call sna_main("","snape_09")
        
        
        
        
        
        
        
        
        
        
        
       
    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            call sna_main("Lately miss Granger has gotten aggressive almost to the point of open hostility...","24")
            call sna_main("I hope you know what you're doing...","snape_05")
            call sna_main("","snape_09")

        elif one_of_ten == 2:
            call sna_main("I shouldn't feel bad about having sex with my students, right?","snape_26")
            call sna_main("I mean, you should see the way some of those girls wear their uniforms...","snape_05")
            call sna_main("They're practically asking for it.","snape_13")
            call sna_main("","snape_12")

        elif one_of_ten == 3:
            call sna_main("It's been raining a lot lately...","23")
            call sna_main("I wonder if I enjoy rainy weather so much simply because it makes most people miserable...","snape_02")
            call sna_main("","23")

        elif one_of_ten == 4:
            call sna_main("According to a recent study 9 out of 10 girls secretly fantasize about being abused by their teacher.","24")
            call sna_main("I bet that 10th girl was Hermione Granger.","snape_03")
            call sna_main("","snape_01")

        elif one_of_ten == 5:
            call sna_main("These days I have to actually make an effort to maintain my usual bad mood.","24")
            call sna_main("","23")

        elif one_of_ten == 6:
            call sna_main("Do You have a few condoms to spare?","24")
            call sna_main("I have a whole pack but...","snape_25")
            call sna_main("...they've expired years ago...","snape_06")
            call sna_main("The changes you brought into my life, mate.","snape_02")
            call sna_main("","23")

        elif one_of_ten == 7:
            call sna_main("You think we could turn Hogwarts into a \"girls only\" school?","24")
            call sna_main("Hogwarts Girls Academy!","23")
            call sna_main("Now that would be bloody perfect... except for Lockhart maybe.","snape_13")

        elif one_of_ten == 8:
            call sna_main("Why did the teacher cross the road?","24")
            call sna_main("To get away from his students!","snape_25")
            call sna_main("Ha-ha-ha! Gets me every time!","snape_28")
            call sna_main("","snape_25")

        elif one_of_ten == 9:
            call sna_main("Want to hear a funny story?","24")
            call sna_main("Well, I don't know any...","snape_06")

        elif one_of_ten == 10:
            call sna_main("Do you know what a \"royal goblet\" is?","snape_05")
            call sna_main("You do, don't you?","snape_13")
            call sna_main("","23")
        
        
        
        
        
        
        
        
        
    
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            call sna_main("15 points for a blowjob is a fair price, right?","24")
            call sna_main("","23")

        elif one_of_ten == 2:
            call sna_main("Have you ever been in love, mate?","24")
            call sna_main("Have you ever been in love with a schoolgirl?","snape_02")
            call sna_main("What about half a dozen of them at once?","snape_22")
            call sna_main("","snape_20")

        elif one_of_ten == 3:
            call sna_main("Something rather brilliant happened last night between me and this Slytherin mynx.","snape_20")
            call sna_main("Long story short, all of my muscles ache and I still feel rather dehydrated...","snape_22")
            call sna_main("","snape_13")

        elif one_of_ten == 4:
            call sna_main("It's getting colder lately...","24")
            call sna_main("Winter is coming...","23")
         
        elif one_of_ten == 5:
            call sna_main("Have you ever seen muggle women dressed as witches?","24")
            call sna_main("So adorable.","snape_19")

        elif one_of_ten == 6:
            call sna_main("Do you know what an \"Internet\" is?","24")
            call sna_main("Apparently it allows you to go \"on the line\" and see magical photographs of naked muggle women.","snape_02") # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
            call sna_main("Kind of makes me wish we had one here in Hogwarts.","snape_26")
            call sna_main("","snape_09")

        elif one_of_ten == 7:
            call sna_main("I have two major passions in life...","24")
            sna "Dark arts..."
            call sna_main("......","snape_12")
            call sna_main("...and sluts.","snape_13")

        elif one_of_ten == 8:
            call sna_main("You think I ought to cut down on my drinking?","24")
            call sna_main("But my life is so stressful...","snape_06")
            call sna_main("Hm...","snape_09")
            call sna_main("I'll try and cut down on the liquor...","snape_06")
            call sna_main("In favour of sweaty monkey-sex with my students!","snape_21")
            call sna_main("","snape_19")

        elif one_of_ten == 9:
            call sna_main("Miss Granger has been suspiciously quiet lately...","24")
            call sna_main("I bet she is scheming something...","snape_03")
            call sna_main("","snape_01")

        elif one_of_ten == 10:
            call sna_main("It's quite easy to write a book and kill off half of the main characters for the sake of dramatic impact...","24")
            sna "To put your characters against impossible odds and let them make it out alive in a believable manner..."
            call sna_main("Now {size=+7}that{/size} requires skill.","snape_02")
            call sna_main("","23")
        
        
        
        
        
        
        
        
        

    if whoring >= 15 and whoring <= 17: # WHORING LEVEL 06.
        if one_of_ten == 1:
            call sna_main("What if the girl is not our pet, but we are her's?","snape_11")
            call sna_main("","snape_26")

        elif one_of_ten == 2:
            call sna_main("Have you heard of the \"Slug club\"?","24")
            sna "What if I start a club of my own?"
            call sna_main("I would call it the \"Snape Club\"!","23")
            sna "I would invite girls over, offer them some tea and muffins..."
            call sna_main("Feel them up a little...","snape_13")
            call sna_main("Bloody brilliant!","snape_22")
            call sna_main("","snape_02")

        elif one_of_ten == 3:
            call sna_main("Tell me Genie... Have you ever had your asshole licked clean by a young witch?","snape_02")
            call sna_main("A life changing experience, neither less nor more...","snape_21")
            call sna_main("","snape_02")

        elif one_of_ten == 4:
            call sna_main("So, how is the training going?","24")
            sna "All according to plan I hope?"
            call sna_main("","snape_05")

        elif one_of_ten == 5:
            call sna_main("I can see Thestrals, you know...","snape_06")
            call sna_main("","snape_09")

        elif one_of_ten == 6:
            call sna_main("You know what I like about Quidditch?","24")
            call sna_main("Nothing! Not a single bloody thing!","snape_15")
            call sna_main("","snape_16")

        elif one_of_ten == 7:
            call sna_main("Hogwarts benefited greatly from your arrival.","24")
            call sna_main("And when I say \"Hogwarts\" I mean \"me\".","snape_02")
            call sna_main("","23")

        elif one_of_ten == 8:
            call sna_main("Real wizards wear black.","24")
            call sna_main("Am I right?","snape_02")
            call sna_main("","23")

        elif one_of_ten == 9:
            call sna_main("Some of those Slytherin girls simply adore me these days...","24")
            call sna_main("Personally I'd much rather be feared...","snape_05")
            call sna_main("But I am willing to settle for mindless adoration...","23")

        elif one_of_ten == 10:
            call sna_main("You are being way too generous with those Gryffindor points, mate.","24")
            call sna_main("Lately I can barely keep up with you...","snape_25")
            call sna_main("","snape_29")
        
        
        
        
   
        
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            call sna_main("Miss Granger really is changing. I can see it clearly now...","24")
            sna "Her grades went down and even her attendance is far from perfect now..."
            call sna_main("But despite that she continues to excel at being a pain in my arse!","snape_10")
            call sna_main("","snape_01")

        elif one_of_ten == 2:
            call sna_main("My least favourite colour?","snape_05")
            call sna_main("Let me give you two: red and gold.","snape_07")
            call sna_main("","snape_04")

        elif one_of_ten == 3:
            call sna_main("I hear the vampire-theme is quite popular among the girls lately.","24")
            call sna_main("I would make a great vampire, don't you think?","snape_05")
            sna "Maybe I should buy a couple of those fake fangs..."
            call sna_main("Just to drive the horny, little sluts completely crazy.","snape_21")
            call sna_main("","snape_02")

        elif one_of_ten == 4:
            call sna_main("I ...hate my life.","24")
            call sna_main("No, wait, let me try this again...","snape_16")
            call sna_main("I ...hate my life.","snape_17")
            call sna_main("Dammit! I'm trying to say \"love\" but it just won't come out...","snape_25")
            call sna_main("I don't think I've ever used the words \"love\" and \"life\" in one sentence before.","snape_29")
            call sna_main("Let me try this again...","snape_06")
            call sna_main("I ha...{w} lo... {w}love my life!","snape_10")
            call sna_main("There you go, I love my life...","23")

        elif one_of_ten == 5:
            call sna_main("Sunlight, chocolate, Quidditch, cats and orange juice...","snape_01")
            sna "That's a list of things I don't care for..."
            call sna_main("Here is a short list of things I do care for a great deal...","snape_02")
            call sna_main("The dark arts, wine and pussy.","23")

        elif one_of_ten == 6:
            call sna_main("have You ever seen two wizards in a fistfight?","snape_02")
            call sna_main("Bloody hilarious!","snape_28")
            call sna_main("","23")

        elif one_of_ten == 7:
            call sna_main("You know that feeling when you just came in a girl's mouth and she swallows it all and says: \"Thank you, professor\"?","snape_14")
            call sna_main("Isn't that the best?","snape_13")
            call sna_main("","23")

        elif one_of_ten == 8:
            call sna_main("do You think the Hogwarts ghosts sometimes spy on girls taking when they a shower and such?","24")
            call sna_main("If I were a ghost I know I would.","snape_13")
            call sna_main("","23")

        elif one_of_ten == 9:
            call sna_main("This one girl confessed to me that she has frequent fantasizes about being abused by that squib mr.Filch.","snape_19")
            call sna_main("I think I could arrange that. Should I?","snape_14")
            call sna_main("","snape_02")

        elif one_of_ten == 10:
            call sna_main("I used to hate my job so much...","24")
            call sna_main("Hate is clean, simple and certain...","snape_06")
            call sna_main("Now, don't get me wrong - I still hate it.","snape_0")
            call sna_main("But I also sort of love it now...","snape_05")
            sna "How could I not? With all that has been happening lately?"
            call sna_main("To both cherish and hate something to an equal degree...","snape_06")
            call sna_main("It's like being in love again...","snape_19")
            call sna_main("","snape_06")
        
        
    if whoring >= 21: # WHORING LEVEL 08+.
        if one_of_ten == 1:
            call sna_main("Do you know what a \"bukkake\" is?","24")
            sna "What about \"deepthroating\"?"
            sna "And then there is also \"hate-sex\"."
            call sna_main("Kids these days, mate...","snape_05")
            sna "They have a special name for everything."
            call sna_main("Although \"hate-sex\" has always been around...","snape_06")
            call sna_main("Back in my days we just called it \"sex\".","snape_02")

        elif one_of_ten == 2:
            call sna_main("Man, my cock is so ready for the \"Princess Trainer Gold Edition\"!","snape_22")
            call sna_main("*Ahem!* I mean, slytherin rules, I hate gryffindor and stuff...","snape_09")

        elif one_of_ten == 3:
            call sna_main("I organized a small party the other day...","24")
            sna "One girl and three boys..."
            call sna_main("They fucked her and I watched...","snape_13")
            call sna_main(".........................","snape_29")
            call sna_main("You think I've been exercising my dark side a bit too often lately?","snape_05")
            call sna_main("","snape_06")

        elif one_of_ten == 4:
            call sna_main("I'm all out of condoms, mate.","24")
            call sna_main("You think you could hook me up?","snape_02")
            call sna_main("","snape_01")

        elif one_of_ten == 5:
            call sna_main("I am secretly making this special herbal brew that should make her tits lactate...","24")
            call sna_main("Pretty brilliant, huh?","snape_13")
            call sna_main("","23")

        elif one_of_ten == 6:
            call sna_main("So, this witch has my cock in her mouth, right?","24")
            call sna_main("Her hot girlfriend is cleaning my asshole with her tongue...","snape_02")
            sna "Meanwhile this third girl is on her knees with her mouth open, waiting for me to spit in it..."
            sna "And every time I spit, she says: \"Thank you, professor Snape\"."
            call sna_main("That was a bloody surreal evening...","snape_22")
            call sna_main("","snape_02")

        elif one_of_ten == 7:
            call sna_main("This one girl has been begging me to urinate in her mouth for days, now...","snape_06")
            sna "Persistent little minx..."
            call sna_main("Should I give in?","snape_05")
            call sna_main("","23")

        elif one_of_ten == 8:
            call sna_main("I mercilessly dominate both male and female students...","snape_04")
            call sna_main("But in very different ways.","snape_22")
            call sna_main("","23")

        elif one_of_ten == 9:
            call sna_main("I love my life!","23")
            call sna_main("Still hate my job though...","snape_16")
            call sna_main("I wish I could skip all the teaching, but keep all the fucking.","snape_14")
            call sna_main("","23")

        elif one_of_ten == 10:
            call sna_main("I almost feel bad for having all the fun.","24")
            call sna_main("do You want me to send you up some young slut?","snape_14")
            call sna_main("","23")

        
    
    
    
    
    
    
    
    
    jump snape_ready
    
    
    
#    $ snape_busy = True
    
#    hide screen snape_02 #Snape stands still.
#    hide screen bld1
#    hide screen snape_main
#    with d3
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

### CHITCHAT EVENTS ###
label chitchat_event_01: #Snape says: so you tutor her now?". Happens after tutoring unlocks.
    hide screen snape_main
    with d3
##############################################################################
#########   JJ Edits   12/29/2014  ###########################################
#    sna_[1] "So..."
#    sna_[1] "I hear miss Granger is taking private lessons from you now?"
#    m "Yeah, I suppose she does..."
#    m "Not sure where this fits into our plan though."
#    sna_[9] "What do you mean? It fits perfectly."
#    sna_[9] "I myself and a couple of other teacher are failing the crap out of that girl!"
#    sna_[9] "As a result she spends more time with studying..."
#    sna_[9] "Even taking private lessons now..."
#    sna_[18] "This way she has very little time left to be noisy and cause me headaches."
#    m "I see..."
#    sna_[10] "Yes, yes... just, you so know..."
#    sna_[10] "Don't actually teach her anything useful, alright?"
#    m "I'll do my best."
#    sna_[1] "Well, if there is that's all..."
###  Altered this chit chat to reflect JJ's tutoring results  
    sna_[1]  "The Granger girl is driving me mad with her accusations.  They must stop!  I think she was even coming on to me!"  
    sna_[7] "As though I would fall for such a transparent ploy! Though she does look to have a luscious body under that frumpy sweater..."
    sna_[4] "Have you done anything to deal with her?  If you have not..."
    sna_[9] "I found a lovely potion in my cupboard that will put her into a long, wasting slumber for which there is no antidote."
    m  "Don’t worry, Severus.  I have her well in hand."  
    sna_[10]  "Oh, really?  How?"  
    m "Well, for starters she is seeing me for magic lessons.  I am teaching her how to do magic without wands or incantations."
    sna_[17] "But that’s nearly impossible for someone of her age!  All but the most powerful wizards and witches must use wands."  
    sna_[2] "And at her ability level she will need to verbalize all but the simplest spells."
    m  "Not to worry.  I plan to teach her how I do magic and I don’t need to do any of that."
    sna_[6] "That's ridiculous!  Your magic only works for you!"
    m "Exactly!"
    sna_[18] "Oh, you are devious!  But you said for starters..."
    m "Are you familiar with a Professor Trelawney?"
    sna_[15] "Sybil Trelawney?  That idiot?!?  Her so-called classes are a blot upon the school’s reputation!"
    sna_[7] "She’s a laughing-stock among all of the other schools in Europe!"
    m "I see. It seems I’ve instructed Miss Granger to re-enroll in Trelawney’s Divination class during her usual study time."
    m "As it turns out, Miss Granger over the years has transferred her magical aura into her wand."
    m  "She is in desperate need of instruction on how to read magical auras."
    sna_[7] "What rubbish is this?  Magical auras?  Transferring to a wand?  There's no such thing!"
    m "Ah, well, we must not disabuse Miss Granger of that notion, shall we?"
    m "She has lost the confidence that she can do much magic at all without her wand now."
    sna_[8] "That's...despicable.  I wish I had thought of that."
    m  "I’ve also asked that Trelawney person to have Miss Granger make up all the work she may have missed before and provide after-class tutoring."
    m  "I think it amounts to a couple of years of class work and of course less time to study in her other classes..."
    sna_[8] "......................"
    sna_[18] "That’s...that’s more brutal than I think I would have been.  And I hate the Granger bitch!"
    m  "Miss Granger is convinced that her troubles are because she has lost her innate magic aura.  I pointed out that the solution is simple.  "
    m  "To retrieve it she must masturbate with her wand several times per day.  This is where you can help."
    m  "You might want to let her know if you notice her aura is dwindling so she'll increase her efforts to regain it."
    sna_[18]  "..........................."
    sna_[15]  "Ah ha ha ha!  I am so very, very glad you are my ally and not my enemy."
    m "That’s kind of you to say Severus."  
    sna_[18]  "I think I'll return to my office and think about how best to leverage this new information before my next class begins."
    m "Good day, Severus."
# End alteration  JJ
    
    

    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snape_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_walk_01_f 
    with d3

    $ chitchat_event_01_happened = True #Activates next event - Event_15 Hermione sells her first favour.
    $ snape_busy = True
    $ days_without_an_event = 0
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    
    jump day_main_menu











### CHITCHAT WITH HERMIONE ###
label chit_chat:
    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            call her_main("Maybe, if I'd work harder, I could squeeze a few more classes into my schedule...","body_04")
            call her_main("","body_03")
        
        elif one_of_ten == 2:
            call her_main("Actually I don't mind it to be called a \"know-it-all\".","body_04")
            her "I think it's rather flattering..."
            call her_main("","body_03")
        elif one_of_ten == 3:
            call her_main("The basilisk, also known as the king of serpents.","body_04")
            her "Herpo the Foul was the first to breed a Basilisk."
            her "He accomplished that by--"
            call her_main("Oh, I'm sorry, professor, we have another test tomorrow...","body_10")
            her "I Just want to make sure that I'm ready..."
            call her_main("","body_01")
        elif one_of_ten == 4:
            call her_main("If my body wouldn't require sleep...","body_10")
            call her_main("I would be able to spend twice as much time with studying!?","body_18")
            call her_main("I wonder if there's a spell for that...","body_14")
            call her_main("","body_03")
        
        elif one_of_ten == 5:
            call her_main("So far professor Trelawney did not taught me a single piece of any actual knowledge, sir.","body_04")
            call her_main("","body_03")
       
        elif one_of_ten == 6:
            call her_main("If only more students were honest, responsible and diligent like me.","body_04")
            call her_main("","body_03")
      
        elif one_of_ten == 7:
            call her_main("How can some people be so ignorant to the world's problems?","body_04")
            her "Personally, I think that every single one of us should work harder to make our world a better place."
            call her_main("","body_03")
            
        elif one_of_ten == 8:
            call her_main("It's been raining quite a lot lately...","body_10")
            call her_main("","body_01")
    
        elif one_of_ten == 9:
            call her_main("Very few people know this...","body_10")
            call her_main("...But I really like chocolate.","body_06")
            call her_main("","body_01")
       
        elif one_of_ten == 10:
            call her_main("I am sorry sir, but I don't really have time for idle chat chats...","body_06")
            call her_main("","body_03")


    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            call her_main("I read somewhere that a full moon often makes it easier to concentrate at a task at hand...","body_04")
            call her_main("","body_03")
            
        elif one_of_ten == 2:
            call her_main("I love nothing more than to curl up by a fireplace during a rainstorm with a good book...","body_06")
            call her_main("","body_01")
            
        elif one_of_ten == 3:
            call her_main("A peculiar rumour concerning professor Snape has been circulating in the school lately...","body_10")
            call her_main("No, I probably shouldn't...","body_15")
            call her_main("","body_03")
            
        elif one_of_ten == 4:
            call her_main("Despite the questionable nature of the favours you have been buying from me lately, sir...","body_04")
            her "I am grateful to you for your help..."
            call her_main("Gryffindor needs those points now more than ever...","body_09")
            call her_main("","body_03")
            
        elif one_of_ten == 5:
            call her_main("Why Quidditch is so popular among the girls is simply beyond me...","body_04")
            call her_main("","body_03")
            
        elif one_of_ten == 6:
            call her_main("The \"Men's Rights Movement\" is steadily gaining popularity.","body_04")
            her "It's very fulfilling to know that you are helping to improve our society."
            call her_main("","body_03")
            
        elif one_of_ten == 7:
            call her_main("The Hogwarts school library is considered to be quite extensive...","body_04")
            call her_main("Still, I can't help but wish that it'd be bigger...","body_08")
            call her_main("","body_03")
            
        elif one_of_ten == 8:
            call her_main("As one of the top students in this school I have a reputation to keep...","body_10")
            her "People look up to me..."
            call her_main("...So, your discretion is very appreciated, sir.","body_31")
            call her_main("","body_29")
            
        elif one_of_ten == 9:
            call her_main("That favour I sold you the other say, sir...","body_11")
            call her_main(".......","body_33")
            call her_main("I only agreed to it because the needs of my house always come first.","body_87")
            call her_main("I just wanted you to know that, sir...","body_120")
            
        elif one_of_ten == 10:
            call her_main("The \"Autumn Ball\" is still several months away...","body_04")
            call her_main("But some girls are already discussing what kind of dress they are going to wear...","body_11")
            call her_main("","body_185")

  
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            call her_main("Do you remember when you asked me to show you my panties for the first time sir?","body_04")
            her "I was so furious with you then..."
            call her_main("Now I see that I was just being selfish...","body_09")
            her "After all, the honour of my house is at stake here..."
            call her_main("And that shall be my one and only concern!","body_07")
            
        elif one_of_ten == 2:
            call her_main("The rate at which the Slytherin house has been gaining points lately is simply ridiculous.","body_04")
            call her_main("I think professor Snape might be behind it.","body_05")
            call her_main("You should look into this, sir.","body_04")
            call her_main("","body_03")
            
        elif one_of_ten == 3:
            call her_main("Ashwinder eggs, rose thorns, moonstone...","body_10")
            call her_main("Huh? Am I thinking out loud again?","body_11")
            call her_main("I apologize...","body_24")
            call her_main("It's just that we have another test soon...","body_13")

        elif one_of_ten == 4:
            call her_main("I dislike the entire house of Slytherin with all my heart, sir.","body_77")
            
        elif one_of_ten == 5:
            call her_main("Hogwarts has really become a second home to me lately...","body_16")
            call her_main("I don't even miss my parents nearly as much anymore...","body_71")
            call her_main("Come to think of it I don't miss them at all...","body_18")
            call her_main("I'm an awful daughter...","body_118")

        elif one_of_ten == 6:
            call her_main("*Yawn!* I read about this technique that supposedly allows you to cut your sleep time in half...","body_70")
            call her_main("It don't think it's working though.... *Yawn!*","body_73")

        elif one_of_ten == 7:
            call her_main("Even after I graduate from Hogwarts I plan to keep on working hard.","body_04")
            call her_main("If I give it my all I can make this world a better place, I know it!","body_02")
            call her_main("","body_03")
           
        elif one_of_ten == 8:
            call her_main("Somehow I have the feeling that this year will become a pivotal turning point in my life...","body_11")
            call her_main("","body_13")
  
        elif one_of_ten == 9:
            call her_main("Some of the less traveled school corridors are not very well lit and rather dusty...","body_04")
            her "Please take care of this, sir..."
            call her_main("","body_03")
       
        elif one_of_ten == 10:
            call her_main("I've read about this thing called \"Time-Turner\".","body_14")
            her "It allows the user to control the flow of time..."
            call her_main("Having a device like that would do wonders for my schedule...","body_16")
            call her_main("","body_17")
        

    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            call her_main("My \"men's rights movement\" has been losing its popularity lately...","body_11")
            call her_main("It's as if people don't even care!","body_12")

        elif one_of_ten == 2:
            call her_main("Thank you for buying all those favours from me, sir.","body_04")
            call her_main("Some of them were borderline inappropriate, sure...","body_07")
            call her_main("But I don't mind sacrificing my dignity if it will allow Gryffindor to compete with Slytherin on equal ground.","body_04")
            call her_main("","body_03")

        elif one_of_ten == 3:
            call her_main("Quidditch is stupid!","body_77")
            call her_main("There. I said it.","body_17")
            
        elif one_of_ten == 4:
            call her_main("Sir, there is something about professor Snape that I think you should know...","body_02")
            call her_main(".................","body_10")
            call her_main(".........................","body_09")
            call her_main("uhm... Never mind...","body_04")
            call her_main("","body_03")
 
        elif one_of_ten == 5:
            call her_main("Some of the Slytherin girls sell sexual favours almost openly these days...","body_04")
            call her_main("You need to put an end to such practices, sir.","body_02")
            call her_main("(I can barely keep up...)","body_69")

        elif one_of_ten == 6:
            call her_main("Life works in mysterious ways...","body_10")
            call her_main("Wouldn't you agree, sir?","body_08")
            call her_main("","body_13")

        elif one_of_ten == 7:
            call her_main("Slytherins...","body_76")
            call her_main("","body_77")
            
        elif one_of_ten == 8:
            call her_main("I've been spending so much time in your office lately, sir...","body_10")
            call her_main("If I'm not careful some people may think that I have become your pet...","body_11")
            call her_main("I meant to say the teacher's pet...","body_34")
            call her_main("","body_33")

        elif one_of_ten == 9:
            call her_main("My favourite colours?","body_02")
            call her_main("scarlet and gold of course!","body_02")
            call her_main("","body_03")
       
        elif one_of_ten == 10:
            call her_main("Is it weird that my best friends are boys?","body_10")
            call her_main("","body_01")
        

        
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            call her_main("Sir, with all due respect...","body_07")
            her "Professor Snape's debauchery is getting out of hand!"
            call her_main("You must do something, sir.","body_11")
            call her_main("","body_03")

        elif one_of_ten == 2:
            call her_main("I am willing to go to great lengths to insure the superiority of my house...","body_04")
            her "But that does not mean that I take pleasure in selling myself out to you in exchange for house points, sir."
            call her_main("{size=-4}(Like some sort of prostitute-witch...){/size}","body_118")

        elif one_of_ten == 3:
            call her_main("What will it be today, sir?","body_79")
            
        elif one_of_ten == 4:
            call her_main("lately I have not been studying nearly as much as I used to...","body_11")
            call her_main("Am I losing my motivation?","body_10")
            call her_main("","body_13")
            
        elif one_of_ten == 5:
            call her_main("My least favourite subject?","body_08")
            call her_main("Divination.","body_09") 
            
        elif one_of_ten == 6:
            call her_main("My father used to say: \"Magic is just science we don't understand yet\".","body_14")
            call her_main("He could't be more wrong of course...","body_10")
            call her_main("","body_13")
            
        elif one_of_ten == 7:
            call her_main("Despite everything...","body_04")
            call her_main("I am thankful that you keep on buying favours from me, sir...","body_10")
            call her_main("","body_13")
            
        elif one_of_ten == 8:
            call her_main("It's quite cold outside today, isn't it?","body_14")
            call her_main("","body_15")
            
        elif one_of_ten == 9:
            call her_main("The \"Autumn Ball\" will be soon...","body_14")
            call her_main("","body_15")
            
        elif one_of_ten == 10:
            call her_main("People hardly show up for my \"men's rights movement\" meetings at all anymore...","body_10")
            call her_main("","body_13")
    
    
    
    
    
    
        
    if whoring >= 15 and whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            call her_main("Would you like me to show you my breasts today, sir?","body_87")
            call her_main("Yes... I would willingly expose myself to you, professor...","body_78")
            call her_main("That's how selfless I am!","body_79")
           
        elif one_of_ten == 2:
            call her_main("I can't help but feel bad for the house elves who do my laundry...","body_14")
            call her_main("I mean, all those dreadful semen stains...","body_87")
            call her_main("","body_118")

        elif one_of_ten == 3:
            call her_main("it Doesn't matter how many times you ask me this, sir...","body_02")
            her "The answer shall remain the same..."
            call her_main("I have nothing but resentment for the \"Slytherins\"!","body_47")
            call her_main("","body_69")
        
        
        elif one_of_ten == 4:
            call her_main("When I think about all the favours I sold you over these last months, sir...","body_02")
            call her_main("Although I do feel a little bit embarrassed...","body_87")
            call her_main("I also feel very proud of myself.","body_120")
            
        elif one_of_ten == 5:
            call her_main("I still dedicate a lot of my time to studying...","body_14")
            her "But not nearly as much of it as I used to..."
            call her_main("Somehow I just don't enjoy studying at all anymore...","body_11")
            call her_main("","body_13")
        
        elif one_of_ten == 6:
            call her_main("Gryffindor shall get the house cup this year!","body_04")
            call her_main("{size=-4}(Even if it should cost me my dignity...){/size}","body_118")
            call her_main("","body_120")
           
           
        elif one_of_ten == 7:
            call her_main("I don't mind the autumn weather...","body_14")
            call her_main("But my favourite season is winter.","body_16")
            call her_main("","body_15")
        
        elif one_of_ten == 8:
            call her_main("I used to look down on girls who spend too much time with worrying about the way they look...","body_14")
            her "But I was wrong to do so..."
            her "I am starting to understand how important it really is for a girl to look pretty."
            call her_main("...............","body_29")
            call her_main("I've been on a diet lately...","body_122")
            call her_main("","body_34")
            call her_main("","body_33")
       
        elif one_of_ten == 9:
            call her_main("Lately I've been feeling rather confident around the boys...","body_14")
            call her_main("I think I have you to thank for that, sir.","body_06")
            
        elif one_of_ten == 10:
            call her_main("My favourite subject?","body_14")
            call her_main("Hm...","body_13")
            call her_main("I suppose that would be \"charms\"...","body_14")
            call her_main("","body_15")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            call her_main("Just let me know what will be required of me today, sir.","body_04")
            call her_main("","body_03")
           
        elif one_of_ten == 2:
            call her_main("I barely study at all anymore...","body_11")
            her "Despite that my popularity among the other students seems to be growing..."
            call her_main("Hm...","body_13")
                 
        elif one_of_ten == 3:
            call her_main("I wouldn't say \"no\" to a bottle of butterbeer right about now...","body_64")
            call her_main("","body_68")
        
        elif one_of_ten == 4:
            call her_main("What is it sir? Do you have another present for me?","body_06")
            call her_main("Oh... I see...","body_12")

        elif one_of_ten == 5:
            call her_main("I am doing well, thank you for asking.","body_06")

        elif one_of_ten == 6:
            call her_main("Do I look fat to you sir?","body_11")
            call her_main("I wonder if the diet is working...","body_29")
           
        elif one_of_ten == 7:
            call her_main("I remember that I used to say that books were my friends...","body_16")
            call her_main("Now that sounds so lame.","body_24")
            call her_main("","body_15")
        
        elif one_of_ten == 8:
            call her_main("Add ashwinder egg to cauldron...","body_04")
            her "Then add horseshoe reddish and heat..."
            her "Then juice a squill bulb..."
            call her_main("Or was it a dash of thyme first?","body_10")
            call her_main("..............","body_13")
            call her_main("Oh, who cares?","body_24")
            call her_main("","body_06")
       
        elif one_of_ten == 9:
            call her_main("Do You think I am wearing enough makeup, sir?","body_14") 
            her "Wearing too much would look vulgar..."
            call her_main("But wearing too little would make me look plain...","body_13")
            call her_main("I don't want to look plain!","body_12")
            
        elif one_of_ten == 10:
            call her_main("Would you like to see my tits today, sir?","body_64") 
            call her_main("25 house points, please.","body_111")
            call her_main("","body_120")
    
   
    if whoring >= 21: # WHORING LEVEL 08+.
        
        if one_of_ten == 1:
            call her_main("Do You have any adult magazines you don't need, sir?","body_189")
            call her_main("","body_188")

        elif one_of_ten == 2:
            call her_main("I am sorry to bother you with this, sir...","body_31")
            her "But do you have any condoms?"
            call her_main("This is not for me of course... I'm asking for a friend...","body_34")
                 
        elif one_of_ten == 3:
            call her_main("It's been getting so cold lately...","body_14")
            call her_main("I hope it's going to start snowing soon...","body_06")
        
        elif one_of_ten == 4:
            call her_main("Jump and scream for the Gryffindor team!","body_127")
            call her_main("So daring and bold, sporting red and gold!","body_80")
            call her_main("","body_06")

        elif one_of_ten == 5:
            call her_main("I hope the ball goes smoothly...","body_10")
            call her_main("","body_13")

        elif one_of_ten == 6:
            call her_main("I wonder what Ginny is going to wear for the ball...","body_06")
        
        elif one_of_ten == 7:
            call her_main("Considering the nature of the favours you keep buying from me sir...","body_16")
            call her_main("I seldom bother to put on underwear at all anymore...","body_11")
        
        elif one_of_ten == 8:
            call her_main("Sir, could you put your penis in my mouth?","body_117")
            call her_main("Sir, I am begging you...","body_135")
            call her_main("Fifty five points, please!","body_111")
            call her_main("","body_122")

        elif one_of_ten == 9:
            call her_main("A read this one article about the positive effects of semen on a woman's skin...","body_127")
            call her_main("I wonder where their information is coming from...","body_128")
            call her_main("Did the magazine conduct research of some sort?","body_122")
            call her_main("","body_128")

        elif one_of_ten == 10:
            call her_main("It goes like this...","body_127")
            her "First Gryffindor, then Ravenclaw, then Hufflepuff..."
            call her_main("And Slytherin is not even on the list!","body_186")
            call her_main("","body_120")



    jump day_time_requests

#    if daytime:
#        jump night_main_menu
#    else:
#        $ hermione_sleeping = True
#        jump day_main_menu            
    
    
    