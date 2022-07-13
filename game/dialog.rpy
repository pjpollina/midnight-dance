define narrator = Character(None, kind=centered, what_style="say_thought")
define prolog   = Character(None, kind=narrator, what_slow_cps=0, show_flair=True)
define soundfx  = Character(None, kind=narrator, what_slow_cps=0, what_size=24, what_italic=True, advance=False)

define everett  = Character("Everett",   image="everett")
define balth    = Character("Balthazar", image="balth")
define maid     = Character("Maid",      image="maid")
define guarda   = Character("Guard #1",  image="guard")
define guardb   = Character("Guard #2",  image="guard")

## Say screen ##################################################################
##
## The most important screen in the game.
## Servin' it up, PJ's way.

screen say(who, what, flair=False):
  if flair:
    text what id "what" at say_flair
  else:
    if who == None:
      text what id "what"
    else:
      frame id "window":
        text who  id "who"
        text what id "what"

    if not renpy.variant("small"):
      add SideImage() xalign 0.0 yalign 1.0

transform say_flair:
  alpha 0.0
  easein 1.0 alpha 1.0 xoffset 0

style say_label is default:
  size 45
  yoffset 4
  align (0.5, 0.0)
  font "gui/fonts/playfair/bolditalic.ttf"

style say_dialogue is default:
  size 33
  text_align 0.0
  xsize 1116
  pos (402, 75)
  font "gui/fonts/playfair/regular.ttf"

style say_thought is say_dialogue:
  align (0.5, 0.5)
  text_align 0.5
  color "#FFF"
  outlines [(absolute(2), "#111", absolute(1), absolute(1))]

style say_window:
  align (0.5, 1.0)
  xfill True
  ysize 278
  background "gui/textbox.png"

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.

screen choice(items):
  style_prefix "choice"

  vbox:
    align (0.5, 0.6)
    spacing 20

    for i in items:
      textbutton i.caption action i.action

style choice_button is default:
  properties gui.button_properties("choice_button")

style choice_button_text is default:
  properties gui.button_text_properties("choice_button")
  idle_color "#000"
  hover_color "#FFF"

init python:
  config.font_replacement_map["gui/fonts/playfair/regular.ttf", False, True] = ("gui/fonts/playfair/italic.ttf", False, False)
  config.font_replacement_map["gui/fonts/playfair/regular.ttf", True, False] = ("gui/fonts/playfair/bold.ttf", False, False)
  config.font_replacement_map["gui/fonts/playfair/regular.ttf", True,  True] = ("gui/fonts/playfair/bolditalic.ttf", False, False)
