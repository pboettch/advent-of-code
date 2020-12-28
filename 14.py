#!/usr/bin/env python3

from typing import List

instr = [line.rstrip().split(' = ') for line in open("14.input").readlines()]

mem = {}

mask_1 = 0
mask_0 = 0

for field, value in instr:
    if field.startswith('mem'):
        value = int(value)
        addr = int(field[4:-1])

        mem[addr] = value
        mem[addr] |= mask_1
        mem[addr] &= mask_0
    else:
        mask_1 = int(value.replace('X', '0'), 2)
        mask_0 = int(value.replace('X', '1'), 2)

print('result 1:', sum(mem.values()))


def addr_generator(start: int, mask_str: str):
    x = [35 - i for i, x in enumerate(mask_str) if x == 'X']
    mask_base = int(mask_str.replace('X', '0'), 2)

    # print(x, len(x), f'{mask_base:>036b}', mask_str)

    for mod in range(2 ** len(x)):
        mask_1 = mask_base
        mask_0 = 0

        for i, o in enumerate(x):
            if (mod & (1 << i)) > 0:
                mask_1 |= 1 << o
            else:
                mask_0 |= 1 << o

        addr = start
        addr |= mask_1
        addr &= ~mask_0

        # print(f'{mod:>016b} {mask_1:>036b} {mask_1} {addr}')
        yield addr


# addr_generator(42, '000000000000000000000000000000X1001X')
# addr_generator(26, '00000000000000000000000000000000X0XX')

mem = {}
for field, value in instr:
    if field.startswith('mem'):
        value = int(value)
        addr = int(field[4:-1])

        for a in addr_generator(addr, mask):
            mem[a] = value
    else:
        mask = value

print('result 2:', sum(mem.values()))
