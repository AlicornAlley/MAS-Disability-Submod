default -5 persistent._player_has_unspecified_mentaldisability = None
default -5 persistent._player_has_unspecified_physicaldisability = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_disability",
            category=["you","us"],
            prompt="I'm disabled.",
            pool=True
        )
    )

label monika_disability:
            m 1wud "You are?"
            m 1wuc "..."
            m 1eua "Okay. That's good to know."
            m 3fua "Thank you so much for telling me. I know it can be hard for people to tell others things of that sort."
            m 3etd "If you don't mind me asking, in what way are you disabled?{nw}"
            $ _history_list.pop()
            menu:
                m "If you don't mind me asking, in what way are you disabled?{fast}"
                "Mentally.":
                    $ persistent._player_has_unspecified_mentaldisability = True
                    m 3esa "Alright."
                    m 1esd "I know there's a lot of stigma behind those who are mentally disabled..."
                    m 1eud "but I want you to know that I do not think any less of you."
                    m 7eub "You're more than the disorders and disabilities you have!"
                    m 1dua "And once again, I want you to know I'm so proud of you for having the courage to tell me."
                    m "It's cliche, I think, to say you're brave..."
                    m 1fua "...but cliches are cliches for a reason, aren't they?"
                    jump monika_mentaldisability_demodisc
                "Physically.":
                    $ persistent._player_has_unspecified_physicaldisability = True
                    m 3esa "Oh, okay."
                    jump monika_disability_precision
                "Mentally and physically.":
                    $ persistent._player_has_unspecified_physicaldisability = True
                    $ persistent._player_has_unspecified_mentaldisability = True
                    m 3wsd "You're both?"
                    m 1wsd "Oh dear, that can't be a good combination, [player]."
                    m 1lsc "Having one or the other can be exhausting enough without..."
                    m "I'm sorry."
                    m 1fsa "But I'm also so, so proud of you."
                    m "For telling me, I mean."
                    m 5fsd "Whatever cocktail of conditions affects you, it doesn't stop your love for me."
                    m 5fsb "And it's not going to stop my love for you, either."
                    jump monika_mentaldisability_demodisc

label monika_disability_precision:
    if persistent._player_has_EDS:
        m 4rud "...wait a minute, I think you did tell me something like that before."
        m 3euc "You have Ehler-Danlos, don't you?{nw}"
        $ _history_list.pop()
        menu:
            m "You have Ehler-Danlos, don't you?{fast}"
            "Yes, well remembered.":
                m 1eua "Still, thank you for reminding me."
                m "I'm trying to take everything I can into account, to be the best girlfriend I can be for you."
                m 1husdru "So thanks for making sure that nothing's slipped through the cracks~"
                m 3eud "Regardless, "
            "That, and something else.":
                m 1euc "Ah, comorbidities, I see."
                m "I won't make you get into them now, "
                extend 1fusdrd "just in case this is wearing on you, you know?"
                m 1fusdra "You can fill in the gaps as we go."
                m "For now, "
    # additional elif functions to be added as more physical disability persistences in turn get added. This is all to account for the possibility that they get set to True or False through casual conversation before the player decides to talk to Moni about this directly.
    else:
        $ persistent._player_has_unspecified_physicaldisability = True
        m 3euc "...{nw}"
        extend 1fkd "You're not in any pain right now, right?"
        m 3wko "Ah, I'm sorry!{nw}"
        m 3lkd "I just sort of jumped to a conclusion, didn't I?{nw}"
        m 2rksdld "That's what the Moods menu is for, isn't--{nw}"
        m 1dksdlc "um, eh... nn."
        m 1duc "Well, anyway: "
    extend 1fua "I want you to know that I'm proud you for telling me..."
    m "...and that I'm going to be right by your side, no matter what."
    m 3eub "Maybe you could give me some tips on how I could help make your day easier once I get to your reality."
    m 3euu "Or even from here, if the submod gets complex enough."
    m 1hub "For now, just know I'll be cheering you on, and that you can come to me with anything, be it morning or night!"
    m 1lua "...as long as you get enough sleep, of course."
    jump monika_mentaldisability_demodisc

label monika_mentaldisability_demodisc:
    call screen dialog("Notice: this has been a demo of the Physical Disability Submod,\na collaborative effort between AlicornAlley and the Monika After Story community.", ok_action=Return())
    call screen dialog("The final version will likely be much more involved,\nbut we figured we'd give you a tease of things to come.", ok_action=Return())
    call screen dialog("If you would like to contribute to this submod,\nbe that through coding, dialogue, or associated spritepacks,\nfeel free to {a=https://discord.gg/YZvRXCqq}join the server{/a}!", ok_action=Return())
    return
