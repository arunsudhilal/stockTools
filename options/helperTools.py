# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 18:27:36 2018

@author: arunks
"""

import json
import csv

def _writeToFile(jsonFile, csvFile):
    f = open(jsonFile)
    data = json.load(f)
    f.close()
    
    f1 = open(csvFile, "wb+")
    f = csv.writer(f1)
    f.writerow(["data__candles__001", "data__candles__002",	"data__candles__003",\
            "data__candles__004", "data__candles__005",	"data__candles__006"])
    data1 = data['data']['candles']
    for x in data1:
        f.writerow([x[0],
                x[1],
                x[2],
                x[3],
                x[4]])
    f1.close()

import glob, os

"""
Convert json downloaded from kite website to csv
"""
def jsonToCsv():
    print "converting all .json to .csv in current directory"
    os.chdir(".")
    jsonList = glob.glob("*.json")

    for jsonFile in jsonList:
        #print(jsonFile)
        csvFile = jsonFile.split('.')[0]
        csvFile +='.csv'
        print jsonFile, csvFile
        _writeToFile(jsonFile, csvFile)

#1 - delta 0.94
#2 - vega 3.0
#3 - theta -1.6
#4 strike -  9900
#5 IV 23.5
#6 LTP 979.55
#7 LTP change % 0.0
#8 OI 0.3
def _toDick(fname, isCE):
    dicti = {}
    with open(fname) as f:
        content = f.readlines()
        # you may also want to remove whitespace characters like `\n` at the end of each line  
    
    content = [x.strip() for x in content]
    count = 1
    for i in content:
        if count == 1:
            delta = i
        elif count == 2:
            vega = i
        elif count == 3:
            theta = i
        elif count == 4:            
            strike = i
            if isCE:
                strike = strike + 'CE'
            else:
                strike = strike + 'PE'
        elif count == 5:
            IV = i
        elif count == 6:
            LTP = i
        elif count == 8:
            if '(' in i:
                OI = i.split('(')[0]
            else:
                OI = i
            
        if count == 8:
            dicti[strike] = [delta, vega, theta, IV, LTP, OI]
            count = 1
            continue
        
        count += 1
        #print i
        
    return dicti

"""
Convert greeks copied from sensibul to dict.
"""        
def greekToDick():
    ceDict =  _toDick('greeks/cal_greeks_9_43.txt', 1)
    peDict = _toDick('greeks/put_greeks_9_43.txt', 0)
        
    for key in sorted(ceDict.iterkeys()):
        if float(ceDict[key][5]) < 10.0:
            continue
        print key, ceDict[key]
        
    for key in sorted(peDict.iterkeys()):
        if float(peDict[key][5]) < 10.0:
            continue
        print key, peDict[key]
    
greekToDick()
    
    
    