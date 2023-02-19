#!/usr/bin/env python3

n = int(input())
total = 0

for i in range(n):
    s = int(input())
    total = total + s

print(total - (n - 1))