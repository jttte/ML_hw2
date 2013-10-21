from operator import itemgetter

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printData(self):
        print(self.x, self.y)

def LoadData (filename):
	f = open(filename, 'r')
	lines = f.readlines()
	N = len(lines)
	dataList = []

	for i in range(N):
		str = lines[i].strip().split(' ')
		d = len(str) - 1
		x = [float(str[i]) for i in range(d)]
		y = int(str[d])
		data = [x, y]
		#data = Data(x, y)
		dataList.append(data)
	return dataList, N
#def LoadData

def DecisionStump(list):
	N = len(list)#number of data points
	error = 0;
	bestError = N
	theta = 0;
	s = 1

	for i in range(N):
		if ( list[i][1] < 0 ):
			error = error + 1
		#if
	#for

	for i in range(N - 1):
		#theta moves right, so if yi > 0, 
		#it will be misclassified
		error = error + list[i][1]
		if ( error < bestError ):
			bestError = error
			theta = i + 1 #theta is placed at the right side of xi
		#if
	#for

	#s = -1
	error = 0
	for i in range(N):
		if ( list[i][1] > 0 ):
			error = error + 1
		#if
	#for

	for i in range(N - 1):
		#theta moves right, so if yi < 0, 
		#it will be misclassified
		error = error - list[i][1]
		if ( error < bestError ):
			bestError = error
			theta = i + 1 #theta is placed at the right side of xi
			s = -1
		#if
	#for
	if theta == 0:
		bestTheta = list[theta][0] - 0.001
	else:
		bestTheta = ( list[theta-1][0] + list[theta][0] ) / 2
	return bestError, bestTheta, s
#def DecisionStump

def MultiDimDS(list):
	N = len(list[0][0][0]) #dimension of datapoint
	bestError = len(list[0]) #number of datapoints
	bestS = 1
	bestTheta = 0
	bestDim = 0

	for i in range(N):
		data = ParseData(list, i)
		error, theta, s = DecisionStump(data)
		#print(i, error, theta, s)
		if ( error < bestError ):
			bestError = error
			bestDim = i + 1
			bestTheta = theta
			bestS = s
		#if
	#for

	return bestS, bestDim, bestTheta, bestError
#def MultiDimDS

def ParseData(list, d):
	N = len(list[0])
	data_on_d = []
	for i in range(N):
		data = [ list[0][i][0][d], list[0][i][1] ]
		data_on_d.append(data)
	#end for
	data_on_d = sorted(data_on_d, key=itemgetter(0))
	return data_on_d

#def ParseData

def CalculateEout( theta, s ):
	Eout = 0.8 * abs (theta) / 2 + 0.2 * abs(2-theta) / 2

	if ( s < 0 ) :
		Eout = 1 - Eout
	#if

	return Eout
#def CalculateEout

def mDecitionStump(dataList, s, theta):
	error = 0
	N = len(dataList)
	for i in range ( N ):
		if( s * ( dataList[i][0] - theta ) * dataList[i][1]< 0 ):  # y =/= s * sign(x - theta)
			error += 1
		#if
	#for
	return error / float(N)
#def CountError