"""
Challenge #3:

Create a function that takes a string and returns it as an integer.

Examples:
- string_int("6") ➞ 6
- string_int("1000") ➞ 1000
- string_int("12") ➞ 12
"""
def string_int(txt):
   if txt.isnumeric():
       return int(txt)
   else:
       return(f'"{txt}" is not a valid string. Please input integers only.')


b = '300!'

print(string_int(b))