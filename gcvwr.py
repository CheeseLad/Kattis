#!/usr/bin/env python3

combined, weight, item_amount = input().split()

combined, weight, item_amount = int(combined), int(weight), int(item_amount)

items = input().split()

total = 0
for i in items:
    total = total + int(i)

print(int(((combined - weight) * 0.9) - total))