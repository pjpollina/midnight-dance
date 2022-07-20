# Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)

screen notify(message):
  zorder 100
  style_prefix "notify"

  frame at notify_appear:
    text "[message!tq]"

  timer 3.25 action Hide('notify')

transform notify_appear:
  on show:
    alpha 0
    linear 0.25 alpha 1.0
  on hide:
    linear 0.5 alpha 0.0

style notify_frame:
  ypos 68
  background Frame("gui/notify.png", Borders(24, 8, 60, 8))
  padding (24, 8, 60, 8)
style notify_text:
  size 24
