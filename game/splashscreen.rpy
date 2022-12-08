##Splashscreen
##
##This is the animation that occurs before the title screen when the game is opened

init python:
    splash_message_default = "This game contains:\nStrong Language\nPlease Play At Your Own Risk."

image white_screen = "#FFFFFF"
image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

label splashscreen:

    $ renpy.music.play(config.main_menu_music)

    $ renpy.pause(1.0, hard='True')

    show white_screen with dissolve
    $ splash_message = splash_message_default
    show splash_warning "[splash_message]" with Dissolve(2.0, alpha=True)
    $ renpy.pause(2.0, hard='True')

    hide white_screen with dissolve

return
