import os

def ifHas (lst, a):
 	return a in lst

def func_BST(lst, a):
	if len(lst) == 0:
		return False

	midIndex = len(lst)/2
	print midIndex, lst[midIndex]
	if lst[midIndex] == a:
		return True
	if lst[midIndex] > a:
		return func_BST(lst[0:midIndex - 1], a)
	else: 
		return func_BST(lst[midIndex:len(lst)], a)


lst = [1,2,3,4,5]
a = 2

#print ifHas(lst, a)

lst1 = []

#assert func_BST(lst1, a) == False

# assert func_BST([], 2) == False
# assert func_BST([1], 2) == False
# assert func_BST([1], 1) == True
print func_BST([1,2,6], 6)
#assert func_BST([1,2,6], 6) == True


class Node(object):
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def add(self, data):
		if self.head:
			self.tail.next = Node(data)
			self.tail = self.tail.next
		else:
			self.head = Node(data)
			self.tail = self.head

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

	def mid(self, head):
		p = fp = head
		while fp and fp.next:
			p = p.next
			fp = p.next
		return fp

	# def search(lt, data):
	# 	if self.count(lt.head) == 0:
	# 		return False
	# 	m = self.mid(lt.head)
	# 	if m.data == data:
	# 		return True
	# 	if m.data > data:
	# 		return self.search(, data)
	# 	else:
	# 		return self.search(, data)


l = LinkedList()
l.add("a")
l.add("b")
l.add("c")
l.add("d")
l.add("e")
l.printList(l.head)




def rev(s):
	s = list(s)
	i = 0
	j = len(s) - 1
	while i < j:
		s[i], s[j] = s[j], s[i]
		i += 1
		j -= 1
		if i == j:
			break
	return ''.join(s)

print rev("AMAZON")
print rev("kumar")

def wordcount(filename):
 	words = {}
 	rt = []
 	file = open(filename)
 	for word in file.read().split():
 		rt.append(rev(word))
 		if word in words:
 			words[word] += 1
 		else:
 			words[word] = 1
 	file.close()
 	print rt
 	return words

print wordcount("/Users/pranavkaran/Documents/Knoesis/Interview/linkdine kumar profile.txt")






