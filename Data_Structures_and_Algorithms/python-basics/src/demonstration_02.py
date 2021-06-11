"""
Challenge #2:

Write a function that takes an integer `minutes` and converts it to seconds.

Examples:
- convert(5) ➞ 300
- convert(3) ➞ 180
- convert(2) ➞ 120
"""
def convert(minutes):
    # 60 seconds in a minute
    # so take minutes and * by 60 to get seconds
    # return the result
    a = minutes * 60
    return str(a + 30) + 'hi'

print(convert(60))
