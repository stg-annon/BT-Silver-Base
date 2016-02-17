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
    menu:
        "-A lollipop candy-([gift_item_inv[1]])" if gift_item_inv[1] >= 1:
            $ gifted = True
            call give_her_gift(1)
            
        "-Chocolate-([gift_item_inv[2]])" if gift_item_inv[2] >= 1:
            $ gifted = True 
            call give_her_gift(2)
        
        "-Stuffed Owl-([gift_item_inv[3]])" if gift_item_inv[3] >= 1:
            $ gifted = True 
            call give_her_gift(3)
            
        "-Butterbeer-([gift_item_inv[4]])" if gift_item_inv[4] >= 1:
            $ gifted = True 
            call give_her_gift(4)
            
        "-Educational magazines-([gift_item_inv[5]])" if gift_item_inv[5] >= 1:
            $ gifted = True 
            call give_her_gift(5)
            
        "-Girly magazines-([gift_item_inv[6]])" if gift_item_inv[6] >= 1:
            $ gifted = True 
            call give_her_gift(6)
            
        "-Adult magazines-([gift_item_inv[7]])" if gift_item_inv[7] >= 1:
            $ gifted = True 
            call give_her_gift(7)
            
        "-Porn magazines-([gift_item_inv[8]])" if gift_item_inv[8] >= 1:
            $ gifted = True 
            call give_her_gift(8)
        
        "-Viktor Krum Poster-([gift_item_inv[9]])" if gift_item_inv[9] >= 1:
            $ gifted = True 
            call give_her_gift(9)
        
        "-Sexy lingerie-([gift_item_inv[10]])" if gift_item_inv[10] >= 1:
            $ gifted = True 
            call give_her_gift(10)
        
        "-A pack of condoms-([gift_item_inv[11]])" if gift_item_inv[11] >= 1:
            $ gifted = True 
            call give_her_gift(11)
            
        "-A jar of anal lubricant-([gift_item_inv[13]])" if gift_item_inv[13] >= 1:
            $ gifted = True 
            call give_her_gift(13)
        
        "-A vibrator-([gift_item_inv[12]])" if gift_item_inv[12] >= 1:
            $ gifted = True 
            call give_her_gift(12)
        
        "-Ball gag and cuffs -([gift_item_inv[14]])" if gift_item_inv[14] >= 1:
            $ gifted = True 
            call give_her_gift(14)
            
        "-Anal plugs -([gift_item_inv[15]])" if gift_item_inv[15] >= 1:
            $ gifted = True 
            call give_her_gift(15)
            
        "- A Thestral strap-on -([gift_item_inv[16]])" if gift_item_inv[16] >= 1:
            $ gifted = True 
            call give_her_gift(16)
        
        "- Lady Speed Stick-2000 -([gift_item_inv[17]])" if gift_item_inv[17] >= 1:
            $ gifted = True 
            call give_her_gift(17)
            
        "- Sex doll \"Joanne\" -([gift_item_inv[18]])" if gift_item_inv[18] >= 1:
            $ gifted = True 
            call give_her_gift(18)
        
        "-School miniskirt-" if have_miniskirt: # Turns TRUE when you have the skirt in your possession.
            $ gifted = True
            jump giving_skirt #28_gifts.rpy
        
        "-\"S.P.E.W.\" badge-" if "SPEW_badge" in cs_existing_stock and "SPEW_badge" not in cs_existing_stock_gifted:
            $ gifted = True
            call give_her_existing_stock("SPEW_badge")
        
        "-Fishnet stockings-" if "fishnet_stockings" in cs_existing_stock and "fishnet_stockings" not in cs_existing_stock_gifted:
            $ gifted = True
            call give_her_existing_stock("fishnet_stockings")
        
        "-Gryffindor Stockings-" if "gryffindor_stockings" in cs_existing_stock and "gryffindor_stockings" not in cs_existing_stock_gifted:
            $ gifted = True
            call give_her_existing_stock("gryffindor_stockings")
        
        "-Lace Bra and Panties-" if "lace_set" in cs_existing_stock and "lace_set" not in cs_existing_stock_gifted:
            $ gifted = True
            call give_her_existing_stock("lace_set")
        
        "-Cup-less Lace Bra-" if "cup_set" in cs_existing_stock and "cup_set" not in cs_existing_stock_gifted:
            $ gifted = True
            call give_her_existing_stock("cup_set")
        
        "-Silk Bra and Panties-" if "silk_set" in cs_existing_stock and "silk_set" not in cs_existing_stock_gifted:
            $ gifted = True
            call give_her_existing_stock("silk_set")
            
        "-Jeans-" if "jeans" in cs_existing_stock and "jeans" not in cs_existing_stock_gifted:
           $ gifted = True
           call give_her_existing_stock("jeans")
        
        ##"-Gryffindor Cheerleader Outfit-" if custom_outfit_1_bought == True:
        ##    $ gifted = True
        ##    jump giving_gryffindor_cheer #28_gifts.rpy

        ##"-Slytherin Cheerleader Outfit-" if custom_outfit_2_bought == True:
        ##    $ gifted = True
        ##    jump giving_slytherin_cheer #28_gifts.rpy

        ##"-Maid Outfit-" if custom_outfit_3_bought == True:
        ##    $ gifted = True
        ##    jump giving_maid_outfit #28_gifts.rpy

        ##"-Silk Nightgown-" if custom_outfit_4_bought == True:
        ##    $ gifted = True
        ##    jump giving_silk_nightgown #28_gifts.rpy
            
        "-The Ball Dress-" if "ball_dress" in outfit_inventory and not gave_the_dress:
            show screen  blktone
            with d3
            m "(I have the feeling that there will be no turning back for me after I give her this dress...)"
            m "(Am I ready for this?)"
            hide screen blktone
            menu:
                "\"Yes, I am...\"":
                    jump giving_thre_dress #27_final_events.rpy
                "\"No, not yet...\"":
                    jump day_time_requests
        "-Never mind-":
            jump day_time_requests
    
    
