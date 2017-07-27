class Solution():
	def __init__(self):
		print "class init"

	def merge(self, left, right):
		result = []
		i, j = 0, 0
		while i < len(left) and j < len(right):
			if int(left[i]) <= int(right[j]):
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
		result += left[i:]
		result += right[j:]
		return result

	def mergesort(self, a):
		if len(a) < 1:
			return a
		if len(a) == 1:
			if a[0].isdigit():
				return a
			else:
				return tuple()
		mid = int(len(a)/2)
		left = self.mergesort(a[:mid])
		right = self.mergesort(a[mid:])
		return self.merge(left, right)

	def median(self, line):
		line = self.mergesort(line)
		mid = len(line)/2
		if len(line) % 2 == 0:
			return (int(line[mid -1]) + int(line[mid]))/2
		else:
			return int(line[mid])

	def mapper(self, fname):
		lines = tuple(open(fname, 'r'))
		s = ""
		for line in lines:
			num = self.median(line.strip().split())
			s += str(num) + " " 
		return s.strip()

	def reducer(self, lineMed):
		return self.median(lineMed.split())

def __MAIN__():
	fname = "/Users/pranavkaran/Documents/Knoesis/Interview/medianTestData.txt"
	a = [3,7,1,10,4,8]
	b = [6,3,4,9,6,11,1,3,9,17,14,8]
	obj = Solution()
	median = obj.reducer(obj.mapper(fname))
	print median

__MAIN__()	
