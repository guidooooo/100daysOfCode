#Given two arrays of integers nums and index. Your task is to create target array under the following rules:

#Initially target array is empty.
#From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
#Repeat the previous step until there are no elements to read in nums and index.
#Return the target array.

#It is guaranteed that the insertion operations will be valid.

class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """

        if len(nums) ==1 : return [nums[0]]
        
        target = []
        for n in range(len(nums)):
        	target.insert(index[n],nums[n])

        return target

sol = Solution()
print(sol.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
print(sol.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
print(sol.createTargetArray(nums = [1], index = [0]))
