def f(n, level=0):
    if n > 1:
        f(n-1, level+1)
        for j in range(n):
            print(' '*(n-j+level)+'*'*(2*j+1))
f(6)