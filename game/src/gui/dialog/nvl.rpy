## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):
  window:
    style "nvl_window"
    has vbox:
      spacing 15

    use nvl_dialogue(dialogue)

    for i in items:
      textbutton i.caption:
        action i.action
        style "nvl_button"

screen nvl_dialogue(dialogue):
  for d in dialogue:
    window id d.window_id:
      fixed:
        if d.who is not None:
          text d.who:
            id d.who_id
        text d.what:
          id d.what_id

define config.nvl_list_length = 6

style nvl_window:
  xfill True
  yfill True
  background Solid("#FFF8")
  padding (0, 15, 0, 30)

style nvl_entry:
  xfill True
  ysize 173

style nvl_label is say_label:
  pos (645, 0)
  anchor (1.0, 0.0)
  xsize 225
  min_width 225
  text_align 1.0

style nvl_dialogue is say_dialogue:
  pos (675, 12)
  xanchor 0.0
  xsize 885
  min_width 885
  text_align 0.0

style nvl_thought:
  pos (360, 0)
  xpos 360
  xanchor 0.0
  xsize 1170
  min_width 1170
  text_align 0.0

style nvl_button is button:
  xpos 675
  xalign 0.0
style nvl_button_text is button_text
