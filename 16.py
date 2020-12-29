#!/usr/bin/env python3

import re
from typing import List


class Field:
    def __init__(self, name, range: List[int]):
        self._r = range
        self._name = name

    def in_range(self, v):
        return self._r[0] <= v <= self._r[1] or self._r[2] <= v <= self._r[3]

    @property
    def name(self):
        return self._name


fields = {}
fields_re = re.compile(r'^([\w ]+): (\d+)-(\d+) or (\d+)-(\d+)$')

nearby_tickets = []

stage = 0
for line in open('16.input').readlines():
    line = line.rstrip()

    if not line:
        continue

    if line == 'your ticket:':
        stage = 1
        continue
    elif line == 'nearby tickets:':
        stage = 2
        continue

    if stage == 0:  # fields
        match = fields_re.match(line)
        fields[match.group(1)] = Field(match.group(1), [int(i) for i in match.groups()[1:]])
    elif stage == 1:
        your_ticket = [int(i) for i in line.split(',')]
    elif stage == 2:
        nearby_tickets.append([int(i) for i in line.split(',')])

# part 1
error_rate = 0
valid_tickets = []
for ticket in nearby_tickets + [your_ticket]:
    valid = True

    for n in ticket:
        ok = False
        for _, r in fields.items():
            if r.in_range(n):
                ok = True
                break
        if not ok:
            valid = False
            error_rate += n

    if valid:
        valid_tickets.append(ticket)
print('error_rate', error_rate)

assert your_ticket in valid_tickets

# part 2

# brute force

# find all possible columns for fields
columns = [[] for _ in range(len(valid_tickets[0]))]
for field, r in fields.items():
    for c in range(len(valid_tickets[0])):
        could_be = True

        # check column of each ticket
        for ticket in valid_tickets:
            if not r.in_range(ticket[c]):
                could_be = False
                break

        if could_be:
            # print(f"{field} could be col {c}")
            columns[c].append(r)

final_columns = ["" for _ in range(len(columns))]

while True:
    assigned = False
    for i, c in enumerate(columns):
        if len(c) == 1:
            field = c[0]
            print('assign', field.name, 'to', i)
            final_columns[i] = field
            for c2 in columns:
                if field in c2:
                    c2.remove(field)
            assigned = True
    if not assigned:
        break

check = 1
for i, field in enumerate(final_columns):
    if field.name.startswith('departure'):
        check *= your_ticket[i]

print('departure product', check)
