# List Comprehensions

# Can we clean this up?
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# YES. Using Comprehensions
# list = [param for param in iterable]

comp_list = [char for char in 'hello']
print(comp_list)

# List of numbers, ranging from 0 to 99?
hund_list = [num for num in range(100)]
print(hund_list)

# Same list as above, but list should be multiplied by 2
two_hund_list = [num*2 for num in range(0, 100)]
print(two_hund_list)

# even two hund list?
even_two_hund_list = [num*2 for num in range(0, 100) if num % 2 == 0]
# essentially, param, for-loop, if condition to return param
print(even_two_hund_list)

# Set Comprehensions
# Identical format to above. Just change from [] to {}

# Dictionary Comprehensions
#new_dict = { param for param in old_dict}

simple_dict = {
    'a': 1,
    'b': 2
}
my_dict = {key: value**2 for key, value in simple_dict.items()}
print(my_dict)

# add new values to dictionary only when even

even_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}
print(even_dict)

# can you construct a dictionary with a comprehension, such that
# the item is the key, and the item multipled by two is the value
# of a list [1,2,3]

comp_dict = {num: num*2 for num in [1, 2, 3]}
print(comp_dict)

# can you write a comprehension that takes a list of characters, removes duplicates, and renders a new list?

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)


duplicate_remover = [char for char in some_list if some_list.count(char) > 1]
print(duplicate_remover)
# change it so that the list only records each char once

print(list(set(duplicate_remover)))
