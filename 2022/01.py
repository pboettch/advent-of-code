#!/usr/bin/env python3

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    elves_calories = []
    for elve in open('01-input').read().split('\n\n'):
        if elve:
            elves_calories += [sum(map(int, elve.split('\n')))]

    elves_calories.sort(reverse=True)

    print('part1', elves_calories[0])
    print('part2', sum(elves_calories[:3]))
