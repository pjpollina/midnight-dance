transform left:
  xalign 0.25
transform right:
  xalign 0.75
transform center:
  xalign 0.5

transform lefter:
  xalign 0.15
transform righter:
  xalign 0.85

transform leftest:
  xalign 0.0
transform rightest:
  xalign 1.0

transform walkon_right:
  xalign 1.5
  parallel:
    linear 1.5 right
  parallel:
    easein 0.2 yoffset 20
    easein 0.3 yoffset  0
    repeat 3

transform runon_lefter:
  xalign -1.0
  parallel:
    linear 1.0 lefter
  parallel:
    easein 0.2 yoffset 50
    easein 0.3 yoffset  0
    repeat 2

## FLIPPING SITUATIONS
transform rflip:
  xzoom -1.0
transform lflip:
  xzoom 1.0

transform rflipturn:
  xzoom 1.0
  ease 0.2 xzoom -1.0
transform lflipturn:
  xzoom -1.0
  ease 0.2 xzoom 1.0
