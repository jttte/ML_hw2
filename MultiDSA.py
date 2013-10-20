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

def DecisionStump(list, d):
	N = len(list) #number of data
	#for i in range(d):

	#for
#def DecisionStump
def ParseData(list, d):
	N = len(list)
	data_on_d = []
	for i in range(N):
		data = [ list[i][0][d], list[i][1] ]
		data_on_d.append(data)
	#end for
	

#def ParseData

def ChooseTheta(data):
	length = len(list)
	error = 0;
    bestError = length
    bestTheta = 0;
    for i in range(length):
        if ( list[i].y < 0 ):
            error = error + 1
        #if
    #for

    for i in range(length):
        #theta moves right, so if yi > 0, 
        #it will be misclassified
        error = error + list[i].y
        if ( error < bestError ):
            bestError = error
            bestTheta = i + 1 #theta is placed at the right side of xi
        #if
    #for
    return bestError, bestTheta
#def ParseData