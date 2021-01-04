#!/usr/bin/env python3

pos = (0,0)
grid = { pos: 1 }

for p in open('3.input').readline():
    print(p)
    if p == '^':
        pos = (pos[0], pos[1]+1)
    elif p == 'v':
        pos = (pos[0], pos[1]-1)
    elif p == '<':
        pos = (pos[0]-1, pos[1])
    elif p == '>':
        pos = (pos[0]+1, pos[1])
    else:
        continue
    grid.setdefault(pos, 0)
    grid[pos] += 1

print('part 1', len(grid.values()))

positions = [(0,0), (0,0)]
grid = { positions[0]: 1 }

for i, p in enumerate(open('3.input').readline()):
    pos = positions[i % 2]
    if p == '^':
        pos = (pos[0], pos[1]+1)
    elif p == 'v':
        pos = (pos[0], pos[1]-1)
    elif p == '<':
        pos = (pos[0]-1, pos[1])
    elif p == '>':
        pos = (pos[0]+1, pos[1])
    else:
        continue
    grid.setdefault(pos, 0)
    grid[pos] += 1
    positions[i % 2] = pos

print('part 2', len(grid.values()))
