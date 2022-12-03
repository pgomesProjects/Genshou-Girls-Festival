##Free Time Events
##All of the free time events go here


##FREE TIME EVENTS 01#########################################

#Outside
label pond1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if pondSeen == False:
        scene bg pond with dissolve
        call noInteraction from _call_noInteraction
        $ pondSeen = True
    call freeTime from _call_freeTime_4
    return

label field1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if fieldSeen == False:
        scene bg field with dissolve
        $sface = 'neutral'
        show seiko at middle
        menu:
            tut "Would you like to hang out with Seiko?"
            "Yes":
                "I walk out to the field to see Seiko sitting down on the grass."
                "I did say we would hang out during free time. Guess it's better now than never."
                "I tap on her shoulder slightly to get her attention."
                $sface = 'happy'
                show seiko at bounce
                s "Woooooooooooooooooooooooooooo you made it!"
                s "I'm super duper happy you decided to come hang out with lil ol me! Heehee!"
                s "How was class and all of that weird first day junk?"
                "Man, Seiko talks a mile a minute!"
                mc "No problem."
                mc "Class was great, Gym was interesting and fun, I guess."
                $sface = 'flirty'
                show seiko
                "Seiko gives me a smirk, like she has some witty or perverted response to whatever I said.."
                s "Wanna do something that's reeeeally fun?"
                mc "Like what? What would you like to do?"
                "Seiko stands up."
                $sface = 'neutral'
                show seiko
                s 'Well, I am what you call "bored"!'
                s "Boredom suuucks, so I shall alleviate said boredom by being awesome!"
                s "So here's a thing I like to do when I'm really really bored!"
                "I look at Seiko weirdly."
                mc "What do you mean? Get to the point already. No need to make it cryptic."
                "I laugh at her softly."
                $sface = 'happy'
                show seiko
                "Seiko gives me a huge smile."
                s "Wanna hold a screamin' contest?"
                s "I take pride in being super DUPER loud, and want to show off my sexy self!"
                show seiko at bounce
                s "So after I'm done screaming, there'll have to be lines made due to the amount of ladiessss that'll flock over to me! Heehee!"
                s "So you in?"
                "That's certainly a really strange activity. I don't see any practical use for it other than being annoying as all hell."
                "Maybe it's some sort of stress reliever for her?"
                "I look around and see that there are many people out here in the field."
                "What to do..."
                window hide
                menu:
                    "Yeah, Why Not?":
                        "It's whatever. I'll try it to see where this goes."
                        "I imagine my reputation can't get any lower."
                        mc "Yeah, yeah, let's get this over with."
                        $sface = 'neutral'
                        show seiko at bounce
                        s "Sweet! Okay! So here's how this is gonna work!"
                        s "We're gonna treat it like a game!"
                        s "So we'll both scream in turns, and whoever's louder or gathers more attention is the winner of that round!"
                        s "Best of three wins!"
                        "Sounds easy enough, although I'm a little uncomfortable with doing this."
                        mc "Cool. I can do that."
                        "I'm gonna give it a shot anyways. It's open here, so what could go wrong?"
                        s " Alright! You first! Go easy for the first round!"
                        "Alright, deep breaths."
                        "Just let everything out."
                        "After a little bit of hesitation, I let out a loud scream to show I got some vocals."
                        mc "...aaaaaAAAAaaaaah!."
                        "Or semi-loud. Guess that works too."
                        $sface = 'flirty'
                        show seiko
                        "Seiko smirks at me once more. She looks determined."
                        "Without hesitation, she screams herself."
                        scene bg field at vpunch
                        $sface = 'happy'
                        show seiko at middle
                        s "AHHHHHHHHHHHHHHHHH!!!"
                        "I swear, this girl is gonna give me tinnitus some day."
                        "Some heads turn. Some of concern and some of confusion."
                        "A couple inspect the area to make sure no one's in danger."
                        "A small rabbit woman with a dress approaches us directly."
                        rab "Are you two okay? If so, can you cut it out?"
                        mc "Right. Sorry, sorry."
                        "The rabbit girl gives us both a nod and hops off."
                        mc "Yeah, this wasn't the best idea."
                        s "Nonsense! It got some attention, meaning I'm the winner of this round! Heehee!"
                        $sface = 'neutral'
                        show seiko
                        s "Buuuut it does seem that the supervisors are onto us! So instead, we're just gonna do a speed round and call it quits!"
                        mc "Speed round?"
                        s "Yeah! For speed rounds, we're just gonna judge based on volume, and then we're gonna bolt the heck out of here so we don't get in any more trouble!"
                        "That's a really dumb idea."
                        mc "Seiko, that's a really dumb idea."
                        s "I know! But did it feel good to scream in general?"
                        mc "No- wait..."
                        "It...oddly felt nice. Comforting, in a way."
                        "Maybe even liberating just to at least try to scream my feelings out."
                        "I nod slowly at her question."
                        "I kind of do want to do it again, but at the same time, I don't want to get in trouble."
                        "Fuck it, let's just try it. Worst case scenario is the bunny gives us another warning."
                        "My turn again."
                        "Lets see if I got this."
                        scene bg field at vpunch
                        show seiko at middle
                        mc "AHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!"
                        "Seiko gets ready."
                        $sface = 'flirty'
                        show seiko
                        s "You may wanna start lining up! Because the ladies will be flying at me!"
                        scene bg field at vpunch
                        $sface = 'happy'
                        show seiko at middle
                        s "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHHHHHH!!!!!"
                        play sound "audio/sfx/running.wav"
                        hide seiko with dissolve
                        "Seiko is out of breath with how loud she really can scream, but she starts running away from the field."
                        "I follow suit, since of course I don't wanna be in trouble for this too."
                        scene bg outside with dissolve
                        $sface = 'neutral'
                        show seiko
                        s " So I win?"
                        mc "I have to admit that was a really loud scream!"
                        "There are people looking at us from the field with very disapproving looks."
                        "But it was fun. Pretty fun, indeed."
                        s "All that screamin' made me hungry, wanna eat lunch?"
                        mc "Yeah! Lead the way!"
                        "Seiko grabs my arm with both of her right hands and leads me to the side of the building with the cafeteria on it."
                        mc "Head towards the wall! As long as you're holding me, you'll go through too!"
                        play sound "audio/sfx/running.wav"
                        show seiko at running
                        "Seiko nods and starts running towards the cafeteria wall."
                        "I have to time this perfectly."
                        "One...two...jump!"
                        scene bg cafeteria with wipeleft_scene
                        play sound "audio/sfx/table_slam.wav"
                        "I jump through the wall with Seiko attached to me and phase through. I unphase as we land on top of a cafeteria table with a thud."
                        "It's over, for now."
                        $sface = 'happy'
                        show seiko at middle with dissolve
                        s "That was AWESOMEEEEEE!"
                        mc "Yeah, but dangerous. I don't wanna get expelled!"
                        s "You won't! If anythin' I'll take all the blame for it."
                        mc "Really?"
                        $sface = 'neutral'
                        show seiko
                        s "Yeah!"
                        "That's...weirdly relieving in a way."
                        "With eyes on both of us, I crawl off of the table top and act as if nothing happened, going to grab some lunch with Seiko."
                        call changeBar(0.005) from _call_changeBar_4

                    "Maybe At A Different Time":
                        mc "Eh, I'm not really sure that's right now is the right place and time for that."
                        s "Oh come on! It won't be that bad!"
                        mc "I don't think it'll be a good idea. There's a lot of people around at this time."
                        s "BOOOOOOOO!!! Party pooperrrr!"
                        mc "How about another time, alright?"
                        mc "Maybe there will be a time soon that you'll have fun with them...ahem...ladiesssss"
                        "Seiko smiles, composing herself even though she wants to scream."
                        s "Fiiiiiiiiiiiiinnnnnnnnnnneeeee!"
                        s "You promise another time, you'll do it with me though?"
                        mc "Of course. Just, too many people who look like they are studying or reading are here right now."
                        s "Alright! Let's go grab some lunch then!"
                        mc "Alright sounds fun!"
                        s "I bet Azura would love to come along! How about Yasuda?"
                        mc "She's busy with a book. Maybe later."
                        s "Got cha! Let's find Azura!"
                        "Seiko grabs my arms and takes me with her to go search the giant campus for Azura."
                        scene classroom with wipeleft_scene
                        "We find Azura in the study hall downstairs, doing some math homework."
                        "She gets up from her seat."
                        a "Hello."
                        s "Hiya cutie patootie! Wanna get some lunch with us?"
                        a "Oooooooh. Yes. Yes."
                        a "I'm doing homework right now, so maybe food will help me think better for my homework."
                        mc "Sounds like a plan."
                        "Azura grabs her papers and heads with us to the cafeteria. She looks really excited."
                        "Thankfully this is a lot better than getting yelled at for screaming."

                    "That's A Bad Idea":
                        mc "Yeah, no. That's not a good idea."
                        s "Awww, really??"
                        s "Well, if you're not gonna join, I'll start my own game!"
                        s "Watch this!"
                        "Seiko takes a deep breath and before I can stop her, she lets out a scream filled with energy."
                        s "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!"
                        "Jesus Christ."
                        "This is second-hand embarrassment at its finest."
                        mc "Yeah, I get it. You're really darn loud."
                        s "Yup yup! And the ladies lllllove it! Don't cha?"
                        "She looks around at the surrounding students."
                        "For the most part, they either ignore her completely or give a very displeased look."
                        "I feel like I'm gonna melt from all of this embarrassment."
                        s "...tough crowd."
                        s "Anyways, what do youuuu propose we do for funsies?"
                        mc " Now that you screamed and disturbed the peace, how about some lunch?"
                        s " Yeah that's fine! Let's go find Azura and Yasuda for some grub!"
                        mc "Well, Yasuda might be busy with her book."
                        mc "Try texting her or something to see if she's busy."
                        s "Alrighty. I'll do that once we all settle down!"
                        s "I know Azura would totally love to go, though!"
                        "She seems pretty pouty that I didn't join in."
                        "I'm sure she'll be fine, though. She doesn't seem genuinely angry."
                        "If anything, she's a little bummed."
                        "We walk side by side to go rally up our group for some lunch."
                        "Well, at least after everything, I didn't get forced into any weird escapades."
                        call changeBar(-0.005) from _call_changeBar_5

                $ fieldSeen = True
            "No":
                hide seiko with dissolve
                call freeTime from _call_freeTime_1

    return

