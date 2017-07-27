class Solution(object):
	def evenOrOdd(self, data):
		if(len(data)%2 == 0):
			return 1
		else:
			return 0

	def targetPresent(self, data, target):
		if(len(data) >= 2):
			minVal = data[0] + data[1]
			maxVal = data[len(data) - 2] + data[len(data) - 1] 
			print minVal
			print maxVal
			if(target >= minVal and target <= maxVal):
				return 1
			else:
				return 0
		else:
			return 0

	def checkDataLenLessThree(self, data, target):
		if(len(data) == 3):
			if(data[0] + data[1] == target):
				print 'traget found - 3'
				return [data[0],data[1]]
			elif(data[0] + data[2] == target):
				print 'traget found - 3'
				return [data[0],data[2]]
			elif(data[1] + data[2] == target):
				print 'traget found - 3'
				return [data[1],data[2]]
			else:
				print 'traget not found - 3'
				return []	
		else:
			if(data[0] + data[1]):
				print 'traget found - 2'
				return data
			else:
				print 'traget not found - 2'
				return []

	def check(self, data, target):
		if(len(data) > 3):
			#do something
			mid = len(data)/2
			data1 = []
			data2 = []
			if(self.evenOrOdd(data) == 1):
				data1 = data[0:mid]
				data2 = data[mid: len(data)]
			else:
				data1 = data[0:mid]
				data2 = data[mid: len(data)]
			print data1
			print data2
			midData1 = len(data1)/2
			midData2 = len(data2)/2

			if(self.targetPresent(data1,target)):
				if(len(data1) > 3):
					return self.checkDataLenLessThree(data1, target)
				else:
					print 'do something'
					return self.findSum(data1, target)
			elif(self.targetPresent(data2,target)):
				if(len(data1) > 3):
					return self.checkDataLenLessThree(data2, target)
				else:
					print 'do something'
					return self.findSum(data2, target)
			elif(data1[midData1] + data2[midData2] == target):
				print 'target found'
				return [data1[midData1],data2[midData2]]
			elif(data1[midData1] + data2[midData2] > target):
				print 'midData2 - end data2 is waste'
				data2 = data2[0: midData2+1]
				data1 = data1[0:midData1]
				print data1
				print data2
				print data1 + data2
				return self.findSum(self, data1 + data2, target)
			elif(data1[midData1] + data2[midData2] < target):
				print 'start data1 - midData1 is waste'
				data1 = data1[midData1:len(data1)]
				data2 = data2[midData2:len(data2)]
				print data1
				print data2
				return self.findSum(data1 + data2, target)
		else:
			return self.checkDataLenLessThree(data, target)


	def findSum(self, data, target):
		print data
		ans = []
		if(self.targetPresent(data, target)):
			print 'target is in this data'
			if(self.evenOrOdd(data) == 1):
				upperMidIndex = len(data)/2
				if(self.targetPresent(data[0: upperMidIndex - 1], target)):
					print 'even left - target is in this data'
					ans = self.findSum(data[0: upperMidIndex - 1], target)
				elif(self.targetPresent(data[upperMidIndex: len(data)], target)):
					print 'even right - target is in this data'
					ans = self.findSum(data[upperMidIndex: len(data)], target)
				else:
					print 'even - target is in this array' + str(data) + str(len(data))
					ans = self.check(data, target)
			elif(self.evenOrOdd(data) == 0):
				midIndex = len(data)/2
				if(self.targetPresent(data[0: midIndex], target)):
					print 'odd left - target is in this data'
					ans = self.findSum(data[0: midIndex], target)
				elif(self.targetPresent(data[midIndex: len(data)], target)):
					print 'odd right - target is in this data'
					ans = self.findSum(data[midIndex: len(data)], target)
				else:
					print 'odd - target is in this array' + str(data) + str(len(data))
					ans = self.check(data, target)
		else:
			print 'no target found'
		return ans

	def twoSum(self, nums, target):
		print nums
		data = sorted(nums)
		print data
		ans = self.findSum(data, target)
		if ans:
			print ans
			print 'index: ' + str(data.index(ans[0])) + ' value: ' + str(data[data.index(ans[0])])
			print 'index: ' + str(data.index(ans[1])) + ' value: ' + str(data[data.index(ans[1])])
		return [nums.index(ans[0]),nums.index(ans[1])]


x = Solution()
ans = x.twoSum([3,2,4], 6)
print ans


