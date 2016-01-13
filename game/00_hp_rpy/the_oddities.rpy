label __init_variables:
    if not hasattr(renpy.store,'gift_item_inv'): #important!
        $ gift_item_inv = []
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        $ gift_item_inv.append(0)
        #$ gift_item_inv.append(0)
    if not hasattr(renpy.store,'shop_found'): #important!
        $ shop_found = False
    if not hasattr(renpy.store,'store_gift_items'): #important!
        $ store_gift_items = []
    if not hasattr(renpy.store,'sscroll_'): #important!
        $ sscroll_ = []
    if not hasattr(renpy.store,'bought_glasses'): #important!
        $ bought_glasses = False
    
    $ store_gift_items = []
    $ store_gift_items.append("null")
    $ store_gift_items.append("lollipop candy")
    $ store_gift_items.append("Chocolate")
    $ store_gift_items.append("Plush owl")
    $ store_gift_items.append("Butterbeer")
    $ store_gift_items.append("Educational magazines")
    $ store_gift_items.append("Girly magazines")
    $ store_gift_items.append("Adult magazines")
    $ store_gift_items.append("Porn magazines")
    $ store_gift_items.append("Viktor Krum Poster")
    $ store_gift_items.append("Sexy lingerie")
    $ store_gift_items.append("A pack of condoms")
    $ store_gift_items.append("Vibrator")
    $ store_gift_items.append("Jar of anal lubricant")
    $ store_gift_items.append("Ball gag and cuffs")
    $ store_gift_items.append("Anal plugs")
    $ store_gift_items.append("Thestral Strap-on")
    $ store_gift_items.append("Lady Speed Stick-2000")
    $ store_gift_items.append("Sex doll \"Joanne\"")
    #$ store_gift_items.append("anal_beads")
    
    $ gift_description = []
    $ gift_description.append("invalid item")
    $ gift_description.append("A lollipop candy. An adult candy for kids or kids candy for adults?")
    $ gift_description.append("The recipe for this delicious milk chocolate is kept a secret. (Rumoured to contain dried faeries).")
    $ gift_description.append("a Toy owl stuffed with feathers of an actual owl. It's so cuddly!")
    $ gift_description.append("Girls can't resist this beverage's buttery texture. Therefore it's always in high demand among the boys. \n{size=-4}Warning: no underage drinking is allowed without adults present.{/size}")
    $ gift_description.append("Educational magazines. \nthe Trusty companions of every social outcast.")
    $ gift_description.append("Girly magazines. \nAll cool girls are reading these.")
    $ gift_description.append("Your boyfriend is turning into a nice guy? \nYour husband won't abuse you anymore? \nAll you wanted to know about relationships, love and sex. Mostly about sex.")
    $ gift_description.append("Give these to your girlfriend to test her, to your wife to shame her and to your daughter to avoid \"the talk\".")
    $ gift_description.append("A skilled Quidditch Seeker, Viktor has been selected to play for the Bulgarian National Quidditch team despite still going to school, and is widely regarded as one of the best players in the world.")
    $ gift_description.append("Sexy lingerie \"Fairy Godmother\". Charm your wizard in bed or empress your sisters at a Sabbath.")
    $ gift_description.append("\"Pink unicorn condoms\". \nUnleash the one-horned beast!\n{size=-4}May contain traces of actual unicorn saliva.{/size}")
    $ gift_description.append("A magnificent, magically enhanced vibrator made of vine wood, with a dragon heartstring core.")
    $ gift_description.append("A Jar of anal lube, Buy this for your loved one - show that you care.")
    $ gift_description.append("Ball gag and cuffs, Turn your soulmate into your cellmate.")
    $ gift_description.append("Anal plugs decorated with actual tails. \nSizes vary to satisfy expert practitioners and beginner alike.")
    $ gift_description.append("Thestral strap-on.\nWhen you see it, you'll shit bricks.")
    $ gift_description.append("The \"Lady Speed Stick-2000\", an elegant way of transportation for passionate witches. The trademarked saddle guarantees full satisfaction. Get one for your witch and she won't use her boring old broom ever again!")
    $ gift_description.append("Sex doll \"Joanne\"... It's so realistic. Almost looks like a real human under the influence of a spell of some sort.")
    #$ gift_description.append("Anal beads engraved with a strange inscription \"Property of L.C.\".")
    return

