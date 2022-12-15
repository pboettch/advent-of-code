#!/usr/bin/env python3

import sys
import re


def range_of_line(sq: tuple[int, int, int], l: int) -> set[int]:
    no = sq[2] - abs(l - sq[1])
    if no < 0:
        return None
    return sq[0] - no, sq[0] + no + 1


def merge(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    ans = []
    for i in range(len(ranges)):

        merged_something = False

        r = ranges[i]
        for j in range(i+1, len(ranges)):
            s = ranges[j]
            if s[0] - 1 <= r[0] <= s[1] or s[1] + 1 >= r[1] >= s[0] or \
                    r[0] < s[0] < s[1] < r[1]:  # r overlaps s, touches s, is inside s or s completely inside r
                ranges[j] = (min(r[0], s[0]), max(r[1], s[1]))
                merged_something = True
                break

        if not merged_something:
            ans += [r]

    return ans


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    match = re.compile(r'[xy]=([-\d]+)')

    squares = []
    beacons = set()
    for l in open(sys.argv[1] if len(sys.argv) > 1 else '15-input').read().splitlines():
        sx, sy, bx, by = map(int, match.findall(l))

        d = abs(bx - sx) + abs(by - sy)
        squares += [(sx, sy, d)]

        beacons.add((bx, by))

    part1_line = 2000000
    # part1_line = 10

    maxy = 4000000

    for line in range(0, maxy):
        # for line in range(0, 4000000):
        ranges = []
        for square in squares:
            if r := range_of_line(square, line):
                ranges.append(r)

        m = merge(ranges)
        if line == part1_line:
            r = m[0]
            part1 = r[1] - r[0]
            for b in beacons:
                if b[1] == part1_line and r[0] <= b[0] <= r[1]:
                    part1 -= 1

        assert 0 < len(m) <= 2

        if len(m) == 2:
            a = min(m[0][1], m[1][1])
            part2 = maxy * a + line

        if 0 not in (part1, part2):
            break

    print('part1', part1)
    print('part2', part2)
