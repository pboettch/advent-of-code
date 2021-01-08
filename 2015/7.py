#!/usr/bin/env python3

import networkx as nx

G = nx.DiGraph()

if __name__ == '__main__':
    for s in open('7.input').readlines():
        l, r = s.rstrip().split(' -> ')

        op = l.split(' ')
        G.add_node(r)

        if len(op) == 1:
            G.nodes[r]['op'] = 'ASSIGN'
            G.add_edge(r, op[0])

        elif l.startswith('NOT'):
            G.nodes[r]['op'] = 'NOT'
            G.add_edge(r, op[1])

        else:
            G.nodes[r]['op'] = op[1]
            G.add_edge(r, op[0])
            G.add_edge(r, op[2])

    cache = {}


    def f(G: nx.DiGraph, n: str):

        if n in cache:
            return cache[n]

        if 'op' in G.nodes[n]:
            op = G.nodes[n]['op']
        else:
            op = 'LITERAL'

        neigh = list(G.neighbors(n))

        if op == 'LITERAL':
            assert len(list(neigh)) == 0
        elif op == 'ASSIGN' or op == 'NOT':
            assert len(list(neigh)) == 1
        else:
            assert len(list(neigh)) == 2

        if op == 'LITERAL':
            result = int(n)
        if op == 'ASSIGN':
            result = f(G, neigh[0])
        elif op == 'NOT':
            result = ~f(G, neigh[0]) & 0xffff
        elif op == 'AND':
            result = f(G, neigh[0]) & f(G, neigh[1])
        elif op == 'OR':
            result = f(G, neigh[0]) | f(G, neigh[1])
        elif op == 'LSHIFT':
            result = (f(G, neigh[0]) << f(G, neigh[1])) & 0xffff
        elif op == 'RSHIFT':
            result = (f(G, neigh[0]) >> f(G, neigh[1])) & 0xffff

        cache[n] = result

        return result


    part1 = f(G, 'a')
    print('part 1', part1)

    # part1
    G.remove_edge('b', '14146')
    G.add_edge('b', str(part1))

    cache = {}
    part2 = f(G, 'a')
    print('part 2', part2)
