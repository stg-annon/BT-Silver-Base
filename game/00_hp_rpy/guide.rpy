

screen quest_completed:

    zorder 8

    imagemap:
        cache False
        ground "01_hp/18_store/00.png"
        hover "01_hp/18_store/00.png"

screen guide:
    
    tag guide_menu
    zorder 8
    
    imagemap:
        cache False

        if guide_show_hint and not guide_show_next_step:               #Visible hint
            ground "interface/guide/ground_guide_next_step_pixelated.png"
            hover "interface/guide/hover_guide_next_step_pixelated.png"

        elif guide_show_next_step and not guide_show_hint:             #Visible next step
            ground "interface/guide/ground_guide_hint_pixelated.png"
            hover "interface/guide/hover_guide_hint_pixelated.png"

        elif guide_show_next_step and guide_show_hint:                 #Visible both
            ground "interface/guide/ground_guide.png"
            hover "interface/guide/hover_guide.png"        

        else:                                                          #Default #All hidden
            ground "interface/guide/ground_guide_pixelated.png" 
            hover "interface/guide/hover_guide_pixelated.png"

        hotspot (115, 4, 25, 25) clicked Jump("guide_return_point")
        text "Quests" xalign 0.5 ypos 100 size 26

        #Page Arrows
        if guide_page <= 0:
            hotspot (360, 140, 25, 25) clicked [SetVariable("guide_page","0"), Show("guide")]
            hotspot (480, 140, 25, 25) clicked [SetVariable("guide_page","+=1"), Show("guide")]
        if guide_page >= 1:
            hotspot (360, 140, 25, 25) clicked [SetVariable("guide_page","-=1"), Show("guide")]
            hotspot (480, 140, 25, 25) clicked [SetVariable("guide_page","+=1"), Show("guide")]

        #Quest Name
        if guide_page == 0:
            text ""+main_quest.name xalign 0.5 ypos 135 size 16
        else:
            for i in range(0,len(side_quest)):
                text ""+side_quest[i].name xalign 0.5 ypos 135 size 16

        #Quest Objctive
        text "- Objective -" xpos 400 ypos 165 size 12
        if guide_page == 0:
            text ""+main_quest.objective xpos 400 ypos 180 size 10
        else:
            for i in range(0,len(side_quest)):
                text ""+side_quest[i].objective xpos 400 ypos 180 size 10

        #Quest Hint
        text "- Hint -" xpos 400 ypos 210 size 12
        if guide_show_hint:
            if guide_page == 0:
                text ""+main_quest.hint_text xpos 400 ypos 225 size 10
                text ""+main_quest.hint_text2 xpos 400 ypos 235+2 size 10
                text ""+main_quest.hint_text3 xpos 400 ypos 245+4 size 10
                text ""+main_quest.hint_text4 xpos 400 ypos 255+6 size 10
                text ""+main_quest.hint_text5 xpos 400 ypos 265+8 size 10
            else:
                for i in range(0,len(side_quest)):
                    text ""+side_quest[i].hint_text xpos 400 ypos 225 size 10
        else:
            hotspot (395, 225, 280, 70) clicked [SetVariable("guide_show_hint","True"),Show("guide")]

        #Quest Next Step
        text "- Next Step -" xpos 400 ypos 310 size 12
        if guide_show_next_step:
            if guide_page == 0:
                text ""+main_quest.full_text xpos 400 ypos 325 size 10
                text ""+main_quest.full_text2 xpos 400 ypos 335+2 size 10
                text ""+main_quest.full_text3 xpos 400 ypos 345+4 size 10
                text ""+main_quest.full_text4 xpos 400 ypos 355+6 size 10
                text ""+main_quest.full_text5 xpos 400 ypos 365+8 size 10
            else:
                for i in range(0,len(side_quest)):
                    text ""+side_quest[i].full_text xpos 400 ypos 325 size 10
        else:
            hotspot (395, 325, 280, 70) clicked [SetVariable("guide_show_next_step","True"),Show("guide")]

        #Tip/Fact of the Day
        if guide_add_tip:
            text "- Tip of the day -" xpos 400 ypos 410 size 12
        else:
            text "- Fact of the day -" xpos 400 ypos 410 size 12

        text ""+guide_tip_text xpos 400 ypos 425 size 10
        text ""+guide_tip_text2 xpos 400 ypos 435+2 size 10
        text ""+guide_tip_text3 xpos 400 ypos 445+4 size 10
        text ""+guide_tip_text4 xpos 400 ypos 455+6 size 10