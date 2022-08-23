## #############################################################################
## Music Screen ################################################################
##
## Listen to all of GGelby's bangers.

screen music():
  tag menu
  style_prefix "music"

  vbox spacing 30:
    textbutton _("Main Menu"         ) action Play(channel="music", file=audio.main_menu     )
    textbutton _("Everett's Theme"   ) action Play(channel="music", file=audio.prince        )
    textbutton _("Balthazar's Theme" ) action Play(channel="music", file=audio.balthazar     )
    textbutton _("Fireworks Theme"   ) action Play(channel="music", file=audio.fireworks     )
    textbutton _("The Midnight Waltz") action Play(channel="music", file=audio.midnight_waltz)
    textbutton _("Hollow Wind"       ) action Play(channel="music", file=audio.hollow_wind   )
    textbutton _("Nearby Party"      ) action Play(channel="music", file=audio.nearby_party  )
    textbutton _("Distant Party"     ) action Play(channel="music", file=audio.distant_party )

style music_button is radio_button:
  xysize (600, 42)
style music_button_text is radio_button_text
