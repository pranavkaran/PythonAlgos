class Solution(object):
	def twoSum(self, nums, target):
		if len(nums) > 1:
			a = {}
			for i in range(len(nums)):
				if(nums[i] in a):
					return [a[nums[i]], i]
				else:
					a[target-nums[i]] = i
		else:
			return False


x = Solution()
ans = x.twoSum([3,2,4], 6)
print ans
