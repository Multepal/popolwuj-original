#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import pandas as pd

# Create xom-topics.csv
cmd = "xsltproc xom-topics.xsl xom-all-flat-mod-pnums.xml > xom-topics.csv"
import os
os.system(cmd)

bigline = ''
with open('xom-topics.csv', 'r') as xom:
    bigline = ' '.join([line.strip() for line in xom.readlines()])
    bigline = re.sub(r'\s+', ' ', bigline)
    #bigline = re.sub(r'\s*-\s*', '', bigline)

data = []
for line in bigline.split(';'):
    data.append(line.split('|'))
df = pd.DataFrame(data, columns=['count', 'text_seg', 'topic_name'])
df['text_seg'] = df.text_seg.str.replace(' –', '')
df['text_seg'] = df.text_seg.str.strip()
df = df.sort_values(['topic_name','text_seg'])
df[['topic_name', 'text_seg', 'count']].to_csv('xom-topic-index.csv', sep='|', index=False)

df2 = df.groupby(['topic_name', 'text_seg']).count()
df2.to_csv('xom-topic-dict.csv', sep='|', index=True)        

df3 = pd.DataFrame(df.topic_name.unique(), columns=['topic_name'])
df3.index.name = 'topic_id'
df3.to_csv('xom-topic-names.csv', sep='|', index=True)

