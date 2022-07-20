## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):
  style_prefix "gm"
  add "gui/game_menu.webp"

  hbox:
    use navigation(title)
    window:
      transclude

  if main_menu:
    key "game_menu" action ShowMenu("main_menu")

style gm_window:
  margin (0, 180, 60, 100)
  xfill True
  yfill True
  background Solid("#F001") # TODO: DEBUG REMOVAL

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation(kind):
  style_prefix "nav"

  window:
    frame:
      style "nav_header"
      text kind:
        size 96
        color "#DB4"
        bold True

    vbox:
      if main_menu:
        textbutton _("Start")   action Start()
      else:
        textbutton _("History") action ShowMenu("history")
        textbutton _("Save")    action ShowMenu("save")

      textbutton _("Load")      action ShowMenu("load")
      textbutton _("Settings")  action ShowMenu("settings")
      textbutton _("About")     action ShowMenu("about")
      if not main_menu:
        textbutton _("Main Menu") action MainMenu()

style nav_window:
  xsize 425
  yfill True
  background Solid("#FFF1") # TODO: DEBUG REMOVAL

style nav_header:
  ysize 125
  align (0.5, 0.0)
  top_margin 90

style nav_vbox:
  xsize 425
  align (0.5, 0.5)
  spacing 30

style nav_button is gui_button:
  align  (0.5, 0.5)
style nav_button_text is gui_button_text:
  align (0.5, 0.5)
  size 32
  bold True
