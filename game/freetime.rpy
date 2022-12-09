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
        classroomLoc = "classroom" + str(freeTimeNum)
        studyHallLoc = "studyHall" + str(freeTimeNum)

        #Floor 1
        libraryLoc = "library" + str(freeTimeNum)
        gymLoc = "gym" + str(freeTimeNum)
        lockerRoomLoc = "lockerRoom" + str(freeTimeNum)
        cafeteriaLoc = "cafeteria" + str(freeTimeNum)
        nurseLoc = "nurse" + str(freeTimeNum)
        advisorsLoc = "advisors" + str(freeTimeNum)

        #Floor 2
        commonRoomLoc = "commonRoom" + str(freeTimeNum)
        azuraSeikoLoc = "azuraSeikoDorm" + str(freeTimeNum)
        playerDormLoc = "playerDorm" + str(freeTimeNum)

    $ renpy.block_rollback()
    $ config.allow_skipping = False
    $ quick_menu = False
    $renpy.music.stop()
    play sound "audio/sfx/fte_start.wav"
    show screen freeTime_ani
    $ renpy.pause(2.4, hard='True')
    hide screen freeTime_ani

    $ config.allow_skipping = True
    play music "audio/datsflaze_haste.mp3"
    call freeTime from _call_freeTime

    #After Set Up
    #Outside
    $ pondSeen = False
    $ fieldSeen = False
    $ shedSeen = False
    $ gardenSeen = False

    #Basement
    $ classroomSeen = False
    $ studyHallSeen = False

    #Floor 1
    $ librarySeen = False
    $ gymSeen = False
    $ lockerRoomSeen = False
    $ cafeteriaSeen = False
    $ nurseSeen = False
    $ advisorsSeen = False

    #Floor 2
    $ commonRoomSeen = False
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

label freeTimeEventSetup:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    $ quick_menu = True

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
    zorder -1
    add "gui/freetime/freetime_background.png"

    #Up and down keys
    key "K_UP" action Call("moveUp")
    key "K_DOWN" action Call("moveDown")
    imagemap:
        style_prefix "hotspot"
        ground "gui/freetime/floor[map_floor].png"
        hover "gui/freetime/hover/floor[map_floor]_hover.png"

        if map_floor == 0:
            #Pond
            hotspot (30,330,197,225) action Call(pondLoc)
            #Field
            hotspot (576,351,328,180) action Call(fieldLoc)
            #Shed
            hotspot (1348,613,98,128) action Call(shedLoc)
            #Garden
            hotspot (1146,315,305,268) action Call(gardenLoc)
        if map_floor == 1:
            #Study Hall
            hotspot (557,630,360,154) action Call(studyHallLoc)
            #Classroom
            hotspot (377,639,37,57) action Call(classroomLoc)
        if map_floor == 2:
            #Library
            hotspot (238,375,191,264) action Call(libraryLoc)
            #Gym
            hotspot (236,638,193,211) action Call(gymLoc)
            #Lockerroom
            hotspot (234,849,195,57) action Call(lockerRoomLoc)
            #Cafeteria
            hotspot (902,782,343,129) action Call(cafeteriaLoc)
            #Nurse
            hotspot (1172,613,73,171) action Call(nurseLoc)
            #Advisors
            hotspot (936,418,174,160) action Call(advisorsLoc)
        if map_floor == 3:
            #Common Room
            hotspot (932,418,172,160) action Call(commonRoomLoc)
            #AzuraSeikoDorm
            hotspot (1161,686,47,42) action Call(azuraSeikoLoc)
            #PlayerDorm
            hotspot (1157,759,54,43) action Call(playerDormLoc)

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

    vbox:
        style_prefix "btns"
        xalign 0.97
        yalign 0.8

        textbutton "Dorms" action SetVariable("map_floor", 3)
        null height 10
        textbutton "Main Floor" action SetVariable("map_floor", 2)
        null height 10
        textbutton "Underground" action SetVariable("map_floor", 1)
        null height 10
        textbutton "Outside" action SetVariable("map_floor", 0)

style btns_button:
    xysize (355, 140)
    background "gui/freetime/freetime_button_idle.png"
    hover_background "gui/freetime/freetime_button_hover.png"

style btns_button_text:
    xalign 0.5
    color "#FFFFFF"
    font "fonts/Merriweather-Regular.otf"

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
