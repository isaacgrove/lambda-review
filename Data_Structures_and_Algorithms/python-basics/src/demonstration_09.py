"""
Challenge #9:

Write a function that creates a dictionary with each (key, value) pair being
the (lower case, upper case) versions of a letter, respectively.

Examples:
- mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }
- mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }
- mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }

Notes:
- All of the letters in the input list will always be lowercase.
"""
def mapping(letters):
    # take in a list of lowercase letters
    # return a dictionary where the keys are lowercase, and the values are uppercase
    my_dict = {}
    for letter in letters:
        my_dict[letter.lower()] = letter.upper()
    return my_dict
        

tester0 = ["p", "s"]
tester1 = ["a", "b", "c"]
tester2 = ["a", "v", "y", "z"]

print(mapping(tester0))
print(mapping(tester1))
print(mapping(tester2))