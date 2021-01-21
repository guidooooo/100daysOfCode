"""
Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.

"""


class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        
        arr_size = len(arr)

        result = 0

        for i in range(arr_size-2):
        	for j in range(i+1,arr_size-1):
        		for k in range(j+1,arr_size):
        			if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <=b and abs(arr[i] - arr[k]) <= c:
        				result+=1

        return result


sol = Solution()
print(sol.countGoodTriplets( arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3))
print(sol.countGoodTriplets(arr = [1,1,2,2,3], a = 0, b = 0, c = 1))