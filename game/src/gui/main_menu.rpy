## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.

screen main_menu():
  tag menu
  add "gui/main_menu.png"

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

style main_menu_text is gui_text:
  properties gui.text_properties("main_menu", accent=True)
style main_menu_title is main_menu_text:
  properties gui.text_properties("title")
style main_menu_version is main_menu_text:
  properties gui.text_properties("version")
