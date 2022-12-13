#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    discs = []
    d = 0
    for l in open(sys.argv[1] if len(sys.argv) > 1 else '15-input').read().splitlines():
        l = l.split()
        n = int(l[3])
        p = int(l[-1][:-1])

        discs += [(n, (p + d) % n)]
        d += 1


    def run(D: list[tuple[int, int]]) -> int:
        for i in range(10000000):
            Dn = []
            all_zero = True
            for n, p in D:

                p += 1
                p %= n
                if p != 0:
                    all_zero = False
                Dn += [(n, p)]
            D = Dn

            if all_zero:
                return i


    part1 = run(discs)
    print('part1', part1)

    part2 = run(discs + [(11, len(discs) % 11)])
    print('part2', part2)
