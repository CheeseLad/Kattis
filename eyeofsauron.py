#!/usr/bin/env python3

line = input()

left = line.split("(")
right = line.split(")")

left = left[:len(left) - 1]
right = right[1:]

if len(left[0]) == len(right[0]):
    print("correct")
elif len(left[0]) != len(right[0]):
    print("fix")