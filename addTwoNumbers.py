class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

x = Solution()
a = [4,3,2]
b = [7,6,5]
l11 = ListNode(a[0])
l12 = ListNode(a[1])
l13 = ListNode(a[2])
l11.next = l12
l12.next = l13
l13.next = None
l21 = ListNode(b[0])
l22 = ListNode(b[1])
l23 = ListNode(b[2])
l21.next = l22
l22.next = l23
l23.next = None
result = []
r = x.addTwoNumbers(l11, l21)
while r:
    result.append(r.val)
    r = r.next
print result
print 'end'
