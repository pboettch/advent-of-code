#!/usr/bin/env python3

from typing import List, Callable


def neighbors_1(p: List[List[str]], i: int, j: int):
    c = 0
    for a in range(i - 1, i + 2):
        if a < 0 or a >= len(p):
            continue
        for b in range(j - 1, j + 2):
            if b < 0 or b >= len(p[a]) or (a == i and b == j):
                continue
            if p[a][b] == 'X':
                c += 1
    return c


def neighbors_2(p: List[List[str]], i: int, j: int):
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    def check(dir, a, b):
        while True:
            a += dir[0]
            b += dir[1]
            if a < 0 or a >= len(p) or b < 0 or b >= len(p[0]):
                return False
            if p[a][b] == 'L':
                return False
            if p[a][b] == 'X':
                return True

    c = 0
    for d in directions:
        if check(d, i, j):
            c += 1
    return c


def iterate(p: List[List[str]], count_func: Callable, thres: int):
    np = [['.' for _ in range(len(p[0]))] for _ in range(len(p))]
    changed = False
    for i in range(len(p)):
        for j in range(len(p[i])):
            state = p[i][j]
            if state == '.':
                continue
            neigh_count = count_func(p, i, j)
            if state == 'L' and neigh_count == 0:
                changed = True
                state = 'X'
            elif state == 'X' and neigh_count >= thres:
                changed = True
                state = 'L'
            np[i][j] = state
    return changed, np


def occupation_count(plan: List[str]):
    c = 0
    for row in plan:
        c += row.count('X')
    return c


plan = [list(line.rstrip()) for line in open("11.input").readlines()]

iterations = 0
while True:
    iterations += 1
    changed, plan = iterate(plan, neighbors_1, 4)
    if not changed:
        break

print('1 part: done after', iterations, 'iterations, seats occupied', occupation_count(plan))

plan = [list(line.rstrip()) for line in open("11.input").readlines()]

print('\n'.join([''.join(line) for line in plan]))
iterations = 0
while True:
    iterations += 1
    changed, plan = iterate(plan, neighbors_2, 5)
    # print('after', iterations, 'iterations')
    # print('\n'.join([''.join(line) for line in plan]))
    if not changed:
        break

print('2 part: done after', iterations, 'iterations, seats occupied', occupation_count(plan))
