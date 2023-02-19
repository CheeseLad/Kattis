#!/usr/bin/env python3

pos = 1

line = input().strip()

for char in line:
    if char == "A":
        if pos == 1:
            pos = 2
        elif pos == 2:
            pos = 1 
    elif char == "B":
        if pos == 2:
            pos = 3
        elif pos == 3:
            pos = 2
    elif char == "C":
        if pos == 3:
            pos = 1
        elif pos == 1:
            pos = 3
print(pos)