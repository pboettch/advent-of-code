#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    part2 = 0

    instrs = {}


    def run(i) -> int:
        if isinstance(i, int):
            return i

        l, op, r = i
        l = run(instrs[l])
        r = run(instrs[r])

        if op == '+': return l + r
        if op == '-': return l - r
        if op == '*': return l * r
        if op == '/': return l / r

        assert False


    for l in open(sys.argv[1] if len(sys.argv) > 1 else '21-input').read().splitlines():
        m, op = l.split(': ')
        try:
            instrs[m] = int(op)
        except:
            a, op, b = op.split(' ')
            instrs[m] = (a, op, b)

            if m == 'root':
                part2_root_instr = (a, '=', b)

    print('part1', run(instrs['root']))

    # part2, trying with approximation

    l, _, r = instrs['root']

    parts = set()

    # find the constant side and direction of side's value depending on humn
    lr1 = run(instrs[l])
    rr1 = run(instrs[r])
    dir = 0
    for i in range(1, 10):
        instrs['humn'] = i
        lr2 = run(instrs[l])
        rr2 = run(instrs[r])

        if lr1 != lr2 and rr1 == rr2:
            if lr1 > lr2:
                dir = -1
            else:
                dir = 1
            parts.add('left')
        elif lr1 == lr2 and rr1 != rr2:
            if rr1 > rr2:
                dir = -1
            else:
                dir = 1
            parts.add('right')
        elif lr1 == lr2 and rr1 == rr2:
            parts.add('nothing')
        else:
            assert False, "Both"

        rr1 = rr2
        lr1 = lr2

    assert 'left' in parts or 'right' in parts

    if 'left' in parts:
        side = l
        target = rr2
    else:
        side = r
        target = lr2

    v = int(2 ** 64)

    instrs['humn'] = v

    while v != 0:
        r = run(instrs[side])
        if r == target:
            break

        v = v // 2
        if r < target:
            instrs['humn'] += v * dir
        else:
            instrs['humn'] -= v * dir

    print('part2', instrs['humn'])
