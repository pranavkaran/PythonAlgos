class Solution():
	def __init__(self):
		pass

	# def allPermu(self, a):
	# 	print a
	# 	perm = list()
	# 	if len(a) == 0:
	# 		return perm
	# 	first = a[0]
	# 	words = self.allPermu(a[1:])
	# 	print words
	# 	for word in words:
	# 		print "word" + str(word)
	# 		# for i in range(len(word)):
	# 		# 	prefix = word[:i]
	# 		# 	suffix = word[i]
	# 		# 	perm.append(prefix+first+suffix)
	# 	return perm

	def binarySearchRec(self, a, n):
		if len(a) < 1:
			return -1
		mid = len(a)/2
		if n == a[mid]:
			return n
		elif n < a[mid]:
			return self.binarySearchRec(a[:mid], n)
		elif a[mid] < n:
			return self.binarySearchRec(a[mid+1:], n)
		else:
			return -1

	def binarySearch(self, a, n, start, end):
		if len(a) < 1:
			return -1
		start,end = 0, len(a) -1
		while start <= end:
			mid = (start + end)/2
			if n == a[mid]:
				return mid
			elif n < a[mid]:
				end = mid -1
			else:
				start = mid + 1
		return -1

	def leader(self, a):
		i = len(a) -2
		lead = a[len(a) -1]
		print lead
		while i >= 0:
			if a[i] > lead:
				lead = a[i]
				print lead
			i -= 1

	def peak(self, a):
		p = list()
		i = 1
		while i < len(a) - 1:
			if (a[i - 1] <= a[i] and a[i] >= a[i+1]):
				p.append(a[i])
			i += 1
		return p

	def peak_Logn(self, a):
		p = list()
		start, end = 0, len(a) -1
		while start < end:
			mid = (start+end)/2
			if ((mid == 0 or a[mid -1] <= a[mid]) and
				(mid == len(a) - 1 or a[mid] >= a[mid + 1])):
				return a[mid]
			elif 
		return p

	def __MAIN__(self):
		a = list("ab")
		b = [1,3,5,7,9]
		c = [98, 23, 54, 20, 7, 12, 27]
		d = [1,9,3,6,4,7,5]
		#print self.allPermu(a)
		print self.binarySearchRec(b, 2)
		print self.binarySearch(b, 3, 0, len(b))
		self.leader(c)
		print self.peak(d)

obj = Solution()
obj.__MAIN__()
