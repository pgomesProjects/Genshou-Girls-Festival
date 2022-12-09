define gui.charaters_text_outlines = [ (0, "#00000080", 2, 2) ]

define tut = Character(None, what_color='#59B84F', what_italic=True)

define mc = DynamicCharacter('player', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#DB7093", who_outlines=[ (1, "#000000") ])
define y = DynamicCharacter('y_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#454046", who_outlines=[ (1, "#000000") ])
define a = DynamicCharacter('a_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#8AA1DE", who_outlines=[ (1, "#000000") ])
define s = DynamicCharacter('s_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color="#BB1B1E", who_outlines=[ (1, "#000000") ])

define m = DynamicCharacter('m_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#DEBA4D', who_outlines=[ (1, "#000000") ])
define bd = DynamicCharacter('bd_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#283F26', who_outlines=[ (1, "#000000") ])
define om = DynamicCharacter('om_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#4B4BBD', who_outlines=[ (1, "#000000") ])
define k = DynamicCharacter('k_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#E0B73D', who_outlines=[ (1, "#000000") ])
define z = DynamicCharacter('z_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#474747', who_outlines=[ (1, "#000000") ])
define trex = DynamicCharacter('trex_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#4F4331', who_outlines=[ (1, "#000000") ])
define rab = DynamicCharacter('rab_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#E9C1D2', who_outlines=[ (1, "#000000") ])
define sec = DynamicCharacter('sec_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#b0b0ff', who_outlines=[ (1, "#000000") ])

##Bestiary NPCs
define lb = DynamicCharacter('lb_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#0B8080', who_outlines=[ (1, "#000000") ])
define lb_bestiary = Mon.Monster('placeholder_portrait.png', 'Libra', 'Professional Tracker', 'After seeing a picture of any person, Libra is able to pinpoint their exact location. While she may be too young to be a faculty member, her ability is too good to not use. In exchange for working with the academy, she is trying to locate her long lost brother.')
define lm = DynamicCharacter('lm_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#D4A35F', who_outlines=[ (1, "#000000") ])
define lm_bestiary = Mon.Monster('placeholder_portrait.png', 'Limil', 'Professional Protector', 'Limil is a changeling, a human raised in a fae household. To save Limil from a life threatening illness, his youngest brother, Wire, consulted Libra\'s older brother and performed [[REDACTED]] to save Limil\'s life. In order to repay the man, Limil has been tasked with protecting Libra at the cost of keeping her older brother\'s name in secrecy.')
define hl = DynamicCharacter('hl_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#195A32', who_outlines=[ (1, "#000000") ])
define hl_bestiary = Mon.Monster('placeholder_portrait.png', 'Helena Ivory', 'Student of Telekinesis', 'Being the oldest sibling in her large family, she ended up getting the responsibility of helping raise them pushed onto her at a young age. She\'s been hardened through having to mature very early on. Initially, she chose to attend the academy to get away from her hectic life, but over the years, she\'s been able to discover herself.')
define ane = DynamicCharacter('ane_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#72A67C', who_outlines=[ (1, "#000000") ])
define ane_bestiary = Mon.Monster('placeholder_portrait.png', 'Anemone Chauveret', 'Student of Hypnotism', 'Anemone is the only child from a first-generation family of people with a snake mutation. As a child, her appearance and ability to hypnotize anyone made her someone people would ostracize. In her teens, she would get in trouble for trying to forcefully hypnotize someone into being her friend, which made the situation even worse.')
define cha = DynamicCharacter('cha_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#f0e9bd', who_outlines=[ (1, "#000000") ])
define cha_bestiary = Mon.Monster('placeholder_portrait.png', 'Charmeine Hale', 'Student of Prayer', 'After being born with an angel mutation, her family soon became religious. She was seen as some kind of prophet, worshipped as a messenger of God. They became too obsessed with her ability to send messages to any deity that she had true faith in, so she ran away from home at an early age.')
define sam = DynamicCharacter('sam_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#87e8db', who_outlines=[ (1, "#000000") ])
define sam_bestiary = Mon.Monster('placeholder_portrait.png', 'Samriti Reilly', 'Student of Memory', 'Samriti is an Indian foreign exchange student, having travelled to come to the reputable academy. She can remember anything that she sees and perfectly replicate the image through art. She wears a blindfold often, so she doesn’t get overwhelmed with having to memorize every minute detail in the world.')
define air = DynamicCharacter('air_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#deae87', who_outlines=[ (1, "#000000") ])
define air_bestiary = Mon.Monster('placeholder_portrait.png', 'Aire Daou', 'Student of Hearing', 'Born with a bat mutation, Aire hears so well that despite being completely blind, she can visualize the world and the shapes around her. She can hear everything within a half mile radius, which has led her to help a lot of people in her community. Many call to question whether she is actually blind or not.')
define elo = DynamicCharacter('elo_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#efb3f2', who_outlines=[ (1, "#000000") ])
define elo_bestiary = Mon.Monster('placeholder_portrait.png', 'Eloise Meyer', 'Professional Regenerator', 'Eloise was the first member of her family to receive the supernatural gene, which made her stand out from the rest. She is able to convert her energy and expel it to regenerate small appendages and minor physical injuries. She’s only had to use her full power once when she cut off the tip of her finger in a cooking accident.')
define chr = DynamicCharacter('chr_name', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", color='#6346ab', who_outlines=[ (1, "#000000") ])
define chr_bestiary = Mon.Monster('placeholder_portrait.png', 'Christine Windsor', 'Professional Oracle', 'Her ability allows her to see up to 15 minutes into the future. As a kid, she used this power for money and ended up becoming very successful from it. As a very recent graduate from H.U.D.A., she decided to dedicate her time as a part-time advisor for the academy and a full-time therapist outside of that.')

##Backgrounds
image bg playerdorm = "bgs/bg playerdorm.png"

##Freetime Variables
image tutorial_floor = "gui/freetime/tutorial_floor.png"
define floor0_spots = []
define floor1_spots = []
define floor2_spots = []
define floor3_spots = []
define currentSpot = ""

#Locations

#Outside
define pondLoc = ""
define pondSeen = False
define fieldLoc = ""
define fieldSeen = False
define shedLoc = ""
define shedSeen = False
define gardenLoc = ""
define gardenSeen = False

#Basement
define classroomLoc = ""
define classroomSeen = False
define studyHallLoc = ""
define studyHallSeen = False

#Floor 1
define libraryLoc = ""
define librarySeen = False
define gymLoc = ""
define gymSeen = False
define lockerRoomLoc = ""
define lockerRoomSeen = False
define cafeteriaLoc = ""
define cafeteriaSeen = False
define nurseLoc = ""
define nurseSeen = False
define advisorsLoc = ""
define advisorsSeen = False

#Floor 2
define commonRoomLoc = ""
define commonRoomSeen = False
define azuraSeikoLoc = ""
define azuraSeikoSeen = False
define playDormLoc = ""

##Memory Variables
##
##These are variables that will change the flow of the story
#Outfit
define objective = "Get comfortable with academy life."
define outfit = ""
default met_helena_at_orientation = None

#Inventory
define inventory = []

default persistent.playername = ""
default player = persistent.playername
default persistent.playthrough = 0
default currentuser = ""

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

    $ day = ""
    $ currentTime = ""
    $ location = ""

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

init python:
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)

    def reset_game():
        persistent._clear(progress=True)
        persistent.playthrough = 0
        renpy.utter_restart()
