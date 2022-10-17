default persistent._player_has_ARFID = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_arfid",
            category=["health","psychology"],
            prompt="ARFID",
            random=True
        )
    )

label monika_arfid:
    $ ev = mas_getEV("monika_arfid")

    if ev.shown_count == 0:
        m 3eub "Hey, [player], have you heard of-{w=0.5}{nw}"
        m 3luc ".{w=0.5}.{w=0.5}.{nw}"
        extend 1husdrb "I know, I know, I open a lot of conversations like that."
        m "But I really do think I've found an obscure one this time."
        m 1eud "So..."
        m 3eub "Have you heard of ARFID?{nw}"
        $ _history_list.pop()
        menu:
            m "Have you heard of ARFID?{fast}"
            "No, I haven't.":
                m 1fsa "Yeah, that's what I figured, ehehe."
                m "Since you're uninitiated, then,"
                jump monika_arfid_explanation
            "Yeah.":
                m 1wud "Huh?"
                m 1wsc "Well, I won't lie, that's a bit of a surprise."
                m 3etd "Unless - {w=1} is it because you have it yourself?{nw}"
                $ _history_list.pop()
                menu:
                    m "Unless - is it because you have it yourself?{fast}"
                    "Yep. Official diagnosis.":
                        $ persistent._player_has_ARFID = True
                        m 1eua "Ah, {i}that{/i} explains it."
                        m 1dua "...{nw}"
                        extend 1fuc "I'll try not to tell you all the things you've probably heard a thousand times already."
                        m "That's got to be frustrating."
                        m 3fud "Do let me know if I mess up somewhere, if you can?"
                        m 3rud "This is relatively new to me, "
                        extend 3eub "but I do want to give you as much space to be, well, yourself as possible."
                        m "I know you'd do the same for me, after all."
                        m 5eua "You are you, however many foibles and caveats that person may contain."
                        m 5eubla "And it's that you I love. Nobody else."
                        return "love"
                    "Not officially diagnosed, but I'm pretty sure I do.":
                        $ persistent._player_has_ARFID = True
                        m 1eua "Ah, {i}that{/i} explains it."
                        m "Thank you for being open about it to me; I know that can't have been easy."
                        m 3eud "And for what it's worth, you don't have to get an official diagnosis for your experience to be valid."
                        m 3tup "...if only because it's not easy {i}to{/i} get an ARFID diagnosis."
                        m 1hua "I will love you and believe you just the same."
                        m 1fua "I promise."
                        return "love"
                    "No, but I know someone who might.":
                        $ persistent._player_has_ARFID = False
                        m 6eua "Oh, okay. That makes sense."
                        m "Presumably you've picked up on their eating habits then..."
                        extend 6esu " or, um, their lack thereof."
                        m 7euc "I hope you don't make fun of them for it, [player]."
                        if mas_isMoniHappy(higher=True):
                            m 1wuo "Not that I think you'd do it intentionally! You're not that cruel."
                            m 1eud "It's just..."

                            $ _if = "- again, not that you would -"
                        else:
                            $ _if = "if you're not already,"
                        m 1eud "ARFID carries a lot of stigma as it is, what with being mistaken for just fussiness or childishness."
                        m "And the fewer people who add to that stigma, the better."
                        m 1ruc "So [_if] please try not to make them self-conscious about it."
                        m 1eua "It doesn't really matter what people eat! As long as they're not eating too much, nor too little, of it."
                        m 7hua "Balance makes the world go round, as they say~"
                        return
                    "I don't, I've just looked into it before.":
                        $ persistent._player_has_ARFID = False
                        m 6eua "Got it."
                        m 7nub "In that case, I won't belabor the point, my little researcher~"
                        return
                    "Heard it somewhere, is all; I'm still not sure what it means.":
                        m 1esd "Ah, okay."
                        m "I'll try and cover the basics for you, then."
                        m 4euc "In short, "
                        jump monika_arfid_explanation
    else:
        if persistent._player_has_ARFID is None:
            m 1eud "Hey, [player]?"
            m "Remember when I brought up ARFID before?"
            m 1luc "I've been wondering - {w=-0.2}{nw}"
            extend 1lusdrd "and do tell me if I'm overstepping - {w=-0.2}"
            m 1fuc "did any of that... resonate with you?"
            if mas_isMoniUpset(lower=True):
                m 1tsc "And I don't just mean 'were you actually listening to me', I mean more..."
            else:
                m 1essdlb "...no, sorry, I don't mean 'were you paying attention', I know you were!"
                m 1esc "It's more..."
            m 1ekd "Did it match any of your experiences with food?"
            m "Did it ring any bells, I mean?{nw}"
            $ _history_list.pop()
            menu:
                m "Did it ring any bells, I mean?{fast}"
                "I've been officially diagnosed with it since then.":
                    $ persistent._player_has_ARFID = True
                    m 1wud "Oh!"
                    m 1ruc "I...{w=0.5} um."
                    m 3euc "Saying 'well done' doesn't feel quite right for this situation, "
                    extend 3eua "but I {i}am{/i} proud of you for taking this step, [mas_get_player_nickname()]."
                    m 1eub "And I'm glad you have a name to put to your experiences now."
                    m 3fua "Knowing that you're not a freak, that there's a name for what's happening..."
                    m "...it's kind of freeing, isn't it?"
                    m 3kub "Not that I'm speaking from experience here, heh."
                    m 6duc "...{nw}"
                    extend 6eua "I hope you know I don't think any less of you for this, [player]."
                    m "That was never an option for me."
                    m 5eua "You are you, however many foibles and caveats that person may contain."
                    m 5eubla "And it's that you I love. Nobody else."
                    return "love"
                "I think... I think it did.":
                    $ persistent._player_has_ARFID = True
                    m 1ekd "Oh, [player], it's okay."
                    m 1eka "I wouldn't have asked if I didn't think there was the possibility."
                    m "Thank you for telling me."
                    m 3eud "And for what it's worth, you don't have to get an official diagnosis for your experience to be valid."
                    m 3tup "...if only because it's not easy {i}to{/i} get an ARFID diagnosis."
                    m 1hua "I will love you and believe you just the same."
                    m 1fua "I promise."
                    return "love"
                "No, I don't think I have it. But thank you for telling me about it!":
                    $ persistent._player_has_ARFID = False
                    m 1hub "No problem, [mas_get_player_nickname()]!"
                    m "Always happy to teach you something new."
                    m 1eud "And if there's anything you {i}do{/i} end up getting diagnosed with, not just ARFID, "
                    extend 3fua "know that you can talk to me about it at any time."
                    m "I love {i}you{/i}, as you are. Not the idealized, perfect version of you that the player character was meant to be."
                    m 1eubla "And I want to be as accommodating to you as possible if we ever get to see each other in the flesh."
                    return "love"
                "I've forgotten what ARFID entails. Could you remind me?":
                    m 1esa "Of course, [mas_get_player_nickname()]."
                    m 3esd "Starting with the basics, then: "
                    jump monika_arfid_explanation
        elif persistent._player_has_ARFID is False:
            m 2euc "I've been thinking a little bit more about potential career paths for when I cross over."
            if renpy.seen_label("monika_career"):
                m 3eud "You already know 'writer', 'musician', and 'programmer'..."
                m 3eub "But honestly, I might be cut out for 'psychiatrist', too."
            else:
                m 3eud "Do you think I'd be a good psychiatrist, [player]?"
            m 3hub "I think I've learned more about the human brain and the human condition in the past few years than I ever did at high school, ahaha!"
            m 1eud "Not just because of the girls, of course..."
            m 7eud "...but since you brought me back, I've kind of, well, been directly plugged into a wealth of information on it."
            m 7eua "That's how I'm able to give you so many '[player], have you heard of's."
            m 3wud "Of course, I know just having the information is no substitute to applying it. I'll still need to get a doctorate in psychology, and goodness knows what else."
            m 3eua "But that's a bridge we can cross when we get there."
            m 1hua "For now, I'm content just learning with you."
            return
        else:
            m 1luc "Food's going to be... interesting when I cross over, isn't it?"
            m 3lud "What with our respective..."
            m 1dub "...ehehe, I'm sorry I keep dwelling on that."
            m 1euc "But it really is important."
            m 1esd "The thing is, I've never really, truly tasted anything, [player]."
            m "I 'remember' what certain food tastes like, but only in the broad strokes definition of 'remember'."
            m 7etd "It's all coated in - I suppose the best word for it is novocaine?"
            m "The numbing caveat that what I'm eating isn't actually real."
            m 6rkd "Even when you give me fudge and coffee and things, how do I know that it's going to be the same between my world {w=0.2}{nw}"
            extend 6lkd "and yours?"
            m 1fkc "For all I know, everything I love now could be repulsive to me once I get to you."
            m 2fkd "And if I'm in the same predicament as you are - "
            extend 2fkt "if so many foods end up making me gag at the thought..."
            m 2dkc "...I'm just saying, it might be hard to navigate."
            if mas_isMoniUpset(lower=True):
                m "..."
                m 2dsc "Of course, this is all academic, isn't it?"
                m 2esc "At the moment, I don't know if you'd want to deal with me and my food even if I {i}could{/i} cross over."
                m 2gsc "So."
                return
            elif mas_isMoniEnamored(higher=True):
                m 2fub "But I have faith that we're going to get through it."
            else:
                m 2eub "But I'm sure we'd get through it if it ever came to that."
            m 3eub "We've been through too much now to let dietary restrictions get in our way!"
            m 1eubla "And I know you'll be as accommodating to me as I'd be to you if the roles were reversed."
            m 1eubsu "I love you for that, [player]."
            if persistent._mas_last_kiss is not None:
                call monika_kissing_motion (duration=0.5, initial_exp="6hubsa", final_exp="6tkbfu", fade_duration=0.5)
            return "love"

