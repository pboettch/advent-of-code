#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    score = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    win_response = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X',
    }

    draw_response = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z',
    }

    lose_response = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y',
    }

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '02-input'):
        a, b = l.strip().split()

        part1 += score[b]
        if b == win_response[a]:
            part1 += 6
        if b == draw_response[a]:
            part1 += 3

        if b == 'X':
            r = lose_response[a]
        elif b == 'Y':
            r = draw_response[a]
            part2 += 3
        elif b == 'Z':
            r = win_response[a]
            part2 += 6
        part2 += score[r]

    print('part1', part1)
    print('part2', part2)
