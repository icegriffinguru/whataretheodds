"""
Formatting deck of cards.
"""
# format of card tuple('A', 'spade')

import card_deck

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


def get_r(card):
    """
    The value for ranks in deck of cards.
    :param cards: Deck of cards.
    :return: The left-hand side value of cards as a tuple returning suits.
    """
    return card[0]


def get_s(card):
    """
    The value for suits in deck of cards.
    :param card: Deck of cards.
    :return: The right-hand side value of cards as a tuple returning suits.
    """
    return card[1]


def get_rank_index(card):
    """
    Retrieve the rank index of the card
    :param card: a card.
    :return: the rank index of the card
    """
    for index, rank in enumerate(card_deck.ranks):
        if get_r(card) == rank:
            return index
    raise Exception('Rank of the card is invalidate.')


# for test purpose
if __name__ == "__main__":
    print(get_rank_index((card_deck.ranks[0], card_deck.suits[0])))
    print(get_rank_index((card_deck.ranks[12], card_deck.suits[3])))
    print(get_rank_index((card_deck.ranks[5], card_deck.suits[2])))