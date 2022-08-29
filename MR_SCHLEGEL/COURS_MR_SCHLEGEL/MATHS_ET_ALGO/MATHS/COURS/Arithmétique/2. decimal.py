def affichage_dec(n, dec):
    s = ""
    while (n > 0):
        unite = n % 10
        s = str(unite) + s
        n = n // 10
        dec = dec - 1
        if dec == 0:
            s = ',' + s

    print(s)

n = 1654103
dec = 3

affichage_dec(n, dec)