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
      button action Show("scene_viewer", dissolve, displayable="cg balthcony"):
        background "gui/gallery/slots/cg_[prefix_]01a.webp"
        alt "The CG of Balthazar on the balcony"
      button action Show("scene_viewer", dissolve, displayable="cg balthcony dark"):
        background "gui/gallery/slots/cg_[prefix_]01b.webp"
        alt "The CG of Balthazar on the balcony, cloaked in shadow, his red eye glowing"
      button action Show("scene_viewer", dissolve, displayable="cg balthcony eyes"):
        background "gui/gallery/slots/cg_[prefix_]01c.webp"
        alt "The CG of Balthazar on the balcony, zoomed in on his face, in shadow"
      button action Show("scene_viewer", dissolve, displayable="cg bedthazar"):
        background "gui/gallery/slots/cg_[prefix_]02.webp"
        alt "The CG of Balthazar asleep in Everett's bed"

    hbox:
      button action Show("scene_viewer", dissolve, displayable="cg waltazar"):
        background "gui/gallery/slots/cg_[prefix_]03.webp"
        alt "The CG of Everett and Balthazar dancing"
      button action Show("scene_viewer", dissolve, displayable="cg yaoitime"):
        background "gui/gallery/slots/cg_[prefix_]04.webp"
        alt "The CG of Everett and Balthazar kissing"
      button action Show("scene_viewer", dissolve, displayable="cg returnazar"):
        background "gui/gallery/slots/cg_[prefix_]05.webp"
        alt "The CG of Balthazar, flowers in hand, smiling"

    text _("Backgrounds by {a=https://ko-fi.com/luciam_artstudio}Luciam Art Studio{/a}")

    hbox:
      button action Show("scene_viewer", dissolve, displayable="bg balcony"):
        background "gui/gallery/slots/bg_[prefix_]01.webp"
        alt "The background of the balcony"
      button action Show("scene_viewer", dissolve, displayable="bg balcony lit"):
        background "gui/gallery/slots/bg_[prefix_]02.webp"
        alt "The background of the balcony, with fireworks"
      button action Show("scene_viewer", dissolve, displayable="bg bedroom"):
        background "gui/gallery/slots/bg_[prefix_]03.webp"
        alt "The background of Everett's bedroom, dark"
      button action Show("scene_viewer", dissolve, displayable="bg bedroom lit"):
        background "gui/gallery/slots/bg_[prefix_]04.webp"
        alt "The background of Everett's bedroom, dark"

screen scene_viewer(displayable):
  zorder 2000
  modal True
  key "game_menu" action Hide(transition=dissolve)
  add displayable

## Styles ######################################################################

style scene_button:
  xysize (320, 180)
  idle_foreground  Solid("#0007")
  hover_foreground None

style scene_hbox:
  spacing 30
  xalign 0.5

style scene_text is text:
  align (0.5, 0.0)
  text_align 0.5
