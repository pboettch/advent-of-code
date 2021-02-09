#!/usr/bin/env python3

cache = {}


def decompress(input: str, max_level: int = 1, level: int = 0):
    if max_level != -1 and level >= max_level:
        return len(input)

    i = 0
    l = 0
    while i < len(input):
        if input[i] == '(':

            end = input.index(')', i)
            length, count = [int(i) for i in input[i + 1:end].split('x')]
            chunk = input[end + 1:end + 1 + length] * count

            if chunk not in cache:
                chunk_len = decompress(chunk, max_level, level + 1)
                cache[chunk] = chunk_len

            l += cache[chunk]
            i = 1 + end + length
        else:
            l += 1
            i += 1

    return l


if __name__ == "__main__":
    assert decompress('ADVENT') == 6
    assert decompress('A(1x5)BC') == 7
    assert decompress('(3x3)XYZ') == 9
    assert decompress('A(2x2)BCD(2x2)EFG') == 11
    assert decompress('(6x1)(1x3)A') == 6
    assert decompress('X(8x2)(3x3)ABCY') == 18

    compressed = open('9.input').read().strip()
    part1 = decompress(compressed)
    print('part1', part1)

    cache = {}
    part2 = decompress(compressed, -1)
    print('part2', part2, 'cache-size', len(cache))
