#!/usr/bin/env python3

input = open('1.input').read(100000).rstrip()
print('part 1', input.count('(') - input.count(')'))

for i in range(1, len(input)+1):
    if input[:i].count('(') - input[:i].count(')') == -1:
        print('part 2', i)
