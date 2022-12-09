##Free Time Events
##All of the free time events go here


##FREE TIME EVENTS 01#########################################

##Variables
init:
    $ artSuppliesNeeded = False
    $ q1_asked = False
    $ q2_asked = False
    $ q3_asked = False

#Outside
label pond1:
    call freeTimeEventSetup from _call_freeTimeEventSetup
    if pondSeen == False:
        scene bg pond with dissolve
        $ location = "Pond"
        show screen in_game_ui
        "I take a look at the academy's pond."
        "It's kind of small, but seems perfect for swimming on a hot day."
        "Maybe people with water-related superpowers would go here."
        "That'd be pretty awesome to see."
        "I take a deeper look into the water to see if I can spot any fish."
        "..."
        "Nope, nothing."
        "Not much I can do here other than look."
        "Before I leave, however, I decide to take a small stone from the ground and try to skip it over the water."
        "I get maybe a skip and a half before it plops into the water."
        "Guess I still suck at doing that."
        $ pondSeen = True
    call freeTime from _call_freeTime_2
    return

label field1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_1
    if fieldSeen == False:
        scene bg field with dissolve
        $ location = "Field"
        show screen in_game_ui
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
                        $sface = 'scream'
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
                        $sface = 'scream'
                        show seiko at middle
                        s "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH HHHHHHHHHHHHHHHHHHHHHHHH!!!!!"
                        play sound "audio/sfx/running.wav"
                        hide seiko with dissolve
                        "Seiko is out of breath with how loud she really can scream, but she starts running away from the field."
                        "I follow suit, since of course I don't wanna be in trouble for this too."
                        scene bg outside with dissolve
                        $ location = "Outside"
                        show screen in_game_ui
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
                        $ location = "Cafeteria"
                        show screen in_game_ui
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
                        call changeColor(0.5) from _call_changeColor

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
                        $ location = "Classroom"
                        show screen in_game_ui
                        show seiko at middle with dissolve
                        "We find Azura in the study hall downstairs, doing some math homework."
                        "She gets up from her seat."
                        show azura at sideRight with dissolve
                        show azura at focus zorder 2
                        a "Hello."
                        show azura at unfocus zorder 0
                        show seiko at focus zorder 2
                        s "Hiya cutie patootie! Wanna get some lunch with us?"
                        show seiko at unfocus zorder 0
                        show azura at focus zorder 2
                        a "Oooooooh. Yes. Yes."
                        a "I'm doing homework right now, so maybe food will help me think better for my homework."
                        show azura at unfocus zorder 0
                        mc "Sounds like a plan."
                        "Azura grabs her papers and heads with us to the cafeteria. She looks really excited."
                        "Thankfully this is a lot better than getting yelled at for screaming."

                    "That's A Bad Idea":
                        mc "Yeah, no. That's not a good idea."
                        s "Awww, really??"
                        s "Well, if you're not gonna join, I'll start my own game!"
                        s "Watch this!"
                        "Seiko takes a deep breath and before I can stop her, she lets out a scream filled with energy."
                        scene bg field at vpunch
                        $sface = 'scream'
                        show seiko at middle
                        s "AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!"
                        "Jesus Christ."
                        "This is second-hand embarrassment at its finest."
                        mc "Yeah, I get it. You're really darn loud."
                        $sface = 'flirty'
                        show seiko
                        s "Yup yup! And the ladies lllllove it! Don't you?"
                        "She looks around at the surrounding students."
                        "For the most part, they either ignore her completely or give a very displeased look."
                        "I feel like I'm gonna melt from all of this embarrassment."
                        $sface = 'neutral'
                        show seiko
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
                        call changeColor(-0.5) from _call_changeColor_1

                $ fieldSeen = True
            "No":
                hide seiko with dissolve
                call freeTime from _call_freeTime_1

    return

