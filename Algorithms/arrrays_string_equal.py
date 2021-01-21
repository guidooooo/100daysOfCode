"""Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.
"""


class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        return ''.join(word1) == ''.join(word2)

sol = Solution()
print(sol.arrayStringsAreEqual(word1 = ["ab", "c"], word2 = ["a", "bc"]))
print(sol.arrayStringsAreEqual(word1 = ["a", "cb"], word2 = ["ab", "c"]))
print(sol.arrayStringsAreEqual(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]))