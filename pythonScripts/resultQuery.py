import sys
import os
import csv

year_array=["(2008)","(2009)","(2010)","(2011)","(2012)","(2013)","(2014)","(2015)","(2016)"]
last_year_array=["(2000)","(2001)","(2002)","(2003)","(2004)","(2005)","(2006)","(2007)","(1999)"]
last_last_year_array=["(1990)","(1991)","(1992)","(1993)","(1994)","(1995)","(1996)","(1997)","(1998)"]
lineCounter=0
resultCounter = 0
resultCounter1 = 0
resultCounter2 = 0

for line in open("final result/secondLoveFinal.csv"):
    lineCounter+=1
    dist_row = line.split()
    #print(dist_row[0].split(",")[2])
    if dist_row[0].split(",")[2] in year_array:
        resultCounter+=1
    if dist_row[0].split(",")[2] in last_year_array:
        resultCounter1+=1
    if dist_row[0].split(",")[2] in last_last_year_array:
        resultCounter2+=1
    if lineCounter == 1300:
        print("result 2008-2016: ", resultCounter)
        print("result 1999-1007: ", resultCounter1)
        print("result 1990-1998: ", resultCounter2)
        break
