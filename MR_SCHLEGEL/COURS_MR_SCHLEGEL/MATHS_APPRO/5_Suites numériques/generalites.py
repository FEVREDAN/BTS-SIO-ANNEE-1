def donneExpl(n):
    return 3 * n + 5

def donneIter(n):
    t = 3
    while n > 0:
        t = 3 * t + 4
        n = n - 1
    return t

def donneRec(n):
    if n == 0:
        return 3
    else:
        return 3 * donneRec(n-1) + 4

print(donneExpl(5))
print(donneIter(0))
print(donneRec(0))