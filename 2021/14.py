#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    repl = {}
    poly = {}
    for l in open(sys.argv[1] if len(sys.argv) > 1 else '14-input'):
        l = l.strip()
        if '->' in l:
            a, b = l.split(' -> ')
            repl[a] = b
        elif l:
            for i in range(0, len(l) - 1):
                T = l[i:i + 2]
                poly.setdefault(T, 0)
                poly[T] += 1

    for i in range(40):
        npoly = {}
        for T in poly:
            N = T[0] + repl[T]
            npoly[N] = npoly.get(N, 0) + poly[T]

            N = repl[T] + T[1]
            npoly[N] = npoly.get(N, 0) + poly[T]

        poly = npoly

        if i == 9:
            part1 = poly.copy()
        if i == 39:
            part2 = poly.copy()


    def result(r: dict) -> int:
        total = {v: 0 for v in repl.values()}
        for p, c in r.items():
            total[p[0]] += c
            total[p[1]] += c
        return int((max(total.values()) - min(total.values())) / 2 + 0.5)


    print('part1', result(part1))
    print('part2', result(part2))
