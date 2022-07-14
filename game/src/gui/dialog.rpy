## Character definitions #######################################################

define narrator = Character(None, kind=centered, what_style="say_thought", show_qm=False)
define prolog   = Character(None, kind=narrator, what_slow_cps=0, show_flair=True)
define soundfx  = Character(None, kind=narrator, what_slow_cps=0, what_size=24, what_italic=True, advance=False)

define everett  = Character("Everett",   ctc="ctc", image="everett")
define balth    = Character("Balthazar", ctc="ctc", image="balth")
define maid     = Character("Maid",      ctc="ctc", image="maid")
define guarda   = Character("Guard #1",  ctc="ctc", image="guard")
define guardb   = Character("Guard #2",  ctc="ctc", image="guard")

image ctc:
  xysize (36, 36) yoffset 4
  block:
    "gui/ctc/ctc_a.webp"
    pause 0.5
    "gui/ctc/ctc_b.webp"
    pause 0.5
    "gui/ctc/ctc_c.webp"
    pause 0.5
    "gui/ctc/ctc_d.webp"
    pause 0.5
    repeat

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

style say_label is default:
  pos (37, 95)
  xysize (658, 101)
  background "gui/namebox.webp"
style say_label_text:
  size 56
  text_align 0.0
  align (0.5, 0.5)
  font book_antiqua
  bold True
  italic True

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
