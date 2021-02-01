#!/usr/bin/env python3

import numpy as np

if __name__ == "__main__":
    directions = [
        np.array((0, -1)),  # N
        np.array((-1, 0)),  # W
        np.array((0, 1)),  # S
        np.array((1, 0)),  # E
    ]
    direction = 0

    visited = set()

    part1 = np.array((0, 0))
    part2 = None

    instrs = open('1.input').read(10000).strip().split(', ')
    for instr in instrs:
        turn, steps = instr[0], int(instr[1:])

        if turn == 'R':
            direction -= 1
        elif turn == 'L':
            direction += 1
        else:
            raise ValueError('unhandled turn', turn)

        if direction == -1:
            direction = len(directions) - 1
        elif direction == len(directions):
            direction = 0

        for _ in range(steps):
            part1 += directions[direction]
            if (part1[0], part1[1]) in visited and part2 is None:
                part2 = np.copy(part1)
            visited.add((part1[0], part1[1]))

    part1 = np.sum(np.abs(part1))
    part2 = np.sum(np.abs(part2))

    print('part1', part1)
    print('part2', part2)