label shed1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_2
    if shedSeen == False:
        scene bg shed with dissolve
        $ location = "Shed"
        show screen in_game_ui
        "It's seems to just be a shed full of random supplies."
        "Not much I can really do here."
        $ shedSeen = True
    if artSuppliesNeeded == True:
        if "Art Supplies" not in inventory:
            "Pretty sure this is the shed where supplies are stored."
            "I can probably find the stuff Samriti and the bat girl needs for their painting."
            "..."
            "..."
            "Fan brushes, paint thinner, Van Dyke brown paint. Got it."
            $ inventory.append("Art Supplies")
            tut "Art Supplies added to Backpack."
    call freeTime from _call_freeTime_4
    return

label garden1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_3
    if gardenSeen == False:
        scene bg garden with dissolve
        $ location = "Garden"
        show screen in_game_ui
        "I'm surprised that no one else is here."
        "Personally, I really like these kind of secluded spaces."
        "Nothing beats a bedroom, but these kind of lonely, open air places are a close second."
        "I take a seat on a boulder barely large enough to hold my size."
        "You know, sometimes it's great to just sit down and do absolutely nothing."
        "Instead of listening to my thoughts, I can listen to the rustling of the trees."
        "The muffled sounds of people chatting far, far away."
        "I can't remember the last time I had a \"secret spot\", but maybe I can make this one."
        "I just get the feeling that nobody really comes here."
        "Even though this place is pretty well maintained, but let's not sweat the details."
        "I close my eyes and let the sounds of nature speak to me."
        $renpy.music.stop(fadeout = 1.0)
        scene black with dissolve
        "..."
        "..."
        "..."
        scene bg garden with dissolve
        if "a notebook" in inventory and "pencils" in inventory:
            "You know what?"
            "I have my notebook and pencils on me."
            "Might as well keep my mind busy for a little bit."
            tut "Side Quest: My Personal Therapy - Started"
            "I take out my notebook and pencils from my backpack and start to draw."
            "I'm no artist, but I like to doodle what's on my mind every now and then."
            "Now seems like one of those times, and the garden seems like the perfect subject."
            "I make tons of scribbles on a piece of paper."
            "I try to replicate the shapes of the yellow tulips, the collection of leaves on the ground, the trees towering around me in pretty much every direction."
            "The final product though barely ends up looking like a garden."
            "Picasso would be proud at how abstract this \"drawing\" looks."
            "Oh well, at least that killed some time."
            tut "Side Quest: My Personal Therapy - Completed"
            $ inventory.append("Drawing of the Garden")
            tut "Drawing of the Garden added to Backpack."
        else:
            "Well, that was nice."

        play music "audio/datsflaze_haste.mp3"
        $ gardenSeen = True
    call freeTime from _call_freeTime_5
    return

