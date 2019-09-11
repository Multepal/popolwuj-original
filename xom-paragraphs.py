#! /usr/bin/env python3
# -*- coding: utf-8 -*-

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
    
    bigline = ''.join([line.strip() for line in xom.readlines()])
    bigline = re.sub(r'\s+', ' ', bigline)
    bigline = re.sub(r'- ', '', bigline)
    
    # for sub in subs:
    #      bigline = re.sub(sub[0], sub[1], bigline)

    # THIS IS WHERE YOU CAN ADD THE SEMANTIC MARKUP

    # Create labels for page codes
    # bigline = re.sub(r'>xom-f', '>F', bigline)
    # bigline = re.sub(r'-s1<', 'r<', bigline)
    # bigline = re.sub(r'-s2<', 'v<', bigline)
    bigline = re.sub(r'>xom-f(\d+)-s(\d+)<', r'>\1.\2<', bigline)
    bigline = re.sub(r'title="xom-f(\d+)-s(\d)"', r'title="Folio \1, side \2"', bigline)

    # Handle punctuation breaks -- can't figure out how to do this in XSLT
    #bigline = re.sub('__PC__', '', bigline) 
    #bigline = re.sub('__LB__', ' ', bigline)
    bigline = re.sub('__PC____LB__', '', bigline)
    bigline = re.sub(r'__PC__\s*', '', bigline)
    bigline = re.sub('__LB__', ' ', bigline)
    
with open(src_file, 'w') as xom:
    bigline = re.sub(r'<(p|div) ', '\n<' + r'\g<1> ', bigline)
    bigline = re.sub(r'<(p|div) ', r'\n<\g<1> ', bigline)
    xom.write(bigline)

print("Done with", src_file)