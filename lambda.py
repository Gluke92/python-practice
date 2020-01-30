# lambda expressions- anonymous functions that we pass in so that
# we reduce memory storage

from functools import reduce
my_list = list(range(0, 5))

# filter using lambda: evens

print(list(filter(lambda x: x % 2 == 0, my_list)))

# reduce using lambda
print(reduce(lambda acc, num: acc + num, my_list))

# square the list
new_list = [5, 4, 3]
print(list(map(lambda x: x**2, new_list)))

# sort the tuple list
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(list(sorted(a, key=lambda x: x[1])))
