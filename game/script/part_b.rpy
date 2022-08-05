label tmd_part_b:
  label .meet_balth:
    $ save_name = _("A stranger in the night...")
    play music "<silence 2.0>"
    queue music balthazar fadein 4.0
    scene cg balthcony with Fade(2.0, 1.0, 3.0)

    "The man was clearly injured,{w=0.25} cradling his shoulder the way he was{dots=4.5}"
    "Also,{w=0.25} who knows how long he'd rap against the glass?{w=0.5} I'd lose all my sleep!"
    "Hesitantly,{w=0.25} I approached the balcony glass and pulled it aside."
    "The strong chilly breeze hit me like a brick,{w=0.25} nearly knocking me back as the stranger stared in a mix of amusement and shock."

    balth "I'm surprised you actually invited me in, just who are you?"
    everett "We will have plenty to talk about once you're out of the cold."
    balth "Plenty to talk about?"

    "The stranger stepped forward out of the harsh elements as I closed the balcony glass behind him."

    everett "Make yourself at home I guess..."

    "There was no response from the stranger,{w=0.25} who stood dangerously still with his chin to the ground."

    everett "A name would be nice too."
    stop music fadeout 1.0

    balth   "..."
    everett "{dots=4.5}Stranger?"

    "The man still didn't reply as I came up behind him,{w=0.25} gently touching his shoulder to turn him around."
    scene black with Dissolve(0.25)

    # TODO: Thud sfx
    soundfx "thud.{w=0.25}{nw}"

    pause 2.0

    "He swayed back and forth before crumpling into the ground without notice."
    "My grip on his shoulder tightened as I swung an arm beneath his armpit to make sure he didn't fall."

    "Slowly, I lowered him to the ground on his knees. He was too heavy for me to keep on his feet."
    everett "This shoulder injury must be worse than I thought..."
    "Even unconscious,{w=0.25} the man concealed his wound,{w=0.25} though nobody could miss the crimson soaking through his clothes."

    everett "I guess we'll have to fix this before I get any answers..."
    "I looped both of my arms beneath his armpits and started dragging him towards my bed."

    pause 3.0

  label .hideaway:
    # TODO: Footstep scramble sfx

    guarda "Where is that criminal fiend?!"
    maid   "I hope Your Highness is okay!"
    guardb "He disappeared into the hedges near the Prince's balcony,{w=0.25} he has to be up there!"
    "My heart leapt to my throat at the sounds of the scullery maid and some guards faintly outside."

    scene bg bedroom
    show everett b frail:
      blur 5
      parallel:
        rflip
        linear 0.25 right
        lflip
        linear 0.25 left
        repeat
      parallel:
        easein 0.25 yoffset 20
        easein 0.25 yoffset  0
        repeat
      parallel:
        pause 0.5
        "everett a shame"
        pause 0.5
        "everett b cough"
        pause 0.5
        "everett c shame"
        repeat
    with Dissolve(1.0)

    "How could I hide the man in such a short time?"

    show everett a frown at rflipturn:
      blur 0 xalign 0.5
    everett "Why am I... doing so much... for you?!"
    "Because I wanted to hear about the outside, of course."

    show everett c cough at lflipturn
    everett "Come on! What could I do?"

    show everett b shame at rflipturn
    everett "Think Everett, think..."
    "Racking my head for a solution, the pillows flung beneath my blankets spawned an idea."

    # TODO: Lightbulb [metaphorical] SFX
    show everett a smile at lflipturn
    everett "The pillows! I'll hide him under my pillows and blankets!"

    # TODO: DRAG SFX
    show everett b frown:
      rotate_pad False
      ease 0.25 ypos 0.5 rflip
      "everett b cough"
      pause 1.25
      ease 0.5 ypos 0.0
      parallel:
        ease  0.8 xalign  0.25
        pause 0.6
        ease  0.8 xalign  0.00
        pause 0.6
        ease  0.8 xalign -0.25
        pause 0.6
        ease  0.8 xalign -0.50
        pause 0.6
        ease  0.8 xalign -0.75
        pause 0.8
        ease  0.4 xalign -1.00
        pause 0.8
      parallel:
        linear 0.4 rotate -5
        linear 0.4 rotate  0
        pause  0.6
        repeat
    show balth a:
      rotate_pad False rotate -5
      xalign 0.65 ypos 1.0 matrixcolor TintMatrix("#111") blur 5 rflip
      pause 1.5
      ease 0.5 ypos 0.25
      parallel:
        ease  0.8 xalign  0.40
        pause 0.6
        ease  0.8 xalign  0.15
        pause 0.6
        ease  0.8 xalign -0.10
        pause 0.6
        ease  0.8 xalign -0.35
        pause 0.6
        ease  0.8 xalign -0.60
        pause 0.6
        ease  0.8 xalign -0.85
        pause 0.6
        ease  0.8 xalign -1.10
      parallel:
        linear 0.4 rotate -10
        linear 0.4 rotate  -5
        pause  0.6
        repeat
    with None
    scene black with MultipleTransition((False, Pause(4.0), False, Dissolve(4.0), True))

    "I hastened my grip and dragged the man towards the side of the bed. Half leant against the bed, I pull him on top trying not to lose my breath."
    "This was the most exertion I've had in awhile. My arms shook from the effort."

    "When half of the man was on the bed, I pushed the rest of him up and immediately flung pillows and blankets on top trying to make it look neat."
    "Taking a deep breath, I ran my fingers through my hair and straightened up trying to rub away the hot feeling in my face."
    "Look normal, Everett."
    "Inhale..."

  label .guests:
    $ save_name = _("Uninvited guests...")
    play sound knock_knock
    soundfx "knock{w=0.25} knock{w=0.25} knock!{w=0.25}{nw}"

    "They were quick!"

    play music everett fadein 2.0

    scene bg bedroom
    show everett c frown at right, rflip
    with Dissolve(2.0)

    maid "Your Royal Highness!{w=0.25} Is everything alright in there?"

    everett "Everything{dots=4.5} {nw}"
    show everett a shame at lflipturn
    extend "is fine,{w=0.25} Miss! {w=0.15}{nw}"
    extend smile "Nothing is wrong here."
    everett smile "What is the matter that you have to wake me up so late?"

    maid "I'm so sorry,{w=0.25} Your Royal Highness,{w=0.25} but we must come in. There is a minor{dots=4.5} disturbance we need to check out."

    show everett c frown
    "So they're keeping me in the dark about him?"

    everett b grimace "If you must,{w=0.25} come in."

    play sound door_open
    show everett c smile:
      parallel:
        linear 1.0 center
      parallel:
        easein 0.2 yoffset 12
        easein 0.3 yoffset  0
        repeat 2
    show maid worry at rflip:
      xalign -0.5
      parallel:
        linear 1.5 leftest
      parallel:
        easein 0.2 yoffset 20
        easein 0.3 yoffset  0
        repeat 3
    show guard as guard_a:
      xalign -1.0
      parallel:
        linear 1.0 right
      parallel:
        easein 0.2 yoffset 50
        easein 0.3 yoffset  0
        repeat 2
    show guard as guard_b:
      xalign -1.0
      parallel:
        linear 1.0 rightest
      parallel:
        easein 0.2 yoffset 50
        easein 0.3 yoffset  0
        repeat 2

    "The door slowly opened to the scullery maid and two guards behind her."
    "They brandished their swords clear as day as the maid quickly lit all the candles."
    show bg lit with dissolve
    "The maid stood by the door with her candle as the guards explored the room."
    show guard as guard_a:
      rflipturn
      pause 0.25
      ease 0.8 xalign 2.0
    show  guard as guard_b:
      rflipturn
      pause 0.25
      ease 0.5 xalign 2.0
    "They mainly focused their attention on the balcony glass."
    "Fortunately,{w=0.25} they didn't think to check the bed."

    maid "Are you sure you're alright,{w=0.25} Your Highness?{w=0.25} Your cheeks are flush."
    everett frown @ grimace "Are they now?"

    "I tried to sound surprised,{w=0.25} but instead it comes out as sarcastic and I bite the inside of my cheek.{w=0.25} The maid will not receive my irritation tonight."

    everett a smile "Must be from before I retired to bed.{w=0.25} It's awfully cold outside."
    maid "...truly."

    "We fell into silence again as the guards finished investigating every crevice. {w=0.25}{nw}{done}I leaned back slightly onto the bed, just to deter them from checking there."
    show guard as guard_a:
      lflip
      parallel:
        linear 1.0 right
      parallel:
        easein 0.2 yoffset 50
        easein 0.3 yoffset  0
        repeat 2
    show guard as guard_b:
      lflip
      parallel:
        linear 1.0 rightest
      parallel:
        easein 0.2 yoffset 50
        easein 0.3 yoffset  0
        repeat 2
    "We fell into silence again as the guards finished investigating every crevice. {fast}I leaned back slightly onto the bed,{w=0.25} just to deter them from checking there."

    everett "I hope everything is alright."
    maid smile @ worry "Oh it is!{w=0.25} We were just checking for some{dots=3.0} critter.{w=0.25} It doesn't seem to be in here so no need to worry."
    everett "Is that so?{w=0.25} I'm glad.{w=0.25} Thank you everyone for making me feel safe."

    show bg:
      matrixcolor BrightnessMatrix(0.0)
      easein 0.5 matrixcolor BrightnessMatrix(0.05)
    "The mood in the room lightened a little as the scullery maid smiled warmly."

    maid "We will be off now,{w=0.25} get some rest."
    everett "Goodnight,{w=0.25} miss."
    maid "Goodnight to you,{w=0.25} Your Royal Highness."

    stop music fadeout 4.0

    show maid:
      rflip
      yalign 1.0
      easein  0.25 ypos 1.05
      easeout 0.25 ypos 1.00
      lflipturn
      parallel:
        linear 3.0 xpos -1.0
      parallel:
        easein 0.2 yoffset 20
        easein 0.3 yoffset  0
        repeat
    show guard as guard_a:
      pause 0.33
      yalign 1.0
      easein  0.2 ypos 1.1
      easeout 0.2 ypos 1.0
      parallel:
        linear 3.0 xpos -1.0
      parallel:
        easein 0.2 yoffset 50
        easein 0.3 yoffset  0
        repeat
    show guard as guard_b:
      pause 0.66
      yalign 1.0
      easein  0.2 ypos 1.1
      easeout 0.2 ypos 1.0
      parallel:
        linear 3.0 xpos -1.0
      parallel:
        easein 0.2 yoffset 50
        easein 0.3 yoffset  0
        repeat
    "With a curtsy from her and a bow from the guards,{w=0.25} they left as quickly as they came in."
    hide maid
    hide guard_a
    hide guard_b
    play sound door_shut
    stop music
    show everett b frown:
      yalign 1.0
      easein  0.25 zoom 1.03
      "everett b cough"
      easeout 0.25 zoom 1.00
    "As soon as their footsteps went quiet,{w=0.25} I let out the breath that I didn't realize I was holding back."
    scene black with Dissolve(1.25)
    "I turned towards the bed and gently pulled the blankets off to see if the stranger was still there."
    "To my irrational surprise,{w=0.25} he was."
    "Though now that danger wasn't looming,{w=0.25} I realized I never got a good look at him."

  label .bedthazar:
    $ save_name = _("Rest for the wicked...")
    "{dots=3.0}"

    play music "<silence 2.5>"
    queue music balthazar fadein 4.0
    scene cg bedthazar with Fade(2.0, 1.0, 3.0)

    "The man had long,{w=0.25} wispy blonde locks that cascaded down from his shoulders to his chest."
    "He was dressed in a gentleman's outfit,{w=0.25} with a noticeable scar poking from the top of his collarbone."
    "I felt self conscious in his presence,{w=0.25} leaned over him like he was some sleeping beauty and I was the prince."
    "He could probably win people from both sides,{w=0.25} he was certainly winning me over."
    "{dots=2.0}{w=0.25}Why did I say that?!"
    "My face felt hot to the touch,{w=0.25} and it definitely wasn't from the exercise."
    "I tenderly raised my hand to his bloody shoulder,{w=0.25} trying to gauge the damage without waking him up."
    "From this position,{w=0.25} blood also stained his side."
    "He must've been shot twice,{w=0.25} one in the shoulder and one in the side."

    everett "No wonder you wanted to rest here{dots=4.5}"
    everett "I guess I'll have to patch you up before I get any answers."

    "Thankfully Mother hired the best teachers to instruct me on medicine. Just so I can always take care of myself and cure any ailment that befalls me."

    everett "Now where had I left that first aid kit{dots=4.5}"
    "Beneath the bed,{w=0.25} I pulled the cumbersome first aid kit and dropped it on the bedside rolling my sleeves up."
    everett "I hope this works{dots=4.5}"

    stop music fadeout 4.0
    scene black with Fade(4.0, 1.0, 0.0)
    stop music

    pause 2.0

  label .monolog:
    prolog """
    Prince Everett worked for hours on the stranger.

    Undressing him was rather a hassle, as he tried not to get humiliated by his own physique staring at the stranger's muscular one.

    He didn't have any bottles of whisky to ease the man's pain in case he woke up, so he had to work fast.
    A long, arduous procedure began with carefully removing the bullets from both gun wounds.
    They were both made of silver and very expensive.

    That process took up most of his time, with a few candles lit. After that was completed, he cleaned the wound with some water.
    Some poultice was put on top and he went to work sewing the holes shut.

    Then clean white bandages would carefully be wrapped across his stomach and shoulder.

    It was the best he could do at this time, though this stranger would probably have to go to the hospital soon.
    Everett wouldn't be surprised if the man became feverish afterward.
    """

  label .post_monolog:
    $ save_name = _("Sixty minutes from midnight...")

    scene bg bedroom
    show everett c smile
    with Dissolve(1.25)

    "Wiping away the beads of sweat,{w=0.25} I breathed out a sigh of relief knowing the man should be okay for the night at least."
    everett b shame @ a smile "That should do it."

    play sound clock_gong
    show everett b shame:
      easein  0.1 yzoom 1.01
      easeout 0.1 yzoom 1.00
      pause 3.3
      repeat 3
    $ renpy.pause(11.0, hard=True)

    play music everett fadein 4.0

    "Eleven o'clock.{w=0.25} The fireworks would light up the sky by now."
    show everett c grimace
    "There was no chance I would fall back asleep with him in my bed{dots=4.5} I might as well stay up and watch."
    show everett shame
    "Speaking of him{dots=3.0}"

    "My fingers brushed down his bare chest,{w=0.25} the sheets beneath him stained with blood from the procedure."

    everett frown "What mess did you wrap yourself in, to end up in this sorry state?"
    show cg balthcony eyes:
      alpha 0.0
      ease 0.2 alpha 0.75
    balth "Nothing I couldn't handle, of course."
    show everett c shame:
      ease 0.75 right
    hide cg
    show balth a smirk at lefter:
      matrixcolor TintMatrix("#000") xzoom -1.0
    with Dissolve(0.75)
    show balth:
      easein 0.75 matrixcolor TintMatrix("#FFF")
    with Dissolve(0.75)

    "I stifle a gasp as the mans eyes slowly open, landing on mine."
    "He shouldn't have awakened so early{dots=4.5} not with his injuries."
    "Who exactly was he?"

    everett a frown "Are you okay?{w=0.25} I tried to patch you up the best I could."
    show balth c frown
    "The man blinked and checked his shoulder confused.{w=0.25} He was surprisingly mobile for someone with bullet wounds."

    balth a smile "I'm doing better thanks to you."
    everett c frail "But you're so pale{dots=4.5}"
    show balth frown

    "I didn't want to sound rude,{w=0.25} but it was so noticeable."
    "Was he sickly like me?"
    "It couldn't be.{w=0.25} This man somehow found his way onto my balcony,{w=0.25} which isn't a close climb from the ground."

    balth c smirk "That's my natural complexion,{w=0.25} nothing for you to worry about."

    show balth a smile:
      parallel:
        ease 0.34 leftest
        ease 0.66 righter xzoom 1.0
      parallel:
        pause  0.34
        linear 0.33 blur 30
        linear 0.33 blur  0
    show everett c cough:
      pause 0.5
      parallel:
        ease  0.5 left xzoom -1.0
      parallel:
        linear 0.25 blur 30
        linear 0.25 blur  0
    everett "Be careful!"
    "The man sat up easily, showing no signs of pain or discomfort."
    everett b frown "...or you'll hurt yourself again."

    balth smirk "Impossible, thank you for taking care of me."
    balth c smile "I'll remember this act."

    "He tossed the covers off of him and stood up. I winced at the sight, but he was already heading towards the balcony glass."
    everett "Wai-wait!"

  label .whiteboy_wasted:
    $ save_name = _("A breathtaking affair...")

    camera:
      align (0.8, 0.25)
      ease 1.0 zoom 30.0 blur 1000
    scene cg balthcony with dissolve
    camera:
      align (0.5, 0.3)
      ease 1.0 zoom 2.0 blur 0

    "I scramble on the other side of the bed getting to my feet."
    everett "Where are you going?{w=0.25} You're still hurt!"
    "The man's speed didn't slow down."
    camera:
      align (0.5, 0.3)
      ease 1.0 zoom 60.0 blur 1000
    scene bg balcony
    show everett c cough:
      xalign -1.0 xzoom -1.0
      linear 1.0 xalign 0.15
    show balth a smirk at right
    with dissolve
    camera:
      align (0.65, 0.15)
      ease 1.0 zoom 1.0 blur 0

    balth "I will be fine,{w=0.25} trust me.{w=0.25} This is nothing."
    everett frown "Couldn't you stay a little longer?{w=0.25} Just to make sure your injuries don't reopen{em}"
    balth smile "That won't be necessary."
    everett c frail @ a frown "No{dots=3.0} please don't go{em}"
    show everett:
      rotate_pad False
      parallel:
        ease 0.75 center rotate 30 yoffset 100
      parallel:
        easein  0.5 zoom 1.03
        easeout 0.7 zoom 1.00
        repeat
    camera:
      matrixcolor ContrastMatrix(1.0) align (0.75, 0.5)
      ease 1.5 blur 100 matrixcolor ContrastMatrix(-1.0) zoom 2.5
    show balth shock:
      ease 1.25 rightest
    "My chest grew tight,{w=0.25} straining to get a proper breath in."
    show balth:
      pause 1.0
      lflipturn
      pause 0.2
      rflipturn
      pause 1.2
      ease 0.5 xalign -1.0

    "No{dots=3.0} not now, not now!"
    "My head whips around in a dizzy confusion,{w=0.25} patting around me trying to find something."
    camera:
      matrixcolor ContrastMatrix() blur 300
    with Dissolve(0.5)

    "What was I trying to find?{w=0.25} Think,{w=0.25} Everett,{w=0.25} think!"
    "The lack of air made my vision go blurry."
    "I gasp for air,{w=0.25} feeling the air sucked out of my body doubling me over."
    "I couldn't focus on anything,{w=0.25} only feeling my body grow heavier and the carpet sticking to my sweaty forehead."
    show balth:
      xzoom -1.0
      ease 0.5 center
    "Stop looking pathetic Everett!{w=0.25} Keep asking him to stay{em}"
    "Something was shoved into my hands,{w=0.25} and I pry open one eye to see my inhaler magically there."
    "With my hands shaking,{w=0.25} I immediately lean my head back and inhale the medication."
    stop music
    scene black
    with fade
    "Slowly,{w=0.25} but surely,{w=0.25} the tightness in my chest went away.{w=0.25} The blurriness dissipating as well."

    play music "<silence 2.0>"
    queue music balthazar fadein 4.0

    scene bg bedroom
    show balth a aloof:
      align (0.25, 1.0) ypos 1.25 xzoom -1.0 rotate 5
    show everett c cough:
      align (0.65, 1.0) ypos 1.40 rotate -25
    camera:
      align (0.5, 0.75)
      blur 2.5 zoom 2.0
    with Dissolve(1.5)
    "When my vision cleared,{w=0.25} the man was kneeling right in front of me with an unreadable expression."

    balth shock "Are you okay?"
    everett frown "Yea-{w=0.25}yeah{dots=4.5}"

    show everett shame
    "I didn't notice it until now,{w=0.25} but the stranger's hand was on my back."
    show everett cough:
      ease 0.05 xoffset -2
      ease 0.05 xoffset  0
    "A shiver ran through me."

    balth frown "Why do you want me to stay?"

    "I froze,{w=0.25} feeling the heat returning to my face as I bowed my head in shame."
    show everett shame
    "What was I doing?{w=0.25} Forcing a stranger to stay in your room is kidnapping right?"

    everett frown "I{dots=4.5}"
    everett "I just wanted to hear about the outside{dots=4.5}"
    everett "I haven't left this room since I was a little kid.{w=0.25} My parents keep me here to prevent any over-exertion."
    everett grimace @ frown "As you saw,{w=0.25} I'm not the healthiest guy out there{dots=4.5}"

    show everett:
      pause 0.1
      ease 0.05 xoffset -2
      ease 0.05 xoffset  0
      "everett c frail"
    "I tried to chuckle,{w=0.25} but it almost brought on a coughing fit which made my chest tighten slightly."

    everett frail "I'm sorry,{w=0.25} I shouldn't force you to stay."
    everett "I just really want to hear about the sights and smells and the sort."
    everett "You know?"

    balth smirk "I think I understand now."
    show balth:
      rotate_pad False
      ease 0.5 ypos 1.0 rotate 0
      pause 0.25
      lflipturn
      pause 0.2
      parallel:
        linear 1.5 leftest
      parallel:
        easein  0.2 yoffset 20
        easeout 0.3 yoffset  0
        repeat 3
      ease 0.2 xzoom -1.0
    show everett shame
    "My eyes widen as the stranger gets up,{w=0.25} walking towards the bed to lean against it."

    balth "If only to repay your generosity,{w=0.25} I'll stay and share with you what you wish to hear."

    show everett smile:
      rotate_pad False
      pause 0.1
      ease 0.05 xoffset -2
      ease 0.05 xoffset  0
      ease 0.5 ypos 0.0 yalign 1.0 yoffset 0 rotate 0
    camera:
      pause 0.2
      ease 0.5 zoom 1.0 blur 0
    "My heart skips a beat,{w=0.25} a smile growing as I eagerly stood."

    everett "Really?{w=0.25} You'll stay?"

    balth "Just for a little while,{w=0.25} you wish to hear from the outside,{w=0.25} right?"
    balth "Fortunately for you,{w=0.25} I carry many stories{dots=4.5}"

    stop music fadeout 2.0
    scene black with Dissolve(2.0)

  scene black
  stop music
  return
