#!/usr/bin/env python3

final = int(input())

num = 0
total = 0
i = 1
while num <= final:
    num = num + (i ** 2)
    i = i + 2
    if num <= final:
        total = total + 1

print(total)