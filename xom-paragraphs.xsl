<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="tei">
    <xsl:output method="html" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />

    <xsl:variable name="themes_ajax_root">http://live-multepal.pantheonsite.io/node/</xsl:variable>

    <xsl:param name="topicsFile" select="'multepal/topics.xml'" />
    <xsl:param name="topics" select="document($topicsFile)" />
    
    <xsl:param name="annotationsFile" select="'multepal/annotations-mod.xml'" />
    <xsl:param name="annotations" select="document($annotationsFile)" />

    <!-- Not sure if this is doing anything -->
    <xsl:strip-space elements="p" /> 

    <!-- Root node: Insert containing page elements -->
    <xsl:template match="/">

        <xsl:text disable-output-escaping='yes'>{% extends "base.html" %}</xsl:text>
        <xsl:text disable-output-escaping='yes'>{% block content %}</xsl:text>

        <!-- Header; may include a menu at some point -->
        <div class="container" id="header">
            <h1 class="text-center">
                <i>Popol Wuj</i><br/><small>Paragraphs and Topics Edition</small>
            </h1>
        </div>

        <!-- Main text viewing area -->
        <div class="container-fluid" id="content">
            <div class="row">
                <xsl:apply-templates select="//tei:text//tei:body"/>
            </div>
        </div>

        <!-- Model box for displaying topic info when segment is selected -->
        <div class="modal" tabindex="-1" role="dialog" id="topic-box" title="Téma">
            <div class="modal-dialog" role="document">
                <div class="modal-content">
                    <div class="modal-header">
                        <h3 class="modal-title">Topic Entry</h3>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&#215;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <p>Modal body text goes here.</p>
                    </div>
                    <div class="modal-footer">
                        <a class="multepal-link btn btn-primary" href="#" target="_blank">See full record</a>
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>

        <div class="container" id="topic-list">
            <xsl:apply-templates select="$topics/topics/topic"/>
        </div>

        <div class="container" id="annotation-list">
            <xsl:apply-templates select="$annotations/annotations/annotation"/>
        </div>
        
        <div class="container text-center mt-3" id="footer">
                <a class="btn btn-primary btn-sm" href="index.html">Return Home</a>
        </div>

        <xsl:text disable-output-escaping='yes'>{% endblock %}</xsl:text>
    
    </xsl:template>

    <xsl:template match="tei:div[@xml:lang='quc']">
        <div class="col quc" xml:lang="quc">    
            <h2 class="text-center">Lado K'iche'</h2>
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tei:div[@xml:lang='spa']">
        <div class="col spa" xml:lan="spa">    
            <h2 class="text-center">Lado Castellano</h2>
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tei:p">
        <p data-pos="{position()}"><xsl:apply-templates /></p>
    </xsl:template>

    <xsl:template match="tei:lb[@n]">
        <xsl:variable name="line_id" select="@id"/>
        <xsl:for-each select="$annotations//annotation-map/item[@line_id = $line_id]">
            <a class="lb" href="#"  title="Annotation for line {@line_id}" data-source-line-id="{$line_id}" data-nid="{@nid}" data-toggle="modal" data-target="#topic-box">
                <sup class="annotation-icon">&#8853;</sup> <!-- 9998 8224 -->
            </a>
        </xsl:for-each>
    </xsl:template>

    <!--
    <xsl:template match="tei:lb">
        <span class="lb" data-n="">
        </span>
    </xsl:template>
    -->

    <xsl:template match="tei:pc">
        <span class="pc">-</span>
    </xsl:template>

    <xsl:template match="tei:pb">
        <span class="pb badge badge-secondary" data-side="{@xml:id}{@corresp}" title="{@xml:id}{@corresp}">
            <xsl:value-of select="@xml:id"/>
            <xsl:value-of select="@corresp"/>
        </span>
    </xsl:template>
    
    <xsl:template match="tei:note">
        <span class="note {@resp} {@place}"><xsl:apply-templates /></span>
    </xsl:template>
    
    <xsl:template match="tei:rs">
        <a class="rs" data-ana="{@ana}" data-toggle="modal" data-target="#topic-box" href="#"><xsl:apply-templates /></a>
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

    <!-- Change this into a data record for use by JQuery, etc. -->
    <xsl:template match="topic">
        <div class="topic-entry" id="topic-{key}">
            <h2 class="topic-title"><xsl:value-of select="title" /></h2>
            <a href="{$themes_ajax_root}{nid}" class="topic-link btn btn-primary btn-sm" target="_blank">See full record</a>
            <div class="topic-type">
                <xsl:value-of select="type"/>
            </div>
            <div class="topic-description">
                <xsl:apply-templates select="description" disable-output-escaping="yes"/>
            </div>
        </div>
    </xsl:template>

    <xsl:template match="annotation">
        <div class="annotation-entry" id="annotation-{@nid}">
            <h2 class="annotation-title"><xsl:value-of select="title" /></h2>
            <a href="{$themes_ajax_root}{@nid}" class="annotation-link btn btn-primary btn-sm" target="_blank">See full record</a>
            <div class="annotation-content">
                <xsl:apply-templates select="content" />
                <div class="annotation-author"><xsl:value-of select="author"/></div>
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