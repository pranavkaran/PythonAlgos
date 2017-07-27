tag = 8
l = [1,3,5,7,9]
i = 0
j = len(l) -1
rt = []
while i < j:
	if l[i] + l[j] == tag :
		rt.append(str(i) + ' : ' + str(j))
		i = i + 1
	elif l[i] + l[j] > tag :
		j = j - 1
	else: 
		i = i + 1
print rt



h = [3,5,1,6,3,4,8,2,9,4,7]

cnt = 1
tall = h[0]
for i in range (1, len(h)):
	if h[i] > tall and h[i] > h[i - 1] :
		tall = h[i]
		cnt = cnt + 1
print cnt

class Comb(object):

	def __init__(self):
		self.li = []

	def permute(self, s, l, r):
		if l == r:
			a = ''.join(s)
			if a not in self.li:
				self.li.append(a)
			print a

		else:
			for i in xrange(l, r + 1):
				s[l], s[i] = s[i], s[l]
				self.permute(s, l+1, r)
				s[l], s[i] = s[i], s[l] #backtrack

o = Comb()
s = "ABA"
n = len(list(s))
#o.li.append(s)
o.permute(list(s), 0, n-1)
print o.li



n = 5
cnt =0
a = 0
b = 1
fn = 0
while cnt <= n:
	fn = a + b
	a = b
	b = fn
	print fn
	cnt += 1


a = list("student. a am I".split())
#a = list("ecar")
j = len(a) - 1
for i in xrange(0, len(a)):
	if a[i] != "@" or a[j] != "@":
		a[i], a[j] = a[j], a[i] 
	j -= 1
	if i == j:
		break
print ' '.join(a)


a = list("abaccdeff")
temp = []
d = {}
for i in xrange(0, len(a)) :
	if a[i] not in temp:
		temp.append(a[i])
		d[a[i]] = 1
	else: 
		temp.remove(a[i])
		del d[a[i]]
print temp
print next(iter(d))


a = list("abcdefg")
k = 2
print ''.join(a[k: len(a)] + a[0: k])


# def func(a, l, r):
# 	if l == r:
# 		print ''.join(a)
# 	else:
# 		for i in xrange(l, r+1):
# 			a[l], a[i] = a[i], a[l]
# 			func(a, l+1, r)
# 			a[l], a[i] = a[i], a[l]

# func(list("abc"),0, 1)

a = list("baabba")
cnt = 0
for i in xrange(0, len(a)):
	for j in xrange(i + 1, len(a)+1):
		temp = a[i:j]
		if len(temp) > 1 and temp == temp[::-1]:
			cnt += 1
print cnt


def func(root):

	queue = []
	queue.append(root)
	while len(queue) > 0:
		print queue[0].data
		node = queue.pop(0)
		if node.left != None:
			queue.append(root.left)
		if node.right != None:
			queue.append(root.right)




