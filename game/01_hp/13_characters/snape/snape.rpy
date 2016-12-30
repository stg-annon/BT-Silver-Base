init python:
    class snape_character(silver_character):
        root = "01_hp/13_characters/snape/"
        
        xpos = 550
        ypos = 0
        
        name = "Severus Snape"
        pet_name = "Snape"
        genie_name = "Albus"
        
        screen = "snape_main_obj_scr"
        screen_head = "snape_head_obj_scr"
        
        body = "snape_01"
        head = "head_1"
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        # alternate way of displaying snapes head
        def say_H(self, string, image=None):
            if image != None:
                self.head = image
            char = Character(self.name, color="#402313", window_right_padding=270, show_side_image=Image("{}head/{}.png".format(self.root,self.head), xalign=1.0, yalign=0.0), show_who_xalign=0.5, show_two_window=True, ctc="ctc3", ctc_position="fixed")
            renpy.say(char,string)
        
        def getLayers(self):
            layers = []
            if self.body not in ["",None]:
                layers.append(self.root+"main/"+self.body+".png")
            return layers
            
    class snape_character_chibi(silver_character_chibi):
        def walk(self, x, x2, speed, y=210):
            if x > x2: #right to left
                chibiWalk(self.walk_img, x, x2, speed, y)
            else: #left to right
                chibiWalk(self.walk_img_f, x, x2, speed, y)
            self.xpos = x2
            
    
    def sna_main(text="",face=""):
        global s_sprite
        if face != "":
            renpy.hide_screen("snape_main")
            s_sprite = "01_hp/13_characters/snape/main/"+str(face)+".png"
            renpy.show_screen("snape_main")
        if text != "":
            renpy.say(sna,text)
        
    def sna_head(text="",face=""):
        global s_sprite
        if face != "":
            s_sprite = "01_hp/13_characters/snape/main/"+str(face)+".png"
        renpy.show_screen("s_head")
        if text != "":
            renpy.say(sna2,text)
        renpy.hide_screen("s_head")
    
    def sna_walk(x, x2, speed=3, y=210):
        global snape_chibi_xpos
        if x > x2: #right to left
            chibiWalk("snape_walk_01", x, x2, speed, y)
        else: #left to right
            chibiWalk("snape_walk_01_f", x, x2, speed, y)
        snape_chibi_xpos = x2
    
    
label __init_variables:
    $ reset_char_obj = True
    if not hasattr(renpy.store,'snape_SC') or reset_char_obj: #important!
        $ snape_SC = snape_character(
            chibi = snape_character_chibi(
                xpos = 750,
                ypos = 210,
                walk_img = "snape_walk_01",
                walk_img_f = "snape_walk_01_f",
                stand_img = "01_hp/13_characters/snape/chibis/snape_00.png"
            )
        )
        $ snape_SC.char_ref = Character('snape_SC.name', dynamic=True, color="#402313", window_right_padding=250, window_left_padding=85, show_two_window=True, ctc="ctc3", ctc_position="fixed")
        $ snape_SC.h_char_ref = Character('snape_SC.name', dynamic=True, color="#402313", window_right_padding=220, show_two_window=True, ctc="ctc3", ctc_position="fixed")
    
    return
    
    
label snape_init:
    $ snape_xpos = 550
    $ snape_ypos = 0
    $ snape_head_xpos = 610
    $ snape_head_ypos = 380
    $ snape_speed = 3
    return
    
    
### NEW SNAPE SCREENS ###
screen snape_main_obj_scr:
    tag snape_sprite
    for layer in snape_SC.getLayers():
        if snape_SC.flip:
            add im.Flip(layer, horizontal=True) xpos snape_SC.xpos ypos snape_SC.ypos
        else:
            add layer xpos snape_SC.xpos ypos snape_SC.ypos
    zorder 4
    
screen snape_head_obj_scr:
    tag silver_head
    for layer in snape_SC.getLayers():
        add layer xpos 610 ypos 380
    zorder 8

screen snape_chibi_standing:
    tag snape_chibi
    add snape_SC.chibi.stand_img at Position(xpos=snape_SC.chibi.xpos, ypos=snape_SC.chibi.ypos)
    
screen snape_chibi_standing_f:
    tag snape_chibi
    add im.Flip(snape_SC.chibi.stand_img, horizontal=True) at Position(xpos=snape_SC.chibi.xpos, ypos=snape_SC.chibi.ypos)
    
### DUEL ###
screen snape_defends:
    tag snape_chibi
    add "ch_sna defend" at Position(xpos=50, ypos=-5)
    
### SNAPE WALK ###
image snape_walk: #Default Snape walk animation.
    "01_hp/13_characters/snape/chibis/snape_02.png"
    pause.18
    "01_hp/13_characters/snape/chibis/snape_03.png"
    pause.18
    "01_hp/13_characters/snape/chibis/snape_02.png"
    pause.18
    "01_hp/13_characters/snape/chibis/snape_05.png"
    pause.18
    repeat

image snape_walk_f: #Default Snape walk animation.
    im.Flip("01_hp/13_characters/snape/chibis/snape_02.png", horizontal=True)
    pause.18
    im.Flip("01_hp/13_characters/snape/chibis/snape_03.png", horizontal=True)
    pause.18
    im.Flip("01_hp/13_characters/snape/chibis/snape_02.png", horizontal=True)
    pause.18
    im.Flip("01_hp/13_characters/snape/chibis/snape_05.png", horizontal=True)
    pause.18
    repeat
    
screen snape_walk: #Default Snape walk animation. 
    tag snape
    add "snape_walk" at custom_walk(walk_xpos, walk_xpos2)
    #at Position(xpos=680, ypos=345, xanchor="center", yanchor="center")
    zorder 4

screen snape_walk_f: #Default Snape walk animation. (Mirrored).
    tag snape
    add "snape_walk_f" at custom_walk(walk_xpos, walk_xpos2)
    zorder 4
    
    
    
    
    
    
### OLD SNAPE SCREENS ###
### SNAPE FULL
screen snape_main: #Snape. Full size.
    tag big_snape
    add s_sprite xpos snape_xpos ypos snape_ypos
    #zorder hermione_main_zorder #(5) Otherwise candle light is shown on top.
    zorder 5 #Otherwise candle light is shown on top.
    
### SNAPE HEAD
screen s_head: #Snape. Head.
    tag head
    add s_sprite xpos snape_head_xpos ypos snape_head_ypos # x = 330, Right bottom corner: y = 340
    zorder 8
   
screen s_head2: #Snape. Head.
    tag head
    add s_sprite xpos s_head_xpos ypos s_head_ypos # x = 330, Right bottom corner: y = 340
    zorder 8

### SNAPE EMOTIONS
screen s_emo_01: #Closed eyes and closed mouth.
    tag semo
    add "01_hp/13_characters/snape/main/s_emo_01.png" xpos tt_xpos ypos tt_ypos
    zorder 2 #Otherwise candle light is shown on top.
    
### SNAPE CHIBI
screen snape_01: #Snape stands still near the door.
    tag snape
    add "01_hp/13_characters/snape/chibis/snape_0130.png" at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos)
    
screen snape_01_f: #Snape stands still near the door. (Mirrored).
    tag snape
    add im.Flip("01_hp/13_characters/snape/chibis/snape_0130.png", horizontal=True) at Position(xpos=snape_chibi_xpos, ypos=snape_chibi_ypos)
    
screen snape_02: #Snape stands still near the desk.
    tag snape
    add "01_hp/13_characters/snape/chibis/snape_0130.png" at Position(xpos=500, ypos=210)
    zorder 3
    
