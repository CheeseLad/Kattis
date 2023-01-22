#!/usr/bin/env python3

import sys

total = 0
amount = int(input())
numbers = sys.stdin.readline().strip().split()

for i in range(amount):
  total = total + int(numbers[i])

print(total)