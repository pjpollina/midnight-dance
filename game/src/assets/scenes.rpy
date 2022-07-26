init python:
  ## Constants
  STARMASKS = [Tile("masks/mask_a.webp"), Tile("masks/mask_b.webp"), Tile("masks/mask_c.webp")]
  FRAMETIME = 0.66

  ## Constructor
  def starframes(child):
    out = []
    for mask in STARMASKS:
      out.append(AlphaMask(child, mask))
    return out

  bedroom_dark_stars = starframes("scenes/bgs/bedroom_dark_stars.webp")
  bedroom_lit_stars  = starframes("scenes/bgs/bedroom_lit_stars.webp")
  balcony_dark_stars = starframes("scenes/bgs/balcony_dark_stars.webp")

## BACKGROUNDS #################################################################

image bg bedroom:
  align (0.5, 0.5)
  contains:
    "scenes/bgs/bedroom_dark.webp"
  contains:
    bedroom_dark_stars[0] with Dissolve(FRAMETIME)
    pause FRAMETIME
    bedroom_dark_stars[1] with Dissolve(FRAMETIME)
    pause FRAMETIME
    bedroom_dark_stars[2] with Dissolve(FRAMETIME)
    pause FRAMETIME
    repeat

image bg bedroom lit:
  align (0.5, 0.5)
  contains:
    "scenes/bgs/bedroom_lit.webp"
  contains:
    bedroom_lit_stars[0] with Dissolve(FRAMETIME)
    pause FRAMETIME
    bedroom_lit_stars[1] with Dissolve(FRAMETIME)
    pause FRAMETIME
    bedroom_lit_stars[2] with Dissolve(FRAMETIME)
    pause FRAMETIME
    repeat

image bg balcony:
  align (0.5, 0.5)
  contains:
    "scenes/bgs/balcony_dark.webp"
  contains:
    balcony_dark_stars[0] with Dissolve(FRAMETIME)
    pause FRAMETIME
    balcony_dark_stars[1] with Dissolve(FRAMETIME)
    pause FRAMETIME
    balcony_dark_stars[2] with Dissolve(FRAMETIME)
    pause FRAMETIME
    repeat

image bg balcony lit:
  "scenes/bgs/balcony_lit.webp"
  align (0.5, 0.5)

## CGs #########################################################################

image cg balthcony      = "scenes/cgs/01a.webp"
image cg balthcony dark = "scenes/cgs/01b.webp"
image cg balthcony eyes = "scenes/cgs/01c.webp"

image cg bedthazar  = "scenes/cgs/02.webp"
image cg waltazar   = "scenes/cgs/03.webp"
image cg yaoitime   = "scenes/cgs/04.webp"
image cg returnazar = "scenes/cgs/05.webp"
