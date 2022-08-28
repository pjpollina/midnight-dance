default persistent.game_clear = False

init python:
  def label_callback(name, abnormal):
    store.current_label = name

  config.label_callback = label_callback

## A developer-mode screen to indicate what scene is active in-game
screen _dev_label():
  zorder 100
  text "[current_label!tq]" color "#F006" xalign 1.0

label start:
  if config.developer:
    show screen _dev_label()
  call tmd_part_a
  call tmd_part_b
  call tmd_part_c
  call tmd_part_d
  $ persistent.game_clear = True
  call credits
  show the_end
  pause 3.0
  return

image the_end:
  Text("The End...", size=72, font="gui/fonts/BookAntiqua/BoldItalic.ttf", color="#FFF")
  align (0.95, 0.95)
  alpha 0.0 xoffset 50
  easein 1.5 alpha 1.0 xoffset 0
