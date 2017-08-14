init python:
    
    class silver_item(object):
        cost = 0
        name = ""
        image = ""
        description = ""
    
    class gift_item(silver_item):
        id = 0
        whoringNeeded = 0
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def costOf(self, number_of_item):
            return self.cost * number_of_item
    
label __init_variables:
    
    
    # $ gift_list = []
    
    # gift_list.append(cost=20, name="Lollipop candy", users=["hermione"],
        # description="A lollipop candy. An adult candy for kids or kids candy for adults?")
    
    # gift_list.append(cost=40, name="Chocolate",
        # description="The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
    
    # gift_list.append(cost=35, name="Plush owl",
        # description="a Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
    
    # gift_list.append(cost=50, name="Butterbeer", whoringNeeded=3,
        # description="Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
    
    # gift_list.append(cost=30, name="Educational magazines",
        # description="Educational magazines. \nthe Trusty companions of every social outcast.")
    
    # gift_list.append(cost=45, name="Girly magazines",
        # description="Girly magazines. \nAll cool girls are reading these.")
    
    # gift_list.append(cost=60, name="Adult magazines",
        # description="Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
    
    # gift_list.append(cost=80, name="Porn magazines", whoringNeeded=3,
        # description="Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
    
    # gift_list.append(cost=25, name="Viktor Krum Poster",
        # description="A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
    
    # gift_list.append(cost=75, name="Sexy lingerie",
        # description="Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
    
    # gift_list.append(cost=50, name="A pack of condoms", whoringNeeded=3,
        # description="\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
    
    # gift_list.append(cost=55, name="Vibrator", whoringNeeded=3,
        # description="A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
    
    # gift_list.append(cost=60, name="Jar of anal lubricant",
        # description="A Jar of anal lube, Buy this for your loved one - show that you care.")
    
    # gift_list.append(cost=70, name="Ball gag and cuffs",
        # description="Ball gag and cuffs, Turn your soulmate into your cellmate.")

    # gift_list.append(cost=85, name="Anal plugs", whoringNeeded=3,
        # description="Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike.")

    # gift_list.append(cost=200, name="Thestral Strap-on", whoringNeeded=3,
        # description="Thestral strap-on.\nWhen you see it, you'll shit bricks.")

    # gift_list.append(cost=500, name="Lady Speed Stick-2000",
        # description="The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!")

    # gift_list.append(cost=350, name="Sex doll \"Joanne\"",
        # description="Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")

    # gift_list.append(cost=65, name="Anal beads",image="01_hp/18_store/gift_anal_beads.png",
        # description="Anal beads engraved with a strange inscription \"Property of L.C.\".")
    
    
    if not hasattr(renpy.store,'Lollipop'): #important!
        $ Lollipop = gift_item()
    $ Lollipop.id = 0
    $ Lollipop.cost = 20
    $ Lollipop.name = "lollipop candy"
    $ Lollipop.image = "01_hp/18_store/gifts/1.png"
    $ Lollipop.description = "A lollipop candy. An adult candy for kids or kids candy for adults?"
    
    
    if not hasattr(renpy.store,'Chocolate'): #important!
        $ Chocolate = gift_item()
    $ Chocolate.id = 1
    $ Chocolate.cost = 40
    $ Chocolate.name = "Chocolate"
    $ Chocolate.image = "01_hp/18_store/gifts/2.png"
    $ Chocolate.description = "The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries)."
    
    if not hasattr(renpy.store,'PlushOwl'): #important!
        $ PlushOwl = gift_item()
    $ PlushOwl.id = 2
    $ PlushOwl.cost = 35
    $ PlushOwl.name = "Plush owl"
    $ PlushOwl.image = "01_hp/18_store/gifts/3.png"
    $ PlushOwl.description = "a Toy owl stuffed with feathers of an actual owl. It's so cuddly!"
    
    if not hasattr(renpy.store,'Butterbeer'): #important!
        $ Butterbeer = gift_item()
    $ Butterbeer.id = 3
    $ Butterbeer.cost = 50
    $ Butterbeer.whoringNeeded = 3
    $ Butterbeer.name = "Butterbeer"
    $ Butterbeer.image = "01_hp/18_store/gifts/4.png"
    $ Butterbeer.description = "Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}"
    
    if not hasattr(renpy.store,'EducationalMagazines'): #important!
        $ EducationalMagazines = gift_item()
    $ EducationalMagazines.id = 4
    $ EducationalMagazines.cost = 30
    $ EducationalMagazines.name = "Educational magazines"
    $ EducationalMagazines.image = "01_hp/18_store/gifts/5.png"
    $ EducationalMagazines.description = "Educational magazines. \nthe Trusty companions of every social outcast."
    
    if not hasattr(renpy.store,'GirlyMagazines'): #important!
        $ GirlyMagazines = gift_item()
    $ GirlyMagazines.id = 5
    $ GirlyMagazines.cost = 45
    $ GirlyMagazines.name = "Girly magazines"
    $ GirlyMagazines.image = "01_hp/18_store/gifts/6.png"
    $ GirlyMagazines.description = "Girly magazines. \nAll cool girls are reading these."
    
    if not hasattr(renpy.store,'AdultMagazines'): #important!
        $ AdultMagazines = gift_item()
    $ AdultMagazines.id = 6
    $ AdultMagazines.cost = 60
    $ AdultMagazines.name = "Adult magazines"
    $ AdultMagazines.image = "01_hp/18_store/gifts/7.png"
    $ AdultMagazines.description = "Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex."
    
    if not hasattr(renpy.store,'PornMagazines'): #important!
        $ PornMagazines = gift_item()
    $ PornMagazines.id = 7
    $ PornMagazines.cost = 80
    $ PornMagazines.whoringNeeded = 3
    $ PornMagazines.name = "Porn magazines"
    $ PornMagazines.image = "01_hp/18_store/gifts/8.png"
    $ PornMagazines.description = "Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\"."
    
    if not hasattr(renpy.store,'ViktorKrumPoster'): #important!
        $ ViktorKrumPoster = gift_item()
    $ ViktorKrumPoster.id = 8
    $ ViktorKrumPoster.cost = 25 #placeholder number
    $ ViktorKrumPoster.name = "Viktor Krum Poster"
    $ ViktorKrumPoster.image = "01_hp/18_store/gifts/9.png"
    $ ViktorKrumPoster.description = "A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world."
    
    if not hasattr(renpy.store,'SexyLingerie'): #important!
        $ SexyLingerie = gift_item()
    $ SexyLingerie.id = 9
    $ SexyLingerie.cost = 75 #placeholder number
    $ SexyLingerie.name = "Sexy lingerie"
    $ SexyLingerie.image = "01_hp/18_store/gifts/10.png"
    $ SexyLingerie.description = "Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath."
    
    if not hasattr(renpy.store,'PackOfCondoms'): #important!
        $ PackOfCondoms = gift_item()
    $ PackOfCondoms.id = 10
    $ PackOfCondoms.cost = 50
    $ PackOfCondoms.whoringNeeded = 3
    $ PackOfCondoms.name = "A pack of condoms"
    $ PackOfCondoms.image = "01_hp/18_store/gifts/11.png"
    $ PackOfCondoms.description = "\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}"
    
    if not hasattr(renpy.store,'Vibrator'): #important!
        $ Vibrator = gift_item()
    $ Vibrator.id = 11
    $ Vibrator.cost = 55
    $ Vibrator.whoringNeeded = 3
    $ Vibrator.name = "Vibrator"
    $ Vibrator.image = "01_hp/18_store/gifts/12.png"
    $ Vibrator.description = "A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core."
    
    if not hasattr(renpy.store,'JarOfLube'): #important!
        $ JarOfLube = gift_item()
    $ JarOfLube.id = 12
    $ JarOfLube.cost = 60
    $ JarOfLube.name = "Jar of anal lubricant"
    $ JarOfLube.image = "01_hp/18_store/gifts/13.png"
    $ JarOfLube.description = "A Jar of anal lube, Buy this for your loved one - show that you care."
    
    if not hasattr(renpy.store,'BallGagAndCuffs'): #important!
        $ BallGagAndCuffs = gift_item()
    $ BallGagAndCuffs.id = 13
    $ BallGagAndCuffs.cost = 70
    $ BallGagAndCuffs.name = "Ball gag and cuffs"
    $ BallGagAndCuffs.image = "01_hp/18_store/gifts/14.png"
    $ BallGagAndCuffs.description = "Ball gag and cuffs, Turn your soulmate into your cellmate."
    
    if not hasattr(renpy.store,'AnalPlugs'): #important!
        $ AnalPlugs = gift_item()
    $ AnalPlugs.id = 14
    $ AnalPlugs.cost = 85
    $ AnalPlugs.whoringNeeded = 3
    $ AnalPlugs.name = "Anal plugs"
    $ AnalPlugs.image = "01_hp/18_store/gifts/15.png"
    $ AnalPlugs.description = "Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike."
    
    if not hasattr(renpy.store,'ThestralStrapon'): #important!
        $ ThestralStrapon = gift_item()
    $ ThestralStrapon.id = 15
    $ ThestralStrapon.cost = 200
    $ ThestralStrapon.whoringNeeded = 3
    $ ThestralStrapon.name = "Thestral Strap-on"
    $ ThestralStrapon.image = "01_hp/18_store/gifts/16.png"
    $ ThestralStrapon.description = "Thestral strap-on.\nWhen you see it, you'll shit bricks."
    
    if not hasattr(renpy.store,'SpeedStick2000'): #important!
        $ SpeedStick2000 = gift_item()
    $ SpeedStick2000.id = 16
    $ SpeedStick2000.cost = 500
    $ SpeedStick2000.name = "Lady Speed Stick-2000"
    $ SpeedStick2000.image = "01_hp/18_store/gifts/17.png"
    $ SpeedStick2000.description = "The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!"
    
    if not hasattr(renpy.store,'SexDollJoanne'): #important!
        $ SexDollJoanne = gift_item()
    $ SexDollJoanne.id = 17
    $ SexDollJoanne.cost = 350
    $ SexDollJoanne.name = "Sex doll \"Joanne\""
    $ SexDollJoanne.image = "01_hp/18_store/gifts/18.png"
    $ SexDollJoanne.description = "Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort."
    
    if not hasattr(renpy.store,'AnalBeads'): #important!
        $ AnalBeads = gift_item()
    $ AnalBeads.id = 18
    $ AnalBeads.cost = 65 #placeholder number
    $ AnalBeads.name = "Anal beads"
    $ AnalBeads.image = "01_hp/18_store/gift_anal_beads.png"
    $ AnalBeads.description = "Anal beads engraved with a strange inscription \"Property of L.C.\"."
    
    
    $ gift_list = []
    $ gift_list.append(Lollipop)
    $ gift_list.append(Chocolate)
    $ gift_list.append(PlushOwl)
    $ gift_list.append(Butterbeer)
    $ gift_list.append(EducationalMagazines)
    $ gift_list.append(GirlyMagazines)
    $ gift_list.append(AdultMagazines)
    $ gift_list.append(PornMagazines)
    $ gift_list.append(ViktorKrumPoster)
    $ gift_list.append(SexyLingerie)
    $ gift_list.append(PackOfCondoms)
    $ gift_list.append(Vibrator)
    $ gift_list.append(JarOfLube)
    $ gift_list.append(BallGagAndCuffs)
    $ gift_list.append(AnalPlugs)
    $ gift_list.append(ThestralStrapon)
    $ gift_list.append(SpeedStick2000)
    #$ gift_list.append(SexDollJoanne)
    #$ gift_list.append(AnalBeads)
    
    return

