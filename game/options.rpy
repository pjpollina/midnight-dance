## Game Info ###################################################################
init python:
  config.name           = _("The Midnight Dance")
  config.version        = "0.1.5"
  config.save_directory = "midnight_dance"
  config.window_icon    = "gui/window_icon.webp"
  gui.about = _p("""
  Prince Everett has been sickly ever since he was young. Out of fear for his life, his parents,
  the King and Queen, forced him to stay in his room. On the night of the biggest seasonal event,
  he is laying in bed wishing to dance the night away like others in his class.

  As if an answer to his prayers, a stranger appears on his balcony injured and asking to be let inside.
  But without knowing his intentions, what can Everett expect of him?
  """)

## In-Game Stuff ###############################################################
init python:
  ## Transitions
  config.enter_transition = dissolve
  config.exit_transition = dissolve
  config.intra_transition = dissolve
  config.after_load_transition = None
  config.end_game_transition = Fade(3.0, 3.0, 0.0, color="#FFF")

  ## Window stuff
  config.window = "auto"
  config.window_show_transition = Dissolve(.2)
  config.window_hide_transition = Dissolve(.2)

  ## Preference defaults
  preferences.text_cps = 35
  preferences.afm_time = 15

  ## Replace the save screen
  _game_menu_screen = "saves"

  ## The width and height of thumbnails used by the save slots.
  config.thumbnail_width  = 480
  config.thumbnail_height = 270

  ## For me
  config.keymap['console'] = "K_BACKQUOTE"

## Build Stuff #################################################################
init python:
  ## Info
  build.name = "midnight_dance"
  build.include_update = False

  ## Stuff to ignore in builds
  build.classify('**~', None)
  build.classify('**.bak', None)
  build.classify('**/.**', None)
  build.classify('**/#**', None)
  build.classify('**/thumbs.db', None)

  ## Stuff to pack into .rpa files
  build.classify('game/**.png',  'archive')
  build.classify('game/**.ttf',  'archive')
  build.classify('game/**.webp', 'archive')

  ## Platform key info
  # build.google_play_key = "..."
  # build.itch_project = "renpytom/test-project"
