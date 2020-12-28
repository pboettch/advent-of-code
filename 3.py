#!/usr/bin/env python3

from functools import reduce


def trav(right: int, down: int):
    trees = 0

    x = right
    y = down

    line = 0

    for l in open('3.input').readlines():
        l.strip()

        if line == y:
            if l[x] == '#':
                trees += 1

            x += right
            x %= len(l) - 1
            y += down

        line += 1

    return trees


rules = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

print('trees 1', trav(3, 1))

results = [trav(r[0], r[1]) for r in rules]
product = reduce(lambda x, y: x * y, results)

print('trees 2', product)