label happy(sub_mad = 0):
    hide screen hermione_main
    with d3
    $ mad -= sub_mad
    if mad <= 0:
        $ mad = 0
    if mad == 0:
        ">Hermione's mood has improved...\n>Hermione is {size=+5}not upset{/size} with you..."
    else:
        ">Hermione's mood has improved...\n>Hermione is {size=+5}still upset{/size} with you..."
    return

label no_change:
    hide screen hermione_main
    with d3  
    ">Hermione's mood didn't change much..."
    return

label upset(add_mad):
    hide screen hermione_main
    with d3
    $ mad += add_mad
    ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
    return
    
label her_gift_menu:
    python:
        choices = []
        for i in gift_list:
            if gift_item_inv[i.id] > 0:
                choices.append( ( ("-"+str(i.name)+"- ("+str(gift_item_inv[i.id])+")"), i) )
        
        choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(choices)
        
    if result == "nvm":
        jump day_time_requests
    else:
        call give_her_gift(result)
    
label give_her_gift(gift_id):
    hide screen hermione_main
    with d5
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if gift_id == 0:#candy
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A lollipop?","body_01")
            call give_gift(">You give the candy to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_06")
            call happy(5)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Candy?","body_03")
            call her_main("Candy is for kids, [genie_name].","body_02")
            call give_gift(">You give the candy to Hermione...",gift_id)
            call her_main("Thank you...","body_29")
            call happy(5)
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Candy?","body_03")
            call give_gift(">You give the candy to Hermione...",gift_id)
            call her_main("Ehm... Sure, thanks...","body_08")
            call happy(5)
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("A lollipop?","body_06")
            call her_main("Clever girls use candy like this as a \"weapon\".","body_46")
            call give_gift(">You give the candy to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_74")
            call happy(5)
            $ h_body = "body_128"
    if gift_id == 1:#chocolate
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A chocolate bar?","body_01")
            call give_gift(">You give the chocolate to Hermione...", gift_id)
            call her_main("Thank you, [genie_name].","body_06")
            call happy(10)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A chocolate bar?","body_03")
            call her_main("Hm...","body_09")
            call her_main("That thing about fairies...")
            call her_main("That is a joke of some sort, right?","body_11")
            call give_gift(">You give the chocolate to Hermione...", gift_id)
            call her_main("Thank you...","body_15")
            call happy(10)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A chocolate bar?","body_03")
            call her_main("I just like the way it crunches, [genie_name]! N-not the taste...","body_24")
            call give_gift(">You give the chocolate to Hermione...", gift_id)
            call her_main("Ehm... Sure, thanks...","body_01")
            call happy(10)
        if whoring >= 18: # Lv 7+  
            call her_main("A chocolate bar?","body_06")
            call her_main("You spoil me, [genie_name].","body_111")
            call give_gift(">You give the chocolate to Hermione...", gift_id)
            call her_main("Thank you.","body_129")
            call happy(10)
    if gift_id == 2:#plush owl
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A stuffed owl?","body_01")
            call her_main("It's cute...","body_06")
            call give_gift(">You give the owl to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_01")
            call happy(7)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A plush toy?","body_11")
            call her_main("I like it!","body_06")
            call give_gift(">You give the owl to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_01")
            call happy(10)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A toy?","body_01")
            call her_main("Toys are for kids, [genie_name].","body_02")
            call her_main("But I'll take it...","body_29")
            call give_gift(">You give the owl to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_01")
            call happy(15)
        if whoring >= 18: # Lv 7+  
            call her_main("This is one of those adult toys isn't it?","body_66")
            call her_main("There's got to be a switch or a button somewhere...","body_87")
            call her_main("So... Does it vibrate or something?","body_124")
            call her_main("Oh...?","body_190")
            call her_main("So it is really just a plush toy then?")
            call her_main("Shame...","body_118")
            call her_main("I mean, thank you, [genie_name].","body_34")
            call give_gift(">You give the owl to Hermione...",gift_id)
            $ h_body = "body_01"
            call happy(4)
    if gift_id == 3:#butterbeer
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Butterbeer?","body_01")
            call her_main("Are you sure about that, [genie_name]?","body_08")
            call her_main("It does contain alcohol, you know...","body_06")
            call give_gift(">You give the bottle to Hermione...",gift_id)
            call her_main("Thank you.","body_01")
            call happy(3)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Butterbeer, [genie_name]?","body_11")
            call her_main("To let you in on a little secret, [genie_name]...","body_14")
            call her_main("I'm a big fan of this completely harmless beverage.","body_06")
            call give_gift(">You give the bottle to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_01")
            call happy(10)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Butterbeer?","body_01")
            call her_main("Thank you, [genie_name].","body_24")
            call give_gift(">You give the bottle to Hermione...",gift_id)
            call her_main("I shall drink this with the girls later.","body_06")
            call happy(15)
        if whoring >= 18: # Lv 7+  
            call her_main("Butterbeer...?","body_06")
            call her_main("Thank you, [genie_name].","body_01")
            call give_gift(">You give the bottle to Hermione...",gift_id)
            call her_main("I shall drink this later with the boys.","body_06")
            call her_main("Err... I meant to say with the girls, of course.","body_189")
            call happy(20)
            $ h_body = "body_01"
    if gift_id == 4:#edu mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("\"Popular magic\" magazines?","body_01")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id)
            call her_main("Thank you, [genie_name]!","body_06")
            call her_main("I will use them for my research!")
            call happy(15)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Sometimes I find information in magazines that I could never find in a book...","body_01")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id)
            call her_main("Thank you, [genie_name]!","body_06")
            call her_main("I will use them for my research!")
            call happy(10)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Oh...","body_02")
            call her_main("Yes, I used to read magazines like that a lot...","body_06")
            call her_main("Lately not so much though...","body_10")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id)
            call her_main("Thank you, [genie_name]!","body_06")
            call happy(3)
        if whoring >= 18: # Lv 7+  
            call her_main("Ehm...","body_10")
            call her_main("To be honest, magazines like that lost their appeal to me completely lately...","body_08")
            call her_main("But I don't mind taking them off you hands anyway, [genie_name].","body_11")
            call give_gift(">You give an assortment of educational magazines to Hermione...",gift_id)
            call her_main("Thank you.","body_13")
            call no_change 
    if gift_id == 5:#girl mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm?","body_15")
            call her_main("This is the sort of press some \"slytherin\" bimbo would appreciate.","body_17")
            call her_main("I am way above silly magazines like that, [genie_name].","body_16")
            call no_change
            $ h_body = "body_01"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("I don't read magazines of that nature, [genie_name]...","body_04")
            call her_main("................","body_13")
            call her_main("But I could give it a try just to humour you I suppose...","body_04")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id)
            call her_main("Thank you, [genie_name]!","body_08")
            call happy(5)
            $ h_body = "body_06"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("I ashamed to admit this, but...","body_10")
            call her_main("I really enjoy reading magazines like that lately...","body_24")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_08")
            call happy(15)
            $ h_body = "body_06"
        if whoring >= 18: # Lv 7+  
            call her_main("The Latest edition of \"Girlz\"?!","body_18")
            call her_main("I can't have enough of that brilliant magazine!","body_24")
            call give_gift(">You give an assortment of rather girly magazines to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_08")
            call happy(15)
            $ h_body = "body_06"
    if gift_id == 6:#adult mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Are that...?","body_02")
            call her_main("Adult magazines, [genie_name]?","body_31")
            call her_main("Given to me by An esteemed wizard of your status?","body_69")
            call her_main("[genie_name], surely you could find a more productive way to spend your free time.","body_66")
            call her_main("And I most definitely would not have use for those...","body_47")
            call upset(7)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Adult magazines?","body_05")
            call her_main("[genie_name], I have no interest in things like that.","body_69")
            call her_main("And how is this an appropriate present for one of your students, [genie_name]?","body_47")
            call upset(3)
            $ h_body = "body_29"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Adult magazines?","body_31")
            call her_main("[genie_name], this is such an inappropriate present for a girl my age...","body_34")
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_id)
            call her_main("I shall throw these away myself...","body_79")
            call happy(8)
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("The New edition of \"L.o.v.e.\"!!!","body_75")
            call her_main("Err.. I mean, adult magazines?","body_122")
            call her_main("This is a little inappropriate...")
            call her_main("But I will take them...","body_74")
            call give_gift(">You give an assortment of adult magazines to Hermione...",gift_id)
            call her_main("thank you, [genie_name].","body_74")
            call happy(15)
    if gift_id == 7:#porn mags
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm... What is this?","body_01")
            call her_main("[genie_name], those are porn magazines!","body_130")
            call her_main("Shame on you, [genie_name]!","body_187")
            call upset(15)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Porn magazines?","body_48")
            call her_main("[genie_name], what do you expect me to do with those?","body_87")
            call her_main("Research them?","body_79")
            call her_main("Despicable!","body_86")
            call upset(8)
            $ h_body = "body_120"
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("That's hardcore porn, [genie_name].","body_31")
            call her_main("Which is a completely inappropriate gift for a girl my age!","body_34")
            call her_main("..............","body_118")
            call her_main("But I will take them...","body_117")
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_id)
            call her_main("And I shall throw them in the trash, where they and... girls who like these things belong...","body_79")
            call no_change
            $ h_body = "body_120"
        if whoring >= 18: # Lv 7+  
            call her_main("Pornography?","body_48")
            call her_main("................","body_118")
            call her_main("How can women even agree to do things like that, [genie_name]?","body_117")
            call her_main(".................","body_118")
            call her_main("Alright, I shall accept them...","body_120")
            call her_main("Solely for research purposes of course...","body_189")
            call give_gift(">You give an assortment of porn magazines to Hermione...",gift_id)
            call happy(15)
            $ h_body = "body_45"
    if gift_id == 8:#krum poster
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A Quidditch poster?","body_73")
            call her_main("What am I supposed to do with it, [genie_name]?","body_185")
            call her_main("No, thank you.","body_184")
            call no_change
            $ h_body = "body_71"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A Quidditch poster?","body_73")
            call her_main("Hm...","body_185")
            call her_main("I think I saw this player once or twice...","body_71")
            call her_main("He is that Durmstrang student, right?","body_06")
            call give_gift(">You give the poster to Hermione...",gift_id)
            call happy(5)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A Viktor Krum poster, [genie_name]?","body_73")
            call her_main("Can't say that I care much for Quidditch, but...","body_08")
            call her_main("I can see why the girls find the brutish physique of some players appealing...","body_87")
            call give_gift(">You give the poster to Hermione...",gift_id)
            call happy(15)
        if whoring >= 18: # Lv 7+  
            call her_main("A Viktor Krum poster?!","body_72")
            call her_main("Thank you, [genie_name]!","body_24")
            call give_gift(">You give the poster to Hermione...",gift_id)
            call her_main("Can't wait to hang it over my bed!","body_46")
            call her_main("The girls will go green with envy...","body_64")
            call happy(25)
    if gift_id == 9:#lingerie
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("lingerie?","body_118")
            call her_main("[genie_name], I cannot accept a gift like this from you...","body_120")
            call upset(10)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("sexy lingerie?","body_118")
            call her_main("You know I cannot possibly accept a gift like that from you, [genie_name].","body_117")
            call her_main("(It's pretty though).........","body_118")
            call no_change
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("sexy lingerie?","body_124")
            call her_main("[genie_name] that is so inappropriate...","body_122")
            call give_gift(">You give the lingerie to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_188")
            call happy(7)
        if whoring >= 18: # Lv 7+  
            call her_main("sexy lingerie?","body_124")
            call her_main("Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?","body_123")
            call her_main("Oh... I mean, thank you, [genie_name].","body_122")
            call give_gift(">You give the lingerie to Hermione...",gift_id)
            call happy(15)
    if gift_id == 10:#condoms
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Condoms?!","body_18")
            call her_main("[genie_name], I wouldn't even know what to do with them...","body_30")
            call upset(6)
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("...Condoms?","body_07")
            call her_main("Ehm... Is this a part of some new Hogwarts sex ed program or something?","body_04")
            call her_main("No, [genie_name]... It feels wrong to accept a thing like this from you...","body_189")
            call no_change
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A pack of condoms?","body_03")
            call her_main("[genie_name], what possible use could I have for those?")
            call her_main("Well, I shall accept them simply because it is rude to refuse a gift...","body_04")
            call give_gift(">You give a pack of condoms to Hermione...", gift_id)
            call happy(3)
            $ h_body = "body_29"
        if whoring >= 18: # Lv 7+
            call her_main("A pack of condoms?","body_08")
            call her_main("I appreciate your concern, [genie_name]. Thank you.","body_128")
            call give_gift(">You give a pack of condoms to Hermione...", gift_id)
            call happy(4)
            $ h_body = "body_45"
    if gift_id == 11:#vibrator
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A magic wand?","body_01")
            call her_main("No, it doesn't look like--","body_15")
            call her_main(".........?")
            call her_main("!!!","body_18")
            call her_main("[genie_name]!","body_187")
            call her_main("This is just beyond inappropriate!","body_30")
            call upset(10)
            $ h_body = "body_120"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Is this what I think it is?","body_118")
            call her_main("[genie_name], let me remind you that I belong to the noble house of \"Gryffindor\".","body_186")
            call her_main("A present like that would be appropriate for a girl from \"Slytherin\", [genie_name].","body_120")
            call upset(10)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Is that a... vibrator?","body_118")
            call her_main("The design...")
            call her_main("it reminds me of my wand...")
            call her_main("Did you have this custom made for me [genie_name]?","body_118")
            call her_main("This is inappropriate...","body_30")
            call her_main("But I shall take it nonetheless...","body_29")
            call give_gift(">You give the vibrator to Hermione...",gift_id)
            call no_change
        if whoring >= 18: # Lv 7+  
            call her_main("This vibrator...","body_11")
            call her_main("It's... calling out for me...","body_10")
            call her_main("But not in a dirty way, [genie_name].","body_66")
            call give_gift(">You give the vibrator to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_124")
            call happy(10)
    if gift_id == 12:#anal lube
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("I don't know what this is...","body_02")
            call her_main("But I have the feeling that the jar is full of something vile and inappropriate...","body_05")
            call her_main("No, thank you, [genie_name].")
            call upset(6)
            $ h_body = "body_03"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("Hm...","body_73")
            call her_main("I think I know what this is...","body_66")
            call her_main("But why would you give something like this to one of your pupils, [genie_name]?")
            call her_main("No, thank you.","body_69")
            call upset(2)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Anal lubricant?","body_118")
            call her_main("Ehm.. well... I know this girl...","body_189")
            call her_main("I mean I don't know her, she is a friend of a friend...")
            call her_main("Yes, I will take this for her...")
            call give_gift(">You give the jar to Hermione...", gift_id, 0)
            call her_main("Still, I think you should not give presents like this to your pupils, [genie_name].","body_186")
            call no_change
            $ h_body = "body_79"
        if whoring >= 18: # Lv 7+  
            call her_main("Anal lubricant, [genie_name]?","body_124")
            call her_main("I know a couple of girls who would do anything for a commodity like that.","body_186")
            call her_main("Thank for looking out for us, [genie_name].","body_128")
            call give_gift(">You give the jar to Hermione...", gift_id)
            call happy(5)
    if gift_id == 13:#gag and cuffs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("What is this?","body_118")
            call her_main("Is this like one of those adult toys?","body_141")
            call her_main("What woman in her right mind would subject herself to a humiliation like that?","body_30")
            call her_main("And what possible use could I have for such objects?","body_186")
            call her_main("This is just insulting, [genie_name]...","body_187")                                                                                                                                                                                                              
            call upset(10)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], do you not realize how inappropriate it would be for me to accept a present like that?","body_186")
            call her_main("And I would not even know what to do with them anyway...","body_189")
            call her_main("I mean these fluffy things are obviously handcuffs...","body_118")
            call her_main("But this ball... ehm...")
            call her_main("[genie_name], please...","body_120")
            call her_main("Just put them away.")
            call upset(5)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A month ago I would've felt insulted to receive a gift like this...","body_120")
            call her_main("But by now I know that some girls really do find pleasure in toys like...","body_118")
            call her_main("But I assure you that I am not one of them, [genie_name].","body_120")
            call her_main("But I know a girl who knows a girl who is into things like...","body_189")
            call her_main("Yes, I shall take these to her...","body_188")
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_id)
            call happy(9)
        if whoring >= 18: # Lv 7+  
            call her_main("A ball gag and handcuffs?","body_190")
            call her_main("This is completely inappropriate, [genie_name].","body_122") # :)
            call her_main("But a gift is a gift, right?","body_129")
            call give_gift(">You give the ball gag and cuffs to Hermione...",gift_id)
            call happy(15)
    if gift_id == 14:#anal plugs
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Hm...?","body_01")
            call her_main("Are those like key-chain toys?","body_15")
            call give_gift(">You give the anal plugs to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_185")
            call happy(8)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("[genie_name], are those adult toys of some sort?","body_186")
            call her_main("those are some of those anal things, aren't they?","body_187")
            call her_main("[genie_name] this is nothing but a weapon meant to oppress women!")
            call her_main("Despicable!","body_120")
            call upset(15)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("Yes, I know that some girls have uhm...","body_120")
            call her_main("Have use for things such as these...","body_186")
            call her_main("But not me, [genie_name].")
            call her_main("No, thank you.","body_120")
            call no_change
        if whoring >= 18: # Lv 7+  
            call her_main("Anal plugs?","body_118")
            call her_main("I have no use for things like that, [genie_name]...","body_117")
            call her_main("They are so pretty though...","body_122")
            call her_main(".....................","body_118")
            call her_main("Well, alright. I shall take them off your hands if I must, [genie_name].","body_121")
            call give_gift(">You give the anal plugs to Hermione...",gift_id)
            call her_main("But I shall never use them of course...","body_127")
            call her_main("................","body_124")
            call happy(10)
    if gift_id == 15:#strap on
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("What is that?","body_18")
            call her_main("An artifact of some sort or a trophy?","body_14")
            call her_main("So well-crafted...","body_01")
            call her_main("Are you sure that it's alright for me to have it, [genie_name]?","body_06")
            call give_gift(">You give the strap-on to Hermione...",gift_id)
            call her_main("Thank you very much, [genie_name]. I promise to take good care of it.","body_16")
            call happy(20)
            $ h_body = "body_15"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("!!!","body_18")
            call her_main("That is...","body_118")
            call her_main("But it doesn't even look... human...")
            call her_main("I mean...","body_69")
            call her_main("[genie_name], do you have no shame?!","body_86")
            call her_main("Presenting a thing like that to a pupil?!")
            call her_main("..................","body_87")
            call her_main("Please put it away, [genie_name].","body_47")
            call upset(15)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("That thing...","body_118")
            call her_main("Is that the actual size of the... of the real \"thing\"?","body_117")
            call her_main("I mean...","body_189")
            call her_main(".......................","body_118")
            call her_main("Is this like a party prank prop?","body_117")
            call her_main("It's so well-crafted though...","body_118")
            call her_main("I will take it...","body_33")
            call give_gift(">You give the strap-on to Hermione...",gift_id)
            call happy(10)
        if whoring >= 18: # Lv 7+  
            call her_main("It's... It's magnificent, [genie_name]...","body_48")
            call her_main("Is it really modeled after a thestral?","body_189")
            call her_main("But the creatures are invisible...","body_190")
            call her_main("..................","body_118")
            call her_main("Breathtaking...","body_123")
            call her_main("Not in the way you think, [genie_name]...","body_120")
            call her_main("I am merely admiring the craftsmanship...","body_127")
            call give_gift(">You give the strap-on to Hermione...",gift_id)
            call her_main("Thank you for the gift, [genie_name].","body_129")
            call happy(30)
    if gift_id == 16:#speed stick
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("A broom...?","body_01")
            call her_main("Hm...","body_03")
            call her_main("What is that silly-looking thing attached to it?","body_07")
            call her_main("Is it like a saddle...?","body_08")
            call give_gift(">You give the broom to Hermione...",gift_id)
            call her_main("Thank you for the gift, [genie_name].","body_11")
            $ h_body = "body_06"
            call happy(20)
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A broom...?","body_01")
            call her_main("Hm...","body_07")
            call her_main("It's a sex-toy of some sort, isn't it?","body_05")
            call her_main("But it is so well crafted...","body_87")
            call give_gift(">You give the broom to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_120")
            call happy(20)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A broom...?","body_118")
            call her_main("Hm...")
            call her_main("What kind of saddle is that...?","body_66")
            call her_main("Well, doesn't matter.","body_127")
            call her_main("Refusing an expensive gift like that would be rude...")
            call give_gift(">You give the broom to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_120")
            call happy(30)
        if whoring >= 18: # Lv 7+  
            call her_main("A broom...","body_124")
            call her_main("Hm...")
            call her_main("That saddle, [genie_name]...","body_189")
            call her_main("It was designed especially for witches, was it not?","body_190")
            call her_main("I am not sure whether this is inappropriate or clever...","body_185")
            call her_main("But this is a brilliant piece of engineering eitherway...","body_129")
            call give_gift(">You give the broom to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_128")
            call happy(30)
    if gift_id == 17:#sex doll
        if whoring >= 0 and whoring <= 5: # Lv 1-2.
            call her_main("Is this...","body_48")
            call her_main("A sex doll?!","body_34")
            call her_main("[genie_name]!!!","body_32")
            call upset(20)
            $ h_body = "body_33"
        if whoring >= 6 and whoring <= 11: # Lv 3-4.
            call her_main("A sex doll?","body_48")
            call her_main("This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]...","body_120")
            call upset(20)
        if whoring >= 12 and whoring <= 17: # Lv 5-6.
            call her_main("A sex doll...","body_118")
            call her_main("This is a little inappropriate...","body_120")
            call her_main("But maybe we could use it for a prank or something...","body_124")
            call give_gift(">You give the blow-up doll to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_124")
            call happy(10)
        if whoring >= 18: # Lv 7+  
            call her_main("the Joanne sex doll?","body_73")
            call her_main("I Can't say that I approve of this...","body_189")
            call her_main("But I know Harry would love to have a go at it...","body_124")
            call give_gift(">You give the blow-up doll to Hermione...",gift_id)
            call her_main("Thank you, [genie_name].","body_188")
            call happy(30)
    
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    show screen hermione_main
    with d3
    return
    
