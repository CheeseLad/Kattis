#!/usr/bin/env python3

n = int(input())

words = []

i = 0
while i < n:
  word = input()
  words.append(word)
  i = i + 1

i = 0
while i < len(words):
  print(words[i])
  i = i + 2