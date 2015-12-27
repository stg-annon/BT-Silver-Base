label snape_chitchat:
    if not chitchat_event_01_happened and tutoring_hermione_unlocked and days_without_an_event >=2:
        jump chitchat_event_01
    
    

    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    ### CHIT CHATS WITH SNAPE ###
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Do You really think you can do this?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Do You think you can break the girl?"
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Don't you just hate this wretched sunny weather?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I wish it would rain every day." 
            
        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I am feeling rather doubtful about our whole plan again..."
            
        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Are you sure that you are not Albus Dumbledore?"
            sna "I'm still having a hard time believing this whole thing sometimes..."
  
        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I killed a pupil once."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Yes... I strangled the maggot with my bare hands."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "........*low growl*."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Did that sound believable?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "The moment those animals stop fearing me, I'm done for."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Cultivating fear in the hearts of your students is the most important task for every teacher."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Those Weasley maggots..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_07.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "One of these days I'll just snap, I swear."

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Don't you think that owl post is a bit ridiculous?"
            sna "I'd much rather use ravens."
            
        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I'm having the worst day of my life..."
            sna "So I'm really Not in the mood for chit-chats..."
            
        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Being a wizard is a 24 hours a day..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "7 days a week..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "365 days a year job."
            sna "We get no vacation days..."
            
        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Quidditch..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "What a waste of time and ressources!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            
            
        
        
    
    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I have yet to notice any changes in miss Granger's behavior..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Are you sure that you know what you're doing?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "It sure feels good to be able to grant house points or take them away whenever I feel like it."
            sna "My authority among the students is growing every day..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "And when I say \"authority\" I mean \"fear\"."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Did you know that the full moon is known to boost male potency?"
            sna "It also makes it easier to focus at a task at hand, making you more proactive."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                    #SNAPE
            sna "But who gives a damn about that, am I right?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "My precious Slytherins make all of this torment worth while..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Their skirts are getting shorter every week, I swear."
  
        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "There was a time when I was young and full of hope..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ha-ha... I'm pulling your leg, mate"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I was never full of hope..."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Duelling is one of my fortes, you know..."

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "A \"Men's rights movement\"...?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "What's next? A house elves' rights movement?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "How could a top student could be that dumb?"
            
        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I don't play favourites with my students."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I merely tolerate some of them and hate the rest."
  
        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "There are four student houses at Hogwarts..."
            sna "Slytherin, Ravenclaw, Gryffindor and..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "...and Huff-something..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "No one really cares."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
 
        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Brooms are for kids and witches."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You'll never see a self-respecting wizard prancing around on a broomstick."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        
    
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Any progress on breaking our little ms. know-it-all?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "The other day this one girl sold me her panties for five house points."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "And man, was she excited about that..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I think she would've given them away for free just to please me."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I'm having a rather pleasant day so far..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Bet you didn't expect to hear me saying that?"

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Quidditch seems to steadily gain more and more popularity over the years..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "How disappointing..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "My life was incredibly dull before your arrival..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Nowadays it's..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "...less dull."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Regrets? I don't know the meaning of the word!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I live a very fulfilling life."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ha-ha-ha! I'm sorry, I just can't say such nonsense with a straight face."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "There is no room for mistakes during class."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "One slip-up and the bloody bastards will tear you to shreds."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You are the only person I have to answer to..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "So I can almost literally do whatever the bloody hell I want these days..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "..............."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "So that's what freedom feels like, huh?"

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Autumn... the most depressing time of the year..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I Love it!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I have a magical portrait of a stripper hanging in my room."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "One of my most precious possessions."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        
        
        
       
    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna  "Lately miss Granger has gotten aggressive almost to the point of open hostility..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I hope you know what you're doing..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I shouldn't feel bad about having sex with my students, right?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I mean, you should see the way some of those girls wear their uniforms..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "They're practically asking for it."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_12.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "It's been raining a lot lately..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I wonder if I enjoy rainy weather so much simply because it makes most people miserable..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "According to a recent study 9 out of 10 girls secretly fantasize about being abused by their teacher."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I bet that 10th girl was Hermione Granger."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "These days I have to actually make an effort to maintain my usual bad mood."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "Do You have a few condoms to spare?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "I have a whole pack but..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "...they've expired years ago..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            her "The changes you brought into my life, mate."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You think we could turn Hogwarts into a \"girls only\" school?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Hogwarts Girls Academy!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Now that would be bloody perfect... except for Lockhart maybe."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Why did the teacher cross the road?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "To get away from his students!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Ha-ha-ha! Gets me every time!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Want to hear a funny story?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Well, I don't know any..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Do you know what a \"royal goblet\" is?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You do, don't you?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        
    
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "15 points for a blowjob is a fair price, right?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Have you ever been in love, mate?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Have you ever been in love with a schoolgirl?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "What about half a dozen of them at once?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_20.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_20.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Something rather brilliant happened last night between me and this Slytherin mynx."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Long story short, all of my muscles ache and I still feel rather dehydrated..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "It's getting colder lately..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Winter is coming..."
         
        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Have you ever seen muggle women dressed as witches?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "So adorable."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Do you know what an \"Internet\" is?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Apparently it allows you to go \"on the line\" and see magical photographs of naked muggle women." # SNAPE SAYS "ON THE LINE" ON PURPOSE. I KNOW THAT WAS REALLY OBVIOUS MAESTRO
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Kind of makes me wish we had one here in Hogwarts."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I have two major passions in life..."
            sna "Dark arts..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_12.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "......"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "...and sluts."

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You think I ought to cut down on my drinking?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "But my life is so stressful..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Hm..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I'll try and cut down on the liquor..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "In favour of sweaty monkey-sex with my students!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Miss Granger has been suspiciously quiet lately..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_03.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I bet she is scheming something..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "It's quite easy to write a book and kill off half of the main characters for the sake of dramatic impact..."
            sna "To put your characters against impossible odds and let them make it out alive in a believable manner..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Now {size=+7}that{/size} requires skill."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
        
        
        
        
        

    if whoring >= 15 and whoring <= 17: # WHORING LEVEL 06.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_11.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "What if the girl is not our pet, but we are her's?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_26.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Have you heard of the \"Slug club\"?"
            sna "What if I start a club of my own?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I would call it the \"Snape Club\"!"
            sna "I would invite girls over, offer them some tea and muffins..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Feel them up a little..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Bloody brilliant!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Tell me Genie... Have you ever had your asshole licked clean by a young witch?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "A life changing experience, neither less nor more..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "So, how is the training going?"
            sna "All according to plan I hope?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I can see Thestrals, you know..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You know what I like about Quidditch?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_15.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Nothing! Not a single bloody thing!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Hogwarts benefited greatly from your arrival."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "And when I say \"Hogwarts\" I mean \"me\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Real wizards wear black."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Am I right?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Some of those Slytherin girls simply adore me these days..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Personally I'd much rather be feared..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "But I am willing to settle for mindless adoration..."

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You are being way too generous with those Gryffindor points, mate."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Lately I can barely keep up with you..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
        
        
   
        
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Miss Granger really is changing. I can see it clearly now..."
            sna "Her grades went down and even her attendance is far from perfect now..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "But despite that she continues to excel at being a pain in my arse!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "My least favourite colour?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_07.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Let me give you two: red and gold."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I hear the vampire-theme is quite popular among the girls lately."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I would make a great vampire, don't you think?"
            sna "Maybe I should buy a couple of those fake fangs..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_21.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Just to drive the horny, little sluts completely crazy."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I ...hate my life."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "No, wait, let me try this again..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_17.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I ...hate my life."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_25.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Dammit! I'm trying to say \"love\" but it just won't come out..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I don't think I've ever used the words \"love\" and \"life\" in one sentence before."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Let me try this again..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_10.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I ha...{w} lo... {w}love my life!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "There you go, I love my life..."

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Sunlight, chocolate, Quidditch, cats and orange juice..."
            sna "That's a list of things I don't care for..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Here is a short list of things I do care for a great deal..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "The dark arts, wine and pussy."

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "have You ever seen two wizards in a fistfight?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_28.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Bloody hilarious!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You know that feeling when you just came in a girl's mouth and she swallows it all and says: \"Thank you, professor\"?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Isn't that the best?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "do You think the Hogwarts ghosts sometimes spy on girls taking when they a shower and such?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "If I were a ghost I know I would."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "This one girl confessed to me that she has frequent fantasizes about being abused by that squib mr.Filch."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I think I could arrange that. Should I?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I used to hate my job so much..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Hate is clean, simple and certain..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_03png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Now, don't get me wrong - I still hate it."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "But I also sort of love it now..."
            sna "How could I not? With all that has been happening lately?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "To both cherish and hate something to an equal degree..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_19.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "It's like being in love again..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
        
        
    if whoring >= 21: # WHORING LEVEL 08+.
        if one_of_ten == 1:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Do you know what a \"bukkake\" is?"
            sna "What about \"deepthroating\"?"
            sna "And then there is also \"hate-sex\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Kids these days, mate..."
            sna "They have a special name for everything."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Although \"hate-sex\" has always been around..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Back in my days we just called it \"sex\"."

        elif one_of_ten == 2:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Man, my cock is so ready for the \"Princess Trainer Gold Edition\"!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_09.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "*Ahem!* I mean, slytherin rules, I hate gryffindor and stuff..."

        elif one_of_ten == 3:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I organized a small party the other day..."
            sna "One girl and three boys..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "They fucked her and I watched..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_29.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "........................."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You think I've been exercising my dark side a bit too often lately?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 4:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I'm all out of condoms, mate."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "You think you could hook me up?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_01.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE     

        elif one_of_ten == 5:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I am secretly making this special herbal brew that should make her tits lactate..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_13.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Pretty brilliant, huh?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 6:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "So, this witch has my cock in her mouth, right?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Her hot girlfriend is cleaning my asshole with her tongue..."
            sna "Meanwhile this third girl is on her knees with her mouth open, waiting for me to spit in it..."
            sna "And every time I spit, she says: \"Thank you, professor Snape\"."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "That was a bloody surreal evening..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_02.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 7:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_06.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "This one girl has been begging me to urinate in her mouth for days, now..."
            sna "Persistent little minx..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_05.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Should I give in?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 8:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_04.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I mercilessly dominate both male and female students..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_22.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "But in very different ways."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 9:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I love my life!"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_16.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "Still hate my job though..."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I wish I could skip all the teaching, but keep all the fucking."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        elif one_of_ten == 10:
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/24.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "I almost feel bad for having all the fun."
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/snape_14.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE
            sna "do You want me to send you up some young slut?"
            hide screen snape_main                                                                                                                   #SNAPE
            with d3                                                                                                                                                  #SNAPE
            $ s_sprite = "01_hp/10_snape_main/23.png"                                                                            #SNAPE
            show screen snape_main                                                                                                                  #SNAPE
            with d3                                                                                                                                                   #SNAPE

        
    
    
    
    
    
    
    
    
    jump snape_ready
    
    
    
