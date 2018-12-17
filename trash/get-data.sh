#!/usr/bin/env bash

mv topics.xml topics.xml.tmp
wget http://live-multepal.pantheonsite.io/export/topics.xml;

mv annotations.xml annotations.xml.tmp
wget http://live-multepal.pantheonsite.io/export/annotations.xml;

