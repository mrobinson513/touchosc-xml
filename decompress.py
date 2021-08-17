import zlib
import argparse

parser = argparse.ArgumentParser(description="A test program.")
parser.add_argument("-f", "--file_name", help="Filename (without extension)", default="temp")
args = parser.parse_args()
compressed_data = open(args.file_name + ".tosc", "rb").read()
decompressed_data = zlib.decompress(compressed_data)
output_xml = open(args.file_name + ".xml", 'w')
output_xml.write(decompressed_data)
output_xml.close()
