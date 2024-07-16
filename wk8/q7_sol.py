#!/usr/bin/env python3

import sys, re, subprocess

for url in sys.argv[1:]:
    process = subprocess.run(f"wget -q -O- {url}", shell=True, capture_output=True, text=True)
    webpage = process.stdout
    for number in re.findall(r'[\d \-]+', webpage):
        number = re.sub(r'\D', '', number)
        if len(number) >= 8 and len(number) <= 15:
            print(number)