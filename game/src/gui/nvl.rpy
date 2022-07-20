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

    use nvl_dialogue(dialogue)

    for i in items:
      textbutton i.caption:
        action i.action
        style "nvl_button"

screen nvl_dialogue(dialogue):
  for d in dialogue:
    window id d.window_id:
      fixed:
        yfit gui.nvl_height is None
        if d.who is not None:
          text d.who:
            id d.who_id
        text d.what:
          id d.what_id

define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default:
  xfill True
  yfill True
  background "gui/nvl.png"
  padding gui.nvl_borders.padding

style nvl_entry is default:
  xfill True
  ysize gui.nvl_height

style nvl_label is say_label:
  xpos gui.nvl_name_xpos
  xanchor gui.nvl_name_xalign
  ypos gui.nvl_name_ypos
  yanchor 0.0
  xsize gui.nvl_name_width
  min_width gui.nvl_name_width
  text_align gui.nvl_name_xalign

style nvl_dialogue is say_dialogue:
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

style nvl_button is button:
  properties gui.button_properties("nvl_button")
  xpos gui.nvl_button_xpos
  xanchor gui.nvl_button_xalign
style nvl_button_text is button_text:
  properties gui.button_text_properties("nvl_button")
