## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():
  tag menu
  style_prefix "about"

  use game_menu(_("About"), scroll="viewport"):
    vbox:
      label "[config.name!t]"
      text _("Version [config.version!t]\n")
      text "[gui.about!t]\n"
      text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style about_label
style about_label_text:
  size 36

## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
  tag menu
  default device = "keyboard"
  style_prefix "help"

  use game_menu(_("Help"), scroll="viewport"):
    vbox:
      spacing 23

      hbox:
        textbutton _("Keyboard")  action SetScreenVariable("device", "keyboard")
        textbutton _("Mouse")     action SetScreenVariable("device", "mouse")
        if GamepadExists():
          textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

      if device == "keyboard":
        use keyboard_help
      elif device == "mouse":
        use mouse_help
      elif device == "gamepad":
        use gamepad_help

screen keyboard_help():
  hbox:
    label _("Enter")
    text  _("Advances dialogue and activates the interface.")
  hbox:
    label _("Space")
    text  _("Advances dialogue without selecting choices.")
  hbox:
    label _("Arrow Keys")
    text  _("Navigate the interface.")
  hbox:
    label _("Escape")
    text  _("Accesses the game menu.")
  hbox:
    label _("Ctrl")
    text  _("Skips dialogue while held down.")
  hbox:
    label _("Tab")
    text  _("Toggles dialogue skipping.")
  hbox:
    label _("Page Up")
    text  _("Rolls back to earlier dialogue.")
  hbox:
    label _("Page Down")
    text  _("Rolls forward to later dialogue.")
  hbox:
    label "H"
    text  _("Hides the user interface.")
  hbox:
    label "S"
    text  _("Takes a screenshot.")
  hbox:
    label "V"
    text  _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
  hbox:
    label "Shift+A"
    text  _("Opens the accessibility menu.")

screen mouse_help():
  hbox:
    label _("Left Click")
    text  _("Advances dialogue and activates the interface.")
  hbox:
    label _("Middle Click")
    text _("Hides the user interface.")
  hbox:
    label _("Right Click")
    text  _("Accesses the game menu.")
  hbox:
    label _("Mouse Wheel Up\nClick Rollback Side")
    text  _("Rolls back to earlier dialogue.")
  hbox:
    label _("Mouse Wheel Down")
    text  _("Rolls forward to later dialogue.")

screen gamepad_help():
  hbox:
    label _("Right Trigger\nA/Bottom Button")
    text  _("Advances dialogue and activates the interface.")
  hbox:
    label _("Left Trigger\nLeft Shoulder")
    text  _("Rolls back to earlier dialogue.")
  hbox:
    label _("Right Shoulder")
    text  _("Rolls forward to later dialogue.")
  hbox:
    label _("D-Pad, Sticks")
    text  _("Navigate the interface.")
  hbox:
    label _("Start, Guide")
    text  _("Accesses the game menu.")
  hbox:
    label _("Y/Top Button")
    text  _("Hides the user interface.")
  textbutton _("Calibrate") action GamepadCalibrate()

style help_button:
  xmargin 12
style help_button_text

style help_label:
  xsize 375
  right_padding 30
style help_label_text:
  size 33
  xalign 1.0
  text_align 1.0
