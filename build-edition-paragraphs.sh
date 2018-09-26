#! /usr/bin/env bash

echo "Applying XSLT to paragraphs ..."
xsltproc xom-paragraphs.xsl xom-all-flat-mod-pnums-lbids.xml > ./templates/xom-paragraphs.html;

echo "Applying replacements ..."
./xom-paragraphs.py ./templates/xom-paragraphs.html;

echo "Done."