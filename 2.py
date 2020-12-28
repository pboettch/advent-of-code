#!/usr/bin/env python3

import re

good = 0
good_2 = 0

with open('2.input') as f:
    line_re = re.compile(r'^(\d+)\-(\d+) (\w): (\w+)$')
    for l in f.readlines():
        res = line_re.match(l)

        f, t = int(res.group(1)), int(res.group(2))
        letter = res.group(3)
        pw = res.group(4)

        if f <= pw.count(letter) <= t:
            good += 1

        if pw[f - 1] != pw[t - 1] and (pw[f - 1] == letter or pw[t - 1] == letter):
            good_2 += 1

print('good passwords 1', good)
print('good passwords 2', good_2)

