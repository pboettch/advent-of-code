#!/usr/bin/env python3

import sys

neigh = dict()


def visit(node: str, paths: list[str], current: str = ''):
    if node == 'end':
        paths += [current]
        return

    if node.islower() and visited[node] == 0:
        return

    visited[node] -= 1

    for n in neigh[node]:
        visit(n, paths, current + node)

    visited[node] += 1


if __name__ == "__main__":

    nodes = set()
    for l in open(sys.argv[1] if len(sys.argv) > 1 else '12-input'):
        a, b = l.strip().split('-')

        nodes.add(a)
        nodes.add(b)

        neigh.setdefault(a, [])
        neigh[a] += [b]

        neigh.setdefault(b, [])
        neigh[b] += [a]

    visited = {n: 1 for n in nodes}

    paths = []
    visit('start', paths)
    part1 = len(paths)

    paths = []
    for twice in nodes - {'start', 'end'}:
        if twice.islower():
            visited[twice] = 2
        visit('start', paths)
        visited[twice] = 1

    part2 = len(set(paths))

    print('part1', part1)
    print('part2', part2)
