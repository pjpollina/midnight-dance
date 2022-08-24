init offset = -2

init python:
  gui.init(1920, 1080)
  gui.language = "unicode"

  ## Mouse
  config.mouse = dict(default = [("gui/mouse.webp", 0, 0)])

  ## Fonts
  book_antiqua = "gui/fonts/BookAntiqua/Regular.ttf"
  config.font_replacement_map[book_antiqua, False, True] = ("gui/fonts/BookAntiqua/Italic.ttf", False, False)
  config.font_replacement_map[book_antiqua, True, False] = ("gui/fonts/BookAntiqua/Bold.ttf", False, False)
  config.font_replacement_map[book_antiqua, True,  True] = ("gui/fonts/BookAntiqua/BoldItalic.ttf", False, False)

  cardinal = "gui/fonts/Cardinal/Regular.ttf"
  config.font_replacement_map[cardinal, False, True] = ("gui/fonts/Cardinal/Alternate.ttf", False, False)

  dejavu_serif = "gui/fonts/DejaVuSerif/Regular.ttf"
  config.font_replacement_map[dejavu_serif, False, True] = ("gui/fonts/DejaVuSerif/Italic.ttf", False, False)
  config.font_replacement_map[dejavu_serif, True, False] = ("gui/fonts/DejaVuSerif/Bold.ttf", False, False)
  config.font_replacement_map[dejavu_serif, True,  True] = ("gui/fonts/DejaVuSerif/BoldItalic.ttf", False, False)

## General styles ##############################################################

style default:
  size 33
  color "#FFF"
  font book_antiqua

style label_text:
  size 36

## Button styles ###############################################################

style button:
  align (0.5, 0.5)
style button_text:
  hover_color "#DB4"
  selected_color "#FFF6"

style radio_button:
  xysize (300, 42)
  left_padding 45
  idle_background     "gui/buttons/pip/idle.webp"
  hover_background    "gui/buttons/pip/hover.webp"
  selected_background "gui/buttons/pip/selected.webp"
style radio_button_text:
  yalign 0.5
  hover_color       "#FFFF9C"
  selected_color    "#FFFF9C"
  outlines          [(1, "#FFF0",     0, 0)]
  hover_outlines    [(1, "#D06BF75A", 0, 0)]
  selected_outlines [(1, "#FFF0",     0, 0)]

style check_button is radio_button:
  selected_hover_background "gui/buttons/pip/unselected.webp"
style check_button_text is radio_button_text:
  selected_hover_color "#FFFF9CAA"
  selected_hover_outlines [(1, "#D06BF75A", 0, 0)]

## Slider styles ###############################################################

style slider:
  xysize    (350, 40)
  left_bar  "gui/slider/full.webp"
  right_bar "gui/slider/empty.webp"
  hover_left_bar  "gui/slider/full_hover.webp"
  hover_right_bar "gui/slider/empty_hover.webp"
  thumb     None
  xalign    0.5

## Hyperlink style #############################################################

style hyperlink is text:
  hover_color "#09A"
  hover_underline True

define config.hyperlink_styler = lambda _: style.hyperlink
