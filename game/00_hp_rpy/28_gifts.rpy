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
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
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
        $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
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
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE 
        
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
        $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
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
    
    $ badges = True
    $ ba_01 = True
    
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
    $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.    
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
    
label jeans_on:
    call her_main("You want me to wear muggle pants?","body_01")
    m "Well their called jeans."
    her "That's not what I meant..."
    
    $ custom_skirt = 1
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label jeans_off:
    call her_main("Ok.","body_01")
    
    $ custom_skirt = 0
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests

label jeans_short_on:
    if whoring >= 12:
        call her_main("You want me to wear pants that are this short?","body_55")
        m "I do."
        call her_main("But they're so short...","body_56")
    else:
        call her_main("You want me to wear muggle pants?","body_08")
        her "That are this short..."
        m "I do."
        call her_main("...{w}Fine","body_12")
    
    $ custom_skirt = 5
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
label jeans_short_off:
    call her_main("Ok.","body_01")
    
    $ custom_skirt = 0
    
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
    
label dye_blonde:
    call her_main("Why do you want me to change my hair?","body_01")
    m "I don't know, I suppose I just have a thing for blondes"
    her "well I've always heard blondes have more fun!"
    
    $ hair_color = 1
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label dye_red:
    call her_main("this'll be fun, Maybe I'll look like Batwoman!","body_01")
    m "You read comics?"
    her "no, i just play certain games"
    m "What?"
    
    $ hair_color = 2
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label dye_black:
    call her_main("I have been feeling a bit depressed recently.","body_01")
    her "I wonder if it's because of all the favors I've been doing"
    m "Don't worry about it"
    
    $ hair_color = 3
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
    
    
label dye_brown:
    call her_main("Brown seems so boring now.","body_01")
    
    $ hair_color = 0
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests
      
label dye_blue:
    call her_main("Blue?","body_01")
    m "Why not?"
    her "Just seems a bit attention seeking..."
    
    $ hair_color = 4
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests

label dye_orange:
    call her_main("Orange?","body_01")
    m "That's what I said."
    her "Alright, well just let me change it."
    
    $ hair_color = 5
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests

label hair_up:
    call her_main("Sure, let me just go change it.","body_01")
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    $ hair_style = "B"
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests

label hair_down:
    call her_main("Sure, let me just go change it.","body_01")
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    
    $ hair_style = "A"
    
    show screen blkfade
    with d3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause 2
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    pause.3
    hide screen blkfade
    with d3
    jump day_time_requests

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
        menu:
            m "..."
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
        $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    
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
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE 
        
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
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
label giving_lube: # JAR OF ANAL LUBRICANT.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 6
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "I don't know what this is..."
        call her_main("But I have the feeling that the jar is full of something vile and inappropriate...","body_05")
        her "No, thank you, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 2
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Hm..."
        call her_main("I think I know what this is...","body_66")
        her "But why would you give something like this to one of your pupils, [genie_name]?"
        call her_main("No, thank you.","body_69")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ anal_lube -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Anal lubricant?"
        call her_main("Ehm.. well... I know this girl...","body_189")
        her "I mean I don't know her, she is a friend of a friend..."
        her "Yes, I will take this for her..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ the_gift = "01_hp/18_store/09.png" # ANAL LUBRICANT
        show screen gift
        with d3
        ">You give the jar to Hermione..."
        hide screen gift
        with d3
        call her_main("Still, I think you should not give presents like this to your pupils, [genie_name].","body_186")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call no_change #Message: Hermione's mood did not change.
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        
    if whoring >= 18: # Lv 7+  
        $ anal_lube -= 1
        $ mad -=5
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Anal lubricant, [genie_name]?"
        call her_main("I know a couple of girls who would do anything for a commodity like that.","body_186")
        call her_main("Thank for looking out for us, [genie_name].","body_128")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        call happy #Message that says that Hermione's mood has improved.
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
label giving_condoms: # A PACK OF CONDOMS
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 6
        $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Condoms?!"
        call her_main("[genie_name], I wouldn't even know what to do with them...","body_30")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "...Condoms?"
        call her_main("Ehm... Is this a part of some new Hogwarts sex ed program or something?","body_04")
        call her_main("No, [genie_name]... It feels wrong to accept a thing like this from you...","body_189")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call no_change 
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ condoms -= 1
        $ mad -= 3
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A pack of condoms?"
        her "[genie_name], what possible use could I have for those?"
        call her_main("Well, I shall accept them simply because it is rude to refuse a gift...","body_04")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">You give a pack of condoms to Hermione..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

        
    if whoring >= 18: # Lv 7+  
        $ anal_lube -= 1
        $ mad -=4
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "A pack of condoms?"
        call her_main("I appreciate your concern, [genie_name]. Thank you.","body_128")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/10.png" # CONDOMS
        show screen gift
        with d3
        ">You give a pack of condoms to Hermione..."
        hide screen gift
        with d3
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
     
     
     
