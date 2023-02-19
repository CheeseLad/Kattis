#!/usr/bin/env python3

cost = float(input())
lines = int(input())
values = 0

i = 0
while i < lines:
  l, w = input().strip().split()
  values = values + (float(l) * float(w))
  i = i + 1

print(values * cost)