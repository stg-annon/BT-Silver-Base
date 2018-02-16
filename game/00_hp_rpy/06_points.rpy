label points_changes: # SLYTHERIN POINTS AWARDING
    if generating_points == 1: # NO POINTS FOR SLYTHERIN ON THIS DAY.
            pass
    elif generating_points == 2: # POINTS WILL BE AWARDED
        

        if game_difficulty <= 1:  #Easy Difficulty
            if snapes_support == 0: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=5     #Normal=2
                hide screen s_p_u
                $ s_p_u_pic = "what_05_points"
                show screen s_p_u
        
            if snapes_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=8     #Normal=5
                hide screen s_p_u
                $ s_p_u_pic = "what_08_points"
                show screen s_p_u

            if snapes_support == 2: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=11    #Normal=7
                hide screen s_p_u
                $ s_p_u_pic = "what_11_points"
                show screen s_p_u
        
            if snapes_support == 3: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=15    #Normal=8
                hide screen s_p_u
                $ s_p_u_pic = "what_15_points"
                show screen s_p_u

            if snapes_support == 4: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=18    #Normal=11
                hide screen s_p_u
                $ s_p_u_pic = "what_18_points"
                show screen s_p_u
        
            if snapes_support == 5: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=21    #Normal=13
                hide screen s_p_u
                $ s_p_u_pic = "what_21_points"
                show screen s_p_u
        
            if snapes_support == 6: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=24    #Normal=15
                hide screen s_p_u
                $ s_p_u_pic = "what_24_points"
                show screen s_p_u
            
            if snapes_support == 7: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=27    #Normal=17
                hide screen s_p_u
                $ s_p_u_pic = "what_27_points"
                show screen s_p_u
        
            if snapes_support == 8: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=29    #Normal=19
                hide screen s_p_u
                $ s_p_u_pic = "what_29_points"
                show screen s_p_u
        
            if snapes_support == 9: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=31    #Normal=21
                hide screen s_p_u
                $ s_p_u_pic = "what_31_points"
                show screen s_p_u
            
            if snapes_support == 10: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=34     #Normal=23
                hide screen s_p_u
                $ s_p_u_pic = "what_34_points"
                show screen s_p_u

            if snapes_support == 11: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=38     #Normal=25
                hide screen s_p_u
                $ s_p_u_pic = "what_38_points"
                show screen s_p_u

            if snapes_support == 12: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=41     #Normal=27
                hide screen s_p_u
                $ s_p_u_pic = "what_41_points"
                show screen s_p_u
        
            if snapes_support == 13: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=44     #Normal=29
                hide screen s_p_u
                $ s_p_u_pic = "what_44_points"
                show screen s_p_u
            
            if snapes_support == 14: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=47     #Normal=31
                hide screen s_p_u
                $ s_p_u_pic = "what_47_points"
                show screen s_p_u

            if snapes_support == 15: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=50     #Normal=40
                hide screen s_p_u
                $ s_p_u_pic = "what_50_points" #Images only go to 50.
                show screen s_p_u

        else:   #normal difficulty

            if snapes_support == 0: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=2
                hide screen s_p_u
                $ s_p_u_pic = "what_02_points"
                show screen s_p_u
       
            if snapes_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=5
                hide screen s_p_u
                $ s_p_u_pic = "what_05_points"
                show screen s_p_u

            if snapes_support == 2: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=7
                hide screen s_p_u
                $ s_p_u_pic = "what_07_points"
                show screen s_p_u
        
            if snapes_support == 3: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=8
                hide screen s_p_u
                $ s_p_u_pic = "what_08_points"
                show screen s_p_u

            if snapes_support == 4: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=11
                hide screen s_p_u
                $ s_p_u_pic = "what_11_points"
                show screen s_p_u
        
            if snapes_support == 5: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=13
                hide screen s_p_u
                $ s_p_u_pic = "what_13_points"
                show screen s_p_u
        
            if snapes_support == 6: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=15
                hide screen s_p_u
                $ s_p_u_pic = "what_15_points"
                show screen s_p_u
            
            if snapes_support == 7: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=17
                hide screen s_p_u
                $ s_p_u_pic = "what_17_points"
                show screen s_p_u
        
            if snapes_support == 8: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=19
                hide screen s_p_u
                $ s_p_u_pic = "what_19_points"
                show screen s_p_u
        
            if snapes_support == 9: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=21
                hide screen s_p_u
                $ s_p_u_pic = "what_21_points"
                show screen s_p_u
            
            if snapes_support == 10: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=23
                hide screen s_p_u
                $ s_p_u_pic = "what_23_points"
                show screen s_p_u

            if snapes_support == 11: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=25
                hide screen s_p_u
                $ s_p_u_pic = "what_25_points"
                show screen s_p_u

            if snapes_support == 12: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=27
                hide screen s_p_u
                $ s_p_u_pic = "what_27_points"
                show screen s_p_u
        
            if snapes_support == 13: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=29
                hide screen s_p_u
                $ s_p_u_pic = "what_29_points"
                show screen s_p_u
            
            if snapes_support == 14: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=31
                hide screen s_p_u
                $ s_p_u_pic = "what_31_points"
                show screen s_p_u

            if snapes_support == 15: #Controls how much points is awarded to SLYTHERIN daily.
                $ slytherin +=40
                hide screen s_p_u
                $ s_p_u_pic = "what_40_points"
                show screen s_p_u
    return

      
#        if snapes_support == 1: #Controls how much points is awarded to SLYTHERIN daily.
#            $ slytherin +=7
#            "Slytherin got +7 points."
            
#        if day >= 15 and day <= 21: #WEEK No.3 (Needs 30)
#            $ slytherin +=10
#            "Slytherin got +10 points."
            
#        if day >= 22 and day <= 28: #WEEK No.4 (Needs 50)
#            $ slytherin +=15
#            "Slytherin got +15 points."
            
#        if day >= 29 and day <= 35: #WEEK No.5 (Needs 60)
#            $ slytherin +=15
#            "Slytherin got +15 points."
            
#        if day >= 36 and day <= 42: #WEEK No.6 (Needs 70)
#            $ slytherin +=22
#            "Slytherin got +22 points."
            
#        if day >= 43 and day <= 49: #WEEK No.7 (Needs 90)
#            $ slytherin +=26
#            "Slytherin got +26 points."
            
#        if day >= 50 and day <= 56: #WEEK No.8 (Needs 100)
#            $ slytherin +=32
#            "Slytherin got +32 points."
            
#        if day >= 57 and day <= 63: #WEEK No.9 (Needs 110)
#            $ slytherin +=36
#            "Slytherin got +36 points."
            
#        if day >= 64 and day <= 70: #WEEK No.10 (Needs 130)
#            $ slytherin +=43
#            "Slytherin got +43 points."
            
#        if day >= 71 and day <= 77: #WEEK No.11 (Needs 140)
#            $ slytherin +=46
#            "Slytherin got +46 points."
            
#        if day >= 78 and day <= 84: #WEEK No.12 (Needs 150)
#            $ slytherin +=50
#            "Slytherin got +50 points."
            
#        if day >= 85 and day <= 91: #WEEK No.13 (Needs 170)
#            $ slytherin +=56
#            "Slytherin got +56 points."
            
#        if day >= 92 and day <= 98: #WEEK No.14 (Needs 185)
#            $ slytherin +=61
#            "Slytherin got +61 points."
            
#        if day >= 105: #WEEK No.15 (Needs 200)
#            $ slytherin +=66
#            "Slytherin got +66 points."




        
    
    
