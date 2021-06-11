"""
Challenge #7:

Given an unsorted list, create a function that returns the nth smallest element
(the smallest element is the first smallest, the second smallest element is the
second smallest, etc).

Examples:
- nth_smallest([7, 5, 3, 1], 1) ➞ 1
- nth_smallest([1, 3, 5, 7], 3) ➞ 5
- nth_smallest([1, 3, 5, 7], 5) ➞ None
- nth_smallest([7, 3, 5, 1], 2) ➞ 3
"""
def nth_smallest(lst, n):
    # take in an unsorted list
    # take in n
    # search for the nth smallest element and return it
    # What is the scale? Fair to assume integers?
    smallest = 10000
    shrinking_lst = []
    for i in lst:
        if i < smallest:
            smallest = i
            shrinking_lst.append(i)
    print(shrinking_lst)
    return shrinking_lst[-n]


tester_lst0 = [7, 5000, 32, 1]
tester_lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tester_lst2 = [50,49,48,47,46]

print(nth_smallest(tester_lst2, 7))
