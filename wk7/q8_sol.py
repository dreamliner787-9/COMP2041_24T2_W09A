#! /usr/bin/env python3

import sys

dash_n = False
dash_v = False

if len(sys.argv) == 1:
    sys.argv.append("-")
else:
    while sys.argv[1][0] == '-':
        if sys.argv[1] == "-n":
            dash_n = True
        elif sys.argv[1] == "-v":
            dash_v = True
        
        sys.argv.pop(1)


for filename in sys.argv[1:]:
    i = 1

    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:
            print_line = ""

            if dash_v:
                for char in line:
                    if char == '\n':
                        print_line += f"${char}"
                    elif ord(char) < 32:
                        print_line += f"^{chr(ord(char) + ord('A') - 1)}"
                    else:
                         print_line += f"{char}"
            else:
                print_line = line

            if dash_n:
                print(f"{i:6} {print_line}", end="")
            else:
                print(f"{print_line}", end="")
            i += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
