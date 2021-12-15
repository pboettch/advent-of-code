#!/usr/bin/env python3

import sys

import numpy as np


def risk(G):
    result = 0
    C = {(0, 0): 0}
    end = (len(G[0]) - 1, len(G) - 1)
    while True:
        for x in range(len(G[0])):
            for y in range(len(G)):
                for n in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if n[0] < 0 or n[0] >= len(G[0]):
                        continue
                    if n[1] < 0 or n[1] >= len(G):
                        continue

                    p = (x, y)
                    r = C[p] + G[n[1]][n[0]]

                    if n not in C or C[n] > r:
                        C[n] = r

        if result == C[end]:
            break

        result = C[end]
    return result


if __name__ == "__main__":

    cave = []

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '15-input'):
        cave += [[*map(int, l.strip())]]

    part1 = risk(cave)

    cave = np.array(cave)
    cave = np.hstack([cave, cave + 1, cave + 2, cave + 3, cave + 4])
    cave = np.vstack([cave, cave + 1, cave + 2, cave + 3, cave + 4])
    cave[cave > 9] -= 9

    part2 = risk(cave.tolist())

    print('part1', part1)
    print('part2', part2)
