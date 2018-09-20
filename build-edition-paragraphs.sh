#! /usr/bin/env bash

echo "Applying XSLT to xom-paragraphs.html ..."
xsltproc xom-paragraphs.xsl xom-all-flat-mod-pnums.xml > ./templates/xom-paragraphs.html; 
#xsltproc xom-paragraphs.1.xsl xom-all-flat-mod-pnums.xml > ./templates/xom-paragraphs.html; 

echo "Applying replacements ..."
./xom-paragraphs.py

echo "Done."