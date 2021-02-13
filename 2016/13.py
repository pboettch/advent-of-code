#!/usr/bin/env python3

import networkx as nx
from typing import Set, Tuple


def is_wall(xy, wh, magic: int):
    if not (0 <= xy[0] < wh[0] and 0 <= xy[1] < wh[1]):
        return True
    x, y = xy
    t = magic + x * x + 3 * x + 2 * x * y + y + y * y
    return f'{t:b}'.count('1') % 2 == 1


def make_graph(w: int, h: int, magic: int):
    G = nx.Graph()
    total = 0
    for y in range(h):
        for x in range(w):
            n = (x, y)
            # print('#' if is_wall(n, (w, h), magic) else '.', end='')
            if is_wall(n, (w, h), magic):
                continue
            total += 1
            for d in range(-1, 2, 2):
                n2 = (x + d, y)
                if not is_wall(n2, (w, h), magic):
                    G.add_edge(n, n2)
                n2 = (x, y + d)
                if not is_wall(n2, (w, h), magic):
                    G.add_edge(n, n2)
        # print()
    # print(total, len(G.nodes))
    return G


total = set()


def visit(G: nx.Graph,
          pos: Tuple[int, int],
          visited: Set[Tuple[int, int]],
          step: int = 0):
    total.add(pos)
    if step == 50:
        return

    for n in G.neighbors(pos):
        if n in visited:
            continue
        visited.add(n)
        visit(G, n, visited, step + 1)
        visited.remove(n)


if __name__ == "__main__":
    start = (1, 1)

    G = make_graph(10, 7, 10)
    assert len(nx.shortest_path(G, start, (7, 4))) == 12

    G = make_graph(50, 50, 1352)
    print('part1', len(nx.shortest_path(G, start, (31, 39))) - 1)

    visit(G, start, set(start))
    print('part2', len(total))
