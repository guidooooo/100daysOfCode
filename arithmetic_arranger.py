def arithmetic_arranger(math_list, answer = False):

	if len(math_list) > 5:
		return "Error: Too many problems."

	allowed_operator_lst = ['+','-']

	arithmetic_lst = []

	result = ''

	for math in math_list:

		math_dict = {}

		# Spliting formula
		math_parts = math.split()

		# Checking if they are numbers and saving them
		try:
			math_dict["num1"] = int(math_parts[0])
			math_dict["num2"] = int(math_parts[2])
		except:
			return "Error: Numbers must only contain digits."

		# Checking numbers length
		if math_dict["num1"]>9999 or math_dict["num2"]>9999 : return "Error: Numbers cannot be more than four digits."

		# Checking valid operators
		op = math_parts[1]

		if op in allowed_operator_lst:
			math_dict["operator"] = op
		else:
			return "Error: Operator must be '+' or '-'."

		# Saving Results
		math_dict["result"] = math_dict["num1"] + math_dict["num2"] if math_dict["operator"] == '+' else math_dict["num1"] - math_dict["num2"]

		# Saving max length to create final dashes
		math_dict["max_length"] = len(str(math_dict["num1"])) if len(str(math_dict["num1"]))>=len(str(math_dict["num2"])) else len(str(math_dict["num2"]))

		arithmetic_lst.append(math_dict)

	# First Line
	for math in arithmetic_lst:
		result += str(math["num1"]).rjust(math["max_length"]+2)
		result += ''.ljust(4)
	result = result[:-4]
	result += '\n'

	# Second Line
	for math in arithmetic_lst:
		result += math["operator"] + ' '
		result += str(math["num2"]).rjust(math["max_length"])
		result += ''.ljust(4)
	result = result[:-4]
	result += '\n'

	# Third Line
	for math in arithmetic_lst:
		result += ''.rjust(math["max_length"]+2,'-')
		result += ''.ljust(4)
	result = result[:-4]

	# Results if answer is True
	if answer:
		result += '\n'
		for math in arithmetic_lst:
			result += str(math["result"]).rjust(math["max_length"]+2)
			result += ''.ljust(4)
		result = result[:-4]

	return result