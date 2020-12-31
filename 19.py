#!/usr/bin/env python3

from lark import Lark
import re

data = open('19.input').read(30000)

rules, messages = data.split('\n\n')

parser_rules = []
numbers_re = re.compile('(\d+)')

for rule in rules.split('\n'):
    id, dep = rule.split(": ")
    if id == '0':
        id = 'start'
    else:
        # part 2
        if id == '8':
            dep = "42 | 42 8"
        elif id == '11':
            dep = "42 31 | 42 11 31"
        # part 2

        id = f'r{id}'

    parser_rules.append("{}: {}".format(id, numbers_re.sub(r'r\1', dep)))

# print('\n'.join(parser_rules))

parser = Lark('\n'.join(parser_rules))

count = 0
for m in messages.split('\n'):
    m = m.rstrip()
    if len(m) > 0:
        try:
            parser.parse(m)
            print(m, 'ok')
            count += 1
        except:
            pass

print('good messages', count)




