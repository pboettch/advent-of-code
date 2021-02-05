#!/usr/bin/env python3

from string import ascii_lowercase


def is_real_room(room: str):
    e = room.split('-')
    id, checksum = e[-1].split('[')
    cypher = "-".join(e[:-1])
    id = int(id)
    checksum = checksum[:-1]

    occurence = {}

    for c in ascii_lowercase:
        count = cypher.count(c)
        if count > 0:
            occurence.setdefault(count, [])
            occurence[count].append(c)

    our_checksum = "".join(["".join(sorted(occurence[count])) for count in sorted(occurence.keys(), reverse=True)])

    name = ""
    for c in cypher:
        if c == '-':
            name += " "
        else:
            name += ascii_lowercase[(ascii_lowercase.index(c) + id) % len(ascii_lowercase)]

    return checksum == our_checksum[:5], id, name


if __name__ == "__main__":

    assert is_real_room("aaaaa-bbb-z-y-x-123[abxyz]")[0] is True
    assert is_real_room("a-b-c-d-e-f-g-h-987[abcde]")[0] is True
    assert is_real_room("not-a-real-room-404[oarel]")[0] is True
    assert is_real_room("totally-real-room-200[decoy]")[0] is False

    part1 = 0
    part2 = 0

    for l in open('4.input'):
        real, id, name = is_real_room(l.strip())
        if real:
            part1 += id
            if "north" in name:
                part2 = id

    print('part1', part1)
    print('part2', part2)
