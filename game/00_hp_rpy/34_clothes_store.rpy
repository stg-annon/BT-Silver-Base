label __init_variables:
    if not hasattr(renpy.store,'outfit_inventory'): #important!
        $ outfit_inventory = []
    if not hasattr(renpy.store,'cs_stock_inventory'): #important!
        $ cs_stock_inventory = []
    if not hasattr(renpy.store,'outfit_order'): #important!
        $ outfit_order = "null"
    if not hasattr(renpy.store,'outfit_wait_time'): #important!
        $ outfit_wait_time = 0
    if not hasattr(renpy.store,'outfit_ready'): #important!
        $ outfit_ready = False
    if not hasattr(renpy.store,'outfit_order_placed'): #important!
        $ outfit_order_placed = False
    if not hasattr(renpy.store,'micro_skirt'): #important!
        $ micro_skirt = False
    if not hasattr(renpy.store,'glasses'): #important!
        $ glasses = False
    if not hasattr(renpy.store,'wear_shirts'): #important!
        $ wear_shirts = True
    if not hasattr(renpy.store,'wear_skirts'): #important!
        $ wear_skirts = True
    if not hasattr(renpy.store,'gave_tinyminiskirt'): #important!
        $ gave_tinyminiskirt = False
    if not hasattr(renpy.store,'clothes_intro_done'): #important!
        $ clothes_intro_done = False
    if not hasattr(renpy.store,'custom_outfit_1_bought'): #important!
        $ custom_outfit_1_bought = False
    if not hasattr(renpy.store,'custom_outfit_2_bought'): #important!
        $ custom_outfit_2_bought = False
    if not hasattr(renpy.store,'custom_outfit_3_bought'): #important!
        $ custom_outfit_3_bought = False
    if not hasattr(renpy.store,'custom_outfit_4_bought'): #important!
        $ custom_outfit_4_bought = False
    if not hasattr(renpy.store,'cs_accessories'): #important!
        $ cs_accessories = [False,False,False]
    if not hasattr(renpy.store,'cs_existing_stock'): #important!
        $ cs_existing_stock = [False,False,False,False,False]
    if not hasattr(renpy.store,'cs_existing_stock_gifted'): #important!
        $ cs_existing_stock_gifted = []
    
    $ outfit_inventory = ["gryffindor_cheerleader","slytherin_cheerleader","maid","silk_nightgown","ball_dress","ms_marvel","heart_dancer","power_girl","harley_quinn","christmas_costume","lara_croft","pirate"]#for testing only
    
    $ clothes_store_order_choice = "null"
    $ clothes_store_curr_page = 1
    $ clothes_store_selection = 0

    $ clothes_store_inv = []
    $ clothes_store_inv.append("null")#buffer for index 0
    $ clothes_store_inv.append("gryffindor_cheerleader")#start page 1
    $ clothes_store_inv.append("slytherin_cheerleader")
    $ clothes_store_inv.append("maid")
    $ clothes_store_inv.append("silk_nightgown")
    $ clothes_store_inv.append("ball_dress")
    $ clothes_store_inv.append("ms_marvel")
    $ clothes_store_inv.append("heart_dancer")
    $ clothes_store_inv.append("power_girl")#end page 1
    ###########################################
    $ clothes_store_inv.append("harley_quinn")#start page 2
    $ clothes_store_inv.append("christmas_costume")
    $ clothes_store_inv.append("lara_croft")
    $ clothes_store_inv.append("pirate")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")#end page 2
    ###########################################
    $ clothes_store_inv.append("")#start page 3
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")
    $ clothes_store_inv.append("")#end page 3
    
    return
    
label clothes_store_gui:
    $ clothes_store_curr_page = 1
    call screen cs_p1
    label cs_select_done:
    return
    
label cs_select:
    $ tmp = ((clothes_store_curr_page-1)*8) + clothes_store_selection
    #DEBUG#"You picked page [clothes_store_curr_page] item [clothes_store_selection]!  ([tmp])"
    if clothes_store_inv[tmp] == "wip":
        call cust_excuse("Sorry this outfit is currently a work in progress and unavalable at this time.")
        jump clothes_menu
    if clothes_store_selection == -1 or clothes_store_inv[tmp] == "":
        jump clothes_menu
    
    $ clothes_store_order_choice = clothes_store_inv[(((clothes_store_curr_page-1)*8)+ clothes_store_selection)]
    jump cs_select_done
    
