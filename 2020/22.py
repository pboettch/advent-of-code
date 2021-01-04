#!/usr/bin/env python3

from typing import List


def play(deck1: List[int], deck2: List[int], part2=False):
    player_decks = [[], []]

    while len(deck1) > 0 and len(deck2) > 0:
        # prevent recursion

        if deck1 in player_decks[0] or deck2 in player_decks[1]:
            return 1, deck1

        player_decks[0].append(deck1.copy())
        player_decks[1].append(deck2.copy())

        c1, deck1 = deck1[0], deck1[1:]
        c2, deck2 = deck2[0], deck2[1:]

        if part2 and c1 <= len(deck1) and c2 <= len(deck2):
            winner, _ = play(deck1[:c1], deck2[:c2], part2)
            # print('sub-game', c1, c2, 'winner', winner)
        else:
            if c1 > c2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]

        # print('round',count)
        # print(deck1)
        # print(deck2)

    return winner, deck1 if winner == 1 else deck2


_deck1, _deck2 = open('22.input').read(2000).rstrip().split('\n\n')

_deck1 = [int(i) for i in _deck1.split('\n')[1:]]
_deck2 = [int(i) for i in _deck2.split('\n')[1:]]

winner, winner_deck = play(_deck1, _deck2)

score = sum([(i + 1) * c for i, c in enumerate(reversed(winner_deck))])
print('part 1, score', score)

winner, winner_deck = play(_deck1, _deck2, True)
score = sum([(i + 1) * c for i, c in enumerate(reversed(winner_deck))])
print('part 2, score', score)
