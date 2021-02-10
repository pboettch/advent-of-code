#!/usr/bin/env python3

from typing import Tuple, List


class Bot:
    part1: int = -1
    compare: Tuple[int] = None

    def __init__(self, id: int):
        self.id = id
        self.chips = []
        self.lo_out_bot = None
        self.hi_out_bot = None

    def output(self):
        assert len(self.chips) <= 2

        if len(self.chips) == 2 and self.lo_out_bot is not None and self.hi_out_bot is not None:
            self.chips = sorted(self.chips)
            if Bot.compare[0] in self.chips and Bot.compare[1] in self.chips:
                print(f'bot {self.id} compares {Bot.compare}')
                Bot.part1 = self.id

            self.lo_out_bot.input(self.chips[0])
            self.hi_out_bot.input(self.chips[1])

            self.chips = []

    def input(self, chip: int):
        self.chips.append(chip)
        self.output()

    def set_lo(self, bot):
        self.lo_out_bot = bot
        self.output()

    def set_hi(self, bot):
        self.hi_out_bot = bot
        self.output()


class Output:
    def __init__(self, id: int):
        self.chips = []
        self.id = id

    def input(self, chip: int):
        self.chips.append(chip)


class Process:
    def __init__(self, compare_element: Tuple[int]):
        self.bots = {}
        self.outputs = {}

        Bot.compare = compare_element

    def process(self, l: List[str]):
        if l[0] == 'value':
            id = int(l[5])
            self.bots.setdefault(id, Bot(id))
            self.bots[id].input(int(l[1]))

        elif l[0] == 'bot':
            id = int(l[1])
            self.bots.setdefault(id, Bot(id))

            lo = int(l[6])
            hi = int(l[11])

            if l[5] == 'bot':
                self.bots.setdefault(lo, Bot(lo))
                lo = self.bots[lo]
            elif l[5] == 'output':
                self.outputs.setdefault(lo, Output(lo))
                lo = self.outputs[lo]

            if l[10] == 'bot':
                self.bots.setdefault(hi, Bot(hi))
                hi = self.bots[hi]
            elif l[10] == 'output':
                self.outputs.setdefault(hi, Output(hi))
                hi = self.outputs[hi]

            self.bots[id].set_lo(lo)
            self.bots[id].set_hi(hi)
        else:
            assert False and "invalid syntax"


if __name__ == "__main__":

    proc = Process((2, 5))

    for l in open('10-ex.input'):
        proc.process(l.strip().split())

    assert Bot.part1 == 2

    proc = Process((17, 61))

    for l in open('10.input'):
        proc.process(l.strip().split())

    print('part1', Bot.part1)
    print('part2', proc.outputs[0].chips[0] * proc.outputs[1].chips[0] * proc.outputs[2].chips[0])
