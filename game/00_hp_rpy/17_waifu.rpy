label __init_variables:
    if not hasattr(renpy.store,'shea'): #important!
        $ shea = 0 #Shows how many times you went on a date with your stepsister Shea.
    if not hasattr(renpy.store,'shea_waifu'): #important!
        $ shea_waifu = False #Turns True if you finish the book with Shea.
    if not hasattr(renpy.store,'complited_shea_already'): #important!
        $ complited_shea_already = False #Turns TRUE when you finish with Shea once. Need so that when you finish with Shea again you don get +1 Imagination.
    
    if not hasattr(renpy.store,'victoria'): #important!
        $ victoria = 0
    if not hasattr(renpy.store,'victoria_waifu'): #important!
        $ victoria_waifu = False #Turns True if you finish the book with ms.Victoria.
    if not hasattr(renpy.store,'complited_stevens_already'): #important!
        $ complited_stevens_already = False #Turns TRUE when you finish with Ms.Stevens once. Need so that when you finish with Shea again you don get +1 Imagination.
    
    if not hasattr(renpy.store,'leena'): #important!
        $ leena = 0
    if not hasattr(renpy.store,'leena_waifu'): #important!
        $ leena_waifu = False #Completed the book with Leena.
    if not hasattr(renpy.store,'complited_leena_already'): #important!
        $ complited_leena_already = False #Turns TRUE when you finish with Leena once. Need so that when you finish with Shea again you don get +1 Imagination.
    
    if not hasattr(renpy.store,'waifu_book_completed'): #important!
        $ waifu_book_completed = False #Turns TRUE when you unlock the harem ending.
    
    return

