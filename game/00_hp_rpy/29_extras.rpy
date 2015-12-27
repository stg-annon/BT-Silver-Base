label gallery_ht:
    #play music galm fadeout 1
    scene title2
    with flashbb

    
    #a1 "Welcome to the \"Hermione Trainer\" gallery. Here you can have a look at some of the production artwork."
    label after_cam:
    menu:
        "-Music room-":
            jump music_room
        
        "-Sacred scrolls volume I-":
            jump volone_ht
        
        "-Sacred scrolls volume II-":
            jump voltwo
            
#        "-Gallery volume 02-":
#            jump volumetwo
        
#        "-Gallery volume 03-":
#            jump volume_three
        
        "-Outskirts of Hogwarts-":
            jump out_hog
        
        "{color=#858585}-Ending 01-{/color}" if not persistent.ending_01:
            jump after_cam
        "-Ending 01-" if persistent.ending_01:
            label end_01_men:
            menu:
                "-First act-":
                    jump end01_01
                "-The speech-":
                    jump end01_02
                "-Finishing act-":
                    jump end01_03
                "-Cancel-":
                    jump after_cam
        
        "{color=#858585}-Ending 02-{/color}" if not persistent.ending_02:
            jump after_cam
        "-Ending 02-" if persistent.ending_02:
            label end_02_men:
            menu:
                "-First act-":
                    jump end02_01
                "-The speech-":
                    jump end02_02
                "-Finishing act-":
                    jump end02_03
                "-Cancel-":
                    jump after_cam
        
            
        "-Commentaries (on)-" if commentaries:
            $ commentaries = False # In the GALLERY turns commentaries ON and OFF. 
            jump after_cam
        
        "-Commentaries (off)-" if not commentaries:
            $ commentaries = True # In the GALLERY turns commentaries ON and OFF. 
            jump after_cam
            
        "-Cancel-":
            return 
            
            
