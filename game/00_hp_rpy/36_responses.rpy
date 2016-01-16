###MAP LOCATIONS AND RESPONSES
label map_attic: #Label controlling what happens when you access the attic
    if not attic_open:
        ">You venture up to the attic but find that the door locked"
        m "Damn, it's locked."
        m "Guess I'll have to ask Snape about a key."
        jump return_office
    if attic_open and tentacle_owned:
        ">You venture up to the attic and find an angry tentacle plant."
        m "Better get out of here before the plant remembers that I'm the one that cut it."
        ">You quickly return to your office."
        jump return_office
    else: #Scene where genie has to take a sample of the devil's snare plant
        ">You find your way through the winding staircases to the attic door."
        m "Hmmmmm, it seems to be open."
        ">You walk through the dusty room, light softly cascading though the windows."
        m "Well where's this magical plant?"
        ">A slender piece of vine is visible, skirting the room, as if to avoid the light."
        m "This must be it."
        ">You cut a piece and leave."
        ">As you shut the door you hear the room erupt in a series of loud crashes."
        $ tentacle_owned = True
        jump return_office


label map_forest: #Label controlling what happens when you go to the forest
    menu:
        "-Search the area-":
            if day_random >= 7:
                ">You search around the forest and manage to find an odd looking herb."
                m "This must be wormwood."
                menu: 
                    "-Take the wormwood-":
                        ">You gain 1 wormwood."
                        $ p_inv.append("Wormwood")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif day_random > 5:
                ">You search around the forest and manage to find an odd looking herb."
                m "This must be Knotgrass."
                menu: 
                    "-Take the Knotgrass-":
                        ">You gain 1 Knotgrass."
                        $ p_inv.append("Knotgrass")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the forest but find nothing of interest."
                jump return_office
   
label map_lake: #Label controlling what happens when you go to the lake
    menu:
        "-Search the area-":
            if day_random >= 7:
                ">You search around the lake and manage to find an slender, green vine."
                m "This must be Niffler's fancy."
                menu: 
                    "-Take the Niffler's fancy-":
                        ">You gain 1 Niffler's fancy."
                        $ p_inv.append("Niffler's fancy")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif day_random > 5:
                ">You search around the lake and manage to find an exposed root that looks similar to ginger."
                m "This must be Root of Aconite."
                menu: 
                    "-Take the Root of Aconite-":
                        ">You gain 1 Root of Aconite."
                        $ p_inv.append("Root of Aconite")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the lake but find nothing of interest."
                jump return_office  

