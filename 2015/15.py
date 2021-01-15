#!/usr/bin/env python3

import numpy as np

ingredients = []

for l in open('15.input'):
    l = l.rstrip().split(' ')

    base = (
            np.tile(
                np.array(
                    [int(l[2][:-1]), int(l[4][:-1]), int(l[6][:-1]), int(l[8][:-1]), int(l[10])],
                    dtype=int),
                (101, 1)).T *
            np.arange(0, 101, dtype=int)
    ).T

    ingredients.append(base)


# https://stackoverflow.com/questions/7748442/generate-all-possible-lists-of-length-n-that-sum-to-s-in-python
def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


part1 = 0
part2 = 0

for perm in sums(len(ingredients), 100):
    r = np.zeros(5, dtype=int)
    for i in range(len(ingredients)):
        r += ingredients[i][perm[i]]

    r[r < 0] = 0

    effect = r[:-1].prod()
    cal = r[4]
    if effect > part1:
        part1 = effect

    if cal == 500 and effect > part2:
        part2 = effect

print('part1', part1)
print('part2', part2)
