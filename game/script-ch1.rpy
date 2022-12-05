label ch1_main:

    #scene bg bus with dissolve
    "I ignore the other passengers, as my head is spinning around with thoughts as per usual."
    "I feel so overwhelmed that my brain might just melt in my head and become some liquidy mess."
    "What do I do?"
    "Will there be immediate classes?"
    "Will I have time to meet people?"
    "Can I get settled before orientation?"

    stop music fadeout 2.0
    "I look up to get out of my thoughts, and when I come to, I see the biggest school I have ever seen."

    play music "audio/serenityextended.mp3" fadein 2.0
    "My eyes get wide in amazement at the sight of the school."
    "For once, my anxiety feels at ease as I gaze at the beautiful architecture."
    "I don't know why, but this feels like a home away from home."
    "I feel the bus come to a complete stop in front of the gates."
    "All of the students start to file out of the bus slowly, as I'm stuck in the back of the bus waiting for my turn."
    "As I watch all the kids get off the bus, I look down and see well dressed butlers holding elegantly crafted signs."
    "Each sign has a name written in calligraphy handwriting."
    "Must be for us new students that are arriving."
    "Wait, this is a school for the supernatural. I doubt they would mind if I used it."
    "Instead of waiting for the bus like I had planned, I just phase through the side of it, making sure to land on the ground gracefully instead of making a fool out of myself."

    #scene bg outside with dissolve
    "I look around at all of the signs, trying to find the one with my first name."
    "After looking through the sea of writing, I stumble across it in big letters."
    "Guess I'm in the right place, after all."
    "I start walking trying to force myself to say hi to the person holding my sign."
    "As I get closer, I see he is an older gentleman with a receding hairline."
    "His hair is a mix of black and grey, blending all together in a way that matches his old age well."
    "I finally get close enough that he will be able to hear me."
    "Wow, he's pretty tall."
    "I try to force myself into eye contact but simply failing to do so."
    mc "Uh...hi, I'm [player]?"
    "He looked at me with a small smile. Maybe one of pity?"
    om "Welcome! You must be one of our newest students, come follow me!"
    om "My name is Mr. Furukawa, the principal at this here academy. A pleasure."
    "Wait, the principal!?"
    "Why is he my assistant!?"
    "Don't they have enough staff for that?"
    "I reach out to shake his hand, hoping to not mess up in front of the person that literally runs the place."
    "While he gives my hand a firm grip, I end up doing one of those limp fish handshakes in return."
    "Sure nailed {i}that{/i} one."
    om "I hope you brought a suitcase with clothes, if not we can have your guardians mail them to you."
    "Suitcase? Uh, that wasn't really in the letter at all."
    mc "Uh...yeah, I haven't even packed my clothes."
    mc "Sorry 'bout that."
    "My hands start to sweat. Have I already messed up?"
    om "Come, follow me to where we will have the meet and greet, along with showing you to your dorm."
    "I look up at him as we start walking into the courtyard of the school, spying on the upperclassmen that are just trying to have their free time."
    "There's an array of different people and specimens that I had never even thought possible."
    "Compared to all these abnormal people, I feel like..."
    "I'm the most {i}normal{/i} from the abnormal."
    mc "So, we all live in dorms, right? Is that how it's gonna work?"
    "He looks down at me, probably wondering why I asked a stupid question."
    om "Yes, everyone that attends this school gets their own space. We have no commuters."
    om "The reason why is that we try to protect our outstanding students from those in society who aren't all that welcome with the supernatural."
    om "Therefore, our students stay here until they have mastered their powers and can show that we can live in harmony with the Normals."
    "I follow him slowly, staying behind him trying to look around and take in the elaborate and quite expensive scenery all around me."
    "I get the feeling of butterflies in my stomach."
    "Thoughts start racing in my head again."
    "What if my roommate doesn't like me? I'm sure to get a roommate. "
    "But hey, at least it's the all girls section so I don't have to deal with brutes screaming down the hallway or something."
    "The thought of that makes me relieved."
    "Boys at my old school would always pick on me for 'switching teams'."
    "There were a lot of homophobes at that school."
    "I'm just happy I'm somewhere I belong, or should belong at least."
    "I keep following the nice man, realizing I was lost in thought."
    "I should probably be listening to him, shouldn't I?"
    "I got out of the clouds for a second to realize he stopped talking. I blush softly in embarrassment."
    "I didn't hear a single word of what he just said."
    mc "Yeah uh, can you repeat that? Didn't get the last part."
    "He smirks patiently and begins to explain it again to my jumbled mind."
    om "Of course, [player]. I was just going over our living facility."
    om "Your dorm is to the right. Two doors up is the bathroom. Common area is on the second floor."
    om "Your roommate should be in there already, eager to meet you."
    om "I hope you enjoy your time here at our academy."
    om "And I surely hope you will attend the orientation ceremony at the courtyard in an hour."
    "I nod in his direction as he departs to work on whatever else principals do."
    "I sigh, since I don't have to keep forcing myself to act proper."

    "Which leaves me with my dorm and...my new roommate."
    "I feel my stomach get butterflies, and my throat feels as though there is something stuck in it."
    "What if she doesn't like me?"
    "What if she is the opposite of me?"
    "What kind of power does she have!?"
    "I stand there trying to take deep breaths through this small panic attack."
    "I've never been good at meeting new people."
    "I look around and notice some of the other students in the distance staring at me, wondering why I wasn't going in."
    "Okay, [player], you got this!"
    "I knock on the door timidly."
    y "Come in!"
    "As the faint, distinctly British, voice invites me, I smile feeling the butterflies go away slightly."
    "I phase through the door."

    #call showCg from _call_showCg_2
    "I see my roommate sitting on the bed."
    y "Hello there."
    "A girl wearing a lolita outfit looks towards me."
    "Her frame is similar to mine, except her skin is ghostly pale from makeup."
    "Her bright blue eyes are warm and inviting like a summer ocean."
    mc "Hi, nice to meet you, I am [player]."
    "My roommate looks at me with a wide smile and gets off the bed to greet me with a bow."
    #hide cg with dissolve

    scene bg playerdorm

    show yasuda at middle

    $y_name = "Roommate"
    y "I hope you like the room, I organized everything alphabetically and cleaned our closet, as well as organizing our halves of the room."
    #$yface = 'blush'
    show yasuda
    y "I'm sort of a clean freak, if you do not mind that."
    "A clean freak though?"
    "I hope she doesn't mind cleaning my clothes and books up all the time."
    "My butterflies went away at this point as I set my bag down in the middle of the floor."
    mc "That's fine. What's your name again?"

    #$yface = 'surprised'
    show yasuda at bounce
    y "Oh my goodness, I totally forgot!"
    $y_name = "Yasuda"
    #$yface = 'neutral'
    show yasuda
    y "My name is Yasuda Nana. It is quite the pleasure to meet you, [player]."
    "I give her a nod to greet her as formally as I can."
    "However, when I look back up, Yasuda seems to be staring at my backpack like it committed arson."
    "She seems to be itching to move my bag, but is holding herself from doing so."
    mc "Erm...would you like me to move my bag? You look uncomfortable."
    #$yface = 'surprised'
    show yasuda
    y "I apologize, did that offend you?"
    y "I just really like a clean room. It refreshes the mind."
    mc "No worries, you're fine."
    $yface = 'neutral'
    show yasuda
    "I pick my bag up to place on my side and make myself comfortable."
    mc "So erm, tell me a little bit about yourself, since we'll be rooming together and all."
    y "Well, I am no one special, really."
    y "I like gardening, tea, and reading a good book over candle light."
    mc "...cool, but what's your power?"
    "Yasuda looks at me a bit hesitantly."
    #$yface = 'blush'
    show yasuda
    y "Well..."
    y "I do not have one, really. I'm sorry."
    "Huh?"
    "She doesn't have a supernatural power? Or a talent?"
    "Nothing?"
    "She's...{i}normal?{/i}"
    "Why is she here?"
    y "I can tell you're quite confused."
    "Is it really that obvious?"
    mc "Sorry...it's just..."
    mc "Isn't this school for people with super talents and supernatural powers?"
    #$yface = 'neutral'
    show yasuda
    y "Yes, yes I would assume so. I was curious when I was scouted too."
    y "But the administration said that their decision was entirely intentional, and therefore I will entrust that they made the right decision."
    y "However, being in an environment with so many spectacular specimens will surely make me an outcast."
    "That makes two of us."
    "Probably why we're paired as roommates then."
    y "And what about yourself, [player]?"
    mc "I uh...phase through stuff, I guess."
    mc "Like, anything. If I wanted to."
    "Yasuda claps her hands together."
    #$yface = 'happy'
    show yasuda
    y "Ah, that's a splendid ability!"
    y "So that explains the phenomenon I saw as you entered our room."
    #$yface = 'neutral'
    show yasuda
    y "I must warn you for the future that if you are to phase through the door, continue to knock beforehand."
    mc "Yeah, of course."
    mc "I'm not a peeping tom or anything."
    #$yface = 'happy'
    show yasuda
    y "I would certainly hope not."
    "Yasuda giggles to herself."
    "She's a sweet young woman, very prim and proper."
    "I'm still really stumped on her status though."
    "I wonder why someone who's normal got thrown in here."
    "Maybe it's some sort of social experiment? Who knows?"
    #$yface = 'neutral'
    show yasuda
    y "Anything else besides your power that you would like to share?"
    mc "Well, other than that, I'm pretty straightforward."
    mc "Don't have many hobbies, just kind of laze around in my room and listen to music."
    y "Hmmm...I see."
    y "Maybe you can share some of your music. I am not very musically inclined."
    "And thus, Yasuda and I began sharing some of our tastes in music."
    "Yasuda's got some...interesting choices in her playlist."
    "Let's see where this goes."

    #scene bg playerdorm

    call storyTransition from _call_storyTransition_4

    #$yface = 'surprised'
    show yasuda
    y "Oh! And before I forget, what do you think of the school?"
    mc "The school? Haven't really seen much of it other than the outside and a few hallways."
    y "Have you not explored outside of the dormitory areas?"
    mc "Not really, just kinda got here."
    y "Well, I urge that you get familiar with your surroundings before orientation."
    y "Might as well if you have the time."
    "I probably should, shouldn't I?"
    "I'd feel kinda dumb if I had trouble getting there in the first place."
    mc "I'll go do that. You do the same."
    #$yface = 'happy'
    show yasuda
    y "Certainly. I will quickly tidy up the room and depart on my own."
    "But...the place is already as clean as I could imagine it to be."
    y "Farewell, for now."
    mc "See ya."
    "I leave Yasuda to herself while I go check out the school's interior."
    #$yface = 'neutral'

    #scene bg hallways with dissolve
    stop music fadeout 2.0

    "The hallways here are pretty wide."
    "They go pretty far too, with tons of doors to the left and right of me."
    "Outside of some of the doors, looks like social circles have already been made."
    "Looks like upperclassmen though from the looks of it."
    "Some of them seem to be reuniting like old friends."
    "Although I've never really had my circle of friends, seeing so many is a little depressing."
    "However, before I can turn around to get away from these people, my vision is obscured by a veil of vibrant blue."

    play music "audio/04_sun_manzai_third.mp3" fadein 2.0
    #call showCg from _call_showCg_3
    "{i}Sniff sniff.{/i}"
    "A blue skinned girl clings onto me, her face pressed into my body."
    "She seems to be smelling me, for some reason."
    "I...don't really know how to react in this situation."

    window hide
    menu:
        "Let Her Sniff":

            "I decide to leave her be."
            "She's not doing any harm, I hope."
            "She sniffs me for a solid minute before backing off."

            call changeColor(-0.1)
            #hide cg with dissolve
            #show azura at middle
            a "Hello. I like your smell."
            #show azura at jumping
            "She jumps happily, despite her face looking quite sad."
            "It's a little weird, but I think she's happy?"
            #show azura at middle

        "Tell Her To Back Off":

            mc "Um...can you, stop that please?"
            a "Oh."
            "The blue girl immediately stops and backs away, however she looks pretty sad."
            "I kind of feel bad now, but she invaded my personal space."

            call changeColor(0.1)
            #hide cg with dissolve
            #show azura

            a "Hello."

        "Back Away Slowly":

            "I try to back away slowly to see if she gets the hint."
            "However, she doesn't and continues to sniff anyway."
            "Makes for a real awkward situation."
            a "Hello. Are you scared?"
            "The blue girl backs off, with a weirdly sad look on her face."

            #hide cg with dissolve
            #show azura

            a "I like you."

    mc "Uh...well hi there."
    "The blue girl with cloudy grey eyes stands a few inches taller than me."
    "I look at her face that kind of seems frozen in a way."
    "It just...doesn't emote, really. I can't tell what she's feeling."
    $a_name = "Azura"
    a "I'm Azura."
    mc "...[player]."
    a "See? See?"
    "Azura takes a little booklet out of her coat. Seems to be a passport."
    "Sure enough, her name is Azura Bell."
    "She's apparently Canadian. I guess that's a first for me."
    "Azura jumps up and down, almost excitedly, while her face remains a constant sad expression."
    "It's really jarring, unsettling even."
    mc "Are you okay?"
    a "Yes. Yes."
    #$aface = 'surprised'
    #show azura
    a "Are you new? I'm new too."
    mc "Yeah, I just got here not long ago."
    a "Oooooooh."
    "She stares at me with a curious, but friendly glare in her eyes."
    a "You look nice too."
    mc "Thanks? Also, why the heck did you sniff me?"
    a "...sniff?"
    #$aface = 'neutral'
    #show azura
    a "Oh. Yes, yes."
    a "I'd like to know your smell."
    "This girl is all sorts of bonkers."
    "And she seems sort of...slow, I guess?"
    "But I think her spirits are in the right place."
    "I'll try my best to steer the conversation, see what she knows and all."
    "Maybe even make a friend."
    "She seems pretty nice, all things considered."
    mc "So uh, what makes you special?"
    a "I'm blue."
    mc "Mhm. I see."
    #$aface = 'excited'
    #show azura
    a "They say I smell better than other people."
    mc "I've noticed. Do you smell everyone you meet?"
    "Azura nods vigorously."
    a "I can tell who's my friend by their smell."
    mc "I guess that's pretty darn neat."
    #how azura at bounce
    a "Yey~"
    #$aface = 'neutral'
    #show azura
    "Azura claps to herself, seemingly excited but her face not showing it."
    mc "Are you alright?"
    a "Hm?"
    mc "You look concerned. Something bugging you?"
    a "Oh. No. I just have a hard time showing...showing..."
    #show azura at bounce
    a "Emotion! That's the word."
    mc "Ah. So you're happy then, right?"
    a "Yes."
    mc "Good to know."
    mc "Hey, by the way, you're going to orientation, right?"
    a "Mhm."
    a "But, what do we do before then?"
    mc "Well, I was planning on looking around the place so I don't-"
    a "Oh. I can show you."
    a "I looked at the c...campus! The campus, yes."
    a "I looked at the campus already."
    a "Can I show you?"
    mc "Um, sure."
    #$aface = 'excited'
    #show azura at bounce
    a "Yey~"
    #show azura at hug
    "Azura proceeds to give me a big, warm hug."
    "She then grabs my hand and leads me deeper in the school, her gait more like that of waddling."
    "Thus begins my mini-tour of the school from a...very interesting guide."

    play music "audio/happydays.mp3" fadein 2.0
    #$aface = 'neutral'
    #show azura

    "Azura starts to bring me around, showing and naming off all of the places we pass by."
    "She really has a good sense of direction."
    "And she's a sweetheart, too."
    "It's strange how fast she learned this place, but at least I know I won't get lost."
    "The place is really fancy all around, and there's a lot of unique faces."

    #scene bg courtyard

    "We reach the courtyard, which seems to have one of those stages in the middle that looks like it was set up for the occasion."
    "There's a few groups of people here already, sitting on benches or just forming their own clusters."
    a "This is where the meet up is."
    mc "Good to know for later. Thank you."
    "Azura seems to try and give me a smile, but her face kind of just twitches."
    "We move onto more areas. Azura practically drags me everywhere."

    #scene bg classroom
    a "...this is class. We learn things here."

    #scene bg cafeteria
    a "...there is food here. They gave me some earlier."
    a "They were very nice."

    #scene bg gym_int with dissolve

    a "...and um, this is the place to get stronger."

    #show azura at jumping
    "While she shows me the big interior of the gym, she starts jumping around a bit more than usual."
    mc "Something up?"
    a "Bathroom, please."
    mc "Ah, okay."
    "Azura points to where the locker rooms are and we head over there."
    #show azura at easeInsideLeft
    "I yank at the door, but..."
    "{i}CLUNK CLUNK.{/i}"
    "It's ID locked. I haven't gotten an ID yet."
    a "Oh."
    "She seems a little disappointed, since the last time we saw a bathroom nearby was near the cafeteria some time ago."
    "However, this is the perfect scenario for weirdos like me."
    mc "It's alright. I'll go unlock it."
    mc "I can phase through walls, so I can just open it, probably."
    #$aface = 'surprised'
    #show azura
    a "Ooooooooooh."
    "She looks at me, but from her eyes it's clear she didn't understand what I said."
    #$aface = 'neutral'
    #show azura
    "I look at my surroundings to see where's the best place to phase through."
    "The ceiling's a little too low for my comfort near the door; I might end up bonking my head on it if I unphase too quickly."
    "I'll go for the wall right next to it."
    "I do my regular hop-n-phase technique through the wall to get inside."

    #scene black with dissolve
    stop music fadeout 2.0
    "However..."
    "I forgot locker rooms usually have lockers, so I unphase too quickly."
    mc "Fu-"
    play sound "audio/sfx/locker_thud.wav"
    "{i}THUD!{/i}"
    "I hit my head on the interior of a locker door."
    "Hey, at least I know I can fit in one of these lockers."
    s "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHH!!!"
    "I hear someone scream in the locker room."
    "I just got into major amounts of trouble, didn't I? Shit."
    "Will there be a security guard?"
    "Will I get kicked out on my first day?"
    "As I sit there in my thoughts for a second, I hear the locker door open slowly."
    #call showCg from _call_showCg_4
    play music "audio/listenup.mp3" fadein 2.0
    "I see a blonde girl who is slightly thin with... 4 arms?!?!"
    "She peers into the small fitting space of what seems to be her locker."
    "She looks at me up and down giving this... flirty look?"
    "I can't stop looking at her extra arms."
    "But I manage to switch to looking her face covered with a big smirk."
    $s_name = "Four-Armed Girl"
    s "So, would ya like to tell me how you ended up in this locker?"
    mc "I-I-I was just trying to unlock the door for my friend..."
    mc "...cause she has to use the bathroom."
    s "Well, how'd ya end up in there when the door's locked on the other side?"
    "My mouth refuses to work, even though the answer's very simple."
    "I hate feeling interrogated by people."
    "It makes me tense up greatly and get me all flustered."
    "She keeps looking at me waiting for an answer."
    mc "I-I can phase through the walls so-"
    s "Ah,  don't worry about it!"
    s "It's fine! I'm just messing with ya! Heehee!"
    "The weirdo with four arms puffs out her tiny chest and begins to scream from the top of her lungs."
    $s_name = "Seiko"
    s "The name's Seiko!"
    s "SEIKOOOOOOOOOOOOOO WATANABEEEEEEEEEEEEEEEEEEEE!"
    s "Nice to meet ya, cutie!"
    "I look at her, covering my ears from how loud she is."
    "She's probably loud enough to make my ears ring."
    "I give Seiko a weird, confused look."
    "Oh great, a loud mouth."
    mc "[player]."
    mc "Nothing spectacular."
    "Seiko extends one of her hands towards me."
    s "Let's get ya outta there!"
    "Seiko yanks me out of the locker, slamming it behind me."
    #hide cg with dissolve

    #scene bg lockerroom
    "I feel her wrap around me as she helps me out of my predicament."
    "Urgh...I'm being touched again... I feel uncomfortable."
    "Four arms wrapping around me, this feels WAYYYY too weird for me."
    "Seiko finally lets me go as I am able to take a breather."
    #show seiko at middle with dissolve
    "She gives me a smile."
    "I inch away slowly, swiftly making it to the door that I have to open for Azura."
    play sound "audio/sfx/running.wav"
    #show azura at running
    "I barely get to open the door as Azura rushes in and goes straight to the stalls."
    "Seiko laughs softly, seeing Azura's goofy run."
    #$sface = 'happy'
    #show seiko zorder 2
    s "S'that your friend? She's such a cuuuuuuuuuuuutie patootie! Heehee!"
    "I cover my ears as she screams once more."
    "If she were just a little bit louder, I bet this entire locker room would just collapse in on itself."

    #show azura at sideLeft with moveinleft
    "Azura comes out of the bathroom sighing with relief."
    "She looks at Seiko with that permanent sad look."
    #show azura at focus
    a "I heard a scream. Are you okay?"
    #show azura at unfocus
    #show seiko at focus
    s "YUUUUUUUUP!"
    #show seiko at unfocus
    "I look at her for the THIRD time as she screams."
    "Does she have an off button?"
    mc "Yes, that was the tiny one."
    mc "Her name is Seiko. She likes to scream."
    mc "...a lot."
    #show azura at focus
    a "Oh. Okay."
    #show azura at unfocus
    "Azura just bounces in place, carelessly. She doesn't seem to mind."
    #$sface = 'neutral'
    #show seiko
    #show seiko at focus
    s "Well you know my name, what's yours?"
    #show seiko at unfocus
    #show azura at focus
    a "I'm Azura."
    #show azura at unfocus
    "Azura does the same routine with taking out her passport and showing it to Seiko."
    "Seiko gives her an interesting look, smiling softly at her."
    "I look at both of them just staring."
    "I wonder if Azura will sniff her? She sniffed me."
    "And just as I make the thought, Azura just goes to town, saying hello to the four armed gremlin with her face."
    "Seiko doesn't seem to mind it. though."
    "Actually, she seems like she's... enjoying it?"
    "Seiko retorts by petting Azura on the head."
    "I guess that seems fitting for her."
    "They seem to like each others company, well that's good at least."
    #$sface = 'happy'
    #show seiko at focus
    s "You are the cutest thing ever!"
    s "You remind me of a big puppy! Heehee!"
    #show seiko at unfocus, easeInsideLeft
    "Seiko hugs Azura with all of her arms, Azura hugging back."
    "Well... here I am, watching the weirdos hug each other."
    "I watch as Seiko uses one of her extra arms to keep petting Azura softly."
    "I wait there patiently, just kicking my feet against each other."
    "All of a sudden, I hear an alarm go off."
    "Seems to be coming from Seiko's phone in her back pocket."
    #$sface = 'neutral'
    #show seiko at easeInmiddle
    "I advert my eyes quickly as the two weirdos finally let each other go."
    "Seiko grabs her phone and makes a face."
    #show seiko at bounce, focus
    s "Oooooh yeahhhhhhhhhhhhh!"
    #show seiko at unfocus
    "Azura I think looks concerned."
    "So hard to tell what she is feeling with the constant sad eye look going on."
    #show seiko at focus
    s "Orientation's in 10 minutes! We have to get going to the courtyard!"
    #show seiko at unfocus
    "Azura and I nod as Seiko grabs our hands."

    #scene bg gym_int with dissolve
    #$sface = 'happy'
    #show seiko at middle with dissolve
    "Her hands are really soft, and I just noticed she has a little bit of fancy perfume on."
    "Seiko uses her free hands to open the door for us."
    #$sface = 'neutral'

    #scene bg field with dissolve

    "We spent a longer time inside that locker room than I thought."
    #show seiko at sideLeft with dissolve
    "Time really flies when you have a really loud four armed woman yelling in your ears."
    #show azura at sideRight with dissolve
    "Along with a big blue woman just...being herself I guess?"
    "What a weird day so far."
    "I guess it will always be weird."
    "I mean it's a supernatural school. Why wouldn't it be weird?"
    "That seems to be the normal here."
    "I stand in the sea of supernaturals, looking for Yasuda."
    "I'm sure she'll get a kick out of the ragtag gang that I've conjured up."
    "Sure enough, I see her strut in from the distance, her posture stiff and straight like a proper Englishwoman."
    "She sticks out like a sore thumb."
    stop music fadeout 2.0
    show yasuda at middle with dissolve
    play music "audio/everyoneisgoodfriend.mp3" fadein 2.0
    show yasuda at focus zorder 2
    y "Hello, [player]. I am glad to see you once more."
    show yasuda at unfocus  zorder 0
    #mc "Heya."
    "Seiko immediately eyes the anomaly that presented itself."
    #$sface = 'flirty'
    #show seiko at focus zorder 2
    s "Who's the goth chick?"
    #$sface = 'neutral'
    #show seiko at unfocus  zorder 0
    mc "She's my roommate, Yasuda Nana."
    #show yasuda at focus zorder 2
    y "A pleasure to meet you, Miss. Is this a new friend?"
    show yasuda at unfocus  zorder 0
    mc "Yeah, not by choice, but yeah."
    #$sface = 'happy'
    #show seiko at focus zorder 2
    s "It was meant to be! DESTINYYYY!"
    #show seiko at unfocus zorder 0
    show yasuda at focus zorder 2
    y "...I see."
    show yasuda at unfocus zorder 0
    #show azura at easeInmiddle zorder 2
    "In the time it takes for Yasuda to meet Seiko, Azura's already done her thing and approached Yasuda with the intent to sniff."
    #$yface = 'surprised'
    #show yasuda at focus zorder 2
    y "Oh!-"
    "Yasuda goes stiff, raising her hands to let Azura do her thing."
    y "Hello, young lady."
    show yasuda at unfocus zorder 0
    "{i}Sniff sniff.{/i}"
    #show azura at focus zorder 2
    a "Hello."
    #show azura at unfocus zorder 0
    mc "That's Azura. She likes to sniff people."
    #$yface = 'blush'
    show yasuda at focus zorder 2
    y "Ah. Well, it is nice to meet you too."
    show yasuda at unfocus zorder 0
    #show azura at easeInsideRight
    "Yasuda avoids touching Azura as she gets herself acquainted."
    show yasuda at focus zorder 2
    #$yface = 'neutral'
    y "So, what do you plan to do for the meet up, [player]?"
    show yasuda at unfocus zorder 0
    mc "What I wanna do?"
    show yasuda at focus zorder 2
    y "Yes. This event is meant for socialization, no?"
    show yasuda at unfocus zorder 0
    mc "Oh yeah. Probably should do that."
    #scene bg field with dissolve
    "But do I really wanna?"
    "Two people is enough, three including Yasuda."
    "Do I really wanna go for more?"

    window hide
    menu:
        "Why Not Socialize?":

            call meet_socialize from _call_meet_socialize

        "Stick Close To The Group":

            call meet_group from _call_meet_group

        "Find Somewhere To Hide!":

            call meet_hide from _call_meet_hide

    #scene bg field with wipeleft_scene
    "The time flies by, feels like hours turned into minutes."
    "I hear speakers shot out some feedback, then a loud boom."
    "Seems like there's a whole set up for this meet and greet that I wasn't even aware of."
    "I look over and see the principal once again."
    "I hear his loud voice echo from the speakers."
    om "Good Afternoon students; newcomers and returning."
    om "Welcome! I am the head of administration, Principal Furukawa."
    om "I know you all are excited for the new year, but first we gotta do the boring stuff."
    om "What to expect for the upcoming year ahead of us."
    om " First off, I hope you all enjoy your new roommates."
    om "If you have an issue with yours, please come to the front office and we can discuss it privately and anonymously."
    "The Principal goes on about the technical stuff, school manuals, blah blah blah."
    "I kinda doze off during some parts, but at least he doesn't seem like a complete buzzkill."
    om "...another matter I would like to address is, of course, the one beginning of the year event everyone looks forward to."
    "Hm, maybe he's going to talk about the festival? Mom mentioned it to me."
    "I heard it's all about talent, decor, and lots of unique booths."
    "I'm surprised they hold it so early in the year, since it's only April."
    om "...The Summer Supernatural Festival!"
    "Nailed it."
    om "This year, however, we will be adding a new event that have been commonly requested."
    om "We, the school board, decided to add a talent show!"
    "Huh, a talent show?"
    "That would be an interesting thing to be able to experience."
    "I can hear happy cheers and clapping from what looks like the Third and Fourth years."
    "Chitter-chatter begins abruptly roaring from the crowd not long after."
    om " Alright, settle down everyone."
    om "We know that these are exciting times and happily encourage anyone to apply for these events!"
    om "We get unique talents every year, so we hope to see some exciting abilities from the student body."
    om "And onto other topics-"
    "As the Principal keeps talking, I start to zone out again."
    "Trying to figure out what I should do."
    "Do I even want to go for the festival?"
    "I still have time to think about it, but I immediately think back to my high school proms and formal events of the like."
    "Will I have to find a date all over again?"
    "My palms start to sweat thinking about it."
    om "Enjoy the rest of your day, everyone."
    om "Classes start the day after tomorrow, so spend it wisely getting prepared."
    "The principal seemingly disappears as he finishes his speech."
    #$sface = 'neutral'
    #show seiko at sideLeft with dissolve
    show yasuda at middle with dissolve
    #show azura at sideRight with dissolve
    "I see the trio walking over to me, smiling."
    "Well, except for Azura, she has that permanent sad face."
    #$sface = 'happy'
    #show seiko at focus, bounce zorder 2
    s "I have like a bajillion ideas for that talent show thing!"
    s "I'm super duper HYYYYPEEEED!"
    #show seiko at unfocus zorder 0
    "Azura looks confused, but doesn't say anything."
    #$yface = 'blush'
    show yasuda
    "Yasuda seems apprehensive."
    mc "I'm looking forward to it, too."
    mc "The festival part, not the people part."
    mc "For now, I think it's time to hit the dorms and call it a day."
    #$yface = 'neutral'
    show yasuda
    "Yasuda nods and leads the way, but Seiko and Azura tag along."

    #scene bg hallways with dissolve
    "We make it to the dorms."
    "Azura and Seiko search for their dorms, but we quickly find out that the two are roommates."
    "Well hey, guess things happen for a reason."
    #$sface = 'happy'
    #show seiko at sideLeft, focus zorder 2
    s "More pets for my big ol' blue friend!"
    "Azura lets out a slow, but loud laugh."
    #show seiko at unfocus zorder 0
    #$aface = 'excited'
    #show azura at slightLeft, focus zorder 2
    a "A-hee-hee-hee."
    #show azura at unfocus zorder 0
    #hide seiko with dissolve
    #hide azura with dissolve
    "She jumps down with excitement as Seiko drags her into their dorm."
    "Yasuda and I go into our dorm."

    #scene bg playerdorm with dissolve

    "I throw myself on my bed."
    "What a day."
    "Got introduced to a weird school and a weird cast of people to boot."

    #if(rel_meter == 0):
        #$yface = 'happy'
        #show yasuda with dissolve
        #y "Well, I am glad that you have gotten a good start to your school career."
        #$yface = 'neutral'
        #hide yasuda with dissolve

    play sound "audio/sfx/knock_01.wav"
    "As Yasuda cleans and dusts literally nothing at this point, a knock is heard at our door."
    "Already???"
    y "Who is it?"
    s "Your favorite girl in the whole universe, that's who!"
    s "Anyways, wanna go eat some lunch later?"
    s "I heard the meal plan stuff is gonna get handed out today!"
    mc "Sure, grab us in a bit."
    "Afterwards, Yasuda keeps to herself while I self reflect."
    "I can tell this is the start of some {i}wonderful{/i} friendships."
    stop music fadeout 2.0

    return

