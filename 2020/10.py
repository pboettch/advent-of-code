#!/usr/bin/env python3

from typing import List

adapters = sorted([int(line) for line in open("10.input").readlines()])
adapters.append(max(adapters) + 3)  # built-in

current = 0
diffs = {1: 0, 3: 0}

for adapter in adapters:
    diffs[adapter - current] += 1
    current = adapter
print(diffs, 'result', diffs[1] * diffs[3])

cached_total = {}


def use_adapter(index: int, adapters: List[int], path: List[int]):
    if index + 1 == len(adapters):
        # print('comb found', path)
        return 1

    if index in cached_total:
        return cached_total[index]

    total = 0

    current = adapters[index] + 3
    for i in range(index + 1, len(adapters)):
        if adapters[i] <= current:
            total += use_adapter(i, adapters, path + [adapters[i]])

    cached_total[index] = total

    return total


adapters = [0] + adapters

print('combinations', use_adapter(0, adapters, [0]))
for i in sorted(cached_total.keys()):
    print(i, cached_total[i])
