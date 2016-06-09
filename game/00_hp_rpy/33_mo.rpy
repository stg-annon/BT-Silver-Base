label tentacle_shop_scene:
    show screen shop_screen
    if tent_scroll:
        "You already own this scroll"
        call screen shop_screen
    if whoring <= 15:
        m "What's in this scroll?"
        sna_[1] "Don't worry about it."
        m "Why?"
        sna_[1] "You're not ready for what's in this scroll."
        m "Well that just makes me want it more."
        sna_[1] "Too bad."
        call screen shop_screen
    m "What's this scroll?"
    sna_[1] "This is the recipe for a powerful and forbidden potion."
    m "What does it do?" 
    sna_[1] "It transforms you into any magical creature you desire."
    m "Like what?"
    sna_[1] "Anything you can secure a sample of."
    sna_[1] "A powerful phoenix, a terrifying gorgon, a deadly basilisk or an awe inspiring dragon."
    m "Not sure I'd really want to transform into any of those, I am trying to keep my presence here a secret after all."
    sna_[1] "Well then perhaps there is a creature that would suit you and your \"Hobbies\"."
    m "Such as?"
    sna_[1] "There are rumours of a plant hidden somewhere on the school grounds"
    m "A plant? Why would I want to be a plant?"
    sna_[1] "This is no ordinary plant, it has fast and powerful limbs that are incredibly sensitive"
    m "So it's a tentacle monster?"
    sna_[1] "Pretty much. I'm not sure where it lives however. The real Dumbledore always kept it's location a secret from me."
    m "Well who does know?"
    sna_[1] "Apparently three students have encountered it."
    m "Do you know their names?"
    sna_[1] "No sorry, I was busy attending to other \"matters\" when it happened. You'll have to ask around, try the inn."
    m "Ok, well how much is the scroll?"
    sna_[1] "1200 gold coins."
    m "1200! Why on earth is it so expensive?"
    sna_[1] "Forbidden magic is quite a risky and expensive endeavour my friend, I'll sell it for no less than 1200."
    menu:
        "-Buy the scroll- (1200)" if gold >= 1200:
            m "Fine, here's the money"
            sna_[1] "Thank you very much"
            $ gold -= 1200
            $ tent_scroll = True
            $ attic_open = True
            call screen shop_screen
        "-No thanks-":
            m "No thanks, not right now"
            sna_[1] "Perhaps later then"
            call screen shop_screen
    
label tentacle_scene_intro: #Public tentacle scene
    show screen blkfade
    spo "Today class, I have been requested by the Headmaster to teach you about a plant called Devil's Snare."
    spo "This is an incredibly dangerous plant, known to constrict and kill it's prey with it's fast and powerful tendrils."
    spo "They are found naturally in caves and swamps as they like dark and damp places and hate sunlight."
    her "Isn't Devil's Snare extremely dangerous?"
    spo "That's correct Miss Granger, that's why Professor Dumbledore has provided us with some freshly grown samples."
    spo "They're barely one week old, they'll barely be able to stroke you with their tendrils, let alone constrict you."
    spo "Now everyone pass the samples around so that you all can get a good look."
    her "Professor Sprout, are they supposed to have mouths?"
    spo "Yes Miss Granger, it's how they eat their prey once they have asphyxiated them."
    her "Ok, well what are the eyes for? I thought they sensed their prey by touch?"
    spo "What are you talking about, Devil's Snare don't have eyes."
    her "This one does..."
    ">All of a sudden, you explode outwards in a flash of thick green tentacles"
    her "What's happening?!?"
    ">You quickly bind her wrists and stomach..."
    her "I can't move!"
    ">then lift her into the air with your powerful appendages."
    spo "Stay calm Miss Granger, Devil's Snare will let you go if you don't move"
    ">Slinking your slimy tentacles under her top and skirt."
    her "Oh no..."
    ">You rip her top of in a flurry of buttons and cotton."
    her "Ahhhh"
    ">Sliding your tentacles up her legs and slowly pull them apart"
    ">Hermione struggles against you but her effort is in vain."
    her "Please no... Not here."
    ">The tentacles slowly pull up her panties, revealing her to the class"
    mal "Wow..."
    fem "This is horrible, someone should do something"
    mal2 "Professor Sprout says as long as she doesn't move she'll be released."
    ">You position a large, flowered tentacle above Hermione's head"
    her "What is that?"
    ">It suddenly opens to reveal a long slender appendage with an engorged base"
    her "What the hell is that? It looks like a..."
    ">While she is focused on the dangling limb above her you move six smaller tentacles towards her waist"
    her "Oh god no, someone please help me! Professor Sprout do something!"
    spo "Ok students, stand back!"
    ">Professor Sprout casts an impressive looking spell at the mass of writhing tentacles"
    spo "Confringo!"
    ">It strikes the plant forcefully but does nothing."
    spo "What? That should have killed it. It must be magically protected."
    ">You move three tentacles to her vagina and start teasing the opening."
    her "Please Professor Sprout, do something! Anything!"
    spo "I'm not sure I can, it has a powerful magical spell protecting it"
    spo "If I try anything more powerful than the spell I just cast I might hurt you."
    ">You move two smaller tentacles to her asshole and start teasing the entrance, slowly prying it open"
    her "Well then what am I supposed to do?"
    spo "Just stay as still as possible and it should eventually let you go..."
    ">You move a tentacle with a mouth on the end of it to her right breast and latch onto it."
    her "Please, I'm not going to be able to stay still if this keeps going"
    ">The three tentacles at the entrance of her vagina suddenly thrust into her"
    $ tentacle_cosmetic = True
    if lock_public_favors == False:
        jump tentacle_1
    jump tentacle_2
            

