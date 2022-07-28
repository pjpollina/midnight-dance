label tmd_part_c:
  prolog """
  And just like that, the sickly prince and his knight in tattered clothes shared stories.
  One of the outdoors and what it offers, and the other of his home life.

  They shared laughs, the first in a long time that made the world spin a little slower.

  Time slowed, and the prince was entranced with the stranger's way of talking.
  More candles were lit so he didn't have to stare indarkness while listening.

  He was just so graceful in everything he did. From the way his blonde hair fell over his shoulders,
  moving with every slight emphasis. His thin lips detailing stories ranging from escapades to late night kisses stolen,
  scandals and the sort that would liven anyone's day.

  How his crimson eyes shone bright in some explanations while dimming warmly in others. Prince Everett admired the man,
  not only for his looks but for his adventures.

  He lived his life to the fullest, running risks every day and always having something to look forward to.

  Oh how he wished he could do the same, so dreadfully so.
  """

label .balls_hehe:
  $ save_name = _("A dream shattered...")

  play music everett

  scene bg bedroom lit
  show everett a smile at right
  show balth a smile at left, rflip
  with Dissolve(1.25)

  pause 0.75

  $ renpy.music.set_volume(0.0, delay=0.2)

  show everett shame
  show balth shock

  play sound clock_gong
  soundfx "GONG... {w=3.5}GONG... {w=3.5}GONG... {w=3.5}{nw}"

  "The clock chimed midnight,{w=0.25} bringing me out of the conversation."

  $ renpy.music.set_volume(1.0, delay=1.0)

  balth smirk "My most recent escapade is the ball hosted down the street,{w=0.25} it was quite{dots=4.5}"
  "My attention immediately honed onto him,{w=0.25} waiting for those details I eagerly wanted."
  balth frown "{dots=6.0}the bore.{w=0.25} I wish I would never go to one as long as I live."

  show everett frown
  "What?"

  everett "No way{dots=4.0}"
  "My stomach churns at the thought of my dream being considered a bore.{w=0.25} Was everything I thought of just fantastical?"
  "The man seemed to notice my dampened mood,{w=0.25} as he immediately changed the subject to something way worse."

  balth c "What prevents you from sneaking out and exploring the town?"
  everett c frail "Me?{w=0.25} Sneak out?"

  "It wasn't a new idea."
  "I had a few escape attempts over the years,{w=0.25} mostly during my pubescent stage."
  "But every time I tried a guard captured me,{w=0.25} or I became so sickly I ran back home in fear."
  "Even now,{w=0.25} the thought of escaping once again made a familiar dread wash over me."

  everett frown "I{dots=4.0} can't.{w=0.25} This will just have to do, I guess."
  "I mustered the most realistic smile I could,{w=0.25} trying to find something else to talk about."
  everett b grimace "But it isn't all that bad,{w=0.25} I like to imagine that I'm attending the ball with everyone else.{w=0.25} Watching them have fun from afar is enough for me{dots=4.5}"
  "{dots=4.5}nothing but a lie!"

  balth smirk "Oh?{w=0.25} You enjoy the balls?"
  balth cocky "I apologize for ruining your vision of it."

  everett smile @ shame "Oh,{w=0.25} no no,{w=0.25} it's okay!{w=0.25} Maybe it wasn't anything too special anyway.{w=0.25} Dancing with someone in a beautiful ballroom,{w=0.25} someone who is special to you{dots=4.0}"
  "I lost track,{w=0.25} smiling distantly until the stranger broke the silence."
  balth a smile "I hope you get the opportunity to dance with someone you admire."
  everett grimace "Yeah{dots=4.5} I do as well."

  "The silence between us was comfortable every time we fell into it."
  "I didn't feel the need to talk anymore,{w=0.25} just enjoy the man's presence."
  "Though it would only be temporary."

  everett a frown "Why haven't you left yet?{w=0.25} It's midnight and you've shared your stories.{w=0.25} I can't keep you here."
  balth c cocky "To be honest with you{dots=4.5} you're too interesting to leave."

  show everett b shame
  "I felt the world come to a screeching halt,{w=0.25} heat blossoming around my cheeks."

  everett "What?"

  balth frown "All my life I've been surrounded by people who mask themselves and act well-bred."
  balth aloof "No one was true to themselves,{w=0.25} or to how they felt about me."
  balth smile "But,{w=0.25} you{dots=3.5} you nearly died to keep me here.{w=0.25} And that was no act."

  show everett smile
  "I chuckled,{w=0.25} rubbing my arm looking away."

  balth "You not only asked me to stay,{w=0.25} but you look sad around me."
  balth "I have never seen someone look so downtrodden in my presence.{w=0.25} They usually say I make it all better."
  balth "You show your true self to me{dots=4.5} and I think that's worth staying longer for."

  show everett c shame
  "I was stunned into silence."
  everett "Re-really{em}?"

  "I was interrupted by the man standing on his feet, {nw}{done}offering a hand towards me."
  stop music fadeout 2.0
  show balth cocky:
    ease 0.5 center
  "I was interrupted by the man standing on his feet, {fast}{w=0.25}offering a hand towards me."
  scene black with Dissolve(0.33)

