# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cum = 0
        result = []
        for n in nums:
        	cum +=n
        	result.append(cum)

        return result


sol = Solution()
print(sol.runningSum([1,2,3,4]))
print(sol.runningSum([1,1,1,1,1]))
print(sol.runningSum([3,1,2,10,1]))