label waifu:
    if Dear_Wifu_OBJ.progress == 1:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}You are a teenage boy who is sharing his home with his cute stepsister Shea. What would you like to do after school today?{/size}"
        if not complited_leena_already and not complited_stevens_already and not complited_shea_already:
            m "Oh, it's one of \"those\" books then. Ok, let's see..."
        call school_ended
    if Dear_Wifu_OBJ.progress == 2:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}During classes ms.Stevens is droning away about something. You admire her chest to stay awake. She's way too hot to be a teacher.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 3:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}You meet your stepsister at school. Unlike you, Shea is quite popular among her classmates, but She all but denies your existence.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 4:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}You bump into a girl in the hallway, She is wearing thick glasses and acts very shy. afterwards She apologizes and quickly runs off, is she even a student of this school?{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 5:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}Ms.Stevens is organizing extracurricular activities today. You decide to show up in hopes of extra credit.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 6:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}A bully takes your lunch money today. Later Shea shows up and brings the bully with her, He apologizes and returns you your money. Shea can be scary...{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 7:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}Another boring class. You ignore the teacher completely and daydream about getting a degree in art and becoming a professional hentai-manga artist.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 8:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}Another terribly generic school day, Ms.Stevens' modest green suit does little to conceal her attractive figure. You couldn't care less about the topic of her class though.{/size}" 
        call school_ended
    if Dear_Wifu_OBJ.progress == 9:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}You ditch your classes and roam through the deserted school corridors, pretending to be the sole survivor of some deadly virus. The janitor spots you, He's infected! You run for your life.{/size}" 
        call school_ended
    if Dear_Wifu_OBJ.progress == 10:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The same bully takes your money again. An hour later an ambulance parks before school, Some guy broke his hand. You recognize your bully... Did Shea do this to him?{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 11:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Another day in school. After the incident with the bully, people are looking at you funnily, but they seem to adore Shea more than ever. How is she doing it?{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 12:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You have no classes with ms.Stevens today. So why even bother? You fall asleep behind your desk.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 13:   
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Your classmates all seem to be very excited about the upcoming prom, but You couldn't care less for the stupid thing.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 14:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Another boring class. You gaze out of the window and notice a suspicious looking black van with tinted windows parked nearby the school library building. Why?{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 15:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You overhear one of your classmates talking about starting a secret \"Ms.Stevens fan club\". Not very surprising, considering how attractive she is.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 16:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Everyone's excitement about the upcoming prom grows with every day. You toy with an idea of asking someone to the prom, but decide to save yourself the awkwardness.{/size}" 
        call school_ended
    if Dear_Wifu_OBJ.progress == 17:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Ms.Stevens is wearing her skintight business suit again today. All the guys in your class look very eager to learn, while many of the girls are pouting.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 18:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The graduation ceremony is tomorrow. Everyone is very excited, but You just want this day to end.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 19:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Today is your graduation day. You see your classmates getting emotional during the ceremony, but you don't care much.{/size}"
        call school_ended
    if Dear_Wifu_OBJ.progress == 20:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The prom will take place tonight. You have nothing to do today, No chores, no homework... So this is how it feels to be free!?{/size}"
        if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1:
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You decide to go to the prom and you're surprised to see the \"library girl\" there. She invites you to a dance and kisses you. You notice Shea staring at you incredulously.{/size}"
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The \"library girl\" leads you outside. She kisses you, takes your dick out and starts jerking it. Shea appears from behind the corner of the building.{/size}"
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Shea gets mad and starts yelling at the girl who continues to jerk you off. Alarmed by all the yelling Ms.Stevens shows up and You still have your pants down.{/size}"
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You pull your pants up, completely embarrassed. Ms.Stevens stays calm and simply leaves to bring her car around. Afterwards She orders all of you in the car and takes you to a motel.{/size}"
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}In the motel room she grabs your crotch, takes your cock out and starts jerking it off. Shea is in shock but the \"library girl\" is already kissing you.{/size}"
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Reluctantly Shea joins the girls. You fuck your step sister first, up her butt of course. The \"library girl\" is next in line, Then Ms.Stevens.{/size}"
            "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}When you wake up everyone but Shea is gone. Your stepsister is asleep, You spread her butt cheeks and slide your morning wood up her little asshole. -The End-{/size}"
            "\"Epilogue\"" "{size=-2}It's been a year. Ms.Stevens is still working at your school and in regards to the dark haired girl... you have no idea what has become of her.{/size}"
            "\"Epilogue\"" "{size=-2}Both you and Shea are students at the same university...{/size}"
            "\"Epilogue\"" "{size=-2}You've been together since that night in the motel, but you still keep it a secret from everyone. Your only worry these days is Shea's insane appetite for the anal sex. -THE END-{/size}"
            "\"Epilogue\"" "{size=-2}-Ending 05 of 05-{/size}" #HAREM IS ENDING # 5.
            return
        else:
            menu:
                "What would you like to do for the rest of the day?"
                "-Hang around the school building (Page 78)-":
                    if victoria >= 7:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The School gym is full of all sorts of decorations for tonight's prom. Ms.Stevens is the head of the decorating committee, she seems very busy.{/size}" 
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You tell ms.Stevens about your plan to skip the prom. She gets mad, then grabs your crotch and whispers that she will let you cum on her face if you change your mind.{/size}"
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Later that night you show up for the prom. You dance with Ms.Stevens, she then takes you to the janitor's closet and let's you jerk off on her face. You plaster it with cum.{/size}"
                        $ victoria_waifu = True #Completed the book with ms.Stevens.
                        "\"Epilogue\"" "{size=-2}It's been a year... You tried to stay in touch with ms.Stevens, but it seems like the moment you stopped being one of her pupils she lost all of her interest in you.{/size}"
                        "\"Epilogue\"" "{size=-2}But your experience with her motivated you to follow your dream of becoming an adult comics artist. Now you attend a prestigious art-school and are actually quite happy.{/size}"
                        "\"Epilogue\"" "{size=-2}-Ending 03 of 05-{/size}" #Ms.Stevens IS ENDING # 3.
                        return
                    if victoria >= 4:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The School gym is full of all sorts of decorations for tonight's prom. Ms.Stevens is the head of the decorating committee, she seems very busy.{/size}" 
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}She notices you. You tell her about your plan to bail on the prom, but it Doesn't look like she cares.{/size}"
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home and go to bed early.{/size}"
                        call epilogue
                        return
                    if victoria < 4:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}School gym is full of all sorts of declarations for the tonights prom. What of time the whole thing is...{/size}" 
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home and go to sleep early.{/size}"
                        call epilogue
                        return
                "-Stay home (Page 51)-":
                    if shea >= 8: #1
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You decide to stay home and, To your surprise, Shea does the same. Then, out of nowhere she asks you out for the prom.{/size}"
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The prom night goes by in a generic way. You dance with your stepsister and Everybody thinks it's because she took pity on you.{/size}"
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}When the prom is over you and Shea return home. That night you take your little stepsister's virginity. And then she asks you to stick it up her butt as well.{/size}"
                        "\"Epilogue\"" "{size=-2}It's been a year. Both you and Shea are students at the same university, You choose completely different majors, but you are still together and very happy. -THE END-{/size}"
                        $ shea_waifu = True #Completed the book with Shea.
                        "\"Epilogue\"" "{size=-2}-Ending 02 of 05-{/size}" #SHEA IS ENDING # 2.
                        return
                    if shea >= 4:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You decide to stay home and To your surprise Shea does the same. You toy with the idea of asking her out to the prom but then decide against it.{/size}"
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Shea goes to the prom with some other guy, while You just stay home.{/size}"
                        call epilogue
                        return
                    if shea < 4:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You decide to stay home And bail on the prom.{/size}"
                        call epilogue
                        return
                "-Hang around the library (page 97)-":
                    if leena >= 8:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You ignore the prom and head towards the library. It's deserted, so You take your usual seat. You're surprised to see the dark haired girl crouching under your desk.{/size}" 
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Two men in black suits appear just as she puts your dick into her mouth. They take her away and you just stand there stupefied and confused with your pants down. What the heck?{/size}"
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The girl shows up at your doorstep Early on the next morning. She says that she's in the witness protection program, and that her cover has now been compromised because of you...{/size}"
                        $ leena_waifu = True #Completed the book with Leena.
                        "\"Epilogue\"" "{size=-2}It's been two years now. You and the \"library girl\" got married. You live in a beach-house at a secret location with new names.{/size}" 
                        "\"Epilogue\"" "{size=-2}You are very much in love with her and left your past behind for her. she's so grateful that, more often than not, you find your cock deep down her throat. -The End-{/size}"
                        "\"Epilogue\"" "{size=-2}-Ending 04 of 05-{/size}" #LEENA IS ENDING # 4.
                        return
                    if leena >= 4:
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You ignore the prom and head towards the library. It's deserted, so You take your usual seat. A girl appears out of nowhere and sits beside you.{/size}" 
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}She starts talking to you and says her name is Leena, but Suddenly two men in black suits appear. You see fear on her face as They take her away. You wish you could do something...{/size}"
                        call epilogue
                        return
                    if leena < 4: 
                        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You ignore the prom and head towards the library. It's deserted, so You take your usual seat. After a while you return home and go to bed.{/size}"
                        call epilogue
                        return
        
    return       
        