label shop_fake:
    $ show_clothes_store = True
    $ shop_found = True
    sna_[1] "Genie? What the hell are you doing here? I thought I told you not to leave your office."
    sna_[1] "What if someone sees you?"
    m "You expected me to stay cramped office for months? Besides, I look like Dumbdoor, no one will be able to tell the difference"
    sna_[1] "It's Dumbledore and stuff like that is exactly why you have to stay in your office."
    sna_[1] "You have no idea what you are talking about. Any student will be able to tell that you're an imposter."
    m "Fine, fine, I'll go back to my office. Let's talk a bit first though, being stuck in that office is making me go crazy."
    sna_[1] "Alright, how's Miss Granger going?"
    m "She's coming along. So what are you doing here? This looks like some sort of shop."
    sna_[1] "As head of potions it's my job to run the potions cupboard for an hour each afternoon."
    m "Why? Surely people can get their own ingredients?"
    sna_[1] "It's not that simple. A lot of ingredients that are essential for standard potions also have more nefarious uses."
    sna_[1] "If left unregulated students could brew some very dangerous concoctions."
    m "Well I guess that makes sense. Is that all you sell?"
    sna_[1] "I also brew potions and sell scrolls and textbooks to potions."
    m "What sort of potions do you make?"
    sna_[1] "Most of the time I just make the bases to potions."
    m "Bases?"
    sna_[1] "Essentially I make most of a potion and then it is finished by adding a few ingredients."
    sna_[1] "It helps preserve the potion as well as allows for the user to change the effect."
    m "Well that's all pretty dull. Do you sell anything \"Interesting\"?"
    sna_[1] "Interesting?"
    m "You know, sex potions, stuff that would help us corrupt Miss Granger."
    sna_[1] "Ah, well I know a few potions that you might like."
    m "Such as?"
    sna_[1] "Well, I don't have a the ingredients to make stronger potions but I can make you a potion that will change her hair color."
    m "Hmmmm, you don't have anything better?"
    sna_[1] "Not at the moment. I'll have to order the ingredients in."
    m "How long will that take."
    sna_[1] "It depends on the items. Some of them are very hard to come by."
    sna_[1] "As a result I will have to charge you for them, but from what I've heard that shouldn't be a problem."
    m "Fair enough. Before I buy though are there any other stores on campus?"
    sna_[1] "Only a tailor, why?"
    m "Just making sure that there isn't a cheaper alternative."
    sna_[1] "There isn't, now are you going to buy anything or not?"
    show screen shop_screen
    call screen shop_screen 

label shop_menu:
    if not shop_found:
        jump shop_fake
    show screen shop_screen
    sna_[1] "Hey Genie, what would you like to buy?"
    call screen shop_screen

label shop_books:
    sna_[1] "What type of book would you like?"
    menu:
        "-Educational Books-":
            jump education_menu
        "-Fictional Books-":
            sna_[1] "These books are mostly light erotica..." 
            sna_[20] "Some of the girls insisted that I order them in."
            jump fiction_menu
        "-Never mind-":
            call screen shop_screen

