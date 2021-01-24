
#Given an array nums of integers, return how many of them contain an even number of digits.

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0

        for num in nums:
        	digits = 0
        	while num >=1:
        		num //=10
        		digits +=1

        	if digits %2 ==0:
        		count +=1

        return count


sol = Solution()
print(sol.findNumbers( [12,345,2,6,7896]))
print(sol.findNumbers( [555,901,482,1771]))