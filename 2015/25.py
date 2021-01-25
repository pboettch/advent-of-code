#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    init = 20151125
    factor = 252533
    divisor = 33554393

    for y in range(1, 3076 * 2):
        d = y
        for x in range(1, y + 1):
            if d == 2981 and x == 3075:
                print('part1', init)
                sys.exit(0)
            init *= factor
            init %= divisor
            d -= 1
