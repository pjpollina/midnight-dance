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
