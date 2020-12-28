#!/usr/bin/env python3

from typing import List


def run(code: List[str]):
    pc = 0
    acc = 0

    duplicate = []

    while pc != len(code):
        inst, arg = code[pc].split(' ')
        arg = int(arg)

        if pc in duplicate:
            return False, acc

        duplicate.append(pc)

        if inst == 'nop':
            pass
        elif inst == 'acc':
            acc += arg
        elif inst == 'jmp':
            pc += arg - 1
        else:
            raise ValueError('Illegal instruction', code[pc])
        pc += 1
    return True, acc


code = open("8.input").readlines()
print('acc value', run(code))

new_code = code
for i, instr in enumerate(code):
    if 'nop' in instr:
        new_code[i] = instr.replace('nop', 'jmp')
    elif 'jmp' in instr:
        new_code[i] = instr.replace('jmp', 'nop')

    result, acc = run(new_code)
    if result:
        print('acc value fixed', acc)
        break
    new_code[i] = instr
