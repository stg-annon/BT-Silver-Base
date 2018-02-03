
init python:

    class main_quest(object):
        id = 0
        name = ""
        objective = ""
        hint_text = ""
        hint_text2 = ""
        hint_text3 = ""
        hint_text4 = ""
        hint_text5 = ""
        full_text = ""
        full_text2 = ""
        full_text3 = ""
        full_text4 = ""
        full_text5 = ""
        started = 0
        completed = False

    class side_quest(object):
        id = 0
        name = ""
        objective = ""
        hint_text = ""
        hint_text2 = ""
        hint_text3 = ""
        hint_text4 = ""
        hint_text5 = ""
        full_text = ""
        full_text2 = ""
        full_text3 = ""
        full_text4 = ""
        full_text5 = ""
        started = 0
        completed = False

label __init_variables:

    #Guide
    if not hasattr(renpy.store,'guide_active'): #important!
        $ guide_active = False
    if not hasattr(renpy.store,'guide_page'): #important!
        $ guide_page = 0
    if not hasattr(renpy.store,'guide_show_hint'): #important!
        $ guide_show_hint = False
    if not hasattr(renpy.store,'guide_show_next_step'): #important!
        $ guide_show_next_step = False
    if not hasattr(renpy.store,'guide_add_tip'): #important!
        $ guide_add_tip = False

    #Main Quests

    if not hasattr(renpy.store,'mQuest_0'): #important!
        $ mQuest_0 = main_quest()
    $ mQuest_0.id = 0
    $ mQuest_0.name = ""
    $ mQuest_0.objective = "No more quests have been added yet."
    $ mQuest_0.hint_text = "You are on your own for now. Good luck!"
    $ mQuest_0.hint_text2 = ""
    $ mQuest_0.hint_text3 = ""
    $ mQuest_0.hint_text4 = ""
    $ mQuest_0.hint_text5 = ""
    $ mQuest_0.full_text = "You are on your own for now. Good luck!"
    $ mQuest_0.full_text2 = ""
    $ mQuest_0.full_text3 = ""
    $ mQuest_0.full_text4 = ""
    $ mQuest_0.full_text5 = ""

    if not hasattr(renpy.store,'mQuest_A'): #important!
        $ mQuest_A = main_quest()
    $ mQuest_A.id = 1
    $ mQuest_A.name = "The Beginning"
    $ mQuest_A.objective = "Find a way to return home!"
    $ mQuest_A.hint_text = ""
    $ mQuest_A.hint_text2 = ""
    $ mQuest_A.hint_text3 = ""
    $ mQuest_A.hint_text4 = ""
    $ mQuest_A.hint_text5 = ""
    $ mQuest_A.full_text = ""
    $ mQuest_A.full_text2 = ""
    $ mQuest_A.full_text3 = ""
    $ mQuest_A.full_text4 = ""
    $ mQuest_A.full_text5 = ""
    $ mQuest_A.started = 0 #counter
    $ mQuest_A.completed = False
        
    if not hasattr(renpy.store,'mQuest_B'): #important!
        $ mQuest_B = main_quest()
    $ mQuest_B.id = 2
    $ mQuest_B.name = "The Lion and the Serpent"
    $ mQuest_B.objective = "Find a way to cope with your boredom."
    $ mQuest_B.hint_text = ""
    $ mQuest_B.hint_text2 = ""
    $ mQuest_B.hint_text3 = ""
    $ mQuest_B.hint_text4 = ""
    $ mQuest_B.hint_text5 = ""
    $ mQuest_B.full_text = ""
    $ mQuest_B.full_text2 = ""
    $ mQuest_B.full_text3 = ""
    $ mQuest_B.full_text4 = ""
    $ mQuest_B.full_text5 = ""
    $ mQuest_B.started = 0 #counter
    $ mQuest_B.completed = False


    #Side Quests

    if not hasattr(renpy.store,'sQuest_get_map'): #important!
        $ sQuest_get_map = side_quest()
    $ sQuest_get_map.id = 0
    $ sQuest_get_map.name = "The Marauder's Map"
    $ sQuest_get_map.objective = "Find a map and use it."
    $ sQuest_get_map.hint_text = "Test 1"
    $ sQuest_get_map.full_text = "Test 2"
    $ sQuest_get_map.started = 0
    $ sQuest_get_map.completed = False

    if not hasattr(renpy.store,'sQuest_buy_at_shop'): #important!
        $ sQuest_buy_at_shop = side_quest()
    $ sQuest_buy_at_shop.id = 1
    $ sQuest_buy_at_shop.name = "Weasley’s Wizard Wheezes"
    $ sQuest_buy_at_shop.objective = "Buy an item from the store."
    $ sQuest_buy_at_shop.hint_text = ""
    $ sQuest_buy_at_shop.full_text = ""
    $ sQuest_buy_at_shop.started = 0
    $ sQuest_buy_at_shop.completed = False


    if not hasattr(renpy.store,'current_main_quest'): #important!
        $ current_main_quest = mQuest_0
    if not hasattr(renpy.store,'current_side_quests'): #important!
        $ current_side_quests = []

    #Quest Rewards
    if not hasattr(renpy.store,'quest_reward_image'): #important!
        $ quest_reward_image = "/01_hp/18_store/01.png" #default image is the gift box
    if not hasattr(renpy.store,'quest_reward_text'): #important!
        $ quest_reward_text = ""

    #Tips and Facts
    if not hasattr(renpy.store,'daily_rndm_tip_or_fact'): #important!
        $ daily_rndm_tip_or_fact = 0
    if not hasattr(renpy.store,'guide_tip_text'): #important!
        $ guide_tip_text = ""
    if not hasattr(renpy.store,'guide_tip_text2'): #important!
        $ guide_tip_text2 = ""
    if not hasattr(renpy.store,'guide_tip_text3'): #important!
        $ guide_tip_text3 = ""
    if not hasattr(renpy.store,'guide_tip_text4'): #important!
        $ guide_tip_text4 = ""

    return

