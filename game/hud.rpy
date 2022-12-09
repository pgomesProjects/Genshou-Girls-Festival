define rel_meter = 0

#Max values for each end
define AZURA_MAX = -5
define SEIKO_MAX = 5

define AZURA_COLOR = Color((138,163,219))
define SEIKO_COLOR = Color((241,217,152))

define prevColor = Color((255,255,255))
define currentColor = Color((255,255,255))

style day:
    size 55

style location:
    size 22

#Show UI
screen in_game_ui:
    fixed:
        add "gui/ui/corner.png"
        vbox:
            xalign 0.01
            yalign 0.007
            $ dayUpper = day.upper()
            $ print(day)
            text "[dayUpper]" style "day"
            null height 10
            text "[currentTime]"
            null height 30
            text "[location]" style "location"

screen relationship_heart:
    zorder 3
    add "gui/ui/relationship_heart.png" xalign 0.01 yalign 0.25 at changeHeart

screen bestiary_popup(name):
    zorder 5
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


#Changes the alpha / color of the heart
label changeColor(changeValue):

    $ rel_meter += changeValue

    if rel_meter > SEIKO_MAX:
        $ rel_meter = SEIKO_MAX

    elif rel_meter < AZURA_MAX:
        $ rel_meter = AZURA_MAX

    $ prevColor = currentColor

    #Currently Yasuda Route
    if rel_meter == 0:
        $ currentColor = Color((255,255,255))

    #Currently Azura Route
    elif rel_meter < 0:
        $ currentColor = Color((255,255,255)).interpolate(AZURA_COLOR, -rel_meter)

    #Current Seiko Route
    elif rel_meter > 0:
        $ currentColor = Color((255,255,255)).interpolate(SEIKO_COLOR, rel_meter)

    hide screen relationship_heart
    show screen relationship_heart

return

transform changeHeart:
    matrixcolor TintMatrix(prevColor)
    linear 0.3 matrixcolor TintMatrix(currentColor)
