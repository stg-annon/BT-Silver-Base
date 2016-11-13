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
        twi "Hello Professor! What would you like to buy?"
        jump shop_menu
    else:
        $ show_clothes_store = True
        $ shop_found = True
        fre "Professor Dumbledore? What are you doing here? I thought you didn't leave your office anymore."
        ger "You're not here to shut us down are you?"
        m "Shut you down? What for?"
        fre "NOTHING!"
        ger "We certainly aren't selling potions that we stole from Snape"
        fre "No sir! No prohibited goods being sold here."
        ger "None at all!"
        fre "But if we did sell them-"
        ger "Which we don't"
        fre "They would be sold at the best prices in the school"
        ger "Unbeatable"
        m "Hmmmm. What sort of potions are you \'not\' selling?"
        fre "Well we aren't selling polyjuice potion"
        ger "Not at all"
        m "Well do you sell anything else"
        ger "We also sell books, treats and knick knacks."
        fre "Take a look."
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
    twi "What type of book would you like?"
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
            twi "These books are mostly light erotica..." 
            ger "Some of the girls insisted that I order them in."
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
    
        "Send loll":
            $ deliveryQ.send(Lollipop,1,5,'Gift')
            "sent"
            jump shop_potion_menu
        "-Questions acquiring items-":
            menu:
                "-Knotgrass-":
                    m "Do you know where I can find \"Knotgrass\""
                    fre "You can sometimge find Knotgrass by the forbidden forest"
                    jump shop_potion_menu
                "-Root of Aconite-":
                    m "Do you know where I can find \"Root of Aconite\""
                    ger "Root of Aconite can be found down by the lake"
                    jump shop_potion_menu
                "-Wormwood-":
                    m "Do you know where I can find \"Wormwood\""
                    ger "Wormwood is sometimes found in the forbidden forest"
                    jump shop_potion_menu
                "-Niffler's Fancy-":
                    m "Do you know where I can find \"Niffler's Fancy\""
                    fre "hmm i think i heard that it's found by the lake"
                    jump shop_potion_menu
                
        "{color=#858585}-Polyjuice Potion-{/color}" if whoring < 5:
            call cust_excuse("Hermione mus be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Polyjuice Potion-" if whoring >= 5:
            menu:
                "-Buy the potion for 40 Gold-":
                    if gold >= 40:
                        $ gold -= 40
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
                "-Buy the potion for 20 Gold-":
                    if gold >= 20:
                        $ gold -= 20
                        $ p_inv.append("Transparent Tincture")
                        m "Transparent Tincture aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "{color=#858585}-Expanding Elixir-{/color}" if whoring < 8:
            call cust_excuse("Hermione must be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Expanding Elixir-" if whoring >= 8:
            menu:
                "-Buy the potion for 30 Gold-":
                    if gold >= 30:
                        $ gold -= 30
                        $ p_inv.append("Expanding Elixir")
                        m "Expanding Elixir aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "{color=#858585}-Moreish Mead-{/color}" if whoring < 14:
            call cust_excuse("Hermione must be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Moreish Mead-" if whoring >= 14:
            menu:
                "-Buy the potion for 60 Gold-":
                    if gold >= 60:
                        $ gold -= 60
                        $ p_inv.append("Moreish Mead")
                        m "Moreish Mead aquired, although it's missing a key ingredient..."
                    else:
                        m "I don't have enough gold."
                    call screen shop_screen
                "-Nevermind-":
                    call screen shop_screen
        "{color=#858585}-Imperius Potation-{/color}" if whoring < 14:
            call cust_excuse("Hermione must be \"Trained\" more before you can purchase this.")
            call screen shop_screen
        "-Imperius Potation-" if whoring >= 14:
            menu:
                "-Buy the potion for 45 Gold-":
                    if gold >= 45:
                        $ gold -= 45
                        $ p_inv.append("Imperius Potation")
                        m "Imperius Potation aquired, although it's missing a key ingredient..."
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
            call object_purchase_item(item, 1)
        "-Buy 2 for ([cost2] galleons)-":
            call object_purchase_item(item, 2)
        "-Buy 4 for ([cost3] galleons)-":
            call object_purchase_item(item, 4)
        "-Buy 8 for ([cost4] galleons)-":
            call object_purchase_item(item, 8)
        "-Never mind-":
            hide screen gift
            call gifts_menu
            
label object_purchase_item(item, quantity):
    $ transit_time = renpy.random.randint(1, 5)
    $ order_cost = item.cost*quantity
    if gold >= (order_cost):
        menu:
            "-add next day delivery (15 galleons)-" if gold >= order_cost + 15:
                $ gold -= 15
                $ transit_time = 1
                # $ next_day = True
            "{color=#858585}-add next day delivery (15 galleons)-{/color}" if gold < order_cost + 15:
                pass
            "-no thanks-":
                pass
        $ gold -= order_cost
        $ deliveryQ.send(item,transit_time,quantity,'Gift')
        # $ gift_order = item
        # $ order_placed = True
        if transit_time ==  1:
            dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered tomorrow."
        else:
            dahr "Thank your for shopping at \"Dahr's oddities\". Your order shall be delivered in 1 to [transit_time] days."
        hide screen gift
        with d3
        jump shop_menu
    else:
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
        "-Fishnet stokings (120 gold)-" if not nets == 7:
            $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
            show screen gift
            with d3
            call nets_text
            menu:
                "-Buy the item (120 gold)-":
                    if nets == 7 or nets == 1: # == 7 means "gifted already"
                        call do_have_book # "I already own this one."
                        jump app
                    else:
                        if gold >= 120:
                            $ gold -= 120
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
    # $ days_in_delivery2 = one_of_five  #Generating one number out of three for various porpoises.
    
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
    
