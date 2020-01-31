# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the
# program: 8 Then, the output should be:40320


def factorial(num):
    count = 0
    total = 1
    while count <= num:
        multiplier = num
        total *= multiplier
        num -= 1
        count += 1
    print(total)


factorial(5)
