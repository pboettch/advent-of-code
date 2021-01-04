#!/usr/bin/env python3

total_surface = 0
total_ribbon = 0
for line in open('2.input').readlines():
    w, h, l = [int(i) for i in line.split('x')]

    dim_s = sorted([w,h,l])
    total_surface += 2*w*h + 2*w*l + 2*h*l + dim_s[0] * dim_s[1]


    total_ribbon += dim_s[0] * 2 + dim_s[1] * 2 + w * h * l

print('part 1', total_surface)
print('part 2', total_ribbon)
