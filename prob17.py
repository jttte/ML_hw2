#!/usr/bin/python
import random

def randMaker(list):
    for i in range(20):
        xi = random.uniform(-1,1)
        n = random.uniform(0,1) - 0.2
        if xi < 0:
            if n < 0:
                xi = 1
            else:
                xi = -1
        else:
            if n <= 0:
                xi = -1
            else:
                xi = 1
        list.append(xi)
    return list


x = []
randMaker(x)
print(x)


