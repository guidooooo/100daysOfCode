# Create a function that takes two or more arrays and returns an array of their symmetric difference. 
# The returned array must contain only unique values (no duplicates).

def sym(*args):

	result =[]
	count_dic = {}

	params_qty = len(args)

	list0 = []

	for n in range(params_qty):
		list1 = list(set(args[n]))
		for m in list1:
			if m in list0:
				list0.remove(m)
			else:
				list0.append(m)
		

	return sorted(list0)

print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]))
print(sym([1, 2, 3], [5, 2, 1, 4]))
print(sym([1, 2, 3, 3], [5, 2, 1, 4]))
print(sym([1, 2, 5], [2, 3, 5], [3, 4, 5]))
print(sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5]))
print(sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3]))