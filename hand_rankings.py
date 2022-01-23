"""
Generate poker hand rankings pairs, 2 pairs, flushes, and high card.
:param What is composed of in a hand dealing, the required to generate each of those in a hand dealing.
:return Flushes, two pair, pair, and high card.
"""

from random import randint
import card_deck as deck

ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['clubs', 'diamonds', 'hearts', 'spades']


def hand_dealings():
    """
    Create 5 hands from dealed deck of cards in the card_deck file.
    :return: The possible hands out of card dealings only with flush, two pair, pair, high card.
    """
    hands = {'Flush': 0,
             'Two pair': 0,
             'Pair': 0,
             'High card': 0}

    #separate function
    hand_dealings.shuffle_deck(hands)
    return hands

place in pokers sim


def is_flush(my_hands):
    """
    Defining hand dealings that are flush.
    :param my_hands: Representing my_hands as the possible hand dealings that would be a flush card.
    :return:
    """
    return all([suits(my_hands) == suits(my_hands[0]) for card in my_hands[1:]])


def is_two_pair(my_hands):
    """
    Composition of a two pair card.; one hand
    :return: Two pair card generated from function.
    """
    suits2 = [h[1] for h in my_hands]
    for card in my_hands
        get_rank(card)


    rank_deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    for i in rank_deck:
        my_hands[i] += 1
    if sorted(my_hands.values()) == [1, 2, 2]:
        return True
    else:
        return False


def is_pair(my_hands):
    """
    Composition of a pair card.
    :return: Pair card generated from function.
    """
    suits2 = [h[1] for h in my_hands]
    rank_deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    for i in rank_deck:
        my_hands[i] += 1
        for j in rank_deck:
            my_hands[j] += 1
    if sorted(my_hands.values()) == [1, 2, 2, 2, 3, 3]:
        return True
    else:
        return False


def high_card(my_hands):
    """
    Composition of a high card.
    :return: High card generated from function.
    """
    suits2 = [h[1] for h in my_hands]
# I have no clue.

except statement

if __name__ == "__main__":
    [is_flush(hand) for hand in my_hands]
