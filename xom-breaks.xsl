<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="tei">
    <xsl:output method="html" omit-xml-declaration="yes" encoding="UTF-8" indent="yes" />
    <xsl:variable name="themes_ajax_root">http://multepal.spanitalport.virgina.edu/api/temas/</xsl:variable>
    
    <xsl:template match="/">
        <xsl:text disable-output-escaping='yes'>&lt;!DOCTYPE html&gt;
</xsl:text>
        <html>
            <head>
                <title>Popol Vuh, Multepal Edition</title>
                <link rel="stylesheet" type="text/css" href="xom-breaks.css"></link>
                <script src="https://code.jquery.com/jquery-3.3.1.min.js" 
                    integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" 
                    crossorigin="anonymous"></script>
                <script src="xom-breaks.js"></script>
            </head>
            <body>
                <h1>Breaks</h1>
                <xsl:apply-templates select="//tei:text//tei:body"/>
            </body>
        </html>
    </xsl:template>

    <xsl:template match="tei:div[@xml:lang='quc']">
        <div class="col quc" xml:lang="quc">
            <b>K'iche'</b>
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tei:div[@xml:lang='spa']">
        <div class="col spa" xml:lan="spa">
            <b>Espanol</b>
            <xsl:apply-templates />
        </div>
    </xsl:template>

    <xsl:template match="tei:p">
        <span class="pilcrow">¶</span>
        <xsl:apply-templates />
    </xsl:template>
    
    <xsl:template match="tei:note">
        <span class="note {@rend}">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    
    <xsl:template match="tei:rs">
        <span class="rs {@rend}" data-ana="{@ana}">
            <xsl:apply-templates />
        </span>
    </xsl:template>
    
    <xsl:template match="tei:corr">
        <span class="corr">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="tei:lb">
        <br class="lb break"/><span class="lb-num break {@rend}">
            <xsl:value-of select="@n" />
        </span>
    </xsl:template>
    
    <xsl:template match="tei:pc">
        <span class="pc break">
            <xsl:apply-templates />
        </span>
    </xsl:template>
        
    <xsl:template match="tei:pb">
        <hr />
        <div class="pb break" name="{@xml:id}{@corresp}">
            <a href="facsimiles/{@xml:id}{@corresp}.jpg" target="_blank">
                <xsl:value-of select="@xml:id"/><xsl:value-of select="@corresp"/>
            </a>
        </div>
    </xsl:template>

    <xsl:template match="tei:hi">
        <span class="hi {@rend}">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="tei:num">
        <span class="num {@rend}">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="tei:del">
        <span class="del {@rend}">
            <xsl:apply-templates />
        </span>
    </xsl:template>

    <xsl:template match="tei:corr">
        <span class="corr {@rend}">
            <xsl:apply-templates />
        </span>
    </xsl:template>


</xsl:stylesheet>