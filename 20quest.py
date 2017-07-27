class Node():
	val = ""
	nxt = None
	def __init__(self, val, nxt):
		self.val = val
		self.nxt = nxt

class Solution():
	def __init__(self):
		print "Solution class"

	def rev(self, head):
		curr = head
		if curr.nxt == None:
			return curr, curr
		else:
			prev = curr
			head, curr = self.rev(curr.nxt)
			prev.nxt = None
			curr.nxt = prev
		return head, prev

	def revwithK(self, head, k):
		prev = head
		curr = head.nxt
		count = 1
		while (curr.nxt != None and count <= k):
			prev.nxt = curr.nxt
			curr.nxt = prev
			count += 1
		if curr.nxt != None:
			head, prev = self.revwithK(curr,k)


	def ll_print(self, head):
		while head != None:
			print head.val
			head = head.nxt

def __MAIN__():
	d = Node(1, None)
	c = Node(4, d)
	b = Node(3, c)
	a = Node(7, b)
	obj = Solution()
	obj.ll_print(a)
	head, tail = obj.rev(a)
	obj.ll_print(head)

__MAIN__()