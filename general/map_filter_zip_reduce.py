my_list = [1,2,3]
your_list = [10,20,30]
their_list = [5,4,3]

# map
def multiply_by2(item):
	return item * 2


print(list(map(multiply_by2, my_list)))
print([i * 2 for i in my_list])  # list comprehension

# filter

def only_odd(item):
	return item % 2 != 0
	
print(list(filter(only_odd,my_list)))

# zip

print(list(zip(my_list,your_list,their_list)))

# reduce
from functools import reduce

def accumulator(acc,item):
	print(acc,item)
	return acc + item

print(reduce(accumulator,my_list,0))