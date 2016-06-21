init python:
    
    class gift_item(object):
        id = 0
        cost = 0
        name = ""
        image = ""
        description = ""
        whoringNeeded = 0
        users = [] # characters that can use this item
        
        def canUse(character_name):
            return character_name in users
        
        def costOf(number_of_item):
            return cost * number_of_item
    
    
    
    Lollipop = gift_item()
    Lollipop.id = 0
    Lollipop.cost = 20
    Lollipop.name = "lollipop candy"
    Lollipop.image = "01_hp/18_store/gifts/1.png"
    Lollipop.description = "A lollipop candy. An adult candy for kids or kids candy for adults?"
    Lollipop.users = ["hermione"]
    
    
    Chocolate = gift_item()
    Chocolate.id = 1
    Chocolate.cost = 40
    Chocolate.name = "Chocolate"
    Chocolate.image = "01_hp/18_store/gifts/2.png"
    Chocolate.description = "The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries)."
    
    PlushOwl = gift_item()
    PlushOwl.id = 2
    PlushOwl.cost = 35
    PlushOwl.name = "Plush owl"
    PlushOwl.image = "01_hp/18_store/gifts/3.png"
    PlushOwl.description = "a Toy owl stuffed with feathers of an actual owl. It's so cuddly!"
    
    Butterbeer = gift_item()
    Butterbeer.id = 3
    Butterbeer.cost = 50
    Butterbeer.whoringNeeded = 3
    Butterbeer.name = "Butterbeer"
    Butterbeer.image = "01_hp/18_store/gifts/4.png"
    Butterbeer.description = "Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}"
    
    EducationalMagazines = gift_item()
    EducationalMagazines.id = 4
    EducationalMagazines.cost = 30
    EducationalMagazines.name = "Educational magazines"
    EducationalMagazines.image = "01_hp/18_store/gifts/5.png"
    EducationalMagazines.description = "Educational magazines. \nthe Trusty companions of every social outcast."
    
    GirlyMagazines = gift_item()
    GirlyMagazines.id = 5
    GirlyMagazines.cost = 45
    GirlyMagazines.name = "Girly magazines"
    GirlyMagazines.image = "01_hp/18_store/gifts/6.png"
    GirlyMagazines.description = "Girly magazines. \nAll cool girls are reading these."
    
    AdultMagazines = gift_item()
    AdultMagazines.id = 6
    AdultMagazines.cost = 60
    AdultMagazines.name = "Adult magazines"
    AdultMagazines.image = "01_hp/18_store/gifts/7.png"
    AdultMagazines.description = "Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex."
    
    PornMagazines = gift_item()
    PornMagazines.id = 7
    PornMagazines.cost = 80
    PornMagazines.whoringNeeded = 3
    PornMagazines.name = "Porn magazines"
    PornMagazines.image = "01_hp/18_store/gifts/8.png"
    PornMagazines.description = "Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\"."
    
    ViktorKrumPoster = gift_item()
    ViktorKrumPoster.id = 8
    ViktorKrumPoster.cost = 25 #placeholder number
    ViktorKrumPoster.name = "Viktor Krum Poster"
    ViktorKrumPoster.image = "01_hp/18_store/gifts/9.png"
    ViktorKrumPoster.description = "A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world."
    
    SexyLingerie = gift_item()
    SexyLingerie.id = 9
    SexyLingerie.cost = 75 #placeholder number
    SexyLingerie.name = "Sexy lingerie"
    SexyLingerie.image = "01_hp/18_store/gifts/10.png"
    SexyLingerie.description = "Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath."
    
    PackOfCondoms = gift_item()
    PackOfCondoms.id = 0
    PackOfCondoms.cost = 50
    PackOfCondoms.whoringNeeded = 3
    PackOfCondoms.name = "A pack of condoms"
    PackOfCondoms.image = "01_hp/18_store/gifts/11.png"
    PackOfCondoms.description = "\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}"
    
    Vibrator = gift_item()
    Vibrator.id = 10
    Vibrator.cost = 55
    Vibrator.whoringNeeded = 3
    Vibrator.name = "Vibrator"
    Vibrator.image = "01_hp/18_store/gifts/12.png"
    Vibrator.description = "A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core."
    
    JarOfLube = gift_item()
    JarOfLube.id = 11
    JarOfLube.cost = 60
    JarOfLube.name = "Jar of anal lubricant"
    JarOfLube.image = "01_hp/18_store/gifts/13.png"
    JarOfLube.description = "A Jar of anal lube, Buy this for your loved one - show that you care."
    
    BallGagAndCuffs = gift_item()
    BallGagAndCuffs.id = 12
    BallGagAndCuffs.cost = 70
    BallGagAndCuffs.name = "Ball gag and cuffs"
    BallGagAndCuffs.image = "01_hp/18_store/gifts/14.png"
    BallGagAndCuffs.description = "Ball gag and cuffs, Turn your soulmate into your cellmate."
    
    AnalPlugs = gift_item()
    AnalPlugs.id = 13
    AnalPlugs.cost = 85
    AnalPlugs.whoringNeeded = 3
    AnalPlugs.name = "Anal plugs"
    AnalPlugs.image = "01_hp/18_store/gifts/15.png"
    AnalPlugs.description = "Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike."
    
    ThestralStrapon = gift_item()
    ThestralStrapon.id = 14
    ThestralStrapon.cost = 200
    ThestralStrapon.whoringNeeded = 3
    ThestralStrapon.name = "Thestral Strap-on"
    ThestralStrapon.image = "01_hp/18_store/gifts/16.png"
    ThestralStrapon.description = "Thestral strap-on.\nWhen you see it, you'll shit bricks."
    
    SpeedStick2000 = gift_item()
    SpeedStick2000.id = 15
    SpeedStick2000.cost = 500
    SpeedStick2000.name = "Lady Speed Stick-2000"
    SpeedStick2000.image = "01_hp/18_store/gifts/17.png"
    SpeedStick2000.description = "The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!"
    
    SexDollJoanne = gift_item()
    SexDollJoanne.id = 16
    SexDollJoanne.cost = 350
    SexDollJoanne.name = "Sex doll \"Joanne\""
    SexDollJoanne.image = "01_hp/18_store/gifts/18.png"
    SexDollJoanne.description = "Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort."
    
    AnalBeads = gift_item()
    AnalBeads.id = 17
    AnalBeads.cost = 65 #placeholder number
    AnalBeads.name = "Anal beads"
    AnalBeads.image = "01_hp/18_store/gift_anal_beads.png"
    AnalBeads.description = "Anal beads engraved with a strange inscription \"Property of L.C.\"."
    
    
    gift_list = []
    gift_list.append(Lollipop)
    gift_list.append(Chocolate)
    gift_list.append(PlushOwl)
    gift_list.append(Butterbeer)
    gift_list.append(EducationalMagazines)
    gift_list.append(GirlyMagazines)
    gift_list.append(AdultMagazines)
    gift_list.append(PornMagazines)
    gift_list.append(ViktorKrumPoster)
    gift_list.append(SexyLingerie)
    gift_list.append(PackOfCondoms)
    gift_list.append(Vibrator)
    gift_list.append(JarOfLube)
    gift_list.append(BallGagAndCuffs)
    gift_list.append(AnalPlugs)
    gift_list.append(ThestralStrapon)
    gift_list.append(SpeedStick2000)
    