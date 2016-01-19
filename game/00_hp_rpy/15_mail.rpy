label mail:
    if finished_report >= 1:
        $ letters -= 1 #Adds one letter in waiting list to be read. Displays owl with envelope.
        $ got_paycheck = False #When TRUE the paycheck is in the mail. Can't do paper work.
        hide screen owl
        show screen owl_02
        ">You read your mail."
        play sound "sounds/money.mp3"  #Quiet...
        if finished_report == 1:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing one report this week.\nHere is your payment:{/size} \n{size=+4}40 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
            $ gold += 40
        
        if finished_report == 2:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing two reports this week.\nHere is your payment:{/size} \n{size=+4}70 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
            $ gold += 70
    
        if finished_report == 3:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing three reports this week.\nHere is your payment:{/size} \n{size=+4}90 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
            $ gold += 90
            
        if finished_report == 4:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing four reports this week.\nHere is your payment:{/size} \n{size=+4}110 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
            $ gold += 110
        
        if finished_report == 5:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing five reports this week.\nHere is your payment:{/size} \n{size=+4}150 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
            $ gold += 150
            
        if finished_report >= 6:
            $ letter_text = "{size=-7}From:Ministry of Magic\nTo: Professor Dumbledore\n\n\n{/size}{size=-2}Thank you for completing six reports this week.\nHere is your payment:{/size} \n{size=+4}200 gold coins.{/size}\n\n\n{size=-3}-With deepest respect-{/size}"    
            $ gold += 200
        
        show screen bld1
        show screen letter
        show screen ctc
        pause
        hide screen letter
        hide screen bld1
        hide screen ctc

            
#            ">Thank you for completing two reports this week. Here is your payment (40 gold)."
#            $ gold += 40

#        if finished_report >= 3:
#            "Thank you for completing three reports this week. Here is your payment (60 gold)."
#            $ gold += 60
            
#        if finished_report >= 4:
#            "Thank you for completing four reports this week. Here is your payment (80 gold)."
#            $ gold += 80
        
#        if finished_report >= 5: #Maximum amount per week.
#            "Thank you for completing five reports this week. Here is your payment (100 gold)."
#            $ gold += 100
        
#        if finished_report >= 6:
#            "Thank you for completing six reports this week. Here is your payment (20 gold)."
#            $ gold += 20
            
#        if finished_report >= 7:
#            "Thank you for completing seven reports this week. Here is your payment (20 gold)."
#            $ gold += 20
            
        $ finished_report = 0

        call screen main_menu_01
    
    
### MAIL FROM HERMIONE ###
#place after ### MAIL FROM HERMIONE ###

if outfit_ready:
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Madam Mafkin\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nThis is a reminder that you have an order ready for pickup at the clothes store\n\n{size=-3}Thank you for your busness,\n M.M.{/size}"
    label letter_outfit:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass    
        "-Not yet-":
            jump letter_outfit
    $ letters -= 1
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01
    
