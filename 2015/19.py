#!/usr/bin/env python3

import re

if __name__ == "__main__":

    conversions = {}
    reverse_conversions = {}

    lines = open('19.input').read(100000).split('\n')
    for l in lines:
        if len(l) == 0:
            break
        source, target = l.strip().split(' => ')
        conversions.setdefault(source, [])
        conversions[source].append(target)

        assert target not in reverse_conversions
        reverse_conversions[target] = source

    molecule = lines[-1]

    part1 = set()
    for part, replacements in conversions.items():
        for m in re.finditer(part, molecule):
            for rpl in replacements:
                part1.add(molecule[:m.start()] + rpl + molecule[m.end():])

    print('part1', len(part1))

    part2 = 0
    while molecule != 'e':
        # start with biggest molecule, apparently it's called greedy
        for part in sorted(reverse_conversions.keys(), key=lambda x: len(x), reverse=True):
            rpl = reverse_conversions[part]

            while part in molecule:
                molecule = molecule.replace(part, rpl, 1)
                part2 += 1

        print(molecule, part2)

    print('part2', part2)
