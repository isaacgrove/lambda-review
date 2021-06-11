"""
Challenge #4:

Create a function that takes length and width and finds the perimeter of a
rectangle.

Examples:
- find_perimeter(6, 7) ➞ 26
- find_perimeter(20, 10) ➞ 60
- find_perimeter(2, 9) ➞ 22
"""
def find_perimeter(length, width):
    # takes in length and width, integers
    # returns perimeter
    # perimeter = 2*length + 2*width
    if type(length) == int and type(width) == int:
        return 2*length + 2*width
    else:
        return TypeError(f'Either length: {length} or width: {width} is not an integer.')

#print(type(3) == float)
print(find_perimeter(2,8))

