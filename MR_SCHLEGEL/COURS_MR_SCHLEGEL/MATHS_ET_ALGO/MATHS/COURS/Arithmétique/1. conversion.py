def binToDecimal(n):
    puis2 = 1
    somme = 0
    while n > 0:
        unite = n % 10
        somme = somme + unite * puis2
        n = n // 10
        puis2 = puis2 * 2

    return somme


nBin = 101011
nDec = binToDecimal(nBin)
print(nBin, ' -> ', nDec)
