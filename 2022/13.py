#!/usr/bin/env python3

import sys
import functools
from copy import deepcopy


def cmp(L, R):
    while L and R:
        l = L.pop(0)
        r = R.pop(0)

        if isinstance(l, int) and isinstance(r, int):
            if l == r:
                continue
            if l < r:
                return -1
            if l > r:
                return 1
            continue

        if isinstance(l, int):
            l = [l]
        elif isinstance(r, int):
            r = [r]

        if (v := cmp(l, r)) != 0:
            return v

    if len(L) == len(R):
        return 0

    return -1 if len(L) < len(R) else 1


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    all_packets = []
    for i, p in enumerate(open(sys.argv[1] if len(sys.argv) > 1 else '13-input').read().split('\n\n')):
        if p:
            a, b = [eval(t) for t in p.split('\n')]

            all_packets += [a, b]
            if cmp(deepcopy(a), deepcopy(b)) == -1:
                part1 += i + 1

    A, B = [[2]], [[6]]
    all_packets += [A, B]

    all_packets = sorted(all_packets, key=functools.cmp_to_key(lambda a, b: cmp(deepcopy(a), deepcopy(b))))

    part2 = (all_packets.index(A) + 1) * (all_packets.index(B) + 1)

    print('part1', part1)
    print('part2', part2)
