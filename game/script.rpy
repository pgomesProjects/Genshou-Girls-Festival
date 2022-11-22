label start:

    #Define Names
    $ y_name = "British Voice"
    $ a_name = "Blue Woman"
    $ s_name = "Four-Armed Woman"
    $ m_name = "Woman's Voice"
    $ lb_name = "Mysterious Girl"
    $ lm_name = "Quiet Man's Voice"
    $ bd_name = "Bus Driver"
    $ om_name = "Old Man"
    $ hl_name = "Helena"
    $ k_name = "Kyzuki"
    $ z_name = "Zebra Student"
    $ trex_name = "T-Rex Student"
    $ sss_name = "Snake Student"
    $ rab_name = "Rabbit Student"
    $ sec_name = "Secretary"

    call storyTransition
    call ch0_main
    call storyTransition
    call ch1_main
    call storyTransition
    call ch2_main

    tut "END OF DEMO."

    return

label chooseSupplies:

    #ensures the inventory is empty when they choose
    $inventory = []

    #Items left that the paper can choose
    $ Items_Left = 3

    #While you can still pick up items
    while Items_Left > 0:

        $item_word = "Items"
        if Items_Left == 1:
            $item_word = "Item"

        #List of items
        menu:
            tut "Choose [Items_Left] More [item_word]."

            #Can choose pencils if the player doesn't have them already
            "Pencils" if "pencils" not in inventory:
                $ inventory.append("pencils")
                $ Items_Left -= 1

            #Can choose a notebook if the player doesn't have them already
            "Notebook" if "a notebook" not in inventory:
                $ inventory.append("a notebook")
                $ Items_Left -= 1

            #Can choose binders if the player doesn't have them already
            "Binders" if "binders" not in inventory:
                $ inventory.append("binders")
                $ Items_Left -= 1

            #Can choose tape if the player doesn't have them already
            "Tape" if "tape" not in inventory:
                $ inventory.append("tape")
                $ Items_Left -= 1

            #Can choose loose paper if the player doesn't have them already
            "Loose Paper" if "loose paper" not in inventory:
                $ inventory.append("loose paper")
                $ Items_Left -= 1

            #Can choose highlighters if the player doesn't have them already
            "Highlighters" if "highlighters" not in inventory:
                $ inventory.append("highlighters")
                $ Items_Left -= 1

            #Can choose stickers if the player doesn't have them already
            "Stickers" if "stickers" not in inventory:
                $ inventory.append("stickers")
                $ Items_Left -= 1

            #Can choose nothing if the player hasn't picked anything up already
            "Choose Nothing" if len(inventory) == 0:
                $ Items_Left = 0

    #If the player chose nothing
    if len(inventory) == 0:
        "Eh, it’s my first day. They’ll probably supply me if anything."
    #If the player picked three items
    else:
        "I pack my backpack with the essentials: [inventory[0]], [inventory[1]], and [inventory[2]]. I feel pretty confident but my anxiety is through the roof."

    return

label storyTransition:

    scene black with dissolve

    "."
    ".."
    "..."

    return
