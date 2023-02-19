#!/usr/bin/env python3

lines = int(input())
total = 0.0

for i in range(lines):
    n1, n2 = input().split()
    total = total + (float(n1) * float(n2))

print(total)