label give_gift(text = "", gift = 0):
    hide screen hermione_main
    with d3
    # note that gift is the index (starting with 0), while the image
    # files are starting with/off by 1!
    $ the_gift = "01_hp/18_store/gifts/"+str(gift+1)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift_item_inv[gift] -= 1
    return
    
    
###GIVING CLOTHING RESPONSES
label giving_gryffindor_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A Cheerleading costume?","body_03",xpos=140)
    hide screen hermione_main
    with d3
    $ the_gift = "01_hp/18_store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Gryffindor Cheerleading outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name], although I don't know when I'd wear it.","body_04")
    call happy
    
    call her_main("","body_03",xpos=370)
    jump day_time_requests    

label giving_slytherin_cheer:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A Cheerleading costume? For Slytherin?","body_03",xpos=140)
    hide screen hermione_main
    with d3
    $ the_gift = "01_hp/18_store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Slytherin Cheerleading outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name], even though I'm not in Slytherin...","body_04")
    call happy
    
    call her_main("","body_03",xpos=370)
    jump day_time_requests    

label giving_maid_outfit:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    $ nets = 7 # Means already gifted.
    call her_main("A maid outfit?","body_03",xpos=140)
    hide screen hermione_main
    with d3
    $ the_gift = "01_hp/18_store/07.png" # blue box
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A maid outfit has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name].","body_04")
    call happy
    
    call her_main("","body_03",xpos=370)
    jump day_time_requests    

