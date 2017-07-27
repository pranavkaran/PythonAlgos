class Solution():
	def __init__(self):
		print "class init"

	def swap(self, n1, n2):
		Headnxt = n1.nxt
		Npre = n2.pre
		Npre.nxt = n2.nxt
		n2.nxt.pre = Npre
		n2.pre = n1
		n2.nxt = Headnxt
		n1.nxt = n2
		Headnxt.pre = n2

	def mapper(self, fname, k):
		lines = list(open(fname, 'r'))
		wordsMap = {}
		wordsMap1 = {}
		head = None
		tail = None
		top = k
		listLen = 0
		cnt = 0
		for line in lines:
			words = line.strip().split(' ')
			for  word in words:
				word = word.lower()
				if word in wordsMap.keys():
					n = wordsMap[word]
					n.val += 1
					if not head:
						head = n
						tail = n
						listLen += 1
					else:
						print "============================"
						print "head: " + head.txt, head.val
						print "tail: " + tail.txt, tail.val
						print "n: " + n.txt, n.val

						if n != head:
							if n.val > head.val:
								head.pre = n
								n.nxt = head
								head = n
							elif (n.val <= head.val and n.val >= tail.val):
								if n.val == head.val:
									if head == tail:
										n.pre = head
										head.nxt = n
										tail = n
										listLen += 1
										print "S"
									else:
										self.swap(head, n)
								elif n.val == tail.val:
									if n != tail:
										Tailpre = tail.pre
										Tailpre.nxt = n
										n.pre = Tailpre
										n.nxt = tail
										tail.pre = n
										listLen += 1
										print "J"
									else:
										print "H: " + n.txt, n.val
										curr = head
										while curr:
											if curr.val <= n.val:
												CurrPre = curr.pre
												tp = tail.pre
												tail.pre = CurrPre
												curr.pre = tail
												CurrPre.nxt = tail
												tail.nxt = curr
												tp.nxt = None
												tail = tp
												break
											curr = curr.nxt

								else:
									if n.pre == None or n.pre.val < n.val:
										curr = head
										while curr:
											if curr.val <= n.val:
												if n.pre == None:
													CurrPre = curr.pre
													CurrPre.nxt = n
													n.pre = CurrPre
													n.nxt = curr
													curr.pre = n
													listLen += 1
												else:	
													self.swap(curr.pre, n)
												break
											curr = curr.nxt
							else:
								print "T" + str(listLen)
								tail.nxt = n
								n.pre = tail
								tail = n
								listLen += 1
							if listLen > k:
								print "----------K----------"
								tailPre = tail.pre
								tailPre.nxt = None
								tail.pre = None
								tail = tailPre
								listLen -= 1
								
							curr = head
							c = 0
							print "fresh loop: --------"
							while curr:
								print curr.txt, curr.val
								c += 1
								curr = curr.nxt
							print "fresh loop end -----"
							print "L: " + str(listLen) + str(c)
					wordsMap[word] = n

				else:
					n = Node(1, word, None, None)
					wordsMap[word] = n

				if word in wordsMap1.keys():
					count = wordsMap1[word]
					wordsMap1[word] = count + 1
				else:
					wordsMap1[word] = 1
		return wordsMap, wordsMap1, head

class Node():
	val = 0
	txt = ""
	nxt = None
	pre = None

	def __init__(self, val, txt, nxt, pre):
		self.val = val
		self.txt = txt
		self.nxt = nxt
		self.pre = pre


def __MAIN__():
	fname = "/Users/pranavkaran/Documents/Knoesis/Interview/topKwordTestData.txt"
	k = 10
	obj = Solution()
	wordsMap, wordsMap1, head = obj.mapper(fname, k)
	from operator import itemgetter
	m = sorted(wordsMap1.items(), key=itemgetter(1), reverse=True)
	print m[:10]
	print "========"
	# for item in wordsMap:
	# 	n = wordsMap[item]
	#  	print n.txt, n.val
	print "========"
	curr = head
	count = 0
	while curr.nxt != None:# and count < k:
		print curr.txt, curr.val
		curr = curr.nxt
		count += 1
__MAIN__()	