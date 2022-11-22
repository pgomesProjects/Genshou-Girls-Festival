define gui.charaters_text_outlines = [ (0, "#00000080", 2, 2) ]

define tut = Character(None, what_color='#59B84F', what_italic=True)

define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#DB7093", who_outlines=[ (1, "#000000") ])
define y = DynamicCharacter('y_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#454046", who_outlines=[ (1, "#000000") ])
define a = DynamicCharacter('a_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#8AA1DE", who_outlines=[ (1, "#000000") ])
define s = DynamicCharacter('s_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#BB1B1E", who_outlines=[ (1, "#000000") ])

define m = DynamicCharacter('m_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#DEBA4D', who_outlines=[ (1, "#000000") ])
define bd = DynamicCharacter('bd_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#283F26', who_outlines=[ (1, "#000000") ])
define om = DynamicCharacter('om_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#283F26', who_outlines=[ (1, "#000000") ])
define k = DynamicCharacter('k_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#E0B73D', who_outlines=[ (1, "#000000") ])
define z = DynamicCharacter('z_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#474747', who_outlines=[ (1, "#000000") ])
define trex = DynamicCharacter('trex_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#4F4331', who_outlines=[ (1, "#000000") ])
define sss = DynamicCharacter('sss_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#72A67C', who_outlines=[ (1, "#000000") ])
define rab = DynamicCharacter('rab_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#E9C1D2', who_outlines=[ (1, "#000000") ])
define sec = DynamicCharacter('sec_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#4B4BBD', who_outlines=[ (1, "#000000") ])

define k = Character('Kyzuki', color='#E0B73D', who_outlines=[ (1, "#000000") ])
define z = Character('Zebra Student', color='#474747', who_outlines=[ (1, "#000000") ])
define trex = Character('T-Rex Student', color='#4F4331', who_outlines=[ (1, "#000000") ])
define sss = Character('Snake Student', color='#72A67C', who_outlines=[ (1, "#000000") ])
define rab =  Character('Rabbit Girl', color='#E9C1D2', who_outlines=[ (1, "#000000") ])
define sec =  Character('Secretary', color='#4B4BBD', who_outlines=[ (1, "#000000") ])

##Bestiary NPCs
define lb = DynamicCharacter('lb_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#0B8080', who_outlines=[ (1, "#000000") ])
define lm = DynamicCharacter('lm_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#D4A35F', who_outlines=[ (1, "#000000") ])
define hl = DynamicCharacter('hl_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#195A32', who_outlines=[ (1, "#000000") ])

##Memory Variables
##
##These are variables that will change the flow of the story
#Outfit
define outfit = ""
default met_helena_at_orientation = None

#Inventory
define inventory = []

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

image azura:
    LiveComposite(
        (675,1000),
        (0,0), im.MatrixColor("actors/azura/bodies/%s.png"%(abody),im.matrix.tint(huer, hueg, hueb)),
        (0,0), im.MatrixColor("actors/azura/faces/%s.png"%(aface),im.matrix.tint(huer, hueg, hueb)),
        )

image seiko:
    LiveComposite(
        (675,1000),
        (0,0), im.MatrixColor("actors/seiko/bodies/%s.png"%(sbody),im.matrix.tint(huer, hueg, hueb)),
        (0,0), im.MatrixColor("actors/seiko/faces/%s.png"%(sface),im.matrix.tint(huer, hueg, hueb)),
        )
