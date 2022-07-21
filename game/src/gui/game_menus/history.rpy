## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
  tag menu
  predict False

  use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
    style_prefix "history"
    vbox spacing 50:
      for h in _history_list:
        if h.who:
          label h.who:
            style "history_name"
            substitute False

            if "color" in h.who_args:
              text_color h.who_args["color"]

        $ what = renpy.filter_text_tags(h.what, allow={"alt", "noalt"})
        text what:
          substitute False

      if not _history_list:
        label _("The dialogue history is empty.")

define gui.history_height = 210
define config.history_length = 250

style history_window:
  xfill True
  ysize gui.history_height

style history_name:
  pos     (233, 0)
  xsize   233
  xanchor 1.0
style history_name_text:
  min_width  233
  text_align 1.0

style history_text:
  pos (255, 3)
  xanchor (0.0)
  xsize 1110
  min_width 1110
  text_align 0.0
  layout "subtitle"

style history_label:
  xfill True
style history_label_text:
  xalign 0.5
