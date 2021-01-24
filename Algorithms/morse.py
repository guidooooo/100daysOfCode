"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.
"""

alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

count = 0
alphabet_dict = {}
for n in range(97,123):
	alphabet_dict[chr(n)] = alphabet[count]
	count+= 1

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_words = []
        for word in words:
        	morse_word = ''
        	for l in word:
        		morse_word += alphabet_dict[l]
        	morse_words.append(morse_word)

        unique_words = []
        for w in morse_words:
        	if w not in unique_words:
        		unique_words.append(w)

        return len(unique_words)


sol = Solution()
print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))