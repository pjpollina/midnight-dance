init python in audio:
  ## Music
  balthazar      = "audio/music/balthazar.ogg"
  midnight_waltz = "audio/music/midnight_waltz.ogg"

  ## SFX
  tap_tap_tap  = "audio/sfx/tap_tap_tap.ogg"
  curtain_open = "audio/sfx/curtain_open.ogg"
  curtain_shut = "audio/sfx/curtain_shut.ogg"

init python:
  config.has_sound = True  ## These three variables control, among other things, which mixers are shown
  config.has_music = True  ## to the player by default. Setting one of these to False will hide the
  config.has_voice = True  ## appropriate mixer.
