init python:
  def ellipse_tag(tag, arg):
    if arg is "":
      return [(renpy.TEXT_TEXT, "...")]
    return [(renpy.TEXT_TAG, "cps={}".format(arg)), (renpy.TEXT_TEXT, "..."), (renpy.TEXT_TAG, "/cps")]

  def em_tag(tag, _arg):
    return [(renpy.TEXT_TEXT, "—")]

  config.self_closing_custom_text_tags["dots"] = ellipse_tag
  config.self_closing_custom_text_tags["em"] = em_tag
