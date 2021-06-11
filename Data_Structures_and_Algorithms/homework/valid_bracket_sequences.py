# Determine if a string sequence of {}[]() is valid
# '[{]}' is invalid

def validBracketSequence(sequence):
    # determine if the string is a valid sequence of brackets
    # empty is valid
    # 
    stack = []
    for char in sequence:
        if char in {'(', '[', '{'}:
            stack.append(char)
        # what happens if we encounter an empty stack?
        elif not stack:
            return False
        else:
            # try to pop
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True


# # This was failed attempt 1 - I naively went at it
# # like another parenthesis-counting problem.
# # It fails on '[{]}' type seqs
#
# def validBracketSequence(sequence):
#     # determine if the string is a valid sequence of brackets
#     # empty is valid
#     # 
#     squiggle_stack = 0
#     square_stack = 0
#     curve_stack = 0
#     for char in sequence:
#         if squiggle_stack < 0 or square_stack < 0 or curve_stack < 0:
#             return False
#         if char == '{':
#             squiggle_stack += 1
#         if char == '[':
#             square_stack += 1
#         if char == '(':
#             curve_stack += 1
#         if char == '}':
#             squiggle_stack -= 1
#         if char == ']':
#             square_stack -= 1
#         if char == ')':
#             curve_stack -= 1
#     if squiggle_stack != 0 or square_stack != 0 or curve_stack != 0:
#         return False
#     return True
        

