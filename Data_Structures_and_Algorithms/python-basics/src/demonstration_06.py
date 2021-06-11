"""
Challenge #6:

Create a function that takes a string, checks if it has the same number of "x"s
and "o"s and returns either True or False.

- Return a boolean value (True or False).
- The string can contain any character.
- When no x and no o are in the string, return True.

Examples:
- XO("ooxx") ➞ True
- XO("xooxx") ➞ False
- XO("ooxXm") ➞ True (Case insensitive)
- XO("zpzpzpp") ➞ True (Returns True if no x and o)
- XO("zzoo") ➞ False
"""
def XO(txt):
    # take in a string - txt
    # check if #x's == #o's, return boolean
    # #strings may contain any character
    # return True by default
    x = 0
    o = 0
    for char in txt:
        if char == 'x':
            x += 1
        if char == 'o':
            o += 1
    if x != o:
        return False
    return True

testers = ['ooxx', 'oooxxx', 'hi', 'oxx', 'xxx', 'oo']
# should be TTTFFF

for _ in testers:
    print(XO(_))
