##Splashscreen
##
##This is the animation that occurs before the title screen when the game is opened

image warning_screen = "images/warning.jpg"

label splashscreen:

    play music "audio/pptsmain.mp3" fadein 2.0

    $ renpy.pause(1.0, hard='True')

    show warning_screen with dissolve
    $ renpy.pause(2.0, hard='True')

return
