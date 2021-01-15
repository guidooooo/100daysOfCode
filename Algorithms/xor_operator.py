#Given an integer n and an integer start.

#Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

#Return the bitwise XOR of all elements of nums.

class Solution(object):
	def xorOperation(self, n, start):
		"""
		:type n: int
		:type start: int
		:rtype: int
		"""
		result = start
		for i in range(1,n):
			result ^= (start + 2*i)
			
		return result

sol = Solution()
print(sol.xorOperation(n = 5, start = 0))
print(sol.xorOperation(n = 4, start = 3))
print(sol.xorOperation(n = 1, start = 7))
print(sol.xorOperation(n = 10, start = 5))

