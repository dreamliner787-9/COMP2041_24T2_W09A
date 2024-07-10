#! /usr/bin/env python3

import sys

dash_n = False
dash_v = False

if len(sys.argv) > 1:
    if sys.argv[1] == "-n":
        dash_n = True
    elif sys.argv[1] == "-v":
        dash_v = True
    
    sys.argv.pop(1)

if len(sys.argv) > 1:
    if sys.argv[1] == "-n":
        dash_n = True
    elif sys.argv[1] == "-v":
        dash_v = True
    
    sys.argv.pop(1)

if len(sys.argv) == 1:
    sys.argv.append("-")

for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        i = 1
        for line in stream:
            if dash_v:
                print_line = ""
                for char in line:
                    if ord(char) >= 32:
                        print_line += char
                    elif char == '\n':
                        print_line += f"${char}"
                    else:
                        print_line += f"^{chr(ord(char) + ord('A') - 1)}"
            else:
                print_line = line

            if dash_n == True:
                print(f"{i:6}  {print_line}", end='')
            else:
                print(f"{print_line}", end='')
            i += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")