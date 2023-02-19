#!/usr/bin/env python3

s = input().split()

set = [1,1,2,2,2,8]

line = [int(n) for n in s]

final = []

for i in range(len(line)):
  final.append(str(set[i] - line[i]))

print(" ".join(final))