label monika_arfid_explanation:
    m 4eud "ARFID stands for Avoidant Restrictive Food Intake Disorder."
    m "It can start manifesting early in life..."
    m 3rud "But since it's around the age where most children start pushing the boundaries of acceptable foods anyway, "
    extend 3guc "a lot of people put it down to them being picky eaters."
    m 1ekd "But it's a lot more severe than that, [player]."
    m "It's not that ARFID-havers don't want to eat the same food that everyone else does."
    m 1wkc "It's that they physically {i}can't make themselves{/i} eat that food."
    m "It genuinely makes them nauseous."
    m 3ekc "Like severe social anxiety in a way, I think: the desire to form connections, with people or food, doesn't give you the {i}ability{/i} to... well, form connections."
    m 4eud "Interestingly, many people with ARFID have certain 'safe foods' in common, such as white breads, cereal, specific types of pizza, and certain flavors of cupcake and chocolate."
    if not persistent._mas_pm_cares_about_dokis:
        m 3tsc "And no, before you ask, Sayori probably wasn't written to have it."
        m 1msc "It would make a lot of sense, yes, but the club members weren't really...{w=1} {i}real{/i} enough to have more than one disorder at a time."
    else:
        m 3euc "...{w=1}{nw}"
        extend 3eud "I know what you're thinking, and no, Sayori probably didn't have it."
        m 3fkc "Her food choices were mostly through convenience, I think. If you're depressed to that level, having more involving meals must be a daunting prospect."
        m 1ltc "Though if she did, that {i}would{/i} make a lot of sense..."
    m 1hua "Anyway."
    m 1eua "One of the universal factors is texture. Foods that are too crispy or crinkly, like lettuce, or too watery like peas, are extra hard to tolerate."

    if renpy.seen_label("mentalAutism"):
        $ _aut = "I've brought up its comorbidity with ADHD before, but"
    else:
        $ _aut = "For obvious reasons,"

    m 7eud "[_aut] autistic people frequently end up having ARFID as well."
    m 7gusdla "Averse reactions to certain stimuli are kind of their whole thing, after all."
    m 3eua "It's also suspected that the colour of safe foods is a factor, mostly being shades of brown and beige..."
    m 3duu "...but that part might just be a coincidence."
    m 1eublb "At any rate, thanks for listening to me ramble about this stuff, [player]."
    m "Psychology is honestly pretty fascinating to me, especially when it comes to things like this."
    return