#Underground
label classroom1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_4
    if classroomSeen == False:
        scene bg classroom with dissolve
        $ location = "Classroom"
        show screen in_game_ui
        if artSuppliesNeeded == False:
            "I take a look into one of the classrooms with the door slightly ajar."
            "There's a young lady with a blindfold painting a very beautiful portrait of a bat woman on a couch."
            "I could only ever dream of painting that well, nevermind with a blindfold."
            "I try to sneak a peek into the room some more, only to accidentally bump the door."
            "Hopefully they don't notice."
            "..."
            "..."
            "Shit, they totally noticed."
            "They look straight in my direction as I contemplate phasing through the wall behind me."
            sam "Come in."
            "The woman speaks with a very distinct Indian accent."
            "The other girl looks in my direction with a smile and very cloudy eyes."
            mc "Uh...hi."
            air "Welcome!"
            air "Don't mind us, Sammy's just doing some painting."
            $ sam_name = "Sammy?"
            sam "For the last time, stop calling me that."
            air "But it's cute!"
            "The blindfolded woman, apparently named something similar to Sammy, is probably rolling her eyes."
            sam "Anyways, since you decided to intrude, young lady, would you mind doing us a favor?"
            mc "Sure, what do you need?"
            sam "Do you mind getting me some supplies from the shed?"
            sam "I need them to finish this painting."
            mc "I can do that, what do you need?"
            sam "Just a couple fan brushes, some Van Dyke brown paint, and some more paint thinner, if you could."
            mc "Yeah, totally."
            air "Awesome! Thanks a bunch!"
            air "I can't wait to see your painting when it's done, Sammy!"
            $ sam_name = "Samriti"
            sam "It's Samriti."
            sam "Nonetheless, I still don't know how you see my paintings."
            "Samriti gives a small smile in the bat girl's direction."
            air "Don't you underestimate my power!"
            air "I'm not bluffing when I say I can hear the colors, you know that."
            sam "Yes, yes. But still, I can't even begin to comprehend that."
            "She turns back to me."
            sam "Anyways, young miss, just get those supplies to us as soon as you can."
            mc "Got it."
            tut "Side Quest: The Blind Painter - Started"
            $ artSuppliesNeed = True
        else:
            if "Art Supplies" in inventory:
                "The bat woman raises her head as I enter the door."
                air "Oh hey, you got it!"
                "Samriti stands up, wiping some excess paint off of a paint brush onto a palette."
                sam "Just place them down next to me."
                "I do as she asks."
                $ inventory.remove("Art Supplies")
                tut "Art Supplies removed from Backpack."
                sam "Thank you. I should be able to finish this painting now."
                sam "What is your name?"
                mc "[player]."
                sam "My name is Samriti Reilly, as you might have heard earlier."
                sam "Thank you, [player]. Your snooping was very convenient for us."
                $air_name = "Aire"
                air "I'm Aire Daou, Samriti's girlfriend!"
                air "We're both second years!"
                "Samriti blushes at the word \"girlfriend\"."
                mc "Nice to meet you two. I'm gonna continue wandering around though."
                sam "Take care."
                air "See ya!"
                python:
                    if(AddToBestiary(sam_bestiary) and AddToBestiary(air_bestiary)):
                        renpy.show_screen("bestiary_popup", name="Samriti and Aire")
                tut "Side Quest: The Blind Painter - Completed"
                sam "Oh, and take this."
                $ inventory.append("Art Brush Pin")
                tut "Art Brush Pin added to Backpack."
                $ classroomSeen = True
            else:
                sam "Let us know when you get the supplies."
                air "Take all the time you need, sweetheart."

        $ artSuppliesNeeded = True
    call freeTime from _call_freeTime_6
    return

