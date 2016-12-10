init python:
    def notNull(object):
        if object == None or object == "":
            return False
        else:
            return True
            
    def chibiWalk(image, x, x2, speed, y=250):
        global universal_walk_image
        global u_walk_x
        global u_walk_x2
        global u_walk_speed
        global u_walk_y
        universal_walk_image = image
        u_walk_x = x
        u_walk_x2 = x2
        u_walk_speed = speed
        u_walk_y = y
        renpy.show_screen("universal_walk")
        renpy.pause(speed)
        renpy.hide_screen("universal_walk")
    
    
##### Base Classes
    class silver_character_chibi(object):
        stand_img = ""
        blink_img = ""
        blink_img_f = ""
        walk_img = ""
        walk_img_f = ""
        zorder = 3
        xpos = 0
        ypos = 250
        
        def walk(self, x, x2, speed, y=250):
            if x > x2: #right to left
                chibiWalk(self.walk_img, x, x2, speed, y)
            else: #left to right
                chibiWalk(self.walk_img_f, x, x2, speed, y)
            self.xpos = x2
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
    
    class silver_character_face(object):
        description = ""
    
    class sliver_character_uniform(object):
        wear_top = True
        wear_bot = True
        wear_bra = True
        wear_panties = True
        
        top = ""
        bot = ""
        panties = ""
        bra = ""
    
    class sliver_character_head(object):
        face = None
        base = ""
        hair = ""
        cheeks = ""
        glasses = ""
        noHair = False
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
    
        def getLayers(self, parent):
            layers = []
            if self.hair != "" and not self.noHair:
                layers.append(parent.root+"body/head/"+self.hair)
            if self.face != None:
                if isinstance(self.face, silver_character_face):
                    layers.extend(self.face.getLayers(parent))
                else:
                    layers.append(parent.root+"body/face/preset/"+self.face)
            return layers
                
    class sliver_character_body(object):
        head = None
        tattoos = []
        left_arm = ""
        right_arm = ""
        torso = ""
        torso_pressed = ""
        abdomen = ""
        legs = ""
        noTorso = False
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
    
        def getLayers(self, parent):
            layers = []
            if self.right_arm != "":
                layers.append(parent.root+"body/arms/right/"+self.right_arm)
            if self.legs != "":
                layers.append(parent.root+"body/legs/"+self.legs)
            if self.abdomen != "":
                layers.append(parent.root+"body/abdomen/"+self.abdomen)
            if self.left_arm != "":
                layers.append(parent.root+"body/arms/left/"+self.left_arm)
            if self.torso != "":
                if not parent.uniform.wear_top and not parent.uniform.wear_bra:
                    layers.append(parent.root+"body/torso/"+self.torso)
                else:
                    layers.append(parent.root+"body/torso/"+self.torso_pressed)
            for tattoo in self.tattoos:
                layers.append(parent.root+"body/tattoo/"+tattoo)
            if self.head != None:
                layers.extend(self.head.getLayers(parent))
            return layers
    
    class silver_character(object):
        root = ""
        flip = False
        busy = False
        known = False
        unlocked = False
        name = ""
        pet_name = ""
        genie_name = "Professor"
        
        screen = ""
        screen_head = ""
        
        chibi = None
        
        xpos = 0
        ypos = 0
        zorder = 5
        
        eye_color = ""
        
        faces = None
        
        char_ref = None
        h_char_ref = None
        
        body = None
        outfit = None
        uniform = None
        
        use_action = False
        use_outfit = False
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def setFace(self, index):
            self.body.head.face = self.faces[index-1]
            for face in self.faces:
                if face.id == index:
                    renpy.say(None,face.id+" "+face)
            
        def setNewFace(self, faceOBJ):
            self.body.head.face = faceOBJ
        
        def setHair(self, style, color):
            if style != None and color != None:
                self.body.head.hair = str(style)+"_"+str(color)+".png"
            
        def setOutfit(self, outfit):
            if outfit == None:
                self.use_outfit = False
            else:
                self.use_outfit = True
            self.outfit = outfit
        
        def outfitFromList(self, id):
            for outfit in hermione_outfits_list:
                if outfit.name == id:
                    self.setOutfit(outfit)
        
        def setUniformLevel(self, level):
            self.uniform.setLevel(level)
            self.chibi.setLevel(level)
        
        # Say w/ sprite
        def say(self, text, face=None):
            if face != None:
                renpy.hide_screen(self.screen)
                self.setFace(face)
            renpy.show_screen(self.screen)
            renpy.with_statement(Dissolve(0.3),always=True)
            renpy.say(self.char_ref,text)
        
        #Say w/ Head
        def sayHead(self, string):
            #set face here
            renpy.show_screen(self.screen_head)
            renpy.say(self.h_char_ref,string)
            renpy.hide_screen(self.screen_head)
        
        def showScreen(self, dissolve=0):
            renpy.show_screen(self.screen)
            if dissolve > 0:
                renpy.with_statement(Dissolve(dissolve/10),always=True)
        def hideScreen(self, dissolve=0):
            renpy.hide_screen(self.screen)
            if dissolve > 0:
                renpy.with_statement(Dissolve(dissolve/10),always=True)
        
        def getActionLayers(self):
            return
            
        def getOutfitLayers(self):
            layers = []
            if self.outfit.hair_layer != "":
                self.body.head.noHair = True
                layers.append(self.root+"clothes/custom/"+self.outfit.hair_layer+".png")
            if self.body != None:
                layers.extend(self.body.getLayers(self))
            if self.outfit.breast_layer != "":
                self.body.noTorso = True
                layers.append(self.root+"body/breasts/"+self.outfit.breast_layer+".png")
            if self.outfit != None:
                layers.extend([self.root+"clothes/custom/"+o_layer for o_layer in self.outfit.outfit_layers])
            if self.outfit.hair_layer != "":
                layers.append(self.root+"clothes/custom/"+self.outfit.hair_layer+"_2.png")
            elif self.body.head.hair != "":
                layers.append(self.root+"body/head/"+self.body.head.hair.replace(".png","_2.png"))
            if self.outfit != None:
                for layer in self.outfit.top_layers:
                    layers.append(self.root+"clothes/custom/"+layer)
            return layers
    
        def getUniformLayers(self):
            layers = []
            if self.body != None:
                layers.extend(self.body.getLayers(self))
            if self.uniform != None:
                layers.extend(self.uniform.getLayers(self))
            if self.body.head.hair != "":
                layers.append(self.root+"body/head/"+self.body.head.hair.replace(".png","_2.png"))
            return layers
            
        def getLayers(self):
            layers = []
            self.body.head.noHair = False
            self.body.noTorso = False
            if self.use_outfit:
                layers.extend(self.getOutfitLayers())
            else:
                layers.extend(self.getUniformLayers())
            return layers
    
    class silver_face_lib(object):
        lib = []
        def getFace(self,id):
            for face in lib:
                if face.id == id:
                    return face
        
    class silver_face(object):
        id = ""
        description = ""
        layers = []
    
    import xml.etree.ElementTree as ET
    character_faces = ET.parse(renpy.loader.transfn('character_faces.xml')).getroot()
    
    def getCharacterFaces(tag=None, character_face=None):
        if tag != None and character_face!=None:
            return [character_face(**face.attrib) for face in character_faces.findall(tag)]
    
    
    
