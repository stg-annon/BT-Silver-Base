init python:
    class hermione_job(object):
        inProgress = False
        responses = ""
        
        def checkProgress(self):
            if self.inProgress:
                renpy.jump(self.responses)


###MAP LOCATIONS AND RESPONSES
# TODO: change how "random" chance works for getting items from locations or immplement a 
# limit to searching an area b/c currenly if day_random is above a vlaue the player can get
# as many items as they want
label map_attic: #Label controlling what happens when you access the attic
    if not attic_open:
        ">You venture up to the attic but find that the door is locked."
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
                        $ potion_inv.add("ing_wormwood")
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
                        $ potion_inv.add("ing_knotgrass")
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
                        $ potion_inv.add("ing_niffler_fancy")
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
                        $ potion_inv.add("ing_aconite_root")
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
                        $ potion_inv.add("ing_cat_hair")
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
                        $ potion_inv.add("ing_luna_hair")
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
    $ hermione_SC.outfitFromList("Maid")
    $ stockings = 1
    $ custom_outfit_old = 1
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    call her_main("","body_01")
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
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit_old = 0
    $ current_job = 0
    jump night_main_menu

label barmaid_responses:
    $ payment = renpy.random.randint(20, 50)
    $ stockings = 5
    $ custom_outfit_old = 5
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    call her_main("","body_01")
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
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit_old = 0
    $ current_job = 0
    jump night_main_menu

label gryffindor_cheer_responses:
    $ payment = renpy.random.randint(40, 80)
    $ stockings = 2
    $ custom_outfit_old = 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    call her_main("","body_01")
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "Hello, [hermione_name], how was your day?"
                call her_main("It was good [genie_name], I think that the team is really starting to liven up.","body_06")
                m "How so?"
                call her_main("Well since I've started they seem to have improved their game.","body_14")
                call her_main("They also seem much happier. Harry is always looking at me with a smile on his face.","body_45")
                m "And does he look at you a lot?"
                call her_main("Of course he does, we're good friends.","body_02")
                m "I'm sure that must be the reason."
                call her_main("Well here's the money, [genie_name].","body_06")
                ">You receive [payment] gold coins."
                m "Well done, [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","body_74")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 3 and day_random <= 5:
                m "Hello, [hermione_name], how was your day?"
                call her_main("Tiring. This cheering really is quite exhausting.","body_11")
                m "Anything interesting happen?"
                call her_main("Not unless you count me almost dropping my pom pom.","body_03")
                m "I don't. Well did they pay you?"
                call her_main("Of course, here you are [genie_name]","body_02")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","body_74")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >= 6 and day_random <= 8:
                m "Welcome back [hermione_name]."
                call her_main("Hello [genie_name].","body_14")
                m "How did you go today?"
                call her_main("Very well, all the boys said that I helped keep their spirits up.","body_31")
                m "{size=-5}I'm sure that wasn't the only thing you kept up...{/size}"
                call her_main("What was that [genie_name]?","body_08")
                m "I was just saying that I'm sure you kept them entertained."
                call her_main("I think so.","body_10")
                m "Well did they pay you for raising their \"spirits\"?"
                call her_main("Of course they did.","body_16")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","body_74")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True or whoring <= 15:
                m "You seem very chipper today."
                call her_main("Of course I am, we won!","body_45")
                m "Won?"
                call her_main("We won! We beat Slytherin in a practice match.","body_75")
                m "You seem a little over-excited for a practice match."
                call her_main("Well it was such a game. Not to mention that we got to rub it in those Slytherin faces afterwards.","body_46")
                m "Well I'm glad that you are enjoying your work."
                call her_main("I am [genie_name]. Given that most of the \"work\" I do to help the house has to be kept private, it feels good to do something public for my house.","body_14")
                m "Not to mention you get paid for it..."
                call her_main("Oh, right. Here you are.","body_13")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","body_74")
            else:
                m "Welcome back [hermione_name], how was your day?"
                call her_main("We won! We managed to beat Slytherin.","body_45")
                m "That must have been very exhilarating. I'm sure your cheering gave the motivation to win."
                call her_main("I think it did [genie_name]. They were all very excited to receive their reward for winning the game.","body_74")
                menu:
                    "-Reward?-":
                        m "What reward did you promise them?"
                        call her_main("Well I was so keen for us to beat Slytherin that I may have promised them that I would give them all blowjobs if they won.","body_68")
                        m "You gave every team member a blowjob after the game?"
                        call her_main("And the water boy...","body_64")
                        m "How did that even work? Did you just crawl around the room on your knees?"
                        call her_main("Of course not, they all lined up and waited their turn.","body_30")
                        m "They lined up? And then what?"
                        call her_main("Well I sucked their cocks until they came and then I swallowed. Surely you of all people know how a blowjob works.","body_29")
                        m "That's not quite what I meant."
                        call her_main("Well I'm glad I did. I can't wait to rub it in Astoria's face tomorrow.","body_46")
                        m "Well I'm glad you think it was worth it. Did they pay you?"

                        her "Of course they did [genie_name], here you are."
                    "-Okay-":
                        m "I'm sure they were. Did they pay you?"
                        her "Of course they did [genie_name], here you are."
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                her "Thank you [genie_name]."
        "-Dismiss her-":
            call her_main("Here's your payment [genie_name].","body_13")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 20 points to Gryffindor."
            call her_main("Thank you [genie_name].","body_74")
            $ gryffindor+= 20
            $ gold += payment
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit_old = 0
    $ current_job = 0
    jump night_main_menu