### CANDY ###
label giving_candy: # CANDY.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 5
        $ candy -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A lollipop?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy #Message that says that Hermione's mood has improved.

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ candy -= 1
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "candy?"
        call her_main("Candy is for kids, [genie_name].","body_02")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you..."
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 5
        $ candy -= 1
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "candy?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ehm... Sure, thanks..."
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
 
        
    if whoring >= 18: # Lv 7+  
        $ candy -= 1
        $ mad -=5
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "A lollipop?"
        call her_main("Clever girls use candy like this as a \"weapon\".","body_46")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/11.png" # CANDY
        show screen gift
        with d3
        ">You give the candy to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE  
        her "Thank you, [genie_name]."
        call happy #Message that says that Hermione's mood has improved.
        $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
    
        
        
        

### CHOCOLATE ###
label giving_chocolate: # CHOCOLATE.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 10
        $ chocolate -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A chocolate bar?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy #Message that says that Hermione's mood has improved.

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ chocolate -= 1
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A chocolate bar?"
        call her_main("Hm...","body_09")
        her "That thing about fairies..."
        call her_main("That is a joke of some sort, right?","body_11")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you..."
        call happy #Message that says that Hermione's mood has improved.
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ chocolate -= 1
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A chocolate bar?"
        call her_main("I just like the way it crunches, [genie_name]! N-not the taste...","body_24")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ehm... Sure, thanks..."
        call happy #Message that says that Hermione's mood has improved.
       
 
        
    if whoring >= 18: # Lv 7+  
        $ chocolate -= 1
        $ mad -= 10
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "A chocolate bar?"
        call her_main("You spoil me, [genie_name].","body_111")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/12.png" # CHOCOLATE
        show screen gift
        with d3
        ">You give the chocolate to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE  
        her "Thank you."
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        

    ### VIBRATOR ###
label giving_vibrator: # VIBRATOR.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad+= 10
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A magic wand?"
        call her_main("No, it doesn't look like--","body_15")
        her ".........?"
        call her_main("!!!","body_18")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        #her "Professor Dumbledore!"
        her "[genie_name]!"
        call her_main("This is just beyond inappropriate!","body_30")
        call upset
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Is this what I think it is?"
        call her_main("[genie_name], let me remind you that I belong to the noble house of \"Gryffindor\".","body_186")
        call her_main("A present like that would be appropriate for a girl from \"Slytherin\", [genie_name].","body_120")
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ vibrator -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Is that a... vibrator?"
        her "The design..."
        her "it reminds me of my wand..."
        call her_main("Did you have this custom made for me [genie_name]?","body_118")
        call her_main("This is inappropriate...","body_30")
        call her_main("But I shall take it nonetheless...","body_29")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">You give the vibrator to Hermione..."
        hide screen gift
        with d3
        call no_change
        

    if whoring >= 18: # Lv 7+  
        $ vibrator -= 1
        $ mad -= 10
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "This vibrator..."
        call her_main("It's... calling out for me...","body_10")
        call her_main("But not in a dirty way, [genie_name].","body_66")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/13.png" # VIBRATOR
        show screen gift
        with d3
        ">You give the vibrator to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3  
        call happy #Message that says that Hermione's mood has improved.
        
 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
        ### STRAP-ON ###
