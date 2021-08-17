import argparse

import xml.etree.ElementTree as ET

import argparse
parser = argparse.ArgumentParser(description="Test parsing a TouchOSC XML file.")
parser.add_argument("-f", "--file_name", help="Filename")
args = parser.parse_args()

root = ET.parse(args.file_name).getroot()

pager_root = root.find("./node/children/node/[@type='PAGER']")

print(pager_root.find("./properties/property/key/[.='script']/../value").text)
