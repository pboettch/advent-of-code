#!/usr/bin/env python3

import sys


def find_start(p: str, L: int) -> int:
    for i in range(len(p) - L + 1):
        if len(set(p[i:i + L])) == L:
            return i + L


if __name__ == "__main__":
    assert find_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 4) == 7
    assert find_start('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19

    l = open(sys.argv[1] if len(sys.argv) > 1 else '06-input').readline().strip()

    part1 = find_start(l, 4)
    part2 = find_start(l, 14)

    print('part1', part1)
    print('part2', part2)
