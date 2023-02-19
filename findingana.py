#!/usr/bin/env python3

s = input()
stop = "0"
for i in range(len(s)):
    if s[i] == "a" and stop == "0":
      j = i
      stop = 1

print(s[j:])