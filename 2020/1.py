#!/usr/bin/env python3

with open('1.input') as f:
    n = [int(i.rstrip() if len(i) > 1 else 0) for i in f.readlines()]

for i in n:
    for j in n:
        if j + i == 2020:
            print('first:', j * i)
        for k in n:
            if k + j + i == 2020:
                print('second:', j * i * k)
