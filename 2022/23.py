#!/usr/bin/env python3

import sys


def dim(E: set[tuple[int, int]]) -> tuple[int, int, int, int]:
    return min(e[0] for e in E), min(e[1] for e in E), max(e[0] for e in E), max(e[1] for e in E)


def draw(E: set[tuple[int, int]]) -> None:
    min_r, min_c, max_r, max_c = dim(E)

    for r in range(min_r, max_r + 1):
        for c in range(min_c, max_c + 1):
            print(end='#' if (r, c) in E else '.')
        print()


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    elves = set()

    directions = [
        [(-1, 0), (-1, 1), (-1, -1)],  # N, NE, NW
        [(1, 0), (1, 1), (1, -1)],  # S, SE, SW

        [(0, -1), (-1, -1), (1, -1)],  # W, NW, NE
        [(0, 1), (-1, 1), (1, 1)],  # E, NE, SE
    ]

    for ri, r in enumerate(open(sys.argv[1] if len(sys.argv) > 1 else '23-input').read().splitlines()):
        for ci, c in enumerate(r):
            if c == '#':
                elves.add((ri, ci))

    R = 0
    while True:
        R += 1
        new_position: dict[tuple[int, int], list[tuple]] = {}  # new_pos: (list of old pos)

        # calculate new positions
        for e in elves:

            free = True
            for rr in range(-1, 2, 1):
                for cc in range(-1, 2, 1):
                    p = (e[0] + rr, e[1] + cc)
                    if p == e:
                        continue
                    if p in elves:
                        free = False
                        break

                if not free:
                    break
            if free:
                continue

            for d in directions:
                if not any((e[0] + dd[0], e[1] + dd[1]) in elves for dd in d):
                    np = (e[0] + d[0][0], e[1] + d[0][1])

                    new_position.setdefault(np, [])
                    new_position[np].append(e)

                    break

        if len(new_position) == 0:
            break

        # move if same position is not appearing twice or more
        for np, es in new_position.items():
            if len(es) > 1:
                continue
            elves.remove(es[0])
            elves.add(np)

        # rotate directions
        directions = directions[1:] + [directions[0]]

        if R == 10:
            min_r, min_c, max_r, max_c = dim(elves)

            part1 = (max_r - min_r + 1) * (max_c - min_c + 1) - len(elves)
            print('part1', part1)

    print('part2', R)
