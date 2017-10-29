label __init_variables:
    
    #place save variables here
    if not hasattr(renpy.store,'request_jeans'):
        $ request_jeans = False
    if not hasattr(renpy.store,'dribble_equippable'):
        $ dribble_equippable = False
    if not hasattr(renpy.store,'hermione_wetpanties'):
        $ hermione_wetpanties = False        
    if not hasattr(renpy.store,'wetpanties_equippable'):
        $ wetpanties_equippable = False            
    if not hasattr(renpy.store,'request_gryyf_stockings'):
        $ request_gryyf_stockings = False
    if not hasattr(renpy.store,'hermione_dribble'):
        $ hermione_dribble = False
    if not hasattr(renpy.store,'freckles'): #important!
        $ freckles = False
    if not hasattr(renpy.store,'robe'): #important!
        $ robe = 0
    if not hasattr(renpy.store,'addicted'): #important!
        $ addicted = False
    if not hasattr(renpy.store,'lift_shirt'): #important!
        $ lift_shirt = False
    if not hasattr(renpy.store,'book_hold'): #important!
        $ book_hold = False
    if not hasattr(renpy.store,'skirt_up'): #important!
        $ skirt_up = False
    if not hasattr(renpy.store,'fingering'): #important!
        $ fingering = False
    if not hasattr(renpy.store,'panties'): #important!
        $ panties = True
    if not hasattr(renpy.store,'temp_panties'): #important!
        $ temp_panties = True
    if not hasattr(renpy.store,'v_tutoring'): #important!
        $ v_tutoring = 0
    if not hasattr(renpy.store,'current_job'): #important!
        $ current_job = 0
    if not hasattr(renpy.store,'custom_breast'): #important!
        $ custom_breast = 0
    if not hasattr(renpy.store,'custom_bra'): #important!
        $ custom_bra = 0
    if not hasattr(renpy.store,'pitch_open'): #important!
        $ pitch_open = True
    if not hasattr(renpy.store,'maid_working_unlocked'): #important!
        $ maid_working_unlocked = True
    if not hasattr(renpy.store,'hg_pth'): #important!
        $ hg_pth = "01_hp/13_hermione_main/"
    if not hasattr(renpy.store,'inn_first'): #important!
        $ inn_first = True
    if not hasattr(renpy.store,'stockings'): #important!
        $ stockings = 0
    if not hasattr(renpy.store,'attic_open'): #important!
        $ attic_open = False
    if not hasattr(renpy.store,'custom_outfit_old'): #important!
        $ custom_outfit_old = 0
    if not hasattr(renpy.store,'show_attic'): #important!
        $ show_attic = True
    if not hasattr(renpy.store,'show_clothes_store'): #important!
        $ show_clothes_store = True
    if not hasattr(renpy.store,'show_forest'): #important!
        $ show_forest = True
    if not hasattr(renpy.store,'show_inn'): #important!
        $ show_inn = True
    if not hasattr(renpy.store,'show_pitch'): #important!
        $ show_pitch = True
    if not hasattr(renpy.store,'tentacle_cosmetic'): #important!
        $ tentacle_cosmetic = False
    if not hasattr(renpy.store,'maid'): #important!
        $ maid = True
    if not hasattr(renpy.store,'cheerleader'): #important!
        $ cheerleader = True
    if not hasattr(renpy.store,'custom_skirt'): #important!
        $ custom_skirt = 0
    if not hasattr(renpy.store,'custom_shirt'): #important!
        $ custom_shirt = 0
    if not hasattr(renpy.store,'transparency'): #important!
        $ transparency = 1
    if not hasattr(renpy.store,'genie_name'): #important!
        $ genie_name = "Sir"
    if not hasattr(renpy.store,'hermione_name'): #important!
        $ hermione_name = "Girl"
    if not hasattr(renpy.store,'tent_scroll'): #important!
        $ tent_scroll = False
    if not hasattr(renpy.store,'shaming'): #important!
        $ shaming = 0
    if not hasattr(renpy.store,'shaming_busy'): #important!
        $ shaming_busy = False
    if not hasattr(renpy.store,'shaming_01'): #important!
        $ shaming_01 = False
    if not hasattr(renpy.store,'shaming_02'): #important!
        $ shaming_02 = False
    if not hasattr(renpy.store,'shaming_03'): #important!
        $ shaming_03 = False
    if not hasattr(renpy.store,'heretic'): #important!
        $ heretic = 0
    if not hasattr(renpy.store,'heretic_01'): #important!
        $ heretic_01 = False
    if not hasattr(renpy.store,'heretic_02'): #important!
        $ heretic_02 = False
    if not hasattr(renpy.store,'heretic_03'): #important!
        $ heretic_03 = False
    if not hasattr(renpy.store,'heretic_busy'): #important!
        $ heretic_busy = False
    if not hasattr(renpy.store,'hermione_desperate_done'): #important!
        $ hermione_desperate_done = False
    if not hasattr(renpy.store,'glasses_worn'): #important!
        $ glasses_worn = False
    if not hasattr(renpy.store,'legs_03'): #important!
        $ legs_03 = False
    if not hasattr(renpy.store,'hair_color'): #important!
        $ hair_color = 0
    if not hasattr(renpy.store,'ears'): #important!
        $ ears = False
    if not hasattr(renpy.store,'wear_bra'): #important!
        $ wear_bra = False
    if not hasattr(renpy.store,'scene_number'): #important!
        $ scene_number = 1
    if not hasattr(renpy.store,'shirt_random'): #important!
        $ shirt_random = 1
    if not hasattr(renpy.store,'badges'): #important!
        $ badges = True
    if not hasattr(renpy.store,'collar'): #important!
        $ collar = 0
    if not hasattr(renpy.store,'cust_char_1_enabled'): #important!
        $ cust_char_1_enabled = False
    if not hasattr(renpy.store,'cust_char_2_enabled'): #important!
        $ cust_char_2_enabled = False
    if not hasattr(renpy.store,'cust_char_3_enabled'): #important!
        $ cust_char_3_enabled = False
    if not hasattr(renpy.store,'fawkes_intro_done'): #important!
        $ fawkes_intro_done = True
    if not hasattr(renpy.store,'temp_stockings'): #important!
        $ temp_stockings = stockings
    if not hasattr(renpy.store,'temp_outfit'): #important!
        $ temp_outfit = custom_outfit_old

    ###Define Luna variables
    if not hasattr(renpy.store,'luna_chibi_zorder') or not hasattr(renpy.store,'luna_corruption'): #important!
        $ hat_known = False
        call luna_init

    if not hasattr(renpy.store,'luna_tears'): #important!
        $ luna_tears = 0

    if not hasattr(renpy.store,'luna_wear_cum'): #important!
        $ luna_wear_cum = False
        $ luna_cum = 1
    
    
    if not hasattr(renpy.store,'new_request_01_heart'): #important!
        $ new_request_01_heart = 0
    if not hasattr(renpy.store,'new_request_02_heart'): #important!
        $ new_request_02_heart = 0
    if not hasattr(renpy.store,'new_request_03_heart'): #important!
        $ new_request_03_heart = 0
    if not hasattr(renpy.store,'new_request_04_heart'): #important!
        $ new_request_04_heart = 0
    if not hasattr(renpy.store,'new_request_05_heart'): #important!
        $ new_request_05_heart = 0
    if not hasattr(renpy.store,'new_request_08_heart'): #important!
        $ new_request_08_heart = 0
    if not hasattr(renpy.store,'new_request_11_heart'): #important!
        $ new_request_11_heart = 0
    if not hasattr(renpy.store,'new_request_12_heart'): #important!
        $ new_request_12_heart = 0
    if not hasattr(renpy.store,'new_request_16_heart'): #important!
        $ new_request_16_heart = 0
    if not hasattr(renpy.store,'new_request_22_heart'): #important!
        $ new_request_22_heart = 0
    if not hasattr(renpy.store,'new_request_29_heart'): #important!
        $ new_request_29_heart = 0
    if not hasattr(renpy.store,'new_request_31_heart'): #important!
        $ new_request_31_heart = 0
    
    if not hasattr(renpy.store,'pub_q_sex_teach'): #important!
        $ pub_q_sex_teach = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_Flag'): #important!
        $ hg_pf_TheGamble_Flag = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagA'): #important!
        $ hg_pf_TheGamble_FlagA = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagB'): #important!
        $ hg_pf_TheGamble_FlagB = False
    if not hasattr(renpy.store,'hg_pf_TheGamble_FlagC'): #important!
        $ hg_pf_TheGamble_FlagC = False
    

    if not hasattr(renpy.store,'hair_style'): #important!
        $ hair_style = "A"
    if not hasattr(renpy.store,'skip_duel'): #important!
        $ skip_duel = False
    if not hasattr(renpy.store,'next_day'): #important!
        $ next_day = False
    if not hasattr(renpy.store,'gift_order'): #important!
        $ gift_order = None
    if not hasattr(renpy.store,'order_quantity'): #important!
        $ order_quantity = 0
    if not hasattr(renpy.store,'force_unlock_pub_favors'): #important!
        $ force_unlock_pub_favors = False
    if not hasattr(renpy.store,'leg_pos'): #important!
        $ leg_pos = 0
    if not hasattr(renpy.store,'right_arm_pos'): #important!
        $ right_arm_pos = 0
    if not hasattr(renpy.store,'left_arm_pos'): #important!
        $ left_arm_pos = 0
    if not hasattr(renpy.store,'her_breasts'): #important!
        $ her_breasts = 0
    if not hasattr(renpy.store,'wear_shirts'): #important!
        $ wear_shirts = True
    if not hasattr(renpy.store,'wear_skirts'): #important!
        $ wear_skirts = True

    if not hasattr(renpy.store,'tentacle_owned'): #important!
        $ tentacle_owned = False
    if not hasattr(renpy.store,'tent_scroll'): #important!
        $ tent_scroll = False

    if not hasattr(renpy.store,'hermione_ass_cum'): #important!
        $ hermione_ass_cum = False

    ### Accesory Variables
    if not hasattr(renpy.store,'hermione_wear_glasses'): #important!
        $ hermione_wear_glasses = False
    if not hasattr(renpy.store,'hermione_glasses'): #important!
        $ hermione_glasses = "01_hp/13_characters/hermione/accessories/head/reading_glasses.png"
    if not hasattr(renpy.store,'hermione_hats'): #important!
        $ hermione_hats = False
    if not hasattr(renpy.store,'hermione_hat'): #important!
        $ hermione_hat = "01_hp/13_characters/hermione/accessories/head/tiara.png"
    if not hasattr(renpy.store,'hermione_freckles'): #important!
        $ hermione_freckles = False
    if not hasattr(renpy.store,'hermione_cum'): #important!
        $ hermione_cum = False

    ##Shaming favour
    if not hasattr(renpy.store,'buttplug_2_worn'): #important!
        $ buttplug_2_worn = False
    if not hasattr(renpy.store,'hermione_buttplugs'): #important!
        $ hermione_buttplugs = False
    if not hasattr(renpy.store,'hermione_buttplug'): #important!
        $ hermione_buttplug = "01_hp/13_characters/hermione/accessories/plugs/plug_a_on.png"
    if not hasattr(renpy.store,'buttplug_magic_known'): #important!
        $ buttplug_magic_known = False
    if not hasattr(renpy.store,'buttplug_2_question'): #important!
        $ buttplug_2_question = False

    ###Tutoring fix
    if not hasattr(renpy.store,'table_position_x'): #important!
        $ table_position_x = 20

    ###MISC
    if not hasattr(renpy.store,'hermione_action_under'): #important!
        $ hermione_action_under = False

    if not hasattr(renpy.store,'hermione_squirt'): #important!
        $ hermione_squirt = False

    #SC34 update 2 stuff, thanks akabur.
    if not hasattr(renpy.store,'sc_cg_base'): #important!
        $ sc_cg_base = "01_hp/28_cg/sc34/1/base_1.png"
        $ sc_cg_image_1 = "01_hp/28_cg/sc34/1/A_1.png"
        $ sc_cg_image_2 = "01_hp/28_cg/sc34/2/B_1.png"
        $ sc_cg_image_3 = "01_hp/28_cg/sc34/2/C_1.png"
        $ sccgxpos = 200
        $ sccgypos = 50
    
    
    
    
    $ override_persistant = False
    
    
    ### Personal Favor ID's ###
    $ hg_pf_TalkToMe_ID = 0        #00 Genie touches himself.
    $ hg_pf_NicePanties_ID = 1     #01 "Lift your skirt".
    $ hg_pf_BreastMolester_ID = 2  #02 "Molest tits."
    $ hg_pf_ButtMolester_ID = 3    #03 "Molest butt."
    $ hg_pf_ShowThemToMe_ID = 4    #04 "Show me your tits."
    $ hg_pf_DanceForMe_ID = 5      #05 "Get naked."
    $ hg_pf_LetMeTouchThem_ID = 6  #06 "Let me play with your tits."
    $ hg_pf_TouchMe_ID = 7         #07 (Handjob).
    $ hg_pf_SuckIt_ID = 8          #08 (Blowjob).
    $ hg_pf_LetsHaveSex_ID = 9     #09 (Sex).
    $ hg_pf_TimeForAnal_ID = 10    #10 (Anal sex)
    $ hg_pf_TheGamble_ID = 11      #11 (Gamble with hg)

    #Personal Favor Points
    if override_persistant or not hasattr(renpy.store,'hg_pf_points'): #important!
        $ hg_pf_points = [0] * 12
    if override_persistant or not hasattr(renpy.store,'hg_pf_hearts'): #important!
        $ hg_pf_hearts = [0] * 12
    if override_persistant or not hasattr(renpy.store,'hg_pf_complete'): #important!
        $ hg_pf_complete = [False] * 12
        
        
    ### Public Request ID's ###
    $ hg_pr_FlirtClassmate_ID = 0 #00 "Flirt with 3 classmates".
    $ hg_pr_FlirtTeacher_ID = 1 #01 "Flirt with a teacher".
    $ hg_pr_ClassmateTouchYou_ID = 2 #02 "Let a classmate molest you."
    $ hg_pr_FlashClassmate_ID = 3 #03 "Flash a classmate."
    $ hg_pr_KissAGirl_ID = 4 #04 "Kiss female classmate."
    $ hg_pr_HandjobClassmate_ID = 5 #05 (Give handjob to a classmate)
    $ hg_pr_BlowjobClassmate_ID = 6 #06 (Blow a classamate).
    $ hg_pr_BlowjobTeacher_ID = 7 #07 (Blow a teacher)
    $ hg_pr_SexWithClassmate_ID = 8 #08 (sex with classamate).
    $ hg_pr_SexWithTeacher_ID = 9 #09 (sex with teacher)
    
    #Public Request Points
    if override_persistant or not hasattr(renpy.store,'hg_pr_points'): #important!
        $ hg_pr_points = [0] * 11
    if override_persistant or not hasattr(renpy.store,'hg_pr_complete'): #important!
        $ hg_pr_complete = [False] * 11
    if override_persistant or not hasattr(renpy.store,'hg_pr_InProgress'): #important!
        $ hg_pr_InProgress = [False] * 11
    
    #Public Request Vars.
    if override_persistant or not hasattr(renpy.store,'hg_pr_SexWithClassmate_AltFlag'): #important!
        $ hg_pr_SexWithClassmate_AltFlag = False
    
    #Public Shaming Flags
    if override_persistant or not hasattr(renpy.store,'hg_ps_PantyThief_SoakedPantiesFlag'): #important!
        $ hg_ps_PantyThief_SoakedPantiesFlag = False

    #HAT stuff
    if not hasattr(renpy.store,'hat_known'):
        $ hat_known = False

    if not hasattr(renpy.store,'cat_ears'):
        $ cat_ears = False
        $ transparent_quest = False
    
    if not hasattr(renpy.store,'elf_ears'):
        $ elf_ears = False
    
    
    
    
    
    $ wardrobe_hair_style = "A"
    $ wardrobe_hair_color = 1
    $ wardrobe_gift_item = 0
    $ wardrobe_costume_selection = 0
    $ wardrobe_uniform_selection = ""
    
    
    $ her_path = "01_hp/13_hermione_main/"
    
    
    $ emote_anger = False
    $ emote_exclam = False
    $ emote_hearts = False
    $ emote_question = False
    $ emote_sweat = False
    $ emote_suprize = False
    $ anger = ["body_51","body_76","body_86","body_110","body_218","body_351","body_346","body_345","body_343","body_317","body_309"]
    $ exclam = []
    $ hearts = []
    $ question = []
    $ sweat = ["body_24","body_34","body_57","body_108","body_208","body_340"]
    $ suprize = ["body_80","body_80b","body_335"]
    
    $ h_body = "body_01"
    $ h_xpos = 370
    $ h_ypos = 0
    $ her_head_xpos = 390
    $ her_head_ypos = 235
    $ her_head_only = 300 #(340,300,290)
    $ her_head_tits = 235
    $ her_chibi_dance_xpos = 210
    $ her_chibi_dance_ypos = 180
    
    $ hermione_chibi_zorder = 3
    
    $ s_head_xpos = 330
    $ s_head_ypos = 380
    $ snape_chibi_xpos=610
    $ snape_chibi_ypos=210
    $ snape_speed = 2.0
    
    $ luna_chibi_xpos = 500
    $ luna_chibi_ypos = 250
    $ luna_speed = 2.0
    
    
    $ row_index_selected = 0
    $ column_index_selected = 0
    
    return
