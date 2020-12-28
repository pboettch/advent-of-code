#!/usr/bin/env python3

with open("13.input") as f:
    timestamp = int(f.readline())
    bus = [x for x in f.readline().rstrip().split(',')]

best = 0
for id in bus:
    if id == 'x':
        continue
    bus_time = int(id)

    this = round(timestamp / bus_time + 0.5) * bus_time - timestamp
    print(id, this)
    if best == 0 or this < best:
        best_id = bus_time
        best = this

print('best bus', best_id, 'diff', best, 'result', best * best_id)

bus_count = 0
for i, id in enumerate(list(bus)):
    if id != 'x':
        bus[i] = int(id)
        bus_count += 1

step = max([x for x in bus if isinstance(x, int)])
offset = 100000000000000
t = offset // step * step + step - bus.index(step)


count = 0
print('start', t, t / step)
while True:
    ok = 0
    for i, id in enumerate(bus):
        if id == 'x':
            continue

        if (t + i) % id == 0:
            ok += 1
        else:
            break

    if ok == bus_count:
        break

    t += step

    count += 1

    if count % 1000000 == 0:
        print(t)

print('first timestamp t', t, 'iterations', t / step)