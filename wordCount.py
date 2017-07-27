class Solution(object):
	def wordCount(self, fname):
		file=open(fname,"r+")
		wordcount={}
		for word in file.read().split():
			if word not in wordcount:
				wordcount[word] = 1
    		else:
        		wordcount[word] += 1
		#print (word,wordcount)
		file.close();
		return wordcount

x = Solution()
fname = "/Users/pranavkaran/Documents/Knoesis/Interview/big.txt"
wc = x.wordCount(fname)
print wc