###
label school_ended:
    $ page_01 = renpy.random.randint(1, 30)  
    $ page_02 = renpy.random.randint(31, 60) 
    $ page_03 = renpy.random.randint(61, 100) 
    menu:
        "Chapter [Dear_Wifu_OBJ.progress]" "{size=-2}The school is over for today. How would you like to spend the rest of your day?{/size}"
        "-Hang at the school building (Page [page_03])-":
            if Dear_Wifu_OBJ.progress == 1:
                call home_victoria
            if Dear_Wifu_OBJ.progress == 2:
                call at_school
            if Dear_Wifu_OBJ.progress == 3:
                call at_school
            if Dear_Wifu_OBJ.progress == 4:
                call home_victoria #Date2
            if Dear_Wifu_OBJ.progress == 5:
                call at_school
            if Dear_Wifu_OBJ.progress == 6:
                call home_victoria #Date3
            if Dear_Wifu_OBJ.progress == 7:
                call home_victoria #Date4
            if Dear_Wifu_OBJ.progress == 8:
                call at_school
            if Dear_Wifu_OBJ.progress == 9:
                call at_school
            if Dear_Wifu_OBJ.progress == 10:
                call home_victoria #Date5
            if Dear_Wifu_OBJ.progress == 11:
                call at_school
            if Dear_Wifu_OBJ.progress == 12:
                call at_school
            if Dear_Wifu_OBJ.progress == 13:
                call home_victoria #Date6
            if Dear_Wifu_OBJ.progress == 14:
                call at_school
            if Dear_Wifu_OBJ.progress == 15:
                call home_victoria #Date7
            if Dear_Wifu_OBJ.progress == 16:
                call home_victoria #Date8
            if Dear_Wifu_OBJ.progress == 17:
                call at_school
            if Dear_Wifu_OBJ.progress == 18:
                call home_victoria #Date9
            if Dear_Wifu_OBJ.progress == 19:
                call at_school
            if Dear_Wifu_OBJ.progress == 20:
                call home_victoria #Date10
                
        "-Go home (Page [page_01])-":
            if Dear_Wifu_OBJ.progress == 1:
                call home_shea #1
            if Dear_Wifu_OBJ.progress == 2:
                call home_shea #2
            if Dear_Wifu_OBJ.progress == 3:
                call im_home
            if Dear_Wifu_OBJ.progress == 4:
                call im_home
            if Dear_Wifu_OBJ.progress == 5:
                call im_home
            if Dear_Wifu_OBJ.progress == 6:
                call home_shea #3
            if Dear_Wifu_OBJ.progress == 7:
                call im_home
            if Dear_Wifu_OBJ.progress == 8:
                call im_home
            if Dear_Wifu_OBJ.progress == 9:
                call home_shea #4
            if Dear_Wifu_OBJ.progress == 10:
                call home_shea #5
            if Dear_Wifu_OBJ.progress == 11:
                call im_home
            if Dear_Wifu_OBJ.progress == 12:
                call home_shea #6
            if Dear_Wifu_OBJ.progress == 13:
                call im_home
            if Dear_Wifu_OBJ.progress == 14:
                call home_shea #7
            if Dear_Wifu_OBJ.progress == 15:
                call home_shea #8
            if Dear_Wifu_OBJ.progress == 16:
                call im_home
            if Dear_Wifu_OBJ.progress == 17:
                call home_shea #9
            if Dear_Wifu_OBJ.progress == 18:
                call im_home
            if Dear_Wifu_OBJ.progress == 19:
                call im_home
            if Dear_Wifu_OBJ.progress == 20:
                "ASS"
                call home_shea

        "-Go to the library (page [page_02])-":
            if Dear_Wifu_OBJ.progress == 1:
                call at_library
            if Dear_Wifu_OBJ.progress == 2:
                call at_library
            if Dear_Wifu_OBJ.progress == 3:
                call at_library
            if Dear_Wifu_OBJ.progress == 4:
                call home_leena #1
            if Dear_Wifu_OBJ.progress == 5:
                call at_library
            if Dear_Wifu_OBJ.progress == 6:
                call home_leena #2
            if Dear_Wifu_OBJ.progress == 7:
                call home_leena #3
            if Dear_Wifu_OBJ.progress == 8:
                call home_leena #4
            if Dear_Wifu_OBJ.progress == 9:
                call at_library
            if Dear_Wifu_OBJ.progress == 10:
                call home_leena #5
            if Dear_Wifu_OBJ.progress == 11:
                call at_library
            if Dear_Wifu_OBJ.progress == 12:
                call home_leena #6
            if Dear_Wifu_OBJ.progress == 13:
                call home_leena #7
            if Dear_Wifu_OBJ.progress == 14:
                call at_library
            if Dear_Wifu_OBJ.progress == 15:
                call at_library
            if Dear_Wifu_OBJ.progress == 16:
                call home_leena #8
            if Dear_Wifu_OBJ.progress == 17:
                call at_library
            if Dear_Wifu_OBJ.progress == 18:
                call home_leena #8
            if Dear_Wifu_OBJ.progress == 19:
                call at_library
            if Dear_Wifu_OBJ.progress == 20:
                call home_leena #8
    
    
    
    
    
    return

        
        
