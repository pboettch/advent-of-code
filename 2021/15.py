#!/usr/bin/env python3

import sys
sys.setrecursionlimit(15000)
if __name__ == "__main__":
    G = []
    V = []

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '15-input'):
        G += [[*map(int, l.strip())]]
        V += [[False] * len(G[-1])]



    for y in range(len(G)):
        for x in range(len(G[0])):
            if G[y][x] > 6:
                V[y][x] = True




    current_sum = 1275

    def find_path(x, y, P):
        global current_sum
        if current_sum is not None and P >= current_sum:
            return

        if x == len(G[0]) - 1 and y == len(G) - 1:
            if current_sum is None or P < current_sum:
                print("new min:", P, current_sum)
                current_sum = P
            return

        for i in range(4):
            dx = x
            dy = y
            if i == 0:
                dx = x + 1
            elif i == 1:
                dx = x - 1
            elif i == 2:
                dy = y + 1
            elif i == 3:
                dy = y - 1

            if dx < 0 or dx >= len(G[0]):
                continue
            if dy < 0 or dy >= len(G):
                continue
            if V[dy][dx]:
                continue

            V[dy][dx] = True
            find_path(dx, dy, P + G[dy][dx])
            V[dy][dx] = False


    find_path(0, 0, 0)

    part1 = current_sum
    part2 = 0

    print('part1', part1)
    print('part2', part2)
