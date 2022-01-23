"""
Deck of 52 cards created for shuffling and dealing.
"""

import random

import card_deck
import card_format as cf


def build_deck():
    """
    Create a deck of cards in 4 suits and 13 ranks.
    :return: Generated ranks and suits added to the empty deck list in the format from card_format file
    """

    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    deck = []
    for rank in ranks:
        for suit in suits:
            match = cf.create(rank, suit)
            deck.append(match)

    return deck


def shuffle_deck(my_decks):
    """
    Shuffling deck of 52 cards copying the deck cards
    :param my_decks: To be shuffled deck
    :return A shuffled deck from a randomly generated pile of cards
    """
    return my_decks.shuffle()


def deal_cards(shuffled_card_deck):
    """
    Dealt deck of cards after deck is shuffled.
    :return: Dealed deck of cards
    """

    deck_shuffling = shuffle_deck()
    dealed_cards = []
    for deal in range(shuffled_card_deck):
        taken_card = random.choice(shuffled_deck)
        dealed_cards.append(taken_card)
        shuffled_deck.remove(taken_card)
    return dealed_cards


if __name__ == "__main__":
    the_cards = deal_cards(2)
    the_cards
    shuffled_deck = shuffle_deck()
