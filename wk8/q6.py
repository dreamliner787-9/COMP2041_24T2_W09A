#!/usr/bin/env python3

from glob import glob

total = 0
for filename in glob("*.[ch]"):
    f = open(filename)
    line_count = len(f.readlines())
    total += line_count
    print(f"{line_count:7} {filename}")

print(f"{total:7} total")