label giving_silk_nightgown:
    hide screen hermione_main
    with d5
    
    $ mad -= 30
    call her_main("A nightgown?","body_03",xpos=140)
    hide screen hermione_main
    with d3
    $ the_gift = "01_hp/18_store/07.png"# blue box
    show screen gift
    with d3
    ">You give the nightgown to Hermione...\n>A silk nightgown has been added to the wardrobe."
    hide screen gift
    call her_main("Thank you, [genie_name].","body_04")
    call happy
    
    call her_main("","body_03",xpos=370)
    jump day_time_requests    
    
    
label giving_skirt:
    $ gifted = True #Prevents you from giving Hermione a several gifts in a row. Turns back to False every night and every morning.
    $ have_miniskirt = False # Turns TRUE when you have the skirt in your possession.
    $ gave_miniskirt = True #Turns True when Hermione has the miniskirt.
    $ days_without_an_event = 0
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5
    
    
    $ mad = 0
    m "Here... This is for you..."
    $ the_gift = "01_hp/18_store/07.png" # Miniskirt.
    show screen gift
    with d3
    $ renpy.play('sounds/win2.mp3')
    ">You give the school miniskirt to Hermione..."
    hide screen gift
    with d3
    hide screen hermione_main
    with d3
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    call her_main("Hm...? What is this?","body_01")
    call her_main("A skirt?","body_11")
    call her_main("Thank you [genie_name].","body_06")
    #her "Thank you professor."
    m "Don't mention it."
    hide screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3  
    $ renpy.play('sounds/win_04.mp3')   #Not loud.
    show screen notes
    #">\"Dresscode\" option unlocked. From now on you can affect Hermione's attire choices."
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "body_01"
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    jump day_time_requests
    
