class Category:

	

	def __init__(self, name):
		self.name = name
		self.ledger = []
		self.funds = 0.00

	def __repr__(self):
		result = f'{self.name.center(30, "*")}\n'
		
		for line in self.ledger:
			result += f'{line["description"][:23].ljust(23)}{str(line["amount"]).rjust(7)}\n'
		
		result += f"Total: {self.funds}"

		return result

	def deposit(self, amount, description = ''):
		
		deposit_dic = {"amount": amount, "description": description}
		self.ledger.append(deposit_dic)

		self.funds += amount

		return True

	def withdraw(self, amount, description = ""):

		if not self.check_funds(amount): return False

		self.funds -= amount
		withdraw_dic = {"amount": amount*-1, "description": description}
		self.ledger.append(withdraw_dic)

		return True

	def get_balance(self):
		return self.funds

	def transfer(self, amount, category_to):
		if not self.check_funds(amount): return False

		self.withdraw(amount, f"Transfer to {category_to.name}")
		category_to.deposit(amount, f"Transfer from {self.name}")

		return True

	def check_funds(self, amount):
		if self.funds < amount: 
			return False 
		else:
			return True


def create_spend_chart(categories):
	
	result = ''
	total_funds = 0
	max_name_length = 0
	name_lst = []
	for category in categories:
		total_funds += category.get_balance()
		if len(category.name) > max_name_length:
			max_name_length = len(category.name)
		name_lst.append(category.name)

	graph_dic = {}
	for category in categories:
		graph_dic[category.name] = int((category.funds * 100 / total_funds) /10) * 10


	result = "Percentage spent by category\n"
	for n in range(100,-1,-10):
		result += str(n).rjust(3) + '| '
		points_lst = [True if perc >= n else False for perc in graph_dic.values()]
		for point in points_lst:
			if point: 
				result += 'o'.ljust(3) 
			else: 
				result += ''.ljust(3)

		result += '\n'

	result += '    ----------\n'

	for x in range(max_name_length):

		result += '     '

		for n in range(len(name_lst)):

			if len(name_lst[n]) > x:
				result += name_lst[n][x].ljust(2)
			else:
				result += ''.ljust(2)

			result += ' '

		result +='\n'	


	result = result[:-2]

	return result


food = Category("food")
print(food.get_balance())
print(food.deposit(1000, "ingreso 1"))
print(food.get_balance())
cloths = Category("cloths")
food.transfer(310.80, cloths)	

print(f"Food Balance {food.get_balance()}")
print(f"Cloths Balance {cloths.get_balance()}")

auto = Category("auto")
print(auto.deposit(500, "ingreso 2"))
auto.withdraw(100, "rueda")

print(create_spend_chart([food, cloths, auto]))