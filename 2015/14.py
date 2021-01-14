#!/usr/bin/env python3

class Reindeer:
    def __init__(self, name: str, speed: int, dur: int, rest: int):
        self._name = name
        self._speed = speed
        self._dur = dur
        self._rest = rest

    def after(self, seconds: int):
        period = self._dur + self._rest

        dist = seconds // period * self._dur

        r = seconds % period
        if r > self._dur:
            r = self._dur

        dist += r

        return dist * self._speed


reindeers = []

for l in open('14.input').readlines():
    elem = l.rstrip().split(' ')

    reindeers.append(Reindeer(elem[0], int(elem[3]), int(elem[6]), int(elem[13])))

part1 = []
for r in reindeers:
    part1.append(r.after(2503))

print('part 1', max(part1))

part2 = [0] * len(reindeers)

for secs in range(1, 2503 + 1):
    dists = [r.after(secs) for r in reindeers]
    lead_dist = max(dists)

    for leader in [i for i, x in enumerate(dists) if x == lead_dist]:
        part2[leader] += 1

print('part 2', max(part2))
