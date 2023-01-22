#!/usr/bin/env python3

text = input()

tokens = text.split()

r1 = int(tokens[0])
s = int(tokens[1])

print((s * 2) - r1)