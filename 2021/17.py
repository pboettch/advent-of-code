#!/usr/bin/env python3

import sys
import numpy as np

if __name__ == "__main__":
    l, = open(sys.argv[1] if len(sys.argv) > 1 else '17-input')
    l = l.strip()[13:]
    x, y = l.split(', ')
    *x, = map(int, x[2:].split('..'))
    *y, = map(int, y[2:].split('..'))

    height = 0
    velocs = 0
    for X in range(int(np.sqrt(x[0])), x[1] + 1):

        for Y in range(-100, 100):
            V = np.array([X, Y])
            P = np.array([0, 0])

            H = 0
            while True:
                P += V

                if P[0] > x[1]:
                    break
                if P[1] < y[1] * 2:
                    break

                H = max(H, P[1])

                V -= 1
                if V[0] < 0:
                    V[0] = 0

                if x[0] <= P[0] <= x[1] and y[0] <= P[1] <= y[1]:
                    if height < H:
                        height = H
                    velocs += 1
                    break

    part1 = height
    part2 = velocs

    print('part1', part1)
    print('part2', part2)
