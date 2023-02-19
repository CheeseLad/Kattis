#!/usr/bin/env python3

x, y, n = input().split()

for i in range(1, int(n) + 1):
    if i % int(x) == 0 and i % int(y) == 0:
      print("FizzBuzz")
    elif i % int(x) == 0:
      print("Fizz")
    elif i % int(y) == 0:
      print("Buzz")
    else:
      print(i)