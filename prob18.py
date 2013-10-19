#!/usr/bin/python
import random
from operator import attrgetter

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):  
                return repr((self.x, self.y))  
    def printData(self):
        print(self.x, self.y)

def randMaker():
    datalist = []
    for i in range(20):
        x = random.uniform(-1,1)
        n = random.uniform(0,1) - 0.2
        if x < 0:
            if n < 0:
                y = 1
            else:
                y = -1
        else:
            if n <= 0:
                y = -1
            else:
                y = 1
        data = Data(x, y)
        datalist.append(data)
    return datalist
#def check(list, theta):
    #end of check
datalist = randMaker()
datalist = sorted(datalist, key=attrgetter('x'))
for i in range(20):
    datalist[i].printData()