label clothes_store:
    if outfit_ready:
        maf "here to pick up your order?"
        m "yes"
        maf "one moment let me go fetch it"
        maf "..."
        maf "here you are"
        call pickup_outfit
    if clothes_intro_done == False:
        jump clothes_intro
    maf "Well what can I get for you today?"
    jump clothes_menu
    
label clothes_intro:
    ">You enter to see an old woman busy sewing together too pieces of long dark fabric."
    ">The woman is dressed almost entirely in pink and has a warm, approachable air to her."
    m "Hello."
    maf "Hello Professor Dumbledore."
    maf "What can I do for you? Would you like a new cloak or do you require some alterations to an existing item?"
    m "Neither thank you, I'm just here to make a few enquiries."
    maf "Of course sir, what could I help you with."
    m "Firstly, what type of items do you sell?"
    maf "Well, I'm a tailor. I make uniforms for the staff and students."
    maf "I also perform alterations to existing items. This is mainly when a student goes through a growth spurt or gets a hole in their cloak."
    m "I see. Do you ever make custom orders?"
    maf "Not really, although it is my passion. Most of what I'm asked to make are standard black robes."
    m "So you're interested in making unique outfits?"
    maf "Absolutely, although I would have to order the fabrics in. I don't really have a range of colors at the moment."
    maf "What did you have in mind?"
    m "A few things. Haven't decided on anything specific yet."
    m "Well, while your making up your mind, feel free to browse the store."
    $ clothes_intro_done = True
    jump clothes_menu
    
label clothes_menu:
    menu:
        "{color=#858585}-Custom Orders-{/color}"if outfit_order_placed:
            call cust_excuse("only one order can be placed at a time.")
            jump clothes_menu
        "-Custom Orders-"if not outfit_order_placed:
            jump custom_orders
        "-Existing Stock-":
            jump existing_stock
        "-Leave-":
            m "That's all for today thank you."
            maf "You're welcome sir. Come back any time."
            jump day_main_menu
   
    
