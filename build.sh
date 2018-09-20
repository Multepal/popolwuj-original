#! /usr/bin/env bash

echo "Applying XSLT to xom-paragraphs.html ..."
xsltproc xom-paragraphs.xsl xom-all-flat-mod-pnums.xml > xom-paragraphs.html; 

echo "Applying replacements ..."
./xom-paragraphs.py

echo "Done."