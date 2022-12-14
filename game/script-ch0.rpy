# The game starts here.

label ch0_main:

    scene black

    $ day = "Wednesday"
    $ currentTime = "Daytime"
    $ location = "Bedroom"

    #Show UI
    show screen in_game_ui with dissolve
    show screen relationship_heart with dissolve

    play music "audio/00_quiet_ambience.mp3" fadein 2.0

    "People call me a {important}freak.{/important} A {important}weirdo.{/important} A {important}monster.{/important}"
    "A... {important}'Destructive'{/important}, people call it."
    "In this world full of abnormal people, even to them, I am {important}not normal.{/important}"
    "Not in the slightest."
    "These are the thoughts that race in my head all the time."
    "I was never normal in the first place."
    "I was born with an ability that sets me apart for the crowd."
    "I call it Phasing."
    "I can pretty much 'phase' through everything for as long as I can remember."
    "Walls, objects, whatever. I can just phase through it at will."
    "Even the ground, if I'm not careful enough."
    "In a society where the weirdest of the weird is shunned, I can't just be myself."

    scene bg room with dissolve
    "These labels society casts upon me and those with powers never leave my mind, and continue to do so while I lay in bed and let my blackout curtains protect me from the morning light."
    m "[player], breakfast tiiiime! Come and eaaat~"
    $m_name = "Mom"
    "Mom's been trying to get us to eat together as a family. Not really feeling like it right now."
    "But either way, might be a good time to wake up."
    "I drag myself out of bed, looking at my drawer before throwing myself right back in bed."
    "College's gonna be starting in like, a month."
    "I should be getting used to waking up early."
    "But I can't, I just don't really have the energy to do that."
    "I'm not ready for college, why did I agree to go?"
    "Imagine if people didn't expect me to go to college? That'd be very convenient."
    "I honestly don't even know what my major would be."
    "However, the college I'll be going to in particular really sucks."
    "Like, the 'worst rated college in the city' kind of sucks."
    "Supernaturals usually don't go there, so I can't really use my power unless I wanna hear about it every day for the next two weeks."
    "Nevermind the 'Defective' label."
    "Maybe if I switched colleges I..."
    "..."
    m "[player]! It's family time, come down and eat already!"
    "{i}Sigh.{/i}"
    "I really don't want to be forced to eat with my family, besides, I'm not really that hungry."
    "I'll just text her or something."
    #call showCg from _call_showCg
    "I pull out my phone and tell Sari to text my mom so she'll stop bugging me."
    "{i}\"I'm not hungry right now maybe later\"{/i}"
    "Annnd send."
    "There, that should get me some privacy."

    stop music
    play sound "audio/sfx/backpack_01.mp3"
    "{i}Rustle rustle.{/i}"

    #hide cg with dissolve

    "A noise comes from the side of my bed where I keep my backpack."
    "Something probably just fell near my bag. No worries."
    play sound "audio/sfx/backpack_02.mp3"
    "{i}Rustle rustle.{/i}"
    "..."
    "Okay maybe two things fell near my bag."
    "Or something's there. Because normally I don't keep anything in my room that could make that noise."
    "Probably a rat or something."
    lb "Hello!"
    "However, the answer to that question soon presented itself to me."
    #call showCg from _call_showCg_1
    lb "I know you're awake!"
    "I freeze."
    "There's an intruder in my house."
    "I know I should scream."
    "Call the police."
    "Run."
    "But I'm scared stiff."
    "The girl seems to be wearing rags and is quite small in stature."
    "However, there seems to be no malice in her voice."
    "Then again, she broke into our house, somehow."
    "Or maybe she's a hobo?"

    $lb_name = "Libra"
    lb "I'm Libra! I like your room!"
    "What is she even saying?"
    mc "Uh. Hi? Get out?"
    lb "I have something for you! Here you go!"
    "The tiny girl, apparently named Libra, places a large card right next to where I lay."
    "I look at the card for a second, which has some kind of emblem on the back."
    "I then look at Libra, who stares at me for a bit."
    "I should call the police now, right?"
    mc "..."
    lb "..."
    lb "Oh, by the way!"
    lb "I like to run, I like to look at people, and I really like to cook!"
    mc "That's...great?"
    lb "Yup!"
    mc "..."
    lb "..."
    lm "If you could, please read the letter."
    "A quiet voice of a man pipes up, seemingly from where Libra is sitting."
    "However, the source of the noise is quickly discovered when I look into the shadows."
    "All I see is a tall, lanky man with wide eyes, staring daggers into me."
    "How did I not see him come in here too?!"
    "All of the color drains from my face."
    lb "Oh! That's Limil! He's my protector!"
    $lm_name = "Limil"

    "The mysterious man named Limil bows his head in a respectful, gentleman-like manner."
    "Libra places the letter in my shaky hands and I took a moment to calm down before reading it."
    "If I entertain their idea, maybe they'll go away."
    "{i}Dear [player].{/i}"
    "{i}Congratulations! You are hereby formally enroll you into the girls' division of Hokkaido Ultra Dimension Academy.{/i}"
    "{i}We have noticed your supernatural ability and thought it would be the perfect time to enroll you into our school as our student of Phasing.{/i}"
    "{i}It will give you the chance to learn and master your ability.{/i}"
    "{i}If you decide to proceed further, leave this card intact and we will send out further details.{/i}"
    "{i}If you decline, please burn this letter.{/i}"
    "{i}We are looking forward to having you.{/i}"
    "{i}Sincerely, Headmaster Furukawa.{/i}"
    "What kind of nonsense is this?"
    "What school has someone break into their house and hand-deliver a letter?"
    "More importantly, I've heard of this school, but, is this really how any kind of school would recruit a student?"
    "This is shady at best."
    "Illegal at worst."
    "I'll ask Mom more about it later to see if she knows anything."
    "Libra turns to me again, her childlike aura unwavering."
    lb "So um, I don't what the letter says, but I think it's good!"
    lb "Anyways, I was told to tell you that you got into my school, so that's very good news!"
    lb "I hope you enjoy university!"
    mc "Erm...thanks for the offer, but could you please leave my house?"
    lb "Okay!"

    python:
        if(AddToBestiary(lb_bestiary) and AddToBestiary(lm_bestiary)):
            renpy.show_screen("bestiary_popup", name="Libra and Limil")

    #hide cg with dissolve
    "Limil retreats into the corner of my room while Libra simply opens my window and hops out."
    "I get up to try to stop her, but it's too late."
    mc "Wha-"
    "I run to the window to make sure the girl is alright, but when I look out, there's no trace of her left."
    "Limil disappeared out of thin air, too."
    "...I feel like drug trips are more normal than those two."

    play music "audio/00_quiet_ambience.mp3" fadein 2.0
    "I head back to my bed and stare at the silhouette of the letter."
    "I can feel my stomach drop."

    "If this is true, why enroll me? I'm no one special."
    "I just go through things and people hate me for it."
    "It's nothing really spectacular. It's just weird."
    "I stumbled out of bed again for good, marking a reminder on my calendar for the start of the school year."
    "Afterwards, I went downstairs with a letter in hand and a mind full of questions."

    scene bg kitchen with dissolve
    $ location = "Kitchen"
    show screen in_game_ui
    "I head to Mom, who's in the kitchen cleaning after having finished her breakfast."
    "Mom looks up at me smiling softly, but her attention is quickly averted to the letter."
    m "What's that, sweet pea?"
    "I show her the letter, feeling a weird sense of fear and confuson."
    "She seems to smile wider, as if she already knew what was on the paper."
    m "Oh my stars, you got accepted!"
    "I look at Mom very surprised."
    "How did she know about this?"
    "Maybe this has happened before?"
    "That's a bit of a relief, but did they really have to break into my house?"
    "Mail literally exists for that reason."
    mc "Mom, you went to this place, right?"
    mc "Also, can you tell me why they just had two people break into our house?"
    "She nods, feeling happy that she can finally talk about it."
    "She gets close to me, almost jumping at the opportunity to talk about the subject."
    m "The way they send their acceptance letters is a little bit...strange."
    m "But when I got accepted I was told through the mail when they'd come give me my decision."
    "...was I stupid and threw away something important?"
    "Honestly, that could be possible, but in fairness, I never applied for this academy on my own."
    m "I was enrolled as the Student of Dreamscaping."
    m "Anything I can read, I can see a full picture and scene in my head. Like imagination, but stronger."
    m "I can create my own little worlds, inserting myself if I need to or spectating like I'm watching a movie."
    m "Thanks to that school, not only did I get to appreciate my power, but I made so many friends."
    "She begins to tell me all her stories about the school and the different types of people who went there."
    "Once you get her talking, she can go on and on about it until hell freezes over."
    m "...so that's how I met my roommate. And then, this one time, when we were in class..."
    "After about an hour of talking to her, I got tired quickly. "
    m "...at the festival, we all had a great time. Furukawa had the most beautiful display of..."
    "I start to zone out."
    "After her blabbering about her school experiences, I head back upstairs with an unnecessary large, but kind of interesting amount of information about the school."
    "But she also cleared up that the scouts hand deliver letters privately."
    "Glad to know that I wasn't in any danger."
    "Still, I think they should change their enrollment process {i}just{/i} a little bit."

    scene bg room with dissolve
    $ location = "Bedroom"
    show screen in_game_ui
    "I go into my room, looking at my calendar, holding the letter still in my hands."
    "The one thing that stuck to my mind was the festival Mom mentioned they hold every year."
    "I try to imagine her story in my head like my mom, but I sure don't have an active imagination, nevermind Dreamscaping."
    "I start to feel down quickly as my anxiety presents itself again."
    "I head over to my bed to lay down."
    "I look around my room, wondering what it's going to be like to go to this new school."
    "My mind races fast."
    "If I go here, what if I make no friends?"
    "No, that's silly. I'll probably make at least one friend."
    "But then again, I'm the biggest freak going to a school."
    "Maybe my power is different enough to make me an outcast?"
    "Maybe nobody will be impressed?"
    "My mind races with a million and one things to think about."
    "My hands get clammy quickly and I roll over in bed."
    "You know what? I'll just give this a shot."
    "If anything, it'll be more interesting than going to a normal college."
    "Maybe I'll finally be talked about without the word 'Destructive' being spit out of people's mouths."
    "I close my eyes both anticipating and dreading the first day of university."

    call storyTransition from _call_storyTransition_3

    scene bg room with dissolve
    $ day = "Monday"
    show screen in_game_ui
    show screen objective_popup
    "I open my eyes, realizing the past month has been a huge blur for me."
    "Living with depression and anxiety does that to a person."
    "I feel it spiking once more, not enjoying the feeling of rushing around and getting myself ready right now."
    "I feel questions being tossed around my head. Will there be my own bus? Will I have to walk? I've never seen this school around the area?"
    "All of these questions are spinning around my head as I try to pick an outfit."
    "Let's see..."

    window hide
    menu:
        "Pink Spotted Skirt With a White Skirt":
            $outfit = "pink"
            "I feel pretty out of my element in these, but I guess first impressions are worth it."
        "Jeans With a Nice Red Blouse":
            $outfit = "red"
            "The jeans are comfortable for me, the blouse is slightly small on me."
            "Maybe a little too provocative? Eh, whatever."
        "Black Hoodie With Black Ripped Pants":
            $outfit = "black"
            "Ah, my standard outfit."
            "I'm sure it'll make me look like the edgelord of the school, but at least I'll feel comfortable."

    "As I get dressed for the day, I feel my anxiety spiking up even more as I look over at my backpack."
    "Shit, I should probably put stuff in there, shouldn't I?"
    "I let out a distressed sigh, walking over to my backpack ready to just shove random stuff into it."
    "What should I put? Should I be prepared for the first day or just wait until a list?"
    "I doubt it matters, but if it does, I don't wanna feel awkward."

    call chooseSupplies from _call_chooseSupplies

    "As I finish my prep routine, I hear my mom call me loudly."
    m "[player]! You better move your little tush and HURRY UP!"
    m "Your bus is here and you missed out on your farewell breakfast!"
    "I grab my backpack, about ready to have an anxiety attack."
    "Remember what the therapist told you."
    "Breathe in."
    "Breathe out."
    "In."
    "Out."
    "In..."
    "..."
    "Out."
    "..."
    "Alright, That's a little bit better."
    "Before I head out, I do a quick 180 and grab my water bottle."
    "Gotta stay hydrated."

    scene bg door with dissolve
    $ location = "Living Room"
    show screen in_game_ui
    "I turn my light off and rush down the stairs, shoving a piece of bacon into my mouth along the way."
    "I hear my mom shuffling around, waiting to send me off."
    "I wave goodbye to her and jump through the door to head outside."
    $ location = "Outside"
    show screen in_game_ui
    "All I see is a yellow bright bus with a few people on it."
    "Seems like a regular school bus, but I imagine that's sort of a disguise like nine and three-quarters."
    "My hands are shaking, as I feel my legs not wanting to move, but yet I'm getting closer to the bus."
    "The doors to the bus swing open and before I can even think, I stomp my way inside."
    "I climb on the bus and meet the friendly smile of the bus driver."
    "I give a weak smile and a wave back."
    bd "Welcome. Hope you'll enjoy your stay once you got yourself packed up."
    "I nod and start towards the end of the bus where I can sit in silence until I reach the academy."

    return
