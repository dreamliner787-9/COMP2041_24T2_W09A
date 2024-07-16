#!/usr/bin/env python3
from glob import glob

total = 0
for filename in glob("*.[ch]"):
    f_handle = open(filename)
    lines = len(f_handle.readlines())
    print(f"{lines:7} {filename}")
    total += lines

print(f"{total:7} total")