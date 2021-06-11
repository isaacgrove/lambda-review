def csMaxNumberOfLambdas(text):
    # takes in a string called text
    # return a count of possible lambdas w/o replacement
    #
    # create a dict (or 5 vars) and return the min,
    # floor dividing by 2 for the a's
    abacus = {'l': 0, 'a': 0, 'm': 0, 'b': 0, 'd': 0}
    for i in range(len(text)):
        if text[i] in abacus:
            abacus[text[i]] += 1
    abacus['a'] = abacus['a'] // 2
    return min(abacus.values())