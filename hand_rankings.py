"""
Generate poker hand rankings pairs, 2 pairs, flushes, and high card.
:param What is composed of in a hand dealing, the required to generate each of those in a hand dealing.
:return Flushes, two pair, pair, and high card.
"""

from random import randint
from card_deck import deal_cards, ranks, suits
from card_format import get_r, get_rank_index

# ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
# suits = ['clubs', 'diamonds', 'hearts', 'spades']

hands = ['Flush', 'Two pair', 'Pair', 'High card']

def hand_rank(dealed_cards):
    """
    Get the hand rank of dealed cards
    :param: dealed cards
    :return: The possible hands out of card dealings only with flush, two pair, pair, high card.
    """

    # sort cards according to the rank of each card
    dealed_cards.sort(key = lambda card: get_rank_index(card))
    
    if is_flush(dealed_cards):
        return hands[0]
    if is_two_pair(dealed_cards):
        return hands[1]
    if is_pair(dealed_cards):
        return hands[2]
    
    # if none of the above ranks, ranking of this hand is a high card
    return hands[3]


def is_flush(my_hands):
    """
    Defining hand dealings that are flush.
    :param my_hands: Representing my_hands as the possible hand dealings that would be a flush card.
    :return:
    """
    cardsCount = len(my_hands)
    indexes = [get_rank_index(card) for card in my_hands]
    # if every card's rank is higher by one than previous card's rank then the hand is flush
    return all([indexes[i] + 1 == indexes[i + 1] for i in range(cardsCount - 1)])

def is_two_pair(my_hands):
    """
    Composition of a two pair card.; one hand
    :return: Two pair card generated from function.
    """
    indexes = [get_rank_index(card) for card in my_hands]
    return (indexes[0] == indexes[1] and indexes[2] == indexes[3]) or ((indexes[1] == indexes[2] and indexes[3] == indexes[4])) or (indexes[0] == indexes[1] and indexes[3] == indexes[3])

def is_pair(my_hands):
    """
    Composition of a pair card.
    :return: Pair card generated from function.
    """
    cardsCount = len(my_hands)
    indexes = [get_rank_index(card) for card in my_hands]
    return any([indexes[i] == indexes[i + 1] for i in range(cardsCount - 1)])

# def high_card(my_hands):
#     """
#     Composition of a high card.
#     :return: High card generated from function.
#     """
#     suits2 = [h[1] for h in my_hands]
# I have no clue.


# for test purpose
if __name__ == "__main__":
    dealed_cards = [(ranks[0], suits[0]), (ranks[12], suits[0]), (ranks[3], suits[0]), (ranks[2], suits[0]), (ranks[1], suits[0])]
    print(hand_rank(dealed_cards))

    dealed_cards = [(ranks[0], suits[0]), (ranks[12], suits[0]), (ranks[12], suits[0]), (ranks[2], suits[0]), (ranks[1], suits[0])]
    print(hand_rank(dealed_cards))

    dealed_cards = [(ranks[7], suits[0]), (ranks[7], suits[0]), (ranks[3], suits[0]), (ranks[2], suits[0]), (ranks[7], suits[0])]
    print(hand_rank(dealed_cards))

    dealed_cards = [(ranks[9], suits[0]), (ranks[12], suits[0]), (ranks[10], suits[0]), (ranks[8], suits[0]), (ranks[11], suits[0])]
    print(hand_rank(dealed_cards))

    dealed_cards = [(ranks[9], suits[0]), (ranks[12], suits[0]), (ranks[10], suits[0]), (ranks[12], suits[0]), (ranks[9], suits[0])]
    print(hand_rank(dealed_cards))