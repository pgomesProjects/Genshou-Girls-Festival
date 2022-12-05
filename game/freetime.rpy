## Free Time Overlay
## Controls the Free Time event functions

define map_floor = 0
define freeTimeNum = 0

label freeTimeSetUp:

    #Beginning Set Up
    init python:
        freeTimeNum += 1

        #Outside
        pondLoc = "pond" + str(freeTimeNum)
        fieldLoc = "field" + str(freeTimeNum)
        shedLoc = "shed" + str(freeTimeNum)
        gardenLoc = "garden" + str(freeTimeNum)

        #Basement
        b01Loc = "b01_Class" + str(freeTimeNum)
        b02Loc = "b02_Class" + str(freeTimeNum)
        b03Loc = "b03_Class" + str(freeTimeNum)
        b04Loc = "b04_Class" + str(freeTimeNum)
        b05Loc = "b05_Class" + str(freeTimeNum)
        b06Loc = "b06_Class" + str(freeTimeNum)
        b07Loc = "b07_Class" + str(freeTimeNum)
        b08Loc = "b08_Class" + str(freeTimeNum)
        b09Loc = "b09_Class" + str(freeTimeNum)
        studyHallLoc = "studyHall" + str(freeTimeNum)

        #Floor 1
        libraryLoc = "library" + str(freeTimeNum)
        gymLoc = "gym" + str(freeTimeNum)
        lockerRoomLoc = "lockerRoom" + str(freeTimeNum)
        cafeteriaLoc = "cafeteria" + str(freeTimeNum)
        nurseLoc = "nurse" + str(freeTimeNum)
        advisorsLoc = "advisors" + str(freeTimeNum)

        #Floor 2
        azuraSeikoLoc = "azuraSeikoDorm" + str(freeTimeNum)
        playerDormLoc = "playerDorm" + str(freeTimeNum)

    $ renpy.block_rollback()
    play sound "audio/sfx/fte_start.wav"
    show screen freeTime_ani
    $ renpy.pause(2.4, hard='True')
    hide screen freeTime_ani

    play music "audio/datsflaze_haste.mp3"
    call freeTime

    #After Set Up
    #Outside
    $ pondSeen = False
    $ fieldSeen = False
    $ shedSeen = False
    $ gardenSeen = False

    #Basement
    $ b01Seen = False
    $ b02Seen = False
    $ b03Seen = False
    $ b04Seen = False
    $ b05Seen = False
    $ b06Seen = False
    $ b07Seen = False
    $ b08Seen = False
    $ b09Seen = False
    $ studyHallSeen = False

    #Floor 1
    $ librarySeen = False
    $ gymSeen = False
    $ lockerRoomSeen = False
    $ cafeteriaSeen = False
    $ nurseSeen = False
    $ advisorsSeen = False

    #Floor 2
    $ azuraSeikoSeen = False

    return

label freeTime:
    $ renpy.block_rollback()
    $ renpy.choice_for_skipping()
    $ config.rollback_enabled = False
    $ quick_menu = False

    show screen schedule_icon with dissolve
    call screen freeTime_minimap with dissolve

    return

transform startAni:
    xalign -2.0
    yalign 0.5
    linear 0.7 xalign 0.5
    linear 1.0 xalign 0.5
    linear 0.7 xalign 2.0

screen freeTime_ani:
    text "{size=72}{color=#8566BC}{outlinecolor=#FFFFFF}FREE TIME START{/outlinecolor}{/color}{/size}":
        at startAni

screen freeTime_minimap:
    #Up and down keys
    key "K_UP" action Call("moveUp")
    key "K_DOWN" action Call("moveDown")
    imagemap:
        style_prefix "hotspot"
        ground "gui/freetime/floor[map_floor].png"
        hover "gui/freetime/hover/floor[map_floor]_hover.png"

        if map_floor == 0:
            #Pond
            hotspot(503, 172, 151, 219) action Call(pondLoc)
            #Field
            hotspot(812, 153, 268, 208) action Call(fieldLoc)
            #Shed
            hotspot(1106, 287, 120, 105) action Call(shedLoc)
            #Garden
            hotspot(1302, 183, 90, 167) action Call(gardenLoc)
        if map_floor == 1:
            #B-01
            hotspot(483, 125, 213, 174) action Call(b01Loc)
            #B-02
            hotspot(481, 301, 216, 187) action Call(b02Loc)
            #B-03
            hotspot(481, 495, 219, 243) action Call(b03Loc)
            #B-04
            hotspot(704, 623, 167, 115) action Call(b04Loc)
            #B-05
            hotspot(879, 627, 180, 110) action Call(b05Loc)
            #B-06
            hotspot(1065, 627, 152, 112) action Call(b06Loc)
            #B-07
            hotspot(1225, 502, 207, 234) action Call(b07Loc)
            #B-08
            hotspot(1227, 297, 207, 196) action Call(b08Loc)
            #B-09
            hotspot(1226, 123, 205, 168) action Call(b09Loc)
            #Study Hall
            hotspot(838, 236, 245, 246) action Call(studyHallLoc)
        if map_floor == 2:
            #Library
            hotspot(606, 126, 169, 164) action Call(libraryLoc)
            #Gym
            hotspot(504, 296, 269, 218) action Call(gymLoc)
            #Lockerroom
            hotspot(605, 523, 170, 111) action Call(lockerRoomLoc), SetVariable("quick_menu", True)
            #Cafeteria
            hotspot(1217, 124, 215, 242) action Call(cafeteriaLoc), SetVariable("quick_menu", True)
            #Nurse
            hotspot(1217, 373, 126, 145) action Call(nurseLoc), SetVariable("quick_menu", True)
            #Advisors
            hotspot(1218, 523, 212, 115) action Call(advisorsLoc), SetVariable("quick_menu", True)
        if map_floor == 3:
            #AzuraSeikoDorm
            hotspot(779, 426, 42, 103) action Call(azuraSeikoLoc)
            #PlayerDorm
            hotspot(1078, 429, 58, 96)action Call(playerDormLoc)

    if map_floor == 0:
        if len(floor0_spots) != 0:
            for i in range(0, len(floor0_spots)):
                $currentSpot = floor0_spots[i]
                add "[currentSpot]" xalign 0.0 yalign 0.0

    if map_floor == 1:
        if len(floor1_spots) != 0:
            for i in range(0, len(floor1_spots)):
                $currentSpot = floor1_spots[i]
                add "[currentSpot]" xalign 0.0 yalign 0.0

    if map_floor == 2:
        if len(floor2_spots) != 0:
            for i in range(0, len(floor2_spots)):
                $currentSpot = floor2_spots[i]
                add "[currentSpot]" xalign 0.0 yalign 0.0

    if map_floor == 3:
        if len(floor3_spots) != 0:
            for i in range(0, len(floor3_spots)):
                $currentSpot = floor3_spots[i]
                add "[currentSpot]" xalign 0.0 yalign 0.0
label moveUp:
    play sound "gui/sfx/smghover.wav"
    if map_floor != 3:
        $ map_floor += 1
    else:
        $ map_floor = 0

    hide screen freeTime_minimap
    call screen freeTime_minimap


    return

label moveDown:
    play sound "gui/sfx/smghover.wav"
    if map_floor != 0:
        $ map_floor -= 1
    else:
        $ map_floor = 3

    hide screen freeTime_minimap
    call screen freeTime_minimap

    return
