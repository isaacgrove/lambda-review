"""
You are implementing your own programming language 
and you've decided to add support for merging strings. 

A typical merge function would take two strings s1 and s2, 
and return the lexicographically smallest result that can 
be obtained by placing the symbols of s2 between the symbols 
of s1 in such a way that maintains the relative order of the
characters in each string. 

For example, if s1 = "super" and s2 = "tower", the result should
be merge(s1, s2) = "stouperwer".

You'd like to make your language more unique, so for your
merge function, instead of comparing the characters in the 
usual lexicographical order, you'll compare them based on 
how many times they occur in their respective strings (fewer 
occurrences means the character is considered smaller). 

If the number of occurrences are equal, then the characters 
should be compared in the usual way. If both number of occurences 
and characters are equal, you should take the characters from 
the first string to the result.

Given two strings s1 and s2, return the result of the special merge function you are implementing.
"""

def merge_two_strings(s1, s2):
    # figure out the counts of letters in both s1 and s2,
    # using two separate hash tables 
    counts = {} 

    # sorting callback
    sort_by_counts = lambda kv: (kv[1], kv[0])

    for char in s1:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    # sort the key-value pairs of both strings into lists of tuples 
    # where the first tuple element is the letter, the second tuple 
    # element is the count 
    # we'll want this ordered in ascending order based on the counts
    s1 = sorted(counts.items(), key=sort_by_counts)

    # reset counts dict to minimize space usage 
    counts = {}

    for char in s2:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1 

    s2 = sorted(counts.items(), key=sort_by_counts)

    # once we have our two lists of tuples, merge them together using 
    # two pointer merging strategy 
    # start pointers at the beginning of both lists
    # take the character whose count is less than the others 
    # if the counts are the same, take the character that is lexicographically
    # smaller than the other 
    return merge_by_counts(s1, s2)

def merge_by_counts(s1, s2):
    # initialize pointers to start at the beginning of both s1 and s2
    p1, p2 = 0, 0
    output = []

    # so long as both pointers are in bounds of their respective lists 
    while p1 < len(s1) and p2 < len(s2):
        char1, char2 = s1[p1][0], s2[p2][0]
        count1, count2 = s1[p1][1], s2[p2][1]

        # check the counts of the current tuples 
        if count1 == count2:
            # if they're equal, take the lexicographically smaller char
            if char1 < char2:
                output.append(char1 * count1)
                p1 += 1
            else:
                output.append(char2 * count2)
                p2 += 1
        # otherwise, counts are not equal, take the char with the smaller count
        elif count1 < count2:
            output.append(char1 * count1)
            p1 += 1
        else:
            output.append(char2 * count2)
            p2 += 1

    # at this point, we're done iterating through one of the two lists 
    # add the remaining chars from the other list 
    while p1 < len(s1):
        output.append(s1[p1][0] * s1[p1][1])
        p1 += 1

    while p2 < len(s2):
        output.append(s2[p2][0] * s2[p2][1])
        p2 += 1

    return "".join(output)

print(merge_two_strings("lambda", "school"))
