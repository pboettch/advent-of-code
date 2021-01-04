#!/usr/bin/env python3

import re


def passport(data: str):
    pp = {}
    for e in data.split(' '):
        if len(e) > 0:
            key, value = e.split(':')
            pp.update({key: value})
    return pp


def validate(pp):
    print(pp)
    if not (1920 <= int(pp['byr']) <= 2002):  # byr (Birth Year) - four digits; at least 1920 and at most 2002.
        print('byr fail')
        return False
    if not (2010 <= int(pp['iyr']) <= 2020):  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        print('iyr fail')
        return False
    if not (2020 <= int(pp['eyr']) <= 2030):  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        print('eyr fail')
        return False

    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    if not pp['hgt'][-2:] in ['in', 'cm']:
        print('in or cm failed')
        return False
    if pp['hgt'][-2:] == 'cm' and not (150 <= int(pp['hgt'][0:-2]) <= 193):
        print('cm failed')
        return False
    if pp['hgt'][-2:] == 'in' and not (59 <= int(pp['hgt'][0:-2]) <= 76):
        print('in failed')
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    rgb_re = re.compile('^#[0-9a-f]{6}$')
    if not rgb_re.match(pp['hcl']):
        print('hcl failed')
        return False

    # ecl (Eye Color) - exactly one of:  oth.
    if not pp['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('ecl failed')
        return False

    pid_re = re.compile(r'^\d{9}$')
    if not pid_re.match(pp['pid']):
        print('pid failed')
        return False

    return True


with open('4.input') as f:
    data = ""
    valid = 0
    valid_2 = 0

    for l in f.readlines():
        l = l.rstrip()

        if len(l) == 0 and len(data) != 0:
            pp = passport(data)
            if len(pp) == 8 or (len(pp) == 7 and 'cid' not in pp):
                valid += 1
                if validate(pp):
                    valid_2 += 1
            data = ""
        else:
            data += l + " "
    else:
        if len(data) != 0:
            pp = passport(data)
            if len(pp) == 8 or (len(pp) == 7 and 'cid' not in pp):
                valid += 1
                if validate(pp):
                    valid_2 += 1

    print('valid 1:', valid)
    print('valid 2:', valid_2)
