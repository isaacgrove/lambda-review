"""
Demonstration #2

Given a non-empty array of integers `nums`, every element appears twice except except for one. Write a function that finds the element that only appears once.

Examples:

- single_number([3,3,2]) -> 1
- single_number([5,2,3,2,3]) -> 5
- single_number([10]) -> 10
"""
def single_number(nums):
    # Your code here
    pass

def csFindAddedLetter(str_1, str_2):
    # takes in two strings
    # str_2 = str_1, shuffled, plus one letter somewhere.
    # return that letter
    #
    # so we have two strings of arbittary length that are identical except for one character
    # that character might be a repeat
    # 
    str1 = list(str_1)
    str2 = list(str_2)
    for char in str1:
        str2.remove(char)
    return str2.pop()

test1 = 'abcdefgaaaaa'
test2 = 'afdegcbaaahaa'

#print(csFindAddedLetter(test1, test2))


def csFirstUniqueChar(input_str):
    # takes in a string
    # return the index of the first character that doesn't repeat
    # else return -1
    dct = {}
    lst = []
    for char in input_str:
        if char not in dct:
            dct[char] = 0
            lst.append(char)
        else:
            if char in lst:
                lst.remove(char)
    if lst:
        return input_str.index(lst[0])
    return -1
    

# for char in str you could add it to a list and also into a dict
# then if you find that char again (i.e. if char in dict), remove it from the list
# 
# look at a character
# check if it's in the dictionary. If not, add it and add it to the list.
# {'a'} ['a']
# Next character is a 'b', Not in the dictionary. Added. {'a', 'b'} ['a', 'b']
# next character is an 'a'. It's in the dict, so if it's in the list, remove it. ['b']
# next is 'a'. In the dict. If it's in the list, remove it. (it isn't, so nothing happens)
# next is 'c'. Add to dict. Add to list. ['b', 'c']
# then 'd', 'e', 'f' --> ['b' cdef]
# then f --> in dict, remove from list bcde
# when done, return list[0]

print(csFirstUniqueChar('vvv'))
print(csFirstUniqueChar('ilovelambda'))
print(csFirstUniqueChar('lambdavelambda'))