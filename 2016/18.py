#!/usr/bin/env python3

def iterate_and_safe_count(line: str, count: int):
    line = [1 if c == '^' else 0 for c in line]

    safe = line.count(0)
    for _ in range(count):
        line = [0, *line, 0]

        n = []
        for i in range(1, len(line) - 1):
            if line[i - 1:i + 2] in [[1, 1, 0], [0, 1, 1], [0, 0, 1], [1, 0, 0]]:
                n.append(1)
            else:
                n.append(0)
        safe += n.count(0)
        line = n

    return safe


if __name__ == "__main__":
    assert iterate_and_safe_count('..^^.', 2) == 6
    assert iterate_and_safe_count('.^^.^.^^^^', 9) == 38

    print('part1', iterate_and_safe_count(
        '.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^', 39))

    print('part2', iterate_and_safe_count(
        '.^^^^^.^^.^^^.^...^..^^.^.^..^^^^^^^^^^..^...^^.^..^^^^..^^^^...^.^.^^^^^^^^....^..^^^^^^.^^^.^^^.^^', 399999))
