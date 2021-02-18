#!/usr/bin/env python3

from hashlib import md5
import re


class KeyGen:
    same_char_3_times = re.compile(r'(.)\1{2}')  # back-referenced regex

    def __init__(self, salt: str):
        self._salt = salt

    def generate(self, distance: int, target: int, md5_extra_loops: int = 0):
        keys = []
        i = 0
        candidates = 0

        pending = []
        while True:
            hash = self._salt + str(i)
            for _ in range(md5_extra_loops + 1):
                hash = md5(hash.encode('utf-8')).hexdigest()

            for p in list(pending):
                if p[1] + distance < i:
                    pending.remove(p)
                else:
                    if p[0] in hash:
                        pending.remove(p)
                        keys.append(hash)
                        print('keys found', len(keys), p[1], i)
                        if len(keys) == target:
                            return p[1]

            result = KeyGen.same_char_3_times.findall(hash)
            if len(result) > 0:
                # print(d, hash, '3', result[0], i)
                pending.append((result[0] * 5, i))
                candidates += 1

            i += 1

        return i, candidates


if __name__ == "__main__":
    # kg = KeyGen('abc')
    # assert kg.generate(1000, 64) == 22728
    # assert kg.generate(1000, 64, 2016) == 22554

    kg = KeyGen('yjdafjpo')
    print('part1', kg.generate(1000, 64))
    print('part2', kg.generate(1000, 65, 2016))
