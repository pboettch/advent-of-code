#!/usr/bin/env python3

from typing import List


class CPU:
    def __init__(self):
        self._regs = {
            'a': 0,
            'b': 0,
            'c': 0,
            'd': 0,
        }
        self.pc = 0

    def process(self, i_str: str):
        i = i_str.strip().split()
        if i[0] == 'cpy':
            try:
                v = int(i[1])
            except:
                v = self._regs[i[1]]
            self._regs[i[2]] = v
        elif i[0] == 'inc':
            self._regs[i[1]] += 1
        elif i[0] == 'dec':
            self._regs[i[1]] -= 1
        elif i[0] == 'jnz':
            try:
                v = int(i[1])
            except:
                v = self._regs[i[1]]

            if v != 0:
                self.pc += int(i[2]) - 1
        else:
            raise NotImplementedError('unknown instruction', i_str)
        self.pc += 1

    def execute(self, instrs: List[str]):
        while 0 <= self.pc < len(instrs):
            self.process(instrs[self.pc])

    def reg(self, r: str):
        return self._regs[r]

    def set_reg(self, r: str, v: int):
        self._regs[r] = v


test = [
    'cpy 41 a',
    'inc a',
    'inc a',
    'dec a',
    'jnz a 2',
    'dec a',
]

if __name__ == "__main__":
    # test
    cpu = CPU()
    cpu.execute(test)
    assert cpu.reg('a') == 42

    cpu = CPU()
    cpu.execute(open('12.input').readlines())
    print('part 1', cpu.reg('a'))

    cpu = CPU()
    cpu.set_reg('c', 1)
    cpu.execute(open('12.input').readlines())
    print('part 2', cpu.reg('a'))
