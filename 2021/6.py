#!/usr/bin/env python3


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    days = [0] * 9

    # fishes = [3, 4, 3, 1, 2]
    *fishes, = map(int, open('6-input').read().split(','))

    for i in fishes:
        days[i] += 1

    for day in range(0, 256):
        days += [0]
        days[day + 7] += days[day]
        days[day + 9] += days[day]
        if day == 79:
            part1 = sum(days[-9:])

        if day == 255:
            part2 = sum(days[-9:])

    print('part1', part1)
    print('part2', part2)
