#!/usr/bin/env python3

import sys

n_lines = 10

# check whether we got any arguments:
if len(sys.argv) > 1:
    # check whether the argument starts with a dash like the spec require
    if sys.argv[1][0] == '-':
        # it does start with a dash, convert all the numbers after the dash into an integer
        n_lines = int(sys.argv[1][1:])

n = 1
for line in sys.stdin:
    if n > n_lines:
        break
    else:
        print(line, end='')
    
    # no ++ operator in python
    n += 1