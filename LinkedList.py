import sys
class Node(object):

	def __init__(self, data = None, node = None):
		self.data = data
		self.next = node
	

class LinkedList(object):
	
	def __init__(self, head = None):
		self.head = head

	def add(self, data):
		node = Node(data)
		if self.head == None:
			self.head = node
		else: 
			curr = self.head
			while curr.next != None:
				curr = curr.next
			curr.next = node

	def printList(self, curr):
		while (curr.next != None):
			print curr.data
			curr = curr.next
		print curr.data


	def remove(self, data):
		curr = self.head
		prev = None
		while (curr.next != None):
			if(curr.data == data):
				if prev == None:
					self.head = curr.next
				else:
					prev.next = curr.next
			prev = curr
			curr = curr.next
	
	def merge(self, head1, head2):
		s = t = Node()
		while not (head1 is None or head2 is None):
			if head1.data < head2.data :
				curr = head1
				head1 = head1.next
			elif head1.data == head2.data :
				head1 = head1.next
				head2 = head2.next
			else: 
				curr = head2
				head2 = head2.next
			t.next = curr
			t = t.next
		t.next = head1 or head2

		return s.next

	def reverse(self, curr):
		tail = None
		if (curr.next == None):
			self.tail = curr
			return curr
		else: 
			prev = curr
			curr = self.reverse(curr.next)
			curr.next = prev
			if(prev == self.head):
				prev.next = None
				return self.tail
			else:
				return prev

	def reverseK(self, head1, k):
		cnt = 0
		curr = head1
		prev = None
		temp = LinkedList()
		rt = LinkedList()
		while curr.next != None:
			if cnt == 0:
				pass
			elif cnt == k:
				temp.head = temp.reverse(temp.head)
				tc = temp.head
				while tc.next != None:
					rt.add(tc.data)
					tc = tc.next
				rt.add(tc.data)
				cnt = 0
				temp = LinkedList()
			temp.add(curr.data)
			cnt += 1
			prev = curr
			curr = curr.next
		temp.add(curr.data)
		cnt += 1
		if cnt == k:
			temp.head = temp.reverse(temp.head)
			tc = temp.head
			while tc.next != None:
				rt.add(tc.data)
				tc = tc.next
			rt.add(tc.data)
		if rt.head != None:
			print "--last--"
			rt.printList(rt.head)


l1 = LinkedList()
l1.add("aaa")
l1.add("bbb")
l1.add("ddd")
l1.add("eee")
l1.add("fff")
l1.add("ggg")
l1.add("hhh")
l1.add("jjj")

l2 = LinkedList()
l2.add("bbb")
l2.add("ccc")
l2.add("eee")
l2.add("fff")

#print l1.head.next

print "l1"
l1.printList(l1.head)
print "l2"
l2.printList(l2.head)
print "--------"

# h = l1.merge(l1.head, l2.head)
# l2.printList(h)

# h = l1.reverse(l1.head)
# l1.printList(h)

l1.reverseK(l1.head, 2)
#print "here --------"
#l1.printList(l1.head)













