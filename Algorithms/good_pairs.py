
#Given an array of integers nums.

#A pair (i,j) is called good if nums[i] == nums[j] and i < j.

#Return the number of good pairs.

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for n in range(len(nums)-1):
        	for m in range(n+1,len(nums)):
        		if nums[n] == nums[m]:
        			result +=1

        return result

        # num_dict = []

        # for index, n in enumerate(nums):

        # 	num_value = num_dict.get(n,[])
        # 	num_value.append(index)
        # 	num_dict[n] = num_value

        # result = 0

        # for pairs in list(num_dict.values()):
        	
        # 	if len(pairs) == 1: continue

        # 	result += 

