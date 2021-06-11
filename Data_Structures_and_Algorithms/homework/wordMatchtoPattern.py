def csWordPattern(pattern, a):
    # make sure lengths of pattern and a.split()
    # 'abba' --> 'apple orange orange apple'
    # Fail: 'abba' --> 'lambda lambda lambda lambda'

    if not pattern or not a:
        if not pattern and not a:
            return True
        return False
    a = a.split()
    
    if len(pattern) != len(a):
        return False
        
    # store a chars as keys and b chars as values
    pairings = {}
    for i in range(len(pattern)):
        if pattern[i] in pairings:
            if a[i] != pairings[pattern[i]]:
                return False
        else: #there is no pairing for this character in a yet.
        # but a[i] might already exist in pairings.values(), 
            if a[i] in pairings.values():
                return False
            pairings[pattern[i]] = a[i]
    return True