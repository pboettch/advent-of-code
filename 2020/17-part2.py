#!/usr/bin/env python3

from typing import Dict, Tuple

# dict of tuple: state
grid = {}

y = 0
for line in open('17.input').readlines():
    for x, c in enumerate(line.rstrip()):
        grid[(x, y, 0, 0)] = c
    y += 1


def create_and_count_nbor(grid: Dict[tuple, str],
                          coord: Tuple[int], state: str):
    count = 0

    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            for z in range(coord[2] - 1, coord[2] + 2):
                for w in range(coord[3] - 1, coord[3] + 2):
                    ncoord = (x, y, z, w)
                    if ncoord == coord:
                        continue

                    if ncoord in grid and grid[ncoord] == state:
                        count += 1
    return count


def extend_grid(grid: Dict[tuple, str]):
    w_lim, z_lim, x_lim, y_lim = [0, 0], [0, 0], [0, 0], [0, 0]
    for c in grid.keys():
        if c[0] < x_lim[0]:
            x_lim[0] = c[0]
        if c[0] > x_lim[1]:
            x_lim[1] = c[0]

        if c[1] < y_lim[0]:
            y_lim[0] = c[1]
        if c[1] > y_lim[1]:
            y_lim[1] = c[1]

        if c[2] < z_lim[0]:
            z_lim[0] = c[2]
        if c[2] > z_lim[1]:
            z_lim[1] = c[2]

        if c[3] < w_lim[0]:
            w_lim[0] = c[3]
        if c[3] > w_lim[1]:
            w_lim[1] = c[3]

    print('dimensions', x_lim, y_lim, z_lim, w_lim)

    ngrid = {}
    for x in range(x_lim[0] - 1, x_lim[1] + 2):
        for y in range(y_lim[0] - 1, y_lim[1] + 2):
            for z in range(z_lim[0] - 1, z_lim[1] + 2):
                for w in range(w_lim[0] - 1, w_lim[1] + 2):
                    c = (x, y, z, w)
                    if c in grid:
                        ngrid[c] = grid[c]
                    else:
                        ngrid[c] = '.'
    return ngrid


for _ in range(6):
    grid = extend_grid(grid)
    ngrid = grid.copy()

    for coord, state in grid.items():
        active_nbor_count = create_and_count_nbor(grid, coord, '#')

        if state == '#' and active_nbor_count not in [2, 3]:
            ngrid[coord] = '.'
        elif state == '.' and active_nbor_count == 3:
            ngrid[coord] = '#'

    grid = ngrid

    print(_, 'done')
    # print_slices(grid)

print('part2', sum(v == '#' for v in grid.values()), 'of', len(grid))
