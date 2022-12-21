#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    sys.setrecursionlimit(15000)
    part1 = 0
    part2 = 0

    cubes: dict[tuple[int, int, int], int] = {}

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '18-input').read().splitlines():
        x, y, z = map(int, l.split(','))

        sides = 6
        for dx, dy, dz in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            c = (x + dx, y + dy, z + dz)
            if c in cubes:
                sides -= 1
                cubes[c] -= 1

        cubes[(x, y, z)] = sides

    part1 = sum(cubes.values())

    xs, xe = min(c[0] for c in cubes.keys()), max(c[0] for c in cubes.keys())
    ys, ye = min(c[1] for c in cubes.keys()), max(c[1] for c in cubes.keys())
    zs, ze = min(c[2] for c in cubes.keys()), max(c[2] for c in cubes.keys())

    sides = set()
    visited = set()

    delta = 2


    def visit(field, dim):
        visited.add(field)

        # out of field
        if field[0] < dim[0] or field[1] < dim[1] or field[2] < dim[2] or \
                field[0] >= dim[3] or field[1] >= dim[4] or field[2] >= dim[5]:
            return

        for i, (dx, dy, dz) in enumerate([(-1, 0, 0), (1, 0, 0), (0, -1, 0),
                                          (0, 1, 0), (0, 0, -1), (0, 0, 1)]):
            f = (field[0] + dx, field[1] + dy, field[2] + dz)
            if f in cubes:
                sides.add((f, i))
                continue
            if f in visited:
                continue
            visit(f, dim)


    # visit recursively all empty fields and see if there are cube-sides visible
    visit((xs - delta, ys - delta, zs - delta),
          (xs - delta, ys - delta, zs - delta, xe + delta, ye + delta, ze + delta))

    part2 = len(sides)

    print('part1', part1)
    print('part2', part2)
