## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.

default persistent.game_clear = False

screen main_menu():
  tag menu
  add ("bg bedroom lit" if persistent.game_clear else "bg bedroom")

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

  vbox xoffset -30:
    textbutton _("Start")    xoffset   0 action [Stop("music", fadeout=3.0), Hide("main_menu", transition=Dissolve(3.0)), Jump("newgame")]
    textbutton _("Load")     xoffset  60 action ShowMenu("saves")
    textbutton _("About")    xoffset 120 action ShowMenu("about")
    textbutton _("Settings") xoffset 180 action ShowMenu("settings")
    textbutton _("Gallery")  xoffset 240 action If(persistent.game_clear, Show("gallery", dissolve), Notify(_("Finish the game first!")))
    textbutton _("Credits")  xoffset 280 action [Stop("music", fadeout=3.0), Hide("main_menu", transition=Dissolve(3.0)), Jump("credits_warp")]
    textbutton _("Quit")     xoffset 380 action Quit()

## Main Menu navigation styles #################################################

style mnav_vbox:
  align (0.0, 1.0)
  spacing 10
  offset (30, -20)

style mnav_button:
  xsize 300
  left_padding 50
style mnav_button_text:
  size 72
  font cardinal
  text_align 0.0
  outlines [(3, "#000", 1, 1)]
  outline_scaling "step"

## Control Labels ##############################################################

label before_main_menu:
  play music main_menu fadein 3.0
  $ renpy.transition(Dissolve(3.0))
  return

label newgame:
  $ renpy.pause(3.0, hard=True)
  $ renpy.jump_out_of_context("start")
  return

label credits_warp:
  $ renpy.pause(3.0, hard=True)
  $ renpy.jump_out_of_context("credits")
