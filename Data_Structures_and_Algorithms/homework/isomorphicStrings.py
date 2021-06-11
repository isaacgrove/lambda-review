def csIsomorphicStrings(a, b):
    # takes in two strings a, b
    # return boolean: isomorphic
    # isomorphic -- preserving order of characters, you can
    # do a 1 for 1 replacement of characters to get the new string
    # odd --> egg
    # hi --> to
    # amandita --> anathema
    # aaaaa --> aaaaa

    if not a or not b:
        if not a and not b:
            return True
        return False
    
    if len(a) != len(b):
        return False
        
    # store a chars as keys and b chars as values
    pairings = {}
    for i in range(len(a)):
        if a[i] in pairings:
            if b[i] != pairings[a[i]]:
                return False
        else: #there is no pairing for this character in a yet. Create one.
            pairings[a[i]] = b[i]
    return True

print(csIsomorphicStrings('abcde', 'aaaaa'))