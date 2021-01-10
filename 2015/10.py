#!/usr/bin/env python3

import re

same_char_multiple_times = re.compile(r'((\d)\2*)') # back-referenced regex

def look_and_say(i: str, l: int):
    for _ in range(l):
        m = same_char_multiple_times.findall(i)
        i = ''.join([str(len(r[0])) + r[1] for r in m])
    return i

assert look_and_say('1', 5) == '312211'

print('part 1', len(look_and_say('1113122113', 40)))
print('part 2', len(look_and_say('1113122113', 50)))
