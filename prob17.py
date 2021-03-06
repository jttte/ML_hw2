#!/usr/bin/python
import random
from operator import attrgetter

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printData(self):
        print(self.x, self.y)

def randMaker(n):
    datalist = []
    for i in range(n):
        x = random.uniform(-1,1)
        n = random.uniform(0,1) - 0.2
        if x < 0:
            if n < 0:
                y = 1
            else:
                y = -1
        else:
            if n < 0:
                y = -1
            else:
                y = 1
        data = Data(x, y)
        datalist.append(data)
    return datalist

def check(list):
    length = len(list)
    error = 0;
    bestError = length
    bestTheta = 0;
    s = 1

    for i in range(length):
        if ( list[i].y < 0 ):
            error = error + 1
        #if
    #for

    for i in range(length-1):
        #theta moves right, so if yi > 0, 
        #it will be misclassified
        error = error + list[i].y
        if ( error < bestError ):
            bestError = error
            bestTheta = i + 1 #theta is placed at the right side of xi
        #if
    #for

    #s = -1
    error = 0
    for i in range(length):
        if ( list[i].y > 0 ):
            error = error + 1
        #if
    #for

    if ( error < bestError ):
        bestError = error
        bestTheta = 0
        s = -1

    for i in range(length-1):
        #theta moves right, so if yi < 0, 
        #it will be misclassified
        error = error - list[i].y
        if ( error < bestError ):
            bestError = error
            bestTheta = i + 1 #theta is placed at the right side of xi
            s = -1
        #if
    #for


    if ( bestTheta == 0 ):
        theta = list[0].x - 0.05
    else:
        theta = ( list[bestTheta-1].x + list[bestTheta].x ) / 2

    return s, bestError, theta
#def check

#main
totalEin = 0;
totalEout = 0;
for i in range(5000):
    datalist = randMaker(20)
    datalist = sorted(datalist, key=attrgetter('x'))
    #for i in range(20):
    #    datalist[i].printData()
    s, Ein, theta = check(datalist)
    totalEin = totalEin + Ein
    Eout = 0.8 * abs (theta) / 2 + 0.2 * ( 2 - abs(theta) ) / 2
    if ( s < 0 ):
        Eout = 1 - Eout
    #if
    totalEout = totalEout + Eout
#for

print(totalEin/50.0/20.0)
print(totalEout/50.0)

