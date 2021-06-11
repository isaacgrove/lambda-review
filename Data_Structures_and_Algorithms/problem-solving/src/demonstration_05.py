"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
def data_type(value):
    # Your code here
    pass


# def csReverseString(chars):
#     # takes in an array of characters
#     # return the reverse of that array
#     # must be "in-place", O(1) space complexity
#     # Many in-place functions do not return the modified input, but we should.
#     # try using 2 pointers.
#     #
#     # Maybe while pointer1 < pointer2, and starting them at the ends,
#     # switch their characters.
#     p1 = 0
#     p2 = len(chars) - 1
#     while p1 < p2:
#         holder = chars[p1]
#         chars[p1] = chars[p2]
#         chars[p2] = holder
#         p1 += 1
#         p2 -= 1
#     return chars

# tester = ['n', 'a']

# print(csReverseString(tester))


def csCheckPalindrome(input_str):
    # case sensitive, punctuation counts, etc. All chars.
    # takes in a string
    # check if string is a palindrome
    # return boolean
    #
    # could implement similar to previous - two pointers
    # except keep track of "True"
    # if ever False, return False
    # else if you exhaust the loop, return True
    p1 = 0
    p2 = len(input_str) - 1
    while p1 < p2:
        if input_str[p1] != input_str[p2]:
            return False
        p1 += 1
        p2 -= 1
    return True


# test1 = 'ahsatanseesnatasha'
# test2 = 'gohangasalamiimalasagnahog'
test3 = 'mayamoodybabydoomayam'

# print(csCheckPalindrome(test1))
# print(csCheckPalindrome(test2))
print(csCheckPalindrome(test3))

# def removeAdjacent(s):
#     # takes in a string
#     # only lowercase english letters
#     # 10^6 characters max
#     # if there are adjacent identical characters, remove all but one
#     # return the string
#     #
#     # build a new string
#     new_s = ''
#     if s:
#         new_s = s[0]
#         for i in range(len(s) - 1):
#             if s[i+1] != s[i]:
#                 new_s += s[i+1]
#     return new_s

# test1 = 'aaa'
# test2 = 'abbbcd'
# test3 = ''

# print(removeAdjacent(test1))
# print(removeAdjacent(test2))
# print(removeAdjacent(test3))