#!/usr/bin/env python3

import numpy as np
import re

rotate_re = re.compile(r'^rotate (\w+) (x|y)=(\d+) by (\d+)$')


def transform(screen: np.array, cmd: str):
    if cmd.startswith('rect'):
        col, row = [int(i) for i in cmd.split()[1].split('x')]
        screen[0:row, 0:col] = 1

    elif cmd.startswith('rotate'):
        (type, orientation, index, count) = rotate_re.match(cmd).groups()
        index, count = int(index), int(count)

        if type == 'column':
            screen[:, index] = np.roll(screen[:, index], count)
        elif type == 'row':
            screen[index] = np.roll(screen[index], count)


if __name__ == "__main__":
    # test
    screen = np.zeros((3, 7), dtype=int)
    transform(screen, 'rect 3x2')
    transform(screen, 'rotate column x=1 by 1')
    transform(screen, 'rotate row y=0 by 4')
    transform(screen, 'rotate column x=1 by 1')
    assert str(screen) == '[[0 1 0 0 1 0 1]\n [1 0 1 0 0 0 0]\n [0 1 0 0 0 0 0]]'

    screen = np.zeros((6, 50), dtype=int)

    for l in open('8.input'):
        transform(screen, l.strip())

    print('part1', np.count_nonzero(screen))

    print('part2:')
    for row in screen:
        print(''.join([' ' if i == 0 else '#' for i in row]))
