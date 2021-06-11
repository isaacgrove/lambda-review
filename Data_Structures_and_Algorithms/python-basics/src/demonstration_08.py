"""
Challenge #8:

Create a function that returns the number of arguments it was called with.

Examples:
- num_args() ➞ 0
- num_args("foo") ➞ 1
- num_args("foo", "bar") ➞ 2
- num_args(True, False) ➞ 2
- num_args({}) ➞ 1
"""
def num_args(*args):
    return len(args)

#print(locals().keys())

print(num_args(True, 'foo', 'bar', 'baz'))

# num_args()
# num_args("foo")
# num_args("foo", "bar")
# num_args(True, False)
# num_args({})