label volone_ht:
    menu:
        "-S.01: [scroll_name_[1]]-" if persistent.ss_01:
            show image "01_hp/19_extras/01.png" with d3
            if commentaries:
                a1 "This is a first ever draft of the Dumbledore's office."
                a1 "Not a very exciting thing to look at, sure. But holds great historical value."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/01.png" with d3
            pass
        "-S.02: [scroll_name_[2]]-" if persistent.ss_02:
            show image "01_hp/19_extras/02.png" with d3
            if commentaries:
                a1 "The calendar..."
                a1 "On the early stages of development I toyed with an idea of implementing an actual in-game calendar into the gameplay..."
                a1 "I soon realized how much more difficult it would be to create a game like that..."
                a1 "And since I personally believe that any time limits in any game always work against the fun factor I decided to abandon the idea..."
                a1 "Later on I used this drawing as a parchment paper for letters to be written on..."

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/02.png" with d3
            pass
        "-S.03: [scroll_name_[3]]-" if persistent.ss_03:
            show image "01_hp/19_extras/03.png" with d3
            if commentaries:
                a1 "A couple of very early drawings of Hermione..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/03.png" with d3
            pass
            
        "-S.04: [scroll_name_[4]]-" if persistent.ss_04:
            show image "01_hp/19_extras/04.png" with d3
            if commentaries:
                a1 "The deepthroating scene..."
                a1 "My first attempt."
                a1 "Been deemed unworthy and ended up here."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/04.png" with d3
            pass
            
        "-S.05: [scroll_name_[5]]-" if persistent.ss_05:
            show image "01_hp/19_extras/05.png" with d3
            if commentaries:
                a1 "The game poster..."
                a1 "Hermione is Dahr's work. The rest is me..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/05.png" with d3
            pass
            
        "-S.06: [scroll_name_[6]]-" if persistent.ss_06:
            show image "01_hp/19_extras/06.png" with d3
            if commentaries:
                a1 "Alternative game poster."
                a1 "This one has never been released."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/06.png" with d3
            pass
            
        "-S.07: [scroll_name_[7]]-" if persistent.ss_07:
            show image "01_hp/19_extras/07.png" with d3
            if commentaries:
                a1 "Some chibi closeups."
                a1 "The one on the left never made it into the final game..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/07.png" with d3
            pass
            
        "-S.08: [scroll_name_[8]]-" if persistent.ss_08:
            show image "01_hp/19_extras/08.png" with d3
            if commentaries:
                a1 "A banch of items that I ended up not using..."
                a1 "I blame dahr and his awesome artwork."

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/08.png" with d3
            pass
            
        "-S.09: [scroll_name_[9]]-" if persistent.ss_09:
            show image "01_hp/19_extras/09.png" with d3
            if commentaries:
                a1 "The drawing of Hermione from the poster. (by Dahr)"
                a1 "I like one on the right with her panties still on."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/09.png" with d3
            pass
            
        "-S.10: [scroll_name_[10]]-" if persistent.ss_10:
            show image "01_hp/19_extras/10.png" with d3
            if commentaries:
                a1 "Another ithing that never made it into the final game..."
                a1 "The idea here was that the more you level up Hermione the more pegs she would let you to put on her..."
                a1 "And the nipple chain was supposed to be worn to class under the uniform."
    
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/10.png" with d3
            pass
            
        "-S.11: [scroll_name_[11]]-" if persistent.ss_11:
            show image "01_hp/19_extras/11.png" with d3
            if commentaries:
                a1 "The house-elf brothel... Just another thing that never happened."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/11.png" with d3
            pass
            
        "-S.12: [scroll_name_[12]]-" if persistent.ss_12:
            show image "01_hp/19_extras/12.png" with d3
            if commentaries:
                a1 "A drawing featuring yours truly as a Durmstrung mage and Lola as a student..."
                a2 "The drawing itself is by Dahr of course."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/12.png" with d3
            pass
        
        
        "-S.13: [scroll_name_[13]]-" if persistent.ss_13:
            show image "01_hp/19_extras/13.png" with d3
            if commentaries:
                a1 "Another one of those side-quests that never happened..."
                a1 "This one was about--"
                a1 "No, I better not. Who knows, maybe we will get to adding those quests eventually."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/13.png" with d3
            pass
        
        "-S.14: [scroll_name_[14]]-" if persistent.ss_14:
            show image "01_hp/19_extras/14.png" with d3
            if commentaries:
                a1 "Another sub-quest..."
                a1 "This one involving the school's wizard chess club."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/14.png" with d3
            pass
        
        "-S.15: [scroll_name_[15]]-" if persistent.ss_15:
            show image "01_hp/19_extras/15.png" with d3
            if commentaries:
                a1 "There is more then one way for a pretty girl to carry her books around."
                a1 "I thought it would be cool to change the way Hermione carries the books as she progresses with her training."
                a1 "Since the whole tutoring arc got canceled I am showing it here..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/15.png" with d3
            pass
        
        "\"Never mind\"":
            jump after_cam
        
    jump volone_ht
        
        
        
        
