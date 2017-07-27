def getTotal(a):
	sum = 0
	for i in a:
		sum += i
	return sum

def sol(a):
	l = list()
	total = getTotal(a)
	print total
	sum = 0
	for i in range(len(a)):
		if (total - 2*sum == a[i]):
			l.append(i)
		sum += a[i]
	return l if len(l) > 0 else -1

a = [-1,3,-4,5,1,-6,2,1]

print sol(a)

import math
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N):
    # write your code in Python 2.7
    m = int(math.floor(math.log( N ) / math.log( 2 )))
    r = N; num0 = 0; maxNum = 0
    while r > 0:
        n = 2**m
    	if r >= n:
            r -= n
            if maxNum < num0:
                maxNum = num0
            num0 = 0
        else:
            num0 += 1
        m -= 1
    return maxNum if maxNum > 0 else num0

print solution(11)

