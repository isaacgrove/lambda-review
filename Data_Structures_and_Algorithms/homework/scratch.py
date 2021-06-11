#
l1 = ['a', 'b']
l2 = [1, 2]

print({i: j for i, j in zip(l1,l2)})
print(dict(zip(l1,l2)))