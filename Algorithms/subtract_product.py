#Given an integer number n, return the difference between the product of its digits and the sum of its digits.

class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        num_lst = list(str(n))

        sum_num = 0
        prod_num = 1

        for n in num_lst:

        	sum_num +=int(n)
        	prod_num *=int(n)

        return prod_num - sum_num


sol = Solution()
print(sol.subtractProductAndSum(234))
print(sol.subtractProductAndSum(4421))