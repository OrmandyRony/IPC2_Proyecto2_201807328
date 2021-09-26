import lxml.etree as ET
file = "simulacion_maquina.xml"
dom = ET.parse(file)
xslt = ET.parse(file)
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))