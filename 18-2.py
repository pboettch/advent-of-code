#!/usr/bin/env python3

from lark import Lark, Transformer, v_args


@v_args(inline=True)  # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, mul
    number = int

part2_parser = Lark(r"""
    ?start: sum
    ?sum: product
        | sum "*" product   -> mul
    ?product: atom
        | product "+" atom  -> add
    ?atom: NUMBER           -> number
         | "(" sum ")"

    %import common.NUMBER

    %import common.WS_INLINE
    %ignore WS_INLINE
    """, start='start', parser='lalr', transformer=CalculateTree())

assert part2_parser.parse('2 * 3 + (4 * 5)') == 46
assert part2_parser.parse('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 1445
assert part2_parser.parse('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 669060
assert part2_parser.parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

part2 = 0
for line in open('18.input').readlines():
    line = line.rstrip()
    part2 += part2_parser.parse(line)

print('part2', part2)


