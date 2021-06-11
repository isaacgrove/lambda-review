"""
Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to the `target`.

Examples:

- two_sum(nums = [2,5,9,13], target = 7) -> [0,1] (nums[0] + nums[1] == 7)
- two_sum(nums = [4,3,5], target = 8) -> [1,2] (nums[1] + nums[2] == 8)

Notes:

- Each input will have only one solution.
- You may not use the same element twice.
- You can return the answer in any order.
"""
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # takes in list of ints as fodder, and a target int
    # two fodder ints will add up to the target
    # return their indices in a list
    #
    # start with an empty list
    # for int in list, for int in list, if sum i, j == target, append i, j to that list
    lst = []
    for i in nums:
        if lst:
            return lst
        else:
            idx = nums.index(i)
            for j in nums[idx:]:
                # question: we can't use the same element twice - can we use different elements of the same value?
                # --> can change 2nd condition below to i != j
                if i + j == target and nums.index(i) != nums.index(j): 
                    lst.append(nums.index(i))
                    lst.append(nums.index(j))
    return lst

num1 = [2,5,9,13]
num2 = [4,3,5]
num3 = [0,1,2,3,4,5,6,7,8,9,10,11]



def second_pass(nums, target):
    #
    # start with an empty dictionary
    # go through the list and store each number as a key, and its index as the value
    # Why? because then we can access numbers in O(1)
    # then go through the list checking if the number we need (target - nums[i]) is in the dict (as a key)
    dct = {}
    for i in range(len(nums)):
        dct[nums[i]] = i
    for i in range(len(nums)):
        check = target - nums[i]
        if check in dct and dct[check] != i:
            return [i, dct[check]]
    return 'match not found'

print(second_pass(num1, 7))
print(second_pass(num2, 8))
print(second_pass(num3, 21))