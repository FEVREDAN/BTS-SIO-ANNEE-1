def diviseur(n):
    for i in range(1, round(n**(1/2))+1):
        if n % i == 0 :
            print(i)
            print(n/i)

def premier(n):
    for i in range(2, round(n**(1/2))+1):
        if n % i == 0 :
            return False
    
    return True

print(premier(48))

