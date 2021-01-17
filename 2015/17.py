#!/usr/bin/env python3

from typing import List

count_combinations = {}


def f(containers: List[int], target: int, current: int = 0, cont_count: int = 0):
    if target == current:
        global count_combinations
        count_combinations.setdefault(cont_count, 0)
        count_combinations[cont_count] += 1
        print('current solutions:', sum(count_combinations.values()),
                                    min(count_combinations.keys()))
        return 1
    elif current > target:
        return 0

    count = 0
    for i in range(len(containers)):
        count += f(containers[i + 1:], target, current + containers[i], cont_count + 1)
    return count


assert f([20, 15, 10, 5, 5], 25) == 4
assert count_combinations[2] == 3

containers = list(reversed(sorted([int(i) for i in open('super17.input').read(10000).strip().split('\n')])))

count_combinations = {}
part1 = f(containers, 400)

print('part1', part1)

part2 = count_combinations[min(count_combinations.keys())]
print('part2', part2, min(count_combinations.keys()))

