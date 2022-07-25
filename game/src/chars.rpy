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

## Balth name function #########################################################

default is_stranger = True

init -10 python:
  def balth_name():
    return (_("Stranger{#Balthazar's name before he's introduced}") if is_stranger else "Balthazar")

## Click-To-Continue ###########################################################

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