### DATES ###
label home_shea:
    if shea == 0: #1
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home and walk in on Shea taking a bath. You stare at her tits until she knocks you out cold with one of her trademark punches.{/size}"
    if shea == 1: #2
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}At home, Shea cooks supper for you. You catch a glimpse of her panties and she knocks you out cold again with one of her trademark punches.{/size}"
    if shea == 2: #3
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home and The house is empty, so You decide to watch an adult movie in the living room. Shea walks in on you... and knocks you out with one of her trademark punches.{/size}"        
    if shea == 3: #4
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}It's a stormy night with rain and thunder. Frightened, Shea crawls into your bed. Your manhood gets hard and Shea knocks you out with one of her trademark punches.{/size}"
    if shea == 4: #5
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}As a peace offering you decide to clean Shea's room. She doesn't appreciate such an invasion of privacy and dishes out another one of her trademark punches, which knocks you out cold.{/size}"
    if shea == 5: #6
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The house is empty. You decide to watch an adult movie in the living room, but Shea walks in on you again. You expect another punch but she just runs off.{/size}"
    if shea == 6: #7
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You come to Shea's room to apologize for the last time. She is wearing her pajamas. You get a little hard during your apology. She accepts your apology blushing.{/size}" 
    if shea == 7: #8
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}It's raining again, so Shea sneaks into your bed at night. She kisses you and asks you to take her anal virginity. You have anal sex with your little step sister.{/size}"
    if shea == 8: #9
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Shea sneaks into your room after supper. While your parents finish eating downstairs, you drill your sister's little asshole with your cock and she takes it ecstatically{/size}"
    $ shea += 1            
    return

