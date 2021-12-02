#!/usr/bin/env python3


if __name__ == "__main__":
    X, Y, Y2 = 0, 0, 0

    for l in open('2-input'):
        cmd, v = l.strip().split()
        v = int(v)
        if cmd == 'up':
            Y -= v
        elif cmd == 'down':
            Y += v
        elif cmd == 'forward':
            X += v
            Y2 += Y * v

    part1 = X * Y
    part2 = X * Y2

    print('part1', part1)
    print('part2', part2)
