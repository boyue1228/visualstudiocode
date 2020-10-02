#!/usr/bin/env python3

#./statistic.py query_data.csv > total.csv
#./statistic.py query_data.csv > partiel.csv
import time
import sys
import csv

room = 107374182400
satroom = 53687091200
timeref = 204500000

satransmission = ['2025063','2025053','2025058','2025059','2025070','2025088','2025094','2025100','2025106','2025114','2025138','2025146','2025143','2025138','2027032','2027028','2027029','2027049','2027050','2027041','2027069','2027057','2027058','2027099','2027090','2027074','2027077','2027112','2027108','2027109']

def readCSV(filename):
    data_array =[]
    element={}
    #timeref = 204500000
    with open(filename, newline='\n') as csvfile:
        statreader = csv.reader(csvfile,delimiter=',')
        for row in statreader:
            if not (row is None):
                timestamp = int(row[7][8:])
                matchid = row[4]
                filesize = row[5]
                #if matchid:
                if matchid == '2027058':
                    print("found")
                if matchid and timestamp > timeref:
                    if matchid not in element:
                        element[matchid] = int(filesize)
                    else:
                        tempvalue = int(element[matchid])
                        totalsize = tempvalue + int(filesize)
                        element[matchid] = int(totalsize)
    return element
    #print(element, len(element))

def main(argv):
    statfile = argv[0]
    uclstat = {}
    uclstat  = readCSV(statfile)
    for matchid in uclstat:
        #print("matchid=",matchid, satransmission)
        if matchid in satransmission:
            remainCap = satroom - int(uclstat[matchid])
            print("Sat",matchid,uclstat[matchid],remainCap)
        else:
            remainCap = room - int(uclstat[matchid])
            print("Fib",matchid,uclstat[matchid],remainCap)

if __name__ == "__main__":
    main(sys.argv[1:])
    #print(len(satransmission))