#! /usr/bin/env bash

echo "Add line ids to TEI source ..."
./xom-all-flat-mod-pnums.py;

echo "Applying XSLT to paragraphs ..."
#xsltproc xom-paragraphs.xsl xom-all-flat-mod-pnums-lbids.xml > ./templates/xom-paragraphs.html;
saxon xom-all-flat-mod-pnums-lbids.xml xom-paragraphs.xsl > ./templates/xom-paragraphs.html;

echo "Applying replacements ..."
./xom-paragraphs.py ./templates/xom-paragraphs.html;

echo "Building site ..."
./build-site.py

echo "Done."