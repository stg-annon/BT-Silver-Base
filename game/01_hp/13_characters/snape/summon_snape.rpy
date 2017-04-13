
label summon_snape:
    if snape_busy:
        ">Professor Snape is unavailable."
        if daytime:
            jump day_main_menu
        else: 
            jump night_main_menu
    
    $ menu_x = 0.2 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ snape_SC.chibi.walk(750,500,2)
    $ snape_SC.body = "snape_01"
    $ snape_SC.showScreen()
    show screen snape_chibi_standing #Snape stands still.
    show screen bld1
    with d3
    
    $ snape_SC.say("Yes, what is it?")
    
    label snape_ready:
        
    if daytime:
        menu:
            "-Chit chat-" if daytime and not chitchated_with_snape: # sfmax - friendship with Snape maxed out.
                $ chitchated_with_snape = True #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                call snape_chitchat
                jump snape_ready
            "\"Nevermind.\"":
                $ snape_SC.say("Alright, back to work then...")
    else:
        menu:
            "-Chit chat-" if not chitchated_with_snape and sfmax: # sfmax - friendship with Snape maxed out.
                $ chitchated_with_snape = True #Prevents you from chitchating more then once a day. Turns back to False every night and every day.
                $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                call snape_chitchat
                jump snape_ready
            "\"Let's hang.\"" if not sfmax: # Turns TRUE when friendship with Snape been maxed out.
                if (renpy.random.randint(1, 10) == 10) or (snape_friendship >= 88 and whoring < 15):
                    if one_out_of_three == 1:
                        $ snape_SC.say("Sorry, I can't tonight...")
                    elif one_out_of_three == 2:
                        $ snape_SC.say("Sorry, I have other business to attend to tonight...")
                    elif one_out_of_three == 3:
                        $ snape_SC.say("Sorry, I have other plans. Maybe some other time?")
                    jump snape_ready
                else:
                    $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
                    jump hang_with_snape
            "\"Nevermind.\"":
                $ snape_SC.say("Goodnight then.")
    
    stop music fadeout 1.0
    $ menu_x = 0.5 #Menu is moved to the left side. (Default menu_x = 0.5)
    $ snape_busy = True
    
    $ snape_SC.hideScreen()
    hide screen snape_chibi_standing #Snape stands still.
    hide screen bld1
    with d3
    
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    if daytime:
        jump day_main_menu
    else: 
        jump night_main_menu
    
