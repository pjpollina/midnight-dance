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
      button style "quick_log" action ShowMenu("history")
      button style "quick_opt" action ShowMenu("settings")
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

## Row 1
style quick_auto is quick_button:
  background "gui/buttons/quick/[prefix_]auto.webp"
  insensitive_background Transform("gui/buttons/quick/idle_auto.webp", alpha=0.66)
style quick_skip is quick_button:
  background "gui/buttons/quick/[prefix_]skip.webp"
  insensitive_background Transform("gui/buttons/quick/idle_skip.webp", alpha=0.66)

## Row 2
style quick_log is quick_button:
  background "gui/buttons/quick/[prefix_]log.webp"
  insensitive_background Transform("gui/buttons/quick/idle_log.webp", alpha=0.66)
style quick_opt is quick_button:
  background "gui/buttons/quick/[prefix_]opt.webp"
  insensitive_background Transform("gui/buttons/quick/idle_opt.webp", alpha=0.66)

## Row 3
style quick_save is quick_button:
  background "gui/buttons/quick/[prefix_]save.webp"
  insensitive_background Transform("gui/buttons/quick/idle_save.webp", alpha=0.66)
style quick_load is quick_button:
  background "gui/buttons/quick/[prefix_]load.webp"
  insensitive_background Transform("gui/buttons/quick/idle_load.webp", alpha=0.66)
