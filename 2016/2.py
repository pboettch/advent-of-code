#!/usr/bin/env python3

from typing import List, Callable, Tuple
import numpy as np


def move(pos: np.array, instr: str, pos_valid: Callable):
    v = {
        'L': (-1, 0),
        'R': (1, 0),
        'U': (0, -1),
        'D': (0, 1)
    }
    for m in instr:
        if m in v:
            pos += v[m]
            if not pos_valid(pos):
                pos -= v[m]
    return pos


def key1(pos: np.array):
    return "123456789"[pos[0] + pos[1] * 3]


def position_valid1(pos: np.array):
    if 0 <= pos[0] <= 2 and 0 <= pos[1] <= 2:
        return True
    else:
        return False


def key2(pos: np.array):
    keypad = [
        '  1  ',
        ' 234 ',
        '56789',
        ' ABC ',
        '  D  ',
    ]
    return keypad[pos[1]][pos[0]]


def position_valid2(pos: np.array):
    valid_indices = [
        [2],
        [1, 2, 3],
        [0, 1, 2, 3, 4],
        [1, 2, 3],
        [2],
    ]
    if not 0 <= pos[1] < len(valid_indices):
        return False
    return pos[0] in valid_indices[pos[1]]


def code(instrs: List[str], start: Tuple, key: Callable, position_valid: Callable):
    code = ''
    pos = np.array(start)
    for l in instrs:
        pos = move(pos, l, position_valid)
        code += key(pos)
    return code


if __name__ == "__main__":
    # 0x0 is top left
    assert code(['ULL', 'RRDDD', 'LURDL', 'UUUUD'], (1, 1), key1, position_valid1) == '1985'

    part1 = code(open('2.input').readlines(), (1, 1), key1, position_valid1)

    assert code(['ULL', 'RRDDD', 'LURDL', 'UUUUD'], (0, 2), key2, position_valid2) == '5DB3'
    part2 = code(open('2.input').readlines(), (0, 2), key2, position_valid2)

    print('part1', part1)
    print('part2', part2)
