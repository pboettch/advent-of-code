#!/usr/bin/env python3

code_len = 0
str_len = 0
esc_str_len = 0

for l in open('8.input').readlines():
    l = l.strip()

    code_len += len(l)
    s = eval(l)
    str_len += len(s)

    e = '"' + l.replace("\\", "\\\\").replace('"', '\\"') + '"'
    esc_str_len += len(e)

print('part1', code_len - str_len, ",", code_len, str_len)
print('part2', esc_str_len - code_len, ",", esc_str_len, code_len)
