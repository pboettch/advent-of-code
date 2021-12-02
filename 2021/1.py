#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    heights = np.array(list(map(int, open('1-input'))))
    part1 = sum(heights[:-1] < heights[1:])

    sums = np.convolve([1, 1, 1], heights, "valid")
    part2 = sum(sums[:-1] < sums[1:])

    print('part1', part1)
    print('part2', part2)