### Quest System ###

#Play Intro
#Skip Intro
### Start of Game ###
### Activate Quest Guide and Icon after Dialogue ###

label update_quests:

    #Side Quests
    $ side_quests = [] #list of your side quests

    #Get Marauder's Map
    if sQuest_get_map.started >=1 and sQuest_get_map.started <= 3 and sQuest_get_map not in side_quests:
        $ side_quests.append(sQuest_get_map)

    #Buy something at the shop
    if sQuest_buy_at_shop.started >=1 and sQuest_buy_at_shop.started <= 3 and sQuest_buy_at_shop not in side_quests:
        $ side_quests.append(sQuest_buy_at_shop)


    #Main Quest A #Start of game till Snape unlock
    if mQuest_A.started >= 1 and mQuest_A.started <=6: #7=.completed
        $ current_main_quest = mQuest_A

    if mQuest_A.started == 1: #Examine room
        $ mQuest_A.hint_text = "Why don't you have a look around!"
        $ mQuest_A.full_text = "Examine the room!"
        $ mQuest_A.full_text2 = "Interact with everything you see!"
    if mQuest_A.started == 2: #Read owl's letter. Snape enters room
        # if looked at door: Side quest map activates here!
        $ mQuest_A.hint_text = "What's that weird looking bird?"
        $ mQuest_A.full_text = "Click on the owl and read the letter!"
        $ mQuest_A.full_text2 = ""
        $ mQuest_A.full_text3 = "Right after that, Snape will appear."
        $ mQuest_A.full_text4 = "Talk to him! - Pick any Dialogue Choice!"
    if mQuest_A.started == 3: #Skip to night
        #rummaging through cupboard unlocked!
        # if clicked on cupboard. Add quest "" #get healing potions
        $ mQuest_A.hint_text = "Time for a nap!"
        $ mQuest_A.full_text = "Click on your desk and take a nap!"
        $ mQuest_A.full_text2 = "Snape will appear the next morning!"
        $ mQuest_A.full_text3 = "Talk to him! - Pick any Dialogue Choice!"
    if mQuest_A.started == 4: #Read owl's 2nd letter
        $ mQuest_A.hint_text = "Don't they know what an email is?"
        $ mQuest_A.full_text = "Read the owl's letter!"
    if mQuest_A.started == 5: #Get healing potions
        $ mQuest_A.hint_text = "Have you looked through your cupboard lately?"
        $ mQuest_A.full_text = "Get three potions from your cupboard!"
        $ mQuest_A.full_text2 = "You will need them later!"
    if mQuest_A.started == 6: # Duel # ADD custom duel guide screen
        $ mQuest_A.hint_text = "He's Attacking you!"
        $ mQuest_A.hint_text2 = "No big deal right!"
        $ mQuest_A.hint_text3 = "He only has that small wooden stick to fight!"
        $ mQuest_A.hint_text3 = "You can easily beat him!"
        $ mQuest_A.full_text = "Beat Snape!"
        $ mQuest_A.full_text2 = "Attack him when his guard is low!"
        $ mQuest_A.full_text3 = "Defend when he's about to attack!"
    #end of quest. #Change in 18_events.rpy

    #Main Quest B #Till Hermione unlock
    if mQuest_B.started >= 1 and mQuest_B.started <=5: #6=.completed
        $ current_main_quest = mQuest_B
        $ mQuest_A.completed = True

    if mQuest_B.started == 1: #wait for Hermione
        $ mQuest_B.hint_text = "Better get comfortable here. Not like you are able to leave anytime soon."
        $ mQuest_B.full_text = "Wait a couple of days until Hermione shows up! Then talk with Hermione and pick any Dialogue Choice!"
    if mQuest_B.started == 2: #Hang with Snape
        #Side quests map could complete here. Rummage through cupboard.
        $ mQuest_B.hint_text = "Maybe Snape knows what's up with that girl?"
        $ mQuest_B.full_text = "Hang out with Snape during the evening and discuss your newest acquaintances with him! The next day Hermione will knock on your door! Invite her in or send her away. You will have to talk to her eventually! There's no way around it!"
    if mQuest_B.started == 3: #Hermione knocks on door #If send her away, else skip to 4
        $ mQuest_B.hint_text = "Knock Knock!"
        $ mQuest_B.full_text = "Invite her in or send her away. You will have to talk to her eventually! There's no way around it!"
    if mQuest_B.started == 4: #Hang with Snape
        $ mQuest_B.hint_text = "Snape? Snape?! SNAAAAPE!"
        $ mQuest_B.full_text = "Hang out with Snape during the evening and have another conversation!"
    if mQuest_B.started == 5: #Wait for Hermione
        $ mQuest_B.hint_text = "Watch your evil plan get set into motion!"
        $ mQuest_B.full_text = "Wait for Hermione! - Talk to her until she's willing to be tutored by you!"

    #Call Reward
    if mQuest_A.started == 7 and not mQuest_A.completed:
        $ mQuest_A.completed = True #makes sure reward screen only happens once
        $ quest_reward_image = "/01_hp/18_store/01.png" #My game crashed if there wasn't a reward image to display
        $ quest_reward_text = ">You've unlocked the ability to summon Severus Snape to your office."
        $ the_gift = quest_reward_image #Again, if I had no gift set, my game crashed
        call give_quest_reward
    if mQuest_B.started == 6 and not mQuest_B.completed:
        $ mQuest_B.completed = True
        $ quest_reward_image = "/01_hp/18_store/01.png" #My game crashed if there wasn't a reward image to display
        $ quest_reward_text = ">You've unlocked the ability to summon Hermione to your office."
        $ the_gift = quest_reward_image #Again, if I had no gift set, my game crashed
        call give_quest_reward

    else:
        pass
    #end of quest.
    #hide star icon and call main_quest_reward = ability to summon Hermione

    return






