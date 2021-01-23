#!/usr/bin/env python3

from typing import List


class Machine:
    def __init__(self, instr: List[str], a: int = 0, b: int = 0):
        self._regs = {
            'a': a,
            'b': b,
        }
        self._instr = instr
        self._pc = 0

    def execute(self):
        if not 0 <= self._pc < len(self._instr):
            return False

        try:
            op, args = self._instr[self._pc].split(' ', 1)
        except ValueError:
            return False

        jmp = 1
        if op == 'inc':
            self._regs[args] += 1
        elif op == 'hlf':
            self._regs[args] //= 2
        elif op == 'tpl':
            self._regs[args] *= 3
        elif op == 'jmp':
            jmp = int(args)
        elif op.startswith('ji'):
            reg, offset = args.split(', ')
            if op[2] == 'o' and self._regs[reg] == 1:
                jmp = int(offset)
            elif op[2] == 'e' and self._regs[reg] % 2 == 0:
                jmp = int(offset)
        else:
            raise ValueError('invalid instruction')

        self._pc += jmp
        return True

    def reg(self, r):
        return self._regs[r]


if __name__ == "__main__":
    instrs = open('23.input').read(10000).strip().split('\n')
    mach = Machine(instrs)
    while mach.execute():
        pass
    print('part1', mach.reg('a'), mach.reg('b'))

    mach = Machine(instrs, a=1)
    while mach.execute():
        pass
    print('part2', mach.reg('a'), mach.reg('b'))