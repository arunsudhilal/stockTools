# -*- coding: utf-8 -*-
"""
Options Trading market tracker.

This script file is useful to track any options pair PL movement w.r.t Nifty.
It plots Nifty's movement from base price. Which can be compared to the net
P/L value of any option pair from a specified entry point.

Varible input to the scripts are,
1. folder - looks for csv files.
2. time - script calculates entry points of options and nifty w.r.t this variable.
3. capital - investement captial. Script uses this to caluclat the position sizes of option entires.

API's available
- plotOptionsCombination(combi) - plots PL charts for all combinations specifed in the combi variable.
- plotNiftyDistance() - plots nifty movement from base.

Pre-requisite: Download the data from kite using chrome devloper options and saved in the folder.
"""

folder = '30/'
time = '2018-11-30T09:55:00+0530'

capital = 40000

import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations 

#calculate average of open and close
def calculateAverage(data):
    data['Av'] = (data['data__candles__002'] + data['data__candles__005']) / 2
    return data[['Av', 'data__candles__001']]

def calculatePL(data1, entryPrice1, size1, data2, entryPrice2, size2):
    data1['value'] = ( data1['Av'] - entryPrice1 ) * size1 + \
                 ( data2['Av'] - entryPrice2 ) * size2 
    return data1[['value', 'data__candles__001']]

def calculateDistance(data, entryPriceNifty):
    data['value'] = data['Av'] - entryPriceNifty
    return data[['value', 'data__candles__001']]

def stripDateAndSetIdex(data):
    data['data__candles__001'] = pd.to_datetime(data['data__candles__001'], format='%Y-%m-%dT%H:%M:%S+0530', utc=True)
    data['Time'] = data['data__candles__001'].dt.strftime("%H:%M")
    data = data[['Time', 'value']]
    data.set_index('Time', inplace=True)
    data.index = pd.to_datetime(data.index)
    return data

def middleRound(x, base=75):
    return int(base *round(float(x)/base))

def drawChart(item, xlabel, ylabel, title):
    plt.figure(figsize = (10,3))
    plt.plot(item, 'b')
    plt.grid(True)
    plt.axis ('tight')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()

def findEntryPriceWithTime(df, time):
    temp = df.loc[df.data__candles__001 == time].index
    return round(df.iloc[temp]['Av'],2), df[int(temp.values):]

def analysePair(item1, item2):
    item1File = folder + item1 + '.csv'
    item2File = folder + item2 + '.csv'

    stock1 = pd.read_csv(item1File)
    stock2 = pd.read_csv(item2File)
    
    stock1 = calculateAverage(stock1);
    stock2 = calculateAverage(stock2);    
    
    EP_item1, stock1 = findEntryPriceWithTime(stock1, time)
    EP_item2, stock2 = findEntryPriceWithTime(stock2, time)
    
    item1Size = middleRound((capital/2)/EP_item1)
    item2Size = middleRound((capital/2)/EP_item2)
        
    profitDF = calculatePL(stock1, EP_item1, item1Size, stock2, EP_item2, item2Size);
    profitDF = stripDateAndSetIdex(profitDF)

    titlePL = item1 + " (" + str(EP_item1) + " * " + str(item1Size) + ") " + " - "
    titlePL += item2  +" (" + str(EP_item2)+ " * " + str(item2Size) + ") "
    
    drawChart(profitDF, 'Time', 'PL', titlePL)

def plotNiftyDistance():
    nifty = pd.read_csv('Nifty.csv')
    nifty = calculateAverage(nifty)
    
    entryPriceNifty, nifty = findEntryPriceWithTime(nifty, time)
    print "Nifty Base price =", entryPriceNifty
    
    nifty = calculateDistance(nifty, entryPriceNifty)
    nifty = stripDateAndSetIdex(nifty)
    
    titleNifty = "Nifty Movement from Base (" + str(entryPriceNifty) + ")"
    drawChart(nifty, 'Time', 'Points', titleNifty)

def plotOptionsCombination(combi):    
    for i in list(combi):
        if ('CE' in i[0] and 'CE' not in i[1]) :
            analysePair(i[0], i[1])
        if ('PE' in i[0] and 'PE' not in i[1]) :
            analysePair(i[0], i[1])

combi = combinations(['11000CE', '11100CE', '11200CE',\
                     '11300CE', '11400CE', '11500CE',\
                     '10000PE', '10100PE', '10200PE',\
                     '10300PE', '10400PE', '10500PE'], 2)

print "Caluclating entries w.r.t time... ", time
plotNiftyDistance()
#plotOptionsCombination(combi)
analysePair('10000PE', '11400CE')
