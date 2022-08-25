## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 20

screen history():
  tag menu
  predict False

  use game_menu(_("History")):
    style_prefix "history"

    frame margin (40, 10, 90, 40) padding (40, 10, 90, 40) yoffset -20:
      viewport:
        id "history"
        mousewheel True
        draggable True
        has vbox spacing 20

        for entry in _history_list:
          hbox:
            frame:
              xsize 200
              text (entry.who or "(...)") align (0.5, 0.5)
            text entry.what

        if not _history_list:
          label _("The dialogue history is empty.")

      vbar value YScrollValue("history")

style history_vscrollbar:
  xpos 1.0
  xoffset 20
  thumb    Solid("#000A", xalign=1.0, xsize=8)
  base_bar Solid("#FFF4", xalign=1.0, xsize=8)