label .midnight_waltz:
  $ save_name = _("The midnight waltz...")

  play music "<silence 3.0>"
  queue music midnight_waltz fadein 2.0

  scene cg waltazar
  with Fade(2.0, 1.0, 3.0)

  balth "{cps=*0.66}{i}May I have this dance?{/i}{/cps}"
  everett "Wha{dots=3.0}what?"
  "What?!{w=0.25} {i}{b}WHAT?!{/b}{/i}"

  balth "You wanted a dance with someone,{w=0.25} right?"
  balth "And from the way your eyes never left my chest during the procedure,{w=0.25} you admire me just enough to make this fine for you."
  everett "You saw that?!"

  "The man stifled a chuckle that escaped.{w=0.25} For the first time in the night,{w=0.25} I saw a genuine smile."
  "It warmed me just a little{dots=4.5} But not long enough to delude me."

  everett "But I'm{dots=4.5} I'm weak."
  balth "Then I'll go slow,{w=0.25} don't worry."
  balth "I have you."

  "My chest tightened,{w=0.25} but with this situation far too good to pass up,{w=0.25} I hesitantly took his hand."

  everett "I don't really know how to dance."
  balth "But I do,{w=0.25} I'll lead the way.{w=0.25} Just follow my steps."

  "He suddenly grabbed my hand firmly as we began the slow waltz."
  "At first we just swayed,{w=0.25} his hand snaking around my waist pulling me close."
  "Then as I figured the rhythm out,{w=0.25} he began spinning me around carefully."
  "We spun in circles,{w=0.25} shuffling our feet to his soft hum."
  "My feet were clumsy and my legs felt like they would buckle from embarrassment."
  "But all he did was pull me towards his chest;{w=0.25} our bodies close the space."
  "Before long,{w=0.25} we were dancing as if we've been dancing all our lives."
  "I couldn't hide the big smile on my face,{w=0.25} growing too excited that I nearly stumbled into his chest."

  everett "You're a good teacher."
  balth "You're not half bad to teach,{w=0.25} I thought you would be way worse."

  "He chuckled beneath his breath as we danced."
  "His humming never quickened,{w=0.25} knowing that I'd make a major fool of myself if he did."
  "This was better than I could ever imagine."
  "I knew that I've always wanted to dance with someone I admire."
  "But who knew it would be as good as this?"
  "It was just as I imagined.{w=0.25} Our feet gracefully sliding across the carpeted floors."
  "The light from the candles had never felt more warm and fuzzy."
  "When we were dancing,{w=0.25} it felt like hours passed.{w=0.25} With only the feeling of his hand in mine resonating."

  # TODO: FIREWORK SFX
  soundfx "kaboom!{nw}"

  "Not wanting to break the dance,{w=0.25} I slowly took the lead and pulled him towards the balcony."
  everett "The fireworks! Let's go watch them."
  balth "If you say so."

  stop music fadeout 3.0
  scene black with Dissolve(3.0)
  stop music

  "I urged him towards the balcony,{w=0.25} leaning against the railing."
  "Moments later,{w=0.25} I regretted coming out without a blanket.{w=0.25} But the stranger tossed one over my shoulders and leaned against the railing next to me."

