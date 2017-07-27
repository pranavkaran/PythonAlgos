import sys

class Node(object):
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head
		self.tail = None

	def add(self, data):
		if self.head == None:
			self.head = Node(data)
			self.tail = self.head
		else:
			self.tail.next = Node(data)
			self.tail = self.tail.next

	def printList(self, head):
		while head :
			print head.data
			head = head.next

	def reverse(self, head):
		prev = curr = head
		if curr.next == None:
			self.tail = curr
			return curr
		else:
			prev = curr
			n = self.reverse(curr.next)
			n.next = prev
			if prev == self.head:
				prev.next = None
				return self.tail
			else:
				return prev

	def count(self):
		cnt = 0
		curr = self.head
		while curr != None :
			cnt += 1
			curr = curr.next
		return cnt

	def countAndPrint(self):
		curr = self.head
		cnt = 0
		cnt0 = 0
		cnt1 = 0
		cnt2 = 0
		rt = LinkedList()
		
		while curr.next != None:
			if(curr.data == "0"):
				cnt0 += 1
			elif(curr.data == "1"):
				cnt1 += 1
			else:
				cnt2 += 1
			curr = curr.next

		while cnt <= cnt0 :
			rt.add("0")
			cnt += 1
		cnt = 0
		while cnt <= cnt1 :
			rt.add("1")
			cnt += 1
		cnt = 0
		while cnt <= cnt2 :
			rt.add("2")
			cnt += 1
		rt.printList(rt.head)
		h = rt.reverse(rt.head)
		rt.printList(h)

	def mid(self):
		p = self.head
		fp = p
		while fp and fp.next :
			p = p.next
			fp = fp.next.next
		return p

	def remove(self, head, node):
		curr = head
		if curr.data == node.data :
			curr.data = curr.next.data
			curr.next = curr.next.next
		elif not curr.next.next and curr.next.data == node.data :
			curr.next = None
		else:
			prev = curr
			self.remove(curr.next, node)

	def getNode(self, data):
		curr = self.head
		while curr:
			if curr.data == data :
				return curr
			curr = curr.next

	def hasLoop(self):
		p = self.head
		fp = p
		while fp and fp.next :
			p = p.next
			fp = fp.next.next
			if(p.data == fp.data):
				print "loop found"
				break

	def getKthElementFromLast(self, k):
		p = fp = self.head
		cnt = 0
		while cnt < k:
			fp = fp.next
			cnt += 1
		while fp:
			p = p.next
			fp = fp.next
		return p

	def palin(self, head):
		p = head
 		fp = head
 		prev = fp
 		while fp and fp.next :
			p = p.next
			prev = fp
			fp = fp.next.next

		curr = head
		s1 = ""
		while curr != p :
			s1 = s1 + str(curr.data)
			curr = curr.next
	
		curr = p.next
		s2 = ""
		while curr :
			s2 = s2 + str(curr.data)
			curr = curr.next
		
		if s1 == s2[::-1]:
			print "palindrome"
		else:
			print "not palindrome"

	def larSeq(self, head):
		curr = head
		prev = head
		start = None
		cnt = 0
		maxCnt = 0

		while curr:
			if int(prev.data) + 1 == int(curr.data) :
				if cnt == 0:
					start = prev
				cnt = cnt + 1
				if cnt > maxCnt:
					maxCnt = cnt
					cnt = 0
			prev = curr	
			curr = curr.next
		print "start.data: " + str(start.data)
		print "maxCnt: " + str(maxCnt)

	def palWithRec(self, head, tail):
		if not tail.next:
			return True, head.next
		else:
			b, head = self.palWithRec(head, tail.next)
			if not b :
				return b, head
			if head.data != tail.data:
				b = False
			head = head.next
			return b, head

	def Kprac(self, head, k):
		curr = prev = head
		cnt = 0
		if not curr.next:
			cnt += 1
			return curr, cnt
		else:
			prev = curr
			curr, cnt = self.Kprac(curr.next, k)
			if cnt == k:
				return curr, cnt
			else:
				cnt += 1
				return prev, cnt

	def Kprac2(self, head, k):
		p = fp = head
		cnt = 0
		while cnt < k:
			fp = fp.next
			cnt += 1
		while fp:
			p = p.next
			fp = fp.next
		return p

	def revPrac(self, head):
		curr = prev = head
		if not curr.next:
			return curr, curr
		else:
			prev = curr
			curr, newHead = self.revPrac(curr.next)
			if prev == head:
				prev.next = None
			curr.next = prev
			return prev, newHead

	def checkLoopPrac(self, head):
		p = fp = head
		while fp or fp.next:
			if p.data == fp.data:
				return True
			p = p.next
			fp = fp.next

	def addTwoList(self, head1, head2):
		prev, head1 = self.revPrac(head1)
		prev, head2 = self.revPrac(head2)
		rt = LinkedList()
		carry = 0
		while head1 and head2:
			carry,r = divmod(int(head1.data) + int(head2.data) + carry, 10)
			rt.add(r)
			head1 = head1.next
			head2 = head2.next
		return rt

	def merge(self, head1, head2):
		if head1 is None:
			return head2
		if head2 is None:
			return head1
		if head1.data <= head2.data:
			result = head1
			result.next = self.merge(head1.next, head2)
		else:
			result = head2
			result.next = self.merge(head1, head2.next)
		return result

	def mergePrac(self, head1, head2):
		if head1 > head2:
			head1, head2 = head2, head1
		rt = head1
		m = LinkedList()
		while head2:
			while head1:
				m.printList(head1)
				print "---"
				if head1.next != None and head1.next.data > head2.data:
					#self.printList(head1)
					#print head1.next.data
					#print head2.data
					temp = head1.next
					head1.next = head2
					head2.next = temp
					#print head1.next.data
					break
				else:
					head1 = head1.next
			head2 = head2.next
		print rt.data
		m.printList(rt)
		return rt