label custom_orders:
    
    call clothes_store_gui
    
    #"{color=#858585}-Gryffindor Cheerleader Outfit-{/color}"if "gryffindor_cheerleader" in outfit_inventory:
    if clothes_store_order_choice == "gryffindor_cheerleader" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #"-Gryffindor Cheerleader Outfit- (200 Gold)"if not "gryffindor_cheerleader" in outfit_inventory:
    if clothes_store_order_choice == "gryffindor_cheerleader" and not clothes_store_order_choice in outfit_inventory:
        m "I'd like to order a cheerleader outfit."
        maf "A cheerleader outfit? Those horribly crass things popular in America?"
        maf "Why on earth would you want to buy that?"
        m "Well I was speaking to Madam Hooch and she was practically begging me to start a Cheer squad for each house."
        maf "Madam Hooch said that?"
        m "Yes, of course I said no but I did agree to a one student trial for Gryffindor."
        maf "Well, that seems fair enough. Did you have any preference as to the design?"
        m "Not really, just make it sporty I suppose."
        maf "Ok, well come and see me in a few days and I will have it for you."
        m "Thank you."
        call place_outfit_order(clothes_store_order_choice,3,200)
        jump clothes_menu
    
    #"{color=#858585}-Slytherin Cheerleader outfit-{/color}"if "slytherin_cheerleader" in outfit_inventory:
    if clothes_store_order_choice == "slytherin_cheerleader" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #"-Slytherin Cheerleader outfit- (200 Gold)"if not "slytherin_cheerleader" in outfit_inventory:
    if clothes_store_order_choice == "slytherin_cheerleader" and  not clothes_store_order_choice in outfit_inventory:
        m "I'd like to order another cheerleader outfit."
        maf "Another cheerleader outfit? I thought you said that it was only a one person trial?"
        m "It was at first but due to the success of the Gryffindor cheerleader Slytherin demanded one aswell."
        maf "Those Slytherins never could stand being second."
        maf "So do you just want the same basic design modified to suit?"
        m "Maybe make this one a little more sporty if you know what I mean."
        maf "Well you can come pick it up in a few days."
        m "Thank you."
        call place_outfit_order("slytherin_cheerleader",3,200)
        jump clothes_menu
    
    #"{color=#858585}-Maid outfit-{/color}"if "maid" in outfit_inventory:
    if clothes_store_order_choice == "maid" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #"-Maid outfit- (100 Gold)"if not "maid" in outfit_inventory:
    if clothes_store_order_choice == "maid" and not clothes_store_order_choice in outfit_inventory:
        m "I'd like to order a maid outfit."
        maf "A maid costume, what on earth for? Surely the cleaning elves keep your office tidy."
        m "It's going to be a present."
        maf "For whom?"
        m "I'm afraid I can't say."
        maf "Well as long as it's not for a student..."
        maf "Did you have any style in mind?"
        m "Prefrerebly a french maid."
        maf "..."
        maf "Well I should have it available for pickup in a few days after I get the materials in."
        m "Thank you."
        call place_outfit_order("maid",2,100)
        jump clothes_menu
    
    #"{color=#858585}-Silk Nightgown-{/color}"if "silk_nightgown" in outfit_inventory:
    if clothes_store_order_choice == "silk_nightgown" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #"-Silk Nightgown- (140 Gold)"if not "silk_nightgown" in outfit_inventory:
    if clothes_store_order_choice == "silk_nightgown"and not clothes_store_order_choice in outfit_inventory:
        m "I'd like to order another custom outfit today."
        maf "Certainly Sir. These outfits have started to become the highlight of my job. Everything else seems quite conservative by comparison."
        m "Well I can assure you that this outfit is not conservative."
        maf "Hmmm?"
        m "I'd like to order a girls Nightgown."
        maf "Well that doesn't seem overl-"
        m "Made of silk."
        maf "Ahh. I assume that you also want it transparent?"
        m "If it's possible."
        maf "Of course it is possible, who do you take me for?"
        maf "I just have to order in the materials, although silks not cheap."
        m "Don't worry about the cost."
        maf "As you wish Sir, it should be ready in a couple of days."
        m "Thank you."
        call place_outfit_order("silk_nightgown",2,140)
        jump clothes_menu
    
    #"{color=#858585}-Ball Dress-{/color}"if "ball_dress" in outfit_inventory:
    if clothes_store_order_choice == "ball_dress" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #"-Ball Dress- (1500 gold)" if sorry_for_hesterics and not "ball_dress" in outfit_inventory:
    if sorry_for_hesterics and clothes_store_order_choice == "ball_dress" and not clothes_store_order_choice in outfit_inventory:
        m "Do you sell Ball Dresses?"
        maf "Hmmm, we do although they're nothing special. Why?"
        m "A 'girl' approached me with a problem. Apparently she's unable to aquire a dress for this years autumn ball."
        maf "How tragic, well I'm sure that one of these cheap ones will suffice."
        m "I was thinking that I could have a custom one made. She is a very good girl."
        maf "I see. Would I be correct in assuming that this girls measurements are the same as the other outfits you've had me make?"
        m "Yes you would."
        maf "Well then I'll make her the best dress this school's ever seen. From what I've heard she's earned it..."
        maf "It should be ready in about a week."
        m "A week? Why so long?"
        maf "A ball dress isn't something that's thrown together. It requires love and attention. It doesn't come cheap either."
        m "Well, thank you."
        maf "You're welcome."
        call place_outfit_order("ball_dress",7,1500)
        jump clothes_menu
    elif clothes_store_order_choice == "ball_dress" and not sorry_for_hesterics:
        call cust_excuse("You cannot purchase this outfit... yet.")
        jump custom_orders

    if clothes_store_order_choice == "ms_marvel" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #
    if clothes_store_order_choice == "ms_marvel"and not clothes_store_order_choice in outfit_inventory:
        m "Tell me Madam Mafkin, have you ever heard of super-heroes?"
        maf "Yes yes, those people in the comic books. My grandson is quite fond of them."
        m "Fantastic, I was wondering if it would be possible for you to make me a costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Ms Marvel?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        m "Thank you very much."
        maf "No need to thank me sir. Payment will suffice."
        call place_outfit_order("ms_marvel",5,250)
        jump clothes_menu
        
    if clothes_store_order_choice == "heart_dancer" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #
    if clothes_store_order_choice == "heart_dancer"and not clothes_store_order_choice in outfit_inventory:
        m "Have you ever seen a burlesque show Madam?"
        maf "I've done more than that, I've designed a few of the outfits for them!"
        m "Splendid, I was wondering if I could commision one."
        maf "Most Certainly, any particular color in mind?"
        m "Ideally red."
        maf "As you wish."
        m "Thank you very much."
        maf "You're quite welcome sir."
        call place_outfit_order("heart_dancer",4,300)
        jump clothes_menu

    if clothes_store_order_choice == "power_girl" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #
    if clothes_store_order_choice == "power_girl"and not clothes_store_order_choice in outfit_inventory:
        m "I was wondering if it would be possible for you to make me a super hero costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Power Girl?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'm set to visit him this weekend so I can take a look."
        m "Thank you very much."
        maf "No need to thank me sir. Payment will suffice."
        call place_outfit_order("power_girl",3,350)
        jump clothes_menu

    if clothes_store_order_choice == "harley_quinn" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #
    if clothes_store_order_choice == "harley_quinn"and not clothes_store_order_choice in outfit_inventory:
        m "I was wondering if it would be possible for you to make me a super villain costume."
        maf "Certainly, who did you have in mind?"
        m "Do you know Harley Quinn?"
        maf "I'm afraid not..."
        maf "But I'm sure that my grandson has a comic of hers. I'll just have to wrestle it out of his grubby little hands."
        m "Thank you very much."
        maf "You're quite welcome."
        call place_outfit_order("harley_quinn",4,300)
        jump clothes_menu

    if clothes_store_order_choice == "lara_croft" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #
    if clothes_store_order_choice == "lara_croft"and not clothes_store_order_choice in outfit_inventory:
        m "I was wondering if it would be possible for you to make me another costume."
        maf "Certainly, what are you after?"
        m "I don't suppose that you know Lara croft?"
        maf "I'm afraid not..."
        m "She's a video game character..."
        maf "Well my little muggle grandson loves video games. I'm sure he can show me what she looks like."
        m "Thank you very much."
        maf "You're welcome. I'm seeing him tonight so I should be able to complete this one slightly faster than usual."
        m "Fantastic."
        call place_outfit_order("lara_croft",2,275)
        jump clothes_menu

    if clothes_store_order_choice == "christmas_costume" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    #
    if clothes_store_order_choice == "christmas_costume" and not clothes_store_order_choice in outfit_inventory:
        m "I was wondering if it would be possible for you to make me a festive costume."
        maf "Certainly, what what holiday are you looking to \"celebrate\"?"
        m "Christmas."
        maf "At this time of year?"
        m "It's never to early to start the festivities..."
        maf "Evidently not. I'll have it done as soon as I can. "
        m "Thank you very much."
        maf "You're welcome. I'll even give you a special price. Consider it my Christmas gift to you.."
        m "Thank you."
        call place_outfit_order("christmas_costume",2,50)
        jump clothes_menu
    
    if clothes_store_order_choice == "pirate" and clothes_store_order_choice in outfit_inventory:
        call cust_excuse("You already own this outfit.")
        jump custom_orders
    if clothes_store_order_choice == "pirate" and not clothes_store_order_choice in outfit_inventory:
        m "I want a pireate outfit"
        maf "ok"
        call place_outfit_order("pirate",2,75)
        jump clothes_menu
        
    if clothes_store_order_choice == "CANCEL":
        jump clothes_menu
        
        
