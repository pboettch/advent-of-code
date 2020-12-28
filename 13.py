#!/usr/bin/env python3

from typing import List

with open("13-adri.input") as f:
    timestamp = int(f.readline())
    bus = [int(x) for x in f.readline().rstrip().replace('x', '0').split(',')]

best = 0
for id in bus:
    if id == 0:
        continue
    bus_time = int(id)

    this = round(timestamp / bus_time + 0.5) * bus_time - timestamp
    if best == 0 or this < best:
        best_id = bus_time
        best = this

print('best bus', best_id, 'diff', best, 'result', best * best_id)


# 2nd part
def find_match(seq: List[int], offset: int = 0):
    clean_seq = {}
    for i, id in enumerate(seq):
        if id != 0:
            clean_seq[i] = id

    step = max(clean_seq.values())
    for index, id in clean_seq.items():
        if id == step:
            break
    t = offset // step * step - index

    count = 0
    print('start', t, 'step', step)

    print(clean_seq)

    while True:
        found = True
        for i, id in clean_seq.items():
            if (t + i) % id != 0:
                found = False
                break

        if found:
            break

        t += step

        count += 1

        if count % 1000000 == 0:
            print(t)

    print('first timestamp t', t, 'iterations', count)
    return t


x = 0
test = {
    1068781: [7, 13, x, x, 59, x, 31, 19],
    3417: [17, x, 13, 19],
    754018: [67, 7, 59, 61],
    779210: [67, x, 7, 59, 61],
    1261476: [67, 7, x, 59, 61],
    1202161486: [1789, 37, 47, 1889],
}

for result, seq in test.items():
    print('testing', result, seq)
    assert find_match(seq) == result

find_match(bus, 210600000000000)
