## Schedule Overlay
## Toggles the schedule onto the screen whenever the icon is pressed

#Show UI

define toggleSchedule = False

screen schedule_icon:
    imagebutton:
        idle "gui/schedule/schedule_icon.png" xalign 1.0 yalign 0.0
        hover "gui/schedule/schedule_icon_hover.png"
        action ToggleScreen("show_schedule", dissolve)

screen show_schedule:
    add "gui/schedule/schedule_overlay.png"
