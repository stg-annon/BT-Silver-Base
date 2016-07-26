label __init_variables:
    if not hasattr(renpy.store,'gift_item_inv'): #important! Gift_Item.ID == Index in this array
        $ gift_item_inv = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    if not hasattr(renpy.store,'shop_found'): #important!
        $ shop_found = False
    if not hasattr(renpy.store,'bought_glasses'): #important!
        $ bought_glasses = False
    if not hasattr(renpy.store,'sscroll_'): #important!
        $ sscroll_ = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    
    $ scroll_name = []
    $ scroll_name.append("null")
    $ scroll_name.append("The room")
    $ scroll_name.append("The calendar")
    $ scroll_name.append("The girl")
    $ scroll_name.append("Deeptroating")
    $ scroll_name.append("Poster 01")
    $ scroll_name.append("Poster 02")
    $ scroll_name.append("Chibi-dancing")
    $ scroll_name.append("Game items")
    $ scroll_name.append("Panties no panties")
    $ scroll_name.append("A lot of pegs")
    $ scroll_name.append("House-elf brothel")
    $ scroll_name.append("Me and Lola")
    $ scroll_name.append("Hard training")
    $ scroll_name.append("Wizard's Chess")
    $ scroll_name.append("Tutoring books")
    $ scroll_name.append("Extra gifts 01")
    $ scroll_name.append("Extra gifts 02")
    $ scroll_name.append("Fiction books")
    $ scroll_name.append("Singer whore")
    $ scroll_name.append("Casting")
    $ scroll_name.append("Witch robe 01")
    $ scroll_name.append("Witch robe 02")
    $ scroll_name.append("Witch robe 03")
    $ scroll_name.append("Witch robe 04")
    $ scroll_name.append("The walk")
    $ scroll_name.append("Durmstrang")
    $ scroll_name.append("Gag ball")
    $ scroll_name.append("New clothes 01")
    $ scroll_name.append("New clothes 02")
    $ scroll_name.append("The gang")
    return
    
label shop_intro:
    show screen shop_screen
    if shop_found:
        sna_[1] "Hey Genie, what would you like to buy?"
        jump shop_menu
    else:
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
        jump shop_menu
    
label shop_menu:
    show screen shop_screen
    call screen shop_screen
    
    
    
label sscrolls:
    show screen shop_screen
    menu:
        "-S.01: [scroll_name[1]]-" if not sscroll_[1]:
            call scroll_block(1,10)
            jump sscrolls
        "-S.02: [scroll_name[2]]-" if not sscroll_[2]:
            call scroll_block(2,30)
            jump sscrolls
        "-S.03: [scroll_name[3]]-" if not sscroll_[3]:
            call scroll_block(3,40)
            jump sscrolls
        "-S.04: [scroll_name[4]]-" if not sscroll_[4]:
            call scroll_block(4,70)
            jump sscrolls
        "-S.05: [scroll_name[5]]-" if not sscroll_[5]:
            call scroll_block(5,80)
            jump sscrolls
        "-S.06: [scroll_name[6]]-" if not sscroll_[6]:
            call scroll_block(6,80)
            jump sscrolls
        "-S.07: [scroll_name[7]]-" if not sscroll_[7]:
            call scroll_block(7,90)
            jump sscrolls
        "-S.08: [scroll_name[8]]-" if not sscroll_[8]:
            call scroll_block(8,50)
            jump sscrolls
        "-S.09: [scroll_name[9]]-" if not sscroll_[9]:
            call scroll_block(9,90)
            jump sscrolls
        "-S.10: [scroll_name[10]]-" if not sscroll_[10]:
            call scroll_block(10,50)
            jump sscrolls
        "-S.11: [scroll_name[11]]-" if not sscroll_[11]:
            call scroll_block(11,110)
            jump sscrolls
        "-S.12: [scroll_name[12]]-" if not sscroll_[12]:
            call scroll_block(12,110)
            jump sscrolls
        "-S.13: [scroll_name[13]]-" if not sscroll_[13]:
            call scroll_block(13,100)
            jump sscrolls
        "-S.14: [scroll_name[14]]-" if not sscroll_[14]:
            call scroll_block(14,80)
            jump sscrolls
        "-S.15: [scroll_name[15]]-" if not sscroll_[15]:
            call scroll_block(15,40)
            jump sscrolls
        "-Never mind-":
            jump shop_menu
    
