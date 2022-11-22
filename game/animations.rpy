#Makes the character bounce up and down
transform bounce:
    linear 0.1 yalign 1.0
    linear 0.1 yalign 1.2

#Makes the character bounce up and down repeatedly
transform jumping:
    linear 0.3 yalign 1.0
    linear 0.3 yalign 1.2
    repeat

#Makes the character ease in close to the screen
transform hug:
    linear 0.25 zoom 5.0 yalign 0.2

transform unhug:
    linear 0.25 zoom 1.0 yalign 1.2

#Makes the character immediately close to the screen
transform closeup:
    zoom 3.0 yalign 0.2

#Stops any vertical based animations
transform stopAniVertical:
    linear 0.1 yalign 1.0

transform running:
    xalign -0.5 yalign 1.0
    linear 0.6 xalign 1.5

transform sideLeft:
    xalign 0.0 yalign 1.2

transform slightLeft:
    xalign 0.25 yalign 1.2

transform easeInsideLeft:
    linear 0.25 xalign 0.0 yalign 1.2

transform easeInmiddle:
    linear 0.25 xalign 0.5 yalign 1.2

transform easeInsideRight:
    linear 0.25 xalign 1.0 yalign 1.2

transform middle:
    xalign 0.5 yalign 1.2

transform sideRight:
    xalign 1.0 yalign 1.2

#Focus animations
transform focus:
    linear 0.1 zoom 1.05

transform unfocus:
    linear 0.1 zoom 1.0