label giving_strapon: # STRAP-ON.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 20
        $ strapon -= 1
        $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "What is that?"
        call her_main("An artifact of some sort or a trophy?","body_14")
        call her_main("So well-crafted...","body_01")
        call her_main("Are you sure that it's alright for me to have it, [genie_name]?","body_06")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">You give the strap-on to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you very much, [genie_name]. I promise to take good care of it."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call happy
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    
    
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 15
        $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "!!!"
        call her_main("That is...","body_118")
        her "But it doesn't even look... human..."
        call her_main("I mean...","body_69")
        call her_main("[genie_name], do you have no shame?!","body_86")
        her "Presenting a thing like that to a pupil?!"
        call her_main("..................","body_87")
        call her_main("Please put it away, [genie_name].","body_47")
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ strapon -= 1
        $ mad -= 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "That thing..."
        call her_main("Is that the actual size of the... of the real \"thing\"?","body_117")
        call her_main("I mean...","body_189")
        call her_main(".......................","body_118")
        call her_main("Is this like a party prank prop?","body_117")
        call her_main("It's so well-crafted though...","body_118")
        call her_main("I will take it...","body_33")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">You give the strap-on to Hermione..."
        hide screen gift
        with d3
        call happy


    if whoring >= 18: # Lv 7+  
        $ strapon -= 1
        $ mad -= 30
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "It's... It's magnificent, [genie_name]..."
        call her_main("Is it really modeled after a thestral?","body_189")
        call her_main("But the creatures are invisible...","body_190")
        call her_main("..................","body_118")
        call her_main("Breathtaking...","body_123")
        call her_main("Not in the way you think, [genie_name]...","body_120")
        call her_main("I am merely admiring the craftsmanship...","body_127")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/14.png" # STRAP-ON
        show screen gift
        with d3
        ">You give the strap-on to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you for the gift, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call happy

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
   
        ### BALL GAG ###
label giving_ballgag: # BALL GAG.
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "What is this?"
        call her_main("Is this like one of those adult toys?","body_141")
        call her_main("What woman in her right mind would subject herself to a humiliation like that?","body_30")
        call her_main("And what possible use could I have for such objects?","body_186")
        call her_main("This is just insulting, [genie_name]...","body_187")                                                                                                                                                                                                              
        call upset

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 5
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], do you not realize how inappropriate it would be for me to accept a present like that?"
        call her_main("And I would not even know what to do with them anyway...","body_189")
        call her_main("I mean these fluffy things are obviously handcuffs...","body_118")
        her "But this ball... ehm..."
        call her_main("[genie_name], please...","body_120")
        her "Just put them away."
        call upset


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ ballgag -= 1
        $ mad -= 9
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A month ago I would've felt insulted to receive a gift like this..."
        call her_main("But by now I know that some girl really do find pleasure in toys like...","body_118")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call her_main("But I assure you that I am not one of them, [genie_name].","body_120")
        call her_main("But I know a girl who knows a girl who is into things like...","body_189")
        call her_main("Yes, I shall take these to her...","body_188")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">You give the ball gag and cuffs to Hermione..."
        hide screen gift
        with d3
        call happy

    if whoring >= 18: # Lv 7+  
        $ ballgag -= 1
        $ mad -= 15
        $ h_body = "01_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "A ball gag and handcuffs?"
        call her_main("This is completely inappropriate, [genie_name].","body_122") # :)
        call her_main("But a gift is a gift, right?","body_129")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/15.png" # BALL GAG.
        show screen gift
        with d3
        ">You give the ball gag and cuffs to Hermione..."
        hide screen gift
        with d3
        call happy
        

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
        
        
        
        
        
        
        
        
  
      ### ANAL PLUGS ###
