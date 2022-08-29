def binToDec(n):
    somme = 0
    rang = 0
    while n > 0:
        unite = n % 10
        somme = somme + (unite * (2 ** rang))
        n = n // 10
        rang = rang + 1
    
    return somme


def decToBin(n):
    rang = 0
    somme = 0
    while n > 0:
        reste = n % 2
        somme = somme  + (reste * (10 ** rang))
        n = n // 2
        rang = rang + 1

    return somme

    


n = 10010011101
print(binToDec(n))
print(decToBin(1181))
