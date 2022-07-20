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