label giving_plug: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 8
        $ plug -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        call her_main("Are those like key-chain toys?","body_15")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">You give the anal plugs to Hermione..."
        hide screen gift
        with d3
        call her_main("Thank you, [genie_name].","body_185")
        call happy


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 15
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], are those adult toys of some sort?"
        call her_main("those are some of those anal things, aren't they?","body_187")
        her "[genie_name] this is nothing but a weapon meant to oppress women!"
        call her_main("Despicable!","body_120")
        call upset

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Yes, I know that some girls have uhm..."
        call her_main("Have use for things such as these...","body_186")
        her "But not me, [genie_name]."
        call her_main("No, thank you.","body_120")
        call no_change

    if whoring >= 18: # Lv 7+  
        $ plug -= 1
        $ mad -= 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Anal plugs?"
        call her_main("I have no use for things like that, [genie_name]...","body_117")
        call her_main("They are so pretty though...","body_122")
        call her_main(".....................","body_118")
        call her_main("Well, alright. I shall take them off your hands if I must, [genie_name].","body_121")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/16.png" # ANAL PLUGS.
        show screen gift
        with d3
        ">You give the anal plugs to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I shall never use them of course..."
        call her_main("................","body_124")
        call happy
        

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests
        
        
        
        
        
        
        
          ### EDUCATIONAL MAGAZINES ###
label giving_mag1: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 15
        $ mag1 -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "\"Popular magic\" magazines?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]!"
        her "I will use them for my research!"
        call happy

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ mag1 -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Sometimes I find information in magazines that I could never find in a book..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]!"
        her "I will use them for my research!"
        call happy

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 3 
        $ mag1 -= 1
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Oh..."
        call her_main("Yes, I used to read magazines like that a lot...","body_06")
        call her_main("Lately not so much though...","body_10")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]!"
        call happy
     

    if whoring >= 18: # Lv 7+  
        $ mag1 -= 1
        $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Ehm..."
        call her_main("To be honest, magazines like that lost their appeal to me completely lately...","body_08")
        call her_main("But I don't mind taking them off you hands anyway, [genie_name].","body_11")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/17.png" # EDUCATIONAL MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of educational magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you."
        call no_change 

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    
        
        
        
        
        
              ### GIRLY MAGAZINES ###
label giving_mag2: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Hm?"
        call her_main("This is the sort of press some \"slytherin\" bimbo would appreciate.","body_17")
        call her_main("I am way above silly magazines like that, [genie_name].","body_16")
        call no_change
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        
        
        
      
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ mag2 -= 1
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "I don't read magazines of that nature, [genie_name]..."
        call her_main("................","body_13")
        call her_main("But I could give it a try just to humour you I suppose...","body_04")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of rather girly magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]!"
        call happy
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15 
        $ mag2 -= 1
        $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "I ashamed to admit this, but..."
        call her_main("I really enjoy reading magazines like that lately...","body_24")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of rather girly magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 18: # Lv 7+  
        $ mag2 -= 1
        $ mad -= 15
        $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "The Latest edition of \"Girlz\"?!"
        call her_main("I can't have enough of that brilliant magazine!","body_24")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/18.png" # GIRLY MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of rather girly magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests        
        
        
        
                  ### ADULT MAGAZINES ###
