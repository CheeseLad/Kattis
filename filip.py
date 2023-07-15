#!/usr/bin/env python3

lines = input().split()

linea = []
i = len(lines[0]) - 1
while i >= 0:
  linea.append(lines[0][i])
  i = i - 1

lineb = []
i = len(lines[1]) - 1
while i >= 0:
  lineb.append(lines[1][i])
  i = i - 1

if int("".join(linea)) > int("".join(lineb)):
  print(int("".join(linea)))
else:
  print(int("".join(lineb)))