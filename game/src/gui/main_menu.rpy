## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.

screen main_menu():
  tag menu
  add Solid("#7F5F5F") # TODO: Get final art

  use navigation("")
  vbox:
    style "main_menu_vbox"
    text "[config.name!t]":
      style "main_menu_title"
    text "[config.version]":
      style "main_menu_version"

style main_menu_frame:
  xsize 420
  yfill True
  background "gui/overlay/main_menu.png"

style main_menu_vbox:
  xalign 1.0
  xoffset -30
  xmaximum 1200
  yalign 1.0
  yoffset -30

style main_menu_title:
  align (1.0, 1.0)
  font cardinal
  size 75
  color "#000"
style main_menu_version:
  align (1.0, 1.0)
  font book_antiqua
  color "#000"