label giving_mag3: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 7
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Are that...?"
        call her_main("Adult magazines, [genie_name]?","body_31")
        call her_main("Given to me by An esteemed wizard of your status?","body_69")
        call her_main("[genie_name], surely you could find a more productive way to spend your free time.","body_66")
        call her_main("And I most definitely would not have use for those...","body_47")
        call upset
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 3
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Adult magazines?"
        call her_main("[genie_name], I have no interest in things like that.","body_69")
        call her_main("And how is this an appropriate present for one of your students, [genie_name]?","body_47")
        call upset
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 8 
        $ mag3 -= 1
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Adult magazines?"
        call her_main("[genie_name], this is such an inappropriate present for a girl my age...","body_34")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of adult magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I shall throw these away myself..."
        call happy
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE


    if whoring >= 18: # Lv 7+  
        $ mag3 -= 1
        $ mad -= 15
        $ h_body = "01_hp/13_hermione_main/body_75.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "The New edition of \"L.o.v.e.\"!!!"
        call her_main("Err.. I mean, adult magazines?","body_122")
        her "This is a little inappropriate..."
        call her_main("But I will take them...","body_74")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/19.png" # ADULT MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of adult magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "thank you, [genie_name]."
        call happy
       

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests            
        
        
        
        
        
                      ### PORN MAGAZINES ###
label giving_mag4: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 15
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Hm... What is this?"
        call her_main("[genie_name], those are porn magazines!","body_130")
        call her_main("Shame on you, [genie_name]!","body_187")
        call upset
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 8
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Porn magazines?"
        call her_main("[genie_name], what do you expect me to do with those?","body_87")
        call her_main("Research them?","body_79")
        call her_main("Despicable!","body_86")
        call upset
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mag4 -= 1
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "That's hardcore porn, [genie_name]."
        call her_main("Which is a completely inappropriate gift for a girl my age!","body_34")
        call her_main("..............","body_118")
        call her_main("But I will take them...","body_117")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of porn magazines to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And I shall throw them in the trash, where they and... girls who like these things belong..."
        call no_change
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 18: # Lv 7+  
        $ mag4 -= 1
        $ mad -= 15
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Pornography?"
        call her_main("................","body_118")
        call her_main("How can women even agree to do things like that, [genie_name]?","body_117")
        call her_main(".................","body_118")
        call her_main("Alright, I shall accept them...","body_120")
        call her_main("Solely for research purposes of course...","body_189")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/20.png" # PORN MAGAZIES.
        show screen gift
        with d3
        ">You give an assortment of porn magazines to Hermione..."
        hide screen gift
        with d3
        call happy
        $ h_body = "01_hp/13_hermione_main/body_45.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
        
        
        
           
                      ### BUTTERBEER ###
label giving_beer: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ beer -= 1
        $ mad -= 3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Butterbeer?"
        call her_main("Are you sure about that, [genie_name]?","body_08")
        call her_main("It does contain alcohol, you know...","body_06")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you."
        call happy
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ beer -= 1
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Butterbeer, [genie_name]?"
        call her_main("To let you in on a little secret, [genie_name]...","body_14")
        call her_main("I'm a big fan of this completely harmless beverage.","body_06")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        

        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ beer -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Butterbeer?"
        call her_main("Thank you, [genie_name].","body_24")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I shall drink this with the girls later."
        call happy
        

    if whoring >= 18: # Lv 7+  
        $ mad -= 20
        $ beer -= 1
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "Butterbeer...?"
        call her_main("Thank you, [genie_name].","body_01")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/21.png" # BUTTERBEER.
        show screen gift
        with d3
        ">You give the bottle to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I shall drink this later with the boys."
        call her_main("Err... I meant to say with the girls, of course.","body_189")
        call happy
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

 
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
            
        
        
        
        
        
                   ### PLUSH OWL ###
