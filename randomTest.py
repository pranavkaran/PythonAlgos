class solution():
	def __init__(self):
		pass

	def merge(self, left, right):
		result = []
		i,j = 0,0
		while i < len(left) and j < len(right):
			if left[i] <= right[i]:
				result.append(left[i])
				i+=1
			else:
				result.append(right[j])
				j+=1
		result += left[i:]
		result += right[j:]
		return result

	def mergesort(self, a):
		if len(a) <= 1:
			return a
		mid = int(len(a)/2)
		left = self.mergesort(a[:mid])
		right = self.mergesort(a[mid:])
		return self.merge(left, right)

	def __MAIN__(self):
		a = [9,8,6,1,5,3]
		print self.mergesort(a)

obj = solution()
obj.__MAIN__()