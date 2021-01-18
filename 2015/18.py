#!/usr/bin/env python3

import numpy as np
from scipy.signal import convolve2d


def f(source: np.array, mask: np.array):
    result = convolve2d(source, mask, 'same')

    output = np.zeros(source.shape, dtype=int)
    output[(source == 1) & ((result == 2) | (result == 3))] = 1
    output[(source == 0) & (result == 3)] = 1

    return output


if __name__ == "__main__":
    mask = np.ones((3, 3), dtype=int)
    mask[1, 1] = 0

    field = None
    for i, l in enumerate(open('18.input')):
        if field is None:
            field = np.empty((len(l) - 1, len(l) - 1), dtype=int)
        field[i] = [0 if c == '.' else 1 for c in l.strip()]

    field1 = field
    field2 = field
    for _ in range(100):
        field1 = f(field1, mask)
        field2 = f(field2, mask)

        field2[0, 0] = 1
        field2[0, -1] = 1
        field2[-1, 0] = 1
        field2[-1, -1] = 1

    part1 = np.sum(field1)
    print('part1', part1)

    part2 = np.sum(field2)
    print('part2', part2)
