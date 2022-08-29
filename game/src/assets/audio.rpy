init python in audio:
  ## Music
  main_menu      = "audio/music/main_menu.ogg"
  prince         = "audio/music/everett.ogg"
  balthazar      = "audio/music/balthazar.ogg"
  fireworks      = "audio/music/fireworks.ogg"
  midnight_waltz = "audio/music/midnight_waltz.ogg"
  hollow_wind    = "audio/music/hollow_wind.ogg"
  nearby_party   = "audio/music/nearby_party.ogg"
  distant_party  = "audio/music/distant_party.ogg"

  ## SFX
  woosh        = "audio/sfx/woosh.ogg"
  bad_end      = "audio/sfx/bad_end.ogg"
  blanket      = "audio/sfx/blanket.ogg"
  collapse     = "audio/sfx/collapse.ogg"
  into_bed     = "audio/sfx/into_bed.ogg"
  firework     = "audio/sfx/firework.ogg"
  clamoring    = "audio/sfx/clamoring.ogg"
  heartbeat    = "audio/sfx/heartbeat.ogg"
  door_open    = "audio/sfx/door_open.ogg"
  door_shut    = "audio/sfx/door_shut.ogg"
  clock_gong   = "audio/sfx/clock_gong.ogg"
  knock_knock  = "audio/sfx/knock_knock.ogg"
  tap_tap_tap  = "audio/sfx/tap_tap_tap.ogg"
  curtain_open = "audio/sfx/curtain_open.ogg"
  curtain_shut = "audio/sfx/curtain_shut.ogg"

  ## VA
  def everett(line):
    return "audio/voices/everett/{}.ogg".format(line)

  def balth(line):
    return "audio/voices/balth/{}.ogg".format(line)

  def maid(line):
    return "audio/voices/maid/{}.ogg".format(line)

  def guard_a(line):
    return "audio/voices/guard_a/{}.ogg".format(line)

  def guard_b(line):
    return "audio/voices/guard_b/{}.ogg".format(line)

init python:
  config.has_sound = True  ## These three variables control, among other things, which mixers are shown
  config.has_music = True  ## to the player by default. Setting one of these to False will hide the
  config.has_voice = True  ## appropriate mixer.

  config.default_sfx_volume = 0.50
  config.default_music_volume = 0.25
  config.default_voice_volume = 0.50
