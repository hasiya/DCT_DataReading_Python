import json
import dicttoxml
import XML.XML as XML
import xml.etree.ElementTree as ET

def readfile(file):
    try:
        with open(file,'r') as jsonfile:
            file = json.load(jsonfile)
            process(file)
            jsonfile.close()
    except IOError as e:
        print(e)


def process(file):
    xml_s = dicttoxml.dicttoxml(file)
    xml=ET.fromstring(xml_s)
    # root = xml.getroot()
    XML.processFile(xml)

    # for key, value in file.items():
    #     if(isinstance(value,list)):
    #         print("list")
    #     else:
    #         print("not list")
    #
    #
    #     process(value)


if __name__ == "__main__":
    readfile("web.json")
