#!/usr/bin/env python3
import copy
import sys
from dataclasses import dataclass, field
from typing import Callable, Optional
from operator import mul, add


@dataclass
class Monkey:
    id: int
    items: list[int]
    op: Callable[[int], int]
    test: int
    true: int
    false: int

    next_items: Optional[list[int]] = field(default_factory=list)
    inspected: int = 0


def create_lambda(o: list[str]) -> Callable[[int], int]:
    op = mul if o[1] == '*' else add

    if o[2] == 'old':
        return lambda operand, _op=op: _op(operand, operand)
    else:
        return lambda operand, _op=op, b=int(o[2]): _op(operand, b)


if __name__ == "__main__":
    C = open(sys.argv[1] if len(sys.argv) > 1 else '11-input').read().splitlines()

    monkeys = []
    while C:
        m, i, o, t, T, F, *_ = map(str.split, C[0:7])
        C = C[7:]

        M = Monkey(
            int(m[1][:-1]),  # remove :
            list(map(int, [s.replace(',', '') for s in i[2:]])),
            create_lambda(o[3:]),
            int(t[-1]),
            int(T[-1]),
            int(F[-1])
        )
        monkeys += [M]

    product = 1
    for M in monkeys:
        product *= M.test

    for part in [1, 2]:
        local_monkeys = copy.deepcopy(monkeys)
        for r in range(20 if part == 1 else 10000):
            for M in local_monkeys:
                items = M.items
                M.items = []
                for i in items:
                    if part == 1:
                        i = M.op(i) // 3
                    else:
                        i = M.op(i) % product

                    if i % M.test == 0:
                        local_monkeys[M.true].items.append(i)
                    else:
                        local_monkeys[M.false].items.append(i)
                    M.inspected += 1

        r = list(sorted((M.inspected for M in local_monkeys), reverse=True))
        print(f'part{part}', r[0] * r[1])

