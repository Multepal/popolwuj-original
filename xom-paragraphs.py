import re

subs = [
    ('ꜩ', 'tz'),
    ('Ꜩ', 'TZ'),
    ('ꜫ', "q'")
]

with open('xom-paragraphs.html', 'r') as xom:
    bigline = ' '.join([line.strip() for line in xom.readlines()])
    bigline = re.sub(r'\s+', ' ', bigline)
    bigline = re.sub(r'- ', '', bigline)
    for sub in subs:
        bigline = re.sub(sub[0], sub[1], bigline)

    # THIS IS WHERE YOU CAN ADD THE SEMANTIC MARKUP

with open('xom-paragraphs.html', 'w') as xom:
    xom.write(bigline)