label tentacle_1: #Public tentacle scene
    $ cg("01_hp/28_cg/p1.png")
    hide screen blkfade
    with d3
    her "What on earth is going on?"
    ">You start pumping the tentacles in her vagina slowly"
    $ cg("01_hp/28_cg/p2.png")
    her "Oh..."
    ">You move a small tentacle with a mouth on the end to her ear so that only she can hear you."
    m "Enjoying yourself slut?"
    her "Professor!"
    spo "Just relax dear. I'm sure it'll let you go soon."
    m "That's right, do as your dear Professor says, just relax."
    her "How am I supposed to relax?!"
    m "Well if you're not going to relax, at least try to enjoy it..."
    ">You start rotating the tentacles in her vagina."
    $ cg("01_hp/28_cg/p3.png")
    her "..."
    spo "What's wrong Miss Granger?"
    her "It's nothing... it's just very uncomfortable..."
    m "Are you sure you're uncomfortable? Judging by how wet you are I'd say that you're the opposite."
    m "Someone might even think that you were enjoying this."
    her "They wouldn't..."
    mal "Who's she talking to?"
    mal2 "I've got no idea."
    m "Are you sure? Do you think you'll be able to stifle every moan?"
    ">You push deeply into her with the 3 tentacles."
    her "!!!"
    $ cg("01_hp/28_cg/p4.png")
    m "Do you think you'll be able to stop your hips from bucking?"
    ">You give her another powerful thrust."
    her "{size=-6}mmmm{/size}"
    m "Do you really think that you'll be able to stop yourself from begging me for more?"
    ">You increase the speed of the tentacles"
    her "{size=-3}mmmmmmm{/size}"
    m "I don't think you will. In fact I know that you won't."
    m "Because I know what you are. A slut."
    m "A slut who can only think about getting off when she's being fucked by a monster in front of her classmates."
    ">You stop moving the tentacles."
    m "Now tell them what you are."
    her "W-w-what? No please, just don't stop."
    m "Tell them what you are and I'll keep going."
    her "I can't... Just keep going..."
    m "Say it."
    her "{size=-3}I'm a slut.{/size}"
    ">You start rotating the tentacles in her vagina ever so slowly."
    m "What was that? I don't think that they heard you. Why don't you say it once more, with feeling."
    her "I'm a slut!"
    ">You begin fiercely fucking her vagina."
    her "Yes, yes, I'm a fucking slut. Fuck me harder."
    m "See that wasn't so hard now was it. How about I give you a little reward."
    her "Wha-"
    $ cg("01_hp/28_cg/p5.png")
    ">You thrust a ribbed tentacle deeply into her asshole in one motion."
    her "!!!"
    her "It's in my ass... I-I'm cumming."
    ">You take alternating turns pumping into her ass and pussy."
    her "I'm cumming! It's too much..."
    $ cg("01_hp/28_cg/p6.png")
    ">You feel her body shudder as the orgasm rocks her."
    ">This only spurs you on to fuck her harder."
    her "Please... no more... I'll faint..."
    ">You start to feel a strange energy flowing through the vines, moving towards the tips."
    m "This is it girl, get ready."
    her "...ready?..."
    $ cg("01_hp/28_cg/p7.png")
    ">With one final surge you release the pent up energy in a surge of white sap all over her."
    m "Oh gods, it's like each vine is cumming. This is amazing..."
    ">The sensations proved to much for hermione and she faints, going limp in your tentacles."
    mal "What a slut..."
    fem "I told you so."
    mal2 "Man, I'm going to have to join Gyrffindor."
    ">You place Hermione back onto the desk as the plant that you are occupying slowly wilts and dies."
    ">Professor Sprout quickly runs over."
    spo "Miss Granger are you okay?"
    her "..."
    spo "Quickly, someone take her to the hospital."
    mal "Should we cover her up?"
    spo "Oh yes, I suppose you should."
    $ tentacle_cosmetic = False
    hide screen cg
    $ hermione_takes_classes = True
    jump day_main_menu

    #enter vagina
    #put flower to ear
    #call her a slut
    #make her call out to class mates
    #have class mates comment
    #continue fucking her
    #have her talk about how enjoyable it is