#Start: There is a star icon at the top left corner of the screen. This is will open the player guide. 
#It will help you progress through the game, give you helpful tips, or even tell you what to do next entirely.

#28.gifts.rpy
#candy:          lvl 1-7= +5
#chocolate:      lvl 1-7= +10
#plush owl:      lvl 1-2= +7,  3-4= +10, 5-6= +15, 7+= +4
#butterbeer:     lvl 1-2= +3,  3-4= +10, 5-6= +15, 7+= 20
#edu-mags:       lvl 1-2= +15, 3-4= +10, 5-6= +3,  7+= +0
#girl-mags:      lvl 1-2= +0,  3-4= +5,  5-6= +15, 7+= +15
#adult-mags:     lvl 1-2= -7,  3-4= -3,  5-6= +8,  7+= +15
#porn-mags:      lvl 1-2= -15, 3-4= -8,  5-6= +0,  7+= +15
#krum poster:    lvl 1-2= +0,  3-4= +4,  5-6= +15, 7+= +25
#lingerie:       lvl 1-2= -10, 3-4= +0,  5-6= +7,  7+= +15
#condoms:        lvl 1-2= -6,  3-4= +0,  5-6= +3,  7+= +4
#vibrator:       lvl 1-2= -10, 3-4= -10, 5-6= +0,  7+= +10
#anal lube:      lvl 1-2= -6,  3-4= -2,  5-6= +0,  7+= +5
#gag and cuffs:  lvl 1-2= -10, 3-4= -5,  5-6= +9,  7+= +15
#anal plugs:     lvl 1-2= +8,  3-4= -15, 5-6= +0,  7+= +10
#strap on:       lvl 1-2= +20, 3-4= -15, 5-6= +10, 7+= +30
#speed stick:    lvl 1-2= +20, 3-4= +20, 5-6= +30, 7+= +30
#sex doll:       lvl 1-2= -20, 3-4= -20, 5-6= +10, 7+= +30
#ADD:            lvl 1-2= ,  3-4= ,  5-6= ,  7+= 

