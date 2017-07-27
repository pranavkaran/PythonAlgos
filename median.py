class Solution():
	def __init__(self):
		print "class init"

	def median(self, lst):
		om0 = -1
		om1 = -1
		count = 1
		m = list()
		up = list()
		for num in lst:
			if count == 1:
				om0 = om1 = num
				upBool = True
			else:
				up.append(num)

			if count % 2 == 0:
				om1 = up.pop(0)
				m.append([om0, om1])
			else:
				m.append([om1])
				om0 = om1
			count += 1
		return m

	def mapper(self, fname):
		lineMed = list()
		with open(fname) as f:
			for line in f:
				lineList = map(int, line.strip().split())
				lineMed.append(self.median(lineList).pop())
		return lineMed

	def reducer(self, lineMed):
		medianLists = list()
		for lst in lineMed:
			medianLists.append(reduce(lambda x, y: x + y, lst) / len(lst))
		medianList = self.median(medianLists).pop()
		return reduce(lambda x, y: x + y, medianList) / len(medianList)

def __MAIN__():
	fname = "/Users/pranavkaran/Documents/Knoesis/Interview/medianTestData.txt"
	a = [3,7,1,10,4,8]
	b = [6,3,4,9,6,11,1,3,9,17,14,8]
	obj = Solution()
	median = obj.reducer(obj.mapper(fname))
	print median

__MAIN__()	
