# The game starts here.

label ch0_main:


    scene black

    #show yasuda at middle

    python:
        AddToBestiary(Mon.Monster('placeholder_portrait.png', 'Example Monster', 'Example Ability', 'This is a test description.'))
        AddToBestiary(Mon.Monster('placeholder_portrait.png', 'Example Monster 2', 'Example Ability 2', 'This is another test description.'))

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

    #scene bg room with dissolve
    "These labels society casts upon me and those with powers never leave my mind, and continue to do so while I lay in bed and let my blackout curtains protect me from the morning light."
    m "[player], breakfast tiiiime! Come and eaaat~"
    $m_name = "Mom"
    "Mom's been trying to get us to eat together as a family. Not really feeling like it right now."
    "But either way, might be a good time to wake up."
    "I drag myself out of bed, looking at my drawer before throwing myself right back in bed."
    "College's gonna be starting in like, a month, I should be getting used to waking up early."
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
    "Sent. There, that should get me some privacy."

    #stop music
    #play sound "audio/sfx/backpack_01.mp3"
    "{i}Rustle rustle.{/i}"

    #hide cg with dissolve

    "A noise comes from the side of my bed where I keep my backpack."
    "Something probably just fell near my bag. No worries."
    #play sound "audio/sfx/backpack_02.mp3"
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
    "There's an intruder in my house. I know I should scream, but I'm scared stiff."
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
    "I look at the card for a second, which has a logo on the back."
    "I then look at Libra, who stares at me for a bit."
    "Should I call the police?"
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
    "{i}Dear [player], I hope Libra and the tall one didn't scare you too much. I hereby formally enroll you into the girls' division of Hokkaido Ultra Dimension Academy.{/i}"
    "{i}We have noticed your supernatural ability and thought it would be the perfect time to enroll you into our school as our student of Phasing. It will give you the chance to learn and master your ability.{/i}"
    "{i}If you decide to accept, leave this card intact and we will send out further details. If you decline, please burn this letter.{/i}"
    "{i}We are looking forward to having you.{/i}"
    "{i}Sincerely, Headmaster Furukawa.{/i}"
    "What kind of nonsense is this?"
    "What school has someone break into their house and hand-deliver a letter?"
    "More importantly, I've heard of this school, but, is this really how any kind of school would recruit a student?"
    "This is shady at best."
    "I'll ask Mom more about it later to see if she knows anything."
    "Libra turns to me again, her childlike aura unwavering."
    lb "So um, I don't what the letter says, but I think it's good!"
    lb "Anyways, I was told to tell you that you got into my school, so that's very good news!"
    lb "I hope you enjoy university!"
    mc "Erm...thanks for the offer, but could you please leave my house?"
    lb "Okay!"

    #hide cg with dissolve
    "Limil retreats into the corner of my room while Libra simply opens my window and hops out."
    "I get up to try to stop her, but it's too late."
    mc "Wha-"
    "I run to the window to make sure the girl is alright, but when I look out, there's no trace of her left."
    "...I feel like drug trips are more normal than those two."

    #play music "audio/00_quiet_ambience.mp3" fadein 2.0
    "I head back to my bed and stare at the silhouette of the letter."
    "I can feel my stomach drop."

    "If this is true, why enroll me? I'm no one special."
    "I just go through things and people hate me for it."
    "It's nothing really spectacular. It's just weird."
    "I stumbled out of bed again for good, marking a reminder on my calendar for the start of the school year."
    "Afterwards, I went downstairs with a letter in hand and a mind full of questions."

    #scene bg kitchen with dissolve
    "I head to Mom, who's in the kitchen cleaning after having finished her breakfast."
    "Mom looks up at me smiling softly, but her attention is quickly averted to the letter."
    m "What's that, sweet pea?"
    "I show her the letter, feeling a weird sense of confusion and pride."
    "She seems to smile wider, as if she already knew what was on the paper."
    m "Oh my stars, you got accepted!"
    "I look at Mom very surprised."
    "How did she know about this?"
    "Maybe this has happened before?"
    mc "Mom, you have a power, right? Did you go to this place?"
    "She nods, feeling happy that she can finally talk about it."
    "She gets close to me, almost jumping at the opportunity to talk about the subject."
    m "I remember getting enrolled as the Student of Dreamscaping."
    m "Anything I can read, I can see a full picture and scene in my head. Like imagination, but stronger."
    m "I can create my own little worlds, inserting myself if I need to or spectating like I'm watching a movie."
    m "Thanks to that school, not only did I get to appreciate my power, but I made so many friends."
    "She begins to tell me all her stories about the school and the different types of people who went there."
    "Once you get her talking, she can go on and on about it until hell freezes over."
    m "...so that's how I met my roommate. And then, this one time, when we were in class..."
    "After about an hour of talking to her, I got tired quickly. "
    m "...at the festival, we all had a great time. Harukawa had the most beautiful display of..."
    "I start to zone out."
    "After her blabbering about her school experiences, I head back upstairs with an unnecessary large, but kind of interesting amount of information about the school."
    "But she also cleared up that the scouts hand deliver letters privately."
    "Glad to know that I wasn't in any danger."
    "Still, I think they should change their enrollment process {i}just{/i} a little bit."

    #scene bg room with dissolve
    "I go into my room, looking at my calendar, holding the letter still in my hands."
    "The one thing that stuck to my mind was the festival Mom mentioned they hold every year."
    "I try to imagine her story in my head like my mom, but I sure don't have an active imagination, nevermind Dreamscaping."
    "I start to feel down quickly as my anxiety presents itself again."
    "I head over to my bed to lay down."
    "I look around my room, wondering what it's going to be like to go to this new school."
    "My mind races fast."
    "What if I make no friends?"
    "No, that's silly. I'll probably make at least one friend."
    "But then again, I'm the biggest freak going to a school."
    "Maybe my power is different enough to make me an outcast?"
    "Maybe nobody will be impressed?"
    "My mind races a lot not knowing what to do."
    "My hands get clammy quickly and I roll over in bed."
    "I close my eyes both anticipating and dreading the first day of university."

    return
