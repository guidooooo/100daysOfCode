# Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        result = []

        max_candies = 0
        less_candies_lst = []

        for kid_candy in candies:
        	if kid_candy >max_candies:
        		max_candies = kid_candy

        for x in candies:
        	if x+extraCandies >= max_candies:
        		result.append(True)
        	else:
        		result.append(False)

        return result

sol = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(sol.kidsWithCandies(candies, extraCandies))

candies = [4,2,1,1,2]
extraCandies = 1
print(sol.kidsWithCandies(candies, extraCandies))

candies = [12,1,12]
extraCandies = 10
print(sol.kidsWithCandies(candies, extraCandies))