#!/usr/bin/env python

import re
import xml.etree.ElementTree as ET


file = "./annotations.xml"
tree = ET.parse(file)
root = tree.getroot()

data = {}

for note in root.findall('annotation'):
    nid = note.find('nid').text
    content = note.find('content').text
    lines = note.find('lineas').text
    if lines == None:
        continue

    data[nid] = {
        'content': content,
        'lines_raw': lines,
        'lines': {}
    }

    F = C = L = ''
    for item in lines.split('|'):
        tokens = item.split()
        key = tokens[0]
        val = '-'.join(tokens)
        if key in ('Folio', 'Escolio'):
            if val != F:
                F = val
                C = ''
                L = ''
                data[nid]['lines'][F] = {}
                if key == 'Escolio':
                    data[nid]['lines'][F]['X'] = []
        elif key == 'Column':
            if val != C:
                C = val
                L = ''
                data[nid]['lines'][F][C] = []
        elif key == 'Line':
            L = val
            if C == '':
                C = 'X'
            Ln = int(L.split('-')[1])
            data[nid]['lines'][F][C].append('Line-{}'.format(Ln))

for nid in data:
    data[nid]['line_ids'] = []
    for folio in data[nid]['lines']:
        for col in data[nid]['lines'][folio]:
            if len(data[nid]['lines'][folio][col]) == 0:
                lb_id = "{} {}".format(folio, col)
                data[nid]['line_ids'].append(lb_id)
            for line in data[nid]['lines'][folio][col]:
                lb_id = "{} {} {}".format(folio, col, line)
                data[nid]['line_ids'].append(lb_id)

for nid in data:
    for lb_id in data[nid]['line_ids']:
        lb_id = re.sub('Folio-', 'xom-f', lb_id)
        lb_id = re.sub('recto', 's1', lb_id)
        lb_id = re.sub('verso', 's2', lb_id)
        lb_id = re.sub(' Column-A', '-quc', lb_id)
        lb_id = re.sub(' Column-B', '-spa', lb_id)
        lb_id = re.sub(' Line', '', lb_id)
        lb_id = re.sub('Escolio-', 'xom_esc-f', lb_id)
        lb_id = re.sub(' X', '', lb_id)

        print(nid, lb_id)
