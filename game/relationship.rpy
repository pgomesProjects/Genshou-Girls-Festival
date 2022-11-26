## Relationship Chart
## Draws a dial to the screen and controls how much the dial moves

define rel_meter = 0

#Max values for each end
define AZURA_MAX = -0.05
define SEIKO_MAX = 0.05

image dial = "gui/relationship/dial.png"

style day:
    size 60

#Show UI
screen in_game_ui:
    fixed at slideIn(0.0, 0.3):
        add "gui/ui/corner.png"
        vbox:
            xalign 0.01
            yalign 0.007
            $ dayUpper = day.upper()
            text "[dayUpper]" style "day"
            null height 10
            text "[time]"
            null height 60
            text "[location]"

screen relationship_heart:
    add "gui/ui/relationship_heart.png" xalign 0.01 yalign 0.25

screen bestiary_popup(name):
    fixed at popupWindow:
        add "gui/ui/bestiary_popup.png" xalign 0.5
        vbox:
            xalign 0.5
            yalign 0.03
            text "{size=40}[name]{/size}\nAdded To Bestiary." text_align 0.5

screen objective_popup:
    fixed at showRight:
        add "gui/ui/objective.png" xalign 1.0 yalign 0.15
        vbox:
            xalign 0.98
            yalign 0.165
            text "{size=40}Objective{/size}\n{size=21}[objective]{/size}" text_align 1.0

style day is text

transform slideIn(finalXAlign, sec):
    on show:
        xalign -0.2
        ease sec xalign finalXAlign

transform popupWindow:
    on show:
        ypos -150
        alpha 0.0
        linear 0.2 ypos -30 alpha 0.8
        ease 1 ypos 0 alpha 1.0
        pause 2
        linear 0.2 ypos -150 alpha 0.0
    on hide:
        linear 0.2 ypos -150 alpha 0.0

transform showRight:
    on show:
        xpos 430
        alpha 0.0
        linear 0.2 xpos 0 alpha 1.0
    on hide:
        linear 0.2 xpos 430 alpha 0.0

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
