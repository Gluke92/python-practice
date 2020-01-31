# With a given integral number n, write a program to generate a dictionary
# that contains (i, i x i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
# Test input: 8
#Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


def comp_square():
    n = int(input('Give me a number!'))

    print({x: x**2 for x in list(range(1, n+1))})


comp_square()

# Alternative
# n = int(input())
# ans = {}
# for i in range(1, n+1):
#     ans[i] = i * i #key-value assignment to empty array
# print(ans)