label .fireworks:
  $ save_name = _("Fires in the sky...")

  play music fireworks
  scene bg balcony lit
  show everett b smile at left, rflip
  show balth a smile at right
  with Dissolve(3.0)

  "The fireworks lit the dark sky with warm colors.{w=0.25} Sprinkling down to the ground after a grand display of vivid colors."
  "Tonight,{w=0.25} the fireworks felt brighter than ever."
  "As I watched the fireworks go by,{w=0.25} I felt the stranger's gaze on me and turned red."
  "What was he looking at?{w=0.25} What was more pretty than the fireworks in front of him?"

  balth c aloof "Balthazar."
  $ is_stranger = False
  show everett a shame

  "I turned to look at him in shock,{w=0.25} wondering if that was what I thought it was."
  everett "That's{dots=4.5}"
  balth smirk @ frown "My name."
  everett smile "Everett,{w=0.25} it's nice to meet you."

  $ renpy.music.set_volume(0.25, delay=3.0)

  show everett:
    ease 1.0 xalign 0.26
  show balth:
    ease 1.0 xalign 0.74
  "I held my hand out for him.{w=0.25} His hand once again enveloped mine,{w=0.25} larger and surprisingly cold for how warm his personality was."
  show everett c frail:
    ease 1.0 xalign 0.27
  show balth a aloof:
    ease 1.0 xalign 0.73
  "Nothing could've made this night better."
  show everett c smirk:
    ease 1.0 xalign 0.28
  show balth c smirk:
    ease 1.0 xalign 0.72
  "Not even{em}"

label .interrupted:
  $ save_name = _("Imperfect timing...")

  stop music
  show everett c shame:
    parallel:
      linear 0.1 yzoom 1.25
      linear 0.1 yzoom 1.00
    parallel:
      lflipturn
    parallel:
      ease 0.2 xalign 0.15
  show balth a shock:
    linear 0.1 yzoom 1.2
    linear 0.1 yzoom 1.0

  play sound knock_knock
  soundfx "knock{w=0.25} knock{w=0.25} knock!{w=0.25}{nw}"

  "I whipped towards the door at the sound of the door banging.{w=0.25} The maid's voice came from the other side again."

  show balth a aloof:
    parallel:
      easein 30.0 xalign 0.4
    parallel:
      easein 0.75 yoffset 10
      easein 0.75 yoffset  0
      repeat 20

  maid "Your Royal Highness?{w=0.25} Why is your room lit?{w=0.25} Is everything alright still?"

  guarda "It must be that scoundrel in his room,{w=0.25} why else would he be awake at this time?"
  guardb "We need to break the door down!"

  maid "You will do no such thing!"

  show everett c shame
  maid "Everett,{w=0.25} are you okay in there?{w=0.25} Why are you awake?"

  everett c shame "Shit{dots=4.5}"
  "I covered my mouth in shock,{w=0.25} watching Balthazar's smile drop into that restrained expression he had coming in."

  balth frown "Everett{dots=4.5}"

  show everett frown at rflipturn
  everett frown "I have to hide you again! We can try my closet this time,{w=0.25} or maybe beneath my bed-"

  balth aloof "{dots=3.0}Everett{dots=3.0}"
  everett frail "No we can do this! I can hide you somewhere until they leave,{w=0.25} and then we can{em}"

  "I hadn't noticed him closing the distance between us,{w=0.25} his hands grazing the sides of my face."

  "Before I had time to retaliate,{done} he lowered one arm around my waist and pulled me closer to him."
  show everett b shame:
    rotate_pad False
    parallel:
      ease 0.4 offset (-6, 12)
    parallel:
      easein 0.6 rotate -25
  show balth a aloof behind everett:
    rotate_pad False
    parallel:
      ease 0.4 offset (-26, 2)
    parallel:
      easein 0.6 rotate -5
  "Before I had time to retaliate,{fast} he lowered one arm around my waist and pulled me closer to him."

  "His lips didn't meet mine,{w=0.25} but his warm breath against my skin brought tingles across me."

  show everett frail:
    ease 0.4 rotate -27.5 yoffset 28
  show balth smirk:
    ease 0.4 rotate -7.5

  balth "I will return,{w=0.25} {nw}"

  show everett shame:
    ease 1.5 rotate -30.0 yoffset 36
  show balth cocky:
    ease 1.5 rotate -10.0

  extend "and you will wait for me right?"

  everett frown "But{em}"

  camera:
    parallel:
      align (0.25, 0.25) matrixcolor TintMatrix("#FFF")
      ease 2.0 matrixcolor TintMatrix("#000") zoom 2.5
    parallel:
      pause 1.5
      "black" with Dissolve(1.5)
  show everett shame:
    ease 6.0 rotate -20.0
  show balth cocky:
    ease 6.0 rotate -20.0
  with Dissolve(0.5)

  $ renpy.pause(3.5, hard=True)

  "Our lips met and we kissed."
  return
