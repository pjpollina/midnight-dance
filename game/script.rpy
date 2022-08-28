default persistent.game_clear = False

label start:
  call tmd_part_a
  call tmd_part_b
  call tmd_part_c
  call tmd_part_d
  $ persistent.game_clear = True
  call credits
  show the_end
  $ renpy.pause(3.0, hard=True)
  scene black with config.end_game_transition
  turmoil "The gallery is now unlocked."
  return

image the_end:
  Text("The End...", size=72, font="gui/fonts/BookAntiqua/BoldItalic.ttf", color="#FFF")
  align (0.95, 0.95)
  alpha 0.0 xoffset 50
  easein 1.5 alpha 1.0 xoffset 0
