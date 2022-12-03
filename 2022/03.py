#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    content = [line.strip() for line in open(sys.argv[1] if len(sys.argv) > 1 else '03-input')]

    prio = lambda c: 27 - ord('A') + ord(only[0]) if str.isupper(c) else 1 - ord('a') + ord(only[0])

    for l in content:
        a, b = set(l[0:len(l) // 2]), set(l[len(l) // 2:])
        only = (a & b).pop()
        part1 += prio(only)

    for i in range(0, len(content), 3):
        a, b, c = map(set, content[i:i + 3])
        only = (a & b & c).pop()
        part2 += prio(only)

    print('part1', part1)
    print('part2', part2)
