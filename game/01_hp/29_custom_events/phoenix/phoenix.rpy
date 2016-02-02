
### PETTING ###
label petting:
    if fawkes_intro_done:
        if day >= 20 and bird_interact >= 10: # Counts how many times you have interacted with the bird.
            stop music fadeout 3.0
            show screen blktone8
            play music "music/Dark Fog.mp3" fadein 2.5
            hide screen genie
            show screen petting
            with d7
            ">The bird starts to warm up as you pet it."
            m "?"
            hide screen petting
            show screen petting
            ">The bird gets hotter and hotter."
            menu:
                "-Continue to pet the bird-":
                    $ bird_interact += 1 # Counts how many times you have interacted with the bird.
                    m "Might as fucking well."
                    hide screen petting
                    show screen petting
                    ">You feel energy swirling in the room."
                    ">Suddenly the entire room is buzzing."
                    hide screen petting
                    show screen petting
                    m "Why am I still petting this thing?"
                    ">The buzzing quickly stops leaving you with a ringing in your ears."
                    $ renpy.play('sounds/door3.mp3')
                    "Professor?"
                    m "Hrm?"
                    "You called me here?"
                    m "? ... No."
                    $ renpy.play('sounds/door.mp3')
                    ">You see someone standing just outside of the door, too far for you to see."
                    her "I felt something calling me here."
                    $ walk_xpos=800
                    $ walk_xpos2=400
                    $ hermione_speed = 02.2
                    show screen hermione_walk_01
                    m "Well come right on in then..."
                    hide screen hermione_walk_01
                    $ hermione_chibi_xpos=400
                    $ hermione_chibi_ypos=240
                    show screen hermione_01
                    her "Something... feels different..."
                    $ h_body = "01_hp/13_hermione_main/body_10.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    ">She looks up at the bird you're petting and her eyes grow wide."
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/body_18.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    her "Professor. Something's wrong."
                    m "Why don't you tell me why you're here in the first place?"
                    her "Professor! Fawkes is-!"
                    $ renpy.play('sounds/pistol2.mp3')
                    ">Popping noises start coming from all around the room."
                    hide screen hermione_main
                    m "What the fuck?! What's going on?!"
                    $ hair_style = "B"
                    $ hair_color = 3
                    $ badges = False
                    $ only_upper = True
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_1.png"
                    $ h_xpos=50
                    $ h_ypos=0
                    show screen hermione_main
                    show screen ctc
                    pause
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_1.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    "Hermione- I think" "Sup?"
                    m "..."
                    m "What?"
                    "Hermione- I think" "You can't tell what's going on?"
                    m "Why don't you just go ahead and fill me in."
                    "Hermione- I think" "Seeing as you can't figure it out, it's me.  Fawkes."
                    m "... Is that supposed to mean something to me?"
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_2.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    faw "The bird you've been petting so nicely for the past few days."
                    m "?"
                    m "Then how are you in the girl?"
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_1.png"
                    show screen hermione_main
                    faw "Really?"
                    faw "It's called magic.  You've been so horny it's started to affect me."
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_3.png"
                    show screen hermione_main
                    faw "So I figured I'd jump into the girl for a bit and see if I can't fix your little... problem."
                    m "Oh?"
                    g9 "And how do you plan on doing that?"
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_2.png"
                    show screen hermione_main
                    faw "Well that depends on you.  I can only take over her if her defences are down."
                    m "Huh?"
                    faw "You need to make her horny for me to jump her."
                    faw "The hornier she is, the longer I can stay on."
                    faw "You've been wanting to fuck this girl so hard for the past few days...  That's what's letting me hold on for so long, but this wont work again."
                    faw "I don't have much time left, but how about I show you some of my other outfits?"
                    m "A small consolation."
                    faw "Enjoy."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_4.png"
                    show screen hermione_main
                    show screen ctc
                    pause
                    faw "How's this?"
                    m "So no original content?"
                    faw "Maverick's not an artist"
                    g4 "No shit"
                    hide screen hermione_01
                    $ hermione_chibi_xpos=400
                    $ hermione_chibi_ypos=240
                    show screen hermione_02_b
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_5.png"
                    show screen hermione_main
                    show screen ctc
                    pause
                    faw "Do you like this one?"
                    g9 "Now this I can get behind!"
                    faw "I bet you'd love that."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_6.png"
                    show screen hermione_main
                    faw "Wouldn't you?"
                    g5 "..."
                    g10 "..."
                    m "You god damned bet I would."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/fawkes_7.png"
                    show screen hermione_main
                    faw "Well, it's been fun, but I'm gonna bring the girl back now."
                    m "That didn't last nearly as long as I'd hoped."
                    faw "I'll do you a small favor and leave her like this."
                    hide screen hermione_main
                    $ hair_color = 0
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/hermione_1.png"
                    show screen hermione_main
                    her "..."
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/hermione_2.png"
                    $ hair_style = "A"
                    show screen hermione_main
                    her "Professor?!"
                    hide screen hermione_main
                    with d3
                    $ h_body = "01_hp/13_hermione_main/phoenix/hermione_3.png"
                    show screen hermione_main
                    her "What's going on?!"
                    m "Hell if I know"
                    her "Why am I wearing this? What's happening? What-!"
                    hide screen hermione_main
                    $ walk_xpos=400
                    $ walk_xpos2=800
                    $ hermione_speed = 00.75
                    show screen hermione_chibi_robe_f
                    m "Well I guess that was interesting"
                    $ fawkes_intro_done = True #Makes this non-repeatable
                    hide screen hermione_chibi_robe_f
                    hide screen petting
                    hide screen blktone8
                    with d3
                    $ badges = True
                    $ only_upper = False
                    call music_block
                    jump day_main_menu
                "-Stop petting the bird-":
                    $ bird_interact -= 2 # Counts how many times you have interacted with the bird.
                    m "Well that's fucking weird"
                    hide screen petting
                    show screen genie
                    hide screen blktone8
                    with d3
                    call music_block
                    jump day_main_menu

        else: #needs more interactions for introduction

            ###DEFAULT PETTING WHEN NOT INTRODUCED###

            $ bird_interact += 1 # Counts how many times you have interacted with the bird.
            hide screen genie
            show screen petting
            with Dissolve(0.3)
            pause 3
            show screen sad_phoenix #SMILEY
            pause 1.5
            m "The bird doesn't look good. Is it sick or something?"
            pause .5
            show screen genie
            hide screen sad_phoenix #SMILEY
            hide screen petting
            with Dissolve(0.3)
            call screen main_menu_01

    else:  #fawkes_intro_done == True

        if whoring <=2:
            stop music fadeout 3.0
            $ bird_interact += 1
            show screen blktone8
            play music "music/Dark Fog.mp3" fadein 2.5
            hide screen genie
            show screen petting
            with d7
            faw "You realize petting me wont make something happen every time don't you?"
            m "..."
            m "How exactly are you talking to me right now?"
            faw "Magic.  When are you going to learn to stop asking questions and realize the answer is always magic."
            m "I liked you a lot better when you were in that witch's body"
            hide screen petting
            hide screen blktone8
            with d3
            call music_block
            jump day_main_menu

        elif bird_interact == 20 and whoring ==1:
            stop music fadeout 3.0
            $ bird_interact += 1
            show screen blktone8
            play music "music/Dark Fog.mp3" fadein 2.5
        #elif whoring > 9000:
            #scene
            #remember to sort the scenes from highest to lowest whoring, this way the highest possible event will happen
        #else:
            #DEFAULT PETTING WHEN INTRODUCED GOES HERE (if you want)