label slytherin_cheer_responses:
    $ payment = renpy.random.randint(50, 100)
    $ stockings = 4
    $ custom_outfit_old = 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    $ hermione_SC.chibi.xpos = 400 #Near the desk.
    show screen hermione_blink #Hermione stands still.
    show screen bld1
    with d3
    if day_random >=9 and lock_public_favors == False:
        $ uni_sperm = True 
        call her_main("","body_78")
    else:
        call her_main("","body_01")
    menu:
        "-Ask her how her day was-":
            if day_random <= 2:
                m "How was your day today [hermione_name]?"
                call her_main("Exhausting. Those Slytherin pigs insisted that I cheer for their entire practice session.","body_04")
                her "They were hardly playing the game by the end. They were just standing there watching me."
                m "Well what was your routine?"
                call her_main("Mostly star jumps while I cheered \"Go Slytherin!\".","body_09")
                m "So you were just jumping up and down? That doesn't seem like a very intricate cheer."
                call her_main("It isn't but it's what they insisted I do.","body_69")
                m "Well it definitely sounds like you earned your points."
                m "30 points to Gryffindor."
                call her_main("Thank you [genie_name], here's your payment.","body_16")
                ">You receive [payment] gold coins."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 3 and day_random <= 5:
                m "How was your day today [hermione_name]?"
                call her_main("Uneventful. I completed my routine and then went back to my room.","body_08")
                m "You didn't talk to anyone?"
                call her_main("I make a point of trying to avoid Slytherin student as best I can. ","body_12")
                m "Are they really that unbearable."
                call her_main("Yes.","body_04")
                m "Well, you earned your points."
                m "30 points to Gryffindor."
                call her_main("Thank you [genie_name], here's your payment.","body_16")
                ">You receive [payment] gold coins."
                $ gold += payment
                $ gryffindor+= 30
            elif day_random >= 6 and day_random <= 8:
                m "Hello [hermione_name]."
                call her_main("Hello [genie_name].","body_03")
                m "How did you go today?"
                call her_main("Very well. In fact I think I might be doing too well.","body_29")
                m "How so?"
                call her_main("I think that my cheering is having too positive an effect.","body_11")
                call her_main("I'm not sure that I want the Slytherin team to improve, let alone because of me.","body_10")
                m "Just think about how your helping your house in other ways."
                call her_main("I suppose your right [genie_name].","body_02")
                m "Of course I am, now did they pay you?"
                call her_main("Yes [genie_name].","body_06")
                ">You receive [payment] gold coins."
                m "Well done [hermione_name], 20 points to Gryffindor."
                call her_main("Thank you [genie_name].","body_74")
                $ gryffindor+= 20
                $ gold += payment
            elif day_random >=9 and lock_public_favors == True:
                call her_main("[genie_name], something must be done about these Slytherin boys.","body_04")
                call her_main("It's bad enough that I have to cheer for them but they are starting to become a little touchy.","body_12")
                m "Touchy?"
                call her_main("Yes, they keep groping me. It's highly inappropriate and it interrupts my routine.","body_30")
                m "You keep dancing while they grope you?"
                call her_main("Of course, I'm there to complete a job. I won't fail at this just because of a few boys.","body_04")
                m "Well what would you have me do?"
                call her_main("Speak to Professor Snape, tell him to chastise them. They'll listen to him.","body_05")
                m "Very well, I'll speak to him. I'm not sure it will have the effect your hoping for."
                call her_main("It better, otherwise I wont put my full effort into the routine.","body_07")
                m "{size=-5}I'm sure that'll show them.{/size}"
                call her_main("What was that [genie_name]?","body_08")
                m "Nothing [hermione_name], I was just saying I'll speak to Professor Snape tonight."
                call her_main("Thank you [genie_name], here's your payment.","body_12")
                ">You receive [payment] gold coins."
                $ gold += payment
                m "Well done [hermione_name], 30 points to Gryffindor."
                call her_main("Thank you [genie_name].","body_16")
                $ gryffindor+= 30
            else:#Comes back with cum on her
                m "What the hell happened to you?"
                call her_main("I did my job [genie_name].","body_118")
                m "What are you talking about? You were supposed to be a cheerleader."
                call her_main("I am [genie_name]. I just performed a different type of cheer today.","body_121")
                m "And that cheer included jerking off the entire Slytherin team?"
                call her_main("Well that's not how it started. I was initially just giving them a bit of a dance in the locker room.","body_118")
                her "And one thing led to another..."
                m "Fine, I don't want to hear it. How much did they pay you for this \"cheering\"?"
                call her_main("Pay me?","body_133")
                m "You are supposed to be paid for this [hermione_name]."
                call her_main("Oh... I must have forgotten. Sorry [genie_name]","body_188")
                m "Fine, but you aren't getting any points."
                call her_main("Of course not [genie_name]. Will that be all?","body_01")
                m "Yes, you can go now."
                call her_main("Thank you [genie_name].","body_128")
        "-Dismiss her-":
            call her_main("Here's your payment.","body_02")
            ">You receive [payment] gold coins."
            m "Well done [hermione_name], 30 points to Gryffindor."
            call her_main("Thank you [genie_name].","body_128")
            $ gryffindor+= 30
            $ gold += payment
    hide screen bld1
    hide screen hermione_main
    hide screen blktone 
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ hermione_sleeping = True
    $ stockings = 0
    $ custom_outfit_old = 0
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
    hide screen hermione_blink
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
    hide screen hermione_blink
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
    hide screen hermione_blink
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
    hide screen hermione_blink
    hide screen ctc
    with d3
    $ current_job = 4
    jump day_main_menu























        
