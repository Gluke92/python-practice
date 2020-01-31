# Recursion

# Reversing a string
##This implements two pointers, and uses them to migrate towards the center.
##At each step, if left is at a location < right, we swap the values.
##We don't care about the value of the value, as much as getting the value to its parallel in the string

def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left, right = left + 1, right - 1
    return s

#not in place
def reverseString2(s):
    return s[::-1]ls

#not in place
def reverseString3(s):
    empty = []
    for i in range(len(s) - 1, -1, -1):
        empty.append(s[i])
    return empty

