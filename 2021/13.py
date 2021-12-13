#!/usr/bin/env python3

import sys
import numpy as np

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    paper = np.zeros((0, 0), dtype=int)

    folding = False
    fold_count = 0
    for l in open(sys.argv[1] if len(sys.argv) > 1 else '13-input'):
        l = l.strip()
        if len(l) == 0:
            folding = True
            continue

        if folding:
            fold_count += 1
            _, _, i = l.split()
            orient, coord = i.split('=')
            coord = int(coord)

            if orient == 'x':
                le = paper[:, 0:coord]
                ri = paper[:, coord + 1:]
                paper = le | ri[:, ::-1]

            elif orient == 'y':
                up = paper[0:coord]
                lo = paper[coord + 1:]
                paper = up | lo[::-1]

            if fold_count == 1:
                part1 = np.count_nonzero(paper)

        else:
            x, y = map(int, l.split(','))
            if x >= paper.shape[1] or y >= paper.shape[0]:
                old = paper
                paper = np.zeros((max(y + 1, old.shape[0]), max(x + 1, old.shape[1])), dtype=int)
                paper[0:old.shape[0], 0:old.shape[1]] = old

            paper[y, x] = 1

    print('part1', part1)

    for row in paper:
        print(''.join('#' if c else ' ' for c in row))
