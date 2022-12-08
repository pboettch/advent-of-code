#!/usr/bin/env python3

import sys
import numpy as np

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    content = [list(map(int, l.rstrip())) for l in open(sys.argv[1] if len(sys.argv) > 1 else '08-input')]
    wood = np.array(content)

    for y, x in np.ndindex(wood.shape):
        p = wood[x, y]
        l, r = np.flip(wood[x, 0:y]), wood[x, y + 1:]
        u, d = np.flip(wood[0:x, y]), wood[x + 1:, y]

        visible = False
        score = 1
        for view in (l, r, u, d):
            block = view < p

            if False not in block or len(view) == 0:  # no blocking view or on the edge
                visible = True

            if False in block:  # index of first blocking
                score *= np.where(block == 0)[0][0] + 1
            else:  # no block
                score *= len(block)

        if visible:
            part1 += 1
        if score > part2:
            part2 = score

    print('part1', part1)
    print('part2', part2)