label shed1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if shedSeen == False:
        scene bg shed with dissolve
        call noInteraction from _call_noInteraction_1
        $ shedSeen = True
    call freeTime from _call_freeTime_5
    return

label garden1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if gardenSeen == False:
        scene bg garden with dissolve
        call noInteraction from _call_noInteraction_2
        $ gardenSeen = True
    call freeTime from _call_freeTime_6
    return

#Basement
label b01_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b01Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_3
        $ b01Seen = True
    call freeTime from _call_freeTime_7
    return

label b02_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b02Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_4
        $ b02Seen = True
    call freeTime from _call_freeTime_8
    return

label b03_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b03Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_5
        $ b03Seen = True
    call freeTime from _call_freeTime_9
    return

label b04_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b04Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_6
        $ b04Seen = True
    call freeTime from _call_freeTime_10
    return

label b05_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b05Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_7
        $ b05Seen = True
    call freeTime from _call_freeTime_11
    return

label b06_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b06Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_8
        $ b06Seen = True
    call freeTime from _call_freeTime_12
    return

label b07_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b07Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_9
        $ b07Seen = True
    call freeTime from _call_freeTime_13
    return

label b08_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b08Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_10
        $ b08Seen = True
    call freeTime from _call_freeTime_14
    return

label b09_Class1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if b09Seen == False:
        scene bg classroom with dissolve
        call noInteraction from _call_noInteraction_11
        $ b09Seen = True
    call freeTime from _call_freeTime_15
    return

