def findRelativeRanks(nums):
    sort = sorted(nums)[::-1]
    rank = ["Gold Medal", "Silver Medal", "Bronze Medal"] + list(map(str, range(4, len(nums) + 1)))
    return list(map(dict(zip(sort, rank)).get, nums))

#print(findRelativeRanks([1,3,2,6,4,8,90,65]))


# unpacking the return statement
# we zip sorted scores and their ranks together, put em in a dict
# We get those items and map them to nums

l1 = ['a', 'b', 'c', 'd']
l2 = [10, 12, 13, 0]

lst = [10,12]