###### Luna
    class luna_character_face(silver_character_face):
        description = ""
        
        forehead = ""
        eyebrow = ""
        eye = ""
        pupil = ""
        nose = ""
        cheeks = ""
        mouth = ""
        tears = ""
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
            
        def changeFace(self, l_eye=None,l_pupil=None,l_eyebrow=None,l_mouth=None,fullName=False):
            if l_eye != None:
                self.eye = "eye_"+l_eye+".png"
            if l_pupil != None:
                self.eye = "pupil_"+l_pupil+".png"
            if l_eyebrow != None:
                self.eye = "eyebrow_"+l_eyebrow+".png"
            if l_mouth != None:
                self.eye = "mouth_"+l_mouth+".png"
            
        def getLayers(self, parent):
            layers = []
            if self.cheeks != "":
                layers.append(parent.root+"body/face/cheeks/"+self.cheeks)
            if self.nose != "":
                layers.append(parent.root+"body/face/nose/"+self.nose)
            if self.mouth != "":
                layers.append(parent.root+"body/face/mouth/"+self.mouth)
            
            layers.append(parent.root+"body/face/eye_white.png")
            if self.pupil != "":
                layers.append(parent.root+"body/face/pupil/"+self.pupil)
            if self.eye != "":
                layers.append(parent.root+"body/face/eye/"+self.eye)
            if self.eyebrow != "":
                layers.append(parent.root+"body/face/eyebrow/"+self.eyebrow)
            if self.tears != "":
                layers.append(parent.root+"body/face/tears/"+self.tears)
            return layers
    
    class luna_character_uniform(sliver_character_uniform):
        
        def __init__(self, **kwargs):
            self.__dict__.update(**kwargs)
        
        def getLayers(self, parent):
            layers = []
            if self.panties != "" and self.wear_panties and not self.wear_bot:
                layers.append(parent.root+"clothes/underwear/"+self.panties)
            if self.bra != "" and self.wear_bra and not self.wear_top:
                layers.append(parent.root+"clothes/underwear/"+self.bra)
            if self.bot != "" and self.wear_bot:
                layers.append(parent.root+"clothes/uniform/"+self.bot)
            if self.top != "" and self.wear_top:
                layers.append(parent.root+"clothes/uniform/"+self.top)
            return layers
    
    
