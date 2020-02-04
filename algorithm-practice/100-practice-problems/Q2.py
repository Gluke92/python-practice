# Write a program which can compute the factorial of a given numbers.
# Suppose the following input is supplied to the
# program: 8 Then, the output should be:40320

n = int(input())

# while loop


def factorial(n):
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print(fact)

# for loop


def fact2(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)


def fact3(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)


# factorial(n)
# fact2(n)
lambda_fact3(n)
