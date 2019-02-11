import sys
import os
from xml.etree import cElementTree as ET

path = 'Lyrics'

for root, dirs, files in os.walk(path):
    for dirname in dirs:

        full_dirname = os.path.join(path, dirname)
        os.makedirs("txtLyrics4/{}".format(dirname))
        for filename in os.listdir(full_dirname):
            if not filename.endswith('.xml'): continue
            fullname = os.path.join(full_dirname, filename)
            
            tree = ET.parse(fullname)
            root = tree.getroot()

                #path for the output files
            
            xml_data_to_txt = open("txtLyrics4/{}/{}.txt".format(dirname, filename[:-4]), "w")
            text = root.find('{http://www.tei-c.org/ns/1.0}text')
            body = text.find('{http://www.tei-c.org/ns/1.0}body')
            lg = body.find('{http://www.tei-c.org/ns/1.0}lg')
            for innerLg in lg.findall('{http://www.tei-c.org/ns/1.0}lg'):

                for line in innerLg.findall('{http://www.tei-c.org/ns/1.0}l'):
                    lineText = line.text
                    newLineText = lineText + '\n'
                    list_head = []
                    list_head.append(newLineText)
                    xml_data_to_txt.write("\n\n".join(list_head).encode('utf-8'))

            xml_data_to_txt.close()


            



 