label shop_potion_menu:
    menu:
        "-Questions aquireing items-":
            menu:
                "-Knotgrass-":
                    m "Do you know where I can find \"Knotgrass\""
                    sna_[6] "You can sometimge find Knotgrass by the forbidden forest"
                    jump shop_potion_menu
                "-Root of Aconite-":
                    m "Do you know where I can find \"Root of Aconite\""
                    sna_[6] "Root of Aconite can be found down by the lake"
                    jump shop_potion_menu
                "-Wormwood-":
                    m "Do you know where I can find \"Wormwood\""
                    sna_[6] "Wormwood is sometimes found in the forbidden forest"
                    jump shop_potion_menu
                "-Niffler's Fancy-":
                    m "Do you know where I can find \"Niffler's Fancy\""
                    sna_[6] "hmm i think i heard that it's found by the lake"
                    jump shop_potion_menu
                
        "{color=#858585}-Polyjuice Potion-{/color}" if whoring < 5:
            call cust_excuse("Hermione mus be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Polyjuice Potion-" if whoring >= 5:
            menu:
                "-Buy the potion for 100 Gold-":
                    if gold >= 100:
                        $ gold -= 100
                        $ p_inv.append("Polyjuice Potion")
                        m "Polyjuice potion aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "{color=#858585}-Transparent Tincture-{/color}" if whoring < 3:
            call cust_excuse("Hermione mus be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Transparent Tincture-" if whoring >= 3:
            menu:
                "-Buy the potion for 75 Gold-":
                    if gold >= 75:
                        $ gold -= 75
                        $ p_inv.append("Transparent Tincture")
                        m "Transparent Tincture aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "{color=#858585}-Expanding Elixir-{/color}" if whoring < 8:
            call cust_excuse("Hermione mus be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Expanding Elixir-" if whoring >= 8:
            menu:
                "-Buy the potion for 150 Gold-":
                    if gold >= 150:
                        $ gold -= 150
                        $ p_inv.append("Expanding Elixir")
                        m "Expanding Elixir aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "{color=#858585}-Moreish Mead-{/color}" if whoring < 14:
            call cust_excuse("Hermione mus be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Moreish Mead-" if whoring >= 14:
            menu:
                "-Buy the potion for 200 Gold-":
                    if gold >= 200:
                        $ gold -= 200
                        $ p_inv.append("Moreish Mead")
                        m "Moreish Mead aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "-Never mind-":
            call screen shop_screen
    
    
    
label the_oddities:
    menu:
        dahr "Welcome to the \"Muggle oddities catalog\". Your taste is never too odd for us!"
        
        "-Educational Books-":
            label education_menu:
            menu:  
                "-Book: [book_name[1]]-" if not "book_1" in books: # Copper book of spirit [1]
                    call book_block(1,40)
                    jump education_menu
                "-Book: [book_name[2]]-" if not "book_2" in books: # Bronze book of spirit [2]
                    call book_block(2,80)
                    jump education_menu
                "-Book: [book_name[3]]-" if not "book_3" in books: # Silver book of spirit [3]
                    call book_block(3,90)
                    jump education_menu
                "-Book: [book_name[4]]-" if not "book_4" in books: # Golden book of spirit [4]
                    call book_block(4,100)
                    jump education_menu
                "-Book: [book_name[5]]-" if not "book_5" in books: # Speedwriting for beginners [5]
                    call book_block(5,90)
                    jump education_menu 
                "-Book: [book_name[6]]-" if not "book_6" in books: # Speedwriting for amateurs [6]
                    call book_block(6,100)
                    jump education_menu
                "-Book: [book_name[7]]-" if not "book_7" in books: # Speedwriting for advanced writers [7]
                    call book_block(7,130)
                    jump education_menu
                "-Book: [book_name[8]]-" if not "book_8" in books: # Speedwriting for experts [8]
                    call book_block(8,175)
                    jump education_menu 
                "-Never mind-":
                    jump shop_menu
         
        "-Fiction books-":
            label fiction_menu:
            menu:
                "-Book: [book_name[11]]- {image=check_07}" if not "book_11" in books: # The game of chairs [11]
                    call book_block(11,100)
                    jump fiction_menu
                "-Book: [book_name[11]]- {image=check_08}-" if "book_11" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
            
                "-Book: [book_name[9]]- {image=check_07}" if not "book_9" in books: # The Tale of Galadriel [9]
                    call book_block(9,200)
                    jump fiction_menu
                "-Book: [book_name[9]]- {image=check_08}-" if "book_9" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
               
                "-Book: [book_name[10]]- {image=check_07}" if not "book_10" in books: # The Tale of Galadriel. BOOK TWO [10]
                    call book_block(10,250)
                    jump fiction_menu
                "-Book: [book_name[10]]- {image=check_08}" if "book_10" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
               
                "-Book: [book_name[12]]- {image=check_07}-" if not "book_12" in books: # My dear waifu [12]
                    call book_block(12,300)
                    jump fiction_menu
                "-Book: [book_name[12]]- {image=check_08}" if "book_12" in books:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
                
                "-Never mind-":
                    jump shop_menu
         
        "-Gifts-":
            label gifts_menu:
            menu:
                #dahr "Gifts that you can gift to that special someone."
                
                "-A lollipop candy- (20 g.)":
                    call gift_block(1,20)
                "-Chocolate- (40 g.)":
                    call gift_block(2,40)
                "-Stuffed Owl- (35 g.)":
                    call gift_block(3,35)
                
                "{color=#858585}-Item is out of stock-{/color}" if whoring < 3:
                    call out # Message "Item us out of stock".
                "-Butterbeer- (50 g.)" if whoring >= 3:
                    call gift_block(4,50)
                
                "-Educational magazines- (30 g.)":
                    call gift_block(5,30)
                "-Girly magazines- (45 g.)":
                    call gift_block(6,45)
                "-Adult magazines- (60 g.)":
                    call gift_block(7,60)
                
                "{color=#858585}-Item is out of stock-{/color}" if whoring < 3:
                    call out # Message "Item us out of stock".
                "-Porn magazines- (80 g.)" if whoring >= 3:
                    call gift_block(8,80)
                
                "{color=#858585}-Item is out of stock-{/color}" if whoring < 3:
                    call out # Message "Item us out of stock".
                "-A pack of condoms- (50 g.)" if whoring >= 3:
                    call gift_block(11,50)
                
                "{color=#858585}-Item is out of stock-{/color}" if whoring < 3:
                    call out # Message "Item us out of stock".
                "-Vibrator- (55 g.)" if whoring >= 3:
                    call gift_block(12,55)
                
                "-A jar of anal lubricant- (60 g.)":
                    call gift_block(13,60)
                "-Ball gag and cuffs- (70 g.)":
                    call gift_block(14,70)
                
                "{color=#858585}-Item is out of stock-{/color}" if whoring < 3:
                    call out # Message "Item us out of stock".
                "-Anal plugs- (85 g.)" if whoring >= 3:
                    call gift_block(15,85)
                
                "{color=#858585}-Item is out of stock-{/color}" if whoring < 3:
                    call out # Message "Item us out of stock".
                "-Thestral Strap-on- (200 g.)" if whoring >= 3:
                    call gift_block(16,200)
                "-Never mind-":
                    hide screen gift
                    with d3
                    jump shop_menu
        
        "-Apparel-":
            label app:
                pass
            menu:
                "-\"S.P.E.W.\" badge (100 gold)-" if not badge_01 == 7:
                    $ the_gift = "01_hp/18_store/29.png" # SPEW BADGE.
                    show screen gift
                    with d3
                    dahr "A \"S.P.E.W.\" badge. Pretend that you care..."
                    menu:
                        "-Buy the item (100 gold)-":
                            if badge_01 == 7 or badge_01 == 1: # == 7 means "gifted already" # badge_01 == 1 because otherwise you could still buy it in the shop, even if you have 1 already.
                                call do_have_book # "I already own this one."
                                jump app
                            else:
                                if gold >= 100:
                                    $ gold -=100
                                    $ order_placed = True
                                    $ bought_badge_01 = True #Affects 15_mail.rpy
                                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                    call screen shop_screen
                                else:
                                    call no_gold #Massage: m "I don't have enough gold".
                                    hide screen gift
                                    with d3
                                    jump app
                        "-Never mind-":
                            hide screen gift
                            with d3
                            jump app
                "-Glasses- (60 g.)":
                    $ the_gift = "01_hp/18_store/glasses.png" # GLASSES
                    show screen gift
                    with d3
                    call glasses_text
                    menu:
                        "-Buy the item (60 gold)-":
                            if gold >= 60:
                                $ gold -= 60
                                $ order_placed = True
                                $ bought_glasses = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                call screen shop_screen
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                jump app
                        "-Never mind-":
                            hide screen gift
                            jump app            
                "-Fishnet stokings (800 gold)-" if not nets == 7:
                    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
                    show screen gift
                    with d3
                    call nets_text
                    menu:
                        "-Buy the item (800 gold)-":
                            if nets == 7 or nets == 1: # == 7 means "gifted already"
                                call do_have_book # "I already own this one."
                                jump app
                            else:
                                if gold >= 800:
                                    $ gold -= 800
                                    $ order_placed = True
                                    $ bought_nets = True #Affects 15_mail.rpy
                                    call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                    call screen shop_screen
                                else:
                                    call no_gold #Massage: m "I don't have enough gold".
                                    hide screen gift
                                    with d3
                                    jump app
                        "-Never mind-":
                            hide screen gift
                            with d3
                            jump app
                "-School Miniskirt- (---)" if not bought_skirt_already and not gave_miniskirt and whoring >= 3:
                    $ the_gift = "01_hp/18_store/07.png" # MINISKIRT
                    show screen gift
                    with d3
                    dahr "School miniskirt. Improves grades drastically."
                    menu:
                        "-Buy the skirt- (---)":
                            if vouchers >= 1: #Shows the amount of DAHR's vouchers in your possession.
                                $ vouchers -= 1 #Shows the amount of DAHR's vouchers in your possession.
                                $ order_placed = True
                                $ bought_miniskirt = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                call screen shop_screen
                            else:
                                dahr "This item is only redeemable with a \"DAHR's voucher\"."
                                hide screen gift
                                with d3
                                jump app
                        "-Never mind-":
                            hide screen gift
                            with d3
                            jump app
                "-Item Sold Out-" if bought_dress_already:
                    "This item has been sold out."
                    jump app
                "{color=#858585}-Item is out of stock-{/color}" if not sorry_for_hesterics: # NIGHT DRESS.
                    call out # Message "Item us out of stock".
                "-The Ball Dress- (1500 gold)" if sorry_for_hesterics and not bought_dress_already:
                    $ the_gift = "01_hp/18_store/01.png" # DRESS.
                    show screen gift
                    with d3
                    dahr "A nightdress for special occasions."
                    menu:
                        "-Buy the dress (1500 gold)-":
                            if gold >= 1500:
                                $ gold -=1500
                                $ order_placed = True
                                $ bought_ball_dress = True #Affects 15_mail.rpy
                                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                                call screen shop_screen
                            else:
                                call no_gold #Massage: m "I don't have enough gold".
                                hide screen gift
                                with d3
                                jump app
                        "-Never mind-":
                            hide screen gift
                            with d3
                            jump app
                "-Never mind-":
                        jump shop_menu
                        
        "-Sacred scrolls Volume I-":
            label sscrolls:
            menu:
                "-S.01: [scroll_name_[1]]-" if not sscroll_[1]:
                    call scroll_block(1,10)
                    jump sscrolls
                "-S.02: [scroll_name_[2]]-" if not sscroll_[2]:
                    call scroll_block(2,30)
                    jump sscrolls
                "-S.03: [scroll_name_[3]]-" if not sscroll_[3]:
                    call scroll_block(3,40)
                    jump sscrolls
                "-S.04: [scroll_name_[4]]-" if not sscroll_[4]:
                    call scroll_block(4,70)
                    jump sscrolls
                "-S.05: [scroll_name_[5]]-" if not sscroll_[5]:
                    call scroll_block(5,80)
                    jump sscrolls
                "-S.06: [scroll_name_[6]]-" if not sscroll_[6]:
                    call scroll_block(6,80)
                    jump sscrolls
                "-S.07: [scroll_name_[7]]-" if not sscroll_[7]:
                    call scroll_block(7,90)
                    jump sscrolls
                "-S.08: [scroll_name_[8]]-" if not sscroll_[8]:
                    call scroll_block(8,50)
                    jump sscrolls
                "-S.09: [scroll_name_[9]]-" if not sscroll_[9]:
                    call scroll_block(9,90)
                    jump sscrolls
                "-S.10: [scroll_name_[10]]-" if not sscroll_[10]:
                    call scroll_block(10,50)
                    jump sscrolls
                "-S.11: [scroll_name_[11]]-" if not sscroll_[11]:
                    call scroll_block(11,110)
                    jump sscrolls
                "-S.12: [scroll_name_[12]]-" if not sscroll_[12]:
                    call scroll_block(12,110)
                    jump sscrolls
                "-S.13: [scroll_name_[13]]-" if not sscroll_[13]:
                    call scroll_block(13,100)
                    jump sscrolls
                "-S.14: [scroll_name_[14]]-" if not sscroll_[14]:
                    call scroll_block(14,80)
                    jump sscrolls
                "-S.15: [scroll_name_[15]]-" if not sscroll_[15]:
                    call scroll_block(15,40)
                    jump sscrolls
                "-Never mind-":
                    jump shop_menu
                    
        "-Sacred scrolls Volume II-":
            label sscrolls2:
            menu:
                "-S.16: [scroll_name_[16]]-" if not sscroll_[16]:
                    call scroll_block(16,30)
                    jump sscrolls
                "-S.17: [scroll_name_[17]]-" if not sscroll_[17]:
                    call scroll_block(17,30)
                    jump sscrolls
                "-S.18: [scroll_name_[18]]-" if not sscroll_[18]:
                    call scroll_block(18,90)
                    jump sscrolls
                "-S.19: [scroll_name_[19]]-" if not sscroll_[19]:
                    call scroll_block(19,50)
                    jump sscrolls
                "-S.20: [scroll_name_[20]]-" if not sscroll_[20]:
                    call scroll_block(20,70)
                    jump sscrolls
                "-S.21: [scroll_name_[21]]-" if not sscroll_[21]:
                    call scroll_block(21,90)
                    jump sscrolls
                "-S.22: [scroll_name_[22]]-" if not sscroll_[22]:
                    call scroll_block(22,90)
                    jump sscrolls
                "-S.23: [scroll_name_[23]]-" if not sscroll_[23]:
                    call scroll_block(23,150)
                    jump sscrolls
                "-S.24: [scroll_name_[24]]-" if not sscroll_[24]:
                    call scroll_block(24,150)
                    jump sscrolls
                "-S.25: [scroll_name_[25]]-" if not sscroll_[25]:
                    call scroll_block(25,100)
                    jump sscrolls
                "-S.26: [scroll_name_[26]]-" if not sscroll_[26]:
                    call scroll_block(26,80)
                    jump sscrolls
                "-S.27: [scroll_name_[27]]-" if not sscroll_[27]:
                    call scroll_block(27,200)
                    jump sscrolls2
                "-S.28: [scroll_name_[28]]-" if not sscroll_[28]:
                    call scroll_block(28,150)
                    jump sscrolls2
                "-S.29: [scroll_name_[29]]-" if not sscroll_[29]:
                    call scroll_block(29,200)
                    jump sscrolls2
                "-S.30: [scroll_name_[30]]-" if not sscroll_[30]:
                    call scroll_block(30,70)
                    jump sscrolls2
                "-Never mind-":
                    jump shop_menu
        
        "-Never mind-":
            call screen shop_screen
    
label book_block(book_id, book_cost):
    if book_id in fiction_books:
        if book_id == 9:
            $ the_gift = "01_hp/18_store/04.png"
        if book_id == 10:
            $ the_gift = "01_hp/18_store/05.png"
        if book_id == 11:
            $ the_gift = "01_hp/18_store/02.png"
        if book_id == 12:
            $ the_gift = "01_hp/18_store/03.png"
    else:
        $ the_gift = "01_hp/18_store/08.png"
    show screen gift
    with d3
    $ temp_str = str(book_description[book_id])
    ">[temp_str]"
    menu:
        "-Buy the book for [book_cost] gold -":
            if gold >= book_cost:
                $ gold -= book_cost
                $ order_placed = True
                $ bought_book[book_id] = True #Affects 15_mail.rpy
                call thx_4_shoping #Massage that says "Thank you for shopping here!".
                call screen shop_screen
            else:
                call no_gold #Massage: m "I don't have enough gold".
                return
        "-Never mind-":
            hide screen gift
            return
    
label gift_block(item_id, item_cost):
    $ the_gift = "01_hp/18_store/gifts/"+str(item_id)+".png"
    show screen gift
    with d3
    $ tmp = gift_description[item_id]
    dahr "[tmp]"
    $ price2 = item_cost*2
    $ price3 = item_cost*4
    $ price4 = item_cost*8
    menu:
        "-Buy 1 for ([item_cost] galleons)-":
            $ order_item = item_id
            $ order_quantity = 1
            call purchase_item(item_id,item_cost)
        "-Buy 2 for ([price2] galleons)-":
            $ order_item = item_id
            $ order_quantity = 2
            call purchase_item(item_id,price2)
        "-Buy 4 for ([price3] galleons)-":
            $ order_item = item_id
            $ order_quantity = 4
            call purchase_item(item_id,price3)
        "-Buy 8 for ([price4] galleons)-":
            $ order_item = item_id
            $ order_quantity = 8
            call purchase_item(item_id,price4)
        "-Never mind-":
            hide screen gift
            call gifts_menu
    
label purchase_item(item_id, order_cost):
    if gold >= (order_cost):
        menu:
            "-add next day delivery (15 galleons)-" if gold >= order_cost + 15:
                $ gold -= 15
                $ next_day = True
            "{color=#858585}-add next day delivery (15 galleons)-{/color}" if gold < order_cost + 15:
                pass
            "-no thanks-":
                pass
        $ gold -= order_cost
        $ order_placed = True
        call thx_4_shoping
        jump shop_menu
    else:
        $ order_item = 0
        call no_gold #Massage: m "I don't have enough gold".
        jump gifts_menu
    
label scroll_block(scroll_id, scroll_cost):
    $ the_gift = "01_hp/18_store/31.png" # SACRED SCROLL.
    show screen gift
    with d3
    dahr "A scroll containing sacred knowledge.\n(May also contain spoilers)."
    menu:
        "-Buy the scroll ([scroll_cost] gold)-":
            if gold >= scroll_cost:
                $ gold -= scroll_cost
                $ sscroll_[scroll_id] = True # Turns TRUE if the scroll had been bought.
                $ renpy.play('sounds/win_04.mp3')   #Not loud.
                call sscroll_bought
                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                call screen shop_screen
            else:
                call no_gold #Massage: m "I don't have enough gold".
                hide screen gift
                return
        "-Never mind-":
            hide screen gift
            return
    
### ALREADY HAVE THIS BOOK
label do_have_book:
    show screen bld1
    m "I already own this one."
    hide screen bld1
    hide screen gift
    with d3
    return
### THANK YOU FOR shopping here.
label thx_4_shoping:
    $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.

    if one_of_five ==  1:
        dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered tomorrow."
        hide screen gift
        with d3
        return
    else:
        dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered in 1 to [one_of_five] days."
        hide screen gift
        with d3
        return
    
### THANK YOU FOR shopping here. IMMEDIATE DELIVERY.
label thx_4_shoping2:
    dahr "Thank your for shopping at \"Dahr's oddities\"."
    hide screen gift
    with d3
    return
### NOT ENOUGH GOLD ###
label no_gold:
    m "I don't have enough gold... This is depressing..."
    hide screen gift
    with d3
    return
    
### ITEM IS OUT OF STOCK ###

label out:
    show screen bld1
    with d3
    dahr "This item is currently out of stock."
    hide screen bld1
    with d3
    jump gifts_menu
    
    
### BOUGHT SACRED SCROLL MESSAGE ###
label sscroll_bought:
    ">A New scroll has been added to your sacred scrolls collection."
    hide screen gift
    with d3
    return