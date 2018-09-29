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
    sources = note.find('sources').text
    title = note.find('title').text
    author = note.find('author').text
    if lines == None:
        continue

    data[nid] = {
        'content': content,
        'sources': sources,
        'title': title,
        'lines_raw': lines,
        'lines': {},
        'author': author
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
            if L == val:
                continue
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
    for i, lb_id in enumerate(data[nid]['line_ids']):
        lb_id = re.sub('Folio-', 'xom-f', lb_id)
        lb_id = re.sub('recto', 's1', lb_id)
        lb_id = re.sub('verso', 's2', lb_id)
        lb_id = re.sub(' Column-A', '-quc', lb_id)
        lb_id = re.sub(' Column-B', '-spa', lb_id)
        lb_id = re.sub(' Line', '', lb_id)
        lb_id = re.sub('Escolio-', 'xom_esc-f', lb_id)
        lb_id = re.sub(' X', '', lb_id)
        data[nid]['line_ids'][i] = lb_id

doc = []
doc.append('<?xml version="1.0" encoding="UTF-8"?>')
doc.append("<annotations>")

for nid in data:
    doc.append('\t<annotation nid="{}">'.format(nid))
    doc.append("\t\t<title>{}</title>".format(data[nid]['title']))
    doc.append("\t\t<lines>")
    for line_id in data[nid]['line_ids']:
        doc.append("\t\t\t<line_id>{}</line_id>".format(line_id))
    doc.append("\t\t</lines>")
    doc.append("\t\t<content>{}</content>".format(data[nid]['content']))
    doc.append("\t\t<sources>{}</sources>".format(data[nid]['sources']))
    doc.append("\t\t<author>{}</author>".format(data[nid]['author']))
    doc.append('\t</annotation>')

doc.append("\t<annotation-map>")
for nid in data:
    for line_id in data[nid]['line_ids']:
        doc.append('\t\t<item nid="{}" line_id="{}"/>'.format(nid, line_id))
doc.append("\t</annotation-map>")

doc.append("</annotations>")

with open("annotations.xml", 'w') as out:
    out.write('\n'.join(doc))
