def linearsearch(ls, value):
	for i in range(len(ls)):
		if (ls[i] == value):
			return i
	return -1

def findSum(ls, value):
	for i in ls:
		for j in ls[ls.index(i) + 1 :]:
			if (i + j == value):
				return "indexes are : " + str(ls.index(i)) + " and " + str(ls.index(j))
	return "Not found"

def findSumByIndex(ls, value):
	for i in range(len(ls)):
		for j in range(len(ls) - i):
			if (ls[i] + ls[j+i] == value):
				return "indexes are : " + str(i) + " and " + str(j+i)
	return "Not found"

def findArrayLenEvenorOdd(ls):
	return len(ls) % 2

def checkRecursive(ls, value):
	if (findArrayLenEvenorOdd(ls) == 0):
		m1 = len(ls)/2
		m2 = (len(ls)/2) + 1
	else:
		m = len(ls)/2
		if(ls[m-1] + ls[m] < value):
			ls = ls[m:len(s)]
			checkRecursive(ls, value)
		else:
			ls = ls[0:m]
			checkRecursive(ls, value)
			

ls = [1, 8, 4, 0, 5, 2, 3, 9, 6]
value = 15

print linearsearch(ls, value)
print findSum(ls, value)
print findSumByIndex(ls, value)
ls.sort()
print len(ls)

print findArrayLenEvenorOdd(ls)