### DATES ###
label home_victoria:
    if victoria == 0: #1
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You decide to roam around the school for a while. Ms.Stevens is sitting behind a desk in one of the classrooms, working and you end up secretly watching her.{/size}"
    if victoria == 1: #2
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You find Ms.Stevens working in one of the empty classrooms again. This time She notices you and You have to lie your way out of it. She gives you a big home assignment.{/size}"
    if victoria == 2: #3
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Ms.Stevens finds you roaming around in some deserted school corridors. You haven't completed the assignment she gave you yet. She treats you with contempt for some reason.{/size}"
    if victoria == 3: #4
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You bump into your teacher Ms.Stevens again. Is she stalking your or something? It's the assignment thing again. You start to really dislike the woman.{/size}"
    if victoria == 4: #5
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You try to avoid Ms.Stevens but fail. Your assignment is not completed yet and You grow tired of her droning on about \"how terrible pupils like you fail at life\".{/size}"
    if victoria == 5: #6
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Ms.Stevens lectures you again. While doing so she Accidentally spills her tea on your lap. Afterwards She uses a tissue to rub it off, even though You get aroused by that she pretends not to notice.{/size}" 
    if victoria == 6: #7
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Ms.Stevens lectures you once again. Suddenly she kisses your lips, apologizes and asks you to keep this a secret. You return home very confused.{/size}" 
    if victoria == 7: #8
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You decide to roam the school after your classes again in hopes of running into Ms.Stevens, but you can't find her anywhere...{/size}"  
    if victoria == 8: #9
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Ms.Stevens invites you to her office. She grabs your crotch and fondles your hard cock for a while, but then just sends you on your way. You return home in a daze.{/size}"   
    $ victoria += 1            
    return


