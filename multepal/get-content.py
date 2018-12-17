#!/usr/bin/env python

import configparser
import requests
import os

config = configparser.ConfigParser()
config.read('../config.ini')

base_path = config['DEFAULT']['base_path']
multepal = config['multepal']['multepal_url']
exports = {'topics':{}, 'annotations':{}, 'snippets':{}}
for export in exports.keys():
    exports[export] = {
        'url': multepal + config['multepal']['{}_url'.format(export)],
        'file': base_path + config['multepal']['{}_src'.format(export)]
    }

for export in exports.keys():
    print("Getting export from Multepal site")
    url = exports[export]['url']
    print(url)
    r = requests.get(url)
    out_file = exports[export]['file']
    if os.path.exists(out_file):
        os.system('mv {0} {0}.tmp'.format(out_file))
    with open(out_file, 'w') as out:
        out.write(r.text)

# Post processing

import re
import xml.etree.ElementTree as ET

file = base_path + "multepal/annotations.xml" # THIS IS IN THE CONFIG
tree = ET.parse(file)
root = tree.getroot()

amap = ET.SubElement(root, 'annotation-map')

def reformat_lb_id(lb_id):
    lb_id = re.sub('Folio-', 'xom-f', lb_id)
    lb_id = re.sub('recto', 's1', lb_id)
    lb_id = re.sub('verso', 's2', lb_id)
    lb_id = re.sub(' Column-A', '-quc', lb_id)
    lb_id = re.sub(' Column-B', '-spa', lb_id)
    lb_id = re.sub(' Line', '', lb_id)
    lb_id = re.sub('Escolio-', 'xom_esc-f', lb_id)
    lb_id = re.sub(' X', '', lb_id)
    return lb_id

for note in root.iter('annotation'): 
    note.set('nid', note.find('nid').text)
    lines = note.find('lineas')
    if lines.text == None:
        continue

    F = C = L = ''
    newlines = {}
    for item in lines.text.split('|'):
        tokens = item.split()
        key = tokens[0]
        val = '-'.join(tokens)
        if key in ('Folio', 'Escolio'):
            if val != F:
                F = val
                C = ''
                L = ''
                newlines[F] = {}
                if key == 'Escolio':
                    newlines[F]['X'] = []
        elif key == 'Column':
            if val != C:
                C = val
                L = ''
                newlines[F][C] = []
        elif key == 'Line':
            if L == val:
                continue
            L = val
            if C == '':
                C = 'X'
            Ln = int(L.split('-')[1])
            newlines[F][C].append('Line-{}'.format(Ln))
            
    newlineids = []            
    for folio in newlines:
        for col in newlines[folio]:
            if len(newlines[folio][col]) == 0:
                lb_id = "{} {}".format(folio, col)
                newlineids.append(reformat_lb_id(lb_id))
            for line in newlines[folio][col]:
                lb_id = "{} {} {}".format(folio, col, line)
                newlineids.append(reformat_lb_id(lb_id))

    #lines.text = ''
    for line_id in newlineids:
        #X = ET.SubElement(lines, 'line_id')
        #X.text = line_id
        Y = ET.SubElement(amap, 'item')
        Y.set('nid', note.find('nid').text)
        Y.set('line_id', line_id)
    lines.set('reformatted','true')

    for el_name in ['nid', 'lineas']:
        el = note.find(el_name)
        note.remove(el)

tree.write(file, method='xml', encoding='utf-8')
