## #############################################################################
## Gallery Screen ##############################################################
##
## A one-stop shop for browsing all the game's assets.

python early:
  GALLARY_ORDERING = {
    "scenes":  ("music",   "sprites"),
    "sprites": ("scenes",  "music"),
    "music":   ("sprites", "scenes"),
  }

screen gallery():
  tag menu
  style_prefix "gallery"

  default page = "scenes"

  frame background "gui/gallery/background.webp":
    add Image("gui/gallery/header.webp", align=(0.5, 0.0))

    window:
      xfill True
      yfill True
      margin (120, 160, 120, 140)

      if page == "scenes":
        $ renpy.transition(dissolve)
        use scenes()
      if page == "sprites":
        $ renpy.transition(dissolve)
        use sprites()
      if page == "music":
        $ renpy.transition(dissolve)
        use music()

    button style_suffix "larrow" action SetScreenVariable("page", GALLARY_ORDERING[page][0])
    button style_suffix "rarrow" action SetScreenVariable("page", GALLARY_ORDERING[page][1])
    textbutton _("Return") action Return()

style gallery_button:
  align (0.5, 1.0)
  xysize (240, 100)
  yoffset -30
style gallery_button_text:
  size 72
  font cardinal
  align (0.5, 0.5)
  idle_color     "#FFF"
  hover_color    "#111"

style gallery_larrow:
  align (0.0, 0.5)
  xysize (120, 160)
  idle_foreground  Image("gui/gallery/arrow_idle.webp",  align=(0.5, 0.5))
  hover_foreground Image("gui/gallery/arrow_hover.webp", align=(0.5, 0.5))
style gallery_rarrow is gallery_larrow:
  align (1.0, 0.5)
  idle_foreground  Transform("gui/gallery/arrow_idle.webp",  xzoom=-1.0, align=(0.5, 0.5))
  hover_foreground Transform("gui/gallery/arrow_hover.webp", xzoom=-1.0, align=(0.5, 0.5))