### TALKING ###
label talkingfawkes:
    $ bird_interact += 1
    hide screen genie
    show screen petting
    with Dissolve(0.3)
    pause 3
    $ genie_speaks = renpy.random.randint(1, 3)
    if genie_speaks == 1:
        m "Well aren't you gonna say anything?"
        faw "..."
        m "..."
        m "Great help you are... Damned bird"
    elif genie_speaks == 2:
        faw "Can I help you?"
        m "Wanna turn into a hot girl and have sex?"
        faw "Maybe if you get that witch from earlier horny I can take over her again."
    elif genie_speaks == 3 and whoring >= 10:
        faw "I'm conflicted."
        m "Why is that?"
        faw "Part of me is extremely horny and wants to jump your bones right now."
        g9 "And that's a problem because?"
        faw "The other part of me is disgusted by what you've turned that girl into."
        g4 "Just stop playing coy and bring her in here."
        faw "If you keep talking like that I'll just find someone else to jump."
    elif genie_speaks == 3 and whoring <= 10:
        faw "Look, I'm horny, but in order for me to get that girl in here I need her to be weaker."
        m "I'm listenting."
        faw "Make her morals a little looser and I might actually be able to fuck you."
        m "..."
        g9 "I'm on it."
    elif genie_speaks == 3 and whoring <= 5:
        faw "I think I'm feeling something!"
        m "Really?"
        g9 "{size=-4}(I'm finally gonna get lucky again!){/size}"
        faw "It's definitely coming!"
        g9 "{size=-4}(Oh I'll be coming alright.){/size}"
        $ faw_sneeze4 = renpy.random.randint(1, 2)
        if faw_sneeze4 == 1:
            faw "{size=+5}ACHOOOOOO!{/size}"
            faw "..."
            g11 "You sneezed?"
            faw "I guess that's what I was feeling."
            g11 "{size=+3}All over me?!{/size}"
            faw "No God bless you?"
            g4 "{size=-4}Fucking bird...{/size}"
        elif faw_sneeze4 == 2 and whoring >= 3:
            $ renpy.play('sounds/door3.mp3')
            g4 "What do you want? I'm busy!"
            her "{size=-2}Are you sure you want me to leave?{/size}"
            m "No no! Come on in!"
            $ renpy.play('sounds/door.mp3')
            $ walk_xpos=620
            $ walk_xpos2=400
            $ hermione_speed = 02.0
            show screen hermione_chibi_robe
            m "Well come right on in then..."
            hide screen hermione_chibi_robe
            $ hermione_chibi_xpos=400
            $ hermione_chibi_ypos=240
            show screen hermione_02_b
            $ robe_on = True
            $ h_body = "01_hp/13_hermione_main/body_10.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            her "Professor.  There was something... calling me here."
            g9 "And what was it calling you here for?"
            her "I'm not sure... Maybe I shouldn'tve come sir."
            m "No no, stay."
            her "Goodbye professor."
            hide screen hermione_main
            $ walk_xpos=400
            $ walk_xpos2=800
            $ hermione_speed = 02.0
            show screen hermione_chibi_robe_f
            g4 "Stop her you damned bird!"
            faw "On it!"
            $ renpy.play('sounds/magic2.mp3')
            pause 1
            $ walk_xpos=620
            $ walk_xpos2=400
            $ hermione_speed = 02.5
            show screen hermione_chibi_robe
            $ h_body = "01_hp/13_hermione_main/phoenix/h0a.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            her "..."
            her "Professor... I shouldn't be here."
            g9 "Oh no, you're right where you should be."
            hide screen hermione_main
            $ robe_on = False
            $ h_body = "01_hp/13_hermione_main/phoenix/h0b.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            $ renpy.play('sounds/glass_break.mp3')
            her "{size=+3}No professor I-{w=.1}{nw}"
            faw "Oh no you don't!"
            $ renpy.play('sounds/magic2.mp3')
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/h1a.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            faw "Don't you worry.  She's not going anywhere."
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/h1b.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            her "No!  Why can't I move?"
            faw "Damnit!  I have to keep her under control!"
            $ renpy.play('sounds/magic2.mp3')
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/h2.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            ">..."
            m "..."
            m "Girl?"
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/h3.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            "Hermione?" "Is this what you want?"
            m "Well shit.  I guess we broke her."
            "Hermione?" "Oh don't worry."
            hide screen hermione_main
            $ hair_style = "B"
            $ hair_color = 3
            $ badges = False
            $ only_upper = True
            $ h_body = "01_hp/13_hermione_main/phoenix/f_new.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            faw "I've got her now."
            g9 "Finally!  Now I get to fuck your brains out."
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/f_dis.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            faw "Well... I'd love to, but that's not really an option right now."
            m "What?"
            faw "She's still too resistant to my magic."
            m "..."
            g4 "{size=+4}WHAT?!{/size}"
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/f_wor.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            faw "Oh come on now."
            faw "I brought her in, and I've got her wearing this don't I?"
            m "Doesn't mean I'm happy yet."
            faw "Just get her to be closer to you."
            faw "Once you get her to whore herself out a little more, I'll be able to control her for longer."
            m "I guess that's what I'm here in the first place."
            faw "Well, I hope you enjoyed the view, but she's coming back."
            faw "Would you rather I leave her here?..."
            hide screen hermione_main
            $ h_body = "01_hp/13_hermione_main/phoenix/f_sin.png"
            $ h_xpos=390
            $ h_ypos=0
            show screen hermione_main
            faw "Or surprise her and make her wear this outside?"
            menu:
                "-Make her stay-":
                    g9 "Go ahead and stay here"
                    faw "Oh I like the way you think."
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/f_trans.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    $ renpy.play('sounds/magic2.mp3')
                    hide screen hermione_main
                    $ hair_color = 0
                    $ h_body = "01_hp/13_hermione_main/phoenix/h_trans.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    her "..."
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/h_react1.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    her "..."
                    hide screen hermione_main
                    $ h_body = "01_hp/13_hermione_main/phoenix/h_react2.png"
                    $ h_xpos=390
                    $ h_ypos=0
                    show screen hermione_main
                    her "Professor?"
                    her "Oh god.  What's happening?!"
                    hide screen hermione_main
                    $ walk_xpos=400
                    $ walk_xpos2=800
                    $ hermione_speed = 02.0
                    show screen hermione_chibi_robe_f
                    $ renpy.play('sounds/door.mp3')
                    g9 "Wonderful show."
                    hide screen hermione_chibi_robe_f
                    faw "Wasn't it?"
                "-Let her go into the hallway-":
                    g9 "Take her outside."
                    faw "As you wish."
                    $ walk_xpos=400
                    $ walk_xpos2=640
                    $ hermione_speed = 02.0
                    show screen hermione_chibi_robe_f
                    $ renpy.play('sounds/door.mp3')
                    hide screen hermione_chibi_robe_f
                    g9 "{size=-4}(Here we go!){/size}"
                    ">..."
                    g9 "{size=-4}(Any second now!){/size}"
                    ">..."
                    m "..."
                    her "{size=+6}AAAAAAAAAAAAAAHHH!!{/size}"
                    g9 "{size=-4}(There we go.){/size}"
                    her "{size=+3}Where are my clothes?{/size}"
                    her "{size=+4}Why am I wearing this?{/size}"
                    her "{size=+4}No! Stop looking at me!{/size}"
                    $ renpy.play('sounds/run_02.mp3')
                    her "{size=+2}Don't look don't look don't look!{/size}"
            g9 "I'm starting to like you more and more you stupid bird."
            faw "It's Fawkes."
            m "Don't push it."
            $ badges = True
            $ only_upper = False
        else:
            faw "There's definitely energy!  I'm just having a hard time focusing it!"
            g4 "Well focus it!"
            faw "{size=+3}I'm trying, but I can't.{/size}"
            faw "You need to make Hermione more of a whore if you want me to take control of her."
            m "..."
            m "Hermione?"
            faw "Really?  The witch you've been drooling over and trying to fuck?"
            m "She has a name?"
            faw "Just make her horny, and try again.  I'm can't bring her here otherwise."
    show screen genie
    hide screen petting
    with Dissolve(0.3)
    call screen main_menu_01