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
scripts['editions'] = [
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
styles['editions'] = [
    dict(href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css",
        integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",
        crossorigin="anonymous"),
    dict(href="pw-default.css")
]
scripts['default'] = [
    dict(src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"),
    dict(src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"),
    dict(src="xom-paragraphs.js")
]
styles['default'] = [
    #dict(href='https://www.w3schools.com/w3css/4/w3.css'),
    dict(href="https://code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css",),
    dict(href="xom-paragraphs.css")
]
docmap = {
    'index.html': {
        'page_title': 'Digital Editions of the Popol Wuj',
        'assets':'editions'
    },
    'xom-paragraphs.html': {
        'page_title': 'DEPW | Paragraphs Edition',
        'assets': 'default'
    },
    'xom-paragraphs.1.html': {
        'page_title': 'DEPW | Paragraphs Edition | Experimental',
        'assets': 'editions'
    }
}

# Convert all templates to pages
for tfile in glob.glob("./templates/*.html"):
    fname = tfile.split('/')[-1]
    if fname == 'base.html':
        continue
    try:
        mapkey = docmap[fname]['assets']
    except IndexError:
        mapkey = 'default'
    print(fname, '+', mapkey)
    template = ENV.get_template(fname)
    data = dict(
        page_title = docmap[fname]['page_title'],
        styles = styles[mapkey],
        scripts = scripts[mapkey]
    )
    html = template.render(**data)
    with open(fname, 'w') as pfile:
        pfile.write(html)