label studyHall1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if studyHallSeen == False:
        scene bg classroom with dissolve
        $aface = 'neutral'
        show azura at middle
        menu:
            tut "Would you like to hang out with Azura?"
            "Yes":
                "I walk to the study hall hoping to find something to do."
                "As I walk through the double doors, I spot Azura at one of the tables looking frustrated."
                "Even with those permanent sad eyes, I can tell she's not having the time of her life."
                "I walk over to her, tapping her shoulder lightly."
                "She turns around and I see her working on some math homework."
                mc "What's wrong Azura?"
                a "I need some help with homework."
                a "It's division. They say it's like multiplication..."
                a "...but I am trying my best."
                a "I still do not get it."
                mc "I'm sure you can do it."
                mc " Well first off, how much do you know?"
                a "Multiplication."
                mc " And much schooling do you have in general?"
                a "Well... I have really great hunting skills."
                mc "That's not really school, though."
                a "I'm really good at hunting. The education stuff I am too. But this is new."
                mc "I see, I know you'll get it, eventually. Let me watch you try to do that problem over there."
                "I watch Azura try to do the second problem, 18 divided by 3. But I can tell..."
                "She really doesn't get it!"
                mc "Azura what is the thinking process when you are doing this?"
                "Azura gives me what seems to be a confused look."
                a "Thinking? Process?"
                "She says that in a slow tone."
                "That must mean she really doesn't know what to do when it comes to this kind of stuff."
                "What should I do to help her out?"
                window hide
                menu:
                    "Find A Tutor To Help":
                        mc "Let's head to the advisor center. They might be able to sign you up with a tutor."
                        a "Oooooooh."
                        "Azura stands up and heads out, waiting for me to tag along."
                        "She's pretty darn quick to the elevators, jumping a little bit as she waits for me."
                        scene bg advisors with dissolve
                        "We head to the advisor center and talk to the secretary there."
                        "She looks professional with a suit and tie, alongside fancy glasses."
                        sec "Hello there. How may I assist you?"
                        mc "Hey uh, where would we find tutors for classes?"
                        sec "You will have to fill out a form. Right this way, ladies."
                        "The woman stands from her chair and heads down a thin corridor, her high heels clicking and clacking as she does so."
                        "She leads us to a place full of forms, one specifically labelled \"Tutor Request Form\"."
                        sec "Please fill out the form and we can get you a formal tutor shortly"
                        sec "In the meantime, you may use your computers to get in touch with our eLearning hub to speak to representatives. They will gladly assist you with any problems."
                        "Wow, even though this place is supernatural, it feels like it's run really similarly to actual colleges."
                        "I nod in response."
                        mc "Thank you."
                        "Azura looks on, confused."
                        a "Computer?"
                        mc "Yeah. Do you know how to use those?"
                        a "...no."
                        "Thought so."
                        mc "We'll head to the library. I'll at least show you that."
                        a "Okay. Thank you."
                        mc "Of course. Anything to help you out."
                        "The secretary nods farewell as we depart to the library."
                        scene bg library with wipeleft_scene
                        "We head to the library and log onto a computer."
                        mc "Alright. So this is your computer mouse. You use it to click on the little pictures on the screen."
                        a "Oh. Okay."
                        "I show her everything she needs to know about computers, and thankfully she's pretty quick about it."
                        "Within no time, we're able to get her to log into the school portal and get to the online tutoring section."
                        a "This computer is cool. I like computers."
                        "She seems really happy to learn about the wonderous world of the internet."
                        "Honestly, I don't know how she's been able to get this far in life without using it. It's a bit weird."
                        mc "Do you think you'll be able to get a tutor with this info?"
                        a "Yes. Yes."
                        "I watch as Azura uses the live chat function of the tutoring module."
                        "She slowly types out her problems for the tutor and they send her a bunch of links to articles back in response."
                        a "Oh. What is this?"
                        mc "Those are links. Use the mouse to click them."
                        a "Ooooooh."
                        "Azura clicks all of them and a bunch of sites pop up on basic division."
                        "Azura claps, happy that she has a bunch of new information readily available."
                        a "Yey~"
                        a "I'm going to read these, but there's a lot of words."
                        a "But I'll do my best."
                        "Azura looks conflicted, since she's not the best reader."
                        "Maybe it would've been more beneficial if I helped her out more."
                        "Oh well, at least she's getting the information she needs here."

                    "Seiko Might Be Able To Help":
                        "Seiko is her roommate after all. Might be best to get someone she trusts a lot."
                        "She gave me her number a little while back during our first lunch together, so that'll be useful here."
                        "I text her in hopes to get her attention. She responds right away."
                        s "Whats up cutie?"
                        mc " Nothing  I was wondering if you could help Azura with her homework."
                        s " What kind of homework?"
                        mc "Basic division."
                        s "Sounds good to me, qt"
                        mc " So is that a yes?"
                        s " Yup! Division is ez pz lol"
                        mc "Head to the study hall"
                        s "See u there in a bit."
                        "I turn to Azura after our exchange."
                        mc "Seiko's coming to help."
                        a "Oh. Yey~"
                        "Azura seems excited, bouncing in her seat."
                        "Seiko eventually storms into the study hall, almost slamming the door open."
                        s "So I heard you need some help with MATHHHHHHH?"
                        "There goes Seiko again with the yelling."
                        "One of the supervisors in the classroom sends a hush our way like it was the library."
                        s " Alright let me see what we got here!"
                        "Seiko looks over her homework."
                        s "Oh! This is like, reallllly easy! Mental math stuff!"
                        s "So you take the big number and cut it up a bunch of times by the dividend number thing and then you'll get your answer!"
                        "That...was singlehandedly the worst explanation of division I could think of."
                        "Azura seems to agree, mindlessly staring through Seiko trying to comprehend that."
                        a "Hwuh?"
                        s "Here! Lemme show you!"
                        "Seiko sits right next to Azura."
                        s "Ya got a paper I can use?"
                        if "loose paper" in inventory:
                            mc "I have some in my bag if you want it."
                            s "Perfect, thankies!"
                            call changeBar(0.005) from _call_changeBar_6
                            "Seiko takes the paper and starts to do the math on the paper."
                        else:
                            mc "Sorry, don't have any on me."
                            s "That's fine, I'll just use a pencil so we can erase it!"
                            "Seiko starts doing the math on the side of the paper."
                        s "So, you make this weird little square thing. Big number inside, little number outside!"
                        s "And then, you do 6 times 3 is 18, cuz 6 times 3 is 18!"
                        "Azura sort of seems to get it, sort of doesn't."
                        a "Where did you get the 6 from?"
                        s "6 times 3!"
                        a "I thought we were doing multiplication."
                        s "It's basically the same thing except in a weird way!"
                        "It seems like Seiko is trying her best, but she is definitely not a good teacher in the slightest."
                        "Azura is still confused."
                        s "You can think of multiplication and stuff if you can for these bigger problems and try to remember the patterns of multiplication!"
                        s "Makes sense?"
                        a "Um...I don't know."
                        "Seiko thinks a little bit, since her method of teaching doesn't seem to get through to her."
                        s "Maybe you need to learn a different way! I learn weirdly, so I dunno if my teaching methods will help!"
                        a " I thought you would be a good teacher."
                        s "I could be, buuuut probably not for this!"
                        s "Try getting a tutor or somethin' maybe! That could help!"
                        a "Oh. Okay."
                        "Azura and Seiko pack up their stuff."
                        a "Do you think tutors are good, [p_firstName]?"
                        mc "Uh, yeah, probably."
                        "Azura didn't seem keen on the idea in her voice. I can hear it in her voice."
                        "She didn't really get anywhere here."
                        "The two roommates pack up their stuff and head out to the dorms."
                        call changeBar(0.005) from _call_changeBar_7

                    "I Can Do It":
                        mc "Alright. Let's sit down and do this together."
                        a "Really? You would do that for me?"
                        mc " Of course I will! I'm not just gonna let you struggle."
                        "Azura seems to be very into the homework now that I'm here to help."
                        mc "So you said you know multiplication, right?"
                        a "Yes."
                        mc "Let's test that first, since they're pretty related."
                        mc "4 times 5."
                        a "20."
                        "She answers as soon as I get the numbers out of my mouth."
                        mc "Very good."
                        mc "11 times 12."
                        a "132."
                        "Again, an instant response."
                        mc "Wow, you're really good at this. Let's try something a little harder."
                        mc "34 times 14-{nw}"
                        a "476."
                        "Wait...huh? She didn't even use the paper."
                        "I look it up on my phone real quick."
                        "34 times 14. Yup. 476."
                        "I'm so confused, how did she do that?"
                        mc "...y-yeah. How'd you know that?"
                        a "They say it's called...m-mental math. Yes. Mental math."
                        mc "Jesus Christ..."
                        a "Wh?"
                        mc "Oh, sorry. It's just, that's a really hard problem to do mental math with."
                        a "Oh. Try a really hard problem. I'll try my best."
                        "I'm just dumbfounded. I'm just gonna spit out random numbers and see this."
                        mc "Uh....563...times....64...."
                        "Not an instant response, but she's thinking it out apparently."
                        a "Um...36,032."
                        "I pull up my calculator. Yup. It's correct."
                        "I...don't really have any words really. She's amazing at multiplication."
                        "Then...why does she come off as a little slow? It's strange. Really strange."
                        mc "Y-yeah. You got it."
                        mc "So division is kinda like reverse multiplication."
                        a "Ooooooooh."
                        mc "So you get how 6 times 3 is 18."
                        mc "So for 18 divided by 3, ask yourself how many times you have to add 3 to get 18. And that will be 6."
                        mc "So 18 divided by 3 is 6."
                        a "Ooooh. Okay. Okay, I think I got it."
                        "Azura tried her hand at the problems, starting off a little slow on the first couple."
                        "But quickly she starts to pick up speed."
                        a "4, 2, 7, 4, 0, 11, 5, 9..."
                        "She's getting them all correct..."
                        "But she seems to doubt herself midway through."
                        a "Did I do this right?"
                        mc "Yep. Keep going."
                        "She finishes the paper and hands it to me to check."
                        "Yup, all correct."
                        "Was she faking this or did she really learn {i}that{/i} quickly???"
                        "Either way, I'm really glad it wasn't a big ordeal."
                        "I hate doing math in general."
                        mc "You did great, Azura. I'm proud of you"
                        a "Thank you, [p_firstName]. I understand division much better."
                        mc "I'm really happy that I could help you out!"
                        a "Will you help me if I need it?"
                        mc "Of course I will Azura! I'll be happy to help you out with any assignment if I can."
                        a "Yey~"
                        "Azura seems satisfied with my help."
                        call changeBar(-0.005) from _call_changeBar_8

                $ studyHallSeen = True
            "No":
                hide azura with dissolve
                call freeTime from _call_freeTime_2

    return

