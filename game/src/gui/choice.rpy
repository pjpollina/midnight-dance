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

style choice_button:
  xsize   1185
  padding (150, 8, 150, 8)
style choice_button_text:
  size 33
  font book_antiqua
  xalign 0.5
  idle_color  "#000"
  hover_color "#FFF"
