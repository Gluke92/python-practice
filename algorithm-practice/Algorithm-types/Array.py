# Array practice

#Problem 1:

def removeDuplicates(nums):
    if (len(nums) != 0):
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        print(i + 1)
        return i + 1

removeDuplicates([1,1,2,2,3,4,5,8,8,9,9,10,10,10,11])


# #Alternate Syntax 
# nums[:] = sorted(set(nums))
# return len(nums)

#Problem 2: Given an array of stock prices, output the max profit
#If no transaction can yield profit, return 0

#use a for-loop to cycle through each value
#

#This solution is a brute force approach
def maxProfit(self, prices):
    res = 0
    for profit in map(lambda x, y: y-x, prices[:-1], prices[1:]):
        res = max(res, res+profit)
    return res

#This solution is a step-wise checker
def maxProfit2(self, prices) -> int:
    profit = 0
    for i in (range(len(prices) - 1)):
        for j in (i+1, range(len(prices))):
            if prices[j] < prices[i]:
                break
            else:
                profit += prices[j] - prices[i]
                i = j
                break
    return profit


#optimized version of above:
# maxProf = 0
# for i in range(1, len(prices)):
#     if (prices[i] > prices[i-1]):
#         maxProf += (prices[i] - prices[i-1])
#         return maxProf


#Problem 3, given two inputs, list, and some number, k.

nums = [1,2,3,4,5,6,7]
new_nums = nums[-3:] + nums[:-3]
print(new_nums)