label voltwo:
    menu:
        "-S.16: [scroll_name_[16]]-" if persistent.ss_16:
            show image "01_hp/19_extras/16.png" with d3
            if commentaries:
                a1 "A couple of items that didn't make it into the final game..."
                a1 "The one on the left is an actual live house-elf to give as a present."
                a1 "The one on the right is a portrait of a pervy but wise wizard. Supposed to be helping with studying..."

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/16.png" with d3
            pass
        "-S.17: [scroll_name_[17]]-" if persistent.ss_17:
            show image "01_hp/19_extras/17.png" with d3
            if commentaries:
                #17.
                a1 "Few more items..."
                a1 "A newspaper, a bottle of perfume and a magical hat that says things you want to hear..."

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/17.png" with d3
            pass
        "-S.18: [scroll_name_[18]]-" if persistent.ss_18:
            show image "01_hp/19_extras/18.png" with d3
            if commentaries:
                 #18.
                a1 "The fiction books..."
                a1 "The top row are my sketches, the bottom row are finalized drawings by dahr."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/18.png" with d3
            pass
            
        "-S.19: [scroll_name_[19]]-" if persistent.ss_19:
            show image "01_hp/19_extras/19.png" with d3
            if commentaries:
                #19.
                a1 "A drawing of a famous singer."
                a1 "Has no connection to this game and is here for no reason whatsoever."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/19.png" with d3
            pass
            
        "-S.20: [scroll_name_[20]]-" if persistent.ss_20:
            show image "01_hp/19_extras/20.png" with d3
            if commentaries:
                #20.
                a1 "It took me a while to come up with a proper look for Hermione..."
                a1 "Version \"A\" was my first attempt. And I liked it up until the moment when I started to hate it..."
                a2 "Version \"B\" was my second attempt. And it's good. But her confident and semi-aggressive facial features didn't fit the character well..."
                a1 "Version \C\" is the one that got the role. The Hermione that we all grew to care for by now, I'm sure."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/20.png" with d3
            pass
            
        "-S.21: [scroll_name_[21]]-" if persistent.ss_21:
            show image "01_hp/19_extras/21.png" with d3
            if commentaries:
                #21 
                a1 "Sub-quests that never happened."
                a1 "You are allowed to feel bad for rushing me."
                a1 "If you did not rush me you are allowed to feel angry at people who did."

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/21.png" with d3
            pass
            
        "-S.22: [scroll_name_[22]]-" if persistent.ss_22:
            show image "01_hp/19_extras/22.png" with d3
            if commentaries:
                #22
                a1 "Hermione presenting her body to Genie..."
                a1 "This would have been a quite memorable scene..."

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/22.png" with d3
            pass
            
        "-S.23: [scroll_name_[23]]-" if persistent.ss_23:
            show image "01_hp/19_extras/23.png" with d3
            if commentaries:
                #23. 
                a1 "Didn't expect this one, did you?"
                a1 "In case you're wondering this is still Hermione."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/23.png" with d3
            pass
            
        "-S.24: [scroll_name_[24]]-" if persistent.ss_24:
            show image "01_hp/19_extras/24.png" with d3
            if commentaries:
                #24.
                a1 "................................."
                a1 "Sub-quests of course..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/24.png" with d3
            pass
            
        "-S.25: [scroll_name_[25]]-" if persistent.ss_25:
            show image "01_hp/19_extras/25.png" with d3
            if commentaries:
                #25.
                a1 "Another sub-quest..."
                a1 "We had a rather lengthy discussion with Dahr about this one..."
                a1 "I was sort of against it, but then Dahr sent me this picture and it made me shut up."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/25.png" with d3
            pass
            
        "-S.26: [scroll_name_[26]]-" if persistent.ss_26:
            show image "01_hp/19_extras/26.png" with d3
            if commentaries:
                #26.
                a1 "One the very early stages of development I had an idea of representing outcomes of your failed or successfully completed sub quests with a simplistic plates, or photographs..."
                a1 "At first many of the sub-quests involved deciding on how to spend the Hogwarts budget..."
                a1 "Spend your money to finance the school quiddich team, or to hire new teachers and such..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/26.png" with d3
            pass
            
        "-S.27: [scroll_name_[27]]-" if persistent.ss_27:
            show image "01_hp/19_extras/27.png" with d3
            if commentaries:
                #27.
                a1 "Isn't she adorable?"

            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/27.png" with d3
            pass

        
        "-S.28: [scroll_name_[28]]-" if persistent.ss_28:
            show image "01_hp/19_extras/28.png" with d3
            if commentaries:
                #28.
                a1 "Another (rather lengthy) sub-quest..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/28.png" with d3
            pass
        
        "-S.29: [scroll_name_[29]]-" if persistent.ss_29:
            show image "01_hp/19_extras/29.png" with d3
            if commentaries:
                #29.
                a1 ".........."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/29.png" with d3
            pass
        
        "-S.30: [scroll_name_[30]]-" if persistent.ss_30:
            show image "01_hp/19_extras/30.png" with d3
            if commentaries:
                #30.
                a1 "One of the very early sketches related to the quiddich sub-quests..."
            show screen ctc
            pause
            hide screen ctc
            hide image "01_hp/19_extras/30.png" with d3
            pass
        
        "\"Never mind\"":
            jump after_cam
        
    jump voltwo
    
        
        
        
        
        
    
            
               


                

                

                
                
                

                

                

                

                
                

                

                


        
            
            
            
            
        
        
        
        
        
        
        
        
        
    ### OUTSKIRTS OF HOGWARTS CGs ###
