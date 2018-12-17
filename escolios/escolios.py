#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import glob

for xmlfile in sorted(glob.glob('./xom-escolios-*.xml')):
    print(xmlfile)
    tree = ET.parse(xmlfile)
    #root = tree.getroot()