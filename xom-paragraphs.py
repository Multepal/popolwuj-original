#! /usr/bin/env python

import re
import sys

if sys.argv[1]:
    src_file = sys.argv[1]
else:
    src_file = "xom-paragraphs.html"
print('src_file:', src_file)

subs = [
    ('ꜩ', 'tz'),
    ('Ꜩ', 'TZ'),
    ('ꜫ', "q'")
]

bigline = ''
with open(src_file, 'r') as xom:
    bigline = ' '.join([line.strip() for line in xom.readlines()])
    bigline = re.sub(r'\s+', ' ', bigline)
    bigline = re.sub(r'- ', '', bigline)
    for sub in subs:
        bigline = re.sub(sub[0], sub[1], bigline)

    # THIS IS WHERE YOU CAN ADD THE SEMANTIC MARKUP

with open(src_file, 'w') as xom:
    xom.write(bigline)

print("Done with", src_file)