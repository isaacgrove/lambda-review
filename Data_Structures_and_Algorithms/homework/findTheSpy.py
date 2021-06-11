# n people in the city state
# trust is a list of pairs [trustor, trustee] i.e. graph edges
# to be the spy, you must trust no one, have everyone trust you, and be the only spy in town

# I kept this because I think it's hilarious. There's no way this is how you're supposed to do it.

def uncover_spy(n, trust):
    dic = {}
    trusts = set()
    finalists = []
    for i in range(len(trust)):
        trusts.add(trust[i][0])
        if trust[i][1] in dic:
            dic[trust[i][1]] += 1
        else:
            dic[trust[i][1]] = 1
    for candidate in dic:
        if dic.get(candidate) == n - 1:
            if candidate not in trusts:
                finalists.append(candidate)
    if len(finalists) == 1:
        return finalists[0]
    return -1