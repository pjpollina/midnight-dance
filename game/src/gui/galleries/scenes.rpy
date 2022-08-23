## #############################################################################
## Scenes Gallery ##############################################################
##
## Browse all of the CGs by Moonkip and backgrounds by Luciam.

screen scenes():
  tag menu
  style_prefix "scene"

  vbox:
    align (0.5, 0.5)
    spacing 30

    hbox:
      button action NullAction():
        background Transform("scenes/cgs/01a.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/cgs/01b.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/cgs/01c.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/cgs/02.webp",  fit="contain")

    hbox:
      button action NullAction():
        background Transform("scenes/cgs/03.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/cgs/04.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/cgs/05.webp", fit="contain")

    null height 30

    hbox:
      button action NullAction():
        background Transform("scenes/bgs/balcony_dark.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/bgs/balcony_lit.webp",  fit="contain")
      button action NullAction():
        background Transform("scenes/bgs/bedroom_dark.webp", fit="contain")
      button action NullAction():
        background Transform("scenes/bgs/bedroom_lit.webp",  fit="contain")

## Styles ######################################################################

style scene_button:
  xysize (320, 180)
  idle_foreground  Solid("#0007")
  hover_foreground None

style scene_hbox:
  spacing 30
  xalign 0.5
