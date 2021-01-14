import re

# txt = 'I love to watch football'
# #re.I is case ignore
# match = re.match('I love to watch', txt, re.I)
# print(match)
# span = match.span()
# print(span)
# start, end = span

# print(start, end)

# substring = txt[start:end]
# print(substring)


# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''


# match = re.search('first', txt, re.I)
# print(match)
# start, end = match.span()

# print(txt[start:end])


# txt = '''Python is the most beautiful language that a human being has ever created.
# I recommend python for a first programming language'''

# match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.
# # OR
# match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.


# txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
# T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
# I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
# D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

# match = re.sub('%', '', txt)
# print(match)

# match ( solo si empieza el texto con el patron buscado)
# search ( devuelve el primer match y puede estar en cualquier parte)
# findall (devuelve una lista con todas las ocurrencias)
# sub ( replace patron buscado por el indicado)


# regex_pattern = r'apple'
# txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
# matches = re.findall(regex_pattern, txt)
# #print(matches)  # ['apple']

# # To make case insensitive adding flag '
# matches = re.findall(regex_pattern, txt, re.I)
# #print(matches)  # ['Apple', 'apple']
# # or we can use a set of characters method
# regex_pattern = r'[Aa]pple'  # this mean the first letter could be Apple or apple
# matches = re.findall(regex_pattern, txt)
# #print(matches)  # ['Apple', 'apple']


# txt = 'GAME_BONUS-23232bonus'

# match = re.findall(r'[^a-zA-z_]', txt)
# print(match)

# regex_pattern = r'[a].+'  # this square bracket means a and . means any character except new line
# txt = '''Apple and banana are fruits'''
# matches = re.findall(regex_pattern, txt)
# print(matches)  # ['an', 'an', 'an', 'a ', 'ar']



paragraph = '''I love teaching. If you do not love teaching what else can you love. 
I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'''

match = re.split(' ', paragraph)

words_dict = {}

for word in match:

	word = re.sub('[.,]','', word)

	words_dict[word] = words_dict.get(word,0) + 1

max_occur = sorted([(word, qty) for word, qty in words_dict.items()], key = lambda x : x[1] , reverse=True)[0]
print(max_occur)

txt = '''
The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.
'''

match = [int(x) for x in re.findall('[-]?[\d+]', txt)]
match = sorted(match)
print(match[-1]-match[0])


def is_valid_variable(string):

	pattern = '(^[^a-zA-z]|[^a-zA-z0-9_])'
	 #

	if re.search(pattern, string) is None:
		return True
	else:
		return False

print(is_valid_variable('first_name23233')) # True
print(is_valid_variable('first-name232323')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('first_name')) # True
print(is_valid_variable('23232_firstname')) # True


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


def clean_text(sentence):

	regex_pattern = '[^a-zA-Z0-9.,\? ]'
	new_sentences = re.sub(regex_pattern,'', sentence)
	print(new_sentences)

	words = re.split(' ', new_sentences)

	words_dict = {}
	for word in words:

		word = re.sub('[.,?]','', word)

		words_dict[word] = words_dict.get(word,0) + 1

	words_list = sorted([(word,qty) for word, qty in words_dict.items()], key = lambda x : (x[1],x[0]), reverse=True)[:3]

	return words_list



print(clean_text(sentence));