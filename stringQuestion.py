class Solution(object):
	def reverse(self, s):
		i = 0
		j = len(s) - 1
		while 1:
			if len(s) % 2 == 0:
				if i == j:
					break
				else:
					temp1 = s[i]
					temp2 = s[j]
					s[i] = temp2
					s[j] = temp1
			else:
				if i + 1 == j:
					break
				else:
					temp1 = s[i]
					temp2 = s[j]
					s[i:i+1] = temp2
					s[j] = temp1
			i += i
			j -= j

o = Solution()
s = "abcde"
print o.reverse(s)

