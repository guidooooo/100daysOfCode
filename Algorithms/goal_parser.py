
#You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

#Given the string command, return the Goal Parser's interpretation of command.

alphabet = {
	"G" : "G",
	"()" : "o",
	"(al)" : "al"
}

class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        letters = ""
        word = list(command)
        result = ""
        
        while len(word) >0:

        	letters += word.pop(0)
        	
        	if letters in alphabet:
        		result += alphabet[letters]
        		letters=""

        return result

sol = Solution()
print(sol.interpret("(al)G(al)()()G"))