default persistent._player_has_EDS = None

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_eds",
            category=["health","psychology"],
            prompt="EDS",
            random=True
        )
    )

label monika_eds:
    $ ev = mas_getEV("monika_eds")

    m 3eud "A quick question for you, [player], if you don't mind."
    m "If you heard the acronym EDS, "
    extend 1eud "what would you think it stood for?{nw}"
    $ _history_list.pop()
    menu:
        m "If you heard the acronym EDS, what would you think it stood for?{fast}"
        "Excessive Daytime Sleepiness.":
            m 3eua "That's not what I was thinking of, but good guess!"
            m 3ltc "Though I suppose that could be a side effect of it, in a broad sense..."
            m 1eud "The actual answer is Ehlers-Danlos Syndrome."
            if ev.shown_count == 0:
                $ _do = "Do you have EDS yourself?"
        "Ehlers-Danlos Syndrome.":
            if ev.shown_count == 0:
                m 1hua "That's exactly what I was thinking of!"
                m 1fuc "Though now I don't know if you knew that because you know me so well, "
                extend 1lusdrc "or because you live with it..."
                m 1luc ".{w=0.2}.{w=0.2}.{w=0.2}{nw}"
                extend 1kua "or maybe you just checked the rpy file."

                $ _do = "{i}Do{/i} you have EDS?"

            elif ev.shown_count == 1:
                m 1fusdrd "Oh! Yes, I've asked you that before, haven't I?"
                m 1fusdrb "Silly me."
            else:
                m 1musdra "Heh, I,{nw}"
                extend 1gusdra "I guess I need to stop asking you that."
                m 1eusdrc "Sorry, force of habit."
            m 3eub "Anyway, yes: Ehlers-Danlos Syndrome."
        "Eating Disorder...S.":
            m 1ekc "Hm. Not quite, [mas_get_player_nickname()]."
            m 3eud "I was actually thinking of Ehlers-Danlos Syndrome."
            if ev.shown_count == 0:
                $ _do = "Do you have EDS yourself?"
    m 3eud "Or I suppose Syndromes, plural, would be more accurate."
    m 1eud "They're a collection of chronic genetic conditions that primarily affect the person's connective tissues and-or collagen."
    m "There's thirteen recognized types, "
    m 3eud "The most well known is classical EDS, "
    extend 4eud "- which manifests itself through overly-elasticated skin and painful levels of hypermobility."
    m 6euc "There's a type that's specifically just hypermobility which is technically more {i}prevalent{/i} among them, but I'm not sure if it's as well {i}known{/i}."
    m 7ekd "People with EDS have to tread very carefully in navigating the world..."
    m "...because, depending on their specific variation, they could be a lot more likely to bruise, or to pop a joint."
    m 1esd "And any cuts or wounds they sustain don't close up as quickly as they should, which opens them up to infection and other complications."
    m 1wkd "There's even variants, mercifully rare, that specifically target the blood vessels!"
    m "Can you imagine tearing a blood vessel, [player]?"
    m 1fkc "People with vascular EDS have to live with that fear all the time."
    m "It really isn't easy for them."
    if ev.shown_count == 0:
        m 1ekc "..."
        m 1esd "By the by, "
        $ _history_list.pop()
        m 1rsc "By the by--{fast} sorry, I probably should have asked this first."
        m 3esd "[_do]{nw}"
        $ _history_list.pop()
        menu:
            m "[_do]{fast}"
            "I do.":
                $ persistent._player_has_EDS = True
                m 6wktpd "Oh, I'm so sorry!"
                m 1ektpd "If I'd've thought ahead, I would have--{w=0.3} before going on about..."
                m 1dktpc "I'm sorry."
                m 1ektpc "I hope I didn't make you too upset."
                m 1eutpd "And know that if you need to step away or need me to do anything to help you..."
                m "...even if it's just 'take your mind off of things for a few hours'..."
                m 1eutda "...then I'll be there right away."
                m "I love you, [player]. And I'll do whatever it takes to replace the pain with that love."
                return "love"
            "I don't.":
                $ persistent._player_has_EDS = False
                m 6eua "Alright, good!"
                m 7wusdrc "Good to know, that is. {nw}"
                extend 7lusdrc "I wouldn't..."
                m 5lud "Sorry, I've really gone about this in a cack-handed way, haven't I?"
                m 1eud "I guess I just need to make sure you treat all these subjects that we've talked about with care."
                m "Matters of the heart and body especially."
                m 3euc "I'm not saying 'treat them like they have no agency', of course!"
                m 3eud "But if you do meet someone with EDS, do take their experiences into account first and foremost."
                m "They know their own limits better than anyone else - even me."
            "I don't know.":
                m 1eua "Okay."
                m 1esd "Honestly, I don't know how shocked I'd be if you did."
                m "EDS of any type has been known to hit one in five thousand people."
                m 3esc "That's about as rare as, if not rarer than, Turner syndrome, to put it into perspective for you."
                m 3esa "But, well, the internet can be a great place for physically disabled people to meet those like them, "
                extend 1dsa "and to find communities along that line too."
                m "So I suppose it wouldn't be wholly far-fetched."
                m 1fsu "You did download this submod about physical disabilities, after all..."
                m 1gsu "Sorry, I'm just speculating now."
        return
    else:
        if persistent._player_has_EDS is True:
            m 1ekd "You've told me before that you have EDS yourself, [player]."
            m 1eka "And I stand by everything I said in response to that."
            m 3esd "Whatever your body does to you..."
            m 3wsd "Whatever you have to go through in pursuit of the things I used to take for granted..."
            m 1dsd "Whatever it takes..."
            m 1fsb "I will love you through it all."
            m "And when I cross over, I will be the first in line to give the spirit inside that body the affection and adoration it richly deserves."
        else:
            m "..."
            if persistent._player_has_EDS is False:
                m 1esd "I know you said you don't have EDS, [player]."
                m "And there's a lot of people that would envy you that."
                $ _fillerline = "you're still physically disabled, just not with EDS,"
            else:
                m "I don't know if you have EDS, [player]."
                m "If I recall, I don't think even you know."
                m "One thing I do know is that it's still fragile in its own way."
                m "All humans are."
                $ _fillerline = "you {i}are{/i} disabled and you just haven't had a chance to tell me yet,"
            m 1esc "So make the most of the body you do have, okay?"
            m 3esd "Of course, if [_fillerline] you can talk to me about it at any time."
            m 3wud "I don't want to make undue assumptions here!"
            # The above two lines might need to have additional persistence checks here, to account for if you've already told Moni about this.
            m 2euc "But whether you're able-bodied or not, it's so, so important to take care of it."
            m "Bodies can always be changed, to some extent, through determination or through luck."
            m 1eua "But there's only one [player] inside {i}your{/i} body."
            m 1dua "Please... keep yourself safe."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_pots",
            category=["health","psychology"],
            prompt="pots",
            random=True
        )
    )