#    $ snape_busy = True
    
#    hide screen snape_02 #Snape stands still.
#    hide screen bld1
#    hide screen snape_main
#    with d3
#    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
            
  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

### CHITCHAT EVENTS ###
label chitchat_event_01: #Snape says: so you tutor her now?". Happens after tutoring unlocks.
    hide screen snape_main
    with d3
##############################################################################
#########   JJ Edits   12/29/2014  ###########################################
#    sna_[1] "So..."
#    sna_[1] "I hear miss Granger is taking private lessons from you now?"
#    m "Yeah, I suppose she does..."
#    m "Not sure where this fits into our plan though."
#    sna_[9] "What do you mean? It fits perfectly."
#    sna_[9] "I myself and a couple of other teacher are failing the crap out of that girl!"
#    sna_[9] "As a result she spends more time with studying..."
#    sna_[9] "Even taking private lessons now..."
#    sna_[18] "This way she has very little time left to be noisy and cause me headaches."
#    m "I see..."
#    sna_[10] "Yes, yes... just, you so know..."
#    sna_[10] "Don't actually teach her anything useful, alright?"
#    m "I'll do my best."
#    sna_[1] "Well, if there is that's all..."
###  Altered this chit chat to reflect JJ's tutoring results  
    sna_[1]  "The Granger girl is driving me mad with her accusations.  They must stop!  I think she was even coming on to me!"  
    sna_[7] "As though I would fall for such a transparent ploy! Though she does look to have a luscious body under that frumpy sweater..."
    sna_[4] "Have you done anything to deal with her?  If you have not..."
    sna_[9] "I found a lovely potion in my cupboard that will put her into a long, wasting slumber for which there is no antidote."
    m  "Don’t worry, Severus.  I have her well in hand."  
    sna_[10]  "Oh, really?  How?"  
    m "Well, for starters she is seeing me for magic lessons.  I am teaching her how to do magic without wands or incantations."
    sna_[17] "But that’s nearly impossible for someone of her age!  All but the most powerful wizards and witches must use wands."  
    sna_[2] "And at her ability level she will need to verbalize all but the simplest spells."
    m  "Not to worry.  I plan to teach her how I do magic and I don’t need to do any of that."
    sna_[6] "That's ridiculous!  Your magic only works for you!"
    m "Exactly!"
    sna_[18] "Oh, you are devious!  But you said for starters..."
    m "Are you familiar with a Professor Trelawney?"
    sna_[15] "Sybil Trelawney?  That idiot?!?  Her so-called classes are a blot upon the school’s reputation!"
    sna_[7] "She’s a laughing-stock among all of the other schools in Europe!"
    m "I see. It seems I’ve instructed Miss Granger to re-enroll in Trelawney’s Divination class during her usual study time."
    m "As it turns out, Miss Granger over the years has transferred her magical aura into her wand."
    m  "She is in desperate need of instruction on how to read magical auras."
    sna_[7] "What rubbish is this?  Magical auras?  Transferring to a wand?  There's no such thing!"
    m "Ah, well, we must not disabuse Miss Granger of that notion, shall we?"
    m "She has lost the confidence that she can do much magic at all without her wand now."
    sna_[8] "That's...despicable.  I wish I had thought of that."
    m  "I’ve also asked that Trelawney person to have Miss Granger make up all the work she may have missed before and provide after-class tutoring."
    m  "I think it amounts to a couple of years of class work and of course less time to study in her other classes..."
    sna_[8] "......................"
    sna_[18] "That’s...that’s more brutal than I think I would have been.  And I hate the Granger bitch!"
    m  "Miss Granger is convinced that her troubles are because she has lost her innate magic aura.  I pointed out that the solution is simple.  "
    m  "To retrieve it she must masturbate with her wand several times per day.  This is where you can help."
    m  "You might want to let her know if you notice her aura is dwindling so she'll increase her efforts to regain it."
    sna_[18]  "..........................."
    sna_[15]  "Ah ha ha ha!  I am so very, very glad you are my ally and not my enemy."
    m "That’s kind of you to say Severus."  
    sna_[18]  "I think I'll return to my office and think about how best to leverage this new information before my next class begins."
    m "Good day, Severus."
