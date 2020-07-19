import sys
import os
import csv

dist = open("timeDayFinal.csv", "w")
Csv_writer = csv.writer(dist)

for line in open("timeDayResult.csv"):
    dist_row = line.split()
    dist_row_1 = line.split()
    for line1 in open("MatchNames11.csv"):
        src_row = line1.split()
        new_row = [dist_row[0].split(',')[0], dist_row[0].split(',')[1]]
        if src_row[0].split(',')[0] == dist_row[0].split(',')[0]:
            if len(src_row[0].split(',')) > 1:
                if src_row[0].split(',')[1] != '0':
                    new_row.append(src_row[0].split(',')[1])
                    Csv_writer.writerow(new_row)
        
dist.close()

