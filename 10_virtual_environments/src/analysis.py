from lxml import etree


def main():
    xml_data = b"""
    <root>
        <gene id="BRCA1"/>
        <gene id="TP53"/>
    </root>
    """

    xslt_data = b"""
    <xsl:stylesheet version="1.0"
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

        <xsl:template match="/">
            <genes>
                <xsl:for-each select="root/gene">
                    <gene>
                        <xsl:value-of select="@id"/>
                    </gene>
                </xsl:for-each>
            </genes>
        </xsl:template>
    </xsl:stylesheet>
    """

    xml = etree.XML(xml_data)
    xslt = etree.XML(xslt_data)
    transform = etree.XSLT(xslt)

    result = transform(xml)
    print(str(result))


if __name__ == "__main__":
    main()