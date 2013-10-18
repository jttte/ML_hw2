#!/usr/bin/python
import random

def randMaker():
    x = []
    y = []
    for i in range(20):
        xi = random.uniform(-1,1)
        n = random.uniform(0,1) - 0.2
        if xi < 0:
            if n < 0:
                yi = 1
            else:
                yi = -1
        else:
            if n <= 0:
                yi = -1
            else:
                yi = 1
        x.append(xi)
        y.append(yi)
    return x, y

x, y = randMaker()
print(x)
print(y)