label out_hog:
    show image  "01_hp/17_ending/171.png" with d3
    show screen ctc
    pause
    
    show image  "01_hp/17_ending/172.png" with d3
    show screen ctc
    pause

    

    show image  "01_hp/17_ending/173.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/173.png" 
    hide image  "01_hp/17_ending/172.png" 
    show image  "01_hp/17_ending/174.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/174.png" 
    show image  "01_hp/17_ending/175.png" 
    with d3
    pause
    

    hide image  "01_hp/17_ending/175.png" with d3
    
    pause
    
    hide image  "01_hp/17_ending/171.png" 
    hide screen ctc
    with fade
    
    jump after_cam
        
        
        
    ### ENDING 01_01
label end01_01:
    show image  "01_hp/17_ending/01.png" with d3
    show screen ctc
    pause
    
    hide image  "01_hp/17_ending/01.png" 
    show image  "01_hp/17_ending/02.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/02.png" 
    show image  "01_hp/17_ending/03.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/03.png" 
    show image  "01_hp/17_ending/04.png" 
    with d3
    pause
        
    hide image  "01_hp/17_ending/04.png" 
    show image  "01_hp/17_ending/05.png" 
    with d3
    pause
        
    hide image  "01_hp/17_ending/05.png" 
    show image  "01_hp/17_ending/06.png" 
    with d3
    pause    
        
    hide image  "01_hp/17_ending/06.png" 
    show image  "01_hp/17_ending/07.png" 
    with d3
    pause    
        
    hide image  "01_hp/17_ending/07.png" 
    show image  "01_hp/17_ending/08.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/08.png" 
    show image  "01_hp/17_ending/09.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/09.png" 
    show image  "01_hp/17_ending/10.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/10.png" 
    show image  "01_hp/17_ending/11.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/11.png" 
    show image  "01_hp/17_ending/12.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/12.png" 
    show image  "01_hp/17_ending/13.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/13.png" 
    show image  "01_hp/17_ending/14.png" 
    with d3
    pause
        
    hide image  "01_hp/17_ending/14.png" 
    show image  "01_hp/17_ending/15.png" 
    with d3
    pause
       
    hide image  "01_hp/17_ending/15.png" 
    show image  "01_hp/17_ending/16.png" 
    with d3
    pause   
       
    hide image  "01_hp/17_ending/16.png" 
    show image  "01_hp/17_ending/17.png" 
    with d3
    pause   
       
    hide image  "01_hp/17_ending/17.png" 
    show image  "01_hp/17_ending/18.png" 
    with d3
    pause   
       
    hide image  "01_hp/17_ending/18.png" 
    show image  "01_hp/17_ending/19.png" 
    with d3
    pause   
       
    hide image  "01_hp/17_ending/19.png" 
    show image  "01_hp/17_ending/20.png" 
    with d3
    pause   
       
    hide image  "01_hp/17_ending/20.png" 
    show image  "01_hp/17_ending/21.png" 
    with d3
    pause   
       
    hide image  "01_hp/17_ending/21.png" 
    show image  "01_hp/17_ending/22.png" 
    with d3
    pause
       
    hide image  "01_hp/17_ending/22.png" 
    show image  "01_hp/17_ending/23.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/23.png" 
    show image  "01_hp/17_ending/24.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/24.png" 
    show image  "01_hp/17_ending/25.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/25.png" 
    show image  "01_hp/17_ending/26.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/26.png" 
    show image  "01_hp/17_ending/27.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/27.png" 
    show image  "01_hp/17_ending/28.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/28.png" 
    show image  "01_hp/17_ending/29.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/29.png" 
    show image  "01_hp/17_ending/30.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/30.png" 
    show image  "01_hp/17_ending/31.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/31.png" 
    show image  "01_hp/17_ending/32.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/32.png" 
    show image  "01_hp/17_ending/33.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/33.png" 
    show image  "01_hp/17_ending/34.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/34.png" 
    show image  "01_hp/17_ending/35.png" 
    with d3
    pause
       
    hide image  "01_hp/17_ending/35.png" 
    show image  "01_hp/17_ending/36.png" 
    with d3
    pause
       
    hide image  "01_hp/17_ending/36.png" 
    with fade
    jump end_01_men
        

    ### ENDING 01_02
