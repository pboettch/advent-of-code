#!/usr/bin/env python3

from typing import List
import functools

with open("13.input") as f:
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

def inv(a: int, m: int):
    m0 = m
    x0 = 0
    x1 = 1

    if m == 1:
        return 0

    # Apply extended Euclid Algorithm
    while a > 1:
        #  q is quotient
        q = a // m

        t = m

        # m is remainder now, process same as
        # euclid's algo
        m = a % m

        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

    #  Make x1 positive
    if x1 < 0:
        x1 += m0

    return x1


def find_match(seq: List[int], offset: int = 0):
    num = []
    rem = []

    for i, n in enumerate(seq):
        if n != 0:
            print('x %', n, '=', n - i)
            num.append(n)
            rem.append(n - i)

    N = functools.reduce(lambda a, b: a * b, num)

    x = 0
    for i in range(len(num)):
        pp = N // num[i]
        x += rem[i] * inv(pp, num[i]) * pp

    print(x, x % N, x / N, N)

    return x % N


x = 0
test = {
    3417: [17, x, 13, 19],
    1068781: [7, 13, x, x, 59, x, 31, 19],
    754018: [67, 7, 59, 61],
    779210: [67, x, 7, 59, 61],
    1261476: [67, 7, x, 59, 61],
    1202161486: [1789, 37, 47, 1889],
}

for result, seq in test.items():
    print('testing', result, seq)
    test_result = find_match(seq)
    if not test_result == result:
        print('failed!')
        break
    else:
        print('ok!')

find_match(bus)
