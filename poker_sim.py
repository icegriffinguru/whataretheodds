"""
Output table of percent of hand rankings with
pairs, 2 pairs, flushes, and high card generated from
range of 10,000 - 100,000 hands
"""

import card_deck as cd

def deal(deck, param):
    pass

def hand_rank(hand):
    pass

def play_rounds(n = 100000, hands = None, rank_names = None):
    """
    Generate the number of hands from 10k to 100k with percentage of hands in each incremental 10k generated hands
    :return: percentage of type generated in total number of hands and specific number, compared hands
    """

    rounds = [i: 0 for in range(9)]
    for i in range(n):
        deck = cd.shuffle_deck()
        deal(deck, 5)
        rounds[hand_rank(hands)] += 1
    
    for j in range(9):
        print(f'{rank_names[j]}; {rounds[j] ({100 * rounds[j] / n}%)')

table = {'# of hands': 10000, 'pairs': xx, '%', xx.xx}
for number, hands in table.items():
    print(f'{number:10} ==> {hands:10d}')
