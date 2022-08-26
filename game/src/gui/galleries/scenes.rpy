## #############################################################################
## Scenes Gallery ##############################################################
##
## Browse all of the CGs by Moonkip and backgrounds by Luciam.

screen scenes():
  tag menu
  style_prefix "scene"

  vbox:
    align (0.5, 0.5)
    spacing 30

    text _("CGs by {a=https://kyleechii.carrd.co/}Kyleechii/Moonkipp{/a}")

    hbox:
      button style style.scene_button["cg_01a"]:
        action Show("scene_viewer", dissolve, displayable="cg balthcony")
        alt "The CG of Balthazar on the balcony"

      button style style.scene_button["cg_01b"]:
        action Show("scene_viewer", dissolve, displayable="cg balthcony dark")
        alt "The CG of Balthazar on the balcony, cloaked in shadow, his red eye glowing"

      button style style.scene_button["cg_01c"]:
        action Show("scene_viewer", dissolve, displayable="cg balthcony eyes")
        alt "The CG of Balthazar on the balcony, zoomed in on his face, in shadow"

      button style style.scene_button["cg_02"]:
        action Show("scene_viewer", dissolve, displayable="cg bedthazar")
        alt "The CG of Balthazar asleep in Everett's bed"

    hbox:
      button style style.scene_button["cg_03"]:
        action Show("scene_viewer", dissolve, displayable="cg waltazar")
        alt "The CG of Everett and Balthazar dancing"

      button style style.scene_button["cg_04"]:
        action Show("scene_viewer", dissolve, displayable="cg yaoitime")
        alt "The CG of Everett and Balthazar kissing"

      button style style.scene_button["cg_05"]:
        action Show("scene_viewer", dissolve, displayable="cg returnazar")
        alt "The CG of Balthazar, flowers in hand, smiling"

    text _("Backgrounds by {a=https://ko-fi.com/luciam_artstudio}Luciam Art Studio{/a}")

    hbox:
      button style style.scene_button["bg_01"]:
        action Show("scene_viewer", dissolve, displayable="bg balcony")
        alt "The background of the balcony"

      button style style.scene_button["bg_02"]:
        action Show("scene_viewer", dissolve, displayable="bg balcony lit")
        alt "The background of the balcony, with fireworks"

      button style style.scene_button["bg_03"]:
        action Show("scene_viewer", dissolve, displayable="bg bedroom")
        alt "The background of Everett's bedroom, dark"

      button style style.scene_button["bg_04"]:
        action Show("scene_viewer", dissolve, displayable="bg bedroom lit")
        alt "The background of Everett's bedroom, dark"

screen scene_viewer(displayable):
  zorder 2000
  modal True
  key "game_menu" action Hide(transition=dissolve)
  add displayable

## Styles ######################################################################

style scene_button:
  xysize (330, 190)
  foreground "gui/gallery/scenes/[prefix_]frame.webp"

init python:
  for pic in ["bg_01", "bg_02", "bg_03", "bg_04", "cg_01a", "cg_01b", "cg_01c", "cg_02", "cg_03", "cg_04", "cg_05"]:
    style.scene_button[pic].idle_background = Transform("gui/gallery/scenes/{}.webp".format(pic), matrixcolor=SepiaMatrix())
    style.scene_button[pic].hover_background = "gui/gallery/scenes/{}.webp".format(pic)

style scene_hbox:
  spacing 30
  xalign 0.5

style scene_text is text:
  align (0.5, 0.0)
  text_align 0.5
