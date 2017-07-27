class Statistics():
	valid = False
	mean = 0
	maxium = 0
	median = 0
	k = 0
	length = 0
	addsum = 0
	buff = None
	def __init__(self):
		self.buff = list()

class StatisticsGenerator():
	inStream = None
	List_k = [3, 20]
	List_stats = list()
	testData = None
	testcnt = 0
	def __init__(self, inStream, testData):
		self.inStream = inStream
		self.testData = testData
		for k in self.List_k:
			stat = Statistics()
			stat.k = k
			self.List_stats.append(stat)
		self.run(self.List_stats)

	def median(self, buff, length):
		mid = length/2
		if length % 2 == 0:
			return (buff[mid -1] + buff[mid])/2
		else:
			return buff[mid]

	def process(self, stat, num):
		stat.buff.append(num)
		stat.length += 1
		stat.addsum += num
		sortBuff = sorted(stat.buff)
		stat.mean = stat.addsum/stat.length
		stat.maxium = sortBuff[stat.length - 1]
		stat.median = self.median(sortBuff, stat.length)
		if stat.length < stat.k:
			stat.valid = False
		else:
			stat.valid = True
			d = stat.buff.pop(0)
			stat.length -= 1
			stat.addsum -= d
		return stat

	def run(self, List_stat):
		while self.inStream.HasNext():
			num = self.inStream.GetNext()
			#print "num: " + str(num)
			if num:
				num = float(num)
				for stat in self.List_stats:
					stat = self.process(stat, num)
				self.PrintValues()

	def HasNext(self):
		for stat in self.List_stats:
			if stat.valid:
				return True
		return False

	def GetNext(self):
		validStats = list()
		for stat in self.List_stats:
			if stat.valid:
				validStats.append(stat)
		return validStats

	def PrintValues(self):
		if self.HasNext():
			for stat in self.GetNext():
				print "==========="
				print "k: " + str(stat.k)
				print "mean: " + str(stat.mean)
				print "maxium: " + str(stat.maxium)
				print "median: " + str(stat.median)
				#self.TestDataSets(stat)
				self.testcnt += 1
				
	def TestDataSets(self, stat):
		cnt = self.testcnt
		assert str(self.testData[cnt][0]) == str(stat.mean)
		assert self.testData[cnt][1] == stat.maxium
		assert self.testData[cnt][2] == stat.median
		print "All assert Passed!"

class InputStream():
	cnt = 0
	arr = []

	def __init__(self, arr):
		self.arr = arr

	def HasNext(self):
		if self.cnt < len(self.arr):
			return True
		return False

	def GetNext(self):
		r = self.arr[self.cnt]
		self.cnt += 1
		return r 

def __MAIN__():
	a = (3,7,1,None,10,4,8)
	test_a = [[3.66666666667, 7.0, 3.0],
			  [6.0, 10.0, 7.0],
			  [5.0, 10.0, 4.0],
			  [7.33333333333, 10.0, 8.0]
			 ]
	b = [3,7,1,None,10,4,8,6,3,4,
		 9,6,11,1,3,9,17,14,8,1,
		 None,4,8,6,3,4,9,6,11,1,
		 3,9,17,10,4,8,6,3,4,9,
		 3,7,1,None,10,4,8,6,3,4,
		 9,6,11,1,3,9,17,14,8,1,
		 None,4,8,6,3,4,9,6,11,1,
		 3,9,17,10,4,8,6,3,4,9]
	objIn = InputStream(a)
	objStat = StatisticsGenerator(objIn, test_a)	
__MAIN__()	
