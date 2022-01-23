"""
Formatting deck of cards.
"""

def add_string(cards):
    """
    Format the deck of cards in rank of suit format in a tuple.
    :param cards: deck of cards
    :return: format of cards when it's returned
    """
    return "[%r of %s]" % (get_r(cards), get_s(cards))


def create(r, s):
    """
    Formatting ranks and suits as a tuple.
    :param r: Rank
    :param s: Suit
    :return: value of rank and suits
    """
    return (r, s)


def get_r(cards):
    """
    The value for ranks in deck of cards.
    :param cards: Deck of cards.
    :return: The left-hand side value of cards as a tuple returning suits.
    """
    return cards[0]


def get_s(cards):
    """
    The value for suits in deck of cards.
    :param cards: Deck of cards.
    :return: The right-hand side value of cards as a tuple returning suits.
    """
    return cards[1]