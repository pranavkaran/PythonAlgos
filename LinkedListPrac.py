class Node (object):
	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

class LinkedList(object):
	def __init__(self, head = None):
		self.head = head
		self.tail = None

	def add(self, data):
		if self.head == None :
			self.head = Node(data)
			self.tail = self.head
		else:
			self.tail.next = Node(data)
			self.tail = self.tail.next

	def printList(self, head):
		while head.next != None:
			print head.data
			head = head.next
		print head.data

	def count(self, curr):
		cnt = 0
		while curr.next != None :
			cnt += 1
			curr = curr.next
		cnt += 1
		return cnt

	


l = LinkedList()
l.add("a")
l.add("b")
l.add("c")
l.add("d")
#l.printList(l.head)
cnt = l.count(l.head)
print cnt

s = "dgjksgfgsklsgjklflaggjkgsagjksss"
p = "gjk"

# for ch in s:
# 	print ch

