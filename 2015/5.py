#!/usr/bin/env python3

def is_nice1(s: str):
    vowel_count = 0

    for v in 'aeiou':
        vowel_count += s.count(v)

    if vowel_count < 3:
        return False

    prev = None
    two_letters = False
    for c in s:
        if prev is not None and prev == c:
            two_letters = True
            break
        prev = c

    if not two_letters:
        return False

    for f in ['ab', 'cd', 'pq', 'xy']:
        if f in s:
            return False

    return True


def is_nice2(s: str):
    rule = False
    for i in range(0, len(s)):
        token = s[i:i + 2]
        if token in s[i + 2:]:
            rule = True
            break

    if not rule:
        return False

    rule = False
    for i in range(2, len(s)):
        if s[i] == s[i - 2]:
            rule = True
            break

    return rule


assert is_nice1('ugknbfddgicrmopn') is True
assert is_nice1('aaa') is True
assert is_nice1('jchzalrnumimnmhp') is False
assert is_nice1('haegwjzuvuyypxyu') is False
assert is_nice1('dvszwmarrgswjxmb') is False

assert is_nice2('qjhvhtzxzqqjkmpb') is True
assert is_nice2('xxyxx') is True
assert is_nice2('uurcxstgmygtbstg') is False
assert is_nice2('ieodomkazucvgmuy') is False

nice1 = 0
nice2 = 0
for line in open('5.input').readlines():
    if is_nice1(line):
        nice1 += 1
    if is_nice2(line):
        nice2 += 1

print('part 1', nice1)
print('part 2', nice2)
