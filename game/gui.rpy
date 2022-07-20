################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
  gui.init(1920, 1080)
  gui.language = "unicode"

  ## Fonts
  book_antiqua = "gui/fonts/BookAntiqua/Regular.ttf"
  config.font_replacement_map[book_antiqua, False, True] = ("gui/fonts/BookAntiqua/Italic.ttf", False, False)
  config.font_replacement_map[book_antiqua, True, False] = ("gui/fonts/BookAntiqua/Bold.ttf", False, False)
  config.font_replacement_map[book_antiqua, True,  True] = ("gui/fonts/BookAntiqua/BoldItalic.ttf", False, False)

  cardinal = "gui/fonts/Cardinal/Regular.ttf"
  config.font_replacement_map[cardinal, False, True] = ("gui/fonts/Cardinal/Alternate.ttf", False, False)

style text:
  size 33
  font book_antiqua
  color "#FFF"
style label_text is text

style button
style button_text is text:
  hover_color "#DB4"
  selected_color "#FFFA"

style slider:
  xysize    (350, 40)
  left_bar  "gui/slider/full.webp"
  right_bar "gui/slider/empty.webp"
  thumb     None
  xalign    0.5
