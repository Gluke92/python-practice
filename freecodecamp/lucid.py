# Lucid Programming

# Binary Search
data = [2, 4, 5, 7, 8, 9, 12, 14, 17, 19, 22, 25, 27, 28, 33, 37]
target = 25

# Linear Search


def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

# Recursive Binary Search


def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target == data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)


print(linear_search(data, target))
print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data) - 1))
#-------------------------#

# Recursion - find first uppercase character, given string

# Iterative

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"


def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return "No uppercase character found"


print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))


def find_uppercase_recursive(input_str, idx=0):
    # Send index into prototype to go on ahead of loop
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return "No uppercase character found"
        # Recursive step
    return find_uppercase_recursive(input_str, idx+1)


print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))

# ----
# Given a string, calculate the length of the string.

input_str = "LucidProgramming"

print(len(input_str))


def iterative_str_len(input_str):
    count = 0
    for char in input_str:
        count += 1
    return count


def recursive_str_len(input_str):
    # what is the base case?
    # What is the recursion going to call?
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])


print(iterative_str_len(input_str))
print(recursive_str_len(input_str))

# Given a string, count the number of consonants.
# Consonant =/ vowel (a,e,i,o,u)


def count_consonants_iterative(inp_str):
    vowel_key = ['a', 'e', 'i', 'o', 'u']
    count = 0
    inp_str = inp_str.replace(' ', '').lower()
    for char in inp_str:
        if char not in vowel_key and char.isalpha():
            count += 1
    return count


input_str_1 = "abc de"
input_str_2 = 'LuCiDProGrAmMiNG'
print(count_consonants_iterative(input_str_1))
print(count_consonants_iterative(input_str_2))


def count_consonants_recursive(inp_str):
    vowel_key = ['a', 'e', 'i', 'o', 'u']
    if inp_str == '':
        return 0

    if inp_str[0].lower() not in vowel_key and inp_str[0].isalpha():
        return 1 + count_consonants_recursive(inp_str[1:])
    else:
        return count_consonants_recursive(inp_str[1:])


print(count_consonants_recursive(input_str_1))
print(count_consonants_recursive(input_str_2))

##----##
# Product of two numbers
# Given two numbers find their product using recursion


def recursion_product(a, b):
    # if both are negative, flip won't work, so reassign both to positives
    if a < 0 and b < 0:
        a *= -1
        b *= -1

    if b < a:  # if either a or b is negative, this will flip the number
        # reduces risk of overflow
        return recursion_product(b, a)

    # run again logic
    if b == 0:
        return 0
    return a + recursion_product(a, b-1)


print(recursion_product(-3, -3))

#--#
# look and say sequence; given one string, we generate the next

# 1
# 11
# 21
# 1211
# 111221

# so, given "1" we should return "11" ('one one' 'COUNT value')
# there is "count" which tells us the number of "the next value"
# "count" and "next value" need to be generated


def next_number(s):
    result = []
    i = 0
    # first loop will get us through string
    while i < len(s):
        count = 1

        # this inner loop will evaluate if the string is more than base case
        # AND if value is a COUNT term, or a value
        # if the term is a COUNT, count will increment, and we'll move along
        # we know if something is COUNT value, if 1) we haven't hit the end AND 2) the next value is not the same as count
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])  # first case: ONE + one
        i += 1
        # move to next value
    return ''.join(result)


s = '1'
n = 4
for i in range(n-1):
    s = next_number(s)
    print(s)

# ---
# Spreadsheet column id to a number script
# if we return a -> 1, z -> 26, AA is 27


def string_processor(col_str):
    num = 0
    count = len(col_str) - 1
    for s in col_str:
        # ord() is a function that gives us a starting point for each of the letters
        num += 26**count*(ord(s) - ord('A') + 1)
        count -= 1
    return num


# Encoding Tests
print(string_processor("A"))  # 1
print(string_processor("AA"))  # 27
print(string_processor("ZZ"))  # 52

# ---
# reading a palindrome

s = "Was it a cat I saw?"

