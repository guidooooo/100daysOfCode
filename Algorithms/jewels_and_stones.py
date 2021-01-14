
#You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

#Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        flag= False
        for index, stone in enumerate(stones):

        	if flag and stones == stones[index-1]:
        		count += 1
        		continue

        	flag = False

        	for jewel in jewels:
        		
        		if jewel == stone:
        			count +=1
        			flag = True
        			break

        return count

sol = Solution()
print(sol.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
print(sol.numJewelsInStones(jewels = "z", stones = "ZZ"))