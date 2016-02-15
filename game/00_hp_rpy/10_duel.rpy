label duel:
    
    ### DUEL ###
    $ d_flag_01 = False #Turns True after conversation triggered when Genie's HP runs low.
    $ d_flag_02 = False #Turns True after conversation triggered when Snape's HP runs low.
    
    $ genie_hp = 100000
    $ snape_hp = 20 #Must be 2000
    


    $ blocking = False #True when "block" command is chosen, when Gennie turn into a guard.
    $ snape_blocking = False #True when Snape goes into defensive stance.
    $ pentogram = False #True when pentagram been casted an is displayed on the floor.
    
    
    
    # Hide all the screens.
    $ phoenix_is_feed = False #At the beginning of every new day Phoenix is not fed.

    stop bg_sounds #Stops playing the fire SFX.
    stop weather #Stops playing the rain SFX.

    hide screen notes #A bunch of notes poping out with a "win" sound effect.
    hide screen phoenix_food
    hide screen done_reading
    hide screen done_reading_02
    hide screen candlefire_01 #CANDLE FIRE.
    hide screen candlefire_02 #CANDLE FIRE.
    hide screen lightening #Hide lighting so it woudn't get stuck during clear sky weather and such.
    hide screen cloud_night_01 #NIGHT CLOUDS.
    hide screen cloud_night_02 #NIGHT CLOUDS.
    hide screen cloud_night_03 #NIGHT CLOUDS.
  
    hide screen room_night #Hiding NIGHT BG from last night.
    #show screen room #Showing main room BG. 

    hide screen door   
    hide screen cupboard
    hide screen chair
    hide screen fireplace
    hide screen phoenix
    hide screen candle_01    
    hide screen candle_02
    hide screen genie
    hide screen owl
    hide screen owl_02
    hide screen points
    hide screen ctc
    

    show image "01_hp/01_bg/01_main_room_02.png"
    show image "01_hp/05_props/01_door.png" at Position(xpos=758, ypos=315, xanchor="center", yanchor="center")
    show image "01_hp/05_props/02_cupboard_00.png" at Position(xpos=120, ypos=280, xanchor="center", yanchor="center")
    show image "01_hp/05_props/04_chair.png" at Position(xpos=653, ypos=300, xanchor="center", yanchor="center")
    show image "01_hp/05_props/03_fireplace.png" at Position(xpos=553, ypos=277, xanchor="center", yanchor="center")
    #show image "01_hp/05_props/05_window.png" at Position(xpos=290, ypos=218, xanchor="center", yanchor="center")
    show image "01_hp/05_props/06_phoenix.png" at Position(xpos=400, ypos=225, xanchor="center", yanchor="center")
    show image "01_hp/05_props/07_candle.png" at Position(xpos=693, ypos=225, xanchor="center", yanchor="center")
    show image "01_hp/05_props/08_candle.png" at Position(xpos=210, ypos=160, xanchor="center", yanchor="center")
    #show image "01_hp/05_props/11_genie_00.png" at Position(xpos=230, ypos=336, xanchor="center", yanchor="center")
    show image "01_hp/05_props/09_table.png" at Position(xpos=220, ypos=330, xanchor="center", yanchor="center")
    show screen candlefire_01 #CANDLE FIRE.
    show screen candlefire_02 #CANDLE FIRE.
    
    hide screen snape_defends
    hide screen blkfade
    
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 

    hide screen end_u_1
    with fade
    
    
    m "This is foolish... You are no match for me..."
    sna_[1] "Amusing..."
    m "{size=-4}(Actually my human body is quite weak...){/size}"
    m "{size=-4}(But I should still be way more powerful than any human wizard...){/size}"
    sna_[1] "Let the duel begin!"
    hide screen bld1
    show screen hp_bar
    with d5

    
    





