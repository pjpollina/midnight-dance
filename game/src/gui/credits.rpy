label credits:
  scene bg bedroom
  show image Solid("#0007")
  with Dissolve(3.0)
  play music midnight_waltz volume 0.75 fadein 3.0

  $ _game_menu_screen = None

  show credit oishii with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit acey with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit luciam with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit kyle with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit nsaid with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit pj ui with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit gelby with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit pj sfx with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit jerron with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit allen with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit magicem with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit pj va with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit proofread with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show credit pj code with dissolve
  $ renpy.pause(3.5, hard=True)
  hide credit with dissolve

  show postcredit a with dissolve
  $ renpy.pause(3.5, hard=True)
  hide postcredit with dissolve

  show postcredit b with Dissolve(1.0)
  $ renpy.pause(5.0, hard=True)
  hide postcredit with Dissolve(1.0)

  stop music fadeout 4.0
  scene black with Dissolve(4.0)

  $ _game_menu_screen = "saves"

  return

style credits_title:
  font cardinal
  size 96
  align (0.5, 0.5)
  text_align 0.5
  outlines [(3, "#000", 1, 1)]

style credits_text_a:
  size 48
  text_align 0.5
  align (0.5, 0.5)
  outlines [(3, "#000", 1, 1)]

style credits_text_b is credits_text_a:
  align (0.45, 0.45)
  text_align 0.0
  font cardinal
  size 72

style credits_text_c is credits_text_a:
  text_align 1.0
  align (0.55, 0.55)
  size 72

image credit oishii:
  contains:
    Text("The Midnight Dance", style="credits_title", yalign=0.45)
  contains:
    Text(_("Created, Directed, and Written by OishiiWrites"), style="credits_text_a", yalign=0.55)

image credit acey:
  contains:
    Text(_("Sprite Artist"), style="credits_text_b")
  contains:
    Text("Social Demonz", style="credits_text_c")

image credit luciam:
  contains:
    Text(_("Background Artist"), style="credits_text_b")
  contains:
    Text("Luciam Art Studio", style="credits_text_c")

image credit kyle:
  contains:
    Text(_("CG Artist"), style="credits_text_b")
  contains:
    Text("Moonkipp", style="credits_text_c")

image credit nsaid:
  contains:
    Text(_("UI Designer"), style="credits_text_b")
  contains:
    Text("NSAID", style="credits_text_c")

image credit pj ui:
  contains:
    Text(_("Gallery/Accessibility Designer"), style="credits_text_b")
  contains:
    Text("PJ Pollina", style="credits_text_c")

image credit gelby:
  contains:
    Text(_("Composer"), style="credits_text_b")
  contains:
    Text("Austin \"GGelby\" Gelber", style="credits_text_c")

image credit pj sfx:
  contains:
    Text(_("Sound Effects"), style="credits_text_b")
  contains:
    Text("PJ Pollina", style="credits_text_c")

image credit jerron:
  contains:
    Text(_("Everett Voice Actor"), style="credits_text_b")
  contains:
    Text("Jerron Bacat", style="credits_text_c")

image credit allen:
  contains:
    Text(_("Balthazar Voice Actor"), style="credits_text_b")
  contains:
    Text("Allen Chan", style="credits_text_c")

image credit magicem:
  contains:
    Text(_("Maid Voice Actor"), style="credits_text_b")
  contains:
    Text("MagicEm", style="credits_text_c")

image credit pj va:
  contains:
    Text(_("Guard \"Voice Actor\""), style="credits_text_b")
  contains:
    Text("PJ Pollina {size=-16}(unfortunately){/size}", style="credits_text_c")

image credit proofread:
  contains:
    Text(_("Proofreading & Editing"), style="credits_text_b", yalign=0.4)
  contains:
    Text("QuickNuminex\nSharlotte Teidy\nPJ Pollina", style="credits_text_c",  yalign=0.6)

image credit pj code = Text(_("Programmed in Ren'Py 8.0.2 by PJ Pollina (aeugchad)"), style="credits_text_a")

image postcredit a = Text(_("Developed in two months for Yaoi Game Jam 2022"), style="credits_text_a")
image postcredit b = Text(_("From everyone on the Midnight Dance Team, thank you for playing!"), style="credits_text_a")
