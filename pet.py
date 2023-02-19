#!/usr/bin/env python3

clist = []
final = []

c1 = clist.append(input().strip().split())
c2 = clist.append(input().strip().split())
c3 = clist.append(input().strip().split())
c4 = clist.append(input().strip().split())
c5 = clist.append(input().strip().split())

for people in clist:
  total = 0
  for num in people:
    total = total + int(num)
  
  final.append(total)
  pos = max(final)

print(int(final.index(pos)) + 1, pos)