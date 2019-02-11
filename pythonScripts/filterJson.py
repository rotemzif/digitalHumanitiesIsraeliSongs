import json
import sys
import os
from xml.etree import cElementTree as ET
import csv

path = 'Lyrics'

xml_data_to_csv = open('Out.csv', 'w')
Csv_writer = csv.writer(xml_data_to_csv)

with open('data.json', 'w') as outfile:           
    with open('merged_file.json') as data_file:
        data = json.load(data_file)
        for p in data['songs']:
            if p['year'] != 0:
                list_head = []
                list_head.append(p['year'])
                list_head.append(p['title'].encode('utf-8'))
                list_head.append(p['singer'].encode('utf-8'))
                newData = {'year': p['year'].encode('utf-8'), 'name': p['title'].encode('utf-8'), 'singer': p['singer'].encode('utf-8')}
                json.dump(newData, outfile)
                Csv_writer.writerow(list_head)
xml_data_to_csv.close()

#assuming i have a list of songs with the analytics of the live topic.
# i can print to a file the song name, singer, year and analytics and then sort it by year or by the highest analytics
# 

# ill use the original json and when i will look for specifiec sings i will have the directory name and the file name and i will
# ask, if the p['title'] equals and the p['singer'] equals then check the year.
# if the year is between 2000-2005 then print add the song to the table

# i will run few scripts like this with the different year
                    
                    