label studyHall1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_5
    if studyHallSeen == False:
        scene bg studyhall with dissolve
        $ location = "Study Hall"
        show screen in_game_ui
        $aface = 'neutral'
        show azura at middle
        menu:
            tut "Would you like to hang out with Azura?"
            "Yes":
                "I walk to the study hall hoping to find something to do."
                "As I walk through the double doors, I spot Azura at one of the tables trying to look frustrated."
                "Even with those permanent sad eyes, I can tell she's not having the time of her life."
                "I walk over to her, tapping her shoulder lightly."
                "She turns around and I see her working on some math homework."
                mc "What's wrong Azura?"
                a "I need some help with homework."
                a "It's division. They say it's like multiplication..."
                a "...but I am trying my best."
                a "I still do not get it."
                mc "I'm sure you can do it."
                mc "Well first off, how much do you know?"
                a "Multiplication."
                mc "...how much schooling do you have in general?"
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
                "I'm not sure what I can do to help her out."
                window hide
                menu:
                    "Find A Tutor To Help":
                        mc "Let's head to the advisor center. They might be able to sign you up with a tutor."
                        a "Oooooooh."
                        "Azura stands up and heads out, waiting for me to tag along."
                        "She's pretty darn quick to the elevators, jumping a little bit as she waits for me."
                        scene bg advisors with dissolve
                        $ location = "Advising Center"
                        show screen in_game_ui
                        "We head to the advisor center and talk to the secretary there, since the actual advisor seems to be busy."
                        "She looks professional with a suit and tie, alongside fancy glasses."
                        sec "Hello there. How may I assist you?"
                        mc "Hey uh, where would we find tutors for classes?"
                        sec "You will have to fill out a form. Right this way, ladies."
                        "The woman stands from her chair and heads down a thin corridor, her high heels clicking and clacking as she does so."
                        "She leads us to a place full of forms, one specifically labelled \"Tutor Request Form\"."
                        sec "Please fill out the form and we can get you a formal tutor shortly."
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
                        $ location = "Library"
                        show screen in_game_ui
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
                        $ aface = "excited"
                        show azura
                        a "Ooooooh."
                        "Azura clicks all of them and a bunch of sites pop up on basic division."
                        "Azura claps, happy that she has a bunch of new information readily available."
                        a "Yey~"
                        $ aface = "neutral"
                        show azura
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
                        $ sface = "scream"
                        show seiko at sideRight with dissolve
                        show seiko at focus zorder 2
                        s "So I heard you need some help with MATHHHHHHH?"
                        show seiko at unfocus zorder 0
                        "There goes Seiko again with the yelling."
                        "One of the supervisors in the classroom sends a hush our way like it was the library."
                        show seiko at focus zorder 2
                        s " Alright let me see what we got here!"
                        show seiko at unfocus zorder 0
                        "Seiko looks over her homework."
                        show seiko at focus zorder 2
                        s "Oh! This is like, reallllly easy! Mental math stuff!"
                        s "So you take the big number and cut it up a bunch of times by the dividend number thing and then you'll get your answer!"
                        show seiko at unfocus zorder 0
                        "That...was singlehandedly the worst explanation of division I could think of."
                        "Azura seems to agree, mindlessly staring through Seiko trying to comprehend that."
                        show azura at focus zorder 2
                        a "Hwuh?"
                        show azura at unfocus zorder 0
                        show seiko at focus zorder 2
                        s "Here! Lemme show you!"
                        show seiko at unfocus zorder 0
                        "Seiko sits right next to Azura."
                        show seiko at focus zorder 2
                        s "Ya got a paper I can use?"
                        show seiko at unfocus zorder 0
                        if "loose paper" in inventory:
                            mc "I have some in my bag if you want it."
                            $ sface = "happy"
                            show seiko at focus zorder 2
                            s "Perfect, thankies!"
                            call changeColor(0.5) from _call_changeColor_2
                            $ sface = "neutral"
                            show seiko at unfocus zorder 0
                            "Seiko takes the paper and starts to do the math on the paper."
                        else:
                            mc "Sorry, don't have any on me."
                            show seiko at focus zorder 2
                            s "That's fine, I'll just use a pencil so we can erase it!"
                            show seiko at unfocus zorder 0
                            "Seiko starts doing the math on the side of the paper."
                        show seiko at focus zorder 2
                        s "So, you make this weird little square thing. Big number inside, little number outside!"
                        s "And then, you do 6 times 3 is 18, cuz 6 times 3 is 18!"
                        show seiko at unfocus zorder 0
                        "Azura sort of seems to get it, sort of doesn't."
                        show azura at focus zorder 2
                        a "Where did you get the 6 from?"
                        show azura at unfocus zorder 0
                        show seiko at focus zorder 2
                        s "6 times 3!"
                        show seiko at unfocus zorder 0
                        show azura at focus zorder 2
                        a "I thought we were doing division."
                        show azura at unfocus zorder 0
                        show seiko at focus zorder 2
                        s "It's basically the same thing except in a weird way!"
                        show seiko at unfocus zorder 0
                        "It seems like Seiko is trying her best, but she is definitely not a good teacher in the slightest."
                        "Azura is still confused."
                        show seiko at focus zorder 2
                        s "You can think of multiplication and stuff for these bigger problems and like, just try to remember the patterns!"
                        s "Makes sense?"
                        show seiko at unfocus zorder 0
                        show azura at focus zorder 2
                        a "Um...I don't know."
                        show azura at unfocus zorder 0
                        "Seiko thinks a little bit, since her method of teaching doesn't seem to get through to her."
                        show seiko at focus zorder 2
                        s "Maybe you need to learn a different way! I learn weirdly, so I dunno if my teaching methods will help!"
                        show seiko at unfocus zorder 0
                        show azura at focus zorder 2
                        a "I thought you would be a good teacher."
                        show azura at unfocus zorder 0
                        show seiko at focus zorder 2
                        s "I could be, buuuut probably not for this!"
                        s "Try getting a tutor or somethin' maybe! That could help!"
                        show seiko at unfocus zorder 0
                        show azura at focus zorder 2
                        a "Oh. Okay."
                        show azura at unfocus zorder 0
                        "Azura and Seiko pack up their stuff."
                        show azura at focus zorder 2
                        a "Do you think tutors are good, [player]?"
                        show azura at unfocus zorder 0
                        mc "Uh, yeah, probably."
                        "Azura didn't seem keen on the idea in her voice. I can hear it in her voice."
                        "She didn't really get anywhere here."
                        "The two roommates pack up their stuff and head out to the dorms."
                        call changeColor(0.5) from _call_changeColor_3

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
                        a "Thank you, [player]. I understand division much better."
                        mc "I'm really happy that I could help you out!"
                        a "Will you help me if I need it?"
                        mc "Of course I will Azura! I'll be happy to help you out with any assignment if I can."
                        $ aface = "excited"
                        show azura
                        a "Yey~"
                        "Azura seems satisfied with my help."
                        $ aface = "neutral"
                        call changeColor(-0.5) from _call_changeColor_4

                $ studyHallSeen = True
            "No":
                hide azura with dissolve
                call freeTime from _call_freeTime_7

    return

