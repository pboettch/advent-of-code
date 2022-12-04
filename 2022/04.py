#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '04-input'):
        p, q = l.strip().split(',')
        a, b = map(int, p.split('-'))
        c, d = map(int, q.split('-'))

        A = set(range(a, b + 1))
        B = set(range(c, d + 1))

        if set() in (A - B, B - A):
            part1 += 1

        if len(A | B) != len(A) + len(B):
            part2 += 1

    print('part1', part1)
    print('part2', part2)
