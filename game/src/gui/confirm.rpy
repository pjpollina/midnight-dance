## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.

screen confirm(message, yes_action, no_action):
  modal True
  zorder 200
  style_prefix "confirm"
  key "game_menu" action no_action

  add Solid("#0F132DAA")
  frame:
    has vbox
    label message
    hbox:
      textbutton _("Yeah{#Confirm}") action yes_action
      textbutton _("Nope{#Deny}")    action no_action

## Confirm styles ##############################################################

style confirm_frame:
  xysize (1510, 640)
  align (0.5, 0.5)
  padding (40, 90, 40, 40)
  background Frame("gui/confirm_frame.webp", Borders(40, 40, 40, 40), tile=False)
style confirm_vbox:
  align (0.5, 0.5)
  spacing 45
style confirm_hbox:
  align (0.5, 0.5)
  spacing 150

style confirm_label:
  align (0.5, 0.5)
style confirm_label_text:
  size 48
  font cardinal
  color "#DB4"
  outlines [(3, "#111", 1, 1)]
  text_align 0.5

style confirm_button xysize (150, 75)
style confirm_button_text:
  align (0.5, 0.5)
  size 40
  font book_antiqua
  color "#FFF"
  hover_size 44
  hover_bold True
  hover_outlines [(2, "#111A", 1, 1)]
