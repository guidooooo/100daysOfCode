#Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
#Return the array in the form [x1,y1,x2,y2,...,xn,yn].

class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """

        x = nums[:n]
        y = nums[n:]

        result= []
        for n in range(n):
        	result.append(x[n])
        	result.append(y[n])

        return result
        
sol = Solution()

nums=[2,5,1,3,4,7]
n=3
print(sol.shuffle(nums, n))

nums=[1,2,3,4,4,3,2,1]
n=4
print(sol.shuffle(nums, n))

nums=[1,1,2,2]
n=2
print(sol.shuffle(nums, n))