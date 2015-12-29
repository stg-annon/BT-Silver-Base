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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_xpos=140 #Defines position of the Hermione's full length sprite. (Default 370). (Center: 140)                                                       #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Hm...? What is this?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "A skirt?"
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Thank you professor."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "You cannot be serious, [genie_name]!"
        her "A skirt this short?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "...It barely covers anything, [genie_name]."
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Gladly..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "well, alright..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But it's so short..."
        menu:
            m "..."
            "\"Just put it on!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "[genie_name] this is hardly the appropriate attire for a Hogwarts student."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "I refuse!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Hm..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Well, in that case..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "As long as it benefits my house..."
            "\"Fine. Forget it\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But it's so short..."
        menu:
            m "..."
            "\"Just put it on!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright, alright..."
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Hm..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright. I don't mind then."
            "\"Fine. Forget it\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Oh..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Of course, [genie_name]..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I'm glad that you came to your senses, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE 
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Gladly, [genie_name]."

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Alright..."
    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "That boring thing again?"
    
    
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "You cannot be serious, [genie_name]!"
        her "A skirt THIS short?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "...It doesn't cover anything, [genie_name]."
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Gladly..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                her "........................"
                her "..............................."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "well, alright..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 10
                call upset
        
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But it's soooo short..."
        menu:
            m "..."
            "\"Just put it on!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "[genie_name] this is hardly the appropriate attire for a Hogwarts student."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "I refuse!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 35 points.\"":
                $ gryffindor +=35
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Hm..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Well, in that case..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "As long as it benefits my house..."
            "\"Fine. Forget it\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But it's soooo short..."
        menu:
            m "..."
            "\"Just put it on!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright, alright..."
            "\"I will give you 10 points.\"":
                $ gryffindor +=10
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Hm..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright. I don't mind then."
            "\"Fine. Forget it\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Oh..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        


    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Of course, [genie_name]..."
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "But I don't need glasses..."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I was just getting used to them though."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Of course, [genie_name]..."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "That boring old thing? ok then"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Finally, it was soooo boring dressing like this"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "What, I can't do that, everyone would call me a slut"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "oh thank you, you have no idea what it was like..."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "You want me to wear muggle pants?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok then"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "A bra?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "You want me to wear this?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Finally. This thing isn't very comfortable."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "You want me to change bra?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "What is this?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "What is this?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "What is this?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "What is this?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "What is this?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Ok"
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Why do you want me to change my hair?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "this'll be fun, Maybe I'll look like Batwoman!"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "I have been feeling a bit depressed recently."
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Brown seems so boring now."
    
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Blue?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Orange?"
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Sure, let me just go change it."
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "Sure, let me just go change it."
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
    hide screen hermione_main                                                                                                                                                                                   #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    show screen hermione_main                                                                                                                                                                                 #HERMIONE
    with d3                                                                                                                                                                                                                        #HERMIONE
    her "As you wish, [genie_name]..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "fishnet stockings...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "You cannot be serious, [genie_name]!"
        menu:
            m "..."
            "\"Fine. Forget it.\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Gladly..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                her "........................"
                her "..............................."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "well, alright..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ mad += 5
                call upset
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I am not that kind of girl [genie_name]..."
        her "You may have better luck with someone from \"Slytherin\"..."
        menu:
            m "..."
            "\"Just put it on!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "[genie_name] this is hardly the appropriate attire for a Hogwarts student."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "I refuse!"
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3  
                $ mad += 5
                call upset                                                                                                                                                                                                                #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Hm..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Well, in that case..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "As long as it benefits my house..."
            "\"Fine. Forget it\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Fishnet stockings?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I don't know about that [genie_name]..."
        menu:
            m "..."
            "\"Just put them on!\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright, alright..."
            "\"I will give you 15 points.\"":
                $ gryffindor +=15
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Hm..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Alright. I don't mind then."
            "\"Fine. Forget it\"":
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                her "Oh..."
                hide screen hermione_main                                                                                                                                                                                   #HERMIONE
                with d3                                                                                                                                                                                                                        #HERMIONE
                show screen hermione_main                                                                                                                                                                                 #HERMIONE
                with d3            
                jump day_time_requests
        

    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "If you insist, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
                                                                                                                                                                                                                          #HERMIONE
    
     
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I'm glad that you came to your senses, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE 
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Gladly, [genie_name]."

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "As you wish, [genie_name]."
    
    if whoring >= 18: # Lv 7+
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_28.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Really? Aw..."
    
    
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I have the feeling that the jar is full of something vile and inappropriate..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I think I know what this is..."
        her "But why would you give something like this to one of your pupils, [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "No, thank you."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
   
        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ anal_lube -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Anal lubricant?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ehm.. well... I know this girl..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Still, I think you should not give presents like this to your pupils, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I know a couple of girls who would do anything for a commodity like that."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank for looking out for us, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], I wouldn't even know what to do with them..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        call upset #Message saying that Hermione became upset with you.
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       
        
        
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "...Condoms?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Ehm... Is this a part of some new Hogwarts sex ed program or something?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "No, [genie_name]... It feels wrong to accept a thing like this from you..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Well, I shall accept them simply because it is rude to refuse a gift..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I appreciate your concern, [genie_name]. Thank you."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Candy is for kids, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_46.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Clever girls use candy like this as a \"weapon\"."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm..."
        her "That thing about fairies..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "That is a joke of some sort, right?"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I just like the way it crunches, [genie_name]! N-not the taste..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "You spoil me, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "No, it doesn't look like--"
        her ".........?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "!!!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Professor Dumbledore!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is just beyond inappropriate!"
        call upset
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
    
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Is this what I think it is?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], let me remind you that I belong to the noble house of \"Gryffindor\"."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "A present like that would be appropriate for a girl from \"Slytherin\", [genie_name]."
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ vibrator -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Is that a... vibrator?"
        her "The design..."
        her "it reminds me of my wand..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Did you have this custom made for me [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is inappropriate..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I shall take it nonetheless..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "It's... calling out for me..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But not in a dirty way, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "An artifact of some sort or a trophy?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "So well-crafted..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Are you sure that it's alright for me to have it, [genie_name]?"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "That is..."
        her "But it doesn't even look... human..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I mean..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], do you have no shame?!"
        her "Presenting a thing like that to a pupil?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Please put it away, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Is that the actual size of the... of the real \"thing\"?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I mean..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "......................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Is this like a party prank prop?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "It's so well-crafted though..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I will take it..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Is it really modeled after a thestral?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But the creatures are invisible..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Breathtaking..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Not in the way you think, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I am merely admiring the craftsmanship..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_141.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Is this like one of those adult toys?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_30.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "What woman in her right mind would subject herself to a humiliation like that?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And what possible use could I have for such objects?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is just insulting, [genie_name]..."                                                                                                                                                                                                              
        call upset

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 5
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], do you not realize how inappropriate it would be for me to accept a present like that?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And I would not even know what to do with them anyway..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I mean these fluffy things are obviously handcuffs..."
        her "But this ball... ehm..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], please..."
        her "Just put them away."
        call upset


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ ballgag -= 1
        $ mad -= 9
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A month ago I would've felt insulted to receive a gift like this..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But by now I know that some girl really do find pleasure in toys like..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I assure you that I am not one of them, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I know a girl who knows a girl who is into things like..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, I shall take these to her..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is completely inappropriate, [genie_name]." # :)
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But a gift is a gift, right?"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Are those like key-chain toys?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3    
        $ the_gift = "01_hp/18_store/16.png" # ANAL PLUG.
        show screen gift
        with d3
        ">You give the anal plugs to Hermione..."
        hide screen gift
        with d3
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
        call happy


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 15
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], are those adult toys of some sort?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "those are some of those anal things, aren't they?"
        her "[genie_name] this is nothing but a weapon meant to oppress women!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Despicable!"
        call upset

        
    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Yes, I know that some girls have uhm..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Have use for things such as these..."
        her "But not me, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "No, thank you."
        call no_change

    if whoring >= 18: # Lv 7+  
        $ plug -= 1
        $ mad -= 10
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5    
        her "Anal plugs?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I have no use for things like that, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "They are so pretty though..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "....................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_121.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Well, alright. I shall take them off your hands if I must, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Yes, I used to read magazines like that a lot..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Lately not so much though..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "To be honest, magazines like that lost their appeal to me completely lately..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I don't mind taking them off you hands anyway, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is the sort of press some \"slytherin\" bimbo would appreciate."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I am way above silly magazines like that, [genie_name]."
        call no_change
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        
        
        
      
    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 5
        $ mag2 -= 1
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "I don't read magazines of that nature, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I could give it a try just to humour you I suppose..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I really enjoy reading magazines like that lately..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I can't have enough of that brilliant magazine!"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Adult magazines, [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Given to me by An esteemed wizard of your status?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], surely you could find a more productive way to spend your free time."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And I most definitely would not have use for those..."
        call upset
        

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 3
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Adult magazines?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], I have no interest in things like that."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "And how is this an appropriate present for one of your students, [genie_name]?"
        call upset
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        


    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 8 
        $ mag3 -= 1
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "Adult magazines?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], this is such an inappropriate present for a girl my age..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Err.. I mean, adult magazines?"
        her "This is a little inappropriate..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_74.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I will take them..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_130.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], those are porn magazines!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_187.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Shame on you, [genie_name]!"
        call upset
        


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 8
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "Porn magazines?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], what do you expect me to do with those?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Research them?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_86.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Despicable!"
        call upset
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mag4 -= 1
        $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "That's hardcore porn, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Which is a completely inappropriate gift for a girl my age!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her ".............."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I will take them..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "How can women even agree to do things like that, [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "................."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Alright, I shall accept them..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Solely for research purposes of course..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Are you sure about that, [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "It does contain alcohol, you know..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "To let you in on a little secret, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I'm a big fan of this completely harmless beverage."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Err... I meant to say with the girls, of course."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "It's cute..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I like it!"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Toys are for kids, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I'll take it..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "There's got to be a switch or a button somewhere..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "So... Does it vibrate or something?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Oh...?"
        her "So it is really just a plush toy then?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Shame..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I mean, thank you, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "A sex doll?!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_32.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Professor Dumbledore!!!"
        call upset
        $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad += 20
        $ h_body = "01_hp/13_hermione_main/body_48.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A sex doll?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is just so unbecoming for an esteemed wizard such as yourself, [genie_name]..."
        call upset

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 10
        $ sexdoll -= 1
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "A sex doll..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "This is a little inappropriate..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But maybe we could use it for a prank or something..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I Can't say that I approve of this..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But I know Harry would love to have a go at it..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name], I cannot accept a gift like this from you..."
        call upset
       
      

    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "sexy lingerie?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "You know I cannot possibly accept a gift like that from you, [genie_name]."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "(It's pretty though)........."
        call no_change

    if whoring >= 12 and whoring <= 17: # Lv 5-6.
        $ mad -= 7
        $ lingerie -= 1
        $ h_body = "01_hp/13_hermione_main/body_124.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5     
        her "sexy lingerie?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "[genie_name] that is so inappropriate..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_123.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Do You think it will make me look like one of the witches in those adult magazines, [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Oh... I mean, thank you, [genie_name]."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "What is that silly-looking thing attached to it?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Is it like a saddle...?"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "It's a sex-toy of some sort, isn't it?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But it is so well crafted..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_66.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "What kind of saddle is that...?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Well, doesn't matter."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "That saddle, [genie_name]..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_190.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "It was designed especially for witches, was it not?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I am not sure whether this is inappropriate or clever..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_129.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "But this is a brilliant piece of engineering eitherway..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "What am I supposed to do with it, [genie_name]?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_184.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "No, thank you."
        call no_change
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
       


    if whoring >= 6 and whoring <= 11: # Lv 3-4.
        $ mad -= 1
        $ krum -= 1
        $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d5                                                                                                                                                                                                                        #HERMIONE
        her "A Quidditch poster?"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Hm..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I think I saw this player once or twice..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "He is that Durmstrang student, right?"
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Can't say that I care much for Quidditch, but..."
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "I can see why the girls find the brutish physique of some players appealing..."
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "Thank you, [genie_name]!"
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
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
        hide screen hermione_main                                                                                                                                                                                   #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        $ h_body = "01_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
        show screen hermione_main                                                                                                                                                                                 #HERMIONE
        with d3                                                                                                                                                                                                                        #HERMIONE
        her "The girls will go green with envy..."
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
        
        