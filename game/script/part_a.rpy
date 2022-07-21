label tmd_00:
  prolog """
  Voices carried across the wind, full of excitement and apprehension.

  Will they find their lover in the onslaught between suitors?

  Will the timid wallflower bloom into a sensation overnight?

  Much was left to the imagination, at least for those who waited with bated breaths to attend.

  All except for the sickly prince, who from his balcony cast a longing glance towards the crowds.

  From where his manor was, he could gaze into the throes of well-mannered gentlemen and gorgeously elegant women streaming into different buildings every night.

  Every night came with a new ball to attend. Another chance to prove yourself.

  Or lose yourself against the night.

  With a deep, heaving sigh that expelled any energy left, he rested his chin on his palm.

  Oh, how deeply he wished he could attend.
  """
  return

label tmd_01:
  "{dots=3.0}"

  scene bg balcony
  show everett b smile:
    xalign 0.66
    xzoom -1.0
  with fade

  """
  A feeling of profound melancholy overcame me as I watched the last of the crowds disappear into the ball.

  The same night, every night, when the arching loneliness overwhelmed me at the sights.

  The sights of people dressing up and dedicating a night to sway and dance.

  Oh, how the looks of excitement made me tap my fingers against the iced railing.
  """

  everett c "Are the lights as bright as I've come to hear? Do they blind you? Bathe you in their warmth as your blood pumps with adrenaline?"
  everett "Are the floors smooth enough to take in every stride, every waltz step that we've trained to do since little?"
  everett frown "{dots=6.0}"
  everett "Will I ever see that light? Those floors? The dancers in their ball gowns and suits?"

  """
  I grit my chattering teeth, trying to tune into the live music playing indoors.

  There was no sound over the breeze. Nothing but the wind and the tapping of my nails.

  I don't want to think of it, yet I do.

  Every night, the same thought in my mind.
  """

  everett shame "Is the food good?"
  everett smirk "The maids often talk of dancing on an empty stomach."
  everett "No lady, especially on her debutante, would want to look bloated in their tight corsets."

  """
  The high stakes! How exciting it was to imagine all the preparation for the night to start.

  It was regulated highly, according to the strictest code of good-breeding.

  I think I would still enjoy it, even moreso because of the rules. It would make for an exciting night.

  Truly! An invigorating night.
  """

  everett shame @ frown "Maybe{em}"
  "???" "Your Royal Highness!"

  """
  A concerned voice breaks me out of my train of thought.

  Behind me, the harried scullery maid rushes forward with her hands fluttering to her bosom.
  """

  show maid worry:
    rotate_pad False xpos -1.0 yalign 1.0
    parallel:
      linear 1.0 xpos 0.15
    parallel:
      easein 0.25 rotate -3 yoffset 50
      easein 0.25 rotate  0 yoffset  0
      repeat 2
  pause 1.0
  show maid worry:
    xpos 0.15 rotate 0 yoffset 0

  maid "You cannot be out here! It is far too chilly for your fragile body. Allow me to accompany you back inside."

  "I sigh once more, {nw}{done}turning to face her with a frown."
  show everett b frown:
    parallel:
      ease 0.2 xzoom 1.0
    parallel:
      ease 0.5 xalign 0.75
  "I sigh once more, {fast}turning to face her with a frown."

  everett frail "Couldn't I enjoy the sights longer? It is the only good entertainment I get from this prison{em}"
  maid "This is far from a prison, Your Royal Highness! It was decorated with your interests in mind."
  maid "There are others less fortunate to live in such chambers as yours."
  everett smirk "Well at least they are given the freedom to leave if they dislike it."

  show maid:
    easein 0.2 xalign 0.5
  pause 0.2
  show maid:
    xalign 0.5
  pause 0.5

  show everett shame:
    linear 2.0 xoffset -2160
  show maid:
    linear 2.0 xoffset -2160
  scene black with Dissolve(1.5)

  "The scullery maid took my wrist, pulling me back inside despite my protests."
  return

