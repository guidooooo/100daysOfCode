class Rectangle:
	
	def __init__(self, width, height):
		self.set_width(width)
		self.set_height(height)

	def __repr__(self):
		return f'Rectangle(width={self.get_width()}, height={self.get_height()})'

	def set_width(self, width):
		self.__width = width

	def set_height(self, height):
		self.__height = height

	def get_width(self):
		return self.__width

	def get_height(self):
		return self.__height

	def get_area(self):
		return self.get_width() * self.get_height()

	def get_perimeter(self):
		return 2 * self.get_width() + 2 * self.get_height()

	def get_diagonal(self):
		return (self.get_width() ** 2 + self.get_height() ** 2) ** .5

	def get_picture(self):

		width = self.get_width()
		height = self.get_height()

		if width > 50 or height > 50:
			return "Too big for picture."

		result = ''

		for n in range(width):
			# print("*", end='')
			result += '*'
		result += '\n'

		for m in range(1,height-1):
			# print("*".ljust(self.__width-2),'*')
			result += ''.ljust(width-1,'*') + '*\n'

		for n in range(width):
			# print("*", end='')
			result += '*'


		return result+'\n'

	def get_amount_inside(self, shape):
		
		sh_width = shape.get_width()
		sh_height = shape.get_height()

		width = self.get_width()
		height = self.get_height()


		if sh_width <= width:
			width_qty =  int(width / sh_width)
		else:
			return False

		if sh_height <= height:
			height_qty =  int(height / sh_height)
		else:
			return False

		return width_qty * height_qty


class Square(Rectangle):
	
	def __init__(self, side):
		self.set_side(side)

	def set_side(self, side):
		super().set_width(side) 
		super().set_height(side)

	def __repr__(self):
		return f'Square(side={self.get_width()})'

	def set_width(self, side):
		self.set_side(side)

	def set_height(self, side):
		self.set_side(side)