#Floor 1
label library1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_6
    if librarySeen == False:
        scene bg library with dissolve
        $ location = "Library"
        show screen in_game_ui
        "I enter the library, looking for something interesting to read."
        "Might as well give it a shot. Could find something interesting."
        tut "Side Quest: A Good Story - Started"
        "I head straight to the young adult section looking for some manga."
        "I'm sure they have at least some."
        "I look through the shelves until I can see any familiar illustrations on the spines of the books."
        "There's some manga here, but I've either read them already, or they're just old titles that I don't really want to bother with."
        "Personally, I'm an isekai or a slice of life kind of person."
        "Anything that can take me to a world that's far away from this one."
        "After some time of going up and down the shelves, I'm about ready to call it quits."
        "However, there seems to be a cart full of books that look worn or are donated by students near the front."
        "I head over to the bin and look around."
        "Usually you can find hidden gems in places like these."
        mc "Hmm...\"Raven's Circle\", huh?"
        "Might be worth the read. I'll take it."
        tut "Side Quest: A Good Story - Completed"
        $ inventory.append("Raven's Circle")
        tut "Raven's Circle added to Backpack."
        $ librarySeen = True

    call freeTime from _call_freeTime_3
    return

label gym1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_7
    if gymSeen == False:
        scene bg gym_int with dissolve
        $ location = "Gym"
        show screen in_game_ui
        call noInteraction from _call_noInteraction_12
        $ gymSeen = True
    call freeTime from _call_freeTime_16
    return

label lockerRoom1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_8
    if lockerRoomSeen == False:
        scene bg lockerroom with dissolve
        $ location = "Locker Rooms"
        show screen in_game_ui
        call noInteraction from _call_noInteraction_13
        $ lockerRoomSeen = True
    call freeTime from _call_freeTime_17
    return

