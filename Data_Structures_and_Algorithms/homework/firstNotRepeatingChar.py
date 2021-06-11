def first_not_repeating_character(s):
    # takes in a lowercase english string
    # return the first character that doesn't repeat
    # return _ if all characters repeat
    #
    repeated = set()
    fresh = []
    
    for char in s:
        # if it's in repeated, continue
        # if it's in fresh, remove from fresh and put in repeated
        # else append to fresh
        # return fresh[0]
        if char in repeated:
            continue
        if char in fresh:
            fresh.remove(char)
            repeated.add(char)
        else:
            fresh.append(char)
        print(fresh)
    return fresh[0]
    
print(first_not_repeating_character('aaabbac'))