label tmd_02:
  scene bg bedroom lit
  show everett b frown:
    xalign 0.25 xzoom -1.0
  with Fade(0.0, 1.0, 2.0)

  # TODO: Door sfx
  """
  She closed the balcony doors and pulled the curtains from either side to conceal the outside.

  And any joy I had from gazing at the night.
  """

  show maid worry:
    rotate_pad False
    xalign 2.0
    parallel:
      linear 2.0 xalign 0.75
    parallel:
      easein 0.5 rotate -1 yoffset 20
      easein 0.5 rotate  0 yoffset  0
      repeat 2

  pause 2.0

  show maid worry:
    xalign 0.75 yoffset 0

  maid "Why are you out of bed again? If Your Majesty knew of this she would remove me for my incompetence."

  everett a "You know why, I want to be out there. There is nothing in this room I haven't seen ever since I was born."
  everett c "I'm not even allowed to explore the manor as often as the commoners who visit."

  maid "It's for your own safety, you know how frail you are. You'd fall over flushed if you stayed out there in the cold."
  maid "You aren't a healthy person, Your Highness{em}"

  everett smirk "And you think I'm foolish enough to not realize that? I didn't ask for the opinion of a servant that leaves every morning!"
  show everett b cough
  show maid:
    ease 0.1 xzoom -1.0
  "I couldn't take back the words as they slipped out. But my heart dropped at the sight of the maid whose shoulders fell."

  everett "I just want to leave, I'm terribly sorry for my attitude. I've grown crazy about these same walls."

  show everett:
    linear 0.2 xzoom 1.0
  with Dissolve(0.1)

  """
  In my hushed tone, I look away from her and towards the wall. The shadows danced alongside it from the candlelight. 

  They were almost dancing.
  """

  maid "I'm... I'm sorry Your Highness, I can't fathom how difficult it is to be in your position."

  """
  I glanced towards her to see her crestfallen expression, still gathering her thoughts in her balled up hands. 

  She was picking her words wisely. This wasn't another monologue sent from mother.
  """

  maid "Me and the others would love to see you outdoors... but Your Majesty asks we keep an eye on you. To keep you safe, that is."
  maid "The most I can do is ask her to change her mind. But we are just following her decree."
  maid "Maybe if we assign an attendant to you then she will lift some of the rules."

  """
  I didn't know how to reply to that. That was the same idea I proposed months ago.

  Mother still said no to it, saying that it was safer if I stayed here.
  """

  maid "...I will try my hardest, Your Highness."
  maid "But please, do get some rest. You really worry us sometimes."
  maid "If just for one more night, please get a good rest so I may bring up the topic tomorrow with Your Majesty."

  """
  That was as good as it was going to get with Mother. Though I respected the scullery maids' boldness in asking the Queen to reframe her decision.

  I couldn't send the frenzied maid away with more worries. 

  With every reluctance clinging to my body, I turned towards my bed to hide my irritation.
  """

  everett frown "I concede, please retire for the night Miss."
  "The sound of clapping reassured me that her feelings weren't hurt anymore, now that she had won."

  show maid smile:
    linear 0.1 xzoom 1.0
  with Dissolve(0.1)
  maid "Of course Your Highness! Allow me to dim the lights."

  "I settled on the bed as the maid blew the candles out."
  show bg bedroom
  show everett:
    linear 1.0 alpha 0.0
  with dissolve

  "All were blown out except for the one in her hand. The single flame illuminating her caring expression."
  show maid:
    parallel:
      linear 2.0 xalign 0.75
    parallel:
      easein 0.5 rotate -1 yoffset 20
      easein 0.5 rotate  0 yoffset  0
      repeat 2
  "She came to my side, gently throwing the blankets over me tucking me in."

  everett "Thank you, Miss."

  maid "Anything for you, Your Highness."
  show maid smile:
    linear 0.05 xzoom -1.0
  pause 0.75
  show maid smile:
    xzoom -1.0

  pause 1.0

  show maid smile:
    linear 0.05 xzoom 1.0
  pause 0.75
  show maid smile:
    xzoom 1.0

  maid "Goodnight."
  everett "Goodnight."

  show maid smile:
    rotate_pad False
    linear 0.05 xzoom -1.0
    pause 0.75
    parallel:
      linear 2.0 xpos 1.5
    parallel:
      easein 0.5 rotate 1 yoffset 20
      easein 0.5 rotate 0 yoffset 0
      repeat 2

  """
  Whispering her farewell, she stood upright and left the room in the same hurry she came in.

  All that remained was a still silence.

  The sort that feels suffocating despite nothing being there.

  Even as I closed my eyes it made no difference.
  """

  camera:
    ease 0.25 matrixcolor TintMatrix("#AAA")
    ease 0.25 matrixcolor TintMatrix("#FFF")
    pause 0.5
    repeat 2
  $ renpy.pause(2.2, hard=True)
  scene black with fade

  prolog """
  ...

  ...

  ...

  Why did I expect sleep would come easily?

  I would rather be dancing the night away, just to return home by the early dawn.

  Maybe with my eyes half-lidded from how tired I was.

  Possibly with someone by my side who would wish to dance more afterwards...

  If I were to dance with someone, anyone, this restless feeling in my legs would probably go away.

  Then I could sleep peacefully, knowing something awaited me the next day.

  Another dance. The waltz, maybe. 

  Before long, with the images of dancing in my mind, my eyelids grew heavy and I fell asleep.
  """

  return

