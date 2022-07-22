## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
  tag menu
  style_prefix "about"

  use game_menu(_("About")):
    vbox:
      xsize 1100
      xalign 0.5

      label "[config.name!t]"
      text _("Version [config.version!t]\n")
      text "[gui.about!t]\n"
      text _("Made with Ren'Py [renpy.version_only].")

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
  tag menu
  style_prefix "help"

  use game_menu(_("Help")):
    vbox:
      spacing 23
      align (0.25, 0.1)

      hbox:
        label _("Enter, Left Click")
        text  _("Advances dialogue and activates the interface.")
      hbox:
        label _("Space")
        text  _("Advances dialogue without selecting choices.")
      hbox:
        label _("Arrow Keys")
        text  _("Navigate the interface.")
      hbox:
        label _("Escape, Right Click")
        text  _("Accesses the game menu.")
      hbox:
        label _("Ctrl")
        text  _("Skips dialogue while held down.")
      hbox:
        label _("Tab")
        text  _("Toggles dialogue skipping.")
      hbox:
        label _("H, Middle Click")
        text  _("Hides the user interface.")
      hbox:
        label "S"
        text  _("Takes a screenshot.")
      hbox:
        label "V"
        text  _("Toggles assistive self-voicing.")
      hbox:
        label "Shift+A"
        text  _("Opens the accessibility menu.")

style help_label:
  xsize 375
  right_padding 30
style help_label_text:
  size 33
  xalign 1.0
  text_align 1.0
  bold True
