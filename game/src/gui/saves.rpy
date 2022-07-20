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
        align (0.5, 0.5)
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

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text
