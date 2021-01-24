#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ''
        for n in str[:]:

        	ascii_value = ord(n)

        	if ascii_value<97 and ascii_value >=65:
        		result += chr(ascii_value+32)
        	else:
        		result += n
        return result


sol = Solution()
print(sol.toLowerCase("Hello"))
print(sol.toLowerCase("here"))
print(sol.toLowerCase("LOVELY"))

"""
print(ord('a'), ord('A'), ord('a')-ord('A'))
print(ord('b'), ord('B'), ord('b')-ord('B'))
print(ord('z'), ord('Z'), ord('z')-ord('Z'))
print(ord('m'), ord('M'), ord('m')-ord('M'))
print(ord('j'), ord('J'), ord('j')-ord('J'))
"""