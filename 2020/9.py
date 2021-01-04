#!/usr/bin/env python3

from typing import List

slice = 25


def find_pair(n: int, nums: List[int]):
    assert len(nums) == slice
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == n:
                return True
    return False


nums = []

fail = 0
for line in open("9.input").readlines():
    n = int(line)
    if len(nums) < slice:
        nums.append(n)
    else:
        if not find_pair(n, nums):
            print('first failed num', n)
            fail = n
            break
        nums = nums[1:] + [n]

nums = []
for line in open("9.input").readlines():
    n = int(line)
    nums.append(n)

    while len(nums) > 1:
        s = sum(nums)
        if s > fail:
            nums = nums[1:]
        elif s == fail:
            print('min/max of series', min(nums) + max(nums))
            break
        else:
            break
