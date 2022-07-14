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