### DRESS CODE ###
label mini_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("You cannot be serious, [genie_name]!","body_04")
        her "A skirt this short?!"
        call her_main("...It barely covers anything, [genie_name].","body_79")
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","body_66")
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("well, alright...","body_66")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","body_15")
        call her_main("But it's so short...","body_17")
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","body_07")
                call her_main("I refuse!","body_09")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","body_07")
                call her_main("Well, in that case...","body_08")
                call her_main("As long as it benefits my house...","body_29")
            "\"Fine. Forget it\"":
                call her_main("Alright...","body_01")
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","body_15")
        call her_main("But it's so short...","body_17")
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("Alright, alright...","body_69")
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","body_07")
                call her_main("Alright. I don't mind then.","body_68")
            "\"Fine. Forget it\"":
                call her_main("Oh...","body_13")
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Of course, [genie_name]...","body_118")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_02 = True
    $ legs_03 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label mini_off:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("I'm glad that you came to your senses, [genie_name].","body_04")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Gladly, [genie_name].","body_01")

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Alright...","body_13")
    
    if whoring >= 18: # Lv 7+
        call her_main("That boring thing again?","body_28")
    
    
    $ legs_02 = False
    $ legs_03 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
   
label tiny_on:
    
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("You cannot be serious, [genie_name]!","body_04")
        her "A skirt THIS short?!"
        call her_main("...It doesn't cover anything, [genie_name].","body_79")
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","body_66")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                her "........................"
                her "..............................."
                call her_main("well, alright...","body_66")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","body_15")
        call her_main("But it's soooo short...","body_17")
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","body_07")
                call her_main("I refuse!","body_09")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                call her_main("Hm...","body_07")
                call her_main("Well, in that case...","body_08")
                call her_main("As long as it benefits my house...","body_29")
            "\"Fine. Forget it\"":
                call her_main("Alright...","body_01")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","body_15")
        call her_main("But it's soooo short...","body_17")
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("Alright, alright...","body_69")
            "\"I will give you 10 points.\"":
                $ gryffindor +=10
                call her_main("Hm...","body_07")
                call her_main("Alright. I don't mind then.","body_68")
            "\"Fine. Forget it\"":
                call her_main("Oh...","body_13")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        call her_main("Of course, [genie_name]...","body_118")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
                                                                                                                                                                                                                          #HERMIONE
    
    
    $ legs_03 = True
    $ legs_02 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label give_glasses:
    call her_main("But I don't need glasses...","body_01")
    
    $ glasses_worn = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label take_glasses:
    call her_main("I was just getting used to them though.","body_01")
    
    $ glasses_worn = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label badge_put:
    call her_main("Of course, [genie_name]...","body_01")
    
    $ hermione_badges = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_off:
    call her_main("That boring old thing? ok then","body_08")
    
    $ wear_shirts = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label shirt_on:
    call her_main("Finally, it was soooo boring dressing like this","body_06")
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_on:
    call her_main("What, I can't do that, everyone would call me a slut","body_05")
    m "just do it"
    $ h_body = "body_30"
    her "[genie_name], I have to draw a line somewhere, I'm not walking around with no shirt on!"
    m "i'll give you 100 points"
    her "200"
    m "sure, why not"
    her ".............fine"
    
    $ wear_shirts = False
    $ gryffindor +=200
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label bra_off:
    call her_main("oh thank you, you have no idea what it was like...","body_01")
    
    $ wear_shirts = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label g_stockings_on:
    call her_main("Ok then","body_01")
    
    $ stockings = 2
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label g_stockings_off:
    call her_main("Ok.","body_01")
    
    $ stockings = 0
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_on:
    call her_main("A bra?","body_01")
    m "I thought that you could use a new one."
    her "Thank you [genie_name]."
    
    $ custom_bra = 1
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label lace_off:
    call her_main("Ok","body_01")
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_on:
    call her_main("You want me to wear this?","body_01")
    m "No one will see it."
    her "...Fine"
    
    $ custom_bra = 2
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label cupless_off:
    call her_main("Finally. This thing isn't very comfortable.","body_01")
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label silk_on:
    call her_main("You want me to change bra?","body_01")
    her "Ok then"
    
    $ custom_bra = 3
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label silk_off:
    call her_main("Ok","body_01")
    
    $ custom_bra = 0
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_on:
    call her_main("What is this?","body_01")
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_06_worn = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_06_off:
    call her_main("Ok","body_01")
    
    $ custom_06_worn = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_on:
    call her_main("What is this?","body_01")
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_07_worn = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_07_off:
    call her_main("Ok","body_01")
    
    $ custom_07_worn = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_on:
    call her_main("What is this?","body_01")
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_08_worn = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_08_off:
    call her_main("Ok","body_01")
    
    $ custom_08_worn = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_on:
    call her_main("What is this?","body_01")
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_09_worn = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_09_off:
    call her_main("Ok","body_01")
    
    $ custom_09_worn = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_on:
    call her_main("What is this?","body_01")
    m "I literally have no idea"
    her "Ok then"
    
    $ custom_10_worn = True
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label custom_10_off:
    call her_main("Ok","body_01")
    
    $ custom_10_worn = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label h_top_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_top = True
    call update_her_uniform
    show screen hermione_main
    with d5 
    return
    