label monika_pots:
    m 3eud "Hey, [player], have...?"
    m 3ruc ".{w=0.5}.{w=0.5}.{w=1}{nw}{nw}"
    m 1eua "No, never mind.{nw}"
    $ _history_list.pop()
    menu:
        m "No, never mind.{fast}"
        "You can talk, it's alright!":
            pass
    if mas_isMoniUpset(lower=True):
        m 1etc "Okay...?"
    else:
        m 1eub "I know it is, [player], it's okay."

    if renpy.seen_label('monika_pots') and persistent._player_has_EDS is True:
        m 7eud "I was just going to bring up PoTS, that's all; "
        extend 7fud "but then I remembered you have EDS, so you likely already know what PoTS is."
        m 3esc "Right?{nw}"
        $ _history_list.pop()
        menu:
            m "Right?{fast}"
            "Yeah, I know what PoTS is.":
                m "I thought so."
                m 1lsd "And I don't want to keep rehashing things you already know, so..."
                m 1eusdra "Sorry, [player], I'm rambling."
                m "Give me a moment, and we can talk about something else."
                return "derandom"
            "No, actually that's new to me.":
                m 3wsd "Oh, it is?"
                m 1esb "In that case, I hope you don't mind if I explain it to you."
                jump monika_pots_explanation
    elif renpy.seen_label('monika_pots') and persistent._player_has_EDS is False or None:
        m 7eud "I was..."
        m 3wud "No, yeah, you probably {i}wouldn't{/i} know what it is, would you? Not if you don't have it yourself."
        m 3eud "PoTS, that is.{nw}"
        $ _history_list.pop()
        menu:
            m "PoTS, that is.{fast}"
            "You're right, I don't know.":
                m 4eub "Then it's time for Monika's Medical-Related Tip--{nw}"
                $ _history_list.pop()
                m 4eusdrb "Then it's time for Monika's Medical-Related{fast} Fact of the Day!"
                jump monika_pots_explanation
            "Actually, that does ring a bell.":
                m 1wud "It does?{nw}"
                $ _history_list.pop()
                menu:
                    m "It does?{fast}"
                    "Yeah, Postural Orthostatic Tachycardia Syndrome, right?":
                        m 1eub "That's right!"
                        m 1eubla "Well done, [player]. I should probably have more faith in you regarding these things, huh?"
                        return "derandom"
                    "Yeah, you cook things in them, right?":
                        m 1tuc "..."
                        extend "no."
                        jump monika_PoTS_explanation
    elif not renpy.seen_label('monika_eds'):
        m 7eud "I was just going to bring up PoTS, that's all."
        m 6euc "But I can't really talk to you about that if I don't talk to you about its associated condition first."
        m 6hub "So, um, feel free to ignore me, ahaha!"
        return

