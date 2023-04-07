#!/usr/bin/env python3

lines = int(input())

for i in range(lines):
    nums = input().split()
    other = nums[1:]
    total = 0
    for n in other:
        total = total + int(n)
    print(total - int(nums[0]) + 1)