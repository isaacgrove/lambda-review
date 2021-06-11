"""
Given a string, implement a function that returns the string with all lowercase
characters.

Example 1:

Input: "LambdaSchool"
Output: "lambdaschool"

Example 2:

Input: "austen"
Output: "austen"

Example 3:

Input: "LLAMA"
Output: "llama"

*Note: You must implement the function without using the built-in method on
string objects in Python. Think about how character encoding works and explore
if there is a mathematical approach that you can take.*
"""
def to_lower_case(string):
    # Your code here
    pass



def csBinaryToASCII(binary):
    # takes in a binary string (ASCII-encoded)
    # return the decoded text
    # return empty string if empty input
    #
    # chunk the string into 8's
    # for each 8, convert to decimal, then letter, then append to string
    my_str = ''
    for i in range(0,len(binary),8):
        b = int(binary[i:i + 8], base=2)
        print(b)
        letter = chr(b)
        my_str += str(letter)
        
    return my_str

tester = "011011000110000101101101011000100110010001100001"

print(csBinaryToASCII(tester))
