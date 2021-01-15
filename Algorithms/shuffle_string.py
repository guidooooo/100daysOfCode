#Given a string s and an integer array indices of the same length.

#The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

#Return the shuffled string.


class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        phrase = ['' for n in range(len(indices))]

        for index, letter in enumerate(s):
        	phrase[indices[index]] = letter

        return ''.join(phrase)


sol = Solution()
print(sol.restoreString( s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
print(sol.restoreString( s = "abc", indices = [0,1,2]))

print(sol.restoreString( s = "aiohn", indices = [3,1,4,2,0]))
print(sol.restoreString( s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]))
print(sol.restoreString( s = "art", indices = [1,0,2]))