# Solution uses extra space proportional to size of string
# s = ''.join([i for i in s if i.isalpha()]).replace(" ".'').lower()
#print(s == s[::-1])


def is_palindrome(s):
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True


s_1 = "Was it a cat I saw?"
s_2 = "Test"

# Testing
print(is_palindrome(s_1))  # true
print(is_palindrome(s_2))  # false


# -anagram checker
s1 = "fairy tales"
s2 = "rail safety"

s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()
# requires n log n time, b/c any comparison based soting algorithm requries at least n log n time to sort

# try a dictionary to store values


def is_anagram(s1, s2):
    ht = dict()
    # base case: check lenghts. If not same, not anagram
    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            return False

    return True


print(is_anagram(s1, s2))
print(is_anagram('why', 'yhw'))

#--greedy algorithm: optimal task assignment--#

# given array, with numbers, numbers correspond to hours at a task
# assign tasks to workers, assuming each worker is independent, such that total time is minimized
# 3 workers

# Given [6,3,2,7,5,5] -> 10 is minimum time (w1 (6,3), w2 (2,7), w3 (5,5))

# Brute force -> feed every possible pair (n!/(2^(n/2)))

# Greedy: Pair the longest with the shortest, until we run out of tasks

# Step 1: sort the tasks from least to greatest
# Step 2: pick the ends
# Step 3+: move inward until the list is empty
# Time compleixity is O(n log n) due to sorting


def greedy_sort(arr):
    A = sorted(arr)
    if len(A)/2 % 2 != 0: 
        for i in range(len(A)//2):
            # bit-wise complmement -> x -> (-x-1) 3, -4 -> used for this type of pointer movement [0] -> [-1]
            print(A[i], A[~i])
    else:
        return ("Array is not even; someone's working an odd number")

greedy_sort([7,3,2,6,5,5])


##--Given 2 lists, calculate the intersection between the lists (set of elements in common between the two)


S1 = [2,3,3,5,7,11]
S2 = [3,3,7,15,31]

print(set(S1).intersection(S2))

#create two iterators, i and j, to track index/values of each list
#increment i, when values at i and j are not equal
#if not equal, and if index of i-1 is not holding a value equal to index at i, store value in unique list
#increment i and j
#do the same scan; is i at a new value, or have we seen this before?
#if i < j, advance i; if j < i, advance j
#if end of length of S1 or length of S@, and i = len(S1) or j = len(S2), then break
#Big(O(n)) = N

def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if i == 0 or A[i] == B[j]:
            if A[i] != A[i-1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else: 
            #B[j] < A[i]:
            j += 1
    return intersection 

print(intersect_sorted_array(S1, S2))

#--Given a string, check if its a permutation of a palindrome - a rearrangement of a palindrome (racecar -> acecarr)

palin_perm = "Tact Coa"
not_palin_perm = "this is not a palindrome permutation"

#if letters are in pairs, with only one unique, the chars can be arranged into a permutation of a palindrome

def is_palin_perm(input_str):
    input_str = input_str.replace(" ", '').lower()
    d = dict()

    for i in input_str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
    odd_count = 0
    for k,v in d.items():
        if v % 2 != 0 and odd_count == 0:
            odd_count += 1
        elif v % 2 != 0 or odd_count != 0:
            return False
    
    return True

print(is_palin_perm(palin_perm)) #True
print(is_palin_perm(not_palin_perm)) #False

#---Given two strings write a method to decide if one is a permutation of the other. Spaces are extra characters.

is_permutation_1 = "god"
is_permutation_2 = "dog"

not_permutation_1 = "not"
not_permuation_2 = "top"

def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    #nlogn for sorting algo 
    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)
    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    return True

print(is_perm_1(is_permutation_1, is_permutation_2)) #True
print(is_perm_1(not_permutation_1, not_permuation_2)) #False

def is_perm_2(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    count = {}
    for i in str_1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    for i in str_2:
        if i in count:
            count[i] -= 1
        else:
            return False
    
    return all(count == 0 for count in count.values()) #final check

    #use a hashtable


