#!/usr/bin/env python3

import re
from typing import List


def has_abba(candidate: str):
    for i in range(0, len(candidate) - 3):
        sub = candidate[i:i + 4]
        if sub[:2] == sub[3:1:-1] and sub[0] != sub[1]:
            return True
    return False


def get_abas(sections: List[str]):
    abas = []
    for section in sections:
        for i in range(0, len(section) - 2):
            sub = section[i:i + 3]
            if sub[0] == sub[2]:
                abas.append(sub)
    return abas


hypernet_re = re.compile(r'\[[a-z]+\]')


def supports_tls(ip: str):
    supernet = hypernet_re.split(ip)
    hypernet = hypernet_re.findall(ip)

    for h in hypernet:
        if has_abba(h):
            return False

    for s in supernet:
        if has_abba(s):
            return True

    return False


def supports_ssl(ip: str):
    supernet = hypernet_re.split(ip)
    hypernet = hypernet_re.findall(ip)

    for aba in get_abas(supernet):
        bab = aba[1] + aba[0] + aba[1]
        for h in hypernet:
            if bab in h:
                return True

    return False


if __name__ == "__main__":
    assert has_abba('a') is False
    assert has_abba('aa') is False
    assert has_abba('aaa') is False
    assert has_abba('aaaa') is False
    assert has_abba('aaaaa') is False
    assert has_abba('aaaaaa') is False
    assert has_abba('abbaaaa') is True
    assert has_abba('aabbaa') is True

    assert supports_tls('abba[mnop]qrst') is True
    assert supports_tls('abcd[bddb]xyyx') is False
    assert supports_tls('aaaa[qwer]tyui') is False
    assert supports_tls('ioxxoj[asdfgh]zxcvbn ') is True

    assert get_abas(['zazbz', 'cbd']) == ['zaz', 'zbz']

    assert supports_ssl('aba[bab]xyz') is True
    assert supports_ssl('xyx[xyx]xyx') is False
    assert supports_ssl('zazbz[bzb]cdb') is True
    assert supports_ssl('aaa[kek]eke') is True

    part1 = 0
    part2 = 0

    for l in open('7.input'):
        if supports_tls(l):
            part1 += 1

        if supports_ssl(l):
            part2 += 1

    print('part1', part1)
    print('part2', part2)
