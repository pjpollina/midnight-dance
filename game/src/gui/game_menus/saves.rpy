## Saves screen ################################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.

screen saves():
  tag menu
  style_prefix "saves"

  use game_menu("Saves"):
    vbox:
      use saves_file(1, _("File A"))
      use saves_file(2, _("File B"))

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
      key "game_menu" capture
      button:
        action If(main_menu, FileLoad(index), FileSave(index))
        alternate FileLoad(index)

        if FileLoadable(index):
          background Transform(FileScreenshot(index), blur=1, alpha=0.66)

    vbox:
      spacing 10
      label name
      text FileTime(index, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("{#Empty file slot}No data"))
      text FileSaveName(index, empty="") italic True size 24 color "#FFFA"

style saves_file_frame:
  background "gui/save_frame/background.webp"
  xysize (480, 270)
style saves_file_button:
  foreground  "gui/save_frame/idle.webp"
  hover_foreground "gui/save_frame/hover.webp"
  xysize (480, 270)

style saves_file_label
style saves_file_label_text:
  size 48
  bold True
