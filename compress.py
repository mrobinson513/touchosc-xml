import zlib
import argparse

import lxml.etree as etree
parser = argparse.ArgumentParser(description="A test program.")
parser.add_argument("-f", "--file_name", help="Filename (without extension)", default="temp")
args = parser.parse_args()

my_data = open(args.file_name + ".xml", "rb").read()
compressed_data = zlib.compress(my_data, 2)
output_tosc = open(args.file_name + ".tosc", 'w')
output_tosc.write(compressed_data)
output_tosc.close()
