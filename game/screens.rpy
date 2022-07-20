################################################################################
## Initialization
################################################################################

init offset = -1

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

  ## This ensures that any other menu screen is replaced.
  tag menu

  add "gui/main_menu.png"

  ## This empty frame darkens the main menu.
  frame:
    style "main_menu_frame"

  ## The use statement includes another screen inside this one. The actual
  ## contents of the main menu are in the navigation screen.
  use navigation("")

  vbox:
    style "main_menu_vbox"

    text "[config.name!t]":
      style "main_menu_title"

    text "[config.version]":
      style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

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

style main_menu_text:
  properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
  properties gui.text_properties("title")

style main_menu_version:
  properties gui.text_properties("version")

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

  tag menu

  ## This use statement includes the game_menu screen inside this one. The
  ## vbox child is then included inside the viewport inside the game_menu
  ## screen.
  use game_menu(_("About"), scroll="viewport"):

    style_prefix "about"

    vbox:

      label "[config.name!t]"
      text _("Version [config.version!t]\n")

      ## gui.about is usually set in options.rpy.
      if gui.about:
        text "[gui.about!t]\n"

      text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
  size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

  tag menu

  use file_slots(_("Save"))


screen load():

  tag menu

  use file_slots(_("Load"))


screen file_slots(title):

  default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

  use game_menu(title):

    fixed:

      ## This ensures the input will get the enter event before any of the
      ## buttons do.
      order_reverse True

      ## The page name, which can be edited by clicking on a button.
      button:
        style "page_label"

        key_events True
        xalign 0.5
        action page_name_value.Toggle()

        input:
          style "page_label_text"
          value page_name_value

      ## The grid of file slots.
      grid gui.file_slot_cols gui.file_slot_rows:
        style_prefix "slot"

        xalign 0.5
        yalign 0.5

        spacing gui.slot_spacing

        for i in range(gui.file_slot_cols * gui.file_slot_rows):

          $ slot = i + 1

          button:
            action FileAction(slot)

            has vbox

            add FileScreenshot(slot) xalign 0.5

            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
              style "slot_time_text"

            text FileSaveName(slot):
              style "slot_name_text"

            key "save_delete" action FileDelete(slot)

      ## Buttons to access other pages.
      hbox:
        style_prefix "page"

        xalign 0.5
        yalign 1.0

        spacing gui.page_spacing

        textbutton _("<") action FilePagePrevious()

        if config.has_autosave:
          textbutton _("{#auto_page}A") action FilePage("auto")

        if config.has_quicksave:
          textbutton _("{#quick_page}Q") action FilePage("quick")

        ## range(1, 10) gives the numbers from 1 to 9.
        for page in range(1, 10):
          textbutton "[page]" action FilePage(page)

        textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
  xpadding 75
  ypadding 5

style page_label_text:
  text_align 0.5
  layout "subtitle"
  hover_color gui.hover_color

style page_button:
  properties gui.button_properties("page_button")

style page_button_text:
  properties gui.button_text_properties("page_button")

style slot_button:
  properties gui.button_properties("slot_button")

style slot_button_text:
  properties gui.button_text_properties("slot_button")

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

  tag menu

  ## Avoid predicting this screen, as it can be very large.
  predict False

  use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

    style_prefix "history"

    for h in _history_list:

      window:

        ## This lays things out properly if history_height is None.
        has fixed:
          yfit True

        if h.who:

          label h.who:
            style "history_name"
            substitute False

            ## Take the color of the who text from the Character, if
            ## set.
            if "color" in h.who_args:
              text_color h.who_args["color"]

        $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
        text what:
          substitute False

    if not _history_list:
      label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
  xfill True
  ysize gui.history_height

style history_name:
  xpos gui.history_name_xpos
  xanchor gui.history_name_xalign
  ypos gui.history_name_ypos
  xsize gui.history_name_width

style history_name_text:
  min_width gui.history_name_width
  text_align gui.history_name_xalign

style history_text:
  xpos gui.history_text_xpos
  ypos gui.history_text_ypos
  xanchor gui.history_text_xalign
  xsize gui.history_text_width
  min_width gui.history_text_width
  text_align gui.history_text_xalign
  layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
  xfill True

style history_label_text:
  xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

  tag menu

  default device = "keyboard"

  use game_menu(_("Help"), scroll="viewport"):

    style_prefix "help"

    vbox:
      spacing 23

      hbox:

        textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
        textbutton _("Mouse") action SetScreenVariable("device", "mouse")

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
    text _("Advances dialogue and activates the interface.")

  hbox:
    label _("Space")
    text _("Advances dialogue without selecting choices.")

  hbox:
    label _("Arrow Keys")
    text _("Navigate the interface.")

  hbox:
    label _("Escape")
    text _("Accesses the game menu.")

  hbox:
    label _("Ctrl")
    text _("Skips dialogue while held down.")

  hbox:
    label _("Tab")
    text _("Toggles dialogue skipping.")

  hbox:
    label _("Page Up")
    text _("Rolls back to earlier dialogue.")

  hbox:
    label _("Page Down")
    text _("Rolls forward to later dialogue.")

  hbox:
    label "H"
    text _("Hides the user interface.")

  hbox:
    label "S"
    text _("Takes a screenshot.")

  hbox:
    label "V"
    text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

  hbox:
    label "Shift+A"
    text _("Opens the accessibility menu.")


