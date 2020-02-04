# Given 2 strings, check to see if anagram (if rearrangement
# of characters is equal to original stirng

# i.e., "public relations" can be "crap built on lies"
# i.e., "clint eastwood" is " old west action"


def anagram(s1, s2):

    # Remove spaces and lowercase letters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # take advantage of pre-built function to rearrange words, and use boolean
    return sorted(s1) == sorted(s2)

# This isn't optimal b/c of python module


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}
    for letters in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count:
        if count[k] != 0:
            return False

    return True

    # ----
# Array Pair Sum
# Given an array, output all the unique pairs that sum up to
# a value
# pair_sum([1,3,2,2], 4) => returns (1,3) and (2,2)


def pair_sum(array, k):
    if len(array) < 2:
        return print("Too small")

    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)

        else:
            output.add((min(num, target), max(num, target)))

    print('\n'.join(map(str, list(output))))


pair_sum([1, 3, 2, 2, 1, 5, 6, -2], 4)

## Largest Sum
#Take an array with positive and negative integers and find the max sum of that array

def largest(arr):
    if len(arr) == 0:
        return print('Too small')

    #create two counter pointers to the first index
    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    
    return max_sum

print(largest([7,1,2,-1,3,4,10,-12, 3, 21, -19]))
    
##How to reverse a string

#Given a string of words, reverse all the words

# start-"This is the best"
# finish-"best the is This"


def reverse(s):
    return " ".join(reversed(s.split()))

#print(reverse("This is the best"))

def reversed2(s):
    return " ".join(s.split()[::-1])

def reversed3(s):
    #Memorize this!

    length = len(s)
    spaces = [' ']
    words = []
    #Get an index tracker
    i = 0
    while i < length:
        if s[i] not in spaces:
            #maintain the letter
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1

            words.append(s[word_start: i])

        i += 1

    return " ".join(reversed(s))
#Reverses letters and words

def reverse4(s):
    return s.split()[::-1]

##Array Rotation/Analysis

#Given 2 arrays (no duplicates) is 1 array a rotation
#of another? return True/False
#Same size and elements, but start index is different

#BigO(n) we are going through each array twice, but O(2n) = O(n)

#select an indexed position in list 1 and get its value
#check index from tehre
#if any variation then we know its false
#Getting to last item without a false means true

def rotation(list1, list2):
    if len(list1) != len(list2):
        return False

    key = list1[0] #1
    key_index = 0

#match the first value in list 1 to the right index holding that value
#in list 2. Store that index
    for i in range(len(list2)):
        if list2[i] == key: #if list1 and list2 have the same value, return the index in list 2
            key_index = i 

            break

#is the rotation an identitical list? If so, no rotation
    if key_index == 0:
        return False

    for x in range(len(list1)):
        two_index = (key_index + x) % len(list1)
        #great formula to cycle, using modulo
        #0 + some value & 7 -> 0 (1,2,3,4,5,6,1)?

        if list1[x] != list2[two_index]:
            #if the inner position of x does not match the value at the new position
            #return false
            return False
    
    return True

print(rotation([1,2,3,4,5,6,7], [4,5,6,7,1,2,3]))

# for x in range(15):
#     print (f'{x % 7}')

## Array of Common Elements
##E.g, [1,3,4,6,7,9] and [1,2,4,5,9,10] => [1,4,9]

def common_elements(a,b):
    p1 = 0
    p2 = 0 

    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 +=1 
            p2 += 2

        elif a[p1] > b[p2]:
            p2 += 1

        else: #if value at a is smaller than b
            p1 += 1
    return result

print(common_elements([1,3,4,6,7,9], [1,2,4,5,9,10]))

##Minesweeper 
##Write a function with three argumens:
#bomb locations, rows_of_grid, columns_of_grid
#mine_sweeper([[0,0],[1,2]], 3, 4)

#bomb at row index 0 column index 0
#bomb at row index 1 column index 2

#we should return a 3 x 4 array (-1) = bomb

def mine_sweeper(bombs, num_rows, num_cols):
    field= [[0 for i in range(num_cols)] for j in range(num_rows)] #creates grid
    
    #fills field with bombs
    for bomb_location in bombs:
        (bomb_row, bomb_col) = bomb_location
        field[bomb_row][bomb_col] = -1
    
    row_range = range(bomb_row - 1, bomb_row + 2)
    col_range = range(bomb_col - 1, bomb_col + 2)

    for i in row_range:
        current_i = i

        for j in col_range:
            current_j = j
            if (0 <= i < num_rows and 0 <= j < num_cols and field[i][j] != -1):
                field[i][j] += 1
    return field

    print(field)


print(mine_sweeper([[0, 0], [1, 2]], 3, 4))

##Frequency Count
#zgiven an array, which is most frequently occuring element?:

def freq_arr(arr):
    count = {}
    max_count = 0
    max_item = []
    for elem in arr:
        if elem in count:
            count[elem] += 1
        else:
            count[elem] = 1
    
        if count[elem] > max_count:
            max_count = count[elem]

            max_item.append(elem)

    return max_item

print(max({1:8, 2:3, 3:4, 1:1}.items()))
#flaw if item


##Given a string, are all characters unique? Return True or False

def unique(string):
    string = string.replace(' ', '')
    return len(set(string)) == len(string)

##Do it without a built in function

def unique_two(s):
    s = s.replace(' ', '')
    characters = set()

    for letter in s:
        if letter in characters:
            return False
        else:
            characters.add(letter)
    return True

print(unique('a b cdef'))

##Non-repeat elements in an array

#Take a stirng, return character that never repeated
#If multiple uniques, return only first unique

def non_repeating(s):

    s = s.replace(' ', '').lower()
    char_count = {}

    for c in s:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1

    
    #how to return first unique? Use string as ordered list, and cycle through string list, correlated to dictionary
    # for c in s:
    #     if char_count[s] == 1:
    # #         return c
    
    # return None

    all_uniques =[]
    y = sorted(char_count.items(), key = lambda x: x[1])
    #sorted char_cont by the second index position, in ascending order
    
    for item in y:
        if item[1] == 1:
            all_uniques.append(item)

    return all_uniques

print(non_repeating('I Apple Ape Peels'))