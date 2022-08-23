## #############################################################################
## Sprites Gallery #############################################################
##
## Check out all of AceyDude's sprites.

screen sprites():
  tag menu
  style_prefix "sprite"

  hbox:
    button style_suffix "everett" action NullAction()
    button style_suffix "balth"   action NullAction()
    button style_suffix "maid"    action NullAction()
    button style_suffix "guard"   action NullAction()

style sprite_button:
  xysize (324, 600)
  idle_background  Solid("#000A")
  hover_background Solid("#FFFA")

style sprite_everett is sprite_button:
  idle_foreground  "everett b frown"
  hover_foreground "everett c smile"

style sprite_balth is sprite_button:
  idle_foreground  "balth b aloof"
  hover_foreground "balth c smirk"

style sprite_maid is sprite_button:
  idle_foreground  "maid worry"
  hover_foreground "maid smile"

style sprite_guard is sprite_button:
  idle_foreground  "guard"
  hover_foreground "guard"

style sprite_hbox:
  spacing 30
  align (0.5, 0.5)
