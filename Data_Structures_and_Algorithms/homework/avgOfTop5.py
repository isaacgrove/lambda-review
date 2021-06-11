def sortByID(e):
    '''Utility function to sort by student ID'''
    return e[0]

def csAverageOfTopFive(scores):
    # takes in list of (presumably test) scores
    # return each student's top 5 scores in a list, where the first
    # element is the lowest student ID #, ascending.
    # *Calculate the average using integer division
    #
    # In the input, each entry scores[i] has an id # scores[i][0]
    # and a score scores[i][1]
    #
    # set up a dict where keys are id numbers and values are lists of scores.
    gradebook = {}
    final = []
    for i in range(len(scores)):
        # if the student isn't in the gradebook yet, put them in
        if scores[i][0] not in gradebook:
            gradebook[scores[i][0]] = [scores[i][1]]
        # else they're in the gradebook already, append a score
        else:
            gradebook[scores[i][0]].append(scores[i][1])
    # gradebook keys are student ID's. values are list of scores
    for student, grades in gradebook.items():
        # just in case there's less than 5 scores
        result = []
        top_5 = sorted(grades)[-5:]
        avg = sum(top_5) // len(top_5)
        result.append(student)
        result.append(avg)
        final.append(result)
    final.sort(key=sortByID)
    return final