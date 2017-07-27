class Node(object):
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head
		self.tail = None

	def add(self, data):
		if self.head is None:
			self.head = Node(data)
			self.tail = self.head
			self.head.next = None
		else:
			self.tail.next = Node(data)
			self.tail = self.tail.next

	def printList(self, head):
		while head:
			print head.data
			head = head.next

	def count(self, head):
		cnt = 0
		while head:
			cnt += 1
			head = head.next
		return cnt

	def getNth(self, n):
		cnt = 0
		while head:
			if cnt == n :
				break
			cnt += 1
			head = head.next
		return head

	def pop(self):
		currHead = self.head
		rt = Node(currHead.data)
		nextNode = currHead.next
		currHead.data = nextNode.data
		currHead.next = nextNode.next
		nextNode.next = None
		self.head = currHead
		return rt

	def remove(self, head, node):
		prev = head
		while head:
			if head.data == node.data:
				if head.next is None:
					prev.next = None
				else:
					rmNode = head.next
					head.data = rmNode.data
					head.next = rmNode.next
					rmNode.next = None
			prev = head 
			head = head.next

	def insertN(self, head, n, node):
		cnt = 0
		while head:
			if cnt == n:
				temp = head.next
				head.next = node
				head.data ,node.data = node.data, head.data
				node.next = temp
				break
			cnt = cnt + 1
			head = head.next

	def sortedInsert(self, head, node):
		while head:
			if head.data > node.data:
				temp = head.next
				head.next = node
				head.data ,node.data = node.data, head.data
				node.next = temp
				break
			head = head.next

	def mid(self, head):
		p = fp = head
		while fp and fp.next:
			p = p.next
			fp = p.next
		return p

l1 = LinkedList()
l1.add("a")
l1.add("b")
l1.add("c")
l1.add("d")
l1.printList(l1.head)
print l1.count(l1.head)
print l1.pop().data
l1.printList(l1.head)
l1.remove(l1.head, Node("c"))
l1.printList(l1.head)
l1.insertN(l1.head, 1, Node("c"))
l1.printList(l1.head)
l1.sortedInsert(l1.head, Node("a"))
l1.printList(l1.head)

l2 = LinkedList()
l2.add("a")
l2.add("b")
l2.add("c")
l2.add("d")

m = l2.mid(l2.head)
print m.data 