label end01_02:
    show image  "01_hp/17_ending/37.png" with d3
    show screen ctc
    pause
    
    hide image  "01_hp/17_ending/37.png" 
    show image  "01_hp/17_ending/38.png" 
    with d3
    pause

    hide image  "01_hp/17_ending/38.png" 
    show image  "01_hp/17_ending/39.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/39.png" 
    show image  "01_hp/17_ending/40.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/40.png" 
    show image  "01_hp/17_ending/41.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/41.png" 
    show image  "01_hp/17_ending/42.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/42.png" 
    show image  "01_hp/17_ending/43.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/43.png" 
    show image  "01_hp/17_ending/44.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/44.png" 
    show image  "01_hp/17_ending/45.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/45.png" 
    with fade
    jump end_01_men
    
    
    
    
   ### ENDING 01_03
label end01_03:
    show image  "01_hp/17_ending/46.png" with d3
    show screen ctc
    pause
    
    hide image  "01_hp/17_ending/46.png" 
    show image  "01_hp/17_ending/47.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/47.png" 
    show image  "01_hp/17_ending/48.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/48.png" 
    show image  "01_hp/17_ending/49.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/49.png" 
    show image  "01_hp/17_ending/50.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/50.png" 
    show image  "01_hp/17_ending/51.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/51.png" 
    show image  "01_hp/17_ending/52.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/52.png" 
    show image  "01_hp/17_ending/53.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/53.png" 
    show image  "01_hp/17_ending/54.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/54.png" 
    show image  "01_hp/17_ending/55.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/55.png" 
    show image  "01_hp/17_ending/56.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/56.png" 
    show image  "01_hp/17_ending/57.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/57.png" 
    show image  "01_hp/17_ending/58.png" 
    with d3
    pause
    hide image  "01_hp/17_ending/58.png" 
    show image  "01_hp/17_ending/59.png" 
    with d3
    pause
    hide image  "01_hp/17_ending/59.png" 
    show image  "01_hp/17_ending/60.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/60.png" 
    show image  "01_hp/17_ending/61.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/61.png" 
    show image  "01_hp/17_ending/62.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/62.png" 
    show image  "01_hp/17_ending/63.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/63.png" 
    show image  "01_hp/17_ending/64.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/64.png" 
    show image  "01_hp/17_ending/65.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/65.png" 
    show image  "01_hp/17_ending/66.png" 
    with d3
    pause
    
    
    hide image  "01_hp/17_ending/66.png" 
    show image  "01_hp/17_ending/67.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/67.png" 
    show image  "01_hp/17_ending/68.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/68.png" 
    show image  "01_hp/17_ending/69.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/69.png" 
    show image  "01_hp/17_ending/70.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/70.png" 
    show image  "01_hp/17_ending/71.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/71.png" 
    show image  "01_hp/17_ending/72.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/72.png" 
    show image  "01_hp/17_ending/73.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/73.png" 
    show image  "01_hp/17_ending/74.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/74.png" 
    show image  "01_hp/17_ending/75.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/75.png" 
    show image  "01_hp/17_ending/76.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/76.png" 
    show image  "01_hp/17_ending/77.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/77.png" 
    show image  "01_hp/17_ending/78.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/78.png" 
    show image  "01_hp/17_ending/79.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/79.png" 
    show image  "01_hp/17_ending/80.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/80.png" 
    show image  "01_hp/17_ending/81.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/81.png" 
    show image  "01_hp/17_ending/82.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/82.png" 
    show image  "01_hp/17_ending/83.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/83.png" 
    show image  "01_hp/17_ending/84.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/84.png" 
    show image  "01_hp/17_ending/85.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/85.png" 
    show image  "01_hp/17_ending/86.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/86.png" 
    show image  "01_hp/17_ending/87.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/87.png" 
    show image  "01_hp/17_ending/88.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/88.png" 
    show image  "01_hp/17_ending/89.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/89.png" 
    with fade
    jump end_01_men
    
    
      ### ENDING 02_01