label tmd_03:
  play sound tap_tap_tap
  soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

  play sound tap_tap_tap
  soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

  everett "Nmh..."

  """
  It was pitch dark when my eyes opened, everything remained as still as it was when I fell asleep.

  What woke me up?
  """
  scene bg bedroom:
    matrixcolor TintMatrix("#555")
  with Fade(0.0, 1.0, 2.0)

  play sound tap_tap_tap
  soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

  """
  It sounded like it came from the balcony.

  Was it a bird trying to come in? Or a twig from a long tree?

  Despite my many protests the night before, I was comfortable in bed and didn't want to leave.

  The blankets were warm and fuzzy against my skin, and it felt like clouds between my heavy limbs.
  """

  everett "Maybe I should ring for her..."

  """
  She wouldn't want me getting out of bed during these later hours.

  Especially when it gets chillier.

  Or maybe...

  I couldn't help myself as my eyes closed once again. The steady rise and fall of my chest luring me back into sleep.

  ...

  ..!
  """

  play sound tap_tap_tap
  soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

  """
  This wasn't going... to work.

  With the last bit of energy I had, my legs slowly kicked over the side of the bed.

  I fumbled with lighting a candle, but eventually gave up and headed towards the balcony.

  If the balcony was so insistent on keeping me awake, I hope it brings me something entertaining.

  Like a balcony size ball, just for me.

  But not a bird, or a twig.

  In front of the balcony glass, I grabbed the curtains and slowly pulled them aside.

  Nothing was there.

  It was hard to see already in the darkness, but not a single scratching sound or sight to behold.

  I tried to hide my resentment towards the situation, but it inevitably showed on my face most likely.
  """

  everett "Is that all, World? Willing to throw me a bone but not meat on it?"

  everett "If only I could show you."

  play sound curtain_shut
  "As I closed the curtains, the same sound came again from outdoors."

  play sound tap_tap_tap
  soundfx "tink.{w=0.25} tink.{w=0.25} tink.{w=0.25}{nw}"

  play sound curtain_open
  """
  Royally irritated, I flung the curtains back open ready to roll my sleeves up and suffocate what poor thing was out there making that sound.

  But I stopped.

  Instead a bird, animal, or even a stray twig brushing against the glass...

  A tall man was there, nursing his right shoulder with his back turned towards me.

  I couldn't see much, but the man seemed to be hunched forward slightly panting.
  """

  everett "He..."

  """
  A greeting slips past me and disappears at the tip of my tongue.

  What would I say to this stranger? 

  My breath hitched in my throat as the strangers' eyes met mine.

  My blood ran cold.

  His eyes were cold and clear on the surface. The crimson color shone strangely while the rest of him was concealed in the darkness.

  Those red eyes... they were as red as blood. 

  My heart skipped a beat, threatening to leap out of my chest.

  What... who was I staring at?

  Unable to control the fear seizing my legs, I stepped backwards slowly.

  Maybe he couldn't see me through the glass, maybe this was just a coincidence. 

  Maybe this was a dream.

  But the stranger's eyes shone in recognition, and he gently rapped against the balcony glass.
  """

  balth "May I seek refuge here, stranger?"

  balth "I've come a long way... and I need rest."

  balth "Harm will not come to you if you choose this."

  """
  ...What?

  I gawked at him in full surprise, trying to gather what he was asking.

  A stranger with strange red eyes and an injured shoulder showing up on his balcony asked for refuge?

  Did he not realize who I was?
  """

  return

label tmd_04:
  "{cps=*0.75}I bit my bottom lip, trying to not make anymore eye contact with the stranger. I...{/cps}{w=0.25}{nw}"(what_yoffset=-50)
  menu:
    extend ""
    "Leave the man outside.":
      play sound ["<silence 1.5>", curtain_shut]
      pause 1.5
      scene black
      pause 2.0
      """
      Without looking at him, I slowly step forward and close the curtains abruptly. Even if I wished for something more than a dreary day in this bedroom, asking a dangerous stranger for it was unnecessary. 

      Moments after that, I immediately rang for the scullery maid who came in with four guards. They had been apparently chasing the man outside the manor but he had disappeared in some hedges.

      The man wasn't apprehended. Instead, he was shot instantly on the balcony due to fear of his strength. I was escorted out of the room during this, but the gunshots still ring in my ears. No answers were given to me afterward. Just a worrisome maid standing guard outside my door as I was told to head back to sleep.

      I couldn't help but wonder what would've happened had I let him in.
      """

      show bad_end
      pause
      $ renpy.full_restart(config.end_game_transition)
    "Invite the man in":
      return

image bad_end:
  Text("Bad End...", size=72, font="gui/fonts/BookAntiqua/BoldItalic.ttf", color="#FFF")
  align (0.95, 0.95)
  alpha 0.0 xoffset 50
  easein 1.5 alpha 1.0 xoffset 0
