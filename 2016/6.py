#!/usr/bin/env python3

from collections import Counter

if __name__ == "__main__":
    lines = open('6.input').read().split()

    part1 = ''
    part2 = ''
    for c in list(zip(*lines[::-1])):  # transform columns to columns
        cnt = Counter(c)
        part1 += cnt.most_common()[0][0]
        part2 += cnt.most_common()[-1][0]

    print('part1', part1)
    print('part2', part2)