if day == 1:
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger-{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sure that you remember the reason why I'm writing you this letter from my last one, sir.\n\nI beg of you, please hear my plea this time. This injustice simply cannot go on...\nNot in this day and age, not in our school.\n\nPlease take action.\n\n{size=-3}With deepest respect,\nHermione Granger{/size}"    
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter01_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass    
        "-Not yet-":
            jump letter01_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    show screen bld1
    with d3
    m "Ehm..............................."
    m "What?"
    m "................................."
    hide screen bld1
    with d3
    jump event_00
    #call screen main_menu_01
    


if letter_from_hermione_02: #Letter from Hermione #02.
    $ letter_from_hermione_02 = False
    #$ letter_text = "{size=-4}-To professor Dumbledore-\n\nI am writing you to bring the current situation in our school to your attention.\n I'm afraid I'll need your help to sort this out.\n\n\n-Sincerely yours Hermione Granger--{/size}"
    $ letter_text = "{size=-7}From: Hermione Granger\nTo: Professor Dumbledore\n\n{/size}{size=-4}I am sorry to disturb you again, professor. I just want to make sure that you take this problem seriously.\n\nLast night another classmate confided inme... I gave my word to keep it a secret, so I cannot go into any details.\n\nAll I can say is that one of the Professors was involved.\n\nPlease take action soon.\n\n{size=-3}With deepest respect,\nHermione Granger.{/size}"
    hide screen owl
    show screen owl_02
    #$ mail_from_her = False #Comented out because replaced with $ letters += 1
    $ letters -= 1
    label letter02_agagin:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass    
        "-Not yet-":
            jump letter02_agagin
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    call screen main_menu_01





### MAIL THAT UNLOCKS ABILITY TO WORK ###
if work_unlock: # Send a letter that will unlock an ability to write reports
    $ work_unlock = False # Send a letter that will unlock an ability to write reports
    $ letters -= 1
    $ work_unlock2 = True # Unlocks the "Paperwork" button.
    hide screen owl
    show screen owl_02
    $ letter_text = "{size=-7}From: Ministry of Magic\nTo: Professor Albus Dumbledore\n\n{/size}{size=-4}Dear professor Dumbledore.\nWe remind you that only upon providing us with a completed report we will be able to make a paymentin your name.\n\n{size=-3}With deepest respect,\nThe Ministry of Magic.{/size}"
    label letter_work:
    show screen letter
    show screen ctc
    show screen bld1
    with Dissolve(.3)
    pause
    menu:
        "-Done reading-":
            pass    
        "-Not yet-":
            jump letter_work
    hide screen letter
    hide screen ctc
    hide screen bld1
    with Dissolve(.3)
    m "Payments? Hm..."
    show screen blktone8
    with d3
    $ renpy.play('sounds/win2.mp3')   #Not loud.
    ">From now on you can do paperwork at your desk in order to earn additional gold..."
    hide screen blktone8
    with d3
    call screen main_menu_01






















    
label mail_02: #Packages only. <=====================================================================### PACKAGES ###=================================================== 
    
### ITEMS ###    
    if order_item != 0:
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ gift_item_inv[order_item] += order_quantity

        $ the_gift = "01_hp/18_store/gifts/"+str(order_item)+".png" # CONDOMS.
        show screen gift
        with d3
        $ tmp_str = "\""+store_gift_items[order_item]
        if order_quantity > 1:
            $ tmp_str += "'s\""
            ">([order_quantity]) [tmp_str] have been added to your possessions."
        else:
            $ tmp_str += "\""
            ">([order_quantity]) [tmp_str] has been added to your possessions."
        hide screen gift
        with d3
        $ order_item = 0
        call screen main_menu_01
        
    
    
    if bought_ball_dress:
        $ bought_ball_dress = False
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_dress_already = True #Makes sure that you won't buy the dress twice.
        
        $ gifts12.append("ball_dress")
        $ the_gift = "01_hp/18_store/01.png" # THE NIGHT DRESS.
        show screen gift
        with d3
        ">A fancy nightdress has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
    
    if bought_miniskirt:
        $ bought_miniskirt = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        #$ gifts12 += ["ball_dress"]
        $ bought_skirt_already = True #Makes sure that you won't buy the skirt twice.
        $ have_miniskirt = True # Turns TRUE when you have the skirt in your possession.
        $ the_gift = "01_hp/18_store/07.png" # MINISKIRT.
        show screen gift
        with d3
        ">A School miniskirt has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
    
    if bought_glasses:
        $ bought_glasses = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ glasses = True #Glasses owned
        $ glasses_worn = False

        $ the_gift = "01_hp/18_store/glasses.png" # MAGAZINE # 3
        show screen gift
        with d3
        ">Some fine reading glasses have been added to your possession."
        hide screen gift
        with d3
        call screen main_menu_01
    
    if bought_badge_01:
        $ bought_badge_01 = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ badge_01 = 1 

        $ the_gift = "01_hp/18_store/29.png" # S.P.E.W. Badge.
        show screen gift
        with d3
        ">A \"S.P.E.W.\" badge has been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01
    
    if bought_nets:
        $ bought_nets = False #Affects 15_mail.rpy
        $ package_is_here = False # Turns True when days_in_delivery >= 5. Package is displayed.
        $ days_in_delivery = 0 #Count's +1 every day when order_placed = True
        
        $ nets = 1 

        $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
        show screen gift
        with d3
        ">A pair of fishnet stockings have been added to your possessions."
        hide screen gift
        with d3
        call screen main_menu_01


