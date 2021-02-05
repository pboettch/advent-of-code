#!/usr/bin/env python3

from hashlib import md5


def find_hash(data: str, work: int, start: int):
    for i in range(start, 100000000):
        d = (data + str(i)).encode('utf-8')
        hash = md5(d).hexdigest()
        if hash.startswith('0' * work):
            return i, hash[5], hash[6]


if __name__ == "__main__":
    assert find_hash('abc', 5, 0) == (3231929, '1', '5')
    assert find_hash('abc', 5, 3231930) == (5017308, '8', 'f')
    assert find_hash('abc', 5, 5017309) == (5278568, 'f', '9')
    assert find_hash('abc', 5, 5278569) == (5357525, '4', 'e')

    id = 'abbhdwsy'
    part1 = ''
    part2 = ' ' * 8
    start = -1
    while len(part1) != 8 or part2.count(' ') > 0:
        start, ch1, ch2 = find_hash(id, 5, start + 1)
        if len(part1) < 8:
            part1 += ch1
            print('part1 next char cracked "{}" - iteration {}'.format(part1, start))

        pos = int(ch1, 16)
        if pos < 8 and part2[pos] == ' ':
            part2 = part2[0:pos] + ch2 + part2[pos + 1:]
            print('part2 next char cracked "{}" - iteration {}'.format(part2, start))

    print('part 1', part1)
    print('part 2', part2)
