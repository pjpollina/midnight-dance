## Say screen ##################################################################
##
## The most important screen in the game.
## Servin' it up, PJ's way.

screen say(who, what, flair=False, qm=True):
  if flair:
    text what id "what" at say_flair
  else:
    if who == None:
      text what id "what"
    else:
      frame id "window":
        label who id "who"
        text what id "what"
  if qm:
    use quick_menu()

transform say_flair:
  alpha 0.0
  easein 1.0 alpha 1.0 xoffset 0

## Say screen styles ###########################################################

style say_label:
  pos (100, 75)
  xysize (700, 120)
  background Frame("gui/namebox.webp")
style say_label_text:
  size 64
  font cardinal
  color "#000"
  align (0.5, 0.5)
  outlines [(3, "#000D", 0, 0)]

style say_dialogue is default:
  size 40
  text_align 0.0
  xsize 1116
  pos (128, 250)
  color "#FFF"
  font book_antiqua

style say_thought is say_dialogue:
  size 33
  align (0.5, 0.5)
  text_align 0.5
  outlines [(absolute(2), "#111", absolute(1), absolute(1))]

style say_window:
  align (0.5, 1.0)
  xfill True
  ysize 468
  background "gui/textbox.webp"
