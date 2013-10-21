from MultiDSA import *

trainData = LoadData('hw2_train.dat')
testData = LoadData('hw2_test.dat')
s, i, theta, Ein = MultiDimDS(trainData)
print(s,i,theta,Ein)
Eout = CalculateEout(theta, s)
print(Eout)

data = ParseData(testData, i-1)
testEout = mDecitionStump(data, s, theta)
print(testEout)
