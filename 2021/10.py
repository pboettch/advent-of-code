#!/usr/bin/env python3

import collections

if __name__ == "__main__":
    part1 = 0
    part2 = 0

    C = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }

    P = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }

    P2 = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }

    scores = []

    for l in open('10-input'):
        l = l.strip()

        error = False
        q = collections.deque()
        for c in l:
            if c in C:  # open
                q.append(C[c])
            else:
                exp = q.pop()
                if exp != c:
                    part1 += P[c]
                    # print('syntax error, expected', exp, 'got', c)
                    error = True
                    break
        if error:
            continue

        q.reverse()
        score = 0
        for c in q:
            score = score * 5 + P2[c]
        scores += [score]

    scores.sort()
    part2 = scores[len(scores) // 2]

    print('part1', part1)
    print('part2', part2)
