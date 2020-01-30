#map, filter, zip, reduce
from functools import reduce
my_list = list(range(10))
print(f'Original: {my_list}')

# Map - takes 2 args: fn, li -> transformed map object, where elem in map is x in fn(x).
# If you want the list, you need to use list function on object.


def double(item):
    return item*2


# should yeild 10 elements, each multiplied by 2
print(f'Map: {list(map(double, my_list))}')

# Filter - 2 args: boolean function, and list => transform the list


def only_even(item):
    return item % 2 == 0


print(f'Filter: {list(filter(only_even, my_list))}')

# Zip - unlimited list arguments, lists must be of same length => zips into new list of tuple pairs
zip_list = list(zip(my_list, list(range(10)) * 2))
print(f'Zip: {zip_list}')
# unclear on use case

# Reduce - 3 args (initial will be default to 0): accumulator function, list, and initial value


def accumulator(acc, item):
    return acc + item


reduce_list = reduce(accumulator, my_list, 0)
print(f'Reduce: {reduce_list}')


# ---Exercises----

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def capitalize(word):
    return word.capitalize()


print(list(map(capitalize, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]


def getKey(item):
    return item[1]


zip_list = list(zip(my_strings, my_numbers))

print(sorted(zip_list, key=getKey))
# Woah. Ok. https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/
# Basically, sorted has a default value assigned for the key argument. You can redefine the key to target a particular index of the tuple/list

# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def over_fifty(x):
    return x > 50


print(list(filter(over_fifty, scores)))

# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?


def accumulator(acc, item):
    return acc + item


combined = my_numbers.append(scores)
print(reduce(accumulator, scores, my_numbers))

# --Solutions--

# Only differences are in 3 and 4. For 3, you can use no argument for sorted and should work
# 4.


def accumulator(acc, item):
    return acc + item


print(reduce(accumulator, (my_numbers + scores)))

# Really close! Just needed to create a new list by adding them together