label cafeteria1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_9
    if cafeteriaSeen == False:
        scene bg cafeteria with dissolve
        $ location = "Cafeteria"
        show screen in_game_ui
        "No time better than now to grab a bite to eat."
        "I decide to check out the cafeteria, hoping that they serve at least somewhat edible food."
        "Back in high school, I'm pretty sure I found mold in my pizza once."
        "I head into the back where all the hustle and bustle is going on."
        "Looks to be a very standard buffet style of salads, soups, meats, and whatever else."
        "I don't smell anything questionable, so I think I should be okay."
        "I decide to grab a grill cheese sandwich and some \"Jasmine Rice\", according to the little label on top."
        "Before I make my way out, I see a familiar face trying to blend into the crowd."
        "It's a bit hard for her though, since she has such a large snake tail."
        "It's that snake girl from my Normal Gym class."
        "She looks just about ready to cry, her eyes darting around frantically."
        "I can relate, definitely been there before."
        "...you know what? I'll try to help her."
        tut "Side Quest: First Day Jitters - Started"
        "I put my plate in one hand and wander over to the strange, shy girl."
        "I tap the table next to her to get her attention."
        ane "Hm?"
        mc "Hey, wanna eat together?"
        ane "Oh, you're that phassssssing girl from gym!"
        ane "That'd be fine, thank you."
        "She looks at me with a weak smile and follows me to a small table."
        ane "You're [player], right?"
        mc "Yep. Glad you remembered."
        mc "What's your name?"
        $ane_name = "Anemone"
        ane "It'sssss Anemone."
        ane "My name isss a bit weird, but mom gave it to me, ssssso..."
        mc "I think it's pretty. Haven't heard it before."
        mc "So, are you new to this academy also?"
        ane "Yep, although I didn't really want to come here."
        ane "Sssssschoolss kind of make me uncomfortable."
        mc "Why's that?"
        "Anemone goes quiet, taking a bite of some fish before she decides to answer."
        ane "It'ssss jusssst that people like to ssssstare and call me weird."
        ane "It makes me feel like I'm not human."
        mc "Well, you look pretty human to me."
        mc "Just uh...very snake-y, too."
        ane "I um...don't really want to be sssssseen assss a sssssnake."
        "Anemone takes another bite of her food, but a single tear rolls down her right eye."
        ane "I'm just a girl."
        ane "A normal girl."
        ane "My {important}mutation{/important} doesn't make me any lesssss human."
        mc "...I see."
        "Man, I guess she has it pretty hard."
        "Thankfully in my family, we can hide our abilities pretty well."
        "For people like Anemone, Azura, and Seiko, they can't really hide how they were born."
        "I won't really pry since I just met her, but I can sympathize."
        mc "Well, you're a really nice girl, Anemone. No matter what you look like."
        ane "Oh. Well, thank you. Really."
        "She gives a bit more of a smile. Seems like she's feeling a bit better."
        ane "I guess that'd make you my firssssssst friend, here."
        ane "It'ssss been a while ssssince I've had sssssome real-life friendsssss."
        mc "Same here, although I found quite the interesting bunch during orientation."
        "Anemone takes out a small item from her coat pocket."
        ane "Have thisssss. As a token of our friendsssship."
        "She hands me a small pin with a spiral on it."
        mc "Oh, that's so cute! Thank you."
        "I grab my backpack and fasten it on the side."
        tut "Side Quest: First Day Jitters - Completed"
        $ inventory.append("Spiral Pin")
        tut "Spiral Pin added to Backpack."
        "We end up chatting for a little bit more before we head our separate ways."
        "And thankfully, the food was definitely edible."
        python:
            if(AddToBestiary(ane_bestiary)):
                renpy.show_screen("bestiary_popup", name="Anemone Chauveret")

        $ cafeteriaSeen = True
    call freeTime from _call_freeTime_8
    return

