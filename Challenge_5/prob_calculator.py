import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **kwargs):
		self.contents = []
		for key, value in kwargs.items():
			# print("%s == %s" %(key, value)) 
			for n in range(value):
				self.contents.append(key)

	def __repr__(self):
		return f"{self.contents}"

	def get_contents(self):
		return self.contents

	def draw(self, draw_qty):

		result = []

		contents = self.get_contents()

		if draw_qty > len(contents):
			return contents

		draw_contents = contents

		for n in range(draw_qty):
			index = random.randint(0,len(draw_contents)-1)
			result.append(draw_contents[index])
			del draw_contents[index]

		return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

	success_qty = 0
	
	for n in range(num_experiments):
		hat_copy = copy.deepcopy(hat)
		# print(hat_copy)
		draw_result = hat_copy.draw(num_balls_drawn)
		# print(draw_result)
		success_fg= True
		for key, value in expected_balls.items():
			key_qty = draw_result.count(key)
			# print(key_qty, value)
			if key_qty < value:
				success_fg =False
				break

		if success_fg: success_qty +=1

		

	return success_qty/num_experiments