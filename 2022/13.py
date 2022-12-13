#!/usr/bin/env python3

import sys
import functools


def cmp(L, R) -> int:
    if isinstance(L, list) and isinstance(R, list):
        for i in range(min(len(L), len(R))):
            r = cmp(L[i], R[i])
            if r != 0:
                return r
        return cmp(len(L), len(R))
    elif isinstance(L, int) and isinstance(R, int):
        if L == R:
            return 0
        if L < R:
            return -1
        if L > R:
            return 1
    elif isinstance(L, int):
        return cmp([L], R)
    elif isinstance(R, int):
        return cmp(L, [R])


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    all_packets = []
    C = open(sys.argv[1] if len(sys.argv) > 1 else '13-input').readlines()
    n = 0
    while C:
        a, b, _, *C = C
        a = eval(a)
        b = eval(b)
        n += 1

        all_packets += [a, b]
        if cmp(a, b) == -1:
            part1 += n

    A, B = [[2]], [[6]]
    all_packets += [A, B]

    all_packets = sorted(all_packets, key=functools.cmp_to_key(cmp))

    part2 = (all_packets.index(A) + 1) * (all_packets.index(B) + 1)

    print('part1', part1)
    print('part2', part2)