label __init_variables:
    
    $ reset_char_obj = True
    if not hasattr(renpy.store,'luna_SC') or reset_char_obj: #important!
        $ luna_SC = silver_character(
            root = "01_hp/13_characters/luna/",
            
            name = "Luna Lovegood",
            pet_name = "Miss Lovegood",
            genie_name = "Professor",
            
            screen = "test_luna_obj",
            screen_head = "test_luna_head_obj",
            
            
            chibi = silver_character_chibi(
                stand_img = "01_hp/13_characters/luna/chibis/walk/l_walk_a_01.png",
                blink_img = "ch_lun blink_a",
                blink_img_f = "ch_lun blink_a_flip",
                walk_img = "ch_lun walk_a",
                walk_img_f = "ch_lun walk_a_flip",
            ),
            
            xpos = 370,
            ypos = 0,
            
            body = sliver_character_body(
                head = sliver_character_head(
                    expression = None,
                    base = "",
                    hair = "hair_01.png",
                    cheeks = "cheeks_01.png",
                    glasses = ""
                ),
                left_arm = "",
                right_arm = "",
                torso = "torso.png",
                torso_pressed = "torso_pressed.png",
                abdomen = "base_01.png",
                legs = ""
                
            ),
            uniform = luna_character_uniform(
                top = "top.png",
                bot = "skirt.png",
                panties = "panties.png",
                bra = "bra.png",
            ),
            acc = ""
        )
    $ luna_SC.faces = getCharacterFaces('luna_face',luna_character_face)
    $ luna_SC.setFace(1)
    
    
    return
    
screen test_herm_obj:
    $ char = hermione_SC
    for layer in char.getLayers():
        if char.flip:
            add im.Flip(layer, horizontal=True) xpos char.xpos ypos char.ypos
        else:
            add layer xpos char.xpos ypos char.ypos
    zorder 4
    
screen test_herm_head_obj:
    $ char = hermione_SC
    for layer in char.getLayers():
        add layer xpos 650 ypos 235
    zorder 8
        
screen test_luna_obj:
    $ char = luna_SC
    for layer in char.getLayers():
        if char.flip:
            add im.Flip(layer, horizontal=True) xpos char.xpos ypos char.ypos
        else:
            add layer xpos char.xpos ypos char.ypos
    zorder 4
    
screen test_luna_head_obj:
    $ char = luna_SC
    for layer in char.getLayers():
        add layer xpos 650 ypos 235
    zorder 8
        
    
label test_char_objs:
    $ hermione_SC.showScreen()
    $ luna_SC.showScreen()
    menu char_obj_menu_root:
        "-Test Walk-":
            $ hermione_SC.chibi.walk(600,200,4)
            jump char_obj_menu_root
        "-Hermione-":
            $ uni_char = hermione_SC
        "-Luna-":
            $ uni_char = luna_SC
        "-Exit-":
            $ hermione_SC.hideScreen()
            $ luna_SC.hideScreen()
            jump day_main_menu
    menu uni_char_obj_root:
        "-Position-":
            menu uni_char_pos:
                "-Flip-":
                    if uni_char.flip:
                        $ uni_char.flip = False
                    else:
                        $ uni_char.flip = True
                    jump uni_char_pos
                "-Left-":
                    $ uni_char.xpos = 0
                    jump uni_char_pos
                "-Right-":
                    $ uni_char.xpos = 570
                    jump uni_char_pos
                "-Back-":
                    jump uni_char_obj_root
        "Layers":
            menu uni_char_layers:
                "-Eye Color-":
                    menu:
                        "-Blue-":
                            $ uni_char.body.head.face.eye_color = "blue"
                            jump uni_char_layers
                        "-Brown-":
                            $ uni_char.body.head.face.eye_color = "brown"
                            jump uni_char_layers
                        "-Green-":
                            $ uni_char.body.head.face.eye_color = "green"
                            jump uni_char_layers
                        "-Pink-":
                            $ uni_char.body.head.face.eye_color = "pink"
                            jump uni_char_layers
                "-Toggle top-":
                    if uni_char.uniform.wear_top:
                        $ uni_char.uniform.wear_top = False
                    else:
                        $ uni_char.uniform.wear_top = True
                    jump uni_char_layers
                "-Toggle bot-":
                    if uni_char.uniform.wear_bot:
                        $ uni_char.uniform.wear_bot = False
                    else:
                        $ uni_char.uniform.wear_bot = True
                    jump uni_char_layers
                "-Toggle bra-":
                    if uni_char.uniform.wear_bra:
                        $ uni_char.uniform.wear_bra = False
                    else:
                        $ uni_char.uniform.wear_bra = True
                    jump uni_char_layers
                "-Toggle panties-":
                    if uni_char.uniform.wear_panties:
                        $ uni_char.uniform.wear_panties = False
                    else:
                        $ uni_char.uniform.wear_panties = True
                    jump uni_char_layers
                "-Back-":
                    jump uni_char_obj_root
        "-Back-":
            jump char_obj_menu_root
    
        # def setOutfitTransition(self, outfit):
            # renpy.show_screen("blkfade")
            # renpy.hide_screen(self.main_screen)
            # renpy.with_statement(Dissolve(0.3))
            # if outfit == None:
                # self.use_outfit = False
            # else:
                # self.use_outfit = True
            # self.outfit = outfit
            # renpy.pause(0.5)
            # renpy.hide_screen("blkfade")
            # renpy.with_statement(Dissolve(0.5))