### DATES ###
label home_leena:
    if leena == 0: #1
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You go to the school library. Apart from an unfamiliar dark haired girl in the corner you are the only visitor. You spend some time with reading a sci-fi novel.{/size}"
    if leena == 1: #2
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You're at the library. There is that girl with the glasses again. You read your sci-fi book and catch the girl staring at you A couple of timesng. What's her problem?{/size}"
    if leena == 2: #3
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}Seems like the girl is always here. You look at her properly for the first time: long dark hair, glasses, with a well-formed body. She is sort of cute, but this time she catches you staring.{/size}"       
    if leena == 3: #4
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The girl is here, just as always. She looks very shy, so You decide to talk to her, but she just ignores you at first and then simply leaves. She's a weird one.{/size}"    
    if leena == 4: #5
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The silent, dark haired girl is absent today, so You just take your usual seat. But There is a note from her in which She apologizes, then says that she actually likes you and apologizes again.{/size}"
    if leena == 5: #6
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}It's just you again. The girl is not here, there's No note either. You can't remember ever seeing her in school apart from that one time. Who the hell is that silent beauty?{/size}"
    if leena == 6: #7
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You try to read your sci-fi novel, but you just can't concentrate. Suddenly The girl takes a seat next to you. You wait for an explanation but she just pretends to read her book.{/size}"
    if leena == 7: #8
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You pretend to read while you wait for the girl. She takes the seat beside you again and starts rubbing your crotch under the desk. What's the matter with her?!{/size}"
    if leena == 8: #9
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}As soon as you show up the girl drags you behind a bookshelf and begs you to fuck her. You comply, cum inside of her and she returns to her desk, while you just keep on standing there, confused and speechless.{/size}"   
    $ leena += 1            
    return
        
        

### HOME ###
label im_home:
$ random_home = renpy.random.randint(1, 5)      
if random_home == 1:
    "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home. The house is empty. You decide to play some video games till the evening.{/size}"
if random_home == 2:
    "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home. The house is empty. You decide to watch an adult movie in the living room.{/size}"
if random_home == 3:
    "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home. Your father is home early. You decide to go for a jog to avoid his awkward questions about your personal life.{/size}"
if random_home == 4:
    "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home. Your stepmother is home early. You listen to her going on and on about something trivial and wonder why your father decided to marry her.{/size}"
if random_home == 5:
    "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You return home. The house is empty. You decide to use this precious moment of solitude to take a nap.{/size}"
return
    

### SCHOOL ###
label at_school:
    $ random_home = renpy.random.randint(1, 5)      
    if random_home == 1:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You go to the school stadium and relax on the bleachers, while you watch cheerleaders practice in the distance...{/size}"
    if random_home == 2:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You sneak to your secret place: the school building's rooftop and watch heavy clouds creep closer slowly high above, hoping that it's gonna rain tonight.{/size}"
    if random_home == 3:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You roam through the deserted school hallways and run into the janitor. He gives you the stink eye and goes on about his business. You head home.{/size}" 
    if random_home == 4:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You buy a chocolate bar from a vending machine, then sneak into one of the empty classrooms and spend a couple of hours with reading one of your favorite sci-fi novels.{/size}" 
    if random_home == 5:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You roam through the deserted school hallways for a while. It's starting to rain. Your stepsister Shea is terrified of thunder so You hope for a stormy night.{/size}"                               
return 

### LIBRARY ###
label at_library:
    $ random_home = renpy.random.randint(1, 5)      
    if random_home == 1:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You head towards the school library and notice a man in a black suit near the entrance, half expecting him to prevent you from entering, but he ignores you.{/size}"
    if random_home == 2:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You spend the rest of the day at the school library, read your sci-fi book, take a nap, buy candy from the vending machine and then read some more. Life is great!{/size}" 
    if random_home == 3:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You browse through ancient-looking bookshelves, hoping to stumble on a long forgotten book of spells or something, but You just get bored soon and decide to head home.{/size}"
    if random_home == 4:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}The library is deserted, so You hide behind a bookshelf and jerk off while imagining Ms.Stevens giving a lecture in her underwear.{/size}"
    if random_home == 5:
        "\"Chapter [Dear_Wifu_OBJ.progress]\"" "{size=-2}You hear voices and hide behind a bookshelf. From there you see one of the cheerleader girls making out with two of the jocks at once, so You decide to leave before you get in trouble.{/size}"
    return


