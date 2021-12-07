#!/usr/bin/env python3

import itertools
import math

if __name__ == "__main__":
    # crabs = '16,1,2,0,4,2,7,1,2,14'
    crabs = open('7-input').read()

    *positions, = sorted(map(int, crabs.split(',')))

    average = round(sum(positions) / len(positions))

    part1 = None
    part2 = None

    for p in range(max(positions) + 1):
        fuel = sum(abs(p - pos) for pos in positions)
        if part1 is None or part1 > fuel:
            part1 = fuel

        fuel2 = sum((abs(p - pos) * (abs(p - pos) + 1) // 2) for pos in positions)
        if part2 is None or part2 > fuel2:
            part2 = fuel2

    print('part1', part1)
    print('part2', part2)