label sscrolls2:
    show screen shop_screen
    menu:
        "-S.16: [scroll_name[16]]-" if not sscroll_[16]:
            call scroll_block(16,30)
            jump sscrolls
        "-S.17: [scroll_name[17]]-" if not sscroll_[17]:
            call scroll_block(17,30)
            jump sscrolls
        "-S.18: [scroll_name[18]]-" if not sscroll_[18]:
            call scroll_block(18,90)
            jump sscrolls
        "-S.19: [scroll_name[19]]-" if not sscroll_[19]:
            call scroll_block(19,50)
            jump sscrolls
        "-S.20: [scroll_name[20]]-" if not sscroll_[20]:
            call scroll_block(20,70)
            jump sscrolls
        "-S.21: [scroll_name[21]]-" if not sscroll_[21]:
            call scroll_block(21,90)
            jump sscrolls
        "-S.22: [scroll_name[22]]-" if not sscroll_[22]:
            call scroll_block(22,90)
            jump sscrolls
        "-S.23: [scroll_name[23]]-" if not sscroll_[23]:
            call scroll_block(23,150)
            jump sscrolls
        "-S.24: [scroll_name[24]]-" if not sscroll_[24]:
            call scroll_block(24,150)
            jump sscrolls
        "-S.25: [scroll_name[25]]-" if not sscroll_[25]:
            call scroll_block(25,100)
            jump sscrolls
        "-S.26: [scroll_name[26]]-" if not sscroll_[26]:
            call scroll_block(26,80)
            jump sscrolls
        "-S.27: [scroll_name[27]]-" if not sscroll_[27]:
            call scroll_block(27,200)
            jump sscrolls2
        "-S.28: [scroll_name[28]]-" if not sscroll_[28]:
            call scroll_block(28,150)
            jump sscrolls2
        "-S.29: [scroll_name[29]]-" if not sscroll_[29]:
            call scroll_block(29,200)
            jump sscrolls2
        "-S.30: [scroll_name[30]]-" if not sscroll_[30]:
            call scroll_block(30,70)
            jump sscrolls2
        "-Never mind-":
            jump shop_menu
    
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
                ">A New scroll has been added to your sacred scrolls collection."
                hide screen gift
                with d3
                call thx_4_shoping2 #Massage that says "Thank you for shopping here!".
                call screen shop_screen
            else:
                call no_gold #Massage: m "I don't have enough gold".
                hide screen gift
                return
        "-Never mind-":
            hide screen gift
            return
    
    
label shop_books:
    show screen shop_screen
    sna_[1] "What type of book would you like?"
    label shop_book_menu:
    menu:
        "-Educational Books-":
            label education_menu:
                python:
                    edu_menu = []
                    edu_list = []
                    edu_list.extend(speed_read_books)
                    edu_list.extend(speed_write_books)
                    for i in edu_list:
                        if i.purchased:
                            edu_menu.append((i.getMenuTextPurchased(),i))
                        else:
                            edu_menu.append((i.getStoreMenuText(),i))
                    edu_menu.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(edu_menu)
                if result == "nvm":
                    jump shop_book_menu
                elif result.purchased:
                    call do_have_book #Message that says that you already bought this book.
                    jump education_menu
                else:
                    call purchase_book(result)
        "-Fiction books-":
            sna_[1] "These books are mostly light erotica..." 
            sna_[20] "Some of the girls insisted that I order them in."
            label fiction_menu:
                python:
                    fic_menu = []
                    for i in fiction_book_list:
                        if i.purchased:
                            fic_menu.append((i.getMenuTextPurchased(),i))
                        else:
                            fic_menu.append((i.getStoreMenuText(),i))
                    fic_menu.append(("-Never mind-", "nvm"))
                    result = renpy.display_menu(fic_menu)
                if result == "nvm":
                    jump shop_book_menu
                elif result.purchased:
                    call do_have_book #Message that says that you already bought this book.
                    jump fiction_menu
                else:
                    call purchase_book(result)
        "-Never mind-":
            call screen shop_screen
    
label purchase_book(BookOBJ):
    $ the_gift = BookOBJ.picture
    show screen gift
    with d3
    "[BookOBJ.book_description]"
    menu:
        "-Buy the book for [BookOBJ.cost] gold -":
            if gold >= BookOBJ.cost:
                $ gold -= BookOBJ.cost
                $ BookOBJ.purchased = True
                "Book [BookOBJ.name] has been added to your collection."
                hide screen gift
                with d3
                if BookOBJ in fiction_book_list:
                    jump fiction_menu
                else:
                    jump education_menu
            else:
                call no_gold #Massage: m "I don't have enough gold".
                if BookOBJ in fiction_book_list:
                    jump fiction_menu
                else:
                    jump education_menu
        "-Never mind-":
            hide screen gift
            return
    
    
label shop_potion_menu:
    show screen shop_screen
    menu:
        "-Questions acquiring items-":
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
    
    
label gifts_menu:
    python:
        choices = []
        for i in gift_list:
            if whoring < i.whoringNeeded:
                choices.append( ("{color=#858585}-Item is out of stock-{/color}", "oos") )
            else:
                choices.append( ( ("-"+str(i.name)+"- ("+str(i.cost)+" g.)"), i) )
        choices.append(("-Never mind-", "nvm"))
        result = renpy.display_menu(choices)
        
    if result == "nvm":
        jump shop_menu
    elif result == "oos":
        call out
    else:
        call object_gift_block(result)
    
label object_gift_block(item):
    $ the_gift = item.image
    show screen gift
    with d3
    #$ tmp = item.description
    dahr "[item.description]"
    $ cost2 = item.cost * 2
    $ cost3 = item.cost * 4
    $ cost4 = item.cost * 8
    menu:
        "-Buy 1 for ([item.cost] galleons)-":
            $ gift_order = item
            $ order_quantity = 1
            call object_purchase_item(item.cost)
        "-Buy 2 for ([cost2] galleons)-":
            $ gift_order = item
            $ order_quantity = 2
            call object_purchase_item(cost2)
        "-Buy 4 for ([cost3] galleons)-":
            $ gift_order = item
            $ order_quantity = 4
            call object_purchase_item(cost3)
        "-Buy 8 for ([cost4] galleons)-":
            $ gift_order = item
            $ order_quantity = 8
            call object_purchase_item(cost4)
        "-Never mind-":
            hide screen gift
            call gifts_menu
            
label object_purchase_item(order_cost):
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
    
    
label app:
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
    