label snape_chitchat:
    if not chitchat_event_01_happened and tutoring_hermione_unlocked and days_without_an_event >=2:
        jump chitchat_event_01
    
    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    ### CHIT CHATS WITH SNAPE ###
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            $ snape_SC.say("Do You really think you can do this?","snape_24")
            $ snape_SC.say("Do You think you can break the girl?","snape_25")
        elif one_of_ten == 2:
            $ snape_SC.say("Don't you just hate this wretched sunny weather?","snape_01")
            $ snape_SC.say("I wish it would rain every day.","snape_06") 
        elif one_of_ten == 3:
            $ snape_SC.say("I am feeling rather doubtful about our whole plan again...","snape_06")
        elif one_of_ten == 4:
            $ snape_SC.say("Are you sure that you are not Albus Dumbledore?","snape_05")
            $ snape_SC.say("I'm still having a hard time believing this whole thing sometimes...")
        elif one_of_ten == 5:
            $ snape_SC.say("I killed a pupil once.","snape_01")
            $ snape_SC.say("Yes... I strangled the maggot with my bare hands.","snape_02")
            $ snape_SC.say("........*low growl*.","snape_03")
            $ snape_SC.say("Did that sound believable?","snape_05")
            $ snape_SC.say("The moment those animals stop fearing me, I'm done for.","snape_06")
            $ snape_SC.say("Cultivating fear in the hearts of your students is the most important task for every teacher.","snape_26")
        elif one_of_ten == 6:
            $ snape_SC.say("Those Weasley maggots...","snape_04")
            $ snape_SC.say("One of these days I'll just snap, I swear.","snape_07")
        elif one_of_ten == 7:
            $ snape_SC.say("Don't you think that owl post is a bit ridiculous?","snape_05")
            $ snape_SC.say("I'd much rather use ravens.")
        elif one_of_ten == 8:
            $ snape_SC.say("I'm having the worst day of my life...","snape_06")
            $ snape_SC.say("So I'm really Not in the mood for chit-chats...")
        elif one_of_ten == 9:
            $ snape_SC.say("Being a wizard is a 24 hours a day...","snape_04")
            $ snape_SC.say("7 days a week...","snape_03")
            $ snape_SC.say("365 days a year job.","snape_04")
            $ snape_SC.say("We get no vacation days...")
        elif one_of_ten == 10:
            $ snape_SC.say("Quidditch...","snape_04")
            $ snape_SC.say("What a waste of time and ressources!","snape_10")
            $ snape_SC.say("","snape_04")
    
    
    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02.
        if one_of_ten == 1:
            $ snape_SC.say("I have yet to notice any changes in miss Granger's behavior...","24")
            $ snape_SC.say("Are you sure that you know what you're doing?","snape_05")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 2:
            $ snape_SC.say("It sure feels good to be able to grant house points or take them away whenever I feel like it.","24")
            $ snape_SC.say("My authority among the students is growing every day...")
            $ snape_SC.say("And when I say \"authority\" I mean \"fear\".","snape_02")
        elif one_of_ten == 3:
            $ snape_SC.say("Did you know that the full moon is known to boost male potency?","24")
            $ snape_SC.say("It also makes it easier to focus at a task at hand, making you more proactive.")
            $ snape_SC.say("But who gives a damn about that, am I right?","snape_28")
            $ snape_SC.say("","snape_29")
        elif one_of_ten == 4:
            $ snape_SC.say("My precious Slytherins make all of this torment worth while...","snape_06")
            $ snape_SC.say("Their skirts are getting shorter every week, I swear.","snape_19")
        elif one_of_ten == 5:
            $ snape_SC.say("There was a time when I was young and full of hope...","snape_06")
            $ snape_SC.say("Ha-ha... I'm pulling your leg, mate","snape_28")
            $ snape_SC.say("I was never full of hope...","snape_29")
        elif one_of_ten == 6:
            $ snape_SC.say("Duelling is one of my fortes, you know...","snape_09")
        elif one_of_ten == 7:
            $ snape_SC.say("A \"Men's rights movement\"...?","snape_05")
            $ snape_SC.say("What's next? A house elves' rights movement?","snape_04")
            $ snape_SC.say("How could a top student could be that dumb?","snape_06")
        elif one_of_ten == 8:
            $ snape_SC.say("I don't play favourites with my students.","snape_05")
            $ snape_SC.say("I merely tolerate some of them and hate the rest.","snape_04")
        elif one_of_ten == 9:
            $ snape_SC.say("There are four student houses at Hogwarts...","24")
            $ snape_SC.say("Slytherin, Ravenclaw, Gryffindor and...")
            $ snape_SC.say("...and Huff-something...","snape_05")
            $ snape_SC.say("No one really cares.","snape_29")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 10:
            $ snape_SC.say("Brooms are for kids and witches.","24")
            $ snape_SC.say("You'll never see a self-respecting wizard prancing around on a broomstick.","snape_05")
            $ snape_SC.say("","snape_09")
    
    
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            $ snape_SC.say("Any progress on breaking our little ms. know-it-all?","24")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 2:
            $ snape_SC.say("The other day this one girl sold me her panties for five house points.","24")
            $ snape_SC.say("And man, was she excited about that...","snape_14")
            $ snape_SC.say("I think she would've given them away for free just to please me.","snape_19")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 3:
            $ snape_SC.say("I'm having a rather pleasant day so far...","23")
            $ snape_SC.say("Bet you didn't expect to hear me saying that?","snape_02")
        elif one_of_ten == 4:
            $ snape_SC.say("Quidditch seems to steadily gain more and more popularity over the years...","24")
            $ snape_SC.say("How disappointing...","snape_04")
        elif one_of_ten == 5:
            $ snape_SC.say("My life was incredibly dull before your arrival...","24")
            $ snape_SC.say("Nowadays it's...","snape_05")
            $ snape_SC.say("...less dull.","snape_02")
        elif one_of_ten == 6:
            $ snape_SC.say("Regrets? I don't know the meaning of the word!","snape_05")
            $ snape_SC.say("I live a very fulfilling life.","snape_06")
            $ snape_SC.say("Ha-ha-ha! I'm sorry, I just can't say such nonsense with a straight face.","snape_28")
            $ snape_SC.say("","snape_26")
        elif one_of_ten == 7:
            $ snape_SC.say("There is no room for mistakes during class.","24")
            $ snape_SC.say("One slip-up and the bloody bastards will tear you to shreds.","snape_04")
        elif one_of_ten == 8:
            $ snape_SC.say("You are the only person I have to answer to...","snape_04")
            $ snape_SC.say("So I can almost literally do whatever the bloody hell I want these days...","snape_05")
            $ snape_SC.say("...............","snape_09")
            $ snape_SC.say("So that's what freedom feels like, huh?","snape_06")
        elif one_of_ten == 9:
            $ snape_SC.say("Autumn... the most depressing time of the year...","snape_06")
            $ snape_SC.say("I Love it!","snape_02")
            $ snape_SC.say("","23")
        elif one_of_ten == 10:
            $ snape_SC.say("I have a magical portrait of a stripper hanging in my room.","24")
            $ snape_SC.say("One of my most precious possessions.","snape_22")
            $ snape_SC.say("","snape_09")
    
    
    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            $ snape_SC.say("Lately miss Granger has gotten aggressive almost to the point of open hostility...","24")
            $ snape_SC.say("I hope you know what you're doing...","snape_05")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 2:
            $ snape_SC.say("I shouldn't feel bad about having sex with my students, right?","snape_26")
            $ snape_SC.say("I mean, you should see the way some of those girls wear their uniforms...","snape_05")
            $ snape_SC.say("They're practically asking for it.","snape_13")
            $ snape_SC.say("","snape_12")
        elif one_of_ten == 3:
            $ snape_SC.say("It's been raining a lot lately...","23")
            $ snape_SC.say("I wonder if I enjoy rainy weather so much simply because it makes most people miserable...","snape_02")
            $ snape_SC.say("","23")
        elif one_of_ten == 4:
            $ snape_SC.say("According to a recent study 9 out of 10 girls secretly fantasize about being abused by their teacher.","24")
            $ snape_SC.say("I bet that 10th girl was Hermione Granger.","snape_03")
            $ snape_SC.say("","snape_01")
        elif one_of_ten == 5:
            $ snape_SC.say("These days I have to actually make an effort to maintain my usual bad mood.","24")
            $ snape_SC.say("","23")
        elif one_of_ten == 6:
            $ snape_SC.say("Do You have a few condoms to spare?","24")
            $ snape_SC.say("I have a whole pack but...","snape_25")
            $ snape_SC.say("...they've expired years ago...","snape_06")
            $ snape_SC.say("The changes you brought into my life, mate.","snape_02")
            $ snape_SC.say("","23")
        elif one_of_ten == 7:
            $ snape_SC.say("You think we could turn Hogwarts into a \"girls only\" school?","24")
            $ snape_SC.say("Hogwarts Girls Academy!","23")
            $ snape_SC.say("Now that would be bloody perfect... except for Lockhart maybe.","snape_13")
        elif one_of_ten == 8:
            $ snape_SC.say("Why did the teacher cross the road?","24")
            $ snape_SC.say("To get away from his students!","snape_25")
            $ snape_SC.say("Ha-ha-ha! Gets me every time!","snape_28")
            $ snape_SC.say("","snape_25")
        elif one_of_ten == 9:
            $ snape_SC.say("Want to hear a funny story?","24")
            $ snape_SC.say("Well, I don't know any...","snape_06")
        elif one_of_ten == 10:
            $ snape_SC.say("Do you know what a \"royal goblet\" is?","snape_05")
            $ snape_SC.say("You do, don't you?","snape_13")
            $ snape_SC.say("","23")
    
    
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            $ snape_SC.say("15 points for a blowjob is a fair price, right?","24")
            $ snape_SC.say("","23")
        elif one_of_ten == 2:
            $ snape_SC.say("Have you ever been in love, mate?","24")
            $ snape_SC.say("Have you ever been in love with a schoolgirl?","snape_02")
            $ snape_SC.say("What about half a dozen of them at once?","snape_22")
            $ snape_SC.say("","snape_20")
        elif one_of_ten == 3:
            $ snape_SC.say("Something rather brilliant happened last night between me and this Slytherin mynx.","snape_20")
            $ snape_SC.say("Long story short, all of my muscles ache and I still feel rather dehydrated...","snape_22")
            $ snape_SC.say("","snape_13")
        elif one_of_ten == 4:
            $ snape_SC.say("It's getting colder lately...","24")
            $ snape_SC.say("Winter is coming...","23")
        elif one_of_ten == 5:
            $ snape_SC.say("Have you ever seen muggle women dressed as witches?","24")
            $ snape_SC.say("So adorable.","snape_19")
        elif one_of_ten == 6:
            $ snape_SC.say("Do you know what an \"Internet\" is?","24")
            $ snape_SC.say("Apparently it allows you to go \"on the line\" and see magical photographs of naked muggle women.","snape_02") # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
            $ snape_SC.say("Kind of makes me wish we had one here in Hogwarts.","snape_26")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 7:
            $ snape_SC.say("I have two major passions in life...","24")
            $ snape_SC.say("Dark arts...")
            $ snape_SC.say("......","snape_12")
            $ snape_SC.say("...and sluts.","snape_13")
        elif one_of_ten == 8:
            $ snape_SC.say("You think I ought to cut down on my drinking?","24")
            $ snape_SC.say("But my life is so stressful...","snape_06")
            $ snape_SC.say("Hm...","snape_09")
            $ snape_SC.say("I'll try and cut down on the liquor...","snape_06")
            $ snape_SC.say("In favour of sweaty monkey-sex with my students!","snape_21")
            $ snape_SC.say("","snape_19")
        elif one_of_ten == 9:
            $ snape_SC.say("Miss Granger has been suspiciously quiet lately...","24")
            $ snape_SC.say("I bet she is scheming something...","snape_03")
            $ snape_SC.say("","snape_01")
        elif one_of_ten == 10:
            $ snape_SC.say("It's quite easy to write a book and kill off half of the main characters for the sake of dramatic impact...","24")
            $ snape_SC.say("To put your characters against impossible odds and let them make it out alive in a believable manner...")
            $ snape_SC.say("Now {size=+7}that{/size} requires skill.","snape_02")
            $ snape_SC.say("","23")
    
    
    if whoring >= 15 and whoring <= 17: # WHORING LEVEL 06.
        if one_of_ten == 1:
            $ snape_SC.say("What if the girl is not our pet, but we are her's?","snape_11")
            $ snape_SC.say("","snape_26")
        elif one_of_ten == 2:
            $ snape_SC.say("Have you heard of the \"Slug club\"?","24")
            $ snape_SC.say("What if I start a club of my own?")
            $ snape_SC.say("I would call it the \"Snape Club\"!","23")
            $ snape_SC.say("I would invite girls over, offer them some tea and muffins...")
            $ snape_SC.say("Feel them up a little...","snape_13")
            $ snape_SC.say("Bloody brilliant!","snape_22")
            $ snape_SC.say("","snape_02")
        elif one_of_ten == 3:
            $ snape_SC.say("Tell me Genie... Have you ever had your asshole licked clean by a young witch?","snape_02")
            $ snape_SC.say("A life changing experience, neither less nor more...","snape_21")
            $ snape_SC.say("","snape_02")
        elif one_of_ten == 4:
            $ snape_SC.say("So, how is the training going?","24")
            $ snape_SC.say("All according to plan I hope?")
            $ snape_SC.say("","snape_05")
        elif one_of_ten == 5:
            $ snape_SC.say("I can see Thestrals, you know...","snape_06")
            $ snape_SC.say("","snape_09")
        elif one_of_ten == 6:
            $ snape_SC.say("You know what I like about Quidditch?","24")
            $ snape_SC.say("Nothing! Not a single bloody thing!","snape_15")
            $ snape_SC.say("","snape_16")
        elif one_of_ten == 7:
            $ snape_SC.say("Hogwarts benefited greatly from your arrival.","24")
            $ snape_SC.say("And when I say \"Hogwarts\" I mean \"me\".","snape_02")
            $ snape_SC.say("","23")
        elif one_of_ten == 8:
            $ snape_SC.say("Real wizards wear black.","24")
            $ snape_SC.say("Am I right?","snape_02")
            $ snape_SC.say("","23")
        elif one_of_ten == 9:
            $ snape_SC.say("Some of those Slytherin girls simply adore me these days...","24")
            $ snape_SC.say("Personally I'd much rather be feared...","snape_05")
            $ snape_SC.say("But I am willing to settle for mindless adoration...","23")
        elif one_of_ten == 10:
            $ snape_SC.say("You are being way too generous with those Gryffindor points, mate.","24")
            $ snape_SC.say("Lately I can barely keep up with you...","snape_25")
            $ snape_SC.say("","snape_29")
    
    
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            $ snape_SC.say("Miss Granger really is changing. I can see it clearly now...","24")
            $ snape_SC.say("Her grades went down and even her attendance is far from perfect now...")
            $ snape_SC.say("But despite that she continues to excel at being a pain in my arse!","snape_10")
            $ snape_SC.say("","snape_01")
        elif one_of_ten == 2:
            $ snape_SC.say("My least favourite colour?","snape_05")
            $ snape_SC.say("Let me give you two: red and gold.","snape_07")
            $ snape_SC.say("","snape_04")
        elif one_of_ten == 3:
            $ snape_SC.say("I hear the vampire-theme is quite popular among the girls lately.","24")
            $ snape_SC.say("I would make a great vampire, don't you think?","snape_05")
            $ snape_SC.say("Maybe I should buy a couple of those fake fangs...")
            $ snape_SC.say("Just to drive the horny, little sluts completely crazy.","snape_21")
            $ snape_SC.say("","snape_02")
        elif one_of_ten == 4:
            $ snape_SC.say("I ...hate my life.","24")
            $ snape_SC.say("No, wait, let me try this again...","snape_16")
            $ snape_SC.say("I ...hate my life.","snape_17")
            $ snape_SC.say("Dammit! I'm trying to say \"love\" but it just won't come out...","snape_25")
            $ snape_SC.say("I don't think I've ever used the words \"love\" and \"life\" in one sentence before.","snape_29")
            $ snape_SC.say("Let me try this again...","snape_06")
            $ snape_SC.say("I ha...{w} lo... {w}love my life!","snape_10")
            $ snape_SC.say("There you go, I love my life...","23")
        elif one_of_ten == 5:
            $ snape_SC.say("Sunlight, chocolate, Quidditch, cats and orange juice...","snape_01")
            $ snape_SC.say("That's a list of things I don't care for...")
            $ snape_SC.say("Here is a short list of things I do care for a great deal...","snape_02")
            $ snape_SC.say("The dark arts, wine and pussy.","23")
        elif one_of_ten == 6:
            $ snape_SC.say("have You ever seen two wizards in a fistfight?","snape_02")
            $ snape_SC.say("Bloody hilarious!","snape_28")
            $ snape_SC.say("","23")
        elif one_of_ten == 7:
            $ snape_SC.say("You know that feeling when you just came in a girl's mouth and she swallows it all and says: \"Thank you, professor\"?","snape_14")
            $ snape_SC.say("Isn't that the best?","snape_13")
            $ snape_SC.say("","23")
        elif one_of_ten == 8:
            $ snape_SC.say("do You think the Hogwarts ghosts sometimes spy on girls taking when they a shower and such?","24")
            $ snape_SC.say("If I were a ghost I know I would.","snape_13")
            $ snape_SC.say("","23")
        elif one_of_ten == 9:
            $ snape_SC.say("This one girl confessed to me that she has frequent fantasizes about being abused by that squib mr.Filch.","snape_19")
            $ snape_SC.say("I think I could arrange that. Should I?","snape_14")
            $ snape_SC.say("","snape_02")
        elif one_of_ten == 10:
            $ snape_SC.say("I used to hate my job so much...","24")
            $ snape_SC.say("Hate is clean, simple and certain...","snape_06")
            $ snape_SC.say("Now, don't get me wrong - I still hate it.","snape_0")
            $ snape_SC.say("But I also sort of love it now...","snape_05")
            $ snape_SC.say("How could I not? With all that has been happening lately?")
            $ snape_SC.say("To both cherish and hate something to an equal degree...","snape_06")
            $ snape_SC.say("It's like being in love again...","snape_19")
            $ snape_SC.say("","snape_06")
    
    
    if whoring >= 21: # WHORING LEVEL 08+.
        if one_of_ten == 1:
            $ snape_SC.say("Do you know what a \"bukkake\" is?","24")
            $ snape_SC.say("What about \"deepthroating\"?")
            $ snape_SC.say("And then there is also \"hate-sex\".")
            $ snape_SC.say("Kids these days, mate...","snape_05")
            $ snape_SC.say("They have a special name for everything.")
            $ snape_SC.say("Although \"hate-sex\" has always been around...","snape_06")
            $ snape_SC.say("Back in my days we just called it \"sex\".","snape_02")
        elif one_of_ten == 2:
            $ snape_SC.say("Man, my cock is so ready for the \"Princess Trainer Gold Edition\"!","snape_22")
            $ snape_SC.say("*Ahem!* I mean, slytherin rules, I hate gryffindor and stuff...","snape_09")
        elif one_of_ten == 3:
            $ snape_SC.say("I organized a small party the other day...","24")
            $ snape_SC.say("One girl and three boys...")
            $ snape_SC.say("They fucked her and I watched...","snape_13")
            $ snape_SC.say(".........................","snape_29")
            $ snape_SC.say("You think I've been exercising my dark side a bit too often lately?","snape_05")
            $ snape_SC.say("","snape_06")
        elif one_of_ten == 4:
            $ snape_SC.say("I'm all out of condoms, mate.","24")
            $ snape_SC.say("You think you could hook me up?","snape_02")
            $ snape_SC.say("","snape_01")
        elif one_of_ten == 5:
            $ snape_SC.say("I am secretly making this special herbal brew that should make her tits lactate...","24")
            $ snape_SC.say("Pretty brilliant, huh?","snape_13")
            $ snape_SC.say("","23")
        elif one_of_ten == 6:
            $ snape_SC.say("So, this witch has my cock in her mouth, right?","24")
            $ snape_SC.say("Her hot girlfriend is cleaning my asshole with her tongue...","snape_02")
            $ snape_SC.say("Meanwhile this third girl is on her knees with her mouth open, waiting for me to spit in it...")
            $ snape_SC.say("And every time I spit, she says: \"Thank you, professor Snape\".")
            $ snape_SC.say("That was a bloody surreal evening...","snape_22")
            $ snape_SC.say("","snape_02")
        elif one_of_ten == 7:
            $ snape_SC.say("This one girl has been begging me to urinate in her mouth for days, now...","snape_06")
            $ snape_SC.say("Persistent little minx...")
            $ snape_SC.say("Should I give in?","snape_05")
            $ snape_SC.say("","23")
        elif one_of_ten == 8:
            $ snape_SC.say("I mercilessly dominate both male and female students...","snape_04")
            $ snape_SC.say("But in very different ways.","snape_22")
            $ snape_SC.say("","23")
        elif one_of_ten == 9:
            $ snape_SC.say("I love my life!","23")
            $ snape_SC.say("Still hate my job though...","snape_16")
            $ snape_SC.say("I wish I could skip all the teaching, but keep all the fucking.","snape_14")
            $ snape_SC.say("","23")
        elif one_of_ten == 10:
            $ snape_SC.say("I almost feel bad for having all the fun.","24")
            $ snape_SC.say("do You want me to send you up some young slut?","snape_14")
            $ snape_SC.say("","23")
    
    return
    