label map_dorms: #Label controlling what happens when you go to the dorms
    menu:
        "-Search the area-":#Luna's Hair
            if day_random >= 7:
                ">You search around the dorms and manage to find a clump for bright orange fur."
                m "This must belong to some sort of animal."
                menu: 
                    "-Take the Fur-":
                        ">You gain 1 Cat Fur."
                        $ p_inv.append("Cat Hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            elif day_random > 5:
                ">You search around the dorms and manage to find an comb with some hair in it."
                m "This must be someones hair."
                menu: 
                    "-Take the hair-":
                        ">You gain 1 Luna's Hair."
                        $ p_inv.append("Luna's Hair")
                    "-Leave it-":
                        pass
                ">Finding nothing else of interest you return to your office."
                jump return_office
            else:
                ">You search around the dorms but find nothing of interest."
                jump return_office         
            
label map_pitch: #Label controlling what happens when you go to the quidditch pitch
    if pitch_open:
        hoo "Hello Professor Dumbledore, nice to see you out of your office today."
        hoo "What brings you down to the Quidditch pitch today?"
        m "Quidditch, what sort of name is that?" #put in low talking tone
        hoo "What was that?"
        m "Nothing, just commenting about the weather." #Maybe change this
        hoo "Well I'm glad that you're here. I wanted to have words with you about a problem that I'm having at the moment."
        m "What's wrong?"
        hoo "Attendance at quidditch matches has slowly been declining over the last couple of months."
        hoo "Students just don't seem to want to turn up to watch their teams play. It's affecting team morale."
        m "And how would you like to fix this?"
        hoo "Perhaps we could make attendance to the match mandatory."
        m "I don't think that that would work. If I did that you would just end up with a lot of disgruntled students booing your own team."
        m "If poor attendance is affecting morale I would hate to think what that would do to the players."
        hoo "Well then what do you suggest?"
        m "You need a way to attract and excite the crowd. To get the students here and to get them cheering."
        m "What you need is a cheerleading team."
        hoo "A what?"
        m "A team of girls to dance and cheer for their team. To get their fellow students brimming with enthusiasm."
        hoo "I'm not sure Sir, Hogwarts has always been a traditional school."
        hoo "Something like this goes in the face of that legacy."
        m "Well if you feel that way then I think you might just have to accept the declining number of students watching the game."
        hoo "Fine, but I'm not comfortable with a team of these \"\Cheerleaders\"\. At most I'd be comfortable with one girl dancing." #Maybe adjust this so that there is a team
        m "Well I think I have the perfect candidate. I'll send her over next practice session to try out."
        hoo "Okay, just make sure she's wearing something appropriate."
        $ pitch_first = False
        jump return_office
    else:
        ">You look around the open field but can't see any students or teachers"
        m "Mustn't be a practice day."
        jump return_office
            
label return_office:
    ">You return to your office."
    if daytime:
        jump day_main_menu
    else:
        jump night_main_menu


label maid_responses:
    $ payment = renpy.random.randint(10, 25)
    $ stockings = 1
    $ custom_outfit = 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3
    $ changeHermioneMainScreen(hg_pth+"body_01.png")
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "How was your day?"
                her "It was as normal a day of cleaning rooms could be."
                her "Although considering that I'm supposed to be in class during the day I guess it's not that normal."
                m "Don't worry [hermione_name], you'll get your points."
                m "Just think of how happy your friends will be when they win the house cup this year."
                her "I suppose..."
                m "10 points to Gryffindor"
                her "Thank you [genie_name]"
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                her "Do I really have to keep doing this?"
                m "What do you mean [hermione_name]?"
                her "It's so degrading. I have to clean other students rooms!"
                m "You can stop anytime."
                her "I can?"
                m "Certainly, I'll just get one of those Slytherin floosies that you are always on about."
                m "I'm sure that they'd jump at the chance to make some points for their house."
                m "They'd probably even do it for next to nothing, if not free."
                her "Fine, I get your point. It's just, surely there are other ways for you to earn money [genie_name]?"
                her "I mean you're the school headmaster, can't you just file some reports and get paid by the ministry?"
                m "I can, it's just not as enjoyable."
                her "Hmmph. Can I at least get my points now?"
                m "Certainly, 10 points to Gryffindor."
                her "Thank you [genie_name]."
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                if whoring >= 15:
                    her " "
                else:
                    "bla bla bla"
            elif day_random >=9:
                if whoring >= 15:
                    "bla bla bla"
                else:
                    her "I think you need to start enforcing harsher punishment for sexual harrasment."
                    her "Hmmph. Can I at least get my points now?"
                    m "Certainly, 10 points to Gryffindor."
                    her "Thank you [genie_name]."
                    $ gryffindor+= 10
                    $ gold += payment
        "-Dismiss her-":
            her "Here's your payment."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            her "Thank you [genie_name]."
            $ gryffindor+= 20
            $ gold += payment
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit = 0
    $ current_job = 0
    jump night_main_menu

label barmaid_responses:
    $ payment = renpy.random.randint(20, 50)
    $ stockings = 5
    $ custom_outfit = 5
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3
    $ changeHermioneMainScreen(hg_pth+"body_01.png")
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                her "Fine."
                m "Anything unusual happen?"
                her "Not really, I just served people drinks."
                m "Well in that case 10 points to Gryffindor."
                her "Thank you [genie_name], here's your payment."
                ">You receive [payment] gold coins."
                her "Good night [genie_name]."
                $ gryffindor+= 10
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                "bla bla bla"
                jump day_time_requests
            elif day_random >= 6 and day_random <= 8:
                "bla bla bla"
                jump day_time_requests
            elif day_random >=9:
                "bla bla bla"
                jump day_time_requests
        "-Dismiss her-":
            her "Here's your payment."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            her "Thank you [genie_name]."
            $ gryffindor+= 20
            $ gold += payment
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit = 0
    $ current_job = 0
    jump night_main_menu

label gryffindor_cheer_responses:
    $ payment = renpy.random.randint(40, 80)
    $ stockings = 2
    $ custom_outfit = 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3
    $ changeHermioneMainScreen(hg_pth+"body_01.png")
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "Hello, [hermione_name], how was your day?"
                $ changeHermioneMainScreen(hg_pth+"body_06.png")
                her "It was good [genie_name], I think that the team is really starting to liven up."
                m "How so?"
                $ changeHermioneMainScreen(hg_pth+"body_14.png")
                her "Well since I've started they seem to have improved their game."
                $ changeHermioneMainScreen(hg_pth+"body_45.png")
                her "They also seem much happier. Harry is always looking at me with a smile on his face."
                m "And does he look at you a lot?"
                $ changeHermioneMainScreen(hg_pth+"body_02.png")
                her "Of course he does, we're good friends."
                m "I'm sure that must be the reason."
                $ changeHermioneMainScreen(hg_pth+"body_06.png")
                her "Well here's the money [genie_name]"
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_74.png")
                her "Thank you [genie_name]."
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                m "Hello, [hermione_name], how was your day?"
                $ changeHermioneMainScreen(hg_pth+"body_11.png")
                her "Tiring. This cheering really is quite exhausting."
                m "Anything interesting happen?"
                $ changeHermioneMainScreen(hg_pth+"body_03.png")
                her "Not unless you count me almost dropping my pom pom."
                m "I don't. Well did they pay you?"
                $ changeHermioneMainScreen(hg_pth+"body_02.png")
                her "Of course, here you are [genie_name]"
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_74.png")
                her "Thank you [genie_name]."
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                m "Welcome back [hermione_name]."
                $ changeHermioneMainScreen(hg_pth+"body_14.png")
                her "Hello [genie_name]."
                m "How did you go today?"
                $ changeHermioneMainScreen(hg_pth+"body_31.png")
                her "Very well, all the boys said that I helped keep their spirits up."
                m "{size=-5}I'm sure that wasn't the only thing you kept up...{/size}"
                $ changeHermioneMainScreen(hg_pth+"body_08.png")
                her "What was that [genie_name]?"
                m "I was just saying that I'm sure you kept them entertained."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "I think so."
                m "Well did they pay you for raising their \"spirits\"?"
                $ changeHermioneMainScreen(hg_pth+"body_16.png")
                her "Of course they did."
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_74.png")
                her "Thank you [genie_name]."
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True or whoring <= 15:
                m "You seem very chipper today."
                $ changeHermioneMainScreen(hg_pth+"body_45.png")
                her "Of course I am, we won!"
                m "Won?"
                $ changeHermioneMainScreen(hg_pth+"body_75.png")
                her "We won! We beat Slytherin in a practice match."
                m "You seem a little over-excited for a practice match."
                $ changeHermioneMainScreen(hg_pth+"body_46.png")
                her "Well it was such a game. Not to mention that we got to rub it in those Slytherin faces afterwards."
                m "Well I'm glad that you are enjoying your work."
                $ changeHermioneMainScreen(hg_pth+"body_14.png")
                her "I am [genie_name]. Given that most of the \"work\" I do to help the house has to be kept private, it feels good to do something public for my house."
                m "Not to mention you get paid for it..."
                $ changeHermioneMainScreen(hg_pth+"body_13.png")
                her "Oh, right. Here you are."
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_74.png")
                her "Thank you [genie_name]."
            else:
                m "Welcome back [hermione_name], how was your day?"
                $ changeHermioneMainScreen(hg_pth+"body_45.png")
                her "We won! We managed to beat Slytherin."
                m "That must have been very exhilarating. I'm sure your cheering gave the motivation to win."
                $ changeHermioneMainScreen(hg_pth+"body_74.png")
                her "I think it did [genie_name]. They were all very excited to receive their reward for winning the game."
                menu:
                    "-Reward?-":
                        m "What reward did you promise them?"
                        $ changeHermioneMainScreen(hg_pth+"body_68.png")
                        her "Well I was so keen for us to beat Slytherin that I may have promised them that I would give them all blowjobs if they won."
                        m "You gave every team member a blowjob after the game?"
                        $ changeHermioneMainScreen(hg_pth+"body_64.png")
                        her "And the water boy..."
                        m "How did that even work? Did you just crawl around the room on your knees?"
                        $ changeHermioneMainScreen(hg_pth+"body_30.png")
                        her "Of course not, they all lined up and waited their turn."
                        m "They lined up? And then what?"
                        $ changeHermioneMainScreen(hg_pth+"body_29.png")
                        her "Well I sucked their cocks until they came and then I swallowed. Surely you of all people know how a blowjob works."
                        m "That's not quite what I meant."
                        $ changeHermioneMainScreen(hg_pth+"body_46.png")
                        her "Well I'm glad I did. I can't wait to rub it in Astoria's face tomorrow."
                        m "Well I'm glad you think it was worth it. Did they pay you?"

                        her "Of course they did [genie_name], here you are."
                    "-Okay-":
                        m "I'm sure they were. Did they pay you?"
                        her "Of course they did [genie_name], here you are."
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                her "Thank you [genie_name]."
        "-Dismiss her-":
            $ changeHermioneMainScreen(hg_pth+"body_13.png")
            her "Here's your payment [genie_name]."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            $ changeHermioneMainScreen(hg_pth+"body_74.png")
            her "Thank you [genie_name]."
            $ gryffindor+= 20
            $ gold += payment
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit = 0
    $ current_job = 0
    jump night_main_menu

label slytherin_cheer_responses:
    $ payment = renpy.random.randint(50, 100)
    $ stockings = 4
    $ custom_outfit = 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_chibi_xpos = 400 #Near the desk.
    show screen hermione_02 #Hermione stands still.
    show screen bld1
    with d3
    if day_random >=9 and lock_public_favors == False:
        $ uni_sperm = True 
        $ changeHermioneMainScreen(hg_pth+"body_78.png")
    else:
        $ changeHermioneMainScreen(hg_pth+"body_01.png")
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "How was your day today [hermione_name]?"
                $ changeHermioneMainScreen(hg_pth+"body_04.png")
                her "Exhausting. Those Slytherin pigs insisted that I cheer for their entire practice session."
                her "They were hardly playing the game by the end. They were just standing there watching me."
                m "Well what was your routine?"
                $ changeHermioneMainScreen(hg_pth+"body_09.png")
                her "Mostly star jumps while I cheered \"Go Slytherin!\"."
                m "So you were just jumping up and down? That doesn't seem like a very intricate cheer."
                $ changeHermioneMainScreen(hg_pth+"body_69.png")
                her "It isn't but it's what they insisted I do."
                m "Well it definitely sounds like you earned your points."
                m "30 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_16.png")
                her "Thank you [genie_name], here's your payment."
                ">You receive [payment] gold coins."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 3 and day_random <= 5:
                m "How was your day today [hermione_name]?"
                $ changeHermioneMainScreen(hg_pth+"body_08.png")
                her "Uneventful. I completed my routine and then went back to my room."
                m "You didn't talk to anyone?"
                $ changeHermioneMainScreen(hg_pth+"body_12.png")
                her "I make a point of trying to avoid Slytherin student as best I can. "
                m "Are they really that unbearable."
                $ changeHermioneMainScreen(hg_pth+"body_04.png")
                her "Yes."
                m "Well, you earned your points."
                m "30 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_16.png")
                her "Thank you [genie_name], here's your payment."
                ">You receive [payment] gold coins."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 6 and day_random <= 8:
                m "Hello [hermione_name]."
                $ changeHermioneMainScreen(hg_pth+"body_03.png")
                her "Hello [genie_name]."
                m "How did you go today?"
                $ changeHermioneMainScreen(hg_pth+"body_29.png")
                her "Very well. In fact I think I might be doing too well."
                m "How so?"
                $ changeHermioneMainScreen(hg_pth+"body_11.png")
                her "I think that my cheering is having too positive an effect."
                $ changeHermioneMainScreen(hg_pth+"body_10.png")
                her "I'm not sure that I want the Slytherin team to improve, let alone because of me."
                m "Just think about how your helping your house in other ways."
                $ changeHermioneMainScreen(hg_pth+"body_02.png")
                her "I suppose your right [genie_name]."
                m "Of course I am, now did they pay you?"
                $ changeHermioneMainScreen(hg_pth+"body_06.png")
                her "Yes [genie_name]."
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_74.png")
                her "Thank you [genie_name]."
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True:
                $ changeHermioneMainScreen(hg_pth+"body_04.png")
                her "[genie_name], something must be done about these Slytherin boys."
                $ changeHermioneMainScreen(hg_pth+"body_12.png")
                her "It's bad enough that I have to cheer for them but they are starting to become a little touchy."
                m "Touchy?"
                $ changeHermioneMainScreen(hg_pth+"body_30.png")
                her "Yes, they keep groping me. It's highly inappropriate and it interrupts my routine."
                m "You keep dancing while they grope you?"
                $ changeHermioneMainScreen(hg_pth+"body_04.png")
                her "Of course, I'm there to complete a job. I won't fail at this just because of a few boys."
                m "Well what would you have me do?"
                $ changeHermioneMainScreen(hg_pth+"body_05.png")
                her "Speak to Professor Snape, tell him to chastise them. They'll listen to him."
                m "Very well, I'll speak to him. I'm not sure it will have the effect your hoping for."
                $ changeHermioneMainScreen(hg_pth+"body_07.png")
                her "It better, otherwise I wont put my full effort into the routine."
                m "{size=-5}I'm sure that'll show them.{/size}"
                $ changeHermioneMainScreen(hg_pth+"body_08.png")
                her "What was that [genie_name]?"
                m "Nothing [hermione_name], I was just saying I'll speak to Professor Snape tonight."
                $ changeHermioneMainScreen(hg_pth+"body_12.png")
                her "Thank you [genie_name], here's your payment."
                ">You receive [payment] gold coins."
                $ gold += payment
                m "Well done [hermione_name], 30 points to Gryffindor."
                $ changeHermioneMainScreen(hg_pth+"body_16.png")
                her "Thank you [genie_name]."
                $ gryffindor+= 30
            else:#Comes back with cum on her
                m "What the hell happened to you?"
                $ changeHermioneMainScreen(hg_pth+"body_118.png")
                her "I did my job [genie_name]."
                m "What are you talking about? You were supposed to be a cheerleader."
                $ changeHermioneMainScreen(hg_pth+"body_121.png")
                her "I am [genie_name]. I just performed a different type of cheer today."
                m "And that cheer included jerking off the entire Slytherin team?"
                $ changeHermioneMainScreen(hg_pth+"body_118.png")
                her "Well that's not how it started. I was initially just giving them a bit of a dance in the locker room."
                her "And one thing led to another..."
                m "Fine, I don't want to hear it. How much did they pay you for this \"cheering\"?"
                $ changeHermioneMainScreen(hg_pth+"body_133.png")
                her "Pay me?"
                m "You are supposed to be paid for this [hermione_name]."
                $ changeHermioneMainScreen(hg_pth+"body_188.png")
                her "Oh... I must have forgotten. Sorry [genie_name]"
                m "Fine, but you aren't getting any points."
                $ changeHermioneMainScreen(hg_pth+"body_01.png")
                her "Of course not [genie_name]. Will that be all?"
                m "Yes, you can go now."
                $ changeHermioneMainScreen(hg_pth+"body_128.png")
                her "Thank you [genie_name]."
        "-Dismiss her-":
            $ changeHermioneMainScreen(hg_pth+"body_02.png")
            her "Here's your payment."
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 30 points to Gryffindor."
            $ changeHermioneMainScreen(hg_pth+"body_128.png")
            her "Thank you [genie_name]."
            $ gryffindor+= 30
            $ gold += payment
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit = 0
    $ current_job = 0
    $ uni_sperm = False 
    jump night_main_menu


label job_1:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ current_job = 1
    jump day_main_menu

label job_2:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ current_job = 2
    jump day_main_menu
label job_3:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ current_job = 3
    jump day_main_menu
label job_4:
    $ menu_x = 0.5 #Menu position is back to default. (Center).
    $ hermione_takes_classes = True
    if whoring <= 6:
        her "*Humph!*..."
    elif whoring >=7 and whoring <= 15:
        her "Yes [genie_name]..."
    else:
        her "As you wish [genie_name]."
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_02
    hide screen ctc
    with d3
    $ current_job = 4
    jump day_main_menu























        