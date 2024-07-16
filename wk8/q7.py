#!/usr/bin/env python3

import sys, re, subprocess

url = sys.argv[1]
website = subprocess.run(f"wget -q -O- {url}", shell=True, capture_output=True)
website_content = str(website.stdout)

for possible_phone in re.findall("[0-9 -]+", website_content):
    possible_phone = possible_phone.replace(" ", "")
    possible_phone = possible_phone.replace("-", "")
    if len(possible_phone) >= 8 and len(possible_phone) <= 15:
        # if (not len(possible_phone.strip()) <= 1):
        print(possible_phone.strip())