label chitchat_event_01: #Snape says: so you tutor her now?". Happens after tutoring unlocks.
    $ snape_SC.hideScreen()
    with d3
    ##############################################################################
    #########   JJ Edits   12/29/2014  ###########################################
    #    $ snape_SC.say_H("So...","head_1")
    #    $ snape_SC.say_H("I hear miss Granger is taking private lessons from you now?","head_1")
    #    m "Yeah, I suppose she does..."
    #    m "Not sure where this fits into our plan though."
    #    $ snape_SC.say_H("What do you mean? It fits perfectly.","head_9")
    #    $ snape_SC.say_H("I myself and a couple of other teacher are failing the crap out of that girl!","head_9")
    #    $ snape_SC.say_H("As a result she spends more time with studying...","head_9")
    #    $ snape_SC.say_H("Even taking private lessons now...","head_9")
    #    $ snape_SC.say_H("This way she has very little time left to be noisy and cause me headaches.","head_18")
    #    m "I see..."
    #    $ snape_SC.say_H("Yes, yes... just, you so know...","head_10")
    #    $ snape_SC.say_H("Don't actually teach her anything useful, alright?","head_10")
    #    m "I'll do my best."
    #    $ snape_SC.say_H("Well, if there is that's all...","head_1")
    ###  Altered this chit chat to reflect JJ's tutoring results  
    $ snape_SC.say_H("The Granger girl is driving me mad with her accusations.  They must stop!  I think she was even coming on to me!","head_1")
    $ snape_SC.say_H("As though I would fall for such a transparent ploy! Though she does look to have a luscious body under that frumpy sweater...","head_7")
    $ snape_SC.say_H("Have you done anything to deal with her?  If you have not...","head_4")
    $ snape_SC.say_H("I found a lovely potion in my cupboard that will put her into a long, wasting slumber for which there is no antidote.","head_9")
    m  "Don’t worry, Severus.  I have her well in hand."  
    $ snape_SC.say_H("Oh, really?  How?","head_10")
    m "Well, for starters she is seeing me for magic lessons.  I am teaching her how to do magic without wands or incantations."
    $ snape_SC.say_H("But that’s nearly impossible for someone of her age!  All but the most powerful wizards and witches must use wands.","head_17")
    $ snape_SC.say_H("And at her ability level she will need to verbalize all but the simplest spells.","head_2")
    m  "Not to worry.  I plan to teach her how I do magic and I don’t need to do any of that."
    $ snape_SC.say_H("That's ridiculous!  Your magic only works for you!","head_6")
    m "Exactly!"
    $ snape_SC.say_H("Oh, you are devious!  But you said for starters...","head_18")
    m "Are you familiar with a Professor Trelawney?"
    $ snape_SC.say_H("Sybil Trelawney?  That idiot?!?  Her so-called classes are a blot upon the school’s reputation!","head_15")
    $ snape_SC.say_H("She’s a laughing-stock among all of the other schools in Europe!","head_7")
    m "I see. It seems I’ve instructed Miss Granger to re-enroll in Trelawney’s Divination class during her usual study time."
    m "As it turns out, Miss Granger over the years has transferred her magical aura into her wand."
    m  "She is in desperate need of instruction on how to read magical auras."
    $ snape_SC.say_H("What rubbish is this?  Magical auras?  Transferring to a wand?  There's no such thing!","head_7")
    m "Ah, well, we must not disabuse Miss Granger of that notion, shall we?"
    m "She has lost the confidence that she can do much magic at all without her wand now."
    $ snape_SC.say_H("That's...despicable.  I wish I had thought of that.","head_8")
    m  "I’ve also asked that Trelawney person to have Miss Granger make up all the work she may have missed before and provide after-class tutoring."
    m  "I think it amounts to a couple of years of class work and of course less time to study in her other classes..."
    $ snape_SC.say_H("......................","head_8")
    $ snape_SC.say_H("That’s...that’s more brutal than I think I would have been.  And I hate the Granger bitch!","head_18")
    m  "Miss Granger is convinced that her troubles are because she has lost her innate magic aura.  I pointed out that the solution is simple.  "
    m  "To retrieve it she must masturbate with her wand several times per day.  This is where you can help."
    m  "You might want to let her know if you notice her aura is dwindling so she'll increase her efforts to regain it."
    $ snape_SC.say_H("...........................","head_18")
    $ snape_SC.say_H("Ah ha ha ha!  I am so very, very glad you are my ally and not my enemy.","head_15")
    m "That’s kind of you to say Severus."  
    $ snape_SC.say_H("I think I'll return to my office and think about how best to leverage this new information before my next class begins.","head_18")
    m "Good day, Severus."
    # End alteration  JJ
    
    hide screen bld1
    with d3
    
    hide screen snape_chibi_standing #Snape stands still.
    $ snape_SC.chibi.walk(500,750,3)
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.

    $ chitchat_event_01_happened = True #Activates next event - Event_15 Hermione sells her first favour.
    $ snape_busy = True
    $ days_without_an_event = 0
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    
    jump day_main_menu

    
    
    
    
