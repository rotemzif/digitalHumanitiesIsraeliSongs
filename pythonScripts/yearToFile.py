import sys
import os
import csv
import json
from xml.etree import cElementTree as ET


xml_data_to_csv = open('MatchNames11.csv', 'w')
Csv_writer = csv.writer(xml_data_to_csv)
path = 'Lyrics'
counter_folder=1
counter_file=1
with open('merged_file.json') as data_file:
    data = json.load(data_file)
    for root, dirs, files in os.walk(path):
        for dirname in dirs:
            full_dirname = os.path.join(path, dirname)
            for filename in os.listdir(full_dirname):
                if not filename.endswith('.xml'): continue
                list_head = []
                list_head.append(counter_file)
                for p in data['songs']:
                    if p['singer']==dirname and filename[:-4] in p['title']:
                        list_head.append(p['year'])
                counter_file+=1
                Csv_writer.writerow(list_head)
                
    xml_data_to_csv.close()



            



 