l = LinkedList()
l.add("0")
l.add("1")
l.add("0")
l.add("1")
l.add("1")
l.add("0")
l.add("2")
l.add("0")
l.add("2")
l.add("1")
l.add("2")
l.add("2")
l.add("1")
l.add("1")
l.add("0")

#l.countAndPrint()


l1 = LinkedList()
l1.add("1")
l1.add("2")
l1.add("3")
l1.add("4")
l1.add("5")
#l1.add("6")
#l1.add("7")
#l1.add("8")
#l1.add("9")

print "count: " + str(l1.count())
print "mid for odd: " + str(l1.mid().data)
print "removed node containing 5"
l1.remove(l1.head, Node("5"))
print "count: " + str(l1.count())
print "mid for even: " + str(l1.mid().data)


print "\n \n"
print "now printing the linked list"
l1.printList(l1.head)
print "now getting last node and setting it None"
n = l1.getNode("4")
print "get node containting data = 4: " + n.data
n = None
print "value of n after None: " + str(n)
print "printing the list"
l1.printList(l1.head)


print "\n --------- \n"
l2 = LinkedList()
l2.add("1")
l2.add("2")
l2.add("3")
l2.add("4")
#l2.add("5")
# l2.add("6")
# l2.add("7")
# l2.add("8")
# l2.add("9")

l2.tail.next = l2.getNode("3")
l2.hasLoop()
l2.tail.next = None
k = 2
kn = l2.getKthElementFromLast(k)
print kn.data

print "\n --------- \n"
l3 = LinkedList()
l3.add("1")
l3.add("2")
l3.add("3")
l3.add("4")
l3.add("3")
l3.add("2")
l3.add("1")
# l2.add("8")
# l2.add("9")

l3.palin(l3.head)
print l3.palWithRec(l3.head, l3.head)

print "\n --------- \n"
l4 = LinkedList()
l4.add("3")
l4.add("6")
l4.add("7")
l4.add("1")
l4.add("3")
l4.add("4")
l4.add("5")
l4.add("1")
l4.add("3")

l4.larSeq(l4.head)

curr, cnt = l4.Kprac(l4.head, 3)
print curr.data
print l4.Kprac2(l4.head, 3).data
prev, nHead = l4.revPrac(l4.head)
l4.printList(nHead)

l5 = LinkedList()
l5.add("1")
l5.add("2")
l5.add("3")
l6 = LinkedList()
l6.add("4")
l6.add("5")
l6.add("6")
l6.add("7")
 
n = l5.addTwoList(l5.head, l6.head)
l5.printList(n.head)

print "\n----merge---- \n"
l7 = LinkedList()
l7.add("1")
l7.add("2")
l7.add("6")
l8 = LinkedList()
l8.add("3")
l8.add("4")
l8.add("9")
 
# n = l7.merge(l7.head, l8.head)
# l7.printList(n)
print "\n----merge prac----\n"
n2 = l7.mergePrac(l7.head, l8.head)
#l7.printList(n2.head)