### EPILOGUE
label epilogue:
    "\"Epilogue\"" "{size=-2}It's been a year. You attend a university abroad and actually enjoy learning for a change, so you seldom think about the past and have high hopes for your future.{/size}"
    "\"Epilogue\"" "{size=-2}-Ending 01 of 04-{/size}"
    return
        
        
### HAREM ###        
        

label chapter_check_waifu: #Checks if the chapter just finished was the last one.
    if Dear_Wifu_OBJ.progress >= 20:
        if fire_in_fireplace:
            show screen done_reading_02  
            hide screen reading_near_fire
        else:
            show screen done_reading  
            hide screen reading

      
        ">That was the last chapter. You finished the entire book."
        if complited_leena_already and complited_shea_already and complited_stevens_already and victoria >= 1 and shea >= 1 and leena >= 1: #Harem ending. The DAHR's ticket.
            m "Wow! What a great book! That was intense!"
            
            #m "No, I mean it! What a great peace of fiction! That Akabur dude must be a genius!"
            if not found_dahrs_ticket_once:
                m "Hm...?"
                m "What is that...? A bookmark?"
                $ the_gift = "01_hp/18_store/06.png" # The DAHR's ticket.
                show screen gift
                with d3
                $ renpy.play('sounds/win2.mp3') #Sound of finding an item.
                ">You found a DAHR's voucher."
                hide screen gift
                with d3
                m "Hm..."
                $ vouchers += 1 #Shows the amount of DAHR's vouchers in your possession.
                $ found_dahrs_ticket_once = True # Turns TRUE after you complete "My Dear Waifu" with the harem ending and "Dahr's voucher" fall out.
                $ waifu_book_completed = True
        elif shea_waifu and shea >= 8: 
            if not complited_shea_already: #Finished with Shea for the first time.
                m "Not bad. I really grew to care about that Shea girl..."
                g9 "Well, her and her anal virginity..."
                $ complited_shea_already = True
            else: #Finished with Shea for the second time.
                m "So I ended up with Shea again, huh?"
                m "Hm... Maybe I should try and make different choices next time...?"
        elif victoria_waifu and victoria >= 7:
            if not complited_stevens_already: #Finished with Ms.Stevens for the first time.
                m "Not bad, not bad. That Ms. Stevens Lady turned out to be one dirty slut..."
                $ complited_stevens_already = True
            else: #Finished with Shea for the second time.
                m "So I ended up with Ms.Stevens again?"
                m "Hm... Maybe I should try and make different choices next time...?"
        elif leena_waifu and leena >= 8:
            if not complited_leena_already: #Finished with Leena for the first time.
                g9 "Sweet! I love happy endings!"
                $ complited_leena_already = True
            else: #Finished with Shea for the second time.
                m "So I ended up with that blond chick again?"
                m "Hm... Maybe I should try and make different choices next time...?"

        else:
            m "Hm... What an anticlimactic ending..."
            #m "Maybe I should read it again sometime."
        
        if not dear_waifu_completed_once:
            $ dear_waifu_completed_once = True # Turns TRUE when complete the book for the first time with any ending. Makes sure you get +1 imagination only once.
            $ renpy.play('sounds/win_04.mp3')   #Not loud.
            hide screen notes
            show screen notes
            ">Your imagination has improved."
            $ imagination +=1
        $ Dear_Wifu_OBJ.progress = 0 #RESTING THE BOOK FOR ANOTHER PLAYTHORUGH.
        $ shea = 0 #RESETING SHEA'S POINTS FOR THE NEXT PLAYTHOURGH.
        $ victoria = 0
        $ leena = 0
        if fire_in_fireplace:
            hide screen reading_near_fire
        else:
            hide screen reading
        
        if daytime:
            jump night_start
        else: 
            jump day_start
    else:
        return