label duel_main:
    if genie_hp <= 30000 and not d_flag_01:
        $ d_flag_01 = True
        sna_[1] "Ready to give up yet?"
        g4 "Tsk..."
        
    if snape_hp <= 400 and not d_flag_02:
        $ d_flag_02 = True
        g4 "{size=-4}(He is getting weaker, I can feel it!){/size}"
        sna_[1] "*Panting*"
    
    call screen duel_buttons
   
    

    
    menu:
        "-Attack-":
            $ blocking = False #To stop the game treating Genie as being in a block stance.
            if snape_blocking:
                $ snape_blocking = False
                pause 1
                jump snape_defends
            else:
                jump genie_attack
        "-Defend-":
            $ blocking = True #Genie is guard.
            show ch_gen guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
            pause 1
            jump snapes_turn
        "-Potion (x[potions])-":
            if potions >= 1:
                jump potion
            else:
                m "Crap! I'm out of healing potions!"
                jump duel_main
    
    
### SNAPE'S TURN ###
label snapes_turn:
    if pentogram:
        $ pentogram = False
        hide ch_sna
        hide pentogram
        show hand at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
        $ renpy.play('sounds/attack_snape3.ogg')
        pause 1.5
        hide hand
        hide ch_gen
        $ renpy.play('sounds/attack_snape4.ogg')
        if blocking: # GENIE BLOCKS AGAINST THE HAND.(Genie -50 HP)
            $ blocking = False
            show hand_guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1.8
            hide hand_guard
            show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
            hide screen minus_50_genie
            show screen minus_50_genie
            $ genie_hp -= 50
            if genie_hp < 50: #Check for gameover
                jump genie_lost
            
            show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
            show ch_gen duel_01 behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            jump duel_main
            
        
        else: # GENIE DOESN'T BLOCK AGAINST THE HAND. (Genie -400 HP)
            show hand_genie at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1.3
            hide hand_genie
            show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
            hide screen minus_400_genie
            show screen minus_400_genie
            $ genie_hp -= 400
            if genie_hp < 50: #Check for gameover
                jump genie_lost
            show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            jump duel_main
    
    
    else:
        $ snape_blocking = False
        #$ snape_decides = 3
        $ snape_decides = renpy.random.randint(1, 3)

        if snape_decides == 1: #ATTACK 
            if blocking:
                $ blocking = False
                jump snape_attack_guard
            else:
                jump snape_attack
        elif snape_decides == 2: #BLOCK 
            $ snape_blocking = True
            show ch_sna defend at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1
            jump duel_main

        elif snape_decides == 3:  #MAGIC. CASTS THE PICTOGRAM. 
            $ pentogram = True
            hide ch_sna 
            show image "01_hp/04_duel/snape_casting_01.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            $ renpy.play('sounds/attack_snape2.ogg')
            pause.8
            show pentogram at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
            pause 1
            hide image "01_hp/04_duel/snape_casting_01.png" #Snape point to the ground with his wand.
            show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
            
            jump duel_main



### SNAPE ATTACK ### (Genie -100 HP)
label snape_attack:
    hide ch_sna
    hide ch_gen
    show snape_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with Dissolve(.1)
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.45
    hide snape_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    $ genie_hp -= 100
    if genie_hp < 50: #Check for gameover
        jump genie_lost
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with Dissolve(.1)
    jump duel_main
    

### SNAPE ATTACKS GUARD ### (-0 HP)
label snape_attack_guard: 
    hide ch_sna 
    hide ch_gen 
    show snape_attack_guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with Dissolve(.1)
    $ renpy.play('sounds/attack_snape.ogg')
    pause 0.5
    hide screen minus_0_genie
    show screen minus_0_genie
    hide snape_attack_guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show ch_gen guard at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1
    
    #show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with Dissolve(.1)

    jump duel_main
    
    
### SNAPE DEFENDS ### (Snape -0 HP)

label snape_defends:   
    hide ch_sna
    hide ch_gen
    $ renpy.play('sounds/magic4.ogg')
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show snape_defend behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with Dissolve(.1)
    pause 2.3
    hide screen minus_0
    show screen minus_0
    hide snape_defend at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show ch_gen barb at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    pause 1
    
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    pause 1
    jump snapes_turn


