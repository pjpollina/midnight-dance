## Settings screen #############################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves. The much better settings screen does this too.

screen settings():
  tag menu
  style_prefix "settings"

  use game_menu("Settings"):
    hbox:
      frame:
        has vbox
        align (0.5, 0.0)

        label _("Display")
        vbox spacing 20:
          textbutton _("Window")     style "radio_button" action Preference("display", "window")
          textbutton _("Fullscreen") style "radio_button" action Preference("display", "fullscreen")

        null height 80

        label _("Skip")
        vbox spacing 20:
          textbutton _("Unseen Text")   style "check_button" action Preference("skip", "toggle")
          textbutton _("After Choices") style "check_button" action Preference("after choices", "toggle")
          textbutton _("Transitions")   style "check_button" action InvertSelected(Preference("transitions", "toggle"))

      frame:
        has vbox
        align (0.5, 0.0)
        style_prefix "slider"

        label _("Text Speed")
        bar value Preference("text speed")
        null height 20

        label _("Auto-Forward Time")
        bar value Preference("auto-forward time")
        null height 80

        label _("Music Volume")
        bar value Preference("music volume")
        null height 20

        label _("Sound Volume")
        bar value Preference("sound volume")
        null height 20

        label _("Voice Volume")
        bar value Preference("voice volume")
        null height 20

## Settings styles #############################################################

style settings_frame:
  xysize (700, 800)
style settings_hbox:
  spacing 35

style settings_label:
  align   (0.5, 0.0)
  padding (10, 10, 10, 10)
style settings_label_text is empty:
  size 96
  font cardinal
  text_align 0.5

style slider_label is settings_label
style slider_label_text:
  yalign 0.5
