def csFindTheSingleNumber(nums):
    # takes in non-empty array of ints [-1, 20, 14, ...]
    # one element appears once; the rest more times
    # find and return the lone wolf
    #
    # for int int in nums:
    # implement two sets: one to put ints in first, another
    # to move them to if there's >1 of them. Each lookup, removal,
    # and addition will be O(1), with the overall n times making
    # it O(n)
    #
    first = set()
    second = set()
    for i in range(len(nums)):
        if nums[i] in second:
            continue
        elif nums[i] in first:
            # remove from first, add to second
            first.remove(nums[i])
            second.add(nums[i])
        else:
            first.add(nums[i])
    a = [num for num in first]
    return a[0]