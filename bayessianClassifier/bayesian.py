#!/usr/bin/python
import csv
import random
import statistics

class DataHandler:
	def __init__(self, filename):
		#self.dataset = self.loadCsv(filename)
		self.dataset = filename

	def loadCsv(self, filename):
		with open(filename, 'r') as csvfile:
			self.dataset = list(csv.reader(csvfile))
			self.prepareDataset(len(self.dataset))
		return self.dataset

	def prepareDataset(self, length):
		for i in range(length):
			self.dataset[i] = [float(x) for x in self.dataset[i]]	

	def splitData(self, percentOfTestData):
		self.trainData = list(self.dataset)
		testDataLen = int(percentOfTestData * len(self.trainData))
		self.testData = []
		while len(self.testData) < testDataLen:		
			self.testData.append(self.trainData.pop(random.randrange(len(self.trainData))))
		return [self.trainData, self.testData]

	def separateByClass(self):
		self.separatedByClass = {}
		for i in range(len(self.dataset)):
			row = self.dataset[i]
			if(row[-1] not in self.separatedByClass):
				self.separatedByClass[row[-1]] = []
			self.separatedByClass[row[-1]].append(row)
		return self.separatedByClass

	def calculateStats(self):
		self.mean, self.stddev = {}, {}
		for separatedClass in self.separatedByClass:
			self.mean[separatedClass], self.stddev[separatedClass] = [], []
			self.__calcMeanStdDev(separatedClass)
		return [self.mean, self.stddev]

	def __calcMeanStdDev(self, sClass):
		for i in range(len(self.separatedByClass[sClass])-1):	
			tmp = statistics.mean([x[i] for x in self.separatedByClass[sClass]])
			self.mean[sClass].append(tmp)
			self.stddev[sClass].append(statistics.stdev([x[i] for x in self.separatedByClass[sClass]]))
			pass

#{0 : [[3, 32, 3],[5, 32, 3],[4, 32, 3]], 1 : [3,4,3]}

filename = '/home/mcbride/Downloads/pima-indians-diabetes.data.csv'
filename = [[1,2,1], [2,5,0], [4,7,0], [3,5,1], [2,5,0], [43,2,1]]
dh = DataHandler(filename)
dh.splitData(0.33)
dh.separateByClass()
dh.calculateStats()

print("mean {0} stddev {1}".format(dh.mean, dh.stddev))

#dataset = loadCsv(filename)

#print("loaded {0} rows from {1}".format(len(dataset), filename))
#percentOfTestData = 0.33
#train, test = splitData(dataset, percentOfTestData)

#print("loaded {0} rows for train and {1} rows for test".format(len(train), len(test)))

#dataset = [[1,2,1], [2,5,0], [4,7,0], [3,5,1], [2,5,0], [43,2,1]]

#separated = separateByClass(dataset)
#print(separated)
#mean, stdev = calculateStats(separated)
#print(mean)
#print(stdev)








