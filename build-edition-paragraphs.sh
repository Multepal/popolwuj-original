#! /usr/bin/env bash

echo "Applying XSLT ..."
xsltproc xom-paragraphs.xsl xom-all-flat-mod-pnums.xml > ./templates/xom-paragraphs.html; 
xsltproc xom-paragraphs.1.xsl xom-all-flat-mod-pnums.xml > ./templates/xom-paragraphs.1.html; 

echo "Applying replacements ..."
./xom-paragraphs.py ./templates/xom-paragraphs.html;
./xom-paragraphs.py ./templates/xom-paragraphs.1.html;

echo "Done."