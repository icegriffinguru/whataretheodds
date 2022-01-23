"""
Deck of 52 cards created for shuffling and dealing.
"""

import random

# import card_deck
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
    random.shuffle(my_decks)
    return my_decks


def deal_cards(decks, dealCount):
    """
    Dealt deck of cards after deck is shuffled.
    :return: Dealed deck of cards
    """

    dealed_cards = []
    for i in range(dealCount):
        taken_card = random.choice(decks)
        dealed_cards.append(taken_card)
        decks.remove(taken_card)
    return dealed_cards


# for test purpose
if __name__ == "__main__":
    for i in range(11):
        decks = build_deck()
        random_decks = shuffle_deck(decks)
        dealed_cards = deal_cards(random_decks, 5)
        print(dealed_cards)
