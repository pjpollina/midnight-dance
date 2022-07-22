init -10 python:
  is_stranger = True
  def balth_name():
    return (_("Stranger{#Balthazar's name before he's introduced}") if is_stranger else "Balthazar")

## Character definitions #######################################################

define narrator = Character(None, kind=centered, what_style="say_thought", show_qm=False)
define prolog   = Character(None, kind=narrator, what_slow_cps=0, show_flair=True)
define soundfx  = Character(None, kind=narrator, what_slow_cps=0, what_size=24, what_italic=True, advance=False)
define turmoil  = Character(None, kind=narrator, show_flair=True)

define everett  = Character("Everett",   ctc="ctc", image="everett", who_text_color="#3B3065", who_top_padding=12, who_text_size=72)
define balth    = Character(balth_name,  ctc="ctc", image="balth",   who_text_color="#580617", dynamic=True)
define maid     = Character("Maid",      ctc="ctc", image="maid",    who_text_color="#8F6A96")
define guarda   = Character("Guard #1",  ctc="ctc", image="guard",   who_text_color="#5D3B42")
define guardb   = Character("Guard #2",  ctc="ctc", image="guard",   who_text_color="#5D3B54")

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
