"""
Output table of percent of hand rankings with
pairs, 2 pairs, flushes, and high card generated from
range of 10,000 - 100,000 hands
"""

from card_deck import build_deck, shuffle_deck, deal_cards
from hand_rankings import hand_rank, hands

def play_rounds(n = 100000):
    """
    Generate the number of hands from 10k to 100k with percentage of hands in each incremental 10k generated hands
    :return: percentage of type generated in total number of hands and specific number, compared hands
    """

    handCount = {}
    for hand in hands:
        handCount[hand] = 0

    for i in range(n):
        shuffled_deck = shuffle_deck(build_deck())
        dealed_cards = deal_cards(shuffled_deck, 5)
        handCount[hand_rank(dealed_cards)] += 1

    print('Total Rounds: %d'%(n))
    for hand in hands:
        print('%12s\t==>\t%d\t==>\t%.2f%%'%(hand, handCount[hand], handCount[hand] * 100.0 / n))


# for test purpose
if __name__ == "__main__":
    play_rounds(100000)