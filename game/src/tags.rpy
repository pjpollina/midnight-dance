init python:
  def ellipse_tag(tag, arg):
    if arg is "":
      return [(renpy.TEXT_TEXT, "...")]
    return [(renpy.TEXT_TAG, "cps={}".format(arg)), (renpy.TEXT_TEXT, "..."), (renpy.TEXT_TAG, "/cps")]

  def em_tag(tag, _arg):
    return [(renpy.TEXT_TEXT, "—")]

  def awt_tag(tag, arg):
    val = float(("6.0" if arg is "" else arg))
    return[(renpy.TEXT_TAG, "cps={}".format(val)), (renpy.TEXT_TEXT, " "), (renpy.TEXT_TAG, "/cps")]

  config.self_closing_custom_text_tags["dots"] = ellipse_tag
  config.self_closing_custom_text_tags["em"]   = em_tag
  config.self_closing_custom_text_tags["awt"]  = awt_tag