label place_outfit_order(outfit_name, wait_time, cost):
    if gold >= cost:
        $ gold -= cost
        $ outfit_wait_time = wait_time
        $ outfit_order = outfit_name
        $ outfit_order_placed = True
        jump clothes_menu
    else:
        m "I don't have [cost] gold."
        m "Well this is depressing."
        jump clothes_menu
return

label outfit_purchase_check:
    if outfit_wait_time <= 0:
        $ outfit_ready = True
        $ letters += 1
    else:
       $ outfit_wait_time -= 1
return
    
label pickup_outfit:

    if outfit_order_placed: # OUTFIT
        
        if outfit_order == "gryffindor_cheerleader":
            $ outfit_inventory.append("gryffindor_cheerleader")
            call receive_package
            call display_package(">A sporty Gryffindor cheerleader outfit has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "slytherin_cheerleader":
            $ outfit_inventory.append("slytherin_cheerleader")
            call receive_package
            call display_package(">A \"more sporty\" Slytherin cheerleader outfit has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "maid":
            $ outfit_inventory.append("maid")
            call receive_package
            call display_package(">A french maid outfit has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "silk_nightgown":
            $ outfit_inventory.append("silk_nightgown")
            call receive_package
            call display_package(">A transparent silk nightgown has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "ball_dress":
            $ outfit_inventory.append("ball_dress")
            call receive_package
            call display_package(">The ball dress has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "ms_marvel":
            $ outfit_inventory.append("ms_marvel")
            call receive_package
            call display_package(">The superhero costume has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "heart_dancer":
            $ outfit_inventory.append("heart_dancer")
            call receive_package
            call display_package(">The dancer costume has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "power_girl":
            $ outfit_inventory.append("power_girl")
            call receive_package
            call display_package(">The superhero costume has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "harley_quinn":
            $ outfit_inventory.append("harley_quinn")
            call receive_package
            call display_package(">The supervillain costume has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "lara_croft":
            $ outfit_inventory.append("lara_croft")
            call receive_package
            call display_package(">The video game costume has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "christmas_costume":
            $ outfit_inventory.append("christmas_costume")
            call receive_package
            call display_package(">The Christmas costume has been added to your possessions.")
            call screen main_menu_01
        if outfit_order == "pirate":
            $ outfit_inventory.append("pirate")
            call receive_package
            call display_package(">The Pirate costume has been added to your possessions.")
            call screen main_menu_01
        #if outfit_order == "": 
return

label display_package(str1):
    $ the_gift = "01_hp/18_store/07.png"
    show screen gift
    with d3
    "[str1]"
    hide screen gift
    with d3
return

label receive_package:
    if letters >= 1:
        $ letters -= 1
    $ outfit_order = ""
    $ outfit_order_placed = False
    $ outfit_ready = False
return

label cust_excuse(text="Meh, you cant use this yet"): #custom text option for other ideas
    show screen blktone8
    ">[text]"
    hide screen blktone8
    return

label existing_stock:
    menu:
        "-Pants/Skirts-":#Jeans#Stockings#Fishnet Stockings#Lace Bra and Panties#Cup-less Lace Bra#Silk Bra and Panties
            label existing_stock_pants_skirts:
            menu:
                "{color=#858585}-Jeans- (75 Gold)-{/color}"if "jeans_long" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_pants_skirts
                "-Jeans- (75 Gold)" if "jeans_long" not in cs_existing_stock:
                    "A pair of standard muggle jeans, albeit a little low slung."
                    menu:
                        "-Buy the item (75 gold)-":
                            call cs_buy_stock("jeans_long", 75)
                            jump existing_stock_pants_skirts
                        "-Never mind-":
                            jump existing_stock_pants_skirts
                "{color=#858585}-Short Jeans- (150 Gold)-{/color}"if "jeans_short" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_pants_skirts
                "-Short Jeans- (150 Gold)" if "jeans_short" not in cs_existing_stock:
                    "A pair of short daisy dukes."
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("jeans_short", 150)
                            jump existing_stock_pants_skirts
                        "-Never mind-":
                            jump existing_stock_pants_skirts
                "-Return-":
                    jump existing_stock
        "-Stockings-":
            label existing_stock_stockings:
            menu:
                "{color=#858585}-Gryffindor Stockings- (50 Gold)-{/color}"if "gryffindor_stockings" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_stockings
                "-Gryffindor Stockings- (50 Gold)" if "gryffindor_stockings" not in cs_existing_stock:
                    "A pair of cheerful school stockings, in house colors."
                    menu:
                        "-Buy the item (50 gold)-":
                            call cs_buy_stock("gryffindor_stockings", 50)
                            jump existing_stock_stockings
                        "-Never mind-":
                            jump existing_stock_stockings
                "{color=#858585}-Fishnet Stockings- (75 Gold)-{/color}"if "fishnet_stockings" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_stockings
                "-Fishnet Stockings- (75 Gold)" if "fishnet_stockings" not in cs_existing_stock:
                    "A pair of sultry fishnet stockings."
                    menu:
                        "-Buy the item (75 gold)-":
                            call cs_buy_stock("fishnet_stockings", 75)
                            jump existing_stock_stockings
                        "-Never mind-":
                            jump existing_stock_stockings
                "-Return-":
                    jump existing_stock
        "-Bras and Panties-":
            label existing_stock_bras_panties:
            menu:
                "{color=#858585}-Lace Bra and Panties- (50 Gold){/color}"if "lace_set" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_bras_panties
                "-Lace Bra and Panties- (50 Gold)" if "lace_set" not in cs_existing_stock:
                    "A lovely lace bra and panty set."
                    menu:
                        "-Buy the item (50 gold)-":
                            call cs_buy_stock("lace_set", 50)
                            jump existing_stock_bras_panties
                        "-Never mind-":
                            jump existing_stock_bras_panties
                "{color=#858585}-Cup-less Lace Bra and panties- (125 Gold){/color}"if "cup_set" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_bras_panties
                "-Cup-less Lace Bra and panties- (125 Gold)" if "cup_set" not in cs_existing_stock:
                    "A revealing piece of clothing that only serves to highlight the wearer's breasts."
                    menu:
                        "-Buy the item (125 gold)-":
                            call cs_buy_stock("cup_set", 125)
                            jump existing_stock_bras_panties
                        "-Never mind-":
                            jump existing_stock_bras_panties
                "{color=#858585}-Silk Bra and Panties- (150 Gold){/color}"if "silk_set" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_bras_panties
                "-Silk Bra and Panties- (150 Gold)" if "silk_set" not in cs_existing_stock:
                    "A smooth and comfortable lace bra and panty set."
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("silk_set", 150)
                            jump existing_stock_bras_panties
                        "-Never mind-":
                            jump existing_stock_bras_panties
                "{color=#858585}-Latex Bra and Panties- (150 Gold){/color}"if "latex_set" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump existing_stock_bras_panties
                "-Latex Bra and Panties- (150 Gold)" if "latex_set" not in cs_existing_stock:
                    "A tight and shiny lace bra and panty set."
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("latex_set", 150)
                            jump existing_stock_bras_panties
                        "-Never mind-":
                            jump existing_stock_bras_panties
                "-Never Mind-":
                    jump existing_stock
        "-Accessories-":
            label accessories:
            menu:
                "{color=#858585}-\"S.P.E.W.\" badge-{/color}"if "SPEW_badge" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-\"S.P.E.W.\" badge-" if "SPEW_badge" not in cs_existing_stock:
                    maf "A badge designed to show one's opposition of elf slavery."
                    menu:
                        "-Buy the item (100 gold)-":
                            call cs_buy_stock("SPEW_badge",100)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "{color=#858585}-\"I <3 C.U.M.\" badge-{/color}"if "CUM_badge" in cs_existing_stock:
                    call cust_excuse("You already own this.")
                    jump accessories
                "-\"I <3 C.U.M.\" badge-" if "CUM_badge" not in cs_existing_stock:
                    maf "A badge that displays ones affection towards semen."
                    menu:
                        "-Buy the item (150 gold)-":
                            call cs_buy_stock("CUM_badge",150)
                            jump accessories
                        "-Never mind-":
                            jump accessories
                "-Never mind-":
                    jump existing_stock
        "-Return-":
            jump clothes_menu
    
label cs_buy_stock(item_id = "", cost):
    if gold >= cost and item_id != "":
        if item_id in cs_existing_stock:
            m "I already own this."
            return
        else:
            $ gold -= cost
            $ cs_existing_stock.append(item_id)
            maf "Thank you very much."
            return
    else:
        m "I don't have enough."
        return

        
