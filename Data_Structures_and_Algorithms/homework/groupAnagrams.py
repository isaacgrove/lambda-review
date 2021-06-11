def sortUtil(e):
    return len(e)

def csGroupAnagrams(strs):
    # array of strings strs
    # put groups of anagrams in sublists, sort by descending group size
    vault = {}
    # For each word, we put its letters into a set and see if it exists
    # in our dictionary. If it does, we add the string to that list
    for i in range(len(strs)):
        bank = set()
        for letter in strs[i]:
            bank.add(letter)
        bank = frozenset(bank)
        if bank in vault:
            vault[bank].append(strs[i])
        else: # this set isn't in the dict yet. Add it and initialize list
            vault[bank] = [strs[i]]
    final = []
    for k, v in vault.items():
        final.append(v)
    final.sort(key=sortUtil, reverse=True)
    return final
    
    # What about different lengthed words with the same set of letters?
    # EDIT: Didn't matter
    #
    # Upon trying to add it to the set, check lengths?
    # Each entry could have its own dictionary w keys = length, values = sublists
    # dict = {{a, b, c}: {3: ['abc', 'bac'], 5: ['abbcd, bddda']}}
    #
    #assume different lengths is ok for now.