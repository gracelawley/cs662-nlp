# Part 1: Reading some data


# called with python 01b_decompress-serialize.py *.xml.gz > deserialized.txt

import gzip, sys, os
from lxml import etree


# get file names and paths
file_names = sys.argv[1:]
file_paths = [os.getcwd() + "/" + file for file in file_names]

# unzip xml files files
xml_files = []
for file in file_paths:
	with gzip.open(file) as f:
		xml_files.append(f.read())


# extract text
text = []
for file in xml_files:
	tree = etree.fromstring(file)
	elements = tree.xpath("//DOC[@type='story']/TEXT/P")
	raw = [x.text for x in elements]
	text = text + raw


# flatten list of strings
joined_text = " ".join(filter(None, text))


print(joined_text)

