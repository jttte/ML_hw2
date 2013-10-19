#!/usr/bin/python
import random
from operator import attrgetter

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
sorted(datalist, key = attrgetter('x'))
print(datalist)
#sortedDatalist = collections.OrderedDict(sorted(datalist.x))
#datalist.sort()
#print(sortedDtalist)
