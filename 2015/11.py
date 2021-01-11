#!/usr/bin/env python3

import re
from string import ascii_lowercase

triples = [ascii_lowercase[i:i + 3] for i in range(24)]
same_char_twice = re.compile(r'(\w)\1')  # back-referenced regex


def password_is_valid(p: str):
    if len(p) != 8:
        # print("length failed")
        return False

    if len(same_char_twice.findall(p)) != 2:
        # print("same char twice - 2 times failed")
        return False

    if 'i' in p or 'l' in p or 'o' in p:
        # print('i l o - failed')
        return False

    for triple in triples:
        if triple in p:
            return True

    # print('no triple')
    return False


def pw2int(p: str):
    assert len(p) == 8
    t = 0
    for i, c in enumerate(p):
        t += 26 ** (7 - i) * (ord(c) - ord('a'))
    return t


def int2pw(i: int):
    p = ''
    for _ in range(8):
        p = chr(i % 26 + ord('a')) + p
        i //= 26
    return p


def next_password(p: str):
    pi = pw2int(p) + 1

    while not password_is_valid(int2pw(pi)):
        pi += 1

    return int2pw(pi)


assert password_is_valid('hijklmmn') is False
assert password_is_valid('abbceffg') is False
assert password_is_valid('abbcegjk') is False
assert password_is_valid('abcdffaa') is True
assert password_is_valid('ghjaabcc') is True

assert next_password('abcdefgh') == 'abcdffaa'

next_pw = next_password('cqjxjnds')
print('part 1', next_pw)
next_pw = next_password(next_pw)
print('part 2', next_pw)
