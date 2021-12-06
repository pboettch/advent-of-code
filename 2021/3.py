#!/usr/bin/env python3

import numpy as np
import operator

if __name__ == "__main__":
    log = None

    for l in open('3-input'):
        *l, = map(int, l.strip())
        if log is None:
            log = np.ndarray((1, len(l)), dtype=int)
            log[0] = l
        else:
            log = np.vstack([log, l])

    gamma = np.mean(log, axis=0) >= 0.5
    epsilon = np.mean(log, axis=0) <= 0.5

    part1 = int(''.join(np.char.mod('%d', gamma)), 2) * \
            int(''.join(np.char.mod('%d', epsilon)), 2)

    print('part1', part1)


    def filter(log: np.array, most: bool):
        c = 0
        while len(log) != 1 and c < len(log[0]):
            thres = np.mean(log[:, c], axis=0) >= 0.5
            if most:
                log = log[log[:, c] == thres]
            else:
                log = log[log[:, c] != thres]

            c += 1

        assert len(log) == 1

        return int(''.join(np.char.mod('%d', log[0])), 2)


    CO2 = filter(np.copy(log), True)
    O = filter(np.copy(log), False)

    part2 = O * CO2

    print('part2', part2)