screen mouse_help():

  hbox:
    label _("Left Click")
    text _("Advances dialogue and activates the interface.")

  hbox:
    label _("Middle Click")
    text _("Hides the user interface.")

  hbox:
    label _("Right Click")
    text _("Accesses the game menu.")

  hbox:
    label _("Mouse Wheel Up\nClick Rollback Side")
    text _("Rolls back to earlier dialogue.")

  hbox:
    label _("Mouse Wheel Down")
    text _("Rolls forward to later dialogue.")


screen gamepad_help():

  hbox:
    label _("Right Trigger\nA/Bottom Button")
    text _("Advances dialogue and activates the interface.")

  hbox:
    label _("Left Trigger\nLeft Shoulder")
    text _("Rolls back to earlier dialogue.")

  hbox:
    label _("Right Shoulder")
    text _("Rolls forward to later dialogue.")


  hbox:
    label _("D-Pad, Sticks")
    text _("Navigate the interface.")

  hbox:
    label _("Start, Guide")
    text _("Accesses the game menu.")

  hbox:
    label _("Y/Top Button")
    text _("Hides the user interface.")

  textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
  properties gui.button_properties("help_button")
  xmargin 12

style help_button_text:
  properties gui.button_text_properties("help_button")

style help_label:
  xsize 375
  right_padding 30

style help_label_text:
  size gui.text_size
  xalign 1.0
  text_align 1.0



################################################################################
## Additional screens
################################################################################

## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

  zorder 100
  style_prefix "skip"

  frame:

    hbox:
      spacing 9

      text _("Skipping")

      text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
      text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
      text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
  alpha .5

  pause delay

  block:
    linear .2 alpha 1.0
    pause .2
    linear .2 alpha 0.5
    pause (cycle - .4)
    repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
  ypos gui.skip_ypos
  background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
  padding gui.skip_frame_borders.padding

style skip_text:
  size gui.notify_text_size

style skip_triangle:
  ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
  ## glyph in it.
  font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

  zorder 100
  style_prefix "notify"

  frame at notify_appear:
    text "[message!tq]"

  timer 3.25 action Hide('notify')


transform notify_appear:
  on show:
    alpha 0
    linear .25 alpha 1.0
  on hide:
    linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
  ypos gui.notify_ypos

  background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
  padding gui.notify_frame_borders.padding

style notify_text:
  properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

  window:
    style "nvl_window"

    has vbox:
      spacing gui.nvl_spacing

    ## Displays dialogue in either a vpgrid or the vbox.
    if gui.nvl_height:

      vpgrid:
        cols 1
        yinitial 1.0

        use nvl_dialogue(dialogue)

    else:

      use nvl_dialogue(dialogue)

    ## Displays the menu, if given. The menu may be displayed incorrectly if
    ## config.narrator_menu is set to True.
    for i in items:

      textbutton i.caption:
        action i.action
        style "nvl_button"

  add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

  for d in dialogue:

    window:
      id d.window_id

      fixed:
        yfit gui.nvl_height is None

        if d.who is not None:

          text d.who:
            id d.who_id

        text d.what:
          id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
  xfill True
  yfill True

  background "gui/nvl.png"
  padding gui.nvl_borders.padding

style nvl_entry:
  xfill True
  ysize gui.nvl_height

style nvl_label:
  xpos gui.nvl_name_xpos
  xanchor gui.nvl_name_xalign
  ypos gui.nvl_name_ypos
  yanchor 0.0
  xsize gui.nvl_name_width
  min_width gui.nvl_name_width
  text_align gui.nvl_name_xalign

style nvl_dialogue:
  xpos gui.nvl_text_xpos
  xanchor gui.nvl_text_xalign
  ypos gui.nvl_text_ypos
  xsize gui.nvl_text_width
  min_width gui.nvl_text_width
  text_align gui.nvl_text_xalign
  layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
  xpos gui.nvl_thought_xpos
  xanchor gui.nvl_thought_xalign
  ypos gui.nvl_thought_ypos
  xsize gui.nvl_thought_width
  min_width gui.nvl_thought_width
  text_align gui.nvl_thought_xalign
  layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
  properties gui.button_properties("nvl_button")
  xpos gui.nvl_button_xpos
  xanchor gui.nvl_button_xalign

style nvl_button_text:
  properties gui.button_text_properties("nvl_button")