label nurse1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_10
    if nurseSeen == False:
        scene bg nurse with dissolve
        $ location = "Nurse's Office"
        show screen in_game_ui
        "Ever since middle school, I've had a pretty intimate relationship with the school nurse."
        "Back when I was starting to discover my ability, I would get myself stuck in walls, floors, and ceilings."
        "I was a walking mess of bandages, casts, and stitches."
        "Thanks to people like me, Defectives are required to have frequent physical and mental checkups."
        "Makes me feel like the government treats my existence as a threat or something."
        "Either way, it's time for the annual \"Hey, look at me, my ability is dangerous\" talk."
        "When I enter, I see a woman in an outfit that I can only describe as \"Nurse Joy\"."
        elo "Welcome, welcome!"
        elo "Whatever seems to be the problem?"
        mc "Hi. I'm new here and just wanted to let you know I'm a Defective."
        elo "I see."
        elo "Don't you worry, I know where you're coming from."
        elo "Defectives aren't required to have checkups in this school, if that's why you're here."
        mc "Wait, really?"
        mc "I thought it was a government thing I had to do."
        elo "At regular schools, yes."
        elo "But at schools meant for the supernatural, it's only optional."
        mc "Okay, thank you very much."
        elo "No worries."
        elo "If you need me for any reason though, don't hesitate to come by."
        $ elo_name = "Eloise"
        elo "My name is Nurse Meyer, but you can call me Eloise."
        mc "Thank you, Eloise."
        elo "No problem. Take care now!"
        python:
            if(AddToBestiary(elo_bestiary)):
                renpy.show_screen("bestiary_popup", name="Eloise Meyer")
        $ nurseSeen = True
    call freeTime from _call_freeTime_9
    return

label advisors1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_11
    if advisorsSeen == False:
        scene bg advisors with dissolve
        $ location = "Advising Center"
        show screen in_game_ui
        "You know, even though I've gotten accepted here, I don't really know all that much about this place."
        "Maybe I can learn a little bit from the advisor here."
        tut "Side Quest: A Little Bit Of History - Started"
        "I enter the advising center and see a slightly open door."
        chr "Come in, [player]."
        "...wait. Huh?"
        "How did she know that I was here?"
        "How does she know who I am?"
        chr "I'm an Oracle."
        chr "I can see up to 15 minutes into the future."
        chr "Don't be shy, I won't bite."
        "...that answers that."
        "I pass by the secretary and enter the advisor's office."
        chr "Sorry if that freaked you out a bit."
        mc "Erm...no worries."
        mc "I will admit that was really weird, though."
        mc "But like, really cool."
        chr "Eheh, thank you, hon."
        chr "So before I answer your questions, let me introduce myself."
        $ chr_name = "Christine"
        chr "My name is Christine Windsor. I graduated from this academy a few years ago now."
        chr "Any questions you have about this place, I can get them answered."
        chr "You can ask away."
        mc "Wait, but don't you already know what I'm going to ask?"
        chr "Yes, but it wouldn't feel much like a conversation if I was the only one doing the talking, no?"
        mc "I mean, I guess that's true."
        mc "But, I guess my first question is..."
        $ questionsAsked = 0
        call advisorQuestionLoop from _call_advisorQuestionLoop
        chr "Does that answer all of your questions?"
        mc "Yes. Thank you."
        chr "Anytime. If you come up with more questions, please let me know."
        chr "Otherwise, feel free to take a complementary school pin on your way out."
        python:
            if(AddToBestiary(chr_bestiary)):
                renpy.show_screen("bestiary_popup", name="Christine Windsor")
        tut "Side Quest: A Little Bit Of History - Completed"
        $ inventory.append("School Emblem Pin")
        tut "School Emblem Pin added to Backpack."
        $ advisorsSeen = True
    call freeTime from _call_freeTime_10
    return

