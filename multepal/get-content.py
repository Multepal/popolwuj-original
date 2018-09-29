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
# Todo: handle this more systematically
os.system(base_path + 'multepal/annotations.py')