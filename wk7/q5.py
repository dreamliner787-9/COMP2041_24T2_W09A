#!/usr/bin/env python3

import sys

n_lines = 10

if len(sys.argv) > 1 and sys.argv[1][0] == '-':
    n_lines = int(sys.argv[1][1:])

i = 0
for line in sys.stdin:
    print(line, end="")
    i += 1
    if i >= n_lines:
        break