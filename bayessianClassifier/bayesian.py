import csv
import random
import statistics

class DataHandler:
	def __init__(self, filename):
		#self.dataset = self.loadCsv(filename)
		self.dataset = filename
		self.trainData = list(self.dataset)
		self.mean, self.stddev = {}, {}
		self.testData = []
		self.separatedByClass = {}
		
	def loadCsv(self, filename):
		with open(filename, 'r') as csvfile:
			self.dataset = list(csv.reader(csvfile))
			self.__prepareDataset(len(self.dataset))
		return self.dataset

	def splitData(self, percentOfTestData):
		testDataLen = int(percentOfTestData * len(self.trainData))
		while len(self.testData) < testDataLen:		
			self.testData.append(self.trainData.pop(random.randrange(len(self.trainData))))

	def separateByClass(self):
		for i in range(len(self.dataset)):
			self.__appendRow(self.dataset[i])

	def calculateStats(self):
		for separatedClass in self.separatedByClass:
			self.mean[separatedClass], self.stddev[separatedClass] = [], []
			self.__calcMeanStdDev(separatedClass)

	def __prepareDataset(self, length):
		for i in range(length):
			self.dataset[i] = [float(x) for x in self.dataset[i]]

	def __calcMeanStdDev(self, separatedClass):
		for i in range(len(self.separatedByClass[separatedClass])-1):
                    tmp = statistics.mean([x[i] for x in self.separatedByClass[separatedClass]])
                    self.mean[separatedClass].append(tmp)
                    tmp = statistics.stdev([x[i] for x in self.separatedByClass[separatedClass]])
                    self.stddev[separatedClass].append(tmp)


	def __appendRow(self, row):
		self.__createIfNotExists(row)
		self.separatedByClass[row[-1]].append(row)

	def __createIfNotExists(self, row):
		if(row[-1] not in self.separatedByClass):
			self.separatedByClass[row[-1]] = []


#	def __calculateStatistics(self, calcType):
#		tmp = statistics.mean([x[i] for x in self.separatedByClass[separatedClass]])
#		self.mean[separatedClass].append(tmp)
#	def __calculateStdDev():
#		tmp = statistics.stdev([x[i] for x in self.separatedByClass[separatedClass]])
#		self.stddev[separatedClass].append(tmp)		

#{0 : [[3, 32, 3],[5, 32, 3],[4, 32, 3]], 1 : [3,4,3]}

filename = '/home/mcbride/Downloads/pima-indians-diabetes.data.csv'
filename = [[1,2,1], [2,5,0], [4,7,0], [3,5,1], [2,5,0], [43,2,1]]
dh = DataHandler(filename)
dh.splitData(0.33)
dh.separateByClass()
dh.calculateStats()

print("mean {0} stddev {1}".format(dh.mean, dh.stddev))
