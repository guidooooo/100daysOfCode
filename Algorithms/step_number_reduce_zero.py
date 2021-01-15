#Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.


class Solution(object):
    def numberOfSteps (self, num):
        """
        :type num: int
        :rtype: int
        """
        count=0
        while num>0:
        	count +=1
        	if num % 2 == 0: 
        		num = num/2
        		continue

        	num -=1

        return count

sol = Solution()
print(sol.numberOfSteps(14))
print(sol.numberOfSteps(8))
print(sol.numberOfSteps(123))