#Floor 1
label library1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if librarySeen == False:
        scene bg library with dissolve
        "I enter the library, looking for some books."
        "However, there seems to be a cart full of books that look worn or are donated by students."
        "Might as well give it a shot. Could find something interesting."
        "I head to the bin and look around."
        mc "Hmm...\"Raven's Circle\", huh?"
        "Might be worth the read. I'll take it."
        $ inventory.append("Raven's Circle")
        tut "Raven's Circle added to Backpack."
        $ librarySeen = True

    call freeTime from _call_freeTime_3
    return

label gym1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if gymSeen == False:
        scene bg gym_int with dissolve
        call noInteraction from _call_noInteraction_12
        $ gymSeen = True
    call freeTime from _call_freeTime_16
    return

label lockerRoom1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if lockerRoomSeen == False:
        scene bg lockerroom with dissolve
        call noInteraction from _call_noInteraction_13
        $ lockerRoomSeen = True
    call freeTime from _call_freeTime_17
    return

label cafeteria1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if cafeteriaSeen == False:
        scene bg cafeteria with dissolve
        call noInteraction from _call_noInteraction_14
        $ cafeteriaSeen = True
    call freeTime from _call_freeTime_18
    return

label nurse1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if nurseSeen == False:
        scene bg nurse with dissolve
        call noInteraction from _call_noInteraction_15
        $ nurseSeen = True
    call freeTime from _call_freeTime_19
    return

