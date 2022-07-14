label tmd_04:
  "{cps=*0.75}I bit my bottom lip, trying to not make anymore eye contact with the stranger. I...{/cps}{w=0.25}{nw}"(what_yoffset=-50)
  menu:
    extend ""
    "Leave the man outside.":
      play sound ["<silence 1.5>", "audio/curtains_shut.ogg"]
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
