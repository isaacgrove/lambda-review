# blanagrams are when you replace exactly one letter
# takes in two lowercase words

# I think you could do this by first controlling for equal length,
# then after the first loop just check if len(lst2) == 1. It has to
# be, and the only cases that blow this are when the words
# are unequal length, which are all non-blanagrams anyway.
#
# Philosophical... It's much easier to not be a blanagram
# than it is to be a blanagram.

def checkBlanagrams(word1, word2):
    lst1 = list(word1)
    lst2 = list(word2)
    lst2_copy = lst2.copy()
    for char in lst1:
        if char in lst2:
            lst2.remove(char)
    for char in lst2_copy:
        if char in lst1:
            lst1.remove(char)
    if len(lst1) == 1 and len(lst2) == 1:
        return True
    return False



test1 = 'tangram'
test2 = 'pangram'
print(checkBlanagrams(test1, test2))