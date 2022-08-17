label tmd_part_d:
  label .yaoikiss:
    $ save_name = _("When lips meet...")

    play music balthazar fadein 8.0
    scene cg yaoitime with Fade(2.0, 2.0, 2.0, color="#FFF")

    "My hands rested on Balthazar's chest,{w=0.25} slowly grabbing his shirt as if it would prevent him from leaving."
    "After what felt like an eternity,{w=0.25} he pulled away and whispered softly in my ear."

    voice audio.balth("d01")
    balth "Wait for me,{w=0.25} Your Royal Highness."

    voice audio.everett("d01")
    everett "Balthazar{dots=4.5}"

    camera:
      align (0.5, 0.25)
      ease 1.0 zoom 30.0 blur 1000
    scene cg balthcony with Dissolve(1.0)
    camera:
      align (0.5, 0.3)
      ease 1.0 zoom 2.0 blur 0
    pause 1.0

    voice audio.balth("d02")
    turmoil "{b}{i}{cps=*0.5}Wait for me.{/cps}{/i}{/b}"

    scene black with ImageDissolve("cg yaoitime", 1.5)
    camera:
      zoom 1.0 align (0.5, 0.5)

    "He backed away from me as I closed my eyes.{w=0.25} I couldn't hear the sounds of his footsteps nor the door opening without my command."
    "When my eyes opened again,{w=0.25} he was gone."
    "I raised a hand to touch my cheek."
    "The maid had a hand on my back,{w=0.25} coaxing me back in the bedroom as the guards searched the balcony."

    voice audio.maid("d01") # NOTE: NO VA
    maid "Look at him,{w=0.25} he's in a state of shock! What came to you,{w=0.25} Your Royal Highness?"

    voice audio.everett("d02")
    everett "{dots=4.5}"
    voice audio.everett("d03")
    everett "I saw an adorable squirrel outside,{w=0.25} but when I went to approach it{dots=4.5} it ran away."
    voice audio.everett("d04")
    everett "I think the critter had returned."

    "The lies rolled so easily out off my tongue that I feared Balthazar had rubbed off on me."
    "The maid relaxed after hearing it was a squirrel,{w=0.25} but from her angry expression it looked as if I wouldn't hear the end of it by tomorrow."
    "Though surprisingly,{w=0.25} she sighed."

    voice audio.maid("d02") # NOTE: NO VA
    maid "Get some rest,{w=0.25} Your Highness.{w=0.25} You look terribly out of it."

    "Was it because of him?"
    "My face grew redder thinking of how he stole a kiss from me so easily.{w=0.25} My first kiss{dots=4.5}"
    "I didn't think I would be able to fall back asleep anytime soon."

    scene cg balthcony:
      matrixcolor SepiaMatrix()
    with Fade(3.0, 3.0, 3.0)
    stop music fadeout 7.0
    pause 3.0
    scene black with Dissolve(6.0)

  label .waiting:
    $ save_name = _("Waiting for him...")

    scene black
    stop music

    prolog """
    After that whimsical night, Prince Everett waited every night by his balcony for Balthazar to show up again.

    He finally had something to look forward to, and it was seeing the man's face again after he so lovingly
    made his night memorable.

    But every night he waited, another night came when the man wouldn't show up.
    It was starting to make him doubt the man's words.

    Days turned into weeks until the disheartened Prince decided that it was all a ruse.
    He shouldn't have eagerly trusted a stranger, let alone a man with red eyes that recovered quickly.

    But even as he told himself he wouldn't wait for Balthazar, every night he found himself on the balcony.

    Waiting...
    """

    scene bg balcony
    show everett b frown at rflip, right
    with ImageDissolve("cg yaoitime", 2.0)

    "The night was just as cold as that night.{w=0.25} It felt harsher today,{w=0.25} as if the world was mocking me for my decision."
    "I didn't want to think about him anymore."
    "He was so wrapped up in my thoughts that I saw him in everything.{w=0.25} From the gentle candlelight wick to the shadows dancing across the wall."
    "My feet still traced the steps in our slow waltz,{w=0.25} memorizing every movement."
    "Except he was gone,{w=0.25} and even though he promised he would return,{w=0.25} he didn't."

    voice audio.everett("d05")
    everett "It was silly to expect that."
    voice audio.everett("d06")
    everett "I'm pretty foolish,{w=0.25} aren't I?"
    voice audio.everett("d07")
    everett "I don't even know why I bother to stand out here."

    "The balcony was now a place of insurmountable sadness rather than joy."
    "The people preparing for the ball didn't interest me anymore."
    show cg balthcony:
      matrixcolor SepiaMatrix()
      alpha 0.5
    with Fade(0.2, 0.0, 0.2, color="#FFF")
    pause 0.5
    show cg bedthazar:
      matrixcolor SepiaMatrix()
      alpha 0.5
    with Fade(0.2, 0.0, 0.2, color="#FFF")
    pause 0.5
    show cg waltazar:
      matrixcolor SepiaMatrix()
      alpha 0.5
    with Fade(0.2, 0.0, 0.2, color="#FFF")
    pause 1.0
    show cg yaoitime:
      matrixcolor SepiaMatrix()
      alpha 0.5
    with Fade(0.2, 0.0, 0.2, color="#FFF")
    pause 2.0
    hide cg with Dissolve(2.0)

    "All I saw was me and him in each couples face as they tried to make every night the best."
    "Just the way he was that night."
    show everett c cough
    camera:
      align (0.75, 0.15)
      zoom 2.0
    with Dissolve(1.0)
    "My chest ached,{w=0.25} and I grabbed my shirt.{w=0.25} Balling it into my fist."
    "Before long I would have to return inside.{w=0.25} Another day gone by."
    show everett frail
    "Another day{dots=3.0}"

    show balth a cocky behind everett at center, rflip:
      matrixcolor TintMatrix("#000") alpha 0.0
      easein 5.0 alpha 1.0
    $ renpy.pause(5.0, hard=True)

    voice audio.balth("d03")
    balth "So you've waited for me,{w=0.25} Your Royal Highness."

    show everett a shame at rflip:
      linear 0.05 yoffset -60
      linear 0.05 yoffset   0
    "My heart leapt to my throat."
    "A chill ran through my spine as I slowly turned."
    "Behind me was him."

  label .the_return:
    $ save_name = _("Reunited...")

    play music fireworks fadein 2.0
    scene cg returnazar
    camera:
      zoom 1.0
    with Fade(0.2, 0.0, 0.2, color="#FFF")

    "Balthazar."

    "He stood in a new set of gentleman's clothing,{w=0.25} carrying a bouquet of flowers."

    voice audio.balth("d04")
    balth "You've done well."

    "Tears welled in my eyes,{w=0.25} and I didn't try to wipe them away."
    "He was finally here{dots=4.5}"

    voice audio.everett("d08")
    everett "What kept you{dots=4.5} so long?"

    "It was hard to talk through the sniffling as I restrained myself from leaping towards him."

    voice audio.balth("d05")
    balth "The guards have increased since I last left you.{w=0.25} It was difficult even for me to find my way back here."
    voice audio.balth("d06")
    balth "But knowing you were waiting for me{dots=4.5} I couldn't stop until I found a way back to you."

    "I rubbed my blurry vision,{w=0.25} a sob trapped in my chest.{w=0.25} I should've asked him why the guards were so persistent to catch him.{w=0.25} But the overwhelming relief of him being here was distracting."
    "I felt the warm embrace of his jacket around my shoulders,{w=0.25} the smell of his cologne tickling my nose."
    "Pulling it closer around me,{w=0.25} he leaned against the railing just like before."

    voice audio.everett("d09")
    everett "Those guards must hate you if they'd still be looking after weeks."
    "The words immediately put a dampen on the mood,{w=0.25} as he lowered his chin and looked away from me in sadness."
    voice audio.everett("d10")
    everett "Balthazar{dots=4.5}?"

    "I reached towards him and he didn't move away."

    voice audio.everett("d11")
    everett "Why are you running away from the guards?{w=0.25} Did you{dots=4.5}"
    voice audio.everett("d12")
    everett "Harm someone?"

    "His eyes flashed with an unrecognizable emotion,{w=0.25} but he didn't deny the accusation."

    voice audio.balth("d07")
    balth "It's been a long life before I met you,{w=0.25} Everett.{w=0.25} One that I shouldn't tell you fully."

    voice audio.everett("d13")
    everett "Why not?"

    voice audio.balth("d08")
    balth "It will entangle you in it,{w=0.25} and I wouldn't wish to harm you."

    "My hand drops from his shoulder to his hand,{w=0.25} squeezing it."

    voice audio.everett("d14")
    everett "Balthazar{dots=4.5}"
    voice audio.everett("d15")
    everett "My life has been entangled in yours the moment you appeared on my balcony."
    voice audio.everett("d16")
    everett "I don't know anything about you,{w=0.25} but I can judge you from the way you acted with me."
    voice audio.everett("d17")
    everett "And you don't seem to be some scoundrel like the guards say."

    voice audio.balth("d09")
    balth "They talk of me like a scoundrel?"

    voice audio.everett("d18")
    everett "{dots=4.5}among other names that aren't nice."

    "Wanting to make him laugh,{w=0.25} I instead succeeded in a deep frown plaguing his features."

    voice audio.everett("d19")
    everett "Listen.{w=0.25} I want to help you however I can.{w=0.25} You rescued me from my prison,{w=0.25} at least let me help you get out of yours."
    voice audio.everett("d20")
    everett "I'm weak,{w=0.25} but I'm not so weak as to steal a night with you and not help you in return."

    voice audio.balth("d10")
    balth "Everett{dots=4.5}"

    "His eyes were wide in shock,{w=0.25} as if he had never heard those words."

    voice audio.balth("d11")
    "Then he chuckled,{w=0.25} bursting out into laughter that seemed unfitting for the situation."

    voice audio.everett("d21")
    everett "What's so funny?"

    voice audio.balth("d12")
    balth "You surprise me,{w=0.25} human."

    "Human?"

    voice audio.balth("d13")
    balth "If I must trudge down that weary road again,{w=0.25} at least I'd like to do it with a companion."

    voice audio.everett("d22")
    everett "So you'll tell me?"

    "Balthazar nodded,{w=0.25} smiling fondly."

    voice audio.balth("d14")
    balth "I'll tell you everything,{w=0.25} starting from the very beginning{dots=4.5}"

    stop music fadeout 0.25
    scene black with Dissolve(0.25)

    voice audio.balth("d15")
    balth "Of when I became a vampire."

  return
