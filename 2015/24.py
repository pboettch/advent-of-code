#!/usr/bin/env python3


class C:
    def __init__(self):
        self.min_qe = 9999999999999999
        pass

    def find_minimum_qant_ent(self, target, weights, index=-1, weight=0, qe=1):

        if weight <= target:
            if weight == target:
                if self.min_qe > qe:
                    self.min_qe = qe
            else:
                for i in range(index + 1, len(weights)):
                    weight += weights[i]
                    qe *= weights[i]
                    self.find_minimum_qant_ent(target, weights, i, weight, qe)
                    weight -= weights[i]
                    qe //= weights[i]


if __name__ == "__main__":
    package_weights = list(reversed(sorted([int(w) for w in open('24.input').read(100000).strip().split("\n")])))

    total_weight = sum(package_weights)

    c = C()
    c.find_minimum_qant_ent(total_weight // 3, package_weights)
    part1 = c.min_qe
    print('part1', part1)

    c = C()
    c.find_minimum_qant_ent(total_weight // 4, package_weights)
    part2 = c.min_qe
    print('part2', part2)
