#!/usr/bin/env python3

import re
import json

numbers = re.compile(r'(-?\d+)')

part1 = 0
for l in open('12.input').readlines():
    for n in numbers.findall(l):
        part1 += int(n)

print('part1', part1)


def dive(item):
    if type(item) is list:
        return sum([dive(i) for i in item])

    elif type(item) is dict:
        if "red" in item.values():
            return 0

        return sum([dive(i) for i in item.values()])

    elif type(item) is int:
        return item
    return 0


book = json.load(open('12.input'))
print('part2', dive(book))
