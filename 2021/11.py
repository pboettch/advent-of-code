#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":

    cave = []
    for l in open('11-input'):
        l = l.strip()
        cave += [list(map(int, l))]

    cave = np.array(cave)

    part1 = 0
    part2 = 0

    step = 0
    while True:
        step += 1

        cave += 1

        while True:
            flash_indices = np.where(cave > 9)

            if step <= 100:
                part1 += len(flash_indices[0])

            if len(flash_indices[0]) == 0:
                break

            cave[flash_indices] = 0

            for i in zip(*flash_indices):
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        j = (i[0] + dy, i[1] + dx)
                        if 0 <= j[0] < 10 and 0 <= j[1] < 10:
                            if cave[j] != 0:
                                cave[j] += 1

        if np.count_nonzero(cave) == 0:
            part2 = step
            break

    print('part1', part1)
    print('part2', part2)