label tentacle_2: #Enjoyable tentacle scene
    $ cg("01_hp/28_cg/p1.png")
    hide screen blkfade
    with d3
    her "What the hell kind of plant is this?"
    ">You start pumping the tentacles in her vagina slowly"
    her "Oh..."
    ">You move a small tentacle with a mouth on the end to her ear so that only she can hear you."
    m "Enjoying yourself [hermione_name]?"
    her "Profes-"
    $ cg("01_hp/28_cg/e2.png")
    ">You quickly force another flowered tentacle into her mouth"
    m "Now, now [hermione_name], you don't want anyone to find out that how you've been earning so many points now do you?"
    her "mmmmmoo"
    m "Well then just do what Miss Sprout says and stay still."
    m "Just act like this is some horrible accident, that you are just a victim."
    m "Instead of the slut that you really are..."
    ">You start to rotate the tentacles in her vagina."
    m "mmmmmm"
    mal "Wow, I think she's starting to enjoy it."
    fem "Hermione? No way she's probably just trying to scream."
    mal2 "I don't know, she doesn't look like she hates it"
    ">You increase the speed of the tentacles in her vagina."
    m "Hear that [hermione_name]? Your classmates are starting to realise what a whore you really are."
    her "mmmoo mmmeey mmnnttt"
    m "What's that? Faster?"
    $ cg("01_hp/28_cg/e3.png")
    ">You begin fucking Hermione in earnest"
    her "mmmmm..."
    "The sensation of fucking Hermione in two different holes is almost overwhelming"
    m "I bet you are loving every second of this..."
    m "Being fucked in front of your class mates."
    m "Trying to pretend that you hate it."
    ">You move a ridged tentacle towards her ass"
    her "mm eehh oorr mmmnooo!"
    $ cg("01_hp/28_cg/e4.png")
    ">You enter her tight ass. The feeling of being in every hole at once is incredible."
    her "mmmmmmmm"
    ">Hermione barely manages a groan. She is being overwhelmed by the shear amount of pleasure that she is receiving."
    m "Admit it. You're loving this aren't you."
    m "Being made to cum in front of you classmates like the slut you are."
    m "Go on say it. Tell me what you are."
    her "hmmm aaaaa hhhhhhuuuttt"
    m "What was that I couldn't quite make it out over the sound of you sucking dick."
    her "hmmm aaaaa hhhhhhuuuttt!"
    m "One last time. Say it like you mean it."
    $ cg("01_hp/28_cg/e5.png")
    ">As she goes to exhale you quickly remove the tentacle from her mouth."
    her "{size=+5}I'm a slut!{/size}"
    ">The realisation of what has just occurred hits her like a ton of bricks."
    her "I-I'm cumming... Profes-"
    $ cg("01_hp/28_cg/e6.png")
    ">You quickly reinsert the tentacle into her mouth, silencing her."
    m "Good girl. Time for your reward."
    ">You quicken the pace as she convulses beneath you."
    $ cg("01_hp/28_cg/e7.png")
    ">You explode from sap from nearly every vine. Exploding onto her head and into each of her holes."
    mal "Told you she was a slut."
    fem "I guess you were right..."
    ">You place Hermione back onto the desk as the plant that you are occupying slowly wilts and dies."
    ">Professor Sprout quickly runs over."
    spo "Miss Granger are you okay?"
    her "..."
    spo "Quickly, someone take her to the hospital, and cover her up."
    $ tentacle_cosmetic = False
    hide screen cg
    $ hermione_takes_classes = True
    jump day_main_menu
    


