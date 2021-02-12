#!/usr/bin/env python3

import re


def bitwise_subset1(num: int, bits: int):
    l = []
    for i in range(0, bits):
        if num & (1 << i):
            l.append(1 << i)
    return l


def bitwise_subset2(num: int, bits: int):
    l = []
    for i in range(0, bits):
        for j in range(i + 1, bits):
            m = (1 << i) | (1 << j)
            if (num & m) == m:
                l.append(m)
    return l


class Floors:
    chip_re = re.compile(r'([a-z]+)-compatible microchip')
    gen_re = re.compile(r'([a-z]+) generator')

    def __init__(self, lines):
        self.material = {}
        self.floors = []

        self.cache = {}

        self.min_step = -1

        microchip = []
        generator = []

        for l in lines:

            map = 0
            for mat in Floors.chip_re.findall(l):
                self.material.setdefault(mat, len(self.material))
                map |= 1 << self.material[mat]
            microchip.append(map)

            map = 0
            for mat in Floors.gen_re.findall(l):
                self.material.setdefault(mat, len(self.material))
                map |= 1 << self.material[mat]
            generator.append(map)

        self.shift = len(self.material)
        assert self.shift <= 7

        for i in range(len(generator)):
            self.floors.append((generator[i] << self.shift) | microchip[i])

        self.full_mask = (1 << self.shift * 2) - 1
        self.mask = (1 << self.shift) - 1

        for i in range(len(self.floors)):
            self.print_floor(i)

        print('{} {:014b} {:07b}'.format(self.shift, self.full_mask, self.mask))

    def print_floor(self, i, s=""):
        print('{}{:014b} ({:07b} {:07b})'.format(s, self.floors[i],
                                                 self.floors[i] >> self.shift,
                                                 self.floors[i] & self.mask))

    def is_stable(self, l: int):
        # no generator or all chips are plugged to their generator and no chip is "floating" with any generator present
        generator = self.floors[l] >> self.shift
        if generator == 0:
            return True

        microchip = self.floors[l] & self.mask
        if (microchip & generator) == microchip:
            return True
        return False

    def id(self):
        id = 0
        for i in range(len(self.floors)):
            id <<= self.shift * 2
            id |= self.floors[i]
        return id

    def solve(self, E: int = 0, step: int = 0):
        id = self.id()
        if id in self.cache and step >= self.cache[id]:
            return

        self.cache[id] = step

        if self.min_step != -1 and step > self.min_step:
            return

        if self.floors[3] == self.full_mask:
            if self.min_step == -1 or self.min_step > step:
                print('new min step', step)
                self.min_step = step

        # get all possible extraction subsets (min 1, max 2)
        subsets_2 = bitwise_subset2(self.floors[E], self.shift * 2)
        subsets_1 = bitwise_subset1(self.floors[E], self.shift * 2)

        if E < 3:
            if not self.move(subsets_2, E, E + 1, step):  # try move of 1 element only no 2-element-move was done
                self.move(subsets_1, E, E + 1, step)

        # if level 0 is empty, do not go back
        if E == 1 and self.floors[0] == 0:
            return

        # if level 1 and 0 are empty, do not go back
        if E == 2 and self.floors[1] == 0 and self.floors[0] == 0:
            return

        if E > 0:
            self.move(subsets_1, E, E - 1, step)

    def move(self, subsets, E, e, step):
        recursed = False
        for subset in subsets:
            orig_floor = self.floors[E]
            self.floors[E] &= ~subset

            if self.is_stable(E):  # removing element leave stable floor
                orig = self.floors[e]

                self.floors[e] |= subset

                if self.is_stable(e):
                    self.solve(e, step + 1)
                    recursed = True

                self.floors[e] = orig

            self.floors[E] = orig_floor

        return recursed


if __name__ == "__main__":
    assert len(bitwise_subset1(int('110011', 2), 6)) == 4
    assert len(bitwise_subset2(int('110011', 2), 6)) == 6

    f = Floors(open('11-ex.input'))

    f.solve()
    assert f.min_step == 11

    f = Floors(open('11.input'))
    f.solve()  # finds but not stops at 31 - or too late

    print('part1', f.min_step, 'cache-size:', len(f.cache))

    f = Floors(open('11-2.input'))
    f.solve()

    print('part2', f.min_step, 'cache-size:', len(f.cache))