### Run label every time before guide gets opened. ###
### Tip of the day ###

label update_tip_of_the_day:

    #Reset Text
    $ guide_tip_text = ""
    $ guide_tip_text2 = ""
    $ guide_tip_text3 = ""
    $ guide_tip_text4 = ""

    #Gift Items Tip
    if mad > 0: #Picks this first when she is mad.

        #Always relevant
        $ rndm_one_of_ten = renpy.random.randint(1, 10)

        if rndm_one_of_ten ==  1: #Broom
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "A new broom is always a great gift!"
            $ guide_tip_text2 = "Buy one at the shop for the cheap price of"
            $ guide_tip_text3 = "only 500g!"
            $ guide_tip_text4 = "Get it now! Get it! GET IT!"
        if rndm_one_of_ten ==  2: #Condoms, Anal Lube
            $ guide_add_tip = False #False=Fact                             #Max Characters
            $ guide_tip_text = "Condoms might not be the best gift for a"
            $ guide_tip_text2 = "young girl..."
            $ guide_tip_text3 = "Neither is anal lube!"
        if rndm_one_of_ten ==  3: #Butterbeer
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Seems like Hermione is mad at you!"
            $ guide_tip_text2 = "Gift her some butterbeer!"
            $ guide_tip_text3 = "Everybody loves butterbeer!"
        if rndm_one_of_ten ==  4: #Candy
            $ guide_add_tip = True                                          #Max Characters
            $ guide_tip_text = "Seems like Hermione is mad at you!"
            $ guide_tip_text2 = "Give her a lollipop to better her mood!"
            $ guide_tip_text3 = "You can also watch her lick it!"
        if rndm_one_of_ten ==  5: #Chocolate
            $ guide_add_tip = True                                          #Max Characters                                          
            $ guide_tip_text = "Seems like Hermione is mad at you!"
            $ guide_tip_text2 = "Why not give her some chocolate to better"
            $ guide_tip_text3 = "better her mood!"

        #whoring specific gifts
        if rndm_one_of_ten >= 6 and rndm_one_of_ten <= 10:
            if whoring >= 0 and whoring <= 5:  #lvl 1-2    
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Why not buy her a strap-on?"
                    $ guide_tip_text2 = "What could possibly go wrong!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Hermione seems to be quite fond of"
                    $ guide_tip_text2 = "educational magazines!"
                    $ guide_tip_text3 = "No not sexual-education..."
                    $ guide_tip_text4 = "Yes the boring looking ones!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Seems like Hermione is mad at you!"
                    $ guide_tip_text2 = "Maybe she'd like a gift?"
                    $ guide_tip_text3 = "Just... don't buy her a sex-doll!"

            if whoring >= 6 and whoring <= 11: #lvl 3-4
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "A girl like Hermione might be into plush"
                    $ guide_tip_text2 = "animals!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "Have you heard of Viktor Krum?"
                    $ guide_tip_text2 = "All the witches love him!"
                    $ guide_tip_text3 = "Maybe Hermione would like a poster of him!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True                                          #Max Characters
                    $ guide_tip_text = "She still prefers her educational magazines,"
                    $ guide_tip_text2 = "but maybe you can get her interested in"
                    $ guide_tip_text3 = "the ones specific for girls!"

            if whoring >= 12 and whoring <= 17: #lvl 5-6
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = True
                    $ guide_tip_text = "Apparently they released a new set of"
                    $ guide_tip_text2 = "new and exclusive plush owls!"
                    $ guide_tip_text3 = "Gotta catch 'em all!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True
                    $ guide_tip_text = "She really seems to like this Krum guy!"
                    $ guide_tip_text2 = "Maybe you should buy her a poster of him!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True
                    $ guide_tip_text = "One might think Hermione has grown"
                    $ guide_tip_text2 = "interested in sex-toys by now!"

            if whoring >= 18 and whoring <= 23: #7
                $ rndm_one_of_three = renpy.random.randint(1, 3)
                if rndm_one_of_three == 1:
                    $ guide_add_tip = False #False=Fact
                    $ guide_tip_text = "Educational Magazines? Fuck that shit!"
                    $ guide_tip_text2 = "Who needs those!"
                elif rndm_one_of_three == 2:
                    $ guide_add_tip = True
                    $ guide_tip_text = "I have heard there is a new Krum poster"
                    $ guide_tip_text2 = "in the store!"
                    $ guide_tip_text3 = "Hermione will kiss your feet if you"
                    $ guide_tip_text4 = "buy it for her!"
                elif rndm_one_of_three == 3:
                    $ guide_add_tip = True
                    $ guide_tip_text = "She is really into sex stuff now."
                    $ guide_tip_text2 = "You really did your job well! "
                    $ guide_tip_text3 = "Still you kind of fucked up and she's"
                    $ guide_tip_text4 = "mad at you! Maybe buy her something!"



    else:
        
        

        ## Funny Tips ##
        if daily_rndm_tip_or_fact ==  0:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Never tickle a sleeping dragon."

        if daily_rndm_tip_or_fact ==  1:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Book 3 will always be the best one!"

        if daily_rndm_tip_or_fact ==  2:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Don't worry headmaster, Snape is not going"
            $ guide_tip_text2 = "to kill you."
            $ guide_tip_text3 = "Different timeline!"

        if daily_rndm_tip_or_fact ==  3:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Don't walk into the forbidden forest alone!"
            $ guide_tip_text2 = "There are creatures that live there,"
            $ guide_tip_text3 = "of the likes you have never seen before."
            $ guide_tip_text4 = "They call them cars!"

        if daily_rndm_tip_or_fact ==  4:                                     #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Flying-carpets were the preferred way for"
            $ guide_tip_text2 = " a wizard to travel. Now it's brooms."
            $ guide_tip_text3 = "What real wizard wants to sit on a broom?"
            $ guide_tip_text4 = "At least carpets don't hurt you crotch!"

        if daily_rndm_tip_or_fact ==  5:                                     #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "The small star icon on the top left of your"
            $ guide_tip_text2 = "screen opens the player guide!... "
            $ guide_tip_text3 = "Oh you already knew that?"
            $ guide_tip_text4 = "Well never mind then!"

        if daily_rndm_tip_or_fact ==  6:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "It's not a good idea to use an unforgivable"
            $ guide_tip_text2 = "curse! While the Imperius Curse might have"
            $ guide_tip_text3 = "had some usefulness to you, you will sadly"
            $ guide_tip_text4 = "have to corrupt Hermione the old way!"

        if daily_rndm_tip_or_fact ==  7:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "We have noticed you are running an Ad-Blocker!"
            $ guide_tip_text2 = "Please disable your Ad-Blocker to"
            $ guide_tip_text3 = "support this Quest-Guide! Thank You."

        if daily_rndm_tip_or_fact ==  8:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "Dumbledore is gay apparently."
            $ guide_tip_text2 = "Not that I mind that,"
            $ guide_tip_text3 = "I'm just running out of useful facts to tell."

        if daily_rndm_tip_or_fact ==  9:                                     #Max Characters
            $ guide_add_tip = False
            $ guide_tip_text = "You can support us on Patreon!"
            $ guide_tip_text2 = "You can find us at..."

        if daily_rndm_tip_or_fact ==  10:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Do. Or do not."
            $ guide_tip_text2 = "There is no try!"


        ## Helpful Tips ##
        if daily_rndm_tip_or_fact ==  11:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Rainy or cloudy day?"
            $ guide_tip_text2 = "Read a book!"
            $ guide_tip_text3 = "The moody weather will help you focus,"
            $ guide_tip_text4 = "and be more productive!"
        if daily_rndm_tip_or_fact ==  12:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Rainy or cloudy day?"
            $ guide_tip_text2 = "Best weather to write some reports!"
            $ guide_tip_text3 = "The moody weather will help you focus,"
            $ guide_tip_text4 = "and be more productive!"
        if daily_rndm_tip_or_fact ==  13:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Turn on the fireplace during the rain!"
            $ guide_tip_text2 = "The warming comfort of a fire-lit room makes"
            $ guide_tip_text3 = "reading faster and writing more enjoyable!"
        if daily_rndm_tip_or_fact ==  14:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "Drinking wine with Snape not only lengthens"
            $ guide_tip_text2 = "your strong friendship with him, he'll also"
            $ guide_tip_text3 = "be more willing to reward Slytherin with"
            $ guide_tip_text4 = "a higher number of house-points!"
        if daily_rndm_tip_or_fact ==  15:                                    #Max Characters
            $ guide_tip_text = "Keep rummaging through your cupboard."
            $ guide_tip_text2 = "You'll never know what useful things you"
            $ guide_tip_text3 = "can find until you try!"
        if daily_rndm_tip_or_fact ==  16:                                    #Max Characters
            $ guide_add_tip = False #False=Fact
            $ guide_tip_text = "Dumbledore had quite a selection of wine."
            $ guide_tip_text2 = "He might have some wine left in his cupboard!"

        if daily_rndm_tip_or_fact ==  17:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "If Hermione is mad at you it might take -days-"
            $ guide_tip_text2 = "for her to like you again!"
            $ guide_tip_text3 = "Better just buy her a gift!"

        if daily_rndm_tip_or_fact ==  18:                                    #Max Characters
            $ guide_add_tip = True
            $ guide_tip_text = "If Hermione is mad you, you can give her"
            $ guide_tip_text2 = "gifts to better her mood! "
            $ guide_tip_text3 = "Dependant on her whoring level she will"
            $ guide_tip_text4 = "prefer some gifts over others!"



    return