label giving_owl: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ owl -= 1
        $ mad -= 7
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A stuffed owl?"
        call her_main("It's cute...","body_06")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 10
        $ owl -= 1
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A plush toy?"
        call her_main("I like it!","body_06")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ owl -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "A toy?"
        call her_main("Toys are for kids, [genie_name].","body_02")
        call her_main("But I'll take it...","body_29")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        
        
        
      
    if whoring >= 18: # Lv 7+  
        $ mad -= 4
        $ owl -= 1
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "This is one of those adult toys isn't it?"
        call her_main("There's got to be a switch or a button somewhere...","body_87")
        call her_main("So... Does it vibrate or something?","body_124")
        call her_main("Oh...?","body_190")
        her "So it is really just a plush toy then?"
        call her_main("Shame...","body_118")
        call her_main("I mean, thank you, [genie_name].","body_34")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/22.png" # PLUSH OWL.
        show screen gift
        with d3
        ">You give the owl to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        call happy

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
    
    
    
        
     ### SEX DOLL ###
label giving_sexdoll: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 20
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Is this..."
        call her_main("A sex doll?!","body_34")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        #her "Professor Dumbledore!!!"
        her "[genie_name]!!!"
        call upset
        $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 20
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A sex doll?"
        call her_main("This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]...","body_120")
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ sexdoll -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "A sex doll..."
        call her_main("This is a little inappropriate...","body_120")
        call her_main("But maybe we could use it for a prank or something...","body_124")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">You give the blow-up doll to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        
    if whoring >= 18: # Lv 7+  
        $ mad -= 30
        $ sexdoll -= 1
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "the Joanne sex doll?"
        call her_main("I Can't say that I approve of this...","body_189")
        call her_main("But I know Harry would love to have a go at it...","body_124")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/23.png" # SEX DOLL.
        show screen gift
        with d3
        ">You give the blow-up doll to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        

        
    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
        
      ### SEXY LINGERIE ###
label giving_lingerie: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad += 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "lingerie?"
        call her_main("[genie_name], I cannot accept a gift like this from you...","body_120")
        call upset
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "sexy lingerie?"
        call her_main("You know I cannot possibly accept a gift like that from you, [genie_name].","body_117")
        call her_main("(It's pretty though).........","body_118")
        call no_change

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 7
        $ lingerie -= 1
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "sexy lingerie?"
        call her_main("[genie_name] that is so inappropriate...","body_122")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">You give the lingerie to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy

        
    if whoring >= 18: # Lv 7+  
        $ mad -= 15
        $ lingerie -= 1
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "sexy lingerie?"
        call her_main("Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?","body_123")
        call her_main("Oh... I mean, thank you, [genie_name].","body_122")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/24.png" # SEXY LINGERIE.
        show screen gift
        with d3
        ">You give the lingerie to Hermione..."
        hide screen gift
        with d3
        call happy
        

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
    ### BROOM ###
label giving_broom: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ mad -= 20
        $ broom -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A broom...?"
        call her_main("Hm...","body_03")
        call her_main("What is that silly-looking thing attached to it?","body_07")
        call her_main("Is it like a saddle...?","body_08")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you for the gift, [genie_name]."
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        call happy
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 20
        $ broom -= 1
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A broom...?"
        call her_main("Hm...","body_07")
        call her_main("It's a sex-toy of some sort, isn't it?","body_05")
        call her_main("But it is so well crafted...","body_87")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy
        
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 30
        $ broom -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "A broom...?"
        her "Hm..."
        call her_main("What kind of saddle is that...?","body_66")
        call her_main("Well, doesn't matter.","body_127")
        her "Refusing an expensive gift like that would be rude..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy

    if whoring >= 18: # Lv 7+  
        $ mad -= 30
        $ broom -= 1
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "A broom..."
        her "Hm..."
        call her_main("That saddle, [genie_name]...","body_189")
        call her_main("It was designed especially for witches, was it not?","body_190")
        call her_main("I am not sure whether this is inappropriate or clever...","body_185")
        call her_main("But this is a brilliant piece of engineering eitherway...","body_129")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/25.png" # BROOM
        show screen gift
        with d3
        ">You give the broom to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy


    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                
        
    ### KRUM POSTER ###
