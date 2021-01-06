#!/usr/bin/env python3

import numpy as np
import re

position_re = re.compile('(\d+),(\d+).*?(\d+),(\d+)')


def execute(cmd: str, a: np.array, a2: np.array):
    items = position_re.search(cmd)
    pos1 = (int(items.group(1)), int(items.group(2)))
    pos2 = (int(items.group(3)) + 1, int(items.group(4)) + 1)

    if cmd.startswith('toggle'):
        a[pos1[0]:pos2[0], pos1[1]:pos2[1]] = np.invert(a[pos1[0]:pos2[0], pos1[1]:pos2[1]])
        a2[pos1[0]:pos2[0], pos1[1]:pos2[1]] += 2

    elif cmd.startswith('turn on'):
        a[pos1[0]:pos2[0], pos1[1]:pos2[1]] = True
        a2[pos1[0]:pos2[0], pos1[1]:pos2[1]] += 1

    elif cmd.startswith('turn off'):
        a[pos1[0]:pos2[0], pos1[1]:pos2[1]] = False
        a2[pos1[0]:pos2[0], pos1[1]:pos2[1]] -= 1
        a2[a2 < 0] = 0


a = np.zeros((1000, 1000), bool)
a2 = np.zeros((1000, 1000), int)

for cmd in open('6.input').readlines():
    execute(cmd, a, a2)

print('part 1', np.sum(a == True))
print('part 2', np.sum(a2))
