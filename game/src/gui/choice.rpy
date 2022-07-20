## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.

screen choice(items):
  style_prefix "choice"

  hbox:
    align (0.5, 0.6)
    spacing 20

    for i in items:
      textbutton i.caption action i.action

style choice_button:
  background Solid("#F00A") # TODO: REMOVE DEBUG
  align (0.5, 0.5)
  xysize (600, 100)
style choice_button_text:
  font cardinal
  align (0.5, 0.5)

  idle_size  40
  hover_size 44
  idle_color  "#000"
  hover_color "#FFF"