label end02_01:
    show image  "01_hp/17_ending/01.png" with d3
    show screen ctc
    pause
    
    hide image  "01_hp/17_ending/01.png" 
    show image  "01_hp/17_ending/02.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/02.png" 
    show image  "01_hp/17_ending/03.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/03.png" 
    show image  "01_hp/17_ending/91.png" 
    with d3
    pause

    hide image  "01_hp/17_ending/91.png" 
    show image  "01_hp/17_ending/92.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/92.png" 
    show image  "01_hp/17_ending/93.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/93.png" 
    show image  "01_hp/17_ending/94.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/94.png" 
    show image  "01_hp/17_ending/95.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/95.png" 
    show image  "01_hp/17_ending/96.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/96.png" 
    show image  "01_hp/17_ending/97.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/97.png" 
    show image  "01_hp/17_ending/98.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/98.png" 
    show image  "01_hp/17_ending/99.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/99.png" 
    show image  "01_hp/17_ending/100.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/100.png" 
    show image  "01_hp/17_ending/101.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/101.png" 
    show image  "01_hp/17_ending/102.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/102.png" 
    show image  "01_hp/17_ending/103.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/103.png" 
    show image  "01_hp/17_ending/104.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/104.png" 
    show image  "01_hp/17_ending/105.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/105.png" 
    show image  "01_hp/17_ending/106.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/106.png" 
    show image  "01_hp/17_ending/107.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/107.png" 
    with fade
    jump end_02_men
    

    
      ### ENDING 02_02
label end02_02:
    show image  "01_hp/17_ending/108.png" with d3
    show screen ctc
    pause
    
    hide image  "01_hp/17_ending/108.png" 
    show image  "01_hp/17_ending/109.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/109.png" 
    show image  "01_hp/17_ending/110.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/110.png" 
    show image  "01_hp/17_ending/111.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/111.png" 
    show image  "01_hp/17_ending/112.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/112.png" 
    show image  "01_hp/17_ending/113.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/113.png" 
    show image  "01_hp/17_ending/114.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/114.png" 
    show image  "01_hp/17_ending/115.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/115.png" 
    show image  "01_hp/17_ending/116.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/116.png" 
    show image  "01_hp/17_ending/117.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/117.png" 
    show image  "01_hp/17_ending/118.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/118.png" 
    show image  "01_hp/17_ending/119.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/119.png" 
    show image  "01_hp/17_ending/120.png" 
    with d3
    pause
    hide image  "01_hp/17_ending/120.png" 
    show image  "01_hp/17_ending/121.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/121.png" 
    show image  "01_hp/17_ending/122.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/122.png" 
    show image  "01_hp/17_ending/123.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/123.png" 
    with fade
    jump end_02_men


         ### ENDING 02_03
