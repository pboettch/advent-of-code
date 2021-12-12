#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '11-input'):
        l = l.strip()

    print('part1', part1)
    print('part2', part2)
