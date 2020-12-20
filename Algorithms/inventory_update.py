# Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. 
# Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array. 
# The returned inventory array should be in alphabetical order by item.

def updateInventory(arr1, arr2):

	inv_item_index = [item[1] for item in arr1]

	for item in arr2:

		item_qty = item[0]
		item_name = item[1]

		try:
			index = inv_item_index.index(item_name)
			arr1[index][0] += item_qty
		except:
			arr1.append([item_qty, item_name])


	return sorted(arr1, key = lambda x : x[1], reverse = False)




# Example inventory lists
curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

print(updateInventory(curInv, newInv));

print(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]))

print(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], []))

print(updateInventory([], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]))

print(updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]))
