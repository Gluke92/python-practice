# Write a program which will find all such numbers
# which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).The numbers obtained
# should be printed in a comma-separated sequence on a
# single line.

##Output is comma-separted sequence of numbers on a single line
##Range: 2000, 3200 [inclusive]
##Dvisible by 7, and not multiple of 5

num_list = [str(x) for x in range(2000, 3201) if x % 7 == 0 and x % 5 != 0]
str_list = ', '.join(num_list)
print(str_list)

##Author's solution
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print("\b")
