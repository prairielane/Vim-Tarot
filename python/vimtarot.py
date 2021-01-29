# import required modules

import copy
import random

# test for vim module!

try:
    import vim
except:
    print("No vim module available outside vim")
    pass


def combinelist(l1, l2):
    new = []
    for i in range(len(l1)):
        new.append(l1[i])
        new.append(l2[i])
    return new


def insertlist(test_list, insert_list, pos):
    test_list[pos:pos] = insert_list
    return test_list


# ================================
# Tarot Celtic Cross
# ================================


def TarotCelticCross():
    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)

    # Get the CelticCross questions
    from questions.questions import CelticCross

    # Get subset of Tarot Cards
    Drawn = TarotDeck[0:10]

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # Combine questions and Drawn Cards

    toinsertlist = combinelist(CelticCross, Drawn)

    # make the output pretty - added 01/10/21
    # Deep copy the list
    copytoinsertlist = copy.deepcopy(toinsertlist)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =================================
# Tarot Celtic Cross Questions
# =================================


def TarotCelticCrossQuestion():

    # Get the CelticCross questions.questions
    from questions.questions import CelticCross

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(CelticCross)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ================================
# Tarot Character Developement
# ================================


def TarotCharacter():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)

    # Get the character questions.questions
    from questions.questions import character

    # Get subset of Tarot Cards
    Drawn = TarotDeck[0 : len(character)]

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # Combine questions.questions and Drawn Cards

    toinsertlist = combinelist(character, Drawn)

    # make the output pretty - added 01/10/21
    # Deep copy the list
    copytoinsertlist = copy.deepcopy(toinsertlist)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ========================================
# Tarot Character Developement Questions
# ========================================


def TarotCharacterQuestion():

    # Get the Character questions.questions
    from questions.questions import character

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(character)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ===========================
# Simple Beat
# ===========================


def TarotSimpleBeat():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)

    # Get the Simple Beatsheet questions.questions
    from questions.questions import simplebeat

    # Get subset of Tarot Cards
    Drawn = TarotDeck[0 : len(simplebeat)]

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # Combine questions.questions and Drawn Cards

    toinsertlist = combinelist(simplebeat, Drawn)

    # make the output pretty - added 01/10/21
    # Deep copy the list
    copytoinsertlist = copy.deepcopy(toinsertlist)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ========================================
# Tarot Simple Beat Questions
# =========================================


def TarotSimpleBeatQuestion():

    # Get the Simple Beat questions.questions
    from questions.questions import simplebeat

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(simplebeat)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ======================
# Complex Beat
# ======================


def TarotComplexBeat():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)

    # Get the Complex Beat Sheet questions.questions
    from questions.questions import complexbeat

    # Get subset of Tarot Cards
    Drawn = TarotDeck[0 : len(complexbeat)]

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # Combine questions.questions and Drawn Cards

    toinsertlist = combinelist(complexbeat, Drawn)

    # make the output pretty - added 01/10/21
    # Deep copy the list
    copytoinsertlist = copy.deepcopy(toinsertlist)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ========================================
# Tarot Complex Beat Questions
# =========================================


def TarotComplexBeatQuestion():

    # Get the Complex Beat questions.questions
    from questions.questions import complexbeat

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(complexbeat)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ======================
# Hero's Journey
# ======================


def TarotHeroJourney():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)

    # Get the complexbeat questions.questions
    from questions.questions import herojourney

    # Get subset of Tarot Cards
    Drawn = TarotDeck[0 : len(herojourney)]

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # Combine questions.questions and Drawn Cards

    toinsertlist = combinelist(herojourney, Drawn)

    # make the output pretty - added 01/10/21
    # Deep copy the list
    copytoinsertlist = copy.deepcopy(toinsertlist)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# ========================================
# Tarot Hero Journey Questions
# =========================================


def TarotHeroJourneyQuestion():

    # Get the Hero Journey questions.questions
    from questions.questions import herojourney

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(herojourney)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Deck
# =====================


def TarotDeck():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(TarotDeck)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Deck Single
# =====================


def TarotDeckSingle():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana
    from cards.TarotMinorArcana import MinorArcana
    from cards.TarotCourtCards import CourtCards

    # Combine lists to get full deck of tarot cards
    TarotDeck = MajorArcana + MinorArcana + CourtCards

    # Shuffle the Tarot Deck
    random.shuffle(TarotDeck)
    single = random.choice(TarotDeck)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    newlist = ["", single, ""]
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Major
# =====================


