## Settings screen #############################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves. The much better settings screen does this too.

python early:
  config.font_transforms["dejavuserif"] = lambda _: "gui/fonts/DejaVuSerif/Regular.ttf"

  noheader = lambda: preferences.font_transform is not None
  ft_dyx = lambda: preferences.font_transform == "opendyslexic"
  ft_dvs = lambda: preferences.font_transform == "dejavuserif"

  ft_hdsize = lambda: (80 if ft_dyx() else (72 if ft_dvs() else 96))

  def nav_header(name, size=None):
    if noheader():
      return Text(name, font=cardinal, size=(size or ft_hdsize()), offset=(0, -10), align=(0.5, 0.5), color="#AB7739", outlines=[(3, "#000", 1, 1)])
    return Image("gui/headers/{}.webp".format(name), align=(0.5, 0.5))

screen settings():
  tag menu
  style_prefix "settings"

  use game_menu("Settings"):
    hbox xalign 0.5:
      yoffset -20
      use display_settings()
      use sound_settings()
      use access_settings()
    null height 35

screen display_settings():
  vbox xsize 425:
    button style "settings_header" action NullAction() background nav_header("Display") alt "Display"

    textbutton _("Screen Mode") action NullAction()
    vbox spacing 15 xalign 0.5:
      textbutton _("Windowed")   action Preference("display", "window")     style "radio_button"
      textbutton _("Fullscreen") action Preference("display", "fullscreen") style "radio_button"

    null height 25
    frame

    textbutton _("Text Speed") action NullAction()
    bar value Preference("text speed")
    textbutton _("Auto-Forward") action NullAction()
    bar value Preference("auto-forward time")

    null height 25
    frame

    textbutton _("Skip") action NullAction()
    vbox spacing 10 xalign 0.5:
      textbutton _("Unseen Text")   style "check_button" action Preference("skip", "toggle")
      textbutton _("After Choices") style "check_button" action Preference("after choices", "toggle")

screen sound_settings():
  vbox xsize 425:
    button style "settings_header" action NullAction() background nav_header("Sound") alt "Sound"

    textbutton _("Music Volume") action NullAction()
    bar value Preference("music volume")

    textbutton _("Sound Volume") action NullAction()
    bar value Preference("sound volume")

    textbutton _("Voice Volume") action NullAction()
    bar value Preference("voice volume")

    null height 25
    frame

    textbutton _("Self Voicing") action NullAction()
    vbox spacing 15 xalign 0.5:
      textbutton _("Disabled")       action Preference("self voicing",      "disable") style "radio_button"
      textbutton _("Clipboard")      action Preference("clipboard voicing",  "enable") style "radio_button"
      textbutton _("Text-to-speech") action Preference("self voicing",       "enable") style "radio_button"
      if config.developer:
          textbutton _("Debug") action Preference("debug voicing", "enable") style "radio_button"

screen access_settings():
  vbox xsize 425:
    button style "settings_header" action NullAction() background nav_header("Access") alt "Access"
    null height 10
    textbutton _("High-Contrast Text") action NullAction()
    vbox spacing 15 xalign 0.5:
      textbutton _("Enable")  style "radio_button" action Preference("high contrast text", "enable")
      textbutton _("Disable") style "radio_button" action Preference("high contrast text", "disable")

    null height 25
    frame

    textbutton _("Font Override") action NullAction()
    null height 10
    vbox spacing 15 xalign 0.5:
      textbutton _("Default")       style "radio_button" action Preference("font transform", None)
      textbutton _("DejaVu Serif")  style "radio_button" action Preference("font transform", "dejavuserif")
      textbutton _("Open Dyslexic") style "radio_button" action Preference("font transform", "opendyslexic")

style settings_header:
  xysize (425, 125)

style settings_button:
  padding (10, 10, 10, 10)
style settings_button_text:
  yalign 0.5
  size 36
  color "#AB7739"
  outlines [(2, "#000", 1, 1)]

style settings_frame:
  xysize (300, 3)
  background Solid("#AB773998")
  align (0.5, 0.5)
