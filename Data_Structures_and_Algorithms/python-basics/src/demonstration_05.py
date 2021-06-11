"""
Challenge #5:

Create a function that returns a list of strings sorted by length in ascending
order.

Examples:
- sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
- sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
- sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
- sort_by_length([]) ➞ []
"""
def sort_by_length(lst):
    # take in a list of strings
    # return that list, sorted by length (ascending order)
    return sorted(lst, key=lambda word: len(word))
    

tester = ["a", "ccc", "dddd", "bb"]
tester2 = ["pie", "apple", 'blasphemy', "shortcake", 'onomatopoeia', '1']
tester3 = ["may", "april", "september", "august"]

print(sort_by_length(tester))
print(sort_by_length(tester2))
print(sort_by_length(tester3))