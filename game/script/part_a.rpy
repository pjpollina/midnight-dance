label tmd_part_a:
  label .prolog:
    $ save_name = _("Prologue")

    play music nearby_party fadein 4.0
    prolog "Voices carried across the wind, full of excitement and apprehension."

    show brl pro a with Dissolve(2.0)

    prolog """
    Will they find their lover in the onslaught between suitors?

    Will the timid wallflower bloom into a sensation overnight?

    Much was left to the imagination, at least for those who waited with bated breaths to attend.
    """

    show brl pro b with Dissolve(2.0)

    prolog """
    All except for the sickly prince, who from his balcony cast a longing glance towards the crowds.

    From where his manor was, he could gaze into the throes of well-mannered gentlemen and gorgeously
    elegant women streaming into different buildings every night.

    Every night came with a new ball to attend. Another chance to prove yourself.

    Or lose yourself against the night.

    With a deep, heaving sigh that expelled any energy left, he rested his chin on his palm.

    Oh, how deeply he wished he could attend...
    """

  label .post_prologue:
    $ save_name = _("The lonely prince...")

    stop  music fadeout 3.0
    queue music distant_party fadein 3.0
    scene bg balcony
    show everett b smile at rflip, right
    with Fade(2.5, 1.0, 2.5)

    "A feeling of profound melancholy overcame me as I watched the last of the crowds disappear into the ball."
    "The same night,{w=0.25} every night,{w=0.25} when the arching loneliness overwhelmed me at the sights."
    "The sights of people dressing up and dedicating a night to sway and dance."
    "Oh,{w=0.25} how the looks of excitement made me tap my fingers against the iced railing."

    everett c "Are the lights as bright as I've come to hear? Do they blind you? Bathe you in their warmth as your blood pumps with adrenaline?"
    everett "Are the floors smooth enough to take in every stride,{w=0.25} every waltz step that we've trained to do since little?"
    everett frown "{dots=6.0}"
    everett "Will I ever see that light? Those floors? The dancers in their ball gowns and suits?"

    "I grit my chattering teeth,{w=0.25} trying to tune into the live music playing indoors."
    "There was no sound over the breeze. Nothing but the wind and the tapping of my nails."
    "I don't want to think of it,{w=0.25} yet I do."
    "Every night,{w=0.25} the same thought in my mind."

    everett shame "Is the food good?"
    everett smirk "The maids often talk of dancing on an empty stomach."
    everett "No lady,{w=0.25} especially on her debutante,{w=0.25} would want to look bloated in their tight corsets."

    "The high stakes! How exciting it was to imagine all the preparation for the night to start."
    "It was regulated highly,{w=0.25} according to the strictest code of good-breeding."
    "I think I would still enjoy it,{w=0.25} even moreso because of the rules. It would make for an exciting night."
    "Truly! An invigorating night."

  label .maid_intro:
    $ save_name = _("A maid's plight...")

    everett shame @ frown "Maybe{em}"

    voice audio.maid("a01")
    maid "{size=+8}Your Royal Highness!{/size}"

    show maid worry at rflip, runon_lefter
    "A concerned voice breaks me out of my train of thought."
    show maid worry at rflip, lefter

    voice audio.maid("a02")
    maid "You cannot be out here! It is far too chilly for your fragile body. Allow me to accompany you back inside."

    "I sigh once more,{w=0.25} {nw}{done}turning to face her with a frown."
    show everett b frown at lflipturn
    "I sigh once more, {fast}turning to face her with a frown."

    everett frail "Couldn't I enjoy the sights longer? It is the only good entertainment I get from this prison{em}"

    voice audio.maid("a03")
    maid "This is far from a prison,{w=0.25} Your Royal Highness! It was decorated with your interests in mind."
    voice audio.maid("a04")
    maid "There are others less fortunate to live in such chambers as yours."

    everett smirk "Well at least they are given the freedom to leave if they dislike it."

  label .maid_drag:
    ## Setup
    show everett shame
    show maid:
      easein 0.2 center
    pause  0.5

    ## Execution
    show maid at center:
      parallel:
        linear 0.4 xalign  0.25
        linear 0.4 xalign  0.00
        linear 0.4 xalign -0.25
        linear 0.4 xalign -0.50
        linear 0.4 xalign -0.75
      parallel:
        easein 0.2 yoffset 20
        easein 0.3 yoffset  0
        repeat 5
    show everett:
      parallel:
        linear 0.4 xalign  0.50
        linear 0.4 xalign  0.25
        linear 0.4 xalign  0.00
        linear 0.4 xalign -0.25
        linear 0.4 xalign -0.50
        linear 0.4 xalign -0.75
      parallel:
        easein 0.2 yoffset 20
        easein 0.3 yoffset  0
        repeat 5
    stop music fadeout 2.5
    show black with Dissolve(2.5)

  label .bedtime:
    $ save_name = _("The maid in the candlelight...")

    "The scullery maid took my wrist,{w=0.25} pulling me back inside despite my protests."

    scene bg bedroom lit
    show everett b frown at rflip, lefter
    with Fade(0.0, 1.0, 2.0)
    play music everett fadein 5.0

    play sound [door_shut, "<silence 0.25>", curtain_shut]
    "She closed the balcony doors and pulled the curtains from either side to conceal the outside."
    "And any joy I had from gazing at the night."

    show maid worry at walkon_right
    pause 1.5
    show maid at right

    voice audio.maid("a05")
    maid "Why are you out of bed again? If Your Majesty knew of this she would remove me for my incompetence."

    everett a "You know why,{w=0.25} I want to be out there. There is nothing in this room I haven't seen ever since I was born."
    everett c "I'm not even allowed to explore the manor as often as the commoners who visit."

    voice audio.maid("a06")
    maid "It's for your own safety,{w=0.25} you know how frail you are. You'd fall over flushed if you stayed out there in the cold."
    voice audio.maid("a07")
    maid "You aren't a healthy person,{w=0.25} Your Highness{em}"

    everett smirk "And you think I'm foolish enough to not realize that?! I didn't ask for the opinion of a servant that leaves every morning!"
    show everett b cough
    show maid:
      ease 0.05 rflip matrixcolor SaturationMatrix(0.75)

    "I couldn't take back the words as they slipped out. But my heart dropped at the sight of the maid whose shoulders fell."
    everett "I just want to leave,{w=0.25} I'm terribly sorry for my attitude. I've grown crazy about these same walls."
    show everett at lflipturn

    "In my hushed tone,{w=0.25} I look away from her and towards the wall. The shadows flicked alongside it from the candlelight."
    "They were{dots=4.5} almost dancing."

    voice audio.maid("a08")
    maid "I'm{dots=4.5} I'm sorry Your Highness,{w=0.25} I can't fathom how difficult it is to be in your position."

    "I glanced towards her to see her crestfallen expression,{w=0.25} still gathering her thoughts in her balled up hands."
    "She was picking her words wisely. This wasn't another monologue sent from mother."

    voice audio.maid("a09")
    maid "Me and the others would love to see you outdoors... but Your Majesty asks we keep an eye on you. To keep you safe,{w=0.25} that is."
    voice audio.maid("a10")
    maid "The most I can do is ask her to change her mind. But we are just following her decree."
    voice audio.maid("a11")
    maid "Maybe if we assign an attendant to you then she will lift some of the rules."

    "I didn't know how to reply to that. That was the same idea I proposed months ago."
    "Mother still said no to it,{w=0.25} saying that it was safer if I stayed here."

    voice audio.maid("a12")
    maid "{dots=4.5}I will try my hardest,{w=0.25} Your Highness."
    voice audio.maid("a13")
    maid "But please,{w=0.25} do get some rest. You really worry us sometimes."
    voice audio.maid("a14")
    maid "If just for one more night,{w=0.25} please get a good rest so I may bring up the topic tomorrow with Your Majesty."

    "That was as good as it was going to get with Mother. Though I respected the scullery maids' boldness in asking the Queen to reframe her decision."
    "I couldn't send the frenzied maid away with more worries.  With every reluctance clinging to my body,{w=0.25} I turned towards my bed to hide my irritation."

    everett frown "I concede,{w=0.25} please retire for the night Miss."
    "The sound of clapping reassured me that her feelings weren't hurt anymore,{w=0.25} now that she had won."

    show maid smile at lflipturn
    voice audio.maid("a15")
    maid "Of course Your Highness! Allow me to dim the lights."

    stop music fadeout 4.0

  label .goodnight:
    $ save_name = _("A room lit only by smiles...")

    scene bg bedroom:
      matrixcolor TintMatrix("#FFF")
      ease 1.5 matrixcolor TintMatrix("#8E7DAC")
    show maid smile at right:
      matrixcolor TintMatrix("#FFF")
      ease 1.5 matrixcolor TintMatrix("#8E7DAC")
    with Dissolve(1.5)
    $ renpy.pause(2.0, hard=True)

    play sound into_bed
    "I settled on the bed as the maid blew the candles out."
    "All were blown out except for the one in her hand. The single flame illuminating her caring expression."

    show maid:
      parallel:
        linear 1.0 left
      parallel:
        easein 0.25 yoffset 20
        easein 0.25 yoffset  0
        repeat 2

    play sound into_bed
    "She came to my side,{w=0.25} gently throwing the blankets over me tucking me in."

    everett "Thank you,{w=0.25} Miss."

    voice audio.maid("a16")
    maid "Anything for you,{w=0.25} Your Highness."

    show maid:
      rflipturn
      pause  1.6
      lflipturn
    $ renpy.pause(2.2, hard=True)

    voice audio.maid("a17")
    maid "Goodnight."

    everett "Goodnight."

    show bg:
      easeout 6.0 matrixcolor TintMatrix("#342948")
    show maid:
      rflipturn
      pause 0.75
      parallel:
        easeout 6.0 matrixcolor TintMatrix("#342948")
      parallel:
        linear 3.0 xalign 1.5
      parallel:
        easein 0.3 yoffset 20
        easein 0.4 yoffset  0
        repeat 5
    $ renpy.pause(3.5, hard=True)

    play sound door_shut volume 0.5
    play music hollow_wind volume 0.25 fadein 4.0

    "Whispering her farewell,{w=0.25} she stood upright and left the room in the same hurry she came in."
    "{dots=4.5}"
    "All that remained was a still silence{dots=4.5}"
    "The sort that feels{dots=3.0} suffocating,{w=0.25} despite nothing being there."
    "Even as I closed my eyes{dots=4.5} it made no difference."

    stop music fadeout 4.0

    camera:
      easein 0.15 matrixcolor TintMatrix("#999")
      easein 0.15 matrixcolor TintMatrix("#FFF")
      pause 0.5
      easein 0.25 matrixcolor TintMatrix("#444")
      easein 0.35 matrixcolor TintMatrix("#AAA")
    $ renpy.pause(2.2, hard=True)
    scene black with Dissolve(2.0)
    $ renpy.pause(2.2, hard=True)

  label .nosleep:
    $ save_name = _("A restless heart...")

    "{size=+4}{dots=4.5}{p}\n{dots=3.0}{p}\n{dots=1.5}{/size}"

    turmoil """
    Why did I expect sleep would come easily?

    I would rather be dancing the night away,{awt}just to return home by the early dawn.

    Maybe with my eyes half-lidded from how tired I was.

    Possibly{dots=3.0}{awt}with someone by my side who would wish to dance more afterwards...

    If I were to dance with someone,{awt}anyone,{awt}this restless feeling in my legs would surely go away.

    Then I could sleep peacefully{dots=3.0}{awt}knowing something awaited me the next day.

    Another dance.{awt=2.0}The waltz,{awt}maybe.

    Before long,{awt}with the images of dancing in my mind,{awt}my eyelids grew heavy{dots=3.0}{awt}and I drifted off to sleep.
    """

    pause 2.0

  label .tapping:
    $ save_name = _("The tap on the window...")

    play sound tap_tap_tap
    soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

    "..."

    play sound tap_tap_tap
    soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

    everett "Nmh..."

    play music hollow_wind volume 0.25 fadein 3.0
    scene bg bedroom:
      matrixcolor TintMatrix("#333")
    with Fade(0.0, 1.0, 2.0)

    "It was pitch dark when my eyes opened,{w=0.25} everything remained as still as it was when I fell asleep."
    "What woke me up?"

    play sound tap_tap_tap
    soundfx "{alpha=0.66}tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{/alpha}{nw}" (what_xalign=0.85)

    "It sounded like it came from the balcony."
    "Was it a bird trying to come in?{w=0.75} Or a twig from a long tree?"
    "Despite my many protests the night before,{w=0.25} I was comfortable in bed and didn't want to leave."
    "The blankets were warm and fuzzy against my skin,{w=0.25} and it felt like clouds between my heavy limbs."

    everett "Maybe I should ring for her{dots=6.0}"

    "She wouldn't want me getting out of bed during these later hours."
    "Especially when it gets chillier."
    "Or maybe{dots=6.0}"
    scene black with dissolve
    pause 1.0

    "I couldn't help myself as my eyes closed once again. The steady rise and fall of my chest luring me back into sleep."

    play sound tap_tap_tap volume 0.75
    soundfx "{size=-4}tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{/size}{nw}"

    "{dots=4.5}"

    play sound tap_tap_tap volume 1.0
    soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"
    pause 0.5

    play sound tap_tap_tap volume 1.25
    soundfx "{size=+4}{b}tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{/b}{/size}{nw}"

    "{cps=4.0}...!{/cps}"

    scene bg bedroom:
      matrixcolor TintMatrix("#333")
    with Fade(0.0, 1.0, 2.0)

    play sound tap_tap_tap
    soundfx "{alpha=0.66}tink.{w=0.25}{size=+4} tink.{w=0.25}{/size}{size=+8} tink.{w=0.25}{/size}{/alpha}{nw}" (what_xalign=0.85)

    "This wasn't going{dots=6.0} to work."
    "With the last bit of energy I had,{w=0.25} my legs slowly kicked over the side of the bed."
    play sound into_bed
    "I fumbled with lighting a candle,{w=0.25} but eventually gave up and headed towards the balcony."
    "If the balcony was so insistent on keeping me awake,{w=0.25} I hope it brought me something entertaining."
    "Like a balcony size ball,{w=0.25} just for me."
    "But not a bird,{w=0.25} or a twig."

    play sound curtain_open
    show bg:
      easein 0.5 matrixcolor TintMatrix("#555")
    "In front of the balcony glass,{w=0.25} I grabbed the curtains and slowly pulled them aside."
    "Nothing was there."
    "It was hard to see already in the darkness,{w=0.25} but not a single scratching sound or sight to behold."
    "I tried to hide my resentment towards the situation,{w=0.25} but it inevitably showed on my face most likely."

    everett "Is that all,{w=0.25} World?{w=0.75} Willing to throw me a bone but not meat on it?"
    everett "If only I could show you."

    play sound curtain_shut
    show bg:
      easeout 0.5 matrixcolor TintMatrix("#333")
    "As I closed the curtains,{w=0.25} the same sound came again from outdoors."

    play sound tap_tap_tap
    soundfx "{alpha=0.66}tink.{w=0.25}{size=+4} tink.{w=0.25}{/size}{size=+8} tink.{w=0.25}{/size}{/alpha}{nw}" (what_xalign=0.85)

    play sound curtain_open
    show bg:
      easein 0.5 matrixcolor TintMatrix("#555")
    "Royally irritated,{w=0.25} I flung the curtains back open ready to roll my sleeves up and suffocate what poor thing was out there making that sound."
    "But I stopped."

  label .darkness:
    $ save_name = _("Those eyes of crimson...")

    scene cg balthcony dark:
      align (0.5, 1.0) zoom 2.5
      linear 30.0 yalign 0.0
    with Dissolve(1.0)

    "Instead a bird,{w=0.25} animal,{w=0.25} or even a stray twig brushing against the glass{dots=6.0}"
    "A tall man was there,{w=0.25} nursing his right shoulder with his back turned towards me."
    "I couldn't see much,{w=0.25} but the man seemed to be hunched forward,{w=0.25} slightly panting{dots=6.0}"
    everett "He{dots=3.0}"

    "A greeting slips past me and disappears at the tip of my tongue."
    "What would I say to this stranger?"
    "My breath hitched in my throat as the strangers' eyes met mine."

    show cg eyes:
      align (0.5, 0.5)
    with Dissolve(1.0)

    "My blood ran cold."
    "His eyes were cold and clear on the surface. The crimson color shone strangely while the rest of him was concealed in the darkness."
    "Those red eyes... they were as red as blood."
    # TODO: Heartbeat sfx
    "My heart skipped a beat,{w=0.25} threatening to leap out of my chest."

    "What... who was I staring at?"
    "Unable to control the fear seizing my legs,{w=0.25} I stepped backwards slowly."
    "Maybe he couldn't see me through the glass,{w=0.25} maybe this was just a coincidence."
    "Maybe this was a dream."
    "But the stranger's eyes shone in recognition,{w=0.25} and he gently rapped against the balcony glass."

    play sound tap_tap_tap
    soundfx "{alpha=0.66}tink.{w=0.25}{size=+4} tink.{w=0.25}{/size}{size=+8} tink.{w=0.25}{/size}{/alpha}{nw}"

    voice audio.balth("a01")
    balth "May I seek refuge here,{w=0.25} stranger?"
    voice audio.balth("a02")
    balth "I've come a long way{dots=3.0} and I need rest."
    voice audio.balth("a03")
    balth "Harm will not come to you if you choose this."

    "{dots=6.0}What?"
    "I gawked at him in full surprise,{w=0.25} trying to gather what he was asking."
    "A stranger with strange red eyes and an injured shoulder showing up on his balcony asked for refuge?"
    "Did he not realize who I was?"

  label .choice:
    $ save_name = _("A fateful decision...")

    "{cps=*0.75}I bit my bottom lip,{w=0.25} trying to not make anymore eye contact with the stranger. I...{/cps}{w=0.25}{nw}"(what_yoffset=-50)
    menu:
      extend ""
      "Leave the man outside.":
        $ save_name = _("A chance squandered...")

        play sound ["<silence 1.5>", curtain_shut]
        pause 1.5
        scene black with ImageDissolve("masks/curtain.webp", 0.15)
        pause 2.0

        turmoil """
        Without looking at him,{awt}I slowly step forward and close the curtains abruptly.

        Even if I wished for something more than a dreary day in this bedroom,{awt}asking a dangerous stranger for it was unnecessary.

        Moments after that,{awt}I immediately rang for the scullery maid who came in with four guards.

        They had been apparently chasing the man outside the manor,{awt}but he had disappeared in some hedges.

        The man wasn't apprehended. Instead,{awt}he was shot instantly on the balcony due to fear of his strength.

        I was escorted out of the room during this,{awt}but the gunshots still ring in my ears.

        No answers were given to me afterward.{awt=2.0}Just a worrisome maid standing guard outside my door as I was told to head back to sleep.

        I couldn't help but wonder what would've happened had I let him in{dots=3.0}
        """

        show bad_end
        pause
        $ renpy.full_restart(config.end_game_transition)
      "Invite the man in":
        return

  return

image bad_end:
  Text("Bad End...", size=72, font="gui/fonts/BookAntiqua/BoldItalic.ttf", color="#FFF")
  align (0.95, 0.95)
  alpha 0.0 xoffset 50
  easein 1.5 alpha 1.0 xoffset 0
