#!/usr/bin/env python3

deck1, deck2 = open('22.input').read(2000).rstrip().split('\n\n')

deck1 = [int(i) for i in deck1.split('\n')[1:]]
deck2 = [int(i) for i in deck2.split('\n')[1:]]

count = 0

while len(deck1) > 0 and len(deck2) > 0:
    c1, deck1 = deck1[0], deck1[1:]
    c2, deck2 = deck2[0], deck2[1:]

    if c1 > c2:
        deck1 += [c1, c2]
    else:
        deck2 += [c2, c1]

    # print('round',count)
    # print(deck1)
    # print(deck2)

    count += 1

score = sum([(i + 1) * c for i, c in enumerate(reversed(deck1 if len(deck2) == 0 else deck2))])
print('done after', count, 'rounds, score', score)
