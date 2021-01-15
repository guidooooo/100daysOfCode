
#You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

#Return the number of consistent strings in the array words.

class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        result = len(words)
        for word in words:

        	for letter in word:
        		if letter not in allowed:
        			result -=1
        			break

        return result

sol = Solution()
print(sol.countConsistentStrings(allowed = "ab", words = ["ad","bd","aaab","baa","badab"]))
print(sol.countConsistentStrings(allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]))
print(sol.countConsistentStrings(allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]))