###COSTUME SCENES
label costume_scene_1: #Maid role-play
    call her_main("A costume? What on earth do you need me to dress up for?","body_18")
    m "[hermione_name], have you ever heard of the term role-play?"
    call her_main("role-play?","body_64")
    m "It's where you pretend to be someone you're not."
    call her_main("I gathered that much but why would I want to do that?","body_64")
    m "Because it can be fun!"
    call her_main("Hmmmm. Who would I be role-playing?","body_64")
    m "Well I was thinking seeing as how I purchased you that lovely new cleaning outfit."
    m "You could play the role of my personal maid."
    if whoring < 17:
        call her_main("And how much would this \"personal maid\" be paid?","body_64")
        m "35 points sounds fair."
    call her_main("...","body_64")
    call her_main("Let me go change.","body_64")
    $ stockings = 1
    $ custom_outfit_old = 1
    call her_main("","body_64")
    pause
    call her_main("Well?","body_64")
    m "You certainly look the part. The question is can you act the part?"
    call her_main("Act? I thought you just wanted me to clean your room?","body_64")
    m "Where's the fun in that? If I wanted a clean room, I'd just get those ugly dwarves to do it."
    call her_main("House elfs.","body_64")
    m "Whatever. Anyway I want you to act like a sexy french maid."
    her "Why does it have to be french?"
    m "Must I explain everything?"
    call her_main("Fine...","body_64")
    call her_main("Is there anything you need cleaned today sir?","body_64")
    m "At least try to do the accent."
    call her_main("...","body_64")
    call her_main("Is there anything that you need cleaned today Monsieur?","body_207")
    m "Much better."
    call her_main("Thank you Monsieur.","body_64")
    m "Now as for your cleaning I think that the fireplace could you a good dusting."
    call her_main("As you command Monsieur!","body_64")
    ">Hermione stands on her toes to reach the mantelpiece giving you a lovely view of the top of her stockings."
    m "That's it, just a little higher."
    ">You reach under the desk and start to stroke your cock."
    her "..."
    her "Ooh-la-la, You wouldn't happen to be doing anything naughty under that table would you now Monsieur?"
    m "Of course not mademoiselle, just an itch, now back to cleaning."
    her "Yes yes."
    ">She resumes dusting the mantelpiece, reaching even higher this time."
    ">You can now almost make out the start of her bottom."
    her "Oh my! When was the last time this was cleaned?"
    m "I couldn't say..."
    her "It's so dirty! I will have to put all my effort into this."
    ">She starts making small hops with each dust to reach the top of the books."
    m "That's it. I think you might have missed a spot near the bottom however."
    her "Did I? How about this."
    ">She bends over in front of you, giving you a clear view up her skirt."
    m "That's it."
    ">You erupt underneath your desk, shooting spunk up and over it and onto the floor."
    her "Monsieur! You are so naughty!"
    her "Making a mess as I am cleaning up this filthy filthy room."
    her "At this rate I'll never be done!"
    m "Well you're cleaning was responsible for this mess."
    her "Hmmm, I suppose you are right as always Monsieur, I better start cleaning."
    ">Hermione drops to her knees and starts wiping up your cum."
    her "Such a big mess!"
    ">Hermione cleans up your cum from the floor and table."
    her "Well how did I do?"
    m "Very well indeed! You've taken to role-play like a duck to water."
    m "40 points to Gyrffindor."
    her "Thank you [genie_name]."

