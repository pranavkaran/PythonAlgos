class Solution(object):
	def palin(self, s, start, end, lst):
		print s
		while start >= 0 and end < len(s) and s[i] == s[end - i]:
			lst.append(s[i:end])
			print lst
			i -= i
			end += end
		return lst

	def longestPalindrome(self, s):
		lst = []
		length = len(s)
		for i in range(len(s)):
			lst = self.palin(s[i: length], i, length, lst)
			print lst
		return lst

x = Solution()
s = 'malyalam'
#s = 'shfgoifsafposdhpgohsaopgpjgfksdffigigofoiasgf'
r = x.longestPalindrome(s)
print r