### GENIE ATTACK ### (Snape -100 HP)
label genie_attack:   
    hide ch_sna
    hide ch_gen
    
    $ renpy.play('sounds/magic4.ogg')
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show genie_attack behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with Dissolve(.1)
    
    pause 1
    $ renpy.play('sounds/attack_axe.mp3')
    
    pause 1.8
    
    
    
    if pentogram:
        hide screen minus_300
        show screen minus_300
        $ snape_hp -= 300
    else:
        hide screen minus_100
        show screen minus_100
        $ snape_hp -= 100
    pause 1
    if snape_hp < 50: #Check for gameover
        jump snape_lost
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    hide genie_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_sna duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show ch_gen barb at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    pause 1
    jump snapes_turn
   
   
   
### GENIE DRINKS POTION ### (+300 HP)
label potion:
    pause.5
    hide heal_02
    show heal_02 at Position(xpos=360, ypos=330, xanchor="center", yanchor="center")
    $ renpy.play('sounds/attack_heal.ogg')
    pause 1 
    
    
    
    hide screen plus_300
    show screen plus_300
    pause 1
    $ potions -=1
    $ genie_hp += 300
    if genie_hp >= 1000:
        $ genie_hp = 1000
    pause.5

    jump snapes_turn
    


### SUBSTITUTE LABELS FOR NEW COOL BUTTONS ###


label main_attack:
    $ blocking = False #To stop the game treating Genie as being in a block stance.
    if snape_blocking:
        $ snape_blocking = False
        pause 1
        jump snape_defends
    else:
        jump genie_attack

label main_block:
    $ blocking = True #Genie is guard.
    $ renpy.play('sounds/magic4.ogg')
    show smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    show ch_gen guard behind smoke at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    pause 1
    jump snapes_turn
    
label main_potion:
    if potions >= 1:
        jump potion
    else:
        m "Crap! I'm out of healing potions!"
        jump duel_main
        
        
        

    
    
    
    
init -1:

   ### DUEL ###

    screen hp_bar:
        if genie_hp <= 100000:
            add "01_hp/04_duel/hp_bar_02.png" 
        if genie_hp <= 95000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -15 ypos 0
        if genie_hp <= 90000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -30 ypos 0
        if genie_hp <= 85000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -45 ypos 0
        if genie_hp <= 80000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -60 ypos 0
        if genie_hp <= 75000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -75 ypos 0
        if genie_hp <= 70000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -90 ypos 0
        if genie_hp <= 65000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -105 ypos 0
        if genie_hp <= 60000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -120 ypos 0
        if genie_hp <= 55000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -135 ypos 0
        if genie_hp <= 50000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -150 ypos 0
        if genie_hp <= 45000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -165 ypos 0
        if genie_hp <= 40000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -180 ypos 0
        if genie_hp <= 35000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -195 ypos 0
        if genie_hp <= 30000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -210 ypos 0
        if genie_hp <= 25000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -225 ypos 0
        if genie_hp <= 20000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -240 ypos 0
        if genie_hp <= 15000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -255 ypos 0
        if genie_hp <= 10000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -270 ypos 0
        if genie_hp <= 5000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -285 ypos 0
        if genie_hp < 5000:
            add "01_hp/04_duel/hp_bar_02.png" xpos -300 ypos 0
        add "01_hp/04_duel/hp_bar.png" #Genie avatr pic.
        add "01_hp/04_duel/hp_bar_05.png" #Inactive buttons.
        
        add "01_hp/04_duel/hp_bar_11.png" #Black background for HP bar.
        if snape_hp == 2000:
            add "01_hp/04_duel/hp_bar_12.png" 
        if snape_hp == 1900:
            add "01_hp/04_duel/hp_bar_12.png" xpos 35 ypos 0 
        if snape_hp == 1800:
            add "01_hp/04_duel/hp_bar_12.png" xpos 70 ypos 0 
        if snape_hp == 1700:
            add "01_hp/04_duel/hp_bar_12.png" xpos 105 ypos 0 
        if snape_hp == 1600:
            add "01_hp/04_duel/hp_bar_12.png" xpos 140 ypos 0 
        if snape_hp == 1500:
            add "01_hp/04_duel/hp_bar_12.png" xpos 175 ypos 0 
        if snape_hp == 1400:
            add "01_hp/04_duel/hp_bar_12.png" xpos 205 ypos 0 
        if snape_hp == 1300:
            add "01_hp/04_duel/hp_bar_12.png" xpos 240 ypos 0
        if snape_hp == 1200:
            add "01_hp/04_duel/hp_bar_12.png" xpos 275 ypos 0 
        if snape_hp == 1100:
            add "01_hp/04_duel/hp_bar_12.png" xpos 305 ypos 0 
        if snape_hp == 1000:
            add "01_hp/04_duel/hp_bar_12.png" xpos 340 ypos 0 #MIDDLE
        if snape_hp == 900:
            add "01_hp/04_duel/hp_bar_12.png" xpos 375 ypos 0
        if snape_hp == 800:
            add "01_hp/04_duel/hp_bar_12.png" xpos 405 ypos 0
        if snape_hp == 700:
            add "01_hp/04_duel/hp_bar_12.png" xpos 440 ypos 0
        if snape_hp == 600:
            add "01_hp/04_duel/hp_bar_12.png" xpos 475 ypos 0
        if snape_hp == 500:
            add "01_hp/04_duel/hp_bar_12.png" xpos 505 ypos 0
        if snape_hp == 400:
            add "01_hp/04_duel/hp_bar_12.png" xpos 545 ypos 0
        if snape_hp == 300:
            add "01_hp/04_duel/hp_bar_12.png" xpos 585 ypos 0
        if snape_hp == 200:
            add "01_hp/04_duel/hp_bar_12.png" xpos 630 ypos 0
        if snape_hp == 100:
            add "01_hp/04_duel/hp_bar_12.png" xpos 670 ypos 0
        if snape_hp < 100:
            add "01_hp/04_duel/hp_bar_12.png" xpos 700 ypos 0
            
        
        
        add "01_hp/04_duel/hp_bar_10.png" #Snape avatr pic.
        
