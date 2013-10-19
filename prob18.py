#!/usr/bin/python
import random
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def x(s):
        return s['x']
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
        #print(data.x)
        #print(data.y)
    return datalist

def check(list, theta):
    

datalist = randMaker()
#datalist.sort()

for i in range(20):
    print(datalist[i].x, datalist[i].y)
