## #############################################################################
## Gallery Screen ##############################################################
##
## A one-stop shop for browsing all the game's assets.

python early:
  next_page = lambda current: ("scenes" if current == "sprites" else "sprites")

screen gallery():
  tag menu
  style_prefix "gallery"

  default page = "scenes"

  frame background "gui/gallery/background.webp":
    add Image("gui/gallery/header.webp", align=(0.5, 0.0))

    button:
      action Show("music")
      style_suffix "music"

    window:
      xfill True
      yfill True
      margin (120, 160, 120, 140)

      $ renpy.transition(dissolve)
      if page == "scenes":
        use scenes()
      if page == "sprites":
        use sprites()

    button style_suffix "larrow" action SetScreenVariable("page", next_page(page))
    button style_suffix "rarrow" action SetScreenVariable("page", next_page(page))
    textbutton _("Return") action Return() style_suffix "return"

style gallery_return:
  align (0.5, 1.0)
  xysize (240, 100)
  yoffset -30
style gallery_return_text:
  size 72
  font cardinal
  align (0.5, 0.5)
  idle_color  "#FFF"
  hover_color "#111"

style gallery_larrow:
  align (0.0, 0.5)
  xysize (120, 160)
  idle_foreground  Image("gui/gallery/arrow_idle.webp",  align=(0.5, 0.5))
  hover_foreground Image("gui/gallery/arrow_hover.webp", align=(0.5, 0.5))
style gallery_rarrow is gallery_larrow:
  align (1.0, 0.5)
  idle_foreground  Transform("gui/gallery/arrow_idle.webp",  xzoom=-1.0, align=(0.5, 0.5))
  hover_foreground Transform("gui/gallery/arrow_hover.webp", xzoom=-1.0, align=(0.5, 0.5))

style gallery_music:
  xysize (120, 120)
  offset (30, 30)
  foreground "gui/gallery/[prefix_]music.webp"
  selected_foreground None
