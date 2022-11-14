label start:

    #Define Names
    $ m_name = "Woman's Voice"
    $ lb_name = "Mysterious Girl"
    $ lm_name = "Quiet Man's Voice"

    call storyTransition
    call ch0_main

    tut "END OF DEMO."

    return

label storyTransition:

    scene black with dissolve

    "."
    ".."
    "..."

    return