label end02_03:
    show image  "01_hp/17_ending/124.png" with d3
    show screen ctc
    pause
    
    hide image  "01_hp/17_ending/124.png" 
    show image  "01_hp/17_ending/125.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/125.png" 
    show image  "01_hp/17_ending/126.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/126.png" 
    show image  "01_hp/17_ending/127.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/127.png" 
    show image  "01_hp/17_ending/128.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/128.png" 
    show image  "01_hp/17_ending/129.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/129.png" 
    show image  "01_hp/17_ending/130.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/130.png" 
    show image  "01_hp/17_ending/131.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/131.png" 
    show image  "01_hp/17_ending/132.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/132.png" 
    show image  "01_hp/17_ending/133.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/133.png" 
    show image  "01_hp/17_ending/134.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/134.png" 
    show image  "01_hp/17_ending/135.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/135.png" 
    show image  "01_hp/17_ending/136.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/136.png" 
    show image  "01_hp/17_ending/137.png" 
    with d3
    pause
    hide image  "01_hp/17_ending/137.png" 
    show image  "01_hp/17_ending/138.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/138.png" 
    show image  "01_hp/17_ending/139.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/139.png" 
    show image  "01_hp/17_ending/140.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/140.png" 
    show image  "01_hp/17_ending/141.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/141.png" 
    show image  "01_hp/17_ending/142.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/142.png" 
    show image  "01_hp/17_ending/143.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/143.png" 
    show image  "01_hp/17_ending/144.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/144.png" 
    show image  "01_hp/17_ending/145.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/145.png" 
    show image  "01_hp/17_ending/146.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/146.png" 
    show image  "01_hp/17_ending/147.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/147.png" 
    show image  "01_hp/17_ending/148.png" 
    with d3
    pause
    hide image  "01_hp/17_ending/148.png" 
    show image  "01_hp/17_ending/149.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/149.png" 
    show image  "01_hp/17_ending/150.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/150.png" 
    show image  "01_hp/17_ending/151.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/151.png" 
    show image  "01_hp/17_ending/152.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/152.png" 
    show image  "01_hp/17_ending/153.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/153.png" 
    show image  "01_hp/17_ending/154.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/154.png" 
    show image  "01_hp/17_ending/155.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/155.png" 
    show image  "01_hp/17_ending/156.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/156.png" 
    show image  "01_hp/17_ending/157.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/157.png" 
    show image  "01_hp/17_ending/158.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/158.png" 
    show image  "01_hp/17_ending/159.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/159.png" 
    show image  "01_hp/17_ending/160.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/160.png" 
    show image  "01_hp/17_ending/161.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/161.png" 
    show image  "01_hp/17_ending/162.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/162.png" 
    show image  "01_hp/17_ending/163.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/163.png" 
    show image  "01_hp/17_ending/164.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/164.png" 
    show image  "01_hp/17_ending/165.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/165.png" 
    show image  "01_hp/17_ending/166.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/166.png" 
    show image  "01_hp/17_ending/167.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/167.png" 
    show image  "01_hp/17_ending/168.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/168.png" 
    show image  "01_hp/17_ending/169.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/169.png" 
    show image  "01_hp/17_ending/170.png" 
    with d3
    pause
    
    hide image  "01_hp/17_ending/170.png" 
    with fade
    jump end_02_men

    
    
    
    ### INTRO ###
    label intro:
        play music "music/TheKiss.mp3" fadein 1 fadeout 1 
        
        centered "{size=+7}{color=#cbcbcb}Previously in the AKABUR's \"MAGIC SHOP\"...{/color}{/size}"
        show intro_01 with flashbb # WHITE FLASH.
        pause
        hide intro_01 
        show intro_02 
        with flashbulb # WHITE FLASH.
        pause
        hide intro_02 
        show intro_03
        with flashbulb # WHITE FLASH.
        pause
        hide intro_03 
        show intro_04 
        with flashbulb # WHITE FLASH.
        pause
        hide intro_04 
        show intro_05 
        with flashbulb # WHITE FLASH.
        pause
        hide intro_05 
        show intro_06 
        with hpunch
        pause
        hide intro_06 
        with flashbulb # WHITE FLASH.
        
        centered "{size=+7}{color=#cbcbcb}And now akabur's \"Witch Trainer\"...{/color}{/size}"
        jump hp
        
        
    ### MUSIC ROOM ###
