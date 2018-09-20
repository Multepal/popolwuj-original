#! /usr/bin/env bash

echo "Building xom-paragraphs.html . . ."
xsltproc xom-paragraphs.xsl xom-all-flat-mod-pnums.xml > xom-paragraphs.html; 
./xom-paragraphs.py
echo "Done."