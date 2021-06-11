# essentially, a 90 degree rotation is a reverse + a transpose

def rotateImage(a):
    a.reverse()
    for i in range(len(a)):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

print(rotateImage(x))

# x, reversed
j = [[3,2,1],
     [6,5,4],
     [9,8,7]]

# j, transposed
y = [[7,4,1],
     [8,5,2],
     [9,6,3]]