#!/usr/bin/env python3

from hashlib import md5


def find_hash(data: str, work: int):
    for i in range(100000000):
        d = (data + str(i)).encode('utf-8')
        if md5(d).hexdigest().startswith('0' * work):
            return i


# assert find_hash('abcdef') == 609043

print('part 1', find_hash('ckczppom', 5))
print('part 2', find_hash('ckczppom', 6))
