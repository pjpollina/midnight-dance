## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():
  zorder 100
  style_prefix "quick"

  frame:
    has vbox
    hbox:
      button style "quick_auto" action Preference("auto-forward", "toggle")
      button style "quick_skip" action Skip() alternate Skip(fast=True, confirm=True)
    hbox:
      button style "quick_log" action ShowMenu('history')
      button style "quick_options" action ShowMenu('preferences')
    hbox:
      button style "quick_save" action QuickSave()
      button style "quick_load" action QuickLoad()

## Quick Menu styles ###########################################################

## Frame
style quick_frame:
  pos (1711, 835)
  xysize (141, 196)
  background None

## Quick menu buttons
style quick_button:
  xysize (76, 75)
style quick_auto is quick_button:
  idle_background  "gui/button/auto_quick_idle.webp"
  hover_background "gui/button/auto_quick_hover.webp"
  insensitive_background Transform("gui/button/auto_quick_idle.webp", alpha=0.66)
style quick_load is quick_button:
  idle_background  "gui/button/load_quick_idle.webp"
  hover_background "gui/button/load_quick_hover.webp"
  insensitive_background Transform("gui/button/load_quick_idle.webp", alpha=0.66)
style quick_save is quick_button:
  idle_background  "gui/button/save_quick_idle.webp"
  hover_background "gui/button/save_quick_hover.webp"
  insensitive_background Transform("gui/button/save_quick_idle.webp", alpha=0.66)
style quick_log is quick_button:
  idle_background  "gui/button/log_quick_idle.webp"
  hover_background "gui/button/log_quick_hover.webp"
  insensitive_background Transform("gui/button/log_quick_idle.webp", alpha=0.66)
style quick_options is quick_button:
  idle_background  "gui/button/options_quick_idle.webp"
  hover_background "gui/button/options_quick_hover.webp"
  insensitive_background Transform("gui/button/options_quick_idle.webp", alpha=0.66)
style quick_skip is quick_button:
  idle_background  "gui/button/skip_quick_idle.webp"
  hover_background "gui/button/skip_quick_hover.webp"
  insensitive_background Transform("gui/button/skip_quick_idle.webp", alpha=0.66)
