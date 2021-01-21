"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.
"""

class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        array_size = len(arr)

        size_option = list(range(1,array_size+1,2))
        sub_array = []
        for n in size_option:
        
        	for m in range(array_size):
        		if m+n-1 > array_size-1:
        			break
        		else:
        			sub_array.append(sum(arr[m:m+n]))


        return sum(sub_array)


sol = Solution()
print(sol.sumOddLengthSubarrays(arr = [1,4,2,5,3]))
print(sol.sumOddLengthSubarrays(arr = [1,2]))
print(sol.sumOddLengthSubarrays(arr = [10,11,12]))