label giving_krum: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    
    if whoring >= 0 and whoring <= 5: # Lv 1-2.
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A Quidditch poster?"
        call her_main("What am I supposed to do with it, [genie_name]?","body_185")
        call her_main("No, thank you.","body_184")
        call no_change
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 1
        $ krum -= 1
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A Quidditch poster?"
        call her_main("Hm...","body_185")
        call her_main("I think I saw this player once or twice...","body_71")
        call her_main("He is that Durmstrang student, right?","body_06")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">You give the poster to Hermione..."
        hide screen gift
        with d3
        call happy
        

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 15
        $ krum -= 1
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "A Viktor Krum poster, [genie_name]?"
        call her_main("Can't say that I care much for Quidditch, but...","body_08")
        call her_main("I can see why the girls find the brutish physique of some players appealing...","body_87")
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">You give the poster to Hermione..."
        hide screen gift
        with d3
        call happy
        
        
       
    if whoring >= 18: # Lv 7+  
        $ mad -= 25
        $ krum -= 1
        $ h_body = "01_hp/13_hermione_main/body_72.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5  
        her "A Viktor Krum poster?!"
        call her_main("Thank you, [genie_name]!","body_24")
        hide screen hermione_main
        with d3
        $ the_gift = "01_hp/18_store/26.png" # KRUM POSTER.
        show screen gift
        with d3
        ">You give the poster to Hermione..."
        hide screen gift
        with d3
        $ h_body = "01_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Can't wait to hang it over my bed!"
        call her_main("The girls will go green with envy...","body_64")
        call happy


    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                    
        
        
        
        
        
     ### S.P.E.W. BADGE ###
label giving_badge_01: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ badge_01 = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A badge?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/29.png" # S.P.E.W. BADGE.
    show screen gift
    with d3
    ">You give the badge to Hermione...\n>The \"S.P.E.W. badge has been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy


    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                    
            
        
        
        
    ### FISHNET STOCKINGS ###
label giving_nets: 
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A pair of stockings?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests                    
            
###GIVING CLOTHING RESPONSES
label giving_gryffindor_cheer:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A Cheerleading costume?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/07.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Gryffindor Cheerleading outfit has been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name], although I don't know when I'd wear it."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_slytherin_cheer:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A Cheerleading costume? For Slytherin?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/07.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A Slytherin Cheerleading outfit has been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name], even though I'm not in Slytherin..."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_maid_outfit:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A maid outfit?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/07.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the outfit to Hermione...\n>A maid outfit has been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_silk_nightgown:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A nightgown?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the nightgown to Hermione...\n>A silk nightgown has been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_jeans:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A pair of stockings?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_gryffindor_stockings:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A pair of stockings?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_lace_bra:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A pair of stockings?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_cupless_bra:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A pair of stockings?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    

label giving_silk_bra:
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    

    $ mad -= 30
    $ nets = 7 # Means already gifted.
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d5                                                                                                                                                                                                                        #HERMIONE
    her "A pair of stockings?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ the_gift = "01_hp/18_store/30.png" # FISHNETS.
    show screen gift
    with d3
    ">You give the stockings to Hermione...\n>Fishnet stockings have been added to the wardrobe."
    hide screen gift

    $ dress_code = True

    $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you, [genie_name]."
    call happy
    $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE

    $ h_xpos=370 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    jump day_time_requests    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    label happy:
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3  
        if mad <= 0:
            $ mad = 0
        if mad == 0:
            ">Hermione's mood has improved...\n>Hermione is {size=+5}not upset{/size} with you..."
        else:
            ">Hermione's mood has improved...\n>Hermione is {size=+5}still upset{/size} with you..."
        return



    label no_change:
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3  
        ">Hermione's mood didn't change much..."
        return
        
    label upset:
        hide screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3  
        ">Hermione's mood worsened...\n>Hermione is {size=+5}upset{/size} with you..."
        return
        
        