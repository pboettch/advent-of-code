#!/usr/bin/env python3

import sys
import networkx as nx

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    S = E = None
    C = []
    a_nodes = []
    for i, l in enumerate(open(sys.argv[1] if len(sys.argv) > 1 else '12-input').read().splitlines()):
        if 'S' in l:
            S = (i, l.index('S'))
            l = l.replace('S', 'a')
        if 'E' in l:
            E = (i, l.index('E'))
            l = l.replace('E', 'z')

        C.append([ord(c) - ord('a') for c in l])

    G = nx.DiGraph()

    w = len(C[0])
    h = len(C)
    for y in range(h):
        for x in range(w):
            if C[y][x] == 0:
                a_nodes += [(y, x)]
            for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dx + x < 0 or dx + x >= w or dy + y < 0 or dy + y >= h:
                    continue
                if C[y + dy][x + dx] - C[y][x] <= 1:
                    G.add_edge((y, x), (y + dy, x + dx))

    part1 = nx.dijkstra_path_length(G, S, E)

    for a in a_nodes:
        try:
            p = nx.dijkstra_path_length(G, a, E)
            if part2 == 0 or part2 > p:
                part2 = p
        except:
            pass

    print('part1', part1)
    print('part2', part2)
