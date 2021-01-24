"""
A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
"""
class Solution(object):
	def removeOuterParentheses(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		count = 0
		result = ''
		ss = []
		for s in S:
			
			if s == '(':
				count +=1
			else:
				count -=1
			ss.append(s)

			if count == 0:
				parentheses_num = s.count('(')
				result += ''.join(ss[1:-1])

				ss= []

		return result

sol = Solution()
print(sol.removeOuterParentheses("(()())(())"))
print(sol.removeOuterParentheses("(()())(())(()(()))"))
print(sol.removeOuterParentheses("()()"))