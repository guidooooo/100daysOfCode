
print("Filter only negative and zero in the list using list comprehension")

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

print([x for x in numbers if x >0])

print("Flatten the following list of lists of lists to a one dimensional list :")

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

print( [x for lists in list_of_lists for list_one in lists for x in list_one])

print("Using list comprehension create the following list of tuples:")


print([(x, x**0, x**1, x**2, x**3, x**4, x**5) for x in range(11)])

print("Flatten the following list to a new list:")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]


print(  [x.upper() for country_list in countries for country, capital in country_list for x in [country, capital]])

print("Change the following list to a list of dictionaries:")

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print([{'country': country.upper(), 'city': capital.upper()} for country_list in countries for country, capital in country_list])

print("Change the following list of lists to a list of concatenated strings:")

names = [[('Asabeneh', 'Yetaeyeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print([first + ' ' + last for name in names for first, last in name	])