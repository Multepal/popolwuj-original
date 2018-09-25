#!/usr/bin/env python

import configparser
from jinja2 import Environment, FileSystemLoader
import glob

# Import config
config = onfig = configparser.ConfigParser()
config.read('./config.ini')

# Open template parser
ENV = Environment(loader=FileSystemLoader('./templates'))


# Define assets -- PUT THESE IN A CONFIG
scripts = dict(default=[], editions=[])
styles = dict(default=[], editions=[])
scripts['index'] = [
    dict(src="https://code.jquery.com/jquery-3.3.1.slim.min.js",
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo",
        crossorigin="anonymous"),
    dict(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49",
        crossorigin="anonymous"),
    dict(src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js",
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy",
        crossorigin="anonymous")
]
styles['index'] = [
    dict(href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
        integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",
        crossorigin="anonymous"),
    dict(href="pw-default.css")
]
scripts['paragraphs'] = [
    dict(src="https://code.jquery.com/jquery-3.3.1.slim.min.js",
        integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo",
        crossorigin="anonymous"),
    dict(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js",
        integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49",
        crossorigin="anonymous"),
    dict(src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js",
        integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy",
        crossorigin="anonymous"),
    dict(src="./xom-paragraphs.js", crossorigin="anonymous")
]
styles['paragraphs'] = [
    dict(href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
        integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",
        crossorigin="anonymous"),
    dict(href="./xom-paragraphs.css", crossorigin="anonymous")
]
docmap = {
    'index.html': {
        'page_title': 'Home',
        'assets':'index'
    },
    'xom-paragraphs.html': {
        'page_title': 'Paragraphs Edition',
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