#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# See if we can do everything with Python

import re
import xml.etree.ElementTree as ET
import configparser 

config = onfig = configparser.ConfigParser()
config.read('./config.ini')

ns = dict(tei="http://www.tei-c.org/ns/1.0")
xom = ET.parse(config['DEFAULT']['xom_src']).getroot()
topics = ET.parse(config['DEFAULT']['topics_src']).getroot()

print("Finind RS instances ...")
for rs in xom.findall('.//tei:rs', ns):
    print(rs.text)