label music_room:
    $ d_flag_01 = False
    $ d_flag_02 = False
    $ d_flag_03 = False
    $ d_flag_04 = False
    $ d_flag_05 = False
    $ d_flag_06 = False
    $ d_flag_07 = False
    $ d_flag_08 = False
    $ d_flag_09 = False
    $ d_flag_10 = False
    $ d_flag_11 = False
    $ d_flag_12 = False
    $ d_flag_13 = False
    $ d_flag_14 = False
    $ d_flag_15 = False
    
    label music_room2:
        pass
    
    menu:
        "{image=note2.png} Playful Tension by Shadow16nh {image=note2.png}" if d_flag_01:
            pass
        "Playful Tension by Shadow16nh" if not d_flag_01:
            $ d_flag_01 = True
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/(Orchestral) Playful Tension by Shadow16nh.mp3" fadein 1 fadeout 1 # SEX THEME.
        
        "{image=note2.png} Shanghai Honey by Orange Range {image=note2.png}" if d_flag_02:
            pass
        "Shanghai Honey by Orange Range" if not d_flag_02:
            $ d_flag_01 = False
            $ d_flag_02 = True
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/02 - Shanghai Honey.mp3" fadein 1 fadeout 1 
       
        
        
        
        
        "{image=note2.png} Introducing Colin Harry Potter OST {image=note2.png}" if d_flag_03:
            pass
        "Introducing Colin Harry Potter OST" if not d_flag_03:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = True
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/07 Introducing Colin2.mp3" fadein 1 fadeout 1 
        
        "{image=note2.png} Neville's Waltz Harry Potter OST {image=note2.png}" if d_flag_04:
            pass
        "Neville's Waltz Harry Potter OST" if not d_flag_04:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = True
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/11 Neville's Waltz.mp3" fadein 1 fadeout 1 
            
            
            
            
        "{image=note2.png} The Quidditch Match Harry Potter OST {image=note2.png}" if d_flag_05:
            pass
        "The Quidditch Match Harry Potter OST" if not d_flag_05:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = True
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/11 The Quidditch Match.mp3" fadein 1 fadeout 1 
        
        
        "{image=note2.png} Anguish by Kevin MacLeod {image=note2.png}" if d_flag_06:
            pass
        "Anguish by Kevin MacLeod" if not d_flag_06:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = True
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Anguish.mp3" fadein 1 fadeout 1 
            
            
            
            
        "{image=note2.png} Brittle Rille by Kevin MacLeod {image=note2.png}" if d_flag_07:
            pass
        "Brittle Rille by Kevin MacLeod" if not d_flag_07:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = True
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Brittle Rille.mp3" fadein 1 fadeout 1 
            
            
            
            
            
        "{image=note2.png} Chipper Doodle v2 by Kevin MacLeod {image=note2.png}" if d_flag_08:
            pass
        "Chipper Doodle v2 by Kevin MacLeod" if not d_flag_08:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = True
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Chipper Doodle v2.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Dark Fog by Kevin MacLeod {image=note2.png}" if d_flag_09:
            pass
        "Dark Fog by Kevin MacLeod" if not d_flag_09:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = True
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Dark Fog.mp3" fadein 1 fadeout 1 



        "{image=note2.png} Final Fantasy VII Game Over Theme {image=note2.png}" if d_flag_10:
            pass
        "Final Fantasy VII Game Over Theme" if not d_flag_10:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = True
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1


 
        "{image=note2.png} Final Fantasy VII Boss Theme {image=note2.png}" if d_flag_11:
            pass
        "Final Fantasy VII Boss Theme" if not d_flag_11:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = True
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Hitman by Kevin MacLeod {image=note2.png}" if d_flag_12:
            pass
        "Hitman by Kevin MacLeod" if not d_flag_12:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = True
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Hitman.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Music for Manatees by Kevin MacLeod {image=note2.png}" if d_flag_13:
            pass
        "Music for Manatees by Kevin MacLeod" if not d_flag_13:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = True
            $ d_flag_14 = False
            $ d_flag_15 = False
            play music "music/Music for Manatees.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Plaint by Kevin MacLeod {image=note2.png}" if d_flag_14:
            pass
        "Plaint by Kevin MacLeod" if not d_flag_14:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = True
            $ d_flag_15 = False
            play music "music/Plaint.mp3" fadein 1 fadeout 1



 
        "{image=note2.png} Under-the-Radar by PhobyAk {image=note2.png}" if d_flag_15:
            pass
        "Under-the-Radar by PhobyAk" if not d_flag_15:
            $ d_flag_01 = False
            $ d_flag_02 = False
            $ d_flag_03 = False
            $ d_flag_04 = False
            $ d_flag_05 = False
            $ d_flag_06 = False
            $ d_flag_07 = False
            $ d_flag_08 = False
            $ d_flag_09 = False
            $ d_flag_10 = False
            $ d_flag_11 = False
            $ d_flag_12 = False
            $ d_flag_13 = False
            $ d_flag_14 = False
            $ d_flag_15 = True
            play music "music/Under-the-Radar by PhobyAk.mp3" fadein 1 fadeout 1 
            
            
            
            
        "-No music-":
            stop music fadeout 1.0
            jump music_room
        "-Keep the current tune-":
            jump gallery_ht
    jump music_room2
        
        
        
        
        
        
        
        
        
        
        
        

        
    ### MESSAGES ###
        
label gallery_locked_ht:
    $ end_u_2_pic =  "title2.jpg" #<---- SCREEN
    show screen end_u_2                                             #<---- SCREEN
    ">Beat the game to unlock the gallery."
    hide screen end_u_2                                             #<---- SCREEN
    show screen extras
    return