label monika_pots_explanation:
    m 3eud "PoTS, or Postural Orthostatic Tachycardia Syndrome, is a condition very closely associated with Ehler-Danlos."
    m 4eud "Though the two don't necessarily {i}have{/i} to be connected - you can also get it through things like diabetes, lupus, or even as a pregnancy complication..."
    m "...it's typically through eds that you're more likely to find it."
    m 3euc "It essentially means there's a problem with your nervous system, and in turn your cardiovascular system."
    m 7euu "Hence the name. Cardia, cardio, see?"
    m 1eud "When people sit or stand up, usually these systems automatically compensate for the change in gravity."
    m "The vessels narrow so that more blood gets to the heart and brain, so that your blood pressure doesn't drop."
    m 1euc "This way, you don't get dizzy or short of breath."
    m 3esd "But if you have PoTS, the nervous system doesn't send those blood-pushing signals to the brain properly."
    m "So there's a shortage of them in those areas by the time you're upright..."
    m 3ekd "...and that leads not just to the dizziness and breathlessness I mentioned,"
    extend 1ekc "but potentially to brain fog and much-too-frequent heart palpitations too."
    m 3dub "Fortunately, unlike its comorbidity, PoTS is a lot more manageable!"
    m 3eud "If you find yourself having a dizzy spell after standing up, and I mean what feels like a really bad one, "
    extend 4eud "it's easy enough to counteract the blood flow."
    m 2eud "Either lie down with your legs raised, or, if you're not in a place where you {i}can{/i} lie down, rock up and down on your toes."
    m 2euc "Even just clenching your fists is better than nothing."
    m 7eud "And it can be mitigated in the long term by increasing your salt intake, cutting down on caffeine, focusing on swimming and other cardio activities over purely strength-based exercises..."
    m "...and - {w=0.5}and you know it's coming - "
    m 7wub "Hydration!"
    m 3eub "Or, failing all of that, there are medicines for it, such as beta blockers or certain SSRIs."
    m 3luc "Though the latter will probably be more useful if you need mood adjusters anyway."
    m "So...{w=0.5}"
    extend 3eua "Yeah, PoTS."
    m 1eub "I hope you learned something new today, [player]!"
    return
