import sys
import os
from xml.etree import cElementTree as ET
import csv

path = 'Lyrics'
xml_data_to_csv = open('Out.csv', 'w')
Csv_writer = csv.writer(xml_data_to_csv)
for root, dirs, files in os.walk(path):
    for dirname in dirs:
        full_dirname = os.path.join(path, dirname)
        for filename in os.listdir(full_dirname):
            if not filename.endswith('.xml'): continue
            fullname = os.path.join(full_dirname, filename)
            tree = ET.parse(fullname)
            root = tree.getroot()

            teiHeader = root.find('{http://www.tei-c.org/ns/1.0}teiHeader')
            fileDesc = teiHeader.find('{http://www.tei-c.org/ns/1.0}fileDesc')
            publicationStmt = fileDesc.find('{http://www.tei-c.org/ns/1.0}publicationStmt')
            date = publicationStmt.find('{http://www.tei-c.org/ns/1.0}date').text
            list_head = []
            list_head.append(date)
            list_head.append(dirname)
            list_head.append(filename[:-4])
            Csv_writer.writerow(list_head)

xml_data_to_csv.close()


            



 