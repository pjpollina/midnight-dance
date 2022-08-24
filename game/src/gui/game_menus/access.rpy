## Access screen ###############################################################
##
## I am so goddamn mad this took so fucking long to do right. I used fucking
## LAMBDAS. IN REN'PY.

default persistent.noheader = False

python early:
  config.font_transforms["dejavuserif"] = lambda _: "gui/fonts/DejaVuSerif/Regular.ttf"

  ft_dyx = lambda: preferences.font_transform == "opendyslexic"
  ft_dvs = lambda: preferences.font_transform == "dejavuserif"

  def access_header(name, path, size=60):
    if persistent.noheader:
      return Text(name, size=size, align=(0.0, 0.0), offset=(-2, -10))
    return Image("gui/headers/access/{}{}.webp".format(path, ("_dyx" if ft_dyx() else "")), align=(0.0, 0.0), color="#DB4")

  ft_suffix = lambda: ("_dyx" if ft_dyx() else ("_dvs" if ft_dvs() else ""))
  ft_hdsize = lambda: (80 if ft_dyx() else (72 if ft_dvs() else 96))

  def nav_header(name, size=None):
    if persistent.noheader:
      return Text(name, font=cardinal, size=(size or ft_hdsize()), offset=(0, -10), align=(0.5, 0.5), color="#DB4")
    return Image("gui/headers/{}{}.webp".format(name, ft_suffix()), align=(0.5, 0.5))

screen access():
  tag menu
  style_prefix "access"

  use game_menu("Access"):
    hbox spacing 35:
      null width 10

      vbox spacing 10:
        null height 25

        button style "access_header" action NullAction():
          background access_header("Font Override", "fontover")
          alt "Font Override"
        textbutton _("Default")       style_suffix "radio_button" action Preference("font transform", None)
        textbutton _("DejaVu Serif")  style_suffix "radio_button" action Preference("font transform", "dejavuserif")
        textbutton _("Open Dyslexic") style_suffix "radio_button" action Preference("font transform", "opendyslexic")
        null height 25

        button style "access_header" action NullAction():
          background access_header("Header Style", "headers")
          alt "Header Style"
        textbutton _("Fancy")           action SetVariable("persistent.noheader", False) style_suffix "radio_button"
        textbutton _("Access Friendly") action SetVariable("persistent.noheader", True ) style_suffix "radio_button"
        null height 25

        button style "access_header" action NullAction():
          background access_header("High Contrast", "contrast")
          alt "High Constrast"
        textbutton _("Enable")  action Preference("high contrast text", "enable")  style_suffix "radio_button"
        textbutton _("Disable") action Preference("high contrast text", "disable") style_suffix "radio_button"

      vbox spacing 10:
        null height 25

        button style "access_header" action NullAction():
          background access_header("Self-Voicing", "selfvoice")
          alt "Self-Voicing"
        textbutton _("Disabled")       action Preference("self voicing",      "disable") style_suffix "radio_button"
        textbutton _("Clipboard")      action Preference("clipboard voicing",  "enable") style_suffix "radio_button"
        textbutton _("Text-to-speech") action Preference("self voicing",       "enable") style_suffix "radio_button"
        if config.developer:
          textbutton _("Debug") action Preference("debug voicing", "enable") style_suffix "radio_button"
        null height 25

style access_radio_button:
  xalign 0.0
  xoffset 40
  xsize 460
style access_header:
  xysize (600, 80)
  background Solid("#F0FA")
