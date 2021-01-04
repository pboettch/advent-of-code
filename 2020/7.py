#!/usr/bin/env python3

import re
import networkx as nx

rule_re = re.compile(r'(\d+)? ?(\w+ \w+) bags?')
G = nx.DiGraph()

for rule in open('7.input').readlines():
    rule = rule.rstrip()
    match = rule_re.findall(rule)
    # print(match)

    name = match[0][1]
    G.add_node(name)

    if match[1][1] != 'no other':
        for bag in match[1:]:
            G.add_edge(name, bag[1], amount=int(bag[0]))

count = len(nx.ancestors(G, 'shiny gold'))
print('shiny gold containers', count)

def get_bags(g: nx.DiGraph, node: str):
    count = 1
    for n in g.neighbors(node):
        # print(node, n, g.get_edge_data(node, n)['amount'])
        count += g.get_edge_data(node, n)['amount'] * get_bags(g, n)

    return count

print('bag count', get_bags(G, 'shiny gold') - 1)



# pdot = nx.drawing.nx_pydot.to_pydot(G)
# pdot.write_png('7.png')








