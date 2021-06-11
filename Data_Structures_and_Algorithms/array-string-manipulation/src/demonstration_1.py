"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here
    pass


#
##
### HOMEWORK
##
#


# def buyAndSellStock(prices):
#     # takes in array of integers
#     # each integer is the price on a day
#     # beware off-by-one errors, we're 0 indexed. There is a 0th day.
#     # Rule: buy then sell, only once
#     # find max possible profit (buy - sell)
#     # assume no fees
#     # if prices drop monotonically, return 0
#     #
#     #
#     # it only makes sense to keep track of the global lowest
#     # and local highest. When you hit a new global low, clear the
#     # local high and restart difference comparison
#     global_min = 0
#     if prices:
#         global_min = prices[0]
#     local_max = 0
#     profit = 0
    
#     for price in prices:
#         if price < global_min:
#             # store profit
#             if local_max - global_min > profit:
#                 profit = local_max - global_min
#             # clear local_max
#             local_max = 0
#             # reset global_min
#             global_min = price
#         if price > local_max:
#             local_max = price
#             # local_max gets set to 0 and then to price every time a new global min is reached.
            
#         # return whichever is higher, the current local_max - global_min or profit.
#     return max(local_max - global_min, profit)

# jeremy's
# def buyAndSellStock(prices):
#     if not prices:
#         return 0
#     max_prof = 0
#     min_price = prices[0]
#     for i in range(1, len(prices)):
#         if prices[i] < min_price:
#             min_price = prices[i]
#         max_prof = max(max_prof, prices[i] - min_price)
#     return max_prof

#print(buyAndSellStock([3,8,100,10,11]))


# def alphabeticShift(inputString):
#     # takes in string of lowercase english letters, len <= 1000 
#     # replace each with the next character, (z with a)
#     # 
#     # for char in input
#     # new_str.append(mapped_char)
#     # make a dict, then mapped_char = dict[char]
#     # this has been done. ASCII is chr() and ord()
#     new_str = ''
#     for char in inputString:
#         if char == 'z':
#             new_str += 'a'
#         else:
#             new_str += chr(ord(char) + 1)
#     return new_str


# print(alphabeticShift('abcd'))
# print(alphabeticShift('xyz'))
# print(alphabeticShift('isaac'))

# def validParenthesesSequence(s):
#     # takes in string of parentheses '(' and ')'
#     # see if it's regular
#     #
#     # keep track of left count and right count...
#     # 
#     count = 0
#     for char in s:
#         if count < 0:
#             return False
#         if char == '(':
#             count += 1
#         if char == ')':
#             count -= 1
#     if count == 0:
#         return True
#     return False