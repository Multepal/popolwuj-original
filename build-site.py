#!/usr/bin/env python

import configparser
from jinja2 import Environment, FileSystemLoader
import glob

# Import config
config = onfig = configparser.ConfigParser()
config.read('./config.ini')
print(config['DEFAULT']['site_title'])

# Open template parser
ENV = Environment(loader=FileSystemLoader('./templates'))

# Convert all templates to pages
for tfile in glob.glob("./templates/*.html"):
    fname = tfile.split('/')[-1]
    if fname == 'base.html':
        continue
    print('Template:', tfile)
    template = ENV.get_template(fname)
    html = template.render(site_title = config['DEFAULT']['site_title'])
    with open(fname, 'w') as pfile:
        pfile.write(html)