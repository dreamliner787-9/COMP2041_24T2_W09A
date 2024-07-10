#! /usr/bin/env python3

import re

# def main():
line = "it is a nice 42 degrees celcius outside today. I will go out to buy 3 packs of sushi!"

# find the first number with re.search()
match_obj = re.search("[0-9]+", line)
print(f"the first number is ${match_obj.group(0)}")

# find all numbers with re.findall()
print(f"all the numbers are: " + str(re.findall("[0-9]+", line)))

# if __name__ == '__main__':
#     main()