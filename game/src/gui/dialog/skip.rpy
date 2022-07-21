## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():
  zorder 100
  style_prefix "skip"

  frame:
    hbox:
      spacing 9
      text _("Skipping")
      text "▸" at delayed_blink(0.0, 1.0) font "DejaVuSans.ttf"
      text "▸" at delayed_blink(0.2, 1.0) font "DejaVuSans.ttf"
      text "▸" at delayed_blink(0.4, 1.0) font "DejaVuSans.ttf"

transform delayed_blink(delay, cycle):
  alpha 0.5
  pause delay
  block:
    linear 0.2 alpha 1.0
    pause  0.2
    linear 0.2 alpha 0.5
    pause (cycle - 0.4)
    repeat

style skip_frame:
  ypos 15
  background Frame(Solid("#FFFA"), Borders(24, 8, 75, 8))
  padding (24, 8, 75, 8)

style skip_text:
  size 24
