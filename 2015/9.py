#!/usr/bin/env python3

import networkx as nx

G = nx.Graph()


class Visit:
    def __init__(self, G: nx.Graph):
        self.seen = []
        self.g = G
        self.best_len = sum([G.get_edge_data(*e)['weight'] for e in G.edges])
        self.worst_len = 0

    def find(self, node, length, best):
        # cutoff
        if best:
            if length > self.best_len:
                return

        if len(self.seen) == len(self.g.nodes) - 1:
            if best:
                if self.best_len > length:
                    print('new best len', length, self.seen + [node])
                    self.best_len = length
            else:
                if self.worst_len < length:
                    print('new worst len', length, self.seen + [node])
                    self.worst_len = length
            return

        self.seen.append(node)

        for neighbor in nx.neighbors(self.g, node):
            if neighbor in self.seen:
                continue

            dist = self.g.get_edge_data(node, neighbor)['weight']

            self.find(neighbor, length + dist, best)

        self.seen.remove(node)


for l in open('9.input').readlines():
    items = l.strip().split(' ')
    G.add_edge(items[0], items[2], weight=int(items[4]))

visit = Visit(G)

for n in G.nodes:
    visit.find(n, 0, True)
    visit.find(n, 0, False)

print('part 1', visit.best_len)
print('part 2', visit.worst_len)
