# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]



import numpy as np

def calculate(list):

	if len(list) != 9 :
		raise ValueError("List must contain nine numbers.")

	calculations = {}

	np_array = np.array(list)
	np_array = np_array.reshape((3,3))

	operation_dict = {
		'mean': np.mean, 
		'variance': np.var, 
		'standard deviation': np.std,
		'max': np.max,
		'min': np.min,
		'sum': np.sum
		}

	for operation_name, function in operation_dict.items():
		result_lst = []

		for n in range(2):
			result_lst.append(np.apply_along_axis(function, n, np_array).tolist())

		result_lst.append(function(np_array))

		calculations[operation_name] = result_lst

	return calculations