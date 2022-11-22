## Free Time Overlay
## Controls the Free Time event functions

define map_floor = 0
define freeTimeNum = 0

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
            hotspot(605, 523, 170, 111) action Call(lockerRoomLoc)
            #Cafeteria
            hotspot(1217, 124, 215, 242) action Call(cafeteriaLoc)
            #Nurse
            hotspot(1217, 373, 126, 145) action Call(nurseLoc)
            #Advisors
            hotspot(1218, 523, 212, 115) action Call(advisorsLoc)
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