label give_gift(text = "", gift_id = 0):
    hide screen hermione_main
    with d3
    $ the_gift = "01_hp/18_store/gifts/"+str(gift_id)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    $ gift_item_inv[gift_id] -= 1
    return
    
label give_her_gift(gift_id):
    hide screen hermione_main
    with d5
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    
    if gift_id == 1:#candy
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
    if gift_id == 2:#chocolate
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
    if gift_id == 3:#plush owl
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
    if gift_id == 5:#edu mags
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
    if gift_id == 6:#girl mags
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
    if gift_id == 7:#adult mags
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
    if gift_id == 8:#porn mags
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
    if gift_id == 9:#krum poster
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
    if gift_id == 10:#lingerie
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
    if gift_id == 11:#condoms
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
    if gift_id == 12:#vibrator
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
    if gift_id == 13:#anal lube
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
    if gift_id == 14:#gag and cuffs
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
    if gift_id == 15:#anal plugs
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
    if gift_id == 16:#strap on
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
    if gift_id == 17:#speed stick
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
    if gift_id == 18:#sex doll
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
    jump day_time_requests
    
    
label display_gift(text=">Gift given", gift_id):
    hide screen hermione_main
    with d3
    $ the_gift = "01_hp/18_store/"+str(gift_id)+".png"
    show screen gift
    with d3
    "[text]"
    hide screen gift
    with d3
    return
    
