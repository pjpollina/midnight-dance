## Sprites Gallery #############################################################
##
## Check out all of AceyDude's sprites.

screen sprites():
  tag menu
  style_prefix "sprite"

  text _("Character sprites by {a=https://twitter.com/SocialDemonz}Social Demonz{/a}") align (0.5, 0.025)
  hbox spacing 30 align (0.5, 0.5):
    button:
      action Show("dressup", dissolve, char="everett")
      style style.sprite_button["everett"]

    button:
      action Show("dressup", dissolve, char="balth")
      style style.sprite_button["balth"]

    button:
      action Show("dressup", dissolve, char="maid")
      style style.sprite_button["maid"]

    button:
      action Show("dressup", dissolve, char="guard")
      style style.sprite_button["guard"]

style sprite_button:
  xysize (334, 610)
  foreground "gui/gallery/portraits/[prefix_]frame.webp"

init python:
  for guy in ["everett", "balth", "maid", "guard"]:
    style.sprite_button[guy].idle_background = Transform("gui/gallery/portraits/{}.webp".format(guy), matrixcolor=SepiaMatrix())
    style.sprite_button[guy].hover_background = "gui/gallery/portraits/{}.webp".format(guy)

## Dressup Screen ##############################################################

init python:
  faces = {
    "everett": {
      _("Smile"  ): SetScreenVariable("face", "smile"  ),
      _("Frown"  ): SetScreenVariable("face", "frown"  ),
      _("Shame"  ): SetScreenVariable("face", "shame"  ),
      _("Smirk"  ): SetScreenVariable("face", "smirk"  ),
      _("Cough"  ): SetScreenVariable("face", "cough"  ),
      _("Frail"  ): SetScreenVariable("face", "frail"  ),
      _("Grimace"): SetScreenVariable("face", "grimace"),
    },
    "balth": {
      _("Smile"): SetScreenVariable("face", "smile"),
      _("Frown"): SetScreenVariable("face", "frown"),
      _("Shock"): SetScreenVariable("face", "shock"),
      _("Smirk"): SetScreenVariable("face", "smirk"),
      _("Aloof"): SetScreenVariable("face", "aloof"),
      _("Cocky"): SetScreenVariable("face", "cocky"),
    },
    "maid": {
      _("Smile"): SetScreenVariable("face", "smile"),
      _("Worry"): SetScreenVariable("face", "worry"),
    },
    "guard": {
      _("Angry"): SetScreenVariable("face", "smile"),
      _("Stoic"): SetScreenVariable("face", "stoic"),
      _("Worry"): SetScreenVariable("face", "worry"),
      _("Aloof"): SetScreenVariable("face", "aloof"),
      _("Happy"): SetScreenVariable("face", "happy"),
      _("Upset"): SetScreenVariable("face", "upset"),
    },
  }

screen dressup(char):
  modal True
  key "game_menu" action Hide(transition=dissolve)
  style_prefix "dressup"

  add "bg {}".format(dict(everett = "bedroom", maid = "bedroom lit", balth = "balcony", guard = "balcony lit")[char])
  add Solid("#0008")

  default pose = "a"
  default face = "smile"
  default page = 0

  hbox:
    window padding (20, 20):
      vbox spacing 20:
        if char != "maid":
          if char == "guard":
            label _("Guard")
            textbutton _("Guard A") style "radio_button" action SetScreenVariable("pose", "a")
            textbutton _("Guard B") style "radio_button" action SetScreenVariable("pose", "b")
          else:
            label _("Pose")
            textbutton _("Pose A") style "radio_button" action SetScreenVariable("pose", "a")
            textbutton _("Pose B") style "radio_button" action SetScreenVariable("pose", "b")
            textbutton _("Pose C") style "radio_button" action SetScreenVariable("pose", "c")
          null

        label _("Expression")
        for k, v in faces[char].items():
          textbutton k style "radio_button" action v

    window:
      if char == "guard":
        add "guard_{}".format(pose)
      elif char == "maid":
        add "maid {}".format(face)
      else:
        add "{} {} {}".format(char, pose, face)

    null width 75

    if char == "guard":
      $ char = "guard_{}".format(pose)
    use profile(char)

style dressup_label:
  padding (10, 10, 10, 10)
style dressup_label_text:
  size 72

style dressup_button is button:
  padding (40, 10)
  background Solid("#000")
style dressup_button_text is button_text:
  size 48
  align (0.5, 0.5)

## Profile Screen ##############################################################

