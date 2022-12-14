#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    grid = set()

    xs, xe = None, None
    lowest_y = 0  # actually max(y)

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '14-input').read().splitlines():
        P = l.split(' -> ')
        while len(P) > 1:
            a, *P = P
            b = P[0]

            x, y = map(int, a.split(','))
            tx, ty = map(int, b.split(','))

            x, tx = sorted([x, tx])
            y, ty = sorted([y, ty])

            for dx in range(x, tx + 1):
                for dy in range(y, ty + 1):
                    grid.add((dx, dy))
                    lowest_y = max(y, lowest_y)
                    if xs is None:
                        xs = x
                    else:
                        xs = min(x, xs)
                    if xe is None:
                        xe = x
                    else:
                        xe = max(x, xe)


    def dropit(grid) -> int:

        count = 0
        while True:
            x, y = 500, 0  # sand drop

            while True:
                if (x, y) in grid:
                    if (x - 1, y) in grid and (x + 1, y) in grid:
                        y -= 1
                        grid.add((x, y))  # add sand
                        count += 1
                        break

                    if (x - 1, y) in grid:
                        x += 1
                    else:
                        x -= 1

                if y >= lowest_y or (500, 0) in grid:
                    break

                y += 1

            if y >= lowest_y or (500, 0) in grid:
                break

        return count


    print('part1', dropit(grid.copy()))

    # create ground-floor
    for x in range(xs - lowest_y, xe + lowest_y + 1):
        grid.add((x, lowest_y + 2))

    lowest_y += 2

    print('part2', dropit(grid.copy()))
