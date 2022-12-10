#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    part1 = 0

    X = 1

    code = open(sys.argv[1] if len(sys.argv) > 1 else '10-input').read().splitlines()

    program = []

    # decode instructios
    for l in code:
        i = l.split()

        if i[0] == 'noop':
            program += [('noop')]
        elif i[0] == 'addx':
            program += [('noop'), ('addx', int(i[1]))]

    display = ["" for _ in range(7)]

    cycle_check = 20
    cycle = 0
    # execute
    for i in program:
        cycle += 1

        position = cycle % 40
        if position in (X, X + 1, X + 2):
            pixel = '#'
        else:
            pixel = '.'
        display[(cycle - 1) // 40] += pixel

        if cycle == cycle_check:
            cycle_check += 40
            part1 += X * (cycle)

        if i[0] == 'noop':
            pass
        elif i[0] == 'addx':
            X += i[1]

    print('part1', part1)
    print('\n'.join(display))
