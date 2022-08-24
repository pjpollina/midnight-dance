## Settings screen #############################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves. The much better settings screen does this too.

screen settings():
  tag menu
  style_prefix "settings"

  use game_menu("Settings"):
    hbox spacing 35:
      vbox spacing 40:

        vbox spacing 20:
          xsize 400
          yfill False

          button style_suffix "header" action NullAction():
            background nav_header("Display")
            alt "Display"
          textbutton _("Window")     style "radio_button" action Preference("display", "window")
          textbutton _("Fullscreen") style "radio_button" action Preference("display", "fullscreen")
          null height 10

          button style_suffix "header" action NullAction():
            background nav_header("Skip")
            alt "Skip"
          textbutton _("Unseen Text")   style "check_button" action Preference("skip", "toggle")
          textbutton _("After Choices") style "check_button" action Preference("after choices", "toggle")
          null height 10

          button:
            xysize (200, 200)
            idle_foreground  "gui/buttons/access_idle.webp"
            hover_foreground "gui/buttons/access_hover.webp"
            action ShowMenu("access")
            alt "Access"

      frame:
        has vbox
        align (0.5, 0.0)
        style_prefix "slider"

        textbutton _("Text Speed"):
          style_suffix "label"
          alt "Text Speed"
          action NullAction()
        bar value Preference("text speed")
        null height 20

        textbutton _("Auto-Forward Time"):
          style_suffix "label"
          alt "Auto-Forward Time"
          action NullAction()
        bar value Preference("auto-forward time")
        null height 80

        textbutton _("Music Volume"):
          style_suffix "label"
          alt "Music Volume"
          action NullAction()
        bar value Preference("music volume")
        null height 20

        textbutton _("Sound Volume"):
          style_suffix "label"
          alt "Sound Volume"
          action NullAction()
        bar value Preference("sound volume")
        null height 20

        textbutton _("Voice Volume"):
          style_suffix "label"
          alt "Voice Volume"
          action NullAction()
        bar value Preference("voice volume")
        null height 20

style settings_header:
  xysize (425, 125)
  alt None

style settings_button
style settings_button_text:
  size 56
  text_align 0.5

style slider_label:
  align   (0.5, 0.0)
  padding (10, 10, 10, 10)
  background Solid("#000A")
style slider_label_text:
  yalign 0.5