label meet_socialize:

    #scene bg field with dissolve
    "I'm already here anyways."
    "Might as well socialize, although Seiko's beat me to it."
    "I walk through the crowds and stray away from the group."
    "A student eventually approaches my awkward self."
    "A wolf girl with bright red hair seems to wanna chat with me."
    stop music fadeout 2.0
    play music "audio/itsshowtime.mp3" fadein 2.0
    $ met_helena_at_orientation = True
    hl "Yo! The name's Helena Ivory! Nice t' fuckin' meet ya!"
    "A sailor mouth, but she's pretty cool looking."
    "She wears a punkish outfit with ripped jeans."
    "Her tail is huge."
    "Definitely the first time I've seen someone like this."
    "I know someone that'd be jealous that I've met a real wolf girl."
    if outfit == "black":
        "Glad I wore this outfit to the meetup."
    else:
        "Should've worn something else, since I look all girly right now."

    hl "You seem like a nice bitch. What's your schtick?"
    mc "I walk through walls and stuff."
    hl "Really? That's actually amazing!"
    hl "But have you seen this?"
    "Before I can inquire, I start floating in the air."
    "I frantically try to grab the ground in a panic."
    mc "Wh-"
    hl "Gahahahaha! Did ya shit yourself?"
    hl "I can move you with my miiind!"
    hl "Pretty fuckin' impressive ain't it?"
    mc "Yeah, but c-could you pleeeease warn me beforehand before you do that?"
    "She puts me back down on the ground. I fumble and catch myself."
    hl "Sorry, toots. Just get carried away sometimes."
    hl "But yeah. Been workin' on my power for the last three years here!"
    hl "Imma be a fuckin' master in no time, huh?"
    mc "Yeah, guess so. Good job."
    "Helena and I talk for a while."
    "In the meantime, I see Seiko in the distance basically trying to woo over the ladies."
    call changeColor(0.1)
    "Guess she's having fun too."

    python:
        if(AddToBestiary(hl_bestiary)):
            renpy.show_screen("bestiary_popup", name="Helena Ivory")
    stop music fadeout 2.0
    play music "audio/everyoneisgoodfriend.mp3" fadein 2.0

    return

