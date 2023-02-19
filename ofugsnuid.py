#!/usr/bin/env python3

lines = int(input())
numbers = []

i = 0
while i < lines:
    numbers.append(int(input()))
    i = i + 1

i = len(numbers) - 1
while i > -1:
    print(numbers[i])
    i = i - 1