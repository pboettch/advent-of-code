#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":
    target = 34000000

    max_houses = 1000000

    houses_a = np.zeros(max_houses, dtype=int)
    houses_b = np.zeros(max_houses, dtype=int)

    for elf in range(1, max_houses):
        houses_a[elf::elf] += 10 * elf
        houses_b[elf:(elf + 1) * 50:elf] += 11 * elf

    print('part1', np.where(houses_a >= target)[0][0])
    print('part2', np.where(houses_b >= target)[0][0])
