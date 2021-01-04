#!/usr/bin/env python3

from typing import List


def part1(init: str, turns: int):
    init = [int(x) for x in init.split(',')]
    hist = {x: [y] for y, x in enumerate(init)}

    last_num = init[-1]

    for t in range(len(init), turns):
        if len(hist[last_num]) == 1:
            num = 0
        else:
            num = hist[last_num][-1] - hist[last_num][-2]

        if num not in hist:
            hist[num] = []
        hist[num].append(t)

        last_num = num

        if (t % 10000) == 0:
            print(f"turn {t} {num}")


        if len(hist[num]) > 2:
            hist[num] = hist[num][-2:]


    return num


tests = {
    '0,3,6': 436,
}

for test, result in tests.items():
    assert part1(test, 2020) == result

print('part1:', part1('17,1,3,16,19,0', 2020))
print('part2:', part1('17,1,3,16,19,0', 30000000))
