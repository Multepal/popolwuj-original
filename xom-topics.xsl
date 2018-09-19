<?xml version="1.0"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
    xmlns:tei="http://www.tei-c.org/ns/1.0" exclude-result-prefixes="tei">
    <xsl:output method="text" omit-xml-declaration="yes" encoding="UTF-8" indent="no" />
    <xsl:strip-space elements="*"/>

    <xsl:template match="/">
        <xsl:for-each select="//tei:rs">
<xsl:value-of select="position()"/><xsl:text>|</xsl:text>
<xsl:value-of select="."/><xsl:text>|</xsl:text>
<xsl:value-of select="@ana"/><xsl:text>;
</xsl:text>
        </xsl:for-each>
    </xsl:template>

    <xsl:template match="text()">
        <xsl:value-of select="normalize-space()" />
    </xsl:template>

</xsl:stylesheet>