label meet_group:

    #scene bg field with dissolve
    show yasuda at middle with dissolve
    "I'm just gonna stay here with Yasuda and catch up on some things."
    #$yface = 'surprised'
    show yasuda
    y "You are not going to socialize?"
    mc "Nah, I'm not really a social butterfly."
    mc "I like smaller groups anyways."
    #$yface = 'neutral'
    show yasuda
    y "I see."
    y "Well if we are going to be here to socialize, why not talk about how you met your two new acquaintances?"
    mc "Sure. It's a little weird, but I guess it's interesting enough."
    "I tell Yasuda all about Azura's little tour and our escapades in the gym locker room."
    "She seems to listen with an open ear, which is nice."
    #$yface = 'happy'
    show yasuda
    y "Well, they certainly are quite colorful in personality."
    mc "Yeah, I guess so."
    mc "Speaking of colorful, where'd Azura go?"
    "I look around, but it seems Azura wandered off to meet some new friends."
    "I imagine she'll make her way back."
    "That, or just listen for anyone screaming from her trying to sniff them."
    y "I would not worry. She seems to love finding new people."
    mc "How about you? Did you want to go meet new people?"
    #$yface = 'blush'
    show yasuda at bounce
    y "Eh? Me?"
    y "Ah, I am...quite the shy woman, I must say."
    y "I don't think I'll do well with conversing with new faces."
    mc "Well, you did well enough warming up to me."
    mc "How about we try it together?"
    #$yface = 'neutral'
    show yasuda
    y "Sure. But only with your assistance, if you do not mind."
    mc "Fine by me."
    "And with that, us two socially awkward women wander deep into the crowd, trying to introduce ourselves to new people in the most cringe inducing ways possible."

    $ met_helena_at_orientation = False

    return

