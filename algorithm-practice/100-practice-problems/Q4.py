# Write a program which accepts a sequence of
# comma-separated numbers from console and
# generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

# 34, 67, 55, 33, 12, 98
# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')


def tuple_list_gen():
    n = str(input('Give me some numbers, separated by numbers'))
    new_list = n.split(', ')
    new_tuple = tuple(new_list)
    print(new_list, new_tuple)


tuple_list_gen()
