<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="tei">
    <xsl:output method="html" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />

    <xsl:variable name="themes_ajax_root">http://live-multepal.pantheonsite.io/node/</xsl:variable>

    <xsl:param name="fileName" select="'topics.xml'" />
    <xsl:param name="topics" select="document($fileName)" />
    
    <!-- Not sure if this is doing anything -->
    <xsl:strip-space elements="p" /> 

    <xsl:template match="/">

        <xsl:text disable-output-escaping='yes'>{% extends "base.html" %}</xsl:text>
        <xsl:text disable-output-escaping='yes'>{% block content %}</xsl:text>

        <div class="w3-container w3-black">
            <h1>The <i>Popol Wuj</i>: Paragraphs Edition</h1>
            <div class="w3-bar">
                <a href="index.html">Home</a>
            </div>
        </div>

        <xsl:apply-templates select="//tei:text//tei:body"/>

        <div class="w3-container" id="topic-list">
            <div id="topic-box" title="Téma"> </div>
            <xsl:apply-templates select="$topics/topics/topic"/>
        </div>

        <xsl:text disable-output-escaping='yes'>{% endblock %}</xsl:text>
    
    </xsl:template>

    <xsl:template match="tei:div[@xml:lang='quc']">
        <div class="w3-container col quc" xml:lang="quc">
            <b>K'iche'</b>
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tei:div[@xml:lang='spa']">
        <div class="w3-container col spa" xml:lan="spa">
            <b>Castellano</b>
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tei:p">
        <p data-pos="{position()}"><xsl:apply-templates /></p>
    </xsl:template>

    <xsl:template match="tei:lb[@n]">
        <span class="lb" data-n="{@n}">
            <!-- <xsl:value-of select="@n"/> -->
        </span>
    </xsl:template>

    <xsl:template match="tei:lb">
        <span class="lb" data-n="">
            <!-- <xsl:value-of select="@n"/> -->
        </span>
    </xsl:template>

    <xsl:template match="tei:pc">
        <span class="pc">-</span>
    </xsl:template>

    <xsl:template match="tei:pb">
        <button class="pb" data-side="{@xml:id}{@corresp}">
            <xsl:text><!-- &#x25C4; --></xsl:text>
            <xsl:value-of select="@xml:id"/>
            <xsl:value-of select="@corresp"/>
        </button>
    </xsl:template>
    
    <xsl:template match="tei:note">
        <span class="note {@resp} {@place}"><xsl:apply-templates /></span>
    </xsl:template>
    
    <xsl:template match="tei:rs">
        <a class="rs" data-ana="{@ana}" href="#"><xsl:apply-templates /></a>
    </xsl:template>
    
    <xsl:template match="tei:corr">
        <xsl:apply-templates />
    </xsl:template>

    <xsl:template match="tei:hi">
        <span class="hi {@rend}"><xsl:apply-templates /></span>
    </xsl:template>

    <xsl:template match="tei:num">
        <span class="num {@rend}"><xsl:apply-templates /></span>
    </xsl:template>

    <xsl:template match="tei:del">
        <span class="del {@rend}"><xsl:apply-templates /></span>
    </xsl:template>

    <!--
    <xsl:template match="text()">
        <xsl:value-of select="normalize-space()" />
    </xsl:template>
    -->

    <xsl:template match="topic">
        <div class="topic-entry" id="topic-{key}">
            <h2><xsl:value-of select="title" /></h2>
            <a href="{$themes_ajax_root}{nid}" target="_blank">See full record</a>
            <div class="topic-description">
                <xsl:apply-templates select="description" />
            </div>
        </div>
    </xsl:template>

    <xsl:template match="p">
        <p>
            <xsl:apply-templates />
        </p>
    </xsl:template>

    <xsl:template match="a">
        <a href="{@href}" target="{@target}">
            <xsl:apply-templates />
        </a>
    </xsl:template>

    <xsl:template match="img">
        <a href="{@src}" target="_blank">
            <img src="{@src}">
                <xsl:apply-templates />
            </img>
        </a>
    </xsl:template>

</xsl:stylesheet>