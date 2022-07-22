## Saves screen ################################################################
##
## The merged save/load screen.

screen saves():
  tag menu
  style_prefix "saves"

  use game_menu("Saves"):
    vbox:
      use saves_file(1, _("File A"))
      use saves_file(2, _("File B"))

## Saves styles ################################################################

style saves_vbox:
  xpos 60
  spacing 60
  align (0.0, 0.5)

style saves_hbox:
  spacing 60

## Save slot screen ############################################################

screen saves_file(index, name):
  hbox:
    spacing 30
    style_prefix "saves_file"
    frame:
      if not main_menu:
        key "game_menu" capture

      button:
        action If(main_menu, FileLoad(index), FileSave(index))
        alternate FileLoad(index)

        if FileLoadable(index):
          idle_background  Transform(FileScreenshot(index), blur=1, alpha=0.66)
          hover_background Transform(FileScreenshot(index), blur=1, alpha=0.80)

    vbox:
      spacing 10
      label name
      text FileTime(index, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("{#Empty file slot}No data")) style "default"
      text FileSaveName(index, empty="")

## Save slot styles ############################################################

style saves_file_frame:
  xysize (480, 270)
  background       "gui/buttons/saveslot/background.webp"
style saves_file_button is saves_file_frame:
  foreground       "gui/buttons/saveslot/idle.webp"
  hover_foreground "gui/buttons/saveslot/hover.webp"

style saves_file_label_text:
  size 48
  bold True

style saves_file_text:
  size 28
  italic True
  color "#FFFA"
