## Settings screen #############################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves. The much better settings screen does this too.

screen settings():
  tag menu
  style_prefix "settings"

  use game_menu("Settings", scroll="viewport"):
    hbox:
      frame:
        has vbox
        align (0.5, 0.0)

        label _("Display")
        textbutton _("Window")     style "radio_button" action Preference("display", "window")
        textbutton _("Fullscreen") style "radio_button" action Preference("display", "fullscreen")

        null height 80

        label _("Skip")
        textbutton _("Unseen Text")   action Preference("skip", "toggle")
        textbutton _("After Choices") action Preference("after choices", "toggle")
        textbutton _("Transitions")   action InvertSelected(Preference("transitions", "toggle"))

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

style settings_frame:
  xysize(700, 800)
  background None
style settings_hbox:
  spacing 35

style settings_label:
  align   (0.5, 0.0)
  padding (10, 10, 10, 10)
style settings_label_text:
  size 96
  color "#FFF"
  font cardinal
  text_align 0.5

style slider_label is settings_label
style slider_label_text is settings_label_text:
  size 40
  font book_antiqua

style slider_slider:
  xysize(350, 40)
  left_bar  "gui/slider/full.webp"
  right_bar "gui/slider/empty.webp"
  thumb     None
  xalign    0.5

style radio_button:
  padding (27, 6, 6, 6)
  foreground "gui/button/radio_[prefix_]foreground.png"
style radio_button_text

style check_button:
  properties gui.button_properties("check_button")
  padding (27, 6, 6, 6)
  foreground "gui/button/check_[prefix_]foreground.png"
style check_button_text
