#!/usr/bin/env python3
import sys

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

words1 = set()
words2 = set()

for word in file1:
    words1.add(word.strip())

for word in file2:
    words2.add(word.strip())

file1.close()
file2.close()

for word in sorted(words1 - words2):
    print(word)