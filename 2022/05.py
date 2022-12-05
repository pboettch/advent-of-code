#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    parse_state = 0

    stacks: list[str] = []
    stacks_p2: list[str] = []

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '05-input'):
        l = l.rstrip()
        if not l:
            continue

        if parse_state == 0:
            box_line = ''.join(l[i:i + 4][1] for i in range(0, len(l), 4))

            if box_line[0] == '1':
                # padding
                max_len = max(len(p) for p in stacks)
                stacks = [line + ' ' * (max_len - len(line)) for line in stacks]
                # rotate
                stacks = list(''.join(p).strip() for p in zip(*stacks[::1]))
                stacks_p2 = stacks[:]

                parse_state = 1
                continue

            stacks += [box_line]
        else:
            count, fro, to = map(int, [p for p in l.split()[1::2]])
            fro -= 1
            to -= 1

            p = stacks[fro][0:count]
            stacks[fro] = stacks[fro][count:]
            stacks[to] = p[::-1] + stacks[to]

            p = stacks_p2[fro][0:count]
            stacks_p2[fro] = stacks_p2[fro][count:]
            stacks_p2[to] = p + stacks_p2[to]

    part1 = ''.join(p[0] for p in stacks)
    part2 = ''.join(p[0] for p in stacks_p2)

    print('part1', part1)
    print('part2', part2)
