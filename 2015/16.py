#!/usr/bin/env python3

result = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

part1 = 0
part2 = 0
best_match_count = 0
best_match_count2 = 0
for i, l in enumerate(open('16.input')):
    l = l.rstrip().replace(',', ':').split(': ')
    props = {k: int(v) for k, v in zip(l[1::2], l[2::2])}

    match_count = 0
    for k, v in result.items():
        if k in props and props[k] == v:
            match_count += 1

    if match_count > best_match_count:
        part1 = i + 1
        best_match_count = match_count

    match_count = 0
    for k, v in result.items():
        if k in props:
            if k in ['cats', 'trees']:
                if props[k] > v:
                    match_count += 1
            elif k in ['pomeranians', 'goldfish']:
                if props[k] < v:
                    match_count += 1
            elif props[k] == v:
                match_count += 1

    if match_count > best_match_count2:
        part2 = i + 1
        best_match_count2 = match_count

print('part1', part1)
print('part2', part2)
