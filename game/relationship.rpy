## Relationship Chart
## Draws a dial to the screen and controls how much the dial moves

define rel_meter = 0

#Max values for each end
define AZURA_MAX = -0.05
define SEIKO_MAX = 0.05

image dial = "gui/relationship/dial.png"

#Show UI
screen relationship_bar():
    add "gui/relationship/relationship.png" xalign 0.0 yalign 0.0
    add "gui/relationship/dial.png" at moveDial
    text "{color=#8AA1DE}Azura{/color}":
        at transform:
            align (0.01, 0.001) alpha 1.0
    text "{color=#BB1B1E}Seiko{/color}":
        at transform:
            align (0.105, 0.001) alpha 1.0


#Changes the position of the dial
label changeBar(changeValue):

    $ rel_meter += changeValue

    if rel_meter > SEIKO_MAX:
        $rel_meter = SEIKO_MAX

    elif rel_meter < AZURA_MAX:
        $rel_meter = AZURA_MAX

    hide screen relationship_bar
    show screen relationship_bar

return

transform moveDial:
    linear 0.3 xpos rel_meter
