import xml.etree.ElementTree as ET
from ptyprocess.ptyprocess import FileNotFoundError


def readfile(file):
    try:
        with open(file, 'r') as xmlFile:
            xml = ET.parse(xmlFile)
            # xmlDOM = minidom.parse(xmlFile)
            root = xml.getroot()
            print(root.tag)

            processFile(root)
    except FileNotFoundError as e:
        print(e)


def processFile(root):
    # root = xml.getroot()
    list = root.getchildren()

    if len(list) > 0:
        for child in list:

            attributes = child.attrib
            attriKeys = attributes.keys()

            if str(child.text).isspace():
                if attributes:
                    print child.tag, attributes
                else:
                    print child.tag
            else:
                if attributes:
                    print child.tag, ":", child.text
                    print " ", attributes
                else:
                    print child.tag, ":", child.text

            processFile(child)


if __name__ == "__main__":
    readfile("web.xml")
