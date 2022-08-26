## #############################################################################
## Music Screen ################################################################
##
## Listen to all of GGelby's bangers.
## Music Menu

screen music():
  zorder 1500
  modal True
  style_prefix "music"

  key "game_menu" action Hide()

  add Solid("#0009")
  add "gui/gallery/music_frame.webp"

  window:
    vbox:
      text _("Soundtrack by {a=https://austingelber.bandcamp.com/}GGelby{/a}")
      null height 30
      textbutton _("Main Menu"         ) action Play(channel="music", file=audio.main_menu     )
      textbutton _("Everett's Theme"   ) action Play(channel="music", file=audio.prince        )
      textbutton _("Balthazar's Theme" ) action Play(channel="music", file=audio.balthazar     )
      textbutton _("Fireworks Theme"   ) action Play(channel="music", file=audio.fireworks     )
      textbutton _("The Midnight Waltz") action Play(channel="music", file=audio.midnight_waltz)
      textbutton _("Hollow Wind"       ) action Play(channel="music", file=audio.hollow_wind   )
      textbutton _("Nearby Party"      ) action Play(channel="music", file=audio.nearby_party  )
      textbutton _("Distant Party"     ) action Play(channel="music", file=audio.distant_party )
    mousearea:
      area (0, 0, 1.0, 1.0)
      unhovered Hide()

style music_window:
  padding (60, 60)
  xsize 500

style music_vbox:
  spacing 30
  align (0.5, 0.5)

style music_button is radio_button:
  xysize (400, 42)
style music_button_text is radio_button_text