label h_top_off:
    hide screen hermione_main
    with d5    
    $ hermione_wear_top = False
    call update_her_uniform
    show screen hermione_main
    with d5 
    return
    
label h_skirt_on:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = True
    call update_her_uniform
    show screen hermione_main
    with d5 
    return
    
label h_skirt_off:
    hide screen hermione_main
    with d5  
    $ hermione_wear_skirt = False
    call update_her_uniform
    show screen hermione_main
    with d5 
    return
    
###WEAR PANTIES
label h_panties_on:
    m "I want you to start wearing panties again"
    her "those boring old things"
    m "yep"
    her "do i get anything for this"
    menu:
        "hows 5 points sound":
            $ gryffindor += 5
            pass
        "nope just do it":
            pass
    her "fine I'll do it"
    $ h_request_wear_panties = True
    return
    
label h_panties_off:
    m "stop wearing those panties"
    her "freedom at last"
    $ h_request_wear_panties = False
    return
    
label h_badge_on(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = True
    $ h_badge = badge
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label h_badge_off(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = False
    $ h_badge = ""
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label set_h_underwear(bra="base_bra_white_1", panties="base_panties_1"):
    hide screen hermione_main
    with d5
    $ h_bra = bra
    $ h_panties = panties
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label set_h_hair(hair_style="A", color=1):
    hide screen hermione_main
    with d5
    $ h_hair_style = hair_style
    $ h_hair_color = color
    call h_update_hair
    show screen hermione_main
    with d5
    return
    
label set_h_hair_style(hair_style = "A"):
    hide screen hermione_main
    with d5
    $ h_hair_style = hair_style
    call h_update_hair
    show screen hermione_main
    with d5
    return
    
label set_h_hair_color(hair_color = 1):
    hide screen hermione_main
    with d5
    $ h_hair_color = hair_color
    call h_update_hair
    show screen hermione_main
    with d5
    return
    
label set_h_stockings(stocking = "00_blank"):
    hide screen hermione_main
    with d5
    if stocking == h_stocking:
        $ h_stocking = "00_blank"
    else:
        $ h_stocking = stocking
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label set_h_costume(costume_id = 0):
    hide screen hermione_main
    with d5
    call h_outfit_OBJ(costume_id)
    show screen hermione_main
    with d5
    return
    
label set_h_skirt(skirt = ""):
    hide screen hermione_main
    with d5
    $ h_skirt = skirt
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label set_h_skirt_color(color = ""):
    hide screen hermione_main
    with d5
    $ h_skirt_color = color
    call update_her_uniform
    show screen hermione_main
    with d5
    return

label set_h_top(top = ""):
    hide screen hermione_main
    with d5
    $ h_top = top[-1:]
    call update_chibi_uniform
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    

#$ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
label badge_take:
    call her_main("As you wish, [genie_name]...","body_01")
    $ badges = True
    $ ba_01 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
### FISHNETS ###
label nets_put:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("fishnet stockings...?","body_11")
        call her_main("You cannot be serious, [genie_name]!","body_31")
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                call her_main("Gladly...","body_69")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                call her_main("well, alright...","body_66")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 5
                call upset
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Hm...?","body_15")
        call her_main("I am not that kind of girl [genie_name]...","body_17")
        her "You may have better luck with someone from \"Slytherin\"..."
        menu:
            m "..."
            "\"Just put it on!\"":
                call her_main("[genie_name] this is hardly the appropriate attire for a Hogwarts student.","body_07")
                call her_main("I refuse!","body_09")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","body_07")
                call her_main("Well, in that case...","body_08")
                call her_main("As long as it benefits my house...","body_29")
            "\"Fine. Forget it\"":
                call her_main("Alright...","body_01")
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
    
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("Hm...?","body_15")
        call her_main("Fishnet stockings?","body_17")
        call her_main("I don't know about that [genie_name]...","body_29")
        m "..."
        menu:
            "\"Just put them on!\"":
                call her_main("Alright, alright...","body_69")
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                call her_main("Hm...","body_07")
                call her_main("Alright. I don't mind then.","body_68")
            "\"Fine. Forget it\"":
                call her_main("Oh...","body_13")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3            
        jump day_time_requests
    
    if whoring >= 18: # Lv 7+
        call her_main("If you insist, [genie_name]...","body_118")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_78"
    
    $ ne = True # Shows fishnets layer.
    $ ne_01 = True # Shows the fishnets.
    
    #$ legs_02 = True
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    pause.1
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
label nets_take:
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        call her_main("I'm glad that you came to your senses, [genie_name].","body_04")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "body_03"
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        call her_main("Gladly, [genie_name].","body_01")

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        call her_main("As you wish, [genie_name].","body_12")
    
    if whoring >= 18: # Lv 7+
        call her_main("Really? Aw...","body_28")
    
    
    $ ne = False # Shows fishnets layer.
    $ ne_01 = False # Shows the fishnets.
    #$ legs_02 = False
    #$ legs_03 = False
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    show screen hermione_main
    with d3
    jump day_time_requests


label give_her_acc(acc_id):
    hide screen hermione_main
    with d5
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if acc_id == 0:#SPEW BADGE
        if not hermione_badges or h_badge != "SPEW_badge":
            call her_main("A S.P.E.W. badge?","body_01")
            call her_main("I'll wear this with pride [genie_name].","body_16")
            call h_badge_on(badge = "SPEW_badge")
        else:
            call her_main("You want me to take it off?","body_01")
            call her_main("Alright [genie_name].","body_01")
            call h_badge_off(badge = "SPEW_badge")
    elif acc_id == 1:#CUM BADGE
        if not hermione_badges or h_badge != "CUM_badge":
            if whoring <= 7:
                jump too_much
            elif whoring <= 15:
                call her_main("An I love cum badge...?","body_11")
                call her_main("You cannot be serious, [genie_name]!","body_31")
                m "What's wrong?"
                call her_main("[genie_name] I am not going to wear a badge that says that I love cum!","body_07")
                call her_main("I absolutely refuse!","body_09")
                $ mad += 5
            else:
                call her_main("Hm...?","body_15")
                call her_main("An I love cum badge?","body_17")
                call her_main("{size=-5}(I suppose that it's not a complete lie...){/size}","body_59")
                call her_main("Ok, i'll wear it...","body_58")
                call h_badge_on(badge = "CUM_badge")
        else:
            call her_main("You want me to take it off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            call h_badge_off(badge = "CUM_badge")
    elif acc_id == 2:#Tiara
        if not hermione_hats:
            if whoring <= 15:
                call her_main("A tiara...?","body_11")
                call her_main("Hmmmmm","body_07")
                call her_main("I suppose I can wear it...","body_09")
                hide screen hermione_main
                with d5
                $ hermione_hats = True
                $ hermione_hat = "01_hp/13_characters/hermione/accessories/head/tiara.png"
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("A Tiara?","body_17")
                call her_main("let me just go put it on...","body_58")
                hide screen hermione_main
                with d5
                $ hermione_hats = True
                $ hermione_hat = "01_hp/13_characters/hermione/accessories/head/tiara.png"
                show screen hermione_main
                with d5
        else:
            call her_main("You want me to take it off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ hermione_hats = False
            show screen hermione_main
            with d5
    elif acc_id == 3:#Freckles
        if not hermione_freckles:
            if whoring <= 15:
                call her_main("Face paint...?","body_11")
                call her_main("Hmmmmm","body_07")
                call her_main("I suppose I can put a few dots on...","body_09")
                hide screen hermione_main
                with d5
                $ hermione_freckles = True
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("Face paint?","body_17")
                call her_main("alright then, let me just go put it on...","body_58")
                hide screen hermione_main
                with d5
                $ hermione_freckles = True
                show screen hermione_main
                with d5
        else:
            call her_main("You want me to wipe it off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ hermione_freckles = False
            show screen hermione_main
            with d5
    elif acc_id == 4:#Reading glasses
        if not hermione_wear_glasses or hermione_glasses != "01_hp/13_characters/hermione/accessories/head/reading_glasses.png":
            if whoring <= 15:
                call her_main("Reading glasses...?","body_11")
                call her_main("But I can see fine.","body_07")
                m "Don't worry, they're fake lenses."
                call her_main("well I suppose I can wear them then...","body_09")
                hide screen hermione_main
                with d5
                $ hermione_wear_glasses = True
                $ hermione_glasses = "01_hp/13_characters/hermione/accessories/head/reading_glasses.png"
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("Reading glasses?","body_17")
                call her_main("let me just go put them on...","body_58")
                hide screen hermione_main
                with d5
                $ hermione_wear_glasses = True
                $ hermione_glasses = "01_hp/13_characters/hermione/accessories/head/reading_glasses.png"
                show screen hermione_main
                with d5
        else:
            call her_main("You want me to take them off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ hermione_wear_glasses = False
            show screen hermione_main
            with d5
    elif acc_id == 5:#Dirty Hipster glasses
        if not hermione_wear_glasses or hermione_glasses != "01_hp/13_characters/hermione/accessories/head/vintage_glasses.png":
            if whoring <= 15:
                call her_main("Old glasses...?","body_11")
                call her_main("But I can see fine... Plus these are a bit old looking","body_07")
                m "Don't worry, they're back in fashion now."
                call her_main("well I suppose I can wear them then...","body_09")
                hide screen hermione_main
                with d5
                $ hermione_wear_glasses = True
                $ hermione_glasses = "01_hp/13_characters/hermione/accessories/head/vintage_glasses.png"
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("Glasses?","body_17")
                call her_main("let me just go put them on...","body_58")
                hide screen hermione_main
                with d5
                $ hermione_wear_glasses = True
                $ hermione_glasses = "01_hp/13_characters/hermione/accessories/head/vintage_glasses.png"
                show screen hermione_main
                with d5
        else:
            call her_main("You want me to take them off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ hermione_wear_glasses = False
            show screen hermione_main
            with d5
    elif acc_id == 6:#Fake cum
        if not hermione_cum:
            if whoring <= 10:
                jump too_much
            elif whoring <= 17:
                call her_main("Fake cum...?","body_11")
                call her_main("You cannot be serious, [genie_name]!","body_31")
                m "What's wrong? It's not real..."
                call her_main("[genie_name] I am not going to smear myself with cum, real or not, and then parade around the school!","body_07")
                call her_main("I absolutely refuse!","body_09")
                $ mad += 8
            elif whoring <=23:
                call her_main("Fake cum...?","body_15")
                call her_main("...","body_17")
                call her_main("well as long as it's not real...","body_58")
                hide screen hermione_main
                with d5
                $ hermione_cum = True
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("YOu want me to cover myself in fake cum?","body_17")
                call her_main("{size=-5}(It's a shame it's not real...){/size}","body_59")
                call her_main("Ok, i'll do it...","body_58")
                $ hermione_cum = True
        else:
            call her_main("You want me to take it off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ hermione_cum = False
            show screen hermione_main
            with d5
    elif acc_id == 7:#Cat ears
        if not cat_ears:
            if whoring <= 5:
                jump too_much
            elif whoring <= 17:
                call her_main("cat ears...?","body_11")
                call her_main("Really, [genie_name]!","body_31")
                m "What's wrong? They're cute..."
                call her_main("Fine...","body_69")
                $ cat_ears = True
            elif whoring <=23:
                call her_main("Cat ears...?","body_15")
                call her_main("...","body_17")
                call her_main("well I suppose they are a little cute...","body_58")
                hide screen hermione_main
                with d5
                $ cat_ears = True
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("Cat ears?","body_17")
                call her_main("{size=-5}(At least they match my hair...){/size}","body_59")
                call her_main("Alright then...","body_58")
                $ cat_ears = True
        else:
            call her_main("You want me to take them off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ cat_ears = False
            show screen hermione_main
            with d5
    elif acc_id == 8:#Transparent
        if transparency == 1:
            if whoring <= 15:
                jump too_much
            call her_main("You want me to make my clothes see through?","body_33")
            call her_main("Really, [genie_name]!","body_30")
            m "Just a little bit."
            call her_main("Fine...","body_08")
            call her_main("How much should I drink...","body_29")
            menu: 
                "-A little bit-":
                    $ transparency_amount = 0.8
                    call her_main("(at least This shouldn't be too noticable.","body_33")
                "-A fair bit-" if whoring >= 20:
                    $ transparency_amount = 0.5
                    call her_main("(Hopefully it's not too bad","body_29")
                "-A lot-" if whoring >= 23:
                    $ transparency_amount = 0.3
                    call her_main("(...)","body_59")
                "-All of it-" if whoring == 24:
                    $ transparency_amount = 0.1
                    call her_main("...","body_68")

            call her_main("Alright then...","body_73")
            hide screen hermione_main
            with d5
            $ transparency = transparency_amount
            $ hermione_breasts = "01_hp/13_characters/hermione/body/breasts/breasts_normal.png"
            show screen hermione_main
            with d5
        else:
            call her_main("You want me to wear new clothes?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ transparency = 1
            show screen hermione_main
            with d5
    elif acc_id == 9:#Elf ears
        if not elf_ears:
            if whoring <= 5:
                jump too_much
            elif whoring <= 17:
                call her_main("elf ears...?","body_11")
                call her_main("Really, [genie_name]!","body_31")
                m "What's wrong? don't you support the house elves or something..."
                call her_main("Fine...","body_69")
                $ elf_ears = True
            elif whoring <=23:
                call her_main("Elf ears...?","body_15")
                call her_main("...","body_17")
                call her_main("well I suppose they're not too noticable...","body_58")
                hide screen hermione_main
                with d5
                $ elf_ears = True
                show screen hermione_main
                with d5
            else:
                call her_main("Hm...?","body_15")
                call her_main("Elf ears?","body_17")
                call her_main("{size=-5}(They are kind of cute...){/size}","body_59")
                call her_main("Alright then...","body_58")
                $ elf_ears = True
        else:
            call her_main("You want me to take them off?","body_70")
            call her_main("Oh... alright then [genie_name].","body_71")
            hide screen hermione_main
            with d5
            $ elf_ears = False
            show screen hermione_main
            with d5

    


    
