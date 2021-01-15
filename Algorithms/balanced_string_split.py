#Balanced strings are those who have equal quantity of 'L' and 'R' characters.

#Given a balanced string s split it in the maximum amount of balanced strings.

#Return the maximum amount of splitted balanced strings.


class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        r_count, l_count = 0, 0
        for letter in s:

        	if letter == 'R': 
        		r_count +=1
        	else:
        		l_count +=1

        	if r_count == l_count:
        		result +=1
        		r_count, l_count = 0, 0

        return result


sol = Solution()
print(sol.balancedStringSplit(s = "RLRRLLRLRL"))
print(sol.balancedStringSplit(s = "RLLLLRRRLR"))
print(sol.balancedStringSplit(s = "LLLLRRRR"))
print(sol.balancedStringSplit(s = "RLRRRLLRLL"))