init python:
  profiles = {
    "everett": _p("""
      Prince Everett was born to inherit the throne of the royal family. He is the first son, the only child to the
      Queen and King currently residing over the city. His parents soon realized that Everett wouldn't fulfill his
      destiny when he was often sickly, weak and often bedridden with flairs of asthma attacks and fevers. With a low
      immune system and a tendency to cough, they locked him away in his room with no visitors fearing for his life.

      Only the same scullery maid could come in to deliver his food and tell him to go to bed. Everett has grown
      attached to the maid moreso than his mother because she's the face he saw. His parents hid away from him out
      of grief that he ended up this way.

      Years passed with this situation growing more dire. At first he sought for any entertainment the maid could
      sneak behind the Queens orders: toys you simply had to move, books, and even hiring a secret medicinal tutor
      to teach him how to take care of his injuries or fevers if he succumbed to them. But Everett deep down was
      unhappy, because at the end of the day the maid left and activity resumed without him.

      Because of his poor health, he could only sneak onto the balcony and watch the people of his city head to
      balls. He soon grew attached to the idea of attending one, dancing among the commoners and nobles alike for
      one night. But everytime he tried to dance he'd stumble on his feet and end up with a bruise which the maid
      would chastise him for.

      Many years passed to the current date, with the same monotony of his life continuing.
    """),

    "balth": _p("""
      Balthazar was born hundreds of years ago when the world was a more different place. Alongside his
      mother, father, and little sister he lived in New Orleans on a plantation. He was the breadwinner
      of the family back in his mortal years, capturing and skinning animals to serve to his family and
      those around him. He was joyous and polite for many years with a full future ahead of him.

      Then when he turned 19, he came home to his plantation lit on fire and his family deceased. He
      tried to search for them in the debris but he only found a cynical vampire waiting for him. The
      man stated that Balthazar was the perfect heir to his fortune, and without warning Balthazar was
      transformed into a vampire.

      After losing his humanity and the death of the man who turned him into a vampire, he was left to
      wander alone trying to control his urges. He became self-destructive, cynical and even desperate
      to break out of this curse. But unfortunately, he'd learn to accept it when decades passed and he
      showed no signs of aging. After decades of staying at his burnt family home feeding of stray
      animals, he left searching for the mans fortune.

      Balthazar was on the road for hundreds of years afterward. Traveling across North America before
      cursing the country and leaving for Britain. There, he used his fortune to buy a manor and make a
      living as one of the noble classes. This of course came with situations he'd rather avoid such as
      looking like a potential suitor to every drooling duchess and their mother. He attended balls,
      walked the streets, all the while concealing his vampiric state by eating animals.

      He still had enough of his humanity with him, and after decades of philosophical thinking he was
      able to control his urges somewhat. No human would ever come to harm under him except for vile ones
      he found in the street. It was only after killing his first criminal fiend that he was on the
      cops watchlist. Evading the watchdogs by night and walking among them by day.
      """),

    "maid": _p("""
      The maid is like any other. She acts worried for everetts health and asks that he obey his and
      his mother's rules. Though she's a little harried when it comes to situations, she cares for Everett.
    """),

    "guard_a": _p("""
      Born in a small village outside the city, he's worked hard from a young age to become the pillar
      of strength he is today. It's paid off in the end, as he rose through the ranks to become an elite
      royal guard faster than anyone on record. Fiercely loyal to his duty, he would not hesitate to lay
      down his life to protect the royal family or their subjects.

      Despite his tough exterior, he's actually quite gentle and caring, and very good with children, in
      no small part due to him growing up the eldest of twelve siblings. His fraternal attitude towards
      both his fellow guards and the other people of the castle have made him quite popular.

      In his off time, he builds model ships in bottles with his boyfriend, Guard B.
    """),

    "guard_b": _p("""
      The second son of a noble family, he was blessed from a young age with a cushy life and
      little-to-no responsibilities. Rather than just accept this easy existence, however, Guard B used
      his status to help the common people, often volunteering anywhere people needed help. This attitude
      is what helped him earn his position as an elite royal guard, a duty he takes incredibly seriously.

      While not as outwardly fierce as his partner and boyfriend, Guard A, he's still a capable warrior in
      his own right, often training with the former for hours. This has made the two an unimaginably strong
      pair both physically and tactically, known by the other guards as being capable of stopping "any
      man alive". Lucky for them, their only loss was to Balthazar, so this title still stands.

      He and Guard A often stop by at the local orphanage after work to read stories to the children.
    """),
  }

screen profile(char):
  style_prefix "profile"

  window:
    has vbox

    text _("Profile") size 72
    frame background Solid("#000A") ysize 3
    null height 15

    frame padding (10, 10, 0, 10):
      viewport id "profile":
        mousewheel True
        text profiles[char]
      vbar value YScrollValue("profile")

style profile_window:
  margin  (20, 20)
  padding (20, 20)
  background Solid("#FFF7")
  xfill True
  yfill True

style profile_vscrollbar:
  xpos 1.0
  thumb Solid("#000A", xalign=1.0, xsize=4)
  base_bar Solid("#0004", xalign=1.0, xsize=4)