label advisors1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if advisorsSeen == False:
        scene bg advisors with dissolve
        call noInteraction from _call_noInteraction_16
        $ advisorsSeen = True
    call freeTime from _call_freeTime_20
    return

#Floor 2

label azuraSeikoDorm1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    if azuraSeikoSeen == False:
        scene bg hallways with dissolve
        "{i}Knock Knock.{/i}"
        "Guess no one's inside. Maybe they're somewhere else."
        $ azuraSeikoSeen = True
    call freeTime from _call_freeTime_21

    return

label playerDorm1:
    $ config.rollback_enabled = True
    hide screen schedule_icon with dissolve
    hide screen show_schedule with dissolve
    scene bg playerdorm with dissolve
    "I head back to our dorm to see Yasuda reading her book."
    $yface = 'neutral'
    show yasuda at middle
    y "Hello, did you need anything?"
    mc "Not really, just bored. I don't know what to do."
    y "Well, here's a suggestion from me."

    $ yasudaChoice = 0
    if (rel_meter == 0):
        #Choose a random number between 1 and 2
        $ yasudaChoice = renpy.random.randint(1, 2)

    #If the meter is on Seiko's side, give Azura advice
    if (rel_meter > 0 or yasudaChoice == 1):
        y "I imagine Azura might need help, since classes just started and all."
        y "Maybe it would be best if you tried your hand at helping her."

    #If the meter is on Azura's side, give Seiko advice
    elif (rel_meter < 0 or yasudaChoice == 2):
        y "Seiko seems to be a lot of fun."
        y "I imagine any escapades she's working on right now would be more enjoyable with your presence."

    mc "Alright, thanks."
    $yface = 'happy'
    show yasuda
    y "Certainly."
    $yface = 'neutral'
    hide yasuda with dissolve
    call freeTime
    return

label noInteraction:
    "I enter and take a look around."
    "Hm. Nothing interesting going on right now. I'll look somewhere else."
    return
