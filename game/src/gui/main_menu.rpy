## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.

screen main_menu():
  tag menu
  add "bg bedroom"

  frame style "logo"

  use mnav()
  text "Ver. [config.version]" style "version_text"

## Main Menu styles ############################################################

style logo:
  align (1.0, 0.0)
  background Transform("gui/logo.webp", alpha=0.75)
  xysize(862, 711)

style version_text:
  align (1.0, 1.0)
  offset (-30, -20)
  color "#000"

## Main Menu navigation ########################################################

screen mnav():
  style_prefix "mnav"

  vbox:
    textbutton _("Start")     left_padding   0 action [Stop("music", fadeout=3.0), Hide("main_menu", transition=Dissolve(3.0)), Jump("newgame")]
    textbutton _("Load")      left_padding  60 action ShowMenu("saves")
    textbutton _("About")     left_padding 120 action ShowMenu("about")
    textbutton _("Settings")  left_padding 180 action ShowMenu("settings")
    textbutton _("Gallery")   left_padding 240 action ShowMenu("gallery")
    textbutton _("Credits")   left_padding 280 action NullAction() # TODO: IMPLEMENT CREDITS
    textbutton _("Quit")      left_padding 380 action Quit()

## Main Menu navigation styles #################################################

style mnav_vbox:
  align (0.0, 1.0)
  spacing 10
  offset (30, -20)

style mnav_button:
  xsize 425
style mnav_button_text:
  size 72
  font cardinal
  text_align 0.0

## Control Labels ##############################################################

label before_main_menu:
  play music main_menu fadein 3.0
  $ renpy.transition(Dissolve(3.0))
  return

label newgame:
  $ renpy.pause(3.0, hard=True)
  $ renpy.jump_out_of_context("start")
  return
