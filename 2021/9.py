#!/usr/bin/env python3


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    caves = []

    for l in open('9-input'):
        caves += [[9, *map(int, list(l.strip())), 9]]

    caves.insert(0, [9] * len(caves[0]))
    caves += [[9] * len(caves[0])]

    low_points = []

    for y in range(1, len(caves) - 1):
        for x in range(1, len(caves[0]) - 1):
            if caves[y][x] < caves[y][x - 1] and \
                    caves[y][x] < caves[y - 1][x] and \
                    caves[y][x] < caves[y][x + 1] and \
                    caves[y][x] < caves[y + 1][x]:
                low_points += [caves[y][x]]

    part1 = sum(p + 1 for p in low_points)


    def detect_basin(x: int, y: int) -> int:
        if caves[y][x] == 9:
            return 0

        if caves[y][x] < 9:
            caves[y][x] = 9
            return 1 + \
                   detect_basin(x + 1, y) + \
                   detect_basin(x, y + 1) + \
                   detect_basin(x, y - 1) + \
                   detect_basin(x - 1, y)


    basin_sizes = []

    for y in range(1, len(caves) - 1):
        for x in range(1, len(caves[0]) - 1):
            size = detect_basin(x, y)
            if size > 0:
                basin_sizes += [size]

    basin_sizes.sort(reverse=True)
    part2 = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    print('part1', part1)
    print('part2', part2)
