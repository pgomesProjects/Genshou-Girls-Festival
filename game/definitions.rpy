define gui.charaters_text_outlines = [ (0, "#00000080", 2, 2) ]

define tut = Character(None, what_color='#59B84F', what_italic=True)

define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#DB7093", who_outlines=[ (1, "#000000") ])
define m = DynamicCharacter('m_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#DEBA4D', who_outlines=[ (1, "#000000") ])
define lb = DynamicCharacter('lb_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#0B8080', who_outlines=[ (1, "#000000") ])
define lm = DynamicCharacter('lm_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#D4A35F', who_outlines=[ (1, "#000000") ])

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0

init python:

    #Custom style for important text
    def important_tag(tag, argument, contents):

        return [
                ( renpy.TEXT_TAG, "color=#fcba03"),
            ] + contents + [
                (renpy.TEXT_TAG, "/color"),
            ]

    config.custom_text_tags["important"] = important_tag

##Live Composites for all of the characters
init:
    #Current faces and bodies
    $ aface = 'neutral'
    $ abody = 'apose1'

    $ sface = 'neutral'
    $ sbody = 'spose1'

    $ yface = 'neutral'
    $ ybody = 'ypose1'

    #Hues for images
    $ huer = 1.0
    $ hueg = 1.0
    $ hueb = 1.0

image yasuda:
    LiveComposite(
        (625,1000),
        (0,0), im.MatrixColor("actors/yasuda/bodies/%s.png"%(ybody),im.matrix.tint(huer, hueg, hueb)),
        (0,0), im.MatrixColor("actors/yasuda/faces/%s.png"%(yface),im.matrix.tint(huer, hueg, hueb)),
        )
