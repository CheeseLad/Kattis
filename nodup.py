#!/usr/bin/env python3

line = input().strip()

answer = "yes"

count = {}
line = line.split()
for word in line:
    if word not in count:
        count[word] = 1
    elif word in count:
        count[word] += 1
        answer = "no"

print(answer)