label meet_hide:

    #scene bg field with dissolve
    "Yeah, my anxiety is rising from all the new people here."
    "I think I'll need some space to breathe."
    "I head towards the outskirts of the crowd, sitting underneath a tree."
    "Thankfully, it seems no one followed me."
    "I'd much rather be alone with my own thoughts."
    "I close my eyes as my mind begins to wander."
    #scene black
    "Today's been quite a day."
    "I don't know if I'll ever get used to this."
    "If I've already met three people, who knows how many I'll meet by the end of this thing."
    "I might just be a hermit for my school career with Yasuda."
    "I doubt she would mind, although she'd probably have to do a lot of cleaning."
    "I don't think I can mentally handle being around people all day."
    "If I have an anxiety attack in public, that's gonna haunt me for the rest of my life."
    "What to do...what to do..."
    a "Hello."
    "I hear Azura's voice and a bunch of warmth around me."
    #scene bg field with dissolve
    #show azura at middle, closeup zorder 5
    "I open my eyes to see Azura sitting right in front of me, staring me down."
    #$sface = 'happy'
    #show seiko at sideLeft, focus zorder 2
    s "Got ya!"
    #show seiko at unfocus zorder 0
    "Welp, that ends my peace and quiet."
    #show azura at slightLeft, unhug zorder 1
    "Seiko pets Azura on the head."
    #show seiko at focus zorder 2
    s "Good girl!"
    #show seiko at unfocus zorder 0
    #$aface = 'excited'
    #show azura
    "Azura practically melts in Seiko's hands, laying on her back, seemingly excited."
    call changeColor(-0.1)
    #show azura at focus zorder 2
    a "I did it."
    "After Azura's second pet session of the day, the two weirdos drag me back into the circle and attempt to get me to socialize with strangers."
    "Guess I have no choice, but I won't like it."
    #$aface = 'neutral'
    #$sface = 'neutral'

    $ met_helena_at_orientation = False

    return
