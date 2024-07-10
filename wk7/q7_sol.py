#! /usr/bin/env python3

import sys

# ORIGINAL:

# if len(sys.argv) == 1:
#     sys.argv.append("-")

# for filename in sys.argv[1:]:
#     try:
#         if filename == "-":
#             stream = sys.stdin
#         else:
#             stream = open(filename)

#         for line in stream:
#             sys.stdout.write(line)

#         if stream != sys.stdin:
#             stream.close()

#     except IOError as e:
#         print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")


# NEW

dash_n = False

if len(sys.argv) == 1:
    sys.argv.append("-")
else:
    if sys.argv[1] == "-n":
        dash_n = True
        sys.argv.pop(1)

for filename in sys.argv[1:]:
    i = 1

    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line in stream:
            if dash_n:
                print(f"{i:6} {line}", end="")
            else:
                print(f"{line}", end="")
            i += 1

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")
