#!/usr/bin/env python3

def mutate(a: str):
    return a + '0' + a[::-1].translate(str.maketrans('01', '10'))


def checksum(a: str):
    return ''.join('1' if a[i] == a[i + 1] else '0' for i in range(0, len(a), 2))


def process(length: int, a: str):
    while len(a) < length:
        a = mutate(a)
    a = a[0:length]

    c = a
    while True:
        c = checksum(c)
        if len(c) & 1:
            break
    return c


if __name__ == "__main__":
    assert mutate('1') == '100'
    assert mutate('0') == '001'
    assert mutate('11111') == '11111000000'
    assert mutate('111100001010') == '1111000010100101011110000'

    assert process(12, '110010110100') == '100'
    assert process(20, '10000') == '01100'

    part1 = process(272, '01110110101001000')
    print('part1', part1)

    part2 = process(35651584, '01110110101001000')
    print('part2', part2)