# End alteration  JJ
    
    

    hide screen bld1
    with d3
    $ walk_xpos=360 #Animation of walking chibi. (From desk)
    $ walk_xpos2=610 #Coordinates of it's movement. (To the door)
    $ snapes_speed = 03.0 #The speed of moving the walking animation across the screen.
    show screen snape_walk_01_f 
    pause 3
    $ renpy.play('sounds/door.mp3') #Sound of a door opening.
    hide screen snape_walk_01_f 
    with d3

    $ chitchat_event_01_happened = True #Activates next event - Event_15 Hermione sells her first favour.
    $ snape_busy = True
    $ days_without_an_event = 0
    
    play music "music/Brittle Rille.mp3" fadein 1 fadeout 1
    
    jump day_main_menu











### CHITCHAT WITH HERMIONE ###
label chit_chat:
    $ one_of_ten = renpy.random.randint(1, 10) #Generating one number out of three for various porpoises.
    
    
    if whoring >= 0 and whoring <= 2: # WHORING LEVEL 01.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Maybe, if I'd work harder, I could squeeze a few more classes into my schedule..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Actually I don't mind it to be called a \"know-it-all\"."
            her "I think it's rather flattering..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "The basilisk, also known as the king of serpents."
            her "Herpo the Foul was the first to breed a Basilisk."
            her "He accomplished that by--"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Oh, I'm sorry, professor, we have another test tomorrow..."
            her "I Just want to make sure that I'm ready..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "If my body wouldn't require sleep..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I would be able to spend twice as much time with studying!?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I wonder if there's a spell for that..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "So far professor Trelawney did not taught me a single piece of any actual knowledge, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "If only more students were honest, responsible and diligent like me."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
      
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "How can some people be so ignorant to the world's problems?"
            her "Personally, I think that every single one of us should work harder to make our world a better place."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It's been raining quite a lot lately..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
    
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Very few people know this..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "...But I really like chocolate."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I am sorry sir, but I don't really have time for idle chat chats..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE


    if whoring >= 3 and whoring <= 5: # WHORING LEVEL 02
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I read somewhere that a full moon often makes it easier to concentrate at a task at hand..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I love nothing more than to curl up by a fireplace during a rainstorm with a good book..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "A peculiar rumour concerning professor Snape has been circulating in the school lately..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "No, I probably shouldn't..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Despite the questionable nature of the favours you have been buying from me lately, sir..."
            her "I am grateful to you for your help..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Gryffindor needs those points now more than ever..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Why Quidditch is so popular among the girls is simply beyond me..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "The \"Men's Rights Movement\" is steadily gaining popularity."
            her "It's very fulfilling to know that you are helping to improve our society."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "The Hogwarts school library is considered to be quite extensive..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Still, I can't help but wish that it'd be bigger..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "As one of the top students in this school I have a reputation to keep..."
            her "People look up to me..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "...So, your discretion is very appreciated, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "That favour I sold you the other say, sir..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "......."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I only agreed to it because the needs of my house always come first."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I just wanted you to know that, sir..."
            
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "The \"Autumn Ball\" is still several months away..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "But some girls are already discussing what kind of dress they are going to wear..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_185.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

  
    if whoring >= 6 and whoring <= 8: # WHORING LEVEL 03.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Do you remember when you asked me to show you my panties for the first time sir?"
            her "I was so furious with you then..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Now I see that I was just being selfish..."
            her "After all, the honour of my house is at stake here..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "And that shall be my one and only concern!"
            
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "The rate at which the Slytherin house has been gaining points lately is simply ridiculous."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_05.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I think professor Snape might be behind it."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "You should look into this, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Ashwinder eggs, rose thorns, moonstone..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Huh? Am I thinking out loud again?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I apologize..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It's just that we have another test soon..."

        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_77.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I dislike the entire house of Slytherin with all my heart, sir."
            
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Hogwarts has really become a second home to me lately..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_71.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I don't even miss my parents nearly as much anymore..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_18.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Come to think of it I don't miss them at all..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I'm an awful daughter..."

        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_70.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "*Yawn!* I read about this technique that supposedly allows you to cut your sleep time in half..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_73.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It don't think it's working though.... *Yawn!*"

        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Even after I graduate from Hogwarts I plan to keep on working hard."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "If I give it my all I can make this world a better place, I know it!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
           
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Somehow I have the feeling that this year will become a pivotal turning point in my life..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
  
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Some of the less traveled school corridors are not very well lit and rather dusty..."
            her "Please take care of this, sir..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I've read about this thing called \"Time-Turner\"."
            her "It allows the user to control the flow of time..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Having a device like that would do wonders for my schedule..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        

    if whoring >= 9 and whoring <= 11: # WHORING LEVEL 04.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "My \"men's rights movement\" has been losing its popularity lately..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It's as if people don't even care!"

        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Thank you for buying all those favours from me, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Some of them were borderline inappropriate, sure..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "But I don't mind sacrificing my dignity if it will allow Gryffindor to compete with Slytherin on equal ground."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_77.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Quidditch is stupid!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_17.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "There. I said it."
            
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Sir, there is something about professor Snape that I think you should know..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "................."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "........................."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "uhm... Never mind..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
 
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Some of the Slytherin girls sell sexual favours almost openly these days..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "You need to put an end to such practices, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "(I can barely keep up...)"

        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Life works in mysterious ways..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Wouldn't you agree, sir?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_76.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Slytherins..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_77.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I've been spending so much time in your office lately, sir..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "If I'm not careful some people may think that I have become your pet..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I meant to say the teacher's pet..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "My favourite colours?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "scarlet and gold of course!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Is it weird that my best friends are boys?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_01.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        

        
    if whoring >= 12 and whoring <= 14: # WHORING LEVEL 05.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_07.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Sir, with all due respect..."
            her "Professor Snape's debauchery is getting out of hand!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "You must do something, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I am willing to go to great lengths to insure the superiority of my house..."
            her "But that does not mean that I take pleasure in selling myself out to you in exchange for house points, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "{size=-4}(Like some sort of prostitute-witch...){/size}"

        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "What will it be today, sir?"
            
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "lately I have not been studying nearly as much as I used to..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Am I losing my motivation?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_08.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "My least favourite subject?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_09.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Divination." 
            
        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "My father used to say: \"Magic is just science we don't understand yet\"."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "He could't be more wrong of course..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Despite everything..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I am thankful that you keep on buying favours from me, sir..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It's quite cold outside today, isn't it?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "The \"Autumn Ball\" will be soon..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "People hardly show up for my \"men's rights movement\" meetings at all anymore..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                     
    
    
    
    
    
    
        
    if whoring >= 15 and whoring <= 17:  # WHORING LEVEL 06.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Would you like me to show you my breasts today, sir?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_78.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Yes... I would willingly expose myself to you, professor..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_79.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "That's how selfless I am!"
           
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I can't help but feel bad for the house elves who do my laundry..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I mean, all those dreadful semen stains..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "it Doesn't matter how many times you ask me this, sir..."
            her "The answer shall remain the same..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_47.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I have nothing but resentment for the \"Slytherins\"!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_69.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_02.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "When I think about all the favours I sold you over these last months, sir..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_87.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Although I do feel a little bit embarrassed..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I also feel very proud of myself."
            
        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I still dedicate a lot of my time to studying..."
            her "But not nearly as much of it as I used to..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Somehow I just don't enjoy studying at all anymore..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Gryffindor shall get the house cup this year!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_118.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "{size=-4}(Even if it should cost me my dignity...){/size}"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
           
           
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I don't mind the autumn weather..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "But my favourite season is winter."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I used to look down on girls who spend too much time with worrying about the way they look..."
            her "But I was wrong to do so..."
            her "I am starting to understand how important it really is for a girl to look pretty."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "..............."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I've been on a diet lately..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_33.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Lately I've been feeling rather confident around the boys..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I think I have you to thank for that, sir."
            
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "My favourite subject?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Hm..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I suppose that would be \"charms\"..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    if whoring >= 18 and whoring <= 20: # WHORING LEVEL 07.
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Just let me know what will be required of me today, sir."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_03.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
           
        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I barely study at all anymore..."
            her "Despite that my popularity among the other students seems to be growing..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Hm..."
                 
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I wouldn't say \"no\" to a bottle of butterbeer right about now..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_68.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "What is it sir? Do you have another present for me?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Oh... I see..."

        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I am doing well, thank you for asking."

        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Do I look fat to you sir?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_29.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I wonder if the diet is working..."
           
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I remember that I used to say that books were my friends..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Now that sounds so lame."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_15.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
        
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_04.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Add ashwinder egg to cauldron..."
            her "Then add horseshoe reddish and heat..."
            her "Then juice a squill bulb..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Or was it a dash of thyme first?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her ".............."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_24.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Oh, who cares?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
       
        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Do You think I am wearing enough makeup, sir?" 
            her "Wearing too much would look vulgar..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "But wearing too little would make me look plain..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_12.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I don't want to look plain!"
            
        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_64.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Would you like to see my tits today, sir?" 
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "25 house points, please."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
    
   
    if whoring >= 21: # WHORING LEVEL 08+.
        
        if one_of_ten == 1:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_189.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Do You have any adult magazines you don't need, sir?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_188.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 2:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_31.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I am sorry to bother you with this, sir..."
            her "But do you have any condoms?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_34.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "This is not for me of course... I'm asking for a friend..."
                 
        elif one_of_ten == 3:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_14.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It's been getting so cold lately..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I hope it's going to start snowing soon..."
        
        elif one_of_ten == 4:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Jump and scream for the Gryffindor team!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_80.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "So daring and bold, sporting red and gold!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 5:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_10.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I hope the ball goes smoothly..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_13.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 6:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_06.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I wonder what Ginny is going to wear for the ball..."
        
        elif one_of_ten == 7:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_16.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Considering the nature of the favours you keep buying from me sir..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_11.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I seldom bother to put on underwear at all anymore..."
        
        elif one_of_ten == 8:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_117.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Sir, could you put your penis in my mouth?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_135.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Sir, I am begging you..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_111.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Fifty five points, please!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 9:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "A read this one article about the positive effects of semen on a woman's skin..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "I wonder where their information is coming from..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_122.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "Did the magazine conduct research of some sort?"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_128.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE

        elif one_of_ten == 10:
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_127.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "It goes like this..."
            her "First Gryffindor, then Ravenclaw, then Hufflepuff..."
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_186.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            her "And Slytherin is not even on the list!"
            hide screen hermione_main                                                                                                                                                                                   #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE
            $ h_body = "01_hp/13_hermione_main/body_120.png" #Sprite of Hermione's upper body.                                                                   #HERMIONE
            show screen hermione_main                                                                                                                                                                                 #HERMIONE
            with d3                                                                                                                                                                                                                        #HERMIONE



    jump day_time_requests

#    if daytime:
#        jump night_main_menu
#    else:
#        $ hermione_sleeping = True
#        jump day_main_menu            
    
    
    