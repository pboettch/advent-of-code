#!/usr/bin/env python3

import itertools

happy = {}


def calculate_happiness(comb: set):
    h = 0
    for i in range(len(comb)):
        h += happy[comb[i]][comb[i - 1]] + happy[comb[i - 1]][comb[i]]
    return h


def best_happiness(items):
    happiness = 0
    for comb in itertools.permutations(items, len(items)):
        h = calculate_happiness(comb)
        if h > happiness:
            print('better happiness', h, comb)
            happiness = h
    return happiness


for l in open('13.input'):
    items = l.rstrip().split(' ')

    value = int(items[3]) * (-1 if items[2] == 'lose' else 1)
    happy.setdefault(items[0], {})
    happy[items[0]][items[-1][0:-1]] = value

print('part1', best_happiness(happy.keys()))

happy['me'] = {}
for o in happy.keys():
    happy['me'][o] = 0

for k in happy.keys():
    if k == 'me':
        continue
    happy[k]['me'] = 0

print('part2', best_happiness(happy.keys()))