label give_her_existing_stock(stock_id):
    hide screen hermione_main
    with d5
    $ hermione_xpos = 140
    
    if stock_id == "fishnet_stockings":
        call her_main("A pair of stockings?","body_03")
        call display_gift(">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe.","30")
        call her_main("Thank you, [genie_name].","body_04")
        $ cs_existing_stock_gifted.append("fishnet_stockings")
        $ dress_code = True
        call happy(30)
    if stock_id == "gryffindor_stockings":
        call her_main("A pair of stockings?","body_03")
        call display_gift(">You give the stockings to Hermione...\n>gryffindor stockings have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("gryffindor_stockings")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
    if stock_id == "SPEW_badge":
        call her_main("A badge?","body_01")
        call display_gift(">You give the badge to Hermione...\n>The \"S.P.E.W. badge has been added to the wardrobe.","29")
        $ cs_existing_stock_gifted.append("SPEW_badge")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_06")
        call happy(30)
    if stock_id == "long_jeans":
        call her_main("A pair of jeans?","body_03")
        call display_gift(">You give the jeans to Hermione...\n>jeans have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("long_jeans")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
    if stock_id == "short_jeans":
        call her_main("A pair of daisy dukes?","body_03")
        call display_gift(">You give the daisy dukes to Hermione...\n>short jeans have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("short_jeans")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
    if stock_id == "lace_set":
        call her_main("A set of undergarments?","body_03")
        call display_gift(">You give the lace bra and panties to Hermione...\n>lace bra and panties have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("lace_set")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
    if stock_id == "cup_set":
        call her_main("A set of undergarments??","body_03")
        call display_gift(">You give the cup bra and panties to Hermione...\n>cup bra and panties have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("cup_set")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
    if stock_id == "silk_set":
        call her_main("A set of undergarments?","body_03")
        call display_gift(">You give the silk bra and panties to Hermione...\n>silk bra and panties have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("silk_set")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
    if stock_id == "ITEM_ID":
        call her_main("HERMIONE_QUESTIONS_ITEM?","body_03")
        call display_gift(">You give the ITEM to Hermione...\n>ITEM have been added to the wardrobe.","07")
        $ cs_existing_stock_gifted.append("ITEM_ID")
        $ dress_code = True
        call her_main("Thank you, [genie_name].","body_04")
        call happy(30)
        
    $ hermione_xpos = 370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)
    show screen hermione_main
    with d3
    jump day_time_requests 
    
    
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
    
    $ dress_code = True
    
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

    $ dress_code = True

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
    
    $ dress_code = True
    
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

    $ dress_code = True

    call her_main("Thank you, [genie_name].","body_04")
    call happy
    
    call her_main("","body_03",xpos=370)
    jump day_time_requests    
    
    
label giving_skirt:
    $ dress_code = True # Turns TRUE when you gift the miniskirt. Unlocks the "dress code" button.
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
    
label h_badge_on(badge = "SPEW_badge"):
    hide screen hermione_main
    with d5
    $ hermione_badges = False
    $ h_badge = ""
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label h_badge_off:
    hide screen hermione_main
    with d5
    $ h_bra = bra
    $ h_panties = panties
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    
label set_h_hair_style(hair_style = "A"):
    hide screen hermione_main
    with d5
    $ h_hair_style = hair_style
    call update_her_body
    show screen hermione_main
    with d5
    return
    
label set_h_hair_color(hair_color = 0):
    hide screen hermione_main
    with d5
    $ h_hair_color = hair_color
    call update_her_body
    show screen hermione_main
    with d5
    return
    
label set_h_stockings(stocking = "00_blank"):
    hide screen hermione_main
    with d5
    $ h_stocking = stocking
    call update_her_uniform
    show screen hermione_main
    with d5
    return
    

label set_h_skirt(skirt="base_skirt"):   
    hide screen hermione_main
    with d5
    $ h_skirt = skirt
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
    
###Jeans ###
label equip_jeans:

    if whoring >= 0 and whoring <= 2 and request_jeans == False: # Lv 0
        call her_main("Muggle pants?","body_11")
        m "Yup"
        call her_main(".....?","body_11")
        call her_main("Wait you want me to WEAR them!?","body_31")
        m "Yup"
        call her_main("At school!?")
        m "How does 10 points sound?"
        call her_main("Those are not part of the school uniform! I'd be suspended or *shudder* worse!","body_18")
        m "Who cares. 15 points?"
        call her_main("NO amount of points is worth being suspended!","body_07")
        m "30?"
        jump very_no
    elif whoring >= 3 and whoring < 6 and request_jeans == False: #Lv 1  - 2
       call her_main("Muggle pants?","body_11")
       m "Yup"
       call her_main(".....","body_11")
       call her_main("You... want me to wear them...","body_31")
       m "Yup"
       call her_main("At school?")
       m "How does 10 points sound?"
       call her_main("But they're not part of the school uniform... I'd get suspended... I don't have permission!","body_18")
       m "I'm the head master, [hermione_name]. I'm giving you permission"
       m "15 points?"
       call her_main("............")   
       call her_main("... How on earth am I going to explain this to my classmates?","body_21")
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_skirt("jeans")
       call her_main("","body_21",xpos=120,ypos=0)
       show screen ctc
       with d3
       pause
       $ request_jeans = True
       m "15 points for Gryffindor!"
       $ gryffindor +=15
       call her_main("Thank you, [genie_name]","body_29",xpos=410)
    elif request_jeans == True:
       call set_h_skirt("jeans")
    elif whoring >= 6 and whoring < 9 and request_jeans == False:
       call her_main("Jeans?","body_02")
       m "Yup"
       call her_main("You want me to wear them at school?","body_17")
       m "Yup"
       call her_main("*sigh* as long as I don't get into any trouble...","body_16")
       call her_main("and I get some points for Gryffindor","body_14")
       m "I'm the head master, [hermione_name], there won't be any trouble."
       m "And 15 points for Gryffindor!"
       $ gryffindor +=15
       call her_main("Thank you, [genie_name]! (These might.. get me some extra attention)","body_59")
       call her_main("(Not that I want the attention!) I'm only in it for the points!","body_58")
       g9 ""
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_skirt("jeans")
       call her_main("","body_58",xpos=120,ypos=0)
       $ request_jeans = True
       show screen ctc
       with d3
       pause
       call her_main("","body_01",xpos=410)
    elif whoring >= 9 and whoring <= 15 and request_jeans == False: 
       call her_main("Jeans?","body_02")
       m "Yup"
       call her_main("Aren't they a little... plain?","body_66")
       m "How do you mean?"
       call her_main("How am I going to save Gryffindor if I look like just another boring girl?","body_16")
       call her_main("How am I going to get my points?","body_16")
       call her_main("At least make this worth while... Please, [genie_name]","body_17")
       m "15 points for Gryffindor, I guess?"
       call her_main("You're the best, [genie_name]!","body_129")
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_skirt("jeans")
       $ request_jeans = True
       show screen ctc
       with d3
       call her_main("*humph* ... (These are so stuffy... How am i supposed to get my hands into...)","body_12",xpos=120)
       call her_main("(What if [genie_name] needs me to...)","body_12",xpos=120)
       call her_main("(No... i shouldn't think about things like that! Keep your head in the game, [hermione_name]","body_141")
       call her_main("...","body_141")
       call her_main("(ahh... i thought about it again... naughty [hermione_name]!)","body_188")
       g9 "....."
       call her_main("","body_188",xpos=410)
    
    elif whoring > 15: 
        call her_main("...Jeans?","body_02")
        m "Yup"
        call her_main("*sigh*...are you serious?","body_04")
        m "...? You're going to draw the line at... a pair of jeans, [hermione_name]?"
        call her_main("Of course not, [genie_name]!","body_87")
        call her_main("It's just that... they take... time to get off","body_204")
        g4 "..."
        call her_main("I have needs and...","body_204")
        call her_main("There's a lot of fabric, [genie_name]")
        call her_main("between [genie_name] and his... [hermione_name]'s ...")
        m "And [hermione_name]'s what?"
        call her_main("...and [hermione_name]'s cunt, [genie_name]","body_208b")
        g4 "(This needy little slut was once the feared Hermione Granger?)"
        g9 ""
        call her_main("...")
        call her_main("I'll go change immediately, [genie_name]","body_209")
        show screen bld1
        with d3
        show screen blktone
        with d3
        call set_h_skirt("jeans")
        call her_main("","body_209",xpos=120,ypos=0)
        $ request_jeans = True
        show screen ctc
        with d3
        pause
        call her_main("If you still have time, [genie_name], we could test how long it takes to get out of this thing?","body_205")
        g9 "(I love my job)"
        call her_main("","body_209",xpos=410)
    
    jump day_request_clothing
    
### Gryffindor Stockings ###
label equip_gryyf_stockings:
    if whoring < 3 and request_gryyf_stockings == False:
       call her_main("Is that!?","body_11")
       call her_main("A pair of legendary Gryffindor socks!?","body_48")
       m "Yep?"
       call her_main("That sell out from the uniform shop on the very first day, of EVERY SINGLE YEAR!?","body_48")
       m "Probably?"
       call her_main("I NEED THEM! What'll it cost me!?","body_34")
       m "No cost"
       call her_main("!","body_48")
       m "It's a gift, [hermione_name], to show you what a great guy ME, Proffesor DeltaDwarf, really is!"
       call her_main("...")
       call her_main("hhmppphhh", "body_42")
       call her_main("hahahahahahaha!","body_80b")
       call her_main("ahhh....","body_157")
       call her_main("You're too funny! Thanks for the gift! I'll put them on right away","body_01")
       g6 "(...What did I say?)"
       call her_main("I've always wanted a pair of these! They're warm, and they reduce unwanted attention from the boys","body_45")
       call her_main("I will be just like having a skirt that's twice as long!","body_46")
       m "Just glad to help, [hermione_name]!
       g4 (hehehe... hope you remember those words after I've made you so needy and desperate that vacuuming up cum from those boys will be your only priority in life)"
       call her_main("They feel great!","body_01",xpos=120,ypos=0)
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_stockings("gryff")
       show screen ctc
       with d3
       pause
       call her_main("Thanks again, [genie_name]! You're too kind","body_01",xpos=410)
       g9 "(We'll see about that)"
       $ request_gryyf_stockings = True
    elif whoring >= 3 and whoring < 6 and request_gryyf_stockings == False:
       call her_main("Is that...","body_11")
       $ hermione_emote_exclam = True
       call her_main("A pair of the incredibly rare Gryffindor stockings!?","body_48")
       m "Yep?"
       call her_main("That are totally sold out!?","body_48")
       m "Yep?"
       call her_main("....")
       $ hermione_emote_exclam = False
       $ hermione_emote_hearts = True
       call her_main("I NEED THEM!", "body_34")
       call her_main("What'll it cost me!?", "body_34")
       call her_main("WHAT DO I HAVE TO DO!?","body_32")
       $ hermione_emote_hearts = False
       m "Just a small favour"
       call her_main("(!)","body_48")
       m "All I want, [hermione_name], is to see how great they look on you."
       m "Easy, right?"
       call her_main("...")
       call her_main("You just want to see my stockings? That should be no problem...", "body_14")
       call her_main("(Is he up to something?)","body_07")
       call her_main(".....")
       call her_main("","body_01",xpos=120,ypos=0)
       show screen bld1
       with d3
       show screen blktone
       with d3
       call set_h_stockings("gryff")
       show screen ctc
       with d3
       pause
       call her_main("What do you think, [genie_name]?")
       m "Impressive..."
       m "They look great, [hermione_name]!"
       call her_main("[genie_name]! My appearance has no bearing on my academic ability.","body_217") #Embarrassed mouth wide eyes closed angry
       call her_main("......","body_186")
       call her_main("(That does make me feel kinda nice, though...)","body_186") #Embarrassed mouth open angry
       g9 "But, I'm having a hard time seeing all the details with that skirt in the way"
       call her_main("(Oh no...)","body_28") #Worried, teeth showing
       call her_main("(I knew it! That pervert!)","body_47") #Angry, teeth showing
       call her_main("(sigh...)","body_47")
       call her_main("(alright, [hermione_name], we've done this before, just roll with it)","body_47")
       call her_main("(there's nothing embarrassing about this!)","body_140") #Worried, embarrassing, small tears
       call her_main("I'm just showing that bastard a little square of fabric", "body_186")
       call her_main("That's all!")
       call her_main("And think of how much more I'll get done without boys oogling at my legs all day...","body_141") #Worried, angry, embarrassed
       m "I'm waiting, [hermione_name]. Don't tell me you don't want your gift?"
       call her_main("No, [genie_name], I want it.")
       g9 "Then earn it, [hermione_name]"
       call her_main("....","body_182b",xpos=120) #embarrassed, eyes closed, mouth closed
       call set_hermione_action("lift_skirt")
       $ skirt_up = True
       show screen hermione_03 #Hermione lifts her skirt
       with d3
       pause
       show screen bld1
       with d3
       show screen blktone
       with d3
       call her_main("","body_141",xpos=120)
       show screen ctc
       with d3
       pause
       $ skirt_up = False
       #call reset_hermione_main
       show screen hermione_blink #Hermione stands still.
       with fade
       m "They suit you, [hermione_name]"
       call her_main("(these compliments shouldn't be affecting me like this...)", "body_182")
       m "Your panties, your stockings... they make you look so pretty"
       call her_main("(ahh! he called me pretty)", "body_188")
       call her_main("You saw what you wanted... now I can go, right [genie_name]?","body_141",xpos=120)
       #call her_main("Please?","body_141")
       m "(True)"
       g9 "(But I could try to get more out of her...)"
       m "What should I do?"
       menu:
            "What a cutie! Let her go":
                m "Of course, [hermione_name]. Enjoy your gift"
                $ hermione_emote_hearts = True
                call set_hermione_action("")
                call update_her_uniform
                call her_main("Thanks, [genie_name]! I'll wear them whenever you want.","body_209")
                call her_main("(phew. why does it feel like a dodged a bullet, though?)","body_209")
                $ hermione_emote_hearts = False
                $mad -= 30
            
            "Cute is boring. Break her.":
               m "That was certainly adequate, [hermione_name]..."
               call her_main("(Adequate...?)","body_81",xpos=120)
               m "But..."
               call her_main("oh no...","body_48",xpos=120)
               m "You're one of our top students..."
               m "And there were still areas I couldn't see..."
               m "You're not giving it 100\%, here!"
               call her_main("(No way...)","body_48",xpos=120)
               g4 "You're going to remove your skirt"
               g4 "Then you're going to remove your panties."
               g9 "And then I'm going to get a proper look. Just as we agreed."
               call set_hermione_action("")
               $ hermione_emote_anger = True
               call her_main("NO", "body_218")
               g4 "(?)"
               call her_main("NO WAY!")
               call her_main("THERE IS ABSOLUTELY NO WAY AM I GOING TO DO THAT!!!")
               call her_main("I'm not some cheap slytherin slut that you can just play with!","body_148")
               g4 "..."
               m "Would you like to have your gift taken back from you?"
               $ hermione_emote_anger = False
               $ hermione_emote_exclam = True
               call her_main("....","body_140")
               m "Forfeit your points?"
               $ hermione_emote_exclam = False
               call her_main("...........","body_140")
               m "How about I remove some points for disobeying the head master?"
               call her_main("...............","body_48",xpos=145)
               m "And end our tutoring arrangement all together..."
               m "I wonder what will happen to your report card?"
               m "I wonder what your parents will think..."
               g9 "When they realize they've raised a failure"
               call her_main("Stop it...","body_143")
               g9 "(Hmm?)"
               call her_main("I get it already...","body_143",xpos=120)
               call her_main(".......","body_143")
               $mad += 55
               ">With tears rolling down her soft cheeks, Hermione begins to unzip her skirt"
               ">Her trembling hands make it difficult just to keep hold of the zipper"
               ">Eventually she gets it, and after hooking her thumb over her panties, she lowers the rest of her dignity to the floor"    
               $ hermione_wear_skirt = False
               #$ h_request_wear_panties = False
               call update_her_uniform
               hide screen ctc
               with d3
               pause
               $ hermione_wear_panties = False
               call update_her_uniform
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_147")
               pause
               show screen ctc
               with d3
               m "Hands behind your back, [hermione_name]. I want to see everything."
               call her_main(".....","body_145")
               call set_hermione_action("hands_behind")
               call set_hermione_action("")
               ">Too weak to fight back, Hermione does as she's told"
               hide screen ctc
               with d3
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_145")
               pause
               show screen ctc
               with d3
               m "Good girl."
               g9 "(What a spectacular body...)"
               call her_main(".......","body_145")
               call her_main("(After all he's done to me... why do i feel...)","body_145")
               call her_main("(like i'm still on fire...)","body_145")
               call her_main("this doesn't make any sense","body_145")
               call her_main("Ahh... hehehehehehehe","body_142")
               m "(...has she lost it already?)"
               call her_main("(whatever... it doesn't need to make sense)")
               call her_main("(You're headed straight to Azkaban once this is over, anyway)","body_142")
               call her_main("(so at least for now, keep looking at my body!)","body_142")
               call her_main("(my whole body needs to melt)","body_142")
               g9 "(hehehehe, i hope [hermione_name] can feel it)"
               g9 "(how a bitch feels when she's in heat)"
               ">Slowly but surely, you see a trickle of nectar begin to leak out of Hermione."
               $ hermione_dribble = True
               call update_her_body
               hide screen ctc
               with d3
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_158")
               pause
               show screen ctc
               with d3
               call her_main("(This is....)")
               call her_main("(too good)")
               g9 "(heh. not long now before you'll be this dripping wet all the time, cunt)"
               call her_main("(more....)")
               call her_main("(i want to be tutored more by [genie_name]!)")
               m "..."
               g9 "....."
               call her_main (".....")
               m "We're done here, [hermione_name]"
               call her_main(".....","body_158")
               m "You can keep the stockings."
               call her_main(".......","body_158")
               m "And 50 points to Gryffindor for your outstanding preformance."
               $ gryffindor += 50
               call her_main("..........","body_158")
               g4 "What do you say when you've been given a gift?"
               call her_main("..........","body_158")
               call her_main("Thank you, [genie_name]","body_158")
               g9 "That's right, [hermione_name]."
               m "Don't forget your clothes on the way out."
               call her_main("(my... p..)","body_158")
               call her_main("(..pussy is throbbing)","body_158")
               call her_main("(i might become an addict if i'm not careful)","body_158")
               ">Hermione retrieves her clothes and starts putting them back on"
               call her_main("(just the panties touching...","body_142")
               call her_main("(feels incredible!)","body_142")
               "You can't help but notice her dripping cunt staining the pure white fabric"
               call set_hermione_action("hands_free")
               call set_hermione_action("")
               $ hermione_wetpanties = True
               $ hermione_wear_panties = True
               call update_her_uniform
               hide screen ctc
               with d3
               show screen bld1
               with d3
               show screen blktone
               with d3
               call her_main("","body_142")
               pause
               call her_main("(ahh, i've made them all sloppy)","body_142")
               g9 "We're going to have a lot of fun in future, [hermione_name]"
               call her_main("","body_142")
               $ hermione_wear_skirt = True
               $ hermione_dribble = False
               call update_her_uniform
               with d3
               call her_main("","body_158")
               ">'Leaking' overlay now equip-able!"
               ">'Wet panties' overlay now equip-able!"
               $ dribble_equip = True
       
       hide screen blktone
       hide screen bld1
       hide screen hermione_main
       hide screen hermione_stand_f #Hermione stands still.
       with d3
       call her_walk(400,610,2)
       $ request_gryyf_stockings = True
       ">Gryffindor stockings now equip-able!"
       #call reset_hermione_main
       
       jump end_hermione_personal_request
    
    
    
    else:
        call set_h_stockings("gryff")
        $ request_gryyf_stockings = True
    
    jump day_request_clothing
        
    
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
    