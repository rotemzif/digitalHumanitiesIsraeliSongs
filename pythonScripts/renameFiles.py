import sys
import os
import csv
import json


#reload(sys)
#sys.setdefaultencoding('utf-8')
path = 'Lyrics'
#path = os.path.join('final_dotted','newTagged')
xml_data_to_csv = open('MatchNames1.csv', 'w')
Csv_writer = csv.writer(xml_data_to_csv)
#list_head = ["originDir", "originFile", "newDir", "newFile","year"]
#Csv_writer.writerow(list_head)
counter_folder=1
counter_file=1

#with open('merged_file.json') as data_file:
    #data = json.load(data_file)
for root, dirs, files in os.walk(path):            
    for dirname in dirs:
        full_dirname = os.path.join(path, dirname)
        counter_folder+=1
        for filename in os.listdir(full_dirname):
            if not filename.endswith('.xml'): continue
            list_head = []
            list_head.append("{}".format(counter_folder-1))
            list_head.append("{}".format(counter_file))
            #for p in data['songs']:
                #if filename in p['title'] and p['singer']==dirname:
                    #list_head = []
                    #list_head.append(p['year'])
            counter_file+=1
            Csv_writer.writerow(list_head)

xml_data_to_csv.close()


 