#!/usr/bin/env python3

import sys

row = int(sys.argv[1])
col = int(sys.argv[2])
width = int(sys.argv[3])

for x in range(1, row + 1):
    for y in range(1, col + 1):
        print(f"{x * y:{width}}", end="")
    
    print()