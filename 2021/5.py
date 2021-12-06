#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":
    ocean = np.zeros((1000, 1000), dtype=int)
    ocean2 = np.zeros((1000, 1000), dtype=int)

    for l in open('5-input'):
        p = l.strip().split(' -> ')
        x1, y1 = map(int, p[0].split(','))
        x2, y2 = map(int, p[1].split(','))

        if x1 > x2 or y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        if x1 == x2 or y1 == y2:
            ocean[y1:y2 + 1, x1:x2 + 1] += 1
            ocean2[y1:y2 + 1, x1:x2 + 1] += 1
        else:
            d = abs(x1 - x2) + 1
            dx = 1 if x1 < x2 else -1
            dy = 1 if y1 < y2 else -1
            for _ in range(d):
                ocean2[y1, x1] += 1
                x1 += dx
                y1 += dy

        ocean2[y1:y2, x1:x2] += 1

    part1 = np.count_nonzero(ocean[ocean >= 2])
    part2 = np.count_nonzero(ocean2[ocean2 >= 2])
    print('part1', part1)
    print('part2', part2)
