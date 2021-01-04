#!/usr/bin/env python3

from lark import Lark, Transformer, v_args


@v_args(inline=True)  # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, mul
    number = int


part1_parser = Lark(r"""
    ?expr: op
         | expr "+" op   -> add
         | expr "*" op   -> mul
        
    ?op: NUMBER          -> number
       | "(" expr ")"
    
    %import common.NUMBER

    %import common.WS_INLINE
    %ignore WS_INLINE
    """, start='expr', parser='lalr', transformer=CalculateTree())

assert part1_parser.parse('2 * 3 + (4 * 5)') == 26
assert part1_parser.parse('5 + (8 * 3 + 9 + 3 * 4 * 3)') == 437
assert part1_parser.parse('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))') == 12240
assert part1_parser.parse('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632

part1 = 0
for line in open('18.input').readlines():
    line = line.rstrip()
    part1 += part1_parser.parse(line)

print('part1', part1)


