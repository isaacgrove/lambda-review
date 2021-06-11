def fibonacciSimpleSum2(n):
    lst = []
    a = 0
    b = 1
    c = 1
    while a < 2*n:
        lst.append(a)
        a = b
        b = c
        c = a + b
    lst.reverse()
    for i in lst:
        if i * 2 == n:
            return True
        for j in lst:
            if i + j == n:
                return True
    return False
    

print(fibonacciSimpleSum2(999))