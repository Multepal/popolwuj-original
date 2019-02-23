#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
from jinja2 import Environment, FileSystemLoader
import glob

# Import config
config = onfig = configparser.ConfigParser()
config.read('./config.ini')

# Open template parser
ENV = Environment(loader=FileSystemLoader('./templates'))

# Define assets -- PUT THESE IN A CONFIG
scripts = dict()
styles = dict()
scripts['index'] = [
    dict(src="assets/jquery-3.3.1.slim.min.js"),
    dict(src="assets/popper.min.js"),
    dict(src="assets/bootstrap.min.js")
]
styles['index'] = [
    dict(href="assets/bootstrap.min.css"),
    dict(href="pw-default.css")
]
scripts['paragraphs'] = [
    dict(src="assets/jquery-3.3.1.slim.min.js"),
    dict(src="assets/popper.min.js"),
    dict(src="assets/bootstrap.min.js"),
    dict(src="./xom-paragraphs.js")
]
styles['paragraphs'] = [
    dict(href="assets/bootstrap.min.css"),
    dict(href="./xom-paragraphs.css")
]
docmap = {
    'index.html': {
        'page_title': 'Home',
        'assets':'index'
    },
    'xom-paragraphs.html': {
        'page_title': 'Paragraphs Version',
        'assets': 'paragraphs'
    }
}

# Convert all templates to pages
for tfile in glob.glob("./templates/*.html"):
    fname = tfile.split('/')[-1]
    if fname == 'base.html':
        continue
    try:
        mapkey = docmap[fname]['assets']
    except KeyError:
        #mapkey = 'default'
        print('{} does not have a docmap entry; skipping.'.format(fname))
        continue
    print(fname, '+', mapkey)
    template = ENV.get_template(fname)
    data = dict(
        site_title = config['DEFAULT']['site_title'],
        page_title = docmap[fname]['page_title'],
        styles = styles[mapkey],
        scripts = scripts[mapkey]
    )
    html = template.render(**data)
    with open(fname, 'w') as pfile:
        pfile.write(html)