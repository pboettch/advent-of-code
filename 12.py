#!/usr/bin/env python3

from typing import List, Callable

def norm(ang: int):
    while ang < 0:
        ang += 360
    return ang % 360

assert norm(0) == 0
assert norm(360) == 0
assert norm(90) == 90
assert norm(-90) == 270
assert norm(180) == 180

x = 0
y = 0
dir = 0

for instr in open("12.input").readlines():
    cmd = instr[0]
    val = int(instr[1:])

    if cmd == 'N' or (cmd == 'F' and dir == 90):
        y += val
    elif cmd == 'S' or (cmd == 'F' and dir == 270):
        y -= val
    elif cmd == 'E' or (cmd == 'F' and dir == 0):
        x += val
    elif cmd == 'W' or (cmd == 'F' and dir == 180):
        x -= val
    elif cmd == 'R':
        dir -= val
    elif cmd == 'L':
        dir += val
    dir = norm(dir)

print('1', abs(x) + abs(y))

