
#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

#Return the answer in an array.


class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        ordered_num = sorted(nums)
        count_dict = {}
        result = []

        for i, n in enumerate(ordered_num):

        	if i == 0:
        		count_dict[n] = 0
        		continue

        	x = i
        	while n == ordered_num[x] and x>=0:
        		x -=1

        	if x == -1:
        		count_dict[n] = 0
        	else:
        		count_dict[n] = x+1


        for n in nums:
        	result.append(count_dict[n])

        return result

sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))
print(sol.smallerNumbersThanCurrent([6,5,4,8]))
print(sol.smallerNumbersThanCurrent([7,7,7,7]))