#        hbox: #горизонтальный «контейнер», где будет изображение золота и его количество
#                spacing 10 xpos 330 ypos 500#отступ для текста, если надо прямо в левом углу — убираем его        
#                text "{size=-3}genie_hp: [genie_hp]\nsnape_hp: [snape_hp]{/size}" #сумма текстом
        
    screen duel_buttons:
        imagebutton: # attack
            focus_mask True
            idle "01_hp/04_duel/hp_bar_03.png"
            hover "01_hp/04_duel/hp_bar_04.png"
            action [Jump("main_attack")]
        imagebutton: # aguard
            focus_mask True
            idle "01_hp/04_duel/hp_bar_07.png"
            hover "01_hp/04_duel/hp_bar_06.png"
            action [Jump("main_block")]
        imagebutton: # item
            focus_mask True
            idle "01_hp/04_duel/hp_bar_09.png"
            hover "01_hp/04_duel/hp_bar_08.png"
            action [Jump("main_potion")]


    
### SNAPE LOSES ###
label snape_lost:
    hide genie_attack at Position(xpos=550, ypos=250, xanchor="center", yanchor="center")
    hide pentogram
    show ch_gen duel_01 at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 

    show image "01_hp/04_duel/snape.png" at Position(xpos=550, ypos=250, xanchor="center", yanchor="center") 
    with flashbulb


    pause 1
    jump event_06
    
    
### GENIE LOSES ###
label genie_lost:
    play music "music/Final Fantasy 7 Game Over Theme.mp3" fadein 1 fadeout 1 
    
    show screen end_u_1
    $ end_u_1_pic =  "01_hp/20_intro/game_over.jpg"
    with flashbulb
    with hpunch
    show screen ctc
    pause
    hide screen ctc
    menu:
        "-Try again-":
            stop music 
            $ renpy.play('sounds/glass_break.mp3') #Sound of a door opening.
            play music "music/Final Fantasy VII Boss Theme.mp3" fadein 1 fadeout 1
            hide screen end_u_1
            if rum_times == 2:
                $ potions = 1
            elif rum_times == 3:
                $ potions = 2
            else:
                pass
            jump duel
            
        "-Give up-":
            pass

    
    