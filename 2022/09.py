#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    def dist(a: tuple[int, int], b: tuple[int, int]):
        return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


    mv = {
        'D': (0, -1),
        'U': (0, 1),
        'L': (-1, 0),
        'R': (1, 0),
    }

    C = [(0, 0) for _ in range(10)]

    part1 = set()
    part2 = set()

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '09-input').read().splitlines():
        d, c = l.split()
        d = mv[d]
        c = int(c)

        for _ in range(c):
            # move the head
            C[0] = (C[0][0] + d[0], C[0][1] + d[1])

            D = [C[0]]
            while len(C) >= 2:
                # a = C[j-1] - previous knot
                # b = C[j] - knot

                a, *C = C
                b = C[0]

                if dist(a, b) > 1:
                    # motion compare to the previous knot
                    # diagonal results in (1, 1), otherwise (1, 0) or (0, 1)
                    m = (a[0] != b[0], a[1] != b[1])
                    # correct sign of L or D motion
                    if a[0] < b[0]:
                        m = (m[0] * -1, m[1])
                    if a[1] < b[1]:
                        m = (m[0], m[1] * -1)

                    b = (b[0] + m[0], b[1] + m[1])  # b's new position

                D.append(b)

            C = D

            part1.add(C[1])
            part2.add(C[9])

    print('part1', len(part1))
    print('part2', len(part2))