label advisorQuestionLoop:

    if questionsAsked == 0:
        $ menuText = "But, I guess my first question is..."
    else:
        $ menuText = "My next question is..."

    menu:
        "[menuText]"
        "Who Built This Academy?" if not q1_asked:
            chr "That would be President Furukawa himself."
            chr "As one of the oldest known people with an ability, he decided to create this school to have a place where the youth could embrace their abilities."
            chr "As you might know, America, England, France, and India also have their own schools under the {important}Supernatural Student System{/important}, but H.U.D.A. is the most recognized."
            chr "He hopes that showing alumni from this school can do good in society can help ease tensions between the normal and the supernatural."
            $ q1_asked = True
        "What Do I Get When I Graduate?" if not q2_asked:
            chr "Well, you don't get the traditional degree like you would in a normal college."
            chr "You get an {important}Ability License{/important}, which basically certifies that you have a expert grasp on your ability."
            chr "Those with an Ability License aren't required to go through screenings when travelling, are allowed to work at any jobs they wish to, and can basically be treated as insurance in case tensions between the normal and supernatural rise."
            $ q2_asked = True
        "Are All Of The Students Here Supernatural?" if not q3_asked:
            mc "My roommate Yasuda doesn't have an ability."
            mc "Does that mean they messed up during their scouting?"
            $renpy.music.stop()
            chr "..."
            chr "All I can say is that H.U.D.A. has never made a mistake in scouting students so far."
            chr "Whatever the reason may be, the academy needs her here."
            chr "That's all I can disclose."
            play music "audio/datsflaze_haste.mp3"
            $ q3_asked = True

    $ questionsAsked += 1
    if(questionsAsked < 3):
        jump advisorQuestionLoop
    return

#Floor 2
label commonRoom1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_12
    if commonRoomSeen == False:
        scene bg commonroom with dissolve
        $ location = "Dorm Common Area"
        show screen in_game_ui

        "I check out the common room area to see what they have."
        "Seems they have a couple of fridges, some stoves..."
        "...a big dining table, laundry in the back..."
        "...a TV, some chairs, some vending machines..."
        "...and a woman with wings on the ground praying."
        "Seems I might've walked in on something."
        "I prepare to tiptoe out of here, but she ends up standing and looking in my direction."
        cha "Hello."
        mc "Sorry, did I like, interrupt you or something?"
        cha "No, you are perfectly fine."
        cha "I was simply having a conversation with someone and now it is complete."
        mc "...uh-huh."
        cha "You see, I am the Student of Praying."
        cha "I can directly communicate with deities of my choosing, as long as I have complete faith in them."
        mc "I see."
        mc "I mean, I've never been a religious person, but I guess that's pretty cool."
        cha "Do not worry, I understand the skepticism."
        cha "In fact, it is welcome."
        cha "Do not believe in things superficially, for you will fail to see the real truth."
        mc "Yep, got cha."
        mc "I gotta head out though, so I guess I'll be seeing you?"
        cha "And you as well."
        cha "But might I ask, what is your name?"
        mc "My name is [player]."
        $ cha_name = "Charmeine"
        cha "Charmeine Hale. A pleasure to meet you."
        mc "And you as well."
        "I head out of the common room and take some deep breaths."
        "Stuff like that gets me {i}really{/i} uncomfortable sometimes."
        "Better find somewhere else to go."
        python:
            if(AddToBestiary(cha_bestiary)):
                renpy.show_screen("bestiary_popup", name="Charmeine Hale")
        $ commonRoomSeen = True
    call freeTime from _call_freeTime_11
    return

label azuraSeikoDorm1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_13
    if azuraSeikoSeen == False:
        scene bg hallways with dissolve
        $ location = "Hallways"
        show screen in_game_ui
        "{i}Knock Knock.{/i}"
        "Guess no one's inside. Maybe they're somewhere else."
        $ azuraSeikoSeen = True
    call freeTime from _call_freeTime_21

    return

label playerDorm1:
    call freeTimeEventSetup from _call_freeTimeEventSetup_14
    scene bg playerdorm with dissolve
    $ location = "Dorm"
    show screen in_game_ui
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
    call freeTime from _call_freeTime_12
    return

label noInteraction:
    "I enter and take a look around."
    "Hm. Nothing interesting going on right now."
    "I'll go look somewhere else."
    return