def TarotMajor():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana

    # Shuffle the Major Arcana
    random.shuffle(MajorArcana)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(MajorArcana)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Major Arcana Single
# =====================


def TarotMajorSingle():

    # import list of cards
    from cards.TarotMajorArcana import MajorArcana

    # Shuffle the Major Arcana
    random.shuffle(MajorArcana)
    single = random.choice(MajorArcana)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    newlist = ["", single, ""]
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Minor
# =====================


def TarotMinor():

    # import list of cards
    from cards.TarotMinorArcana import MinorArcana

    # Shuffle the Minor Arcana
    random.shuffle(MinorArcana)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(MinorArcana)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Minor Arcana Single
# =====================


def TarotMinorSingle():

    # import list of cards
    from cards.TarotMinorArcana import MinorArcana

    # Shuffle the Minor Arcana
    random.shuffle(MinorArcana)
    single = random.choice(MinorArcana)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    newlist = ["", single, ""]
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Court Cards
# =====================


def TarotCourt():

    # import list of cards
    from cards.TarotCourtCards import CourtCards

    # Shuffle the Court Cards
    random.shuffle(CourtCards)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(CourtCards)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Court Cards Single
# =====================


def TarotCourtSingle():

    # import list of cards
    from cards.TarotCourtCards import CourtCards

    # Shuffle the Court Cards
    random.shuffle(CourtCards)
    single = random.choice(CourtCards)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    newlist = ["", single, ""]
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Cups
# =====================


def TarotCups():

    # import list of cards
    from cards.TarotMinorArcana import cups

    dccups = copy.deepcopy(cups)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(dccups)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Cups Random
# =====================


def TarotCupsRandom():

    # import list of cards
    from cards.TarotMinorArcana import cups

    # Shuffle the Tarot Deck
    random.shuffle(cups)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(cups)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Wands
# =====================


def TarotWands():

    # import list of cards
    from cards.TarotMinorArcana import wands

    dcwands = copy.deepcopy(wands)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(dcwands)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Wands Random
# =====================


def TarotWandsRandom():

    # import list of cards
    from cards.TarotMinorArcana import wands

    # Shuffle the Tarot Deck
    random.shuffle(wands)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(wands)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Swords
# =====================


def TarotSwords():

    # import list of cards
    from cards.TarotMinorArcana import swords

    dcswords = copy.deepcopy(swords)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(dcswords)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Swords Random
# =====================


def TarotSwordsRandom():

    # import list of cards
    from cards.TarotMinorArcana import swords

    # Shuffle the Tarot Deck
    random.shuffle(swords)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(swords)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Pentacles
# =====================


def TarotPentacles():

    # import list of cards
    from cards.TarotMinorArcana import pentacles

    dcpentacles = copy.deepcopy(pentacles)

    # Shuffle the Tarot Deck
    # random.shuffle(pentacles)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(dcpentacles)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Pentacles Random
# =====================


def TarotPentaclesRandom():

    # import list of cards
    from cards.TarotMinorArcana import pentacles

    rcpentacles = copy.deepcopy(pentacles)

    # Shuffle the Tarot Deck
    random.shuffle(rcpentacles)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(rcpentacles)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot Fool
# =====================


def TarotFool():

    # import list of cards
    from cards.TarotMajorArcana import fooljourney

    dcfooljourney = copy.deepcopy(fooljourney)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(dcfooljourney)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)


# =====================
# Tarot FoolJourney Random
# =====================


def TarotFoolRandom():

    # import list of cards
    from cards.TarotMajorArcana import fooljourney

    # dcfooljourney = copy.deepcopy(fooljourney)

    # Shuffle the Tarot Deck
    random.shuffle(fooljourney)

    # Get buffer line insert point
    pos = int(vim.eval('line(".")'))

    # make the output pretty - added 01/10/21
    # Deep copy the list

    copytoinsertlist = copy.deepcopy(fooljourney)
    blanklist = [""] * len(copytoinsertlist)
    newlist = combinelist(copytoinsertlist, blanklist)
    vim.current.buffer.append(newlist, pos)
