#!/usr/bin/env python3

adapters = sorted([int(line) for line in open("10-ex2.input").readlines()])
adapters.append(max(adapters) + 3)  # built-in

current = 0
diffs = {1: 0, 3: 0}

for adapter in adapters:
    diffs[adapter - current] += 1
    current = adapter
print(diffs, 'result', diffs[1] * diffs[3])

combinations = 1

adapters = [0] + adapters

for i in range(len(adapters) - 1):
    comb = 0
    for j in range(i + 1, len(adapters)):
        if adapters[j] <= adapters[i] + 3:
            print(j, adapters[i], '->', adapters[j])
            comb += 1
        else:
            break
    assert comb > 0
    print('   ', comb)
    combinations += comb

print('combinations', combinations)
