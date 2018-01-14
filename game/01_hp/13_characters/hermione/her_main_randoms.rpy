
## Random Mood Expressions for Her_Main ##
############################################

## Neutral ##
label her_main_rndm_neutral: #01(06,45,52), 03,54,82,84,(198),201 #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","body_01") #default look #01,06,45 and 52 are exactly the same!
    elif rndm_one_of_six == 2:
        call her_main("","body_03") #
    elif rndm_one_of_six == 3:
        call her_main("","body_54") #
    elif rndm_one_of_six == 4:
        call her_main("","body_82") #
    elif rndm_one_of_six == 5:
        call her_main("","body_84") #
    elif rndm_one_of_six == 6:
        call her_main("","body_201") #
    return


## Happy ##
label her_main_rndm_happy: #01(06,45,52), 53,54,68,74,84 #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","body_01") #default look #01,06,45 and 52 are exactly the same!
    elif rndm_one_of_six == 2:
        call her_main("","body_53") #sly. naughty
    elif rndm_one_of_six == 3:
        call her_main("","body_54") #look left
    elif rndm_one_of_six == 4:
        call her_main("","body_68") #smile, look left
    elif rndm_one_of_six == 5:
        call her_main("","body_74") #happy eyes
    elif rndm_one_of_six == 6:
        call her_main("","body_84") #confident, look down
    return


## Naughty ##
label her_main_rndm_naughty: #58,59,78,106,111,124,128,129,134,136, #DONE
    $ rndm_one_of_ten = renpy.random.randint(1, 10)
    if rndm_one_of_ten == 1:
        call her_main("","body_58") #
    elif rndm_one_of_ten == 2:
        call her_main("","body_59") #
    elif rndm_one_of_ten == 3:
        call her_main("","body_78") #
    elif rndm_one_of_ten == 4:
        call her_main("","body_106") #
    elif rndm_one_of_ten == 5:
        call her_main("","body_111") #
    elif rndm_one_of_ten == 6:
        call her_main("","body_124") #
    elif rndm_one_of_ten == 7:
        call her_main("","body_128") #
    elif rndm_one_of_ten == 8:
        call her_main("","body_129") #
    elif rndm_one_of_ten == 9:
        call her_main("","body_134") #
    elif rndm_one_of_ten == 10:
        call her_main("","body_136") #
    return


## Naughty w/ Blush ##
label her_main_rndm_naughty_wBlush: #188,200,205,209,213 #DONE
    $ rndm_one_of_five = renpy.random.randint(1, 5)
    if rndm_one_of_five == 1:
        call her_main("","body_188") #look left #+
    elif rndm_one_of_five == 2:
        call her_main("","body_200") #shy + look left #+
    elif rndm_one_of_five == 3:
        call her_main("","body_205") #eyes rolled up #+
    elif rndm_one_of_five == 4:
        call her_main("","body_209") #wink + smile #+
    elif rndm_one_of_five == 5:
        call her_main("","body_213") #naughty #+
    return


## Annoyed ##
label her_main_rndm_annoyed: #12,50,61,69,79(81),83,103,185, #DONE
    $ rndm_one_of_eight = renpy.random.randint(1, 8)
    if rndm_one_of_eight == 1:
        call her_main("","body_12") #
    elif rndm_one_of_eight == 2:
        call her_main("","body_50") #
    elif rndm_one_of_eight == 3:
        call her_main("","body_61") #
    elif rndm_one_of_eight == 4:
        call her_main("","body_69") #
    elif rndm_one_of_eight == 5:
        call her_main("","body_79") #eyes closed
    elif rndm_one_of_eight == 6:
        call her_main("","body_83") #grumpy, look left
    elif rndm_one_of_eight == 7:
        call her_main("","body_103") #annoyed
    elif rndm_one_of_eight == 8:
        call her_main("","body_185") #annoyed
    return


## Annoyed w/ Blush ##
label her_main_rndm_annoyed_wBlush: #182b,184b,191,199,203,208b #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","body_182b") #embarrased, eyes closed
    elif rndm_one_of_six == 2:
        call her_main("","body_184b") #eyes closed
    elif rndm_one_of_six == 3:
        call her_main("","body_191") #angry
    elif rndm_one_of_six == 4:
        call her_main("","body_199") #embarrased, look down
    elif rndm_one_of_six == 5:
        call her_main("","body_203") #annoyed smirk + look left
    elif rndm_one_of_six == 6:
        call her_main("","body_208b") #embarrased
    return


## Angry ##
label her_main_rndm_angry: #05,07,09,12,47(49), 77, #DONE
    $ rndm_one_of_six = renpy.random.randint(1, 6)
    if rndm_one_of_six == 1:
        call her_main("","body_05") #
    elif rndm_one_of_six == 2:
        call her_main("","body_07") #
    elif rndm_one_of_six == 3:
        call her_main("","body_09") #
    elif rndm_one_of_six == 4:
        call her_main("","body_12") #
    elif rndm_one_of_six == 5:
        call her_main("","body_47") #same as 49
    elif rndm_one_of_six == 6:
        call her_main("","body_77") #
    return


## Angry w/ Blush ##
label her_main_rndm_angry_wBlush: #187,191,207,209,213, #DONE
    $ rndm_one_of_five = renpy.random.randint(1, 5)
    if rndm_one_of_five == 1:
        call her_main("","body_187") #angry + teeth
    elif rndm_one_of_five == 2:
        call her_main("","body_191") #angry + teeth
    elif rndm_one_of_five == 3:
        call her_main("","body_207") #angry + teeth
    elif rndm_one_of_five == 4:
        call her_main("","body_209") #wink + smile
    elif rndm_one_of_five == 5:
        call her_main("","body_213") #naughty
    return