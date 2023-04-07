#!/usr/bin/env python3

nums = input().split()

nums = [int(n) for n in nums]

nums = sorted(nums)

final = []

letters = input().strip()

for char in letters:
    if char == "A":
        final.append(str(nums[0]))
    elif char == "B":
        final.append(str(nums[1]))
    elif char == "C":
        final.append(str(nums[2]))

print(" ".join(final))